---
tags: [biblia, serie, laminas]
serie: "Harry Potter"
canal: "#anuncios"
fecha: 2026-09-24
---

# Biblia · Harry Potter — para #anuncios

> [!important] Cómo se hizo (léelo primero)
> - **Dos pasadas.** La primera (24-sep-2026, mañana) se hizo con la red
>   cerrada: sólo buscador web (64 búsquedas) y GitHub (subtítulos en inglés
>   de las 8 películas con sus tiempos, y los archivos de las letras).
> - **Segunda pasada, 24-sep-2026, con la red abierta.** Se pudo usar:
>   - **Wiki de Fandom** (`harrypotter.fandom.com`) por su API: 2 tandas de
>     `investigar_serie.py` (**538 + 63 imágenes**, 14 hojas numeradas) y
>     búsquedas de archivos. **Las miré todas.** Monté 3 hojas propias en
>     `hojas/` (§2.0). Los tamaños son los reales de la API.
>   - **Doblaje Wiki** por la API: las 8 películas y 9 fichas de personaje.
>     Estudio, dirección y reparto **por película**, y **65 muestras de audio
>     del doblaje**, que pasé por reconocimiento de voz (Whisper) para sacar
>     frases textuales (§10).
>   - **YouTube con yt-dlp**: 28 vídeos comprobados. YouTube no dejaba bajar
>     el vídeo («Sign in to confirm you're not a bot», «This video is not
>     available»; lo intenté con 6 clientes y en 4 momentos distintos).
>     **Los miré por sus *storyboards***: fotogramas de 160×90 o 320×180,
>     uno cada 1-5 s, en hojas numeradas con su minuto (±2 s). Opening,
>     ending, 3 tráileres oficiales en español y 11 escenas de los canales
>     oficiales, Movieclips y HBO Max Latinoamérica (§12, §15).
>   - **`fotogramas.py` sí funcionó con vídeo de verdad** bajado del
>     **Internet Archive**: la escena del vociferador en 1080p (copia del
>     vídeo «en 23 idiomas», con el doblaje latino dentro) y el tráiler
>     final oficial de P6. Fotogramas grandes mirados y colores medidos
>     (§3, §12).
>   - **Reconocimiento de voz** (Whisper, modelo *medium*) sobre el audio
>     latino de esa escena y sobre muestras de Doblaje Wiki (§10.3).
>   - **Sketchfab** (licencias por su API), **MinaLima** (imágenes de sus
>     láminas, medidas), subtítulos en inglés otra vez (para cruzar minutos).
>   - Colores **medidos con Pillow** en fotogramas, láminas de MinaLima y
>     arte oficial de la wiki (se dice de cuál en cada hex).
> - **Siguen cerradas o fallan:** bajar vídeo, audio o subtítulos de YouTube
>   (sólo dan *storyboards*), Wayback Machine (el túnel se corta), Blog
>   Hogwarts (503), ArtStation (403), Texturelabs (reto antibots).
> - La segunda pasada la hicieron **tres ayudantes seguidos** el mismo día: al
>   primero lo cortó el límite de uso; el segundo terminó §15-§21,
>   `referencias.json`, la tabla de cumplimiento y la bitácora; el tercero
>   (cierre, tarde del 24-sep-2026) miró **5 vídeos más de verdad con
>   `fotogramas.py`** (tráiler y *teaser* oficiales de P1 y un fragmento de P1
>   en 1080p del Internet Archive; Dobby libre y Luna en Dailymotion, 512 px),
>   leyó la **Wikipedia en español por su API** (ya responde), **DubDB** y
>   los **créditos de cine del doblaje** (P1 y P2), transcribió con Whisper
>   las **voces de los insertos** del doblaje latino (§10.3) y resolvió dudas.

**Leyenda**
- ✅ **confirmado**: dos fuentes, o un archivo que abrí, medí o miré.
- ⚠️ **dudoso**: una sola fuente, o de memoria. Míralo antes de dibujar.
- «P1 00:42:20» = película 1, minuto de los subtítulos en inglés. Puede
  moverse un minuto según la edición.
- «P·7» = número 7 de `hojas/personajes_01.jpg`; «O·3» = `objetos_01.jpg`;
  «F·5» = `fondos_01.jpg`. La tabla de §2.0 enlaza cada original.
- «clip 0:43» = minuto dentro del vídeo de YouTube enlazado (±2 s).

## Segunda pasada · qué cambió

**Corregido (antes → ahora)**
- **El atril del búho no sale en la película 1.** Antes: «P1 00:42:20,
  Dumbledore en el atril». Ahora: en P1 da los avisos **de pie en la mesa de
  profesores, entre velas** (F·1). El atril dorado aparece **desde la
  película 3** (la wiki lo marca «1st» en P3, y en los libros no existe) ✅.
  Lo vi en el [clip oficial de P3, 0:43](https://www.youtube.com/watch?v=dvFehFzph7I&t=43).
- **«Boy Who Lived» de MinaLima no es de la «primera época».** La lámina
  dice «Harry Potter and the Order of the Phoenix» (P5). La cabecera alegre es
  la **gótica adornada** «The Daily Prophet» de P1-P4 (O·1, O·2, O·9) ✅.
- **El tablón de Gryffindor no es de corcho** en el arte oficial: es
  **fieltro rojo oscuro `#51201D`** en un **marco de madera tallada**, entre
  tapices de flores (O·21, Pottermore). Y no sale «sólo en los libros»: la
  wiki lo lista también en las películas 1-6 y en los juegos.
- **Doblaje, película a película** (Doblaje Wiki): P1 **Audiomaster 3000**
  (no «Audiomaster»); P3 la dirigió **José Luis García Agraz** (no Molina);
  P5 **Herman López** en **DAT**; P5 a P8 en **DAT Doblaje Audio
  Traducción**. Hagrid en P2 y P3 es **Víctor Hugo Aguilar**. Snape tuvo
  **6 voces** (no 1). Hay un **redoblaje argentino de 2019** (Caja de
  Ruidos) de P3 a P8: no mezclarlo.
- **«Dobby es un elfo libre»**: de dudoso a ✅. Es la frase del doblaje latino de P7
  (muestra de audio de Doblaje Wiki: «Dobby no tiene amo. Dobby es un elfo
  libre, y Dobby vino a salvar a Harry Potter y a sus amigos»).
- **Poses de memoria → miradas** en los clips: Dumbledore **abre los brazos**
  tras el atril (P3, clip 0:43) y **alza los dos índices** al hablar de la
  felicidad (clip 2:42); Hermione **agarra el brazo de Ron** para corregirlo
  (clip 0:04) y cierra los ojos con la barbilla alta (clip 0:17); Luna
  **lee El Quisquilloso tapándose la cara** en el carruaje (clip 0:59).
- **Licencias de Sketchfab**: por la API. El tablón de corcho es **CC BY**
  ✅; el Gran Comedor con velas de JER3D **ya no existe** (404).
- **Concepto B tenía a Dumbledore en el atril «como en P1 00:42:20»**: en
  P1 no hay atril. Ahora: Gambon con los brazos abiertos tras el atril
  (clip oficial de P3, 0:43) o la mano abierta de P·26.
- **Concepto C era de corcho** → **fieltro rojo `#51201D`** con marco
  tallado (O·21). Los gorros de Dobby, de memoria a la wiki (*Elf hat*).
- **`referencias.json` seguía siendo el de la 1.ª pasada** (páginas web,
  sin tamaños), aunque aquí ya se daba por rehecho. Ahora sí: 40 entradas
  con la imagen o el vídeo y el tamaño medido.
- **Poses de memoria → vistas** (§15): 52 poses; casi todas con su clip o su
  número de hoja. Dobby en P7 no «saca pecho con el dedo en alto»: está **erguido,
  brazos a los lados, cara alzada** (clip de Movieclips 2:44).
- **Vestuario a ojo → medido** (§16). Ej.: la corbata de Harry `#740001` →
  `#61121B`; Dumbledore de P1 es **burdeos con oro**, no «ciruela».
- **Doblaje de P1 y P3**: de dudoso a ✅ con prensa de 2001 y 2004 y el blog del
  director Javier Rivero. **«Tell them to wait»** lo dice Dumbledore ✅.
  **Luna reparte El Quisquilloso en el pasillo del tren** ✅ (wiki).
  **Desplat** en P7-P8 ✅.

**Añadido**
- 3 hojas de contacto propias (§2.0), con 100 imágenes elegidas de 601.
- **20 frases textuales del doblaje latino** de 11 personajes (§10.3). Entre
  ellas, **dos avisos oficiales** dichos a todo el colegio: el de McGonagall
  del baile (P4) y el de Snape director (P8).
- Colores **medidos** (§5, §16) y hex de las láminas de MinaLima.
- Minutos y enlaces `&t=` de 28 vídeos (§12) y poses con clip (§15).
- **Vídeo real con `fotogramas.py`** (Internet Archive): el vociferador en
  1080p y el tráiler final de P6. Y el **doblaje latino del vociferador,
  con minuto**: «¡Ronald Weasley! ¡Cómo osaste robar el auto!» (§10.3). En
  latino se dice **«vociferador»**; en España, «Howler».
- **El anuncio de Hagrid** en P3 («I'm delighted to announce…», 00:24:29):
  el anuncio alegre que faltaba (§3).
- **Fondos de pantalla** con tamaño y autor (§17), guía para IA ampliada
  (§18), §20 al día.
- La **Tabla de cumplimiento** (antes de la bitácora) y la bitácora de la
  2.ª pasada.
- Aviso: hay **serie de HBO en marcha** («Harry Potter y la piedra
  filosofal», teaser latino de HBO Max, 2026). No confundir su reparto.

**Tercer ayudante (cierre): corregido (antes → ahora)**
- **El tablón de Gryffindor sí sale en la película 1, y lo vi**: la mañana
  de Navidad (P1 ≈01:28:25), detrás de Harry con la capa. Es **fieltro rojo
  con una cuadrícula de cintas oscuras y un cordón trenzado rojo y oro** de
  borde, con tarjetas de Navidad clavadas, junto al tapiz del unicornio
  (fragmento en 1080p, [0:14](https://archive.org/download/670343/colombus_harry_potter_philosophers_stone_extrait.HD.mp4#t=14)).
  Antes sólo teníamos el de Pottermore (O·21). **Cambia el concepto C.**
- **Quién lee El Profeta en P1**: de dudoso a ✅. Harry le pide el diario a Ron
  («Can I borrow this?») y lo lee en voz alta (wiki + guion transcrito de
  [Moviepedia](https://movies.fandom.com/wiki/Harry_Potter_and_the_Philosopher%27s_Stone/Transcript)).
- **Luna lee El Quisquilloso al revés**, también en la película: la portada
  boca abajo ([P5, 0:48 del clip](https://www.dailymotion.com/video/x3dhmzl?start=48);
  la wiki lo cita del libro 5) ✅. Nuevo guiño para el concepto A.
- **Doblaje P3**: la Wikipedia en español dice «Art Sound, dirección de
  Helgar Pedrini»; Doblaje Wiki y DubDB dicen **Audio Post** y ponen a
  Pedrini como **director creativo** de Warner. Queda Audio Post (dos
  fuentes contra una, §10.1).
- **Doblaje P5**: estudio **DAT** ✅ (Wikipedia + Doblaje Wiki). La
  dirección no cuadra: Herman López (Doblaje Wiki) o Helgar Pedrini
  (Wikipedia): sigue dudosa.
- **Los enlaces a archivos de Doblaje Wiki** (muestras de audio y
  créditos) **daban 404**: a esa wiki le falta el `/es/` en la ruta. Ahora
  van a `static.wikia.nocookie.net/doblaje/es/images/…` y los 36
  responden (comprobados uno a uno, también los 130 enlaces de imágenes de
  la wiki y de `referencias.json`).
- **Nick Casi Decapitado en Hogwarts Legacy es Álvaro Sarlich**, no
  «Salarich» ([ANMTV](https://www.anmtvla.com/2023/02/hogwarts-legacy-warner-bros-games.html)).
- **Logo de Hogwarts Legacy**: «Customized from the typeface Tongari»,
  lo dice **Pentagram**, el estudio que lo diseñó ✅ (antes sólo FontBolt).
- **Pasan de dudoso a ✅** (segunda fuente encontrada): las voces de
  Hermione en P3 (Priscila Reyes), McGonagall en P1 (Magda Giner), Snape en
  P3 y P8 (César Monroy, Sebastián Llapur), Umbridge (Ruth Toscano) y Molly
  en P2 (Carmen Martínez); el redoblaje argentino; Hermione levantando la
  mano; Luna repartiendo El Quisquilloso; los gorros de Dobby (HP Lexicon);
  Caxambu en El Profeta (O Tempo); la encuesta de MTV y la coreana; el
  vídeo de Bilibili y el TikTok; las capturas de *Hogwarts Mystery*.

**Tercer ayudante: añadido**
- **La voz de los insertos del doblaje latino**: un narrador **lee en voz
  alta los titulares de El Profeta** y los carteles («Silencio. TIMOS en
  progreso…», «Dumbledore y Potter reivindicados», «Harry Potter, el
  elegido»). Es el anuncio oficial hecho voz (§7.1, §10.3).
- **Créditos de cine del doblaje** de P1 y P2 (fotos en Doblaje Wiki):
  confirman estudio, director y voces (§10.1, §10.2).
- **Logos latinos de cine**: el de P4 dice «Y EL CÁLIZ DE FUEGO», **con
  tilde** (§6.1).
- 5 vídeos más mirados con `fotogramas.py` (§12.1), poses nuevas de
  Hermione, Luna, Dobby y Dumbledore (§15), la caja de diálogo de
  *Hogwarts Mystery* medida (§7.2).

**Marcas de duda:** había **55** antes de la segunda pasada; **38** cuando
cerró el segundo ayudante; quedan **22** (contadas con `grep -o`; el número
incluye la leyenda). Lo que sigue dudoso y por qué: §20.

---

## 0 · El canal y lo que tiene que decir

Del inventario del servidor (`servidor/inventario.md`, sección EMPIEZA AQUÍ):

> **ıı・📢・anuncios** (anuncios) · 0 fijados — _Solo staff. Para comentar,
> abre un hilo en el anuncio._

Función según el encargo: **las novedades oficiales del servidor**.
No tiene etiquetas ni fichas.

**Los 4 textos de la lámina** (una idea cada uno, sin «·», «—» ni paréntesis):

| # | Texto | Idea |
|---|---|---|
| 1 | **Anuncios** | nombre del canal |
| 2 | **Las novedades oficiales del servidor** | para qué es |
| 3 | **Solo el staff publica aquí** | quién escribe |
| 4 | **¿Quieres comentar? Abre un hilo en el anuncio** | cómo participar |

Caben en una sola lámina. **No hace falta lámina 2.**

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Cuadro de diálogo propio | **La portada de El Profeta**, época alegre (P1-P4: cabecera gótica adornada, titulares góticos, texto en espiral; O·1, O·2). En Harry Potter el texto vive dentro de objetos: periódico, carta, pergamino, aviso clavado, **la cinta de pergamino de los créditos de P3**. Nunca en un globo. |
| Mejor objeto para #anuncios | **El Profeta en la mesa del Gran Comedor, a la hora del correo.** Escena real: P1 00:53:45 («Mail's here») a 00:54:57. Arte oficial del correo del desayuno: F·8. |
| Segundo objeto | **El atril del búho dorado**, alas abiertas. **Sale desde P3**, no en P1: [clip oficial de P3, 0:43](https://www.youtube.com/watch?v=dvFehFzph7I&t=43), Dumbledore abre los brazos tras él. En P1 da los avisos de pie en la mesa (00:42:20, F·1). |
| Tercer objeto | **El tablón de anuncios de Gryffindor**: fieltro rojo en marco tallado (O·21, Pottermore); **en la película 1 se ve de fondo** con cuadrícula de cintas y cordón rojo y oro (P1 ≈01:28:25, §3). Según la wiki, cada día se clavaban ahí **El Profeta y El Quisquilloso**. |
| El más querido | En tres grandes encuestas gana **Snape**. De la lista del encargo, **Hermione** va siempre arriba. **Luna** supera a Harry en dos encuestas y **Dobby** en una. |
| Letras | **UnifrakturMaguntia** para la cabecera. **IM Fell English** para el texto. Las dos son libres y traen todas las tildes. Comprobado en el archivo. |
| Voz latina | Harry: **Víctor Ugarte** (P3-P8). Hermione: **Leyla Rangel** (P4-P8). Dumbledore: **César Arias** (las 8). Luna: **Lu Leal** (P5-P8). Dobby: **Ismael Castro** (P2 y P7). Todos ✅ (Doblaje Wiki + prensa). |
| La voz de los avisos en latino | En el doblaje latino **un narrador lee en voz alta los titulares de El Profeta** y los carteles: «Silencio. TIMOS en progreso», «Dumbledore y Potter reivindicados» (§10.3). |
| Frase latina para #anuncios | Dumbledore, P8: «**Las palabras son, en mi no tan humilde opinión, nuestra fuente más inagotable de magia**» (muestra de Doblaje Wiki, §10.3). |
| Tono | La época alegre de las películas 1 a 4: vela, madera y papel crema. La cabecera oscura, de propaganda (P5 en adelante), no va aquí. |

---

## 2 · Arte oficial y referencias visuales

### 2.0 Las hojas de contacto (lo que vi en la wiki) ✅

Corrí `investigar_serie.py` dos veces sobre `harrypotter.fandom.com`:
- `herramientas/referencias/harry-potter/`: 8 páginas de personajes (los 6 del encargo, Snape y McGonagall). **754 imágenes enlazadas, 538 grandes, 12 hojas.**
- `herramientas/referencias/harry-potter-objetos/`: 12 páginas de objetos y sitios (El Profeta, El Quisquilloso, atril, tablón, vociferador, decretos, Gran Comedor, sala común, carta, gafas espectrales, calcetín). **92 imágenes, 63 grandes, 2 hojas.**
- Y busqué en el espacio de archivos de la wiki («Daily Prophet», «lectern», «notice board», «Hogwarts letter», «Educational Decree»…): 51 archivos más, con su tamaño.

**Las miré todas.** Mucho no sirve: fotos de *Animales fantásticos* y de *El legado maldito* (teatro), muñecos LEGO y Funko, escudos de casas, fotogramas oscuros de P7-P8. Lo que más sirve: los **promos con fondo** de Warner, los **renders recortables** del juego *Puzzles & Spells* (PAS, fondo verde en la hoja), el **arte de Pottermore** (ilustraciones anchas de 4000 px, de Atomhawk Design y otros) y **los props de papel** (El Profeta, El Quisquilloso, decretos).

Monté **3 hojas propias** con Pillow (`hojas.py` en mi carpeta de trabajo). En cada celda va el tamaño real. El verde de fondo marca lo recortable.

**`hojas/personajes_01.jpg`** (P·)

| N.º | Qué es | Tamaño | Para qué | Original |
|---|---|---|---|---|
| 1 | Hermione P3, promo con Crookshanks | 2923×4000 | Hermione de cuerpo entero, erguida, mano en el mueble: **presentar** | [enlace](https://static.wikia.nocookie.net/harrypotter/images/d/d2/Hermione_poa.jpg) |
| 2 | Hermione render PAS, libros | 1080×2009 | recorte limpio (fondo verde): libros abrazados, **explicar** | [enlace](https://static.wikia.nocookie.net/harrypotter/images/c/c4/Hermione_Granger_-_PAS.png) |
| 3 | Hermione, retrato promo | 1535×2048 | cara y pelo de la época madura | [enlace](https://static.wikia.nocookie.net/harrypotter/images/3/34/Hermione_Granger.jpg) |
| 4 | Hermione P5, perfil | 640×900 | uniforme P5, mirada seria | [enlace](https://static.wikia.nocookie.net/harrypotter/images/2/21/Hermione_Granger_OOTP_profile.jpg) |
| 5 | Hermione: diseño vestido de gala P4 | 1182×1255 | vestido rosa de volantes: **qué NO** (gala, no anuncio) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/3/33/HermioneGranger_WB_F4_HermioneGrangerCharacterIllustration_Illust_080615_Port.jpg) |
| 6 | Hermione y Ron P2, promo | 744×1000 | Hermione y Ron juntos, uniforme P2 | [enlace](https://static.wikia.nocookie.net/harrypotter/images/e/e0/Hermione_Granger_and_Ron_Weasley_COSF_promo.jpg) |
| 7 | El trío P1, escoba y libros | 1080×1350 | **el trío con escoba y libros**: grupo, presentar | [enlace](https://static.wikia.nocookie.net/harrypotter/images/a/ac/Trio_in_their_younger_days_Harry%2C_Ron_and_Hermione.jpg) |
| 8 | Ejército de Dumbledore P5 | 4064×2704 | **el Ejército de Dumbledore en fila**: grupo, animar | [enlace](https://static.wikia.nocookie.net/harrypotter/images/9/96/Dumbledore%27s_Army.jpg) |
| 9 | Luna P6, retrato promo | 1346×2000 | Luna, cara y pendientes de rábano | [enlace](https://static.wikia.nocookie.net/harrypotter/images/e/ed/Luna_Lovegood.jpg) |
| 10 | Luna con el sombrero de león | 1365×2048 | **Luna con el sombrero de león**: el guiño que ama el fan | [enlace](https://static.wikia.nocookie.net/harrypotter/images/2/22/Lion_Lovegood.jpg) |
| 11 | Luna con las gafas espectrales | 1401×2100 | **Luna con las gafas espectrales y El Quisquilloso en la mano** | [enlace](https://static.wikia.nocookie.net/harrypotter/images/7/70/Luna_wearing_Spectrespecs.jpg) |
| 12 | Luna leyendo El Quisquilloso | 1325×1298 | **Luna leyendo El Quisquilloso**: la prensa «no oficial» | [enlace](https://static.wikia.nocookie.net/harrypotter/images/6/6b/Quibbler-Luna.JPG) |
| 13 | Luna: figurín de vestuario P6 | 857×1386 | figurín P6: chaqueta ciruela, medias turquesa (hex en §16) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/d/d9/LunaLovegood_WB_F6_LunaLovegoodCharacterIllustration_V2_Illust_080615_Port.jpg) |
| 14 | Luna: boceto de vestuario P5 | 788×1182 | boceto P5: rebeca verde y falda | [enlace](https://static.wikia.nocookie.net/harrypotter/images/1/15/WB_F5_LunaLovegood_ConceptArtCostumeSketch_ArtWork-181.jpg) |
| 15 | Luna ante avisos clavados, Pottermore | 910×935 | **Luna ante avisos clavados en la pared** (Pottermore): pose para el tablón | [enlace](https://static.wikia.nocookie.net/harrypotter/images/f/ff/Luna_Lovegood_-_Jessica_Roux_PM.jpeg) |
| 16 | Sombrero de león, arte conceptual | 836×1231 | concepto del sombrero | [enlace](https://static.wikia.nocookie.net/harrypotter/images/6/60/Luna%27s_Lion_Hat_-_Concept_Art.jpg) |
| 17 | Dobby, cartel de personaje P7 | 1600×2560 | cartel P7: medio rostro en sombra (tono oscuro, no para #anuncios) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/f/f2/Dobbyposter.jpg) |
| 18 | Dobby P7, chasquea los dedos | 1300×1312 | **Dobby chasquea los dedos, mano en alto**: magia, **proclamar** | [enlace](https://static.wikia.nocookie.net/harrypotter/images/f/f4/DobbyDH.jpg) |
| 19 | Dobby, brazos en jarra | 944×1056 | **Dobby con los brazos en jarra**: orgullo, «elfo libre» | [enlace](https://static.wikia.nocookie.net/harrypotter/images/8/82/Dobby.jpg) |
| 20 | Dobby, primer plano | 931×919 | cara de Dobby, ojos verdes | [enlace](https://static.wikia.nocookie.net/harrypotter/images/f/f0/Dobbyelve.jpg) |
| 21 | Dobby recibe el calcetín, PAS | 833×1442 | recorte limpio: Dobby con el libro donde va el calcetín | [enlace](https://static.wikia.nocookie.net/harrypotter/images/6/6e/Dobby_Receives_Sock_PAS.png) |
| 22 | Dobby liberado, Pottermore | 4140×1500 | Dobby liberado (Pottermore), oscuro | [enlace](https://static.wikia.nocookie.net/harrypotter/images/7/72/B2C18M2_Dobby_is_freed.jpg) |
| 23 | Dobby, títere de rodaje P7 | 907×720 | el títere de rodaje P7 | [enlace](https://static.wikia.nocookie.net/harrypotter/images/b/bb/DH_Dobby_puppet_artwork.jpg) |
| 24 | Dumbledore P6, varita en alto | 2136×2850 | **Dumbledore P6 con la varita en alto**: presentar con énfasis | [enlace](https://static.wikia.nocookie.net/harrypotter/images/7/75/Albus_Dumbledore_%28HBPF_promo%29.jpg) |
| 25 | Dumbledore P6, sentado | 2136×2850 | Dumbledore sentado, sereno: **pensar** | [enlace](https://static.wikia.nocookie.net/harrypotter/images/0/04/Albus_Dumbledore_%28HBP_promo%29_1.jpg) |
| 26 | Dumbledore render PAS, mano abierta | 1080×2400 | **recorte limpio: mano abierta hacia arriba**: presentar, explicar | [enlace](https://static.wikia.nocookie.net/harrypotter/images/f/fc/Albus_Dumbledore_2_-_PAS.png) |
| 27 | Dumbledore P1 (Richard Harris) | 1347×1820 | Dumbledore de Richard Harris, túnica burdeos en el banquete | [enlace](https://static.wikia.nocookie.net/harrypotter/images/8/81/Albus_Dumbledore_PSF.jpg) |
| 28 | McGonagall y Dumbledore P2, promo | 784×1024 | McGonagall y Dumbledore, el «staff» | [enlace](https://static.wikia.nocookie.net/harrypotter/images/8/83/COS_promo_Minerva_Albus.jpg) |
| 29 | Harry P6, promo | 1500×1982 | Harry P6, perfil serio | [enlace](https://static.wikia.nocookie.net/harrypotter/images/3/3a/Harry_Potter_HBPF_promo_2.jpg) |
| 30 | Harry P2, uniforme | 694×967 | Harry P2 con uniforme | [enlace](https://static.wikia.nocookie.net/harrypotter/images/e/ee/COS_promo_Harry_Potter_Hogwarts_uniform_cropped.jpg) |
| 31 | Ron P5, promo | 775×1155 | Ron P5 | [enlace](https://static.wikia.nocookie.net/harrypotter/images/3/3f/OOTP_promo_front_Ron_cropped.jpg) |
| 32 | Ron render PAS, varita y libro | 860×1280 | recorte limpio: Ron con varita y libro | [enlace](https://static.wikia.nocookie.net/harrypotter/images/8/89/Ronald_Weasley_-_PAS.png) |
| 33 | McGonagall: figurín de vestuario | 2360×2728 | figurín de McGonagall (verde) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/1/1e/MinervaMcGonagall_WB_F1_MinervaMcGonagallRobeIllustration_Illust_080615_Port.jpg) |
| 34 | Snape y Dumbledore | 2531×3797 | Snape y Dumbledore | [enlace](https://static.wikia.nocookie.net/harrypotter/images/2/26/Snape_and_Dumbledore.jpg) |
| 35 | Hermione estilo Magic Awakened | 825×641 | estilo Magic Awakened (sólo referencia de estilo) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/7/77/Hermione_Granger_Ministry_MA.png) |
| 36 | Harry render PAS, libro | 636×870 | recorte limpio: Harry con libro | [enlace](https://static.wikia.nocookie.net/harrypotter/images/4/44/Harry_Potter_-_PAS.png) |

**`hojas/objetos_01.jpg`** (O·)

| N.º | Qué es | Tamaño | Para qué | Original |
|---|---|---|---|---|
| 1 | El Profeta Vespertino: el Ford Anglia | 1680×2448 | **cabecera gótica adornada** de la primera época (P2) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/c/c6/EveningProphetFlyingFordAnglia.png) |
| 2 | El Profeta: robo de Gringotts P1 | 854×1267 | **El Profeta de P1**: titular gótico, texto en espiral | [enlace](https://static.wikia.nocookie.net/harrypotter/images/3/39/Daily_prophet_gringotts_break_in.jpg) |
| 3 | Recorte del robo de Gringotts | 560×854 | recorte del mismo número | [enlace](https://static.wikia.nocookie.net/harrypotter/images/a/a3/1991_Gringotts_Break-in_Daily_Prophet.jpg) |
| 4 | El Profeta PAS: sale el expreso | 1536×2048 | portada estilo juego (PAS) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/9/95/Daily_Prophet_-_Hogwarts_Express_Departs_-_PAS.png) |
| 5 | El Profeta PAS: Gryffindor gana | 720×1280 | portada estilo juego: «Gryffindor gana» | [enlace](https://static.wikia.nocookie.net/harrypotter/images/c/cb/Daily_Prophet_-_Gryffindor_wins_the_House_Cup_-_PAS.png) |
| 6 | Premio de El Profeta: búho dorado | 750×1000 | premio de El Profeta: búho dorado | [enlace](https://static.wikia.nocookie.net/harrypotter/images/6/68/Daily_prophet_owl.jpg) |
| 7 | El Profeta P5: The boy who lies | 1024×1620 | cabecera P5 (propaganda): qué NO | [enlace](https://static.wikia.nocookie.net/harrypotter/images/e/eb/Daily_prophet_the_boy_who_lies.jpg) |
| 8 | El Profeta P5: He who must not… | 900×1425 | cabecera P5: qué NO | [enlace](https://static.wikia.nocookie.net/harrypotter/images/4/4f/He_who_must_be_not_be_named_returns.jpg) |
| 9 | El Profeta P3: fuga de Azkaban | 920×1351 | **P3: «Escape from Azkaban!» con foto**: hueco de foto que se mueve | [enlace](https://static.wikia.nocookie.net/harrypotter/images/a/a8/DailyProphetAzkaban.png) |
| 10 | El Profeta P5: Dumbledore | 564×892 | P5, foto de Dumbledore en la portada | [enlace](https://static.wikia.nocookie.net/harrypotter/images/7/78/Campaign_to_discredit_Albus_Dumbledore_and_Harry_Potter.jpg) |
| 11 | Undesirable No. 1, P7 | 1200×1912 | P7, cartel de búsqueda: qué NO | [enlace](https://static.wikia.nocookie.net/harrypotter/images/1/10/Undesirable_no._1.jpg) |
| 12 | Anuncios del Ministerio, concepto | 785×956 | anuncios del Ministerio en El Profeta (concepto): pequeños avisos | [enlace](https://static.wikia.nocookie.net/harrypotter/images/d/d5/Ministry_Advertisements_From_The_Daily_Prophet_concept_art.jpg) |
| 13 | El Quisquilloso, doble portada | 2294×1679 | El Quisquilloso, dos portadas | [enlace](https://static.wikia.nocookie.net/harrypotter/images/c/c3/Quibbler_4.jpg) |
| 14 | El Quisquilloso con gafas espectrales | 1765×1200 | **El Quisquilloso con las gafas espectrales de regalo** | [enlace](https://static.wikia.nocookie.net/harrypotter/images/7/7a/Quibbler-Spectrospecs.jpg) |
| 15 | El Quisquilloso n.º 1 | 758×1060 | El Quisquilloso n.º 1 | [enlace](https://static.wikia.nocookie.net/harrypotter/images/1/1a/Quibbler_No1.png) |
| 16 | El Quisquilloso: Harry in hiding | 1537×2127 | El Quisquilloso P7 | [enlace](https://static.wikia.nocookie.net/harrypotter/images/e/ec/QuibblerWhereisTheChosenOne.jpg) |
| 17 | Vociferador, foto promo P2 | 1720×1416 | **el vociferador**: sobre rojo que habla | [enlace](https://static.wikia.nocookie.net/harrypotter/images/3/39/Howler_WB_F2_HowlerCloseUpPromo_Promo_100615_Land.jpg) |
| 18 | Ron recibe el vociferador P2 | 2100×1552 | Ron recibe el vociferador en el desayuno | [enlace](https://static.wikia.nocookie.net/harrypotter/images/7/7e/COS_HQ_still_Ron_Howler.jpg) |
| 19 | Carta de Hogwarts, promo P1 | 1778×2682 | **carta de Hogwarts con lechuza**: el aviso que llega sí o sí | [enlace](https://static.wikia.nocookie.net/harrypotter/images/8/81/Hogwarts_acceptance_letter_PSF_promo.jpg) |
| 20 | Carta a Harry, P1 | 1919×1054 | sobre de la carta, tinta verde | [enlace](https://static.wikia.nocookie.net/harrypotter/images/2/26/Letter_to_Harry.jpeg) |
| 21 | Tablón de Gryffindor, Pottermore | 1100×1100 | **el tablón de Gryffindor** (Pottermore): fieltro rojo, notas clavadas | [enlace](https://static.wikia.nocookie.net/harrypotter/images/0/0a/Gryffindor_Notice_Board.png) |
| 22 | Tablón de Gryffindor, retocado | 1624×1459 | el mismo, retocado | [enlace](https://static.wikia.nocookie.net/harrypotter/images/2/2d/GryffindorNoticeboard.jpg) |
| 23 | Aviso de libro perdido | 780×1308 | aviso de «libro perdido» escrito a mano | [enlace](https://static.wikia.nocookie.net/harrypotter/images/a/ae/PeterJamesLostBook.jpg) |
| 24 | Pared de decretos P5 | 1263×568 | pared de decretos P5 | [enlace](https://static.wikia.nocookie.net/harrypotter/images/5/5f/Educational_Decrees.png) |
| 25 | Decreto de Educación n.º 23 | 352×527 | decreto n.º 23: letra de cartel oficial | [enlace](https://static.wikia.nocookie.net/harrypotter/images/b/bf/Educational_Decree_Number_23.jpg) |
| 26 | Atril del búho, PAS | 2048×2048 | **atril del búho** (juego, 2048×2048): modelar en Blender | [enlace](https://static.wikia.nocookie.net/harrypotter/images/8/85/Lecturn_in_Great_Hall_PAS.png) |
| 27 | Atril del búho, recorte | 381×647 | atril del búho, recorte | [enlace](https://static.wikia.nocookie.net/harrypotter/images/a/a1/Dumbledore%27s_owl_podium.png) |
| 28 | El calcetín de Dobby | 547×325 | el calcetín de Dobby | [enlace](https://static.wikia.nocookie.net/harrypotter/images/e/e9/Dobby%27s_sock.png) |
| 29 | Mapa del Merodeador | 3709×2140 | Mapa del Merodeador abierto | [enlace](https://static.wikia.nocookie.net/harrypotter/images/1/1d/Marauder%27s_Map_OOTPG.jpg) |
| 30 | Mapa del Merodeador, portada | 988×1861 | portada del Mapa | [enlace](https://static.wikia.nocookie.net/harrypotter/images/a/a3/Marauder%27sMap.png) |
| 31 | Cartas y sello, exposición | 3600×2400 | cartas y lacre en una exposición | [enlace](https://static.wikia.nocookie.net/harrypotter/images/1/1b/Hpexhibit001.jpg) |
| 32 | Copa de los Tres Magos | 1480×1944 | copa de los Tres Magos | [enlace](https://static.wikia.nocookie.net/harrypotter/images/1/1d/Triwizard_Cup.png) |

**`hojas/fondos_01.jpg`** (F·)

| N.º | Qué es | Tamaño | Para qué | Original |
|---|---|---|---|---|
| 1 | Dumbledore en la mesa P1, velas | 1920×800 | **P1: Dumbledore da los avisos de pie en la mesa, entre velas** (sin atril) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/6/69/Dumbledore_speech.jpg) |
| 2 | Umbridge interrumpe, atril P5 | 1834×799 | **P5: el atril del búho con las alas abiertas**, Umbridge al lado | [enlace](https://static.wikia.nocookie.net/harrypotter/images/0/08/Umbridge_speech.jpg) |
| 3 | Discurso de inicio P6 | 1309×557 | P6: discurso de inicio (oscuro) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/5/54/Dumbledore%27s_1996_Start-of-term_speech_HBPF.jpg) |
| 4 | Dumbledore y el cáliz P4 | 1200×798 | P4: Dumbledore junto al cáliz | [enlace](https://static.wikia.nocookie.net/harrypotter/images/e/ee/Albus_Dumbledore_before_presenting_the_Goblet_of_Fire.jpg) |
| 5 | Mesa de profesores P5 | 1599×749 | mesa de profesores P5 | [enlace](https://static.wikia.nocookie.net/harrypotter/images/d/dd/Professors_at_the_Start-of-Term_Feast_OOTP.PNG) |
| 6 | Banquete de inicio P5 | 1280×532 | banquete de inicio P5: las cuatro mesas | [enlace](https://static.wikia.nocookie.net/harrypotter/images/6/62/1995_Start-of-Term_Feast_1.jpg) |
| 7 | Leen El Profeta en el Gran Comedor P3 | 1920×800 | **P3: alumnos de Gryffindor leen El Profeta en el Gran Comedor** | [enlace](https://static.wikia.nocookie.net/harrypotter/images/8/8c/Gryffindor_students_reading_the_Daily_Prophet_POAF.PNG) |
| 8 | Correo del desayuno, Pottermore | 1278×500 | **el correo del desayuno: lechuzas sobre la mesa** (Pottermore) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/f/f6/B4C28M1_Hermione_opening_hate_mails.jpg) |
| 9 | Hedwig trae el correo, Pottermore | 5152×1866 | **Hedwig trae el correo a la sala común** (Pottermore) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/9/91/B4C14M2_Hedwig%27s_Gryffindor_Common_Room_delivery.png) |
| 10 | Gryffindor gana la copa, Pottermore | 4120×1536 | Gryffindor gana la copa: estandartes rojos | [enlace](https://static.wikia.nocookie.net/harrypotter/images/6/63/B1C17M3_Gryffindor_winning_the_House_Cup.jpg) |
| 11 | Gran Comedor de noche, velas | 1620×1708 | **Gran Comedor de noche con velas flotando**: fondo del concepto B | [enlace](https://static.wikia.nocookie.net/harrypotter/images/c/c6/B1-background.jpg) |
| 12 | Gran Comedor, Studio Tour, Navidad | 2048×1365 | Gran Comedor del Studio Tour (Navidad 2022) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/2/2a/Great_Hall_Table.png) |
| 13 | Gran Comedor de día | 1280×640 | Gran Comedor de día: luz de mañana (concepto A) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/3/3e/Great_hall.jpg) |
| 14 | Banquete de Halloween P1 | 1920×800 | banquete de Halloween P1: calabazas | [enlace](https://static.wikia.nocookie.net/harrypotter/images/f/fa/Hallowe%27en_Feast.jpg) |
| 15 | Banquete de Navidad, Pottermore | 4120×1536 | banquete de Navidad (Pottermore) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/b/bf/B1C12M2_Christmas_feast_at_Hogwarts.jpg) |
| 16 | Clases de Aparición, Pottermore | 3834×1500 | clases de Aparición: el aviso del libro 6 | [enlace](https://static.wikia.nocookie.net/harrypotter/images/a/a4/B6C18M1_Apparition_lessons_in_the_Great_Hall.png) |
| 17 | Sala común de Gryffindor, Pottermore | 4120×1536 | **sala común de Gryffindor** (Pottermore): mesa con pergaminos | [enlace](https://static.wikia.nocookie.net/harrypotter/images/8/89/B1C11M1_Gryffindor_Common_Room_PM.jpg) |
| 18 | Sala común, chimenea, Pottermore | 4120×1536 | sala común con chimenea (Pottermore) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/f/f4/B1C13M1_Gryffindor_CommonRoom1_PM.jpg) |
| 19 | Sala común, Hogwarts Legacy | 1540×848 | sala común en Hogwarts Legacy | [enlace](https://static.wikia.nocookie.net/harrypotter/images/4/4c/Gryffindor_common_room_HL.jpeg) |
| 20 | El trío en la sala común P6 | 2100×1401 | el trío en la sala común P6 | [enlace](https://static.wikia.nocookie.net/harrypotter/images/9/99/The_trio_relaxing_in_the_common_room.jpg) |
| 21 | Chimenea de la sala común | 3965×1500 | chimenea de la sala común | [enlace](https://static.wikia.nocookie.net/harrypotter/images/1/1e/B2C18M1_Sword_of_Gryffindor_engraving.png) |
| 22 | Lluvia de cartas en Privet Drive | 4098×1536 | **lluvia de cartas en Privet Drive** | [enlace](https://static.wikia.nocookie.net/harrypotter/images/d/db/B1C3M1_Hogwarts_letters_privet_drive.jpg) |
| 23 | Carruaje de Hogwarts P5 | 1765×799 | **el carruaje de P5 donde Luna lee El Quisquilloso** | [enlace](https://static.wikia.nocookie.net/harrypotter/images/f/fa/Fifth_year_Hogwarts_carriage.jpg) |
| 24 | Cartas de fans de Lockhart | 4140×1493 | mesa llena de cartas de fans | [enlace](https://static.wikia.nocookie.net/harrypotter/images/1/1b/B2C7M2_Harry_replying_to_Lockhart%27s_fan_mail.png) |
| 25 | Elfos en las cocinas | 3676×1500 | elfos en las cocinas: el mundo de Dobby | [enlace](https://static.wikia.nocookie.net/harrypotter/images/6/63/B4C21M2_House-elves_in_Hogwarts_kitchens.png) |
| 26 | Cabeza de Puerco, 1.ª reunión | 3684×1500 | Cabeza de Puerco: primera reunión del ED | [enlace](https://static.wikia.nocookie.net/harrypotter/images/c/ce/B5C16M1_First_meeting_in_the_Hog%27s_Head.png) |
| 27 | Castillo de noche | 1920×1080 | el castillo de noche | [enlace](https://static.wikia.nocookie.net/harrypotter/images/1/11/Hogwarts_Castle_%E2%80%93_HPatPS.jpg) |
| 28 | Gran Comedor vertical, PAS | 1080×2307 | Gran Comedor vertical (PAS): lámina alta | [enlace](https://static.wikia.nocookie.net/harrypotter/images/f/f0/Great_Hall_2_-_PAS.png) |
| 29 | Baile de Navidad, Pottermore | 3224×1316 | baile de Navidad (Pottermore) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/4/4c/B4C23M1_Weird_Sisters_playing_at_the_Yule_Ball.png) |
| 30 | San Valentín en el Gran Comedor | 4140×1500 | San Valentín en el Gran Comedor: qué NO (cursi) | [enlace](https://static.wikia.nocookie.net/harrypotter/images/5/52/B2C13M2_Lockhart%27s_Valentine%27s_Day_Great_Hall_decoration.png) |
| 31 | Club de duelo | 4140×1500 | club de duelo | [enlace](https://static.wikia.nocookie.net/harrypotter/images/7/7e/B2C11M2_Great_Hall_Duelling_Club.png) |
| 32 | Marca Tenebrosa (qué NO) | 1462×824 | Marca Tenebrosa: **qué NO** | [enlace](https://static.wikia.nocookie.net/harrypotter/images/8/89/B4C9M1_Dark_Mark_PM.png) |

**Lo mejor de cada hoja, en una línea**
- Para **presentar o explicar**: Dumbledore con la mano abierta (P·26, recortable) o con la varita en alto (P·24); Hermione con libros (P·2, recortable).
- Para **proclamar**: Dobby chasqueando los dedos (P·18) o en jarra (P·19).
- Para **el guiño del fan**: Luna con las gafas espectrales (P·11) o el sombrero de león (P·10).
- Para **el objeto**: El Profeta de P1 (O·2), el tablón (O·21), el atril (O·26, F·2), el vociferador (O·17).
- Para **el sitio**: el correo del desayuno (F·8), el Gran Comedor de noche (F·11), la sala común (F·17).
- **Licencia**: todo © Warner Bros. / Wizarding World. Sólo referencia; no pegar.

### 2.1 Los papeles de MinaLima (el estudio del grafismo de las películas)
MinaLima es Miraphora Mina y Eduardo Lima. Hicieron **todos** los papeles
de las ocho películas: El Profeta, cartas, decretos, el Mapa del Merodeador.
([HP Fan Zone](https://www.harrypotterfanzone.com/exclusive-meet-minalima-part-1/),
[New Statesman](https://www.newstatesman.com/culture/2015/12/graphic-art-harry-potter-films-two-designers-bringing-fiction-life),
[Wikipedia](https://en.wikipedia.org/wiki/MinaLima))

Portadas de El Profeta que venden como láminas (sólo referencia). En la
segunda pasada bajé la imagen de cada una (3000×3000, medida) y **las miré**:
- [«Boy Who Lived»](https://minalima.com/product/the-daily-prophet-boy-who-lived/)
  ([imagen](https://media.minalima.com/2025/01/thumb-p61lpr.jpg)): **es de P5**
  (lo dice la lámina: «Harry Potter and the Order of the Phoenix»). Cabecera
  «DAILY PROPHET» de palo grueso con la P dorada. Papel `#E8E0D4`, tinta
  `#030202` (medidos). **No es la época alegre** (antes lo puse mal).
- [Recopilación de portadas](https://minalima.com/product/art-print-the-daily-prophet-compilation/)
  ([imagen](https://media.minalima.com/2025/04/thumb-p141lpr.jpg)): 9
  portadas de P3 a P7. Se ve el cambio: **P3 «Escape from Azkaban!» con la
  cabecera gótica adornada** → desde P5, «DAILY PROPHET» de palo con el escudo
  alado. Es la mejor chuleta para elegir época.
- [«Mass Breakout from Azkaban»](https://minalima.com/product/the-daily-prophet-mass-breakout-from-azkaban/): P5, época oscura.
- [«Undesirable No. 1»](https://minalima.com/product/the-daily-prophet-undesirable-number-1/): P7, propaganda.
- [«Dumbledore's Dark Secrets Revealed»](https://minalima.com/product/the-daily-prophet-dumbledores-dark-secrets-revealed/): P7.
- [Decretos y proclamas del Ministerio](https://minalima.com/ministry-of-magic-collection/) y la [proclama n.º 85](https://minalima.com/product/proclamation-no-85/)
  ([imagen](https://media.minalima.com/2025/01/thumb-p28lpr-2025.jpg)):
  papel amarillo `#E4CE93`, tinta `#6D5C3F`, el número en rojo `#B81714`
  (medidos). Mano que señala «☞ No.», palos rectos, firma roja de Umbridge.
- [El Mapa del Merodeador](https://minalima.com/product/the-marauders-map/) y el [vociferador de Ron](https://minalima.com/product/art-print-ron-weasleys-howler/)
  ([imagen](https://media.minalima.com/2019/01/thumb-ron-howler-print-scaled.jpg),
  2560×2560): sobre rojo `#B12E38` con etiqueta «Ronald Weasley, Hogwarts
  School of Witchcraft & Wizardry»; la carta, en caligrafía de tinta roja
  sobre papel `#EFE1CF`, **y al final una posdata en tinta dorada**: «Oh, and
  Ginny, dear, congratulations on making Gryffindor». Un grito con una posdata
  amable: buena idea para un aviso.

### 2.2 Fotos del decorado real (Studio Tour de Londres, en Wikimedia Commons)
Licencia, autor y tamaño comprobados con la API de Commons ✅:
- Atril del búho con el traje de Dumbledore:
  [foto 1](https://upload.wikimedia.org/wikipedia/commons/2/21/Professor_Dumbledore_and_The_Owl_Podium_%287119146507%29.jpg) (1978×2976, vertical),
  [foto 2](https://upload.wikimedia.org/wikipedia/commons/1/1f/Professor_Dumbledore_and_The_Owl_Podium_%287119147107%29.jpg) (2920×1951).
  **CC BY 2.0**, Rob Young, 27-abr-2012.
- Gran Comedor:
  [05](https://upload.wikimedia.org/wikipedia/commons/b/b1/Hogwart%E2%80%98s_Great_Hall%2C_Warner_Bros_Harry_Potter_Studio%2C_London_05.jpg),
  [07](https://upload.wikimedia.org/wikipedia/commons/1/17/Hogwart%E2%80%98s_Great_Hall%2C_Warner_Bros_Harry_Potter_Studio%2C_London_07.jpg)
  (4608×3456 cada una), y [su categoría](https://commons.wikimedia.org/wiki/Category:Warner_Bros._Studio_Tour_London_(great_hall)).
  **CC BY-SA 4.0**, Ank Kumar, 3-mar-2013.
- [Sala común de Gryffindor](https://upload.wikimedia.org/wikipedia/commons/7/7f/Gryffindor_Common_Room_at_Warner_Bros._Studio_Tour_London.jpg)
  (4320×3240). **CC BY 2.0**, Robert Clarke, 20-jul-2012.
- [Maqueta de Hogwarts](https://upload.wikimedia.org/wikipedia/commons/4/4d/Studio_model_of_Hogwarts_at_Leavesden_Studios.jpg)
  (6000×4000). **CC BY-SA 4.0**, CapStudio (Clementp.fr), 11-dic-2020.
- Crédito: «Foto: <autor>, Wikimedia Commons, <licencia>». Son fotos del
  decorado: el diseño sigue siendo de Warner.

### 2.3 Arte de los videojuegos
- **Magic Awakened** (NetEase): estilo de **libro ilustrado antiguo**. Hay
  niveles hechos como páginas de libro.
  [Entrevista al director creativo](https://www.harrypotter.com/features/behind-harry-potter-magic-awakened-with-creative-director-justin-webb-interview) ·
  [diario de desarrollo del arte](https://www.youtube.com/watch?v=Z_BJLuv5WiI) ·
  [entrevista al artista jefe](https://www.youtube.com/watch?v=kBeIPiTRVuw).
- **Hogwarts Legacy** (Avalanche): el director de arte, Jeff Bunker, releyó
  los libros muchas veces. Estética victoriana.
  [Preguntas a los expertos](https://www.harrypotter.com/features/hogwarts-legacy-interviews-with-the-experts) ·
  [el libro de arte](https://www.harrypotter.com/news/exploring-the-art-and-making-of-hogwarts-legacy) ·
  [arte conceptual en Game Rant](https://gamerant.com/hogwarts-legacy-concept-art-developer-interview/).

### 2.4 La wiki de Fandom (hecho en la segunda pasada)
Comandos que corrí (las hojas numeradas quedan en `herramientas/referencias/`,
que git ignora):

```
python3 herramientas/investigar_serie.py --serie "Harry Potter" --wiki harrypotter \
  --paginas "Hermione Granger" "Luna Lovegood" "Dobby" "Albus Dumbledore" \
  "Harry Potter" "Ronald Weasley" "Severus Snape" "Minerva McGonagall"
python3 herramientas/investigar_serie.py --serie "Harry Potter objetos" --wiki harrypotter \
  --paginas "Daily Prophet" "Owl Lecturn" "Gryffindor Notice Board" "Great Hall" \
  "The Quibbler" "Educational Decree" "Howler" "Marauder's Map" \
  "Gryffindor Common Room" "Hogwarts acceptance letter" "Spectrespecs" "Sock"
```

Lo que dice el texto de la wiki y sirve:
- [Owl Lecturn](https://harrypotter.fandom.com/wiki/Owl_Lecturn): **primera
  aparición, la película 3**. En los libros Dumbledore sólo se pone de pie. Lo
  usan también Umbridge (P5), Rita Skeeter y McGonagall en *Hogwarts Mystery*.
  Hay arte conceptual de P8 con **Snape director en el atril** ✅ (wiki + clip).
- [Gryffindor Notice Board](https://harrypotter.fandom.com/wiki/Gryffindor_Notice_Board):
  objetos perdidos, cromos, pruebas de quidditch, salidas a Hogsmeade,
  orientación profesional, clases de Aparición, los decretos de Umbridge y
  **«cada día se clavaban ahí el último Profeta y El Quisquilloso»** ⚠️ (la
  wiki no dice de qué fuente sale esa frase). Sale en las películas 1-6 como
  decorado, en los juegos y en Pottermore. **En P1 lo vi** (mañana de
  Navidad, 1080p, §3) ✅.

### 2.5 Libros ilustrados y portadas (2.ª pasada)
Buscados en el espacio de archivos de la wiki y **mirados**; tamaño por la
API. Todo © Bloomsbury / Salamandra / Jim Kay: sólo referencia.

| Qué es | Tamaño | Para qué |
|---|---|---|
| [Neville y Luna, de Jim Kay](https://static.wikia.nocookie.net/harrypotter/images/f/fc/OOTPIE_-_Neville_and_Luna.png) (libro 5 ilustrado) | 2000×2362 | **Luna con El Quisquilloso abierto** entre las manos: otro estilo para el concepto A |
| [Dobby, de Jim Kay](https://static.wikia.nocookie.net/harrypotter/images/b/b5/Dobby_-_Jim_Kay_COS_IE.jpg) (libro 2 ilustrado) | 1330×1571 | Dobby sentado en la cama, funda de almohada |
| [Hermione con varita y farol, de Jim Kay](https://static.wikia.nocookie.net/harrypotter/images/1/1a/Hermione_Granger_-_PS_IE.jpg) (libro 1 ilustrado) | 4494×5248 | Hermione ilustrada, luz de farol azul |
| [Dumbledore, de Jim Kay](https://static.wikia.nocookie.net/harrypotter/images/5/5c/Albus_Dumbledore_by_Jim_Kay_-_PS_IE.jpeg) | 527×610 | retrato con cartela «Albus Dumbledore» arriba: un rótulo del mundo |
| [Portada del libro 2 ilustrado](https://static.wikia.nocookie.net/harrypotter/images/7/7a/Bloomsbury_02_COSIE_cover_-_Jim_Kay.jpg) (Bloomsbury) | 2741×3225 | el Ford Anglia sobre el campo: luz de día |
| [Portada de Salamandra, libro 1](https://static.wikia.nocookie.net/harrypotter/images/1/1f/Spanish_01_PS.jpg) | 1594×2541 | la portada en español: «Harry Potter y la piedra filosofal» con el logo |
| [Salamandra, libro 5 (15.º aniversario)](https://static.wikia.nocookie.net/harrypotter/images/e/e4/Spanish_15th_anniversary_05_OOTP.jpg) | 1614×2603 | el trío en azul: tono oscuro, qué NO |

Los carteles de cine en alta no los busqué: los promos de §2.0 cubren lo
mismo.
---

## 3 · Escenas icónicas con su minuto

**De dónde sale el minuto**: subtítulos en inglés de las 8 películas, en
[este repositorio público de GitHub](https://github.com/sydney-machine-learning/sentimentanalysis-Hollywood).
Ejemplo: [película 1](https://raw.githubusercontent.com/sydney-machine-learning/sentimentanalysis-Hollywood/main/Year/2001/Harry%20Potter%20and%20the%20Sorcerer%27s%20Stone.srt).
Es el momento en que se dice la frase. Con la versión extendida o la de la
tele puede moverse uno o dos minutos.

**Lo que vi (2.ª pasada):** 5 escenas, el comienzo y el final, en los clips
del canal oficial «Harry Potter» de YouTube, por sus *storyboards* (§12).
Donde hay clip, va el enlace `&t=` al segundo exacto (±2 s). El fotograma
grande para recortar sale del Blu-ray o de las capturas de la wiki (§2.0).

Películas: **P1** La piedra filosofal · **P2** La cámara secreta ·
**P3** El prisionero de Azkaban · **P4** El cáliz de fuego ·
**P5** La Orden del Fénix · **P6** El misterio del príncipe ·
**P7** Reliquias 1 · **P8** Reliquias 2.

### Las que sirven para #anuncios

| Peli | Minuto | Qué pasa (lo visto o lo dicho) | Para qué |
|---|---|---|---|
| P1 | 00:03:08 a 00:03:37 | Dumbledore deja **una carta** sobre el bebé en la puerta de Privet Drive. Sobre de pergamino, tinta verde: «Mr. and Mrs. Dursley, 4 Privet Drive…». Después, el título dorado sobre nubes ([clip oficial 3:08](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=188), [3:23](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=203), [3:37](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=217)) ✅ visto | El primer «aviso» de la saga es una carta. |
| P1 | 00:42:20 a 00:42:50 | Dumbledore, **de pie en la mesa de profesores, entre velas** (F·1): «I have a few start-of-term notices…». Prohíbe el Bosque Oscuro y el pasillo del tercer piso «a quien no desee sufrir una muerte muy dolorosa». En P1 **no hay atril del búho** ✅ (F·1 + wiki). Subtítulo oficial de HBO Max: «Los de primer año deben saber que el bosque oscuro está estrictamente prohibido» ([tráiler 1:12](https://www.youtube.com/watch?v=ZgrCZVjPg9g&t=72)). **Visto en vídeo real** (tráiler oficial de 2001, 720p, [1:15](https://archive.org/download/harry-potter-and-the-sorcerers-stone-2001-720p-trailer/Harry%20Potter%20and%20the%20Sorcerers%20Stone_2001_720p_trailer.mp4#t=75)): Harris **de pie en el centro de la mesa**, brazos caídos dentro de la túnica, copa dorada delante; McGonagall sentada a su derecha, de terciopelo verde; velas blancas en candelabros sobre la mesa; detrás, paneles de madera y ventanales de rombos azul noche ✅ | **Un anuncio oficial en el mundo de la serie.** Concepto B. |
| P1 | 00:53:45 | «Mail's here»: entran las lechuzas al desayuno. | El correo cae en la mesa. Concepto A. |
| P1 | 00:54:38 a 00:54:57 | Leen El Profeta en voz alta: robo en Gringotts, cámara 713. Responde Harry: «That's the vault Hagrid and I went to». Lo lee **Harry**: a él no le llega correo, **le pide el diario a Ron** («Can I borrow this?») y lo lee en voz alta ✅ (wiki de la película + [guion transcrito de Moviepedia](https://movies.fandom.com/wiki/Harry_Potter_and_the_Philosopher%27s_Stone/Transcript)). No encontré clip oficial de la escena. La portada de ese número: O·2. | **El Profeta sobre la mesa del Gran Comedor.** Concepto A. |
| P1 | 00:09:50 a 00:12:00 | «No more mail through this letterbox»; luego la lluvia de cartas por la chimenea (F·22). | Las novedades llegan sí o sí. |
| P1 | ≈01:28:10 a 01:28:45 | Mañana de Navidad en la sala común: Harry se prueba la capa (01:28:20). **Detrás, el tablón de anuncios de Gryffindor**: fieltro rojo oscuro con una **cuadrícula de cintas finas**, **borde de cordón trenzado rojo y oro**, tarjetas de Navidad y notas a mano clavadas; al lado, el tapiz del unicornio con collar de lunas. Visto en 1080p (fragmento académico TECHNÈS, Univ. de Montreal, [0:14](https://archive.org/download/670343/colombus_harry_potter_philosophers_stone_extrait.HD.mp4#t=14), [0:20](https://archive.org/download/670343/colombus_harry_potter_philosophers_stone_extrait.HD.mp4#t=20), [0:29](https://archive.org/download/670343/colombus_harry_potter_philosophers_stone_extrait.HD.mp4#t=29)) ✅ | **El tablón real de las películas.** Concepto C. |
| P1 | 02:19:16 | Dumbledore da los últimos puntos: 50 para Hermione. | Celebrar. |
| P2 | 00:34:11 a 00:34:56 | El vociferador en el desayuno: **se abre el sobre rojo** ([clip 0:17](https://www.youtube.com/watch?v=fBziSx7RtqY&t=17)), **se levanta de la mesa y es una boca con dientes de papel** ([0:25](https://www.youtube.com/watch?v=fBziSx7RtqY&t=25)), grita a Ron a la cara ([0:39](https://www.youtube.com/watch?v=fBziSx7RtqY&t=39)) y **se rompe en confeti** sobre libros abiertos ([0:57](https://www.youtube.com/watch?v=fBziSx7RtqY&t=57)) ✅ visto. **En 1080p** (vídeo «en 23 idiomas», §12): el sobre en la mano con etiqueta de caligrafía «Ronald Weasley, Hogwarts School of Witchcraft & Wizardry» ([0:16](https://www.youtube.com/watch?v=3KNNglv24a0&t=16)); la boca de papel con dientes y el texto de la carta dentro ([0:26-0:28](https://www.youtube.com/watch?v=3KNNglv24a0&t=26)); Ron con los ojos muy abiertos, encogido ([0:32](https://www.youtube.com/watch?v=3KNNglv24a0&t=32)). En latino: «**¡Ronald Weasley! ¡Cómo osaste robar el auto!**» ([15:55-16:03](https://www.youtube.com/watch?v=3KNNglv24a0&t=955), §10.3) ✅ | Otro «cuadro» que habla. En latino se llama **vociferador**. |
| P2 | 02:25:12 a 02:26:30 | «Master has given Dobby a sock. Dobby is free.» Dobby **alarga un dedo hacia el calcetín** con media sonrisa pícara; luego **se planta delante de Harry**, pies separados y palmas abiertas, ante Lucius («You shall not harm Harry Potter», 02:25:41); al final, primer plano con la **cabeza ladeada y los ojos húmedos**. Visto en vídeo real (copia de fan en Dailymotion, audio francés, 512×216: [3:00](https://www.dailymotion.com/video/x3d4quh?start=180), [3:20](https://www.dailymotion.com/video/x3d4quh?start=200), [4:00](https://www.dailymotion.com/video/x3d4quh?start=240)) ✅ | La libertad de Dobby: celebrar. |
| P3 | 00:10:36 | En el autobús noctámbulo, la foto de Sirius Black se mueve en El Profeta. | **La foto que se mueve.** |
| P3 | 00:23:44 a 00:25:45 | **El atril del búho, por primera vez.** Dumbledore **abre los brazos** tras las alas doradas: «Welcome! Welcome to another year at Hogwarts» ([clip 0:43](https://www.youtube.com/watch?v=dvFehFzph7I&t=43)); presenta a Lupin ([1:05](https://www.youtube.com/watch?v=dvFehFzph7I&t=65)); **alza los dos índices**: «happiness can be found… if one only remembers to turn on the light» ([2:42](https://www.youtube.com/watch?v=dvFehFzph7I&t=162)) y **apaga una vela con los dedos** ([2:48](https://www.youtube.com/watch?v=dvFehFzph7I&t=168)) ✅ visto | **El discurso desde el atril.** Concepto B. |
| P3 | 00:24:21 a 00:24:39 | **Anuncia a Hagrid como nuevo profesor**: «I'm delighted to announce… that his place will be taken by none other than our own Rubeus Hagrid». Dumbledore tras el atril ([clip 1:31-1:39](https://www.youtube.com/watch?v=dvFehFzph7I&t=91)), Hagrid se levanta en la mesa de profesores ([1:41-1:53](https://www.youtube.com/watch?v=dvFehFzph7I&t=101)) y **el comedor aplaude** ([1:55-1:57](https://www.youtube.com/watch?v=dvFehFzph7I&t=115)) ✅ visto (*storyboard* 160×90) y subtítulo inglés | **Un anuncio que alegra**: el tono justo para #anuncios. «Me complace anunciar» es la fórmula. |
| P3 | 00:57:24 y 00:58:15 | «I solemnly swear…» y «Mischief managed» con el Mapa. | El pergamino que se escribe solo. |
| P3 | créditos | Cada nombre va en **una cinta de pergamino dibujada a tinta**, con huellas que caminan (copia de fan, no oficial: [0:11](https://www.youtube.com/watch?v=MJzymmFvtlk&t=11)) ✅ visto | Un cuadro de texto que es de la serie. |
| P4 | 00:16:31 a 00:17:02 | Dumbledore: «I'd like to make an announcement». Anuncia el Torneo. | **Otro anuncio desde el atril** (la wiki lo lista en P4). |
| P4 | 00:20:04 | «Eternal glory». | Presentar con énfasis. |
| P4 | 01:06:47 a 01:07:20 | **McGonagall anuncia el baile de Navidad** a los de Gryffindor. En latino: «La víspera de Navidad, junto con nuestros invitados, nos reunimos en el gran salón para una noche de recatada frivolidad» (§10.3) ✅ | Un aviso del staff, con humor. |
| P5 | 00:29:41 a 00:30:06 | Luna en el carruaje: lee **El Quisquilloso tapándose la cara** ([clip 0:59](https://www.youtube.com/watch?v=8k2bj-R9m8E&t=59)) y **mira a Harry por encima** ([1:09](https://www.youtube.com/watch?v=8k2bj-R9m8E&t=69)) ✅ visto. En vídeo real (Dailymotion, 512×288, [0:48](https://www.dailymotion.com/video/x3dhmzl?start=48)): **la revista está al revés**, con el título «QUIBBLER» abajo y boca abajo; botas de agua rojas ([0:44](https://www.dailymotion.com/video/x3dhmzl?start=44)) ✅ (y la wiki lo cita del libro 5) | Luna y su revista. |
| P5 | 00:50:13 | Umbridge cita el «Decreto de Educación n.º 23». | Los decretos clavados. |
| P5 | 00:54:01 | Hermione abre la primera reunión del ED. En latino: «**Ya saben a qué vinieron**» (§10.3) ✅ | Explicar a un grupo. |
| P5 | ≈01:34:20 | Examen de los TIMOS en el Gran Comedor (justo antes de los gemelos, 01:34:39). En latino, **una voz lee el cartel**: «Silencio. TIMOS en progreso. Examen de teoría de encantamientos. Comienza a las 16 horas, termina a las 18» (§10.3) ✅ oído | **Un aviso oficial leído en voz alta.** |
| P5 | 02:03:25 a 02:04:35 | Tras «He's back», los titulares de El Profeta giran en pantalla. En latino **el narrador los lee**: «Dumbledore y Potter reivindicados. ¿Renunciará el ministro? … Director de Hogwarts, restituido» (§10.3) ✅ oído | **El Profeta, dicho en voz alta.** |
| P6 | ≈00:03:15 | En un café muggle, Harry lee El Profeta con su foto. En latino, la voz de los insertos: «**Harry Potter, el elegido.** Se derrumba puente. Aumenta el número de muertos» (§10.3) ✅ oído | Titular leído en voz alta (tono oscuro). |
| P6 | 00:22:36 a 00:22:57 | Luna reparte El Quisquilloso («Quibbler… Quibbler…») y explica los *wrackspurts*. Es **en el pasillo del expreso de Hogwarts**: la wiki lo dice en las diferencias libro-película («Luna is seen in the corridor selling issues of the Quibbler») y el guion transcrito dice «She runs down the aisle with the magazine in her hand» ([Moviepedia](https://movies.fandom.com/wiki/Harry_Potter_and_the_Half-Blood_Prince/Transcript)) ✅ | Luna repartiendo prensa. |
| P7 | 00:32:51 | Xenophilius Lovegood: El Quisquilloso frente a El Profeta. | Prensa libre contra prensa oficial. |
| P7 | 02:08:59 a 02:09:18 | Dobby: «Dobby has no master. Dobby is a free elf». En latino: «**Dobby no tiene amo. Dobby es un elfo libre**» (§10.3) ✅ | Una proclama. |
| P8 | 00:35:09 a 00:36:33 | Snape, director, reúne al colegio. En latino: «Si cualquiera, estudiante o maestro, pretendiera ayudar al señor Potter, será castigado…» (§10.3) ✅ | Aviso del «staff», en tono oscuro: **qué NO**. |
| P8 | 01:34:46 a 01:35:18 | King's Cross blanco. Dumbledore: «Help will always be given at Hogwarts…» y «Words are, in my not so humble opinion…». En latino: «**Siempre se ayudará en Hogwarts, Harry, a quienes lo pidan**» (§10.3) ✅ | La frase amable para el pie de la lámina. |
| P8 | final | «19 años después»: andén 9¾, el expreso rojo con vapor ([clip 0:51](https://www.youtube.com/watch?v=yv-UwwOvOzA&t=51)), jaulas de lechuza en los carritos ([0:15](https://www.youtube.com/watch?v=yv-UwwOvOzA&t=15)) ✅ visto | Cierre, despedida. |

---

## 4 · Fan art y 3D (sólo como referencia)

### Modelos 3D descargables

Licencias y autores **comprobados con la API de Sketchfab** (24-sep-2026) ✅.

| Modelo | Autor | Licencia (API) | Caras | Para qué |
|---|---|---|---|---|
| [Gran Comedor](https://sketchfab.com/3d-models/the-great-hall-in-hogwarts-harry-potter-aa65c92e370f464ba81080cae44ab71f) | s23383 | CC BY | 98 046 | fondo A y B |
| [Gran Comedor 2](https://sketchfab.com/3d-models/hogwarts-grand-hall-203784d1e8704cfba3af8a2b224b74ff) | zack_graham | CC BY | 25 913 | alternativa |
| ~~Gran Comedor con velas animadas~~ (JER3D) | — | **ya no existe** (404) | — | — |
| [**Periódico doblado**](https://sketchfab.com/3d-models/4fc14ea5129b4ea3b34a22844a6f1b3f) | abdillaamy | CC BY | 1 162 | **base de El Profeta doblado** (concepto A): poner la portada como textura |
| [Periódico](https://sketchfab.com/3d-models/84683791c7e74992b8f2baeb52595de6) | JeremyGrayson | CC BY | 11 674 | periódico abierto |
| [Búho con 9 animaciones, vuela](https://sketchfab.com/3d-models/owl-d177e1fbcce940cba32e434cc5a62f1a) | po (@pothedev) | CC BY | 15 428 | lechuza del correo |
| [Lechuza low poly](https://sketchfab.com/3d-models/eggbert-low-poly-barn-owl-d96c7d6d405b4b71aeac3f62757ebeac) | LachieRobertson | CC BY | 3 716 | lechuza de fondo |
| [Búho dorado](https://sketchfab.com/3d-models/621580dcef944845b59f6dee69b5b8b2) | vjgsiongd | CC BY | 785 902 | punto de partida para **el atril del búho** (abrirle las alas) |
| [Pergamino](https://sketchfab.com/3d-models/parchment-paper-10e53ca757a2482d8fe1bc94e9043826) | Claire Combs | CC BY | 27 648 | hoja del atril |
| [Pluma](https://sketchfab.com/3d-models/quill-67771bc3f8024e6faea9af9f6f7d6bfb) | FlukierJupiter | CC BY | 400 | primer plano |
| [Pluma en tintero](https://sketchfab.com/3d-models/quill-in-inkwell-7968ef86540d431ebba1e8597e4122b0) | Valo Niskanen | CC BY-NC | 1 282 | sólo si no es comercial |
| [Velas](https://sketchfab.com/3d-models/92bb9f59fd9046b1beb9dca6b21489e2) | thegraphicsgeek | CC BY | 22 564 | velas flotantes |
| [Tablón de corcho](https://sketchfab.com/3d-models/cork-board-9534ee2ad4344ea6b02b95b61bd4a913) | rickmaolly | **CC BY** (antes dudoso) | 41 684 | concepto C (cambiar corcho por fieltro rojo) |
| [Tablón medieval](https://sketchfab.com/3d-models/566a4332b57d4045a1cc4ffec77b4b8f) | avelium | CC BY | 2 472 | marco de madera para el tablón |
| [Sello de lacre](https://sketchfab.com/3d-models/bd18fd7b6c1847bc8e7d9e779c122ed5) | plaggy | CC BY | 332 | lacre del aviso oficial |
| [Varita de Saúco](https://sketchfab.com/3d-models/the-elder-wand-efc7362a857749b3ae55fcbbba8baafb) | James Allison | CC BY | 1 664 | varita de Dumbledore |
| [Carta de Hogwarts con lechuza](https://sketchfab.com/3d-models/harry-potter-acceptance-letter-d96d1f11fc4c4a9180718ae604e71cf9) | antonia_s | sin licencia, no descargable | 29 000 | sólo mirar |
| [Vociferador](https://sketchfab.com/3d-models/howler-card-4331889cf315488e8cd49cf2e0a94a48) | luismi93 | «Editorial», no descargable | 184 096 | sólo mirar |

Crédito exacto para las CC BY: «Modelo "<nombre>" de <autor>, Sketchfab,
CC BY».

**No encontré** un modelo de El Profeta ni del atril del búho con licencia
libre (búsquedas en la API: «daily prophet» sin resultados; «owl lectern»,
sólo atriles genéricos). Solución: el periódico doblado de abdillaamy con la
portada como textura, y el atril a partir del búho dorado y las fotos CC BY
del Studio Tour (§2.2).

### Fan art y renders (mirar, nunca pegar)
- [Castillo gótico con luz de Hogwarts Legacy](https://www.artstation.com/artwork/XJ98vY), de Jesús Arroyo Jiménez: luz cálida en piedra.
- [Concepto de interfaz de Hogwarts Legacy](https://www.artstation.com/artwork/Pe48r3).
- [Concepto de letra del Mapa del Merodeador](https://www.deviantart.com/gothsavagebowserx/art/The-Marauder-s-Map-Font-Concept-1310537034), de GothSavageBowserX.
- Proyectos de El Profeta «con foto que se mueve» hechos por fans:
  [con Raspberry Pi](https://magazine.raspberrypi.com/articles/harry-potter-daily-prophet),
  [con papel electrónico](https://hackaday.com/2021/10/29/muggle-uses-e-paper-for-daily-prophet-replica/),
  [con realidad aumentada](https://github.com/lekhamirjankar/Daily-Prophet).

---

## 5 · Sitios, luz, paleta y texturas

> **Hex medidos con Pillow** (2.ª pasada) en fotogramas de los clips oficiales
> (*storyboards*, JPEG pequeño: ±10 por canal) y en arte oficial grande. Se
> dice de dónde sale cada uno. Los de la 1.ª pasada, a ojo, quedan tachados.

### El Gran Comedor (conceptos A y B)
- Mesas larguísimas de madera oscura, una por casa. Estandartes de las casas.
- **Velas flotando** y techo encantado que copia el cielo.
- En el Studio Tour se exponen el atril y el **contador de puntos de las
  casas** ([London Tickets](https://www.london-tickets.co.uk/warner-bros-studio-tour-london/great-hall/)).
- Luz (vista en el [clip de P3](https://www.youtube.com/watch?v=dvFehFzph7I&t=13)):
  **cientos de velas flotando** forman un techo de luz amarilla; los
  ventanales góticos del fondo dan un azul gris frío. De noche, la única luz
  es la de las velas: caras cálidas, fondo en sombra.
- Paleta medida:
  - luz de velas `#BFAE7C` y su penumbra `#6D5730` (clip P3, 0:47);
  - ventanales, luz fría `#989D92` y piedra `#3C382D` (clip P3, 0:59);
  - mesa y bandejas `#554832` / `#948F76` (clip P3, 1:09).
  - ~~piedra `#6B5E50` · madera `#4A2F1D` · llama `#FFB347` · cielo `#1C2541` · oro `#C9A43B`~~ (a ojo, 1.ª pasada).
- De mañana (desayuno, concepto A): mismas mesas, luz blanca de los
  ventanales (F·13) y en el [clip del vociferador](https://www.youtube.com/watch?v=fBziSx7RtqY&t=2)
  la mesa lleva **libros abiertos, bandejas y migas doradas**.

### El atril del búho (concepto B)
- Búho dorado **con las alas abiertas en horizontal**, sobre un pie
  retorcido; las velas del candelabro quedan detrás de las alas (F·2,
  [clip P3 0:57](https://www.youtube.com/watch?v=dvFehFzph7I&t=57)).
  **Sale desde P3**; en P1 y P2 no existe (§2.4).
- Oro medido en F·2 (1834×799): luz `#B4956C`, medio `#664B2F`, sombra
  `#3B2410`. En el clip de P3: brillo `#98885F`, medio `#42351A`.
- Está cubierto de **pan de oro de verdad** y de **años de cera derretida**
  ([London Tickets](https://www.london-tickets.co.uk/warner-bros-studio-tour-london/great-hall/),
  [Potterhead Posts en X](https://twitter.com/PotterheadPosts/status/1317918385825566720)) ✅.
- Fotos para modelarlo: sección 2.2.

### La sala común de Gryffindor (concepto C)
- Tapices rojos de flores y árboles (*millefleurs*), chimenea, butacas
  gastadas (O·21, F·17, F·18).
- Tiene un **tablón de anuncios**. En los libros se clavan ahí: libros de
  segunda mano, las normas de Filch, los entrenamientos de quidditch, cromos
  de ranas de chocolate, los anuncios de los gemelos Weasley, las salidas a
  Hogsmeade y objetos perdidos. En el libro 6 un cartel oficial de clases de
  Aparición **es tan grande que lo tapa todo**
  ([Harry Potter Wiki](https://harrypotter.fandom.com/wiki/Gryffindor_Notice_Board),
  [HP Lexicon](https://www.hp-lexicon.org/thing/notice-board/)) ✅.
- **El tablón oficial (Pottermore, O·21) es de fieltro rojo oscuro, no de
  corcho**, con marco de madera tallada casi negra.
- **El de la película 1** (visto en 1080p, [fragmento TECHNÈS, 0:14](https://archive.org/download/670343/colombus_harry_potter_philosophers_stone_extrait.HD.mp4#t=14)):
  también **fieltro rojo**, pero dividido en cuadros por **cintas finas
  oscuras** y rematado con un **cordón trenzado rojo y oro**. Tarjetas de
  Navidad y notas en papel crema, algunas torcidas. A su izquierda, el tapiz
  de flores con **un unicornio blanco con collar azul de lunas**; delante,
  butacas de terciopelo rojo. Luz de mañana de invierno, tenue y cálida.
  Medido en ese fotograma (con su penumbra): fieltro `#32100F`, cordón con
  luz `#704131`, tapiz `#401716`, butaca `#210D0F`.
- Paleta medida en O·21 (1100×1100): fieltro `#51201D`, marco `#1D120C` /
  `#32231B`, tapiz `#4A211C`, papel de las notas `#D7D2CB`.
  ~~rojo tapiz `#7A1F1F` · dorado `#C8A04A` · fuego `#E0782F` · corcho `#B8895A` · pergamino `#E9DFC7`~~ (a ojo).

### Otros sitios
- **Privet Drive**: la lluvia de cartas (P1 00:11:31). Salón suburbano, luz de día.
- **Expreso de Hogwarts**: compartimentos de madera, luz de ventanilla. Luna reparte El Quisquilloso (P6 00:22:36).
- **Pared de los decretos**: fuera del Gran Comedor. MinaLima hizo **más de cien decretos**, con letra rígida y formas duras, para mostrar el control del Ministerio ([MinaLima](https://minalima.com/ministry-of-magic-collection/), [Harry Potter Wiki](https://harrypotter.fandom.com/wiki/Educational_Decree)) ✅.

### Texturas reales equivalentes

Comprobadas por la API de Poly Haven y ambientCG (autor y tamaño máximo) ✅.

| Material | Textura | Autor · tamaño | Licencia |
|---|---|---|---|
| Mesa del comedor | [Wood Table Worn](https://polyhaven.com/a/wood_table_worn), [Wooden Table 01](https://polyhaven.com/a/WoodenTable_01) (modelo 3D) | Dimitrios Savva y Rico Cilliers · 8K; Ethan Place · 4K | CC0 |
| Muro | [Castle Wall Slates](https://polyhaven.com/a/castle_wall_slates), [Stone Block Wall](https://polyhaven.com/a/stone_block_wall) | Rob Tuytel · 8K; Amal Kumar · 16K | CC0 |
| Luz de salón viejo | HDRI [Old Hall](https://polyhaven.com/a/old_hall), [Entrance Hall](https://polyhaven.com/a/entrance_hall) | Sergej Majboroda · 16K | CC0 |
| Papel | [Paper001](https://ambientcg.com/view?id=Paper001), [Paper005](https://ambientcg.com/view?id=Paper005) | ambientCG | CC0 |
| Periódico viejo | [Texturelabs paper_290](https://texturelabs.org/textures/paper_290/) | Texturelabs | gratis; la página de condiciones devuelve un reto antibots (202) y no la pude leer ⚠️ |
| Corcho | [Cork001](https://ambientcg.com/view?id=Cork001) | ambientCG | CC0 |
| Fieltro rojo del tablón | no busqué una textura de fieltro: teñir [Paper005](https://ambientcg.com/view?id=Paper005) o una tela a `#51201D` (luz de Pottermore) o `#32100F` (penumbra de P1); el cordón trenzado rojo y oro, con una curva y un material de cuerda | — | — |
| Cartón del marco | [Cardboard004](https://ambientcg.com/view?id=Cardboard004) | ambientCG | CC0 |

MinaLima **prefiere escanear papeles antiguos reales** a usar vectores limpios
([HP Fan Zone](https://www.harrypotterfanzone.com/exclusive-meet-minalima-part-1/)).
Y cortaba los bordes de cada página de El Profeta con **una herramienta hecha
a propósito**, para que no parecieran cortados a máquina
([Steps to Magic](https://stepstomagic.com/house-of-minalima-london-fun-facts/)) ⚠️ una fuente.

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia
- **El logo de las películas** (visto en el [comienzo de P1, 3:37](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=217)):
  «Harry Potter» en letras doradas biseladas, la P y la y con rabos largos y
  el rayo; debajo, en versalitas con serifa pequeñas, «AND THE PHILOSOPHER'S
  STONE», sobre nubes de noche. En el [tráiler de HBO Max Latinoamérica, 2:05](https://www.youtube.com/watch?v=ZgrCZVjPg9g&t=125)
  el mismo logo dice «**Harry Potter y la piedra filosofal**»: el título
  latino oficial ✅. Oro medido en el comienzo: `#B19F72` sobre `#3A3331`.
- **Los logos latinos de cine** (fotos de la pantalla en Doblaje Wiki,
  miradas): P1 «Harry Potter **Y LA PIEDRA FILOSOFAL**» en oro sobre nubes
  ([imagen](https://static.wikia.nocookie.net/doblaje/es/images/c/cc/Harry_Potter_y_la_Piedra_Filosofal_Logo_Espa%C3%B1ol_para_Cines.png), 1342×622);
  P3 «Y EL PRISIONERO DE AZKABAN» en acero ([imagen](https://static.wikia.nocookie.net/doblaje/es/images/5/54/Harry_Potter_y_el_prisionero_de_Azkaban_-_Logo_cine.png), 1886×881);
  P4 «**Y EL CÁLIZ DE FUEGO**» en plata, **con la tilde en la Á**
  ([imagen](https://static.wikia.nocookie.net/doblaje/es/images/0/02/Harry_Potter_y_el_C%C3%A1liz_de_Fuego_Logo_Espa%C3%B1ol_para_Cines.png), 1548×1045) ✅.
  El subtítulo va en **versalitas con serifa en cuña**, la «Y» y el «EL»
  pequeños y montados. Prueba de que en español el logo lleva tildes: la
  letra que se use tiene que traerlas.
- **La cartela del tráiler de 2001** (720p, [2:15](https://archive.org/download/harry-potter-and-the-sorcerers-stone-2001-720p-trailer/Harry%20Potter%20and%20the%20Sorcerers%20Stone_2001_720p_trailer.mp4#t=135)):
  «THE MAGIC BEGINS» y luego «SOON», **versalitas doradas, espaciadas,
  con serifas en cuña**, sobre nubes de tormenta azul pizarra. Es la misma
  familia que el subtítulo del logo ✅ visto. Para #anuncios, una línea así
  («PRÓXIMAMENTE») queda muy de la saga: la letra libre más cercana es
  **Cinzel** o **IM Fell English SC** (§6.2).
- **La letra de las cartas de Hogwarts** (*teaser* de 2001, [0:24](https://archive.org/download/HarryPotterTheSorcerersStoneTrailer1/HarryPotterTheSorcerersStoneTrailer1.mp4#t=24)):
  «Mr. H. Potter, The Cupboard under the Stairs, 4, Privet Drive, Little
  Whinging, Surrey», **caligrafía de pluma en tinta verde oscura**,
  mayúsculas y minúsculas mezcladas y alguna mayúscula pequeña dentro de
  la palabra («StaiRs», «DRive»). Medido en el fotograma del *teaser*
  (con poca luz): papel `#7E7063`, tinta `#4B4838`.
- **Las cartelas de los tráileres** en español (P8, [WB Pictures Latinoamérica, 0:09](https://www.youtube.com/watch?v=-kDonIIXuqo&t=9)):
  «CADA MOMENTO DE SU VIDA», «ESTE AÑO», «SE ACABA». Mayúsculas romanas con
  serifa, grabadas en metal, entre humo gris. Tono oscuro: **no** para
  #anuncios.
- **Los créditos de P3**: cada nombre en **una cinta de pergamino dibujada**,
  a pluma, con huellas del Mapa que caminan alrededor ([copia de fan, 0:11](https://www.youtube.com/watch?v=MJzymmFvtlk&t=11)).
  Pergamino medido `#8A7246` / `#937E50`.
- **El Profeta, primera época** (P1-P4; O·1, O·2, O·9): cabecera «The Daily
  Prophet» en **gótica adornada** dentro de un marco; titulares en **gótica
  (fraktur)**, «Break-in at Gringotts»; capitulares enormes; texto que gira
  en espiral. Por eso **UnifrakturMaguntia** encaja ✅ (visto en O·2).
- **Desde P5** la cabecera se rehace con el **constructivismo ruso de los
  años veinte**: «DAILY PROPHET» de palo grueso con la P dorada (visto en la
  recopilación de MinaLima, §2.1)
  ([HP Fan Zone](https://www.harrypotterfanzone.com/exclusive-meet-minalima-part-1/),
  [House of MinaLima](https://www.itsnicethat.com/news/house-of-minalima-harry-potter-graphic-art-030616)) ✅.
- Para la cabecera de El Profeta los fans señalan **P22 Operina Fiore**, y
  **Prison Pro** para el titular «He Who Must Not Be Named». Las dos son de
  pago ([HP Fan Zone: la letra de El Profeta](https://www.harrypotterfanzone.com/fonts/the-daily-prophet-font/),
  [foro de dafont](https://www.dafont.com/forum/read/12072/the-daily-prophet-font)) ⚠️.
- **Mapa del Merodeador**: dibujado a mano por Miraphora. Su letra se usó en
  los créditos de P3 y P4 ([MinaLima](https://minalima.com/product/the-marauders-map/)).
- **Logo de Hogwarts Legacy**: «Customized from the typeface **Tongari**,
  the spurred serif…», con biselado y ligaduras propias; lo dice
  [Pentagram](https://www.pentagram.com/work/hogwarts-legacy/story), el
  estudio que lo diseñó, y lo repite [FontBolt](https://www.fontbolt.com/font/hogwarts-legacy-font/) ✅.
  Que «LEGACY» vaya en *Tautz* sólo lo dice FontBolt ⚠️.
  La letra de sus menús y subtítulos **no la encontré**.
- **Magic Awakened**: letra medieval un poco gótica, con el rayo de Harry
  como guiño ([GameRes](https://www.gameres.com/885575.html),
  [Zhihu](https://zhuanlan.zhihu.com/p/415443640)).

### 6.2 Letras libres comprobadas por mí
Bajé cada `.ttf` de [google/fonts en GitHub](https://github.com/google/fonts)
y miré con fontTools si trae **á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü**. Las 13 los traen
(Cinzel, añadida en el cierre: 367 glifos, no le falta ninguno).

| Letra | Para qué | ¿Tildes, ñ, ¿ ¡? |
|---|---|---|
| **UnifrakturMaguntia** | cabecera tipo El Profeta | ✅ |
| **IM Fell English** | texto del periódico y del pergamino | ✅ |
| **IM Fell DW Pica** | columnas de texto pequeño | ✅ |
| **IM Fell English SC** | subtítulos en versalitas, rótulos del Mapa | ✅ |
| **Cinzel Decorative** | titular de aviso solemne | ✅ |
| **Cinzel** | versalitas tipo «THE MAGIC BEGINS» del tráiler de 2001 y el subtítulo del logo | ✅ |
| **Almendra** | notas del tablón, aire medieval | ✅ |
| **Grenze Gotisch** | cabecera gótica más legible | ✅ |
| **Pinyon Script** | firma de Dumbledore o McGonagall | ✅ |
| **Mrs Saint Delafield** | nota escrita a mano, deprisa | ✅ |
| **Old Standard TT** | titular de periódico serio | ✅ |
| **Big Shoulders Display** / **Russo One** | sólo si se quiere la cabecera de propaganda de P5 | ✅ |

Todas con licencia OFL. Fuente de la licencia y el subset: su `METADATA.pb`, p. ej.
[UnifrakturMaguntia](https://raw.githubusercontent.com/google/fonts/main/ofl/unifrakturmaguntia/METADATA.pb)
e [IM Fell English](https://raw.githubusercontent.com/google/fonts/main/ofl/imfellenglish/METADATA.pb).

### 6.3 Letras de fans (con trampa)

| Letra | Qué es | Licencia | ¿Tildes? |
|---|---|---|---|
| **Harry P** ([dafont](https://www.dafont.com/harry-p.font)) | imita el logo | «100 % gratis», dice el autor | **No.** Comprobé el archivo: 95 glifos. Le faltan á é í ó ú ñ ¿ ü. Sí trae ¡. Sirve para «ANUNCIOS», no para «Aquí». |
| **Parry Hotter** ([1001 Fonts](https://www.1001fonts.com/parry-hotter-font.html)), de Anke Arnold | parodia del logo | el «léeme» pide un enlace a su web o un donativo | **No.** Comprobado en la 2.ª pasada: 101 glifos; le faltan **todas** las tildes, ñ, ¿ y ¡. |
| **Lumos** ([Social Fonts](https://social-fonts.com/harry-potter/lumos/)) | títulos de capítulo de los libros de EE. UU. | personal y comercial, dice la web | **No.** Comprobado: 91 glifos; le faltan tildes, ñ, ¿, ¡ y ü. |
| **MuggleNews** | texto tipo El Profeta, de fans | desconocida | sí, comprobado en el archivo del [proyecto dailyprophet](https://github.com/gstrenge/dailyprophet) |
| **BlackCastleMF** | cabecera gótica de ese proyecto | «All rights reserved», 1995 | sí, comprobado |
| **Headline Two HPLHS** | titulares de periódico antiguo | de la HPLHS | **no trae ¿ ni ¡** |

**Recomendación**: cabecera en **UnifrakturMaguntia**, texto en
**IM Fell English**, firma en **Pinyon Script**. Nada de pago, nada roto.

---

## 7 · Cómo hablan en pantalla: el cuadro de diálogo

**Regla de la franquicia: el texto vive dentro de un objeto del mundo.**
No hay globos. Ya lo dice la guía de cuadros de diálogo del repositorio
(sección 5). Aquí va ampliado.

### 7.1 Los «cuadros» reales

1. **La portada de El Profeta** ✅
   - MinaLima le dio una identidad que **cambia con la historia**:
     caprichosa al principio; propaganda del Ministerio desde P5
     ([HP Fan Zone](https://www.harrypotterfanzone.com/exclusive-meet-minalima-part-1/)).
   - Las fotos se mueven. En el rodaje llevaban **papel verde** encima para
     meter luego el vídeo ([New Statesman](https://www.newstatesman.com/culture/2015/12/graphic-art-harry-potter-films-two-designers-bringing-fiction-life)).
   - Eduardo Lima hacía de «editor» y maquetaba cada número. Fue **el
     accesorio que más trabajo costó**
     ([New Statesman](https://www.newstatesman.com/culture/2015/12/graphic-art-harry-potter-films-two-designers-bringing-fiction-life)).
   - Tenía de todo, como un diario real: lotería, horóscopos, esquelas.
     Y en el tiempo de cada número aparece **Caxambu**, el pueblo de Brasil
     donde creció Eduardo Lima ✅
     ([Steps to Magic](https://stepstomagic.com/house-of-minalima-london-fun-facts/);
     y el propio Lima en [O Tempo, 2017](https://www.otempo.com.br/entretenimento/magazine/designer-mineiro-e-o-criador-de-diversos-objetos-de-harry-potter-1.1554532):
     «Caxambu está até na previsão do tempo»). Lima hacía de editor: él
     firmaba como reportero, su madre salía como «editora de Seguridad», y
     hay titulares de broma como «Ginger witch arrested in Caxambu with fake
     henna». **Un periódico lleno de guiños internos: justo lo que puede
     llevar la lámina** (un titular pequeño con un guiño del servidor).
   - **En la lámina**: el titular dice el canal; la foto es un fotograma
     real; las columnas llevan los textos.
2. **El discurso desde el atril del búho**: desde P3 (clip oficial, §3) y en
   P4, P5 y P6. En P1 Dumbledore da los avisos de pie en la mesa (00:42:20,
   F·1). En la lámina, un **pergamino sobre el atril** con los avisos.
3. **El tablón de anuncios** de Gryffindor: en los libros, en los juegos,
   en Pottermore (O·21) y de fondo en las películas 1-6 (según la wiki; en
   P1 lo vi: fieltro rojo en cuadros de cinta y cordón rojo y oro, §3, §5).
   **Fieltro rojo oscuro con marco tallado**; notas en papel crema, con letra
   de alumno a mano («LOST: a purple Care of Magical Creatures textbook»,
   «Potion Rules», «Top Ten Spells»). La wiki dice que ahí se clavaban cada
   día El Profeta y El Quisquilloso ⚠️.
4. **Los decretos de Educación**: marcos en la pared, letra rígida.
   Más de cien en P5 ([MinaLima](https://minalima.com/ministry-of-magic-collection/),
   [Shmoop](https://www.shmoop.com/study-guides/harry-potter-order-of-the-phoenix-movie/educational-decrees-symbol.html)).
5. **El vociferador**: sobre rojo `#B12E38` (lámina de MinaLima) que grita
   con la voz de quien lo manda (P2 00:34:28): se levanta, es **una boca de
   papel con dientes** y acaba en confeti ([clip 0:25 y 0:57](https://www.youtube.com/watch?v=fBziSx7RtqY&t=25)).
   En la película, con su luz, el sobre mide **`#5B2022`** (carmesí oscuro),
   con una cinta casi negra `#210D0F` y la etiqueta crema con orla de
   rombos (fotograma 1080p, [0:16](https://www.youtube.com/watch?v=3KNNglv24a0&t=16)).
   **En el doblaje latino se llama «vociferador»**; en el de España,
   «Howler» (§10.3).
   En la lámina de MinaLima, la carta termina con **una posdata en tinta
   dorada**, amable, para Ginny (§2.1). Ver la [guía del repositorio](../_ya_hechas/_Cuadros%20de%20dialogo%20por%20franquicia%20(23-sep-2026).md).
6. **La carta de Hogwarts**: sobre de pergamino y lacre. La lluvia de cartas
   (P1 00:11:31).
7. **El Mapa del Merodeador**: el pergamino responde e insulta; los nombres
   van en cartelitos junto a las huellas (P3 00:57:24).
8. **El Quisquilloso**: la revista rara de Luna. Regalaba las **gafas
   espectrales** para ver *wrackspurts*
   ([Harry Potter Wiki](https://harrypotter.fandom.com/wiki/Spectrespecs),
   [Wizarding World](https://www.harrypotter.com/fact-file/objects/the-quibbler)).
9. **La cinta de pergamino de los créditos de P3**: cada nombre en una
   filacteria dibujada a pluma, con huellas alrededor (§6.1). Es un marco de
   texto del propio mundo, sin globo.
10. **La voz de los insertos (sólo en el doblaje latino)** ✅: cuando sale
    un texto en pantalla, **un narrador lo lee**. Así el público latino
    «oyó» El Profeta: «Dumbledore y Potter reivindicados», «Harry Potter,
    el elegido», y hasta el cartel del examen: «Silencio. TIMOS en
    progreso» (§10.3). Lo hacen Francisco Colmenero (título de P1) y Helgar
    Pedrini (P3-P6), según Doblaje Wiki. **Para la lámina**: el titular de
    la portada puede escribirse como se leería en voz alta, corto y en
    presente, igual que esos titulares.

### 7.2 En los videojuegos
- **Magic Awakened**: interfaz «de escena». Papel medieval, libros de
  magia, **páginas que pasan** para explicar de dónde sale cada cosa
  ([GameRes](https://www.gameres.com/885575.html),
  [UISDC](https://www.uisdc.com/harry-potter-art-design),
  [GAMEUI](https://www.gameui.net/games/2967)).
- **Hogwarts Legacy**: HUD mínimo en las esquinas de abajo, todo se puede
  ocultar. El menú es la **Guía de campo**
  ([Deltia's Gaming](https://deltiasgaming.com/hogwarts-legacy-user-interface/),
  [Game Rant](https://gamerant.com/hogwarts-legacy-gameplay-showcase-november-2022-combat-castle-tour-hud/),
  [Interface In Game](https://interfaceingame.com/games/hogwards-legacy/),
  [soporte de Portkey](https://portkeygamessupport.wbgames.com/hc/en-us/articles/11893402078355-Hogwarts-Legacy-Accessibility-Features-A11Y)).
- **Juego de PC de 2001**: Harry tiene **más de 100 frases grabadas y sin
  usar**, quizá para que no fuera pesado
  ([The Cutting Room Floor](https://tcrf.net/Harry_Potter_and_the_Sorcerer's_Stone_(Windows,_Mac_OS_Classic,_Mac_OS_X)/Unused_Dialogue)).
  Al principio los hechizos se elegían en un menú
  ([TCRF, gráficos](https://tcrf.net/Harry_Potter_and_the_Sorcerer's_Stone_(Windows,_Mac_OS_Classic,_Mac_OS_X)/Unused_Graphics)).
- **La cámara secreta, Game Boy Color**: RPG con cajas de texto clásicas
  ([TCRF](https://tcrf.net/Harry_Potter_and_the_Chamber_of_Secrets_(Game_Boy_Color)),
  [Spriters Resource](https://www.spriters-resource.com/game_boy_gbc/harrypotterthechamberofsecrets/)).
- **Hogwarts Mystery** (Jam City, 2018): vista la [captura de la wiki](https://static.wikia.nocookie.net/harrypotter/images/4/4b/Rowan_mentions_Maya.png)
  (1920×1080) ✅. La caja es **una franja ancha abajo, azul petróleo
  translúcido** (`#0F222B` a `#103D4E`), con **el nombre en dorado con
  serifa** (`#D6CCAC`) arriba a la izquierda, el texto en blanco azulado
  (`#D8F3FD`) y las respuestas en **botones rectangulares** de fondo
  `#023341` y filo turquesa `#118D94`. En otras capturas Dumbledore y Rita
  Skeeter hablan **desde el atril del búho**
  ([1](https://static.wikia.nocookie.net/harrypotter/images/9/93/Professor_Dumbledore%27s_start-of-term_speech_HM41.png),
  [2](https://static.wikia.nocookie.net/harrypotter/images/a/aa/Rita_Skeeter%27s_Great_Hall_speech_HM.png)).
  Es una caja de móvil, moderna: sirve como contraste, no para la lámina
  ([Wikipedia](https://en.wikipedia.org/wiki/Harry_Potter:_Hogwarts_Mystery),
  [portafolio de su diseñador de UI](https://cargocollective.com/richoki/Harry-Potter-Hogwarts-Mystery)).

### 7.3 Qué NO hacer con el texto
- Globo blanco con cola. No existe en este mundo.
- Una sans moderna o vectores limpios sin textura de papel.
- La cabecera de propaganda en una lámina alegre.
- El Quisquilloso para algo oficial: es la revista de rumores.

---

## 8 · Los personajes

> Carácter y relaciones: de los libros y las películas. El lenguaje corporal
> de Hermione, Luna, Dobby y Dumbledore ya está **visto en los clips
> oficiales** (2.ª pasada, §15). Las frases «En latino» son del doblaje, de
> las muestras de audio de Doblaje Wiki (§10.3).

### Hermione Granger
- **Qué es**: hija de muggles, la mejor alumna, de Gryffindor. Se lo ha
  leído todo.
- **Qué le importa**: las normas, los libros, y más aún sus amigos. Pelea
  por los elfos domésticos.
- **Miedo**: suspender, que la expulsen. «Or worse, expelled» (P1 01:03:32).
- **Relaciones**: corrige a Ron y acaba con él. Cuida a Harry. Choca con Draco.
- **Cómo habla**: rápido, con datos, corrigiendo. **Levanta la mano muy
  estirada** mientras Snape pregunta a Harry ✅ (guion transcrito de
  [Moviepedia](https://movies.fandom.com/wiki/Harry_Potter_and_the_Philosopher%27s_Stone/Transcript):
  «Hermione raises her hand… Hermione's hand raises again»; y la
  [captura de la wiki](https://static.wikia.nocookie.net/harrypotter/images/9/9f/Hermione_with_her_Hand_Up.jpg),
  500×759: brazo recto arriba, dedos juntos, ojos muy abiertos). Explica con paciencia de profesora. Se enfada
  en seco: «Ron, you spoiled everything!» (P4 01:22:02).
- **Cuerpo** (visto en el [clip de Leviosa](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=4)):
  **agarra el brazo de Ron** para frenarlo (0:04), explica con la cabeza
  ladeada y las cejas altas (0:10-0:13), **cierra los ojos con la barbilla
  alta**, orgullosa (0:17), hace el giro de varita con la muñeca (0:20) y
  sonríe satisfecha cuando lo logra (0:34). En la promo de P3 (P·1), erguida,
  una mano apoyada en el mueble. Libros abrazados: P·2. En el tráiler de P6
  (0:44, fotograma grande): sentada en la mesa de Gryffindor, **un libro
  abrazado contra el pecho y la mirada de reojo**, seria: su gesto de
  «esto no me parece bien».
- **En latino** (Mitzy Corona en P1, Leyla Rangel desde P4): explica de
  corrido, con datos: «Nicolás Flamel es el único que ha podido crear la
  piedra filosofal… y produce el elixir de la vida» (P1). Abre la reunión del
  ED: «**Ya saben a qué vinieron. Por un maestro, un maestro de verdad**»
  (P5). Y regaña a Ron: «**tienes tanta sensibilidad como una piedra**» (P5;
  en inglés era «a teaspoon», una cucharita).
- **Para #anuncios**: perfecta para **explicar**. En P5 00:54:01 abre la
  primera reunión del Ejército de Dumbledore: «So you all know why we're here».

### Luna Lovegood
- **Qué es**: de Ravenclaw, soñadora, cree en criaturas que nadie ve.
  La llaman «Lunática» (P5 00:29:49).
- **Qué le importa**: la verdad tal como ella la ve, su padre, sus amigos.
- **Miedo**: casi nada la asusta; le esconden las cosas y ella lo acepta
  con calma (P5 02:06:14).
- **Relaciones**: fiel a Harry, amiga de Neville y Ginny.
- **Cómo habla**: voz lenta y tranquila, dice cosas raras con total
  seriedad. «You're just as sane as I am» (P5 00:29:41). «Keeps away the
  Nargles» (P5 00:30:06).
- **Cuerpo** (visto en el [clip del carruaje, P5](https://www.youtube.com/watch?v=8k2bj-R9m8E&t=53)):
  **lee El Quisquilloso levantado con las dos manos, tapándose la cara**
  (0:53-1:07), asoma los ojos por encima y **mira a Harry sin parpadear, con
  media sonrisa** (1:09-1:12). Luego la revista en el regazo (1:22). Mirada
  soñadora, cabeza un poco ladeada. Gafas espectrales y revista: P·11.
  **La revista, al revés**: en vídeo real se ve el título «QUIBBLER» boca
  abajo mientras ella mira a Harry por encima ([0:48](https://www.dailymotion.com/video/x3dhmzl?start=48)); en el libro 5
  Harry la ve igual, «reading a magazine upside down» (wiki) ✅. Botas de
  agua rojas y collar de corchos de cerveza de mantequilla.
- **En latino** (Lu Leal, P5-P8): voz suave, frases cortas y raras dichas
  con calma. «Hola, Harry. **Torposoplos. Tienes la cabeza llena**» (P6;
  Whisper *medium* oyó «torposolos» y *large-v3* «por posolos»: en los
  libros en español son «torposoplos» ⚠️).
  «Fue como estar con un amigo» (P6). «Excepcionalmente ordinaria» (P6).
  Y habla de la prensa: «**el Ministerio y El Profeta conspiran contra ti y
  Dumbledore**» (P5).
- **Momentos favoritos del fandom**:
  [Wizarding World: sus ocho momentos más locos](https://www.harrypotter.com/features/luna-lovegoods-eight-wackiest-moments).
- **Para #anuncios**: **reparte El Quisquilloso por el pasillo del tren** (P6 00:22:36; wiki de la película ✅).
  Es la «prensa no oficial». Mejor como guiño que como portavoz.

### Dobby
- **Qué es**: elfo doméstico esclavo de los Malfoy. Harry lo libera con un
  calcetín (P2 02:25:12).
- **Qué le importa**: Harry Potter, la libertad.
- **Miedo**: desobedecer. Se castiga solo: «Bad Dobby!» (P2 00:04:14).
- **Cómo habla**: **en tercera persona** siempre: «Dobby has come to…».
  Chillón, exagerado, muy cortés: «Dobby has heard of your greatness, sir»
  (P2 00:03:56).
- **Cuerpo** (visto en el [clip del calcetín, P2](https://www.youtube.com/watch?v=8DTb-lseCdQ&t=59)):
  sostiene el diario con el calcetín dentro (0:59-1:03); **de pie, erguido,
  con el calcetín** (1:34); **cabeza ladeada, ojos húmedos y sonrisa** al
  despedirse (1:58-2:00). En vídeo real (Dailymotion, 512 px): **alarga un
  dedo larguísimo hacia el calcetín**, pícaro ([3:00](https://www.dailymotion.com/video/x3d4quh?start=180)); **se planta delante de
  Harry, pies separados y palmas abiertas**, pequeño y valiente ([3:20](https://www.dailymotion.com/video/x3d4quh?start=200));
  y agradece con la **cabeza ladeada y los ojos húmedos** ([4:00](https://www.dailymotion.com/video/x3d4quh?start=240)). En el arte: **chasquea los dedos con la mano en
  alto** (P·18), **brazos en jarra** (P·19). Orejas de murciélago, funda de
  almohada.
- **En latino** (Ismael Castro, P2 y P7): siempre en tercera persona.
  «Harry Potter debió escuchar a Dobby.» «**A Dobby lo amenazan cinco veces
  al día en casa**» (P2). «**Dobby no tiene amo. Dobby es un elfo libre, y
  Dobby vino a salvar a Harry Potter y a sus amigos**» (P7).
- **Frase de proclama**: «Dobby has no master. Dobby is a free elf»
  (P7 02:09:15); en latino, «Dobby es un elfo libre» ✅. Es literalmente un
  anuncio.
- **Cuidado**: su muerte (P7 02:10:48) es de las escenas más tristes de la
  saga ([Game Rant](https://gamerant.com/saddest-most-tragic-harry-potter-deaths-books-moviesdumbledore-sirius-dobby/)).
  No mezclar la lámina con eso.

### Albus Dumbledore
- **Qué es**: director de Hogwarts. **Es quien da los avisos oficiales.**
- **Qué le importa**: los alumnos, el amor, las segundas oportunidades.
- **Miedo**: el poder, su pasado.
- **Cómo habla**: calma, humor seco, frases para recordar. «Happiness can
  be found…» (P3 00:25:37). Sabe cortar el ruido: «Tell them to wait»
  (P4 00:16:53). Lo dice él a Filch sin soltar el discurso: «Yes, what is
  it?… Tell them to wait… So Hogwarts has been chosen…» ✅ (subtítulos).
- **Dos actores**: Richard Harris en P1 y P2, Michael Gambon desde P3. En
  latino **la misma voz en las ocho**, César Arias (sección 10).
- **Cuerpo** (visto en el [clip del discurso, P3](https://www.youtube.com/watch?v=dvFehFzph7I&t=43)):
  **abre los brazos en alto** tras el atril (0:43-0:45), camina hacia las
  mesas de espaldas (0:47-0:55), **alza los dos índices** para subrayar
  (2:42-2:44) y **apaga una vela con los dedos** (2:48). En P1 (Harris),
  de pie en la mesa entre velas, túnica burdeos con dibujo dorado (F·1, P·27);
  en el tráiler de 2001, **erguido en el centro de la mesa, los brazos
  caídos dentro de la túnica**, solemne ([1:15](https://archive.org/download/harry-potter-and-the-sorcerers-stone-2001-720p-trailer/Harry%20Potter%20and%20the%20Sorcerers%20Stone_2001_720p_trailer.mp4#t=75)),
  y en el *teaser*, **bebiendo de una copa dorada** con gorro de terciopelo
  burdeos de estrellitas, en un sillón dorado tallado ([0:51](https://archive.org/download/HarryPotterTheSorcerersStoneTrailer1/HarryPotterTheSorcerersStoneTrailer1.mp4#t=51)).
- **En latino** (César Arias): pausado, de abuelo sabio. «**Siempre se
  ayudará en Hogwarts, Harry, a quienes lo pidan.** Las palabras son, en mi
  no tan humilde opinión, nuestra fuente más inagotable de magia, capaces
  tanto de ocasionar dolor como de remediarlo» (P8). «Tiempos difíciles y
  oscuros nos aguardan. Pronto deberemos elegir entre lo que es correcto y lo
  que es fácil» (P4). «Envíe una lechuza con esta orden de libertad a
  Azkaban. Me parece que queremos que Hagrid vuelva» (P2).

### Harry Potter
- **Qué es**: el protagonista, huérfano, famoso sin quererlo.
- **Qué le importa**: sus amigos, la verdad sobre sus padres.
- **Cómo habla**: poco, directo, a veces cortante. Cuando enseña se suelta:
  «Every great wizard in history has started out…» (P5 01:02:39).
- **En latino** (Arturo Castañeda en P1, Claudio Velázquez en P2, Víctor
  Ugarte desde P3): deduce en voz alta, rápido. «Está buscando algo que era
  propiedad de Gregorovitch… **Me ponen los pelos de punta**» (P7).
- **Para #anuncios**: el diario se lee en voz alta en el desayuno
  (P1 00:54:38) y lo lee él ✅ (wiki + guion transcrito, §3): no le llega
  correo, **le pide el diario a Ron** («Can I borrow this?») y lee:
  «Somebody broke into Gringotts. Listen…» y «That's the vault Hagrid and I went to».

### Ron Weasley
- **Qué es**: el mejor amigo, sexto hijo de una familia pobre y enorme.
- **Qué le importa**: su familia, no quedar por debajo.
- **Miedo**: las arañas. «Why spiders?» (P2 01:43:18).
- **Cómo habla**: quejica, cómico. «Bloody hell» es su muletilla en inglés
  (P8 00:33:45). **En latino** (Luis Daniel Ramírez, P3-P8) sale como
  «**Ay, diablos, ahí va**» (P8, muestra de Doblaje Wiki). En P1 (Carlos
  Díaz) dirige el ajedrez: «Harry, tú eres el que tiene que continuar».
- **Cuerpo** (visto en 1080p, [vociferador](https://www.youtube.com/watch?v=3KNNglv24a0&t=32)):
  **ojos como platos, hombros encogidos**, mira el sobre sin tocarlo (0:32);
  el grito le llega a la cara y se echa atrás (0:40); al final, quieto y
  rojo junto a Harry (0:44-0:48). En la clase de Leviosa agita la varita
  como un látigo (clip [0:00-0:02](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=0)).
- **Para #anuncios**: el que **recibe** el aviso a gritos: el vociferador
  (P2 00:34:28). En latino, sus compañeros lo anuncian: «**¡Miren nada más!
  ¡Weasley recibió un vociferador!**» ([15:37-15:41](https://www.youtube.com/watch?v=3KNNglv24a0&t=937)).

### Dos extra que conviene tener a mano
- **Severus Snape**: el más votado en tres encuestas (sección 9). Como
  director reúne al colegio para un aviso (P8 00:35:09). En latino
  (Sebastián Llapur): «Si cualquiera, estudiante o maestro, pretendiera
  ayudar al señor Potter, será castigado de una manera consistente con la
  severidad de su infracción… **Lo invito a que pase al frente, ahora**».
  Es un anuncio, pero de miedo: tono oscuro, **no** para #anuncios.
- **Minerva McGonagall**: jefa de Gryffindor, la cara del staff. Puesto 9 en
  la encuesta de Cinema Today. **Es la otra voz de los avisos**: en P4
  anuncia el baile a su casa. En latino (Keta Leonel, P2-P8): «La víspera de
  Navidad, junto con nuestros invitados, nos reunimos en el gran salón para
  **una noche de recatada frivolidad**» (P4). Seca y firme: «Nada. Repito.
  Nada. Justifica que un estudiante camine por la escuela en la noche» (P1,
  Magda Giner). Figurín verde: P·33.

---

## 9 · ¿Quién es el más querido?

| Encuesta | Votos | Resultado |
|---|---|---|
| Bloomsbury, editorial inglesa, 2011 | más de 70 000 | 1 **Snape** (20 %) · 2 Hermione · 3 Sirius · 4 Harry · 5 Ron · 6 **Luna** · 7 Ginny · 8 Dumbledore · 9 **Dobby** · 10 Draco ([Leaky Cauldron](http://www.the-leaky-cauldron.org/2011/08/30/severus-snape-chosen-as-favorite-harry-potter-character-via-bloomsbury-poll/), [SnitchSeeker](https://www.snitchseeker.com/harry-potter-news/bloomsbury-announces-severus-snape-voted-as-favourite-character-in-harry-potter-books-85213/)) ✅ |
| MTV «Mundial de Harry Potter», 2011 | 7,4 millones | gana **Snape** entre 64 personajes; Rickman recogió el premio en el estreno de P8 en Nueva York ([Newsis](https://www.newsis.com/view/NISX20110721_0008742182), [IBTimes](https://www.ibtimes.com/severus-snape-named-greatest-harry-potter-character-alan-rickman-says-i-wont-miss-it-videos-645822), [IMDb News](https://www.imdb.com/news/ni12732815/)) ✅ |
| National Book Tokens, 2017 | más de 10 000 | 1 **Hermione** · 2 Snape · 3 **Luna**. Harry, 6.º, por detrás de Sirius y **Dobby** ([Marie Claire UK](https://www.marieclaire.co.uk/entertainment/tv-and-film/favourite-harry-potter-character-518389)). La prensa coreana ([Dispatch, 26-dic-2017](https://www.dispatch.co.kr/1047033)) cuenta la misma votación del 20.º aniversario, de dos semanas y más de 10 000 votos: 1.ª Hermione, 5.º Dobby ✅ |
| Cinema Today, Japón | 5 964 | 1 **Snape** 19 % · 2 Hermione · 3 **Luna** 12,4 % · 4 Draco · 5 Sirius · 6 Harry · 7 gemelos · 8 Ron · 9 McGonagall · 10 **Dobby** ([Cinema Today](https://www.cinematoday.jp/news/N0141040)) ✅ |
| Nlab, Japón, 2023 | — | 1 **Harry** · 2 Hermione ([Nlab](https://nlab.itmedia.co.jp/research/articles/1785486/), [PressWalker](https://presswalker.jp/press/17011)) |

**Conclusión**
- El más votado en general: **Snape**.
- De los seis del encargo: **Hermione** siempre entre las dos primeras.
- **Luna** queda por encima de Harry en dos encuestas. **Dobby**, en una.
- Para un canal oficial y amable, **Hermione** (o Dumbledore, por su papel)
  es la apuesta segura; **Luna** o **Dobby**, el guiño que el fan agradece.
- La encuesta de muertes más tristes de Fanpop la gana Fred, con el 35 %
  de más de 200 votos ([Looper](https://www.looper.com/788977/the-saddest-death-in-the-harry-potter-series/);
  Yahoo reproduce el mismo artículo, así que no cuenta como segunda fuente).
  La [página de la encuesta](https://www.fanpop.com/clubs/harry-potter/picks/results/20418/saddest-death-harry-potter)
  da 403 ⚠️.

---

## 10 · Doblaje latino

**Sí hay doblaje latino**, hecho en México para Warner. En la 2.ª pasada leí
Doblaje Wiki **por su API** (las 8 películas y las fichas de Harry,
Hermione, Ron, Dumbledore, Luna, Dobby, Snape, McGonagall y Hagrid) y lo crucé
con la Wikipedia en español (P2), un artículo de prensa con el reparto
([Genial.guru, 7-may-2020](https://genial.guru/articles/asi-se-ven-los-actores-que-doblan-al-espanol-latino-a-los-personajes-del-mundo-de-harry-potter-1293760/))
y las fuentes de la 1.ª pasada.

### 10.1 La producción, película a película

| Peli | Estudio | Dirección | Grabación | Fuentes |
|---|---|---|---|---|
| P1 | **Audiomaster 3000** | **Javier Rivero**; loops de Jorge Roig y Herman López. Traducción: Jesús Vallejo | nov-2001 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Harry_Potter_y_la_piedra_filosofal), [La Prensa de Panamá / El Universal, 21-dic-2001](https://www.prensa.com/impresa/opinion/Harry-Potter-hablara-espanol_0_539946170.html) y [el blog del propio Javier Rivero, 2007](http://javodubb.blogspot.com/2007/05/harry-potter.html); **los créditos de cine**, «Recording Studio: AUDIOMASTER MEXICO» ([foto](https://static.wikia.nocookie.net/doblaje/es/images/1/12/CR%C3%89DITOSHARRYPOTTERYLAPIEDRAFILOSOFAL.png)) ✅ |
| P2 | **Audiopost** | **Roberto Molina** | 2002 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta), [Wikipedia](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)) y **los créditos de cine**: «Director de Doblaje: Roberto Molina · Doblaje y Post Producción: SPG Studios - Audio Post, Los Angeles - México» ([foto](https://static.wikia.nocookie.net/doblaje/es/images/0/06/Harry_Potter_y_la_Camara_Secreta_Creditos_de_Doblaje_en_Cines.png)) ✅ |
| P3 | Audiopost | **José Luis García Agraz**; Vicky Burgoa (incidentales); Molina (escenas añadidas) | 2004 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Harry_Potter_y_el_prisionero_de_Azkaban), [DubDB](https://dubdb.fandom.com/wiki/Harry_Potter_y_el_prisionero_de_Azkaban_(Latin_American_Spanish,_Audio_Post)) (estudio Audio Post), [El Siglo de Durango (agencias), 2004](https://www.elsiglodedurango.com.mx/noticia/2004/breves-del-cine.39317.html): Cuarón invitó a su amigo García Agraz a dirigir el doblaje ✅. **Ojo**: la [Wikipedia en español](https://es.wikipedia.org/wiki/Harry_Potter_y_el_prisionero_de_Azkaban_(pel%C3%ADcula)) dice «Art Sound, dirección de Helgar Pedrini» (cita una web de 2009 ya caída); las otras dos ponen a Pedrini como director creativo |
| P4 | Audiopost | Roberto Molina | 2005 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Harry_Potter_y_el_c%C3%A1liz_de_fuego) ⚠️ |
| P5 | **DAT Doblaje Audio Traducción** | **Herman López** | may-2007 | Estudio ✅: [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Harry_Potter_y_la_orden_del_F%C3%A9nix) y [Wikipedia](https://es.wikipedia.org/wiki/Harry_Potter_y_la_Orden_del_F%C3%A9nix_(pel%C3%ADcula)). Dirección ⚠️: Wikipedia pone a Helgar Pedrini |
| P6 | DAT | Roberto Molina (Carlos Segundo se dirigió a sí mismo) | may-2009 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Harry_Potter_y_el_misterio_del_pr%C3%ADncipe) ⚠️ |
| P7 | DAT | Roberto Molina | oct-2010 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Harry_Potter_y_las_reliquias_de_la_muerte_-_Parte_1), [Blog Hogwarts](https://www.bloghogwarts.com/2011/01/13/el-doblaje-de-las-reliquias-de-la-muerte-parte-1-al-espanol-latino/) ✅ |
| P8 | DAT | Roberto Molina | may-2011 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Harry_Potter_y_las_reliquias_de_la_muerte_-_Parte_2) ⚠️ |

- **Ojo: hay un segundo doblaje, argentino**, de 2019 (Caja de Ruidos,
  dirección de Jorge Riveros), de P3 a P8: Harry es Alejandro Bono, Hermione
  Florencia Coianis, Luna Malena Oriolo. **El que conoce el público es el
  mexicano**; no mezclar voces ni frases (Doblaje Wiki, fichas de Hermione y
  Luna; y [DubDB](https://dubdb.fandom.com/wiki/Harry_Potter_y_el_prisionero_de_Azkaban_(Latin_American_Spanish,_Caja_de_Ruidos)),
  que tiene la ficha del de P3 con Caja de Ruidos) ✅.
- **Helgar Pedrini** fue el **director creativo** de Warner para toda la
  saga (Doblaje Wiki y DubDB) y es **la voz de los insertos** de P3 a P6:
  la que lee títulos y titulares (§10.3).
- **Tampoco mezclar con España**: allí Harry es Axel Amigo y Hermione Michelle
  Jenner ([Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula))).

### 10.2 Las voces (cada nombre con dos fuentes)

| Personaje | Voz latina | Películas | Fuentes | Estado |
|---|---|---|---|---|
| Harry | **Arturo Castañeda** | P1 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Arturo_Casta%C3%B1eda), [EcuRed](https://www.ecured.cu/Arturo_Casta%C3%B1eda_Mendoza) | ✅ |
| Harry | Claudio Velázquez | P2 | Doblaje Wiki, [Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)) | ✅ (antes dudoso) |
| Harry | **Víctor Ugarte** | P3 a P8 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/V%C3%ADctor_Ugarte), [Otaku Press](https://www.otakupress.pe/2017/04/victor-ugarte-harry-potter-sasuke-doblaje.html), [Noroeste](https://www.noroeste.com.mx/amp/entretenimiento/espectaculos/presta-victor-ugarte-su-voz-a-harry-potter-DANO230322), Genial.guru | ✅ |
| Hermione | Mitzy Corona | P1 y P2 | Doblaje Wiki, [Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)) | ✅ (antes dudoso) |
| Hermione | Priscila Reyes | P3 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Hermione_Granger), [DubDB](https://dubdb.fandom.com/wiki/Harry_Potter_y_el_prisionero_de_Azkaban_(Latin_American_Spanish,_Audio_Post)); la [Wikipedia](https://es.wikipedia.org/wiki/Harry_Potter_y_el_prisionero_de_Azkaban_(pel%C3%ADcula)) (con El Universal, 4-jun-2004) la cuenta entre las actrices de fuera del doblaje que entraron | ✅ (antes dudoso) |
| Hermione | **Leyla Rangel** | P4 a P8 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Leyla_Rangel), [Vía País](https://viapais.com.ar/streaming/es-leviosa-no-leviosa-ella-es-la-mujer-detras-de-la-voz-de-hermione-de-harry-potter/), Genial.guru | ✅ |
| Ron | Carlos Díaz | P1 y P2 | Doblaje Wiki, [Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)) | ✅ (antes dudoso) |
| Ron | **Luis Daniel Ramírez** | P3 a P8 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Luis_Daniel_Ram%C3%ADrez), Genial.guru, [Wikia Fandub](https://fandub-doblaje-latino.fandom.com/es/wiki/Luis_Daniel_Ram%C3%ADrez) | ✅ |
| Dumbledore | **César Arias** | P1 a P8 | Doblaje Wiki, [Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)), [Infobae](https://www.infobae.com/america/entretenimiento/2020/12/21/murio-el-actor-de-doblaje-cesar-arias-fue-la-voz-de-dumbledore-y-tambien-participo-en-naruto-y-los-caballeros-del-zodiaco/), [El Universal](https://www.eluniversal.com.mx/espectaculos/muere-cesar-arias-actor-de-doblaje-que-dio-voz-dumbledore/) | ✅ |
| Luna | **Lu (Lupita) Leal** | P5 a P8 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Lu_Leal), Genial.guru, [Anime Argentina](https://animeargentina.net/lupita-leal-doblaje/) | ✅ |
| Dobby | **Ismael Castro** | P2 y P7 | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Ismael_Castro), [Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)), Genial.guru | ✅ |
| McGonagall | Magda Giner | P1 (y el teaser de la serie de HBO) | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Minerva_McGonagall), [DubDB](https://dubdb.fandom.com/wiki/Harry_Potter_y_la_piedra_filosofal_(Latin_American_Spanish)) y los créditos de cine de P1 («Professor McGonagall · MAGDA GINER») | ✅ (antes dudoso) |
| McGonagall | **Keta Leonel** | P2 a P8 | Doblaje Wiki, [Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)) | ✅ |
| Hagrid | Humberto Solórzano | P1 | Doblaje Wiki, [Doblaje Latino Wiki](https://doblaje-latino.fandom.com/es/wiki/Humberto_Sol%C3%B3rzano) | ✅ (dos wikis) |
| Hagrid | Víctor Hugo Aguilar | P2 y P3 | Doblaje Wiki, [Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)) | ✅ (nuevo) |
| Hagrid | **Blas García** | P4 a P8 | Doblaje Wiki, Genial.guru, [Wikia Fandub](https://fandub-doblaje-latino.fandom.com/es/wiki/Blas_Garc%C3%ADa) | ✅ |
| Snape | **Carlos Segundo** | P1, P5, P6 | Doblaje Wiki, Genial.guru | ✅ |
| Snape | Rolando de Castro | P2 y P4 | Doblaje Wiki, [Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)) | ✅ (nuevo) |
| Snape | César Monroy | P3 | Doblaje Wiki, [DubDB](https://dubdb.fandom.com/wiki/Harry_Potter_y_el_prisionero_de_Azkaban_(Latin_American_Spanish,_Audio_Post)) | ✅ (antes dudoso) |
| Snape | Sebastián Llapur | P8 | Doblaje Wiki, [Wikipedia, P8](https://es.wikipedia.org/wiki/Harry_Potter_y_las_reliquias_de_la_Muerte:_parte_2) | ✅ (antes dudoso) |
| Snape | Jorge Badillo | P7 | Doblaje Wiki | ⚠️ (una fuente) |
| Umbridge | Ruth Toscano | P5 y P7 | Doblaje Wiki, [Wikipedia, P5](https://es.wikipedia.org/wiki/Harry_Potter_y_la_Orden_del_F%C3%A9nix_(pel%C3%ADcula)) | ✅ (antes dudoso) |
| Ginny | Alondra Hidalgo | P2, P4 a P8 (en P1, Lupita Leal) | Doblaje Wiki, [Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)), Genial.guru | ✅ |
| Molly Weasley (la voz del vociferador) | Carmen Martínez | P2 (en P1, Ruth Toscano) | [Doblaje Wiki, P2](https://doblaje.fandom.com/es/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta), [Wikipedia, P2](https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)) y los créditos de cine de P2 («Mrs. Weasley · CARMEN MARTINEZ»); Ruth Toscano en P1, también en sus créditos | ✅ (antes dudoso) |

**Datos de interés** (Doblaje Wiki ⚠️, salvo lo marcado):
- P1 fue **«la fatídica Harry Potter»** para Javier Rivero: Audiomaster
  estrenaba ProTools, tres salas a la vez por las prisas (con Jorge Roig y
  Herman López), y un ingeniero **borró a las 4 de la mañana un rollo de 20
  minutos ya grabado**. Por eso P2 pasó a Audiopost y cambió medio reparto
  ✅ (lo cuenta el propio Rivero en [su blog, 31-may-2007](http://javodubb.blogspot.com/2007/05/harry-potter.html)).
  Hizo más de 200 pruebas de voz; la prensa de 2001 habla de 140 voces
  probadas y 25 elegidas ([La Prensa](https://www.prensa.com/impresa/opinion/Harry-Potter-hablara-espanol_0_539946170.html)).
- En P3, **Alfonso Cuarón** eligió al director del doblaje y él mismo invitó
  a actores de cine como Damián Alcázar y Julieta Egurrola ✅ ([El Siglo de
  Durango](https://www.elsiglodedurango.com.mx/noticia/2004/breves-del-cine.39317.html)
  y Doblaje Wiki).
- Harry cambió en P2 porque no hubo acuerdo económico con la familia de
  Castañeda. **Víctor Ugarte hizo a Oliver Wood en P2** antes de ser Harry
  (Wikipedia P2 lo confirma ✅).
- **Leyla Rangel hizo el casting de Hermione para P1, P2 y P3** y no la
  eligieron; en P1 hizo voces adicionales. El «Leviosa» de P1 es de Mitzy
  Corona.
- **Lupita Leal fue Ginny en P1** antes de ser Luna desde P5.
- Snape volvió a Carlos Segundo en P5 **porque lo pidieron los fans**, y lo
  hizo sin cobrar; en P7 no aceptó el presupuesto (entró Jorge Badillo).
- En P2 el hechizo *Vera Verto* se dobló «Fera Verto», y Lucius grita
  «¡Arrara-» en vez de *Avada*. En P7 la capa pasa a llamarse «**Manto de la
  invisibilidad**».
- Dobby en P7 suena distinto: «Castro dobla a Dobby con otra
  caracterización» (Doblaje Wiki). Antes puse que «se le gastó la voz»: eso
  sólo lo dice un resumen del buscador; la wiki habla de caracterización.
- **Serie de HBO** (en camino): Doblaje Wiki ya tiene su ficha; en el teaser
  latino, **McGonagall vuelve a ser Magda Giner**, su voz de P1. El resto del
  reparto latino, «por identificar».
- César Arias murió el 21-dic-2020, a los 79 años ✅ (Infobae y El Universal).
- Víctor Ugarte cuenta que antes de grabar hace relajación y meditación
  ([Otaku Press](https://www.otakupress.pe/2017/04/victor-ugarte-harry-potter-sasuke-doblaje.html)).

### 10.3 Frases propias del doblaje latino (textuales)

**De dónde salen.** Los clips oficiales doblados de YouTube (los tráileres de
Warner Bros. Pictures Latinoamérica y México, §12) **no tienen subtítulos**,
y YouTube no deja bajar su audio. Pero **Doblaje Wiki guarda 65 muestras de
audio del doblaje** de estos personajes (20-60 s cada una). Las bajé y las pasé
por **Whisper** (modelo *small*; las 14 más útiles, otra vez con *medium*).
Corregí sólo nombres rotos («Dovi» → Dobby, «Jermaine» → Hermione). El minuto
sale de cruzar el sentido con los subtítulos en inglés. ✅ = el sentido
coincide con el subtítulo inglés de ese minuto.

**Y un clip con minuto exacto**: el vídeo «Ron receives a Howler in
different languages» (canal Compare Languages, 2022, 722 000 visitas) pone
la misma escena en 23 doblajes; el tramo **«Latin Spanish» va de 15:35 a
16:30**. No es un canal oficial (es un montaje de fan con el audio
oficial), pero es el doblaje de cine. Lo bajé de su copia en el Internet
Archive y pasé ese tramo por Whisper *medium*. Canales oficiales doblados
que busqué y no sirven: el clip «Baile de Navidad» de **HBO Max
Latinoamérica** no tiene subtítulos y YouTube no deja bajar su audio.

| Personaje | Frase del doblaje latino | Dónde | Estado |
|---|---|---|---|
| **Dumbledore** (César Arias) | «Siempre se ayudará en Hogwarts, Harry, a quienes lo pidan. Siempre me he vanagloriado de mi habilidad para las frases. **Las palabras son, en mi no tan humilde opinión, nuestra fuente más inagotable de magia**, capaces tanto de ocasionar dolor como de remediarlo.» | P8 01:34:46-01:35:00 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/e/e5/HP8AlbusDumbledore-1.ogg)) | ✅ |
| Dumbledore | «Tiempos difíciles y oscuros nos aguardan. Pronto deberemos elegir entre lo que es correcto y lo que es fácil.» | P4, final ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/3/36/HP4AlbusDumbledore-1.ogg)) | ✅ sentido |
| Dumbledore | «Sin embargo, es imperioso que ambos reciban el Premio Especial por Servicios al Colegio. Ahora, señor Weasley, envíe una lechuza con esta orden de libertad a Azkaban. Me parece que queremos que Hagrid vuelva.» | P2 02:18:22-02:18:50 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/7/79/HP2AlbusDumbledore-1.ogg)) | ✅ (Whisper oyó «Whistley»; el inglés dice «Mr. Weasley») |
| **McGonagall** (Keta Leonel) | «La víspera de Navidad, junto con nuestros invitados, nos reunimos en el gran salón para **una noche de recatada frivolidad**. Como representantes del colegio sede, espero que todos y cada uno de ustedes se esfuerce por dar un buen paso. Y lo digo literalmente, porque el baile de Navidad es eso, justamente: un baile.» | P4 01:06:47-01:07:20 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/0/01/HP4MinervaMcGonagall-1.ogg)) | ✅ **un aviso oficial** |
| McGonagall (Magda Giner) | «Nada. Repito. Nada. Justifica que un estudiante camine por la escuela en la noche.» · «Recibió una lechuza urgente del Ministerio de Magia y salió de inmediato a Londres.» | P1 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/3/3a/HP1MinervaMcGonagall-1.ogg)) | ✅ sentido |
| **Hermione** (Leyla Rangel) | «**Ya saben a qué vinieron. Por un maestro, un maestro de verdad.** Alguien con experiencia en defensa contra las artes oscuras.» · «Es porque tienes tanta sensibilidad como una piedra.» | P5 00:54:01 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/2/26/HP5HermioneGranger-1.ogg)) | ✅ |
| Hermione (Mitzy Corona) | «Nicolás Flamel es el único que ha podido crear la piedra filosofal… Transforma la materia en oro macizo y produce el elixir de la vida.» | P1 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/d/dd/HP1HermioneGranger-1.ogg)) | ✅ sentido |
| **Luna** (Lu Leal) | «Hola, Harry. **Torposoplos. Tienes la cabeza llena.** … Fue como estar con un amigo. … Excepcionalmente ordinaria.» | P6 00:27:24-00:27:40 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/a/ad/HP6LunaLovegood-1.ogg)) | ✅ (la palabra «torposoplos», ⚠️: Whisper oyó «torposolos») |
| Luna | «Por cierto, los dos te creemos. Que volvió el que no debe ser nombrado, y que pelearon, **y que el Ministerio y El Profeta conspiran contra ti y Dumbledore**.» | P5 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/c/cc/HP5LunaLovegood-1.ogg)) | ✅ sentido |
| Luna | «Hola, Harry. Interrumpí un pensamiento, ¿verdad? Vi que se hacía pequeño en tus ojos.» | P7 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/0/0c/HP7LunaLovegood-1.ogg)) | ✅ sentido |
| **Dobby** (Ismael Castro) | «Dobby nunca ha querido matar. Dobby sólo quería mutilar o lesionar de gravedad. **Dobby no tiene amo. Dobby es un elfo libre.** Y Dobby vino a salvar a Harry Potter y a sus amigos.» · «Qué playa tan hermosa para estar con amigos.» | P7 02:08:59-02:10:48 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/e/ed/HP7Dobby-1.ogg)) | ✅ |
| Dobby | «Harry Potter debió escuchar a Dobby. … A Dobby siempre lo amenazan. **A Dobby lo amenazan cinco veces al día en casa.**» | P2 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/2/2b/HP2Dobby-1.ogg)) | ✅ sentido |
| **Snape** (Sebastián Llapur) | «Si cualquiera, estudiante o maestro, pretendiera ayudar al señor Potter, será castigado de una manera consistente con la severidad de su infracción… **Lo invito a que pase al frente, ahora.**» | P8 00:35:29-00:36:33 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/9/9d/HP8SeverusSnape-1.ogg)) | ✅ aviso oficial (oscuro) |
| Ron (Luis Daniel Ramírez) | «**Ay, diablos, ahí va.**» (el «Bloody hell, here we go») | P8 00:33:45 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/8/8f/HP8RonWeasley-1.ogg)) | ✅ |
| Harry (Víctor Ugarte) | «Y no sé qué, pero lo quiere con desesperación… **Me ponen los pelos de punta.**» | P7 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/3/32/HP7HarryPotter-1.ogg)) | ✅ sentido |
| **El vociferador** (Molly: Carmen Martínez) | «**¡Ronald Weasley! ¡Cómo osaste robar el auto! ¡Estoy verdaderamente enojada!** ¡Ahora tu padre enfrenta una averiguación y tienes toda la culpa! ¡Si te atreves una vez más a desobedecer, te regresaré a casa!» … «Ginny, cariño, felicidades por entrar a Gryffindor. **Estamos muy orgullosos.**» | P2 00:34:28 · vídeo [«Howler in different languages», 15:55-16:26](https://www.youtube.com/watch?v=3KNNglv24a0&t=955) (tramo «Latin Spanish») | ✅ oído (Whisper *medium*; escribió «Wisley» y «Chini»). El sentido coincide con el inglés. **Es el grito y la posdata amable en un solo aviso** |
| Alumnos, en el desayuno | «¡Ay, no! **¡Miren nada más! ¡Weasley recibió un vociferador!**» · Neville: «¡Ábrela, Ronald! Una vez no abrí una de la abuela. ¡Fue horrible!» | P2 00:34:11 · mismo vídeo, [15:35-15:48](https://www.youtube.com/watch?v=3KNNglv24a0&t=935) | ✅ oído. En latino es **«vociferador»** |
| Molly (Carmen Martínez) | «Camas vacías, ninguna nota, ni el auto. Pudieron haber muerto…» · «**Ven, Harry, vamos a almorzar.**» | P2 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/0/01/HP2MollyWeasley-1.ogg)) | ✅ sentido |
| Hagrid (Humberto Solórzano) | «**Ahora escúchenme, esto es serio.** … Es peligroso. … No debí decirlo. No debí decir eso.» | P1 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/8/83/HP1RubeusHagrid-1.ogg)) | ✅ sentido. Su manía: se le escapa algo y se arrepiente |
| Harry (Arturo Castañeda) | «¿No lo ven? **¡Nos equivocamos!** Snape no quiere la piedra para él mismo. Quiere la piedra para Voldemort.» | P1 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/a/a9/HP1HarryPotter-1.ogg)) | ✅ sentido |

**La voz de los insertos: El Profeta leído en voz alta** (cierre, 24-sep-2026).
En el doblaje latino, cuando sale texto en pantalla (títulos, titulares,
carteles), **un narrador lo lee**. Doblaje Wiki guarda esas muestras
(«Insertos», «Narración», «Logo»); las pasé por Whisper *medium*. El minuto
sale de los subtítulos en inglés que rodean la escena.

| Qué se lee | Texto del doblaje latino | Dónde | Estado |
|---|---|---|---|
| **Cartel del examen** (P5) | «**Silencio. TIMOS en progreso.** Examen de teoría de encantamientos. Comienza a las 16 horas, termina a las 18.» | P5 ≈01:34:20 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/2/2b/HP5Logo-1.ogg), 0:00-0:05) | ✅ oído. **Un aviso oficial, tal cual** |
| **Titulares de El Profeta** (P5, final) | «**Dumbledore y Potter reivindicados.** ¿Renunciará el ministro? Nuevo residente de Azkaban. Umbridge suspendida. Investigación pendiente. El que no debe ser nombrado, regresa. **Director de Hogwarts, restituido.**» | P5 02:03:25-02:04:35 (misma muestra, 0:06-0:21) | ✅ oído. Voz: Helgar Pedrini (Doblaje Wiki) |
| **Titular de El Profeta** (P6, inicio) | «**Harry Potter, el elegido.** Se derrumba puente. Aumenta el número de muertos.» · y el libro: «Recetas de pociones avanzadas» | P6 ≈00:03:15 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/a/a8/HP6Insertos-2.ogg)) | ✅ oído |
| Cartel y cierre (P8) | «Indeseable número 1, Harry Potter.» · «**19 años después.**» | P8, cartel y rótulo del epílogo ≈01:54 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/5/5c/HP8Insertos-1.ogg)) | ✅ oído |
| Título (P1) | «Harry Potter y la piedra filosofal.» (Francisco Colmenero; hay otra versión de TV con Pedrini) | P1, [muestra](https://static.wikia.nocookie.net/doblaje/es/images/9/96/HP1Logo-1.ogg) | ✅ oído; los dos narradores, Doblaje Wiki y [DubDB](https://dubdb.fandom.com/wiki/Harry_Potter_y_la_piedra_filosofal_(Latin_American_Spanish)) (dos versiones del título) |
| Tráileres doblados | P3: «**Este año** la hechicería se desencadenará y una fuerza siniestra llegará. Todo lo que esperabas se transformará.» · P4: «Este año, su mayor desafío será su momento más sombrío.» · P5: «Este año, la tiranía llegará y la rebelión comenzará.» · P6: «Este año la maldad pasará de su mundo hacia el nuestro y la hora más oscura está a punto de llegar.» | muestras [P3](https://static.wikia.nocookie.net/doblaje/es/images/d/db/HP3NarradorT.ogg), [P4](https://static.wikia.nocookie.net/doblaje/es/images/f/f2/HP4NarracionT.ogg), [P5](https://static.wikia.nocookie.net/doblaje/es/images/5/57/HP5LogoT-1.ogg), [P6](https://static.wikia.nocookie.net/doblaje/es/images/1/18/HP6InsertosT-1.ogg) | ✅ oído. La fórmula «**Este año…**» es la voz de los anuncios de la saga |

**Más frases de personajes** (muestras nuevas, Whisper *medium*):

| Personaje | Frase del doblaje latino | Dónde | Estado |
|---|---|---|---|
| **Flitwick** (Jorge Roig) | «Una de las habilidades más rudimentarias de los magos es la levitación… ¿Todos tienen sus plumas? Bien. Ahora, no olviden el movimiento de muñeca que practicamos… Y digan lo siguiente: *Wingardium leviosa*. **¡Miren todos! La señorita Granger lo hizo. ¡Espléndido!**» | P1 01:05:57 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/6/67/HP1FiliusFlitwick-1.ogg)) | ✅ sentido (igual que el guion inglés; Whisper escribió «evitación» y no entendió el «swish and flick») |
| **Dumbledore** (César Arias) | «Te prometí que podrías acompañarme y me apego a esa promesa, pero con una condición. Debes obedecer sin cuestionar cualquier orden que te dé. **Si te digo que te escondas, te escondes. Si te digo que corras, corres.**» | P6 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/a/aa/HP6AlbusDumbledore-1.ogg)) | ✅ sentido. Una norma dicha con calma |
| Dumbledore | «Entiendo cómo te sientes, Harry. No, es mi culpa…» | P5 02:04:35 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/5/51/HP5AlbusDumbledore-1.ogg)) | ✅ (coincide con «I know how you feel, Harry», 02:04:35) |
| Dumbledore | «Tú, Harry, que no conociste a tu familia, los ves a tu lado… Esta es la razón por la que mañana cambiará de hogar.» (el espejo de Oesed) | P1 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/5/51/HP1AlbusDumbledore-1.ogg)) | ✅ sentido |
| McGonagall (Keta Leonel) | «Sólo le pido que lo que respecta a mis alumnos se conforme con las prácticas disciplinarias tradicionales… **cuestiono sus métodos medievales.**» | P5 ([muestra](https://static.wikia.nocookie.net/doblaje/es/images/7/75/HP5MinervaMcGonagall-1.ogg)) | ✅ sentido |

**Latino frente a España, la misma escena** (vociferador, mismo vídeo):
España dice «Weasley ha recibido un **Howler**», «¿cómo te atreves a robar
el **coche**?», «¡Estoy **absolutamente disgustada**!» ([0:55-1:45](https://www.youtube.com/watch?v=3KNNglv24a0&t=55)).
Latino: «vociferador», «auto», «verdaderamente enojada». **Para el público
del servidor, sólo las del latino.**

**Subtítulos oficiales en español** (HBO Max Latinoamérica, [tráiler de P1](https://www.youtube.com/watch?v=ZgrCZVjPg9g);
no son el guion del doblaje, pero son la traducción oficial): «Eres un mago,
Harry.» «¿Soy un qué?» (0:15-0:17) · «Estimado Sr. Potter, nos complace
informarle que ha sido aceptado en la Escuela Hogwarts de Magia y
Hechicería» (0:23-0:27) · «**Los de primer año deben saber que el bosque
oscuro está estrictamente prohibido**» (1:12-1:16) · «No está permitido usar
magia en los corredores fuera de clase» (1:18) · «El corredor del tercer piso
está restringido para todo aquel que no desee sufrir la muerte más dolorosa»
(1:28-1:33) · «O peor aún, que nos expulsen» (1:49) ✅ (vistos en los
fotogramas).

**Frases que la gente recuerda**
- «**Es Leviosa, no Leviosá**» ✅ ([Vía País](https://viapais.com.ar/streaming/es-leviosa-no-leviosa-ella-es-la-mujer-detras-de-la-voz-de-hermione-de-harry-potter/)).
  En P1 la dijo Mitzy Corona. Original: P1 01:06:44.
- «**Dobby es un elfo libre**» ✅ (muestra de P7, arriba).
- «¡Weasley recibió un vociferador!» y «¡Ronald Weasley!» ✅ (clip de
  arriba, 15:39 y 15:55).
- «Eres un mago, Harry»: así sale en los subtítulos oficiales de HBO Max;
  en el audio latino no lo comprobé ⚠️ (la muestra de Hagrid de Doblaje Wiki
  es de otra escena: «Ahora escúchenme, esto es serio»).

---

## 11 · Música

| Película | Compositor | Fuente |
|---|---|---|
| P1 a P3 | **John Williams** | [wiki: banda sonora de P1](https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Philosopher%27s_Stone_(soundtrack)), [«Hedwig's Theme»](https://harrypotter.fandom.com/wiki/Hedwig%27s_Theme) ✅ (con la 1.ª pasada) |
| P4 | **Patrick Doyle** | [wiki: banda sonora de P4](https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Goblet_of_Fire_(soundtrack)) ✅ |
| P5 y P6 | **Nicholas Hooper** | [wiki: banda sonora de P5](https://harrypotter.fandom.com/wiki/Harry_Potter_and_the_Order_of_the_Phoenix_(soundtrack)) ✅ |
| P7 y P8 | **Alexandre Desplat** | [wiki: Alexandre Desplat](https://harrypotter.fandom.com/wiki/Alexandre_Desplat) («scored Part 1 and Part 2»), que cita a Film Score Monthly ✅ |

- **«Hedwig's Theme»** (Williams) nació dentro del «Prologue» de P1 y sonó en
  los créditos. **Todos los compositores siguientes lo citan** en sus
  películas, y también los juegos (James Hannigan). Hagrid lo toca con la
  flauta en P1; Luna lo tararea en el juego de P6 ([wiki](https://harrypotter.fandom.com/wiki/Hedwig%27s_Theme)) ✅.
  Celesta, misterio amable: **es el ambiente de #anuncios**.
- En el [clip oficial del discurso de P3](https://www.youtube.com/watch?v=dvFehFzph7I&t=13)
  se ve **el coro de ranas** que dirige Flitwick (0:13-0:39) antes del
  discurso: la bienvenida con música es parte del ritual ✅ visto (sin audio).
- Para #anuncios: la época de Williams. La de Desplat es triste.

---

## 12 · Vídeos

**Cómo los miré (2.ª pasada).** `herramientas/fotogramas.py` no pudo bajar de
YouTube: «Sign in to confirm you're not a bot», «This video is not
available» y 429 (somos varios ayudantes con la misma IP; lo reintenté con 6
clientes de yt-dlp y en 3 momentos). Con yt-dlp sí salen los datos y los
***storyboards***: las miniaturas oficiales de YouTube, **una cada 1-2 s**,
a 320×180 o 160×90. Con Pillow las monté en hojas numeradas con su minuto
(±2 s) y **las miré**. Sirven para pose, encuadre, luz y color; para
recortar, la wiki (§2.0).

**Vídeo de verdad, con `fotogramas.py`**: dos vídeos que están en el
**Internet Archive** (bajan sin bloqueo): la escena del vociferador en
**1920×1080** y el tráiler final oficial de P6 (1130×480; hay .mov de
1920×816). Fotograma cada 2-3 s y fotogramas grandes de los momentos
clave, mirados uno a uno. Los `video.mp4` se borraron al terminar.

**Cierre (tercer ayudante)**: YouTube seguía igual (probé `web_safari`,
`mweb` y `tv_embedded`: sólo *storyboards* o «Sign in»). Pasé
`fotogramas.py` por **5 vídeos más**: el **tráiler oficial de P1** (2001,
1280×720) y el **primer *teaser*** (848×480), los dos en el Internet
Archive; un **fragmento de P1 en 1920×796** que publica el proyecto
académico TECHNÈS (Universidad de Montreal) en el Internet Archive; y dos
copias de fan en **Dailymotion** (512 px, audio francés): Dobby libre (P2)
y Luna en el carruaje (P5). Borrados los `video.mp4`.

### 12.1 Los que miré fotograma a fotograma

| Vídeo (canal, fecha, duración) | Lo que se ve, con su minuto |
|---|---|
| **Comienzo (el «opening»)**: [«The First 10 Minutes», P1](https://www.youtube.com/watch?v=PdVxAuFY1Bk) (canal oficial Harry Potter, 6-ene-2026, 10:09) | [0:00](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=0) letrero **«PRIVET DRIVE»** de noche con una lechuza. [0:29-0:34](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=29) Dumbledore apaga las farolas con el apagador. [1:19](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=79) McGonagall. [2:08](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=128) Hagrid en la moto. [3:08](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=188) **Dumbledore deja la carta** sobre el bebé; [3:23](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=203) el sobre en tinta verde. [3:37](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=217) **el logo dorado sobre nubes**. [5:36](https://www.youtube.com/watch?v=PdVxAuFY1Bk&t=336) el zoo |
| **Final (el «ending»)**: [«19 Years Later», P8](https://www.youtube.com/watch?v=yv-UwwOvOzA) (canal oficial, 1-sep-2017, 3:47, 16,7 millones de visitas) | [0:01-0:09](https://www.youtube.com/watch?v=yv-UwwOvOzA&t=1) la estación de King's Cross, ladrillo rojo. [0:15](https://www.youtube.com/watch?v=yv-UwwOvOzA&t=15) **jaulas de lechuza** en los carritos. [0:51-0:59](https://www.youtube.com/watch?v=yv-UwwOvOzA&t=51) **el expreso rojo echando vapor** bajo la bóveda de hierro. [1:13](https://www.youtube.com/watch?v=yv-UwwOvOzA&t=73) Harry y Ginny con sus hijos |
| **Tráiler latino** de P1: [«Harry Potter y la piedra filosofal · Trailer · HBO Max»](https://www.youtube.com/watch?v=ZgrCZVjPg9g) (HBO Max Latinoamérica, 27-dic-2021, 2:19, 1,7 millones) | **Subtitulado en español**, no doblado. [0:03](https://www.youtube.com/watch?v=ZgrCZVjPg9g&t=3) Hedwig en la jaula. [0:15](https://www.youtube.com/watch?v=ZgrCZVjPg9g&t=15) «Eres un mago, Harry.» [0:23-0:27](https://www.youtube.com/watch?v=ZgrCZVjPg9g&t=23) «Estimado Sr. Potter, nos complace informarle…». [0:33-0:35](https://www.youtube.com/watch?v=ZgrCZVjPg9g&t=33) el Gran Comedor con velas. [1:12-1:16](https://www.youtube.com/watch?v=ZgrCZVjPg9g&t=72) **Dumbledore, de pie en la mesa: «el bosque oscuro está estrictamente prohibido»**. [2:05](https://www.youtube.com/watch?v=ZgrCZVjPg9g&t=125) **logo «Harry Potter y la piedra filosofal»** |
| **Tráiler doblado** de P8: [«trailer 2 doblado · oficial WB»](https://www.youtube.com/watch?v=-kDonIIXuqo) (Warner Bros. Pictures Latinoamérica, 17-jun-2011, 2:26) | Fotogramas de 105×45: se ven las **cartelas en español** «CADA MOMENTO DE SU VIDA» ([0:09](https://www.youtube.com/watch?v=-kDonIIXuqo&t=9)), «LO HA LLEVADO A ESTO» ([0:19](https://www.youtube.com/watch?v=-kDonIIXuqo&t=19)), «ESTE AÑO» ([0:52](https://www.youtube.com/watch?v=-kDonIIXuqo&t=52)), «SE ACABA» ([1:00](https://www.youtube.com/watch?v=-kDonIIXuqo&t=60)), en romanas grabadas entre humo. Tono de guerra: qué NO |
| **Spot de TV** de P7: [«El elegido»](https://www.youtube.com/watch?v=IqlkIE5s1UA) (Warner Bros. Pictures México, 2-nov-2010, 0:32) | Subtítulos en español: «¡Uno!», «¡Dos!», «¿Dónde demonios estás?», «Siempre estoy enfadada con él» ([0:16](https://www.youtube.com/watch?v=IqlkIE5s1UA&t=16)). [0:25](https://www.youtube.com/watch?v=IqlkIE5s1UA&t=25) **Dobby aparece con los brazos abiertos**. [0:28](https://www.youtube.com/watch?v=IqlkIE5s1UA&t=28) «PRÓXIMAMENTE SÓLO EN CINES» |
| Escena 1: [«Dumbledore's Speech · Full Scene», P3](https://www.youtube.com/watch?v=dvFehFzph7I) (canal oficial, 5-sep-2025, 4:54) | [0:13-0:39](https://www.youtube.com/watch?v=dvFehFzph7I&t=13) coro de ranas bajo cientos de velas. [0:43](https://www.youtube.com/watch?v=dvFehFzph7I&t=43) **brazos abiertos tras el atril del búho**. [0:57](https://www.youtube.com/watch?v=dvFehFzph7I&t=57) el búho dorado de cerca. [1:05](https://www.youtube.com/watch?v=dvFehFzph7I&t=65) presenta a Lupin. [2:42](https://www.youtube.com/watch?v=dvFehFzph7I&t=162) **los dos índices arriba**. [2:48](https://www.youtube.com/watch?v=dvFehFzph7I&t=168) apaga una vela con los dedos. [4:02](https://www.youtube.com/watch?v=dvFehFzph7I&t=242) en el dormitorio alguien lee El Profeta |
| Escena 2: [«Ron receives a Howler», P2](https://www.youtube.com/watch?v=fBziSx7RtqY) (canal oficial, 22-mar-2018, 1:27, 6,1 millones) | [0:02](https://www.youtube.com/watch?v=fBziSx7RtqY&t=2) desayuno: libros abiertos y bandejas en la mesa. [0:17](https://www.youtube.com/watch?v=fBziSx7RtqY&t=17) **se abre el sobre rojo**. [0:25](https://www.youtube.com/watch?v=fBziSx7RtqY&t=25) **boca de papel con dientes**. [0:39](https://www.youtube.com/watch?v=fBziSx7RtqY&t=39) grita a Ron a la cara. [0:49](https://www.youtube.com/watch?v=fBziSx7RtqY&t=49) Ginny mira. [0:57](https://www.youtube.com/watch?v=fBziSx7RtqY&t=57) confeti rojo sobre la mesa |
| Escena 3: [«It's Leviosa, Not Leviosaaa!», P1](https://www.youtube.com/watch?v=Qgr4dcsY-60) (canal oficial, 14-may-2021, 1:12, 5 millones) | [0:04](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=4) **Hermione agarra el brazo de Ron**. [0:10-0:13](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=10) explica, cejas altas. [0:17](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=17) **ojos cerrados, barbilla alta**. [0:25](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=25) la pluma flota. [0:29](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=29) Flitwick feliz. [0:43](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=43) explota la pluma de Seamus |
| Escena 4: [«Introducing Luna Lovegood», P5](https://www.youtube.com/watch?v=8k2bj-R9m8E) (canal oficial, 19-oct-2017, 1:59, 3,4 millones) | [0:02](https://www.youtube.com/watch?v=8k2bj-R9m8E&t=2) camino del bosque con farolas. [0:24-0:30](https://www.youtube.com/watch?v=8k2bj-R9m8E&t=24) el thestral. [0:53-1:07](https://www.youtube.com/watch?v=8k2bj-R9m8E&t=53) **Luna tras El Quisquilloso** en el carruaje. [1:09](https://www.youtube.com/watch?v=8k2bj-R9m8E&t=69) **mira a Harry**. Luz de noche azul verdosa `#1D464A` |
| Escena 5: [«Dobby is a Free Elf», P2](https://www.youtube.com/watch?v=8DTb-lseCdQ) (canal oficial, 20-feb-2018, 2:36, 9,9 millones) | Fotogramas de 160×90. [0:59](https://www.youtube.com/watch?v=8DTb-lseCdQ&t=59) Dobby con el diario. [1:34](https://www.youtube.com/watch?v=8DTb-lseCdQ&t=94) **Dobby erguido con el calcetín**. [1:58](https://www.youtube.com/watch?v=8DTb-lseCdQ&t=118) **cabeza ladeada, feliz**. Claustro de piedra con luz blanca |
| Créditos de P3 ([copia de fan, «Mr End Credits»](https://www.youtube.com/watch?v=MJzymmFvtlk), 23-dic-2022, 4:08) | No es oficial. [0:07](https://www.youtube.com/watch?v=MJzymmFvtlk&t=7) logo en mancha de tinta; [0:11-1:33](https://www.youtube.com/watch?v=MJzymmFvtlk&t=11) **cada crédito en una cinta de pergamino** con huellas |
| **Escena 6, en 1080p con `fotogramas.py`**: [«Ron receives a Howler in different languages»](https://www.youtube.com/watch?v=3KNNglv24a0) (Compare Languages, 13-ago-2022, 21:10, 722 251 visitas; [copia en el Internet Archive](https://archive.org/details/youtube-3KNNglv24a0), 1920×1080) | No oficial: montaje de fan con el audio oficial de 23 doblajes. 28 fotogramas del tramo inglés, uno cada 2 s: [0:00](https://www.youtube.com/watch?v=3KNNglv24a0&t=0) Ron y Neville en la mesa, lechuza encima, cuencos de copos y libros abiertos; [0:08](https://www.youtube.com/watch?v=3KNNglv24a0&t=8) una jarra de zumo de naranja en la mesa de Slytherin; [0:16](https://www.youtube.com/watch?v=3KNNglv24a0&t=16) **el sobre en la mano, etiqueta en caligrafía**; [0:24-0:28](https://www.youtube.com/watch?v=3KNNglv24a0&t=24) **se dobla en boca con dientes**, texto de carta dentro; [0:32](https://www.youtube.com/watch?v=3KNNglv24a0&t=32) **Ron aterrado**; [0:40](https://www.youtube.com/watch?v=3KNNglv24a0&t=40) le grita a la cara; [0:50](https://www.youtube.com/watch?v=3KNNglv24a0&t=50) Ginny mira de reojo. **Doblaje latino: [15:35-16:30](https://www.youtube.com/watch?v=3KNNglv24a0&t=935)**; España: 0:55-1:50 |
| **Tráiler con `fotogramas.py`**: tráiler final oficial de P6, 2:27 ([Internet Archive, colección de tráileres oficiales](https://archive.org/details/harry-potter-and-the-half-blood-prince-official-trailer-video-collection)) | 50 fotogramas, uno cada 3 s. 0:09-0:15 mar verde contra el acantilado; 0:27 fuego naranja; 0:44 **Hermione en la mesa de Gryffindor, un libro abrazado contra el pecho, mirada de reojo**, copas de peltre; 1:33 Harry y Ginny; 1:36 gradas de quidditch con estandartes rojos; 2:18 **el logo en acero gris**, no en oro. Paleta verde azulada y fuego: **época oscura, qué NO para #anuncios** |
| Escena 7 (*storyboard*): [«Baile de Navidad», P4](https://www.youtube.com/watch?v=_WBTnZgWKAE) (**HBO Max Latinoamérica**, 29-jun-2022, 3:32, 323 028 visitas) | Clip oficial latino, sin subtítulos. [0:29-0:43](https://www.youtube.com/watch?v=_WBTnZgWKAE&t=29) McGonagall con sombrero negro de ala enorme habla con Harry; [1:19-1:35](https://www.youtube.com/watch?v=_WBTnZgWKAE&t=79) **Hermione baja la escalera con el vestido rosa**; [1:41-1:46](https://www.youtube.com/watch?v=_WBTnZgWKAE&t=101) se abren las puertas al salón helado. Luz de antorchas ámbar |
| **Tráiler (tema principal), con `fotogramas.py`**: [tráiler oficial de P1, 2001, 720p](https://archive.org/details/harry-potter-and-the-sorcerers-stone-2001-720p-trailer) (Internet Archive, 2:23; suena «Hedwig's Theme») | 48 fotogramas, uno cada 3 s. [0:03](https://archive.org/download/harry-potter-and-the-sorcerers-stone-2001-720p-trailer/Harry%20Potter%20and%20the%20Sorcerers%20Stone_2001_720p_trailer.mp4#t=3) el callejón Diagon; 0:12-0:18 Harry con la varita en Ollivander; [0:36](https://archive.org/download/harry-potter-and-the-sorcerers-stone-2001-720p-trailer/Harry%20Potter%20and%20the%20Sorcerers%20Stone_2001_720p_trailer.mp4#t=36) **los de primero suben por el pasillo central del Gran Comedor bajo cientos de velas**, enmarcados por las puertas talladas; 0:48 clase de vuelo en el césped; [1:15](https://archive.org/download/harry-potter-and-the-sorcerers-stone-2001-720p-trailer/Harry%20Potter%20and%20the%20Sorcerers%20Stone_2001_720p_trailer.mp4#t=75) **Dumbledore (Harris) de pie en la mesa de profesores**; 1:39 banquete con Quirrell; 1:48 el ajedrez; [2:12](https://archive.org/download/harry-potter-and-the-sorcerers-stone-2001-720p-trailer/Harry%20Potter%20and%20the%20Sorcerers%20Stone_2001_720p_trailer.mp4#t=132) logo dorado con lechuza; [2:15](https://archive.org/download/harry-potter-and-the-sorcerers-stone-2001-720p-trailer/Harry%20Potter%20and%20the%20Sorcerers%20Stone_2001_720p_trailer.mp4#t=135) «THE MAGIC BEGINS / SOON». Medido en 0:36: mesas `#5A4131`, puertas `#2D1C13`, llama de antorcha `#F0CAB2`; en 1:15: gorro de Dumbledore `#652B31`, copa `#895F36`, piedra `#494E46` |
| ***Teaser* de P1, con `fotogramas.py`**: [«trailer 1»](https://archive.org/details/HarryPotterTheSorcerersStoneTrailer1) (Internet Archive, 1:50) | 37 fotogramas. [0:15](https://archive.org/download/HarryPotterTheSorcerersStoneTrailer1/HarryPotterTheSorcerersStoneTrailer1.mp4#t=15) **lechuzas volando sobre las nubes del logo de Warner**; [0:18-0:21](https://archive.org/download/HarryPotterTheSorcerersStoneTrailer1/HarryPotterTheSorcerersStoneTrailer1.mp4#t=18) **la lluvia de cartas** y Harry cazando una; [0:24](https://archive.org/download/HarryPotterTheSorcerersStoneTrailer1/HarryPotterTheSorcerersStoneTrailer1.mp4#t=24) **el sobre en tinta verde** («Mr. H. Potter, The Cupboard under the Stairs…»); 0:27-0:33 el expreso rojo; [0:51](https://archive.org/download/HarryPotterTheSorcerersStoneTrailer1/HarryPotterTheSorcerersStoneTrailer1.mp4#t=51) **Dumbledore bebe de una copa dorada**, gorro burdeos con estrellas; 1:15 Hedwig. **El aviso que llega sí o sí**: la mejor secuencia para #anuncios |
| **Escena, con `fotogramas.py`**: [fragmento de P1, Navidad y Sección Prohibida](https://archive.org/details/670343) (TECHNÈS, Universidad de Montreal, Internet Archive; 1920×796, 1:50) | 55 fotogramas, uno cada 2 s. 0:00-0:12 Ron con el jersey de la «R» y Harry probándose la capa junto al árbol; [0:14](https://archive.org/download/670343/colombus_harry_potter_philosophers_stone_extrait.HD.mp4#t=14) y [0:20](https://archive.org/download/670343/colombus_harry_potter_philosophers_stone_extrait.HD.mp4#t=20) **el tablón de anuncios de Gryffindor**, fieltro rojo en cuadros con cordón rojo y oro y tarjetas clavadas; [0:29](https://archive.org/download/670343/colombus_harry_potter_philosophers_stone_extrait.HD.mp4#t=29) la cabeza de Harry flotando ante el tablón; 0:34-1:34 la Sección Prohibida con farol, estanterías y el cartel «RESTRICTED» tallado |
| **Escena, con `fotogramas.py`**: [«Dobby Est Libre (Scène Culte)», P2](https://www.dailymotion.com/video/x3d4quh) (Dailymotion, copia de fan, audio francés, 512×216, 4:21) | 66 fotogramas, uno cada 4 s. 0:12-1:28 Dumbledore (Harris) y Lucius en el despacho; [2:44](https://www.dailymotion.com/video/x3d4quh?start=164) Dobby, encogido, **sostiene el diario con las dos manos**; [3:00](https://www.dailymotion.com/video/x3d4quh?start=180) **alarga un dedo hacia el calcetín**; [3:20](https://www.dailymotion.com/video/x3d4quh?start=200) **se planta ante Harry con las palmas abiertas** en el claustro; [4:00](https://www.dailymotion.com/video/x3d4quh?start=240) **cabeza ladeada, ojos húmedos**, arco con montañas detrás |
| **Escena, con `fotogramas.py`**: [«Luna Lovegood», P5](https://www.dailymotion.com/video/x3dhmzl) (Dailymotion, canal Hitek, 512×288, 1:23) | 42 fotogramas, uno cada 2 s. 0:16-0:22 los carruajes con faroles en el bosque azul; [0:44](https://www.dailymotion.com/video/x3dhmzl?start=44) Luna sentada, **botas rojas**; [0:48](https://www.dailymotion.com/video/x3dhmzl?start=48) **El Quisquilloso al revés**, ella mira por encima; [1:06](https://www.dailymotion.com/video/x3dhmzl?start=66) la revista en el regazo, collar de corchos, chaqueta ciruela |
| Escenas 8-12 (*storyboards* 160×90, para las poses de §15) | [P4, los campeones](https://www.youtube.com/watch?v=pLv1HXl_J10) (canal oficial, 5:04): [1:33](https://www.youtube.com/watch?v=pLv1HXl_J10&t=93) **Dumbledore con los brazos abiertos de par en par**, cáliz de fuego azul, luz fría. [P5, «Joining Dumbledore's Army»](https://www.youtube.com/watch?v=HOKRi1yJfJU) (oficial, 3:27): [0:33](https://www.youtube.com/watch?v=HOKRi1yJfJU&t=33) Hermione de pie ante el grupo en Cabeza de Puerco. [P5, «Harry Trains Dumbledore's Army»](https://www.youtube.com/watch?v=SnmpiWHrRSA) (oficial, 9:33): [3:12](https://www.youtube.com/watch?v=SnmpiWHrRSA&t=192) **el Decreto n.º 82 clavado en la pared**, [3:22](https://www.youtube.com/watch?v=SnmpiWHrRSA&t=202) Harry enseña señalando. [P7, «Escape From Malfoy Manor»](https://www.youtube.com/watch?v=R2zNRrOXbPY) (Movieclips, 3:42): [2:44-2:54](https://www.youtube.com/watch?v=R2zNRrOXbPY&t=164) Dobby erguido ante Bellatrix. [P1, clase de Pociones](https://www.youtube.com/watch?v=hMIN4wmHuiA) (Warner Bros. Entertainment, 3:32): mazmorra en sepia con haces de luz; no se ve a Hermione alzar la mano |

### 12.2 Otros vídeos (existen: comprobados con yt-dlp el 24-sep-2026)

También existen (vistos en la búsqueda de YouTube, no mirados): el
[teaser latino de la serie de HBO](https://www.youtube.com/watch?v=H2Gf5fWQw2s)
(HBO Max Latinoamérica, 2:28) y el [spot «El Final» de P8 en español](https://www.youtube.com/watch?v=SZ2rMkFvVAw)
(Warner Bros. Pictures México, 1:03).


| Vídeo | Qué sirve | Datos |
|---|---|---|
| [Entrevista a Leyla Rangel](https://www.youtube.com/watch?v=__pudICRBDk) (Capa Invisible) | voz latina de Hermione; la entrevista que cita Doblaje Wiki sobre sus castings | 5:59, 16-dic-2017, 640 232 visitas ✅ |
| [Entrevista a Víctor Ugarte (1)](https://www.youtube.com/watch?v=6yFHCEmRWzw) (Activa TV Honduras) · [(2)](https://www.youtube.com/watch?v=vHlRVV9pQ3Q) (James S.U.) | voz latina de Harry | 29:24 (2016) · 1:42:27 (2021) ✅ |
| [Podcast de Otaku Press con Ugarte](https://soundcloud.com/sofiapichihua/victor-ugarte-voz-de-harry-potter-y-sasuke-cuenta-sus-secretos-de-doblaje) | sus secretos de doblaje | existe: «Víctor Ugarte: Voz de Harry Potter y Sasuke cuenta sus secretos de doblaje», Otaku Press podcast ✅ (no lo escuché) |
| [Diario de desarrollo del arte de Magic Awakened](https://www.youtube.com/watch?v=Z_BJLuv5WiI) (canal oficial Harry Potter) | estilo de libro ilustrado. Capítulos: [inspiración 1:12](https://www.youtube.com/watch?v=Z_BJLuv5WiI&t=72), [luz 1:46](https://www.youtube.com/watch?v=Z_BJLuv5WiI&t=106), [diseño de personajes 2:00](https://www.youtube.com/watch?v=Z_BJLuv5WiI&t=120), [cartas 3:05](https://www.youtube.com/watch?v=Z_BJLuv5WiI&t=185) | 4:21, 11-jul-2023 ✅ |
| [Entrevista al artista jefe de Magic Awakened](https://www.youtube.com/watch?v=kBeIPiTRVuw) (canal del juego) | cómo dibujan a los personajes | 4:52, 18-jul-2023 ✅ |
| [Los decretos de Educación](https://www.youtube.com/watch?v=gwwD3rlAGzU) (Vermilion Studios) | la pared de decretos | 3:21, 23-sep-2019 ✅ |
| [Tráiler en español de P5](https://www.youtube.com/watch?v=fYBe1RNqaAw) (Warner Bros. Pictures México) | tráiler oficial en español | 2:16, 27-abr-2007 ✅ (fotogramas de 105×45, casi ilegibles) |
| [Clases de UI de Magic Awakened en Bilibili](https://www.bilibili.com/video/BV1vA411e7Az/) | controles de interfaz, en chino | «【神奇美术公开课】《哈利波特魔法觉醒》界面风格——界面控件» (clase pública sobre el estilo de la interfaz: los controles), canal 神奇美术, 1:04:31, 9-jul-2020 ✅ (datos con yt-dlp; no la vi) |
| [Featurette de Hogwarts Legacy](https://www.harrypotter.com/news/go-behind-the-scenes-of-hogwarts-legacy) | detrás de cámaras | existe: «Go behind the scenes of Hogwarts Legacy with a new featurette» ✅ (no lo vi) |

Ninguno de estos vídeos tiene subtítulos (comprobado con yt-dlp).

**TikTok**: vivos los memes «Dobby es un elfo libre»
([1](https://www.tiktok.com/discover/eres-libre-dobby),
[2](https://www.tiktok.com/@valeria_arvizug/video/7322549984585387269)) y
las actrices latinas en convenciones (Lu Leal en la EXPOMAC Veracruz, 18 de
diciembre de 2022). Del segundo saqué los datos por el *oEmbed* de TikTok:
«Dobby es un elfo libre. 🧦⚡️ #dobby #elfo #harrypotter… #doblaje», de
Valeria Arvizu (@valeria_arvizug) ✅. El vídeo en sí no lo vi.

---

## 13 · Videojuegos de la franquicia

| Juego | Interfaz y diálogo | Fuente |
|---|---|---|
| La piedra filosofal, PC, 2001 | frases habladas; más de 100 de Harry sin usar | [TCRF](https://tcrf.net/Harry_Potter_and_the_Sorcerer's_Stone_(Windows,_Mac_OS_Classic,_Mac_OS_X)/Unused_Dialogue) |
| La cámara secreta, PC | un nivel de desafío entero sin usar tras una puerta de la sala común | [TCRF](https://new.tcrf.net/Harry_Potter_and_the_Chamber_of_Secrets_(Windows,_Mac_OS_Classic,_Mac_OS_X)) |
| La cámara secreta, GBC, 2002 | RPG con cajas de texto; último juego con licencia de GBC en Norteamérica | [TCRF](https://tcrf.net/Harry_Potter_and_the_Chamber_of_Secrets_(Game_Boy_Color)), [StrategyWiki](https://strategywiki.org/wiki/Harry_Potter_and_the_Chamber_of_Secrets_(Game_Boy_Color)) |
| Hogwarts Mystery, 2018 | móvil; retrato y caja | [Wikipedia](https://en.wikipedia.org/wiki/Harry_Potter:_Hogwarts_Mystery) |
| Magic Awakened | libro ilustrado, páginas que pasan, animación Spine en las cartas | [GameRes](https://www.gameres.com/885575.html), [ZCOOL](https://www.zcool.com.cn/article/ZMTI5OTkwNA==.html) |
| Hogwarts Legacy, 2023 | HUD mínimo, Guía de campo, subtítulos | [Deltia's](https://deltiasgaming.com/hogwarts-legacy-user-interface/), [Interface In Game](https://interfaceingame.com/screenshots/hogwarts-legacy-hud-7/) |

**Hogwarts Legacy tiene doblaje latino** ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Hogwarts_Legacy),
leído por la API; [TV Azteca](https://www.tvazteca.com/aztecadeportes/hogwarts-legacy-revela-las-voces-de-su-doblaje)
publicó las voces ✅): estudio **Pink Noise**, cinco directores a la vez
(Alan Fernando Velázquez, Angélica Villa, Gaby Willer, Rick Loera, Rebeca
Gómez). **César Arias hizo a Dumbledore en el tráiler de presentación: fue
su último Dumbledore.** Confirmado también por
[ANMTV](https://www.anmtvla.com/2023/02/hogwarts-legacy-warner-bros-games.html)
(nota de Warner Bros. Games) ✅: Natsai «Natty» Onai es **Lulú (Lourdes)
Arruti**; Nick Casi Decapitado, **Álvaro Sarlich** (antes puse «Salarich»),
que lo tomó tras la muerte de Alfonso Ramírez (2019); y la subdirectora
**Matilda Weasley es Magda Giner**, la McGonagall latina de P1. El profesor
Fig (Jaime Vega), Sebastian Sallow (Alberto Bernal) y Poppy (Jocelyn
Robles) sólo salen en Doblaje Wiki ⚠️.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen
- «Es Leviosa, no Leviosá» (P1 01:06:44).
- El calcetín de Dobby (P2 02:25:12) y «Dobby es un elfo libre».
- El vociferador de Ron (P2 00:34:28).
- «Juro solemnemente que mis intenciones no son buenas» y «Travesura
  realizada» (P3 00:57:24 y 00:58:15).
- Dumbledore zarandeando a Harry: «Did you put your name in the Goblet of
  Fire?» (P4 00:35:21; [escena oficial](https://www.youtube.com/watch?v=pLv1HXl_J10)).
  El fandom se ríe de que en el libro lo pregunta **con calma**: «[*Dumbledore
  said calmly*](https://www.reddit.com/r/harrypotter/comments/u7z4uc/dumbledore_said_calmly/)»
  (7 429 votos, 2022) y hasta «[Kelce said calmly](https://www.reddit.com/r/harrypotter/comments/1apc4pf/kelce_said_calmly/)»
  (13 501 votos, 2024) ✅ (Reddit por Arctic Shift).
- Los *nargles* de Luna (P5 00:30:06) y sus gafas espectrales.
- «Won-Won», el mote que le pone Lavender a Ron (P6 01:21:27).
- «Always» de Snape (P8 01:22:37).
- **El Profeta como sección de noticias**: en r/harrypotter se pidió
  «[renombrar la etiqueta *News* como *Daily Prophet*](https://www.reddit.com/r/harrypotter/comments/11ntalv/petition_for_this_subreddit_to_have_news_be/)»
  (820 votos, 10-mar-2023). El meme «[Daily prophet intensifies](https://www.reddit.com/r/harrypotter/comments/j9vi8r/daily_prophet_intensifies/)»
  tiene 35 335 votos (2020) ✅. **Para un fan, un canal de anuncios que es El
  Profeta tiene todo el sentido.**
- **Luna**: «[Everyone needs to have a Luna in their lives ✨](https://www.reddit.com/r/harrypotter/comments/1nq24gz/everyone_needs_to_have_a_luna_in_their_lives/)»
  (6 555 votos, 25-sep-2025) ✅.

### Qué NO hacer (lo que un fan notaría)
- **Globo de cómic** o burbuja blanca.
- **El atril del búho en una escena de P1 o P2**: no existía hasta P3.
- **Cabecera de P5 («DAILY PROPHET» de palo) con Harry niño**: son épocas
  distintas.
- **Voces o frases del redoblaje argentino de 2019 o del doblaje de España**
  presentadas como «las latinas».
- **Fotos que no se mueven** en El Profeta: si hay foto, que sea un
  fotograma con algo de movimiento sugerido, no un retrato de estudio.
- Mezclar épocas: cabecera de propaganda con Harry de 11 años.
- Poner a Luna en la sala común de Gryffindor: es de Ravenclaw.
- Hacer hablar a Dobby en primera persona: **siempre** dice «Dobby».
- Dumbledore gritando para un aviso amable: el aviso del atril es sereno.
- Usar la escena de la muerte de Dobby para algo alegre.
- Letras de logo que rompen las tildes (Harry P: sección 6.3).
- Colores chillones: la paleta es vela, madera, oro viejo y papel crema.

---

## 15 · Poses analizadas por personaje

> **2.ª pasada**: cada pose dice de dónde sale. «✅ clip» = la vi en un
> clip oficial (*storyboard*, ±2 s) o en un fotograma 1080p; «✅ hoja» =
> la vi en la imagen de la hoja de contacto (P·, O·, F·, §2.0). Las pocas
> que siguen marcadas como dudosas tienen el minuto y la frase comprobados en los
> subtítulos, pero **el gesto no lo vi**: mirar el fotograma antes de
> recortar.

### Hermione

| Dónde | Qué hace el cuerpo | Visto | Sirve para |
|---|---|---|---|
| P1, [clip Leviosa 0:04](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=4) | **agarra el brazo de Ron** para frenarlo, se inclina hacia él | ✅ clip | **regañar**, corregir |
| P1, [clip 0:10-0:15](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=10) | explica con la cabeza ladeada, cejas altas, boca muy abierta | ✅ clip | **explicar** |
| P1, [clip 0:17-0:18](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=17) | **ojos cerrados, barbilla alta**: «ya lo sé» | ✅ clip | presentar con orgullo |
| P1, [clip 0:21](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=21) | giro de muñeca con la varita, codo pegado | ✅ clip | explicar, demostrar |
| P1, [clip 0:33-0:35](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=33) | sonrisa satisfecha mirando la pluma que flota | ✅ clip | **celebrar** |
| P6, tráiler final 0:44 (§12) | sentada, **libro abrazado al pecho, mirada de reojo**, boca apretada | ✅ fotograma grande | **regañar**, pensar |
| P1, Pociones, [captura de la wiki](https://static.wikia.nocookie.net/harrypotter/images/9/9f/Hermione_with_her_Hand_Up.jpg) (500×759) | **brazo derecho recto hacia arriba**, dedos juntos, ojos muy abiertos, boca entreabierta: «¡yo sé!» (el guion transcrito lo confirma) | ✅ imagen | **pedir la palabra, explicar**; muy reconocible |
| P·1 (promo P3) | de pie, erguida, una mano apoyada en el mueble, gato al lado | ✅ hoja | **presentar** |
| P·2 (render PAS) | libros abrazados, sonrisa, recortable | ✅ hoja | explicar, **animar** |
| P4, [clip «Baile de Navidad» 1:19-1:35](https://www.youtube.com/watch?v=_WBTnZgWKAE&t=79) | baja la escalera con el vestido rosa, sonríe | ✅ clip | **qué NO** (gala) |
| P5 00:54:01, [clip oficial «Joining Dumbledore's Army» 0:33-0:53](https://www.youtube.com/watch?v=HOKRi1yJfJU&t=33) | **de pie ante el grupo sentado**, erguida, manos bajas, abrigo oscuro y jersey blanco de rombos; Harry a un lado. «Ya saben a qué vinieron» | ✅ clip | **explicar a un grupo** |

### Luna

| Dónde | Qué hace el cuerpo | Visto | Sirve para |
|---|---|---|---|
| P5, [clip del carruaje 0:53-1:07](https://www.youtube.com/watch?v=8k2bj-R9m8E&t=53) | **lee El Quisquilloso levantado con las dos manos**, tapándose la cara | ✅ clip | leer la prensa (concepto A) |
| P5, [clip 1:09-1:12](https://www.youtube.com/watch?v=8k2bj-R9m8E&t=69) | asoma por encima de la revista y **mira a Harry sin parpadear**, media sonrisa | ✅ clip | presentar, **animar** |
| P5, [clip 1:22](https://www.youtube.com/watch?v=8k2bj-R9m8E&t=82) | la revista en el regazo, cabeza un poco ladeada | ✅ clip | pensar |
| P5, [vídeo real 0:48](https://www.dailymotion.com/video/x3dhmzl?start=48) (512 px) | sostiene **El Quisquilloso abierto y al revés** a la altura del pecho, con las dos manos; mira por encima, cabeza ladeada, media sonrisa | ✅ vídeo | **el guiño de Luna**; animar |
| P5, [vídeo real 1:06](https://www.dailymotion.com/video/x3dhmzl?start=66) | mira hacia abajo, la revista en el regazo, collar de corchos colgando | ✅ vídeo | pensar, leer |
| P·11 | gafas espectrales puestas, **El Quisquilloso abrazado** | ✅ hoja | el guiño al fan |
| P·12 | lee El Quisquilloso abierto, con la portada hacia nosotros | ✅ hoja | enseñar un titular |
| P·15 (Pottermore) | de pie **ante avisos clavados en la pared** | ✅ hoja | concepto C |
| P·10 | **sombrero de león** en la cabeza | ✅ hoja | celebrar, animar |
| P6 00:22:36 | «Quibbler… Quibbler»: **corre por el pasillo del tren con la revista en la mano** y se la da a Ginny | ✅ texto (wiki + guion transcrito); no lo vi en imagen | presentar, repartir |

### Dobby

| Dónde | Qué hace el cuerpo | Visto | Sirve para |
|---|---|---|---|
| P2, [clip del calcetín 0:45](https://www.youtube.com/watch?v=8DTb-lseCdQ&t=45) | pequeño, de pie junto a Harry, orejas caídas | ✅ clip | presentar |
| P2, [clip 0:59-1:03](https://www.youtube.com/watch?v=8DTb-lseCdQ&t=59) | **sostiene el diario con las dos manos** y mira dentro: ahí está el calcetín | ✅ clip | **presentar un objeto** |
| P2, [clip 1:34](https://www.youtube.com/watch?v=8DTb-lseCdQ&t=94) | de pie, erguido, con el calcetín | ✅ clip | **celebrar** |
| P2, [clip 1:58-2:00](https://www.youtube.com/watch?v=8DTb-lseCdQ&t=118) | **cabeza ladeada, ojos húmedos, sonrisa** | ✅ clip | agradecer, despedir |
| P7, [spot «El elegido» 0:25](https://www.youtube.com/watch?v=IqlkIE5s1UA&t=25) | aparece **con los brazos abiertos** | ✅ clip | **animar** |
| P·18 | **chasquea los dedos, mano en alto** | ✅ hoja | **proclamar** |
| P·19 | **brazos en jarra**, pecho fuera | ✅ hoja | orgullo, «elfo libre» |
| P·21 (render PAS) | de cuerpo entero con el libro, recortable | ✅ hoja | recorte limpio |
| P2 02:25:12, [vídeo real 3:00](https://www.dailymotion.com/video/x3d4quh?start=180) (512 px) | **alarga un dedo larguísimo** hacia el calcetín que cuelga del diario, sonrisa pícara, ojos verdes muy abiertos | ✅ vídeo | **señalar**: «mira esto» |
| P2 02:25:41, [vídeo real 3:20](https://www.dailymotion.com/video/x3d4quh?start=200) | **de pie delante de Harry, pies separados, palmas abiertas hacia fuera**, en mitad del claustro | ✅ vídeo | proteger, **proclamar** |
| P2, [vídeo real 2:44](https://www.dailymotion.com/video/x3d4quh?start=164) | encogido, **sostiene el diario con las dos manos** contra la barriga, mira de reojo hacia arriba | ✅ vídeo | presentar un objeto con timidez |
| P2, [vídeo real 4:00](https://www.dailymotion.com/video/x3d4quh?start=240) | primer plano: **cabeza ladeada, ojos húmedos mirando arriba, sonrisa apretada** | ✅ vídeo | agradecer, despedir |
| P7 02:09:15, [clip de Movieclips 2:44-2:54](https://www.youtube.com/watch?v=R2zNRrOXbPY&t=164) | «Dobby no tiene amo…»: **de pie, erguido, brazos a los lados, la cara alzada** hacia Bellatrix; escena muy oscura | ✅ clip | proclamar (el gesto; la escena, no) |

### Dumbledore

| Dónde | Qué hace el cuerpo | Visto | Sirve para |
|---|---|---|---|
| P3, [clip del discurso 0:43-0:45](https://www.youtube.com/watch?v=dvFehFzph7I&t=43) | **abre los brazos en alto tras el atril del búho** | ✅ clip | **presentar**, dar la bienvenida |
| P3, [clip 0:47-0:55](https://www.youtube.com/watch?v=dvFehFzph7I&t=47) | baja del estrado hacia las mesas, de espaldas | ✅ clip | encuadre de sala |
| P3, [clip 1:03](https://www.youtube.com/watch?v=dvFehFzph7I&t=63) | **brazo extendido** hacia la mesa de profesores | ✅ clip | presentar a alguien |
| P3, [clip 1:31-1:39](https://www.youtube.com/watch?v=dvFehFzph7I&t=91) | tras las alas doradas, sereno, anuncia a Hagrid | ✅ clip | **anunciar** |
| P3, [clip 2:42-2:44](https://www.youtube.com/watch?v=dvFehFzph7I&t=162) | **los dos índices en alto** | ✅ clip | explicar, **animar** |
| P3, [clip 2:48-2:52](https://www.youtube.com/watch?v=dvFehFzph7I&t=168) | apaga una vela con los dedos | ✅ clip | el remate |
| F·1 (P1, Harris) | de pie en la mesa, entre velas, túnica burdeos | ✅ hoja | presentar (época P1) |
| P1, [tráiler de 2001, 1:15](https://archive.org/download/harry-potter-and-the-sorcerers-stone-2001-720p-trailer/Harry%20Potter%20and%20the%20Sorcerers%20Stone_2001_720p_trailer.mp4#t=75) (720p) | **erguido en el centro de la mesa, brazos caídos dentro de la túnica**, mirada al frente; copa dorada delante, velas en candelabros | ✅ vídeo | **anunciar** (época P1, sin atril) |
| P1, [*teaser*, 0:51](https://archive.org/download/HarryPotterTheSorcerersStoneTrailer1/HarryPotterTheSorcerersStoneTrailer1.mp4#t=51) | sentado en el sillón dorado, **bebe de una copa dorada** mirando por encima de las gafas | ✅ vídeo | el remate amable, brindar |
| P·26 (render PAS) | **mano abierta hacia arriba**, recortable | ✅ hoja | explicar |
| P·24 · P·25 | varita en alto · sentado, una mano con anillos en el brazo del sillón | ✅ hoja | presentar con énfasis · **pensar** |
| P4, [escena oficial de los campeones 1:33-1:42](https://www.youtube.com/watch?v=pLv1HXl_J10&t=93) | **brazos abiertos de par en par** ante el comedor y luego las palmas hacia arriba, junto al cáliz de fuego azul | ✅ clip | **anunciar**, presentar con énfasis |
| P4 00:35:21, [misma escena 3:55](https://www.youtube.com/watch?v=pLv1HXl_J10&t=235) | «¿Pusiste tu nombre en el cáliz?»: se le echa encima a Harry, cara a cara (miniatura cada 5 s: el agarrón en sí no lo veo) | ✅ clip | regañar (meme) |

### Harry

| Dónde | Qué hace el cuerpo | Visto | Sirve para |
|---|---|---|---|
| P2, [vociferador 1080p 0:44-0:48](https://www.youtube.com/watch?v=3KNNglv24a0&t=44) | junto a Ron, mira de lado, quieto | ✅ fotograma | acompañar |
| P6, tráiler final 1:27 | primer plano serio, ojos al frente | ✅ fotograma | pensar |
| P·30 (promo P2) | retrato de frente, uniforme completo | ✅ hoja | **presentar** |
| P·36 (render PAS) | con un libro, recortable | ✅ hoja | explicar |
| P·29 (promo P6) | perfil serio, luz lateral | ✅ hoja | pensar |
| P1 00:54:38 | pide el diario a Ron y lo lee en voz alta en el desayuno (wiki + guion transcrito, §3) | quién y qué ✅; el gesto no lo vi ⚠️ | explicar |
| P5, [clip oficial «Harry Trains Dumbledore's Army» 3:22-3:27 y 4:26](https://www.youtube.com/watch?v=SnmpiWHrRSA&t=202) | enseña al ED: **brazo extendido señalando** a un alumno, varita en la otra mano | ✅ clip | **explicar, animar** |

### Ron

| Dónde | Qué hace el cuerpo | Visto | Sirve para |
|---|---|---|---|
| P2, [vociferador 1080p 0:32](https://www.youtube.com/watch?v=3KNNglv24a0&t=32) | **ojos como platos, hombros encogidos** ante el sobre | ✅ fotograma | recibir el aviso |
| P2, [0:40](https://www.youtube.com/watch?v=3KNNglv24a0&t=40) | el grito le llega a la cara, se echa atrás | ✅ fotograma | cómico |
| P1, [clip Leviosa 0:00-0:02](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=0) | agita la varita como un látigo | ✅ clip | lo que NO se hace |
| P1, [clip 0:15-0:16](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=15) | mira de lado, enfurruñado | ✅ clip | fastidio |
| P·32 (render PAS) | varita y libro, recortable | ✅ hoja | explicar |
| P·7 (trío P1) | con el trío, escoba y libros | ✅ hoja | grupo |
| P8 00:33:45 | «Ay, diablos, ahí va» | frase ✅, gesto ⚠️ | resignarse |

**Las mejores para #anuncios**: presentar → Dumbledore con los brazos
abiertos tras el atril (clip P3 0:43) o con la mano abierta (P·26);
explicar → Hermione con la cabeza ladeada (clip 0:10) o con libros (P·2);
celebrar → Dobby erguido con el calcetín (clip 1:34) o chasqueando los dedos
(P·18); regañar → Hermione con el libro abrazado (tráiler P6 0:44); pensar →
Dumbledore sentado (P·25); animar → Luna asomando por encima de la revista
(clip 1:09) o **con la revista al revés** (vídeo 0:48). **Pedir la palabra**
→ Hermione con la mano arriba (captura de Pociones). **Anunciar en época
P1** → Harris de pie en la mesa (tráiler 1:15).

---

## 16 · Vestuario

> **Hex medidos con Pillow** (2.ª pasada): mediana de los píxeles de la
> prenda en la imagen original de la wiki (se dice cuál). Las fotos promo
> llevan su luz: el mismo uniforme sale más oscuro en una que en otra. Los
> de la 1.ª pasada, a ojo, quedan tachados. La paleta de Gryffindor que
> circula entre fans (`#740001` / `#AE0001` / `#D3A625` / `#EEBA30`) no es
> oficial: sólo contraste.

| Personaje | Lo icónico (visto en las hojas y clips) | Colores medidos |
|---|---|---|
| Harry | túnica negra, jersey gris de pico con ribete rojo y oro, corbata de rayas rojas y doradas, camisa blanca, **gafas redondas**, pelo negro revuelto (P·30, P·36) | túnica `#191B20`, jersey `#3F484A`, rojo de corbata `#61121B`, oro de corbata y ribete `#CC8E2A`, pelo `#2E1F17` (P·30). ~~`#1A1A1A` `#740001` `#D3A625`~~ |
| Hermione | uniforme de falda gris y jersey; **pelo castaño rizado y abundante**; en P3 ropa de calle oscura; vestido rosa de volantes sólo en el baile (P·5, clip del baile) | pelo `#835318` en sombra, `#BD924B` con luz (P·3); jersey `#2E211C`, falda `#251A17` (P·1). ~~`#6B4226` `#E8A0B4`~~ |
| Ron | pelo pelirrojo; uniforme con la corbata floja; forro de la túnica granate (P·31, P·7) | pelo `#8C4C1C` (P·7, P1) y `#A08058` (P·31, luz de estudio); forro `#472D29` (P·31). ~~`#B5472B` `#6E1F2A`~~ |
| Dumbledore (P1-P2, Harris) | túnica **burdeos con bordado dorado**, gorro a juego (en el *teaser*, **gorro de terciopelo con estrellitas doradas**), barba blanca muy larga, gafas ovaladas de alambre (P·27, F·1, *teaser* 0:51) | burdeos `#3E1613`, bordado `#DDB47F`, barba `#C1A696` (P·27, luz de velas); en el tráiler de 2001 (1:15, 720p): gorro `#652B31`, túnica en sombra `#291E25`, copa `#895F36` |
| Dumbledore (P3-P8, Gambon) | túnicas **gris pardo y lila apagado**, gorro de punto, gafas de media luna, barba más recogida (P·24, P·26, clip P3) | gris `#4D4A42`, barba `#A9937F` (P·24); lila `#585163`, gorro `#424244` (P·26, juego). ~~`#C9C9C9` `#4B2C4F`~~ |
| Luna | rubia muy clara, **gafas espectrales** rosa y azul, pendientes de rábano, abrigo de cuadros rosados; en el carruaje de P5, chaqueta ciruela, **collar de corchos** y **botas de agua rojas** (vídeo 0:44-1:06); en P6 chaqueta ciruela, falda oscura y **medias turquesa** (P·9, P·11, P·13) | pelo `#AE8F6B` (P·9, luz cálida); abrigo `#B37D71`, gafas `#F8C3F3` (P·11); chaqueta `#5F3D4D`, falda `#1F1A1F`, medias `#24576F` (figurín P·13). ~~`#E8DDB5` `#0E1A40`~~ |
| McGonagall | túnica y sombrero puntiagudo **verde oscuro** con brillo de tafetán; en el baile, sombrero negro de ala enorme (P·33, clip del baile) | verde `#1E4A23` (figurín P·33) |
| Dobby | **funda de almohada vieja** atada, piel rosada, orejas de murciélago rojizas por dentro, **ojos verdes enormes** (P·20) | funda `#998D64`, piel `#9B6B50`, dentro de la oreja `#67181F`, ojo `#7D9146` (P·20). ~~`#A39E86` `#6F8F3A`~~ |

**Lo que todos reconocen**: gafas y cicatriz de Harry, el pelo de
Hermione, el pelo Weasley, la barba de Dumbledore, las gafas espectrales
de Luna, el sombrero verde de McGonagall y la funda y el calcetín de Dobby.

**Por época**: en P1-P2 Dumbledore va de burdeos y oro (Harris); desde P3,
de gris y lila (Gambon). Para la época alegre de la lámina, **el burdeos
de P1** o el gris de P3 junto al atril (que sólo existe desde P3): no
mezclar a Harris con el atril.

---

## 17 · Paisajes y fondos de pantalla

- **Fotos libres del decorado**: sección 2.2. Gran Comedor, atril, sala común.
- **Maqueta de Hogwarts** del Studio Tour:
  [en Commons](https://commons.wikimedia.org/wiki/File:Studio_model_of_Hogwarts_at_Leavesden_Studios.jpg).
- **HDRI** para la luz: sección 5.
- **Vídeos 4K de salas comunes de Hogwarts Legacy** en Commons:
  [Hufflepuff](https://commons.wikimedia.org/wiki/File:Hogwarts_Legacy_-_Tour_the_Hufflepuff_Common_Room_(4K).webm),
  [Ravenclaw](https://commons.wikimedia.org/wiki/File:Hogwarts_Legacy_-_Tour_the_Ravenclaw_Common_Room_(4K).webm).
  Ravenclaw es la casa de Luna.

### Fondos de pantalla y arte ancho, en alta (2.ª pasada)

Tamaño medido con la API de la wiki; autor y origen, de la ficha de cada
archivo. Todo © de su dueño: **sólo referencia de luz y composición**.

| Qué es | Tamaño | Autor · origen | Para qué |
|---|---|---|---|
| [Fondo de pantalla oficial de Hogwarts Legacy](https://cdn-hogwartslegacy.warnerbrosgames.com/media/hogwarts-legacy-wallpaper.jpg) (bosque con criaturas, rayos de luz) | 11832×6264 (27 MB, la web oficial responde) | Avalanche Software / Warner Bros. Games ([ficha](https://harrypotter.fandom.com/wiki/File:Hogwarts-legacy-wallpaper.jpg)) | el más grande que hay; no es el Gran Comedor |
| [El Gran Comedor en Hogwarts Legacy](https://static.wikia.nocookie.net/harrypotter/images/3/3e/Hogwarts_Legacy_%28the_great_hall%29.png) | 2560×1362 | Avalanche Software (captura del juego) | **cientos de velas flotando, ventanal al fondo, mesas largas**: fondo de los conceptos A y B |
| [Alumnos en el Gran Comedor](https://static.wikia.nocookie.net/harrypotter/images/1/15/King-chen-greathall-final.jpg), arte conceptual | 1920×1034 | King Chen para Jam City (*Hogwarts Mystery*); original en [ArtStation](https://www.artstation.com/artwork/xVYYX) (da 403) | **todos mirando a quien habla al fondo**: la composición de un anuncio |
| [Galería del Gran Comedor](https://static.wikia.nocookie.net/harrypotter/images/7/70/Great_hall_gallery_HL.png) | 1919×1007 | Avalanche Software | galería de madera: sitio alternativo |
| [Arte clave de Magic Awakened](https://static.wikia.nocookie.net/harrypotter/images/1/15/Magic_Awakened_Key_Art.png) | 1900×1069 | NetEase / Portkey Games ([harrypotter.com](https://www.harrypotter.com/news/everything-you-need-to-know-about-harry-potter-magic-awakened)) | estilo libro ilustrado, compartimento del tren |
| [Póster de Hogwarts Legacy de Gus Morais](https://static.wikia.nocookie.net/harrypotter/images/0/08/Hogwarts_Legacy_artwork_by_Gus_Morais.jpg) | 7200×10800 | Gus Morais ([cuenta oficial del juego en X](https://twitter.com/HogwartsLegacy/status/1697678206701277663)) | lámina alta, llena de detalles |
| [Gran Comedor del Studio Tour](https://static.wikia.nocookie.net/harrypotter/images/4/4d/GreatHall.jpg) | 1500×1000 | Warner Bros. Studio Tour (la wiki avisa: luz eléctrica, fuera del mundo) | mesas con copas de peltre y platos |
| [Arte clave nocturno del castillo](https://static.wikia.nocookie.net/harrypotter/images/8/84/The-Nighttime-Lights-at-Hogwarts-Castle-key-art-WWoHP-at-USH.jpg) | 2400×3000 | Universal Studios Hollywood | castillo de noche con luces: qué NO (parque, no película) |
| [Fondo de Ravenclaw de Pottermore](https://static.wikia.nocookie.net/harrypotter/images/0/04/Pm-pride-Ravenclaw-Desktop-Wallpaper-1024-x-768-px.png) | 1024×768 | Pottermore | azul y bronce de la casa de Luna |
| Ilustraciones anchas de Pottermore (F·9, F·10, F·15, F·17, F·18) | 4120-5152 px de ancho | Pottermore (§2.0) | **las mejores para una lámina 1200×800**: ya son escenas |

**Fondos de fans en alta**: la wiki trae fondos viejos de fans de
800×600 a 1280×1024 (p. ej. [el de P4](https://static.wikia.nocookie.net/harrypotter/images/0/09/Harry-potter-and-the-goblet-of-fire-movie-wallpaper.jpg), 800×600): no sirven. En el
cierre busqué en **DeviantArt** por su RSS («hogwarts great hall
wallpaper», 60 resultados): casi todo son relatos de fans o imágenes de
700-1200 px, y alguna con pinta de IA. **No encontré fondos de fans en alta
que valgan**; ArtStation sigue dando 403. Para la lámina, mejor el arte
ancho de Pottermore (4000-5000 px) y las capturas del juego.

### Horas del día y luz (vistas)
- **Desayuno** (concepto A): mesas con cuencos de copos dorados, jarras
  de zumo de naranja, libros abiertos y una lechuza encima; luz cálida y
  gris, fondo en penumbra ([vociferador 1080p, 0:00-0:08](https://www.youtube.com/watch?v=3KNNglv24a0&t=0)).
  Luz blanca de día por los ventanales: F·13.
- **Banquete de noche** (concepto B): cientos de velas y ventanales azul
  frío ([clip P3, 0:13](https://www.youtube.com/watch?v=dvFehFzph7I&t=13)); F·11.
- **Sala común** (concepto C): fuego naranja de chimenea y tapices rojos
  (F·17, F·18, O·21).
- **Qué NO**: la luz verde azulada y el fuego de P6 (tráiler final, §12).

---

## 18 · Guía para generar con IA (Firefly, Canva)

> Sólo para bocetos de pose o de fondo. La lámina final va con fotogramas y
> recortes reales. Nunca inventar una cara: el fan la reconoce.

**Rasgos que nunca cambian**
- Harry: gafas redondas, cicatriz de rayo en la frente, pelo negro revuelto, ojos verdes.
- Hermione: pelo castaño muy rizado y abundante; uniforme de Gryffindor.
- Luna: pelo rubio muy claro, largo; mirada soñadora; gafas espectrales de colores.
- Dumbledore: barba plateada muy larga, gafas de media luna, túnica larga.
  Con Harris (P1-P2), burdeos y oro; con Gambon (P3-P8), gris y lila.
- Dobby: elfo pequeño, orejas enormes de murciélago, ojos verdes grandes,
  funda de almohada; **siempre habla de sí mismo en tercera persona**.

**Estilo de imagen (lo que se ve en los clips y fotogramas)**
- Es **cine de acción real**, no dibujo: piel real, tela real, grano de
  película. Nada de contorno negro ni sombreado plano.
- Luz **cálida y baja** (velas, antorchas, chimenea) contra un fondo frío
  o en penumbra; mucho contraluz en el pelo.
- Encuadres: plano medio a la altura de la mesa, con cabezas desenfocadas
  delante (clips del vociferador y del discurso); planos generales
  simétricos del Gran Comedor, con el pasillo central en el eje.
- Paleta medida (§5, §16): velas `#BFAE7C`, penumbra `#6D5730`, piedra
  `#3C382D`, ventanal frío `#989D92`, oro del atril `#B4956C`/`#664B2F`,
  fieltro del tablón `#51201D`, papel `#E8E0D4`, tinta `#030202`,
  vociferador `#5B2022`.

**Palabras que ayudan**: *Victorian gothic castle interior, candlelit great
hall, hundreds of floating candles, long wooden tables, pewter goblets,
warm amber light, cold blue gothic windows, parchment, aged newsprint,
sepia photograph, film still, 2000s fantasy film look, practical set,
35mm film grain, shallow depth of field, gilded owl lectern with spread
wings.*

**Palabras que lo estropean**: *anime, cartoon, chibi, neon, cyberpunk,
flat vector, clean sans serif, speech bubble, comic panel, glossy 3D
render, teal and orange, modern classroom, fluorescent light.*

**Referencias que hay que darle** (de las hojas y de `referencias.json`):
- **Estilo y luz**: el Gran Comedor de Hogwarts Legacy (2560×1362, §17),
  F·11 (noche con velas), F·13 (día).
- **Pose**: Dumbledore con la mano abierta (P·26, ya recortado); Hermione
  con libros (P·2); Dobby chasqueando los dedos (P·18); Luna con El
  Quisquilloso (P·11, P·12).
- **Objeto**: la portada de P1 (O·2), el atril (O·26, F·2), el tablón
  (O·21), el vociferador (O·17 y el fotograma 1080p de 0:16).
- **Composición de anuncio**: el arte de King Chen, todos mirando al que
  habla (§17), y el pasillo central del Gran Comedor con cientos de velas
  (tráiler de 2001, 0:36).
- **Luz de P1 en vídeo real**: el tráiler de 2001 (1:15, Dumbledore en la
  mesa) y el fragmento en 1080p de la sala común con el tablón (0:14).

**Lo que la IA suele estropear y hay que corregir a mano**: las letras del
periódico (salen garabatos: la portada se compone con las letras de §6),
las gafas de Dumbledore redondas en vez de media luna, y Dobby con ropa
(sólo lleva la funda).

### 18.1 · Para una IA de texto (diálogos en su voz)

> Añadido en el repaso corto (24-sep-2026) con las frases **ya oídas** de
> §10.3 y la forma de hablar de §8. Todas son del doblaje latino de cine.

**Reglas que la IA tiene que seguir**
- **Latino, no España**: «auto», «vociferador», «ustedes». Nunca «coche»,
  «Howler» ni «vosotros» (§10.3, la misma escena en los dos doblajes).
- **Signos dobles** ¡! y ¿?, con tildes. Sin «·», «—» ni paréntesis
  (regla 4 del dueño).
- **Dobby**: siempre **en tercera persona** y muy cortés («señor»).
  Exagera: «A Dobby lo amenazan cinco veces al día en casa».
- **Luna**: frases cortas y raras, dichas con calma. Criaturas que nadie
  ve (nargles; «torposoplos» ⚠️, sin oír del todo).
- **Dumbledore**: calma, humor seco, una frase para recordar. En un aviso,
  **nunca grita** (§14).
- **Hermione**: datos y correcciones. Su frase de marca: «Es Leviosa, no
  Leviosá».
- **Ron**: quejica y cómico. Su muletilla latina: «**Ay, diablos**».
- **Titulares de El Profeta**: cortos, casi sin verbo, como los que lee
  el narrador del doblaje: «Dumbledore y Potter reivindicados»,
  «Director de Hogwarts, restituido», «Harry Potter, el elegido».
- **Gritos**: exclamaciones seguidas, como el vociferador. Es cine: no hay
  onomatopeyas dibujadas. El vocabulario de expresiones del anime (gotas de
  sudor, fondos de emoción, *chibi*) **no aplica**.

**Frases reales, por emoción** (doblaje latino, §10.3)

| Emoción | Frase | Quién y dónde |
|---|---|---|
| Alegre | «¡Miren todos! La señorita Granger lo hizo. ¡Espléndido!» | Flitwick, P1 01:05:57 |
| Alegre | «Ginny, cariño, felicidades por entrar a Gryffindor. Estamos muy orgullosos.» | Molly en el vociferador, P2 00:34:28 |
| Enfadado | «¡Ronald Weasley! ¡Cómo osaste robar el auto! ¡Estoy verdaderamente enojada!» | Molly, P2 00:34:28 |
| Enfadado | «Nada. Repito. Nada. Justifica que un estudiante camine por la escuela en la noche.» | McGonagall, P1 |
| Explicando | «Nicolás Flamel es el único que ha podido crear la piedra filosofal.» | Hermione, P1 |
| Explicando | «Si te digo que te escondas, te escondes. Si te digo que corras, corres.» | Dumbledore, P6 |
| Anunciando | «La víspera de Navidad… nos reunimos en el gran salón para una noche de recatada frivolidad.» | McGonagall, P4 01:06:47 |
| Anunciando | «Silencio. TIMOS en progreso.» | narrador de los insertos, P5 ≈01:34:20 |
| Animando | «Ya saben a qué vinieron. Por un maestro, un maestro de verdad.» | Hermione, P5 00:54:01 |
| Animando | «Las palabras son, en mi no tan humilde opinión, nuestra fuente más inagotable de magia.» | Dumbledore, P8 01:34:46 |
| Triste | «Entiendo cómo te sientes, Harry. No, es mi culpa…» | Dumbledore, P5 02:04:35 |
| Triste | «Qué playa tan hermosa para estar con amigos.» | Dobby, P7 ≈02:10:48 (no usar en #anuncios) |
| Raro y tierno | «Hola, Harry. Interrumpí un pensamiento, ¿verdad? Vi que se hacía pequeño en tus ojos.» | Luna, P7 |

**Ejemplo para #anuncios** (inventado a partir de esas reglas, para
revisar): Dobby, en su notita del concepto C: «Dobby ha clavado el aviso,
señor. ¡Dobby está muy orgulloso!».

---

## Punto 18 · Estilo de imagen y técnica, y cómo replicarlo

> De `partes/texto.md` (repaso corto, 24-sep-2026). Harry Potter es **cine
> de acción real**: no hay línea de dibujo ni tramas. Hay 4 capas de estilo,
> cada una con su técnica documentada, y El Profeta de la lámina mezcla las 4.

### Cine (P1-P8): película, luz y color
- **Película de 35 mm de verdad**, no digital (Arricam, Arriflex 435;
  Kodak Vision2 500T y 200T) en P3 y P8. **Grano visible a propósito**: las
  sombras «tienen textura y densidad», no son negro digital ✅
  ([Color Culture P3](https://colorculture.org/harry-potter-and-the-prisoner-of-azkaban-cinematography-analysis/),
  [Color Culture P8](https://colorculture.org/deathly-hallows-part-2-cinematography-analysis/)).
- **Objetivos cálidos, revelado frío**: Cooke S4/i (P3) y Panavision (P8)
  dan piel cálida y redonda contra un color frío. **Michael Seresin** (P3)
  quería «más sombra y luz cruzada», tan dramática como se pudiera «sin
  llegar a parecer *Seven*» ✅ ([entrevista en The Leaky Cauldron](http://www.the-leaky-cauldron.org/2004/06/13/interview-with-poa-cinematographer-michael-seresin/),
  [resumen de *American Cinematographer*](https://cinema.wisc.edu/2017/02/17/untucked-world-harry-potter-and-prisoner-azkaban/)).
- **Luz con fuente visible**: en el tren de P3, el tungsteno cálido del
  vagón pasa a **cian frío y desaturado** cuando llegan los dementores. En
  P8 la luz sale de los hechizos y del fuego, con negros muy cerrados y el
  brillo de la magia **sin cortar** (*bloom* suave) ✅ (Color Culture P3 y P8).
- **Color**: colorista **Peter Doyle** en P3 y P8. P3 vira a azules y cian
  desaturados; P8, frío de base con el rojo y naranja de las explosiones
  como único acento; en los recuerdos de Snape sube el blanco para dar
  nostalgia ✅ (Color Culture). **Bruno Delbonnel** graduaba más frías,
  casi monocromas, las escenas tensas, y dejaba el cálido otoñal para las
  ligeras ([In Depth Cine](https://www.indepthcine.com/videos/bruno-delbonnel)).
- **Stuart Craig**, diseñador de producción de las 8: «sin luz no hay
  forma». Empieza cada decorado **dibujando una ventana**. En Hogwarts, casi
  todo en grises («grises verdosos, grises ocre») y **pan de latón de
  verdad**, no pintura dorada, porque el reflejo no se finge ✅
  ([IndieWire](https://www.indiewire.com/awards/industry/immersed-in-movies-production-designer-stuart-craig-talks-the-long-road-of-harry-potter-183079/),
  de pago, leído su resumen; [SGFA Journal](https://sgfajournal.wordpress.com/2011/07/27/drawn-to-cinema-award-winning-production-designer-stuart-craig/),
  misma cita de la ventana).
- **Filtros**: grano de película y *bloom* de la magia, confirmados. De
  **aberración cromática** u otros filtros ópticos no encontré ninguna
  entrevista ⚠️.
- **Serie de HBO** (sin estrenar): el director de fotografía **Adriano
  Goldman** separa el mundo muggle, frío y pálido, del Hogwarts cálido; la
  quiere «más vibrante» ⚠️ ([CBR](https://www.cbr.com/hbo-harry-potter-color-grading-criticism-cinematographer/), una fuente).

### Encuadres y composición según la emoción
- **Secretos**: personajes **enmarcados por ventanas o puertas**; barandillas
  o velas **entre ellos** marcan distancia, y desaparecen cuando se
  reconcilian (P3) ⚠️.
- **Escala y vulnerabilidad** (P8): planos generales con mucha profundidad
  de campo en la batalla; **foco corto** en los momentos frágiles.
- **Poder**: **ángulo bajo** para Voldemort; Harry, al principio, más
  pequeño en el cuadro ⚠️ (las dos cosas, de Color Culture; sin segunda
  fuente línea a línea).
- Lo visto en los clips (§18): plano medio a la altura de la mesa con
  cabezas desenfocadas delante; planos simétricos del Gran Comedor.

### Ilustración: Jim Kay y MinaLima
- **Jim Kay** (ediciones ilustradas, libros 1-4): línea a **lápiz 4B o más
  blando**; color con «cualquier pintura vieja»: acuarela buena, **botes de
  prueba de pintura de pared** y ceras, **en capas y lijando**. En el
  callejón Diagon coloreó en digital para no perder el lápiz. Los fantasmas
  los pinta **en negativo** y superpone capas. Tira el 85 % de lo que
  prueba ✅ ([MuggleNet](https://www.mugglenet.com/2015/10/the-great-big-harry-potter-fansite-interview-with-jim-kay/),
  [Lines and Colors](https://linesandcolors.com/2015/09/25/jim-kay/)).
- **MinaLima** (Miraphora Mina y Eduardo Lima, todo el papel de las
  películas): **escanean papel antiguo real**, no parten de vectores
  limpios; probaron «del *letterpress* victoriano al diseño moderno». Mina
  aprendió **Photoshop e Illustrator** a la fuerza para el primer encargo ✅
  ([Harry Potter Fan Zone](https://www.harrypotterfanzone.com/exclusive-meet-minalima-part-1/),
  [Wikipedia](https://en.wikipedia.org/wiki/MinaLima)).

### Videojuegos: dos técnicas opuestas
- **Hogwarts Legacy** (Avalanche, Unreal Engine): **realista**, luz
  dinámica y activos «a escala de cine». El director de arte **Jeff
  Bunker** releía los libros para cada función nueva. Hechizos, fuego y
  humo con **Niagara** (partículas de Unreal); el flujo típico usa
  Houdini, EmberGen y Substance Designer, y Maya y ZBrush para esculpir ✅
  ([80.lv](https://80.lv/articles/an-in-engine-look-at-hogwarts-legacy-s-environments),
  [VFX Apprentice](https://www.vfxapprentice.com/blog/magical-vfx-behind-hogwarts-legacy)).
- **Magic Awakened** (NetEase): **libro ilustrado pintado a mano**, con
  *shaders* de personaje y escena hechos a medida (charla de GDC de
  **Qingfeng Zeng**, artista líder; sólo leí el resumen, la charla es de
  pago ⚠️, [GDC Vault](https://gdcvault.com/play/1028748/Creating-the-Art-of-Harry)).
  Las cartas «respiran» con animación 2D por huesos (**Spine**) ✅
  ([GameRes](https://www.gameres.com/885575.html), [ZCOOL](https://www.zcool.com.cn/article/ZMTI5OTkwNA==.html)).

### Cómo replicarlo en Photoshop
- **Papel viejo** (portada, pergamino, avisos): textura de papel real en
  **Multiplicar**, manchas en **Trama de color** y una **Curva que suba el
  negro** (nunca negro puro: MinaLima usa papel escaneado). Papeles CC0 en
  §5 y en el punto 19.
- **Grano de película**: filtro **Grano** pequeño y suave, o un grano de
  35 mm en **Superponer**. **Viñeteado** leve. Temperatura a cian para
  tensión, a ámbar para confort, con la paleta medida: velas `#BFAE7C`,
  ventanal frío `#989D92` (§5, §16).
- **La foto que se mueve**: en las películas es **vídeo de fondo verde**
  compuesto en **After Effects** sobre el hueco del atrezo ✅
  ([PerfectCorp](https://www.perfectcorp.com/consumer/blog/video-editing/how-to-do-prophet-poster-video-effect),
  [Filmbro](https://www.filmbro.com/blogs/tutorials/newspaper-flythrough-in-after-effects-like-harry-potter)).
  En una lámina quieta: **2 o 3 fotogramas semitransparentes y un poco
  desplazados** (doble exposición), o una foto nítida con el borde
  corrido, como una estela.

### Cómo replicarlo en Blender
- **Contorno** (sólo si se quiere un acabado de ilustración; el cine no
  lleva): **Solidify invertido** (malla duplicada, normales al revés, grosor
  negativo, material negro), que va en Eevee y Cycles. Para línea fina y
  selectiva, **Line Art** con Grease Pencil o **Freestyle** ✅
  ([BlenderNation](https://www.blendernation.com/2020/02/06/how-to-make-a-toon-shader-with-dynamic-outlines/),
  [CGian](https://cgian.com/blender-line-art/)).
- **Modelos de base**: los de §4 (periódico doblado de abdillaamy, búho
  dorado para el atril, velas, pergamino, tablón). La portada hecha en
  Photoshop va encima como *Image Texture*.
- **Luz de vela**: varias luces de punto pequeñas con la fuerza animada con
  ruido, no una luz de área. Render en **Cycles**, para que el oro refleje
  como el latón de Craig y no quede un `#B4956C` plano.
- **Papel que «respira»**: una *Noise Texture* suave en el desplazamiento UV
  de la foto la hace temblar sin renderizar vídeo.
- **Modelos o *rigs* libres de los personajes**: no hacen falta (la lámina
  lleva fotogramas y recortes reales). Los que hay están en
  `partes/datos.json` (Sketchfab, CC BY): Hermione y Ron de zack_graham, y
  los de *La cámara secreta* para PS2 y GameCube de Chronis.

---

## Punto 19 · Texturas 2D (papel, patrones de ropa, emblemas y pinceles)

> De `partes/imagen.md`. No es manga: **no hay tramas** que buscar. Sí
> papel, patrones de tela, emblemas y pinceles de tinta. Las otras capas:
> 3D en §4, texturas reales de sitios en §5.

### Emblemas oficiales (para calcar la forma, nunca pegar)
Todos de un artículo oficial, [harrypotter.com, «The MACUSA seal and other
emblems»](https://www.harrypotter.com/features/the-macusa-seal-and-other-emblems-of-the-wizarding-world) ⚠️ (una fuente, pero oficial):
- **Escudo de Hogwarts**: 4 cuarteles, uno por casa, y un escudete con la
  «H» en el centro. Gryffindor, en el cuartel de más honor.
- **Ministerio de Magia**: «M» con serifas atravesada por una varita.
  Insignia oficial de MinaLima en el punto 25.
- **Wizengamot**: la «M» del Ministerio, una balanza y el lema latino
  «ignorantia juris neminem excusat».
- **Sortilegios Weasley**: simétrico, con una explosión en el centro.
- **Durmstrang**: águila de dos cabezas, latín y cirílico, cúpula de
  cebolla, cabeza de ciervo. **Beauxbatons**: dos varitas cruzadas y
  adorno rococó. **MACUSA**: fénix en un círculo de 48 estrellas.

### Emblemas con licencia libre
- **Reliquias de la Muerte**, PNG transparente de 600×600 (medido),
  [freesvg.org](https://freesvg.org/deathlyhallows), espejo de Openclipart,
  **CC0** ⚠️ (una ficha). Es el único emblema del fandom con licencia limpia.
- **León heráldico** para montar un escudo propio con los hex de §16:
  [Openclipart, león alado](https://openclipart.org/detail/313397/heraldic-winged-lion-silhouette)
  y [león de perfil](https://openclipart.org/detail/255195/lion-profile-silhouette),
  CC0 ⚠️. [heraldicart.org](https://heraldicart.org/lion/) no dice licencia.
  **Serpiente, águila y tejón sueltos: no los encontré** con licencia clara.
- Escudos de casa de [The Noun Project](https://thenounproject.com/icon/gryffindor-crest-1704953/):
  **no son libres** (cuenta Pro o 4,99 USD y atribución). Sólo para ver la
  composición: escudo, animal y yelmo.

### Patrones de ropa
- **Qué patrón va con cada casa, oficial**: la colaboración Vans × Harry
  Potter (7-jun-2019) puso **rayas rojas y doradas** a Gryffindor,
  **serpiente** a Slytherin y **tablero de ajedrez** a Ravenclaw ✅
  ([harrypotter.com](https://www.harrypotter.com/news/first-look-at-hogwarts-house-themed-vans-x-harry-potter-collection),
  [CNN](https://www.cnn.com/style/article/vans-harry-potter-shoes-intl-scli)).
- **25 tartanes** tileables de Luke.RUSTLTD,
  [OpenGameArt](https://opengameart.org/content/25-tartan-patterns), **CC0** ✅.
  Son al azar: base para pintar encima la bufanda de una casa, no un tartán
  oficial.
- **Rayas y tramas SVG** para la corbata: [Hero Patterns](https://heropatterns.com/),
  CC BY 4.0 ⚠️ (la propia web).
- **Túnica**: «Poly Wool Herringbone», **8216×8387**, [Poly Haven](https://polyhaven.com/a/poly_wool_herringbone), CC0 ✅.
- **Jersey Weasley**: «Knitted Fleece», **8103×8226**, [Poly Haven](https://polyhaven.com/a/knitted_fleece), CC0 ✅.
  El patrón de punto real, en Ravelry ([Alison Hansel](https://www.ravelry.com/patterns/library/the-weasley-sweater),
  [RitaKhor](https://www.ravelry.com/patterns/library/weasley-sweater-6)):
  raglán con la inicial; no comprobé si es gratis ⚠️.

### Papel, grano y pinceles
- **Papel extra** (por si Texturelabs sigue cerrado):
  [Paper](https://opengameart.org/content/paper),
  [Old paper texture](https://opengameart.org/content/old-paper-texture) y
  [Old-squared paper](https://opengameart.org/content/old-squared-paper),
  OpenGameArt, **CC0** ✅.
- **Pinceles de tinta y pluma** (cartas, Mapa del Merodeador):
  [Brusheezy, «Vintage Ink Pen Brushes»](https://www.brusheezy.com/brushes/47193-vintage-ink-pen-brushes-and-splatter-brush-pack)
  ⚠️ (licencia según quién lo sube; no la comprobé).
- **Trama de puntos de imprenta** para las fotos de El Profeta: **no la
  encontré con licencia clara** (Unblast, Spoongraphics y Texturelabs
  bloquearon dos veces) ⚠️. Mientras, el papel viejo CC0 de arriba, que
  no trae el punto de imprenta.

---

## Punto 20 · Gustos y detalles de cada personaje

> De `partes/voz.md`: fichas de la [Harry Potter Wiki](https://harrypotter.fandom.com/wiki/Harry_Potter)
> leídas por su API, que citan los libros, Pottermore y a J. K. Rowling.
> Las alturas salen del [HP Lexicon](http://www.hp-lexicon.org) vía la wiki.

| | Harry | Hermione | Ron |
|---|---|---|---|
| **Cumpleaños** | 31-jul-1980, Valle de Godric ✅ | 19-sep-1979 ✅ | 1-mar-1980, Ottery St Catchpole ✅ |
| **Altura** | menos de 1,75 m (deducido: Ron es más alto) ⚠️ | 1,65 m ⚠️ | 1,75 m, 69 kg ⚠️ |
| **Le encanta** | la tarta de melaza | Aritmancia («¡Es mi materia favorita!»); *Historia de Hogwarts* | el sándwich de tocino; el ajedrez mágico; los **Chudley Cannons**, el peor equipo, con pósters en su cuarto |
| **Odia** | — | que la llamen «sangre sucia»; la injusticia con los elfos (§8) | el sándwich de carne en conserva; el **granate** de su jersey de Navidad |
| **Siempre lleva** | la capa invisible y el Mapa del Merodeador; varita de acebo y pluma de fénix | en la guerra, el **bolsito de cuentas** con encantamiento de extensión (libros, ropa, una tienda) | el **Desiluminador** de Dumbledore |
| **Amortentia** (lo que huele) | tarta de melaza, mango de escoba y algo floral: el pelo de Ginny ✅ | césped recién cortado, pergamino nuevo y el pelo de Ron (en la película, pasta de dientes de menta) ✅ | — |
| **Cómo se ve** | en el Espejo de Oesed, **sus padres vivos a su lado**: quiere familia, no fama ✅ | su boggart: McGonagall diciéndole que **lo ha suspendido todo** ✅ | en el Espejo, **capitán de quidditch y Premio Anual** con la copa: quiere que lo noten ✅ |
| **Miedo (boggart)** | un dementor ✅ | suspender ✅ | Aragog, las arañas ✅ |

| | Dumbledore | Luna | Dobby |
|---|---|---|---|
| **Cumpleaños** | entre el 16 y el 31 de agosto de 1881 ⚠️ (sólo el rango) | 13-feb-1981, lo dijo [Rowling en X](https://x.com/jk_rowling/status/622008983000363008) ✅ | 28 de junio, año sin confirmar ✅ |
| **Altura** | 1,80 m ⚠️ | no consta en la wiki | 91 cm; ojos verdes «como pelotas de tenis» ✅ |
| **Le encanta** | los dulces raros (sus contraseñas: grageas ácidas, racimos de escarabajos), la música de cámara, los bolos ✅ | las criaturas de *El Quisquilloso* (snorkacks, nargles); collar de chapas de cerveza de mantequilla, pendientes de rábano ✅ | Harry, la libertad y **los calcetines**: los colecciona y lleva varios sin pareja ✅ |
| **Manías** | gafas de media luna | la varita **detrás de la oreja izquierda**, las revistas **al revés**, descalza porque le escondían los zapatos ✅ | se castiga: «¡Dobby es malo!» |
| **Siempre lleva** | la Varita de Saúco ✅ | el collar «contra los nargles» y las gafas espectrales ✅ | la funda de almohada, y el calcetín que lo liberó (P2 02:25:12) ✅ |
| **Cómo se ve** | en el Espejo dice ver **calcetines de lana** («uno nunca tiene suficientes»): esquiva la pregunta ✅ | no le importa que la llamen «Lunática» | en **tercera persona**, hasta que se sabe «un elfo libre» ✅ |
| **Miedo (boggart)** | el cadáver de su hermana **Ariana**, su culpa ✅ | campo vacío en la wiki: **no lo encontré** | Voldemort, sólo en *LEGO Harry Potter Years 1-4* ⚠️ |

Fuentes de las filas: fichas de [Hermione](https://harrypotter.fandom.com/wiki/Hermione_Granger),
[Ron](https://harrypotter.fandom.com/wiki/Ronald_Weasley),
[Dumbledore](https://harrypotter.fandom.com/wiki/Albus_Dumbledore),
[Luna](https://harrypotter.fandom.com/wiki/Luna_Lovegood),
[Dobby](https://harrypotter.fandom.com/wiki/Dobby),
[Amortentia](https://harrypotter.fandom.com/wiki/Amortentia) (cita el
[chat de Rowling con Bloomsbury, 2007](https://www.the-leaky-cauldron.org/2007/07/30/bloomsbury-chat.html))
y [Espejo de Oesed](https://harrypotter.fandom.com/wiki/Mirror_of_Erised).

**Para la lámina**: los **calcetines sin pareja de Dobby** son su objeto,
su gag y su libertad a la vez. Encajan en el concepto C (colgados del
tablón) y en una lámina 2.

---

## Punto 21 · Por qué la gente la ama (y las escenas que hacen llorar)

> De `partes/voz.md`, más títulos de Reddit de `partes/datos-voz.md`.

### Datos duros
- **Más de 600 millones de libros** en más de 80 idiomas (cifra de 2023;
  en 2019 la web oficial [decía 500 millones](https://www.harrypotter.com/news/500-million-harry-potter-books-have-now-been-sold-worldwide))
  ✅. Los más vendidos de la historia fuera de textos religiosos y políticos.
- **Récord Guinness**: la saga de cine con **más BAFTA infantiles**
  ([Guinness](https://www.guinnessworldrecords.com/world-records/452669-most-childrens-bafta-awards-won-by-a-movie-series)) ✅.
  Mejor película infantil con P3 (2004) y P8 (2011); voto del público con
  P2 (2003) y P4 (2006); premio a la «contribución destacada al cine
  británico» en 2011 ([BAFTA](https://www.bafta.org/media-centre/press-releases/harry-potter-films-awarded-bafta/)) ✅.

### Por qué la aman
- **Familia elegida**: Harry no tiene padres y la encuentra en los
  Weasley, en Ron y Hermione. La familia es lealtad, no sólo sangre ✅
  ([Medium](https://medium.com/@aylinkanber/why-do-we-love-harry-potter-c28fdf51800b),
  [APU](https://www.apu.edu/articles/family-matters-in-the-harry-potter-novels/)).
- **Escapismo que refleja el mundo real**: lealtad, amor y estar juntos,
  lo que el lector querría fuera del libro ✅ (mismas dos fuentes).
- En Reddit (títulos de hilos): «Why I love Ron and Harry's interaction
  after the destruction of the locket» (84 votos), «Why I love Book Snape»,
  y quien acaba la saga: «I understand why people love this series»
  ([r/harrypotter](https://www.reddit.com/r/harrypotter/comments/1mldsrl/just_finished_the_entire_series_i_understand_why/)) ⚠️ (sólo títulos).

### Con quién se identifica el público
- **Neville**: tímido y torpe, florece tarde. Lo quieren **por** sus
  torpezas ✅ ([CBR](https://www.cbr.com/harry-potter-most-understandable-characters/),
  [ScreenRant](https://screenrant.com/harry-potter-best-most-relatable-characters/)).
- **Luna**: la de quien se sintió raro; nunca finge ser otra ✅ (CBR,
  ScreenRant, y el hilo de 6 555 votos de §14).
- **Ron**: el «normal» entre dos genios, el menos especial de su familia
  (su Espejo de Oesed, punto 20) ✅.
- En [Goodreads](https://www.goodreads.com/topic/show/597754-which-character-from-any-of-the-harry-potter-books-do-you-most-identify),
  las respuestas se reparten entre Luna, Ron, Ginny y Hermione ⚠️ (un hilo).

### Las escenas que hacen llorar, reír o gritar

**1. La muerte de Dobby** (la que más se cita como «la que más duele»)
- **Dónde**: P7, **02:10:48**, en la playa de la Cabaña Concha (§8) ✅.
- **Qué pasa**: rescata a Harry y a sus amigos de la mansión Malfoy y le
  alcanza el cuchillo que Bellatrix lanza. Harry **lo entierra a mano, sin
  magia**. Su última frase latina: «Qué playa tan hermosa para estar con
  amigos» (§10.3).
- **Por qué duele**: fiel desde P2, muere rescatando, y tiene **funeral en
  pantalla** ✅ ([Collider](https://collider.com/harry-potter-dobby-death/),
  [CBR](https://www.cbr.com/saddest-harry-potter-scenes/),
  [Syfy](https://www.syfy.com/syfy-wire/harry-potter-movies-saddest-moments-hedwig-dobby-deaths)).
- **Música**: *Farewell to Dobby*, de Alexandre Desplat, pista 25 de la
  banda sonora de P7, **3:44** ✅ ([Spotify](https://open.spotify.com/track/6TnfdR9iEcLnWdw1AIJeWZ)).
- **Reacción**: miles de vídeos en TikTok («Dobby Dies Scene»). En Reddit,
  un hilo de escenas que hacen llorar **deja fuera las muertes** porque ya
  se dan por hechas ([r/harrypotter](https://www.reddit.com/r/harrypotter/comments/1wcgx8j/what_scenes_from_harry_potter_made_you_cry_your/), 34 votos) ✅.
- **Cómo está dibujada**: no lo miré en vídeo ⚠️. Hay fotograma oficial del
  funeral en `partes/datos.json` («Dobby's funeral», 3834×1500).

**2. Snape: «Always»**
- **Dónde**: P8, **01:22:37** (§14) ✅.
- **Qué pasa**: en el Pensadero, Harry ve que Snape amó a Lily toda la
  vida. Dumbledore le pregunta si aún la ama; él conjura su Patronus
  plateado, igual al de Lily, y dice «Always».
- **Por qué duele**: da la vuelta a siete libros. No era crueldad: era dolor.
- **Música**: *Snape's Demise* trae el tema de Hedwig en celesta; el
  recuerdo usa *Severus and Lily*, que retoma «Dumbledore's Farewell» de
  Nicholas Hooper (P6) ✅ ([MovieMusicUK](https://moviemusicuk.us/2011/08/15/harry-potter-and-the-deathly-hallows-part-ii-alexandre-desplat/)).
- **Cómo está filmada**: Snape en **silueta contra un cielo gris** tras una
  ventana, en uno de los silencios de la batalla ⚠️
  ([ensayo en Medium](https://alpenglowmemory.medium.com/harry-potter-and-the-deathly-hallows-part-2-spectacle-and-silence-24d4a32efcb2), una fuente).
- **En latino**: cómo se dice «Always» en el doblaje **no lo comprobé** ⚠️.

**3. Molly contra Bellatrix** (la que hace gritar de emoción)
- **Dónde**: P8, Batalla de Hogwarts. **El minuto no lo encontré** ⚠️.
- **Qué pasa**: Bellatrix va a matar a Ginny. Molly se interpone: «Not my
  daughter, you bitch!» y la derriba.
- **Reacción**: el público **gritó y aplaudió en los estrenos de 2011** ⚠️
  ([BuzzFeed](https://www.buzzfeed.com/kaileyhansen/people-are-sharing-movies-that-got-applause),
  testimonios de lectores). Julie Walters habla del rodaje en
  [este vídeo](https://www.youtube.com/watch?v=T-mM69B08ko), sin mirar
  (YouTube pide iniciar sesión).

**Para #anuncios**: ninguna de estas escenas va en la lámina (§14: no usar
la muerte de Dobby para algo alegre). Sirven para láminas 2, eventos o el
canal de doblaje.

---

## Punto 22 · Fan dubs y comunidad hispana

_(pendiente)_

---

## Punto 23 · Colaboraciones, figuras y cosplay

_(pendiente)_

---

## Punto 24 · Obras parecidas y láminas vecinas

_(pendiente)_

---

## Punto 25 · El mundo, la historia por arcos y sus símbolos

_(pendiente)_

---

## 19 · Tres conceptos para la lámina de #anuncios

### Concepto A — «El correo de la mañana» (el que pedía el plan, mejorado)

- **Objeto y sitio**: **El Profeta doblado sobre la mesa de Gryffindor, en
  el Gran Comedor, a la hora del desayuno.** Es la escena real de P1
  00:53:45 a 00:54:57: llegan las lechuzas y el diario se lee en voz alta
  («Somebody broke into Gringotts. Listen.»; lo lee Harry, según la wiki
  de la película, §3).
  Arte oficial de la misma idea: F·7 (P3, Gryffindor lee El Profeta en el
  comedor) y F·8 (Pottermore, lechuzas sobre la mesa).
  En Blender: plano con simulación de tela, doblado en tres, con una esquina
  levantada. Papel de [ambientCG](https://ambientcg.com/view?id=Paper001) y
  capa de [periódico viejo](https://texturelabs.org/textures/paper_290/).
  Mesa de [Poly Haven](https://polyhaven.com/a/wood_table_worn).
- **Personaje**: **Hermione**, sentada al otro lado de la mesa. Sostiene un
  borde del diario y señala el titular con el dedo, como quien explica.
  Pose de referencia **vista**: la cabeza ladeada y las cejas altas del
  [clip de Leviosa, 0:10](https://www.youtube.com/watch?v=Qgr4dcsY-60&t=10);
  el cuerpo, del render recortable P·2 (libros abrazados).
- **La foto que se mueve**: dentro del diario, un fotograma de **Dumbledore
  de pie entre velas** (F·1, P1: época de la cabecera gótica; en P1 aún no
  hay atril), en sepia, con trama de puntos. El hueco de la foto, como en
  O·9 (P3).
  Dos copias superpuestas y desplazadas, con poca opacidad, sugieren el
  movimiento. Si el formato lo permite, una versión animada de 2 o 3 segundos.
- **Cómo habla**: la portada es el cuadro de diálogo. Estilo de la primera
  época: **nada de cabecera de propaganda**. Los titulares, cortos y en
  presente, como los que **lee en voz alta el narrador del doblaje
  latino** («Dumbledore y Potter reivindicados», §10.3). Y un titular
  pequeño de broma interna, como hacía Eduardo Lima con Caxambu (§7.1).
- **El guiño**: al fondo, desenfocada, **Luna leyendo El Quisquilloso al
  revés** (vídeo de P5, 0:48): la «otra prensa» frente a la oficial.
- **Dónde va cada texto**:
  - Cabecera, en **UnifrakturMaguntia**: «**Anuncios**».
  - Bajo la cabecera, línea de fecha en IM Fell English SC: «Las novedades oficiales del servidor».
  - Titular grande, en IM Fell English: «**Solo el staff publica aquí**».
  - Recuadro de columna, tipo «cartas al director»: «¿Quieres comentar? Abre un hilo en el anuncio».
- **Profundidad**: una lechuza ([modelo CC BY](https://sketchfab.com/3d-models/owl-d177e1fbcce940cba32e434cc5a62f1a))
  entra batiendo las alas en primer plano, desenfocada. Un cuenco de copos
  dorados y una jarra de zumo de naranja tapan una esquina del diario (así
  es la mesa del desayuno en el [fotograma 1080p, 0:00-0:08](https://www.youtube.com/watch?v=3KNNglv24a0&t=0)). Velas flotando desenfocadas
  detrás. Luz de mañana desde los ventanales, fría, contra la cálida de
  las velas.

### Concepto B — «Avisos de inicio de curso» (Dumbledore en el atril)

- **Objeto y sitio**: **el atril del búho dorado**, en el Gran Comedor, de
  noche. Sobre el atril, **un pergamino desenrollado** con los avisos.
  Modelar el atril en Blender con las [fotos del Studio Tour](https://commons.wikimedia.org/wiki/File:Professor_Dumbledore_and_The_Owl_Podium_(7119146507).jpg):
  alas abiertas, pan de oro y **gotas de cera** reales. Pergamino
  ([CC BY](https://sketchfab.com/3d-models/parchment-paper-10e53ca757a2482d8fe1bc94e9043826)).
- **Personaje**: **Dumbledore (Gambon)**, de pie detrás del atril, **los
  brazos abiertos en alto**, como en el [clip oficial de P3, 0:43](https://www.youtube.com/watch?v=dvFehFzph7I&t=43),
  o la mano abierta hacia arriba del render recortable P·26. El atril sólo
  existe desde P3: **no usar a Harris (P1-P2) aquí**. Es su gesto de anunciar:
  en ese mismo discurso dice «I'm delighted to announce…» y presenta a
  Hagrid (P3 00:24:29). Encaja con «solo staff».
  **Versión época P1**, si se quiere a Harris: sin atril, **de pie en el
  centro de la mesa de profesores**, brazos caídos, copa dorada delante y
  velas en candelabros (tráiler de 2001, 1:15, visto en 720p); el
  pergamino, entonces, sobre la mesa.
- **Cómo habla**: no hay globo. Sus palabras **son el pergamino**, con letra
  de pluma. Una firma suya al pie en Pinyon Script.
- **Dónde va cada texto**:
  - En el frontal del atril, grabado en el oro como una placa: «**Anuncios**».
  - Primera línea del pergamino: «Las novedades oficiales del servidor».
  - Segunda: «Solo el staff publica aquí».
  - Al pie, casi fuera del pergamino, como posdata: «¿Quieres comentar? Abre un hilo en el anuncio».
- **Profundidad**: velas flotando **delante** de Dumbledore, desenfocadas.
  Las cabezas de alumnos de espaldas en primer plano, en sombra, como en el
  arte de King Chen (§17) y en el clip de P3 (0:13-0:39). Detrás,
  el techo encantado de noche y la mesa de profesores. Luz de vela desde
  abajo en el oro del atril.

### Concepto C — «El tablón de Gryffindor» (con Dobby)

- **Objeto y sitio**: **el tablón de anuncios de la sala común de
  Gryffindor**, junto a la chimenea. **Cambiado en el cierre: ahora se
  copia el de la película 1**, que vi en 1080p (P1 ≈01:28:25,
  [fragmento, 0:14](https://archive.org/download/670343/colombus_harry_potter_philosophers_stone_extrait.HD.mp4#t=14)): **fieltro rojo dividido en cuadros
  por cintas finas oscuras y con borde de cordón trenzado rojo y oro**, al
  lado del tapiz del unicornio. El de Pottermore (O·21: **fieltro rojo
  oscuro `#51201D` con marco de madera tallada casi negra**; no es corcho)
  sirve para el marco. Entre tapices de flores, lleno de avisos pequeños de los libros: libros de segunda mano,
  normas de Filch, entrenamientos de quidditch, anuncios de los gemelos
  Weasley. **Encima de todo, un aviso oficial enorme** con lacre de
  Hogwarts, como el cartel de Aparición del libro 6. Fácil en Blender:
  base de [este tablón](https://sketchfab.com/3d-models/cork-board-9534ee2ad4344ea6b02b95b61bd4a913)
  (CC BY) y marco del [tablón medieval](https://sketchfab.com/3d-models/566a4332b57d4045a1cc4ffec77b4b8f)
  (CC BY), con el corcho teñido a fieltro `#51201D`, las cintas en cuadrícula
  y el cordón rojo y oro como una curva con material de cuerda.
- **Personaje**: **Dobby**, subido a un taburete, clava el aviso. Lleva
  encima la torre de gorros de lana: en el libro 5 Hermione teje gorros para
  liberar elfos y **Dobby se los lleva al limpiar la sala común y se los
  apila en la cabeza** ([Harry Potter Wiki, «Elf hat»](https://harrypotter.fandom.com/wiki/Elf_hat),
  que cita el libro, y [HP Lexicon](https://www.hp-lexicon.org/character/dobby/):
  «a tower of knitted hats», de 60 a 90 cm de alto, libro 5, cap. 18) ✅. Pose **vista**: la mano en alto
  chasqueando los dedos (P·18) o los brazos en jarra (P·19); la cara, P·20.
  Es el guiño al fan: el elfo libre que eligió ayudar. (La lista de
  apariciones de la wiki pone a Dobby en el libro 5 y no en la película 5:
  es un guiño de libro, y el fan lo sabe.)
- **Cómo habla**: el aviso oficial es su «cuadro». Una notita escrita a mano
  por Dobby, en tercera persona, torcida, en Mrs Saint Delafield: «Dobby
  ha clavado el aviso, señor».
- **Dónde va cada texto**:
  - Aviso grande con lacre, en Cinzel Decorative: «**Anuncios**».
  - Debajo, en IM Fell English: «Las novedades oficiales del servidor».
  - Sello o franja al pie del aviso: «Solo el staff publica aquí».
  - **El juego de palabras**: de un gorro de Dobby cuelga **un hilo de lana**
    que llega a una tarjetita clavada: «¿Quieres comentar? Abre un hilo en el anuncio».
- **Profundidad**: el respaldo de una butaca roja en primer plano,
  desenfocado. Luz naranja de la chimenea desde un lado (F·18); sombras
  largas de las chinchetas en el fieltro. Una lechuza dormida en la ventana del fondo.
  A un lado, el borde del tapiz del unicornio con collar de lunas (como en
  el fotograma de P1): el fan lo reconoce.

### ¿Cuál primero?
**A**, porque es el objeto del plan con escena real y la lectura de «noticia»
es inmediata. **B** es la más solemne y la más «staff». **C** es la más
querida por el fan y la más fácil en Blender.

---

## 20 · Lo que no pude verificar

**Resuelto en la 2.ª pasada** (antes estaba aquí): hojas de contacto e
imágenes (§2.0), licencias de Sketchfab y Commons (§2.2, §4), hex medidos
(§5, §16), frases del doblaje latino (§10.3), poses vistas (§15), música
de P7-P8, Reddit (§14), portadas y Jim Kay (§2.5), fondos de pantalla (§17).

**Resuelto en el cierre (tercer ayudante)**: quién lee El Profeta en P1
(Harry, guion transcrito), Hermione con la mano arriba (captura + guion),
Luna repartiendo El Quisquilloso (guion), el tablón en la película (visto),
Caxambu (O Tempo), la encuesta de MTV (IBTimes, IMDb), la coreana
(Dispatch), el logo de Hogwarts Legacy (Pentagram), las capturas de
*Hogwarts Mystery*, el vídeo de Bilibili y el TikTok (datos), los fondos de
fans (buscados: no hay en alta), el redoblaje argentino (DubDB), y seis
voces del doblaje (créditos de cine, DubDB, Wikipedia).

**Sigue dudoso, y por qué** (cada uno lleva su marca de duda en su sitio):
- **Vídeo de YouTube a tamaño real**: YouTube no dejó bajar ni un clip
  (bloqueo por IP compartida; sólo *storyboards*). Lo visto en vídeo real
  sale del Internet Archive y de Dailymotion (§12.1).
- **Gestos sin ver**: Harry leyendo El Profeta (P1) y Ron en P8. Tienen
  minuto y frase comprobados; el gesto, no.
- **Doblaje con una sola web** (Doblaje Wiki): estudio y dirección de P4,
  P6 y P8; la dirección de P5 (Wikipedia dice otra cosa); Snape en P7;
  parte del reparto de Hogwarts Legacy; los datos de interés de §10.1.
- **«Torposoplos»** en el audio de Luna: Whisper *medium* oye «torpo
  solos» dos veces y *large-v3* «por posolos»; la palabra de los libros sí
  existe en la wiki en español. Hace falta oírlo una persona.
- **«Eres un mago, Harry»** en el audio latino: no hay muestra ni clip.
- **Una sola fuente**: El Profeta y El Quisquilloso clavados cada día en el
  tablón (la wiki no lo cita), la herramienta de MinaLima para cortar los bordes (Steps to Magic), la
  encuesta de muertes de Fanpop, que «LEGACY» vaya en Tautz (FontBolt).
- **Letras sin comprobar**: la de El Profeta que señalan los fans (P22
  Operina, dos webs de fans). La de los menús de Hogwarts Legacy no aparece
  en ninguna fuente.
- **Licencia de Texturelabs**: la página de condiciones devuelve un reto
  antibots y la copia de Wayback no baja.

---

## Cumplimiento del encargo

| Punto de `ENCARGO.md` | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | 601 imágenes de la wiki miradas; 100 elegidas en 3 hojas (§2.0): promos, renders del juego, figurines, Pottermore, props de papel, láminas de MinaLima (§2.1), Jim Kay y portadas de Salamandra (§2.5) |
| 2 · Fotogramas con capítulo y minuto | ✅ | minutos de los subtítulos ingleses (§3); fotogramas 1080p del vociferador y de la sala común de P1 (el tablón), 720p del tráiler de P1; fotogramas de wiki a 1920×800. Los clips de YouTube, sólo a 160-320 px |
| 3 · Fan art y 3D con licencia | ✅ | 17 modelos de Sketchfab con licencia por la API (§4); fan art de ArtStation y DeviantArt, sólo enlazado |
| 4 · Fondos, luz, paleta, texturas | ✅ | hex medidos en clips y arte (§5); texturas CC0 de Poly Haven y ambientCG. Texturelabs, licencia sin leer |
| 5 · Tipografía con tildes | ✅ | 12 letras libres y 6 de fans abiertas con fontTools (§6) |
| 6 · Cómo hablan en pantalla | ✅ | 9 «cuadros» del mundo (§7.1), juegos (§7.2) y qué NO (§7.3) |
| 7 · Personajes y popularidad | ✅ | 5 encuestas, fuentes en inglés, japonés y coreano (§9): gana Snape; Hermione siempre arriba |
| 8 · Doblaje latino con dos fuentes | ⚠️ | reparto principal ✅ con dos fuentes; P1 y P2 con sus **créditos de cine**, P3 y P5 (estudio) con Wikipedia y DubDB; 6 voces más pasan a ✅. Siguen con una sola web: estudio y dirección de P4, P6 y P8, la dirección de P5, Snape en P7 (§10) |
| 8b · Frases latinas textuales | ✅ | unas 30 frases (§10.3): muestras de Doblaje Wiki, el vociferador con minuto exacto en vídeo y **la voz de los insertos** (titulares de El Profeta y carteles leídos en voz alta). No hay clips oficiales doblados que se puedan bajar |
| 9 · Música | ✅ | compositores con fuente; el coro de ranas visto en el clip de P3 (§11) |
| 10 · Vídeos con minuto | ✅ | 33 vídeos, casi todos con enlace al segundo (§12); **7 mirados con `fotogramas.py` en vídeo real**: tráiler y *teaser* de P1, tráiler de P6 (tema principal y tráileres), vociferador, sala común de P1, Dobby libre y Luna (escenas); el resto por *storyboard*. De TikTok, sólo los datos |
| 11 · Videojuegos: interfaz y diálogo | ✅ | 6 juegos (§13, §7.2); la caja de diálogo de *Hogwarts Mystery* vista y medida |
| 12 · Lo que ama el fandom y qué NO | ✅ | Reddit por Arctic Shift con votos (§14); 12 «qué NO» |
| 13 · Descripción profunda y forma de hablar | ✅ | 6 personajes + Snape y McGonagall (§8), con cuerpo visto y voz latina transcrita |
| 14 · Poses con minuto | ✅ | 6 tablas, 7-15 poses cada una (§15); casi todas vistas en vídeo, clip u hoja; 2 gestos sin ver (Harry P1, Ron P8) |
| 15 · Vestuario con hex | ✅ | hex medidos en figurines y promos (§16) |
| 16 · Ciudades y fondos de pantalla | ✅ | 10 fondos con tamaño y autor (§17); fondos de fans en alta: buscados en DeviantArt, no hay que valgan |
| 17 · Guía para IA | ✅ | rasgos, estilo, paleta medida, palabras sí y no, referencias numeradas (§18) |
| 3 conceptos de lámina | ✅ | A, B y C distintos, con pose vista y número de hoja (§19); el C copia ahora el tablón de la película 1 |
| 40 fuentes distintas | ✅ | unas 80 webs distintas enlazadas (el cierre añadió Pentagram, DubDB, Moviepedia, Wikipedia en español, O Tempo, IBTimes, IMDb News, ANMTV, Looper, TECHNÈS y Dailymotion) |
| Oficiales | ✅ | harrypotter.com, MinaLima, Warner Bros. Games, Pentagram (estudio del logo de Hogwarts Legacy), canales oficiales de YouTube, tráileres oficiales en el Internet Archive, créditos de cine del doblaje, soporte de Portkey |
| Entrevistas al staff | ✅ | MinaLima, Magic Awakened, Hogwarts Legacy, Javier Rivero (su blog), Cuarón (prensa) |
| Otros idiomas | ✅ | japonés, coreano, chino (§9, §7.2, §12.2) y portugués (O Tempo, sobre Eduardo Lima) |
| Wikis, TV Tropes, TCRF, Wayback | ⚠️ | Fandom (inglés, español, doblaje), Wikipedia en español, DubDB, Moviepedia (guiones), HP Lexicon, TCRF ✅; TV Tropes sigue en 403 (Cloudflare); Wayback: la API de disponibilidad responde, las páginas guardadas no bajan |
| Foros y comunidades | ✅ | Reddit por Arctic Shift, foro de dafont |
| Arte | ✅ | ArtStation, DeviantArt (ArtStation da 403 a la API) |
| Vídeo | ✅ | YouTube (oficial y análisis, por *storyboard*), Internet Archive y Dailymotion (vídeo real), Bilibili y TikTok (datos) |
| Código y recursos | ✅ | GitHub (subtítulos, letras), Sketchfab, Poly Haven, ambientCG |
| Doblaje latino | ✅ | Doblaje Wiki (API y audios), prensa mexicana, entrevistas en YouTube |
| Hojas (`hojas/`) | ✅ | 3 JPEG de menos de 1 MB, numeradas y descritas (§2.0) |
| `referencias.json` | ✅ | 40 entradas: la imagen misma (o el vídeo con su segundo), con ancho y alto medidos, uso y licencia; 3 cambiadas en el cierre (tablón de P1, tráiler de P1, logo latino de P4) |

---

## 21 · Bitácora de búsqueda

### Segunda pasada (24-sep-2026, red abierta)

La hicieron tres ayudantes seguidos. Del primero quedó el texto (§2-§14
corregidos y ampliados) pero se perdió su carpeta de trabajo y **no quedó
registro de sus búsquedas web**; lo que usó se lee en cada sección y se
resume aquí.

**Primer ayudante (hecho por la red directa)**
- Fandom `harrypotter`: `investigar_serie.py` dos veces (20 páginas, 601
  imágenes grandes) y búsquedas en el espacio de archivos.
- Doblaje Wiki por la API: 8 películas, 9 fichas, 65 muestras de audio
  pasadas por Whisper.
- YouTube con yt-dlp: 13 vídeos, sólo datos y *storyboards*.
- APIs de Sketchfab, Poly Haven, ambientCG y Wikimedia Commons (licencias y
  tamaños); láminas de MinaLima bajadas y medidas; Reddit por Arctic Shift;
  fontTools sobre Parry Hotter y Lumos.

**Segundo ayudante (este cierre)**
- **YouTube**: `fotogramas.py` con 6 clientes de yt-dlp (`mweb`,
  `tv_simply`, `android_vr`, `web_embedded`, `ios`, `tv`) y 3 reintentos
  espaciados: «Sign in to confirm you're not a bot» o «This video is not
  available». Con `web_embedded` salen los datos y los *storyboards*; con
  un script de Pillow monté las miniaturas de 10 vídeos en hojas (P3 discurso, Leviosa,
  Luna, Dobby P2, Baile de Navidad, campeones P4, ED en Cabeza de Puerco,
  Harry enseña al ED, Malfoy Manor, clase de Pociones).
- **Búsquedas en YouTube** (yt-dlp `ytsearch`, no cuentan en el cupo):
  «Harry Potter escena doblaje latino oficial Warner», «Harry Potter HBO Max
  Latinoamérica escena», «Harry Potter doblado Warner Bros Pictures
  Latinoamerica», «harrypottermexico tv spot», «Harry Potter Wizarding World
  en español latino clip», «Harry Potter Warner Bros Mexico trailer
  doblado», y 6 más en inglés para las poses (Dobby en Malfoy Manor, «Did
  you put your name», el desayuno de P1, Cabeza de Puerco, el ED, Pociones).
  **El desayuno de P1 no tiene clip oficial.**
- **Internet Archive** (búsqueda avanzada y metadatos): «harry potter
  trailer», «harry potter latino/doblaje/español», «harry potter clip
  scene…», «different languages». Encontrado: el vociferador en 23 idiomas
  (1080p) y la colección de tráileres oficiales de P6. Bajados y mirados
  con `fotogramas.py`; `video.mp4`/`.webm` borrados al terminar. Los
  espejos `youtube-<id>` de los 10 clips oficiales: no existen.
- **Whisper** (`faster-whisper`, modelo *medium*, instalado en un entorno virtual
  dentro de mi carpeta de trabajo): el tramo latino y el de España del vociferador, y 5
  muestras de Doblaje Wiki (Molly P2, Hagrid, Dumbledore, Harry y Ron de P1).
- **APIs de Fandom**: tamaños de las 100 imágenes de las hojas (todos
  coinciden con las tablas); búsquedas de texto («broke into Gringotts»,
  «Dobby hats», «notice board Daily Prophet Quibbler», «Luna Quibbler
  train»); wikitext de *Elf hat*, *Gryffindor Notice Board*, *Dobby*, la
  película 6 y la 1, *Alexandre Desplat*; espacio de archivos «wallpaper»,
  «Hogwarts Legacy key art», «Great Hall wallpaper». Wiki en español:
  «Torposoplo» (existe), «Audiomaster», «Javier Rivero» (sin resultados).
  Doblaje Latino Wiki: sólo tiene fichas de actores.
- **Subtítulos ingleses** de GitHub (P1, P3, P4, P6) para los minutos
  de «Tell them to wait», «Quibbler», el anuncio de Hagrid y El Profeta.
- **Buscador web** (4 búsquedas, en español): «Harry Potter doblaje latino
  DAT Herman López Orden del Fénix director de doblaje», «"José Luis García
  Agraz" doblaje "Prisionero de Azkaban" director», «Javier Rivero director
  doblaje "Harry Potter y la piedra filosofal" Audiomaster entrevista»,
  «Roberto Molina director doblaje Harry Potter "Reliquias de la Muerte"
  DAT entrevista». Sirvieron La Prensa de Panamá (2001), el blog de Javier
  Rivero (2007) y El Siglo de Durango (2004).
- **Comprobados con curl**: el fondo oficial de Hogwarts Legacy (27 MB,
  responde), SoundCloud, Bilibili y harrypotter.com (200).
- **Fallan**: Wikipedia y Commons (429), TV Tropes (403, reto de
  Cloudflare), ArtStation (403), Texturelabs (reto antibots en sus
  condiciones), `web.archive.org` (el túnel se corta; la API de
  disponibilidad sí confirma que el artículo de Blog Hogwarts está guardado).

**Tercer ayudante (cierre, tarde del 24-sep-2026)**
- Encontré la biblia más avanzada de lo que decía `ESTADO.md` (1882
  líneas y 38 marcas de duda, no 1725 y 45): seguí desde ahí.
- **YouTube**: `fotogramas.py` otra vez («This video is not available») y
  yt-dlp con `web_safari`, `mweb` y `tv_embedded`: sólo *storyboards* o
  «Sign in». No insistí más.
- **Internet Archive** (búsqueda avanzada): «harry potter clip / scene /
  extrait», «opening / intro / hedwig», «trailer stone / sorcerer»,
  «trailer azkaban / goblet / phoenix», «latino / doblaje», «dumbledore»,
  «dobby», «luna lovegood». Sirvieron el tráiler oficial de P1 en 720p, el
  *teaser* y el fragmento de TECHNÈS (1920×796). Pasados por
  `fotogramas.py`, fotogramas grandes mirados, colores medidos con Pillow.
- **Dailymotion** (API de búsqueda: «harry potter leviosa / dumbledore
  speech / luna lovegood / dobby / escena latino»): sólo copias de fan;
  bajan a 512 px como mucho. Usé dos (Dobby libre y Luna).
- **Doblaje Wiki**: lista de sus 637 audios «HP…» por la API; bajé 23 y
  los pasé por Whisper *medium* (insertos de P1, P3-P6 y P8; Dumbledore de
  P1, P3, P5 y P6; Flitwick, Filch, Neville, McGonagall, Hagrid, Luna).
  Búsqueda en su espacio de archivos: «Créditos Harry Potter», «Harry
  Potter Logo Español» → **créditos de cine de P1 y P2** y logos latinos de
  P1, P2, P3 y P4, mirados.
- **Wikipedia en español por su API** (con el título bien codificado ya
  responde; a ratos 429): P1-P8 y el anexo de reparto. Doblaje Latino Wiki:
  casi vacía. **DubDB** (dubdb.fandom.com): fichas de P1, P2 y P3.
- **Harry Potter Wiki**: búsquedas de texto («Quibbler upside down»,
  «notice board Daily Prophet Quibbler», «raised her hand», «Dobby hats»),
  archivos de *Hogwarts Mystery* y «Hermione with her Hand Up».
  **Moviepedia**: guiones transcritos de P1 y P6.
- **Subtítulos ingleses** (raw de GitHub; la API de GitHub no está
  habilitada en esta sesión): P1-P8, para los minutos nuevos.
- **Buscador web** (8 búsquedas): «MTV "Harry Potter World Cup" Snape wins
  2011» (inglés); «Harry Potter redoblaje argentino 2019 Caja de Ruidos
  Alejandro Bono» (español); «"Caxambu" "Daily Prophet" MinaLima weather»
  (inglés); «Eduardo Lima Caxambu Profeta Diário Harry Potter cidade»
  (portugués); «Hogwarts Legacy doblaje latino voces Jaime Vega…»
  (español); «Hogwarts Legacy logo font Tongari Tautz» (inglés);
  «"Somebody broke into Gringotts. Listen" Harry transcript» (inglés);
  «Fanpop poll saddest Harry Potter death Fred Weasley percent» (inglés).
- **Leído con curl**: Pentagram, ANMTV, O Tempo, Rede NoticiaZ, IBTimes,
  Dispatch, Looper, HP Lexicon, Bilibili (datos con yt-dlp), TikTok
  (*oEmbed*), DeviantArt (RSS). **fontTools** sobre Cinzel.
- **Fallan**: Fanpop y TV Tropes (403, Cloudflare), Texturelabs (202),
  `web.archive.org` (el túnel se corta), WebFetch (bloqueado; usé curl).

**Lo que sigue sin encontrarse (2.ª pasada)**
- Un clip oficial doblado al latino con subtítulos o audio que se pueda
  bajar.
- Segunda fuente para el estudio y la dirección de P4, P6 y P8, y para la
  dirección de P5 (créditos de cine sólo encontré de P1 y P2).
- La letra de los menús de Hogwarts Legacy y un modelo 3D libre de El
  Profeta o del atril.
- Una encuesta de popularidad hecha en Latinoamérica.
- El clip oficial del desayuno de P1 (quién lee El Profeta ya está
  confirmado por el guion; el gesto, sin ver).

**Marcas de duda** (contadas con `grep -o` sobre el símbolo en
`biblia.md`; el número incluye la leyenda): **55 antes de la segunda pasada → 57 cuando se
cortó el primer ayudante → 38 al cerrar el segundo → 22 al cerrar el
tercero**.

### Primera pasada (24-sep-2026, red cerrada)

### Comprobación de red (24-sep-2026)
- `community.fandom.com` → 000/403. También 403: Doblaje Wiki, Wikipedia,
  Wikimedia, YouTube, TV Tropes, Sketchfab, Poly Haven, ambientCG, dafont,
  Google Fonts, Flickr, harrypotter.com, MinaLima, Arctic Shift, archive.org,
  Kaggle, Hugging Face.
- Responden: `api.github.com`, `raw.githubusercontent.com`,
  `media.githubusercontent.com`, pypi y npm.

### Búsquedas web (64 hechas, 4 rechazadas por cuota)

**Español (20)**
1. Harry Potter doblaje latino reparto Eleazar Gómez Harry Leyla Rangel Hermione Ron voz
2. Harry Potter y la piedra filosofal doblaje (en doblaje.fandom.com)
3. Harry Potter doblaje latino Harry James Potter voz Eleazar Gómez Víctor Ugarte (en doblaje.fandom.com)
4. Hermione Granger doblaje latino voz Leyla Rangel primera película actriz
5. Ron Weasley voz latino Enzo Fortuny Luis Daniel Ramírez
6. Dumbledore voz doblaje latino Blas García Humberto Solórzano
7. voces de Harry Potter español latino Claudio Velázquez
8. Luna Lovegood doblaje latino voz actriz
9. Dobby doblaje latino voz actor cámara secreta
10. César Arias voz de Dumbledore muere 2020
11. Arturo Castañeda voz Harry Potter piedra filosofal
12. Ismael Castro Dobby voz latino
13. Víctor Ugarte voz de Harry Potter entrevista
14. Lupita Leal Luna Lovegood entrevista
15. Harry Potter doblaje latino estudio director Javier Rivero Roberto Molina
16. «Las Reliquias de la Muerte» doblaje latino Blog Hogwarts
17. Hagrid «Eres un mago, Harry» doblaje latino Blas García
18. frases doblaje latino «Dobby es un elfo libre»
19. personaje favorito de Harry Potter encuesta Latinoamérica
20. (rechazada) portadas Salamandra y sus ilustradores

**Inglés (41)**
21. Harry Potter characters popularity poll YouGov
22. MinaLima Daily Prophet design typography moving photographs
23. poll favourite Harry Potter character results
24. most beloved character poll Dobby death saddest
25. Marie Claire voted best Harry Potter character
26. Bloomsbury poll favourite character Snape
27. Daily Prophet prop moving pictures green screen
28. MinaLima Daily Prophet hidden jokes Easter eggs
29. Daily Prophet font masthead
30. Gryffindor common room notice board announcements book
31. Harry P font dafont license (en dafont.com)
32. logo font Parry Hotter Lumos license
33. Hogwarts Legacy UI font menus subtitles
34. Marauder's Map font MinaLima handwriting
35. Hogwarts Legacy Game UI Database dialogue HUD
36. Harry Potter unused content (en tcrf.net)
37. Hogwarts Mystery dialogue box UI
38. Chamber of Secrets Game Boy Color dialogue box
39. Magic Awakened art style storybook interview
40. Hogwarts Legacy art director interview Victorian
41. Daily Prophet newspaper 3D model (en sketchfab.com)
42. wand owl Hogwarts letter 3D model Creative Commons (en sketchfab.com)
43. cork notice board 3D model CC0
44. wooden table old wood texture CC0 (en polyhaven.com)
45. owl free download CC Attribution rigged (en sketchfab.com)
46. quill inkwell parchment CC Attribution (en sketchfab.com)
47. Howler red envelope model (en sketchfab.com)
48. Great Hall Hogwarts candles model license (en sketchfab.com)
49. paper newspaper cardboard cork CC0 (en ambientcg.com)
50. cork board texture, stone wall castle (en polyhaven.com)
51. HDRI candlelit interior castle hall (en polyhaven.com)
52. old newspaper paper texture public domain
53. Dumbledore owl lectern Great Hall Studio Tour
54. Gryffindor notice board film prop Studio Tour
55. Educational Decree Umbridge MinaLima
56. The Quibbler Luna Spectrespecs
57. Daily Prophet prop Studio Tour (en commons.wikimedia.org)
58. Great Hall studio tour Leavesden (en commons.wikimedia.org)
59. «Professor Dumbledore and The Owl Podium» Flickr
60. Gryffindor common room set (en commons.wikimedia.org)
61. (rechazada) licencia de la foto del atril en Flickr
62. (rechazada) key art de Hogwarts Legacy en 4K
63. (rechazada) Jim Kay: Luna y Dobby ilustrados

**Japonés (2)**
64. ハリー・ポッター 人気キャラクター ランキング 投票 結果
65. シネマトゥデイ ハリー・ポッター 好きなキャラ トップ10

**Coreano (1)**
66. 해리포터 인기 캐릭터 순위 설문 결과

**Chino (2)**
67. 哈利波特 魔法觉醒 UI 设计 卡牌 界面 美术 网易 访谈
68. 《哈利波特：魔法觉醒》 魔法世界的UI魔法 羊皮纸 对话框 字体 设计

### GitHub (código y recursos)
- Búsqueda de código: `"Leviosa" extension:srt`, `"Dobby is free" extension:srt`,
  `"Leviosa, no" extension:srt`, `"Dobby es un elfo libre"`,
  `"Dobby es libre" extension:srt` (sin resultados), `filename:HARRYP__.TTF`,
  `"Daily Prophet" font extension:css`.
- Repositorios: «potter db», «daily prophet moving newspaper»,
  «marauders map», «hogwarts legacy».
- Bajado y usado:
  - Subtítulos en inglés de las 8 películas, de
    [sydney-machine-learning/sentimentanalysis-Hollywood](https://github.com/sydney-machine-learning/sentimentanalysis-Hollywood).
  - 12 letras de [google/fonts](https://github.com/google/fonts), revisadas con fontTools.
  - Letras de fans del proyecto [gstrenge/dailyprophet](https://github.com/gstrenge/dailyprophet):
    MuggleNews, BlackCastleMF y Headline Two.
  - «Harry P» del repositorio [Kruhlmann/wow_conf](https://github.com/Kruhlmann/wow_conf) (vía Git LFS).
- Mirado y descartado: [icochi/The-Marauders-Map](https://github.com/icochi/The-Marauders-Map)
  (sólo usa Apple Chancery). No abrí repositorios de «Hogwarts Legacy» que
  parecían descargas piratas.

### Fuentes consultadas por tipo
- **Oficiales**: harrypotter.com (Wizarding World), MinaLima, soporte de
  Portkey Games, Warner Bros. Studio Tour.
- **Entrevistas al staff**: MinaLima en HP Fan Zone, Cool Hunting e It's
  Nice That; Justin Webb y Daniel Zeng (Magic Awakened); Jeff Bunker
  (Hogwarts Legacy).
- **Otros idiomas**: Cinema Today, Nlab, Mynavi, PressWalker (japonés);
  Newsis, Dispatch (coreano); GameRes, UISDC, ZCOOL, Zhihu, Bilibili,
  GAMEUI (chino).
- **Wikis**: Harry Potter Wiki (Fandom), HP Lexicon, Doblaje Wiki, Wikia
  Fandub, Doblaje Latino Wiki, EcuRed, Wikipedia.
- **Videojuegos**: The Cutting Room Floor, Spriters Resource, StrategyWiki,
  Interface In Game, Deltia's Gaming.
- **Foros**: foro de dafont, debates de Fandom y Goodreads, LiveJournal.
- **Arte**: ArtStation, DeviantArt, Behance.
- **Vídeo**: YouTube, TikTok, SoundCloud, Bilibili.
- **3D y texturas**: Sketchfab, Poly Haven, ambientCG, Texturelabs,
  Wikimedia Commons.
- **Doblaje latino**: Doblaje Wiki, Infobae, El Universal, Vía País, Otaku
  Press, Noroeste, Blog Hogwarts, TikTok de las actrices.

### Lo que NO encontré (1.ª pasada; lo resuelto después, en §20)
- Un modelo 3D de El Profeta con licencia libre.
- La letra de los menús de Hogwarts Legacy.
- Una encuesta de popularidad hecha en Latinoamérica.
- Frases latinas confirmadas aparte de «Es Leviosa, no Leviosá».
- Nada en Reddit, TV Tropes, Pixiv ni Wayback Machine: bloqueados o sin
  cuota.
