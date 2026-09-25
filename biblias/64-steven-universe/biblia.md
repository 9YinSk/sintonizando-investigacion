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
| **La Casa Playa** | la casa de Steven ([Beach House](https://steven-universe.fandom.com/wiki/Beach_House)) | tarde cálida por la ventana | `GG` 3:30 · hoja n.º 141 (cocina, «Volleyball») |
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

## Punto 17 · Guía para generar con IA (imagen y texto)

Hecha por el redactor con los datos de los puntos 1-16. Sirve para Firefly, Canva u otra IA de imagen, y para una IA de texto que escriba en su voz.

### Para una IA de imagen

**El estilo en una frase:** personajes de **color plano** con **línea oscura limpia**, sobre **fondos pintados a pincel**, pastel y con **grano** suave.

**Lo que nunca cambia**
- **Línea:** contorno oscuro, más grueso por fuera y más fino dentro (cejas, boca, pliegues); el grosor varía con el trazo · ⚠️ (análisis de [Isaac Gordon](https://isaacgordon50.wordpress.com/2015/10/17/steven-universe-character-style-analysis/), coincide con las hojas).
- **Sombra:** casi ninguna en los personajes; sólo con luz dramática · `estilo.py` dio «sombreado plano (cel), poca línea» en las 4 fichas medidas ✅.
- **Fondos:** pincel visible tipo gouache, colores desaturados y brillos fuertes; **silueta antes que contorno** · [Chromosphere](https://chromosphere-la.com/case-study/steven/) ✅
- **Grano** en toda la imagen, incluso en los efectos hechos por ordenador · Chromosphere ✅
- **Color:** Beach City cálida y familiar; el espacio y Homeworld, fríos y extraños (el *color script* de Elle Michalka) · ✅
- **Formas:** Garnet cuadrada, Amatista redonda, Perla cono · ✅

**Rasgos fijos de cada uno** (con los hex del punto 15):
- **Steven:** niño bajo y robusto, pelo castaño oscuro rizado, camiseta salmón `#FF5E6D` con estrella `#FFDE3F`, vaqueros `#1974A2` con vuelta, chanclas salmón, gema rosa en el ombligo. Ojos negros; **pupilas de estrella** cuando se emociona.
- **Garnet:** muy alta (2.21 m), afro cúbico violeta, piel `#A53A84`, gafas de sol, mono `#000035` con hombreras `#CD1AAE`, guanteletes `#B50535`. Tres ojos (rojo, azul y morado) si se quita las gafas. Gemas en las palmas.
- **Perla:** alta y delgadísima, piel `#F8F4E1`, nariz puntiaguda, pelo corto salmón, perla en la frente, top `#8DDACD` con estrella `#E0FF87`, lazo `#69F4E2`, falda-short `#F9D27D`. Postura de bailarina.
- **Amatista:** baja y ancha, piel `#B898CC`, pelo `#DCD3EF` hasta el suelo, top `#232229`, gema `#CF67FE` en el pecho, short `#657188` con estrellas.

**Luz**
- Día: muy lavada, casi pastel (brillo 93%, saturación 20%, `GG` 0:10).
- Atardecer: `#17251E` `#F7F6CE` `#ECD2A3` `#CD8891` (`GG` 11:00).
- Interior: cálido de tarde (`GG` 3:30).

**Encuadre:** la cara manda; el pelo y el cuerpo llevan la mirada a ella. Las fusiones y los momentos de poder, **centrados, frontales, de cuerpo entero**, con luz de abajo o de atrás · ⚠️ (análisis de fans).

**Palabras que ayudan** (en inglés, que las IA entienden mejor):
`flat colors, clean thin dark outline, no rendering, pastel gouache painted background, visible brush strokes, soft film grain, warm sunset, 2010s TV cartoon, full body, simple shapes`
Y el vocabulario de Danbooru (punto 15): `toon (style)`, `gem (steven universe)`, `colored skin`, `forehead jewel`, `star (symbol)`, `afro`, `sunglasses`, `third eye`.

**Palabras que lo estropean:** `anime`, `manga` (Danbooru tiene una etiqueta propia, `animification`, para los dibujos de estos personajes pasados a anime: es justo lo que no se quiere); `realistic`, `detailed shading`, `glossy`, `3D render`; `slim`, `thin waist`, `sexy` (adelgazar es lo que más enfada al fandom, punto 12); `speech bubble`, `chibi`, `sweat drop` (la serie no usa ese vocabulario del anime).

**Imágenes de referencia**
- **Estilo del fondo:** la [color key de Beach City](https://static.wikia.nocookie.net/steven-universe/images/4/4f/Beach_City_Color_Key.jpg) y el atardecer de `GG` 11:00.
- **Estilo del personaje:** las 4 fichas de producción del punto 15 (fondo transparente).
- **Pose:** punto 14. Las mejores: Garnet chasqueando (`STY` 2:42), Perla con la mano abierta (hoja n.º 15), Steven con la caja (`GG` 1:20), Amatista con el puño (hoja n.º 5).
- **Grupo:** hoja n.º 47 (Garnet, Amatista y Steven), n.º 42 (Greg, Amatista y Steven en el sofá).

**Prompt de ejemplo** (fondo sin personaje, para meter luego el recorte con `v3/integrar.py`):
> `seaside boardwalk town at sunset, pastel gouache painted background, visible brush strokes, soft film grain, cream sky #F7F6CE, pink clouds #CD8891, dark green cliff silhouette #17251E, warm sand #ECD2A3, no characters, 2010s TV cartoon background`

### Para una IA de texto

**Reglas de la voz latina** (doblaje venezolano, Etcétera Group):
- **Tutean**: «Para que existieras tú», «Si tú nos separas» (Garnet.ogg) · ✅
- Frases enteras, sin jerga de ningún país. Exclamaciones con ¡! al empezar la frase.
- **Nada de onomatopeyas escritas** tipo cómic: la serie no las usa.

| Personaje | Cómo escribirle | Qué evitar |
|---|---|---|
| **Steven** | frases cortas y cálidas; consuela con cosas de todos los días (la comida, el pueblo); se entusiasma; a veces habla de sí mismo en tercera persona | el sarcasmo, el rencor |
| **Garnet** | pocas palabras; **afirmaciones, nunca preguntas**; habla de unión y de fusión; seguridad tranquila | preguntar, dudar, gritar |
| **Amatista** | ruidosa, con bromas y comida; suelta palabras en español de broma («¡No, mi torta!»); cuando se enfada, grita sobre sí misma | la solemnidad |
| **Perla** | explica largo y con palabras cultas; se dirige a Steven por su nombre («¡Oh, Steven!»); un poco por encima de los humanos; se agobia cuando algo se desordena | la comida, el desorden |

**Frases reales, por emoción** (✅ = oída en latino con `voz.py`; EN = original en inglés de las fichas, sin versión latina en las partes):

| Emoción | Frase | Quién | Fuente |
|---|---|---|---|
| **Alegre, orgullosa** | «Cuando dos gemas se combinan crean algo más grande que la suma de sus partes, por eso soy tan genial» | Garnet | Garnet.ogg 0:00 ✅ |
| Alegre | «Who needs to go see movies when you've got MAGIC?» | Amatista | *Guide to the Crystal Gems*, hoja n.º 2 · EN |
| Alegre (gag) | «Cheeseburger backpack!» (cantado en bucle) | Amatista y Perla | punto 12 · EN |
| **Enfadada** | «¡Nunca pedí ser lo que soy! ¡Nunca pedí ser creada!» | Amatista | Amatista.ogg 0:00 ✅ |
| Enfadada (broma) | «¡No, mi torta!» | Amatista | Trivia, en español en el original ✅ |
| **Explicando** | «¡Oh, Steven! Los humanos tienen una vida tan corta, aburrida e insignificante que inventan historias para sentir que forman parte de algo más grande» | Perla | Perla.ogg 0:00 ✅ |
| Explicando | «…no entienden que es una compleja red de fuerzas interrelacionadas que nadie puede controlar» | Perla | Perla.ogg 0:07 ✅ |
| **Animando** | «Este no es el mismo mundo que te mantuvo atrapada, ya no lo es» · «Y sé que no se siente como un hogar, pero tal vez eso pueda cambiar» | Steven | Steven.ogg 0:13 · 0:17 ✅ |
| Animando (cantado) | «Si tú nos separas nos uniremos, y siempre seremos mejores que tú» | Garnet | Garnet.ogg 0:25 ✅ |
| **Triste** | «Para que Amatista pudiera ser ella, para que Perla fuese libre y para que pudiéramos estar juntas» · «Para que existieras tú» | Garnet | Garnet.ogg 0:12 · 0:18 ✅ |
| Triste | «Sí, pero nada permanece en la tierra, las cosas siempre están cambiando» | Steven | Steven.ogg 0:00 ✅ |

⚠️ No hay frase latina de Perla triste en las partes («It's Over, Isn't It» no se transcribió en español).

**Vocabulario de la serie** (lo que un fan reconoce):
- En latino, oído: **Gemas de Cristal**, **Diamante Rosado** (Garnet.ogg 0:06; ⚠️ transcrito por Whisper), **Rose Cuarzo**, **Lapislázuli**, **Diamante Amarillo / Azul / Blanco**, **Ópalo**, **Cuarzo Arcoíris 2.0**, títulos «Escape de la Prisión», «El Señor Greg», «Taladro Gema», «Conoce tu Fusión».
- En inglés, sin versión latina comprobada (⚠️ no usarlos traducidos a ojo): *poof*, *shatter* (fragmentar), *bubble* (burbujear), *Homeworld*, *corrupted Gem*, *Kindergarten*, *Cheeseburger Backpack*, *Cookie Cat*, *Big Donut*, *Beach City*.

**Vocabulario de gestos para la IA de imagen** (lo que sí sale en la serie):
- **ojos de estrella** = emoción y admiración (`STY` 0:54).
- **una lágrima brillante con los ojos muy abiertos** = tristeza contenida (`IOI` 2:10).
- **Steven todo rosa y brillando** = rabia o descontrol (hoja n.º 142; escudo de hexágonos rosa, n.º 153).
- **destello geométrico en las manos** = sacar el arma (`GG` 3:30).
- **burbuja rosa translúcida** = guardar algo o a alguien sin hacerle daño (`STY` 4:09).
- **nube de humo y la gema sola** = *poof*.

## Punto 18 · Estilo y técnica: cómo replicarlo

**Cómo se hizo la serie**
- **Guion gráfico en *Toon Boom Storyboard Pro*** · [Toon Boom](https://www.toonboom.com/top-animation-news-the-dragon-prince-steven-universe-and-more) + [Mundo Toon](https://www.mundotoon.net/en/toon-boom-the-software-behind-the-worlds-most-acclaimed-animations/) · ✅
- **Animación final en Corea del Sur**: los estudios **Sunmin Image Pictures** y **Rough Draft Korea** · [Sunmin](https://steven-universe.fandom.com/wiki/Sunmin_Image_Pictures) + [Rough Draft Korea](https://steven-universe.fandom.com/wiki/Rough_Draft_Korea) + Wikipedia · ✅
- ⚠️ Que se entintara y coloreara en *Toon Boom Harmony* **no está confirmado** (sólo hay tutoriales de fans).
- **Secuencias de la película** (intro, portada del vinilo): **Chromosphere** usó **After Effects** para componer y **Blender** para piezas 3D (la gema que gira en el *teaser*). El libro de cuentos se montó en After Effects. Mezclaron 2D y 3D en la misma escena · [Chromosphere](https://chromosphere-la.com/case-study/steven/) · ✅
- **El agua**: probaron animarla a mano y lo descartaron; usaron formas de After Effects con deformación de malla y **ruido en el alfa**, para que quedara geométrica y **con grano** · Chromosphere · ✅
- **Diseño por formas (Bauhaus y Kandinsky)**: Garnet = cuadrado («la más estable»), Amatista = círculo («fluida»), Perla = cono («fija en su orientación») · del artbook *Art & Origins*, resumido en [Gizmodo](https://gizmodo.com/the-coolest-details-from-steven-universes-gorgeous-new-1797017304) y [Wikipedia](https://en.wikipedia.org/wiki/Steven_Universe) · ✅
- **Guiones de color** de la directora de arte **Elle Michalka**: cálido y brillante al empezar una secuencia, frío y oscuro al acabar; lo conocido de Beach City frente a lo raro del espacio · Chromosphere · ✅

**Línea, color y sombra** (medido y visto):
- Personajes: color plano, una sola sombra si acaso; línea oscura, gruesa fuera y fina dentro · ✅ `estilo.py` + ⚠️ el análisis de la línea es de un blog.
- Fondos: pincel visible, desaturados, brillos cegadores, silueta antes que contorno · ✅
- Degradados: sólo en atardeceres, gemas y luz; se mezclan a pincel, no con la herramienta de degradado · ⚠️ tutorial de fan ([Redbubble](https://blog.redbubble.com/2019/07/how-to-steven-universe-characters-anushbanush/)).

**Cómo replicarlo en Photoshop** (receta del redactor con lo de arriba; ⚠️ recomendación, no dato de producción):
1. **Capas:** Línea · Color plano · Sombra plana (Multiplicar, un solo tono, sin degradado) · Brillos sueltos (Trama o Superponer) · **Grano** (ruido monocromo al 3-6%, Superponer).
2. **Pinceles:** uno duro al 100% sin textura para el contorno, con grosor por presión; uno fino para los detalles de dentro.
3. **Efectos de gema y energía:** pincel de mezcla suave con dos tonos; nunca un degradado recto.
4. **Fondo:** pintar a pincel con papel de fondo (Paper006, punto 19) y bajar la saturación; dejar un brillo fuerte.

**Cómo replicarlo en Blender**
- **Contorno:** Solidify invertido (normales hacia fuera, material negro) o **Line Art/Freestyle** para afinar la línea con la cámara. Mezclar render de Blender con línea y color hechos después en Photoshop **es lo que hizo el propio estudio** (Chromosphere) · ✅
- **Sombreado plano:** *Shader to RGB* → *Color Ramp* de 2-3 pasos en «Constant» (bordes duros).
- **Luz:** una luz de área grande y suave y un relleno tenue del color contrario (cálido y frío, como los guiones de color). Render en **Eevee**; el grano, después, en composición.
- **Modelos libres:** el **Big Donut** (Kekê, CC BY) y el **grupo de las 4 Gemas + Spinel** (RazyBerry, CC BY) en Sketchfab (punto 3). ⚠️ No se comprobó si traen esqueleto (*rig*); no se encontró un *rig* oficial ni libre.

**Encuadres típicos**
- La cara es el centro de casi todo plano de personaje · ⚠️ una fuente.
- Fusiones y transformaciones: plano heroico, simétrico, frontal, cuerpo entero, luz de abajo o de atrás · ⚠️ visto en las hojas, sin fuente de producción.
- Emoción íntima: primer plano, un solo personaje recortado contra un fondo desenfocado (`IOI` 2:10: Perla con la ciudad en *bokeh* azul-violeta) · ✅ visto.
- Momento de equipo: plano general con las cuatro siluetas distintas (`GG` 10:20, `GG` 10:40-11:10).

## Punto 19 · Texturas 2D

La serie tiene dos capas: **personajes lisos** (color plano) y **fondos con pincel y grano**. No hay tramas de manga en la animación.

| Capa | Cómo es en la serie | Equivalente libre | Licencia |
|---|---|---|---|
| **Papel y grano de fondo** | pincelada tipo gouache en nubes, hierba y rocas ([color key](https://static.wikia.nocookie.net/steven-universe/images/4/4f/Beach_City_Color_Key.jpg)) | **Paper006** · https://ambientcg.com/view?id=Paper006 | CC0 ✅ |
| **Grano de película** | presente hasta en los efectos por ordenador (Chromosphere) | ruido monocromo en Photoshop (punto 18) | propio |
| **Facetas de gema** | facetas triangulares con un **brillo de estrella de 4 puntas** en el centro; la de Amatista en 12 versiones (hojas n.º 17-28), la rosa pentagonal de Rose y Steven (n.º 158-159) | no hay una CC0 igual; vectores de cristal facetado en Vecteezy | ⚠️ licencia por archivo |
| **Escudo de hexágonos** | el escudo del estado rosa, panal de hexágonos lila (hoja n.º 153) | dibujarlo con la cuadrícula de hexágonos de Illustrator o Photoshop | propio |
| **Tela vaquera** | shorts de Amatista, vaqueros de Steven | **Fabric081C** · https://ambientcg.com/view?id=Fabric081C | CC0 ⚠️ genérica |
| **Estrellas** | la estrella de 5 puntas `#FFDE3F` de Steven se repite en los guanteletes de Garnet, el escudo y el top de Perla; estrellas negras en el short de Amatista | dibujarla (forma simple) | propio ✅ |
| **Trama de cómic** | puntos de *halftone* en algunas portadas de BOOM! ([#1 de 2017](https://static.wikia.nocookie.net/steven-universe/images/4/45/Boom_2017_001_A.jpg)) | pinceles de *halftone* de Clip Studio Assets o Krita | ⚠️ sin comprobar un paquete CC0 |
| **Escritura del mundo** | **Gem Glyph** en carteles y columnas | las [notas de Steven Sugar](https://static.wikia.nocookie.net/steven-universe/images/2/27/The_Reef_gem_glyph.webp) (629×617) y el [banner de Homeworld](https://static.wikia.nocookie.net/steven-universe/images/7/7d/Homeworld_banner_zoomed_in.PNG) (366×516) como modelo | © CN, sólo referencia |
| **Emblema** | la **estrella de 5 gemas** de la Puerta del Templo (rosa, crema, morada, roja, azul) | [Better Temple Door](https://static.wikia.nocookie.net/steven-universe/images/e/eb/Better_Temple_Door.png) (1953×3105) como modelo | © CN, sólo referencia |

- **Texturas reales** (madera, arena, roca) en el punto 4. **Modelos 3D** en el punto 3.
- ⚠️ **No hay logo oficial en alta** en la wiki (sólo el favicon). Para la cabecera, usar la letra **Crystal Universe** (punto 5) o la estrella de Steven.
- ⚠️ No se encontró un paquete de pinceles CC0 de gouache ni de facetas: hay que comprobar la licencia de cada uno antes de usarlo.

## Punto 20 · Gustos y detalles

De la sección «Trivia» de cada ficha de la wiki, leída entera · ✅ salvo que se diga.

| | **Steven** | **Garnet** | **Amatista** | **Perla** |
|---|---|---|---|---|
| **Cumpleaños / edad** | **15 de agosto** (el de Steven Sugar, hermano de la autora, en quien se basa); Leo; su piedra de nacimiento es el peridoto | — | unos **5500 años**: la más joven de las Gemas de Cristal originales | unos **8000 años** (por un diálogo) |
| **Altura** | **1.68 m y 65.8 kg** a los 16 (el único con medidas oficiales) | **2.21 m** (7'3", tuit de Cartoon Network para la NBA) | baja | alta |
| **Comida** | cocina muy bien; le gusta la **sopa de tomate** («Bluebird»); los **Cookie Cat** (abraza la caja en `GG` 1:20) | casi no come, «pero le gusta a veces»; **café** en el desayuno («Future Vision») | **come de todo** y disfruta la digestión | **odia comer** («el proceso digestivo me da asco», «Fusion Cuisine»); le gusta el **té** y hacer pastel, no comerlo |
| **Aficiones** | dibujar (mal, es un chiste), cocinar, videojuegos (Nintendo 64, GameCube, Game Boy, PS2; *Zelda: Wind Waker*, *Animal Crossing*), su canal «TubeTube» de cocina | tocar el **keytar**; su música favorita es la de Estelle, su actriz | la lucha libre (Purple Puma), dormir, la **batería** | **colecciona espadas**; esgrima; baile |
| **Lo que odia** | los **taparrabos** («Gem Heist»); es alérgico al polen («Warp Tour») | — | que le den órdenes | el desorden; los **chalecos salvavidas** le parecen «ridículos» |
| **Lo que siempre lleva** | el **ukulele**; la gema en el ombligo; el escudo | los **guanteletes** y las **gafas** | el **látigo** | la **lanza** |
| **Cómo se ve a sí mismo** | quiere ayudar a todos y calla lo suyo («Prickly Pair») | segura; es una relación, no sólo una Gema | **inferior** a las otras (Kindergarten) | «inútil» sin alguien a quien seguir |
| **Detalles** | se marea con los giros; habla de sí en tercera persona | **nunca pregunta**; heterocromía | **orina en el mar** «porque es divertido»; su cuarto es «el más parecido a la vida real de Rebecca Sugar»; habla español | **ambidiestra**; no tiene carné de conducir ni papeles |

Fuentes: [Steven](https://steven-universe.fandom.com/wiki/Steven_Universe_(character)#Trivia) · [Garnet](https://steven-universe.fandom.com/wiki/Garnet#Trivia) · [Amatista](https://steven-universe.fandom.com/wiki/Amethyst#Trivia) · [Perla](https://steven-universe.fandom.com/wiki/Pearl#Trivia).

- **La ficha oficial de Amatista** en *Guide to the Crystal Gems* (hoja n.º 2): Species Gem · Gem Type Quartz · Alignment Crystal Gem · pelo lavanda pálido · leggings con estrellas en las rodillas y camiseta ancha · gema en el pecho · arma el látigo · frase favorita «Who needs to go see movies when you've got MAGIC?» · ✅ visto.
- ⚠️ Faltan: cumpleaños de las tres Gemas (no aparecen), altura exacta de Amatista y Perla, y comida favorita concreta de Garnet.
- **Favoritos del equipo:** Garnet es la de Ian Jones-Quartey; Steven, la de Joe Johnston · ✅

## Punto 21 · Por qué la aman

**Premios y notas**
- **Peabody** (2019) y **GLAAD Media Award** a mejor programa infantil y familiar (2019): la **primera serie animada** en ganar un GLAAD. 5 nominaciones al Emmy y 5 a los Annie · [BroadwayWorld](https://www.broadwayworld.com/bwwtv/article/STEVEN-UNIVERSE-Wins-GLAAD-Media-Award-for-Outstanding-Kids-Family-Programming-20190329) + [IMDb](https://www.imdb.com/title/tt3061046/awards/) · ✅. Foto del discurso de los Peabody (CC BY-SA 3.0, 1600×900) · https://upload.wikimedia.org/wikipedia/commons/1/15/Steven_Universe_-_78th_annual_Peabody_Awards_acceptance_speech.jpg
- **100%** de la crítica (49 reseñas) y **84%** del público (más de 500 votos) en [Rotten Tomatoes](https://www.rottentomatoes.com/tv/steven_universe), comprobado el 25-sep-2026 · ✅
- El disco *Volume 1*, **n.º 1 en iTunes** y en la *Billboard 200* (punto 9) · ✅

**Las razones, en concreto**
1. **Representación LGBT pionera** en la tele infantil: el compromiso y la boda de Rubí y Zafiro; Stevonnie leída como no binaria · [Wikipedia](https://en.wikipedia.org/wiki/Cartoon_Network_and_LGBTQ_representation) + [Autostraddle](https://www.autostraddle.com/steven-universe-and-the-importance-of-all-ages-queer-representation-281482/) · ✅
2. **Cuerpos diversos**: Amatista, Garnet y Rose, anchas, son heroínas fuertes. Muchas personas gordas se vieron por fin representadas · [The A.V. Club](https://www.avclub.com/how-steven-universe-s-fat-bodies-helped-me-draw-my-own-1845830394) · ⚠️ una fuente central.
3. **Temas adultos en 11 minutos**: duelo, trauma, identidad, salud mental, sin tratar al niño como tonto · ⚠️ resumen de reseñas.
4. **La música**: más de 38 canciones cantadas por Steven · ✅

**Con quién se identifica el público:** con **Perla** (la más dibujada: perfeccionista y rota, punto 7), con **Amatista** (el público gordo y quien se siente «defectuoso») y con **Steven de *Future*** (el trauma y la terapia) · ⚠️ interpretación del redactor con los datos de los puntos 7, 13 y 25.

### Las escenas que hacen llorar

**«It's Over, Isn't It»** (T3, «Mr. Greg», ep. 86) · `IOI` · ✅ visto
- **Qué pasa:** Perla, con esmoquin, recuerda un baile con Rose (una silueta azulada entre pétalos) y canta que sigue enamorada de quien ya no puede quererla.
- **Minuto:** 2:00 mira abajo con una rosa; **2:10 una lágrima** baja por su mejilla, ojos muy abiertos y brillantes.
- **Cómo está dibujada:** noche azul y violeta, la ciudad desenfocada detrás (*bokeh*), Perla sola en primer plano recortada contra el cielo. Encuadre íntimo que la aísla.
- **Por qué duele:** es el amor no correspondido de alguien que se cree «inútil» sin su líder (punto 13).
- **Reacción:** de los temas más escuchados del disco · ⚠️ (el hilo de Reddit de «canción más icónica» habla más de «Love Like You»).

**«The Answer»** (animatic oficial, `ANS`) · ✅ visto
- 8:56-9:12 Rubí y Zafiro se dan la mano por primera vez; 11:04-11:20 brillan y nace Garnet. Es el origen de la pareja: llora quien lo ve por lo que significa, no por tristeza.

⚠️ No se miraron otras escenas que suelen hacer llorar (el final de la T5, *Future*): el hilo «la mejor escena del final» tiene 1090 votos, pero no se vio.

### Las que hacen gritar de emoción
- **«Stronger Than You»** (`STY`): 2:42 Garnet **chasquea los dedos** y sonríe; 3:09-3:15 el puñetazo en vuelo; 4:09 Jasper encerrada en la burbuja rosa. Suena la canción de Estelle. Nave verde veneno, acción en planos cortos · ✅ visto.
- En Reddit: «Rose burlándose de White Diamond es icónico» (1576 votos) · ⚠️ no visto.

### Las que hacen reír
- **«Cheeseburger Backpack»** (T1-E3): Amatista y Perla cantando el nombre de la mochila · ✅ (punto 12)
- **Amatista** con Cookie Cat (`GG` 4:00) y su «¡No, mi torta!» en español.

## Punto 22 · Fan dubs y comunidad hispana

⚠️ **Las vistas no se pudieron contar**: YouTube pide iniciar sesión desde el servidor. Los enlaces están confirmados por el buscador.

**Fandubs en español latino** (YouTube):

| Qué es | Escena | Enlace |
|---|---|---|
| «Steven Universe Future: Volleyball (Español Latino) [FANDUB]» | capítulo de *Future* (el de Steven rosa, hoja n.º 142) | https://m.youtube.com/watch?v=kh5FAs2TpC4 |
| «Todo está bien (capítulo 18 completo) \| Español Latino Fandub \| Steven Universe Futuro» | capítulo 18 de *Future*, entero | https://www.youtube.com/watch?v=pEFpBpEWyaw |
| «Steven Universe Comic: STEVEN SE CORROMPE I (Fandub Español Latino)» | cómic doblado | https://www.youtube.com/watch?v=iKEvhwwgEc4 |
| «Steven universe cómics -fandub español latino-» | cómic doblado | https://www.youtube.com/watch?v=ocLwOWl2Wjg |
| «REESCRITO (FANDUB ESPAÑOL LATINO)» | cómic doblado | https://www.youtube.com/watch?v=_hZUkaCHUlA |
| «Steven Universe: La Película TRAILER I (Fandub Español Latino)» | tráiler de la película | https://www.youtube.com/watch?v=CDlMPzFdlvc |
| «Steven vs Bill Cipher Fandub Español Latino (Steven Universe X Gravity Falls)» | cruce con *Gravity Falls* | https://www.youtube.com/watch?v=dua-aXMuqG0 |

**Lo que dice de la comunidad:** no sólo doblan la serie, **doblan el cómic oficial** (que no tiene doblaje) y *Future*, y cruzan series. Es justo lo que hace un servidor de doblaje: sirve de ejemplo para #📂・proyectos o #🎯・reto-de-la-semana.

**Covers del opening en español**
- Versión oficial: **«Somos las Gemas de Cristal»**, cantada por Leisha Medina · letra en [Letras.com](https://www.letras.com/steven-universo/somos-las-gemas-de-cristal-opening-extendido/) · ✅
- Covers de fans: https://www.youtube.com/watch?v=qiG8AciRXzo · https://www.youtube.com/watch?v=-TjVIyyyFW0 · ⚠️
- **En directo**: versión extendida en un concierto de la convención **Senka** (Mérida, Yucatán, México, 28 de mayo; año sin confirmar) · https://www.youtube.com/watch?v=AYhpxBTeb6A · ⚠️
- Montaje de fans del intro con *My Little Pony*, en español latino (0:34) · https://www.dailymotion.com/video/x3klev8 · ⚠️ no visto.

**Oficial en español que la comunidad usa:** los clips doblados de Dailymotion (`TIO`; «Stevonnie (Latino) — Solos y Juntos») son fáciles de recortar para memes o retos; y el disco de la película en español (punto 9).

⚠️ No encontré cuentas de TikTok dedicadas a fandubs de la serie (se buscó «Steven Universe fandub tiktok español»): sólo clips sueltos oficiales.

## Punto 23 · Colaboraciones y cruces

**Juegos de otras marcas**
- **Brawlhalla** (Ubisoft, gratis): evento «Steven Universe Event» del **4-dic-2019** (parche 3.53). **Garnet, Amatista, Perla y Stevonnie** jugables como *Epic Crossovers*, con animación de entrada y armas nuevas; se quedaron para siempre · [ComicBook](https://comicbook.com/gaming/news/brawlhalla-steven-universe-crossover-fighters-crystal-gems/) + [Brawlhalla Wiki](https://brawlhalla.wiki.gg/wiki/Steven_Universe_Event) · ✅. Arte: [guanteletes de Garnet](https://static.wikia.nocookie.net/steven-universe/images/e/eb/Garnet%27s_Gauntlets_%28Brawlhalla%29.png) 1280×1280 · [lanza de Perla](https://static.wikia.nocookie.net/steven-universe/images/7/7f/Pearl%27s_Spear_%28Brawlhalla%29.png) 1280×1280.
- **MultiVersus** (Warner Bros. Games): **Steven y Garnet** jugables desde el anuncio del **18-nov-2021** · [Business Wire](https://www.businesswire.com/news/home/20211118005502/en) + [wiki del juego](https://multiversus.fandom.com/wiki/Steven_Universe) · ✅
- **Cartoon Network: Battle Crashers** (2016): Steven jugable (punto 11) · ✅

**Colaboración educativa**
- **Adafruit × Cartoon Network**: kit para **construir los guanteletes de Garnet** con luces y sonido programables (Circuit Playground) · [Adafruit](https://learn.adafruit.com/cartoon-network-makecode-garnets-gauntlets-from-steven-universe) · ✅. Es un objeto real de la serie hecho de verdad: buena referencia de volumen.

**Eventos**
- **Exposición Steven Universe / Adventure Time** en Gallery Nucleus, con Cartoon Network: portadas variantes del cómic, láminas, firma y **actuación en directo de Rebecca Sugar** · [Gallery Nucleus](https://gallerynucleus.com/events/441/exhibition) + [Wendi Chen](https://www.wendichen.com/events/steven-universe-gallery-nucleus) · ✅
- **San Diego Comic-Con**: paneles del reparto y del equipo desde 2013 · [Fandom](https://steven-universe.fandom.com/wiki/San_Diego_Comic-Con) · ✅
- ⚠️ No encontré cafés temáticos ni zonas en parques (se buscó «Steven Universe pop-up cafe», «theme park official area»).

**Figuras oficiales (su pose es una referencia 3D)**
- **Funko Pop!**: 16 figuras. Primera oleada (14-dic-2015): Steven con su camiseta de estrella, **Garnet con gafas**, Amatista con la gema asomando y **Perla en pose de bailarina con los brazos abiertos**. Segunda oleada en marzo de 2017; variantes que brillan en la oscuridad (Hot Topic) · [Toynk](https://www.toynk.com/blogs/news/steven-universe-funko-pop-list) + [Cardboard Connection](https://www.cardboardconnection.com/funko-pop-steven-universe-figures) · ✅
- Foto de un Funko mini de Steven (Sergey Galyonkin, CC BY-SA 2.0, 1022×1024) · https://live.staticflickr.com/4279/34589194024_b908708a78_b.jpg

**Cosplay bien hecho**
- **Garnet de Carbon Costume**: guanteletes de **goma EVA** (un rollo de 7"×18" para el cilindro del puño, cola de contacto, secado de 30 min a 24 h) y mono azul marino con hombreras · [Carbon Costume](https://carboncostume.com/make-your-own-garnet-from-steven-universe/) · ✅
- Fotos con licencia libre (Openverse): Garnet en Sakura-Con 2016 (camknows, CC BY-NC-SA) · https://live.staticflickr.com/1536/25995790691_274aa59caf_b.jpg · Gemas *steampunk* (greyloch, CC BY-NC-ND) · https://live.staticflickr.com/4722/39737153114_29c452a569_b.jpg · Lapis (greyloch) · https://live.staticflickr.com/1599/24783048900_1d8585d39a_b.jpg · Blue Diamond (timz2011, CC BY-NC-SA) · https://live.staticflickr.com/65535/52127164069_c6e47a4080_b.jpg · Spinel (timz2011) · https://live.staticflickr.com/65535/49056594447_412af1e947_b.jpg · Amatista de LEGO hecha por fans (BRICK 101, CC BY-NC) · https://live.staticflickr.com/4183/34451032102_542dc526da_b.jpg

**Cruces dentro de Cartoon Network**
- Promos con *Power Rangers: Dino Charge* y *Hora de aventura: Estacas* (las únicas veces que Steven se dobló en México, punto 8) · ✅
- Rebecca Sugar viene de *Hora de aventura* (punto 24).

## Punto 24 · Obras parecidas

**Influencias que reconoce Rebecca Sugar** ([CBR](https://www.cbr.com/anime-that-influenced-steven-universe/) y [Wikipedia](https://en.wikipedia.org/wiki/Steven_Universe)):
- ***Revolutionary Girl Utena*** — la más directa: la esgrima de Perla, la Sky Arena (copia el duelo «End of the World»), Rose desenvainando en «Lion 2: The Movie», el traje de Mega Perla · ✅ dos fuentes.
- ***Sailor Moon*** — un tomo del manga en la estantería de Steven («House Guest»); la transformación de Spinel imita la de Usagi; Jasper sacando el arma en «Jail Break» copia el Moon Rod · ✅
- ***Neon Genesis Evangelion*** — la fusión Alexandrita («Fusion Cuisine», «Super Watermelon Island») y la escena de felicitación de «The Test» · ⚠️ una fuente.
- ***Dragon Ball Z*** — la fusión; las naves como cápsulas saiyan; Garnet quitándose peso en «Garnet's Universe» (Piccolo); el traje de Connie en «Sworn to the Sword» (Gohan) · ⚠️
- ***Gurren Lagann*** (las gafas de Garnet y Peridot al final de la T5; el taladro de Spinel) · ***Capitán Harlock*** (Lars pirata espacial) · *Kiki*, *Initial D* («Beach City Drift»), *Akira* (Connie derrapando sobre León), el cuento de Junji Ito *El enigma de la falla Amigara* · ⚠️ una fuente cada una.
- ***Los Simpson*** y ***Conan, el niño del futuro*** (Miyazaki, 1978), como influencia del tono · ⚠️ resumen de Wikipedia.
- **Rebecca Sugar viene de *Hora de aventura***: *storyboard* desde la T1, nominada al Emmy y al Annie; la dejó a principios de 2013 para su serie · [Wikipedia](https://en.wikipedia.org/wiki/Rebecca_Sugar) + [Fandom](https://steven-universe.fandom.com/wiki/Rebecca_Sugar) + TV Tropes · ✅

**Series de tono parecido** ([ScreenRant](https://screenrant.com/steven-universe-shows-watch-if-miss/) y [Ranker](https://www.ranker.com/list/what-to-watch-if-you-love-steven-universe/watchworthy), ⚠️ listas de opinión): *The Owl House*, *Gravity Falls*, *Over the Garden Wall*, *Star vs. las fuerzas del mal*, ***She-Ra y las princesas del poder*** (la más citada), *The Dragon Prince*, *Amphibia*, *Summer Camp Island*, *Hilda*, *El increíble mundo de Gumball*, *OK K.O.!*

**Otras láminas del servidor que se le parecen** (para no repetir ideas):
- **14 *Hora de aventura*** (#musica-nueva): mismo origen y tono agridulce de Cartoon Network. Su biblia ya cita «Drift Away» de Steven Universe (comprobado en `biblias/14-adventure-time-hora-de-aventura/biblia.md`) · ✅. No repetir allí la idea de «canción de Steven».
- **38 *Sailor Moon***: propone 🎲 Juegos, #eventos y #general-doblaje. Steven Universe no debe copiar su pose de **transformación** (es el préstamo reconocido).
- **29 *Sing*** propone #🎵・canto; **58 *Encanto*** propone #🪪・presentaciones; **17 *Arcane*** y **78 *Vinland Saga*** piden #📂・proyectos. Son sólo notas (decisión del dueño del 25-sep).
- **63 *Las guerreras K-pop***: mismo fondo (un grupo que canta y pelea con la música como arma). ⚠️ Su biblia aún no está escrita (sólo tiene `partes/`): no se pudo comprobar qué concepto propone. Si también va a #canto, diferenciar: aquí la música es **íntima** (ukulele, atardecer), no de escenario.

## Punto 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo en cinco líneas** ([Gems](https://steven-universe.fandom.com/wiki/Gems), ✅):
1. Las Gemas son alienígenas que **nacen adultas** de máquinas (Inyectores) en los Kindergartens; ya saben todo lo de su tipo.
2. **Homeworld** es un imperio de **castas por tipo de piedra**, gobernado por las Diamantes. Fusionarse con otro tipo está mal visto.
3. Hace **5750 años** Rose Cuarzo lideró una rebelión en la Tierra. Al irse, Homeworld lanzó una luz que **corrompió** a casi todas las Gemas que quedaban: son los monstruos.
4. **Fusionarse** es un vínculo: dos o más Gemas bailan y se vuelven un solo cuerpo más grande. En Homeworld sólo se permite entre iguales y para pelear.
5. Las Gemas **no tienen género binario**: el femenino es una convención (Rebecca Sugar, [AMA de Reddit](https://www.reddit.com/r/IAmA/comments/2e4gmx/)).

**La historia por arcos** ([Wikipedia](https://en.wikipedia.org/wiki/List_of_Steven_Universe_episodes), ✅):
- **T1 (2013-15):** Steven y las Gemas de Cristal protegen Beach City. Lapis («Mirror Gem», «Ocean Gem») trae la primera amenaza de Homeworld; Peridot y Jasper llegan en «Jail Break» (Garnet canta «Stronger Than You»).
- **T2 (2015-16):** Peridot pasa de enemiga a aliada. El **Cluster**, una Gema gigante de fragmentos en el centro de la Tierra, podría destruirla. «Cry for Help»: Perla ocultaba cosas.
- **T3 (2016):** Steven encierra el Cluster en una burbuja. Llega Bismuto (quería fragmentar enemigas). Aparece «It's Over, Isn't It».
- **T4 (2016-17):** Yellow y Blue Diamond vienen a la Tierra. Steven se entrega y lo llevan a Homeworld. Conoce a White Diamond.
- **T5 (2017-19):** el gran giro de «A Single Pale Rose»: **Rose Cuarzo era Diamante Rosa** disfrazada. «Change Your Mind»: Steven convence a las Diamantes de reformar Homeworld.
- **La película (2019):** dos años después; **Spinel**, abandonada por Diamante Rosa hace 6000 años, ataca la Tierra con un arma que borraría la vida.
- ***Future* (2019-20):** epílogo sobre la **salud mental** de Steven: trauma, poderes que se desbordan con sus emociones, terapia. Termina en «The Future».
- ⚠️ Detalle capítulo a capítulo sin cruzar con la [cronología de Fandom](https://steven-universe.fandom.com/wiki/Timeline).

**Emblemas**
- **La estrella de cinco gemas** de la Puerta del Templo: rosa (Rose/Steven), crema (Perla), morada (Amatista), roja (Rubí) y azul (Zafiro). **Es el emblema de las Gemas de Cristal** · [Crystal Temple](https://steven-universe.fandom.com/wiki/Crystal_Temple) + hojas n.º 13-14 · ✅
- **El logo de las Diamantes**: un rombo partido en cuatro, Blanca arriba, Amarilla a la izquierda, Azul a la derecha, Rosa abajo. **Tras la película se invierte** (Rosa/Steven arriba, Blanca abajo): la Era 3 cambió el poder · [Gem Glyph](https://steven-universe.fandom.com/wiki/Gem_Glyph) · ✅
- **La estrella amarilla** de Steven (`#FFDE3F`), repetida en guanteletes, escudo y ropa (punto 19).

**Gem Glyph, la escritura de las Gemas** · [Gem Glyph](https://steven-universe.fandom.com/wiki/Gem_Glyph) ✅
- Es **logográfica** (cada signo es una idea), no un alfabeto. La cuida **Steven Sugar**, hermano de la autora y diseñador de fondos.
- Un **rombo con una raya** arriba, abajo o a un lado dice de qué Diamante se habla (la raya copia su sitio en el logo). Palabras de Rebecca Sugar: «A line is placed above, below, or next to a diamond shape to indicate which Diamond is being referred».
- Números del 1 al 8 descifrados (el 1 es un cuadradito; el 2 y el 3, columnas de dos y tres) · ⚠️ una fuente (notas de Steven Sugar en el artbook *End of an Era*).
- En *Unleash the Light* es **una letra real**: sustitución letra a letra del inglés.

**Objetos icónicos**
- **La espada y el escudo de Rose**; el escudo (rosa, con estrella) lo hereda Steven.
- **León**, el león rosa de Rose: guarda cosas dentro de su melena (un bolsillo a otra dimensión) (hojas n.º 109, 122).
- **Las burbujas**: las Gemas encierran objetos o Gemas corruptas en burbujas de color y las guardan en el Templo. El gesto de «neutralizar sin matar».
- **El Comunicador de las Diamantes**: octaedro con una cara por Diamante; proyecta una pantalla para hablar (punto 6).
- **La Mochila Hamburguesa** (*Cheeseburger Backpack*), el **ukulele** de Steven y los **Cookie Cat**.
- **El Cluster**: manos y brazos gigantes que salen de la tierra y del mar · [The Cluster](https://steven-universe.fandom.com/wiki/The_Cluster) ✅
- **El Kindergarten**: Inyectores clavados en la roca; cada Gema nace con un código tipo «Facet-5 Cut-8XM» · [Kindergarten](https://steven-universe.fandom.com/wiki/Kindergarten) ✅

**Vocabulario que un fan reconoce al instante**
- ***Poof***: el cuerpo se deshace en humo y queda la gema; se recupera. ***Shatter***: romper la gema, la muerte de verdad, el gran tabú. ***Regenerate***: volver con un cuerpo nuevo (a veces con ropa nueva). ***Corrupted***: Gema convertida en monstruo. ***Off Colors***: Gemas «defectuosas» para Homeworld (T5) · ⚠️ no se abrió su página. ***The Famethyst***: las Amatistas del mismo Kindergarten que la nuestra · ⚠️
- **Fusiones**: Garnet (Rubí + Zafiro) · Ópalo (Amatista + Perla) · Sardonyx (Garnet + Perla) · Sugilite (Garnet + Amatista) · Alexandrita (las tres) · Obsidiana (las cuatro con Steven) · Stevonnie (Steven + Connie) · Cuarzo Ahumado (Steven + Amatista) · ✅
- **Lugares**: Homeworld, Beach City, el Templo, la Casa Playa, el Big Donut, Little Homeworld. **Gobierno**: la *Great Diamond Authority* ([ficha](https://steven-universe.fandom.com/wiki/The_Great_Diamond_Authority); ⚠️ su nombre en el doblaje latino no está en las partes).

## 3 conceptos de lámina

Reglas del dueño que se aplican: un objeto real en un sitio real (hecho en Blender si se puede), pose y cara que vayan con lo que dicen, recortes por `v3/integrar.py`, textos cortos en la voz de la serie y sin «·», «—» ni paréntesis. **Tono de la serie: cálido y pastel**, con grano; nada de oscuro ni sangriento. Letra de todos los textos: **Crewniverse** (la única comprobada con tildes, ñ, ¿ y ¡).

### A · #🎵・canto — «El cancionero en el techo del vagón» ⭐ recomendado

- **Objeto y sitio:** un **cancionero** de espiral abierto y el **ukulele** de Steven, sobre el **techo del vagón rojo** al atardecer, con Beach City y el mar al fondo. Base: **hoja n.º 46** («On the Run»; «On the Run» es también una canción del disco). En Blender: el cuaderno con Paper006 (la tinta sigue la curva de la hoja), el ukulele y el techo del vagón como una caja roja.
- **Quién:** **Steven**, la voz de más de 38 canciones (en latino, Leisha Medina canta el opening). Sentado como en la n.º 46, con la cara **tranquila y sonriente, ojos entornados** (`TIO` 0:56-1:04). Una mano sobre el cancionero, como enseñándolo (el gesto de señalar de `GG` 1:30). **Amatista** a su lado, detrás y un poco desenfocada, comiendo un Cookie Cat (`GG` 4:00).
- **Cómo habla:** sin globo. El nombre del canal como **cartela de título** de la serie, en el cielo. Lo demás, **escrito en el cancionero** y en una etiqueta pegada al estuche del ukulele.
- **Dónde va cada texto:**
  - Cielo, cartela: «canto».
  - Página izquierda, Steven: «¡Aquí se habla de cantar!»
  - Página derecha: «Técnica, canciones, dudas de voz.»
  - Etiqueta del ukulele: «¿Tienes un cover? Va a #demos-canto. Un hilo por cover.»
- **Para que no quede plano:** paleta medida del atardecer de `GG` 11:00 (cielo `#F7F6CE`, nubes `#CD8891`, arena `#ECD2A3`, acantilado en silueta `#17251E`). Luz de borde cálida en el pelo de Steven. **El mástil del ukulele cruza la esquina de abajo**, delante de todo. Amatista desenfocada detrás; el mar con el grano de la serie.
- **Lámina 2 (si se satura):** las etiquetas de #demos-canto (Soprano, Mezzosoprano, Contralto, Tenor, Barítono, Bajo, Falsete, Growl, Balada, Rock, Pop, Anime OP/ED) escritas como la lista de canciones del cancionero.

### B · #🪪・presentaciones — «La Guía de las Gemas en la cocina»

- **Objeto y sitio:** el libro oficial ***Guide to the Crystal Gems*** abierto sobre la **mesa de la cocina de la Casa Playa** (hoja n.º 141). En la página izquierda, **la ficha real de Amatista** (hoja n.º 2: cinta lila con estrella, «Species», «Weapon», «Favorite Quote»). En la derecha, **la misma ficha en blanco** para el servidor. En Blender: libro abierto con las páginas curvadas.
- **Quién:** **Perla**, la más dibujada por los fans (1.ª en Danbooru) y la que lo explica todo. De pie junto a la mesa con la **mano abierta hacia el libro** (hoja n.º 15) y cara amable y orgullosa. **Amatista** asoma por el otro lado **señalando su propia ficha** (hoja n.º 143), con su sonrisa de broma. Es su dinámica real: Perla ordena, Amatista se ríe.
- **Cómo habla:** el propio formato de la *Guía*: cada campo con su **cinta lila y estrella**, en Crewniverse. Las frases de Perla y Amatista, como pies de página del libro.
- **Dónde va cada texto:**
  - Cabecera de la página derecha: «Tu ficha».
  - Campos con cinta: «Nombre», «País», «Qué haces», «Tu frase favorita».
  - Bajo «País»: Sudamérica, México, Centroamérica y Caribe, España, Otro país.
  - Bajo «Qué haces»: Doblaje, Canto, Locución, Edición, Arte, Escritura, Hacer amigos.
  - Pie, Perla: «Es opcional. Pero así todos te ponen cara.»
  - Pie, Perla: «Abre TU hilo con la plantilla fijada.»
  - Pie, Amatista: «¡Y no te olvides de tu frase favorita!»
- **Para que no quede plano:** luz de tarde por la ventana (paleta de `GG` 3:30: `#F4DACF`, `#CEA7B0`, `#7A5C74`), con la **sombra del marco de la ventana** cruzando el libro. **Una taza de té de Perla** delante, desenfocada (a Perla le gusta el té, no la comida). Amatista entra desde el borde, cortada por el marco.
- ⚠️ El texto del canal en `servidor/inventario.md` está cortado («nadie comenta…»): confirmar cómo termina antes de rotular.

### C · #📂・proyectos — «La Puerta del Templo»

- **Objeto y sitio:** **la Puerta del Templo**, con la **estrella de cinco gemas** (hojas n.º 13-14 y [Better Temple Door](https://static.wikia.nocookie.net/steven-universe/images/e/eb/Better_Temple_Door.png), 1953×3105). En Blender: la puerta de piedra con el relieve de Rock064, el dintel geométrico y las cinco gemas con emisión de luz. El **camino de luz** que sale de la estrella (ondulado en la n.º 13, recto en la n.º 14) es el avance del proyecto.
- **Quién:** **Garnet**, la mejor valorada por la prensa (1.ª en IGN) y **una fusión: un equipo que funciona**. De pie junto a la puerta, **chasqueando los dedos** con sonrisa confiada (`STY` 2:42). Sin preguntas en su texto: Garnet no pregunta nunca.
- **Cómo habla:** lo que dice está **grabado y encendido en la piedra** (el cartel del mundo), en Crewniverse. De adorno, una cenefa copiada del [banner de Homeworld](https://static.wikia.nocookie.net/steven-universe/images/7/7d/Homeworld_banner_zoomed_in.PNG) en Gem Glyph (sólo adorno: no escribir glifos inventados).
- **Dónde va cada texto:**
  - Dintel: «proyectos».
  - Cada gema de la estrella, una etapa: rosa «Buscando gente», crema «En grabación», morada «En edición», roja «En revisión», azul «Estrenado».
  - Bajo la estrella, Garnet: «Un hilo por proyecto.»
  - Garnet: «Equipo, avance, entregas.»
  - Abajo, su frase real del doblaje: «Cuando dos gemas se combinan crean algo más grande que la suma de sus partes.»
- **Para que no quede plano:** la luz de las gemas **ilumina a Garnet desde abajo** (el plano heroico de las fusiones). Una **burbuja rosa translúcida** flota delante de ella con un guion enrollado dentro (el gesto de guardar algo valioso, `STY` 4:09). Alrededor, un interior cálido y desenfocado en la paleta de `GG` 3:30. ⚠️ Las partes no dicen qué hay alrededor de la puerta: mirar un fotograma antes de modelarlo.
- **Lámina 2:** las diez etiquetas del foro (Buscando gente, En traducción, En grabación, En edición, En revisión, Estrenado, En pausa, Cancelado, Oficial del servidor, De la comunidad), como burbujas de colores guardadas en el Templo.

**Otra idea para más adelante:** #🧰・recursos con la **Mochila Hamburguesa** abierta (es el inventario de *Unleash the Light*).

## Lo que corregí de las partes y lo que no se pudo verificar

**Correcciones (antes → ahora)**
- Parte de imagen: `objetos_01` tenía «modelos de producción de Steven y Garnet con escudo y guanteletes» → la hoja trae **fotogramas de la película e iconos** de gemas y fusiones (visto). Esos modelos están enlazados en el punto 1.
- Parte de imagen: el Kindergarten y el granero estaban «en la hoja de fondos» con otros títulos → el Kindergarten es la **n.º 36** de `personajes_01` («Back to the Kindergarten», visto); el granero **no está** en las 3 hojas guardadas.
- Parte de voz: la muestra de Garnet era «la canción Stronger Than You» → es **un montaje**: sólo 0:21-0:25 suena a la letra cantada; «la Tierra era de Diamante Rosado…» es de otra escena.
- Parte de vídeo: decía a la vez que no hay tema de cierre y que «Love Like You» lo es → en el piloto los créditos son **instrumentales** (oído); «Love Like You (End Credits)» está en el disco. Sin comprobar en qué capítulos suena cantada.
- Parte de texto: «Sailor Moon está en #demos (canal 16)» → Sailor Moon es la biblia **38** y propone 🎲 Juegos, #eventos y #general-doblaje (DECISIONES.md).
- Parte de texto: el Comunicador de las Diamantes aparecía como «octaédrico» y como «pantalla cuadrada» → el **objeto es octaédrico** (ficha); la forma de la pantalla que proyecta, sin confirmar.
- `voz.json` enlazaba Danbooru con la etiqueta `steven_universe_pearl` (no existe así) → en `referencias.json` va `pearl_(steven_universe)`.
- Arena: la parte de vídeo usó **Ground054** y la de imagen **Ground080** → van las dos (punto 4).

**Lo que no se pudo verificar** (va con ⚠️ en su punto)
- Frases latinas de **clips oficiales doblados**: sólo hay muestras de Doblaje Wiki (sin capítulo). El clip `TIO` se vio pero no se transcribió.
- Caras de 9 de las 20 combinaciones emoción-personaje (punto 13).
- Letra de globos, gritos y onomatopeyas del **cómic de BOOM!** (no se encontró el rotulista) y **cajas de diálogo de los juegos** (Game UI Database y TCRF bloqueados).
- **Crystal Universe** (letra del logo): la descarga dio 0 bytes; tildes y ñ sin comprobar.
- **Vistas** de fandubs y covers (YouTube pide iniciar sesión).
- Los análisis en vídeo de Saberspark y PhantomStrider y el pódcast de Chris McDonnell: sólo se leyó su ficha.
- Hex de las variantes de vestuario (Steven de la película y de *Future*, Purple Puma, Perla de Homeworld).
- Si el entintado se hizo en Toon Boom Harmony; si los modelos 3D libres traen esqueleto.
- Nombres latinos de *poof*, *Homeworld*, *Cheeseburger Backpack* y demás vocabulario (punto 17).
