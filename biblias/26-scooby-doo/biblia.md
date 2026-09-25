---
tags: [biblia, serie, laminas]
serie: "Scooby-Doo (¿Dónde estás?, Misterios S.A. y las películas)"
canal: "#dudas"
fecha: 2026-09-24
---

# Biblia · Scooby-Doo — para #dudas

> [!important] Cómo se hizo, y sus límites
> - **Dos fases.** Empecé con la red **cerrada** (Fandom, Doblaje Wiki,
>   Wikipedia y YouTube daban bloqueo) y trabajé con **búsqueda web** (44
>   búsquedas) y **GitHub**. A mitad de trabajo **se abrió la red** y
>   completé con las fuentes directas. Lo escrito en la primera fase está
>   **revisado** con las nuevas fuentes.
> - **Imágenes de la wiki**: corrí `herramientas/investigar_serie.py`
>   sobre **Scoobypedia** dos veces: 19 páginas generales (116 imágenes
>   grandes, 3 hojas, carpeta `herramientas/referencias/scooby-doo/`) y
>   las **25 páginas de episodios de 1969-1970** (75 imágenes, 2 hojas,
>   `herramientas/referencias/scooby-doo-clasico-1969/`). **Miré todas las
>   hojas** y bajé 30 originales para verlas a tamaño real y **medir
>   colores** con Pillow. Además monté una hoja con **27 fondos pintados
>   de 1969** del blog *Secret Fun Spot*. En `hojas/` van tres:
>   `hoja_01_clasico_1969.jpg`, `hoja_02_wiki_general.jpg` y
>   `hoja_03_fondos_1969.jpg`. Cito las imágenes así: **C-19** (hoja
>   clásica, n.º 19), **G-4** (hoja general, n.º 4), **F-22** (fondos, n.º
>   22).
> - **Doblaje**: leí **22 páginas de Doblaje Wiki por su API** (serie,
>   personajes, actores) y crucé con **ANMTV**, **SensaCine** y los
>   **vídeos oficiales de WB Kids Latino**.
> - **Minutos exactos**:
>   1. **Subtítulos en inglés con tiempos** (GitHub) de un episodio de
>      1978 y de las **dos películas de imagen real** (2002 y 2004)
>      ([mesutgurlek/Movie-Category-Classification-from-Subtitles](https://github.com/mesutgurlek/Movie-Category-Classification-from-Subtitles),
>      [imkira3/imkira3Keys](https://github.com/imkira3/imkira3Keys)).
>   2. **Subtítulos automáticos en español** (con `yt-dlp`) de **6 vídeos
>      oficiales de WB Kids Latino**: dan el minuto de frases del
>      **doblaje latino** («chicos entrometidos», «¡Caracoles!», «¡Cielos!»).
>      Son transcripciones automáticas: el minuto es fiable, la palabra
>      exacta puede tener errores.
>   3. **No hay subtítulos con tiempos de la serie de 1969** en GitHub.
> - **Datos**: la **base de datos de 603 episodios y películas** de
>   [TidyTuesday](https://github.com/rfordatascience/tidytuesday/tree/master/data/2021/2021-07-13)
>   (hecha a mano por un fan, *plummye*, en Kaggle). Las cuentas son mías.
> - **Otras**: API de **Sketchfab** (licencias comprobadas), archivo de
>   Reddit **Arctic Shift**, **Know Your Meme**, Scoobypedia por su API,
>   letras de [google/fonts](https://github.com/google/fonts) comprobadas
>   con fontTools.
> - **Lo que siguió bloqueado**: TV Tropes (403), The Cutting Room Floor
>   (403), Wikipedia (429, demasiadas peticiones), Poly Haven y ambientCG,
>   dafont, y parte de YouTube (429 en algunos vídeos: el vídeo
>   «Supercorte de chicos entrometidos» no se pudo leer).
> - **No vi los vídeos en movimiento**: vi fotogramas de la wiki y leí
>   subtítulos. Lo que describo de un gesto sin fotograma va marcado.
> - ✅ **confirmado**: dos fuentes, o el subtítulo o fotograma con su
>   minuto o número. ⚠️ **dudoso**: una sola fuente, o de memoria.
> - **Cómo nombro las series** (título latino primero):
>   «**¿Dónde estás?**» = *Scooby-Doo, Where Are You!* (1969-1970; en
>   latino se presentó como **«Misterio a la orden»** ✅).
>   «**El show**» = *The Scooby-Doo Show* (1976-1978).
>   «**¿Qué hay de nuevo?**» = *What's New, Scooby-Doo?* (2002-2006).
>   «**Misterios S.A.**» = *Scooby-Doo! Mystery Incorporated* (2010-2013).
>   «**Ponte en onda**» = *Be Cool, Scooby-Doo!* (2015-2018).
>   «**¿Quién crees?**» = *Scooby-Doo and Guess Who?* (2019-2021).
>   «**Película 2002**» y «**Película 2004**» = las de imagen real.

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, categoría **✦ LA ACADEMIA ✦**):

> **ıı・🙋・dudas** (foro) · 2 hilos · etiquetas: Doblaje, Canto,
> Locución, Edición, Del programa, Del micro, Resuelta, Sigue abierta —
> _Pregunta sin miedo, por tonta que te parezca. Un hilo por duda.
> Etiqueta la disciplina y marca «Resuelta» cuando lo esté._
> - 📌 📌 De qué va esto (0 msj) · adj: dudas.png
> - EJEMPLO · Se me oye el ratón al grabar, ¿cómo lo quito? (0 msj) · adj: —

Función según el encargo: **foro de dudas técnicas**, con dos estados:
**Resuelta** y **Sigue abierta**.

Sus vecinos en LA ACADEMIA son **#avisos-clases** (encargo 24,
Assassination Classroom) y **#material-de-clase** (encargo 25, My Hero
Academia). Esos dos son «el colegio». #dudas es **el sitio al que vas
cuando no entiendes algo**. Scooby-Doo encaja por otra razón: cada
episodio es **una pregunta que nadie sabe responder** («¿quién es el
fantasma?») y **siempre acaba resuelta**.

### Por qué Scooby-Doo le va como anillo al dedo a #dudas

| Lo del canal | Lo de la serie |
|---|---|
| **Una duda** | **Un misterio**. Cada episodio es uno. |
| «**Pregunta sin miedo**» | Shaggy y Scooby **tienen miedo de todo**, y aun así el misterio se resuelve. Es el chiste perfecto. |
| «**Por tonta que te parezca**» | Scooby y Shaggy encuentran las pistas **sin querer**, tropezando ✅ (lo dice la base de datos: Scooby es **quien más villanos atrapa**, 160 veces, más que Fred) |
| «**Un hilo por duda**» | «Un caso cada vez»: el episodio empieza con **el monstruo** y termina con **el desenmascarado** |
| **Sigue abierta** | «**¡Separémonos y busquemos pistas!**» (129 veces en la franquicia ✅ en la base de datos; la redacción latina exacta cambia ⚠️) |
| **Resuelta** | **El desenmascarado**: la máscara fuera, y «¡Y hubiera sido mío de no haber sido por esos **chicos entrometidos**!» (doblaje latino ✅, vídeo oficial 00:17:24). Y Fred: «Ya que **el caso está resuelto**…» (00:21:02 ✅) |
| Las etiquetas | Las **pistas** del tablero, cada una con su color |

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Dudas** | nombre del canal |
| 2 | **Pregunta sin miedo, por tonta que te parezca** | para qué es |
| 3 | **Un hilo por duda** | cómo se ordena |
| 4 | **Etiqueta la disciplina** | regla 1 |
| 5 | **Marca Resuelta cuando lo esté** | regla 2 |
| 6 | **Resuelta** | estado A (el desenmascarado) |
| 7 | **Sigue abierta** | estado B (seguimos buscando pistas) |
| 8 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Los textos de la lámina 2 (las etiquetas)

Las **ocho etiquetas** no caben bien en la lámina 1 sin saturarla.
Propongo **lámina 2**, en tres grupos. Encajan con la serie como **tres
tipos de pista** en el tablero:

| Grupo | Etiquetas | Pista de la serie |
|---|---|---|
| **De qué va** | Doblaje · Canto · Locución · Edición | fichas de sospechoso |
| **Dónde está el fallo** | Del programa · Del micro | huellas y lupa |
| **Cómo va** | Resuelta · Sigue abierta | máscara quitada / signo de interrogación |

(En la lámina, cada etiqueta va en su propio sitio: sin «·».)

> [!tip] El ejemplo del inventario ya es un misterio de Scooby
> «**Se me oye el ratón al grabar, ¿cómo lo quito?**»: un ruido raro que
> nadie sabe de dónde sale. Es literalmente el arranque de un episodio
> (un ruido en la casa encantada). Se puede usar tal cual en la lámina,
> como **ficha clavada en el tablero**, con Vilma señalándola.

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué Scooby-Doo encaja | Cada episodio es **una duda** («¿quién es el fantasma?») que la pandilla resuelve **buscando pistas**. Siempre termina igual: **la máscara fuera**. Y hay una escena que es literalmente #dudas: Shaggy pregunta «¿**nos lo explican otra vez** para que Scooby y yo entendamos?» y la pandilla se lo explica (*El show*, 1978, 00:19:44 ✅). |
| El objeto | **El tablero de pistas** (lo propone el plan). No sale tal cual en la serie clásica ⚠️ (lo busqué: no hay episodio con «tablero de pistas»). Sí salen: el **club de la pandilla** (película 2004, 00:58:30 ✅; cómics de DC, G-4 ✅), la **pared con máscaras colgadas** (F-22 ✅), el **museo con los disfraces de los villanos** (película 2004 ✅) y **las pistas** en cada episodio (ep. 2 «Una pista para Scooby-Doo», C-15 ✅). Propuesta en §19: **el tablero de corcho del club**, con fichas «Who's Who», la máscara colgada y la lupa. |
| El más querido | No hay encuesta oficial ⚠️. Scoobypedia (2010, 97 votos): **Scooby 39**, Daphne 22, **Shaggy 19**, Vilma 12, Fred 5 ✅. En Reddit (r/Scoobydoo) **Fred** divide (sale como favorito **y** como el menos querido) y **Shaggy casi nunca es el menos querido** ✅ (conté los comentarios). **Shaggy** es el rey del meme (Ultra Instinct ✅). Para #dudas: **Vilma explicando** y **Shaggy y Scooby preguntando**. |
| Quién habla en la lámina | Tres opciones: **Vilma** con la lupa frente al tablero (explica, resuelve), **Shaggy y Scooby** asomados con miedo (preguntan) o **Fred** quitando la máscara (Resuelta). Ver §19. |
| Cuadro de diálogo propio | **No es una burbuja blanca**. Lo propio de la franquicia: la **ficha «Who's Who»** de los cómics (recuadro amarillo con «REAL NAME», C-44 ✅), el **titular del periódico** «GHOST BUSTED!» (C-45 ✅), el **cartón de título** con letras amarillas estrechas (C-47 ✅), **fichas clavadas** en el corcho y el **letrero de la furgoneta**. Si hace falta globo, el **de los cómics de DC** (G-4 ✅). Ver §7. |
| Letras | **Luckiest Guy** (logo gordo y saltarín), **League Gothic** (letras amarillas de los títulos), **Mystery Quest** o **Creepster** (miedo), **Caveat** y **Permanent Marker** (a mano), **Special Elite** (ficha a máquina). Todas con tildes, ñ, ¿ y ¡ ✅. La fuente de fans «**Scooby Doo**» **no trae tildes ni ñ** (sirve para «DUDAS», sin tilde). **Butcherman no trae ¿**. |
| Voz latina | **1969** (SISSA, dir. Francisco Colmenero ✅): Scooby **Ismael Larumbe Sr.**, Shaggy **Arturo Mercado**, Fred **Luis de Alba**/Luis Bayardo, Daphne **María Santander**, Vilma **Linda Smith**. **1998-2015**: Scooby **Antonio Gálvez** ✅, Shaggy **Arturo Mercado** ✅, Fred **Luis Alfonso Padilla** y **Ricardo Mendoza** ✅, Daphne **Yolanda Vidal** ✅, Vilma **Irene Jiménez** ✅. **Desde 2015**: Scooby **Óscar Flores**, Shaggy **Miguel Ángel Ruiz**, Fred **Irwin Daayán**, Daphne **Carla Castañeda**, Vilma **Leyla Rangel** ✅. Ver §10. |
| Tono | **Miedo de broma**: noche azul y morada, luna, niebla verde, casas encantadas, pero con colores planos y alegres de los 60 (la furgoneta azul y verde con flores naranjas ✅). Da miedo **pero nunca de verdad**. |
| Juegos | **MultiVersus** (Vilma junta **pistas** y al llenar el medidor **resuelve el misterio**: llega la Máquina del Misterio y se lleva al villano ✅), **Night of 100 Frights** (2002), **Mystery Mayhem**, **Unmasked**, **LEGO Dimensions**. Ver §13. |

---

## 2 · Las escenas que sirven para #dudas (con minuto)

### 2.1 Lo que dice la base de datos (603 episodios y películas)

La base de datos de TidyTuesday (hecha a mano por un fan que vio **todo**
Scooby-Doo de 1969 a 2021) permite contar. Las cuentas son mías ✅:

| Qué | Cuántas veces | Para qué sirve |
|---|---|---|
| **«Zoinks»** (Shaggy) | **1229** | El grito más repetido de la franquicia |
| **«Jinkies»** (Vilma) | 503 | Su «¡Cielos!» del doblaje |
| **«Ruh-roh» / «Rooby-rooby-roo»** | 413 | Scooby |
| **«Jeepers»** (Daphne) | 247 | |
| **«¡Separémonos!»** (*split up*) | 129 | = **Sigue abierta** |
| **«Scooby-Doo, ¿dónde estás?»** | 76 | Cuando lo buscan |
| **Otro misterio** al final | 68 | = «otra duda, otro hilo» |
| **Tender una trampa** | 47 | Fred |
| **«¡Mis anteojos!»** | 45 | Vilma sin gafas |
| **«Chicos entrometidos»** (y variantes) | 189 finales con la frase del villano; «*you meddling kids*» tal cual, 65 | = **Resuelta** |

Quién hace qué ✅:

| | Fred | Daphne | Vilma | Shaggy | Scooby |
|---|---|---|---|---|---|
| **Atrapa** al monstruo | 132 | 29 | 41 | 77 | **160** |
| **Desenmascara** al villano | **102** | 37 | **94** | 13 | 23 |
| **Lo capturan** a él o ella | 71 | **91** | 74 | 85 | 83 |
| Da una **galleta Scooby** | 18 | **49** | 29 | 43 | 12 |

Lo que se saca de aquí:
- Quien **quita la máscara** es **Fred** (102) o **Vilma** (94). Para
  «Resuelta», cualquiera de los dos es fiel.
- Quien **atrapa** al monstruo es **Scooby** (160), casi siempre sin querer.
  Es el chiste de «por tonta que te parezca»: la pista la encuentra el
  que menos se lo espera.
- **Daphne** es la que más veces cae prisionera («Daphne en apuros»). La
  película 2002 se ríe de eso («Vienes con tu propia nota de rescate»,
  00:06:00 ✅).
- **La trampa de Fred** sale 47 veces y **funciona a la primera sólo la
  mitad**: 125 sí y 124 no ✅. Chiste útil para «Sigue abierta».
- **El monstruo era real** sólo en 112 de 603 casos. En el resto había
  **una persona** detrás ✅: el misterio **siempre tiene explicación**.
  Eso es #dudas: tu problema **tiene arreglo**.
- **Mejores notas en IMDb** por serie ✅: *Misterios S.A.* 8,29 de media
  (52 ep.), *¿Dónde estás?* 8,11 (25 ep.), *¿Quién crees?* 7,87.
  **La peor**: *Shaggy y Scooby-Doo detectives* 5,6.
- **El episodio mejor valorado** de toda la franquicia es el cruce con
  *Supernatural*, «**Scoobynatural**» (2018, 9,6). De la serie clásica,
  «**A Night of Fright Is No Delight**» (1970, 8,7) ✅.

### 2.2 El episodio 2 se llama «Una pista para Scooby-Doo»

El segundo episodio de la serie (20 de septiembre de 1969) es **«A Clue for
Scooby Doo»**: «**Una pista para Scooby-Doo**» ✅ (base de datos y lista de
episodios). El fantasma es el del **capitán Cutler**, un buzo que brilla
en verde. **Fred** le quita la máscara ✅. Es un buen guiño para la lámina:
**la pista** es el centro del canal.

### 2.3 Escenas con minuto (subtítulos con tiempos)

**A) *El show de Scooby-Doo*, «A Creepy Tangle in the Bermuda Triangle»
(16-9-1978).** Archivo: `Scooby Doo, Where Are You!.srt` en
[mesutgurlek/Movie-Category-Classification-from-Subtitles](https://github.com/mesutgurlek/Movie-Category-Classification-from-Subtitles/tree/master/NonImpairedSubtitles/Horror).
Lo identifiqué por el villano (Dr. Grimsley, los Hombres Esqueleto) en la
base de datos ✅. La traducción es mía.

| Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|
| 00:03:03 | Shaggy: «¡**Zoinks**! ¿Adónde se fue?» | El grito de Shaggy |
| 00:07:02 a 00:07:14 | Fred: «Vamos, háganlo **por una galleta Scooby**». «Ni hablar». «¿Y **dos**?». «¿**Tres**?» Los dos: «¡Ajá, ajá, ajá!» | **Cómo se convence** a Shaggy y Scooby: el soborno |
| 00:08:38 a 00:08:47 | Vilma: «**Alto ahí**. No nos vamos». Fred: «Vilma tiene razón. Podemos estar **a punto de resolver un gran misterio**» | Vilma **frena la huida** |
| 00:08:54 | Vilma: «**Empezaremos buscando pistas** por la isla» | **El arranque de cada caso** |
| 00:08:57 a 00:09:01 | «¿Allá arriba? ¿**A oscuras**?». Shaggy: «Mejor nos quedamos aquí cuidando el fuego» | La excusa del miedoso |
| 00:12:20 | Vilma: «Cuando lo sepamos, estaremos **más cerca de resolver** este misterio» | **Sigue abierta** |
| 00:14:29 | «No, **ni una pista**» | Duda sin resolver |
| 00:15:00 a 00:15:03 | Vilma: «Este misterio **empieza a tener sentido**». «Vamos, **sigamos buscando pistas**» | **Sigue abierta**, pero cerca |
| 00:19:39 | El comandante: «La Marina les agradece **haber resuelto este misterio**» | **Resuelta** |
| 00:19:44 a 00:19:47 | Shaggy: «¿Les importa **explicarlo otra vez**… para que Scooby y yo **entendamos qué pasaba**?» | **La escena de #dudas**: el que pregunta sin vergüenza |
| 00:19:49 a 00:20:12 | Fred, Vilma y Daphne **explican por turnos** cómo funcionaba el truco (el platillo era un holograma) | **Explicar**: cada uno una parte |
| 00:20:15 | «**Veamos quiénes son en realidad** estos Hombres Esqueleto» | **El desenmascarado** |
| 00:21:02 | Scooby: «¡**Scooby-Dooby-Doo**!» | El cierre de cada episodio |

**B) Película 2002 (imagen real, de James Gunn y Raja Gosnell).** Archivo:
`Scooby-Doo.srt` de [imkira3/imkira3Keys](https://github.com/imkira3/imkira3Keys/tree/main/Subtitles).

| Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|
| 00:01:06 | Vilma: «**Jinkies**» (en latino **no se tradujo** en esta película ✅, lo dice Doblaje Wiki) | |
| 00:04:51 | Vilma: «**Supe desde el principio** que no había ningún fantasma» | Vilma resuelve |
| 00:05:11 a 00:05:26 | «Fred, ¿cómo podía volar el fantasma?». Vilma: «**Yo puedo responder a eso. Miren**» | **Explicar**: la frase exacta para #dudas |
| 00:05:30 a 00:05:34 | El villano: «¡Y me habría salido con la mía si no fuera por **ustedes, chicos entrometidos**… **y su perro tonto**!» | **Resuelta** |
| 00:05:38 | «¡**Scooby-Dooby-Doo**!» | Celebrar |
| 00:05:47 | Vilma: «Fred, no puedo creer que **te llevaras el mérito de mi plan** otra vez» | Vilma, la que piensa |
| 00:06:05 | Vilma: «¡**Mis anteojos**!» | La manía |
| 00:06:21 a 00:06:25 | Shaggy: «Somos como **un banana split** enorme y delicioso. Fred, tú eres **la banana grande**» | Shaggy une al grupo |
| 00:26:57 | Fred: «Ya que estamos todos, **separémonos y busquemos más pistas**» | **Sigue abierta** |
| 00:36:45 | «Hemos dado con **un bufé de pistas**» | Muchas respuestas a la vez |
| 00:41:43 a 00:41:54 | Vilma: «Mis anteojos. **No encuentro mis anteojos**. Ayúdenme a encontrarlos» | Vilma perdida (no sabe) |
| 00:56:16 | «**Una parte del misterio, resuelta**» | Resuelta a medias |
| 01:17:56 a 01:18:19 | «Fred, ¿**cómo resolviste el caso**?». «Gracias a los poderes intuitivos combinados de Misterio a la Orden…» | Explicar al final |

**C) Película 2004, *Scooby-Doo 2: Monstruos desatados*.** Archivo:
`Scooby-Doo 2 Monsters Unleashed.srt` del mismo repositorio.

| Minuto | Qué pasa / qué se dice | Para qué sirve |
|---|---|---|
| 00:02:08 a 00:04:37 | Inauguran el **Museo de Criminología de Coolsville**: la pandilla **dona los disfraces de los villanos que desenmascaró** | **Las máscaras colgadas** como trofeo: idea para el tablero |
| 00:14:09 | Shaggy: «¡Ah, **pistas**!» | |
| 00:19:07 a 00:19:15 | Shaggy (le roba la frase a Fred): «Bien, pandilla. **Separémonos y busquemos pistas**». Y alguien protesta, Fred por el contexto ⚠️: «**¡Me robó mi frase!**» | **Sigue abierta** con humor |
| 00:19:30 a 00:19:36 | «Buscar pistas, buscar pistas». «¡Ajá! **¡Una pista!**» | Scooby y Shaggy **buscando** |
| 00:21:25 a 00:21:39 | Scooby: «¡Pistas!». Shaggy: «**Eso no son pistas, Scoob. Son cosas que quieres**». «¿Por qué iba a ser una pista **un cepillo de váter**?» | **La duda tonta**: «por tonta que te parezca» |
| 00:22:02 a 00:22:12 | «¡**Somos detectives**!». «¡**Encontraste una pista de verdad**!». «¡Encontré una pista!». «¡**Haz el baile de la pista**!» | **Celebrar**: el «baile de la pista» |
| 00:27:35 | «Al final **les quitamos la máscara** y dentro hay un señor asustado» | Resuelta: el miedo era nada |
| 00:46:09 | «Este sitio es **Pistilandia**, Scoob» (*Clue-topia*) | Muchas pistas juntas |
| 00:58:30 a 00:58:37 | «**El viejo club del instituto**. Aquí estaremos a salvo. Hace años que no veníamos» | **El sitio real** para el tablero |
| 00:59:28 | Fred: «Miren, **todas mis viejas herramientas**» | Fred y sus trampas |
| 01:00:32 a 01:00:37 | Vilma: «**Resolvíamos misterios por amor a ellos**, no para demostrar nada». «Y los misterios **se resolvían solos**» | El espíritu del canal |
| 01:24:00 | El villano: «¡Me habría salido con la mía si no fuera por **esos mocosos entrometidos**!» (*meddling punks*) | Resuelta |

### 2.4 Las frases que todo el mundo conoce (doblaje latino)

Fuentes: **Doblaje Wiki** (API, página de la serie de 1969) y los
**subtítulos automáticos en español** de los vídeos oficiales de **WB Kids
Latino** (con su minuto). Los vídeos:
[«Scooby-Doo expone a los malos»](https://www.youtube.com/watch?v=r1sQtlBZHHQ) (23:49, recopilación de *¿Dónde estás?*),
[«prepara la trampa»](https://www.youtube.com/watch?v=xZV_2-7OBRU) (29:15),
[«Computadoras»](https://www.youtube.com/watch?v=BtGo-X-jjP8) (6:49),
[«Mejor de Velma»](https://www.youtube.com/watch?v=fdqVXWBkr9g) (3:31) y
[«¡Velma sabe!»](https://www.youtube.com/watch?v=zY8Vgn-bqhc) (8:28).

| Inglés | Latino | Quién | Estado |
|---|---|---|---|
| *Jinkies!* | «**¡Cielos!**» («¡Cielos, un misterio!», *Computadoras* 00:01:56; *¡Velma sabe!* 00:03:59) | Vilma | ✅ Doblaje Wiki y vídeo |
| *Zoinks!* | «**¡Caracoles!**» (*prepara la trampa* 00:08:39) | Shaggy | ✅ Doblaje Wiki y vídeo |
| *Jeepers!* | «**¡Rayos!**», «¡Repámpanos!», «¡Recórcholis!», «¡Caracoles pintos!» | Daphne | ⚠️ sólo Doblaje Wiki |
| *Scooby Snacks* | «**Scooby-galletas**» (nombre creado en el doblaje de 1969 y que sigue hoy) | | ⚠️ sólo Doblaje Wiki (fuente fuerte) |
| *The Mystery Machine* | «**La Máquina del Misterio**» | | ✅ Doblaje Wiki y la guía de cuadros |
| *Mystery Inc.* | «**Misterio a la orden**» (clásica y películas desde 1998); «**Misterios S.A.**» (serie de 2010) | | ✅ Doblaje Wiki y ANMTV |
| *Malt Shop* | «**la fuente de sodas**» («Ya que **el caso está resuelto**, ¿por qué no nos vamos a **la fuente de sodas**?», *expone a los malos* 00:21:02 a 00:21:10) | Fred | ✅ vídeo (y Scoobypedia: tras resolver, van al Malt Shop) |
| *Danger-prone Daphne* | «**La peligrosa Daphne**» | | ⚠️ sólo Doblaje Wiki |
| *Let's see who you really are* | «**Ahora veamos quién está detrás de la** [máscara]» (*expone a los malos* 00:02:49); «**veamos quién es el impostor** que se encuentra detrás de…» (00:07:51); «**ahora veamos de quién se trata**» (*¡Velma sabe!* 00:05:00) | Fred o Vilma | ✅ vídeo y TikTok latino |
| *And I would have gotten away with it too, if it weren't for you meddling kids!* | «**¡Y hubiera sido mío de no haber sido por esos chicos entrometidos!**» (*expone a los malos* 00:17:24). Según Doblaje Wiki se dijo por primera vez en «**La noche de los pies helados**» (su ep. 21; es *Scooby's Night with a Frozen Fright*, 26-9-1970, el primero con *meddling kids* en la base de datos) | El villano | ✅ Doblaje Wiki y vídeo |
| (cierre del caso) | «**Bien, con eso terminó el misterio. Vamos a la fuente de sodas**» (*expone a los malos* 00:17:30 a 00:17:36) | | ✅ vídeo |
| (Vilma en *Misterios S.A.*) | «**Oigan, amantes de los misterios, habla Vilma**» (su programa de radio o vídeo; *Computadoras* 00:01:21 y *Mejor de Velma* 00:00:00) | Vilma | ✅ dos vídeos |
| (alguien a la pandilla) | «**Hola, señores, parece que necesitan una pista**» (*Computadoras* 00:05:25) | ⚠️ no sé quién la dice | ✅ minuto |
| *My glasses!* | «¡Mis anteojos!» | Vilma | ⚠️ de memoria (en latino alterna «anteojos», «lentes») |
| *Let's split up, gang!* | «Separémonos, pandilla» | Fred | ⚠️ de memoria |
| *Scooby-Dooby-Doo!* | igual | Scooby | ✅ |

> [!tip] «Chicos entrometidos» y «el caso está resuelto»
> Las dos palabras «**chicos entrometidos**» bastan para que cualquiera en
> Latinoamérica reconozca la escena ✅ (Wikipedia en español y Doblaje
> Wiki: la traducción «se mantiene intacta» en todas las producciones).
> El canal oficial **@GenWBLatino** tiene un vídeo llamado
> «**¡SUPERCORTE de “Chicos entrometidos”!**»
> ([YouTube](https://www.youtube.com/watch?v=qBIpQcjSyOk); no pude
> leerlo: YouTube dio 429). Para **Resuelta**, la frase de la serie es
> «**el caso está resuelto**» (00:21:02). Para cerrar con humor, «**vamos
> a la fuente de sodas**».

---

## 3 · Arte oficial y referencias visuales

### 3.0 Las hojas de contacto (mira esto primero)

Tres hojas en `hojas/` (JPEG de menos de 1 MB). Los números son los de
cada hoja; el original está en el `indice.json` de
`herramientas/referencias/<carpeta>/` y se baja con
`python herramientas/investigar_serie.py --bajar <carpeta> <n>`.

**Hoja C** = `hojas/hoja_01_clasico_1969.jpg` (episodios de 1969-1970,
carpeta `scooby-doo-clasico-1969`). Las mejores:

| N.º | Qué es | Tamaño real | Para qué |
|---|---|---|---|
| **C-15** | «Scooby encuentra algas brillantes»: **Shaggy sostiene la pista** (algas verdes que brillan), **Vilma inclinada con la mano en la cadera** mirándola, Scooby sentado. Ep. 2, «**A Clue for Scooby Doo**» | 1439×1079 | **La escena de la pista**: pose de Vilma «pensar» |
| **C-19** | La pandilla conoce al **Caballero Negro** en el museo (ep. 1). Fred de frente: **jersey blanco de cuello azul y pañuelo naranja**; Daphne con **medias rosas** | 1439×1079 | Vestuario exacto de 1969 |
| **C-10** | «VoodooDolls»: **muñecos vudú de la pandilla clavados con alfileres** en la pared (ep. «Which Witch is Which?») | 1440×1080 | **Los cuatro de pie en fila**, colores planos. Y un guiño: la pandilla literalmente «clavada» en un tablero |
| **C-24** | **Henry Bascombe** desenmascarado, con el traje del **Space Kook** («Spooky Space Kook») | 1438×1079 | **El villano sin máscara**: la cara de «señor normal» |
| **C-35** | El Hombre Lobo sorprende a **Fred leyendo un mapa** con Daphne, entre telarañas | 1024×768 | **Fred con un papel en la mano**: leer una pista |
| **C-39** | Shaggy y Scooby se topan con el **Creeper** | 1024×767 | Susto |
| **C-22** | **Scooby disfrazado de cebo** y Shaggy con gabardina y bombín | 1438×1079 | Disfraces |
| **C-6** | Vilma conduciendo **a ciegas** («Velma Driving Blind») | 1440×1080 | Vilma sin ver |
| **C-43** | **Hoja de modelo original** del Space Kook, «GHOSTLY SPACEMAN», © Hanna-Barbera, **8-8-1969** | 987×685 | **Tipo de línea** de 1969: contorno negro fino y limpio |
| **C-44** | Ficha «**Who's Who in Scooby-Doo**» de los cómics: THE SPACE KOOK, **REAL NAME: HENRY BASCOMB**, OCCUPATION, LURKING LOCATION, FIRST APPEARANCE, y el resumen del caso | 864×693 | **La ficha del caso**: un cuadro de texto propio de la franquicia (§7) |
| **C-45** | Viñeta de cómic: Dick Dastardly lee el periódico «**The Daily Babbler**» con el titular «**GHOST BUSTED!**» (fantasma atrapado) | 762×717 | **El titular = Resuelta** |
| **C-47 a C-70** | Los **cartones de título** de los 25 episodios: la pandilla **corriendo en fila** abajo y el título arriba en **letras amarillas estrechas** con contorno oscuro | 720×540 | **Tipografía y composición** (§6) |

**Hoja G** = `hojas/hoja_02_wiki_general.jpg` (páginas generales,
carpeta `scooby-doo`). Las mejores:

| N.º | Qué es | Tamaño real | Para qué |
|---|---|---|---|
| **G-4** | **El club de Misterio a la Orden** en los cómics de DC: salón con **estanterías, un sofá verde**, cojines, **una foto enmarcada de la pandilla con la furgoneta**. Daphne: «Hmm, qué raro…». Vilma: «¿Qué es lo raro?» | 2048×1536 | **El sitio real para el tablero** (concepto A) y los **globos de cómic** |
| **G-5** | Fachada del club (cómic «There's a Mummy in My Mineral Water») con la furgoneta aparcada | 2260×1372 | Exterior del club |
| **G-7** | La **casa compartida** de la pandilla (cómic) | 2037×1115 | Otro exterior |
| **G-9 a G-16** | Personajes de *Misterios S.A.* a 1920×1080 (Daphne, Fred, Scooby, Shaggy, grupo, furgoneta) | 1920×1080 | Si se usa el estilo de 2010 |
| **G-17** | Vilma de *Misterios S.A.*, de noche | 1920×1080 | |
| **G-23** | = C-15 (algas brillantes) | 1439×1079 | |
| **G-27** | **Vilma a gatas buscando sus gafas** («Velma loses glasses in Furgeson Estate») | 1428×1080 | Pose de Vilma perdida |
| **G-1 a G-3** | **Lupa de Vilma**: accesorio oficial de disfraz (Spirit Halloween), **verde agua con flores naranjas** como la furgoneta | 1583×2000 | **La lupa** para la lámina |
| **G-59, G-81, G-88, G-91, G-92** | Dibujos «**Original**» de cuerpo entero: Vilma, Daphne, Fred, Shaggy | 401 a 574 × 1149 a 1440 | Proporciones de pie |
| **G-79** | Cómic «**The Bed Sheet That Goes Boo**»: título en **letras rojas**, globo de Shaggy, créditos (rotulista **Nick J. Napolitano**) | 950×712 | Globos y rótulo de cómic |
| **G-87** | = C-45 (el periódico «GHOST BUSTED!») | 762×717 | |
| **G-100, G-101** | **Vilma pierde las gafas** («A Gaggle of Galloping Ghosts» y «It's Mean, It's Green…»): **a gatas en el suelo de madera**, las gafas delante | 768×576 | Pose de Vilma |
| **G-103 a G-107** | Cartones de título (A Clue for Scooby Doo, Hassle in the Castle, Jeepers It's the Creeper, **el logo «SCOOBY DOO, WHERE ARE YOU!»**, What a Night for a Knight) | 720×540 | Tipografía |
| **G-18 a G-21, G-34 a G-58** | Muchas **cajas de Scooby-galletas** de distintas series | 1124 a 1920 de ancho | La caja de galletas como objeto |

**Hoja F** = `hojas/hoja_03_fondos_1969.jpg`: **27 fondos pintados** de
las temporadas 1 y 2, tomados del blog
[Secret Fun Spot](https://secretfunspot.blogspot.com/2007/10/50-scooby-doo-background-paintings.html)
(720×540 cada uno). Los mejores: **F-8** la **Malt Shop** (la «fuente de
sodas»), **F-22** una **pared con máscaras colgadas** de clavos (¡el
trofeo de villanos!), **F-24** un cuarto con **mesa, vela verde y
calavera**, **F-10** castillo con luna, **F-15** casa encantada con
ventanas amarillas, **F-18** salón rojo con chimenea, **F-2** la sala de
la adivina (bola de cristal).

### 3.1 Quién dibujó a la pandilla (1969)

- **Creadores**: los guionistas **Joe Ruby y Ken Spears**, con el
  diseñador **Iwao Takamoto**, para Hanna-Barbera y la cadena CBS ✅
  (Wikipedia y Doblaje Wiki). Estreno: **13 de septiembre de 1969**,
  episodio «What a Night for a Knight» ✅ (Wikipedia y la base de datos).
- **Cómo nació**: el primer proyecto se llamaba «**Mysteries Five**»: cinco
  chicos en **un grupo de rock** que resolvían misterios, con un perro
  llamado «**Too Much**» (Mucho). CBS lo rechazó. **Fred Silverman** (jefe
  de la programación infantil de CBS) pidió **quitar el grupo de música y
  poner al perro en el centro**, con la amistad de Shaggy y el perro ✅
  (Wikipedia y [Cartoon Research](https://cartoonresearch.com/index.php/the-origin-of-scooby-doo/)).
  Otro título de trabajo fue «**Who's S-S-Scared?**» ✅.
- **El nombre**: Silverman lo sacó del «**doo-be-doo-be-doo**» que canta
  Frank Sinatra en «**Strangers in the Night**», oyéndola en un avión ✅
  (Wikipedia, [Cartoon Research](https://cartoonresearch.com/index.php/the-origin-of-scooby-doo/)
  y [RX Music](https://rxmusic.com/editorial/the-scooby-sinatra-connection/)).
- **El diseño de Scooby**: Takamoto le dio **barbilla hundida, manchas,
  cola larga y el lomo caído**. «Too Much» dudaba entre **gran danés y
  pastor inglés** y acabó siendo **un gran danés cobarde** ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Scooby-Doo_(character))).
  Cuenta la historia que Takamoto habló con una criadora de gran danés y
  **dibujó lo contrario** de lo que ella le dijo que era un buen ejemplar
  (patas arqueadas, barbilla hacia atrás) ⚠️ (de memoria; es anécdota muy
  repetida).
- **Fondos**: el ex de Disney **Walt Peregoy** fue el estilista de fondos
  del **primer episodio**; el estilismo lo siguió **Fernando
  Montealegre**. Pintaron los fondos **Ron Dias, Daniela Bielecka, Gary
  Niblett, Rolly Oliva, Peter Van Elk, Eric Semones, Curtiss D. Perkins,
  Richard Khim, Gino Giudice y Robert Gentle** ✅
  ([Secret Fun Spot](https://secretfunspot.blogspot.com/2007/10/50-scooby-doo-background-paintings.html),
  leído entero; y Heritage Auctions en la búsqueda). El autor del blog lo
  resume: «cielos de tormenta y sitios abandonados», con **la Malt Shop
  como único refugio** de la pandilla. **Paul Julian** pintó cuadros de
  desarrollo del **primer plano** del episodio 1 ✅
  ([Van Eaton Galleries](https://vegalleries.com/art/hanna-barbera/58/miscellaneous-hanna-barbera/scooby-doo-background-development-painting-by-paul-julian-id)).
  El diseñador de *layouts* fue **Alvaro Arce** ⚠️ (una fuente).
- **Misterios S.A. (2010)**: la desarrollaron **Mitch Watson, Spike
  Brandt y Tony Cervone**. El diseñador jefe de personajes fue **Derrick
  J. Wyatt** (1972-2021): le pidieron dibujar «al estilo de Iwao» y
  **no le salía**; ese intento es el estilo de la serie ✅
  ([podcast *Unmasked History of Scooby-Doo*, ep. 14](https://www.unmaskedsdpodcast.com/2020/09/18/uhsd-episode-14-derrick-j-wyatt/)
  y [Cartoon Brew](https://www.cartoonbrew.com/rip/derrick-wyatt-character-designer-on-teen-titans-transformers-and-scooby-doo-dies-at-49-211888.html)).

### 3.2 Dónde mirar arte oficial (en alta)

| Qué | Enlace | Qué tiene | Sirve para |
|---|---|---|---|
| **Hoja de modelo de la pandilla** (réplica) | [Choice Fine Art](https://choicefineart.com/products/mystery-gang-model-sheet-1) y [The Artifacts Gallery](https://www.artifactsgallery.com/art.asp?%21=W&ID=13442) | Los cinco de pie, con proporciones | **Rasgos que nunca cambian** |
| **Cel original** firmado por Bob Singer e Iwao Takamoto | [1stDibs](https://www.1stdibs.com/art/more-art/hanna-barbera-studio-artists-scooby-doo-original-cel-signed-bob-singer-iwao-takamoto-scooby-shaggy/id-a_13951682/) | **Shaggy y Scooby corriendo** | Pose de huida |
| **Diseños tempranos de Scooby** por Takamoto | [Traditional Animation (Facebook)](https://www.facebook.com/traditionalanimation/posts/artist-iwao-takamotos-early-designs-for-scooby-doo-hanna-barbera-1969/3120868467999808/) | Bocetos de 1969 | El perro antes de ser Scooby |
| **Fondos de producción** de 1969 | [Heritage Auctions: layout](https://comics.ha.com/itm/animation-art/concept-art/scooby-doo-where-are-you-background-layout-art-hanna-barbera-1969-/a/7193-97542.s), [Heritage: 2 fondos](https://comics.ha.com/itm/animation-art/painted-cel-background/scooby-doo-where-are-you-master-production-background-group-of-2-hanna-barbera-1969-total-2-original/a/7122-97678.s) | Pintura original, noche | **Paleta de los fondos** |
| **Fondo del primer plano** del ep. 1 | [Van Eaton: primera escena](https://vegalleries.com/art/hanna-barbera/236/scooby-doo-1969-present/scooby-doo-where-are-you-first-scene-background-development) | Desarrollo de fondo | La **luz de luna** clásica |
| **Cels con fondo** | [Van Eaton 7708](https://vegalleries.com/art/hanna-barbera/236/scooby-doo-1969-present/scooby-doo-where-are-you-production-cel-and-background-id), [7709](https://vegalleries.com/art/hanna-barbera/236/scooby-doo-1969-present/scooby-doo-where-are-you-production-cel-and-background-id-1), [fondo janhbbg6802](https://vegalleries.com/art/hanna-barbera/236/scooby-doo-1969-present/scooby-doo-where-are-you-production-background-id-janhbbg6802), [cel marhan12](https://vegalleries.com/art/hanna-barbera/236/scooby-doo-1969-present/scooby-doo-where-are-you-production-cel-id-marhan12) | Personaje plano sobre fondo pintado | **Cómo se integra** un personaje plano en un fondo pintado (clave para la lámina) |
| **50 fondos de Scooby-Doo** | [Secret Fun Spot (blog)](http://secretfunspot.blogspot.com/2007/10/50-scooby-doo-background-paintings.html) | 50 fondos de la serie de 1969 | **Sitios** y paleta |
| Fondos (Tumblr) | [atomic-chronoscaph](https://www.tumblr.com/atomic-chronoscaph/130721933298/scooby-doo-where-are-you-background-art) | Selección de fondos 1969-1970 | Idem |
| **Logo y su historia** | [1000logos](https://1000logos.net/scooby-doo-logo/) | Todos los logos | Tipografía (§6) |
| **50 aniversario** (2019) | [PR Newswire](https://www.prnewswire.com/news-releases/warner-bros-celebrates-50-years-of-scooby-doo-with-a-50-days-of-scooby-fan-and-family-celebration-300883329.html), [Toy Book](https://toybook.com/warner-bros-kicks-off-scooby-doo-50th-anniversary-celebration/) | «50 días de Scooby», del 26 de julio al 13 de septiembre de 2019; caja «**Mystery Mansion**» de la serie completa ✅ | Arte promocional de grupo |

### 3.3 Las poses que da el arte oficial (lo que el dueño pide)

El dueño se quejó de «salen de pie con una ropa». Scooby-Doo tiene muchas
poses vivas. Las que tienen número las vi en la hoja; las demás son de
memoria ⚠️:

- **La huida**: toda la pandilla **corriendo en fila hacia la derecha**,
  Scooby con Shaggy encima (cartones de título **C-47 a C-70** ✅). El cel
  de 1stDibs: Shaggy y Scooby corriendo.
- **El salto al brazo**: Scooby salta **a los brazos** de Shaggy (o de
  Fred) del susto.
- **La torre del miedo**: Scooby **encima de la cabeza** de Shaggy,
  temblando.
- **El desenmascarado**: Fred (o Vilma) **tira de la máscara** hacia
  arriba; el villano atado con cuerda o dentro de **la red de la trampa**;
  el sheriff al lado.
- **Vilma a gatas buscando sus gafas** en el suelo de madera, con la
  mano estirada; las gafas, delante (**G-100**, **G-101**, **G-27** ✅).
- **Vilma examinando la pista**: inclinada hacia delante, **mano en la
  cadera**, ceño fruncido (**C-15** ✅). Con **lupa** es el accesorio
  oficial (**G-1**), no una escena ⚠️.
- **Fred leyendo un papel** (un mapa) con Daphne al lado (**C-35** ✅).
- **La pandilla en fila, de pie** (los muñecos vudú, **C-10** ✅).
- **La pandilla asomada** detrás de una esquina, **las cabezas en fila**
  (el «tótem»).
- **La furgoneta** con todos saludando por las ventanas.
- **Scooby atrapando una galleta Scooby** en el aire, con la lengua fuera.
- **El sándwich gigante** de Shaggy y Scooby (torre de pan).

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D (Sketchfab)

Licencia **comprobada con la API de Sketchfab** (24-9-2026) ✅. Todos
son **descargables** y **CC Attribution** salvo donde se dice. Crédito
exacto: «"Título" by Autor (Sketchfab), licensed under CC BY 4.0».

| Modelo | Autor | Polígonos | Enlace | Nota |
|---|---|---|---|---|
| Mystery Machine - Scooby-Doo Van 3D Model | **Evans.Abarca** (26-7-2024) | 172 668 | [Sketchfab](https://sketchfab.com/3d-models/mystery-machine-scooby-doo-van-3d-model-ced86f6c51734cdd829d4af07a59be7d) | Detallada: **pesada** para la PC del dueño |
| MYSTERY MACHINE SCOOBY-DOO | **smoler_man** (16-1-2025) | 6254 | [Sketchfab](https://sketchfab.com/3d-models/mystery-machine-scooby-doo-923ee01828534275ba3da7749e45ccec) | **Ligera**: la mejor para el dueño (regla 9) |
| The Mystery Machine | **vegzavr** (15-7-2022) | 15 022 | [Sketchfab](https://sketchfab.com/3d-models/the-mystery-machine-9f6fd2e34eb1461a9f4e8925182ffc0e) | **Estilo dibujo animado** |
| Mystery Machine | Odami_3D | 1343 | [Sketchfab](https://sketchfab.com/3d-models/mystery-machine-d0e756d8eeaf47c19352b206209fb917) | Muy simple |
| Scooby do "The mystery machine" | MoonStore | 2712 | [Sketchfab](https://sketchfab.com/3d-models/scooby-do-the-mystery-machine-256aaa1b6e44484c85894a0bcd654333) | Simple |
| The Mystery Machine | perceval-66 | 22 776 | [Sketchfab](https://sketchfab.com/3d-models/the-mystery-machine-56e8c4502c4d443694c931d9f6f7b7fe) | |
| Scooby Doo Spooky House (with sound) | danatomashevych (2019) | 35 285 | [Sketchfab](https://sketchfab.com/3d-models/scooby-doo-spooky-house-with-sound-0c5d85f5196e43d0b178f95aa27ece6f) | **Casa encantada** de fondo |
| Scooby (Scooby-Doo) | guinavarro.al (13-5-2026) | 2733 | [Sketchfab](https://sketchfab.com/3d-models/scooby-scooby-doo-2a58d1dad71242698522094f0017029b) | Sólo como maniquí de pose, **nunca** en la lámina (el personaje va en 2D) |
| **Corkboard** | **sousinho** (2023) | 5524 | [Sketchfab](https://sketchfab.com/3d-models/corkboard-1e5469eaf8b54337aacfc42a713b3a98) | **Tablero de corcho**: base del concepto A |
| Cork Board (con papeles) | rickmaolly | 41 684 | [Sketchfab](https://sketchfab.com/3d-models/cork-board-9534ee2ad4344ea6b02b95b61bd4a913) | |
| Model of Cork Pin Board | windymore | 82 | [Sketchfab](https://sketchfab.com/3d-models/model-of-cork-pin-board-f07b7c65dbc44fd489e66e959b0c90ca) | Muy simple |
| «CC0 - Pin 2» (chincheta) | **plaggy** | 830 | [Sketchfab](https://sketchfab.com/3d-models/cc0-pin-2-4e7f37bee0674d569f558b0f08b7fdb7) | **Ojo**: se llama «CC0» pero en Sketchfab figura **CC Attribution** ✅: dar crédito |
| Magnifying glass, Victorian, wooden handle | risteralline | 1834 | [Sketchfab](https://sketchfab.com/3d-models/magnifying-glass-victorian-wooden-handle-aa27d07ebf114ecbaebff69e3ba888ad) | **La lupa** de Vilma |
| Square Net | HenryMead | 16 384 | [Sketchfab](https://sketchfab.com/3d-models/square-net-b5579a86b60146ad859cd8f8a60aaedd) | **La red de la trampa** de Fred |
| PSX Cork/Evidence Board | Kasujin | 28 | [Sketchfab](https://sketchfab.com/3d-models/psx-corkevidence-board-1aa12ebf9ed94305a79f344b4d08d0f4) | Estilo PS1: **no pega** con Hanna-Barbera |

> [!tip] El tablero se hace mejor a mano en Blender
> Un corcho es un plano con textura, un marco de madera y chinchetas (la
> de plaggy, con crédito). Las fichas son planos con un poco de curva: así **la
> tinta sigue la arruga** y la luz es real (regla 1 del dueño). El hilo
> rojo, una curva con grosor.

### 4.2 Fan art 2D (mirar, nunca pegar)

| Obra | Autor | Enlace | Para qué |
|---|---|---|---|
| «A Scooby-Doo Unmasking Meme» | WileE2005 | [DeviantArt](https://www.deviantart.com/wilee2005/art/A-Scooby-Doo-Unmasking-Meme-864569066) | Plantilla del desenmascarado |
| «50th anniversary of Scooby Doo» | brazilianferalcat | [DeviantArt](https://www.deviantart.com/brazilianferalcat/art/50th-anniversary-of-Scooby-Doo-784501647) | Grupo de celebración |
| «Scooby-Doo (1969-2014) Font Pack» | Charlieaat | [DeviantArt](https://www.deviantart.com/charlieaat/art/Scooby-Doo-1969-2014-Font-Pack-921135257) | Las letras de cada logo (sólo mirar, licencia dudosa) |

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Qué es | Luz típica | Sirve para |
|---|---|---|---|
| **La Máquina del Misterio** | Furgoneta **azul medio** con **franja verde**, **flores naranjas** y el panel verde con «THE MYSTERY MACHINE» en **naranja**; rueda de repuesto delante, verde con flor naranja ✅ ([Hanna-Barbera Wiki](https://hanna-barbera.fandom.com/wiki/Mystery_Machine), [Hagerty](https://www.hagerty.com/media/entertainment/mysteries-of-the-scooby-doo-mystery-machine/)). La inspiró la **cultura de las furgonetas** del sur de California; se cita a **Bob Singer** ✅ | Faros en la noche, interior en penumbra | **El tablero dentro**, con las puertas traseras abiertas |
| **Coolsville** | El pueblo de la pandilla, en **California** ✅ (Scoobypedia en la búsqueda). Tiene **instituto** (Coolsville High) y **heladería** (*malt shop*) | Día soleado | El sitio «de casa» |
| **El club de Misterio a la Orden** | En la película 2004 es «**el viejo club del instituto**» (00:58:30 ✅). En los cómics de DC el club está **en el pantano de Coolsville** ✅ (Scoobypedia) | Interior de madera, luz de tarde | **El tablero de pistas** (concepto B) |
| **Museo de Criminología de Coolsville** | Película 2004: allí se exponen **los disfraces de los villanos** desenmascarados (00:02:08 a 00:04:37 ✅) | Luz de museo, vitrinas | **Las máscaras colgadas** |
| **La casa encantada** | El sitio más repetido: mansión, castillo, faro. En la base de datos, **urbano** 267 veces, **rural** 109, **bosque** 48 ✅ | **Luna llena**, azul y morado | Fondo de cualquier concepto |
| **Crystal Cove** | El pueblo de *Misterios S.A.*, «**el lugar más embrujado de la Tierra**» (lema del pueblo, ⚠️ de memoria). La sede de la pandilla está en el **ayuntamiento** según un resumen de búsqueda ⚠️ (dudoso) | Costa, cuevas | Si se usa la serie de 2010 |

### 5.2 Luz (vista en las hojas C y F)

- **La noche de Hanna-Barbera** (F-6, F-10, F-15, F-16 ✅): cielo **azul
  marino casi negro** arriba y **azul cobalto** abajo, luna **celeste
  pálida** (no amarilla: medí `#86CDE3` en F-10), árboles y casas en
  **siluetas azul oscuro**, ventanas encendidas **amarillas** (F-15).
- **Interiores**: tres ambientes. **Rojo y morado** con fuego (F-18,
  salón con chimenea), **ocre y verde oliva** con una **vela verde**
  (F-24), y **azul gris** con telarañas (C-35).
- **Los personajes son planos** (color liso, contorno negro fino, casi
  sin sombra), y **el fondo está pintado a pincel**, con textura y
  degradados. Esa diferencia es el estilo (C-10, C-15, C-19 ✅): **no hay
  que sombrear a los personajes como en 3D**.
- **De noche, los personajes se tiñen de azul**: la camiseta de Shaggy
  pasa de verde `#689860` a **verde azulado** `#489080` en la escena de
  la playa (C-15, medido ✅).
- **El monstruo o la pista brillan**: el fantasma del capitán Cutler y
  las algas son **verde fosforito con halo** (C-15, C-47 ✅).

### 5.3 Paleta (medida en fotogramas y fondos ✅)

Medí con Pillow el color más frecuente de cada zona (margen ±8 por
canal). «C-10» es un fotograma de luz neutra; «C-15» es de noche.

| Qué | Hex medido | Dónde |
|---|---|---|
| Fred, jersey blanco | `#E0E0E8` | C-10 |
| Fred, cuello de la camisa (azul) | `#1858C0` | C-10 |
| Fred, pantalón azul | `#1048B8` | C-10 |
| Fred, pelo rubio | `#F8E090` | C-10 |
| Fred, pañuelo naranja | `#F2872B` ⚠️ (aprox.) | C-19 (no medido) |
| Daphne, vestido morado | `#282070` | C-10 (sombra de noche; en luz de día es más claro, `#7E4BA6` aprox. ⚠️) |
| Daphne, franja del vestido | `#9880D0` | C-10 |
| Daphne, pañuelo verde | `#98A840` | C-10 |
| Daphne, medias rosas | `#F088B8` | C-10 |
| Daphne, pelo | `#F04818` | C-10 |
| Vilma, jersey naranja | `#F87820` (noche `#E87828`) | C-10, C-15 |
| Vilma, falda roja | `#A01010` (noche `#800808`) | C-10, C-15 |
| Vilma, calcetines naranjas | `#F87020` | C-10 |
| Shaggy, camiseta verde | `#689860` (noche `#489080`) | C-10, C-15 |
| Shaggy, pantalón **granate** (no marrón) | `#601000` (noche `#400808`) | C-10, C-15 |
| Shaggy, pelo | `#A05818` | C-10 |
| Scooby, pelaje (de noche) | `#704838` | C-15 |
| Scooby, collar azul | `#1868B0` | C-15 |
| Scooby, placa del collar (rombo con «SD») | `#E0E0C0` | C-15 |
| Noche, cielo alto | `#020A17` | F-10 |
| Noche, azul medio | `#042B5F` / `#024993` | F-10 |
| Noche, azul claro | `#2E91B4` / `#349AB6` | F-10, F-15 |
| Luna | `#86CDE3` | F-10 |
| Salón rojo (F-18) | `#62164D`, `#A13448`, `#C55453`, `#DF7F66` | F-18 |
| Cuarto de la vela (F-24) | `#695B26`, `#79753A`, `#43141B` | F-24 |
| Malt Shop (F-8) | `#526E63`, `#779072`, `#7DD0D3` | F-8 |
| Furgoneta azul / verde / flores | `#59A7C9` / `#6DBE45` / `#F28C28` | ⚠️ aprox. (no medí: las imágenes de la furgoneta eran de noche) |
| Corcho del tablero | `#C79A5E` | ⚠️ referencia real, no de la serie |

> [!note] Shaggy lleva pantalón granate
> Las tiendas de disfraces dicen «pantalón marrón». En los fotogramas de
> 1969 es **granate oscuro** (`#601000`). Usar el medido.

### 5.4 Texturas reales equivalentes

- **Corcho** para el tablero: foto real de corcho, o el material del
  modelo de corcho de sousinho (CC BY). En Blender, *noise* marrón sobre base
  `#C79A5E`.
- **Papel de ficha** (tarjeta de 7 × 12 cm, rayada azul con margen rojo):
  las fichas de biblioteca de los 60.
- **Madera** del marco y del club: pino barnizado, oscuro.
- **Cuerda y red** (la trampa de Fred).
- **Chapa pintada** de furgoneta de los 60, con algo de brillo.
- **Goma** de la máscara del monstruo: látex verde o gris, con arrugas.
- Poly Haven y ambientCG estaban **bloqueados** desde aquí: buscar allí
  «cork», «plywood», «rope» desde la PC.

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **El logo de 1969**: letras **blancas, extra gruesas**, con los bordes
  **un poco ondulados**; cada letra **salta** por encima de la línea, y el
  conjunto recuerda a **siluetas de fantasma** ✅ (análisis de
  [1000logos](https://1000logos.net/scooby-doo-logo/)). Es **letra
  dibujada a mano**: no hay tipografía comercial igual; se compara con
  *Splashdown* o *Surfer Shop* ✅.
- **Fuente de fans «Scooby Doo»** de **Lauren Ashpole** (2009), gratis
  **sólo para uso personal** («Free for personal use», dice su
  `readme.txt`; licencia comercial en laurenashpole.com)
  ([dafont](https://www.dafont.com/scoobydoo.font)). **La bajé y la
  comprobé** con fontTools: tiene 99 caracteres, **trae ¿ y ¡** pero
  **NO trae á é í ó ú ñ** ❌. Sirve **sólo para palabras sin tilde**:
  «**DUDAS**», «**RESUELTA**», «**SIGUE ABIERTA**» funcionan tal cual.
  Para frases con tilde, usar Luckiest Guy (§6.2).
- **La furgoneta**: «THE MYSTERY MACHINE» en letras **naranjas, gruesas,
  redondeadas y retro** sobre el panel verde ✅ (Scoobypedia y Hagerty;
  el tipo exacto es a mano).
- **Los cartones de título de 1969** (C-47 a C-70, vistos ✅): arriba,
  «**SCOOBY DOO, WHERE ARE YOU!**» en letras **blanco hueso**, gordas y
  saltarinas (el logo), seguido de «**IN:**» pequeño; debajo, **el título
  del episodio** en **letras amarillas estrechas y altas** (tipo cartel,
  condensadas), con **contorno oscuro**, a veces en dos líneas; al fondo,
  un bosque azul oscuro con **caras fantasmales** y la pandilla **corriendo
  en fila** abajo. Algunos cambian el fondo (el Caballero Negro en rojo,
  C-67; el buzo fantasma verde, C-47).
- **Los cómics de DC** (G-4, G-79 ✅): globos **blancos ovalados con
  contorno negro fino** y cola curva; letra de cómic **en mayúsculas**,
  con **negrita cursiva** para la palabra que se enfatiza. Títulos de
  historia en **letras rojas con contorno**. Rotulista de G-79: **Nick J.
  Napolitano**.
- **La ficha «Who's Who»** de los cómics (C-44 ✅): recuadro **amarillo
  pálido** con el nombre del monstruo en **negritas grandes** y los datos
  en **mayúsculas pequeñas tipo máquina**: «REAL NAME», «OCCUPATION»,
  «LURKING LOCATION», «FIRST APPEARANCE».

### 6.2 Letras libres comprobadas por mí

Bajadas de [google/fonts](https://github.com/google/fonts) y comprobadas
con fontTools (á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü):

| Letra | Licencia | Para qué | Tildes, ñ, ¿, ¡ |
|---|---|---|---|
| **Scooby Doo** (Lauren Ashpole, dafont) | Sólo uso personal | **El logo tal cual**: sólo palabras sin tilde («DUDAS», «RESUELTA») | ❌ **sin tildes ni ñ**; sí ¿ ¡ |
| **Luckiest Guy** | Apache 2.0 | **Título «Dudas»**: gorda y saltarina, lo más cerca del logo con tildes | ✅ todas |
| **Titan One** | OFL | Título alternativo, más redonda | ✅ todas |
| **Lilita One** | OFL | Rótulos de la furgoneta | ✅ todas |
| **Bowlby One** | OFL | Rótulo retro de los 60 | ✅ todas |
| **League Gothic** | OFL | Las **letras amarillas estrechas** de los cartones de título (la más parecida: alta y condensada) | ✅ todas |
| **Oswald**, **Anton**, **Bebas Neue**, **Fjalla One** | OFL | Alternativas condensadas para el título del caso | ✅ todas |
| **Chango** | OFL | Rótulo retro ancho | ✅ todas |
| **Mystery Quest** | OFL | **Título de miedo divertido** (el nombre ya lo dice) | ✅ todas |
| **Creepster** | OFL | Letras que gotean: **«Sigue abierta»** con susto | ✅ todas |
| **Griffy** | OFL | Letras de cuento de brujas | ✅ todas |
| **Nosifer** | OFL | Sangre: **demasiado fuerte** para Scooby, no usar | ✅ todas |
| **Eater** | OFL | Miedo exagerado | ✅ todas |
| **Butcherman** | OFL | Miedo | ❌ **no trae ¿** |
| **Permanent Marker** | Apache 2.0 | **Rotulador** en las fichas del tablero | ✅ todas |
| **Caveat** | OFL | **Letra a mano de Vilma** en las fichas | ✅ todas |
| **Kalam** | OFL | Letra a mano, más clara en móvil | ✅ todas |
| **Patrick Hand** | OFL | Letra a mano tipo cómic | ✅ todas |
| **Gochi Hand** | OFL | Letra a mano infantil | ✅ todas |
| **Rock Salt** | Apache 2.0 | A mano, rasposa: poco legible pequeña | ✅ todas |
| **Special Elite** | Apache 2.0 | **Máquina de escribir**: expediente del caso | ✅ todas |
| **Courier Prime** | OFL | Máquina de escribir limpia | ✅ todas |
| **Fredoka** | OFL | Texto de apoyo redondo y amable | ✅ todas |
| **Sniglet** | OFL | Texto de apoyo, dibujo animado | ✅ todas |
| **Freckle Face** | OFL | Letra de los 60 juguetona | ✅ todas |
| **Londrina Solid** | OFL | Rótulo a mano gordo | ✅ todas |
| **Shrikhand** | OFL | Rótulo retro con cola | ✅ todas |

**Combinación que propongo**: **Luckiest Guy** (título, en blanco con
borde negro y sombra, como el logo) + **Caveat** o **Permanent Marker**
(fichas del tablero) + **Special Elite** (el sello «RESUELTA» y el
expediente). Para el susto de «Sigue abierta», **Creepster** en verde
fantasma.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

La guía de cuadros de este repo (`_Cuadros de dialogo por franquicia`, §32)
dejó Scooby-Doo **sin cuadro propio verificado** ⚠️: sólo «el
desenmascarado + chicos entrometidos». Aquí lo completo.

### 7.1 Lo que la serie pone en pantalla

La serie de televisión **no usa globos**: todo se habla. El texto escrito
aparece en objetos. Esto es lo que hay:

| Dónde aparece el texto | Cómo es | Fuente |
|---|---|---|
| **La furgoneta** | Panel verde con «THE MYSTERY MACHINE» en naranja, letras gordas retro ✅ | Hanna-Barbera Wiki, Hagerty |
| **La explicación final** | No es texto: **cada uno explica una parte por turnos** (Fred, Vilma, Daphne) mientras el villano está atado ✅ | Subtítulo 1978, 00:19:49 a 00:20:12 |
| **El desenmascarado** | La máscara fuera, una cara de señor normal, la frase del villano ✅ | Base de datos (189 veces) |
| **La advertencia del fantasma** | «**¡Váyanse de esta isla!**»: el aviso que abre el caso ✅ | Subtítulo 1978, 00:07:39 y 00:08:09 |
| **Los carteles del sitio** | Letreros pintados en el fondo: «**MALT SHOP**» (F-8), «**GOLD CITY** GUEST RANCH / VACANCY» (F-20), «**FUN FUN**» con luces de feria (F-4), «**FUNHOUSE**» y «TICKETS» (F-9) ✅ | Hoja F |
| **La pared de máscaras** | Máscaras de monstruo **colgadas de clavos** en una pared (F-22) ✅ | Hoja F |
| **Las etiquetas del museo** | Cada disfraz de villano desenmascarado, expuesto con su cartela ✅ (película 2004, 00:02:08 a 00:04:37) | Subtítulo 2004 |
| **La tele y los periódicos** | En la película 2004, el noticiero «**Investigative Probe**» y la gente gritando «**Mystery Stink!**» ✅ (00:57:03 a 00:57:18) | Subtítulo 2004 |
| **El cartón de título** | Logo en blanco hueso + «IN:» + **título en letras amarillas estrechas** con contorno oscuro sobre bosque azul (§6.1) ✅ | C-47 a C-70 |
| **El periódico** | «**The Daily Babbler**», titular «**GHOST BUSTED!**» con la foto de la pandilla y el villano atado (cómic) ✅. En la serie, **el periódico de la Malt Shop** les da el caso y, al resolverlo, **salen en las noticias** ✅ (Scoobypedia, «A Clue for Scooby Doo») | C-45, Scoobypedia |
| **La ficha «Who's Who»** | Recuadro amarillo con nombre del monstruo, **REAL NAME** (el culpable), ocupación, dónde acecha y primera aparición, más el resumen del caso ✅ | C-44 (cómics) |

Los **tebeos** sí usan globos. La serie de DC **«Scooby-Doo, Where Are
You!»** (desde 2010) la escribe **Sholly Fisch** con dibujo de **Dario
Brizuela** ✅ ([DC](https://www.dc.com/comics/scooby-doo-where-are-you-2010/scooby-doo-where-are-you-67),
[Amazon](https://www.amazon.com/Scooby-Doo-Where-Are-You-2010-ebook/dp/B01BPY16SE)).
También **«Scooby-Doo Team-Up»**, con los superhéroes de DC ✅. El globo es
el de cómic americano: **blanco, ovalado, contorno negro fino, cola
curva**, letra de cómic **en mayúsculas** con **negrita cursiva** en la
palabra clave (G-4: «HMM, THAT'S STRANGE…» / «WHAT'S STRANGE?»; G-79 ✅
vistos). Por eso **el globo NO es lo propio** de Scooby-Doo: lo propio
son **las pistas, las fichas y el desenmascarado**.

### 7.2 Lo que ponen los videojuegos

| Juego | El «cuadro» | Fuente |
|---|---|---|
| **MultiVersus** (2022 y 2024) | **Vilma junta pruebas** con sus ataques. Con el medidor lleno **resuelve el misterio**: primero llamaba a **la policía** (que revelaba que el rival era «**el viejo Jenkins**»); tras el parche 1.02 llega **la Máquina del Misterio** y se lleva al villano ✅ | [PC Gamer](https://www.pcgamer.com/multiversus-removes-the-police-from-velmas-special-move/), [GameRevolution](https://www.gamerevolution.com/news/714472-multiversus-velma-police-car-lebron-arrest-update-patch-1-02), [TheGamer](https://www.thegamer.com/multiversus-velma-tips-tricks-tutorial-guide/) |
| **Mystery Mayhem** (2004) | Cada nivel: **atrapar a los monstruos, encontrar 5 pistas** y terminar la misión. Las pistas **abren la galería de arte** ✅ | [GameFAQs](https://gamefaqs.gamespot.com/gamecube/919748-scooby-doo-mystery-mayhem/faqs/31416), [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/ScoobyDooMysteryMayhem) |
| **Unmasked** (2005) | Se juntan **pistas para Vilma** (abren niveles), ingredientes para Shaggy y **piezas de trampa**; en DS se **investigan las pistas** arrastrando herramientas con el lápiz ✅ | [Wikipedia](https://en.wikipedia.org/wiki/Scooby-Doo!_Unmasked), Nintendo Wiki |
| **Night of 100 Frights** (2002) | Se juntan **fichas de monstruo** para la **Galería de Monstruos**; galletas Scooby y **cajas de galletas** ✅ (nombres del código del randomizador [vgm5/Night_Of_100_Frights_ap_world](https://github.com/vgm5/Night_Of_100_Frights_ap_world)) | GitHub, [TCRF](https://tcrf.net/Scooby-Doo!_Night_of_100_Frights_(GameCube,_PlayStation_2,_Xbox)) |
| **Scooby-Doo Mystery** (1995, SNES y Genesis) | SNES: plataformas con **pistas** en 4 misterios. Genesis: **aventura de apuntar y hacer clic** en 2 misterios ✅ | [Wikipedia](https://en.wikipedia.org/wiki/Scooby-Doo_Mystery), [MobyGames](https://www.mobygames.com/game/39832/scooby-doo-mystery/) |

**La idea que sirve**: en los juegos, **una pista es un objeto que se
colecciona** y, con todas, **el misterio se resuelve**. Eso es un hilo de
#dudas: se juntan respuestas hasta que queda **Resuelta**.

### 7.3 Cómo hablan (por los subtítulos)

- **Vilma explica y frena**: «**Alto ahí**. No nos vamos» (1978,
  00:08:38 ✅). «**Yo puedo responder a eso. Miren**» (2002, 00:05:11 ✅).
  «Este misterio **empieza a tener sentido**» (1978, 00:15:00 ✅).
- **Fred dirige**: «**Vilma tiene razón**. Podemos estar a punto de
  resolver un gran misterio» (1978, 00:08:42 ✅). «**Separémonos** y
  busquemos más pistas» (2002, 00:26:57 ✅). «**Veamos quiénes son en
  realidad**» (1978, 00:20:15 ✅).
- **Shaggy negocia y pregunta**: empieza con «*Like*» (en latino, un
  «**oye**» o «**viejo**» ⚠️ de memoria). Negocia por galletas: «¿Y
  **tres**?» (1978, 00:07:14 ✅). Pregunta sin vergüenza: «¿**Nos lo
  explican otra vez**?» (1978, 00:19:44 ✅).
- **Scooby** dice pocas palabras y **cambia la primera letra por R**:
  «*Ruh-roh*», «*Rokay*», «*Rooby-Rooby-Roo*» (413 veces ✅ en la base de
  datos). Se ríe con **risita entre dientes** y **se come las pistas** ⚠️.
- **Daphne** comenta lo que ve: «**Jeepers**, ¿vieron eso?» (1978,
  00:05:18 ✅). Explica su parte: «Luego los aviones volaban a control
  remoto hasta la pista de la isla» (1978, 00:20:08 ✅).
- **El villano** siempre dice lo mismo: «¡Y me hubiera salido con la mía si
  no fuera por **ustedes, chicos entrometidos**… **y su perro tonto**!»
  (2002, 00:05:30 ✅).

### 7.4 Cómo se traduce a una lámina fija

1. **La ficha de pista** clavada en el corcho: tarjeta rayada, **letra a
   mano de Vilma** (Caveat o Permanent Marker), una chincheta de color por
   etiqueta. Es el cuadro principal.
2. **La cartela del museo**: placa de latón o cartulina con el nombre del
   villano y «**Resuelta**». Para el estado cerrado.
3. **El sello «RESUELTA»** sobre la ficha, en rojo, letra de máquina de
   escribir (Special Elite), torcido.
4. **La máscara quitada**, colgada de un clavo con una **etiqueta de
   equipaje** atada con cordel: ahí va el texto corto.
5. **El «?» de Shaggy y Scooby**: un **signo de interrogación dibujado en
   la ficha** (no un globo de pensamiento).
6. **El panel verde de la furgoneta**: título del canal en las letras
   naranjas de «THE MYSTERY MACHINE».
7. **La ficha «Who's Who»** (C-44): recuadro amarillo pálido con
   «**DUDA:** …», «**DISCIPLINA:** …», «**ESTADO:** Resuelta». Es el
   formato de ficha que ya usa la franquicia: perfecto para explicar el
   hilo de un foro.
8. **El titular del periódico** (C-45): «**¡CASO RESUELTO!**» en letras
   de periódico, con la foto de la pandilla. Para el estado Resuelta.
9. **El cartón de título** (C-47): «**DUDAS**» en letras amarillas
   estrechas sobre bosque azul, con la pandilla corriendo debajo. Para el
   encabezado de la lámina.
10. **Si hace falta globo** (una frase del personaje): globo de **tebeo
   de DC** (G-4), blanco con **contorno negro fino y cola curva**, letra
   de cómic en mayúsculas y la palabra clave en negrita cursiva. Nunca un
   óvalo blanco sin borde.

### 7.5 Qué NO hacer con el texto

- Una **burbuja blanca genérica** flotando: el dueño la rechazó.
- **Letras con sangre** (Nosifer, Butcherman): Scooby da miedo **de risa**.
- **Pantallas de ordenador** o paneles de interfaz sueltos: al dueño no le
  convencen. El medidor de *MultiVersus* sirve de idea, **no** de marco.
- **Un tablero con hilo rojo por todas partes** estilo serie policíaca
  oscura: recuerda a *Velma* (2023), la serie que los fans odian (§14).
  Poco hilo, fichas limpias, colores de los 60.

---

## 8 · Los personajes

Descripción de carácter: lo marcado ✅ sale de los subtítulos o de dos
fuentes. Lo demás es de memoria ⚠️ (la serie tiene 57 años: lo esencial
es muy conocido, pero conviene mirar el fotograma).

### Scooby-Doo — el perro, el que da nombre

- **Qué es**: un **gran danés** marrón con manchas negras, **cobarde y
  glotón**. Diseñado por Iwao Takamoto al revés de lo que sería un gran
  danés de concurso ⚠️ (§3.1). Primera aparición: 13-9-1969 ✅.
- **Carácter**: miedoso, cariñoso, **se deja comprar con galletas
  Scooby**. Es el **mejor amigo de Shaggy**: van juntos a todo. Tiene
  **suerte tonta**: tropieza con las pistas y atrapa al villano sin querer
  (**160 veces**, el que más ✅).
- **Miedos**: todos los monstruos, la oscuridad, quedarse solo.
- **Qué le importa**: comer, Shaggy, la pandilla.
- **Cómo se expresa**: frases de una o dos palabras con **R delante**
  («Ruh-roh», «Rokay»). Su grito de victoria: «**¡Scooby-Dooby-Doo!**»
  (cierre de episodio, 1978, 00:21:02 ✅; película 2002, 00:05:38 ✅).
  Ríe **entre dientes, con los hombros** ⚠️. Olfatea el suelo buscando el
  rastro (1978, 00:07:27, «[olfateando]» ✅).
- **Cuerpo**: postura de **perro sentado muy recto** o **de pie a dos
  patas** como una persona; **se esconde detrás de sus orejas** o
  **salta a los brazos** de Shaggy ⚠️.
- **Voz original**: **Don Messick** (1969-1994), **Frank Welker** (desde
  2002) ✅ (base de datos).

### Shaggy Rogers — el que pregunta

- **Qué es**: el amigo flaco, alto, de pelo castaño revuelto y **perilla**.
  **Camiseta verde de cuello en V** y **pantalón acampanado granate**
  (`#601000`, medido en C-10 ✅; las tiendas de disfraces dicen
  «marrón»).
- **Carácter**: miedoso como Scooby, **hambriento sin fondo**, bueno,
  **sincero**: dice lo que todos piensan. En los finales **pide que se lo
  expliquen** (1978, 00:19:44 ✅). En la película 2002 es **el que une al
  grupo** («Somos como un banana split», 00:06:21 ✅).
- **Miedos**: todo. **Qué le importa**: Scooby, comer, que nadie se pelee.
- **Cómo se expresa**: «**Zoinks**» (**1229 veces**, la frase más dicha de
  la franquicia ✅; en latino «**¡Caracoles!**» ✅, Doblaje Wiki y vídeo oficial 00:08:39). Empieza las frases
  con «*Like*…». Negocia («¿Y **tres** galletas?», 1978, 00:07:14 ✅).
  Corre con **las piernas en rueda**, se abraza a Scooby, **se pone
  pálido** ⚠️.
- **En internet**: el meme «**Ultra Instinct Shaggy**» (Shaggy con poder
  infinito; nació el 12-10-2017 con una pelea de *Legend of the
  Phantosaur*, 2011) ✅; en enero de 2019, una petición para meterlo en
  *Mortal Kombat 11* juntó **más de 83 000 firmas en 24 horas** ✅
  ([Know Your Meme](https://knowyourmeme.com/memes/ultra-instinct-shaggy),
  [CBR](https://www.cbr.com/ultra-instinct-shaggy-history-explained/)).
  En *MultiVersus* es **luchador con esos poderes** ✅.
- **Voz original**: **Casey Kasem** (1969-2009), **Matthew Lillard**
  (desde 2002 en cine y 2010 en series) ✅ (base de datos).

### Vilma Dinkley — la que resuelve

- **Qué es**: la lista del grupo. **Jersey naranja de cuello alto**,
  **falda roja**, calcetines hasta la rodilla, **gafas gruesas** y
  melena corta castaña ✅ (búsqueda de vestuario).
- **Carácter**: inteligente, lectora, práctica, algo seca. **Es la que
  entiende el truco** («Supe desde el principio que no había ningún
  fantasma», 2002, 00:04:51 ✅) y **la que frena la huida** (1978,
  00:08:38 ✅). En la película 2002 se queja de que **Fred se lleva el
  mérito de sus planes** (00:05:47 ✅).
- **Miedos**: **perder las gafas** (sin ellas no ve nada: 45 veces ✅).
- **Qué le importa**: la verdad, la lógica, que el misterio cuadre.
- **Cómo se expresa**: «**¡Cielos!**» (*Jinkies*, 503 veces ✅). Señala
  con el dedo y **se sube las gafas** ⚠️. Explica con **frases cortas y
  exactas**. Desenmascara **94 veces** (casi tanto como Fred ✅); en
  *¿Qué hay de nuevo?* desenmascara **más que nadie** (12 ✅).
- **En latino**: se llama **Vilma**, no Velma ✅ (Doblaje Wiki).
- **Voz original**: Nicole Jaffe (1969), Pat Stevens (1976-1979), **Mindy
  Cohn** (2002-2015), **Kate Micucci** (desde 2015) ✅ (base de datos).

### Fred Jones — el que dirige y quita la máscara

- **Qué es**: el líder, rubio, **jersey blanco con el cuello azul de la
  camisa**, **pañuelo naranja al cuello** (*ascot*) y **pantalón azul**
  (C-19 ✅) ✅ (búsqueda de vestuario; el
  *ascot* lo nombra hasta la película 2002: «¡Cuidado con el pañuelo!»,
  00:06:11 ✅).
- **Carácter**: seguro, animoso, algo vanidoso (en la película 2002
  escribe un libro, «*Fred on Fred*», 00:10:04 ✅). **Obsesionado con
  las trampas** (47 trampas ✅; **fallan la mitad**, 124 de 249 casos
  anotados ✅).
- **Qué le importa**: que el plan salga, el grupo, la furgoneta.
- **Cómo se expresa**: «**Muy bien, pandilla**», «**¡Separémonos!**» (le
  roban la frase en la película 2004, 00:19:07 ✅). Desenmascara **más
  que nadie**: **102 veces** ✅. Es **el del meme** «Veamos quién es en
  realidad» (§14).
- **Voz original**: **Frank Welker** desde 1969 hasta hoy ✅ (base de
  datos: 351 episodios).

### Daphne Blake — la que se mete en líos (y sale)

- **Qué es**: pelirroja, **vestido morado**, **pañuelo verde** al cuello,
  **cinta morada** en el pelo, **medias rosas** ✅ (búsqueda de vestuario
  y [Scoobypedia: la ropa de Daphne](https://scoobydoo.fandom.com/wiki/Daphne's_outfits_and_disguises)).
  Viene de **familia rica** (mansión en Coolsville ✅ Scoobypedia).
- **Carácter**: valiente, curiosa, con estilo. La que **más veces cae
  prisionera** (91 ✅), de ahí el apodo «**Danger-prone Daphne**», que en el doblaje de 1969 fue «**La peligrosa Daphne**» (lo pusieron los propios Ruby y Spears por lo torpe que era; Doblaje Wiki)
  ⚠️. La película 2002 se ríe de eso y la hace **karateka** ⚠️ («No
  siempre me secuestran», 00:05:56 ✅; «Vienes con tu propia nota de
  rescate», 00:06:00 ✅).
- **Qué le importa**: sus amigos, no ser «la que rescatan».
- **Cómo se expresa**: «**Jeepers**» (247 veces ✅; en latino «¡Rayos!»,
  «¡Recórcholis!» ⚠️). Es la que **más galletas Scooby da** (49 ✅): la
  que convence a Scooby.
- **Voz original**: Stefanianna Christopherson (1969-1970), **Heather
  North** (1970-2003), **Grey DeLisle** (desde 2001) ✅ (base de datos).

### Los secundarios que conviene tener a mano

| Personaje | Qué es | Ojo |
|---|---|---|
| **Scrappy-Doo** | Sobrino de Scooby, cachorro valiente («¡Poder cachorro!»). Sale en **165** entradas de la base de datos ✅ | **El más odiado** por los fans: la película 2002 lo hizo **el villano** a propósito (§14). **No usar** |
| **El Caballero Negro** | Primer villano de la historia (1969) ✅ | Armadura que se mueve |
| **El fantasma del capitán Cutler** | Buzo fantasma que brilla en verde, ep. 2 «Una pista para Scooby-Doo» ✅ | Encaja con «pista» |
| **El Fantasma de Bluestone** | El del **meme del desenmascarado** («Hassle in the Castle», 27-9-1969) ✅ | §14 |
| **El Creeper** | «Jeepers, It's the Creeper» (1970), de los mejor valorados (8,5) ✅ | Muy reconocible |
| **El «viejo Jenkins»** | **Chiste de fans**: «seguro que es el viejo Jenkins». En la base de datos **no hay** ningún villano con ese nombre (sólo una Sarah Jenkins, 1969) ✅. *MultiVersus* lo usa como guiño ✅ | Se puede usar como broma |
| **Las Hex Girls** | Grupo de rock gótico de *La bruja fantasma* (1999); salen **6 veces** ✅ | Muy queridas ⚠️ |
| **Blue Falcon** | Superhéroe de Hanna-Barbera; 33 cruces ✅ | |
| **El profesor Pericles** | Loro villano de *Misterios S.A.*, el culpable más repetido (4) ✅ | Sólo si se usa la serie de 2010 |

---

## 9 · ¿Quién es el más querido?

- **No hay encuesta oficial** de Warner con votos por personaje ⚠️.
- **Scoobypedia** (la wiki de fans), encuesta de **febrero de 2010**
  (97 votos): **Scooby 39**, **Daphne 22**, **Shaggy 19**, **Vilma 12**,
  **Fred 5** ✅ (resumen de búsqueda y la página leída por API,
  «[Scoobypedia:Monthly Poll Results](https://scoobydoo.fandom.com/wiki/Scoobypedia:Monthly_Poll_Results)»).
  En marzo de 2010, la película de imagen real favorita fue **la de 2004**
  (23 votos) por delante de la de 2002 (18) ✅. Encuesta vieja y
  pequeña: orientativa. Hay otras en [IMDb](https://www.imdb.com/poll/78cg8QoQmkg/),
  [Fanpop](https://www.fanpop.com/clubs/scooby-doo/picks/results/2989/who-favorite-scooby-doo-character)
  y [Looper (ranking)](https://www.looper.com/750196/most-popular-scooby-doo-characters-ranked-worst-to-best/)
  que no leí.
- **Reddit (r/Scoobydoo, por el archivo Arctic Shift)**: conté quién
  nombra primero cada comentario principal en tres hilos ✅:
  - «[Who's your favourite member of the gang?](https://reddit.com/r/Scoobydoo/comments/pm44xz/whos_your_favourite_member_of_the_gang/)»
    (15 comentarios): Fred 5, **Shaggy 4**, Vilma 3, Scooby 2, Daphne 1.
  - «[Which Member of the Scooby Gang is your favourite?](https://reddit.com/r/Scoobydoo/comments/1476mam/which_member_of_the_scooby_gang_is_your_favourite/)»
    (22): **Shaggy 6**, Fred 4, Daphne 4, Scooby 3, Vilma 1.
  - «[Who's your LEAST favourite member?](https://reddit.com/r/Scoobydoo/comments/twsi1k/whos_your_least_favourite_member_of_the_original/)»
    (44): **Fred 15**, Vilma 5, Scooby 4, **Shaggy 3**, Daphne 2.
  - Muestra pequeña, pero clara en una cosa: **Fred divide** y **Shaggy
    casi nadie lo odia**.
- **Internet**: **Shaggy** es el más «meme» con diferencia (Ultra Instinct
  Shaggy, petición de 83 000 firmas en un día, luchador en *MultiVersus*
  ✅). **Vilma** es la **más citada como la lista**: el canal oficial latino
  tiene recopilaciones solo de ella («**Mejor de Velma**», «**¡Velma
  sabe!**») ✅ ([YouTube](https://www.youtube.com/watch?v=fdqVXWBkr9g),
  [YouTube](https://www.youtube.com/watch?v=zY8Vgn-bqhc)).
- **El más odiado**: **Scrappy-Doo**, sin duda ✅ (James Gunn, guionista
  de la película 2002: «Nuestro objetivo era **destruir a Scrappy para
  siempre**», [Far Out](https://faroutmagazine.co.uk/why-james-gunn-hates-scrappy-doo-and-cast-him-as-a-villain/),
  [Screen Rant](https://screenrant.com/scooby-doo-2002-scrappy-villain-twist-reason-perfect/)).

**Para #dudas**: la lámina funciona mejor con **dos papeles**:
- **Vilma** = la que **responde** (Resuelta). Es la lista, y es la que
  aparece como «la que sabe» en los vídeos oficiales.
- **Shaggy y Scooby** = los que **preguntan** («pregunta sin miedo»). Son
  los más queridos por el público y los más graciosos.
- **Fred** = el que **quita la máscara** (el momento «Resuelta»).

---

## 10 · Doblaje latino

> [!important] Fuentes
> **Doblaje Wiki** leída por su **API** (22 páginas: la serie de 1969,
> *El show*, *Las nuevas películas*, *¿Qué hay de nuevo?*, *Misterios
> S.A.*, *Ponte en onda*, las películas 2002 y 2004, *¡Scooby!*, los
> cinco personajes y seis actores). Cruzada con **ANMTV** (tres
> artículos), **SensaCine** y los **vídeos oficiales de WB Kids Latino**.
> ✅ = Doblaje Wiki **y** otra fuente. ⚠️ = sólo Doblaje Wiki.

### 10.1 La serie de 1969: «Misterio a la orden»

**Estudio SISSA (Oruga), México. Dirección: Francisco Colmenero** ✅
(Doblaje Wiki y [ANMTV](https://www.anmtvla.com/2021/10/the-scooby-doo-show-y-scooby-doo-donde.html)).

| Personaje | Voz latina | Episodios | Estado |
|---|---|---|---|
| Scooby-Doo | **Ismael Larumbe Sr.** | los 25, salvo el 4 (lo hizo **Francisco Colmenero**) | ✅ Doblaje Wiki (serie y personaje) y búsqueda |
| Shaggy | **Arturo Mercado** | los 25, salvo el 5 (**Salvador Nájar**) | ✅ Doblaje Wiki y guía de cuadros |
| Fred | **Luis de Alba** (ep. 1-3, 5-7, 9-17) y **Luis Bayardo** (ep. 4, 8 y 18-25) | | ⚠️ Doblaje Wiki (dos páginas) |
| Daphne | **María Santander** (todos salvo el 9, **Emilia Carranza**) | | ⚠️ Doblaje Wiki |
| Vilma | **Linda Smith**: **la única que dobló a su personaje en los 25 episodios** | | ⚠️ Doblaje Wiki |
| Narrador e insertos | **Francisco Colmenero** | | ⚠️ Doblaje Wiki |

Lo que inventó ese doblaje y **sigue vivo hoy** (Doblaje Wiki):
«**Scooby-galletas**», «**La Máquina del Misterio**», el nombre
«**Misterio a la orden**», y las exclamaciones «**¡Cielos!**» (Vilma),
«**¡Caracoles!**» (Shaggy) y «¡Rayos!» (Daphne). Arturo Mercado creó para
Shaggy **un tono, risas y frases propias**, distintas del inglés: por eso
en Latinoamérica Shaggy «suena» a Mercado. Y **improvisaban**: en el ep.
21 Scooby dice «**¡Ay, mamá pulpa!**» (guiño al Pulpo Manotas) y en el
23 Shaggy suelta «¡Hey, Daphne, te están gruñendo las tripas!» ⚠️
(Doblaje Wiki).

### 10.2 Las series de los 70 y 80

| Serie | Estudio y dirección | Voces | Estado |
|---|---|---|---|
| *Las nuevas películas de Scooby-Doo* (1972) | **CINSA**, dir. **Jorge Arvizu «El Tata»** | Scooby: **Jorge Arvizu**. Shaggy: **Santiago Gil**. Fred: **José Lavat** | ⚠️ Doblaje Wiki |
| *El show de Scooby-Doo* (1976-1978) | **CINSA** (T1-T2, dir. Arvizu); vuelve a **SISSA** en la T3 | T3: **Francisco Colmenero** (Scooby), **Arturo Mercado** (Shaggy), **María Santander** (Daphne), **Jesús Brock** (Fred) | ✅ ANMTV y Doblaje Wiki (estudios); ⚠️ voces |
| *Un cachorro llamado Scooby-Doo* (1988) | | Voces **infantiles** nuevas (Scooby: Gustavo Toquero, Benjamín Rivera, Jesús Barrero) | ⚠️ |

### 10.3 El reparto «de Warner» (1998 a 2015)

| Personaje | Voz | Estado |
|---|---|---|
| Scooby | **Antonio Gálvez** (desde *La persecución cibernética*, 2001; lo eligió **Warner por contrato**; la voz **más duradera**) | ✅ Doblaje Wiki y ANMTV |
| Shaggy | **Arturo Mercado**: vuelve en *La isla de los zombies* (1998) y sigue hasta 2015. **46 años** con el personaje | ✅ Doblaje Wiki y ANMTV |
| Fred | **Luis Alfonso Padilla** (2001 a 2012; murió el 12-5-2012) | ✅ Doblaje Wiki y TikTok «Joyas del Doblaje» |
| Fred (desde la T2 de *Misterios S.A.*) | **Ricardo Mendoza** | ✅ Doblaje Wiki y ANMTV |
| Daphne | **Yolanda Vidal** (29 producciones) | ✅ Doblaje Wiki y ANMTV |
| Vilma | **Irene Jiménez** (41 producciones: la voz de Vilma que más ha durado) | ✅ Doblaje Wiki y ANMTV |

| Producción | Estudio y dirección | Estado |
|---|---|---|
| *La isla de los zombies* (1998) | **Suite Sync**, dir. **Genaro Vásquez** | ⚠️ |
| *¿Qué hay de nuevo, Scooby-Doo?* (2002) | **Suite Sync / Sensaciones Sónicas**, dir. **Víctor Hugo Aguilar** (T1-T2) | ⚠️ |
| *Misterios S.A.* (estreno en Cartoon Network LA: **6-3-2011**) | **Sensaciones Sónicas**, dir. **Antonio Gálvez** (T1), que **pidió conservar a todo el reparto**; la T2 la empezó **Circe Luna** y la siguió **Carlos Hugo Hidalgo** | ✅ Doblaje Wiki y ANMTV |

**Las películas de imagen real (2002 y 2004)**: estudio **Audiopost**,
dir. **Roberto Molina** ⚠️. Scooby: **Rolando de Castro** (las **risas**
las hizo Roberto Molina). Shaggy: **Arturo Mercado Jr.** (el hijo, con
una voz parecida a la del padre). **Arturo Mercado padre hace de
Scrappy-Doo** en la de 2002. Fred: **Ricardo Mendoza**. Daphne: **Xóchitl
Ugarte**. Vilma: **Gaby Ugarte** ✅ (Doblaje Wiki, página de la película
y del personaje; Mercado Jr. también en ANMTV). En la de 2002, «*Jinkies*»
**se dejó sin traducir** ✅.

### 10.4 Desde 2015: el reparto nuevo

**¿Por qué cambió?** La serie *¡Ponte en onda, Scooby-Doo!* (2015) se
dobló en **SDI Media de México**, dir. **Carla Castañeda**. Según ella,
fue «**decisión del cliente**», que pidió casting porque los personajes
eran más jóvenes y la animación distinta. Luego las películas siguieron
con el reparto nuevo y **los fans protestaron**, sobre todo por la voz de
Shaggy ✅ (Doblaje Wiki y la
[petición de Change.org](https://www.change.org/p/warner-brothers-regresen-el-doblaje-original-de-scooby-doo)).

| Personaje | Voz | Estado |
|---|---|---|
| Scooby | **Óscar Flores** | ✅ Doblaje Wiki y SensaCine |
| Shaggy | **Miguel Ángel Ruiz** | ✅ Doblaje Wiki y SensaCine |
| Fred | **Irwin Daayán** | ✅ Doblaje Wiki y SensaCine |
| Daphne | **Carla Castañeda** (también directora) | ✅ Doblaje Wiki y SensaCine |
| Vilma | **Leyla Rangel** | ✅ Doblaje Wiki y SensaCine |

- ***¡Scooby!* (2020, cine)**: el mismo reparto; SDI Media de México,
  dir. **Karla Falcón**. Los niños: Sergio Barberi (Shaggy), Sebastián
  Albavera (Fred), Regina Carrillo (Daphne) ✅
  ([SensaCine](https://www.sensacine.com.mx/noticias/noticia-18567589/) y
  Doblaje Wiki).
- ***¡Feliz Halloween, Scooby-Doo!* (2020)**: se dobló en **Sysdub**,
  dir. **Guillermo Rojas**, y **volvieron Antonio Gálvez** (Scooby) y
  **Arturo Mercado Jr.** (Shaggy); Vilma **Cynthia Chong**, Fred
  **Christian Strempler**, Daphne **Sandra Olarra** ✅
  ([ANMTV](https://www.anmtvla.com/2020/08/se-revela-reparto-de-voces-de-happy.html)
  y Doblaje Wiki, página de Fred).

### 10.5 Qué voz «oye» el lector

> [!tip] Para el servidor
> Quien creció en los 90 y 2000 (la mayoría del servidor) oye a Scooby
> con la voz de **Antonio Gálvez** y a Shaggy con la de **Arturo
> Mercado**. Si la lámina «cita» una frase del doblaje, que sea de las que
> **no han cambiado nunca**: «**¡Cielos!**», «**¡Caracoles!**»,
> «**chicos entrometidos**», «**Scooby-galletas**», «**la Máquina del
> Misterio**», «**Misterio a la orden**».

- El canal oficial **WB Kids Latino** sube clips doblados cada semana
  (§12). En *Misterios S.A.*, Vilma abre sus vídeos con «**Oigan, amantes
  de los misterios, habla Vilma**» ✅ (dos vídeos, 00:01:21 y 00:00:00).
- Hay dos vídeos de análisis:
  «[El Doblaje Latino de Scooby-Doo: ¿Por qué es tan ICÓNICO?](https://www.youtube.com/watch?v=f3Bkkvr1s8s)»
  y «[El doblaje de Scooby Doo Misterios S.A. y la dirección de Antonio Gálvez](https://www.youtube.com/watch?v=w9uTUfL7zf0)»
  (no pude leerlos: YouTube limitaba).
- En **España** hay otro doblaje y allí es «**Velma**»; en Latinoamérica
  siempre «**Vilma**» ✅ (Doblaje Wiki). **No mezclar**.

---

## 11 · Música

| Tema | Qué es | Ambiente | Fuente |
|---|---|---|---|
| **«Scooby-Doo, Where Are You!»** | Tema de 1969, de **David Mook y Ben Raleigh**. Lo canta **Larry Marks** (T1) y **George A. Robertson Jr.** (T2) | Pop de los 60, alegre con susto | ✅ Wikipedia y Animation Wiki |
| **Las canciones de persecución** (*chase songs*) | De **Danny Janssen y Austin Roberts**, cantadas por **Roberts** (T2, La La Productions) | Pop chicle mientras huyen del monstruo | ✅ Wikipedia y Scoobypedia |
| **Música de fondo** | Compositor **Ted Nichols** (1969-1970) | Órgano, cuerdas de miedo ⚠️ | ✅ (la búsqueda) |
| **Intro latina** | En el doblaje de 1969 **la canción no se dobló**: sonaba el instrumental de **Ted Nichols** (primeros episodios) o el tema de Mook y Raleigh (instrumental, o con la voz de Austin Roberts en la T2), y **Shaggy (Arturo Mercado) gritaba «¡Scooby-Doo, ¿dónde estás?!»** sobre el logo en inglés; Daphne (María Santander) tenía otro inserto. Desde 2011, Cartoon Network, Boomerang y Tooncast pasan una versión recortada del instrumental de Nichols. Las **canciones de persecución de la T2** («Love the World», «Recipe for My Love», «I Can Make You Happy», «Seven Days a Week») **quedaron mudas** en el doblaje por un error de mezcla ([intro en YouTube](https://www.youtube.com/watch?v=6Jj8sIcCsuU)) | Pop instrumental | ⚠️ sólo Doblaje Wiki (fuente detallada). La letra «Scooby Dooby Doo, ¿dónde estás? Tenemos mucho trabajo por hacer» es **una traducción de fans**, no el doblaje |
| **«What's New, Scooby-Doo?»** | Tema de la serie de 2002, por **Simple Plan** | Pop punk | ✅ (letras.com y la búsqueda) |
| **«Scooby Doo Pa Pa»** | De **DJ Kass**, dominicano criado en el Bronx. En 2018 se llamó «**el nuevo baile de moda**»; baile en fila en TikTok e Instagram; sigue saliendo en tendencias | Fiesta latina | ✅ [Wikipedia](https://en.wikipedia.org/wiki/DJ_Kass) y [TikTok (sonido)](https://www.tiktok.com/music/Scooby-Doo-Pa-Pa-6529585632031806464) |

> [!tip] «Scooby Doo Pa Pa» es latino
> Para un servidor de Perú, México, Venezuela y Colombia, **«Scooby Doo Pa
> Pa»** es tan conocido como la serie. No hace falta ponerlo en la lámina,
> pero es un guiño que se entiende.

---

## 12 · Vídeos

Duración y fecha sacadas con `yt-dlp`. Los **minutos** salen de los
**subtítulos automáticos en español** de cada vídeo (fiables en el
tiempo; la palabra exacta puede fallar). No vi las imágenes en
movimiento.

### 12.1 Oficiales en latino (canal WB Kids Latino)

| Vídeo | Duración y fecha | Minuto útil | Para qué |
|---|---|---|---|
| [«Scooby-Doo Expone a Los Malos»](https://www.youtube.com/watch?v=r1sQtlBZHHQ) (recopilación de *¿Dónde estás?*; Doblaje Wiki lo cita como muestra del doblaje de 1969) | 23:49 | **00:02:49** «Ahora veamos quién está detrás de la…»; **00:07:51** «veamos quién es el impostor»; **00:17:24** «**y hubiera sido mío de no haber sido por esos chicos entrometidos**»; **00:17:30** «con eso terminó el misterio, vamos a **la fuente de soda**»; **00:21:02** «**ya que el caso está resuelto**…» | **Resuelta**: las frases exactas del doblaje |
| [«prepara la trampa»](https://www.youtube.com/watch?v=xZV_2-7OBRU) | 29:15 (13-1-2018) | **00:08:39** «¡**Caracoles**!»; 00:11:00 «trampa número 3 activada por luz»; 00:12:58 «decir que **el misterio está resuelto**» | Fred y sus trampas |
| [«Computadoras»](https://www.youtube.com/watch?v=BtGo-X-jjP8) | 6:49 (14-12-2022) | **00:00:51** «buscaremos **pistas**»; **00:01:21** «**Oigan, amantes de los misterios, habla Vilma**»; **00:01:56** «**¡Cielos, un misterio!**»; **00:05:25** «parece que **necesitan una pista**» | **Encaja con dudas técnicas**: buscar pistas en la computadora |
| [«Mejor de Velma»](https://www.youtube.com/watch?v=fdqVXWBkr9g) | 3:31 (2-11-2017) | **00:00:00** «Oigan, amantes de los misterios, habla Vilma»; 00:00:25 «estaré en **la biblioteca**» | Poses y voz de Vilma |
| [«¡Velma sabe!»](https://www.youtube.com/watch?v=zY8Vgn-bqhc) | 8:28 (1-11-2023) | **00:03:59** «Shaggy y Scooby tienen razón. **¡Cielos!**»; **00:04:45** «**La pregunta es**…»; **00:05:00** «ahora veamos de quién se trata»; **00:07:26** «antes de **contestar a tus preguntas**, tú debes contestar una» | **Vilma responde preguntas** |
| [«¡El regreso de los villanos del pasado!»](https://www.youtube.com/watch?v=M7hnzoDzBzs) | 4:35 (30-1-2019) | | Los villanos clásicos juntos |
| [«¡Las MEJORES escenas de la Temporada 1 de Misterios S.A.»](https://www.youtube.com/watch?v=XLqQfznKomA) | 49:37 | (no leído) | Estilo 2010 |
| [«Robot Explorador 1»](https://www.youtube.com/watch?v=fKuE09hl2Do), [«Atrapar al Minotauro»](https://www.youtube.com/watch?v=6MRulDo30e4), [«Niños Tenebrosos»](https://www.youtube.com/watch?v=AwmeF_GaBSE), [«Locura a medianoche»](https://www.youtube.com/watch?v=xE5CL1aTyDg) | | (no leídos) | Más clips doblados |
| [«¡SUPERCORTE de “Chicos entrometidos”!»](https://www.youtube.com/watch?v=qBIpQcjSyOk) (@GenWBLatino) | | **no se pudo leer** (YouTube 429) | Todos los desenmascarados |

### 12.2 Otros

| Vídeo | Enlace | Para qué |
|---|---|---|
| Intro latina de 1969 | [YouTube](https://www.youtube.com/watch?v=6Jj8sIcCsuU) | Shaggy grita «¡Scooby-Doo, ¿dónde estás?!» sobre el logo en inglés ✅ (Doblaje Wiki) |
| «El Doblaje Latino de Scooby-Doo: ¿Por qué es tan ICÓNICO?» | [YouTube](https://www.youtube.com/watch?v=f3Bkkvr1s8s) | Análisis (no leído) |
| «El doblaje de Scooby Doo Misterios S.A. y la dirección de Antonio Gálvez» | [YouTube](https://www.youtube.com/watch?v=w9uTUfL7zf0) | Análisis (no leído) |
| «Ultra Instinct Shaggy» | [Know Your Meme](https://knowyourmeme.com/videos/199349-ultra-instinct-shaggy) | El meme |
| «Scooby Doo Pa Pa - DJ Kass (TikTok Dance Challenge)» | [YouTube](https://www.youtube.com/watch?v=3mcnibRbGTw) | La tendencia de baile |
| TikTok | [#scoobydoo](https://www.tiktok.com/tag/scoobydoo), [«Veamos quién está detrás de la máscara»](https://www.tiktok.com/discover/scooby-doo-veamos-quien-esta-detras-de-la-mascara-scooby) | El desenmascarado como meme en latino |

**Tendencias de TikTok** ⚠️ (resumen de búsqueda, sin ver los vídeos):
el baile de «**Scooby Doo Pa Pa**» (vuelve cada año; en 2025, con
**gorilas hechos con IA**), el sonido «**dooby scooby doo**», y el cruce
**Shaggy con Billy Loomis** (*Scream*) en Halloween. Y siempre, el meme
del **desenmascarado**. Know Your Meme tiene 14 entradas de la serie:
«**Let's See Who This Really Is**», «**Scooby-Doo Doors**» (la
persecución de las puertas), «**Rehehehe / Scooby-Doo Laugh**» (la risa),
«**Missing Sixth Member of the Scooby-Doo Gang**», «**I Think Coolsville
Sucks**», entre otras ✅ (página de KYM leída).

---

## 13 · Videojuegos de la franquicia

| Juego | Año | Qué tiene que sirva | Estado |
|---|---|---|---|
| **Scooby-Doo Mystery** (SNES, de Argonaut; Genesis, de Illusions Gaming) | 1995 | SNES: plataformas con **pistas** en 4 misterios. Genesis: **aventura de apuntar y hacer clic** (2 misterios), muy parecida a la serie según *Electronic Gaming Monthly* (7,6 sobre 10) | ✅ Wikipedia, MobyGames |
| **Night of 100 Frights** (Heavy Iron, THQ) | 2002 | Niveles con nombres de chiste («Mind Your Manors!», «Shock on the Dock», «Scared Stiff at Skull Cliff!», «Panic in the Attic!», «On Edge In The Hedge», «Wreck on the Deck!»), **Scooby-galletas**, **fichas de monstruo** y una **Galería de Monstruos**, la **Mystic Manor** | ✅ código del randomizador [vgm5/Night_Of_100_Frights_ap_world](https://github.com/vgm5/Night_Of_100_Frights_ap_world) y TCRF (en la búsqueda) |
| **Mystery Mayhem** | 2004 | Cada nivel: **atrapar monstruos y encontrar 5 pistas**; las pistas abren **arte conceptual** en una galería | ✅ GameFAQs, TV Tropes |
| **Unmasked** | 2005 | **Pistas para Vilma** (abren niveles), ingredientes para Shaggy, **piezas de trampa**; en DS se **investiga la pista** con herramientas | ✅ Wikipedia, Nintendo Wiki |
| **LEGO Dimensions** (pack de Scooby-Doo) | 2015 | Shaggy con la voz de **Arturo Mercado Jr.** en latino ⚠️ | Doblaje Wiki |
| **MultiVersus** | 2022 y 2024 | **Vilma junta pruebas**; con el medidor lleno **resuelve el misterio** y llega **la Máquina del Misterio** a llevarse al rival (antes llegaba la policía y decía que el rival era «el viejo Jenkins»; lo cambiaron en el parche 1.02 tras las quejas). **Shaggy** juega con los poderes del meme Ultra Instinct y lanza sándwiches | ✅ PC Gamer, GameRevolution, GameSpot, CBR |
| **Fortnite** (Capítulo 6, Temporada 4) | 2025 | Lote «**Mystery Inc.**» con el pico «**Velma's Investigation Kit**» (una **lupa** inspirada en la furgoneta) | ✅ Scoobypedia (API) |
| **Dead by Daylight** | 2026 | Colección de aspectos de Scooby-Doo anunciada en el 10.º aniversario; fecha sin concretar | ⚠️ una fuente (Shacknews) |

**Lo que se saca para la lámina**: en todos los juegos **la pista es un
objeto que se junta** y, con todas, **el misterio se resuelve**. No hay
una «caja de diálogo» propia de Scooby-Doo en los juegos que merezca
copiarse: al dueño no le gustan los paneles de interfaz. Se usa **la
idea** (juntar pistas hasta resolver), no el panel.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

- **El desenmascarado** («Let's See Who This Really Is»): nace de
  **«Hassle in the Castle»** (27-9-1969), cuando la pandilla quita la
  máscara al fantasma y es **Bluestone el Grande**, un exmago ✅ (Know
  Your Meme y la base de datos). En latino: «**Ahora veamos quién está
  detrás de la máscara**» (vídeo oficial, 00:02:49 ✅).
- **«Chicos entrometidos»**: 189 finales con la frase ✅; en latino se
  conserva igual desde 1970 ✅ (Doblaje Wiki y vídeo 00:17:24).
- **«Es el viejo Jenkins»**: el chiste de que el villano siempre es un
  señor mayor. **No existe** un villano así en la base de datos ✅ (sólo
  una Sarah Jenkins, 1969); es un **chiste de fans**, que hasta
  *MultiVersus* usó ✅.
- **Las Scooby-galletas** y cómo **sobornan** a Scooby y Shaggy («¿Y
  tres?», 1978, 00:07:14 ✅). Hay decenas de cajas distintas en la wiki
  (G-18 a G-58).
- **La persecución de las puertas** (*Scooby-Doo Doors*): todos entran y
  salen de puertas en un pasillo con música pop. En la base de datos, 59
  episodios ✅.
- **La risa de Scooby** («Rehehehe») y el «**Scooby-Dooby-Doo**» del
  final ✅ (KYM).
- **Vilma sin gafas**, a gatas (G-100 ✅).
- **La trampa de Fred que falla** (la mitad de las veces ✅).
- **«Ultra Instinct Shaggy»** y **«Scooby Doo Pa Pa»** ✅.
- **La Malt Shop** («fuente de sodas» en latino): al resolver el caso, a
  celebrar ✅ (vídeo oficial 00:17:30 y 00:21:02).
- **Las películas que se recuerdan**: *La isla de los zombies* (1998,
  aquí los monstruos **eran reales**), *La bruja fantasma* (con las **Hex
  Girls**) y las de imagen real de 2002 y 2004 ✅ (base de datos y
  Doblaje Wiki). **Misterios S.A.** es la serie mejor valorada (8,29 de
  media) ✅.

### 14.2 Qué NO hacer (lo que un fan notaría)

1. **Poner a Scrappy-Doo** de protagonista: es el personaje más odiado ✅.
2. **Copiar el estilo de *Velma* (2023)**: **1,3** en IMDb y **6 %** del
   público en Rotten Tomatoes; es de las series peor puntuadas de la
   historia ✅ (Animation Magazine, MovieWeb, Forbes). Nada de su
   diseño ni de su tono.
3. **Hacerlo de terror de verdad**: nada de sangre ni letras que gotean
   rojo. Scooby-Doo da **miedo de risa**; en toda la franquicia **el
   monstruo es un señor disfrazado** en 404 de 516 casos con dato ✅.
4. **La policía llevándose al villano**: *MultiVersus* la quitó tras las
   quejas ✅. Para «Resuelta», mejor **la red de la trampa** o **la
   furgoneta**.
5. **Decir «Velma» en un texto en latino**: es **Vilma** ✅. Y «Mystery
   Inc.» es «**Misterio a la orden**»; «Scooby Snacks», «**Scooby-galletas**».
6. **Cambiar la ropa icónica**: Fred **sin su pañuelo naranja**, Vilma
   sin gafas cuadradas negras, Daphne sin pañuelo verde, Shaggy con
   camisa de otro color. (En algunas series cambian: el público reconoce
   la de 1969.)
7. **Scooby hablando con frases largas**: dice palabras sueltas con R.
8. **Dibujarlo como un perro real**: Scooby tiene barbilla hundida,
   patas arqueadas y **el collar azul con la placa en rombo** (C-15 ✅).
9. **Sombreado 3D en los personajes**: el estilo es **color plano** sobre
   **fondo pintado**.
10. **El hilo rojo de «serie policiaca oscura»** por todo el tablero:
    pocas líneas, fichas limpias, colores de los 60.
11. **Mezclar el doblaje de España** (allí «Velma», otras exclamaciones).

---

## 15 · Poses analizadas por personaje

Los números **C-** y **G-** son imágenes de las hojas que **vi**; lo
demás es subtítulo con minuto (la postura, de memoria ⚠️).

### Vilma

| # | Imagen o escena | Qué hace | Sirve para |
|---|---|---|---|
| 1 | **C-15** (ep. 2, algas brillantes) | Inclinada hacia la pista, **mano izquierda en la cadera**, ceño fruncido, gafas grandes | **Pensar** / examinar |
| 2 | **G-100** («A Gaggle of Galloping Ghosts») | **A gatas** en el suelo de madera, mano estirada, las gafas delante | Duda (**Sigue abierta**) con humor |
| 3 | **G-101** («It's Mean, It's Green…») | A gatas de noche buscando las gafas | Idem |
| 4 | **C-10** (muñeco vudú) | De pie, **manos a la espalda**, sonrisa tranquila | **Presentar** con calma |
| 5 | **C-6** (ep. «Foul Play in Funland») | Al volante, **a ciegas** | Chiste |
| 6 | **G-4** (cómic, club) | De pie junto a Fred, **manos a la espalda**, sonrisa pícara: «¿Qué es lo raro?» | **Preguntar** con interés |
| 7 | 1978, 00:08:38 | «**Alto ahí**. No nos vamos» | **Regañar** (frenar la huida) |
| 8 | Película 2002, 00:05:11 | «Yo puedo responder a eso. **Miren**» y enseña el truco | **Explicar** |
| 9 | Vídeo *Computadoras*, 00:01:21 | «Oigan, amantes de los misterios, habla Vilma» (presenta su programa) | **Presentar** |
| 10 | Película 2004, 01:00:32 | «Resolvíamos misterios por amor a ellos» | **Animar** |

### Shaggy

| # | Imagen o escena | Qué hace | Sirve para |
|---|---|---|---|
| 1 | **C-15** | **Sostiene la pista** (algas) con las dos manos, cara de asco y duda | **Enseñar** algo raro |
| 2 | **C-39** | Se topa con el Creeper, **boca abierta**, Scooby al lado | Susto |
| 3 | **C-22** | **Disfrazado** con gabardina y bombín | Chiste |
| 4 | **C-10** | Muñeco vudú: **cuello torcido**, sonrisa boba, brazos caídos | Relajado |
| 5 | **G-79** (cómic) | Tendiendo la ropa: «Like, this wind should…» | Hablar en globo de cómic |
| 6 | 1978, 00:07:14 | «¿Y **tres** galletas?» (negocia) | Humor |
| 7 | 1978, 00:19:44 | «¿Nos lo **explican otra vez**?» | **Preguntar** (la pose del canal) |
| 8 | Película 2004, 00:21:29 | «Eso **no son pistas**, Scoob» | **Regañar** con cariño |
| 9 | Película 2004, 00:22:12 | «¡Haz **el baile de la pista**!» | **Celebrar** |
| 10 | Cel 1stDibs | Corriendo con Scooby | Huida |

### Scooby-Doo

| # | Imagen o escena | Qué hace | Sirve para |
|---|---|---|---|
| 1 | **C-15** | **Sentado**, con las algas en la boca, **ojos de lado** («¿yo qué?») | **La pista la encontró él** |
| 2 | **C-18** («What the Hex Going On?») | **Cara de enfado**, dientes apretados, se enfrenta al fantasma | Valiente por un rato |
| 3 | **C-22** | **Disfrazado de cebo** con collar de pinchos rojo | Chiste |
| 4 | **C-39** | Mirando al Creeper, **cejas arriba** | Susto |
| 5 | 1978, 00:07:27 | **Olfateando** el rastro | **Buscar pistas** |
| 6 | 1978, 00:21:02 | «¡**Scooby-Dooby-Doo**!» | **Celebrar** (cierre) |
| 7 | Película 2004, 00:21:25 | Trae **un cepillo de váter** como «pista» | **La duda tonta** |
| 8 | Película 2004, 00:22:09 | «¡Encontré **una pista**!» | **Celebrar** |

### Fred

| # | Imagen o escena | Qué hace | Sirve para |
|---|---|---|---|
| 1 | **C-19** | De pie, **mano en el pecho**, mirando atrás al Caballero Negro | Alerta |
| 2 | **C-35** | **Lee un mapa** con las dos manos, Daphne al lado | **Leer la pista** |
| 3 | **G-4** (cómic) | **Mano en el bolsillo**, sonrisa segura | **Presentar** |
| 4 | **C-10** | Muñeco vudú: firme, mirada al frente | |
| 5 | 1978, 00:08:42 | «Vilma tiene razón» | Apoyar |
| 6 | 1978, 00:20:15 | «**Veamos quiénes son en realidad**» y quita la máscara | **Resuelta** |
| 7 | Película 2002, 00:26:57 | «**Separémonos** y busquemos más pistas» | **Sigue abierta** |
| 8 | Película 2004, 00:59:28 | «Miren, **todas mis viejas herramientas**» (el club) | El sitio |

### Daphne

| # | Imagen o escena | Qué hace | Sirve para |
|---|---|---|---|
| 1 | **G-4** (cómic) | **Sentada en el sofá** con una tableta, **boca abierta**: «Hmm, qué raro…» | **La duda**: descubre algo raro |
| 2 | **C-19** | En la puerta, **mano cerca de la cara**, asustada | Susto |
| 3 | **C-10** | Muñeco vudú, **mano en la cadera** | Presentar |
| 4 | **C-2** («Mystery Mask Mix-Up») | **Secuestrada** en un coche | «La peligrosa Daphne» |
| 5 | 1978, 00:05:18 | «**Jeepers**, ¿vieron eso?» | Señalar |
| 6 | 1978, 00:20:08 | **Explica** su parte del truco | Explicar |

### Qué pose para cada función del canal

| Función | Personaje y pose |
|---|---|
| **Presentar** el canal | Vilma con las manos a la espalda (C-10, G-4) o Fred con la mano en el bolsillo (G-4) |
| **Explicar** (cómo se usa) | Vilma señalando la ficha: «Yo puedo responder a eso. Miren» (2002, 00:05:11) |
| **Preguntar** («pregunta sin miedo») | **Shaggy con la pista en las manos** (C-15) o Daphne en el sofá (G-4) |
| **Pensar** | Vilma con la mano en la cadera (C-15) |
| **Sigue abierta** | Vilma a gatas buscando las gafas (G-100) o Fred «¡Separémonos!» |
| **Resuelta** / celebrar | Fred quitando la máscara; Scooby «¡Scooby-Dooby-Doo!»; Shaggy y Scooby «el baile de la pista» |
| **Regañar** (no mezclar temas) | Vilma «Alto ahí» o Shaggy «Eso no son pistas, Scoob» |
| **Animar** | Vilma: «Resolvíamos misterios por amor a ellos» |

---

## 16 · Vestuario

**La ropa icónica es la de 1969** (C-10, C-15, C-19 ✅). Colores medidos
en §5.3.

| Personaje | 1969 (la icónica) | Detalles que no se pueden olvidar |
|---|---|---|
| **Fred** | **Jersey blanco** de manga larga, **cuello azul** de camisa asomando, **pañuelo naranja** anudado al cuello, **pantalón azul**, zapatos marrones | El pañuelo (*ascot*) |
| **Daphne** | **Vestido morado corto** con **franjas lila**, **pañuelo verde** al cuello, **cinta morada** en el pelo, **medias rosas**, zapatos morados | Las medias rosas y el pañuelo verde |
| **Vilma** | **Jersey naranja de cuello alto**, muy ancho, **falda roja plisada**, **calcetines naranjas** hasta la rodilla, **zapatos rojos** de merceditas, **gafas negras cuadradas** | Las gafas y los calcetines |
| **Shaggy** | **Camiseta verde de cuello en V**, **pantalón granate acampanado**, zapatos negros; pelo castaño revuelto y **perilla** | El granate, no marrón |
| **Scooby** | Marrón con **manchas negras**, **collar azul** con **placa dorada en rombo** con «SD» | La placa en rombo |

**Otras épocas** (para no confundirse):
- **Misterios S.A.** (2010): mismos colores, líneas más finas y
  angulosas (G-9 a G-17, 1920×1080 ✅). Fred sigue con pañuelo.
- **Películas 2002 y 2004**: Vilma con jersey naranja, Daphne con
  morado y verde, Fred con **pañuelo** («¡Cuidado con el pañuelo!»,
  00:06:11 ✅).
- **Cómics de DC** (G-4 ✅): la ropa de 1969 con color más vivo.
- **Disfraces**: en la serie se disfrazan a menudo (C-22 ✅).

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz (vistos en la hoja F)

| Sitio | Imagen | Hora y luz |
|---|---|---|
| **Castillo con luna** | F-10 | Noche azul, luna celeste |
| **Casa encantada** con ventanas encendidas | F-15, F-26 | Noche, **ventanas amarillas** |
| **Mansión con rayo** | F-16 | Tormenta, azul gris |
| **Malt Shop** («fuente de sodas») | F-8 | Tarde, **verde agua y ocre** |
| **Feria** («FUN FUN», «FUNHOUSE») | F-4, F-9 | Noche con **bombillas** |
| **Rancho «Gold City»** | F-20 | Noche morada |
| **Barco fantasma** | F-3 | Noche azul con niebla |
| **Cementerio** | F-11 | Noche, lápidas grises |
| **Cabaña del pantano** | F-13, F-25 | Noche, niebla verde |
| **Salón rojo con chimenea** | F-18 | Fuego, rojo y magenta |
| **Cuarto con vela verde** | F-24 | Penumbra ocre, luz verde |
| **Pared de máscaras** | F-22 | Interior oscuro |
| **Ciudad de noche** | F-27 | Rascacielos azules con ventanas encendidas |

### 17.2 Fondos de pantalla

| Qué | Enlace | Tamaño | Nota |
|---|---|---|---|
| 361 fondos de Scooby-Doo | [Wallpapers.com](https://wallpapers.com/scooby-doo) | hasta 1920×1080 | Mezcla oficial y fans ✅ (búsqueda) |
| «Haunted Mansion from Scooby Doo» | [Wallpapers.com](https://wallpapers.com/background/scooby-doo-background-dfh4old3rzu8i1ce.html) | varios | Casa encantada |
| Cel de producción con la furgoneta y la mansión | [WallHere 2244454](https://wallhere.com/en/wallpaper/2244454) | 1920×1080 | ✅ (búsqueda) |
| **27 fondos originales de 1969** | [Secret Fun Spot](https://secretfunspot.blogspot.com/2007/10/50-scooby-doo-background-paintings.html) | 720×540 (DVD) | ✅ bajados y medidos (hoja F) |
| Fondos de *Misterios S.A.* | Scoobypedia (G-9 a G-17) | 1920×1080 | ✅ |

> [!warning] Resolución
> Los fondos de 1969 que hay en internet salen del DVD: **720×540**. Para
> una lámina de 1200×800 (o ×3 al renderizar) **no se pueden usar tal
> cual**: sirven de **referencia de paleta y de composición**. El fondo
> se **pinta de nuevo** (o se hace en Blender) siguiendo F-10, F-15 y
> F-22.

---

## 18 · Guía para generar con IA (Firefly, Canva)

> [!warning] Para qué sí y para qué no
> La IA sirve para **fondos, objetos y poses de apoyo**. **No** para
> inventar a los personajes: salen deformes y el fan lo nota. Los
> personajes se recortan de fotogramas reales (C-10, C-15, C-19, G-4,
> G-100) y se integran con `v3/integrar.py` (regla 3 del dueño).

### 18.1 Rasgos que nunca cambian

- **Scooby**: gran danés **marrón** con **manchas negras** en el lomo,
  **barbilla hundida**, **nariz negra grande**, **collar azul** con
  **placa dorada en rombo**, cola larga, orejas caídas con interior más
  claro.
- **Shaggy**: flaco y alto, **encorvado**, pelo castaño revuelto,
  **perilla**, camiseta **verde** en V, pantalón **granate** acampanado.
- **Vilma**: bajita, **melena corta castaña con flequillo recto**,
  **gafas negras cuadradas grandes**, jersey **naranja de cuello alto**
  muy holgado, falda **roja plisada**, calcetines **naranjas**.
- **Fred**: alto, **rubio**, mandíbula cuadrada, jersey **blanco**,
  **cuello azul**, **pañuelo naranja** al cuello, pantalón **azul**.
- **Daphne**: **pelirroja** de melena larga con **cinta morada**,
  vestido **morado** con franjas lila, **pañuelo verde**, **medias
  rosas**.

### 18.2 El estilo

- **Línea**: contorno **negro fino y uniforme** (C-43, hoja de modelo de
  1969).
- **Color de los personajes**: **plano**, sin degradado, casi sin sombra.
- **Fondo**: **pintado a pincel** (gouache), con textura, degradados y
  siluetas oscuras; **más detallado que los personajes**.
- **Luz**: noche **azul cobalto** con luna **celeste**, ventanas
  **amarillas**, brillos **verde fosforito** de lo fantasmal; interiores
  en **rojo y morado** o **ocre con vela verde** (§5.2).
- **Encuadre**: plano general a la altura de los ojos, como en la serie
  de televisión; composiciones anchas.

### 18.3 Palabras que ayudan (en inglés, para Firefly)

- *1969 Hanna-Barbera cartoon background, hand-painted gouache,
  flat cel animation style, thin black outlines*
- *haunted mansion at night, deep cobalt blue sky, pale cyan full moon,
  glowing yellow windows, eerie green glow, bare black trees*
- *cozy teen clubhouse interior 1960s, wood paneling, bookshelves, green
  sofa, cork bulletin board with index cards and pushpins*
- *vintage 1960s index card, typewriter text, rubber stamp*
- *monster rubber mask hanging on a nail, museum label*

### 18.4 Palabras que lo estropean

- *realistic, photorealistic, 3D render, Pixar* (sale 3D, no dibujo).
- *gore, blood, horror, creepy realistic* (sale terror de verdad).
- *anime, manga* (cambia ojos y proporciones).
- *Velma 2023, adult animation* (el estilo odiado).
- *red string conspiracy board, crime drama* (sale serie policiaca).
- Nombres de personajes con marca: la IA inventa versiones falsas.

### 18.5 Qué imágenes usar de referencia

| Para | Imagen |
|---|---|
| Estilo de fondo nocturno | **F-10**, **F-15**, **F-16** |
| Interior | **F-24** (vela verde), **F-18** (salón rojo), **G-4** (club, cómic) |
| La pared de máscaras | **F-22** |
| La Malt Shop | **F-8** |
| Colores de la ropa | **C-10** (luz neutra) |
| Tipo de línea | **C-43** (hoja de modelo de 1969) |
| Pose de Vilma pensando y Shaggy con la pista | **C-15** |
| Composición de título | **C-47** |

---

## 19 · Tres conceptos para la lámina de #dudas

Los tres cumplen las reglas del dueño: **objeto real en un sitio real**
de la serie, **personaje con la pose que va con lo que dice**, **texto
corto en la voz de la serie** y **lámina 2** para las etiquetas.

### Concepto A — «El tablero de pistas del club» (el objeto del plan, mejorado)

- **El objeto**: un **tablero de corcho** con marco de madera, colgado en
  la pared del **club de Misterio a la Orden** (el «viejo club del
  instituto» de la película 2004, 00:58:30 ✅; el salón del club de los
  cómics, G-4 ✅: estanterías, sofá verde, **foto enmarcada de la pandilla
  con la furgoneta**). Se hace en **Blender**: corcho (modelo de
  **sousinho**), chinchetas (**plaggy**), fichas de papel con leve curva,
  una **lupa** (**risteralline**) apoyada en el marco.
- **El tablero tiene dos mitades**, como el canal:
  - **Izquierda, «SIGUE ABIERTA»**: fichas con un **signo de
    interrogación** dibujado a mano y **huellas de monstruo** en el corcho.
    La ficha de ejemplo: «**Se me oye el ratón al grabar, ¿cómo lo
    quito?**» (el hilo real del inventario).
  - **Derecha, «RESUELTA»**: la **máscara de monstruo colgada de un clavo**
    (como la pared de F-22) con una **etiqueta de equipaje** atada, y una
    ficha «Who's Who» con el sello **RESUELTA**.
- **Quién**: **Vilma** a la derecha, **inclinada hacia el tablero con la
  mano en la cadera** (pose de C-15), señalando una ficha. **Shaggy y
  Scooby** asomados **desde abajo a la izquierda**, detrás del sofá, con
  una **caja de Scooby-galletas** (Shaggy con cara de «¿nos lo explican
  otra vez?»).
- **Cómo habla**: no hay globo. **Vilma escribe en las fichas** (Caveat).
  Si hace falta una frase suya: **globo de cómic de DC** (G-4) con «**¡Cielos!
  Pregunta sin miedo, por tonta que te parezca**». Shaggy, en otro globo
  pequeño: «**¿Nos lo explican otra vez?**».
- **Dónde va cada texto**:
  - Arriba, **letrero de madera pintado** sobre el tablero: «**DUDAS**»
    (Luckiest Guy o la fuente «Scooby Doo», blanco con contorno negro).
  - **Ficha grande clavada en el centro**: «**Un hilo por duda**».
  - **Ficha a la izquierda**: «**Etiqueta la disciplina**».
  - **Cabeceras de cada mitad**, en cinta de papel: «**SIGUE ABIERTA**» y
    «**RESUELTA**» (League Gothic, amarillo como los títulos de 1969).
  - **Ficha con sello**: «**Marca Resuelta cuando lo esté**».
  - Globo de Vilma: el gancho.
- **Cómo no queda plano**: **lámpara de mesa** encendida a la izquierda
  (luz cálida sobre el corcho) y **ventana de noche azul** a la derecha
  con la luna celeste (F-10): dos luces, dos colores. **Delante**, fuera
  de foco, **la oreja y la nariz de Scooby** entrando por abajo y la
  **caja de Scooby-galletas**. Las fichas **proyectan sombra** en el
  corcho.

### Concepto B — «La vitrina del Museo de Criminología de Coolsville»

- **El objeto**: las **vitrinas del museo** donde la pandilla **dona los
  disfraces de los villanos que desenmascaró** (película 2004, 00:02:08 a
  00:04:37 ✅). Cada vitrina es **una duda resuelta**, con su **cartela
  de latón**. En **Blender**: vitrinas de cristal, cartelas, **cordones
  de terciopelo** delante.
- **Resuelta**: una vitrina con **el disfraz del Caballero Negro** (el
  primer villano, 1969 ✅) o del Space Kook (C-24), y la cartela
  «**RESUELTA**».
- **Sigue abierta**: la **vitrina vacía** del centro, con un **signo de
  interrogación** en la cartela y huellas en el suelo.
- **Quién**: **Fred** como guía, **quitando la máscara** a un maniquí o
  señalando la vitrina (desenmascara 102 veces ✅); **Daphne** a su lado
  leyendo la cartela. O **Vilma** con la lupa ante la vitrina vacía.
- **Cómo habla**: con **las cartelas del museo** (Special Elite sobre
  latón) y un **titular de periódico** enmarcado en la pared:
  «**¡CASO RESUELTO!**» (como C-45).
- **Dónde va cada texto**: el **rótulo del museo** arriba: «**DUDAS**»; el
  **cartel de la entrada**: «**Pregunta sin miedo, por tonta que te
  parezca**»; **cartela de la vitrina vacía**: «**Un hilo por duda**»;
  **segunda cartela**, más pequeña: «**Etiqueta la disciplina**»; **cartela de la vitrina llena**: «**Marca
  Resuelta cuando lo esté**»; el **periódico**: «**¡Caso resuelto!**».
- **Cómo no queda plano**: **focos de museo** desde arriba (conos de luz
  sobre cada vitrina), **reflejos en el cristal**, los **cordones de
  terciopelo** delante en primer plano y el pasillo que se pierde al
  fondo.

### Concepto C — «La Máquina del Misterio a medianoche»

- **El objeto**: **la furgoneta**, aparcada frente a la **casa
  encantada** (F-15), con las **puertas traseras abiertas**. Dentro,
  pegado a la puerta, un **tablero de pistas pequeño** con la lista de
  Vilma. En **Blender**: la furgoneta ligera de **smoler_man** (6254
  polígonos, regla 9), repintada con los colores de 1969.
- **Quién**: **Shaggy y Scooby** sentados en el borde trasero, con **un
  sándwich gigante**, **mirando la lista con duda** (pose de C-15, con
  Shaggy sosteniendo algo). **Vilma** de pie con la **linterna**, que es
  la fuente de luz, leyendo la lista.
- **Cómo habla**: el **panel verde del costado** lleva «**DUDAS**» en las
  letras naranjas de «THE MYSTERY MACHINE». Shaggy, en globo de cómic:
  «**¿Nos lo explican otra vez?**». Vilma responde en la lista.
- **Dónde va cada texto**: panel lateral: «**DUDAS**»; **matrícula**:
  «**UN HILO POR DUDA**»; lista pegada en la puerta: «**Pregunta sin
  miedo**», «**Etiqueta la disciplina**», «**Marca Resuelta cuando lo
  esté**»; dos **pegatinas de flor** naranjas con «**RESUELTA**» y
  «**SIGUE ABIERTA**».
- **Cómo no queda plano**: **haz de la linterna** atravesando la
  **niebla verde**; **faros** encendidos; la casa al fondo con ventanas
  amarillas; delante, **la rueda de repuesto con la flor** y hierba
  alta.

### ¿Cuál primero?

**El concepto A.** Es el objeto del plan (el tablero), está en un sitio
real de la franquicia (el club), el tablero **se parte en «Sigue
abierta» y «Resuelta»** como el canal, y reparte los papeles como
funciona un foro de dudas: **Shaggy y Scooby preguntan, Vilma
responde**. El B es el más elegante (museo, luz de focos) y encaja con
la película 2004, pero pide más modelado. El C es el más reconocible
(la furgoneta), pero el texto queda más apretado.

### La lámina 2 (las etiquetas)

**Objeto**: el **mismo tablero**, de cerca, o **una caja de fichas** de
Vilma con separadores de colores. **Tres filas de fichas**, cada una con
su **color de chincheta**:

| Chincheta | Fila | Fichas |
|---|---|---|
| **Naranja** (Vilma) | **De qué va** | Doblaje · Canto · Locución · Edición |
| **Verde** (Shaggy) | **Dónde está el fallo** | Del programa · Del micro |
| **Azul** (Fred) | **Cómo va** | Resuelta · Sigue abierta |

Con **Scooby olfateando** la fila de abajo y la lupa sobre «Del micro».

---

## 20 · Lo que no pude verificar

- **Un «tablero de pistas» en la serie**: no hay ninguno canónico que yo
  encontrara (busqué en la web y en Scoobypedia). Es una **propuesta**
  razonable, apoyada en el club, las máscaras colgadas (F-22) y el museo.
- **Minutos de la serie de 1969**: no hay subtítulos con tiempos en
  GitHub; los de los vídeos oficiales son **recopilaciones**, no
  episodios enteros.
- **El vídeo «Supercorte de chicos entrometidos»**: YouTube dio 429.
- **Voces de Fred, Daphne y Vilma en 1969** y de las series de los 70:
  sólo Doblaje Wiki (una fuente).
- **Letra de la intro latina**: no la encontré transcrita del doblaje.
- **TV Tropes y The Cutting Room Floor**: 403 incluso con la red
  abierta. Lo que cito de ellos sale de resúmenes de búsqueda.
- **Encuesta oficial de popularidad**: no existe (o no la hallé).
- **Colores de la furgoneta**: no medidos (las imágenes que tenía eran de
  noche); van aproximados.
- **Wikipedia**: 429 (demasiadas peticiones); cito lo que salió en la
  búsqueda.
- **Poly Haven y ambientCG**: bloqueados; las texturas de corcho y madera
  hay que buscarlas desde la PC.

---

## 21 · Bitácora de búsqueda

### 21.1 Comprobación de red (24-sep-2026)

| Fase | Qué respondía | Qué no |
|---|---|---|
| **1 (red cerrada)** | WebSearch, GitHub (clon y raw), google/fonts | Fandom, Doblaje Wiki, Wikipedia, YouTube, dafont, Poly Haven, ambientCG, TCRF, blogspot (`EGRESS_BLOCKED` o `000`) |
| **2 (red abierta)** | Scoobypedia y Doblaje Wiki por API, ANMTV, SensaCine, Sketchfab (API), Arctic Shift, Know Your Meme, blogspot, dafont, YouTube (a ratos) | TV Tropes (403), TCRF (403), Wikipedia (429), YouTube en algunos vídeos (429), Poly Haven y ambientCG, laurenashpole.com |

### 21.2 Búsquedas web (44)

Español (es), inglés (en), japonés (ja).

1. (es) Scooby-Doo doblaje latino reparto Shaggy Arturo Mercado Vilma Daphne Fred voces
2. (es) «Scooby-Doo, ¿dónde estás?» doblaje Doblaje Wiki reparto «Misterio a la Orden»
3. (es) Vilma Dinkley Doblaje Wiki voz latina Irene Jiménez Rocío Garcel Mónica Manjarrez
4. (es) Daphne Blake Doblaje Wiki voz latina Yolanda Vidal; Fred Jones Luis Alfonso Padilla Ricardo Mendoza
5. (es) Scooby-Doo cambio de voces doblaje latino 2015
6. (es) Scooby-Doo personaje Doblaje Wiki voz Antonio Gálvez Jorge Arvizu Ismael Larumbe
7. (es) ANMTV Happy Halloween Scooby-Doo reparto de voces
8. (es) SensaCine ¡Scooby! doblaje español latino
9. (es) «chicos entrometidos» Scooby-Doo frase doblaje latino
10. (es) Scooby-Doo frases doblaje latino ¡Cielos! ¡Caracoles! galletas separémonos
11. (en) Mystery Incorporated gang hideout clue board Crystal Cove
12. (en) MultiVersus Velma evidence clue mechanic case closed
13. (en) most popular Scooby-Doo character poll YouGov
14. (en) Iwao Takamoto Scooby design model sheet Joe Ruby Ken Spears
15. (en) Ultra Instinct Shaggy meme origin MultiVersus
16. (en) Scrappy-Doo most hated; Velma 2023 backlash
17. (en) «Let's see who this really is» unmasking meme origin
18. (es) «Scooby Doo Pa Pa» DJ Kass origen TikTok
19. (en) Scooby-Doo, Where Are You! theme Mook Raleigh Larry Marks chase songs
20. (es) canción tema en español latino «Scooby Doo, ¿dónde estás?»; Simple Plan
21. (en) Scooby-Doo logo font typeface dafont
22. (en) Mystery Machine original design colors lettering
23. (en) 1969 background painters Walt Peregoy Fernando Montealegre
24. (en) Mystery Incorporated Derrick J. Wyatt character design
25. (en) Night of 100 Frights dialogue, The Cutting Room Floor
26. (en) Scooby-Doo Mystery 1995 SNES Genesis
27. (en) new Scooby-Doo video game 2025 2026
28. (en) Unmasked / Mystery Mayhem / Who's Watching Who clue mechanic
29. (en) Sketchfab Mystery Machine CC Attribution
30. (en) Sketchfab cork board evidence board CC
31. (en) Scooby-Doo name origin Sinatra «Strangers in the Night» Fred Silverman
32. (en) gang costume colors (Velma, Daphne, Fred, Shaggy)
33. (en) Coolsville hometown clubhouse malt shop
34. (en) 50th anniversary 2019 official key art
35. (en) DC Comics Scooby-Doo, Where Are You! Sholly Fisch Dario Brizuela
36. (ja) スクービー・ドゥー 日本語吹き替え 声優
37. (en) Scooby-Doo TikTok trend 2025
38. (es) WB Kids Latino «Scooby-Doo! en Latino» Velma pistas
39. (en) TV Tropes «Scooby-Doo» Hoax, Let's Split Up Gang, Meddling Kids
40. (es) «Misterios S.A.» doblaje latino reparto
41. (es) Scooby-Doo película 2002 doblaje latino
42. (en) Scooby-Doo clue board / evidence board episode
43. (en) Scooby-Doo wallpaper 4K 1920×1080
44. (es) «Scooby-Doo y ¿quién crees?» doblaje latino reparto

### 21.3 GitHub (búsquedas y clones)

- Búsqueda de repositorios: «scooby doo transcripts», «scooby-doo
  subtitles srt» (0 resultados), «scooby» (1403).
- Búsqueda de código: «ruh-roh zoinks jinkies», «"meddling kids"
  extension:srt», «"split up" Scooby extension:srt», «"Mystery Machine"
  Velma extension:srt», «Scooby in:path extension:srt».
- Descargados: [rfordatascience/tidytuesday](https://github.com/rfordatascience/tidytuesday/tree/master/data/2021/2021-07-13)
  (base de datos), [mesutgurlek/Movie-Category-Classification-from-Subtitles](https://github.com/mesutgurlek/Movie-Category-Classification-from-Subtitles)
  (episodio de 1978), [imkira3/imkira3Keys](https://github.com/imkira3/imkira3Keys)
  (películas 2002 y 2004), [vgm5/Night_Of_100_Frights_ap_world](https://github.com/vgm5/Night_Of_100_Frights_ap_world)
  (nombres del juego), [google/fonts](https://github.com/google/fonts) (34
  letras comprobadas), [homoquiestfaba/Subtitle_Stylometry](https://github.com/homoquiestfaba/Subtitle_Stylometry)
  (índice: sólo películas, sin archivos útiles), [rzmic/tes](https://github.com/rzmic/tes)
  (subtítulo en indonesio: descartado), [aryankadam1256/StreamSage](https://github.com/aryankadam1256/StreamSage)
  (subtítulos falsos: descartado).

### 21.4 Con la red abierta

- `investigar_serie.py` en Scoobypedia: 19 páginas generales + 25
  episodios de 1969-1970 → 191 imágenes grandes, 5 hojas, 30 originales
  bajados.
- Scoobypedia por API: páginas del club (DC), Malt Shop, Coolsville,
  Mystery Machine, Daily Babbler, lupa de Vilma, kit de Fortnite, y el
  uso de cada imagen (`imageusage`).
- Doblaje Wiki por API: 22 páginas.
- ANMTV (3 artículos) y SensaCine (1).
- `yt-dlp`: búsqueda en YouTube + subtítulos automáticos en español de 6
  vídeos oficiales de WB Kids Latino.
- API de Sketchfab: 8 búsquedas y 10 modelos comprobados uno a uno.
- Arctic Shift: 6 búsquedas en r/Scoobydoo y 3 hilos de comentarios.
- Know Your Meme (2 páginas) y el blog Secret Fun Spot (27 fondos).
- dafont: la fuente «Scooby Doo» de Lauren Ashpole, comprobada.

### 21.5 Fuentes consultadas por tipo (más de 40 distintas)

| Tipo | Fuentes |
|---|---|
| **Oficiales** | WB Kids Latino (YouTube, 6 vídeos leídos), @GenWBLatino, [DC Comics](https://www.dc.com/comics/scooby-doo-where-are-you-2010/scooby-doo-where-are-you-67), [PR Newswire (50 aniversario)](https://www.prnewswire.com/news-releases/warner-bros-celebrates-50-years-of-scooby-doo-with-a-50-days-of-scooby-fan-and-family-celebration-300883329.html), hoja de modelo de 1969 (C-43) |
| **Staff y producción** | [Cartoon Research](https://cartoonresearch.com/index.php/the-origin-of-scooby-doo/), [podcast *Unmasked History of Scooby-Doo*](https://www.unmaskedsdpodcast.com/2020/09/18/uhsd-episode-14-derrick-j-wyatt/), [Cartoon Brew](https://www.cartoonbrew.com/rip/derrick-wyatt-character-designer-on-teen-titans-transformers-and-scooby-doo-dies-at-49-211888.html), [RX Music](https://rxmusic.com/editorial/the-scooby-sinatra-connection/), [Van Eaton Galleries](https://vegalleries.com/art/hanna-barbera/236/scooby-doo-1969-present/scooby-doo-where-are-you-first-scene-background-development), [Heritage Auctions](https://comics.ha.com/itm/animation-art/concept-art/scooby-doo-where-are-you-background-layout-art-hanna-barbera-1969-/a/7193-97542.s), [1stDibs](https://www.1stdibs.com/art/more-art/hanna-barbera-studio-artists-scooby-doo-original-cel-signed-bob-singer-iwao-takamoto-scooby-shaggy/id-a_13951682/), [Choice Fine Art](https://choicefineart.com/products/mystery-gang-model-sheet-1) |
| **Wikis** | Scoobypedia (API), Doblaje Wiki (API), Hanna-Barbera Wiki, Wikipedia (en la búsqueda), Animation Wiki, Nintendo Wiki, MultiVersus Wiki, Loathsome Characters Wiki |
| **TV Tropes / TCRF** | TV Tropes (Scooby-Doo Hoax, Mystery Mayhem, SNES) y TCRF (Night of 100 Frights): **sólo por resumen de búsqueda** (403) |
| **Doblaje** | Doblaje Wiki, [ANMTV](https://www.anmtvla.com/2020/08/se-revela-reparto-de-voces-de-happy.html), [SensaCine](https://www.sensacine.com.mx/noticias/noticia-18567589/), The Dubbing Database, [Change.org](https://www.change.org/p/warner-brothers-regresen-el-doblaje-original-de-scooby-doo), TikTok «Joyas del Doblaje» |
| **Foros y comunidades** | Reddit r/Scoobydoo (Arctic Shift), Scoobypedia (encuesta), IMDb (encuesta), Fanpop, Tumblr (atomic-chronoscaph), Facebook (Traditional Animation, CID San Luis) |
| **Memes** | [Know Your Meme](https://knowyourmeme.com/memes/lets-see-who-this-really-is), [CBR](https://www.cbr.com/ultra-instinct-shaggy-history-explained/), Georgetown Voice |
| **Prensa** | PC Gamer, GameRevolution, GameSpot, Animation Magazine, MovieWeb, Forbes, Far Out, Screen Rant, Collider, Hagerty, Looper, Shacknews |
| **Arte** | [Secret Fun Spot](https://secretfunspot.blogspot.com/2007/10/50-scooby-doo-background-paintings.html), DeviantArt (WileE2005, brazilianferalcat, Charlieaat), Wallpapers.com, WallHere, 1000logos |
| **Vídeo** | YouTube (WB Kids Latino, análisis del doblaje), TikTok (#scoobydoo, «Veamos quién está detrás de la máscara», sonido de DJ Kass) |
| **Código y recursos** | GitHub (TidyTuesday, subtítulos, randomizador de N100F, google/fonts), Sketchfab (API), dafont |
| **Datos** | Kaggle vía TidyTuesday (603 episodios), GameFAQs, MobyGames |
| **Otros idiomas** | Japonés: U-NEXT, eiga.com, ピクシブ百科事典 (sólo la película de 2002; sin datos útiles de voces). Scooby-Doo es de EE. UU.: no busqué en coreano ni chino |

### 21.6 Lo que NO encontré

- Un **tablero de pistas** canónico en la serie.
- **Subtítulos con tiempos** de *¿Dónde estás?* (1969) y de *Misterios
  S.A.*
- Una **encuesta oficial** de popularidad de personajes.
- La **letra exacta** de la intro latina.
- Imágenes de la serie clásica **en más de 1440×1080** (las de la wiki
  son remasterizaciones de 1440×1080; los fondos, de DVD a 720×540).
- Las páginas de **TV Tropes** y **TCRF** (403) y de **Wikipedia** (429).
- El vídeo «**Supercorte de chicos entrometidos**» (YouTube 429).
- Texturas de **Poly Haven** y **ambientCG** (bloqueadas).
