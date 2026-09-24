---
tags: [biblia, serie, laminas]
serie: "Doraemon"
canal: "#recursos"
fecha: 2026-09-24
---

# Biblia · Doraemon — para #recursos

> [!important] Cómo se hizo, y sus límites
> - **Primera pasada (24-sep-2026, red cerrada).** Fandom, Doblaje Wiki,
>   ANMTV y casi todas las webs daban bloqueo. Se trabajó con el buscador
>   web, con subtítulos japoneses de GitHub
>   ([Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror):
>   *Stand by Me Doraemon* 2014, la película del museo 2013 y 66 episodios
>   de la serie de 2005) y con letras de [google/fonts](https://github.com/google/fonts)
>   comprobadas con fontTools. Los minutos de esos subtítulos van como
>   `00:06:14`: es el minuto de ese archivo, puede moverse uno o dos minutos.
> - **Segunda pasada (24-sep-2026, red abierta, equipo de 4 investigadores
>   y redactor).** Ya se pudo usar: la API de Doblaje Wiki (4 páginas
>   completas), la API de Fandom y `investigar_serie.py` (hojas de contacto
>   miradas), Dailymotion e Internet Archive para **mirar vídeo de verdad**
>   con `fotogramas.py` (YouTube pedía iniciar sesión), `voz.py` (Whisper)
>   sobre un episodio con **doblaje latino real**, `estilo.py` y Pillow para
>   **medir los hex**, la API de Sketchfab para licencias, Arctic Shift para
>   Reddit, `yt-dlp` para buscar *fandubs* sin sesión y entrevistas japonesas
>   del estudio (CGWorld, ITmedia). Lo nuevo está en «Segunda pasada · qué
>   cambió», justo debajo, y en las secciones «Punto 18» a «Punto 25».
> - Lo que sigue sin poder usarse: YouTube en vídeo (pide sesión),
>   AnimeThemes (error 522 todo el día), TV Tropes y The Cutting Room Floor
>   (403), TikTok (sin buscador sin sesión).
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto, o
>   lo vimos en el fotograma. ⚠️ **dudoso**: una sola fuente, o de memoria.
>   Lo de memoria siempre va marcado.

## Segunda pasada · qué cambió

**Corregido (antes → ahora):**
- **Hojas de contacto**: «no hay» → **3 hojas miradas** en `hojas/`, con
  tabla de números (§3.0).
- **Ropa de Shizuka**: «falda rosa, blusa clara» → **top rosa `#F29FC2` y
  falda granate `#B71840`**, medido en su retrato oficial (§16).
- **Hex de la ropa**, «míos, a ojo» → **medidos** con Pillow: azul de
  Doraemon `#18A2E7` → `#1D99C8`, rojo `#E61737` → `#E02333`, amarillo
  `#FED037` → `#FCDC2A`, Nobita `#F5D23A` → `#FDD23C`, Gigante `#F08A24` →
  `#F08E39`, Suneo `#3FA38C` → `#27B585` (§16).
- **Paleta de sitios**, «de fans y de memoria» → **medida** en 5 fondos
  oficiales y 9 fotogramas; tatami `#B9B77A` → `#A7A741`/`#658D36` (serie
  clásica) y `#C1DBAA` (fondo oficial) (§5.2).
- **Traductora de Netflix**: «Jennifer Mendel» → **Jennifer Medel**
  (wikitext de Doblaje Wiki) (§10.1).
- **Nobita niño en el doblaje clásico**: «Laura Torres, luego Rommy Mendoza
  ⚠️» → **Laura Torres → Ariadna Rivas → Rommy Mendoza** ✅ (§10.2).
- **Doblaje de los 80**: «una fuente» → Doblaje Wiki + Lost Media ✅; y
  **Carlos Carrillo dobló a Doraemon y a Gigante** (§10.1).
- **Voz latina de Dorami**: «no la encontré» → **María Fernanda Morales**
  (1999-2011) y **Lupita Leal** (2014-2015) ✅ (§8, §10).
- **Frases del doblaje latino**: «ninguna» → **3 frases textuales con
  minuto**, oídas con Whisper en un episodio doblado (§10.6).
- **Fondos oficiales**: «tamaño: no lo sé» → **1280×894 a 1280×929**,
  bajados (§3.1, §17).
- **Fondo del momento del invento**: «no lo vi» → **visto** en las
  cartelas: rayos de color con destellos y letra con borde (§7.1).
- **Licencias de Sketchfab**: «comprobar ⚠️» → **CC BY por la API** (§4.1).
- A ✅: cumpleaños de Gigante (manga, 1980), boniatos de Shizuka (AniList),
  Nobita adulto Miguel Ángel Ruiz, el apodo «Cósmico», la acuarela de *Story
  of Seasons*, el pelo de Suneo, el bolsillo de media luna.
- **Errores de las partes que corrige el redactor** (mirando las hojas y
  bajando dos fondos): la hoja n.º 17 es Gigante con **guitarra**, no con
  micrófono; el bolsillo 4D es el **n.º 58**, no el 64; los enlaces de
  Dropbox de los fondos estaban **cruzados** (el 01 es el túnel, el 04 el
  cuarto).
- **Nuevo choque** ⚠️: el sonido del invento en la serie de 2005, «pua-pua…
  ¡te-tte-rē!» o «¡bikān!» (§7.1).

**Añadido:**
- Escenas **miradas** en vídeo con minuto (§2.4), poses vistas (§15.0) y de
  las hojas (§15.1), caras por emoción (§8).
- Arte oficial nuevo: retratos 2005, cel de producción, artbook, hoja de
  modelo, 83 portadas (§3.5); fan art con origen y etiquetas de Danbooru
  (§4.3); fondos de pantalla de fans con tamaño y autor (§17).
- Doblaje: repartos completos por temporada y película, el **doblaje
  cubano de 1985**, **Irwin Daayán de Suneo a Doraemon**, por qué se fue
  Laura Torres, nombres de inventos (§10).
- El opening latino antiguo **oído** y por qué hay dos letras (§11).
- Una letra por cada uso (§6.3); Dora-e-moji avisada (§6.1).
- Guía de IA con paleta medida, etiquetas y **guía para IA de texto** con
  frases reales por emoción (§18).
- Secciones nuevas **Punto 18 a Punto 25**: técnica de Shin-Ei y Shirogumi
  (CGWorld) y cómo replicarla en Photoshop y Blender; texturas 2D; gustos;
  por qué la aman (88,4 % lloró); *fandubs* con vistas; colaboraciones
  (UNIQLO × Louvre, Converse en México, *Granblue*); obras parecidas y
  láminas vecinas; el mundo y sus símbolos.
- Tabla «Cumplimiento del encargo» y bitácora de la segunda pasada.
- `referencias.json`: de **35** entradas sin tamaño a **243**, **150 con
  ancho y alto medidos**; primero el bolsillo, los fondos oficiales, los
  retratos, las cartelas y los fotogramas vistos.

**Conceptos de lámina**: la idea de los tres no cambia. **A** gana el fondo
oficial exacto, el fondo de rayos visto (n.º 58) y el guiño del caramelo
«Voice Thickener» (n.º 85). **C** pasa a la **noche con focos de recital**,
con la pose de Gigante **vista** (0:20) o con su guitarra (n.º 17).

**Los ⚠️**: había **73**. Unos **25** de los antiguos se resolvieron (los de
arriba). El total sube a **153** porque la biblia casi dobla su tamaño
(de 1233 a unas 2400 líneas) y cada dato nuevo con una sola fuente lleva su
⚠️. Los que quedan y por qué, en §20.

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección EL ESTUDIO):

> **ıı・🧰・recursos** (foro) · 3 hilos · etiquetas: Verificado, Programa,
> Plantilla, Pista sin voz, Efectos de sonido, Musica libre, Tutorial,
> Guion, Banco de voces, Gratis, De pago, Windows, Mac, Movil, Online —
> _Lo que le sirve a los demas: programas, plantillas, pistas sin voz,
> efectos, tutoriales. Un hilo por recurso. NADA pirata: ni cracks ni prog_

Hilos que ya existen:
- 📌 **Cómo colgar algo aquí (léeme)**
- **Audacity**
- **Cómo se pide una pista sin voz**

> [!warning] La descripción está cortada en el inventario
> Termina en «ni cracks ni prog». No invento el final. Lo más probable es
> «ni programas crackeados» o «ni programas pirata», pero **el dueño tiene
> que confirmarlo** antes de rotular. En la lámina basta con «Nada pirata.
> Ni cracks.»

### Las 15 etiquetas, ordenadas en 4 grupos

Las 15 no caben con aire en una sola lámina. Se agrupan así (el orden es mío;
las palabras son las del inventario, sin cambiar ni una):

| Grupo | Etiquetas | Cuántas |
|---|---|---|
| **Qué es** | Programa · Plantilla · Pista sin voz · Efectos de sonido · Musica libre · Tutorial · Guion · Banco de voces | 8 |
| **Cuánto cuesta** | Gratis · De pago | 2 |
| **Dónde funciona** | Windows · Mac · Movil · Online | 4 |
| **Sello** | Verificado | 1 |

> Ojo con las tildes: en el inventario van **sin tilde** «Musica libre» y
> «Movil». En la lámina se escriben **como en Discord** para que la gente
> las reconozca; si el dueño las corrige en Discord, se corrigen aquí.

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Recursos** | nombre del canal |
| 2 | **Lo que le sirve a los demás** | para qué es |
| 3 | **Programas, plantillas, pistas sin voz, efectos y tutoriales** | qué se cuelga |
| 4 | **Un hilo por recurso** | regla 1 |
| 5 | **Nada pirata. Ni cracks.** | regla 2 |
| 6 | **Lee el hilo fijado antes de colgar** | a dónde ir |
| 7 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Los textos de la lámina 2 (las 15 etiquetas)

**Propongo lámina 2**, porque 15 etiquetas con su explicación no caben en la
1 sin saturarla (regla 5 del dueño). Cada etiqueta es **un artilugio con su
placa**, como en el museo de la película de 2013 (ver §2.2). Texto corto por
etiqueta:

| Etiqueta | Texto de su placa (propuesta) |
|---|---|
| Programa | Para grabar, editar o mezclar |
| Plantilla | Un proyecto listo para rellenar |
| Pista sin voz | La música sin la voz, para cantar o doblar encima |
| Efectos de sonido | Golpes, pasos, puertas, ambientes |
| Musica libre | Música que puedes usar sin pedir permiso |
| Tutorial | Te enseña paso a paso |
| Guion | Textos para practicar doblaje o locución |
| Banco de voces | Voces o muestras para usar |
| Gratis | No cuesta nada |
| De pago | Cuesta, y dilo en el hilo |
| Windows / Mac / Movil / Online | Dónde funciona |
| Verificado | Alguien del equipo lo probó |

> ⚠️ Las explicaciones de cada etiqueta son **mías**. El inventario sólo
> da los nombres. «Verificado» sobre todo: no sé quién lo pone ni cómo. El
> dueño tiene que decir qué significa antes de rotularlo.

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué Doraemon encaja | Doraemon **es** un canal de recursos con patas: saca de su **bolsillo mágico** la herramienta justa para cada problema. En la película de 2014 lo dice él: «pasé todo lo del cajón a este bolsillo de cuatro dimensiones; **aquí cabe de todo**» (*Stand by Me Doraemon*, 00:06:14) ✅. Y en el opening latino se canta «Doraemon, **con su bolsillo mágico**, los hace realidad por mí» ✅. |
| De dónde saca los inventos | De una **tienda del futuro**, el **Mirai Depāto** («未来デパート», los Grandes Almacenes del Futuro). Pide por catálogo, mete el pedido en el cajón de Nobita y le llega al momento. **Lo caro no lo compra**: alquila unos dos tercios, y a veces le mandan **muestras gratis** ✅. Es justo el «Gratis / De pago» del foro. |
| Y lo pirata | En su mundo hay una **Patrulla del Tiempo** (タイムパトロール) que persigue los delitos con el tiempo ✅, y en la película de 2013 el malo es un **ladrón de artilugios**, el «Ladrón DX» (怪盗DX) ✅. Sirve para decir «nada pirata» sin sermón. |
| Cuadro de diálogo propio | No es un globo. Es **el momento de sacar el invento**: Doraemon mete la mano en el bolsillo, lo levanta y **canta su nombre**. En el subtítulo japonés va entre corchetes: «｢タイムテレビ｣！» ✅. En la serie de 2005 suena un «pua-pua-pua… ¡te-tte-rē!» ⚠️. Ver §7. |
| Objeto para la lámina | **El bolsillo mágico** (el del plan) sigue siendo bueno, pero propongo mejorarlo: **el catálogo gigante de los Grandes Almacenes del Futuro, abierto sobre el escritorio de Nobita, con el cajón abierto** (ver §19, concepto A). En Blender: escritorio, cajón, catálogo, tatami. |
| El más querido | **Doraemon**, primero en todas las encuestas ✅. **Dorami**, su hermana, sale **segunda** entre los de 20 a 30 años, **por delante de Nobita** (Mynavi, 2025) ✅. Buena candidata para una lámina 2. |
| Voz latina | **Irwin Daayán** (Doraemon, serie de 2005 y películas de Netflix) ✅ · **Laura Torres** (Nobita) ✅. En la serie clásica, la primera voz de Doraemon fue **Ricardo Tejedo** ✅. Ver §10. |
| Letras | **Fredoka** o **M PLUS Rounded 1c** (redondas como la serie). **Kiwi Maru** o **Zen Maru Gothic** si va algo en japonés. **Klee One** o **Yomogi** para lo escrito a mano. Todas traen tildes, ñ, ¿ y ¡: comprobado en el archivo. |
| Tono | Luminoso, cotidiano, de barrio. Cielo azul, tatami, tarde de colegio. **Nada oscuro ni de terror**: el fandom tiene una «leyenda del final» triste que **no hay que tocar** (ver §14). |

---

## 2 · Las escenas que sirven para #recursos (con minuto)

Salen de los subtítulos japoneses con tiempos (ver arriba). El texto
japonés es literal; la traducción es mía.

### 2.1 *Stand by Me Doraemon* (2014): «aquí cabe de todo»

Subtítulo: `[Erai-raws] Stand By Me Doraemon - Movie [1080p][JPN]`. Es la
**primera película de Doraemon en 3D**, de **Shin-Ei, Shirogumi y ROBOT**,
dirigida por **Takashi Yamazaki y Ryūichi Yagi** ✅
([Wikipedia JP](https://ja.wikipedia.org/wiki/STAND_BY_ME_%E3%83%89%E3%83%A9%E3%81%88%E3%82%82%E3%82%93),
[eiga.com](https://eiga.com/movie/79515/)). Entrevistas al staff:
[eiga.com](https://eiga.com/movie/79515/interview/) y, sobre cómo pasaron
los personajes a 3D, [CGWORLD](https://cgworld.jp/interview/1408-sbmd.html)
(en la segunda pasada sí se leyó entera: ver «Punto 18»). Sirve para la luz y el cuarto, **no para copiar la
línea** de la serie.

| Minuto | Qué pasa | Para qué sirve |
|---|---|---|
| 00:05:35 | Doraemon sale del **cajón del escritorio**: «こんばんは 僕 ドラえもん» (Buenas noches, soy Doraemon) ✅ | **presentar** |
| 00:06:14 | «Todo lo que había en el cajón lo pasé a este **bolsillo de cuatro dimensiones**» ✅ | la idea del canal |
| 00:06:18 | «**Aquí cabe de todo**, en este bolsillo» ✅ | frase para la lámina |
| 00:11:26 | «Ahora te enseño lo que es el siglo XXII» ✅ | **explicar** |
| 00:11:31 | «**¡Chan!** “Takecopter”» (ジャ～ン “タケコプター”) ✅ | la pose de sacar el invento |
| 00:15:54 → 00:19:13 | **Desfile de inventos**, uno tras otro: la puerta a cualquier lugar, el pan de la memoria, la capa invisible, el guante fuerte, el pañuelo del tiempo, la cámara de disfraces, la tuerca de las prisas, el túnel de Gulliver, el árbol-apartamento y el gas que endurece nubes ✅ | **el catálogo**: 10 inventos en 3 minutos |
| 00:26:42 | Nobita, pensando: «道具に頼らない…» (no depender de los inventos) ✅ | el «Tutorial»: aprender tú |
| 00:57:40 → 00:57:53 | Los **dos Nobitas**, el niño y el adulto, se dan las gracias: «es raro decírmelo a mí mismo, pero gracias por confiar en mí» ✅ | ejemplo de pedir ayuda y darla |
| 01:08:32 → 01:09:02 | **El padre de Shizuka**, la noche antes de la boda: «Nobita sabe desear la felicidad de los demás y sufrir con su desgracia… Tranquila, **tu futuro será brillante**» ✅ | la escena más famosa de la película; **no es de Doraemon** |

### 2.2 *Nobita y el museo de los artilugios secretos* (2013): un museo de recursos

Subtítulo de Netflix: `映画ドラえもん.のび太のひみつ道具博物館.WEBRip.Netflix.ja[cc].srt`.
Es la película que **más se parece al canal**: un museo con **todos los
inventos, del primer modelo al último**, cada uno en su vitrina.

| Minuto | Qué pasa | Para qué sirve |
|---|---|---|
| 00:03:49 | «¡No está! ¡No está! ¡**Me robaron el cascabel**!» ✅ | el robo = lo pirata |
| 00:09:37 | «Esto es el **Museo de los artilugios secretos**, en el siglo XXII» ✅ | **presentar** el sitio |
| 00:09:44 | «En mi bolsillo hay **muchísimos** inventos, ¿no?» ✅ | |
| 00:09:49 | «**Desde el primer modelo hasta el último**, todos están ahí» ✅ | un hilo por recurso |
| 00:13:44 | Voz del coche: «Eso que flota en la cima de la isla es el museo» ✅ | el plano del museo flotante |
| 00:16:14 | El director, Fiekus: «**Bienvenidos** al Museo de los artilugios secretos» ✅ | **saludo** |
| 00:18:28 | «Ese grande es el **artilugio número uno** de la historia» ✅ | «Verificado», el primero de la vitrina |
| 00:45:27 | «Todos son **únicos en el mundo**. Son mis inventos» (うん どれも 世界に一つしかない 僕の道具だよ) ✅; creo que lo dice Kurt, el joven inventor ⚠️ | quien cuelga lo suyo |
| 00:55:54 | Pepler, el maestro: «Para quien fabrica inventos, lo más importante es **que le guste fabricarlos**» ✅ | frase de cierre |
| 00:57:03 | Aviso del ladrón: «Vendré a **llevarme** un artilugio valioso» ✅ | el ladrón = lo pirata |

> ⚠️ El nombre latino de esta película no lo pude confirmar. En inglés es
> *Doraemon: Nobita's Secret Gadget Museum* ([Wikipedia](https://en.wikipedia.org/wiki/Doraemon:_Nobita%27s_Secret_Gadget_Museum)).

### 2.3 La serie de 2005: el pedido a la tienda del futuro

Subtítulos japoneses por fecha de emisión (`Doraemon (AAAA.MM.DD).srt`).
Doy la **fecha de emisión** en Japón porque así se llama el archivo; el
título del episodio no venía en el subtítulo.

| Emisión · minuto | Qué pasa | Para qué sirve |
|---|---|---|
| 2006-11-10 · 00:16:23 | «**¡Chan!** Ya puedes estar tranquilo» y saca el «｢幸運ダイヤ｣» (Diamante de la suerte) ✅ | la pose de sacar el invento |
| 2006-11-10 · 00:16:34 | «Viendo tanta mala suerte, **lo pedí a los Grandes Almacenes del Futuro**» ✅ | el pedido = colgar un recurso |
| 2006-11-10 · 00:16:50 | «¡Esto es el ｢悪運ダイヤ｣, el Diamante de la **mala** suerte!» Llegó otro producto ✅ | por qué hace falta **«Verificado»** |
| 2005-08-05 · 00:10:02 | Nobita: «**¡Haz algo, Doraemoon!**» (なんとかしてよ ドラえも～ん！) ✅ | la petición: «Cómo se pide una pista sin voz» |
| 2006-05-26 · 00:17:32 | Nobita: «¡Haz algo, Doraemoon!» · Doraemon: «**Ay, qué remedio…**» (しょうがないな～) ✅ | el diálogo más repetido de la serie |
| 2005-04-15 · 00:23:56 → 00:24:07 | Saca inventos en ráfaga: «｢桃太郎印のきびだんご｣！» «｢必中ゴムパチンコ｣！» «｢スモールライト｣！» ✅ | varios recursos de golpe |
| 2006-09-08 · 00:09:08 | Gigante: «Esta noche doy un **recital en el descampado**» ✅ | el descampado de las tuberías |
| 2006-09-08 · 00:11:29 | Gigante: «¡Empieza el recital!» ✅ | la «Pista sin voz» es su micrófono |

> Datos contados en los subtítulos de 2005-2006 (66 archivos): «しょうがないな»
> (qué remedio) sale **28 veces** ✅. Los nombres de invento van **entre
> corchetes ｢ ｣** (「タイムテレビ」, 「幸運ダイヤ」…) ✅; esos corchetes
> también marcan cartas y voces de la tele, así que no doy un recuento.

### 2.4 Segunda pasada: escenas **miradas** en vídeo, con minuto real

Lo de arriba sale de subtítulos. Esto se **vio**: fotogramas sacados con
`fotogramas.py` de Dailymotion e Internet Archive y abiertos uno a uno
(21 fotogramas; YouTube pedía iniciar sesión). El minuto es el de esa copia.

| Qué | Enlace con minuto | Minuto | Qué se ve | Para qué sirve |
|---|---|---|---|---|
| **Opening 1979** «Doraemon no Uta», doblaje latino antiguo, rótulo «Doraemon, el gato cósmico» | [x8k1ck8](https://www.dailymotion.com/video/x8k1ck8?t=5) ✅ | 0:05 · 0:20 · 0:40 | 0:05 Doraemon sale girando de un túnel azul. 0:20 de pie, sonriente, sobre una luna creciente con estrellas. 0:40 vuela con el Takecopter sobre bocetos de máquinas de Leonardo da Vinci; Nobita, Shizuka, Suneo y Gigante lo miran desde abajo | luz del opening; **Doraemon mostrando un invento en el aire** |
| **Ending** del doblaje de **España** (no latino) | [x2vhonl](https://www.dailymotion.com/video/x2vhonl?t=10) ⚠️ copia descolorida, una fuente | 0:10 | cielo de nubes claras y siluetas de niños en un cerro | sólo el tono pastel del cierre |
| **Tráiler** en español de *Stand by Me Doraemon* (junta un anuncio «Esta Navidad, Doraemon…» que puede ser de la secuela ⚠️) | [x33a56v](https://www.dailymotion.com/video/x33a56v?t=30) ✅ | 0:03 · 0:30 · 1:00 · 1:20 | 0:30 Nobita en 3D, cabizbajo y con la mochila, choca contra la puerta corredera. 1:00 Doraemon y Nobita gritan abrazados sobre el tatami, de noche. 1:20 primer plano oscuro de un muñeco de Doraemon en la pared | la luz 3D del cuarto, de día y de noche |
| **Recital de Gigante** en el descampado | [x3402n2](https://www.dailymotion.com/video/x3402n2?t=20) ✅ (es el mismo episodio 2006-09-08 de §2.3) | 0:05 · 0:20 · 0:40 | esmoquin blanco y capa roja, ojos cerrados, boca muy abierta, brazo izquierdo al público, **micrófono en la derecha**, confeti y focos de colores | **presentar o celebrar**; la «Pista sin voz» |
| Gigante asustado en una cabina o nave (película sin identificar ⚠️) | [x2uugoz](https://www.dailymotion.com/video/x2uugoz?t=25) ⚠️ copia con marca de un canal pirata encima | 0:10 · 0:25 | camiseta turquesa a rayas, ojos redondos, cejas en zigzag, consola verde oscuro | cara de **miedo** de Gigante |
| **«El Pueblo de Nobita»**, episodio con **doblaje latino real** (grabación de TV de Ecuador) | [Internet Archive](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=180) ✅ | 0:30 · 1:30 · 3:00 · 5:00 | 0:30 los dos señalan una placa diminuta en la pared de la casa. 1:30 sentados en el cuarto, **tatami verde**, Nobita tirado quejándose. 3:00 Nobita riega con una regadera **un pueblo en miniatura**. 5:00 plano general del pueblo con ellos al lado | **un invento en uso**: «aquí cabe de todo», a escala |
| **«Un mundo sin dinero»** (el archivo dice «Episodio 184 - El indicador del desorden», mal nombrado ⚠️) | [Internet Archive](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%20184%20-%20El%20indicador%20del%20desorden%20.mp4?t=180) ✅ | 3:00 → 3:09 | Nobita, con la camiseta **roja** de la serie clásica, llora tapándose la cara con las dos manos; su papá lo abraza por los hombros | la única **tristeza** vista con minuto |

> No encontré fuera de YouTube el vídeo del **sonido de sacar un invento**
> (antes y después) ni un clip limpio de **la boda y el padre de Shizuka**:
> siguen con el minuto del subtítulo, sin fotograma visto. Búsquedas en la
> bitácora.

---

## 3 · Arte oficial y referencias visuales

> [!note] Segunda pasada
> Ya hay **3 hojas de contacto** miradas (§3.0) y los fondos oficiales se
> bajaron y se midieron (§3.1). Lo que sigue sin verse lleva ⚠️.

### 3.0 Las hojas de contacto (qué número sirve) ✅

Las tres están en `hojas/`. Las dos primeras salen de
`investigar_serie.py` (wiki `doraemon`, página de Gigante, «Takeshi
Gouda»); la tercera la montó el investigador de imagen con los 5 fondos
oficiales. **Las miré yo al redactar** y corrijo dos números de la parte de
imagen (abajo). Bajo cada miniatura va su tamaño real y el nombre del
archivo en la wiki: el original está en
`https://doraemon.fandom.com/wiki/File:<nombre>`.

**`hojas/personajes_01.jpg`** (n.º 1-48, 2400×1704, 823 KB)

| N.º | Qué es | Para qué |
|---|---|---|
| 1 | «Handsome Gian», cara de Gigante en primer plano, **5016×2822** ([original](https://static.wikia.nocookie.net/doraemon/images/2/24/Handsome_Gian.png)) | el meme del «Gigante guapo»; la cara más grande que hay |
| 2 | **Cel de producción** pintado a mano: Doraemon al volante de un barco del tiempo, Nobita y una niña de rojo, rayos celestes; se ve la cinta de papel, **2048×1632** ([original](https://static.wikia.nocookie.net/doraemon/images/3/3e/DoraemonTimeMachine.jpg)) | el color plano de producción; hex medidos en §16 |
| 3 | La máquina del tiempo de Dorami, un tulipán naranja, 1712×1880 | objeto de Dorami |
| 5 | «All eating Gian»: todos gritando con la boca abierta | reacción de grupo |
| 15 | Doraemon, Nobita y Gigante abrazados en el bosque, 2048×1536 ([original](https://static.wikia.nocookie.net/doraemon/images/5/50/Doraemon_Nobita_and_Gian.jpg)) | **amistad**; hex de la camiseta en escena |
| 16 | «Four together happy»: los cuatro niños contentos en la calle | grupo **celebrar** |
| 17 | «Gian ID card»: **Gigante con una guitarra**, rótulo «GIAN TAKESHI.G.» | con su instrumento. **Corrige** a la parte de imagen: no es un micrófono, es una guitarra |
| 18 | «Gian and Doraemon fight»: Gigante con gorro de cocinero y la mano de Doraemon | gag de la cocina de Gigante |
| 21 | Gigante y Suneo con Nobita en **3D** (*Stand by Me*) | contraste 2D/3D |
| 25 | Gigante con su equipo de béisbol | grupo |
| 28 | «Gian mad»: puño y dientes, primer plano | **regañar** |
| 29 | Gigante sale de un agujero blanco y cae en un cuarto con estantería y reloj | un invento en uso |
| 33 | «Gian smirking deeply»: ríe con los ojos cerrados y un libro en la mano | presumir |
| 37 | Shizuka le da un regalo a Gigante con gorro de fiesta; Doraemon y Nobita al lado | el cumpleaños de Gigante (15 de junio) |
| 43 | Nobita, Gigante y Suneo saltando de alegría sobre fondo de rayos | **celebrar** |
| 44-48 | Shizuka, Gigante y Suneo en la calle, mezclados, chocando, sentados | grupos de 3 |

**`hojas/objetos_01.jpg`** (n.º 49-96, 2400×1704, 770 KB). **La más útil
para el objeto del encargo.**

| N.º | Qué es | Para qué |
|---|---|---|
| 57 | **Hoja de modelo de Gigante de 1973**: 10 caras y cuerpos a línea, 2033×1296 | la única hoja de modelo oficial encontrada |
| 56 · 83 | Gigante, modelo 2005 limpio (2344×1320) y otra versión 2005 (1600×891) | comparar 1973 con 2005 |
| **58** | **El bolsillo 4D** (media luna blanca) sobre fondo de rayos azules y estrellas, con la cartela roja «四次元ポケット», **2151×1210** | **la imagen clave del bolsillo**: su forma y cómo se anuncia. **Corrige**: la parte de imagen lo daba como n.º 64 |
| 59 | «Obtaining Bag»: un monedero rosa acolchado con cadena, sobre los mismos rayos azules, 2100×1181 | otro invento anunciado igual |
| 60-63 · 65 | Béisbol: gorra blanca con **«G»**, lanzamiento de Gigante | emblema del equipo (Punto 19) |
| 64 | «YWK last shot»: los cinco juntos sobre amarillo, Doraemon en el centro con los brazos abiertos, 2046×1142 | **presentar en grupo** |
| 73 | Nobita y Doraemon en la máquina del tiempo, dentro del túnel, 1920×1080 | el cajón y el túnel |
| 74 | Cartela «Path-Finding Stick / ミチサキステッキ» sobre rayos, 1617×1018 | **cómo se rotula un invento**: letra roja con borde blanco |
| 75 | Linterna pequeña (Small Light), película de 2021, 1562×1050 | objeto en 3D-look |
| 76-80 | **Gigante de 1979 volando con el Takecopter**, cinco poses seguidas sobre verde, 1400×1082-1152 | poses de acción recortables |
| 81 | Página del manga en inglés con la puerta a cualquier lugar, 1440×1024 | cómo es el globo del manga |
| 82 | Cartela «するとレンズ» (Act Predictor Lens), 1599×899 | otra cartela de invento |
| **85** | Cartela «**Voice Thickener / コエカタマリン**» (el caramelo que vuelve sólidas las palabras), 1450×954 | **un invento de la voz**: perfecto para un servidor de doblaje |
| 86 | La **puerta a cualquier lugar en 3D** en una calle, 1066×1067 | el rosa de la puerta en luz real |
| 95-96 | «Yume wo Kanaete»: los cinco en paneles de colores, 1366×768 | presentación en paneles |

**`hojas/fondos_01.jpg`** (652×2433, 379 KB, montaje propio con Pillow)

| N.º | Qué es | Original |
|---|---|---|
| 1 | Cuarto de Nobita, lado del escritorio (cortina verde, estantería, mochila) | [Wallpaper04](https://www.dropbox.com/s/vnho086qmwv4y0v/Wallpaper04.jpg?dl=1), 1280×894 |
| 2 | Cuarto de Nobita, lado del armario (oshiire) y la puerta naranja | [Wallpaper05](https://www.dropbox.com/s/71u5znm49vhn49w/Wallpaper05.jpg?dl=1), 1280×894 |
| 3 | El descampado con las tres tuberías, árbol y casas | [Wallpaper03](https://www.dropbox.com/s/uk3juifiwls5geh/Wallpaper03.jpg?dl=1), 1280×894 |
| 4 | Túnel del tiempo, relojes blandos | [Wallpaper01](https://www.dropbox.com/s/qvquqzlta7m0hp6/Wallpaper01.jpg?dl=1), 1280×929 |
| 5 | Túnel del tiempo, otro ángulo | [Wallpaper02](https://www.dropbox.com/s/n77qhby5jq9tpfz/Wallpaper02.jpg?dl=1), 1280×905 |

> Ojo: la parte de imagen daba los enlaces de Dropbox cruzados (el 01 como
> cuarto). **Lo comprobé bajando el 01 y el 04**: el 01 mide 1280×929 y es
> azul (túnel); el 04 mide 1280×894 y es verde y beige (cuarto). La tabla de
> arriba ya va bien.

### 3.1 Fondos oficiales para descargar (lo mejor que hay) ✅

- **Fondos oficiales de la serie para videollamadas**, abril de 2020: **5
  dibujos de fondo** del anime (settei), entre ellos **el cuarto de Nobita**,
  **el descampado con las tuberías** y **el túnel del tiempo** de la máquina
  del tiempo. Página de descarga:
  [dora-world.com/contents/1399](https://dora-world.com/contents/1399).
  Lo cuentan cuatro medios:
  [@DIME](https://dime.jp/genre/898907/),
  [Famitsu](https://www.famitsu.com/news/202004/20197007.html),
  [Anime!Anime!](https://animeanime.jp/article/2020/04/20/53113.html) y la
  [nota de prensa de Shogakukan](https://prtimes.jp/main/html/rd/p/000000647.000013640.html).
  **Es la base perfecta**: fondo oficial, sin personajes, para meter el
  escritorio en Blender delante.
  **Segunda pasada: bajados y medidos** ✅. Siguen en Dropbox, enlazados
  desde la propia página: **1280×894 a 1280×929, JPEG** (tabla de §3.0,
  hoja `fondos_01.jpg`). Llevan la marca «DORAEMON Channel dora-world.com»
  arriba a la derecha y «©藤子プロ・小学館・テレビ朝日・シンエイ・ADK» abajo:
  **hay que taparlas** si se usa el fondo entero. Paleta medida en §5.2.
- **Página de fondos de pantalla** de la web oficial:
  [dora-world.com/wallpaper](https://dora-world.com/wallpaper) (tamaños
  sin ver ⚠️).

### 3.2 Películas: carteles y webs oficiales

- **2026 · *Nuevo Nobita y el castillo del diablo submarino*** (新・のび太の
  海底鬼岩城), película n.º 45, estreno en Japón el **27 de febrero de 2026**,
  dirigida por **Tetsuo Yajima** ✅
  ([eiga.com](https://eiga.com/movie/104573/),
  [Wikipedia](https://en.wikipedia.org/wiki/Doraemon:_New_Nobita_and_the_Castle_of_the_Undersea_Devil)).
  Web oficial con el cartel: [doraeiga.com/2026](https://doraeiga.com/2026/).
  Ficha del estudio: [Shin-Ei](https://shin-ei-animation.jp/works/movie_doraemon_2026/).
- **2013 · *Nobita y el museo de los artilugios secretos***: la del museo
  (ver §2.2). Ficha: [IMDb](https://www.imdb.com/title/tt2768084/). En
  España se llamó *Doraemon y Nobita Holmes en el misterioso museo del
  futuro* ✅ ([eCartelera](https://www.ecartelera.com/peliculas/doraemon-y-nobita-holmes-en-el-misterioso-museo-del-futuro/),
  [Ramen Para Dos](https://ramenparados.com/critica-doraemon-y-nobita-holmes-en-el-misterioso-museo-del-futuro/)).
- ***Quédate conmigo, Doraemon*** (2014) y ***Quédate conmigo, Doraemon: 2***
  (2020), en **Netflix Latinoamérica con doblaje latino**: las dos llegaron
  al catálogo el 24 de diciembre de 2021, y **la primera recibió su
  doblaje latino después, en febrero de 2022** ✅ (ANMTV, TVLaint, FUNiAnime): [película 1](https://www.netflix.com/us-es/title/80158156),
  [película 2](https://www.netflix.com/us-es/title/81451264).

### 3.3 El manga (Fujiko F. Fujio)

- **45 tomos** en la colección *Tentōmushi Comics*, con **821 historias**
  elegidas por el propio autor, más un **tomo 0** ✅
  ([Shogakukan](https://www.shogakukan.co.jp/pr/tencomi/doraemon/),
  [lista oficial de tomos](https://shogakukan-comic.jp/book-series?cd=13325)).
- Hay **6 tomos a color** (*Doraemon Color Sakuhinshū*), con los originales
  a color tal como salieron en revista ✅ (mismo resultado de búsqueda).
  **Para la lámina interesan más que los de blanco y negro.**
- Todas las portadas juntas, para elegir pose:
  [mangamuseum.hatenablog.com/entry/doraemon](https://mangamuseum.hatenablog.com/entry/doraemon)
  (galería de fan, no oficial).

### 3.4 Sitios reales con fotos

- **Museo Fujiko F. Fujio** (Kawasaki). En la azotea, «la **Harappa**»: el
  **descampado** con **las tuberías de cemento** y una **puerta a cualquier
  lugar** de tamaño real, rodeado de verde ✅
  ([web del museo](https://fujiko-museum.com/hiroba.html),
  [plus KAWASAKI](https://kawasaki.metropolitan.jp/plus-kawasaki/fujikomuseum/index.html)).
  Fotos de visitante, con ángulos: [camera10.me](https://camera10.me/blog/photospot/fujiko-museum).
- **Tienda oficial «Doraemon Mirai Department Store»**, en DiverCity Tokyo
  Plaza (Odaiba): la tienda real que lleva el nombre de los Grandes
  Almacenes del Futuro ✅
  ([ficha del centro comercial](https://mitsui-shopping-park.com/divercity-tokyo/shopguide/1456788.html),
  [web de la tienda](https://mirai.dora-world.com/),
  [Instagram oficial](https://www.instagram.com/dora_mirai/)).

### 3.5 Arte oficial nuevo de la segunda pasada ✅

Todo visto y medido por el investigador de imagen.

- **Retratos oficiales limpios, modelo 2005, sin fondo** (la mejor base de
  pose y ropa): [Doraemon](https://static.wikia.nocookie.net/doraemon/images/d/d1/Doraemon_2005_Anime_Remake.png)
  877×1248 · [Nobita](https://static.wikia.nocookie.net/doraemon/images/6/62/NobitaNobi2005R.png)
  162×270 · [Shizuka](https://static.wikia.nocookie.net/doraemon/images/7/7c/ShizukaMinamoto2005R.png)
  153×270 · [Suneo](https://static.wikia.nocookie.net/doraemon/images/8/80/SuneoHonekawa2005R.png)
  144×270 · [Gigante](https://static.wikia.nocookie.net/doraemon/images/1/1e/TakeshiGouda2005R.png)
  192×270. Los cuatro niños son pequeños: sirven para el color, no para
  ampliar.
- **Cel de producción** del barco del tiempo (hoja personajes n.º 2,
  2048×1632): la referencia más fiable de **color plano de producción**.
- **Portadas de los tomos**: el catálogo oficial de Shogakukan tiene **83
  portadas** (los 45 *Tentōmushi* más los 6 a color y otros). La del tomo 1
  se bajó: 200×316 px, miniatura ([imagen](https://www.shogakukan.co.jp/pr/tencomi/doraemon/images/cover1_1.png)).
  Portada clásica: Doraemon de cerca, fondo degradado rosa y morado, título
  grande en katakana.
- **Artbook del 50.º aniversario, «THE GENGA ART OF DORAEMON»**
  (ドラえもん拡大原画美術館): **más de 130 originales** a color y a línea,
  elegidos por Hashimoto Asari, con una charla de los mangakas **Naoki
  Urasawa y Shintaro Mugiwara** sobre el trazo de Fujiko F. Fujio ✅
  ([dora-world](https://dora-world.com/contents/1805),
  [Amazon.co.jp](https://www.amazon.co.jp/GENGA-ART-DORAEMON-%E3%83%89%E3%83%A9%E3%81%88%E3%82%82%E3%82%93%E6%8B%A1%E5%A4%A7%E5%8E%9F%E7%94%BB%E7%BE%8E%E8%A1%93%E9%A4%A8/dp/409199069X)).
  No se hojeó por dentro ⚠️.
- **Hoja de modelo de Gigante de 1973** (hoja objetos n.º 57). Es la única
  hoja de modelo pública que apareció.
- **Poses vivas, con objeto**: Gigante con **guitarra** (personajes n.º 17),
  Gigante **volando** con el Takecopter en cinco poses (objetos n.º 76-80),
  Gigante de béisbol (objetos n.º 60-65), los cinco juntos (objetos n.º 64).
- **Sigue faltando** ⚠️: *key visuals* sueltos de la serie de TV (no de
  película) y portadas de Blu-ray/DVD. No aparecieron fuera de Fandom.

---

## 4 · Fan art y 3D (sólo como referencia)

> Nada de esto se pega. Se mira para la luz, el encuadre y las medidas.
> Los modelos 3D de personajes o de inventos son **fan art de una marca
> ajena**: aunque Sketchfab diga «gratis», el diseño es de Fujiko Pro.

### 4.1 Modelos 3D de sitios y objetos (Sketchfab y otros)

**Segunda pasada: licencias comprobadas por la API de Sketchfab** ✅. Todos
estos son **CC Attribution (CC BY)**: se pueden usar **nombrando al autor**.
La licencia cubre la malla, no el personaje: sigue siendo de Fujiko Pro.

| Modelo | Autor | Licencia (API) | ♥ | Enlace | Para qué |
|---|---|---|---|---|---|
| **Doraemon** | Andy (Pandabox) | CC BY | 355 | [Sketchfab](https://sketchfab.com/3d-models/none-7b1db542a10f40da9a250c33afb5325f) | el más valorado; volumen del cuerpo |
| Doraemon Lucky Cat | Patrickart.hk | CC BY | 280 | [Sketchfab](https://sketchfab.com/3d-models/none-73672e27df964ebc8bc1d72a639c4896) | figura tipo gato de la suerte |
| Doraemon (Fan Art) | Takiri Cube | CC BY | 95 | [Sketchfab](https://sketchfab.com/3d-models/none-d60a33c2a0e0487ca13115f04a65e0ee) | otra versión del cuerpo |
| **Nobita's Room** | Cre8t!ve V!be | CC BY | 77 | [Sketchfab](https://sketchfab.com/3d-models/none-7ac2289be8be408292b29a06f8f40a71) | **medidas del cuarto**: escritorio, estantería, tatami |
| Doraemon City | Aizen | CC BY | 71 | [Sketchfab](https://sketchfab.com/3d-models/none-1c6ff7650cb5467d9871bffd4030eca1) | barrio |
| Nobita | hito127 | CC BY | 18 | [Sketchfab](https://sketchfab.com/3d-models/none-1a54ed50a2b24d758c8e14e744a4d637) | Nobita en 3D |
| Tin Airship (*Nobita and the Tin Labyrinth*) | chemicalX | CC BY | 16 | [Sketchfab](https://sketchfab.com/3d-models/none-54daadccf4434f85b30f6c22bc1830e1) | objeto de una película concreta |
| Suneo · Dekisugi · 3D Movie Maker Shizuka | dannilloboyy | CC BY | 2-4 | [Suneo](https://sketchfab.com/3d-models/none-e05f60fed1de499eb07dae51fd2d2f70), [Dekisugi](https://sketchfab.com/3d-models/none-8abc15899c494f4f9e1074be465cde8a), [Shizuka](https://sketchfab.com/3d-models/none-521844bf0f7645d792312881dfaa99ba) | secundarios, baja calidad |
| Shizuka 3D Model For Retopology | Asim-ali | **«Free Standard», no CC** ⚠️ | 4 | [Sketchfab](https://sketchfab.com/3d-models/none-be39bdeddc3647739ba5996a1a8a1e88) | no está claro si se puede reutilizar |

> Choque entre partes: la de texto decía «no hay modelos de Doraemon con
> licencia libre». La de imagen lo comprobó **por la API** y sí los hay (CC
> BY). Vale la de imagen. **Rigs** listos para animar: no se confirmó
> ninguno ⚠️.

Los de la primera pasada (licencia sin comprobar por la API ⚠️):

| Modelo | Autor | Enlace | Para qué |
|---|---|---|---|
| **Nobita's Room (Doraemon)** | Cre8t!ve V!be (@unfocusedblender) | [Sketchfab](https://sketchfab.com/3d-models/nobitas-roomdoraemon-3d-model-7ac2289be8be408292b29a06f8f40a71) | medidas del cuarto: escritorio, estantería, tatami |
| **Doraemon Anywhere Door** | mfxmotions | [Sketchfab](https://sketchfab.com/models/726f19f5469a45a18396876076093997/embed) | la puerta rosa |
| **Doraemon Gadgets: Small/Big Light, Anywhere door** | aryan-angra | [Sketchfab](https://sketchfab.com/3d-models/doraemon-gadgets-small-big-light-anywhere-door-7fb20d2b56ec411ab994d508279e4f46) | las linternas que encogen y agrandan |
| **Anywhere Door (Pintu Kemana Saja)** | Riza Bassam | [Sketchfab](https://sketchfab.com/3d-models/anywhere-door-pintu-kemana-saja-9aaec1a3f8b44ea1aba3d7aba6fc6227) | puerta sencilla, sin texturas, hecha en Blender |
| Doraemon en bloques, con bolsillo y cascabel | Leandro.Lexknot.Skunk | [Sketchfab](https://sketchfab.com/3d-models/doraemon-38e5a3892d494bc699612a425a43ffdc) | **no** para la lámina: estilo distinto |
| Puerta para imprimir en 3D | varios | [MakerWorld](https://makerworld.com/en/models/823760-doraemon-anywhere-door), [Printables](https://www.printables.com/model/621254-doraemon-anywhere-door-ren-yi-men-tabletop-miniatu) | proporciones de la puerta |

### 4.2 Renders de fans del cuarto y la casa (mirar la luz)

- **Nobi's Residence remade in Blender** (casa entera, Cycles):
  [ArtStation L32aWK](https://www.artstation.com/artwork/L32aWK).
- **Nobita's home en Unreal Engine**, basado en *Stand by Me*:
  [ArtStation 8wklBG](https://www.artstation.com/artwork/8wklBG).
- **Nobita's Room with Doraemon**, hecho en Maya:
  [The Rookies](https://www.therookies.co/projects/28051).
- Dos cuartos hechos en Blender por la comunidad:
  [Blender Artists 1](https://blenderartists.org/t/doraemon-nobitas-room/695493),
  [Blender Artists 2](https://blenderartists.org/t/nobitas-room-from-one-of-my-favourite-shows-as-a-kid-doraemon-i-made-in-blender/1373548).
- De pago (no hace falta): [Gumroad](https://ajaayvine.gumroad.com/l/iosyzr).
- Figura oficial del cuarto de Nobita (Figuarts ZERO), con **el cajón que
  se abre y el túnel del tiempo dibujado dentro** ✅
  ([Dengeki Hobby](https://hobby.dengeki.com/news/953237/),
  [MANTANWEB](https://mantan-web.jp/article/20200308dog00m200006000c.html)).
  Buena referencia de **cómo se ve el cajón abierto**.
- Vídeo: recorrido en 3D por la casa de los Nobi, con el plano de cada
  planta ([youpouch](https://youpouch.com/2016/02/05/333606/)).

### 4.3 Fan art 2D

Pixiv sigue sin abrirse directo, pero **Safebooru enlaza el origen real**
(Pixiv o X) de cada dibujo. Sólo para mirar encuadre y color, nunca pegar:

- El mejor valorado: **Doraemon y Suneo**, 2520×2520, de
  [@totototo0507 en X](https://twitter.com/totototo0507/status/1807802641482985883)
  ([imagen](https://safebooru.org/images/4619/14fcd3507038cb1636e15d640de74c13deac4fa3.png)) ✅.
- Doraemon, 2893×2343, origen Pixiv
  ([imagen](https://safebooru.org/images/897/b713a0308b864a370fac498c2adec46e829c0ef0.jpg));
  Doraemon, 2048×1593, de [@doremifaso64](https://x.com/doremifaso64)
  ([imagen](https://safebooru.org/images/59/5649988be249ff454aeaf1f7e448f16843663cd6.jpg)).
- Shizuka, 1323×1488, origen Pixiv
  ([imagen](https://safebooru.org/images/2075/25dcb27b778fe410ee77d7797966dfc865a77f9b.jpg));
  Nobita, 1280×1468, origen Pixiv
  ([imagen](https://safebooru.org/images/501/7457609beb5a940008f8eb38fd205e38af541888.jpg)).
- Casi todo es de Pixiv de 2008-2016, de 500 a 1300 px de lado.

**Etiquetas de Danbooru** que más se repiten al dibujar a cada uno (el
vocabulario que entienden las IA de imagen, ver §18) ✅:

| Personaje | Etiquetas |
|---|---|
| `doraemon_(character)` | bell, red_nose, collar, jingle_bell, whiskers, simple_background |
| `nobi_nobita` | glasses, yellow_shirt, blunt_bangs, shorts, blue_pants |
| `minamoto_shizuka` | twintails, black_hair, skirt, short_twintails |
| `honekawa_suneo` | school_uniform, headphones (ojo: mezcla un Suneo DJ de un cruce de fans, no es canon) |

**Fotos con licencia libre** (Openverse, Flickr): una guitarra de Doraemon
([CC BY 2.0, Adrian F](https://live.staticflickr.com/44/146729298_09935ccd37_b.jpg),
1024×768), una tarta de Doraemon
([CC BY 2.0, Cillian Storm](https://live.staticflickr.com/2234/3541290988_99c0ce9945_b.jpg),
1024×685) y Doraemon junto a la Landmark Tower de Yokohama
([CC BY-SA 2.0, DocChewbacca](https://live.staticflickr.com/3275/2829786921_7ca2a96e59_b.jpg),
768×1024). Sirven para ver **merchandising real con luz real**.

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Qué es | Luz y hora típicas |
|---|---|---|
| **El cuarto de Nobita** | 2.º piso de la casa de los Nobi, **unos 6 tatamis**. Sólo hay ese cuarto y **el armario empotrado (oshiire) donde duerme Doraemon** ✅ ([Fandom JP](https://doraemon.fandom.com/ja/wiki/%E3%81%AE%E3%81%B3%E5%A4%AA%E3%81%AE%E9%83%A8%E5%B1%8B), [HOME'S](https://www.homes.co.jp/cont/living/living_00324/)) | **de día**: claro, crema y verde (fondo oficial y tráiler 0:30). **De noche**: casi a oscuras, un solo rayo de ventana (tráiler 1:00). Medido en §5.2 ✅ |
| **El cajón del escritorio** | La **entrada de la máquina del tiempo**. Dentro está el **túnel del tiempo** (時空間) ✅ ([pixiv](https://dic.pixiv.net/a/%E3%82%BF%E3%82%A4%E3%83%A0%E3%83%9E%E3%82%B7%E3%83%B3(%E3%83%89%E3%83%A9%E3%81%88%E3%82%82%E3%82%93))) | el túnel: espiral blanca sobre azul y morado, con **relojes blandos** rojos, verdes y amarillos que caen (fondos oficiales 4 y 5; opening 0:05) ✅ |
| **El descampado** | solar vacío con **tres tuberías de cemento** apiladas. Ahí juegan, ahí canta Gigante ✅ (2006-09-08, 00:09:08) | de día, cielo celeste y tierra clara (fondo oficial 3) ✅; **de noche con focos** para los recitales (clip 0:20) ✅. El atardecer naranja, sin ver ⚠️ |
| **La tienda del futuro** | Grandes Almacenes del Futuro (未来デパート), donde Doraemon **compra por catálogo**. El catálogo mide **como dos tatamis** ✅ ([pixiv](https://dic.pixiv.net/a/%E6%9C%AA%E6%9D%A5%E3%83%87%E3%83%91%E3%83%BC%E3%83%88), [numan](https://numan.tokyo/anime/M5OEY)) | no sale casi nunca: se ve el catálogo, no la tienda |
| **El Museo de los artilugios** | museo del siglo XXII **flotando en la cima de una isla** (2013, 00:13:44) ✅ | luz de exposición ⚠️ |

### 5.2 Paleta **medida** (segunda pasada) ✅

Ya no sale de paletas de fans. Se midió con `estilo.py` y Pillow sobre los
**fondos oficiales** (investigador de imagen) y sobre **fotogramas vistos**
(investigador de vídeo). El % es la parte de la imagen con ese color.

**Fondos oficiales de dora-world** (hoja `fondos_01.jpg`):

| Sitio | Hex medidos | Cómo está pintado |
|---|---|---|
| Cuarto, lado del escritorio (n.º 1) | `#C1DBAA` 18% (tatami) · `#D3B177` 17% (mueble) · `#B09265` 14% (escritorio) · `#E7EBE6` 14% (pared) | brillo 81%, saturación 28% |
| Cuarto, lado del armario (n.º 2) | `#C1DAAC` 15% · `#E9E3D2` 15% · `#B4986B` 14% · `#E5EDED` 14% · `#97BEAE` 13% | claro, poco saturado |
| Descampado (n.º 3) | `#E4ECF1` 19% (cielo) · `#D8D69D` 16% (tierra) · `#92C064` 13% (árbol) · `#B1CDDE` 12% · `#67C3EE` 9% | brillo 84%, saturación 28%, línea `#7C8B7B` |

**Fotogramas vistos** (enlaces con minuto en §2.4):

| Sitio y toma | Hex medidos | Cómo está pintado |
|---|---|---|
| Túnel del tiempo (opening, [0:05](https://www.dailymotion.com/video/x8k1ck8?t=5)) | `#0F1113` 25% · `#2F4863` 23% · `#3F728B` 17% · `#81947F` 12% · `#173640` 12% | degradado, línea fina `#505F59`, brillo 39% |
| Luna y cielo de noche (opening, [0:20](https://www.dailymotion.com/video/x8k1ck8?t=20)) | `#101012` 50% · `#1E1F24` 21% · `#908D7A` 13% (luna) | muy oscuro, brillo 20% |
| Bocetos de Da Vinci (opening, [0:40](https://www.dailymotion.com/video/x8k1ck8?t=40)) | `#8D6E41` 33% · `#9E8359` 30% · `#131112` 23% · `#674B29` 11% | sepia de pergamino, línea `#474032` |
| **Recital de noche** en el descampado ([0:20](https://www.dailymotion.com/video/x3402n2?t=20)) | `#395A81` 20% (cielo) · `#CA5E41` 16% (foco) · `#F0AD76` 12% (piel con luz cálida) · `#803520` 10% | degradado, brillo 61% por los focos |
| **Cuarto 3D de día** (tráiler, [0:30](https://www.dailymotion.com/video/x33a56v?t=30)) | `#A09B7F` 47% · `#B8B495` 26% (puertas correderas) · `#70624C` 15% · `#F9F9E1` 5% | crema y beige, brillo 61% |
| Cuarto 3D de noche (tráiler, [1:00](https://www.dailymotion.com/video/x33a56v?t=60)) | `#0F0905` 35% · `#2F2313` 27% · `#1C0E05` 20% (cómoda) · `#3E372C` 9% | **brillo 13%**, sólo un rayo de ventana |
| Calle y casa de Nobita, de día (serie clásica, [0:30](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=30)) | `#8D9679` 22% (arbustos) · `#2B4036` 17% (seto) · `#83B3B2` 13% · `#B4D1C5` 12% (cielo) | línea `#5E665B`, brillo 47% |
| **Tatami** de la serie clásica ([1:30](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=90)) | `#A7A741` 23% · `#658D36` 18% (verde amarillento) · `#07150C` 24% (sombra) · `#DFDEC4` 6% (pared) | saturación 67% |
| Cielo del ending (España) | `#B6B2B5` 62% · `#96A9B4` 17% · `#67788F` 9% ⚠️ copia descolorida | plano (cel) |

**Lo que cambia respecto a la primera pasada:**
- Tatami: `#B9B77A` «de memoria» → `#A7A741`/`#658D36` en la serie clásica y
  `#C1DBAA` en el fondo oficial de 2005. Misma familia verde-amarilla; la
  serie clásica es más saturada y más oscura.
- Cielo de tarde `#8FD0F0` «de memoria» → cielo de día medido `#E4ECF1` y
  `#67C3EE` (fondo oficial). El atardecer sigue sin medir ⚠️.
- Los colores de los personajes, medidos, están en §16.

**Para #recursos** (canal de día, para consultar): la paleta clara del
cuarto de día (`#C1DBAA`, `#D3B177`, `#E7EBE6`, o en 3D `#A09B7F`,
`#F9F9E1`). El azul negro del túnel es para acción, no para leer.

Las paletas de fans de la primera pasada quedan **sólo como contraste**:
azul `#18A2E7`/`#03ADF0`, rojo `#E61737`, amarillo `#FED037`, rosa de la
puerta `#F8AAC0`, marrón `#403C2C`/`#904A30`
([brandpalettes](https://brandpalettes.com/doraemon-color-codes/)). El rosa
de la puerta tiene ahora el valor de su ficha en la wiki, `#F17BAF`
(Punto 25).

### 5.3 Texturas reales equivalentes (libres)

| Textura | Enlace | Licencia |
|---|---|---|
| **Tatami** | [Poly Haven · tatami_mat](https://polyhaven.com/a/tatami_mat) | CC0 ✅ |
| **Tatami** (otro) | [ambientCG · Tatami005](https://ambientcg.com/view?id=Tatami005) | CC0 ✅ |
| Tatami 1024×1024 | [3dtextures.me · tatami](https://3dtextures.me/tag/tatami/) | gratis (ver ficha) ⚠️ |
| Madera del escritorio, papel del catálogo, cemento de las tuberías | [Poly Haven · texturas](https://polyhaven.com/textures), [ambientCG](https://ambientcg.com/) | CC0 |

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **El logo japonés «ドラえもん»**: letras redondas y gruesas, como de
  rotulador, sin esquinas ⚠️. La segunda pasada no encontró una fuente que
  describa el trazo oficial (búsquedas en japonés en la bitácora). Lo
  confirma **de forma indirecta** una letra de fan que lo copia (abajo).
- **「ドラえ文字」 (Dora-e-moji)**, letra japonesa gratuita hecha por un fan
  a partir del logo ([cute-freefont](https://cute-freefont.flop.jp/tukiakari_doraemoji.html)) ⚠️
  (una fuente; la web del autor está archivada). **Sólo uso personal.**
  **Sólo trae hiragana, katakana y números: ni letras latinas, ni tildes,
  ni ñ, ni ¿ ¡** (lo dice su ficha; el enlace de descarga está roto, no se
  pudo abrir con fontTools). Sirve de **referencia visual del logo**, nunca
  para el texto en español.
- **Las cartelas de invento** (lo vi en la hoja `objetos_01.jpg`, n.º 58,
  74, 82 y 85): el nombre del invento sale en **letra gruesa y redonda, de
  color (rojo, amarillo), con borde blanco u oscuro**, sobre un fondo de
  **rayos azules con destellos**; a veces con el nombre en inglés encima
  («Path-Finding Stick», «Voice Thickener») ✅.
- **El logo de *Stand by Me Doraemon***: la letra **Britannic**, que es **de
  pago** ✅ ([fontmeme](https://fontmeme.com/stand-by-me-doraemon-font/)).
- **Letra «Doraemon»** hecha por fans (fluffyartstudio): gratis **sólo
  para uso personal** ✅ ([dafont](https://www.dafont.com/doraemon-2.font)).
  Para Discord, mejor una de Google Fonts.
- **Los nombres de los inventos** en el subtítulo japonés van **entre
  corchetes** ｢ ｣ y con **¡!** al final ✅ (§2.3).

### 6.2 Letras libres comprobadas por mí

Bajadas de [google/fonts](https://github.com/google/fonts) y revisadas con
fontTools: **todas traen á é í ó ú ñ Ñ ¿ ¡ ü** ✅.

| Uso | Letra | Por qué | Japonés |
|---|---|---|---|
| **Títulos** («Recursos») | **Fredoka** (variable, gruesa) | redonda y blanda, como el cuerpo de Doraemon | no |
| Títulos (otra) | **M PLUS Rounded 1c** Black/ExtraBold | redonda, seria para textos largos | sí |
| **Texto de las placas y etiquetas** | **Zen Maru Gothic** Bold o **Nunito** | se lee bien en el móvil | Zen sí |
| Algo en japonés («ひみつ道具») | **Kiwi Maru** o **Mochiy Pop One** | redonda, de libro infantil | sí |
| **Lo escrito a mano** (el pedido, notas de Nobita) | **Klee One** o **Yomogi** | lápiz de colegio | sí |
| Globo de manga, si hace falta | **Comic Neue** o **Patrick Hand** | rotulado de cómic suave | no |
| Gritos («¡Chan!») | **Rammetto One** o **Lilita One** | gruesa y alegre | no |

> **No usar** Bangers ni Dela Gothic One: son de acción y de golpe, no del
> tono de Doraemon.

### 6.3 Una letra para cada uso (segunda pasada)

Reparto propuesto por el redactor **sólo con las letras ya comprobadas con
fontTools** (§6.2); todas traen tildes, ñ, ¿ y ¡ salvo donde se dice:

| Uso | Letra | Cómo |
|---|---|---|
| Logo o título | **Fredoka** gruesa | azul `#1D99C8` con borde blanco, como las cartelas |
| Globo normal | **Comic Neue** o **Zen Maru Gothic** | negro sobre blanco, en recuadro redondeado (§7.3) |
| Grito («¡Chan!», nombre del invento) | **Rammetto One** o **Lilita One** | rojo `#E02333` con borde blanco, como la cartela n.º 58 |
| Pensamiento | **Zen Maru Gothic** regular | gris oscuro, sin negrita |
| Onomatopeya | **Lilita One** | inclinada, con borde; en japonés, **Mochiy Pop One** |
| Cartel del mundo (placas del museo, catálogo) | **M PLUS Rounded 1c** ExtraBold | sobre placa de latón o papel |
| Interfaz de juego | **Nunito** Bold | como el recuadro blanco de *Story of Seasons* (§13) |
| Subtítulos o créditos | **Nunito** o **M PLUS Rounded 1c** | blanco con borde oscuro |
| Lo escrito a mano | **Klee One** o **Yomogi** | lápiz de colegio |
| Sólo como referencia del logo japonés | **Dora-e-moji** | ⚠️ sin letras latinas; uso personal |

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la serie pone en pantalla

1. **El momento de sacar el invento** (lo más reconocible de toda la serie):
   - Doraemon **mete la mano en el bolsillo**, busca, y **levanta el
     invento** diciendo su nombre con voz de anuncio.
   - **El sonido cambia según la época** ✅
     ([nokikero](https://nokikero.com/dora-gadget-jingle-origin-tidbit/), y un
     vídeo que compara los dos:
     [YouTube](https://www.youtube.com/watch?v=8PCLcvDnuh0)). Con **Nobuyo
     Ōyama** (serie de 1979) era «**¡pikon!**» al sacarlo y
     «pisha-pisha-pisha» al decir el nombre ✅ (segunda pasada: nokikero más
     una encuesta de [questant](https://questant.jp/q/0EA0ACCN) y una
     pregunta de [Yahoo! Chiebukuro](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1479644414)).
     Con **Wasabi Mizuta** (serie de 2005) las fuentes **no coinciden** ⚠️:
     la primera pasada leyó en nokikero «**pua-pua-pua…**» (la mano dentro
     del bolsillo) y «**¡te-tte-rē!**»; la segunda pasada lo da como
     «**¡bikān!**» (ビカーン) al anunciar el nombre. Hay que oírlo en un
     episodio.
   - El famoso «**te-re-re-tte-tere**» que todo el mundo imita **no es el de
     la serie**: es un error popular que viene de los cómicos japoneses ✅
     (nokikero, y lo repite como chiste
     [bokete](https://bokete.jp/boke/67191241)).
   - En la serie de 2005, mientras lo levanta, **el nombre del invento sale
     escrito en pantalla**, sobre un **fondo de colores** ✅ ([Yahoo!
     Chiebukuro](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11258732946)
     y, en la segunda pasada, **visto** en las cartelas de la hoja
     `objetos_01.jpg`: n.º 58 «四次元ポケット» en rojo con borde blanco sobre
     **rayos azules con destellos**; n.º 74 y 82 sobre rayos morados y
     rosas; n.º 85 «Voice Thickener / コエカタマリン» en amarillo sobre
     rayos verdes).
     **Esto es el «cuadro de diálogo» de Doraemon**: un rótulo con el
     nombre, no un globo.
   - Detrás de Doraemon aparece ese **fondo especial** mientras lo levanta.
     **En enero de 2024 ese fondo cambió de diseño** ⚠️ (una sola fuente, un
     post de X con el antes y el después:
     [x.com](https://x.com/x3657yama/status/1743585478052581865)). La
     segunda pasada repitió la búsqueda en japonés y todo remite al mismo
     post. Las cartelas de la hoja no dicen su año, así que **no sé cuál es
     el fondo de antes y cuál el de después**.
   - En *Stand by Me* dice «**¡Chan!**» (ジャ～ン) antes del nombre ✅
     (00:11:31).
2. **El grito de Nobita**: «**¡Doraemooon!**» (ドラえも～ん), casi siempre
   con «**¡haz algo!**» (なんとかしてよ) ✅. Y Doraemon contesta «**ay, qué
   remedio**» (しょうがないなぁ) ✅ (§2.3).
3. **El catálogo y el pedido**: el catálogo gigante de los Grandes Almacenes
   del Futuro y el **sobre del pedido** que se mete en el cajón ✅
   ([doranew](https://doranew.net/mirai-catalog-envelope/), pixiv).
4. **Etiquetas en los inventos**: en la película de 2013 cada invento está
   en su vitrina del museo ✅ (§2.2). La forma de la placa no la vi ⚠️.

### 7.2 Cómo hablan (por el subtítulo)

| Quién | Cómo llama a los demás | Muletillas |
|---|---|---|
| **Doraemon** | «Nobita-kun» (のび太君) ✅ | «qué remedio» (しょうがないな); «¡chan!» al sacar algo; «tranquilo» (安心していいよ, 2006-11-10 00:16:23) ✅ |
| **Nobita** | «Doraemon», «Shizuka-chan» ✅ | «¡Doraemooon!», «¡haz algo!» ✅; «jejeje, encantado, Doraemon» (エヘヘヘヘ よろしくね, *Stand by Me* 00:10:35) ✅ |
| **Shizuka** | «Nobita-san» (のび太さん), «Dora-chan» (ドラちゃん) ✅ (2006-06-30 00:12:02) | educada; defiende a Nobita: «¡Paren los dos! A Nobita no le gusta» (*Stand by Me* 00:02:35) ✅ |
| **Gigante** | «Nobita» a secas | «¡Nobita, qué te crees!» (のび太のくせに生意気だぞ, 2006-11-10 00:08:58) ✅ ⚠️ (no dice quién habla, pero es su frase); el **recital** ✅ |
| **Suneo** | — | presume: «¡Se lo voy a contar a todos!» (みんなにうんと自慢してやろう, 2006-06-23 00:04:33) ⚠️ quién lo dice |

### 7.3 Cómo se traduce a una lámina fija

La lámina **no lleva un globo blanco**. Tres opciones reales de la serie:

- **A · La placa del invento**: el texto va escrito **en el propio objeto**
  (la tapa del catálogo, la etiqueta del producto, la placa de la vitrina).
  Letra: Zen Maru Gothic o Nunito, sobre cartón o metal real en Blender.
- **B · El anuncio del invento**: una línea corta y grande con **corchetes
  japoneses ｢ ｣ y ¡!**, como en el subtítulo: «｢Recursos｣!». Detrás, el
  **fondo de rayos de color con destellos** del momento de sacar algo
  (hoja `objetos_01.jpg`, n.º 58 y 74) ✅. Letra: Fredoka o Rammetto One,
  de color y con borde blanco.
- **C · La hoja del pedido**: lo que el usuario tiene que hacer, escrito a
  mano en **el sobre de pedido** de la tienda del futuro. Letra: Klee One.

Si hace falta un globo de manga, que sea **redondo, fino, con la cola
corta**, como en el manga de Fujiko F. Fujio ⚠️ (sólo visto en miniatura: la
página de la hoja `objetos_01.jpg` n.º 81, y la línea limpia de
[«Gian manga.jpg»](https://static.wikia.nocookie.net/doraemon/images/a/a0/Gian_manga.jpg)),
nunca un rectángulo blanco con sombra.

### 7.4 En los videojuegos de la franquicia

- ***Doraemon Story of Seasons*** (Steam, **10 de octubre de 2019** ✅, con
  **español de Hispanoamérica** en la lista de idiomas): letra blanca sobre
  fondo oscuro en casi todo; en las escenas animadas, **letra negra sobre
  blanco**; **el nombre de quien habla siempre va encima** ✅
  ([Can I Play That?](https://caniplaythat.com/2019/10/28/mobility-review-doraemon-story-of-seasons/)).
  Capturas del cuadro de diálogo:
  [Interface In Game](https://interfaceingame.com/screenshots/doraemon-story-of-seasons-dialogue/)
  (no pude abrirla). En la segunda pasada hay **capturas de Steam en
  1920×1080** de los tres juegos, enlazadas en §13.
- ***Doraemon Story of Seasons: Friends of the Great Kingdom*** (2 de
  noviembre de 2022) ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Doraemon_Story_of_Seasons),
  [RPGFan](https://www.rpgfan.com/gallery/doraemon-story-of-seasons-friends-of-the-great-kingdom-screenshots/)).
- ***Doraemon Dorayaki Shop Story*** (Kairosoft; 27 de agosto de 2024 según
  la primera pasada, **8 de diciembre de 2024 en Steam** ⚠️ puede ser otra
  plataforma):
  **una tienda en pixel art** donde los inventos de Doraemon ayudan ✅
  ([Steam](https://store.steampowered.com/app/2934180/Doraemon_Dorayaki_Shop_Story/),
  [wiki de Kairosoft](https://kairosoft.wiki.gg/wiki/Doraemon_Dorayaki_Shop_Story)).
  Es **una tienda con estanterías**: sirve de idea para la lámina 2.

### 7.5 Qué NO hacer con el texto

- Nada de burbuja blanca genérica con sombra.
- No escribir «te-re-re-tte-tere» como sonido: es el error popular.
- No mezclar el logo de *Stand by Me* (Britannic, 3D) con dibujo de la
  serie de TV.
- No usar letras duras o de terror.

---

## 8 · Los personajes

Voces japonesas actuales (desde 2005): Doraemon **Wasabi Mizuta**, Nobita
**Megumi Ōhara**, Shizuka **Yumi Kakazu**, Gigante **Subaru Kimura**, Suneo
**Tomokazu Seki** ✅ ([eiga.com](https://eiga.com/movie/104573/),
[Wikipedia](https://ja.wikipedia.org/wiki/%E6%98%A0%E7%94%BB%E3%83%89%E3%83%A9%E3%81%88%E3%82%82%E3%82%93_%E6%96%B0%E3%83%BB%E3%81%AE%E3%81%B3%E5%A4%AA%E3%81%AE%E6%B5%B7%E5%BA%95%E9%AC%BC%E5%B2%A9%E5%9F%8E)).
Hasta 2005 Doraemon era **Nobuyo Ōyama**, que murió en 2024 a los 90 años ✅
([¡Hola!](https://www.hola.com/actualidad/20241015724196/doraemon-voz-actriz-doblaje-nobuyo-oyama-muere/),
[Diario Libre](https://www.diariolibre.com/revista/cine/2024/10/11/fallece-a-los-90-anos-la-actriz-de-doblaje-que-dio-voz-a-doraemon/2878191)).

### Doraemon — el protagonista, 1.º en todas las encuestas ✅

- **Qué es**: un **robot gato** del siglo XXII, modelo **MS-903** de la
  fábrica Matsushiba Robot ✅ ([Fandom](https://doraemon.fandom.com/wiki/Doraemon)).
  Nació el **3 de septiembre de 2112**; la fecha salió en CoroCoro en
  abril de 1975 ✅ ([nokikero](https://nokikero.com/dora-character-birthday/)). Mide **129,3 cm** y pesa **129,3 kg** ✅
  ([Precious](https://precious.jp/articles/-/62479),
  [Wikipedia JP](https://ja.wikipedia.org/wiki/%E3%83%89%E3%83%A9%E3%81%88%E3%82%82%E3%82%93_(%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC))).
- **Por qué es azul y no tiene orejas**: un **ratón robot** le mordió las
  orejas; lloró tanto que **se le cayó la pintura amarilla** y quedó azul ✅
  (película de 1995 *2112: el nacimiento de Doraemon*;
  [nokikero](https://nokikero.com/dora-blue-reason/), Precious).
- **Miedo**: **los ratones**. Huyendo de uno corre a 129,3 km/h ✅ (Precious).
- **Lo que le importa**: que Nobita salga adelante. Lo mandó **Sewashi**,
  el tataranieto de Nobita, para cambiar su futuro ✅ (*Stand by Me*
  00:05:47-00:08:54).
- **Cómo se expresa**:
  - **Presenta** con cortesía: «Buenas noches, soy Doraemon» (00:05:35) ✅.
  - **Se niega** en ráfaga: «¡Imposible, imposible, imposible!» (無理 無理
    無理, *Stand by Me* 00:09:51) ✅.
  - **Cede** con un suspiro: «ay, qué remedio» ✅.
  - **Presume** al sacar un invento: «¡Chan! Ya puedes estar tranquilo» ✅.
  - **Se ríe** con malicia suave: «nufufufu» (ヌフフフ, 00:14:46) ✅.
  - **Regaña**: «¡Si no puedes cumplir una promesa, no la hagas!»
    (*Stand by Me* 01:12:44) ✅.
  - **Anima**: «¡Chan! **Ya puedes estar tranquilo**» (でも もう 安心していいよ！,
    serie 2006-11-10 · 00:16:23) ✅.
- **Manías**: le encantan los **dorayaki** ⚠️ (lo dice la ficha de
  [AniList](https://anilist.co/character/4304); ninguna ficha oficial lo da
  como dato, es más un gag de siempre). Duerme en el **armario empotrado**
  del cuarto ✅. Lleva **cascabel amarillo en collar rojo**: en la película
  de 2013, sin él se porta como un gato cualquiera ✅ (Punto 25).
- **Con quién**: Nobita siempre; Dorami (su hermana); Sewashi.

### Nobita Nobi — el que pide

- Chico de primaria, torpe, dormilón. **Sus tres talentos**: **dormirse en
  0,93 segundos**, **puntería** (acierta cerca del 90 %) y **el juego de
  hilos** (ayatori) ✅
  ([futaman](https://futaman.futabanet.jp/articles/-/123052?page=1),
  [note · Fujiko F Note](https://note.com/shatoru0619/n/neee3d31f983d)).
- **Cómo se expresa**: llora y **grita el nombre de Doraemon** ✅; pide
  «¡haz algo!» ✅; se enfada fuerte y corto («¡Mentira! ¡Vete! ¡Vete!»,
  *Stand by Me* 00:07:46) ✅; saluda con risa tímida («jejeje, encantado»,
  00:10:35) ✅.
- **Qué le importa**: **Shizuka**; no quedar en ridículo delante de
  Gigante y Suneo; que lo dejen en paz. En el doblaje latino lo dice así:
  «**Quisiera estar en un pueblo libre donde nadie me molestara y pudiera
  ser lo que se me antojara**» («El Pueblo de Nobita», 1:34, transcrito con
  Whisper) ✅.
- **Cumpleaños**: **7 de agosto**; sale en el propio manga (CoroCoro, agosto
  de 1972, «El día en que nació Nobita») ✅ (nokikero,
  [oshiete.goo](https://oshiete.goo.ne.jp/qa/13493125.html), AniList).
- En la serie clásica lleva **camiseta roja**; la **amarilla** es de 2005
  (visto en «Un mundo sin dinero», 3:00) ✅.
- **Moraleja que la serie repite**: los inventos no bastan; al final tiene
  que hacerlo él ✅ (*Stand by Me* 00:26:42, «no depender de los inventos»).

### Shizuka Minamoto — la amable

- Buena alumna, amable, **defiende a Nobita** ✅ (*Stand by Me* 00:02:35).
- **Le gusta el violín pero lo toca mal**; **odia el piano pero lo toca
  bien**; le encantan **los boniatos** asados, y lo esconde ✅ (segunda
  pasada: [futaman / legend-anime](http://legend-anime.com/archives/315) y
  la ficha de [AniList](https://anilist.co/character/8260), «sweet
  potatoes… the violin, in which her playing is as atrocious as Gian's
  singing»).
- **Se baña varias veces al día** (de ahí el gag de Nobita entrando al baño
  por error); quiere ser **enfermera o azafata**; cuida muñecas, animales
  y a los débiles ✅ (AniList y
  [Fandom](https://doraemon.fandom.com/wiki/Shizuka_Minamoto)).
- **Cumpleaños**: **en mayo**. Sólo el mes es oficial (fijado en 1993 con el
  visto bueno de Fujiko F. Fujio); el «2 de mayo» que circula **no es
  oficial** ✅ (nokikero, con cita de *Neo Utopia* n.º 33, p. 168).
- **Ropa**: **top rosa y falda granate**, no un vestido rosa entero (medido,
  §16) ✅.
- Habla con educación: «Nobita-san», «Dora-chan» ✅.

### Gigante (Takeshi Gōda, «Gian» en japonés) — el matón que canta

- Nació el **15 de junio** ✅ (segunda pasada: lo dice el propio manga,
  CoroCoro de junio de 1980, «El cumpleaños de Gigante», según
  [nokikero](https://nokikero.com/dora-character-birthday/), y la ficha de
  [AniList](https://anilist.co/character/8262)). El matón del barrio, pero
  **no duda en ayudar a Nobita** cuando hace falta ✅ (AniList).
- Lleva **camiseta naranja** (`#F08E39` medido) y de béisbol una gorra con
  **«G»** (hoja `objetos_01.jpg`, n.º 62) ✅.
- **Le encanta cantar** y organiza **recitales en el descampado**, sin
  darse cuenta de que **canta fatal** ✅ (2006-09-08, 00:09:08 y 00:11:29).
- Su filosofía famosa, «**lo tuyo es mío y lo mío es mío**» (おまえのもの
  はおれのもの), **no la encontré en los subtítulos** que bajé ⚠️. En la wiki
  en español aparece como «**Lo mío es mío, y lo tuyo también**», dentro de
  una canción ⚠️ ([Doraenciclopedia](https://doraemon.fandom.com/es/wiki/El_d%C3%BAo_prodigioso:_Giga_y_Sune));
  parece del doblaje de España, no del latino.
- En el doblaje latino Gigante **canta canciones de verdad**: «Historia de
  taxi» de Ricardo Arjona en el episodio «Tecnología avanzada» (LTN 26-B /
  original 0077), y en otra escena «Si las gotas de lluvia fueran
  dulces» de *Barney* ⚠️ (ahora leído en el wikitext de
  [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Doraemon_(1979)), «Datos
  de interés», pero sigue siendo una sola fuente).

### Suneo Honekawa — el que presume

- Rico, **presume de todo** (juguetes, viajes, comida) y va detrás de
  Gigante ✅ (2006-06-23 y *Stand by Me* 00:01:50: «¡Qué cansancio, tres
  días seguidos de filete!») ✅.
- **Qué NO hacer**: dibujarlo sin su **pelo en punta** hacia atrás ✅ (se ve
  en su retrato oficial y en la hoja `personajes_01.jpg`/`objetos_01.jpg`,
  n.º 44-53).
- **Es el más bajo de la clase** y lo vive como un complejo ✅ (el manga
  varias veces y fichas en japonés). Cara «de zorro», heredada de su madre;
  sabe mucho de ciencia y **dibuja y diseña bien**; se mira al espejo y se
  dice lo guapo que es ✅ (AniList y
  [Fandom](https://doraemon.fandom.com/wiki/Suneo_Honekawa)).
- Invita a Gigante y a Shizuka **y deja fuera a Nobita** con una excusa ✅
  (las mismas dos fuentes).
- **Cumpleaños**: **en febrero** (sólo el mes es oficial; el «18 de
  febrero» sale de un móvil en *Stand by Me* y la franquicia no lo adoptó)
  ✅ (nokikero).
- **Suéter verde azulado** `#27B585` (medido, §16) ✅.

### Dorami — la hermana (la secundaria más querida) ✅

- **Hermana pequeña** de Doraemon, también robot gato. **Amarilla** (el
  color que Doraemon tenía al principio), con un **lazo rojo** en la cabeza.
  Mide **100 cm**, pesa **91 kg**, nació el **2 de diciembre de 2114** ✅
  ([Honcierge](https://honcierge.jp/articles/shelf_story/6096),
  [pixiv](https://dic.pixiv.net/a/%E3%83%89%E3%83%A9%E3%83%9F),
  [futaman](https://futaman.futabanet.jp/articles/-/130585?page=1)).
- **Más capaz que su hermano**: seria, ordenada, **la que resuelve**. Le
  encanta el **pan de melón** (melonpan). Canta, cocina, lleva la casa ✅.
- Su máquina del tiempo tiene **forma de tulipán** ✅.
- En la película de 2013 aparece con él y le pregunta por qué le importa
  tanto el cascabel (00:10:22) ✅.
- **Para este canal encaja muy bien**: es la **ordenada**, la que sabe dónde
  está cada invento. **Buena para la lámina 2** (las etiquetas).
- **Voz latina** (segunda pasada, Doblaje Wiki por la API) ✅: **María
  Fernanda Morales** en el doblaje de 1999-2011 (Rebeca Gómez en el ep.
  477) y **Lupita Leal** en el de 2014-2015 (§10).

### Otros

- **Dekisugi**: el listo de la clase; **4.º** entre los de 20-30 años ✅ (§9).
  Guapo, deportista y listo, el rival de Nobita por Shizuka; su nombre es un
  juego de palabras, «demasiado capaz» ✅ ([AniList](https://anilist.co/character/31870)).
  Voz latina: **Miguel Ángel Leal** (2014) y **Bruno Coronel** (4.ª
  temporada clásica y Netflix) ✅ (§10).
- **Sewashi**: el tataranieto de Nobita que manda a Doraemon ✅.

### Su cara en cada emoción (con minuto) — segunda pasada

Reordenado por el investigador de voz con **minutos ya comprobados**
(subtítulos de §2) y lo **visto** en 7 episodios de Internet Archive
(fotogramas cada 3 s, unos 45 minutos de metraje). Casilla vacía = no
encontrado con minuto; no se inventa.

| Personaje | Alegría | Rabia | Tristeza | Miedo | Vergüenza |
|---|---|---|---|---|---|
| **Doraemon** | risita «nufufu», *Stand by Me* 00:14:46 ✅ | — no apareció enfadado en ninguno de los 7 episodios ⚠️ | — | «¡Me robaron el cascabel!», museo 00:03:49 ✅; cara de susto corriendo, ep. «Las tabletas de Komon» 2:51-2:57 ✅ | — |
| **Nobita** | «¡Gracias, gracias, Doraemon!», *Stand by Me* 00:42:57 ✅ | «¡Mentira! ¡Vete!», *Stand by Me* 00:07:46 ✅ | **llora tapándose la cara**, su papá lo abraza, «Un mundo sin dinero» [3:00-3:09](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%20184%20-%20El%20indicador%20del%20desorden%20.mp4?t=180) ✅ visto | «¡Haz algo, Doraemoon!», 2005-08-05 · 00:10:02 ✅ | — |
| **Shizuka** | «¡Qué divertido!», *Stand by Me* 00:00:45 ✅ | se planta: «¡Paren los dos!», *Stand by Me* 00:02:35 ✅ (firmeza) | — | — | — |
| **Gigante** | «¡Empieza el recital!», 2006-09-08 · 00:11:29 ✅; recital visto en [0:20](https://www.dailymotion.com/video/x3402n2?t=20) | «¡Nobita, qué te crees!», 2006-11-10 · 00:08:58 ✅; «Gian mad», hoja n.º 28 | — | cejas en zigzag, [0:10](https://www.dailymotion.com/video/x2uugoz?t=10) ⚠️ película sin identificar | — |
| **Suneo** | presume del filete, *Stand by Me* 00:01:50 ✅ | — | — | — | ser el más bajo es su complejo, pero **sin escena con minuto** ⚠️ |

**Huecos que quedan** ⚠️: la rabia de Doraemon; la tristeza de Doraemon,
Shizuka, Gigante y Suneo; la vergüenza de todos. Suneo no salió en ninguno
de los 7 episodios mirados. Candidatos sin mirar del mismo ítem de Internet
Archive: episodios 153, 172, 182 y 194. Para vergüenza también sirven las
imágenes de la wiki con nombre de emoción, sin minuto: «Shizuka angry»,
«Shizuka amazed shocked», «Nobita Shizuka Suneo scared», «Sadness Nobita
Shizuka Suneo» (2048×1536, en `referencias.json`).

**Dinámicas** (quién con quién): Nobita pide y Doraemon cede («ay, qué
remedio»); Gigante manda y Suneo le hace coro, pero **le teme** (AniList);
Suneo presume y deja fuera a Nobita; Shizuka defiende a Nobita y regaña a
los dos; Dorami resuelve lo que su hermano no ✅.

---

## 9 · ¿Quién es el más querido?

| Encuesta | Resultado |
|---|---|
| **Mynavi News, marzo de 2025**, 301 personas, **20 a 30 años** | 1.º **Doraemon** (40,3 %) · 2.º **Dorami** (12,3 %) · 3.º Nobita (11,5 %) · 4.º Dekisugi (5,5 %) · 5.º Shizuka y Sewashi (3,2 %) ✅ ([Mynavi](https://news.mynavi.jp/article/20250329-doraemon_2030/)) |
| Mynavi, 40 a 50 años | Doraemon y Nobita delante ⚠️ ([Mynavi](https://news.mynavi.jp/article/20250329-3162715/)) |
| **Nlab (ITmedia), 2022**, 1.425 votos | 1.º **Doraemon** ✅ ([Nlab](https://nlab.itmedia.co.jp/research/articles/666418/)) |
| ranking.net (votación abierta) | 1.º Doraemon · 2.º Dorami · 3.º Nobita ⚠️ ([ranking.net](https://ranking.net/rankings/best-doraemon-characters), [cmoasemi](https://cmoasemi.com/mannga-dorae-rannkinngu/)) |
| Macromill, 2023, adultos | «El favorito de los hombres: **Doraemon**» ✅ ([note de Macromill](https://note.com/macromill/n/nd91b9d5d17dd)) |

| **AniList** (favoritos de usuarios, internacional; segunda pasada) | 1.º **Doraemon** (687) · 2.º Nobita (189) · 3.º Shizuka (94) · 4.º Suneo (47) · 5.º Gigante (40) · 6.º Dekisugi (10) ✅ ([AniList](https://anilist.co/anime/501)). Dorami no aparece en la ficha de esta serie |
| **Reddit r/Doraemon** (segunda pasada, por Arctic Shift) | hilos con más votos: «Feliz cumpleaños a mi favorito, **Nobi Nobita**» (213 votos) y «¿Hay una razón para que **Suneo** sea mi favorito?» (81 votos, 30 comentarios) ⚠️ subreddit poco activo ([Reddit](https://www.reddit.com/r/Doraemon/comments/1vi893s/happy_birthday_my_favorite_character_nobi_nobita/)) |

**Conclusión**: aquí **el protagonista sí es el más querido**. La sorpresa
es **Dorami**, que en los jóvenes japoneses **supera a Nobita**. Fuera de
Japón (AniList, Reddit), el segundo es **Nobita**.

**Premio oficial**: en **marzo de 2008** el Ministerio de Asuntos Exteriores
de Japón nombró a Doraemon **primer «embajador anime»** del país ✅
([comunicado oficial](https://www.mofa.go.jp/announce/announce/2008/3/0319-3.html),
[Anime News Network](https://www.animenewsnetwork.com/news/2008-03-14/doraemon-to-be-japan-first-anime-ambassador),
[CBC](https://www.cbc.ca/news/entertainment/robot-cat-becomes-japan-s-first-anime-ambassador-1.728930)).

**Los inventos más queridos** (sirve para elegir qué objetos poner):
- **El más deseado**: la **puerta a cualquier lugar** (どこでもドア); 2.º
  la máquina del tiempo; 3.º la cabina «¿Y si…?» (もしもボックス) ✅
  ([Nlab 2021](https://nlab.itmedia.co.jp/research/articles/284303/),
  [ranking.net](https://ranking.net/rankings/best-doraemon-tools)).
- **El que más sale** en las películas: el **Takecopter** (la hélice de la
  cabeza), y después la puerta ✅
  ([Bookoff](http://pro.bookoffonline.co.jp/entertainment/entertainment-low/20150519_doraemon-himitudougu.html),
  [@DIME](https://dime.jp/genre/878477/)).
- Hay **más de 1.900 inventos** (una wiki dice 2.332; las cifras cambian
  según qué se cuente) ⚠️
  ([pixiv](https://dic.pixiv.net/a/%E3%81%B2%E3%81%BF%E3%81%A4%E9%81%93%E5%85%B7)).

---

## 10 · Doblaje latino

> **Segunda pasada**: ya se leyó **la API de Doblaje Wiki** (wikitext
> completo de *Doraemon (1979)*, *Doraemon (2005)* y *Quédate conmigo,
> Doraemon*) y la de [Dubbing Database](https://dubdb.fandom.com/wiki/Doraemon,_el_gato_c%C3%B3smico_(2005,_Latin_American_Spanish)).
> Marco ✅ lo que coincide en **dos fuentes distintas**.

### 10.1 Las épocas del doblaje latino

| Época | Qué | Datos |
|---|---|---|
| **1981-1982** | Primer doblaje, en Los Ángeles, emitido como *Las aventuras del gato cósmico*; casi perdido | Estudio ESM (Sonomex), dirección **Alejandro Byrd** ⚠️. **Doraemon y Gigante: Carlos Carrillo** (el mismo actor para los dos), Nobita **Gladys Parra**, Shizuka **Gloria González**, Tamako **Carmina Vásquez**; Suneo sin identificar ✅ (tabla «Original» de [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Doraemon_(1979)) y [Lost Media Wiki](https://lostmedia.fandom.com/es/wiki/Las_aventuras_del_gato_c%C3%B3smico_(primer_doblaje_latino_parcialmente_encontrado;_1980s))) |
| **1985** | **Doblaje cubano** del **ICAIC** de la película *Doraemon en la tierra secreta* (en España, *Doraemon y el mundo perdido*) | hallazgo nuevo ⚠️ (una fuente: [Internet Archive](https://archive.org/details/doraemon-en-la-tierra-secreta-doblaje-cubano-icaic-1985)); sin nombres de actores |
| **1999-2011** | ***Doraemon, el gato cósmico*** (serie de 1979), Rose Entertainment, México. El que conoce casi todo el mundo. **312 medias horas** dobladas en 6 tandas | tabla de §10.2 ✅ |
| **2014-2015** | Serie de **2005**, **Art Sound México**, grabada del 23-jun-2014 al 8-abr-2015 (eps. 1-104) | dirección **Armando Coria** ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Doraemon_(2005)), [ANMTV 2014](https://www.anmtvla.com/2014/06/doraemon-comienza-doblaje-para.html?m=0)); tabla de §10.3 |
| **2021-2022** | ***Quédate conmigo, Doraemon*** 1 y 2, Netflix | **New Art Dub**, dirección **Irwin Daayán**, traducción **Jennifer Medel** ✅ (antes decía «Mendel»: el wikitext dice `Jennifer Medel`, letra por letra) |

Dónde se vio la serie de 2005: Netflix (10-dic-2014 a 10-jun-2016),
Ecuavisa y ETC TV (2015), Teleamazonas (2017), Azteca 7 (2018), CityTV
Colombia (2020), Senpai TV (2023) ✅ (Dubbing Database). La clásica salió en
Chile por Chilevisión (2000-2007) ⚠️.

### 10.2 *El gato cósmico* (1999-2011): dos etapas ✅

Wikitext de Doblaje Wiki, con actor por temporada y episodio; los nombres
principales coinciden con [dubdb](https://dubdb.fandom.com/wiki/Doraemon,_el_gato_c%C3%B3smico_(1979,_Latin_American_Spanish))
y [ANMTV](https://www.anmtvla.com/).

| Personaje | Primera etapa (temporadas 1.ª-3.ª) | Segunda etapa (4.ª) |
|---|---|---|
| **Doraemon** | **Ricardo Tejedo** | **Irwin Daayán** |
| **Nobita** niño | **Laura Torres** (hasta ~ep. 484-563) → **Ariadna Rivas** (eps. 387-472 y 564-585) | **Rommy Mendoza** |
| Nobita mayor | Gerardo del Valle (preadolescente, ep. 45), Manuel Campuzano (adolescente), **Yamil Atala** (adulto, 2.ª-3.ª) | Héctor Emmanuel Gómez |
| **Shizuka** | **Cristina Hernández** (Vanessa Garcel en eps. 397 y 563) | Cristina Hernández |
| **Suneo** | **Irwin Daayán** | Irwin Daayán |
| **Gigante** | **Luis Daniel Ramírez** | Luis Daniel Ramírez |
| **Dorami** | **María Fernanda Morales** (Rebeca Gómez, ep. 477) | — |
| Tamako | — | Rebeca Manríquez |
| Dekisugi | — | Bruno Coronel |

- **Corrección**: antes decía «luego lo dobló Rommy Mendoza ⚠️». Fueron
  **tres**: Laura Torres → Ariadna Rivas → Rommy Mendoza ✅.
- **Por qué se fue Laura Torres**: tenía la garganta lastimada de tantos
  años haciendo a Goku, Gohan y Goten niños en *Dragon Ball*, y dejó de
  doblar niños un tiempo ✅ (Doblaje Wiki y dubdb). Ariadna Rivas
  **renunció después junto con Ricardo Tejedo**, «por compromisos» ⚠️ (sólo
  Doblaje Wiki).
- **Irwin Daayán dobló a Suneo en todo el doblaje clásico y pasó a ser
  Doraemon** en la 4.ª temporada, y desde 2014 hasta hoy ✅. **El dato
  perfecto para un servidor de doblaje**: del rival presumido al
  protagonista.

### 10.3 Serie de 2005 (Art Sound México, 2014-2015) ✅

Wikitext de [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Doraemon_(2005))
y [Dubbing Database](https://dubdb.fandom.com/wiki/Doraemon,_el_gato_c%C3%B3smico_(2005,_Latin_American_Spanish)):

| Personaje | Voz latina |
|---|---|
| **Doraemon** | **Irwin Daayán** |
| **Nobita** | **Laura Torres** (volvió) |
| **Shizuka** | **Cristina Hernández** |
| **Suneo** | **Irwin Daayán** |
| **Gigante** | **Luis Daniel Ramírez** |
| **Dorami** | **Lupita Leal** |
| Sewashi | Laura Torres |
| Tamako (mamá de Nobita) | Adriana Casas |
| Nobisuke (papá de Nobita) | Agustín López Lezama |
| Dekisugi | Miguel Ángel Leal |
| Profesor | Jorge Ornelas |
| Jaiko (Gigantita) | Rebeca Gómez |

Nobita con Laura Torres también lo confirma un vídeo de la propia
[Laura Torres](https://www.tiktok.com/@lau_tor_oficial/video/7270311149307055366) ✅.
Las **104 medias horas** ya salen en la ficha ✅ (antes ⚠️).

### 10.4 Reparto de las películas de Netflix ✅

Coinciden el wikitext de [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Qu%C3%A9date_conmigo,_Doraemon),
[ANMTV](https://www.anmtvla.com/2022/02/quedate-conmigo-doraemon-ya-dispone-de.html),
[TVLaint](https://www.tvlaint.com/2022/02/netflix-agrega-doblaje-latino-de.html),
[Desde la Cuna](https://www.desdelacuna.net/doblaje/voces-quedate-conmigo-doraemon-2-pelicula-netflix-doblaje-actores-elenco-personajes-reparto/)
y [FUNiAnime](https://funianime.com/quedate-conmigo-doraemon2-anuncia-fecha-de-estreno-en-latinoamerica/):

| Personaje | Voz latina |
|---|---|
| **Doraemon** | **Irwin Daayán** |
| **Nobita** (niño) | **Laura Torres** |
| Nobita adulto | **Miguel Ángel Ruiz** ✅ (antes ⚠️) |
| **Shizuka** | **Cristina Hernández** |
| **Gigante** | **Abraham Vega** |
| **Suneo** | **Irwin Daayán** (el mismo actor que Doraemon) |
| Sewashi | Sebastián García |
| Tamako | Yolanda Vidal |
| Nobisuke | Carlos del Campo |
| Dekisugi | Bruno Coronel |
| Jaiko | Cassandra Valtier |
| Sra. Goda | Jahel Morga |
| Profesor | Jorge Ornelas |

(Los secundarios, sólo del wikitext ⚠️.)

- En Latinoamérica **Doraemon siempre lo ha doblado un hombre** (Carrillo,
  Tejedo, Daayán); en Japón, mujeres (Ōyama, Mizuta) ✅ (las tablas de
  arriba y §8).
- **«El gato cósmico»** es la marca de la serie en Latinoamérica, y en el
  doblaje **a Doraemon le dicen «Cósmico»** de apodo. Ahora leído en los
  «Datos de interés» del wikitext ✅ (Doblaje Wiki), y el opening latino
  antiguo lo canta en 0:13: «**Doraemon, el gato cósmico**» ([Dailymotion](https://www.dailymotion.com/video/x8k1ck8?t=13),
  transcrito con Whisper) ✅.

### 10.5 Nombres latinos de los inventos

Ahora leído en los «Datos de interés» del wikitext de Doblaje Wiki (una
wiki, pero leída entera, no por el buscador) ⚠️:
- Al principio **«bolsillo mágico»** y **«puerta mágica»**, como en España.
  Después, **«bolsillo tetradimensional»** y **«puerta a donde sea / a
  cualquier lugar»**.
- El Takecopter se llamó **«gorrocóptero»**, **«coco-cóptero»** y
  **«cabeza-cóptero»** en la 1.ª temporada.
- El Sr. Kaminari pasó a ser **«Señor Kobayashi»**, quizá por su actor,
  Gabriel Cobayassi.
- El primer opening latino se grabó con **la misma letra que el de
  España**; luego se grabó otra versión con otra adaptación (§11).
- «**Bolsillo mágico**» está confirmado en el **opening latino**: «Doraemon,
  con su bolsillo mágico, los hace realidad por mí» ✅
  ([Doraenciclopedia](https://doraemon.fandom.com/es/wiki/Canci%C3%B3n_de_Doraemon),
  [cancioneros.com](https://www.cancioneros.com/lyrics/song/1989807/opening-doraemon-el-gato-cosmico-espanol-latino-doraemon)).

**Para la lámina**: «**bolsillo mágico**» es el nombre que reconoce todo
latino. No uses «bolsillo tetradimensional» en el texto principal.

Otros nombres: una publicación de TikTok dice que en un doblaje mexicano muy
antiguo se llamaron **Robotín, Felipe, Andrea, Enrique y Cantimplora**. Una
sola fuente: **no usar** ⚠️.

### 10.6 Frases del doblaje latino, textuales (segunda pasada)

Antes: «no encontré ninguna». Ahora hay frases **sacadas del audio**: el
episodio **«El Pueblo de Nobita»**, con doblaje latino de una grabación de
TV ([Internet Archive](https://archive.org/details/episodio-737-chip-de-reservacion),
colección *Doraemon Español, episodios 01-300*), pasado por `voz.py`
(Whisper) y revisado a oído. Por la numeración es casi seguro el doblaje de
**Rose Entertainment (1999-2011)** ⚠️; Whisper no distingue voces, así que
**quién dice cada frase** va con ⚠️ salvo la de Nobita.

| Minuto | Frase textual | Quién | Emoción |
|---|---|---|---|
| [0:54](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=54) | «¡Oigan! Si no tienen nada que hacer, ¿por qué no vienen a jugar pelota conmigo?» | por el contexto, Gigante ⚠️ | mandón |
| [1:19](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=79) | «¡Eso duele! ¿Acaso crees que tengo la cabeza de piedra?» | sin confirmar ⚠️ | queja tras un golpe |
| [1:34](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=94) | «Quisiera estar en un pueblo libre donde nadie me molestara y pudiera ser lo que se me antojara» | **Nobita** ✅ (es el deseo que arranca el episodio) | triste, soñador |

Y del **opening latino antiguo** ([Dailymotion](https://www.dailymotion.com/video/x8k1ck8?t=13)):
0:13 «**Doraemon, el gato cósmico**» y 0:16 «**Ojalá mi sueño se…**» ✅.

**Cómo suena el doblaje clásico** (`voz.py`, varias voces de niño juntas):
tono medio **375 Hz** (muy agudo), **22,9 semitonos** de rango (muy
expresivo), **2,12 palabras por segundo** ✅. Agudo y exagerado, nunca plano.

Las frases de §2 y §7 siguen siendo del **japonés**, traducidas por mí. Las
latinas de Nobita y Doraemon más famosas («¡Doraemon, haz algo!», «ay, qué
remedio») **no se encontraron en un clip latino con minuto** ⚠️: las muestras
de audio de Doblaje Wiki no salieron en esta ficha.

## 11 · Música

| Tema | Datos | Ambiente |
|---|---|---|
| **Opening latino «Doraemon, el gato cósmico»** | versión de «Doraemon no Uta», cantada por **Maggie Vera** ✅ ([Doraenciclopedia](https://doraemon.fandom.com/es/wiki/Canci%C3%B3n_de_Doraemon); vídeos [V1](https://www.youtube.com/watch?v=vF-PDfmOdfo) y [V2](https://www.youtube.com/watch?v=Gb_KCQGHYQU)). Letra: «**Shalalalala, en mi corazón / mis sueños siempre brillarán sin fin / Doraemon / con su bolsillo mágico / los hace realidad por mí**» ✅ | alegre, infantil, nostalgia pura para Latinoamérica |
| «**Doraemon no Uta**» (ドラえもんのうた) | el tema clásico de la serie de 1979; lo cantaron varias artistas ✅ ([Columbia](https://columbia.jp/prod-info/COCX-35911-2/)) | el sonido de «Doraemon» para cualquiera |
| «**Hug Shichao**» (ハグしちゃお) | Rimi Natsukawa ✅ (Columbia) | primer opening de la serie de 2005 ⚠️ |
| «**Yume wo Kanaete Doraemon**» (夢をかなえてドラえもん) | **mao**, opening de **2007 a 2019**. **Su letra nombra inventos** ✅ ([Columbia](https://columbia.jp/doraemonthemesong/), [Wikipedia JP](https://ja.wikipedia.org/wiki/%E5%A4%A2%E3%82%92%E3%81%8B%E3%81%AA%E3%81%88%E3%81%A6%E3%83%89%E3%83%A9%E3%81%88%E3%82%82%E3%82%93)) | la canción de «pedir un deseo» |
| «**Doraemon**» (ドラえもん) | **Gen Hoshino**, para las películas ✅; opening de TV desde 2019 ⚠️ | moderna, con metales |

Recopilación de 62 temas de la franquicia:
[DIGLE MAGAZINE](https://mag.digle.tokyo/sch/news/ranking/popular/75022).

**Segunda pasada: el opening latino, oído de verdad.** El opening de 1979
con doblaje latino antiguo de [Dailymotion](https://www.dailymotion.com/video/x8k1ck8?t=13)
se pasó por `voz.py` (Whisper): en **0:13** canta «**Doraemon, el gato
cósmico**» y en **0:16** «**Ojalá mi sueño se…**» ✅. Es **otra letra** con
la misma música que la de Maggie Vera citada arriba. Doblaje Wiki explica
por qué: el **primer opening latino se grabó con la letra de España**, y
luego se grabó otra versión con otra adaptación ✅ (wikitext, «Datos de
interés»). **Cuál es cuál y quién canta la del vídeo** ⚠️: no sale en el
vídeo ni en su ficha. La voz: registro medio (183 Hz), muy expresiva (31,3
semitonos), lenta (1,59 palabras por segundo).

| Más temas (segunda pasada) | Datos |
|---|---|
| Ending latino de *El gato cósmico*, con **Maggie Vera** | [YouTube, 178 732 vistas](https://www.youtube.com/watch?v=lLZX4c8wOBQ) ✅ |
| «**Nuestro Planeta**» (ぼくたち地球人, *Bokutachi Chikyūjin*), ending oficial en latino | [YouTube, canal Doraemon Latino](https://www.youtube.com/watch?v=eljPM34kWmE) ✅ |
| «**Himawari no Yakusoku**», tema de *Stand by Me Doraemon* | suena en la película que hizo llorar al 88,4 % (Punto 21); en qué escena exacta, sin ver ⚠️ |
| Discos de banda sonora | *Doraemon Encyclopedia* (1995), *Doraemon Sound Track History 2* (Kan Sawada, 2010), *DORA THE BEST* (20.º aniversario, 1999) ([MusicBrainz](https://musicbrainz.org/release-group/f7c47f81-3066-4f32-9ab2-669541881072)) ✅ |

**Efectos que todos reconocen**: el sonido de **sacar un invento** (§7.1) y
el «¡Doraemooon!» de Nobita (§7.1). AnimeThemes, que tiene los openings en
vídeo limpio, dio **error 522** todo el día ⚠️.

> **Ojo para el canal**: en #recursos no se pueden colgar las canciones de
> Doraemon como «pista sin voz» ni «música libre»: **tienen derechos**. Es
> justo el ejemplo de lo que NO va.

---

## 12 · Vídeos

| Vídeo | Enlace | Para qué |
|---|---|---|
| Tráiler oficial latino de *Quédate conmigo, Doraemon: 2* | [YouTube UNMulZxlpZ8](https://www.youtube.com/watch?v=UNMulZxlpZ8) | oír a Irwin Daayán y Laura Torres |
| Tráiler 2 de *Quédate conmigo, Doraemon* en español (no sé si latino o de España ⚠️) | [YouTube IWmYJA9D6pg](https://www.youtube.com/watch?v=IWmYJA9D6pg) | la luz 3D del cuarto |
| **El sonido de sacar un invento, antes y ahora** | [YouTube 8PCLcvDnuh0](https://www.youtube.com/watch?v=8PCLcvDnuh0) | ver la pose y el fondo del momento del invento |
| Recopilación de openings «Yume wo Kanaete Doraemon» | [YouTube bDZIJRRHyFc](https://www.youtube.com/watch?v=bDZIJRRHyFc) | poses de grupo |
| Opening latino (Maggie Vera) | [V1](https://www.youtube.com/watch?v=vF-PDfmOdfo) | el tono latino |
| Todas las voces latinas de Doraemon | [TikTok @sengek56](https://www.tiktok.com/@sengek56/video/7500317759486561542) | comparar voces |

> ⚠️ YouTube siguió sin poder verse en la segunda pasada (pide iniciar
> sesión): **estos vídeos van sin minuto**. Los vídeos **mirados** con
> minuto están en §2.4 (Dailymotion e Internet Archive):

| Vídeo mirado | Enlace con minuto | Qué sirve |
|---|---|---|
| Opening 1979 latino antiguo | [0:40](https://www.dailymotion.com/video/x8k1ck8?t=40) | Doraemon volando con el Takecopter sobre bocetos de Da Vinci |
| Tráiler en español de *Stand by Me* | [0:30](https://www.dailymotion.com/video/x33a56v?t=30) · [1:00](https://www.dailymotion.com/video/x33a56v?t=60) | el cuarto 3D de día y de noche |
| Recital de Gigante | [0:20](https://www.dailymotion.com/video/x3402n2?t=20) | la pose con micrófono |
| «El Pueblo de Nobita», doblaje latino | [3:00](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=180) | un invento en uso |
| Tráiler de *Doraemon el gladiador* en español (FilmAffinity) | [Dailymotion](https://www.dailymotion.com/video/x9d5trc) ⚠️ sin mirar | película reciente |
| *Doraemon Traffic Safety* (1981), restauración de 16 mm | [Internet Archive](https://archive.org/details/doraemon-traffic-safety-16mm) ⚠️ sin mirar | corto educativo; una rareza |

**Tendencias**: los *fandubs*, parodias y covers en español, con vistas,
están en el Punto 22. TikTok sigue sin poder medirse ⚠️.

---

## 13 · Videojuegos de la franquicia

Resumido en §7.4. Lo útil para el canal:

- ***Doraemon Dorayaki Shop Story*** (Kairosoft, 2024): **una tienda**. Idea
  para la lámina 2: estanterías con un producto por etiqueta.
- ***Doraemon Story of Seasons*** (2019) y ***Friends of the Great
  Kingdom*** (2022): dibujo **de acuarela**, suave, con agua muy trabajada
  (reflejos, ondas), salvo los retratos y las escenas animadas ✅ (segunda
  pasada: [switchaboo](https://www.switchaboo.com/doraemon-story-of-seasons-switch-review-2/)
  y [Can I Play That?](https://caniplaythat.com/2019/10/28/mobility-review-doraemon-story-of-seasons/)),
  con el **nombre de quien habla** encima del cuadro ✅. Los dos traen
  **español de Hispanoamérica** en Steam ✅.
- **Capturas oficiales de Steam en 1920×1080** (para ver el cuadro de
  diálogo y los menús; en `referencias.json`):
  [Story of Seasons](https://store.steampowered.com/app/965230) (6),
  [Friends of the Great Kingdom](https://store.steampowered.com/app/1492730) (6)
  y [Dorayaki Shop Story](https://store.steampowered.com/app/2934180) (6).
  Ejemplo: [captura de *Story of Seasons*](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/965230/ss_c6c598c4ee381645e9b419996197adfef8566596.1920x1080.jpg).
  No las abrió nadie una por una ⚠️: cuál trae un cuadro de diálogo, sin
  comprobar.
- Colaboración con el gacha ***Granblue Fantasy*** (diciembre de 2021):
  Doraemon y Nobita jugables (Punto 23).
- Lista de juegos: [Wikipedia](https://en.wikipedia.org/wiki/List_of_Doraemon_video_games).

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen

- **Sacar un invento del bolsillo** y el nombre en voz alta ✅.
- «**¡Doraemooon!**» de Nobita y el «**qué remedio**» de Doraemon ✅.
- **El recital de Gigante** en el descampado ✅, y en el latino, Gigante
  cantando «Historia de taxi» de Arjona ⚠️ (§8).
- **«Handsome Gian»**, la cara de Gigante «guapo», un meme con imagen de
  5016×2822 en la wiki (hoja `personajes_01.jpg`, n.º 1) ✅.
- **La puerta a cualquier lugar** (el invento más deseado) ✅.
- **El miedo de Doraemon a los ratones** ✅ y **los dorayaki** ⚠️.
- **«El gato cósmico»** y el opening de Maggie Vera, pura nostalgia latina ✅.
- **Dorami** y su pan de melón ✅.
- **«ドラ泣き» (Dora-naki, «el llanto de Doraemon»)**: casi un meme oficial
  en Japón desde *Stand by Me* (2014); la revista de cine
  [Cinematoday](https://www.cinematoday.jp/page/A0004197) hizo una votación
  pública sobre en qué escena lloró cada quien ✅ (Punto 21).
- **Irwin Daayán, de Suneo a Doraemon** (§10.2): el dato del doblaje que más
  gusta a los fans hispanos ✅.
- **Nobita no es un fracaso a secas**: el hilo más votado de r/Doraemon en
  la búsqueda de favoritos le desea feliz cumpleaños (213 votos); y hay
  quien defiende a Suneo (81 votos) ⚠️ (Reddit poco activo).

### Qué NO hacer (lo que un fan notaría)

- **No dibujar orejas** a Doraemon, ni hacerlo amarillo (amarilla es
  Dorami) ✅.
- **No darle dedos**: sus manos son bolas, la «**Petari Hand**» (ペタリハンド),
  que **pega** las cosas por succión ✅
  ([mirai-hikidashi](https://mirai-hikidashi.com/archives/218),
  [COROBUZZ](https://corobuzz.com/archives/29538)).
- **Flota 3 mm sobre el suelo** (por eso no lleva zapatos) ✅
  ([Mynavi Woman](https://woman.mynavi.jp/article/130722-079/),
  [cocorety](https://cocorety.net/entame/130028.html)). La historia de que
  fue «por una queja de la asociación de padres» es **un bulo** ⚠️
  ([nota de TOKAS](https://note.com/tokasimnet/n/nb61d36f13942)).
- **No confundir el bolsillo**: es una **media luna blanca** en la barriga ✅
  (visto: hoja `objetos_01.jpg`, n.º 58, y el retrato oficial). El de
  **Dorami** lleva **rayas rojas cruzadas**: así se distinguen ✅
  ([Fandom · 4D Pocket](https://doraemon.fandom.com/wiki/4D_Pocket)).
- **El cascabel** es amarillo (`#FCDC2A` medido), redondo, en collar rojo
  (`#E02333`) ✅; la raya y la ranura, sin medir de cerca ⚠️. Sin él Doraemon
  se porta como un gato normal (la película de 2013 va de eso) ✅.
- **No le quites el «Poko»**, el bultito en la comisura del labio: «sin esto
  no se puede hacer un personaje de Fujiko», dice el director de arte de
  *Stand by Me* ✅ ([CGWorld](https://cgworld.jp/interview/1408-sbmd.html);
  Punto 18).
- **No vistas a Shizuka de rosa entera**: top rosa, **falda granate** ✅ (§16).
- **No tocar la «leyenda del final»** (que Nobita está en coma y todo es un
  sueño): es falsa, **la editorial la desmintió** ⚠️. El final real que
  se repite es otro: *Adiós, Doraemon…* (Doraemon vuelve al futuro y Nobita
  decide seguir solo) ✅ ([Doraenciclopedia](https://doraemon.fandom.com/es/wiki/Adi%C3%B3s%2C_Doraemon...))
  ([TikTok](https://www.tiktok.com/discover/cap%C3%ADtulo-final-de-doraemon));
  un fan la reconoce y le parece de mal gusto en un Discord alegre.
- **No mezclar estilos**: el 3D de *Stand by Me* y el dibujo plano de la
  serie no van juntos en la misma lámina.
- **No usar el falso «te-re-re-tte-tere»** ✅.
- **No poner a Doraemon a regalar programas pirata**: en la serie los
  inventos **se compran o se alquilan** en la tienda del futuro ✅. Encaja
  con la regla del canal.

---

## 15 · Poses analizadas por personaje

> [!warning] Cómo está hecho este apartado
> Las tablas por personaje son de la primera pasada: cada pose sale de **lo
> que dice el subtítulo en ese minuto**, y la postura se **deduce** ⚠️. Los
> minutos sí están comprobados en el archivo ✅. **La segunda pasada añade
> poses VISTAS** (§15.0, fotogramas abiertos uno a uno) y poses de las hojas
> de contacto (§15.1).

### 15.0 Poses vistas en vídeo (segunda pasada) ✅

| Personaje | Fotograma visto | Postura (lo que se ve) | Sirve para |
|---|---|---|---|
| **Doraemon** | [opening 0:40](https://www.dailymotion.com/video/x8k1ck8?t=40) | vuela con el Takecopter, **brazos abiertos**, sonrisa grande, cuerpo inclinado hacia delante | **explicar**: enseñar un invento en movimiento |
| **Doraemon** | [tráiler 1:00](https://www.dailymotion.com/video/x33a56v?t=60) | boca muy abierta, un brazo arriba, agarrado a Nobita sobre el tatami | sorpresa, susto |
| **Doraemon** | [«El Pueblo de Nobita» 0:30](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=30) | de pie junto a Nobita, **brazos abiertos hacia arriba**, mirando una placa en la pared | **presentar** (serie clásica 2D) |
| **Nobita** | [tráiler 0:30](https://www.dailymotion.com/video/x33a56v?t=30) | encorvado, cabeza gacha, mochila puesta, choca de espaldas con la puerta corredera | cansancio; llegar a casa |
| **Nobita** | [«El Pueblo de Nobita» 3:00](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=180) | agachado, sonrisa traviesa, **regadera de juguete con las dos manos** sobre un pueblo a escala | **explicar**: «así se usa» |
| **Nobita** | [«Un mundo sin dinero» 3:00](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%20184%20-%20El%20indicador%20del%20desorden%20.mp4?t=180) | se tapa la cara con las dos manos, llorando; su papá lo abraza | tristeza |
| **Gigante** | [recital 0:20](https://www.dailymotion.com/video/x3402n2?t=20) | de pie, ojos cerrados, boca muy abierta, **brazo extendido al público**, micrófono en la otra mano, capa roja | **presentar, celebrar** |
| **Gigante** | [0:10](https://www.dailymotion.com/video/x2uugoz?t=10) ⚠️ película sin identificar | cejas en zigzag, ojos redondos, boca entreabierta, quieto | miedo |
| **Nobita, Shizuka, Suneo y Gigante** | [opening 0:40](https://www.dailymotion.com/video/x8k1ck8?t=40) | los cuatro de pie en fila, **cabeza hacia arriba**, mirando a Doraemon volar | mirar un invento en el aire |

Shizuka, Suneo y Dorami **no se vieron solos** en ningún clip limpio ⚠️:
sus tablas siguen deducidas del subtítulo.

### 15.1 Poses de las hojas de contacto (sin minuto; con número)

| Personaje | N.º y hoja | Pose | Sirve para |
|---|---|---|---|
| Gigante | 17, personajes | sentado con **guitarra**, cantando | **presentar** una «Pista sin voz» |
| Gigante | 76-80, objetos | **volando con el Takecopter**: carrera, despegue, brazos en cruz (1979) | acción, celebrar |
| Gigante | 28, personajes | puño cerrado, dientes, primer plano | **regañar** |
| Gigante | 83, objetos | saca bíceps, sonrisa enorme | animar |
| Los cinco | 64, objetos | Doraemon al centro con los brazos abiertos, los demás alrededor saltando | **presentar** en grupo |
| Nobita, Gigante, Suneo | 43, personajes | saltan a la vez sobre fondo de rayos | **celebrar** |
| Doraemon, Nobita, Gigante | 15, personajes | abrazados | amistad |
| Doraemon y Nobita | 73, objetos | sentados en la máquina del tiempo, dentro del túnel | viajar, el cajón |

### Doraemon

| # | Dónde | Qué dice / hace | Sirve para |
|---|---|---|---|
| 1 | *Stand by Me* 00:05:35 | sale del cajón y saluda: «Buenas noches, soy Doraemon» | **presentar** |
| 2 | *Stand by Me* 00:11:31 | «¡Chan! Takecopter»: **levanta el invento** con una mano | **explicar** (la pose del canal) |
| 3 | serie, 2006-11-10 · 00:16:23 | «¡Chan! Ya puedes estar tranquilo» y saca el diamante | **explicar** |
| 4 | museo (2013) 00:09:37 | explica qué es el museo | **explicar** |
| 5 | *Stand by Me* 00:14:46 | risita «nufufu», con picardía | **pensar**, travesura |
| 6 | *Stand by Me* 00:09:51 | «¡Imposible, imposible, imposible!» | negar |
| 7 | *Stand by Me* 01:12:44 | «¡Si no puedes cumplirla, no la prometas!» | **regañar** |
| 8 | serie, 2006-11-10 · 00:16:23 | «¡Chan! Ya puedes estar tranquilo» | **animar** |
| 9 | *Stand by Me* 01:02:04 | Nobita le pide el Takecopter y él contesta «**¡Okey!**» (オーケー) y salen volando | **celebrar**, acción |
| 10 | museo (2013) 00:03:49 | «¡No está! ¡Me robaron el cascabel!»: pánico, se busca por todo el cuerpo | lo pirata (el robo) |

### Nobita

| # | Dónde | Qué dice / hace | Sirve para |
|---|---|---|---|
| 1 | *Stand by Me* 00:10:35 | «Jejeje, encantado, Doraemon» | saludar |
| 2 | serie, 2005-08-05 · 00:10:02 | «¡Haz algo, Doraemooon!» | **pedir** (el hilo «Cómo se pide…») |
| 3 | *Stand by Me* 00:07:46 | «¡Mentira! ¡Vete!» | enfado |
| 4 | *Stand by Me* 00:26:42 | piensa: «no depender de los inventos» | **pensar** |
| 5 | *Stand by Me* 00:42:57 | «¡Gracias, gracias, Doraemon!» | **celebrar** |
| 6 | *Stand by Me* 01:02:01 | «¡Doraemon, el Takecopter!» y salen volando | acción |

### Shizuka

| # | Dónde | Qué dice / hace | Sirve para |
|---|---|---|---|
| 1 | *Stand by Me* 00:02:35 | se planta delante: «¡Paren los dos!» | **regañar** con educación |
| 2 | *Stand by Me* 00:00:45 | «¡Qué divertido!», corriendo (sueño de Nobita) | celebrar |
| 3 | serie, 2006-06-30 · 00:12:02 | «¿Estás bien, Nobita-san, Dora-chan?» | cuidar, **animar** |

### Gigante

| # | Dónde | Qué dice / hace | Sirve para |
|---|---|---|---|
| 1 | serie, 2005-05-06 · 00:10:34 | «**Bienvenidos a mi recital**» | **presentar** (con micrófono) |
| 2 | serie, 2006-09-08 · 00:11:29 | «¡Empieza el recital!» | celebrar |
| 3 | serie, 2006-11-10 · 00:08:58 | «¡Nobita, qué te crees!» | **regañar** (con miedo) |

### Suneo

| # | Dónde | Qué dice / hace | Sirve para |
|---|---|---|---|
| 1 | *Stand by Me* 00:01:50 | «Qué cansancio, tres días seguidos de filete» | presumir |
| 2 | serie, 2006-06-23 · 00:04:33 | «¡Se lo voy a contar a todos!» ⚠️ quién | presumir |

### Dorami

| # | Dónde | Qué dice / hace | Sirve para |
|---|---|---|---|
| 1 | museo (2013) 00:10:22 | «¿Por qué te importa tanto ese cascabel?» | preguntar, **pensar** |
| 2 | museo (2013) 00:11:35 | «Vamos todos al museo a buscar el cascabel» ⚠️ (no dice quién; por el tono, ella) | **animar** |

---

## 16 · Vestuario

Los **colores de la ropa** están confirmados ✅: en el día a día **Nobita
va de amarillo con pantalón corto azul marino**, **Shizuka de rosa con
falda granate**, **Suneo de verde azulado** y **Gigante de naranja**
([Chiebukuro 1](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11148106111),
[Chiebukuro 2](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q12116884012),
[blog de Shimizu](https://ameblo.jp/shimizu90723/entry-12641161808.html)).
Pero **Nobita tiene 137 camisetas distintas** en 823 historias
([hatosan](https://www.hatosan.com/ensoku/2011/05/post-25.html)), y hay una
lista de **todas las camisetas de Gigante**
([ajaidesu](https://ajaidesu.hatenablog.com/entry/2020/12/21/200548)).
En la **serie clásica** Nobita lleva a menudo **camiseta roja** (visto en
«Un mundo sin dinero», 3:00) ✅.

**Segunda pasada: hex MEDIDOS** con Pillow, píxel a píxel, sobre los
retratos oficiales de 2005 y el cel de producción (enlaces en §3.5):

| Personaje | Prenda | Hex medido | Fuente |
|---|---|---|---|
| Doraemon | cuerpo azul | `#1D99C8` | retrato oficial 2005 ✅ |
| Doraemon | cuerpo azul, con la luz del cel | `#0072B8` | cel de producción (hoja n.º 2) ✅ |
| Doraemon | nariz, collar y cola | `#E02333` | retrato oficial ✅ |
| Doraemon | cascabel | `#FCDC2A` | retrato oficial ✅ |
| Doraemon | cara, barriga, bolsillo | blanco | retrato oficial ✅ |
| Nobita | camiseta amarilla | `#FDD23C` | retrato oficial 2005 ✅ |
| Nobita | pantalón corto azul marino | `#2D457C` | retrato oficial 2005 ✅ |
| Shizuka | top y mangas rosa | `#F29FC2` | retrato oficial 2005 ✅ |
| Shizuka | **falda granate** (no rosa) | `#B71840` | retrato oficial 2005 ✅ |
| Suneo | suéter verde azulado | `#27B585` | retrato oficial 2005 ✅ |
| Gigante | camiseta naranja | `#F08E39` | retrato oficial 2005 ✅ |
| Gigante | camiseta naranja, en el bosque | `#D78241` | fotograma «Doraemon Nobita and Gian» (hoja n.º 15) ✅ |
| Dorami | amarillo y lazo rojo | `#F7DB3E` y `#E61737` | **de memoria / paleta de fans** ⚠️: no se midió |

| Personaje | Ropa icónica |
|---|---|
| **Doraemon** | no lleva ropa: cuerpo azul, cara y barriga blancas, **nariz roja**, **collar rojo con cascabel amarillo**, **bolsillo blanco de media luna**, **cola roja de bola** ✅ |
| **Nobita** | **gafas redondas**, camiseta o polo **amarillo**, **pantalón corto azul marino** ✅ |
| **Shizuka** | **dos coletas cortas**, **top rosa y falda granate** ✅ (corrige «falda rosa, blusa clara») |
| **Gigante** | camiseta **naranja** ancha, pantalón corto; de béisbol, gorra con **«G»** ✅ |
| **Suneo** | ropa cara y cambiante, casi siempre **verde azulado**; **pelo en punta** hacia atrás ✅ |
| **Dorami** | amarilla, **lazo rojo** en la cabeza, bolsillo con **rayas rojas cruzadas**; cola con dibujo de flor ⚠️ (sin verla en imagen) |

**Ojo con dos imágenes mal tituladas en la wiki** ✅ (el investigador de
imagen las abrió): en «Shizuka and Nobita.jpg» la niña **no es Shizuka** y
va con falda verde (ropa de gimnasia); en «Suneo and Doraemon.jpg» el niño
**lleva gafas: es Nobita** con suéter verde menta. No sacar de ahí la ropa
«icónica».

**Gigante 1973 y 2005**: en el de 1973 la cara es más ovalada y menos
definida; en 2005, más redonda y con menos púas en el pelo ✅ (hoja
`objetos_01.jpg`, n.º 57 y 56).

---

## 17 · Paisajes y fondos de pantalla

### Los sitios, con su luz (segunda pasada: medida)

- **Cuarto de Nobita, de día**: claro, verde tatami y madera: `#C1DBAA`,
  `#D3B177`, `#E7EBE6`, brillo 81% (fondo oficial) ✅. En 3D, crema
  `#A09B7F`/`#F9F9E1` (tráiler [0:30](https://www.dailymotion.com/video/x33a56v?t=30)) ✅.
- **Cuarto de noche**: casi a oscuras, madera `#1C0E05`, **un solo rayo de
  ventana**, brillo 13% (tráiler [1:00](https://www.dailymotion.com/video/x33a56v?t=60)) ✅.
- **Cajón abierto de noche**: la luz sale del **túnel del tiempo** (en
  *Stand by Me*, 00:04:46 «¡se abrió!» y 00:05:35 sale Doraemon) ✅ el
  minuto. El túnel: azul `#2F4863`/`#3F728B` sobre negro `#0F1113` en el
  opening ([0:05](https://www.dailymotion.com/video/x8k1ck8?t=5)); espiral
  blanca con relojes rojos, verdes y amarillos en el fondo oficial ✅.
- **Descampado de día**: cielo `#E4ECF1`/`#67C3EE`, tierra `#D8D69D`, árbol
  `#92C064` (fondo oficial) ✅. **De noche, recital**: cielo `#395A81` y
  focos naranja `#CA5E41` ([0:20](https://www.dailymotion.com/video/x3402n2?t=20)) ✅.
  El **atardecer** naranja, sin medir ⚠️.
- **Calle de los Nobi, de día**: setos `#2B4036`, cielo claro `#B4D1C5`
  (serie clásica, [0:30](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=30)) ✅.
- **Museo del siglo XXII**: blanco, luminoso, vitrinas ⚠️ (sin ver).

### Fondos de pantalla

- **Oficiales**: los 5 fondos para videollamadas de
  [dora-world.com/contents/1399](https://dora-world.com/contents/1399) ✅.
  **Tamaño medido: 1280×894 a 1280×929** (tabla de §3.0, hoja
  `fondos_01.jpg`) ✅. Recopilación de fondos de anime para Zoom con
  Doraemon: [Animate Times](https://www.animatetimes.com/news/details.php?id=1587701645).
- **Página de fondos oficiales**: [dora-world.com/wallpaper](https://dora-world.com/wallpaper) (tamaños sin ver ⚠️).
- **De fans en alta** (Wallhaven, sólo aptos; tamaño y ♥ de su API) ✅:

| Tamaño | ♥ | Qué | Autor u origen | Imagen |
|---|---|---|---|---|
| 5120×2880 | 16 | **Doraemon, Nobita y Shizuka** juntos, fondo claro | subido por kite16017 | [wallhaven-k8359q](https://w.wallhaven.cc/full/k8/wallhaven-k8359q.jpg) |
| 3088×4667 | 104 | **Shizuka**, vertical | **Muyuan**, [Bilibili](https://t.bilibili.com/426404335972917520?tab=2) | [wallhaven-9mzwl1](https://w.wallhaven.cc/full/9m/wallhaven-9mzwl1.jpg) |
| 3840×2160 | 18 | Doraemon, manga, corazón, fondo azul | subido por Rkomy | [wallhaven-1qqxpg](https://w.wallhaven.cc/full/1q/wallhaven-1qqxpg.jpg) |
| 2400×3597 | 37 | **Tamako**, la mamá de Nobita | [NeoArtCoRe en X](https://x.com/NeoArtCoRe/status/2087914313403265066) | [wallhaven-5ypgv9](https://w.wallhaven.cc/full/5y/wallhaven-5ypgv9.jpg) |
| 2560×1440 | 184 | escritorio en arte digital (el más guardado; que salga Doraemon, sin comprobar ⚠️) | [John Stone](https://x.com/JohnStone2078) | [wallhaven-wejgqr](https://w.wallhaven.cc/full/we/wallhaven-wejgqr.jpg) |
| 1920×1080 | 81 | Doraemon en un cuarto de **tatami** | subido por rainrelaxme | [wallhaven-q2zpeq](https://w.wallhaven.cc/full/q2/wallhaven-q2zpeq.jpg) |
| 1920×1200 | 14 | Doraemon con ratones y figuras, reflejo | subido por whhitlp | [wallhaven-lqqxlq](https://w.wallhaven.cc/full/lq/wallhaven-lqqxlq.jpg) |
| 1920×1080 | 28 | Doraemon minimalista | subido por 恰好心动 | [wallhaven-l8yl7p](https://w.wallhaven.cc/full/l8/wallhaven-l8yl7p.jpg) |
| 1920×1080 | 12 | los cinco juntos | subido por Paititi | [wallhaven-qzrz3q](https://w.wallhaven.cc/full/qz/wallhaven-qzrz3q.jpg) |

---

## 18 · Guía para generar con IA (Firefly, Canva)

> Para fondos, texturas y pruebas de encuadre. **No** para inventar al
> personaje: el recorte de Doraemon sale de un fotograma o arte oficial.

### Rasgos que nunca cambian

- Doraemon: **cabeza enorme y redonda** (más grande que el cuerpo),
  **sin orejas**, ojos blancos grandes **pegados entre sí**, nariz roja
  redonda, **seis bigotes** (tres por lado) ⚠️, boca justo debajo de la
  nariz, collar rojo, cascabel amarillo, **bolsillo de media luna**, **manos
  redondas sin dedos** (la Petari Hand ✅), pies blancos que **no tocan del
  todo el suelo** ✅, y el **«Poko»**, el bultito en la comisura del labio
  que cambia de lado según el ángulo ✅ ([CGWorld](https://cgworld.jp/interview/1408-sbmd.html)).
- Nobita: gafas redondas, pelo negro corto con flequillo recto, camiseta
  amarilla `#FDD23C`, pantalón corto `#2D457C`.
- Shizuka: dos coletas cortas negras, top rosa `#F29FC2`, falda granate
  `#B71840`.
- Gigante: grande, camiseta naranja `#F08E39`; se le ven los dientes (a
  Nobita y Shizuka no) ✅ (CGWorld).
- Suneo: bajito, pelo en punta hacia atrás, labio casi de pico, suéter
  `#27B585` ✅.
- Dorami: más pequeña, amarilla, lazo rojo, bolsillo con rayas rojas.

**Paleta fija** (medida, §16): azul `#1D99C8`, rojo `#E02333`, amarillo
`#FCDC2A`, blanco. Fondo de día: `#C1DBAA`, `#D3B177`, `#E7EBE6`, cielo
`#67C3EE`.

### Estilo

- **Línea**: negra o marrón oscura, **gruesa y de grosor igual**, curvas
  suaves, casi sin ángulos ✅ (visto en la página de manga
  [«Gian manga.jpg»](https://static.wikia.nocookie.net/doraemon/images/a/a0/Gian_manga.jpg):
  sin tramas; sombra con negro plano). En los fondos oficiales la línea es
  gris verdosa `#7C8B7B`, no negra ✅.
- **Color**: **plano (cel)**, con **una sola sombra** suave o ninguna ✅
  (ending y serie clásica medidos). Colores **limpios y alegres**. **No
  mezclar** con el degradado dramático del 3D de *Stand by Me*.
- **Luz**: de día, suave; nada de contraluces dramáticos.
- **Encuadre**: a la altura de los ojos de un niño; planos medios.
- **Fondos**: más detallados que los personajes, dibujados a mano, como un
  libro ilustrado.

### Palabras que ayudan

`1980s Japanese children's manga style, Fujiko F. Fujio style, thick uniform
outlines, flat cel colors, soft daylight, Japanese suburban house, tatami
room, wooden study desk, 1970s Tokyo residential street, vacant lot with
three concrete pipes, cheerful, warm afternoon light`

### Palabras que lo estropean

`realistic, 3D, glossy, dramatic lighting, dark, horror, cyberpunk, anime
girl, detailed shading, cat ears` (¡Doraemon no tiene orejas!), `fingers`,
`screentone`, `halftone` (el manga casi no lleva tramas).

**Etiquetas que entienden las IA de imagen** (las más repetidas en
Danbooru, §4.3) ✅: Doraemon `bell, red_nose, collar, jingle_bell, whiskers,
simple_background`; Nobita `glasses, yellow_shirt, blunt_bangs, shorts,
blue_pants`; Shizuka `twintails, black_hair, skirt, short_twintails`.

### Qué referencias subir

- **Estilo de fondo**: los fondos oficiales de
  [dora-world.com/contents/1399](https://dora-world.com/contents/1399).
- **Cuarto en 3D (medidas)**: [Sketchfab · Nobita's Room](https://sketchfab.com/3d-models/nobitas-roomdoraemon-3d-model-7ac2289be8be408292b29a06f8f40a71).
- **Descampado real**: fotos de la Harappa del museo Fujiko
  ([camera10.me](https://camera10.me/blog/photospot/fujiko-museum)).
- **Estilo de color de los personajes**: el cel de producción (hoja
  `personajes_01.jpg`, n.º 2) y los retratos oficiales de 2005 (§3.5).
- **Pose**: Gigante con guitarra (personajes n.º 17), Gigante volando
  (objetos n.º 76-80), los cinco juntos (objetos n.º 64), el bolsillo y su
  cartela (objetos n.º 58).

### Vocabulario de expresiones (lo que se ve en las hojas y fotogramas)

- **Boca enorme**: en Doraemon la boca abierta ocupa media cara ✅ (CGWorld;
  y visto en hoja n.º 5 y en el tráiler 1:00).
- **Ojos que se cierran del todo**: en Doraemon, hasta «tres rayas» ✅
  (CGWorld); Gigante canta con los ojos cerrados (recital 0:20) ✅.
- **Cejas en zigzag** y ojos redondos: miedo o sorpresa (Gigante, 0:10) ✅.
- **Manos tapando la cara**: llanto (Nobita, «Un mundo sin dinero» 3:00) ✅.
- **Fondo de rayos de color** detrás del personaje: alegría o el momento
  del invento (hoja n.º 43 y 58) ✅.
- **Chibi**: la serie no tiene una versión *chibi* aparte; los personajes
  ya son cabezones (visto en las hojas). Gotas de sudor y otros signos de
  manga: no documentados en las partes ⚠️.

### Para una IA de texto: cómo escribir sus diálogos

**Reglas de voz**:
- **Doraemon**: explica con paciencia y con orgullo de su invento. Suspira
  antes de ceder: «ay, qué remedio…». Anuncia el invento con «¡Chan!» y el
  nombre entre corchetes o en mayúscula. Se ríe «nufufu». Regaña corto y
  claro. Llama a Nobita «Nobita» (en japonés, «Nobita-kun»).
- **Nobita**: alarga la vocal al gritar («¡Doraemooon!»), pide «¡haz
  algo!», se enfada en ráfaga («¡Mentira! ¡Vete!»), se ríe tímido
  («jejeje»).
- **Gigante**: manda, grita, invita a su manera («¡Oigan!»), anuncia su
  recital como una estrella.
- **Suneo**: presume y se queja de lujo («qué cansancio, tres días seguidos
  de filete»).
- **Shizuka**: educada, pone orden («¡Paren los dos!»), cuida («¿Estás
  bien?»).
- **Puntuación**: ¡…! mucho; repetición para exagerar («¡Imposible,
  imposible, imposible!»); vocales alargadas; puntos suspensivos al
  suspirar. Nada de palabrotas ni sarcasmo duro: es una serie familiar.

**Frases reales por emoción** (japonés traducido, con minuto de §2 y §7;
las marcadas «latino» son textuales del doblaje, §10.6):

| Emoción | Frases |
|---|---|
| **Alegre** | «¡Gracias, gracias, Doraemon!» (Nobita, *Stand by Me* 00:42:57) · «¡Qué divertido!» (Shizuka, 00:00:45) · «¡Empieza el recital!» (Gigante, 2006-09-08 · 00:11:29) · «¡Okey!» (Doraemon, 01:02:04) |
| **Enfadado** | «¡Mentira! ¡Vete!» (Nobita, 00:07:46) · «¡Nobita, qué te crees!» (Gigante, 2006-11-10 · 00:08:58) · «¡Si no puedes cumplir una promesa, no la hagas!» (Doraemon, 01:12:44) · latino: «¡Eso duele! ¿Acaso crees que tengo la cabeza de piedra?» (1:19) |
| **Explicando** | «Todo lo que había en el cajón lo pasé a este bolsillo de cuatro dimensiones. Aquí cabe de todo» (Doraemon, 00:06:14-00:06:18) · «Ahora te enseño lo que es el siglo XXII» (00:11:26) · «Desde el primer modelo hasta el último, todos están ahí» (museo, 00:09:49) |
| **Animando** | «¡Chan! Ya puedes estar tranquilo» (Doraemon, 2006-11-10 · 00:16:23) · «Tranquila, tu futuro será brillante» (padre de Shizuka, 01:08:32) · «Para quien fabrica inventos, lo más importante es que le guste fabricarlos» (Pepler, museo 00:55:54) |
| **Triste** | latino: «Quisiera estar en un pueblo libre donde nadie me molestara y pudiera ser lo que se me antojara» (Nobita, 1:34) · «¡Haz algo, Doraemoon!» (2005-08-05 · 00:10:02) · «¡No está! ¡Me robaron el cascabel!» (Doraemon, museo 00:03:49) |

**Vocabulario de la serie**: bolsillo mágico, inventos o artilugios
secretos (ひみつ道具), puerta a cualquier lugar, Takecopter, máquina del
tiempo, Grandes Almacenes del Futuro, Patrulla del Tiempo, dorayaki,
descampado, recital, «el gato cósmico».

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

### Quién lo hace y con qué

- **Manga**: Fujiko F. Fujio, con **herramientas normales de papelería**,
  sin materiales de pintura elaborados ⚠️ (dicho por la editorial según la
  parte de imagen; sin enlace a la fuente original). Línea limpia de grosor
  igual, **casi sin tramas**, sombra con negro plano ✅ (visto en
  [«Gian manga.jpg»](https://static.wikia.nocookie.net/doraemon/images/a/a0/Gian_manga.jpg)).
- **Anime de TV (1979 y 2005-hoy)**: **Shin-Ei Animation** (シンエイ動画),
  fundado en 1976 por Daikichirō Kusube, antiguo animador de Toei ✅
  ([Fandom](https://doraemon.fandom.com/wiki/Shin-Ei_Animation) y
  Wikipedia). Qué programa usa: **no encontrado** ⚠️. Lo normal en la TV
  japonesa es RETAS Studio de CELSYS ([Wikipedia](https://en.wikipedia.org/wiki/RETAS)),
  pero no hay confirmación para Doraemon.
- **Staff de la serie de 1973** (AniList): director jefe Mitsuo Kaminashi,
  directores de arte Shōhei Kawamoto y Morishige Suzuki, fotografía
  Nobuyuki Sugaya, efectos de sonido Yōzō Kataoka y Katsuo Ogawa ✅
  ([AniList](https://anilist.co/anime/501/staff)).
- ***Stand by Me Doraemon*** (2014) y ***2*** (2020), en **3DCG**:
  **Shirogumi**, **Robot Communications** y Shin-Ei; dirección Takashi
  Yamazaki y Ryūichi Yagi ✅. Software: **Autodesk 3ds Max** (2012 en la
  primera, 2017 en la segunda) ✅ ([CGWorld](https://cgworld.jp/interview/1408-sbmd.html),
  [ITmedia](https://www.itmedia.co.jp/pcuser/articles/1408/14/news030.html)).
  En la segunda, render con **V-Ray** y composición en **Nuke** con color
  **ACES/OpenColorIO** ✅ ([CGWorld 2021](https://cgworld.jp/feature/202101-cgw269t2dora.html)).
  Grabaron las voces **antes** de animar, para el movimiento de labios ✅.

### Cómo pensaron el 3D (entrevista de CGWorld al director de arte Makoto Hanabusa y a Yoshitaka Takeuchi) ⚠️ un solo medio, pero oficial

- Probaron un Doraemon «electrodoméstico», con tornillos y azul
  transparente. **Lo descartaron**: le quitaba calidez.
- El **azul es «goma del futuro»** (goma y metal, con las huellas de Nobita)
  y el **blanco, «plástico del futuro»**, lo más suave posible.
- **La línea entre colores no es geometría**: es un **mapa de
  desplazamiento en la textura** ([segunda parte](https://cgworld.jp/interview/1408-sbmd-2.html)).
- El azul **cambia de tono** entre luz y sombra.
- Los ojos se cierran del todo, con variantes de pupila, hasta «tres rayas».
- El **Poko** (ポコ), el bultito del labio, tiene variantes «de lado» y «en
  diagonal»; en Suneo el labio casi es un pico.
- **Asimetría a propósito** en Gigante. A Gigante se le ven los dientes; a
  Nobita y Shizuka no.
- Cada cara se probó en **plano medio y en primer plano** por separado.

### Cómo reproducirlo (guía práctica de la parte de texto: dato del estudio + adaptación)

- **Photoshop (2D, estilo serie)**: pincel de tinta de **grosor fijo** (2-3
  px a resolución de impresión), sin presión; relleno **plano** en una capa
  bajo la línea; una sola capa de sombra en *Multiplicar* o ninguna; línea
  negra en personajes y **gris verdosa `#7C8B7B`** en fondos. Sin trama. Sin
  grano: el anime de TV no lo lleva marcado ⚠️ (no hay entrevista sobre sus
  filtros).
- **Blender (objeto 3D, estilo *Stand by Me*)**:
  - **Contorno**: exterior con *Freestyle* (o *Solidify* con normales
    invertidas); **las líneas entre colores, pintadas como textura** sobre
    el UV, como hizo Shirogumi.
  - **Sombreado**: *Shader to RGB* + *ColorRamp* de 2-3 escalones, **dos
    azules** con corte duro y un brillo pequeño.
  - **Materiales**: azul con *Principled BSDF* algo satinado («goma»);
    blanco mate («plástico»); nariz y cascabel lisos, con reflejo.
  - **Render**: **Cycles** + compositor de nodos + **AgX o Filmic** (el
    equivalente a ACES) para que la luz no se queme.
- **Encuadre**: presentar y explicar en **plano medio**; emociones fuertes
  en **primer plano**. En la serie, cámara a la altura de un niño.
- **Modelos libres**: Doraemon CC BY de Andy (Pandabox) y el cuarto de
  Nobita CC BY (§4.1). **Rigs**: no encontrados ⚠️.

## Punto 19 · Texturas 2D

- **Trama del manga**: prácticamente **ninguna** ✅ (visto en
  «Gian manga.jpg»). No hace falta pincel de trama.
- **Papel**: el color de fondo de las cartelas y del manga es blanco limpio;
  para el catálogo o el sobre de pedido, papel de ambientCG o Poly Haven
  (CC0, §5.3).
- **Tatami**: [Poly Haven · tatami_mat](https://polyhaven.com/a/tatami_mat) y
  [ambientCG · Tatami005](https://ambientcg.com/view?id=Tatami005), CC0 ✅.
- **Patrones de ropa**: **ninguno** de los cinco lleva estampado; todo liso
  ✅. El único patrón es la **flor de la cola de Dorami**, sin ver en imagen ⚠️.
- **Emblemas**: la **«G»** del equipo de béisbol de Gigante, letra de bloque
  sobre gorra blanca (hoja `objetos_01.jpg`, n.º 62) ✅; las **rayas rojas
  cruzadas** del bolsillo de Dorami ✅.
- **Fondo de rayos del invento**: rayos azules con destellos (n.º 58) o
  morados (n.º 74). Se hace en Photoshop con un degradado radial y
  *Filtro › Distorsionar › Coordenadas polares* sobre rayas ⚠️ (técnica
  propuesta, no del estudio).
- **Pinceles libres**: no se buscaron en esta pasada ⚠️. Con un pincel
  redondo duro de Photoshop basta, porque la línea es de grosor fijo.

## Punto 20 · Gustos y detalles de cada personaje

| Personaje | Cumpleaños | Altura y peso | Le gusta | Odia o teme | Objeto que siempre lleva |
|---|---|---|---|---|---|
| **Doraemon** | **3-sep-2112** ✅ | **129,3 cm / 129,3 kg** ✅ | dorayaki ⚠️ (AniList) | **ratones** ✅; médicos (la cirugía de orejas salió mal) ✅ | bolsillo mágico, cascabel ✅ |
| **Nobita** | **7-ago** ✅ (manga, 1972) | sin ficha oficial ⚠️ | dormir (0,93 s), ayatori, puntería ✅ | los estudios, que le molesten ✅ | honda o tirachinas ⚠️; gafas ✅ |
| **Shizuka** | **mayo** ✅ (sólo el mes) | sin ficha oficial ⚠️ | **boniatos** asados, violín, bañarse ✅ | el piano (lo toca bien) ✅ | muñecas ✅ |
| **Gigante** | **15-jun** ✅ (manga, 1980) | el más alto, sin ficha oficial ⚠️ | cantar (mal), béisbol ✅ | — | micrófono; bate y gorra «G» ✅ |
| **Suneo** | **febrero** ✅ (sólo el mes) | **el más bajo de la clase**, su complejo ✅ | presumir, juguetes caros, dibujar y diseñar ✅ | quedar por debajo | cámara, juguetes ✅ |
| **Dorami** | **2-dic-2114** ✅ | **100 cm / 91 kg** ✅ | **pan de melón** ✅ | — | bolsillo de rayas, máquina tulipán ✅ |

- **Cómo se ven a sí mismos**: Suneo se mira al espejo y se dice guapo ✅;
  Gigante se cree un gran cantante ✅; Nobita se sabe torpe ✅ (AniList).
- **Sueños**: Shizuka quiere ser **enfermera o azafata** ✅ (Fandom).
- Fuentes: [nokikero](https://nokikero.com/dora-character-birthday/)
  (cumpleaños con la revista y número de cada uno), AniList y Fandom, y lo ya
  citado en §8. Las alturas de los niños **no tienen ficha oficial única**:
  las webs de fans se contradicen
  ([Scratchpad Wiki](https://scratchpad.fandom.com/wiki/Heights_of_the_Doraemon_Characters)) ⚠️.

## Punto 21 · Por qué la gente la ama (y las escenas que hacen llorar)

**Razones** ✅ (análisis japoneses e internacionales):
- **Doraemon no consiente demasiado ni abandona** a Nobita: un equilibrio
  raro en la ficción infantil ([tamatebox](https://tamatebox.net/doraemon/),
  [ampmedia](https://ampmedia.jp/2020/07/23/doraemon/)).
- **El público se identifica con Nobita**, el torpe normal, no con un genio
  (Medium «Why is Doraemon Popular» y tamatebox).
- **Ritual de familia**: padres e hijos la ven juntos desde hace 50 años
  ([Japan Times](https://www.japantimes.co.jp/culture/2020/02/01/general/doraemon-50th-anniversary/)).
- **Mensajes que no envejecen**: ecología, familia, empatía, perseguir
  sueños.
- **Cifras**: manga de **250 a 300 millones** de copias según la fuente ⚠️;
  más de **40 películas**; emitida en **más de 35 países** ✅; **primer
  embajador anime** de Japón (2008) ✅; elegido por *TIME* en **2012** entre
  **22 héroes asiáticos**, el único personaje de anime ✅; **residencia
  oficial en Kawasaki** el 3-sep-2012 ✅ (Fandom).

**La escena que hace llorar**: ***Stand by Me Doraemon*** (2014).
- **01:08:32 → 01:09:02**: el **padre de Shizuka**, la noche antes de la
  boda: «Nobita sabe desear la felicidad de los demás y sufrir con su
  desgracia… tu futuro será brillante» ✅ (subtítulo). Duele porque es un
  padre soltando a su hija y porque por fin alguien ve a Nobita por lo que
  es.
- **00:57:40 → 00:57:53**: los **dos Nobitas** se dan las gracias ✅.
- **La despedida** de Doraemon y Nobita: lo que más citan las reseñas es que
  **nunca se dicen en voz alta cuánto se necesitan**, y por eso golpea
  ✅ ([eiga.com](https://eiga.com/movie/79515/review/)). Minuto, sin ver ⚠️.
- **Reacción**: el **88,4 %** del público **lloró** (encuesta a la salida)
  ✅ ([ARAMA! JAPAN](https://aramajapan.com/news/tvmovie/movies/88-4-of-stand-by-me-doraemon-moviegoers-cried-during-the-film/6358/)
  y eiga.com); la votación **«Dora-naki»** de
  [Cinematoday](https://www.cinematoday.jp/page/A0004197) ✅; **2.ª
  animación más taquillera de Japón en 2014**, 183,4 millones de dólares,
  sólo detrás de *Frozen* ✅ ([Variety](https://variety.com/2015/film/festivals/film-review-stand-by-me-doraemon-1201352301)).
- Cómo está dibujada: 3D con **luz de noche de un solo rayo de ventana**
  en el cuarto (tráiler [1:00](https://www.dailymotion.com/video/x33a56v?t=60),
  brillo 13%) ✅. La escena del padre, sin fotograma ⚠️.
- **Otra que duele**: *Adiós, Doraemon…* (1973 y repetida después):
  Doraemon vuelve al futuro y Nobita decide seguir solo ✅
  ([Doraenciclopedia](https://doraemon.fandom.com/es/wiki/Adi%C3%B3s%2C_Doraemon...)).
  Sin clip latino con minuto ⚠️.
- **Las que hacen reír**: el recital de Gigante ✅ y el Doraemon que huye de
  un ratón ✅. Reddit: «Esta tiene que ser una de las mejores entradas de
  Doraemon» (143 votos) ⚠️ ([hilo](https://www.reddit.com/r/Doraemon/comments/1fkivd1/this_got_to_be_one_of_doraemons_best_entrances/)).

## Punto 22 · Fan dubs y comunidad hispana

Buscado con `yt-dlp ytsearch` (título, canal y vistas sin iniciar sesión;
vistas del 24-sep-2026) ✅:

| Qué | Canal | Vistas | Enlace |
|---|---|---|---|
| Parodia «Doraemon tapa del Pluto» | **Dobla2** (canal argentino de parodias de doblaje) | **394 565** | [YouTube](https://www.youtube.com/watch?v=D_hkGW0fZ_k) |
| Ending de *El gato cósmico* con Maggie Vera | DobleHDMedia | 178 732 | [YouTube](https://www.youtube.com/watch?v=lLZX4c8wOBQ) |
| Cortometraje parodia | ParodiAnime (das95balas) | 80 009 | [YouTube](https://www.youtube.com/watch?v=OqQ9XaTgkrs) |
| Cover de *Stand by Me Doraemon* en latino | Unkos Channel | 76 990 | [YouTube](https://www.youtube.com/watch?v=mn1G54SY7Bo) |
| Cover de «Doraemon no Uta» (1979) en latino | Lissette Chan | 46 460 | [YouTube](https://www.youtube.com/watch?v=SMJkerRUG2g) |
| Fandub de «Himawari no Yakusoku» | SINAY PAOHLA | 20 756 | [YouTube](https://www.youtube.com/watch?v=wUurnNVqJZc) |
| Ending «Nuestro Planeta» en latino | Doraemon Latino | 18 584 | [YouTube](https://www.youtube.com/watch?v=eljPM34kWmE) |
| Cover de «Yume wo Kanaete Doraemon» | Lissette Chan | 7228 | [YouTube](https://www.youtube.com/watch?v=LxnVt7tYnio) |
| «Doraemon el cirujano», parodia | Norita | 734 ⚠️ canal pequeño | [YouTube](https://www.youtube.com/watch?v=csvegcKHCIw) |

> Ojo: la parte de voz da el 1979 y el 2005 de Lissette Chan con los
> enlaces al revés en `voz.json`; se citan aquí los dos sin asegurar cuál es
> cuál ⚠️.

- **Todas las voces latinas de Doraemon** en un TikTok:
  [@sengek56](https://www.tiktok.com/@sengek56/video/7500317759486561542)
  ⚠️ (vistas sin medir: TikTok no se puede buscar desde aquí).
- **Otras lenguas cercanas**: *Doraemon, o gato cósmico* en gallego
  ([Internet Archive](https://archive.org/details/doraemon-galego_202208)) y
  openings en catalán (TVC, TVV) en Dailymotion ✅.
- **No encontrado** ⚠️: un canal de *fandub* que doble capítulos enteros;
  sólo hay covers y parodias sueltas.
- **Para el servidor**: Dobla2 es el ejemplo perfecto de parodia de doblaje;
  y la historia de **Irwin Daayán (Suneo → Doraemon)** y de **Laura Torres**
  (dejó a Nobita por la garganta y volvió en 2014) son anécdotas del gremio.

## Punto 23 · Colaboraciones, figuras y cosplay

| Colaboración | Cuándo | Qué trae | Fuente |
|---|---|---|---|
| **UNIQLO UT × Museo del Louvre** | abril de 2025 | Doraemon **metido en cuadros del Louvre** (p. ej. de espaldas mirando el globo en *El astrónomo* de Vermeer); banner **1200×628**, productos 2000×2000 | [doraemon-world](https://www.doraemon-world.com/uniqlo-lanza-una-coleccion-de-doraemon-y-el-louvre/), [imagen](https://www.doraemon-world.com/wp-content/uploads/2025/04/25SS-Doraemon_Louvre_1200x628.jpg) ✅ |
| **New Era** | enero de 2026 | gorras y ropa con dibujo a mano alzada, paneles de cómic y grafiti, siluetas de Nobita, Shizuka y Dorami | [Hypebeast](https://hypebeast.com/2026/1/doraemon-new-era-original-colleciton-caps-t-shirts-apparel-collaboration-collection-release-info) ✅ |
| **Converse** | julio de 2026 | zapatillas y ropa; **también en México** | [El Sol de Cuautla](https://oem.com.mx/elsoldecuautla/tendencias/llega-la-coleccion-converse-y-doraemon-fecha-de-lanzamiento-precios-y-detalles-24681680) ✅ |
| ***Granblue Fantasy*** (gacha) | diciembre de 2021 | evento «Nobita's Flying Ship»; Doraemon y Nobita jugables | [Siliconera](https://www.siliconera.com/granblue-fantasy-reveals-doraemon-collab-characters/), [GamerBraves](https://www.gamerbraves.com/granblue-fantasy-announces-doraemon-collab-for-december/) ✅; el arte, sin ver (Cloudflare) ⚠️ |
| **Toyota «ReBorn»** | 2011 | los personajes 20 años mayores; **Jean Reno** hace de Doraemon en imagen real | Fandom ⚠️ (una fuente) |
| **Doraemon F's Kitchen** (café oficial) | 7-nov a 31-dic-2025 | «Dorami Birthday Fair», menú por el cumpleaños de Dorami | [haveagood-holiday](https://www.haveagood-holiday.com/en/articles/doraemon-fs-kitchen-dorami-birthday-fair-2025) ✅ |
| Gashapon «Doraemon Light Mascot» | septiembre de 2026 | cápsulas con luz | [collabo-cafe](https://collabo-cafe.com/en/events/collabo/doraemon-light-mascot-gashapon-2026/) ✅ |

- **Fortnite**: **no hay colaboración oficial**; sólo fans pidiéndola
  (2025). Es un «busqué y no hay», no un «no busqué».
- **Figuras oficiales**: la **Figuarts ZERO del cuarto de Nobita**, con el
  **cajón que se abre y el túnel del tiempo dentro** ✅
  ([Dengeki Hobby](https://hobby.dengeki.com/news/953237/)). Es la mejor
  referencia 3D del cajón abierto.
- **Tienda oficial**: «Doraemon Mirai Department Store» en DiverCity Tokyo
  (§3.4) ✅.
- **Cosplay**: no apareció uno bien hecho, con materiales dignos de citar;
  sólo disfraces de tienda ⚠️. Un robot sin rasgos humanos se hace más como
  botarga que como cosplay.

## Punto 24 · Obras parecidas y temas relacionados

- **Del mismo autor y del mismo estudio (Shin-Ei)** ✅
  ([Fandom · Shin-Ei](https://doraemon.fandom.com/wiki/Shin-Ei_Animation)):
  ***Perman*** (un niño con aparatos de un extraterrestre, héroe a ratos),
  ***Kiteretsu Daihyakka*** (1988-1996; el niño **inventa** sus propios
  aparatos, al revés que Nobita), ***Chinpui***, ***21-Emon***, ***Obake no
  Q-Taro***.
- **Del mismo estudio, otro autor**: ***Crayon Shin-chan***, humor familiar
  de barrio ✅. Es además la obra que más recomiendan los usuarios de
  AniList a quien le gusta Doraemon (15 votos); después *Ninja Hattori-kun*
  (4) y *Takopi's Original Sin* (2) ✅ ([AniList](https://anilist.co/anime/501)).
- **Influencias de Fujiko F. Fujio**: **Osamu Tezuka**. Leyó *Shin
  Takarajima* (1947) y le marcó «como ver una película»; en 1954 se mudó a
  Tokio para estar cerca de él y ayudó a terminar páginas de *Kimba, el león
  blanco* ✅ ([Toons Mag](https://www.toonsmag.com/fujiko-fujio/) y Fandom).
  Los cómics y dibujos animados de EE. UU., Hanna-Barbera incluido ⚠️ (una
  fuente).
- **Láminas del servidor que se le parecen** (para no repetir ideas):
  - **Big Hero 6 / Grandes Héroes** (encargo 08): robot amigo que ayuda a un
    chico. **Diferenciar**: aquí el protagonista es el **bolsillo/catálogo**,
    no el robot.
  - **Pokémon** (encargo 07): cuidado con repetir un «catálogo para elegir»
    (la Pokédex). **Diferenciar**: aquí es una tienda con pedido y sobre.
  - **Mafalda** (encargo 09): humor de niños y barrio; formato de tira.

## Punto 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo, en cinco líneas** ✅ (Fandom):
1. Doraemon es un robot gato **MS-903** de la fábrica Matsushiba, del año
   2112.
2. Lo manda **Sewashi**, descendiente de Nobita, para que la familia Nobi no
   acabe arruinada.
3. Todo sale del **bolsillo de cuatro dimensiones**: sin límite de tamaño ni
   peso.
4. Los **inventos** (ひみつ道具, *himitsu dōgu*) se piden por catálogo a los
   **Grandes Almacenes del Futuro** (未来デパート).
5. El futuro cambia según lo que Nobita hace hoy; hay una **Patrulla del
   Tiempo** que vigila.

**Por qué es azul** ✅: era **amarillo** y tenía orejas; un **ratón robot**
se las comió, lloró tanto que **las lágrimas le lavaron la pintura** y quedó
azul. Por eso teme a los ratones.

**La historia por etapas** ✅ (Fandom):
- **Manga**: de **diciembre de 1969 a 1996**, en seis revistas de
  Shogakukan; 45 tomos *Tentōmushi*. *CoroCoro Comic* nace en 1977 como su
  revista insignia.
- **Anime**: **1973** (corto, poco éxito); **1979-2005** (1787 episodios,
  voz de Nobuyo Ōyama); **2005-hoy** (rediseño, voz de Wasabi Mizuta).
- **Películas**: **una al año desde 1980** (Toho), más aventureras, con
  temas de ecología y tecnología; algunas sobre mitos (Atlántida, *Viaje al
  Oeste*, *Las mil y una noches*). En 2013, con *El museo de los artilugios
  secretos*, **superó a Godzilla** en entradas acumuladas (100 millones
  contra 99).
- **Momentos clave**: 2008 embajador anime; 2011 abre el **Museo Fujiko F.
  Fujio** en Kawasaki; 2012 *TIME* y la residencia en Kawasaki; 2014 *Stand
  by Me*; 2020, 50.º aniversario; 2026, película 45.
  > La ficha de Fandom fecha el nombramiento de embajador en 2008 y en otra
  > frase habla de 2012 ⚠️. El comunicado oficial del ministerio es de
  > **marzo de 2008** ✅.

**Símbolos y vocabulario** ✅ (fichas de Fandom):

| Símbolo | Japonés | Cómo es |
|---|---|---|
| **Puerta a cualquier lugar** | どこでもドア | puerta **rosa**, color de ficha `#F17BAF`; lleva a donde pienses |
| **Takecopter** | タケコプター | hélice **amarilla** en la cabeza, color de ficha `#FFC107`; en inglés *The Hopter* |
| **Linterna pequeña** y grande | スモールライト | linterna verde con base naranja y amarilla que encoge (la grande agranda) |
| **Cabina «¿Y si…?»** | もしもボックス | cabina de teléfono que cumple un «qué pasaría si…» |
| **Bolsillo 4D** | 四次元ポケット | media luna blanca; el de Dorami, con rayas rojas cruzadas |
| **Cascabel** | 鈴 | amarillo, en collar rojo; símbolo de su identidad (película 2013) |
| **Máquina del tiempo** | タイムマシン | plataforma plana con mandos (hoja `objetos_01.jpg`, n.º 73); se entra por el cajón del escritorio |
| **Logo** | ドラえもん | desde 2005, sólo la palabra, sin adorno; el de **Fujiko Pro** en todo lo oficial |

## 19 · Tres conceptos para la lámina de #recursos

Los tres usan **un objeto real en un sitio real** de la serie, y el texto va
**en el objeto**, no en una burbuja. **Segunda pasada**: los conceptos no
cambian de idea, pero ya llevan **fondos oficiales medidos, poses vistas con
minuto, hex medidos y números de hoja**; y el «fondo de colores» del invento
ya se vio (rayos con destellos, hoja `objetos_01.jpg` n.º 58).

### Concepto A — «El catálogo de la tienda del futuro» (el recomendado)

**La idea**: en la serie, Doraemon **no inventa** los inventos: los **pide
por catálogo** a los Grandes Almacenes del Futuro, mete el pedido en el
cajón y llegan ✅ (§5.1). Algunos los **compra**, otros los **alquila**, y a
veces le mandan **muestras gratis** ✅. Es #recursos tal cual: un catálogo
donde cada cosa tiene su ficha, su precio (Gratis / De pago) y sus reglas.

- **Objeto y sitio**: el **escritorio de Nobita** en su cuarto de tatami,
  por la tarde. **El cajón abierto** deja salir el brillo del túnel del
  tiempo. Encima, y **cayendo hasta el tatami** (mide dos tatamis ✅),
  el **catálogo gigante abierto**. Asomando del cajón, el **sobre del
  pedido**. Todo en **Blender**: escritorio, cajón, catálogo con páginas
  curvadas, sobre de papel, tatami CC0
  ([Poly Haven](https://polyhaven.com/a/tatami_mat)).
- **Referencias**: el fondo oficial del **cuarto de Nobita, lado del
  escritorio** (hoja `fondos_01.jpg` n.º 1,
  [Wallpaper04, 1280×894](https://www.dropbox.com/s/vnho086qmwv4y0v/Wallpaper04.jpg?dl=1)),
  con su paleta medida `#C1DBAA`, `#D3B177`, `#E7EBE6` (§5.2); medidas del
  cuarto en [Sketchfab, CC BY de Cre8t!ve V!be](https://sketchfab.com/3d-models/none-7ac2289be8be408292b29a06f8f40a71);
  el cajón abierto de la [figura oficial](https://hobby.dengeki.com/news/953237/);
  el túnel del cajón en la hoja `objetos_01.jpg` n.º 73.
- **Personaje**: **Doraemon**, de pie junto al escritorio, **una mano
  dentro del bolsillo y la otra levantando un invento** (pose 2 de §15,
  *Stand by Me* 00:11:31, o la 3, serie 2006-11-10 · 00:16:23). Pose
  **vista** para el cuerpo: los brazos abiertos de «El Pueblo de Nobita»
  [0:30](https://archive.org/download/episodio-737-chip-de-reservacion/Episodio%2001%20-%20El%20Pueblo%20de%20Nobita.mp4?t=30);
  color del retrato oficial 2005 (azul `#1D99C8`, rojo `#E02333`, cascabel
  `#FCDC2A`) y el **Poko** en la boca. Detrás, pequeño, **Nobita** asomado
  al catálogo (pose de «pedir»; camiseta `#FDD23C`).
- **Cómo habla**: el **anuncio del invento**, con corchetes japoneses y
  ¡!, grande, en **Fredoka**: «**｢Recursos｣！**». Debajo, su frase: «**¡Chan!
  Aquí cabe de todo.**» (de *Stand by Me* 00:06:18). **Sin globo**: la frase
  va sobre el **fondo de rayos azules con destellos** del momento del
  invento, recortado en círculo detrás de él, con la letra roja `#E02333`
  y borde blanco de la cartela (hoja `objetos_01.jpg` n.º 58) ✅. Si es el
  fondo de antes o de después de 2024, sin saber ⚠️.
- **Dónde va cada texto**:
  - **Portada del catálogo**: «Recursos» + «Lo que le sirve a los demás».
  - **Página abierta, lista con dibujitos**, una línea por cosa y con su
    icono: «Programas», «Plantillas», «Pistas sin voz», «Efectos»,
    «Tutoriales».
  - **Recuadro de «condiciones de pedido»** en la página: «Un hilo por
    recurso» y «**Nada pirata. Ni cracks.**» (con un sello rojo, como el de
    un producto prohibido).
  - Guiño para un servidor de voz: en la página, el invento de muestra es
    el **caramelo «Voice Thickener» (コエカタマリン)**, con su cartela
    (hoja `objetos_01.jpg` n.º 85).
  - **Sobre del pedido**, escrito a mano en **Klee One**: «Lee el hilo
    fijado antes de colgar».
- **Cómo no queda plano**: tres luces (**ventana cálida** de lado, **brillo
  frío del cajón** desde abajo, el fondo de colores detrás de Doraemon); **el Takecopter
  desenfocado** en primer plano, en la esquina del escritorio; el catálogo
  **se sale del escritorio** hacia la cámara; páginas curvadas con sombra.
- **Lámina 2**: el **índice del catálogo** con **15 pestañas de colores**,
  una por etiqueta: 8 de «Qué es» en azul, 2 de precio en rojo, 4 de
  sistema en verde y **«Verificado» como un sello dorado** en la esquina.
  Aquí **Dorami** (la segunda más querida, la ordenada) señala las
  pestañas.

### Concepto B — «El Museo de los artilugios secretos»

**La idea**: la película de 2013 ✅. Un museo con **todos los inventos,
del primer modelo al último**, cada uno en su vitrina con su placa, y un
**ladrón de inventos** que es el malo. Encaja con «un hilo por recurso»
(una vitrina por cosa) y con «nada pirata» (el ladrón).

- **Objeto y sitio**: **tres vitrinas de cristal** en la sala del museo
  del siglo XXII, luminosa y blanca. Cada vitrina tiene **una placa de
  latón**. En Blender: vitrinas, pedestales, placas con el texto grabado.
- **Referencias**: la película (00:09:37 a 00:18:28, §2.2). ⚠️ Tampoco en
  la segunda pasada se vio la sala: hay que sacar capturas de la película.
  La ficha de la película en [Fandom](https://doraemon.fandom.com/wiki/Doraemon:_Nobita%27s_Secret_Gadget_Museum)
  da el equipo (dir. Yukiyo Teramoto, arte Makoto Dobashi).
- **Personaje**: **Doraemon** de guía, **señalando** una vitrina (pose 4
  de §15, «explicar»). Opcional: **Dorami** al lado, con un folleto.
- **Cómo habla**: su frase va en la **placa de bienvenida** de la entrada,
  como texto del museo: «**Bienvenidos**. Cada cosa en su vitrina.» (de
  00:16:14). Letra **Zen Maru Gothic** grabada en latón.
- **Dónde va cada texto**:
  - **Cartel de entrada**: «Museo de los recursos» + «Lo que le sirve a los
    demás».
  - **Placas de las vitrinas**: «Programas», «Pistas sin voz», «Efectos»
    (y en pequeño, «Plantillas y tutoriales»).
  - **Placa bajo la vitrina vacía**, con el cristal roto: «Nada pirata. Ni
    cracks.» (el hueco que dejó el ladrón).
  - **Cordón de visita** con cartelito: «Un hilo por recurso».
- **Cómo no queda plano**: **reflejos en el cristal**; una vitrina en primer
  plano desenfocada; luz cenital de museo que hace **sombras duras** bajo
  los pedestales; el fondo de la sala se pierde.
- **Riesgo**: la película **no tiene doblaje latino** que yo encontrara
  (§2.2); el museo lo conocen menos que el cuarto de Nobita.

### Concepto C — «El bolsillo mágico en el descampado» (el objeto del plan)

**La idea**: el **bolsillo mágico** (lo que proponía el plan) volcando
cosas, en el sitio más reconocible del barrio: **el descampado de las tres
tuberías**, donde **Gigante da sus recitales** ✅. Y Gigante, para cantar,
**necesita una pista sin voz**: el chiste se explica solo.

- **Objeto y sitio**: **las tres tuberías de cemento** del descampado, **de
  noche con focos de recital** (visto en [0:20](https://www.dailymotion.com/video/x3402n2?t=20):
  cielo `#395A81`, foco `#CA5E41`) o de día (fondo oficial, cielo `#67C3EE`).
  El atardecer no se midió ⚠️. Sobre la tubería de arriba, **cajas de cartón abiertas** (una
  por tipo de recurso) donde van cayendo los inventos. Un **cartel de madera
  clavado** en una tubería con las reglas. En Blender: tuberías, cajas,
  cartel, hierba.
- **Referencias**: el fondo oficial del **descampado** (hoja
  `fondos_01.jpg` n.º 3, [Wallpaper03, 1280×894](https://www.dropbox.com/s/uk3juifiwls5geh/Wallpaper03.jpg?dl=1)); fotos reales de
  la **Harappa** del museo Fujiko, con tuberías de verdad
  ([camera10.me](https://camera10.me/blog/photospot/fujiko-museum),
  [web del museo](https://fujiko-museum.com/hiroba.html)).
- **Personajes**: **Doraemon** sentado en la tubería, **sacando cosas del
  bolsillo** a manos llenas (la ráfaga de la serie, 2005-04-15 · 00:23:56).
  A un lado, **Gigante** con su micrófono, **brazo extendido al público,
  ojos cerrados, capa roja** (pose **vista** en el recital,
  [0:20](https://www.dailymotion.com/video/x3402n2?t=20)), o con su
  **guitarra** (hoja `personajes_01.jpg` n.º 17), junto a la caja «Pista sin
  voz». Camiseta `#F08E39` si va de diario.
- **Cómo habla**: Doraemon **canta el nombre de cada cosa** que saca, con
  los corchetes de la serie, en letras que salen del bolsillo hacia las
  cajas: «｢Programas｣！» «｢Plantillas｣！» «｢Pistas sin voz｣！». Letra
  **Rammetto One**.
- **Dónde va cada texto**:
  - **Letrero de madera** en la tubería, en dos líneas: «Recursos» arriba y
    «Lo que le sirve a los demás» debajo.
  - **Las cajas**: una palabra cada una.
  - **Cartel clavado** (pintura a mano, **Klee One**): «Un hilo por
    recurso», «Nada pirata. Ni cracks.», «Lee el hilo fijado».
- **Cómo no queda plano**: de noche, **focos de colores** del recital desde
  atrás y confeti delante (como en el clip); de día, sol lateral que
  alarga las sombras de las tuberías; **hierba alta desenfocada** delante;
  los objetos en el aire con desenfoque de movimiento.
- **Riesgo**: es la más cargada; las cajas tienen que ser pocas (cinco) y
  grandes.

### ¿Cuál primero?

**A**. Es la más fiel a cómo funciona la serie (**comprar, alquilar o
recibir gratis** en la tienda del futuro), tiene el fondo oficial del
cuarto, se hace entera en Blender, y da una **lámina 2 natural** (el índice
con 15 pestañas). **C** es la alternativa más alegre y más reconocible para
el público latino, y la que mejor usa lo **visto** en la segunda pasada
(el recital de Gigante). **B** es la más original, pero la película es la
menos conocida en Latinoamérica.

---

## 20 · Lo que no pude verificar (tras la segunda pasada)

**Resuelto en la segunda pasada** (antes estaba en esta lista): imágenes
vistas (3 hojas), licencias de Sketchfab (API), voz latina de Dorami,
Dekisugi y todo el reparto de 2005, frases latinas textuales (3 con minuto),
hex de ropa y tatami (medidos), fondo del invento (visto en cartelas).

**Sigue sin verificar** ⚠️:
- **El final de la descripción del canal** («ni cracks ni prog…»): cortado
  en el inventario.
- **Qué significa «Verificado»** en el foro, y quién lo pone.
- **Cuál es el fondo del invento de antes y cuál el de después de enero de
  2024** (sólo un post de X).
- **El sonido del invento en la serie de 2005**: «pua-pua… ¡te-tte-rē!» o
  «¡bikān!» (§7.1).
- **Quién dice** dos de las tres frases latinas (Whisper no separa voces),
  y las frases latinas más famosas («¡Doraemon, haz algo!», «qué remedio»)
  con minuto.
- **Doblaje latino de la película del museo (2013)**: sólo el de España y
  una «propuesta de doblaje» de fans en Doblaje Wiki; **no lo encontré**.
- **Actores del doblaje cubano de 1985** (sólo el estudio, ICAIC).
- **Quién canta el opening latino antiguo** («Doraemon, el gato cósmico…
  Ojalá mi sueño se…»).
- **Título del episodio** de cada fecha de emisión de §2.3 (el subtítulo
  no lo trae).
- **Caras**: la rabia de Doraemon; la tristeza de Doraemon, Shizuka,
  Gigante y Suneo; la vergüenza de todos, con minuto.
- **Poses vistas** de Shizuka, Suneo y Dorami solos.
- **Hex de Dorami** (no se midió).
- **Software 2D de Shin-Ei** y filtros de cámara del anime de TV.
- **Alturas oficiales** de los niños (no hay ficha única).
- *Key visuals* de la serie de TV y portadas de Blu-ray; el arte de
  *Granblue Fantasy*; un cosplay bien hecho.
- «Lo tuyo es mío y lo mío es mío» de Gigante: no salió en los subtítulos
  de 2005-2006 revisados.
- **Vistas de TikTok** de los *fandubs*.

## Cumplimiento del encargo

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | 3 hojas miradas (96 piezas con tamaño), 5 retratos oficiales 2005, cel de producción 2048×1632, hoja de modelo de 1973, 83 portadas de tomo, artbook del 50.º aniversario, 5 fondos oficiales medidos; poses vivas: guitarra, vuelo, béisbol, grupo (§3.0, §3.5). **Falta** ⚠️: *key visuals* de la serie de TV y portadas de Blu-ray |
| 2 · Fotogramas de escenas icónicas con capítulo y minuto | ⚠️ | 21 fotogramas **vistos** con minuto y enlace (§2.4), pero de copias de **720p** (Dailymotion, Internet Archive), no 1080p; las escenas de *Stand by Me* y el museo llevan el minuto del subtítulo 1080p, sin fotograma; la boda, sin clip |
| 3 · Fan art y 3D con licencia | ✅ | 12 modelos de Sketchfab con licencia **por la API** (CC BY, uno «Free Standard» avisado); fan art de Safebooru con origen en Pixiv y X; renders de ArtStation; fotos CC de Flickr (§4) |
| 4 · Fondos, luz, paleta y texturas | ✅ | paleta **medida** en 5 fondos oficiales y 9 fotogramas, con hex y % (§5.2); luz por sitio (§17); tatami, madera y papel CC0 (§5.3) |
| 5 · Tipografía, una por uso, con tildes | ✅ | **una letra por uso** (§6.3) con letras comprobadas con fontTools; Dora-e-moji avisada (sin letras latinas, uso personal); cartelas del invento vistas. El trazo del logo japonés sigue sin fuente ⚠️ |
| 6 · Cómo hablan en pantalla | ✅ | el momento del invento y su **cartela vista** (rayos de color, letra con borde); subtítulos con corchetes ｢ ｣; cuadro de *Story of Seasons*; qué NO hacer (§7). Quedan ⚠️: el sonido de 2005 y el fondo de 2024 |
| 7 · Personajes y encuestas | ✅ | Mynavi 2025, Nlab 2022, Macromill, ranking.net, **AniList** y Reddit; Doraemon 1.º; Dorami 2.ª entre jóvenes japoneses (§9) |
| 8 · Doblaje latino, dos fuentes | ✅ | **API de Doblaje Wiki** + dubdb, ANMTV, TVLaint, Desde la Cuna, FUNiAnime: 5 épocas (con el cubano de 1985), repartos completos por temporada; corregidos Jennifer **Medel** y los tres Nobitas; 3 frases latinas textuales con minuto (§10) |
| 9 · Música | ⚠️ | openings japoneses y latinos (el antiguo **oído** con Whisper, dos letras explicadas), endings latinos, 3 discos de banda sonora, sonido del invento (§11, §7.1). **No sé** qué tema suena en la escena del padre de Shizuka; AnimeThemes caído |
| 10 · Vídeos con minuto | ✅ | 7 vídeos mirados con minuto y `?t=` (§2.4, §12); *fandubs* con vistas (Punto 22). YouTube y TikTok, sin minuto ⚠️ |
| 11 · Videojuegos | ✅ | *Story of Seasons* 1 y 2 (cuadro con nombre encima, acuarela con dos reseñas, español latino en Steam), *Dorayaki Shop Story*, *Granblue*; 18 capturas de Steam 1920×1080 enlazadas, sin abrir una a una ⚠️ |
| 12 · Lo que ama el fandom y qué NO hacer | ✅ | memes («Handsome Gian», Dora-naki, Irwin Daayán de Suneo a Doraemon), lista de errores con el Poko, la falda de Shizuka y el bolsillo de Dorami (§14) |
| 13 · Carácter, forma de hablar y caras | ⚠️ | cada personaje con historia, miedos, cómo se expresa y dinámicas (§8); **tabla de caras por emoción** con minuto. **Huecos**: rabia de Doraemon, tristeza de 4 de los 5, vergüenza de todos (7 episodios mirados sin hallarlas) |
| 14 · Poses con minuto | ⚠️ | 9 poses **vistas** con minuto (§15.0), 8 de las hojas (§15.1) y las tablas de subtítulo; Doraemon y Nobita llegan a 6-10. **Shizuka, Suneo y Dorami** sólo 2-3, deducidas del subtítulo |
| 15 · Vestuario con hex | ✅ | **12 hex medidos** con Pillow en retratos oficiales y cel (§16); corrige la falda de Shizuka (granate). Dorami sin medir ⚠️ |
| 16 · Ciudades y fondos de pantalla con tamaño y autor | ✅ | 5 oficiales medidos (1280×894-929); 9 de Wallhaven con tamaño, ♥ y autor u origen (§17) |
| 17 · Guía para IA de imagen y de texto | ✅ | rasgos fijos, paleta medida, línea, etiquetas de Danbooru, referencias por número, vocabulario de expresiones; **IA de texto**: reglas de voz por personaje y frases reales por emoción (§18) |
| 18 · Estilo y técnica, cómo replicarlo | ✅ | Shin-Ei, Shirogumi, 3ds Max, V-Ray, Nuke y ACES (dos fuentes); la entrevista de CGWorld (goma y plástico del futuro, línea como textura, Poko); guía de Photoshop y Blender. Software 2D y filtros, no encontrados ⚠️ |
| 19 · Texturas 2D | ✅ | trama del manga comprobada (casi ninguna), sin estampados en la ropa, emblema «G», bolsillo de Dorami, tatami y papel CC0. Pinceles libres, no buscados ⚠️ |
| 20 · Gustos y detalles | ✅ | tabla de los 6 con cumpleaños (con revista y año), alturas, gustos, miedos y objeto (Punto 20). Alturas de los niños sin ficha oficial ⚠️ |
| 21 · Por qué la aman, y las escenas que hacen llorar | ⚠️ | razones con fuente, cifras, *TIME*, embajador anime; *Stand by Me* con minuto del padre (subtítulo), **88,4 %** que lloró, Dora-naki, taquilla. **Falta**: minuto de la despedida y qué música suena |
| 22 · Fan dubs y comunidad hispana | ✅ | 9 vídeos con canal y vistas (Dobla2 394 565), covers de opening y ending, gallego y catalán. TikTok sin medir ⚠️ |
| 23 · Colaboraciones, figuras y cosplay | ⚠️ | UNIQLO × Louvre (imagen medida), New Era, Converse (México), *Granblue Fantasy*, Toyota, café, gashapon; figura del cuarto. **Falta**: el arte de *Granblue* y un cosplay destacado; Fortnite no existe |
| 24 · Obras parecidas | ✅ | obras de Fujiko y de Shin-Ei, recomendaciones de AniList con votos, Tezuka (dos fuentes); láminas vecinas (Big Hero 6, Pokémon, Mafalda) y cómo no repetirlas |
| 25 · Mundo, historia y símbolos | ✅ | 5 reglas, por qué es azul, historia por etapas con hitos, 8 símbolos con japonés y color de ficha (Punto 25) |
| 3 conceptos de lámina | ✅ | catálogo del cuarto, museo, bolsillo en el descampado; ahora con fondos oficiales, poses vistas, hex y números de hoja (§19) |
| 40 fuentes distintas | ✅ | **124 dominios** enlazados (revisar.py) |
| Fuentes oficiales | ⚠️ | dora-world, Shogakukan, Shin-Ei, MOFA, Steam, Netflix, Columbia; entrevistas al staff de *Stand by Me* **abiertas** (CGWorld, ITmedia). **Falta**: hojear el artbook y entrevistas del anime de TV |
| Otros idiomas | ⚠️ | japonés e inglés a fondo; chino sólo un autor en Bilibili; **coreano no** |
| Wikis, TV Tropes, TCRF, Wayback | ⚠️ | Fandom (inglés, español, japonés), Doblaje Wiki, dubdb, Lost Media, Scratchpad; TV Tropes y TCRF dieron 403; Wayback no se probó |
| Foros y comunidades | ✅ | Reddit por Arctic Shift, Yahoo! Chiebukuro, oshiete.goo, questant |
| Arte (Pixiv, ArtStation, DeviantArt) | ✅ | Pixiv y X por el origen de Safebooru; ArtStation (renders); DeviantArt no |
| Vídeo | ⚠️ | Dailymotion e Internet Archive mirados; YouTube sólo por búsqueda (sin ver análisis con minuto); TikTok enlazado sin medir |
| Código y recursos | ✅ | GitHub (subtítulos, letras), Sketchfab por API, Poly Haven, ambientCG, MusicBrainz |
| Doblaje latino (Doblaje Wiki, ANMTV, Netflix, entrevistas) | ⚠️ | Doblaje Wiki por API, dubdb, ANMTV y 4 medios; créditos de Netflix y **entrevistas a actores en YouTube, sin ver** |
| Mirar los vídeos (opening, ending, tráiler, 3 escenas) | ✅ | opening latino 1979, ending (de España), tráiler de *Stand by Me*, recital, «El Pueblo de Nobita» y «Un mundo sin dinero», más 7 episodios cada 3 s; con Dailymotion e Internet Archive (plan B) |
| Frases latinas textuales de clips oficiales | ⚠️ | **no hay clips oficiales doblados** a la vista; las 3 frases salen de una grabación de TV subida a Internet Archive, transcritas con Whisper y revisadas a oído |
| Hojas de contacto | ✅ | 3 JPEG en `hojas/` (0,4-0,8 MB), miradas, con tabla de números (§3.0) |
| `referencias.json` | ✅ | ver el recuento en «Segunda pasada · qué cambió»: las imágenes medidas primero, luego fotogramas, 3D, fondos, juegos y páginas |

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- **Bloqueados** (curl o WebFetch): `doblaje.fandom.com`,
  `doraemon.fandom.com`, `www.anmtvla.com`, `www.desdelacuna.net`,
  `ppdtp.com`, `interfaceingame.com`, `dora-world.com`, `prtimes.jp`,
  `www.famitsu.com`, `api.sketchfab.com`, `api.polyhaven.com`,
  `ambientcg.com`.
- **Funciona**: WebSearch; GitHub por `git clone` (subtítulos y letras).
- `herramientas/investigar_serie.py` **no se pudo usar** (depende de
  Fandom): **no hay hojas de contacto** ni carpeta `hojas/`.

### Búsquedas web (50)

| # | Idioma | Búsqueda (resumida) | Qué salió |
|---|---|---|---|
| 1 | es | doblaje latino reparto Doraemon Nobita Laura Torres… | páginas de Doblaje Wiki; Laura Torres dejó a Nobita por la garganta |
| 2 | es | doblaje mexicano 2005, Disney, Boomerang | «104 medias horas»; sin reparto |
| 3 | es | «Irwin Daayán» «Laura Torres» «Cristina Hernández» | reparto de la película de Netflix |
| 4 | es | Quédate conmigo Doraemon, reparto, New Art Dub | estudio, director y traductora ✅ |
| 5 | es | Doraemon 1979, «el gato cósmico», primera voz | doblaje de los 80 (ESM, Carlos Carrillo) |
| 6 | es/en | dubdb «Doraemon, el gato cósmico» | 1999-2011, Chilevisión |
| 7 | es | quién hace la voz de Doraemon en 1999 | **Ricardo Tejedo** |
| 8 | es | ANMTV 2014, comienza doblaje | Armando Coria, Irwin Daayán, Laura Torres |
| 9 | es | nombres latinos de los inventos | bolsillo mágico, puerta mágica, gorrocóptero |
| 10 | es | Gigante «lo tuyo es mío», frases | canción en la wiki española; Arjona |
| 11 | ja | ドラえもん キャラクター 人気投票 | Nlab 2022, Mynavi 2025 |
| 12 | ja | マイナビ 20～30代 TOP5 | **Dorami 2.ª**, por delante de Nobita |
| 13 | ja | ひみつ道具 人気ランキング | puerta a cualquier lugar 1.ª; Takecopter el que más sale |
| 14 | ja | 効果音 テッテレー 大山 水田 | los dos sonidos; el falso «te-re-re» |
| 15 | ja | 道具を出すシーン 背景 演出 2005 | post de X sobre el cambio de fondo en 2024 |
| 16 | ja | PPDTP, cómo dibujar la escena en PowerPoint | nada concreto (página bloqueada) |
| 17 | en | Doraemon logo font | Britannic (de pago), letra de fan en dafont |
| 18 | en | Doraemon color palette hex | paletas de fans |
| 19 | en | sketchfab Doraemon anywhere door | 4 modelos |
| 20 | ja | のび太の部屋 間取り 土管 | 6 tatamis; figura oficial del cuarto |
| 21 | ja | 公式 バーチャル背景 | **5 fondos oficiales** (dora-world 1399) |
| 22 | ja | プロフィール 129.3cm 2112年 | ficha de Doraemon; por qué es azul |
| 23 | ja | リニューアル 2005 インタビュー | director Kōzō Kusuba; ninguna entrevista abierta |
| 24 | ja | ドラミ プロフィール | ficha de Dorami |
| 25 | es | Dorami voz latina | **nada** |
| 26 | es | opening latino, quién canta | **Maggie Vera** |
| 27 | en | Doraemon Story of Seasons dialogue box | descripción del cuadro |
| 28 | en | Kairosoft Dorayaki Shop Story | tienda en pixel art, 2024 |
| 29 | ja | 未来デパート カタログ タイムパトロール | **la tienda del futuro, alquiler y muestras gratis** |
| 30 | ja | 未来デパート カタログ 登場話 | tomos 42 y Plus 3; la tienda real de Odaiba |
| 31 | ja | 漫画 ひみつ道具 登場コマ | número de inventos; nada de viñetas |
| 32 | ja | オープニング 歴代 | mao, Rimi Natsukawa, Gen Hoshino |
| 33 | es | memes Latinoamérica, final, coma | la leyenda del coma; nombres «Robotín» |
| 34 | ja | のび太 特技, しずか, ジャイアン | talentos y gustos |
| 35 | ja | 映画 2026 海底鬼岩城 | película 45, voces japonesas |
| 36 | en | tatami texture CC0 | Poly Haven, ambientCG |
| 37 | en | fan art ArtStation Blender Nobita room | 3 renders, modelo del cuarto |
| 38 | ja | 藤子・F・不二雄ミュージアム はらっぱ | el descampado real con tuberías y puerta |
| 39 | ja | 描き方 頭身 | consejos de fans para dibujarlo |
| 40 | es | película 2013 museo, título latino | título de España; no hay doblaje latino a la vista |
| 41 | ja | 背景 変わった 2024 | sólo el mismo post de X |
| 42 | es | tráiler Quédate conmigo 2 latino | tráiler en YouTube; estreno 24-dic-2021 |
| 43 | es | «Maggie Vera» opening | confirmado |
| 44 | es | «Abraham Vega» Gigante | confirmado |
| 45 | ja | てんとう虫コミックス 表紙 一覧 | 45 tomos, 821 historias |
| 46 | es | frases famosas del doblaje latino | **nada** fiable |
| 47 | ja | のび太 服 黄色 しずか ピンク | colores de la ropa ✅; 137 camisetas |
| 48 | ja | ひみつ道具 出す 背景 水田版 | el nombre sale escrito en pantalla ⚠️ |
| 49 | ja | ペタリハンド, 3 mm | manos y flotar ✅; el bulo de la asociación de padres |
| 50 | ja | STAND BY ME 白組 山崎貴 八木竜一 | estudio y directores; entrevistas |

### GitHub (sin cupo)

- [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror):
  subtítulos japoneses de *Stand by Me Doraemon* (Erai-raws), de la película
  del museo (Netflix) y de **66 episodios** de la serie de 2005-2006. De ahí
  salen todos los minutos.
- [google/fonts](https://github.com/google/fonts): 18 familias bajadas y
  comprobadas con fontTools (§6.2).

### Fuentes consultadas por tipo

- **Oficiales**: dora-world.com (fondos, tienda), doraeiga.com/2026,
  Shin-Ei, Shogakukan (manga), Columbia (música), Museo Fujiko F. Fujio,
  Netflix, Steam.
- **Entrevistas al staff**: eiga.com y CGWORLD sobre *Stand by Me*
  (encontradas, no abiertas en la primera pasada; CGWORLD sí en la segunda).
- **En japonés**: Nlab, Mynavi, Macromill, pixiv, nokikero, futaman,
  Honcierge, Precious, numan, doranew, hatosan, @DIME, Famitsu, Anime!Anime!,
  eiga.com, Chiebukuro.
- **En inglés**: Wikipedia, IMDb, Can I Play That?, RPGFan, Kairosoft Wiki,
  brandpalettes, fontmeme, dafont.
- **Wikis de fans**: Doblaje Wiki, dubdb, Doraenciclopedia, Lost Media Wiki,
  Fandom JP (sólo por el buscador).
- **Doblaje latino**: ANMTV, TVLaint, Desde la Cuna, FUNiAnime,
  animeargentina.net, TikTok de Laura Torres.
- **Arte y 3D**: Sketchfab, ArtStation, The Rookies, Blender Artists,
  MakerWorld, Printables, Poly Haven, ambientCG.
- **Vídeo**: YouTube (tráileres, opening latino, efecto de sonido), TikTok.
- **No usé**: TV Tropes, The Cutting Room Floor, Reddit, Arctic Shift,
  Wayback Machine, Tumblr (bloqueados o sin resultados útiles), ni coreano
  ni chino (la obra es japonesa y con el japonés bastó).

### Lo que NO encontré

- Entrevista abierta al staff de la serie de TV sobre el diseño.
- Hojas de modelo oficiales.
- El diseño del fondo del momento de sacar un invento.
- Frases del doblaje latino verificadas.
- Voz latina de Dorami.
- Doblaje latino de la película del museo.
- Fan art 2D con autor verificado.
- Minutos exactos dentro de los vídeos de YouTube.

### Segunda pasada (24-sep-2026, red abierta, equipo de 4 + redactor)

**Qué respondió y qué no**: Doblaje Wiki, Fandom (en inglés y español),
dubdb, ANMTV, Arctic Shift, Dailymotion (API), Internet Archive, Sketchfab
(API), Wallhaven, Safebooru, Openverse, AniList, Steam, MusicBrainz,
dora-world (HTML crudo), Shogakukan, CGWorld e ITmedia **sí**. YouTube
(vídeo: pide sesión; la búsqueda de `yt-dlp` sí funciona), AnimeThemes
(522), TV Tropes y The Cutting Room Floor (403), Wikipedia por API (429),
gbf.wiki (Cloudflare) y TikTok **no**.

**Herramientas**:
- `recolectar.py` (datos de AniList, Doblaje Wiki, Fandom, Danbooru,
  Safebooru, Wallhaven, Sketchfab, Openverse, Dailymotion, Internet
  Archive, MusicBrainz, Steam y Reddit).
- `investigar_serie.py --serie "Doraemon" --wiki doraemon` con las páginas
  Doraemon, Nobita Nobi, Shizuka Minamoto, Takeshi Gouda, Suneo Honekawa, y
  una segunda tanda con 4D Pocket, Anywhere Door, Time Machine, Small Light,
  Big Light. Hojas miradas; el redactor las volvió a mirar y corrigió dos
  números.
- `fotogramas.py`: 7 vídeos de Dailymotion e Internet Archive (21
  fotogramas mirados) y 7 episodios más de Internet Archive cada 3 s (unos
  45 minutos) buscando caras.
- `voz.py` (Whisper): el opening latino antiguo y «El Pueblo de Nobita».
- `estilo.py` y Pillow: 11 fotogramas, 5 fondos oficiales y los retratos
  oficiales (hex de §5.2 y §16).
- `yt-dlp ytsearch`: 7 búsquedas de *fandubs* y covers.
- API de Doblaje Wiki: *Doraemon (1979)*, *Doraemon (2005)*, *Quédate
  conmigo, Doraemon* (wikitext completo).
- El redactor bajó 2 fondos de Dropbox para comprobar cuál era cuál.

**Búsquedas web (unas 20, en cuatro partes)**:

| Idioma | Búsqueda (resumida) | Qué salió |
|---|---|---|
| es | Doraemon fandub español YouTube canal doblaje fans | Dobla2, ParodiAnime, covers |
| es | cover opening español latino «El gato cósmico» | Lissette Chan, Unkos Channel |
| es | cumpleaños Nobita Suneo Gigante Shizuka altura databook | nokikero; alturas que no coinciden |
| es | escena que hace llorar «Sayonara Doraemon» reacción | *Adiós, Doraemon…* |
| es | ventas manga tomos récord premios | 250-300 millones ⚠️ |
| en | why beloved analysis nostalgia generations | Medium, Japan Times |
| en | Stand by Me final scene audiences cry box office | 88,4 %, Variety |
| en | 2008 anime ambassador foreign ministry | MOFA, ANN, CBC |
| ja | スネ夫 ジャイアン しずかちゃん 誕生日 身長 体重 公式設定 | nokikero, oshiete.goo |
| ja | ドラえもん なぜ人気 理由 世代を超えて | tamatebox, ampmedia |
| ja | STAND BY ME ドラえもん ラストシーン 号泣 感想 | eiga.com, Cinematoday |
| ja | ジャイアン のび太 スネ夫 しずか セリフ 口癖 話し方 | fichas de personaje |
| es/en/ja | Stand by Me 3DCG Shirogumi · セルルック 3DCG 質感 インタビュー · 3ds Max 白組 | CGWorld, ITmedia |
| en | Shin-Ei RETAS Toon Boom TVPaint software | nada específico ⚠️ |
| en/es | Fujiko F. Fujio influencias Tezuka · series parecidas Perman Kiteretsu | Toons Mag, Fandom |
| ja | 道具を出す 背景 2024年1月 変更 · 効果音 1979 2005 ちがい | el mismo post de X; questant, Chiebukuro |
| en | Story of Seasons art style watercolor review | switchaboo |
| ja | ドラえもん ロゴ 書体 デザイン 由来 | Dora-e-moji; nada oficial |
| es/en | colaboraciones 2025-2026, artbook, Fortnite, gacha, cosplay, Granblue | UNIQLO×Louvre, New Era, Converse, Granblue; Fortnite no |

**Búsquedas en Dailymotion (API, sin cupo)**: doraemon opening / ending /
latino, «gato cósmico Maggie Vera», «stand by me doraemon trailer latino»,
desfile de inventos, final, museo, recital de Gigante, puerta, dorayaki,
descampado, habitación, capítulo completo latino, escena más triste, boda y
padre, llorando, cero en el examen.

**Internet Archive**: `q=doraemon` (2187 resultados), `title:("stand by me"
doraemon)` (15), `doraemon español latino` (el doblaje cubano de 1985 y la
colección de episodios doblados).

**Fuentes nuevas por tipo** (además de las de la primera pasada):
- **Oficiales**: dora-world (fondos bajados, artbook), Shogakukan (83
  portadas), MOFA (embajador anime), Steam (capturas), CGWorld e ITmedia
  (entrevistas al staff, **abiertas**).
- **Otros idiomas**: japonés (nokikero, Cinematoday, eiga.com, tamatebox,
  ampmedia, questant, oshiete.goo, cute-freefont), inglés (ANN, CBC, Japan
  Times, Variety, ARAMA! JAPAN, Hypebeast, Siliconera, GamerBraves,
  switchaboo, Toons Mag), chino (Bilibili, autor del fondo de Shizuka).
  Coreano: no se buscó ⚠️.
- **Wikis**: Doblaje Wiki y dubdb por API, Fandom en inglés por API,
  Scratchpad Wiki, AniList. TV Tropes y TCRF, 403; Wayback, no se llegó a
  probar ⚠️.
- **Foros**: Reddit r/Doraemon por Arctic Shift (poco activo).
- **Arte**: Safebooru (con origen en Pixiv y X), Danbooru (etiquetas),
  Wallhaven, Openverse/Flickr.
- **Vídeo**: Dailymotion, Internet Archive, YouTube (sólo búsqueda).
- **Código y recursos**: Sketchfab (API), MusicBrainz, GitHub (primera
  pasada).
- **Doblaje latino**: Doblaje Wiki (API), dubdb, ANMTV, un episodio doblado
  oído con Whisper.

**Lo que NO encontré en la segunda pasada** (con búsqueda hecha): el sonido
de sacar un invento fuera de YouTube; un clip limpio de la boda; poses de
Shizuka, Suneo y Dorami solos; la rabia de Doraemon y la vergüenza de
todos con minuto; el software 2D de Shin-Ei; filtros de cámara del anime;
segunda fuente del fondo de 2024; *key visuals* de TV y Blu-ray; arte de
*Granblue*; cosplay destacado; colaboración con Fortnite (**no existe**);
licencia clara del modelo de Shizuka; alturas oficiales; actores cubanos
de 1985; vistas de TikTok.
