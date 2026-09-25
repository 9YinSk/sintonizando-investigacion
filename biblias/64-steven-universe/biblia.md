---
tags: [biblia, serie, animacion, laminas]
serie: "Steven Universe (Cartoon Network, 2013-2020)"
canal: "sin canal: se propone #🎵・canto (A, recomendado), #🪪・presentaciones (B) y #📂・proyectos (C)"
fecha: 2026-09-25
---

# Biblia · Steven Universe — propuesta para #🎵・canto

> [!important] Cómo se hizo (léelo primero)
> - **Es una serie animada de EE. UU., no un anime.** No hay manga, ni globos, ni onomatopeyas en pantalla, ni *ending* cantado distinto por capítulo. Eso cambia los puntos 5, 6 y 19 (se explica en cada uno).
> - Franquicia: 5 temporadas (160 capítulos de unos 11 minutos), *Steven Universe: The Movie* (2019) y el epílogo *Steven Universe Future* (2019-2020). Más cómics de BOOM! Studios y 3 videojuegos propios.
> - La hicieron **4 investigadores** (imagen, vídeo, voz, texto) y la escribió un redactor con sus partes (`partes/*.md` y `partes/*.json`). **No se añadió nada que no esté en las partes o en las 3 hojas de contacto** (que el redactor miró). Lo que falta va con ⚠️ y se explica.
> - **Los vídeos se miraron de verdad**, pero en **Internet Archive y Dailymotion**: YouTube pide iniciar sesión desde el servidor. Se vieron enteros el capítulo piloto «Gem Glow», la escena de «Stronger Than You», el animatic oficial de «The Answer», el tráiler de la película y dos recopilaciones de fans; y dos clips en Dailymotion («El Tío», doblado, y «It's Over, Isn't It»).
> - **Las voces latinas se oyeron**: 4 muestras de Doblaje Wiki (Steven, Garnet, Amatista, Perla) pasadas por `voz.py` (frase textual, tono en Hz, velocidad).
> - **Los colores se midieron** con Pillow y `estilo.py` en fichas de producción y en fotogramas del piloto.

**Leyenda:** ✅ confirmado en dos fuentes o visto con los propios ojos · ⚠️ una sola fuente, dudoso o a medias.

**Hojas de contacto** (en `hojas/`; los números no se repiten entre hojas):
- `personajes_01_pearl_amatista.jpg` → n.º **1-48** (Perla, Amatista, gemas, puertas del Templo y escenas).
- `fondos_01_lugares.jpg` → n.º **97-144** (fotogramas 1920×1080 de capítulos, de la serie a *Future*).
- `objetos_01_steven_garnet.jpg` → n.º **145-167** (fotogramas de la película e iconos de gemas y fusiones).

En el texto se citan como **hoja n.º X**.

**Vídeos citados** (el código corto es el que se usa en el texto):
- `GG` «Gem Glow», T1-E1, capítulo piloto completo, 11:30 · https://archive.org/details/steven-universe-s-01-e-01-gem-glow
- `STY` «Stronger Than You», clímax de «Jail Break» (T1-E52), 4:11 · https://archive.org/details/Steven_Universe_Garnets_Fusion_Song_Stronger_Than_You_
- `ANS` «The Answer», animatic oficial de Cartoon Network, 11:26 · https://archive.org/details/steven-universe-the-answer-animatic
- `TRL` tráiler Toonami de *Steven Universe: The Movie*, 2:00 · https://archive.org/details/steven-universe-the-movie-toonami-trailer
- `1S` «1 Second From Every Steven Universe Episode» (fan), 2:55 · https://archive.org/details/1-second-from-every-steven-universe-episode
- `TT` «Steven Universe Tik Toks» (recopilación de fans), 4:59 · https://archive.org/details/steven-universe-tik-toks
- `IOI` clip oficial «It's Over, Isn't It? | Steven Universe | Cartoon Network» · https://www.dailymotion.com/video/x4wic92
- `TIO` «Steven Universe - El Tío (Latino) (Clip 3)», doblado, 2:49 · https://www.dailymotion.com/video/x5ejzz4

## Índice

- 0 · Steven Universe no tiene canal: dónde encaja mejor
- 1 · Lo esencial
- 2 · Las 3 hojas de contacto, número a número
- Punto 1 · Arte oficial
- Punto 2 · Fotogramas de escenas icónicas
- Punto 3 · Fan art y 3D con licencia
- Punto 4 · Sitios: luz, paleta y texturas reales
- Punto 5 · Tipografía: una letra por uso
- Punto 6 · Cómo hablan en pantalla (el «cuadro» de Steven Universe)
- Punto 7 · Personajes y popularidad
- Punto 8 · Doblaje latino y frases textuales
- Punto 9 · Música y sonido
- Punto 10 · Vídeos y tendencias
- Punto 11 · Videojuegos
- Punto 12 · Lo que ama el fandom y qué NO hacer
- Punto 13 · Personajes a fondo
- Punto 14 · Poses analizadas
- Punto 15 · Vestuario y hex medidos
- Punto 16 · Ciudades, paisajes y fondos de pantalla
- Punto 17 · Guía para generar con IA (imagen y texto)
- Punto 18 · Estilo y técnica: cómo replicarlo
- Punto 19 · Texturas 2D
- Punto 20 · Gustos y detalles
- Punto 21 · Por qué la aman
- Punto 22 · Fan dubs y comunidad hispana
- Punto 23 · Colaboraciones y cruces
- Punto 24 · Obras parecidas
- Punto 25 · El mundo, la historia y sus símbolos
- 3 conceptos de lámina
- Lo que corregí de las partes y lo que no se pudo verificar
- Cumplimiento del encargo
- Bitácora de búsqueda

## 0 · Steven Universe no tiene canal: dónde encaja mejor

El encargo dice por qué está: **música y personajes queridos**. La biblia es general (sirve para láminas, vídeos, textos, doblaje…). El canal es sólo una propuesta.

| Canal (de `servidor/inventario.md`) | Qué dice el canal | Por qué encaja | Nota |
|---|---|---|---|
| **#🎵・canto** ⭐ | «Hablar de cantar. Tus covers van a demos-canto, un hilo por cover.» | Es una serie **cantada**: más de 38 canciones de Steven; el álbum *Soundtrack: Volume 1* llegó al n.º 1 de iTunes y a la *Billboard 200* (punto 9). | La biblia 29 propone *Sing* para #canto. No bloquea nada. |
| **#🪪・presentaciones** | «Tu ficha del servidor… Abre TU hilo con la plantilla fijada.» | Existe un libro oficial de **fichas**: *Guide to the Crystal Gems* (hoja n.º 2). Su ficha es una plantilla hecha. | *Encanto* (58) también lo propone. |
| **#📂・proyectos** | «Un hilo por proyecto: equipo, avance, entregas.» | La **fusión** es la idea central de la serie: dos se juntan y hacen algo más grande. Lo dice Garnet en el doblaje latino (punto 8). | *Arcane* (17) y *Vinland Saga* (78) también lo piden. |
| 🎶・Karaoke | sala de voz | Hay un disco oficial de karaoke (MusicBrainz, 12-abr-2019). | *Sing* (29). Queda como reserva. |
| #🧰・recursos | «Lo que le sirve a los demás…» | La **Mochila Hamburguesa** es el inventario del juego *Unleash the Light* (punto 11). | Idea para una lámina 2 o un sticker. |

Los choques de canal quedan sólo como nota (decisión del dueño, 25-sep).

## 1 · Lo esencial

- **Quién es el más querido:** no hay encuesta oficial (se buscó en inglés y español). En dibujos de fans (Danbooru) gana **Perla** (414), seguida de **Lapis Lázuli** (394) y **Peridot** (355); Steven 264, Amatista 209, Garnet 175. En el ranking editorial de IGN (2019) gana **Garnet** (⚠️ una fuente). Dos secundarias (Lapis y Peridot) superan a Amatista y Garnet: justo lo que temía el dueño.
- **El «cuadro de diálogo» propio:** la serie **no usa globos**. Lo suyo es la **cartela de título** de cada capítulo (letra libre **Crewniverse**, con tildes, ñ, ¿ y ¡ comprobadas), y dentro del mundo, la **pantalla holográfica del Comunicador de las Diamantes** y los carteles en **Gem Glyph**.
- **La voz latina:** Venezuela, Etcétera Group. Steven = Leisha Medina, Garnet = Rocío Mallo, Amatista = Stefani Villarroel, Perla = María José Estévez (dos fuentes cada una).
- **El color de la serie:** personajes en color **plano** con línea fina; fondos **pintados a pincel**, pastel y con grano. Atardecer medido en el piloto: `#17251E` `#F7F6CE` `#ECD2A3` `#CD8891`.
- **Qué NO hacer:** adelgazar a Amatista, Garnet, Rose o Steven. El fandom lo vigila mucho (punto 12).

## 2 · Las 3 hojas de contacto, número a número

Las generó el investigador de imagen con `investigar_serie.py` sobre la wiki de Fandom. El redactor las miró enteras. Tamaño original en la esquina de cada celda.

**`personajes_01_pearl_amatista.jpg` (n.º 1-48)** — la mejor para ropa, armas y grupo:
- **n.º 2** · página de Amatista del libro oficial *Guide to the Crystal Gems* (3028×3960). Se lee: «Species: Gem · Gem Type: Quartz · Alignment: Crystal Gem · Hair Color: Pale lavender · Clothing: Leggings with stars on the knees and an oversize tank top · Gem Location: Chest · Weapon: Whip · Fun Fact: … wrestling alter ego the Purple Puma · Favorite Quote: "Who needs to go see movies when you've got MAGIC?"». Título en cinta lila con estrella morada. **Base del concepto B.**
- **n.º 3 y 31** · el látigo de Amatista (normal y con púas).
- **n.º 5-7** · Amatista de cuerpo entero, puño cerrado, sonrisa y látigo (archivos «Jfek»; ⚠️ no se sabe si es arte de producción o de fan).
- **n.º 9 y 10** · Perla de cuerpo entero con su lanza (ficha actual y de debut, 2400×3933). **n.º 15** · Perla con la mano abierta, como explicando (modelo de distancia).
- **n.º 12** · Lapis Lázuli en su gota de agua. **n.º 29** · Peridot en su triángulo verde.
- **n.º 13 y 14** · la **Puerta del Templo** con la estrella de 5 gemas y el camino de luz hacia el cuarto de Amatista (ondulado, lila) y de Perla (recto). Arriba, un dintel con dibujo geométrico. **Base del concepto C.**
- **n.º 17-28** · la gema de Amatista en 12 versiones (n.º 21 rajada; n.º 23 «Purple Puma»). **n.º 34** · la perla de Perla. **n.º 33** · lanza mejorada.
- **n.º 30** · plantilla de fusión de Garnet (Rubí + Zafiro).
- **n.º 35-48** · escenas 1920×1090. Las mejores: **n.º 38** (fusión de cuatro brazos haciendo el signo de la paz, «Back to the Moon»); **n.º 41** (Perla bailando de noche); **n.º 42** (Greg, Amatista y Steven apretados en un sofá, «Maximum Capacity»); **n.º 46** (Steven y Amatista sentados en el techo de un **vagón de tren rojo** al atardecer, «On the Run»: **base del concepto A**); **n.º 47** (Garnet, Amatista y Steven, «Reformed»); **n.º 48** (Amatista entre muchas Amatistas, «That Will Be All»).

**`fondos_01_lugares.jpg` (n.º 97-144)** — la mejor para sitios, luz y emociones:
- **n.º 97** · Steven con el escudo rosa, «Gem Glow». **n.º 98** · fusión gigante con Steven, «Giant Woman».
- **n.º 102, 112, 135** · Homeworld: Blue Diamond llorando (n.º 112), Yellow y Blue Diamond en sus tronos (n.º 135).
- **n.º 107** · interior del **Big Donut**: mostrador, vitrinas, Sadie y Steven («Joking Victim»).
- **n.º 109 y 122** · León, el león rosa. **n.º 115 y 116** · Bismuto.
- **n.º 117** · Steven mayor (sudadera azul) y Greg, de noche al aire libre («Mr. Universe»).
- **n.º 120** · Lapis abrazando a Steven con traje, Peridot al lado, cielo verde y amarillo sobre el mar («Reunited»).
- **n.º 123 y 124** · Steven triste al atardecer con Rose («Storm in the Room»).
- **n.º 125** · Connie y Steven con espada y escudo («Sworn to the Sword»).
- **n.º 126-132** · *Future*: Steven mayor con chaqueta rosa; Peridot, Lapis y Bismuto en Little Homeworld; Steven conduciendo (n.º 132).
- **n.º 138** · Connie con el anillo. **n.º 140** · Garnet y Steven con traje («Together Forever»).
- **n.º 142** · Steven rosa y furioso («Volleyball»). **n.º 143** · Amatista señalando al cielo con Steven («What's Your Problem»).

**`objetos_01_steven_garnet.jpg` (n.º 145-167)** — película e iconos:
- **n.º 145** · Greg y Steven tocando guitarra y bajo eléctricos con llamas detrás (película). **Pose de música.**
- **n.º 146-151** · más de la película: Spinel peleando con Steven (n.º 148, 150), Bismuto (n.º 151).
- **n.º 153** · escudo rosa de hexágonos (estado rosa). **n.º 155** · fragmentos de gema.
- **n.º 156-160** · fusiones: Sunstone, rubíes en quíntuple, Obsidiana. **n.º 158-159** · la gema rosa (Rose y Steven, pentágono facetado).
- **n.º 161-167** · iconos circulares de personaje: Larimar, Rhodonita, Azurita, Amatista, Zafiro, Rubí, Steven.

⚠️ La parte de imagen describía `objetos_01` como «modelos de producción de Steven y Garnet con escudo y guanteletes». **No es así:** la hoja no trae esos modelos. Esos archivos existen y están enlazados en el punto 1.

## Punto 1 · Arte oficial

Todo en la wiki de Fandom ([steven-universe.fandom.com](https://steven-universe.fandom.com/)). Las imágenes de `static.wikia.nocookie.net` piden la cabecera `Referer: https://www.fandom.com/`.

**Fichas de producción** (fondo transparente, sin artista externo). Sirven para medir color (punto 15) y para posar:
- Steven en pose de acción con el escudo · 1680×1428 · https://static.wikia.nocookie.net/steven-universe/images/c/c2/Steven_Universe_-_With_Weapon3.png · ✅
- Garnet con los guanteletes en alto · 1750×3050 · https://static.wikia.nocookie.net/steven-universe/images/2/27/Garnet_With_Rings.png · ✅
- Garnet, modelo simplificado para planos lejanos · 1869×4288 · https://static.wikia.nocookie.net/steven-universe/images/9/9b/Garnet_%28Distance_Model%29.png · ✅
- Perla con la lanza, diseño final · 2400×3933 · https://static.wikia.nocookie.net/steven-universe/images/8/8c/Current_Pearl_Request.png · ✅ (hoja n.º 9)
- Perla, diseño del debut · 2400×3933 · https://static.wikia.nocookie.net/steven-universe/images/8/84/Debut_Pearl_Request.png · ✅ (hoja n.º 10). Sirve para ver cómo cambió el pelo y las proporciones.
- Amatista, traje base · 2750×3780 · https://static.wikia.nocookie.net/steven-universe/images/4/4b/Amethyst_CYM_Outfit.png · ✅

**Concept art de 2012** (el *pitch* de Rebecca Sugar, antes del diseño final). Pequeñas, de época:
- Steven 377×410 · https://static.wikia.nocookie.net/steven-universe/images/1/19/2012ConceptArtSteven.png
- Garnet 428×298 · https://static.wikia.nocookie.net/steven-universe/images/8/8e/2012ConceptArtGarnet.png
- Perla 273×490 · https://static.wikia.nocookie.net/steven-universe/images/7/7f/2012ConceptArtPearl.png
- Amatista 243×374 · https://static.wikia.nocookie.net/steven-universe/images/b/b1/2012ConceptArtAmethyst.png · ✅ (wiki + artbook)

**Libros oficiales:**
- *Steven Universe: Art & Origins* (Chris McDonnell, Abrams, 11-jul-2017, ISBN 9781419724435): concept art, arte de producción, storyboards y comentario del equipo · https://www.abramsbooks.com/product/art-of-steven-universe_9781419724435/ · ✅ (Abrams + ficha en la wiki).
- *Guide to the Crystal Gems* (2015): una ficha a toda página por Gema. Amatista 3028×3960 · https://static.wikia.nocookie.net/steven-universe/images/a/a7/Guide_to_the_Crystal_Gems_-_Amethyst.jpg · Garnet 401×1115 · https://static.wikia.nocookie.net/steven-universe/images/6/6f/Garnet_-_Guide_To_The_Crystal_Gems.png · contraportada 540×720 · https://static.wikia.nocookie.net/steven-universe/images/0/04/Back_of_Guide_to_the_Crystal_Gems.jpg · ✅

**Arte de videojuegos** (poses vivas, arma en alto):
- *Attack the Light* (2015): icono 1024×1024 · https://static.wikia.nocookie.net/steven-universe/images/c/c4/Attack_The_Light.png · fondo de batalla pintado 2992×1336 · https://static.wikia.nocookie.net/steven-universe/images/8/86/Attack-the-Light-Background-1.png · ✅
- *Save the Light* (2017): arte clave con todo el grupo en acción · 1280×854 · https://static.wikia.nocookie.net/steven-universe/images/1/1b/Save_the_Light.png · ✅
- *Unleash the Light* (2019), arte de batalla: Garnet 1216×1808 · https://static.wikia.nocookie.net/steven-universe/images/5/59/Garnet_Unleash_the_Light.png · Perla 1176×2184 · https://static.wikia.nocookie.net/steven-universe/images/1/14/Pearl_Unleash_the_Light.png · Amatista 1113×1477 · https://static.wikia.nocookie.net/steven-universe/images/0/03/Amethyst_Unleash_the_Light.png · ✅

**Cómics oficiales** (BOOM!/KaBOOM! Studios; muchas portadas alternativas, arte nuevo):
- #1 de 2017, portada A · 1032×1566 · https://static.wikia.nocookie.net/steven-universe/images/4/45/Boom_2017_001_A.jpg
- *Camp Pining Play* (2019) · 1800×2700 · https://static.wikia.nocookie.net/steven-universe/images/4/41/Camp_Pining_Play_cover.jpg
- *Harmony* #1 (2024) · 2400×2400 · https://static.wikia.nocookie.net/steven-universe/images/c/ca/Harmony1_Cover.jpg · ✅ (wiki + [BOOM! Studios](https://www.boom-studios.com/archives/category/series/steven-universe/))

**Fondos oficiales de Cartoon Network** (con su marca de agua): 1920×1080 · https://w.wallhaven.cc/full/73/wallhaven-73zzov.jpg · origen `https://www.cartoonnetwork.com/backgrounds/` · ✅. Hay dos más del mismo origen: https://w.wallhaven.cc/full/83/wallhaven-83qlxk.jpg y https://w.wallhaven.cc/full/ey/wallhaven-ey5jo8.jpg (1920×1080).

**Fotogramas 1920×1080 de la wiki**: 48 en `fondos_01` y 14 en `personajes_01` (ver §2).

## Punto 2 · Fotogramas de escenas icónicas

Vistos con `fotogramas.py`. El minuto es del vídeo citado.

**«Gem Glow» (T1-E1, `GG`, visto entero cada 10 s, 1280×714 recortado de un original 1080p):**
- 0:00-0:20 · Steven corre con Perla por un puente hacia un acantilado · ✅
- 1:00-1:50 · interior del **Big Donut** (la tienda de Sadie y Lars) · ✅
- 2:00-2:50 · interior del **Templo de Cristal**: pasillo de cristales triangulares rosas y azules · ✅
- 8:20-8:50 · el Centipeetle (gema corrupta verde) ataca en el acantilado; pelean Garnet, Amatista y Perla · ✅
- 10:40-11:10 · las 4 Gemas y Steven sentados en la playa al atardecer · ✅
- 11:10-11:30 · créditos con música instrumental · ✅

**«Stronger Than You» (`STY`, de «Jail Break», T1-E52, visto cada 3 s):**
- 0:00 · Garnet sentada y tranquila, Steven a su lado · ✅
- 0:54-0:57 · Steven con **ojos de estrella**, boquiabierto · ✅
- 2:42-2:45 · Garnet de pie **chasqueando los dedos**, sonrisa confiada (gesto icónico) · ✅
- 3:00-3:33 · pelea cuerpo a cuerpo contra Jasper en la nave; 3:09-3:15 puñetazo en vuelo · ✅
- 4:09 · Jasper vencida, atrapada en una **burbuja rosa** · ✅

**«The Answer» (`ANS`, animatic oficial, 1920×1080, visto cada 8 s):**
- 8:56-9:12 · Rubí y Zafiro se dan la mano por primera vez · ✅
- 11:04-11:20 · brillan y se funden en una sola silueta: nace Garnet · ✅

**Tráiler de la película (`TRL`, visto entero cada 2 s):** 1:36-1:48 fusión morada de cuatro brazos y León; 1:52-1:54 cartela «STEVEN UNIVERSE THE MOVIE — Monday September 2nd 6:00P» con el logo de Cartoon Network · ✅

**«It's Over, Isn't It» (`IOI`, visto cada 10 s):** 2:00 Perla mira abajo sosteniendo una rosa; 2:10 **una lágrima** baja por su mejilla, ojos muy abiertos · ✅

## Punto 3 · Fan art y 3D con licencia

**Sólo como referencia** (enlace y autor, nunca para pegar).

**Fan art mejor valorado** (Safebooru, con su origen real):
- Perla · 741×1389 · https://safebooru.org/images/5/fb5d3c804058829025176df0b5af6adfa9fc6e84.jpg · autor: https://svacob.tumblr.com/post/730465461156921344
- Perla y Lapis · 1080×1119 · https://safebooru.org/images/2761/ead5cb3ae2bc263cd41f9a766ca5f1048b79bad3.png · autor: https://twitter.com/nano8__8/status/1142802212973772800
- Grupo · 1586×1191 · https://safebooru.org/images/2922/d6f6641dee3e436feec84b999de9d4276b0a0403.jpg · autor: https://twitter.com/sakaki_momo/status/1243851843597291520
- Garnet · 1024×724 · https://safebooru.org/images/2229/c0fe04245141c09769fbfc10b835ff2699299f3e.png · autor: DeviantArt, chinchongcha
- Garnet · 1300×1733 · https://safebooru.org/images/3235/2c77c296cf612e308d1a2e4d9f9be51765571058.jpg · autor: https://twitter.com/dowmansayman/status/1315271890554904576
- Lapis · 1500×2000 · https://safebooru.org/images/2/cbc8d76e3883bf7f9c364fd7fe0a8c94c414eb24.jpg · autor: https://twitter.com/9wj836/status/1848094730489598176
- Peridot · 2048×2048 · https://safebooru.org/images/4269/2ccb4d15c7adbf7d868a8879d6fd5ba67097b836.jpg · autor: https://twitter.com/karin_apple25/status/1682036255322939394
- ⚠️ Steven y Amatista: la API de Safebooru no devolvió nada con sus etiquetas (dos intentos).

**Fan art subido a la wiki** (el recolector lo trajo como «las imágenes más grandes»; el nombre del archivo lleva la firma del artista, así que **no es oficial**):
- Steven en acción, por TheOffColors · 6180×6749 · https://static.wikia.nocookie.net/steven-universe/images/e/e9/StevenUniverse16_By_TheOffColors.png · ⚠️
- Garnet, por Kmes · 1750×3050 · https://static.wikia.nocookie.net/steven-universe/images/1/16/GarnetByKmes.png · ⚠️
- Hoja de modelo de «Monster Steven», por RylerGamerDBS · 3072×3356 · https://static.wikia.nocookie.net/steven-universe/images/5/5b/Monster_Steven_%28Modelsheet%29_by_RylerGamerDBS.png · ⚠️

**Modelos 3D en [Sketchfab](https://sketchfab.com/)** (licencia y crédito exactos; CC BY = se puede usar citando al autor; CC BY-NC = sólo sin fines comerciales):

| Modelo | Autor | Licencia | ♥ | Enlace |
|---|---|---|---|---|
| **Grupo: Garnet, Amatista, Perla, Steven (+ Spinel)** | RazyBerry | CC BY | 46 | https://sketchfab.com/3d-models/5e1f0e20308f4db5bd9a33282c1c07bd |
| **Big Donut** (el local de Beach City) | Kekê | CC BY | 275 | https://sketchfab.com/3d-models/none-b44b20b741ce4dbba2339fec366cc3c9 |
| Garnet (versión VRChat) | Placidone | CC BY | 315 | https://sketchfab.com/3d-models/none-9863948a5d6c45d08a4c207f10230494 |
| Garnet | Offy | CC BY | 91 | https://sketchfab.com/3d-models/none-4c36594e7f054e228f59feae640fd334 |
| Garnet | Miaru3d | CC BY | 61 | https://sketchfab.com/3d-models/none-38ff74df366146aaafa235f1aff30ce0 |
| Perla («perla») | marcoslate1999 | CC BY | 69 | https://sketchfab.com/3d-models/4f64109a55d74b438f3e145373e5270e |
| Perla («PEARL») ⚠️ | dexver | CC BY | 8 | https://sketchfab.com/3d-models/ad6866217a9340e6b744278924364a95 |
| Amatista | ShadowPuchi | CC BY | 13 | https://sketchfab.com/3d-models/none-b83b49f660bd4c239d4c42be570dc79c |
| Rose Quartz | ASideOfChidori | CC BY-NC | 452 | https://sketchfab.com/3d-models/none-4ef4f349782e4105b61f24446b4ff297 |
| «Stronger Than You» (escena) | ASideOfChidori | CC BY-NC | 421 | https://sketchfab.com/3d-models/none-512044f0e8e345939a62ffd8b0c1af11 |
| White Diamond | ASideOfChidori | CC BY-NC | 524 | https://sketchfab.com/3d-models/none-c75fed0294484e32945ed20048cfda3a |

Crédito tipo: «"Big Donut - Steven Universe" by Kekê, CC BY, sketchfab.com».

**Fotos con licencia libre** (Openverse): cosplay de Garnet en Sakura-con 2016 (camknows, CC BY-NC-SA) · https://live.staticflickr.com/1536/25995790691_274aa59caf_b.jpg · Perla (Tekno Omega, CC BY-NC-ND) · https://live.staticflickr.com/8651/28277935443_e53ea413ab_b.jpg · el discurso de los Peabody (CC BY-SA 3.0, 1600×900) · https://upload.wikimedia.org/wikipedia/commons/1/15/Steven_Universe_-_78th_annual_Peabody_Awards_acceptance_speech.jpg · y 16 más en `referencias.json`.

## Punto 4 · Sitios: luz, paleta y texturas reales

Paletas medidas con `estilo.py` sobre fotogramas propios de `GG` (no de arte de fans). Porcentaje = cuánto ocupa cada color.

| Sitio | Fotograma | Paleta medida | Luz |
|---|---|---|---|
| Acantilado y playa, de día | `GG` 0:10 | `#CBFDF5` 32% · `#F9FBF9` 26% · `#ACFCEF` 17% · `#BCDCCB` 15% · `#58AAA8` 7% · `#4C2433` 3% | muy lavada, casi pastel (brillo 93%, saturación 20%) |
| Big Donut, interior | `GG` 1:10 | `#D1B797` 23% · `#A5847E` 19% · `#EFE8C8` 18% · `#F2DB9B` 16% · `#FCFCEC` 14% · `#443B3B` 10% | cálida de tienda, vitrinas |
| Templo de Cristal, pasillo | `GG` 2:10 | `#522F42` 22% · `#AA827C` 19% · `#D3DEDA` 16% · `#726670` 16% · `#F8F6F8` 14% · `#BFAEA5` 13% | tenue, con brillo de cristal |
| Cocina de la Casa Playa | `GG` 3:30 | `#7A5C74` 22% · `#CEA7B0` 21% · `#F4DACF` 19% · `#090306` 17% · `#5B1D37` 13% · `#F7ECFC` 8% | tarde cálida por la ventana |
| Playa al atardecer | `GG` 11:00 | `#17251E` 29% · `#F7F6CE` 23% · `#ECD2A3` 18% · `#445651` 13% · `#CD8891` 11% · `#946463` 6% | cielo cálido, acantilado en silueta |

Y en la **color key oficial de Beach City** (pintura de fondo de producción, 1280×720, medida con Pillow): cielo `#D0E2F3`, mar `#76AEC0`, mar lejano `#ABCDDF`, acantilado `#B6AC96` · https://static.wikia.nocookie.net/steven-universe/images/4/4f/Beach_City_Color_Key.jpg · ✅. Mañana nublada, luz difusa, casi sin sombras duras.

- La **nave gema** de «Stronger Than You» (`STY` 2:48-3:24): interior **verde veneno** con paredes que parecen raíces. Es el color «de amenaza» frente al calor de la Tierra · ✅ visto (sin hex).
- Nombres oficiales en la wiki: [Crystal Temple](https://steven-universe.fandom.com/wiki/Crystal_Temple) y [Beach House](https://steven-universe.fandom.com/wiki/Beach_House) · ✅

**Texturas reales equivalentes (CC0, [ambientCG](https://ambientcg.com/))**:
- Madera del mostrador y del paseo marítimo: **Wood095** · https://ambientcg.com/view?id=Wood095
- Arena: **Ground054** · https://ambientcg.com/view?id=Ground054 y **Ground080** · https://ambientcg.com/view?id=Ground080
- Roca del Templo y acantilados (sólo el relieve; el tono es el hex medido): **Rock064** · https://ambientcg.com/view?id=Rock064

## Punto 5 · Tipografía: una letra por uso

Steven Universe no es manga: **no hay letra de globo, de grito ni de onomatopeya en pantalla**. Hay logo, cartelas de título, créditos, el cómic de BOOM!, la escritura del mundo (Gem Glyph) y los juegos. Las tres letras libres son de MaxiGamer en [DaFont](https://www.dafont.com/), «100% Free».

| Uso | Letra de la serie | Letra libre más parecida | ¿Tildes, ñ, ¿ y ¡? |
|---|---|---|---|
| **Logo / título** | rotulación propia, redondeada, con brillo de gema ([MadeGoodDesigns](https://madegooddesigns.com/steven-universe-font/), ⚠️) | **Crystal Universe** · https://www.dafont.com/crystal-universe.font | ⚠️ sin comprobar: la descarga dio 0 bytes dos veces |
| **Cartela de título** (el «globo» de la serie) | la de las cartelas de cada capítulo | **Crewniverse** · https://www.dafont.com/crewniverse.font | ✅ **sí**: á é í ó ú, Á É Í Ó Ú, ñ, Ñ, ¿, ¡, ü (comprobado con fontTools) |
| **Créditos / subtítulos** | la de los créditos finales | **Creditverse** · https://www.dafont.com/creditverse.font | ⚠️ **no**: 0 de 14 caracteres (fontTools). No sirve para español sin arreglos |
| **Globo normal, grito, pensamiento, onomatopeya** | sólo existen en el cómic de BOOM! | ⚠️ no encontré el rotulista ni la letra | — |
| **Cartel del mundo** | **Gem Glyph** (escritura logográfica; punto 25) | en *Unleash the Light* es una letra real letra a letra | no aplica (no son letras latinas) |
| **Interfaz de juego** | ⚠️ sin identificar (Game UI Database bloqueado) | — | — |

**Para la lámina: usa Crewniverse** en todo el texto en español. Es la única comprobada con tildes y ñ, y es la letra de las cartelas reales.

Cómic: dos series oficiales. Miniserie 2014-2015 (guion Jeremy Sorese, dibujo Coleman Engle) y serie regular desde 2017 (guion Melanie Gillman, dibujo Katy Farina, color Whitney Cogar) · [Fandom](https://steven-universe.fandom.com/wiki/Steven_Universe_(comic_series)) + [ComicsAlliance](https://comicsalliance.com/boom-steven-universe-ongoing-melanie-gilman-katy-farina/) · ✅. Una reseña dice que los globos de la miniserie eran «caprichosos y difíciles de leer» (⚠️ una sola fuente, no se pudo abrir el original).

## Punto 6 · Cómo hablan en pantalla (el «cuadro» de Steven Universe)

**La serie casi nunca usa globos.** Se habla con voz y gesto. Por eso la lámina **no debe llevar una burbuja blanca de cómic**. Lo que sí es de la serie:

1. **La cartela de título de cada capítulo** con la letra Crewniverse (punto 5). La de Garnet lleva una **estrella doble**, pista de que es una fusión ([Garnet · Trivia](https://steven-universe.fandom.com/wiki/Garnet#Trivia), ✅). ⚠️ El diseño exacto de las cartelas (fondo, marco, colores) no está descrito en las partes: mirar una antes de copiarla.
2. **El Comunicador de las Diamantes**: objeto **octaédrico** con una cara de color por Diamante (blanca, amarilla, azul, rosa). Se gira y **proyecta una pantalla holográfica** para hablar en directo. Es la «videollamada» de la serie · [Diamond Communicator](https://steven-universe.fandom.com/wiki/Diamond_Communicator) · imagen 1000×1034 · https://static.wikia.nocookie.net/steven-universe/images/d/d5/Diamond_Communicator.png · ✅ la función, ⚠️ la forma exacta de la pantalla.
3. **Carteles en Gem Glyph** en Little Homeworld, las columnas del Sky Arena y la Fragua. Fotograma 1920×1080 con carteles de fondo · https://static.wikia.nocookie.net/steven-universe/images/6/6a/Little_Homeschool_259.png · banner de Homeworld · https://static.wikia.nocookie.net/steven-universe/images/7/7d/Homeworld_banner_zoomed_in.PNG · ✅
4. **El libro «Tale of Steven»** que lee White Diamond en la película: inglés y Gem Glyph en la misma página. Único caso con las dos escrituras juntas · [Gem Glyph](https://steven-universe.fandom.com/wiki/Gem_Glyph) · ✅
5. **El blog de Ronaldo, «Keep Beach City Weird»**: un Tumblr real (desde el 19-sep-2013, antes del estreno) donde el personaje cuenta cosas raras del pueblo · [Fandom](https://steven-universe.fandom.com/wiki/Keep_Beach_City_Weird_(blog)) · ✅

**Pensamientos:** no hay nubes de pensamiento. Los recuerdos y sueños se animan como escena entera. ⚠️ Deducción: «thought bubble» no aparece en la wiki.

**Videojuegos:** la vida no se llama «HP» sino **«harmony»** (punto 11). ⚠️ No se vio la caja de diálogo de ningún juego.

**Cómic:** ⚠️ no se vio una página para describir el globo.

## Punto 7 · Personajes y popularidad

**No hay encuesta oficial** de Cartoon Network: se buscó en inglés y español («favorite character poll», «encuesta personaje favorito oficial»). Lo que hay:

**Dibujos de fans en [Danbooru](https://danbooru.donmai.us/posts?tags=steven_universe)** (2213 dibujos de la serie; cifra exacta) · ✅:

| Puesto | Personaje | Dibujos |
|---|---|---|
| 1 | **Perla** | 414 |
| 2 | **Lapis Lázuli** | 394 |
| 3 | **Peridot** | 355 |
| 4 | Steven | 264 |
| 5 | Amatista | 209 |
| 6 | Garnet | 175 |
| 7 | Blue Diamond | 153 |
| 8 | Rose Quartz | 134 |
| 9 | Connie / Jasper | 122 |
| 10 | Spinel | 92 |

(Hatsune Miku, Kirby y Sonic salen antes por un cruce de etiquetas; no son de la serie.)

- **Ranking de IGN** (2019): Garnet 1.ª, luego Steven y Peridot · https://www.ign.com/articles/2019/07/03/every-steven-universe-character-ranked · ⚠️ (una fuente; la lista completa no se pudo abrir).
- **[Reddit r/stevenuniverse](https://www.reddit.com/r/stevenuniverse)**: en los hilos de «mejor escena» e «icónico» salen sobre todo **Garnet, Lapis y Rose / Pink Diamond**. Steven sale en «opinión impopular»: «Steven era mucho más molesto en las primeras temporadas» (241 votos, 155 comentarios) · ⚠️ (títulos de hilos, no encuesta).
- Hilos con más votos: «Rose burlándose de White Diamond es icónico» (1576 votos) · https://www.reddit.com/r/stevenuniverse/comments/1p0mk6n/rose_making_fun_of_white_diamond_is_iconic/ · «la mejor escena del final» (1090 votos) · https://www.reddit.com/r/stevenuniverse/comments/fq9wza/the_best_scene_from_the_finale/ · «Lapis se luce en esta escena» (883 votos).
- Favoritos del equipo: Garnet es la favorita de Ian Jones-Quartey (co-showrunner) y Steven la de Joe Johnston (animador) · Trivia de [Garnet](https://steven-universe.fandom.com/wiki/Garnet#Trivia) y [Steven](https://steven-universe.fandom.com/wiki/Steven_Universe_(character)#Trivia) · ✅

**Conclusión para la lámina:** Perla es la más dibujada; Garnet la mejor valorada por la prensa y el equipo; Lapis y Peridot, las secundarias con más tirón. Steven es el centro, pero no el más querido.

**Personajes y con quién aparecen** (detalle en el punto 13):
- **Steven**: niño medio Gema, con las tres Gemas, su padre Greg, su amiga Connie y León.
- **Garnet**: la líder; separa a Perla y Amatista cuando discuten.
- **Amatista**: la bromista; hace reír a Steven, comparte con él la comida basura.
- **Perla**: la perfeccionista; sobreprotege y corrige a Steven.

## Punto 8 · Doblaje latino y frases textuales

**Ficha** ([Doblaje Wiki por la API](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Steven_Universe) + [ANMTV](https://www.anmtvla.com/2014/03/steven-universe-estrena-en-abril-por.html)) · ✅:
- Estudio **Etcétera Group**, **Venezuela**. Dirección de casting **Walter Véliz** y **Ángel Lugo**. Dirección musical **Marielba Suárez**. Ingeniera de grabación **Gabriela Belén** (T3-T5).
- Grabado de diciembre de 2013 a enero de 2018. Estreno en Latinoamérica el **7 de abril de 2014** (preestreno el 30 de marzo) en el bloque *Tele Héroes*. 5 temporadas, 160 capítulos.
- Sólo se emitió por **Cartoon Network Latinoamérica**; no hay otro doblaje de Netflix o Crunchyroll.
- Traducción y letras: **Germán Esaá** (p. ej. «El Señor Greg», canción «Nada nos cuesta») y **Jorge Bringas** («En Esa Costa»).
- Curiosidad: los únicos Steven doblados en **México** fueron dos promos cruzadas (*Power Rangers: Dino Charge* y *Hora de aventura: Estacas*), con una actriz mexicana desconocida.

**Reparto principal (dos fuentes cada nombre):**

| Personaje | Original | Latino | Fuente 2 |
|---|---|---|---|
| Steven | Zach Callison | **Leisha Medina** | [ANMTV](https://www.anmtvla.com/2020/01/leisha-medina-habla-sobre-los-motivos.html) (sobre su renuncia) ✅ |
| Garnet | Estelle | **Rocío Mallo** | [ModoGeeks](https://modogeeks.com/2018/07/07/vig-entrevista-a-rocio-mallo-voz-de-garnet-en-steven-universe/) (entrevista) ✅ |
| Amatista | Michaela Dietz | **Stefani Villarroel** (desde el ep. 147 grabó autodirigida desde Chile, con un tono algo distinto) | [ANMTV](https://www.anmtvla.com/2013/12/el-universo-de-steven-comienza-doblaje.html) ✅ |
| Perla | Deedee Magno | **María José Estévez** (T1-T2 en Venezuela; T2-T5 desde Miami) | [Steven Universe Wiki en español](https://steven-universe.fandom.com/es/wiki/Mar%C3%ADa_Jos%C3%A9_Est%C3%A9vez) ✅ |

**Secundarios** (sólo Doblaje Wiki, ⚠️ una fuente): Connie **Yasmil López** · Greg **Henrique Palacios** (canta «Soy un cometa» **Adrián Blanco**) · Lars **Ángel Lugo** · Sadie **Karina Parra** / **Mariangny Álvarez** · Peridot **Sofía Narváez** / **Mariangny Álvarez** · Lapis **Andrea Navas** · Rose / Pink Diamond **Maythe Guedes** · Rubí **Judith Noguera** · Zafiro **Arelys González** · Bismuto **Ivette García**, **Alix Ramírez**, **Catherine Reyes** · Yellow Diamond **Elena Díaz Toledo** · Blue Diamond **Rebeca Aponte** / **Leisha Medina** · White Diamond **Aura Caamaño** · Jasper **Valentina Toro** · Stevonnie **Yojeved Meyer** · Sardonyx **Claudia Álvarez** · Ópalo **Aura Caamaño** · Sugilite **Lileana Chacón** · Cuarzo Arcoíris 2.0 **David D'Urso** (✅ también lo confirma el traductor en [Twitter](https://twitter.com/lobo_jurji/status/1097474721627676672)).

⚠️ María José Estévez dobla a **todas** las Perlas (también a Perla Blanca), según un resumen de búsqueda.

**Frases textuales** (muestras de Doblaje Wiki oídas con `voz.py`, Whisper local; el minuto es el de la muestra):

| Personaje | Frase (textual) | Min. | Cómo suena |
|---|---|---|---|
| **Perla** | «¡Oh, Steven! Los humanos tienen una vida tan corta, aburrida e insignificante que inventan historias para sentir que forman parte de algo más grande» | 0:00 | aguda (263 Hz), muy expresiva (20.8 semitonos), rápida (3.0 palabras/s) |
| Perla | «Quieren responsabilizar por todos los problemas del mundo a un solo enemigo que puedan combatir y no entienden que es una compleja red de fuerzas interrelacionadas que nadie puede controlar» | 0:07 | — |
| **Garnet** | «Cuando dos gemas se combinan crean algo más grande que la suma de sus partes, por eso soy tan genial» | 0:00 | media (190 Hz), muy expresiva (25.0 semitonos), normal (2.57 palabras/s): grave y firme |
| Garnet | «Para que Amatista pudiera ser ella, para que Perla fuese libre y para que pudiéramos estar juntas» · «Para que existieras tú» | 0:12 · 0:18 | — |
| Garnet (cantado) | «No destruirás lo que tenemos, juntos por siempre así estaremos» · «Si tú nos separas nos uniremos, y siempre seremos mejores que tú» | 0:21 · 0:25 | — |
| **Amatista** | «¡Nunca pedí ser lo que soy! ¡Nunca pedí ser creada!» | 0:00 | muy aguda (449 Hz), expresiva (9.3 semitonos), normal (2.33 palabras/s) |
| **Steven** | «Sí, pero nada permanece en la tierra, las cosas siempre están cambiando, las hojas, las ciudades, incluso Jersey cambia» | 0:00 | aguda (244 Hz), muy expresiva (17.9 semitonos), rápida (3.29 palabras/s) |
| Steven | «Mi papá dice que las paradas de descanso eran asquerosas, pero ahora venden sushi» · «Este no es el mismo mundo que te mantuvo atrapada, ya no lo es» · «Y sé que no se siente como un hogar, pero tal vez eso pueda cambiar» | 0:09 · 0:13 · 0:17 | — |

Muestras: [Perla.ogg](https://static.wikia.nocookie.net/doblaje/images/8/87/Perla.ogg/revision/latest?cb=20170601232503&path-prefix=es) · [Garnet.ogg](https://static.wikia.nocookie.net/doblaje/images/b/bd/Garnet.ogg/revision/latest?cb=20170620183938&path-prefix=es) · [Amatista.ogg](https://static.wikia.nocookie.net/doblaje/images/a/a6/Amatista.ogg/revision/latest?cb=20170130215341&path-prefix=es) · [Steven.ogg](https://static.wikia.nocookie.net/doblaje/images/a/af/Steven.ogg/revision/latest?cb=20170614194925&path-prefix=es).

- La de Perla es la versión latina de su frase de «Keep Beach City Weird» («Humans just live short, boring, insignificant lives…») · ✅
- ⚠️ **La de Garnet parece un montaje de varias escenas**, no sólo la canción «Stronger Than You» como dice la parte de voz: «la Tierra era de Diamante Rosado…» (0:06) no es de la pelea con Jasper. Sólo 0:21-0:25 suena a la letra cantada. No se sabe de qué capítulo es cada frase.
- ⚠️ La de Amatista encaja con su pelea con Perla en «On the Run», pero la muestra no dice el capítulo. La de Steven tampoco.
- En 0:17 de Perla.ogg Whisper oyó mal un verso cantado: **no citarlo**.
- ⚠️ **No hay clips oficiales doblados transcritos.** El clip `TIO` (doblado) se miró en fotogramas, no se transcribió.


## Punto 9 · Música y sonido

**Es una serie cantada.** Steven canta más de 38 canciones ([Trivia de Steven](https://steven-universe.fandom.com/wiki/Steven_Universe_(character)#Trivia), ✅). Por eso se propone #🎵・canto.

**El opening**
- **«We Are the Crystal Gems»**. Música de Rebecca Sugar y Aivi & Surasshu. Versión corta de 0:36, cantada por Zach Callison (Steven). Versión larga de 2:23 con Estelle (Garnet), Michaela Dietz (Amatista) y Deedee Magno Hall (Perla) · [ficha de la canción](https://steven-universe.fandom.com/wiki/We_Are_the_Crystal_Gems) + oído en `GG` 0:00-0:36 · ✅
- En latino es **«Somos las Gemas de Cristal»**, cantada por **Leisha Medina** (la voz de Steven). Letra del opening extendido en [Letras.com](https://www.letras.com/steven-universo/somos-las-gemas-de-cristal-opening-extendido/) · ✅

**El cierre**
- No hay un *ending* cantado distinto por capítulo, como en el anime. En el piloto los créditos van con **música instrumental** (`GG` 11:10-11:30, oído) · ✅
- El álbum oficial trae **«Love Like You (End Credits)»**, cantada por Rebecca Sugar, como tema de créditos (pista 37) · ✅. ⚠️ No se comprobó en qué capítulos suena cantada y en cuáles instrumental.

**Las canciones que más pesan**

| Canción | Capítulo | Quién la canta | Qué ambiente da |
|---|---|---|---|
| **«Stronger Than You»** («Más Fuerte que Tú») | «Jail Break» («Escape de la Prisión»), T1-E52 · dura 2:52 | Estelle; en latino, **Rocío Mallo** | triunfo y confianza. Garnet pelea contra Jasper. El himno del fandom · [ficha](https://steven-universe.fandom.com/wiki/Stronger_Than_You) ✅ |
| **«It's Over, Isn't It»** | «Mr. Greg» («El Señor Greg»), T3, ep. 86 · dura 2:20 | Deedee Magno Hall (Perla) | duelo y amor no correspondido. La que más hace llorar (punto 21) · [ficha](https://steven-universe.fandom.com/wiki/It%27s_Over_Isn%27t_It) ✅ |
| **«Love Like You»** | créditos | Rebecca Sugar | ternura. En Reddit la citan como «la más icónica» ([hilo](https://www.reddit.com/r/stevenuniverse/comments/1vb7f3s/in_your_opinion_what_is_the_most_iconic_steven/), 203 votos) ⚠️ |
| **«Soy un cometa»** | — | en latino, **Adrián Blanco** (canta por Greg) | Doblaje Wiki ⚠️ (una fuente) |
| **«Nada nos cuesta»** · **«En Esa Costa»** | «El Señor Greg» · — | letras adaptadas por Germán Esaá y Jorge Bringas | Doblaje Wiki ⚠️ |

Otras del álbum: «Giant Woman», «On the Run», «Full Disclosure», «Mr. Greg», «Here Comes a Thought» y «What's the Use of Feeling (Blue)?» · [Soundtrack: Volume 1](https://steven-universe.fandom.com/wiki/Soundtrack:_Volume_1) · ✅

**Discos oficiales** ([MusicBrainz](https://musicbrainz.org/release-group/9ced52a8-db50-4e7e-b2de-17a87c936626) + wiki):
- *Soundtrack: Volume 1* (2-jun-2017): 37 canciones. N.º 1 en iTunes y entró en la *Billboard 200* · ✅
- *Soundtrack: Volume 2* (12-abr-2019) · [MusicBrainz](https://musicbrainz.org/release-group/0fdf4d2c-5a0c-4c27-8cee-0f06206ce18d) · ✅
- Disco de **karaoke** (12-abr-2019) · [MusicBrainz](https://musicbrainz.org/release-group/486f567b-ddac-4093-80ae-9ed5e4a5d9da) · ⚠️ (una fuente)
- *Steven Universe: The Movie* (2-sep-2019) y **su versión en español** (25-oct-2019) · [MusicBrainz, versión en español](https://musicbrainz.org/release-group/065a1034-b94b-4630-8613-6724ade62833) · ⚠️ (una fuente; no dice qué doblaje es). Muy útil para #canto: son canciones oficiales cantadas en español.
- *Steven Universe Future* (23-oct-2020) y las partituras instrumentales de la T1 (29-may-2020) y la T2 (26-jun-2020) de Aivi & Surasshu · [MusicBrainz T1](https://musicbrainz.org/release-group/e0e63ef4-81df-4c2a-ae78-73a127320b1f) · ⚠️
- Bandas sonoras de los juegos *Attack the Light* y *Save the Light*, completas en [Internet Archive](https://archive.org/details/steven-universe-attack-the-light-full-ost) · ⚠️ existen, no se escucharon.

**Los instrumentos de cada uno** (Trivia de la wiki, ✅): Steven, el **ukulele** (también guitarra, bajo, batería y piano; tiene oído absoluto). Greg, la guitarra. Garnet, el **keytar** (se lo enseñó Greg). Amatista, una **batería eléctrica** «suelta y salvaje». Pose de música: **hoja n.º 145** (Greg y Steven con guitarra y bajo, llamas detrás, película).

**Sonidos que todos reconocen**
- **El «poof»**: cuando una Gema recibe mucho daño, su cuerpo se deshace en humo y queda sólo la piedra. No muere · [Gems](https://steven-universe.fandom.com/wiki/Gems) · ✅ la palabra; ⚠️ no hay página de «efectos de sonido» en la wiki (se buscó `sound effect`, `onomatopoeia`).
- **Sacar el arma**: destello geométrico con líneas de brillo alrededor de las manos. Perla en `GG` 3:30, Garnet en `GG` 6:00-6:10 · ✅ visto. ⚠️ No se aisló el sonido.
- **No hay onomatopeyas escritas en pantalla**: es animación de EE. UU. (ver punto 5).

## Punto 10 · Vídeos y tendencias

**YouTube pide iniciar sesión desde el servidor.** Todo lo que lleva ✅ se vio en Internet Archive o Dailymotion con `fotogramas.py`. Los enlaces `#t=` van al minuto.

**Tráileres**
- `TRL` Toonami de la película (2:00, visto cada 2 s): 1:36-1:48 fusión morada de cuatro brazos y León; 1:52-1:54 cartela «STEVEN UNIVERSE THE MOVIE — Monday September 2nd 6:00P» · [#t=96](https://archive.org/download/steven-universe-the-movie-toonami-trailer/Steven%20Universe%20The%20Movie%20TOONAMI%20Trailer.mp4#t=96) · ✅
- En Dailymotion (sin mirar, ⚠️): tráiler oficial de la serie (JustWatch, 0:41) · https://www.dailymotion.com/video/x8hroiu · tráiler de la película en VO (Sensacine, 1:51) · https://www.dailymotion.com/video/x88pl5q · tráiler de *Future* (BetaSeries, 0:51) · https://www.dailymotion.com/video/x86qv4j
- Los demás clips de Dailymotion con «Steven Universe» (0:21-0:33) son **avisos de la tele francesa**, no escenas. Descartados.

**Escenas completas** (punto 2): `GG`, `STY`, `ANS`, `IOI` y `TIO`.

**Análisis y ensayos**
- «Steven Universe VS Social Norms | A Video Essay», de **Saberspark**, 14:45: cómo la serie rompe normas de género en los dibujos para niños · [Internet Archive](https://archive.org/details/youtube-oHkd2QERNy8) · ⚠️ sólo se leyó la ficha, no se vio.
- «Steven Universe Review - Is it good or bad?», de **PhantomStrider**, 5:13 · [Internet Archive](https://archive.org/details/steven-universe-review-is-it-good-or-bad) · ⚠️ sólo la ficha.
- Pódcast «The Secret Origin of STEVEN UNIVERSE» con **Chris McDonnell** (autor del artbook *Art & Origins*) · [Internet Archive](https://archive.org/details/98fc287479a22cb81f0e3dcd9ff72b8e) · ⚠️ sólo el título.

**Tendencias de TikTok** (recopilación de fans `TT`, 4:59, vista cada 3 s) · ✅:

| Minuto | Qué pasa | Para qué sirve |
|---|---|---|
| [2:33-2:57](https://archive.org/download/steven-universe-tik-toks/Steven%20Universe%20Tik%20Toks.mp4#t=153) | cosplay en pareja: Steven y Rose/Perla por la calle (cuenta «PorkCutlett») | ideas de cosplay |
| 2:57-3:15 | *speedpaints* de fan art de Steven | #arte |
| [3:18-3:33](https://archive.org/download/steven-universe-tik-toks/Steven%20Universe%20Tik%20Toks.mp4#t=198) | TikTok de «elige tu aventura»: «You meet a Jasper… Fuse with me? Yes/No», con botones de sí y no | formato de reto o de rol |
| 3:48-4:03 | cosplay de **Spinel** bailando al aire libre | Spinel tiene mucho tirón en TikTok |
| 4:33-4:45 | figura rosa corriendo por una acera, estilo Spinel | — |

**«1 Second From Every Steven Universe Episode»** (`1S`, 2:55, visto cada 2 s): un segundo de cada capítulo, en orden. Sirve para ver qué se repite: **Steven corriendo, Garnet señalando, Perla con la lanza** · ✅

**Episodios subidos a Internet Archive** (del recolector, ⚠️ sin comprobar uno a uno): el episodio 86 «Mr. Greg» · https://archive.org/details/StevenUniverseE86 (4302 descargas) · la T1 «Rose's Scabbard» y «Open Book» · https://archive.org/details/StevenUniverseS01E4546RosesScabbardOpenBook · la película · https://archive.org/details/stevenuniversethemovie_202001 . Si hace falta un minuto nuevo, se empieza por aquí.

**Reacciones**: en Internet Archive hay *blind reactions* (reacciones a ciegas) de la T1 51-52, la T4 21-25 y la T5; se descartaron porque no aportan fotogramas propios.

## Punto 11 · Videojuegos

Tres juegos propios de Grumpyface Studios, uno de ritmo, uno de cartas y un *crossover*. No hay ficha en Steam (`datos-texto.md`).

| Juego | Año y plataforma | Cómo es | Lo que sirve para una lámina |
|---|---|---|---|
| ***Attack the Light*** | 2015, móvil | RPG por turnos con aire de *Paper Mario*: mazmorras en cuadrícula y golpes a tiempo (tocar o deslizar en el momento justo) | la vida no se llama «HP», se llama **«harmony»** (armonía). Al llegar a 0 la Gema «se retira a su piedra». Las acciones gastan **«starpower»** (estrellas, máximo 9). El modo difícil «Diamond Mode» **esconde las estrellas** · [Fandom](https://steven-universe.fandom.com/wiki/Attack_the_Light) + [Wikipedia](https://en.wikipedia.org/wiki/Steven_Universe:_Attack_the_Light) ✅ |
| ***Save the Light*** | 2017, PS4, Xbox One, PC, Switch | pasa a 3D, más puzles; 8 personajes jugables (uno de pago); el «vínculo» en combate desbloquea **fusiones jugables** | el guion lo escribieron **Rebecca Sugar y el equipo de la serie** (el «Crewniverse»): los diálogos del juego suenan como la serie · [Fandom](https://steven-universe.fandom.com/wiki/Save_the_Light), que cita PlayStation Blog, GameSpot y The Verge ✅ |
| ***Unleash the Light*** | 2019, móvil | combate por turnos en una **cuadrícula con forma de diamante**: la punta de arriba golpea la fila de arriba, etc. | el **inventario es la Mochila Hamburguesa** (*Cheeseburger Backpack*). Los carteles de las colonias usan **Gem Glyph como letra real**, letra a letra · [Fandom](https://steven-universe.fandom.com/wiki/Unleash_the_Light) ✅ |
| *Soundtrack Attack* | web de Cartoon Network | juego de ritmo gratis | ⚠️ sólo se vio el título |
| *Beach-A-Palooza Card Battling Game* | dic. 2020, Cryptozoic, sólo mecenas de Kickstarter | juego de cartas de mesa: eliges personajes, formas una **banda** y fusionas en el escenario | encaja con #canto. Foto del producto 1655×916 · https://static.wikia.nocookie.net/steven-universe/images/9/95/SU_Beach-A-Palooza_Beauty_Shot.png · ⚠️ una fuente |
| *Cartoon Network: Battle Crashers* | 2016, PS4, Xbox One, 3DS, Switch | *beat 'em up* de hasta 4 jugadores; Steven junto a Finn, Gumball, Mordecai y Clarence | [UPI](https://www.upi.com/Entertainment_News/2016/08/18/Cartoon-Network-Battle-Crashers-Adventure-Time-Steven-Universe-team-up-in-new-game/7091471540606/) + [Wikipedia](https://en.wikipedia.org/wiki/Cartoon_Network:_Battle_Crashers) ✅ |

- *Attack the Light* **se retiró de las tiendas el 23-dic-2024**: sólo quedan capturas y vídeos · [MobileSyrup](https://mobilesyrup.com/2017/06/25/attack-light-game-ios-android/) · ⚠️ una fuente.
- Arte de los juegos (poses con arma en alto): ver punto 1 (*Save the Light* 1280×854; *Unleash the Light* Garnet, Perla y Amatista).
- Los juegos de lucha de otras marcas (Brawlhalla, MultiVersus) van en el punto 23.

⚠️ **No se vio la caja de diálogo de ningún juego ni sus menús.** [Game UI Database](https://www.gameuidatabase.com/) pide un reto de Cloudflare y [The Cutting Room Floor](https://tcrf.net/Steven_Universe:_Save_the_Light_(Windows)) (contenido descartado de *Save the Light*) dio 403, directo y por Wayback. No se sabe si la caja lleva retrato, marco o color. **No inventarla**: si una lámina usa un juego, que use el «harmony» o la cuadrícula de diamante, que sí están descritos.

## Punto 12 · Lo que ama el fandom y qué NO hacer

**Lo que todos reconocen**
- **«Cheeseburger Backpack»** (la Mochila Hamburguesa de Steven), T1-E3. Amatista y Perla la cantan y gritan en bucle. Es de los GIF y remixes más repetidos · [Fandom](https://steven-universe.fandom.com/wiki/Cheeseburger_Backpack_(episode)) + [The Avocado](https://the-avocado.org/2019/11/13/steven-universe-rewind-cheeseburger-backpack-together-breakfast/) · ✅
- **«Stronger Than You»**: el himno. Se usa en *covers*, remixes y en el meme de «por eso soy tan genial» (la frase latina de Garnet, punto 8). En Internet Archive, 13 590 descargas del vídeo y 5060 del tema · ✅
- **La boda de Rubí y Zafiro** («Reunited»): la primera boda entre dos personajes del mismo sexo en un programa infantil de Cartoon Network. Motivo de orgullo · [Wikipedia](https://en.wikipedia.org/wiki/Cartoon_Network_and_LGBTQ_representation) · ✅
- **Los ojos de estrella de Steven** cuando algo le emociona (`STY` 0:54-0:57, y el texto de «Appearance» de la wiki) · ✅
- **Lo que sube a lo más alto en [Reddit](https://www.reddit.com/r/stevenuniverse)** (votos, del recolector) · ⚠️ son títulos, no encuesta:
  - «Rose burlándose de White Diamond es icónico» (1576) · «Lo vi en directo: uno de los momentos más icónicos de Cartoon Network» (1263, 96 comentarios) · «la mejor escena del final» (1090) · «ojalá esta fusión hubiera pasado» (955) · «Lapis se luce en esta escena» (883).
  - **Lo que divide**: «No entiendo el *hype* de Spinel» (359 votos, 110 comentarios) · «Steven era mucho más molesto en las primeras temporadas» (241, 155 comentarios).
- **Parejas del fandom** (*ships*): Perla y Rose («Pearlrose»), Lapis y Peridot («Lapidot»). Explican por qué Perla, Lapis y Peridot son las más dibujadas · ⚠️ interpretación de la parte de voz.

**Qué NO hacer (un fan lo notaría al instante)**
1. **No adelgazar** a Amatista, Garnet, Rose ni Steven. En 2018 el fandom se lanzó contra una artista por dibujar a Rose más delgada. Es el tema más vigilado · [Jezebel](https://www.jezebel.com/steven-universe-fandom-turns-on-fan-artist-mobs-her-wi-1793852421) + [The A.V. Club](https://www.avclub.com/how-steven-universe-s-fat-bodies-helped-me-draw-my-own-1845830394) · ✅
2. **No usar un cuerpo genérico de anime.** Cada Gema es una forma: **Garnet cuadrada**, **Amatista redonda**, **Perla cono** (alta y fina). Lo decidió Rebecca Sugar siguiendo la Bauhaus (punto 18) · ✅
3. **Garnet no hace preguntas.** No ha hecho ni una en toda la serie ([Trivia](https://steven-universe.fandom.com/wiki/Garnet#Trivia), ✅). Sus textos son afirmaciones.
4. **Perla no come** («el proceso digestivo me da asco»); sí toma té. Amatista come de todo · ✅ (punto 20)
5. **Una Gema no «muere» por un golpe**: hace «poof» y se regenera. Morir de verdad es **fragmentarse** (*shatter*), el gran tabú · ✅ (punto 25)
6. **No decir que las Gemas son «mujeres»**: usan el femenino por convención (Rebecca Sugar en su [AMA de Reddit](https://www.reddit.com/r/IAmA/comments/2e4gmx/)) · ✅
7. **No poner una burbuja blanca de cómic** (la serie no las usa, punto 6) ni **«HP»** en una interfaz (es «harmony», punto 11).
8. **No copiar la transformación de Sailor Moon** para Steven o Spinel: ya es un préstamo reconocido (punto 24).
9. **No mezclar el verde veneno de las naves de Homeworld** con escenas de hogar: el verde es «amenaza», lo cálido es «la Tierra» (punto 4).

⚠️ No encontré una lista de memes propia del fandom hispano (se buscó «Steven Universe memes fandom hispano» y «chiste interno fandom latino»). Comparte los memes globales traducidos.

## Punto 13 · Personajes a fondo

Base: las secciones «Personality» y «Trivia» de la wiki, leídas enteras por la parte de voz; las voces, oídas con `voz.py`; las caras, vistas en fotogramas.

### Steven Universe (Cuarzo Universe)
- **Cómo es:** optimista, amable, abierto, de corazón blando. Ve lo mejor de todos, hasta de sus enemigos. Casi nunca guarda rencor. Prefiere negociar a pelear · [Personality](https://steven-universe.fandom.com/wiki/Steven_Universe_(character)#Personality) ✅
- **Qué le importa:** su familia (Greg y las Gemas), Connie, Beach City. De Greg heredó la música; de Rose, la compasión · ✅
- **Miedos:** no cuenta sus problemas a las Gemas por miedo a cómo reaccionarán (Perla se culparía, Garnet le sermonearía, Amatista fingiría madurez), según «Prickly Pair». Las misiones le dejan trauma y ansiedad («Growing Pains») · [Trivia](https://steven-universe.fandom.com/wiki/Steven_Universe_(character)#Trivia) ✅
- **Arco:** de niño que no controla su poder a asumir su lado de Diamante Rosa; crisis de identidad en la T5 y en *Future* · ✅
- **Qué transmite:** calidez y ganas de arreglarlo todo. Consuela con ejemplos pequeños y cotidianos: «incluso Jersey cambia», «ahora venden sushi» (Steven.ogg 0:00-0:13) · ✅
- **Cómo habla:** agudo (244 Hz), **muy expresivo** (17.9 semitonos) y **rápido** (3.29 palabras/s). A veces habla de sí mismo en tercera persona · ✅
- **Manías:** se marea con los giros, le encanta cocinar, canta de repente, toca el ukulele · ✅

### Garnet
- **Cómo es:** la líder. Práctica y directa, pero **actúa por intuición**. Calmada casi siempre (eso le viene de Zafiro). Pone paz entre Perla y Amatista. Exige respeto y regaña si no se sigue una orden · [Personality](https://steven-universe.fandom.com/wiki/Garnet#Personality) ✅
- **Quién es de verdad:** una **fusión** de Rubí y Zafiro, planeada desde antes del piloto. Pistas: la estrella doble de su cartela y las gemas roja y azul · ✅
- **Cómo habla:** pausada, pocas palabras, **nunca pregunta**. Voz media (190 Hz), firme y sostenida; se suelta al cantar (25.0 semitonos) · ✅
- **Su grieta:** cuando se separa (Rubí llora, Zafiro se enfría), en «Jail Break», «Hit the Diamond», «Made of Honor» · ✅ la ficha, ⚠️ no visto en vídeo.
- **Qué transmite:** seguridad total. Es la que dice «por eso soy tan genial» sin sonar arrogante.

### Amatista
- **Cómo es:** divertida, ruidosa, «fuera de control» (Rebecca Sugar). Come y duerme sin necesitarlo, por gusto. Desordenada y acumuladora («Maximum Capacity»). Bromista, pero **nota lo que sienten los demás** (consuela a Steven en «An Indirect Kiss») · [Personality](https://steven-universe.fandom.com/wiki/Amethyst#Personality) ✅
- **Su herida:** nació en el Kindergarten y se siente **inferior** a Perla y Garnet. Estalla en «On the Run» y en su obsesión con Jasper («Crack the Whip», «Steven vs. Amethyst», «Beta»). Lo cierra al fusionarse con Steven en **Cuarzo Ahumado** («Earthlings») · ✅
- **Su grito, en latino:** «¡Nunca pedí ser lo que soy! ¡Nunca pedí ser creada!» (Amatista.ogg 0:00). Voz muy aguda (449 Hz) · ✅
- **Alter ego:** **Purple Puma**, luchadora enmascarada, para soltar el estrés de recibir órdenes · ✅
- **Guiño hispano:** habla español: «¡No, mi torta!» en «Monster Buddies» · [Trivia](https://steven-universe.fandom.com/wiki/Amethyst#Trivia) ✅

### Perla
- **Cómo es:** perfeccionista, ordenada hasta la obsesión, sabe «de un sinfín de temas». A la vez, **muy baja autoestima**: necesita aprobación; sin un líder se ve «inútil» · [Personality](https://steven-universe.fandom.com/wiki/Pearl#Personality) ✅
- **Por qué:** en Homeworld las Perlas son **propiedad**, no Gemas con derechos. Golpea a Peridot para demostrar que no es un objeto («Back to the Barn») · ✅
- **Su amor:** Rose Cuarzo (luego, Diamante Rosa). No correspondido: es el motor de «It's Over, Isn't It» · ✅
- **Cuerpo:** de **bailarina**: de puntillas, piernas rectas, piruetas al pelear. Su lanza es en realidad una *glaive* · [Trivia](https://steven-universe.fandom.com/wiki/Pearl#Trivia) ✅
- **Cómo habla:** aguda (263 Hz), muy expresiva (20.8 semitonos), **rápida** (3.0 palabras/s). Explica largo y un poco por encima de los humanos: «…inventan historias para sentir que forman parte de algo más grande» (Perla.ogg 0:00) · ✅
- Es «la más propensa a llorar y cantar» después de Steven (lo dice Peridot, en broma) · ✅

### Su cara en cada emoción (fotograma y minuto)

| Emoción | Steven | Garnet | Amatista | Perla |
|---|---|---|---|---|
| **Alegría** | `GG` 1:20 abraza la caja de Cookie Cat · `TIO` 0:56-1:04 relajado, ojos entornados | `GG` 10:20 manos en la cadera · `STY` 2:42 sonrisa confiada | `GG` 4:00-4:10 comiendo feliz · `TIO` 0:32-0:40 apoyada en Garnet | ⚠️ no capturada |
| **Rabia** | hoja n.º 142 (Steven rosa, «Volleyball») · ⚠️ sin minuto | `STY` 3:09-3:15 puñetazo en vuelo | ⚠️ sólo audio (Amatista.ogg) | `GG` 10:10 lanza en alto, determinada |
| **Tristeza** | hoja n.º 123-124 («Storm in the Room») · ⚠️ sin minuto | ⚠️ no vista | ⚠️ no vista | `IOI` 2:10 **lágrima** en la mejilla · `IOI` 2:00 mira abajo con una rosa |
| **Miedo** | `GG` 8:20 brazos abiertos, alarma | ⚠️ no vista | ⚠️ no vista | `GG` 2:20 manos junto a la cara, ojos muy abiertos |
| **Vergüenza / frustración** | ⚠️ no vista | ⚠️ no vista | ⚠️ no vista | `GG` 4:30 se tapa la cara, exasperada |
| **Seriedad / mando** | — | `TIO` 1:36 primer plano, boca firme · `GG` 2:40 brazos cruzados | — | `GG` 8:00 brazos cruzados, desaprueba |
| **Asombro** | `STY` 0:54-0:57 **ojos de estrella** | — | — | — |

Enlaces: `TIO` 1:36 · https://www.dailymotion.com/video/x5ejzz4 · `IOI` 2:10 · https://www.dailymotion.com/video/x4wic92 . ⚠️ De las 20 casillas que pide el encargo (5 emociones × 4 personajes) faltan 9, y 2 de Steven van sin minuto (fotogramas de la wiki). Se miraron 8 vídeos y no salen: hay que buscarlas en capítulos que no se vieron.

### Dinámicas (para láminas en grupo)
- **Garnet separa** a Perla y Amatista cuando discuten. Discuten fuerte en «Cry for Help» y «On the Run», pero se reconcilian por Steven · ✅
- **Amatista hace reír a Steven**: comparten humor y comida basura. **Perla lo sobreprotege y lo corrige**; Steven la saca de su perfeccionismo · ✅
- Buen trío para una lámina: Garnet en el centro, Perla explicando, Amatista haciendo la broma.

### Las secundarias más queridas
- **Lapis Lázuli** (394 dibujos, 2.ª): pasó unos 6000 años atrapada en un espejo. Desconfía de casi todos, sobre todo de Peridot al principio, y de sí misma por lo que hizo como Malaquita (fusión dañina con Jasper). Se abre con Steven, que la liberó y curó su gema. Miedo a la responsabilidad y a repetir relaciones dañinas · [Personality](https://steven-universe.fandom.com/wiki/Lapis_Lazuli#Personality) ✅
- **Peridot** (355, 3.ª): empieza fría y leal a Homeworld. Varada en la Tierra se vuelve nerviosa, **risas exageradas y gestos enormes**. Sin sus «potenciadores» se vuelve infantil y paranoica, se encierra en el baño de Steven, y él la calma: ahí empieza su redención · [Personality](https://steven-universe.fandom.com/wiki/Peridot#Personality) ✅
- **Connie Maheswaran**: estudiosa, tímida al principio, gran lectora. Aprende espada con Perla. Con Steven forma a **Stevonnie** · ⚠️ no se leyó su ficha entera.
- **Greg Universe**: exmúsico de gira, relajado y cariñoso; vive en su furgoneta. Es el lado humano de Steven · ⚠️ no se leyó su ficha entera.

## Punto 14 · Poses analizadas

Todas vistas con `fotogramas.py` (no de memoria) o en las hojas. `GG` = [«Gem Glow»](https://archive.org/download/steven-universe-s-01-e-01-gem-glow/Steven%20Universe%20-%20S01E01%20-%20Gem%20Glow.mkv#t=90); añade `#t=<segundos>` para ir al minuto.

### Steven
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | `GG` 0:50 | se echa atrás, brazos arriba, manos abiertas, protege la caja de rosquillas | reaccionar, sorpresa |
| 2 | `GG` 1:20 | abraza la caja de Cookie Cat contra el pecho, sonrisa enorme | **celebrar** |
| 3 | `GG` 1:30 | señala con el índice un símbolo en la pared | **presentar**, descubrir |
| 4 | `GG` 3:20 | se abraza a sí mismo, mira de lado, hablando con Perla | **pensar**, preguntar |
| 5 | `GG` 5:30 | brazo extendido hacia delante, decidido | **animar** a que le sigan |
| 6 | `GG` 8:20 | brazos abiertos, cara de alarma, de espaldas al monstruo | advertir |
| 7 | `GG` 9:30 | sostiene dos Cookie Cats, preocupado, ofreciendo | pedir ayuda, ofrecer |
| 8 | `STY` 0:54-0:57 | ojos de estrella, boca abierta | admirar |
| 9 | hoja n.º 145 | toca el bajo junto a Greg, llamas detrás (película) | **música** |
| 10 | hoja n.º 46 | sentado en el techo del vagón rojo con Amatista, atardecer («On the Run») | acompañar, contar algo tranquilo |

### Garnet
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | `GG` 2:40 | de pie, brazos cruzados, seria tras las gafas | vigilar, **autoridad** |
| 2 | `GG` 6:00-6:10 | saca los guanteletes con un destello | prepararse |
| 3 | `GG` 9:40-10:00 | dispara un rayo junto a Perla y Amatista | pelear en equipo |
| 4 | `GG` 10:20 | en el centro, manos en la cadera, tras la victoria | **celebrar** |
| 5 | `STY` 0:00 | sentada, tranquila, Steven al lado | **explicar** con calma |
| 6 | `STY` 2:42-2:45 | de pie, **chasquea los dedos**, sonrisa confiada | **presentar**, seguridad |
| 7 | `STY` 3:09-3:15 | puñetazo en vuelo contra Jasper | enfrentar (lo más parecido a **regañar**) |
| 8 | `ANS` 8:56-9:12 | Rubí y Zafiro se dan la mano por primera vez | **animar**, unir |
| 9 | `ANS` 11:04-11:20 | brillan y se funden: nace Garnet | transformación |
| 10 | hoja n.º 140 | junto a Steven de traje, de noche («Together Forever») | acompañar |

### Amatista
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | `GG` 4:00-4:10 | come un Cookie Cat, feliz, con el envoltorio | **celebrar**, disfrutar |
| 2 | `GG` 5:40 | ofrece un Cookie Cat a Steven, encorvada y relajada | compartir |
| 3 | `GG` 6:30 | señala mientras habla con Steven en la cocina | **explicar** |
| 4 | `GG` 8:40-8:50 | corre por el acantilado con Garnet y Perla | **animar**, actuar en equipo |
| 5 | `GG` 10:40 | cava en la arena junto a Steven, juguetona | jugar |
| 6 | `GG` 10:50 | agachada junto a Steven en la playa | acompañar |
| 7 | hoja n.º 5-7 | cuerpo entero, puño cerrado, sonrisa, látigo | **presentar** con actitud · ⚠️ no se sabe si el archivo es oficial |
| 8 | hoja n.º 143 | señala al cielo con Steven al lado («What's Your Problem») | **presentar**, mostrar algo |

### Perla
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | `GG` 2:20 | manos junto a la cara, ojos muy abiertos | miedo, sorpresa |
| 2 | `GG` 3:30 | saca la lanza con círculos de luz en las manos | **presentar** con poder |
| 3 | `GG` 4:30 | se tapa la cara con las manos | frustración (**pensar**, agobio) |
| 4 | `GG` 7:10-7:40 | regaña a Steven de cerca por las normas de la casa | **regañar** |
| 5 | `GG` 8:00 | brazos cruzados, mirada de desaprobación | vigilar |
| 6 | `GG` 10:10 | lanza en alto, brillando, decidida | pelear, decidir |
| 7 | hoja n.º 15 | de pie, **mano abierta** hacia un lado | **explicar** |
| 8 | hoja n.º 41 | baila de noche, brazo en alto («Log Date 7 15 2») | canto, gracia |
| 9 | `IOI` 2:00-2:10 | mira abajo con una rosa; luego la lágrima | tristeza |

### Qué pose para qué

| Para… | Steven | Garnet | Amatista | Perla |
|---|---|---|---|---|
| presentar | 3 | **6** (chasquido) | 7 u 8 | 2 |
| explicar | 4 | 5 | 3 | **7** (mano abierta) |
| celebrar | **2** | 4 | 1 | — |
| regañar | 6 (advertir) | 7 (enfrentar) | — | **4** |
| pensar | 4 | — | — | 3 |
| animar | **5** | 8 | 4 | — |
| cantar | 9 | — | — | 8 |

⚠️ Faltan poses vistas de Amatista regañando y de Perla y Amatista celebrando.

## Punto 15 · Vestuario y hex medidos

Hex medidos con Pillow en las **fichas de producción** del punto 1 (zona plana de cada prenda, sin el negro de la línea ni el fondo). No son de fan art.

| Personaje | Prenda | Hex | De qué archivo |
|---|---|---|---|
| **Steven** | camiseta salmón | `#FF5E6D` | [With Weapon3](https://static.wikia.nocookie.net/steven-universe/images/c/c2/Steven_Universe_-_With_Weapon3.png) |
| | estrella amarilla del pecho | `#FFDE3F` | ídem |
| | vaqueros azules con vuelta | `#1974A2` | ídem |
| | escudo rosa | `#FA98C9` | ídem |
| **Garnet** | piel magenta violácea | `#A53A84` | [Garnet With Rings](https://static.wikia.nocookie.net/steven-universe/images/2/27/Garnet_With_Rings.png) |
| | pico del pecho | `#FF5EF2` | ídem |
| | hombreras | `#CD1AAE` | ídem |
| | mono azul marino casi negro | `#000035` | ídem |
| | guanteletes rojo oscuro (estrella dorada en la palma) | `#B50535` | ídem |
| **Perla** | piel crema pálida | `#F8F4E1` | [Current Pearl Request](https://static.wikia.nocookie.net/steven-universe/images/8/8c/Current_Pearl_Request.png) |
| | top turquesa | `#8DDACD` | ídem |
| | estrella del top | `#E0FF87` | ídem |
| | lazo de la cintura | `#69F4E2` | ídem |
| | falda-short tostada | `#F9D27D` | ídem |
| **Amatista** | piel lavanda | `#B898CC` | [Amethyst CYM Outfit](https://static.wikia.nocookie.net/steven-universe/images/4/4b/Amethyst_CYM_Outfit.png) |
| | top de tirantes negro carbón (y estrellas del short) | `#232229` | ídem |
| | gema del pecho | `#CF67FE` | ídem |
| | shorts vaqueros grises | `#657188` | ídem |
| | pelo lila pálido hasta el suelo | `#DCD3EF` | ídem |

✅ los cuatro (contrastados con el texto de «Appearance» de la wiki: «salmon-pink T-shirt with a gold star», «magenta skin tone», «deep violet cube-shaped afro»).

**Lo icónico (lo que todos reconocen)** · ✅ repetido en Funko Pop y en las 3 hojas:
- **Steven:** camiseta salmón con estrella, vaqueros con vuelta y **chanclas salmón**. Gema rosa en el ombligo. Pelo castaño oscuro rizado.
- **Garnet:** **afro cúbico** violeta oscuro, **gafas de sol** (gafas-visor), mono azul marino, guanteletes rojos. **Tres ojos**: el derecho rojo rubí, el izquierdo azul zafiro y el del centro morado. Una gema en cada palma: la de Zafiro (derecha) con faceta triangular y la de Rubí (izquierda) con faceta cuadrada · [Appearance](https://steven-universe.fandom.com/wiki/Garnet#Appearance) ✅
- **Perla:** top turquesa, falda-short tostada, botas rosa pálido, **nariz puntiaguda**, pelo corto salmón y la **perla en la frente**. Con la lanza.
- **Amatista:** top negro, short vaquero con estrellas, pelo largo hasta el suelo, gema en el pecho. Con el látigo.

**Por temporada o arco**
- **Steven en la película (2019):** más alto, se le ve el cuello; **camisa celeste**, sigue con vaqueros y chanclas salmón · ✅ texto de la wiki; ⚠️ hex sin medir.
- **Steven en *Future*:** **chaqueta rosa** (hojas n.º 126-132) · ⚠️ hex sin medir.
- **Garnet, sus guanteletes cambian 4 veces:** los del debut, los de tras regenerarse, los de latón con pinchos y los de «Change Your Mind» y la película (galería de «Abilities» de la wiki) · ✅
- **Garnet, primera forma** («The Answer»): pelo rizado casi todo azul claro con el lado izquierdo rosa fuerte; mono partido en dos · ✅ texto de la wiki.
- **Perla:** diseño del debut y diseño final (hoja n.º 9 y 10: cambian pelo y proporciones); uniforme de Homeworld de la Era 1, túnica blanca larga · ⚠️ sin medir.
- **Amatista:** traje **Purple Puma** (luchadora con máscara y capa) y un traje de fiesta · ⚠️ sin medir.

**Etiquetas que usan las IA de imagen** (Danbooru, rasgos más repetidos): Perla `forehead_jewel, short_hair, pointy_nose, pale_skin, pink_hair`; Garnet `afro, colored_skin, purple_skin, sunglasses, third_eye, thick_lips, gloves`; Lapis `blue_skin, blue_hair, crop_top, liquid_wings, hydrokinesis`; Peridot `green_skin, blonde_hair, triangle-shaped_hair, face_shield` · [Danbooru](https://danbooru.donmai.us/related_tag?query=garnet_(steven_universe)) · ✅

## Punto 16 · Ciudades, paisajes y fondos de pantalla

**Los sitios, con su luz y su hora** (paletas medidas en el punto 4):

| Sitio | Cómo es | Luz y hora | Dónde verlo |
|---|---|---|---|
| **Beach City** | pueblo costero de EE. UU. (en la costa de Delmarva): paseo de tablas, muelle, letrero «BEACH CITY» en la colina, faro en el acantilado | mañana nublada, difusa, fría (azul, verde, turquesa) | [color key oficial](https://static.wikia.nocookie.net/steven-universe/images/4/4f/Beach_City_Color_Key.jpg) 1280×720 ✅ · [mapa oficial](https://static.wikia.nocookie.net/steven-universe/images/2/24/SU-Beach_City_Map.jpg) 3626×2792 ✅ |
| **La Casa Playa** | la casa de Steven, pegada al Templo | tarde cálida por la ventana | `GG` 3:30 · hoja n.º 141 (cocina, «Volleyball») |
| **El Templo de Cristal** | montaña con forma de mujer; dentro, pasillos de cristales triangulares | tenue, con brillos de cristal | `GG` 2:00-2:50 · hojas n.º 13-14 (la Puerta) |
| **El Big Donut** | la tienda de rosquillas de Sadie y Lars | cálida, de vitrina | `GG` 1:00-1:50 · hoja n.º 107 · [modelo 3D CC BY](https://sketchfab.com/3d-models/none-b44b20b741ce4dbba2339fec366cc3c9) |
| **La playa** | arena, acantilado | atardecer: cielo crema, rosa y silueta verde oscura | `GG` 10:40-11:10 |
| **Homeworld** | el planeta de las Gemas: arquitectura geométrica gigante, naves con forma de mano, tronos | artificial, muy saturada, sin cielo | hojas n.º 102, 112 y 135 ✅ |
| **Naves gema** | pasillos verdes con paredes como raíces | **verde veneno** | `STY` 2:48-3:24 ✅ |
| **El Kindergarten** | cantera árida con agujeros con forma de Gema | ocre y naranja | hoja n.º 36 («Back to the Kindergarten»: Steven y Amatista abrazan a Peridot entre bloques de piedra, luz naranja) ✅ visto |
| **El granero** | campo abierto, silos (T5) | atardecer cálido | ⚠️ no está en las 3 hojas guardadas (la parte de imagen lo citaba de otra hoja de contacto que no se subió) |
| **Little Homeworld** | el barrio de Gemas en la Tierra de *Future*, con carteles en Gem Glyph | día claro | hoja n.º 126-128 · [fotograma 1920×1080](https://static.wikia.nocookie.net/steven-universe/images/6/6a/Little_Homeschool_259.png) |
| **La noche con aurora** | cielo verde y amarillo sobre el mar | noche mágica | hoja n.º 120 («Reunited») |
| **El vagón rojo** | techo de un vagón de tren, al atardecer | puesta de sol rosa | hoja n.º 46 («On the Run») |

**Fondos de pantalla** (de [Wallhaven](https://wallhaven.cc/), con tamaño y autor):

| Tamaño | ♥ | Qué es | Autor u origen | Enlace |
|---|---|---|---|---|
| 1920×1080 | 38 | **oficial de Cartoon Network** | [cartoonnetwork.com/backgrounds](https://www.cartoonnetwork.com/backgrounds/) | https://w.wallhaven.cc/full/73/wallhaven-73zzov.jpg |
| 1920×1080 | 35 | oficial de Cartoon Network | ídem | https://w.wallhaven.cc/full/83/wallhaven-83qlxk.jpg |
| 1920×1080 | 27 | oficial de Cartoon Network | ídem | https://w.wallhaven.cc/full/ey/wallhaven-ey5jo8.jpg |
| 4096×2291 | 31 | paisaje pintado | **@lulusketches** · [X](https://x.com/lulusketches/status/1246255713975861248) | https://w.wallhaven.cc/full/yq/wallhaven-yq8e7l.jpg |
| 2560×1600 | 24 | ilustración | **onemegawatt** · [Tumblr](http://onemegawatt.tumblr.com/) | https://w.wallhaven.cc/full/6q/wallhaven-6q6ew6.png |
| 1920×1080 | 39 | cruce de series de Cartoon Network | **hbrunatv** · [DeviantArt](https://www.deviantart.com/hbrunatv/art/VDF-02-Cartoon-Network-451673335) | https://w.wallhaven.cc/full/4y/wallhaven-4yqgjd.png |
| 1920×1080 | 40 | fantasía | ⚠️ sin origen | https://w.wallhaven.cc/full/0p/wallhaven-0pqqjp.png |
| 1920×1080 | 38 | isla con cascada, azul | ⚠️ sin origen | https://w.wallhaven.cc/full/4o/wallhaven-4ozzl7.png |
| 2048×1154 | 33 | *Future* | subido por grazielless, ⚠️ sin origen | https://w.wallhaven.cc/full/dg/wallhaven-dgqv8l.jpg |
| 2048×1153 | 27 | cielo y mar de colores | subido por grazielless, ⚠️ sin origen | https://w.wallhaven.cc/full/83/wallhaven-8318g1.jpg |

Los de «sin origen» sólo como referencia de ambiente: no se sabe quién los pintó.

**Para reconstruir en Blender:** el Big Donut ya está modelado (CC BY, Kekê). Texturas CC0 del punto 4 (Wood095, Ground054/080, Rock064).
