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

