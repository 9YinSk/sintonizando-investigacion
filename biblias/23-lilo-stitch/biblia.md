---
tags: [biblia, serie, laminas]
serie: "Lilo & Stitch"
canal: "#fotos"
fecha: 2026-09-24
---

# Biblia · Lilo & Stitch — para #fotos

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada (24-25 de septiembre de 2026), con la red abierta.**
>   Cuatro investigadores (imagen, vídeo, voz y texto) dejaron sus notas en
>   `partes/`, y el redactor las metió aquí sección por sección. Esta vez
>   **sí se miraron vídeos**: la película de 2002 entera en Internet Archive
>   (copia `lilo-stitch-2002_202609`, 85 min, audio francés, imagen
>   original), el tráiler de 2002, los créditos finales, el luau en 1080p y
>   el tráiler latino de 2025 en Dailymotion, con `fotogramas.py`. Colores
>   medidos con Pillow y `estilo.py`. Doblaje comprobado en Doblaje Wiki
>   (API) y The Dubbing Database. Licencias de Sketchfab leídas en su API.
>   Letras comprobadas con fontTools. 3 hojas de contacto en `hojas/`.
> - **Ojo con los minutos**: los de la primera pasada (formato `00:22:54`)
>   salen de subtítulos del Blu-ray. Los de la segunda (formato `22:10` y
>   enlaces `?t=`) salen de la copia de Internet Archive: coinciden ±10 s,
>   a veces hasta ~30 s por los créditos iniciales distintos.
> - Lo que sigue abajo es el recuadro de la **primera pasada** (24-sep,
>   red cerrada). Lo dejo como historia; lo que la segunda corrigió está
>   en «Segunda pasada · qué cambió».
>
> **Primera pasada:**
> - La red de esta sesión estaba cerrada. Fandom (también Doblaje Wiki y la
>   wiki de Disney), Wikipedia, YouTube, IMDb, clip.cafe, eldoblaje.com,
>   ANMTV, Game UI Database y los espejos de Fandom (BreezeWiki,
>   antifandom) daban **403** por curl o «bloqueado» por WebFetch.
>   Por eso **no se pudo correr** `herramientas/investigar_serie.py`:
>   **no hay hojas de contacto** ni carpeta `hojas/`.
> - Hice **51 búsquedas web** (español, inglés, japonés, chino y
>   coreano). La lista está al final, en la bitácora. Cito **78 sitios
>   distintos**.
> - GitHub sí respondía. De ahí saqué lo más útil: **dos subtítulos en
>   inglés de la película de 2002, con sus tiempos**
>   ([alfredlu1986/movie-english-sub](https://github.com/alfredlu1986/movie-english-sub),
>   versión Blu-ray con descripciones de sonido, y
>   [imkira3/imkira3Keys](https://github.com/imkira3/imkira3Keys), de
>   OpenSubtitles). Comparé 17 frases clave: **el mismo minuto en los
>   dos** (seguramente salen de la misma copia Blu-ray). Con ellos
>   pongo el **minuto de cada escena**. Puede moverse unos segundos según
>   la copia.
> - También bajé de [google/fonts](https://github.com/google/fonts) las
>   letras propuestas y comprobé una a una, con fontTools, si traen
>   á é í ó ú ñ ¿ ¡.
> - **No vi ninguna imagen ni vídeo.** Lo que se ve en cada escena lo
>   cuento por lo que dicen las fuentes o de memoria, y lo marco.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto.
>   ⚠️ **dudoso**: una sola fuente, o de memoria.
> - «2002» es la película animada de Chris Sanders y Dean DeBlois.
>   «2025» es la película de imagen real de Dean Fleischer Camp.
>   El minuto va así: 00:22:54.

---

## Segunda pasada · qué cambió

Repaso del 24-25 de septiembre de 2026 con la red abierta. Sale de las
partes de los cuatro investigadores (`partes/imagen.md`, `video.md`,
`voz.md`, `texto.md`) y de `partes/datos-*.md`. Se editó cada sección
en su sitio; lo nuevo va marcado «**Nuevo, 2.ª pasada**» o «**2.ª
pasada**».

### Corregido (antes → ahora)

| Qué | Antes | Ahora | Fuente |
|---|---|---|---|
| Voz latina de Nani, 2025 | Karen Vallejo (nota de prensa) | **Alicia Vélez** | Doblaje Wiki y The Dubbing Database (§10.2) |
| Voz latina de Pleakley, 2025 | Arturo Castañeda (nota de prensa) | **Armando Guerrero** | ídem |
| Voces de 2002 de Nani, Pleakley, Cobra y David | ❌ no encontradas | **Claudia Garzón, Rubén Trujillo, Rubén Moya, Noé Velázquez Pedroza** ✅✅ | ídem (§10.1) |
| Mario Filio | «no sé a quién dobla» | **Kumu**, el profesor de hula | ídem |
| Voz de Stitch en cine, 2002 | ¿Sanders, Aldana o mezcla? | Aldana sólo en los diálogos en español; gruñidos y ruidos, Sanders | Doblaje Wiki ⚠️ |
| Intérprete de «Muero de amor por ti» | ❌ no encontrado | **Bandana** (Argentina) | ficha de Doblaje Wiki ⚠️ |
| Licencia de «Set of four low-poly Cameras» | CC Attribution | **CC BY-NC-SA** (no comercial) | API de Sketchfab (§4.1) |
| Fondos de pantalla oficiales | «no encontré ninguno» | **8 con tamaño**, el mayor de 3000×1535 | API de la wiki (§17.1) |
| Artbook | «no encontré» | *Collected Stories From the Film's Creators*, Disney Press, 2002 | Worthpoint, LabyrinthBooks (§3.6) |
| Noche del cuarto de Lilo | azul `#1F2E52` | **morada y roja**: `#432626`, `#62414D`, `#6A1B1B` | tráiler 2002, 2:12, `estilo.py` (§5.4b) |
| Luau | noche fría | **cálida de antorchas**: `#8D4232`, `#813B2D` | luau 1080p, 0:48 y 1:00 |
| Bosque del Patito Feo | luz de amanecer | **noche**, luz de luna, sin música | película, 55:27 (§2.1, §5.3) |
| Truco de la sal de Maurice Noble | ⚠️ un resumen | ✅ dos fuentes | AV Club, Animation Obsessive |
| Director del doblaje de 2002 | José Carlos Moreno ⚠️ | **en duda**: la ficha dice Ricardo Tejedo; Moreno sale de actor | Doblaje Wiki (§10.1) ⚠️ |
| Datos de la parte de imagen | — | ruta de la hoja de Pleakley (`/7/74/` → `/7/7b/`), Britto (n.º 4 → 12), Disney Cruise Line (n.º 554 → 559); **retirado** «KH III con Stitch's Great Escape» (el n.º 535 es una foto del parque) | el redactor, mirando las hojas y con `curl` |

### Añadido

- **Hojas de contacto** (3, miradas y con cada número explicado).
- **Vídeos mirados de verdad**: película entera, tráiler 2002, créditos,
  luau 1080p, tráiler latino 2025, *featurette* musical (§2.4, §12.1).
- **Caras por emoción con fotograma**, 14 de 25 (§8.2); **18 poses
  vistas** con minuto (§15.1); **paleta medida** (§5.4b) y **vestuario
  medido** (§16.1).
- **Bocadillo real** del cómic Dynamite (§7.6); **9 letras por uso**
  comprobadas con fontTools (§6.3).
- **Créditos musicales** leídos en pantalla (§11.1); **lista completa de
  videojuegos** (§13.1); **reparto latino completo** de 2002 y 2025.
- **Guía de IA** puesta al día y **guía de IA de texto** (§18.7, §18.8).
- **Puntos 18 a 25**, que no existían: técnica y cómo replicarla,
  texturas 2D, gustos, por qué la aman, fandubs, colaboraciones, obras
  parecidas y el mundo.
- **Tabla de cumplimiento** y bitácora de la 2.ª pasada (21.6).
- `referencias.json`: de 35 a **193** (todas las útiles de las partes y
  de `datos.json`, sin repetidas, las mejores primero; 114 con tamaño
  medido).

### Los ⚠️

- Antes: **97** ⚠️. Ahora: **206**. Hay más porque se marcó cada dato
  nuevo con una sola fuente y cada casilla vacía de caras por emoción.
  De los 97 viejos, **30 se reescribieron** (casi todos resueltos: voces
  de 2002, estudio, voces de 2025, licencias, fondos, artbook, luz,
  orejas de Stitch, la sal) y 67 siguen en el texto de la 1.ª pasada;
  varios de ésos quedan contestados en las secciones nuevas (§15.1 para
  las poses, §16.1 para el vestuario, §5.4b para la paleta).
- **Quedan** (lo importante): la frase latina de la cámara, el director
  del doblaje de 2002, 11 caras por emoción, la marca de la cámara y el
  «TIMER DINGS», hex planos de Stitch, Jumba, Cobra y David, vídeos de
  YouTube y TikTok sin mirar. Lista entera en §20 y en la tabla de
  cumplimiento.
- **Conceptos de lámina**: los tres siguen; ganan referencias vistas. B
  gana el *collage* de los créditos con Stitch colado, que es la mejor
  imagen para #fotos (§19).

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, categoría ✦ EL TALLER ✦):

> **ıı・📸・fotos** (foro) · 1 hilos · etiquetas: Paisaje, Retrato,
> Naturaleza, Ciudad, Nocturna, Analógica, Con el móvil, Con cámara,
> Editada, Sin editar, Detrás de cámara — _Fotos que hagáis vosotros: lo
> que veis, dónde grabáis, cómo os montáis el rincón. Un hilo por foto o
> por serie._
> - 📌 **De qué va esto** (0 msj) · adj: `fotos.png` ← aquí va la lámina.

Función según el encargo: **foro de fotografía** (paisaje, retrato, con
el móvil, con cámara…). Objeto que propone el plan: **el álbum de fotos
de Lilo**.

**Por qué Lilo & Stitch encaja tan bien:** Lilo es **la fotógrafa de la
película**. Tiene una cámara de carrete y una pared de su cuarto
**tapizada de fotos de turistas**. Su frase de fotógrafa es la escena
«Oh! My camera's full again.» → «Aren't they beautiful?» (00:22:54 y
00:22:57) ✅ (los dos subtítulos). Y la película **termina con un montaje
de fotografías** de la familia nueva, con «Burning Love» (01:17:18) ✅.
Hay, además, una foto clave: **la de sus padres**, que Lilo le enseña a
Stitch (00:53:49) ✅. Y la foto final junta a Stitch con esa familia ✅
(ver §2).

> [!warning] «Vosotros» en un servidor latino
> El texto del canal usa formas de España (hagáis, veis, grabáis,
> montáis). El resto del servidor es latino (Perú, México…), y el
> doblaje que se cita es el latino. En la lámina propongo **«ustedes»**.
> Si el dueño prefiere su frase tal cual, se cambia sin problema.

### Los textos de la lámina 1 (qué es el canal)

Una idea cada uno, sin «·», «—» ni paréntesis:

| # | Texto | Idea |
|---|---|---|
| 1 | **Fotos** | nombre del canal |
| 2 | **Fotos que hagan ustedes** | qué va |
| 3 | **Lo que ven** | tema 1 |
| 4 | **Dónde graban** | tema 2 |
| 5 | **Cómo se montan su rincón** | tema 3 |
| 6 | **Un hilo por foto** | regla 1 |
| 7 | **O uno por serie** | regla 2 |
| 8 | **Ponle su etiqueta** | remite a la lámina 2 |
| 9 | **¡Mi cámara está llena otra vez!** | gancho, en voz de Lilo |

- El 9 es una **adaptación** de la línea de 00:22:54. **No encontré la
  frase exacta del doblaje latino** ⚠️. Hay que oírla en la película
  (Disney+) antes de rotularla como cita. **2.ª pasada**: la parte de voz
  tampoco la encontró (sus 2 tandas se agotaron; queda ⚠️ en la tabla de
  cumplimiento).
- Alternativa de gancho, con frase latina sí documentada: «**Ohana
  significa familia**» (§10). Pero es la frase más gastada de la
  franquicia. Para un canal de fotos, la de la cámara es más propia.

### Los textos de la lámina 2 (las 11 etiquetas)

Las 11 etiquetas **no caben bien** en la lámina 1 si cada una lleva su
ejemplo. Propongo **lámina 2**: cada etiqueta es **una foto** del álbum
(o de la pared de Lilo), con su nombre escrito a mano en el borde
blanco. Agrupadas en cuatro páginas o cuatro filas:

| Grupo | Etiquetas | Foto de ejemplo, sacada de la película |
|---|---|---|
| **Qué sale** | Paisaje · Retrato · Naturaleza · Ciudad · Nocturna | Paisaje: acantilados de Kauai. Retrato: un turista de la pared de Lilo (00:22:57). Naturaleza: el bosque donde Stitch se pierde (00:55:31). Ciudad: la calle del pueblo, inspirada en Hanapepe. Nocturna: la estrella fugaz (00:23:10). |
| **Con qué** | Analógica · Con el móvil · Con cámara | Analógica: la cámara de carrete de Lilo. Con cámara: la misma, vista de frente. Con el móvil: la videollamada del final de 2025 ⚠️. |
| **Cómo quedó** | Editada · Sin editar | La misma foto dos veces: una con colores de acuarela, otra tal cual. |
| **Detrás de cámara** | Detrás de cámara | Una foto del montaje final: la familia arreglando la casa (01:17:18 en adelante) ⚠️ lo que se ve. **2.ª pasada, visto**: la foto de familia de los créditos con **Stitch sentado fuera del marco**, colado en la esquina ([créditos, 1:20](https://archive.org/details/lilo-stitch-3?t=80)) ✅. Es el «detrás de cámara» perfecto. |

- En la tabla de arriba el «·» separa etiquetas; **en la lámina no se
  usa**: cada etiqueta va en su foto.
- Un texto corto por grupo, en voz de Lilo (lista numerada, ver §7):
  «**Número uno: qué sale.**» «**Número dos: con qué.**» «**Número
  tres: cómo quedó.**» «**Y detrás de cámara.**»

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué encaja | Lilo **hace fotos**: tiene cámara de carrete y una pared con más de cien fotos de turistas ✅. La película **acaba con fotos** de la familia ✅. |
| Escena clave | 00:22:54 «My camera's full again» → 00:22:57 «Aren't they beautiful?», en el cuarto de Lilo, con Nani ✅ (subtítulos). |
| Cuadro de diálogo propio | **No hay globos** en la película (salvo el del libro del Patito Feo). Si hace falta globo, el del **cómic oficial de Dynamite**: óvalo blanco, borde negro grueso, Comic Neue Bold en mayúsculas, palabra clave en cursiva (§7.6). El texto vive en **objetos**: la foto con su borde blanco, **la lista de Lilo** («número uno es el baile», 00:42:36), el libro del **Patito Feo** (00:40:27), el **papel de adopción con su sello** (01:15:48) ✅. Para la lámina: **pie de foto escrito a mano** en el borde blanco, con cinta de carrocero. |
| Objeto para la lámina | **La pared de fotos del cuarto de Lilo** o **el álbum de la familia** del final. Los dos se hacen en Blender: tablero o pared, fotos con borde, chinchetas, cinta, cámara. |
| El más querido | **Stitch**, de lejos: más de **4.000 millones de dólares** en ventas de productos en el año fiscal 2025 ✅. Pero **la que fotografía es Lilo**. Solución: **Lilo dispara, Stitch posa**. |
| Voces latinas | 2002: Lilo **Anaís Portillo** ✅, Stitch **Raúl Aldana** ✅ (sólo los diálogos; los ruidos son de Sanders), Nani **Claudia Garzón** ✅, Jumba **Maynardo Zavala** ✅, Pleakley **Rubén Trujillo** ✅ (§10). 2025: Stitch **Gerardo Becker** ✅, Nani **Alicia Vélez** ✅ (corregido: no Karen Vallejo), Jumba **Sergio Gutiérrez Coto** ✅, Pleakley **Armando Guerrero** ✅ (corregido: no Arturo Castañeda). |
| Estilo | Formas **redondas y pesadas abajo**, «como un saco de harina» ✅ (IndieWire). Fondos **en acuarela** de verdad, lo primero así en Disney en unos 60 años ✅. |
| Letras | Títulos: **Lilita One**, **Chewy** o **Kavoon**. Pies de foto a mano: **Gochi Hand**, **Reenie Beanie** o **Covered By Your Grace**. Todas traen á é í ó ú ñ ¿ ¡ (comprobado con fontTools). |
| Tono | Tierno, raro y cálido. Hawái de verdad, no de postal. Nada de neón ni de tiki de souvenir. |
| La mejor referencia nueva (2.ª pasada) | **Los créditos son un álbum**: fotos de borde blanco pegadas con cinta sobre azul, y **Stitch sentado fuera del marco** de una foto de familia ([1:20](https://archive.org/details/lilo-stitch-3?t=80)) ✅ visto. |

---

## 2 · Las escenas que sirven para #fotos (con minuto)

Minutos de los subtítulos en inglés de la película de 2002
([Blu-ray, alfredlu1986](https://github.com/alfredlu1986/movie-english-sub/blob/main/2002/Lilo.and.Stitch.2002.1080p.720p.BluRay.x264.%5BYTS.MX%5D-English.srt)
y [OpenSubtitles, imkira3](https://github.com/imkira3/imkira3Keys/blob/main/Subtitles/Lilo%20%26%20Stitch.srt)).
El texto y el minuto están comprobados ✅. Lo que **se ve** lo cuento
por las fuentes o de memoria ⚠️: mira el fotograma antes de usarlo.

### 2.1 Lilo, fotógrafa

| Minuto | Qué pasa (subtítulo inglés) | Para qué sirve |
|---|---|---|
| 00:22:54 | Lilo: «Oh! My camera's full again.» | **La escena del canal.** Cámara llena = hay que subir fotos. |
| 00:22:57 | Lilo, susurrando: «Aren't they beautiful?» Le enseña a Nani **la pared de fotos de turistas** | La pared: más de cien fotos que casi tapan la pared ✅ ([filmboards](https://filmboards.com/board/t/Lilos-obsession-with-fat-people-1118389/), resumen de la [lista de personajes de Wikipedia](https://en.wikipedia.org/wiki/List_of_Lilo_%26_Stitch_characters)). Nani pone cara de susto ⚠️. |
| 00:23:10 | Lilo: «A falling star!» | Foto **Nocturna**: la «estrella» es la nave de Stitch. |
| 00:23:42 | Lilo pide un deseo en la ventana: «I need someone to be my friend… Maybe send me an angel» | Pose de pensar, de noche. |
| 00:53:49 | Lilo: «That's us before…» Le enseña a Stitch **la foto de sus padres**. 00:53:52: «It was rainy, and they went for a drive.» | **La foto como recuerdo.** Tono serio: sirve para «Sin editar». |
| 00:54:57 | Lilo: «I remember everyone that leaves.» | Por qué se hacen fotos. |
| 01:17:18 → 01:20:13 | Montaje final con «Burning Love». Fotos de la familia nueva | **El álbum.** La última foto junta a Stitch con Lilo, Nani y sus padres: otra foto tapa en parte a la vieja para meter a Stitch ✅ ([TV Tropes, momentos tiernos](https://tvtropes.org/pmwiki/pmwiki.php/Heartwarming/LiloAndStitch2002), [DeviantArt, comparación de la foto](https://www.deviantart.com/danielnewton/journal/Lilo-s-Family-Photo-Comparison-872752082)). |
| 01:17:56 | «(TIMER DINGS)» en el subtítulo | ⚠️ No sé si es el temporizador de una cámara o el de la cocina. Si es la cámara, es la **foto de grupo con temporizador**. Mirar. |
| Créditos | Las «fotos instantáneas» de los créditos | Hay una serie de **pins oficiales** que las copian ✅ ([Pin & Pop](https://pinandpop.com/series/lilo-stitch-end-credits-snapshot-photos)). |

- **La cámara**: se describe como **una cámara de carrete Kodak** ⚠️
  (resumen de la [lista de Wikipedia](https://en.wikipedia.org/wiki/List_of_Lilo_%26_Stitch_characters)).
  Un foro dice «polaroids» ⚠️ ([filmboards](https://www.filmboards.com/board/p/1118389/)).
  Las dos cosas no pueden ser a la vez: **mirar el fotograma de
  00:22:54**. Para la lámina, **no poner marca** en la cámara.
- **Escena eliminada**: Lilo **asusta a todos los turistas de la
  playa** ✅ ([Cinemablend](https://www.cinemablend.com/new/Lilo-Stitch-Terrorize-Tourists-Deleted-Scene-33401.html),
  [TikTok de @decineyseries](https://www.tiktok.com/@decineyseries/video/7465966539066412293)).
  El TikTok la lee como una respuesta a turistas que la tratan como
  una rareza ⚠️ (interpretación).

### 2.2 Lilo, profesora: la lista (el mejor «cuadro de diálogo»)

| Minuto | Qué pasa | Para qué sirve |
|---|---|---|
| 00:42:30 | Lilo: «Elvis Presley was a model citizen.» | Arranque de la lección |
| 00:42:33 | «I've compiled a list of his traits for you to practice.» | **La lista escrita de Lilo** |
| 00:42:36 | «Number one is dancing.» 00:42:44: «Hands on your hips.» | **Número uno…**: formato de los pasos de la lámina |
| 00:43:12 | «Elvis played guitar. Here.» 00:43:15: «Hold it like this, and put your fingers here.» | Explicar con las manos |
| 00:43:40 | Stitch toca el ukelele «expertly» | Celebrar |
| 00:44:24 | «It's all you! Knock 'em dead!» Stitch actúa de Elvis ante turistas | Animar |
| 00:44:49 | «Don't crowd him!» Stitch se agobia y todo acaba mal | ⚠️ De memoria: **los turistas le hacen fotos con flash**. Si se confirma, es un chiste perfecto para «Detrás de cámara». |

En latino circula: «Elvis Presley era un buen ciudadano. Recopilé estos
ejemplos para que practiques, el número uno es el baile» ⚠️ (resumen de
buscador sobre listas de frases; no oído).

### 2.3 Otras escenas que dan fotos de ejemplo

| Minuto | Qué pasa | Etiqueta |
|---|---|---|
| 00:07:23 | Pleakley, «experto en la Tierra»: «Earth is a protected wildlife reserve» | Naturaleza (con humor) |
| 00:10:22 | Clase de hula: canción «He Mele No Lilo» | Retrato de grupo |
| 00:14:25 | Lilo en el porche: «This is Scrump.» | Retrato |
| 00:38:44 | Pleakley, con peluca, en la playa: «Don't move. A mosquito has chosen me as her perch.» 00:38:48: «She's so beautiful.» | Naturaleza (macro) |
| 00:40:27 | Lilo le lee a Stitch **El Patito Feo** | Nocturna, interior |
| 00:46:05 | Surf con David: «Hawaiian Roller Coaster Ride» | **Paisaje**, acción |
| 00:52:51 | Nani canta «Aloha ʻOe» a Lilo | Retrato íntimo |
| 00:55:31 | Stitch, solo en el bosque con el libro: «Lost.» 00:55:41: «I'm lost.» | Naturaleza, **de noche**: luz azul de luna y sin música (2.ª pasada, visto en [55:27](https://archive.org/details/lilo-stitch-2002_202609?t=3327); antes decía «luz de amanecer», de memoria) ✅ |
| 01:15:00 | Stitch: «This is my family. I found it all on my own. It's little and broken… But still good.» | Foto de familia |
| 01:15:48 | Lilo: «I paid two dollars for him. See this stamp? I own him.» | El papel con sello: otro texto-objeto |

### 2.4 Lo que se vio en vídeo (Nuevo, 2.ª pasada)

Mirado con `fotogramas.py` en Internet Archive y Dailymotion (YouTube
pedía iniciar sesión). Los minutos son **de cada vídeo**, con enlace.

| Vídeo y minuto | Qué se ve | Para #fotos |
|---|---|---|
| Película 2002, [22:10](https://archive.org/details/lilo-stitch-2002_202609?t=1330) | Lilo sentada en la cama, abrazada a su peluche verde, mirando **la pared de fotos de turistas**, mirada baja ✅ | La pared de fotos, vista por fin. Tono triste |
| Película 2002, [20:50](https://archive.org/details/lilo-stitch-2002_202609?t=1250) → 23:15 | Nani la arrastra a casa, bronca, Lilo llora sola con el peluche (21:30-22:15), Nani entra y se duermen abrazadas (22:20-22:55) ✅ | «Regañar → hacer las paces», para lámina en pareja |
| Película 2002, [31:44](https://archive.org/details/lilo-stitch-2002_202609?t=1904) | Lilo y Stitch a carcajadas en el cohete de monedas «Space Adventure», frente a una tienda ✅ | Alegría; foto de pueblo |
| Película 2002, [38:00](https://archive.org/details/lilo-stitch-2002_202609?t=2280) | Stitch construye a oscuras una maqueta de ciudad (puente, edificios, barco); Lilo lo mira desde la cama ✅ | «Cómo os montáis el rincón» |
| Créditos 2002, [1:20](https://archive.org/details/lilo-stitch-3?t=80) | **Foto de familia pegada con cinta** sobre fondo azul (madre, padre con bigote y gafas de sol, dos chicas, bebé con ukelele) y **Stitch sentado fuera del marco blanco**, abajo a la derecha, colado ✅ | El gag «Stitch se cuela en la foto» dentro de la película |
| Créditos 2002, [0:00](https://archive.org/details/lilo-stitch-3?t=0) · 0:10 · 0:20 · 1:20 | **Los créditos son un álbum**: fotos con borde blanco, pegadas en ángulo con cinta sobre azul liso, unas tapando a otras ✅ | Es el fondo de la lámina, hecho por Disney |
| Tráiler 2002, [1:48](https://archive.org/details/LiloStitchTrailer?t=108) | La **cápsula azul con correas** de Stitch lleva dentro **una fotito de Lilo** (vestido rosa) pegada junto a un garabato de tela de araña ✅ | Otro objeto-foto, más pequeño que el álbum |
| Tráiler 2002, [2:12](https://archive.org/details/LiloStitchTrailer?t=132) | Nani entra en el cuarto de noche, boca abierta, un brazo hacia Stitch, junto a Lilo dormida. Lámpara **verde con base de piña** ✅ | Susto; attrezzo nuevo |

- **Sigue sin resolver** ⚠️: la marca de la cámara (Kodak de carrete o
  polaroid). Ningún vídeo disponible llegaba a 00:22:54 con imagen
  clara (el «Part 1 HD» de Internet Archive sólo llega a 7:59 y está
  degradado). Para la lámina: **cámara sin marca**.
- **Sigue sin resolver** ⚠️: el «TIMER DINGS» de 01:17:56. El clip de
  créditos empieza ya con el *collage* avanzado; no se sabe si son las
  mismas fotos del montaje 01:17:18-01:20:13.
- **No encontrado en vídeo** ⚠️: la lección de Elvis (00:42-00:44) y si
  los turistas le hacen fotos con flash a Stitch.

---

## 3 · Arte oficial y referencias visuales

Primera pasada: **no se pudo bajar ni ver ninguna imagen** (red
cerrada). La 2.ª pasada **sí las vio** (§3.6 y «Las hojas de contacto»).

### 3.1 La campaña de 2002: los «Inter-Stitch-als»

- Cuatro tráileres de 2001-2002 en los que **Stitch se cuela en escenas
  famosas de Disney**: La Sirenita, La Bella y la Bestia, Aladdín y El
  Rey León ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Advertising/InterStitchals),
  [YouTube, los cuatro](https://www.youtube.com/watch?v=Oh5SvyCX9QE)).
- Idea de Sanders: «¿y si Stitch invadiera otras películas de Disney?».
  Suena «Back in Black» de AC/DC ✅ (TV Tropes).
- En el de Aladdín, Stitch pone **«Hound Dog»** en la radio: primer
  aviso de que Elvis iba a importar ✅ (TV Tropes).
- En el de La Bella y la Bestia, Stitch mira desde la lámpara del salón
  hasta que la tira ✅ ([4K en YouTube](https://www.youtube.com/watch?v=0EPdOPhwpUA)).
- **Para #fotos**: es la idea de «**colarse en la foto**» (photobomb).
  Sirve para «Detrás de cámara».

### 3.2 Arte de producción

- **Guía de estilo «Surfing the Sanders Style»**, de **Sue Nichols**,
  supervisora de desarrollo visual ✅
  ([Scribd](https://www.scribd.com/document/552265347/Lilo-Stitch-Style-Guide-by-Sue-Nichols-Maciorowski),
  [Tumblr @disneyconceptsandstuff](https://www.tumblr.com/disneyconceptsandstuff/86440010066/read-more-of-sanders-style-surfing-made-for-the),
  [Tumblr @animatorial](https://www.tumblr.com/animatorial/161908140873/the-disney-elite-chris-sanders-style-surfing)).
  Sus reglas, en §18.
- **Hojas de modelo** ([After Hours Animation School](https://afterhoursanimationschool.tumblr.com/post/142262804364/lilo-and-stitch-model-sheets-part-2)) ✅ enlace.
- **Arte de concepto de Chris Sanders**
  ([Tumblr @thedisnerd](https://www.tumblr.com/thedisnerd/11542577166/lilo-and-stitch-2002-concept-art-by-chris),
  [Best of Disney Art](https://www.facebook.com/BestofDisneyArt/posts/concept-art-for-lilo-stitch-by-director-chris-sanders-/1081766257406143/),
  [Character Design References: «Art of Lilo & Stitch»](https://characterdesignreferences.com/art-of-animation-5/art-of-lilo-stitch)).
- **El primer diseño de Stitch**, con arte exclusivo de Sanders
  ([Gold Derby, 2025](https://www.goldderby.com/film/2025/lilo-stitch-story-behind-animated-movie-original-designs-chris-sanders/)).
  Sanders creó a Stitch **en 1985 para un libro infantil que no salió**
  ✅ (resumen de Wikipedia y de la [FAQ de Sanders](https://www.chrissandersart.com/pages/faq)).
- Web del propio Sanders: [chrissandersart.com](https://www.chrissandersart.com/).
- Pins de la Comic-Con 2019 con su arte de concepto
  ([PinTradingDB](https://www.pintradingdb.com/pin/32200)).

### 3.3 Fotos de la película convertidas en objeto

- **Pins «End Credits Snapshot Photos»**: las fotos de los créditos,
  hechas pin ✅ ([Pin & Pop](https://pinandpop.com/series/lilo-stitch-end-credits-snapshot-photos)).
  **Es la mejor referencia** de cómo son esas fotos (borde, encuadre).
- Productos con cámara: una **cámara desechable oficial** con Stitch
  ([Amazon](https://www.amazon.com/Disney-Stitch-Disposable-Camera-Flash/dp/B0DRZ2VBFT)).
  Sólo muestra que la idea «Stitch + cámara» ya existe en tienda.

### 3.4 Cómics y la película de 2025

- **Cómic de Dynamite (2024)**: 8 números, guion de **Greg Pak** y
  dibujo de **Giulia Giacomino** ✅
  ([Bleeding Cool](https://bleedingcool.com/comics/lilo-stitch-gets-a-new-comic-by-greg-pak-giulia-giacomino-in-2024/),
  [wiki de Lilo & Stitch](https://liloandstitch.fandom.com/wiki/Lilo_%26_Stitch_(Dynamite_Comics))).
  Portadas de **Nicoletta Baldari, Trish Forstner, Edwin Galmon, Craig
  Rousseau**, David Nakayama, Joshua Middleton y Jennifer L. Meyer ✅
  ([AIPT, n.º 2](https://aiptcomics.com/2024/02/23/dynamite-preview-lilo-stitch-2/)).
  **Las portadas son las poses más variadas** que hay: buscarlas.
- **2025**: [web oficial de Disney](https://movies.disney.com/lilo-and-stitch-2025),
  [ficha de Disney+ (HK)](https://www.disneyplus.com/zh-hk/browse/entity-3edb5cb2-fba6-4473-bfa2-8a867e00bdeb).
- **Japón**: [página oficial de personajes, Disney Japón](https://www.disney.co.jp/fc/stitch).

### 3.5 Lo que faltaba en la primera pasada

- ~~No vi pósteres ni carátulas~~ → 2.ª pasada: pósteres vistos en la
  hoja 1 (n.º 18 «There's one in every family», n.º 19 Lilo, Nani y
  Stitch surfeando). Carátulas de Blu-ray: siguen sin mirar ⚠️.
- ~~No encontré fondos de pantalla oficiales~~ → **7 oficiales con
  tamaño medido** (§17).
- ~~No encontré artbook~~ → **sí existe** (§3.6).

### 3.6 Arte oficial visto de verdad (Nuevo, 2.ª pasada)

Tamaños medidos con la API `imageinfo` de la wiki de Disney. Las
imágenes de `static.wikia.nocookie.net` piden la cabecera
`Referer: https://www.fandom.com/`.

- **Artbook oficial**: *Lilo & Stitch: Collected Stories From the
  Film's Creators*, Disney Press, 2002, 128 páginas, con el equipo
  contando su proceso ✅ ([Worthpoint, ficha con ISBN](https://www.worthpoint.com/worthopedia/lilo-stitch-collected-stories-films-1886596031),
  [LabyrinthBooks](https://labyrinthbooks.myshopify.com/products/chris-sanders-lilo-stitch-collected-stories-disney-art-book)).
  No es «Disney Editions» ni se llama «The Art of…».
- **Key visual** «Lilo & Stitch promo art 2.jpg», **3523×5000**, la
  imagen oficial más grande de la wiki: Lilo y Stitch en la playa al
  atardecer, ella con traje de hula ✅
  ([imagen](https://static.wikia.nocookie.net/disney/images/1/1b/Lilo_%26_Stitch_promo_art_2.jpg); hoja 1, n.º 2).
  Sirve de referencia de luz y color (hex en §16).
- **Hoja de modelo de Pleakley** firmada por Chris Sanders («Lilo and
  Stitch Rough Model Sheet»), frente, perfil y expresiones, **2048×1319**
  ✅ ([imagen](https://static.wikia.nocookie.net/disney/images/7/7b/Pleakley_concept_art.jpg); hoja 2, n.º 63).
  Corrección: la parte de imagen daba la ruta `/7/74/`, que da 404; la
  buena es `/7/7b/`.
- **Poses de hula de Lilo** en una sola hoja, «LiloHulaAD.jpg»,
  **1600×1068**, y **estudio de Lilo**, «LiloStudyAD.jpg», **1600×1058**
  ✅ ([hula](https://static.wikia.nocookie.net/disney/images/9/93/LiloHulaAD.jpg),
  [estudio](https://static.wikia.nocookie.net/disney/images/0/09/LiloStudyAD.jpg)).
  Poses vivas, justo lo que pide el dueño.
- **Arte de desarrollo de Stitch**, **3338×2160** ✅
  ([imagen](https://static.wikia.nocookie.net/disney/images/5/56/Stitch_Development_art.png); hoja 1, n.º 16).
- **Stitch sentado con Scrump, el sándwich y Pato el pez**, firmado por
  Chris Sanders, **1646×1646** (hoja 2, n.º 62, «Daveigh Chase
  posthumo») ✅ visto.
- **Portadas de Dynamite**: más de 15 distintas vistas en las hojas 1 y
  2 (n.º 7, 17, 56-59, 64-69, 78-80). La n.º 17 lleva a Stitch **de
  traje negro y gafas, de agente secreto**; la n.º 59 a Lilo con su
  vestido rojo sobre fondo rojo; la n.º 7 a Stitch surfeando ✅ visto.
- **Revistas Disney Adventures** con Stitch en portada: 9 números (hoja
  1, n.º 39-47) ✅ visto. Arte de época que no estaba.
- **Libros «Agent Stitch»** (hoja 1, n.º 26, 28, 35, 36) y **«Stitch Day
  Crashes Disney»** (hoja 2, n.º 49-51: Stitch en portadas de Big Hero
  6, El Rey León y Winnie the Pooh) ✅ visto.
- **Figuras oficiales** (pose = referencia 3D): Britto pop-art (hoja 1,
  n.º 12), Jim Shore «'Ohana» tallada estilo folk (hoja 2, n.º 74),
  peluche de Lilo de Disney Animators' Collection (hoja 1, n.º 37),
  playsets (hoja 1, n.º 13-14) ✅ visto. Más en «Punto 23».
- **Fotogramas limpios**: «Nani, Lilo, and Stitch enjoying a big wave»,
  **3000×1782** ([imagen](https://static.wikia.nocookie.net/disney/images/a/a0/Lilo_%26_Stitch_-_Nani%2C_Lilo%2C_and_Stitch_enjoying_a_big_wave.jpg); hoja 1, n.º 20) ✅.
- **Lilo abrazando a Scrump**, **1806×1080** ✅
  ([imagen](https://static.wikia.nocookie.net/disney/images/9/9d/Lilo_%26_Stitch_-_Lilo_holding_Scrump.png/revision/latest?cb=20230820215155)).
- **Logo oficial**, 800×310 ✅ ([imagen](https://static.wikia.nocookie.net/disney/images/9/9d/Lilo_%26_Stitch_Logo.png/revision/latest?cb=20160630120430)); ver §6.

---

## 4 · Fan art y 3D (sólo como referencia)

> [!note] Licencias
> Primera pasada: Sketchfab y Poly Haven **no abrían**. **2.ª pasada**:
> las licencias marcadas «API» se leyeron en la API de Sketchfab
> (`license.label`) y son seguras; las demás siguen «según buscador» ⚠️.
> Copia el crédito exacto: «<Modelo> by <autor>, CC BY 4.0, Sketchfab».

### 4.1 Objetos para la lámina (Sketchfab)

| Modelo | Autor | Licencia (según buscador) | Para qué |
|---|---|---|---|
| [Canon AE-1 Program 35mm Film Camera](https://sketchfab.com/3d-models/canon-ae-1-program-35mm-film-camera-03b0ac7d99c44197a09640179f360f3c) | Marc Sawyer (@whitewashstudio) | **CC Attribution 4.0 ✅ API**; fotogrametría, 77 532 caras | Cámara de carrete. **Quitar la marca.** Es réflex; la de Lilo parece compacta ⚠️ |
| [Set of four low-poly Cameras](https://sketchfab.com/3d-models/set-of-four-4-low-poly-cameras-275be0c563754a038c0a50f19785a8ea) | JeffK (@jeffkolada) | **Corregido: CC BY-NC-SA ✅ API** (antes decía CC Attribution). No comercial: sólo para mirar volúmenes, o preguntar al dueño | Cámaras sencillas, más «de dibujo» |
| [Low Poly Camera](https://sketchfab.com/3d-models/low-poly-camera-a8a59f14d82043698945590bc6779c50) | Maurice Svay | gratis, licencia sin ver ⚠️ | Alternativa |
| [35mm Film Roll](https://sketchfab.com/3d-models/35mm-film-roll-6d8a6d290de043e898420a04072a3a1e) | Alligator Alex | gratis, licencia sin ver ⚠️ | Carrete suelto junto al álbum |
| [Photo Album](https://sketchfab.com/3d-models/photo-album-b891198a35a64b2c9c3c1a26338b1a48) | mnaglak | **CC Attribution 4.0 ✅ API** | **El álbum** |
| [Cork Board](https://sketchfab.com/3d-models/cork-board-9534ee2ad4344ea6b02b95b61bd4a913) | rickmaolly | **CC Attribution ✅ API** | Tablero con papeles clavados |
| [Corkboard](https://sketchfab.com/3d-models/corkboard-1e5469eaf8b54337aacfc42a713b3a98) | Sousinho | gratis ⚠️ | Chinchetas que se mueven |
| [Corkboard](https://sketchfab.com/3d-models/corkboard-3ceda8ed02af45d1a8b36570076193e1) | K.Shitanaga | gratis ⚠️ | Otro tablero |

### 4.2 Personajes en 3D de fans (sólo para mirar poses)

Los personajes son de Disney: **no se pegan**, sirven para girar la
pose y ver volúmenes.

- [Stitch (626) rigged](https://sketchfab.com/3d-models/stitch-626-from-lilo-and-stitch-rigged-5ae4cd66c67d42c49202f2003fe7f559), Werasik2aa.
- [Stitch en su forma «de perro»](https://sketchfab.com/3d-models/stitch-7a72d3375a284824a15201d774de4e95),
  BOSSNINO: brazos de abajo, antenas y púas escondidos ✅ (descripción).
- [Lilo](https://sketchfab.com/3d-models/lilo-from-lilo-stitch-0eb59f0dfd354ec685d431284a8859ec), Ibokk ·
  [Lilo](https://sketchfab.com/3d-models/lilo-from-lilo-and-stitch-0cc80d7ff2cf494b9a9774da455c87ab), Werasik2aa.
- [Angel (624)](https://sketchfab.com/3d-models/experiment-624-angel-from-lilo-and-stitch-71ede4ebbbfb47ef9a1241170830df32) y
  [cápsula de experimento](https://sketchfab.com/3d-models/experiment-pod-container-from-lilo-and-stitch-6e0aa3df6154430082d27a98ff09e417), Werasik2aa.

**Nuevo (2.ª pasada)**: modelos con *rig* y licencia **CC Attribution
leída en la API** (la parte de texto miró sus miniaturas, 1920×1080):

| Modelo | Autor | Caras | Nota |
|---|---|---|---|
| [Stitch (626) Rigged](https://sketchfab.com/3d-models/stitch-626-from-lilo-and-stitch-rigged-5ae4cd66c67d42c49202f2003fe7f559) | werasik2aa1 | 35 464 | el mejor para posar a Stitch ✅ |
| [Stitch (KH3) Rig](https://sketchfab.com/3d-models/stitch-kh3-rig-d1c674e7c0424687935d1839a2a55843) | guinavarro.al | 34 782 | estilo Kingdom Hearts III ✅ |
| [Pleakley](https://sketchfab.com/3d-models/pleakley-lilo-stitch-3a4305debb52451a8ba5ccb8a174e7ef) | ArbitraryCanary | 260 220 | **muy pesado**: regla 9 del dueño, no saturar el PC ✅ |
| [Nani](https://sketchfab.com/3d-models/nani-from-lilo-and-stitch-8ed9ce5f0f944c7182fc150cf9d4c10b) | werasik2aa1 | 2 758 | ligero ✅ |

Más modelos de fans con **CC Attribution** según la API de Sketchfab
(los juntó `recolectar.py`, en `partes/datos.json`; sin mirar uno a uno
⚠️): [Space Adventure](https://sketchfab.com/3d-models/none-9cf9da6809894cae9377ae94b1d4256b)
de Fanny Ngo (el **cohete de monedas** de la película, visto en
[31:44](https://archive.org/details/lilo-stitch-2002_202609?t=1904)),
[Smug Lilo](https://sketchfab.com/3d-models/none-8886725fc8c543c5ad0872a0301cfbc9)
y [Lilo and Stitch's shenanigans](https://sketchfab.com/3d-models/none-09964de38fc04df19fb0753b35d03d55)
de Fanny Ngo, [Stitch (Fan Art)](https://sketchfab.com/3d-models/none-65880617586342db903f9236c014aeab)
y [Yuna (Fan Art)](https://sketchfab.com/3d-models/none-024b3f1d804b4dea9da4534ed0add0f4) de Bema,
[Stitch](https://sketchfab.com/3d-models/none-5a85d135283e4356a86bccd7a7ca6938) de procyonlotor y
[Nani Peleaki](https://sketchfab.com/3d-models/none-2d4b1ccf80cd4be480bb4cc5a46e1b84) de roachfilmopticals.

- **No hay rig libre de Lilo ni de Jumba** con CC descargable ⚠️ (parte
  de texto; los de Lilo de arriba no tienen licencia vista).

### 4.3 Fan art 2D (mirar, nunca pegar)

- [ArtStation, Ego: Lilo & Stitch Fan Art](https://www.artstation.com/artwork/3D5eA).
- [DeviantArt, p-yeah: Stitch](https://www.deviantart.com/p-yeah/art/Stitch-Fan-Art-Lilo-Stitch-713227266).
- [DeviantArt, aliciamartin851: fotos del final](https://www.deviantart.com/aliciamartin851/art/Lilo-and-stitch-ending-pics-960086384).
- [DeviantArt, danielnewton: la foto de familia comparada](https://www.deviantart.com/danielnewton/journal/Lilo-s-Family-Photo-Comparison-872752082).
- No encontré fan art concreto de **Lilo con la cámara** ⚠️. La 2.ª
  pasada lo buscó otra vez en ArtStation y DeviantArt (inglés): el fan
  art se centra en Stitch solo o en el abrazo final; la cámara casi
  nunca sale.
- **Fondos de fans en alta** (Wallhaven, con autor y tamaño): ver §17.

### 4.4 Luz y texturas libres (Poly Haven, CC0)

- HDRI de playa: [Secluded Beach](https://polyhaven.com/a/secluded_beach),
  [Ingwe Beach Sunny](https://polyhaven.com/a/ingwe_beach_sunny),
  [Fish Hoek Beach](https://polyhaven.com/a/fish_hoek_beach),
  [Beach Parking](https://polyhaven.com/a/beach_parking).
- Madera pintada, como la casa de Lilo:
  [Distressed Painted Planks](https://polyhaven.com/a/distressed_painted_planks) (pintura verde pálida saltada),
  [Wood Peeling Paint Weathered](https://polyhaven.com/a/wood_peeling_paint_weathered),
  [Worn Planks](https://polyhaven.com/a/worn_planks),
  [Wooden Planks](https://polyhaven.com/a/wooden_planks).
- No encontré corcho en Poly Haven ⚠️: usar el del modelo de Sketchfab.

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la película

| Sitio | Qué es | Fuente |
|---|---|---|
| **El pueblo (Kokaua Town)** | Pueblo de Kauai. Su nombre sale en la serie, no en la película. Se basa en **Hanapepe**, en la costa sur de Kauai | ✅ [wiki de Lilo & Stitch](https://liloandstitch.fandom.com/wiki/Kokaua_Town), [Hawaii Aloha Travel](https://www.hawaii-aloha.com/blog/lilo-and-stitch-find-a-home-in-hanapepe/), [Only In Your State](https://www.onlyinyourstate.com/hawaii/lilo-and-stitch-town-hi) |
| **Hanapepe hoy** | Casas de madera de la época de las plantaciones, aceras de tablas, murales, un **puente colgante** de principios del siglo XX. En el **Aloha Theater** hay un mural: «Home of Lilo and Stitch» | ✅ Only In Your State, [Finding Debra](https://findingdebra.com/hanapepe-a-must-stop-town-in-kauai-for-disney-fans/), [Tours4fun](https://blog.tours4fun.com/find-lilo-and-stitch-location-in-hawaii.html) |
| **Acantilados** | El valle de **Kalalau** y la costa de **Nā Pali** salen al principio; Stitch aterriza cerca | ⚠️ «se parece mucho», dice [SFGate](https://www.sfgate.com/hawaii/article/lilo-stitch-tour-kauai-hawaii-17574368.php) |
| **Hanalei** | La bahía del norte, otra influencia probable | ⚠️ SFGate |
| **La película de 2025** | Se fue de Kauai | ⚠️ titular de [Beat of Hawaii](https://beatofhawaii.com/lilo-stitch-left-kauai-heres-the-story/) |
| **Más** | Guía de sitios reales | [Mapping Disney](https://mappingdisney.com/lilo-and-stitch-where-to-go-in-hawaii/) |

Sitios dentro de la película (de memoria ⚠️, mirar fotogramas):
- **El cuarto de Lilo**: arriba, con la pared de fotos, sus discos de
  Elvis y la ventana del deseo.
- **La casa Pelekai**: de madera, en alto, rodeada de verde.
- **El hālau de hula** con su porche (00:13:54: «She said to wait for
  her here on the porch») ✅ el porche.
- **La playa** del surf (00:46) y **el luau falso** donde trabajan Nani
  y David ✅ (lo del luau: [Cinemablend](https://www.cinemablend.com/new/Lilo-Stitch-Terrorize-Tourists-Deleted-Scene-33401.html)).
- **El puesto de fruta** de la señora Hasagawa (00:42:27) ✅ el nombre.
- **El bosque** donde Stitch se pierde (00:55).

### 5.2 Cómo se pintó: acuarela de verdad

- **Primera película de Disney con fondos en acuarela en unos 60 años**
  (desde Dumbo) ✅ ([AV Club](https://www.avclub.com/read-this-lilo-stitch-disney-watercolor-animation-1849681724),
  [Andreas Deja](http://andreasdeja.blogspot.com/2016/10/watercolor-backgrounds.html),
  [Animated Views](https://am.animatedviews.com/LiloAndStitch.html)).
- La idea fue del director de arte **Ric Sluiter**: las formas redondas
  pedían la acuarela de los años cuarenta. Al salir de la reunión se
  asustó y propuso gouache que pareciera acuarela; al final el estudio
  de **Florida** aprendió acuarela y acabó pintando **más rápido** que
  con gouache ✅ (resumen de [AV Club](https://www.avclub.com/read-this-lilo-stitch-disney-watercolor-animation-1849681724)
  y de la [historia oral](https://graduateschool.aub.ac.uk/top-news/an-oral-history-of-lilo-stitch.html)).
- **Las rocas de lava se texturizaron con sal gorda de mar** sobre la
  acuarela húmeda: truco de Maurice Noble ✅ (2.ª pasada: dos fuentes,
  [Animation Obsessive](https://animationobsessive.substack.com/p/the-shape-and-color-of-lilo-and-stitch)
  y [AV Club](https://www.avclub.com/read-this-lilo-stitch-disney-watercolor-animation-1849681724)).
- Artículo largo sobre forma y color: [Animation Obsessive](https://animationobsessive.substack.com/p/the-shape-and-color-of-lilo-and-stitch)
  (en la 2.ª pasada **sí abrió**: sus citas, en «Punto 18»).

### 5.3 Luz por sitio ⚠️ (de memoria, mirar fotogramas)

| Sitio | Hora | Luz |
|---|---|---|
| Cuarto de Lilo, pared de fotos | anochecer, 00:22 | lámpara cálida dentro, azul fuera; sombras suaves |
| Ventana del deseo | noche, 00:23 | azul profundo, estrellas; la «estrella» cruza |
| Playa del surf | mediodía, 00:46 | sol alto, agua turquesa, espuma blanca |
| Montaje final | día | luz limpia de foto casera, colores saturados |
| Bosque | amanecer, 00:55 | verdes fríos, niebla |

**Corregido en la 2.ª pasada, mirando vídeo** ✅:

| Sitio | Hora | Luz vista | Dónde |
|---|---|---|---|
| **Luau** donde trabaja Nani | noche | **cálida**: antorchas, madera de cabaña quemada, bailarín de fuego (0:12-0:24); fondo casi negro azulado | [clip del luau 1080p, 0:48](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p?t=48) |
| **Cuarto de Lilo** | noche | **morada y roja**, no azul: edredón rojo y blanco de flores, cómoda de madera oscura, lámpara verde con base de piña, collares en un clavo | [tráiler 2002, 2:12](https://archive.org/details/LiloStitchTrailer?t=132) |
| **Bosque del Patito Feo** | **noche**, no amanecer | luz azul de luna, plano cerrado, silencio | [película, 55:27](https://archive.org/details/lilo-stitch-2002_202609?t=3327) |
| **Mar del surf, 2025** | día | turquesa **apagado**, grado de color más gris que el 2002; plano de dron | [tráiler latino 2025, 1:44](https://www.dailymotion.com/video/x9fzrlk?start=104) |

### 5.4 Paleta de partida ⚠️ (sin medir: propuesta)

No pude bajar ni un fotograma. Estos hex son **una propuesta para
empezar**; hay que **muestrearlos** en capturas reales antes de pintar.

| Qué | Hex propuesto | Nota |
|---|---|---|
| Stitch, pelo | `#5A7EC8` | azul lavanda («periwinkle», según un resumen del buscador ⚠️) |
| Stitch, pecho y cejas | `#A8C6EA` | azul claro |
| Stitch, oreja por dentro | `#E6A2B8` | rosa |
| Stitch, nariz y parches | `#23305E` | azul marino |
| Vestido de Lilo | `#C6282E` | rojo con hojas blancas ✅ el diseño |
| Hojas del vestido | `#F4F1EA` | blanco roto |
| Top de Nani | `#E57A5C` | coral con corazón rosa ✅ el diseño |
| Cielo en acuarela | `#9FCBE0` | con bordes de agua |
| Mar | `#2E8FA8` | turquesa |
| Arena | `#E8D3A2` | cálida |
| Verde de hojas | `#4D8A4A` | acuarela, no plano |
| Borde de foto | `#F7F3E8` | papel fotográfico, un poco amarillo |
| Noche | `#1F2E52` | azul, nunca negro |

### 5.4b Paleta medida (Nuevo, 2.ª pasada) ✅

Medida con `estilo.py --colores` en fotogramas y con Pillow en arte
oficial. El % es cuánto ocupa en el fotograma.

| Qué | Hex medidos | De dónde |
|---|---|---|
| Luau de noche | `#234543` 17 % · `#150311` 15 % · `#8D4232` 15 % · `#662F30` 15 % · `#351930` 14 % | clip del luau, fotograma 0:48 |
| Luau, surtido amplio | `#813B2D` 27 % · `#02042A` 26 % · `#5F3421` 10 % · `#0E0103` 9 % | clip del luau, 1:00 |
| Cuarto de Lilo de noche | `#0C1F2A` 25 % · `#432626` 25 % · `#62414D` 16 % · `#954D2D` 13 % · `#6A1B1B` 12 % | tráiler 2002, 2:12 |
| Mar, 2025 | `#2F6867` 38 % · `#497B7E` 16 % · `#255757` 10 % | tráiler 2025, 1:44 |
| Stitch, pelaje con luz de atardecer | `#003D63` (sombra) → `#167DB1` (luz) | key visual «promo art 2», 3523×5000 |
| Pelo de Lilo | `#030308` | key visual |
| Falda de hula de Lilo | `#559B73` claro · `#146243` pliegues | key visual |

- **Correcciones a la propuesta de 5.4**: la noche de interior **no es
  azul** `#1F2E52`: es morada y roja (cuarto) o cálida de fuego (luau).
  El mar de 2002 sigue sin medir; el de 2025 es más gris que `#2E8FA8`.
- Estilo medido (`estilo.py`): sombreado degradado, poca línea,
  saturación 66-74 %, brillo 29-32 % en el luau. Coincide con la
  acuarela.
- El azul de Stitch medido lleva la luz del atardecer del cartel: el
  tono **plano** del cel sigue sin medir ⚠️ (§16).

### 5.5 Texturas reales equivalentes

- **Papel de acuarela** grano fino (para fondos pintados a mano).
- **Papel fotográfico** brillante y mate, con **borde blanco** y
  esquinas algo dobladas.
- **Cinta de carrocero** y **chinchetas** de colores (pared de Lilo).
- **Corcho** (tablero).
- **Madera pintada y saltada** (casa Pelekai; Poly Haven, §4.4).
- **Roca de lava** porosa, **arena**, **hojas de monstera**.
- **2.ª pasada, vistas en vídeo**: madera de cabaña con vetas oscuras y
  quemada (luau), edredón floral de tela gruesa (cuarto), **antorchas de
  fuego real** para poner luz cálida detrás del personaje.
- **CC0 en ambientCG**: telas lisas `Fabric030`, `Fabric061`, `Fabric083`
  ([lista](https://ambientcg.com/list?type=Material&q=fabric)) como base
  para pintar encima el estampado hawaiano; roca para el truco de la sal
  ([API](https://ambientcg.com/api/v2/full_json?type=Material&q=rock)).

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **El logo** «Lilo & Stitch» es rotulado a mano: letras redondas, de
  trazo grueso, algo inclinadas y bailando sobre la línea ✅ (varias
  webs de letras, p. ej. [FontMeme](https://fontmeme.com/lilo-stitch-font/)).
- La copia que circula se llama **«Buka Bird»**, de **Steve Ferrera**,
  **gratis sólo para uso personal** ✅ ([FontMeme](https://fontmeme.com/lilo-stitch-font/),
  [FontBolt](https://www.fontbolt.com/font/lilo-stitch-font/),
  [Fontspace.io](https://fontspace.io/lilo-and-stitch-font/)).
  **No pude bajarla** para ver si trae tildes ⚠️. Sirve, como mucho,
  para la palabra «Fotos» si el dueño acepta la licencia personal.
- Rótulos de la película: el libro del Patito Feo, la lista de Lilo,
  el papel de adopción. **No sé qué letra usan** ⚠️.

### 6.2 Letras libres comprobadas por mí

Bajadas de [google/fonts](https://github.com/google/fonts) y revisadas
con fontTools: **todas traen á é í ó ú ñ ¿ ¡** ✅.

| Para qué | Letra | Diseñador | Licencia |
|---|---|---|---|
| Título, redondo y gordo (lo más cercano al logo) | **Lilita One** | Juan Montoreano | OFL |
| Título con rebote de dibujo | **Chewy** | Sideshow | Apache 2.0 |
| Título con aire de surf y pincel | **Kavoon** | Viktoriya Grabowska | OFL |
| Título grueso alternativo | Titan One · Luckiest Guy · Carter One | Rodrigo Fuenzalida · Astigmatic · — | OFL · Apache · OFL |
| Rótulos redondos suaves | Sniglet · Fredoka · Baloo 2 · Bubblegum Sans | — | OFL |
| **Pie de foto a mano de Lilo** | **Gochi Hand** | HT Fonts | OFL |
| Pie de foto, rotulador fino y torcido | **Reenie Beanie** | James Grieshaber | OFL |
| Pie de foto de niña, redondito | **Covered By Your Grace** | Kimberly Geswein | OFL |
| Lista numerada de Lilo | Short Stack · Schoolbell · Patrick Hand | James Grieshaber · — · Patrick Wagesreiter | OFL · Apache · OFL |
| Rotulador gordo en el dorso de una foto | Permanent Marker | Font Diner | Apache |
| Papeles oficiales (Cobra Bubbles, adopción) | Special Elite | Astigmatic | Apache |

Recomendación: **Lilita One** para «Fotos» y **Gochi Hand** para los
pies de foto. Si la lámina lleva la lista de Lilo, **Short Stack**.

### 6.3 Una letra por uso (Nuevo, 2.ª pasada)

La parte de texto bajó cada letra de `fonts.gstatic.com` (la URL que da
la API `css2` de Google Fonts) y abrió su cmap con `fontTools`: **las 9
traen á é í ó ú ñ Ñ ¿ ¡** ✅ (comprobado el 24-sep-2026). Las 5
marcadas ⭐ son nuevas.

| Uso (punto 5 del encargo) | Letra libre | Diseñador | Licencia | Tildes, ñ, ¿ ¡ |
|---|---|---|---|---|
| Logo o título | **Lilita One** | Juan Montoreano | OFL | ✅ |
| Globo normal de cómic ⭐ | **[Comic Neue](https://fonts.google.com/specimen/Comic+Neue) Bold**, en mayúsculas | Craig Rozynski | OFL | ✅ |
| Grito, exclamación ⭐ | **[Bangers](https://fonts.google.com/specimen/Bangers)** | Vernon Adams | OFL | ✅ |
| Pensamiento (nube blanda) | **Baloo 2** | Ek Type | OFL | ✅ |
| Onomatopeya | **Luckiest Guy** | Astigmatic | OFL | ✅ |
| Cartel del mundo (tiki, surf, luau) ⭐ | **[Trade Winds](https://fonts.google.com/specimen/Trade+Winds)**: cartel de tiki-bar de los 50 | Sideshow | OFL | ✅ |
| Interfaz de juego, pantallas de la Federación ⭐ | **[Actor](https://fonts.google.com/specimen/Actor)**: sans condensada «de nave» | Sorkin Type Co. | OFL | ✅ |
| Subtítulos o créditos de vídeo ⭐ | **[Quicksand](https://fonts.google.com/specimen/Quicksand)** | Andrew Paglinawan | OFL | ✅ |
| Pie de foto a mano | **Gochi Hand** | HT Fonts | OFL | ✅ |

- **Variantes del logo vistas** ✅: en el juego de **Game Boy Advance**
  (2002, Digital Eclipse) el rótulo rojo con blanco va **metido en una
  tabla de surf**, con un borde verde de florecitas blancas y «Disney's»
  arriba en letra fina ([pantalla de título, 480×320](https://archive.org/download/stitch_gba/screenshot_12.png)).
  Sirve para un objeto físico (tabla, cartel de playa) sin copiar el
  logo tal cual. En el manga japonés *Stitch & the Samurai* el título es
  **pincel rojo anguloso** de cartel de samurái
  ([portada, 432×648](https://tokyopop.com/cdn/shop/products/9781427868961.jpg?v=1775858242&width=1946)):
  no va con #fotos.
- **Buka Bird** sigue sin poder bajarse (no está en Google Fonts ni en
  GitHub): tildes sin comprobar ⚠️. Para uso comercial hay que comprar
  la licencia o pedir permiso a Ferrera.
- Letra de los rótulos de la película (libro, lista, papel de adopción):
  **sigue sin identificar** ⚠️.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que la película pone en pantalla

**No hay globos, ni cartelas, ni pensamientos escritos.** Es una
película de Disney de 2002: todo se dice en voz alta. El texto escrito
aparece **en objetos de su mundo**:

| Objeto | Minuto | Qué dice | Estado |
|---|---|---|---|
| **Las fotos de Lilo** (pared) | 00:22:57 | Lo que ella ve bonito | ✅ la escena; el aspecto de las fotos ⚠️ |
| **La lista de Lilo** | 00:42:33 | «I've compiled a list of his traits…» «Number one is dancing» | ✅ subtítulo |
| **El anuncio del periódico** de la Sra. Hasagawa | 00:42:28 | «I'm here to answer your newspaper ad» | ✅ subtítulo |
| **El libro del Patito Feo** | 00:40:27 | «That's the Ugly Duckling» | ✅ subtítulo |
| **La foto de los padres** | 00:53:49 | «That's us before…» | ✅ subtítulo |
| **El papel de adopción con sello** | 01:15:48 | «See this stamp? I own him.» | ✅ subtítulo |
| **Los nudillos de Cobra** | 00:18:08 | «Your knuckles say "Cobra."» | ✅ subtítulo |
| Pantallas de la Federación Galáctica | 00:07 | hologramas de la Tierra | ⚠️ de memoria |

### 7.2 Cómo hablan (por el subtítulo)

- **Lilo** habla rápido, muy seria, con una **lógica propia**: «Pudge
  controls the weather» (00:13:09). Explica con **listas numeradas**
  (00:42:36). Insulta con «**Stupidhead!**» (00:15:17 y 01:12:31).
- **Stitch** casi no habla. Su idioma alienígena: «**Meega, nala
  kweesta!**» (00:02:23, un insulto que escandaliza al consejo). Dice
  «**Ih**» (01:07:39) y frases cortas sin verbos: «**My name Stitch**»
  (01:14:31), «**Lost.**» (00:55:31). Se ríe con **carcajada de loco**
  (00:02:29, «cackling sinisterly»).
- **Nani** manda con órdenes cortas: «**Go to your room!**» (00:21:19).
  Cuando se ablanda, habla bajito: «We're a broken family, aren't we?»
  (00:21:46).
- **Jumba** habla fino y teatral, con un inglés algo roto (sin
  artículos: «can think faster than supercomputer», 00:01:41). Se llama
  a sí mismo «**evil genius**» (00:02:37).
- **Pleakley** es nervioso y pedante, «experto en la Tierra»: «Earth is
  a protected wildlife reserve» (00:07:23). Chilla, se ofende, y se cree
  guapo: «You're just jealous 'cause I'm pretty!» (00:38:40).

### 7.3 Cómo se traduce a una lámina fija

1. **Pie de foto a mano** en el borde blanco de una foto, pegada con
   cinta. Es la voz de Lilo. Letra: Gochi Hand o Reenie Beanie.
2. **La lista de Lilo**: una hoja de cuaderno con «Número uno…»,
   «Número dos…». Es donde van las reglas del canal. Letra: Short Stack.
3. **Stitch no escribe**. Si «habla», es una **palabra suelta** al lado,
   o sale señalando la foto. Nunca un párrafo.
4. **Papel oficial con sello** (el de adopción, 01:15:48) para una
   norma seria. Letra: Special Elite, sello rojo.

### 7.4 En los videojuegos de la franquicia

Ver §13. Ninguno tiene una caja de diálogo tan reconocible como la de
Pokémon o Undertale. No la uses: el público reconoce la película, no
los juegos.

### 7.5 Qué NO hacer con el texto

- **Una burbuja blanca de cómic.** La película no tiene. (2.ª pasada:
  si hace falta un bocadillo, que sea **el del cómic oficial**, §7.6,
  nunca una burbuja plana de chat.)
- **Letras tiki de souvenir** (las de bar hawaiano con bambú): son el
  Hawái de turista del que la película se ríe.
- Poner a Stitch a explicar normas con frases largas: él dice tres
  palabras.
- Citar «**No estoy loco, mi realidad es simplemente diferente a la
  tuya**» como frase de Lilo y Stitch: circula en listas, pero **no
  está en los subtítulos** de la película ❌.

### 7.6 El bocadillo real de la franquicia (Nuevo, 2.ª pasada) ✅

La parte de texto **miró 3 páginas** del cómic de **Dynamite, *Disney's
Lilo & Stitch* n.º 1** (2024, guion de Greg Pak, dibujo de Giulia
Giacomino), de la [preview de DuckTalks](https://ducktalks.com/2024/01/03/dynamite-comics-lilo-stitch-1-preview/)
(1988×3057 cada página: [pág. 7](https://ducktalks.com/wp-content/uploads/2024/01/0007-1.jpg),
[pág. 8](https://ducktalks.com/wp-content/uploads/2024/01/0008-1.jpg)).

- **Bocadillo normal**: óvalo blanco, **borde negro de 3-4 px**, cola
  recta hacia quien habla. Letra **en mayúsculas, sans redondeada y
  gruesa** (como Comic Neue Bold). Las palabras clave, **en cursiva y
  más gruesas** («*BLOW* up», «*responsible* older sister», «*'OHANA*»).
  Nada de línea fina de cómic americano clásico: todo redondo, como los
  personajes.
- **Cartela de recuerdo o aparte**: rectángulo de esquinas redondeadas,
  **fondo azul pálido**, misma letra (el «Look, you can't… you can't
  just blow things up!» de Nani).
- **Vocabulario hawaiano dentro del globo, en cursiva**: *'Ohana*,
  *Kuleana* (responsabilidad) y *Mālama 'āina* (cuidar la tierra); el
  significado, con dos fuentes ([Ko Olina](https://koolina.com/destination/kuleana/),
  [NOAA](https://sanctuaries.noaa.gov/magazine/6/kuleana.html)).
- **La frase de la franquicia, en el cómic**: «'OHANA MEANS FAMILY. AND
  FAMILY MEANS NO ONE GETS LEFT BEHIND OR FORGOTTEN, RIGHT?» «RIGHT.»
  (David a Nani). Película + cómic: dos fuentes independientes.
- No vi bocadillo de pensamiento ni onomatopeyas en esas 3 páginas ⚠️
  (sólo un número del cómic).
- **Bocadillos vacíos para que escriban los niños**: en mayo de 2006
  *Disney Adventures* publicó «Stitch's Movie Mix-Up», una tira con los
  globos vacíos para que los lectores pusieran su diálogo ✅
  ([Lilo & Stitch Wiki](https://liloandstitch.fandom.com/wiki/Comic_Zone_Volume_1:_Disney%27s_Lilo_%26_Stitch),
  [TV Tropes, Comic Zone](https://tvtropes.org/pmwiki/pmwiki.php/ComicStrip/ComicZoneLiloAndStitch)).
  Idea para #fotos: «escribe tú el pie de foto».
- **Un globo dentro de la película**: la página del libro del Patito
  Feo lleva el texto «I'm Lost!» en un globo dibujado ✅ (fotograma
  propio de la parte de voz, [55:31](https://archive.org/details/lilo-stitch-2002_202609?t=3331)).
  Es el único «bocadillo» que sale en pantalla, y es de un libro.
- **Resumen para la lámina**: primero, texto escrito en objetos (pie de
  foto, lista, sello). Si hace falta un globo: **óvalo blanco de borde
  grueso, Comic Neue Bold en mayúsculas, palabra clave en cursiva**.

---

## 8 · Los personajes

### Lilo Pelekai — la fotógrafa

- **Quién es**: una niña hawaiana, huérfana, que vive con su hermana
  Nani. Sus padres murieron **un día de lluvia, en coche** ✅ (00:53:52).
- **Qué le importa**: que no la dejen (00:54:57: «I remember everyone
  that leaves»). Encontrar un amigo que no se vaya (00:23:42).
- **Manías**: el **sándwich de mantequilla de maní** para el pez Pudge
  cada jueves (00:12:35) ✅. Su muñeca **Scrump**, hecha por ella, con la
  cabeza demasiado grande (00:14:27) ✅. **Elvis** (00:40:56: «You look
  like an Elvis fan») ✅. **Fotografiar turistas** ✅.
- **Con quién**: Nani (se pelean y se quieren), Stitch (su «perro»),
  las niñas del hula (la rechazan; Mertle Edmonds, 00:22:25).
- **Cómo se expresa**: seria, directa, muy dramática. Muerde (00:22:29:
  «Before I bit her»). Explica en listas. Se enfada gritando y dando
  portazos (00:21:18). Cuando habla de algo que ama, **susurra**
  (00:22:57).
- **Lenguaje corporal** ⚠️ (de memoria): ceño fruncido de niña que se
  toma todo en serio; brazos cruzados; se tumba en el suelo cuando se
  enfada.

### Stitch (Experimento 626) — el más querido

- **Quién es**: creado por Jumba. «A prueba de balas y de fuego, piensa
  más rápido que una supercomputadora, ve en la oscuridad y mueve
  objetos 3.000 veces más grandes que él» (00:01:39 a 00:01:44) ✅. Su
  único instinto: **destruir** (00:01:49).
- **Qué le pasa**: no tiene nada que destruir y nadie a quien querer
  (Jumba, 00:39:35: «now he has nothing to destroy»). Con el Patito
  Feo descubre que **está perdido** (00:55:31) y busca familia.
- **Diseño**: pelo de **koala**, dientes redondos de **delfín**, orejas
  de **ciervo**, translúcidas ✅ (IndieWire / Yahoo, sobre cómo el
  director de 2025 siguió el «manual» de Sanders:
  [IndieWire](https://www.indiewire.com/features/craft/lilo-stitch-live-action-remake-dean-fleischer-camp-vfx-1235129089/)).
  Tiene **brazos de más, antenas y púas** que esconde para parecer perro
  ✅ (descripción del modelo de Sketchfab, §4.2).
- **Voz original**: **Chris Sanders**, el propio director, también en
  2025 y en Dreamlight Valley ✅.
- **Manías**: Elvis, el **ukelele** (00:43:40), leer el Patito Feo
  (00:40:27), el café (Lilo le llena el biberón de café, 00:36:51).
- **Cómo se expresa**: gruñe, olfatea, se ríe a carcajadas. Cuando está
  triste, **las orejas caen** ✅ (2.ª pasada, visto en
  [55:27](https://archive.org/details/lilo-stitch-2002_202609?t=3327):
  orejas caídas, mano en la barbilla, mirada baja).

### Nani Pelekai — la hermana que hace de madre

- **Quién es**: la hermana mayor y tutora legal de Lilo; **18 años** en
  la primera película ⚠️ (wiki de fans).
- **Qué le pasa**: pierde el trabajo en el luau, busca otro por todo el
  pueblo (00:42:28 a 00:44:18: «I am all about coffee», «Concierge-er-ing
  is my life», «I'm all about saving people») ✅, y un asistente social
  puede quitarle a Lilo.
- **Qué le importa**: que no la separen de Lilo. «I like you better as
  a sister than a mom» (00:22:06) ✅.
- **Cómo se expresa**: órdenes secas y enfado rápido; ternura bajita;
  canta «Aloha ʻOe» (00:52:51). Su mejor explicación (00:58:54):
  «Sometimes you try your hardest but things don't work out the way you
  want them to… maybe sometimes they're for the better» ✅.
- **Con quién**: David (el surfista que la quiere), Cobra Bubbles (el
  asistente social que la vigila).

### Dr. Jumba Jookiba — el «genio malvado»

- **Quién es**: jefe científico de Galaxy Defense Industries, juzgado
  por experimentos ilegales (00:00:31) ✅.
- **Cómo es**: de buen humor, listo y un poco loco; orgulloso de su
  obra; con la familia se vuelve **una especie de padre** para Lilo ✅
  (resumen de varias wikis:
  [Disney Wiki](https://disney.fandom.com/wiki/Jumba_Jookiba),
  [Lilo & Stitch Wiki](https://liloandstitch.fandom.com/wiki/Jumba_Jookiba)).
- **Frases**: «I prefer to be called "evil genius"!» (00:02:37).
  «I'll make you taller and not so fluffy!» → Stitch: «I like fluffy!»
  (01:00:46) ✅.
- **Ojo 2025**: en la película de imagen real Jumba **acaba de malo** y
  no se une a la familia ✅ ([TheWrap](https://www.thewrap.com/lilo-and-stitch-nani-gives-up-lilo-remake/),
  [Slate](https://slate.com/culture/2025/05/lilo-and-stitch-2025-movie-live-action-ending-vs-original-2002-controversy.html)).
  Para la lámina, el Jumba bueno es el de 2002.

### Agente Pleakley — el experto en la Tierra

- **Quién es**: alienígena de un ojo y tres piernas, «experto» de la
  Federación en la Tierra ✅ (00:07:39: «Agent Pleakley at your
  service»).
- **Manías**: los **mosquitos** (especie protegida, 00:07:29); se
  **disfraza de mujer** con peluca y vestido para pasar por humano ✅
  (Gizmodo, Deadline, The Mary Sue, sobre 2025); los dulces ⚠️.
- **Cómo se expresa**: nervioso, pedante, chillón, presumido. Se
  maravilla con cualquier cosa de la Tierra (00:38:48: «She's so
  beautiful», de un mosquito).
- **Por qué importa**: es **el secundario más querido** por los fans
  adultos. Que en 2025 **no lleve vestido** fue una de las quejas más
  sonadas: «Put Pleakley in the wig, cowards» ✅
  ([The Mary Sue](https://www.themarysue.com/put-pleakley-in-the-wig-cowards-audiences-are-frustrated-about-this-character-design-change-in-lilo-stitch/),
  [Deadline](https://deadline.com/2025/05/lilo-stitch-director-live-action-pleakley-not-wearing-dress-1236390838/),
  [Gizmodo](https://gizmodo.com/disney-lilo-stitch-movie-pleakley-dress-drag-2000600142)).
  El director de 2025 dice que **lo intentó** ✅.

### Los secundarios que conviene tener a mano

- **Cobra Bubbles**: asistente social enorme, con gafas negras;
  ex-CIA («Roswell. 1973», 01:16:03) ✅. Presentación: «Your knuckles
  say "Cobra."» (00:18:08) ✅. Frase: «I am the one they call when things
  go wrong» (00:19:11) ✅.
- **David Kawena**: el surfista amable. «There's no better cure for a
  sour face than a couple of boards and some choice waves» (00:45:52) ✅.
- **Capitán Gantu**: el gigante de la Federación. **Quitarlo en 2025
  enfadó mucho a los fans** ✅ ([Screen Rant](https://screenrant.com/lilo-and-stitch-2025-gantu-absence-reuben-introduction-issue-explained/),
  [SAN](https://san.com/cc/lilo-stitch-remake-breaks-records-sparks-controversy-over-characters/)).
- **Angel (Experimento 624)**: la «novia» de Stitch en la serie; muy
  vendida en productos ⚠️ (no lo medí).
- **Scrump** (la muñeca) y **Pudge** (el pez): objetos queridos.

### 8.1 Qué transmite cada uno, y su arco (Nuevo, 2.ª pasada)

- **Lilo**: pasa de estar sola y castigar a los demás **por adelantado**
  (antes de que la dejen) a dejar entrar a Stitch y rehacer su idea de
  familia (parte de voz). La wiki la describe como «muy
  desobediente» y «emocionalmente sensible: llora cuando la hieren o
  cuando le pasa algo a quien quiere» ✅ ([Disney Wiki, Personality](https://disney.fandom.com/wiki/Lilo_Pelekai#Personality)).
  Cumple **7 años** en la película (7 velas en el montaje final) ⚠️ un
  wiki. Miedos: que la gente se vaya, que Nani deje de quererla, que se
  la lleve un asistente social. **Qué deja**: ternura con un punto de
  pena; es la niña rara con la que se identifica quien fue un niño solo.
- **Stitch**: de arma sin propósito a «hijo» que aprende qué es una
  familia; el giro, el Patito Feo. Quien no lo quiere le llama «feo y
  deforme»; quien lo quiere, «tierno y esponjoso» ✅ ([Disney Wiki,
  Personality](https://disney.fandom.com/wiki/Stitch#Personality)).
  **Qué deja**: risa por el caos y un nudo en la garganta cuando se
  queda solo. Su registro en pantalla es rabia, alegría o melancolía;
  **no se le ve avergonzado ni con miedo** (parte de voz: puede ser
  propio del personaje).
- **Nani**: «amable, madura y cariñosa», pero el estrés del trabajo y
  de cuidar a la familia la vuelve «temperamental y sarcástica»; Jumba
  dice que su ira da más miedo que la de Hämsterviel ✅ ([Disney Wiki](https://disney.fandom.com/wiki/Nani_Pelekai#Personality)).
  **Qué deja**: agotamiento y amor a la vez.
- **Jumba**: «cómico, bocazas y entrañable» pese a lo de «malvado»; le
  interesa más el caos que el mal ✅ ([Disney Wiki](https://disney.fandom.com/wiki/Jumba_Jookiba#Personality)).
- **Pleakley**: exagerado y obsesivo, entra en pánico por nada, pero
  «no quiere mal a nadie» ✅ ([Disney Wiki](https://disney.fandom.com/wiki/Pleakley#Personality)).
  Especie **Plorgonarian**; Jumba le llama «Walking Noodle» (fideo
  andante) ([Lilo & Stitch Wiki](https://liloandstitch.fandom.com/wiki/Wendy_Pleakley)).
  Los directores pensaron a **Pleakley y Jumba como Marty McFly y Doc
  Brown** de *Regreso al futuro* ⚠️ un wiki.

### 8.2 Su cara en cada emoción, con fotograma (Nuevo, 2.ª pasada)

Fotogramas propios de la parte de voz con `fotogramas.py` sobre la
película entera de 2002 en Internet Archive (`?t=` = segundo de esa
copia). ✅ = visto en el fotograma. ⚠️ = falta: la parte de voz lo dejó
en su «Sigue:» y ya no se relanza (2 tandas agotadas).

| Personaje | Alegría | Rabia | Tristeza | Miedo | Vergüenza |
|---|---|---|---|---|---|
| **Lilo** | a carcajadas en el cohete de monedas, [31:44](https://archive.org/details/lilo-stitch-2002_202609?t=1904) ✅; ternura, sonrisa de lado mirando a Stitch, [36:56](https://archive.org/details/lilo-stitch-2002_202609?t=2216) ✅ | ⚠️ sin fotograma propio; sólo subtítulo: portazo 00:21:18, «Before I bit her» 00:22:29 | abrazada al peluche verde ante la pared de fotos, [22:10](https://archive.org/details/lilo-stitch-2002_202609?t=1330) ✅ | ⚠️ sin fotograma (la llamada a Cobra, 01:01:44, es pánico hablado); sólo la silueta del tráiler 2002, [1:24](https://archive.org/details/LiloStitchTrailer?t=84) | enseña a Scrump con sonrisa torcida y un ojo entornado, [14:35](https://archive.org/details/lilo-stitch-2002_202609?t=875) ✅ |
| **Stitch** | a carcajadas en el cohete, [31:44](https://archive.org/details/lilo-stitch-2002_202609?t=1904) ✅ | dientes y gruñido en la cápsula, [2:25](https://archive.org/details/lilo-stitch-2002_202609?t=145) ✅; silueta sobre escombros con luz verde, [23:59](https://archive.org/details/lilo-stitch-2002_202609?t=1439) ✅ | con el Patito Feo, orejas caídas, [55:27](https://archive.org/details/lilo-stitch-2002_202609?t=3327) ✅ | ⚠️ no aparece claro | ⚠️ no aparece claro |
| **Nani** | ternura: se duerme abrazada a Lilo, 22:20-22:55 ✅ | fastidio sirviendo en el luau, [1:39](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p?t=99) (1080p) ✅; rama en alto contra Stitch, [1:05:30](https://archive.org/details/lilo-stitch-2002_202609?t=3930) ✅; arrastra a Lilo, [20:50](https://archive.org/details/lilo-stitch-2002_202609?t=1250) ✅ | agotamiento: la misma cara del luau, a punto de perder el trabajo ✅ | ⚠️ sin fotograma (candidata: la entrevista de Cobra); el susto del tráiler, [2:12](https://archive.org/details/LiloStitchTrailer?t=132), es sorpresa | ⚠️ sin fotograma |
| **Jumba** | ⚠️ sin fotograma | ⚠️ sin fotograma | ⚠️ sin fotograma | escondido en arbustos con Pleakley, ojos muy abiertos, [28:37](https://archive.org/details/lilo-stitch-2002_202609?t=1717) ✅; entre escombros con un trozo de madera, [1:01:05](https://archive.org/details/lilo-stitch-2002_202609?t=3665) ✅ | ⚠️ sin fotograma |
| **Pleakley** | riendo con los brazos arriba junto a Jumba, [38:40](https://archive.org/details/lilo-stitch-2002_202609?t=2320) ✅; sonrisa traviesa cubierto de mosquitos, [39:00](https://archive.org/details/lilo-stitch-2002_202609?t=2340) ✅ | ⚠️ sin fotograma | ⚠️ sin fotograma | agachado en los arbustos, boca abierta, antena atrás, [28:37](https://archive.org/details/lilo-stitch-2002_202609?t=1717) ✅ | ⚠️ sin fotograma |

- **Cuenta**: 14 de 25 casillas con fotograma propio. Faltan (⚠️, de la
  línea «Sigue:» de `partes/voz.md`): miedo y vergüenza de Jumba y
  Pleakley, rabia y miedo de Lilo, miedo y vergüenza de Nani, y las
  demás de Jumba y Pleakley. Para sacarlas: volver a bajar
  `lilo-stitch-2002_202609` con `fotogramas.py`.
- **Dinámicas para láminas en grupo**: Lilo y Nani, **regañar → hacer
  las paces** (20:50-23:15, arriba). Jumba y Pleakley, **el dúo cómico**
  (se esconden juntos, 28:37; ríen juntos, 38:40). Lilo y Stitch,
  **cómplices** (cohete, 31:44; mesa del luau leyendo, §15). Nani y
  Stitch, **enemigos que se enseñan los dientes** (1:05:30).

---

## 9 · ¿Quién es el más querido?

**Respuesta corta: Stitch.** Lilo es la protagonista, pero el que vende,
el que sale en camisetas y el que la gente reconoce es Stitch.

| Dato | Fuente | Estado |
|---|---|---|
| Ventas de productos de Stitch: **2.600 millones de dólares** en el año fiscal 2024, **más de 4.000 millones** en 2025 | [Sherwood News](https://sherwood.news/markets/disney-sold-more-than-usd4-billion-in-stitch-merch-in-its-latest-fiscal-year/), [WDW News Today](https://wdwnt.com/2025/12/stitch-makes-disney-over-4-billion-in-merchandise-sales-replaces-mickey-on-national-tour/), [The Hollywood Reporter](https://www.hollywoodreporter.com/movies/movie-news/disney-2025-big-winner-stitch-character-1236457944/) | ✅ |
| Hace cinco años vendía unos 200 millones | resumen de [The Paper](https://www.thepaper.cn/newsDetail_forward_30930310) / [Tencent](https://news.qq.com/rain/a/20250524A06UMF00) | ⚠️ |
| Stitch **sustituye a Mickey** en una gira nacional | WDW News Today | ⚠️ titular |
| La película de 2025 pasó de **1.000 millones** en taquilla: la primera de Hollywood en 2025 | [THR](https://www.hollywoodreporter.com/movies/movie-news/lilo-and-stitch-becomes-first-billion-box-office-1236318553/), [Variety](https://variety.com/2025/film/news/lilo-stitch-first-2025-movie-billion-dollar-global-box-office-1236459515/), [Deadline](https://deadline.com/2025/07/lilo-stitch-1-billion-global-box-office-milestone-1236460970/) | ✅ |
| China: ventas de Stitch **casi ×4 en tres años**; cajas sorpresa con 52TOYS | [Tencent News](https://news.qq.com/rain/a/20250524A06UMF00), [The Paper](https://www.thepaper.cn/newsDetail_forward_30930310) | ⚠️ (resumen en chino) |
| Japón, «みんなのランキング» (encuesta de fans): Stitch **1.º** entre los personajes de Lilo & Stitch | [ranking.net](https://ranking.net/rankings/best-lilo-and-stitch-characters) | ⚠️ un resultado |
| Japón, misma web, **todos los personajes de Disney** (más de 8.000 votos): Stitch **5.º**, tras Ariel, Rapunzel, StellaLou y Donald | [ranking.net](https://ranking.net/rankings/best-disney-characters), [Magmix](https://magmix.jp/post/302508) | ⚠️ |
| Corea: la película de 2025 **fue floja** allí; el original se conoce poco | [Maxmovie](https://www.maxmovie.com/news/442952) | ⚠️ |
| Entre los secundarios, **Pleakley** y **Gantu**: las quejas por cambiarlos en 2025 muestran el cariño | §8 | ✅ |

**Nuevo (2.ª pasada)**, de la parte de voz:

| Dato | Fuente | Estado |
|---|---|---|
| Taquilla 2025: **1.038 millones de dólares** con un presupuesto de 100 millones | [Wikipedia (dato de Box Office Mojo)](https://en.wikipedia.org/wiki/Lilo_%26_Stitch_(2025_film)), THR | ✅ |
| Stitch como **marca-personaje** de Disney, cruce entre generaciones (quien lo vio en 2002 se lo enseña a sus hijos) | [The Walt Disney Company](https://thewaltdisneycompany.com/news/stitch-character-brand/), [THR](https://www.hollywoodreporter.com/movies/movie-news/disney-2025-big-winner-stitch-character-1236457944/) | ✅ |
| **26 de junio, «Día de Stitch»** (6/26, por el número 626); etiqueta #626day en TikTok | [Disney Latino](https://www.disneylatino.com/novedades/dia-de-stitch-que-significa-ohana), §14 | ✅ |
| **Pleakley, el secundario más querido por los adultos** (reacción a quitarle el vestido en 2025) | §8, The Mary Sue, Deadline | ✅ |

**No encontré ninguna encuesta oficial de Disney** por personajes de la
película (2.ª pasada: se buscó otra vez en español e inglés, «Disney
character popularity poll», «encuesta popularidad Disney personajes»;
sólo hay pistas indirectas: taquilla, ventas, quejas por recortes).

**Qué significa para #fotos**: la cámara la lleva **Lilo** (es su
afición en la película). Pero la foto que más gusta es **una de
Stitch**. Por eso en los tres conceptos **Stitch sale siempre**, aunque
no siempre hable.

---

## 10 · Doblaje latino

> [!note] 2.ª pasada: Doblaje Wiki ya abre
> En la primera pasada su API daba 403 y todo salía de resúmenes. En la
> 2.ª, la parte de voz leyó el wikitext por la API y lo cruzó con **The
> Dubbing Database** ([dubdb.fandom.com](https://dubdb.fandom.com/wiki/Lilo_y_Stitch_(Latin_American_Spanish)),
> wiki en inglés que redacta aparte su página del doblaje: cuenta como
> segunda fuente). ✅✅ = las dos fuentes.

### 10.1 Película de 2002

| Personaje | Voz latina | Estado y fuentes |
|---|---|---|
| **Lilo** | **Anaís Portillo** | ✅ [Doblaje Wiki: Lilo Pelekai](https://doblaje.fandom.com/es/wiki/Lilo_Pelekai), [TikTok de SDV: reto con Anaís Portillo](https://www.tiktok.com/@sdv_serviciosdevoz/video/7143761341776497925), [vídeo de Magic Treasures](https://www.facebook.com/magictreasures.cl/videos/mario-filio-y-anais-portillo-las-voces-de-doblaje-latino-de-lilo-stitch-2002-com/1426813825325701/) |
| **Stitch** | **Raúl Aldana** | ✅ ([Doblaje Wiki: Raúl Aldana](https://doblaje.fandom.com/es/wiki/Ra%C3%BAl_Aldana), [TikTok de SDV](https://www.tiktok.com/@sdv_serviciosdevoz/video/7207515646316252422?lang=es)). **Resuelto el matiz** (Doblaje Wiki, «Datos de interés»): en esta película Aldana **sólo grabó los diálogos en español** («Hola», «Así me gusta», «Tierno y esponjoso»); **gemidos, gruñidos y balbuceos se quedaron con la voz original de Chris Sanders**. Los **ladridos** con los que Stitch sale de la perrera sí los hizo Aldana (en inglés eran de un perro real), y ese audio se usó también en el doblaje japonés ⚠️ una fuente. Las dos versiones de los tráileres con clásicos Disney (cine y DVD de dos discos) siguen igual: en la del DVD, Aldana dobló a Stitch. |
| **Nani** | **Claudia Garzón** (canciones: Irasema Terrazas) | ✅✅ [Doblaje Wiki, Nani Pelekai](https://doblaje.fandom.com/es/wiki/Nani_Pelekai), The Dubbing Database. **Antes ❌, resuelto** |
| **Jumba** | **Maynardo Zavala**, acreditado en pantalla como «**José Maynardo**» | ✅✅ [Doblaje Wiki, Jumba Jookiba](https://doblaje.fandom.com/es/wiki/Jumba_Jookiba), The Dubbing Database. Lo hizo hasta *Leroy y Stitch* (2006); murió en 2008 y en «¡Stitch!» lo sustituyó Armando Réndiz ⚠️ (sólo Doblaje Wiki) |
| **Pleakley** | **Rubén Trujillo** «Trujo» | ✅✅ Doblaje Wiki, The Dubbing Database. **Antes ❌, resuelto** |
| **Cobra Bubbles** | **Rubén Moya** (también los insertos) | ✅✅ **Antes ❌, resuelto** |
| **David Kawena** | **Noé Velázquez Pedroza** | ✅✅ **Antes ❌, resuelto** |
| Capitán Gantu | Gerardo Reyero | ✅✅ |
| Gran Concejal | Patricia Martínez | ✅✅ |
| Mertle Edmonds | Fernanda Robles | ✅✅ |
| **Kumu Moses Puloki** (el profesor de hula) | **Mario Filio** | ✅✅ **Resuelve el misterio** de la 1.ª pasada: ésa es su voz |
| Encargada de la perrera | Jessica Ortiz | ✅✅ |
| Primera oficial Ombit | Cristina Hernández | ✅✅ |
| Teniente de custodia, conductor de camión 2 | Ricardo Tejedo | ✅✅ |
| Piloto | Yamil Atala Cabrera | ✅✅ (nuevo) |
| Piloto femenina rosa | Karla Falcón | ✅✅ |
| Conductor de camión | Raúl Aldana | ✅✅ |
| Guardia intergaláctico | José Carlos Moreno | ⚠️ sólo Doblaje Wiki |
| Dueño del restaurante · dueña de la cafetería · salvavidas | Raúl Anaya · Loretta Santini · Aurora Mijangos | ⚠️ sólo Doblaje Wiki |
| **Estudio** | **Doblaje Audio Traducción, S.A. de C.V.** | ✅✅ Doblaje Wiki y la ficha de The Dubbing Database. **Sube de ⚠️ a ✅** |
| **Dirección** | **Ricardo Tejedo** según la ficha de Doblaje Wiki; la 1.ª pasada decía **José Carlos Moreno** | ⚠️ **sigue en duda**. Pista: en Doblaje Wiki Moreno sale como **actor** (el guardia) y la nota dice que fue «uno de los últimos proyectos del querido actor y director» antes de morir el 3 de mayo de 2002; de ahí salió la confusión. Pero la dirección sólo la da una fuente (The Dubbing Database no la dice) y la parte de voz no pudo confirmarla (quedó en su «Sigue:») |
| Traducción · gerente creativo | Raúl Aldana | ⚠️ sólo Doblaje Wiki |
| Grabación | abril-mayo de 2002, en México | ⚠️ sólo Doblaje Wiki |
| Canción «**Muero de amor por ti**» | la canta **Bandana** (Argentina); letra de Laura Rama y Walterio Pesqueira; estudio Santito, mezcla Igloo Music | ⚠️ sólo la ficha de Doblaje Wiki. **Resuelve** el «intérprete no encontrado» de la 1.ª pasada, con una fuente |

Más datos sueltos:
- **Fernanda Robles** (Mertle) hizo prueba para Lilo, con la escena en
  que llega tarde a hula por darle el sándwich a Pato el pez (Doblaje
  Wiki, entrevista con Idzi Dutkiewicz) ⚠️ una fuente.
- En latino, el pez **Pudge** se llama «**Pato el pez**» ✅ (Doblaje Wiki
  y un [TikTok](https://www.tiktok.com/discover/doblaje-lilo-y-stitch-pato-el-pez-tu-voz)).
  Y por el ajuste de labios, el sándwich es **de mermelada**, no de
  mantequilla de maní, aunque en la imagen se ve la mantequilla ⚠️
  (Doblaje Wiki).
- **Disney+** cambió la escena de Lilo escondida en la **lavadora** por
  una **caja de pizza** en una cajonera vacía; en inglés quitaron el
  ruido metálico ⚠️ (Doblaje Wiki).
- Vídeo que repasa el doblaje: [Draquio, «Doblaje de Lilo y Stitch»](https://www.youtube.com/watch?v=-_9cimLHdaA).

### 10.2 Película de 2025 (imagen real)

Doblaje **nuevo** para México y Latinoamérica ✅ (sdpnoticias). La 2.ª
pasada lo comprobó contra el reparto final de
[Doblaje Wiki, Lilo y Stitch (2025)](https://doblaje.fandom.com/es/wiki/Lilo_y_Stitch_(2025))
y [The Dubbing Database (2025)](https://dubdb.fandom.com/wiki/Lilo_y_Stitch_(Latin_American_Spanish,_2025)).
**Dos nombres de prensa estaban mal.**

| Personaje | Voz latina | Estado y fuentes |
|---|---|---|
| **Stitch** | **Gerardo Becker Ania**, abogado laboralista de Huixquilucan que dobla por afición | ✅✅ [ABC Noticias](https://abcnoticias.mx/tendencia/2025/5/21/quien-es-el-abogado-mexicano-que-hace-la-voz-de-stitch-videos-249770.html), [MG Noticias](https://mgnoticias.mx/quien-es-el-abogado-mexicano-que-hace-la-voz-de-stitch/), Doblaje Wiki, The Dubbing Database |
| **Nani** | **Alicia Vélez** | ✅✅ Doblaje Wiki y The Dubbing Database. **Corregido**: antes decía «Karen Vallejo» (nota de prensa de sdpnoticias y la-lista) |
| **Jumba** | **Sergio Gutiérrez Coto** (Batman en la trilogía de Nolan) | ✅✅ |
| **Pleakley** | **Armando Guerrero** | ✅✅ **Corregido**: antes decía «Arturo Castañeda» (nota de prensa) |
| **Lilo** | **Aurora Villegas Romero** | ✅✅ sube de ⚠️ |
| Cobra Bubbles | Octavio Rojas | ✅✅ sube de ⚠️ |
| Gran Concejal | Rebeca Manríquez | ✅✅ sube de ⚠️ |
| David Kawena | **Iván Bastidas** | ✅✅ nuevo |
| Gantu | no sale en 2025, no hay voz | ✅ |
| Mertle Edmonds · Tutu (la abuela) · Sra. Kekoa · Kumu Hula | Habana Zoé · Ma. Eugenia Guzmán · Yolanda Vidal · Polo Rojas | ✅✅ nuevos |

### 10.3 Frases del doblaje latino

| Quién | Frase | Minuto (inglés) | Estado |
|---|---|---|---|
| Lilo y Nani | «**Ohana significa familia, y tu familia nunca te abandona ni te olvida**» | 00:36:13 | ✅ [Disney Latino](https://www.disneylatino.com/novedades/las-7-frases-de-lilo-y-stitch-que-quedaron-en-tu-memoria), [El Tiempo](https://www.eltiempo.com/cultura/gente/lilo-y-stitch-las-7-mejores-frases-de-la-pelicula-y-por-que-siguen-emocionando-al-publico-3456648), [YouTube](https://www.youtube.com/shorts/GED3bZM-to8) |
| Stitch | «**Esta es mi familia, la encontré, estaba aquí. Es chiquita y rota, pero es buena**» | 01:15:00 | ✅ Disney Latino, El Tiempo |
| Lilo, por teléfono a Cobra | «Extraterrestres atacan mi casa… **¡quieren a mi perro!**» | 01:01:44 | ⚠️ sólo la lista de las «7 frases» |
| Lilo a Stitch | «Destruyes todo lo que tocas, ¿por qué no intentas cambiar algunas cosas?» | 00:37:35 | ⚠️ la lista la da así; el inglés dice «make something» |
| Lilo | «Elvis Presley era un buen ciudadano. Recopilé estos ejemplos para que practiques, el número uno es el baile» | 00:42:30 | ⚠️ |
| Nani | «Lilo, a veces tratas con ganas, pero las cosas no salen como esperabas…» | 00:58:54 | ⚠️ |
| Lilo | «¡Mi cámara está llena otra vez! ¿No son…?» | 00:22:54 | ⚠️ **no encontrada** en ninguna de las dos pasadas: la parte de voz la dejó en su «Sigue:» (bajar subtítulos en español de un clip oficial doblado) y ya no se relanza. Es una adaptación: no rotularla como cita |

- **Ojo con «Ohana»**: circula otra versión, «…y familia significa que
  nadie se queda atrás ni se olvida». Parece la de **España** ⚠️ (no lo
  pude confirmar). En latino, la documentada es «**nunca te abandona ni
  te olvida**».
- **Ojo con las listas de frases**: la de las «7 frases» (Disney Latino
  o El Tiempo; el buscador las mezcla) incluye «No estoy loco, mi
  realidad es simplemente diferente a la tuya», que **no está en la
  película** (§7.5).
- **2.ª pasada**: la parte de voz no sumó frases latinas nuevas
  transcritas de vídeo; confirma que las dos con ✅ siguen en pie. Los
  clips latinos de Dailymotion son sólo tráileres de 2025.

---

## 11 · Música

| Tema | Qué es | Ambiente | Estado |
|---|---|---|---|
| **«He Mele No Lilo»** | Canción de la clase de hula (00:10:22 ⚠️ que sea esta, por la letra del subtítulo). De **Mark Keali'i Ho'omalu** y **Alan Silvestri**, con el **coro infantil de las Kamehameha Schools** | tradición, alegría de grupo | ✅ [Wikipedia (resumen)](https://en.wikipedia.org/wiki/Lilo_%26_Stitch_(2002_soundtrack)), [Filmtracks](https://www.filmtracks.com/titles/lilo_stitch.html) |
| **«Hawaiian Roller Coaster Ride»** | El surf (00:46:05) | energía, sol, mar | ✅ ídem |
| **«Aloha ʻOe»** | Nani se la canta a Lilo (00:52:51) | despedida, ternura | ✅ subtítulo |
| **Elvis Presley** | «Heartbreak Hotel» (00:15:22), «Stuck on You» (00:30:26), «(You're the) Devil in Disguise» (00:42:22), «Hound Dog» (01:00:18) | rock de los 50, humor | ✅ subtítulos |
| **«Burning Love»** | Montaje final de fotos (01:17:26); versión de **Wynonna** | fiesta, final feliz | ✅ subtítulo, TV Tropes |
| **«Can't Help Falling in Love»** | Créditos (01:20:25), versión pop | romántico | ✅ subtítulo |
| **Versiones en español** | Las ediciones latinas del disco añaden **«Muero de amor por ti»** («Can't Help Falling in Love» en español). Las europeas, **«Ardiente amor»** («Burning Love») | — | ⚠️ un resumen. **2.ª pasada**: según la ficha de Doblaje Wiki la canta **Bandana** (Argentina) ⚠️ una fuente (§10.1) |
| **Música de Alan Silvestri** | La partitura; la versión completa está en [Internet Archive](https://archive.org/details/lilo-stitch-complete-soundtrack) | aventura, ternura | ✅ existencia |

**Para #fotos**: el montaje final con «Burning Love» **es** un álbum de
fotos con música. Es el ambiente de la lámina: alegre, casero, de
familia.

### 11.1 Los créditos, leídos en pantalla (Nuevo, 2.ª pasada) ✅

La parte de vídeo leyó el **cartel de créditos** en el vídeo de los
créditos finales ([Internet Archive, emisión de Disney Channel 2004](https://archive.org/details/lilo-stitch-3)),
con `fotogramas.py --fotograma`. Una fuente, pero es el propio crédito.

| Canción | Escrita por | La canta | Minuto del vídeo |
|---|---|---|---|
| «He Mele No Lilo» y «Hawaiian Roller Coaster Ride» | Alan Silvestri y Mark Keali'i Ho'omalu | coro infantil | [0:50](https://archive.org/details/lilo-stitch-3?t=50) |
| «Can't Help Falling in Love» | Luigi Creatore, Hugo Peretti y George David Weiss | **A*Teens** (grupo pop sueco, Stockholm Records), producida por Mark Hammond | [4:20](https://archive.org/details/lilo-stitch-3?t=260) |
| «Burning Love» | Dennis Linde | **Wynonna** (Curb/Universal) | [4:30](https://archive.org/details/lilo-stitch-3?t=270) |
| «Hound Dog» · «Heartbreak Hotel» · «(You're the) Devil in Disguise» · «Blue Hawaii» · «Stuck on You» | Leiber y Stoller · Presley, Axton y Durden · Baum, Giant y Kaye · Rainger y Robin · (cortado) | **Elvis Presley** (RCA/BMG) | 4:20-4:30 |
| «Suspicious Minds» | Mark James | (cortado en el fotograma) ⚠️ | 4:20 |

- **Coro**: Kamehameha Schools Children's Chorus, dirigido por **Lynell
  K. Bright** ✅ visto (4:30-4:40). La 1.ª pasada no tenía el director.
- **Equipo de la partitura**: arreglos de coro de Silvestri y Ho'omalu;
  orquestaciones de **Mark McKenzie** y **William Ross**; editor de
  música **Ken Karman**; coordinación de grabación David Bifano ✅ visto.
- **2025**: sigue siendo Elvis y tradición hawaiana. En el *featurette*
  oficial de Disney Francia una cantante hawaiana vuelve a grabar
  «Hawaiian Roller Coaster Ride» y un entrevistado dice que «no puede
  haber Lilo y Stitch sin Elvis» ✅ visto
  ([Dailymotion, NoPopCorn, en francés, 0:00-3:01](https://www.dailymotion.com/video/x9jtp6m)).
  Banda sonora de 2025: **Dan Romer** ([MusicBrainz](https://musicbrainz.org/release-group/1271a043-7119-475c-b060-2c8a246c3ba3)).
- Discos publicados (MusicBrainz): el original del 11-jun-2002, *Island
  Favorites* (2002), *Hawaiian Album* (2006) y el promocional de Alan
  Silvestri ([MusicBrainz](https://musicbrainz.org/release-group/5f2eaaca-e3c9-393e-bc31-83b7d60250d7)).
- **Silencio que duele**: la escena del Patito Feo (55:27) **no lleva
  música**, sólo el bosque; la de la hamaca, «Aloha ʻOe» **a capela**
  (parte de voz, §Punto 21).

---

## 12 · Vídeos

Primera pasada: YouTube no abría, **no vi ninguno**. **2.ª pasada**: los
de §12.1 se miraron de verdad con `fotogramas.py` (Internet Archive y
Dailymotion; YouTube pedía iniciar sesión). Los de la tabla de abajo
siguen sin mirar ⚠️.

### 12.1 Vídeos mirados de verdad (Nuevo, 2.ª pasada)

| Vídeo | Qué se ve | Minutos útiles |
|---|---|---|
| [Tráiler original 2002](https://archive.org/details/LiloStitchTrailer) (640×346) | Cameos de clásicos Disney antes de revelar «STITCH»; cápsula con la foto de Lilo; «INDESCRIBABLE»; sombra que asusta a Lilo; cena; título «Walt Disney LILO & STITCH»; baile con un tocadiscos; Nani descubre a Stitch | [0:36](https://archive.org/details/LiloStitchTrailer?t=36) Stitch tras una malla · 1:06 playa de noche · [1:36](https://archive.org/details/LiloStitchTrailer?t=96)-1:42 cena · [1:48](https://archive.org/details/LiloStitchTrailer?t=108) cápsula · 2:00 título · [2:06](https://archive.org/details/LiloStitchTrailer?t=126) tocadiscos · [2:12](https://archive.org/details/LiloStitchTrailer?t=132) susto de Nani |
| [Tráiler oficial 2025, doblado latino](https://www.dailymotion.com/video/x9fzrlk) (Sensacine, 512×288) | Castillo Disney, Stitch CGI mojado en casa, coche, playa, surf con dron, portal con Jumba y un agente, niña llorando junto a Stitch | 0:40 cocina · 1:04-1:20 playa, coche, carrera · [1:44](https://www.dailymotion.com/video/x9fzrlk?start=104)-1:52 surf |
| [Créditos finales 2002](https://archive.org/details/lilo-stitch-3) (TV 2004, 854×480) | El «álbum» de fotos con Stitch colado; ficha técnica; créditos de canciones | 0:00-1:20 fotos · 0:50 y 4:20-4:40 canciones |
| [Luau, «Nani Loses Her Job», 1080p](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p) (1824×1080) | Bailarín de fuego, Nani sirviendo, Lilo y Stitch cenando y leyendo | [0:12](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p?t=12)-1:00 |
| [Película 2002 entera](https://archive.org/details/lilo-stitch-2002_202609) (85 min, audio francés) | Mirada por la parte de voz: más de 25 fotogramas propios (§8.2) | ver §8.2 y §15 |
| [*Featurette* de la música 2025](https://www.dailymotion.com/video/x9jtp6m) (francés) | Compositor, cantante hawaiana grabando | 0:00-3:01 |

- **Descartado**: el «Part 1 HD» de Internet Archive (480×360, rayas de
  VHS, sólo llega a 7:59): no sirve para confirmar nada.
- **Sin bajar por tamaño** (por si hace falta): la película en VHS de
  fans (`lilo-stitch-2002-fanmade-vhs`, 1,9 GB) y el especial de ABC
  *Aloha From Hollywood* con Wynonna (`disneys-lilo-stitch-aloha-from-hollywood-2002`,
  1,3 GB), que puede tener «Burning Love» en directo.
- **TikTok**: no hay acceso desde el servidor; los enlaces de abajo
  siguen sin ver ⚠️.

### 12.2 Vídeos citados en la primera pasada (sin mirar)

| Vídeo | Qué es | Para qué sirve |
|---|---|---|
| [Tráiler oficial latino 2025](https://www.youtube.com/watch?v=XbhjvJ-Ye7Q) | Tráiler en español latino | Voces nuevas; tono del remake |
| [Teaser latino 2025](https://www.youtube.com/watch?v=msQ9LwDaKrE) | Primer teaser | Stitch solo, gags |
| [«Stitch puede despedirse», clip latino de Disney](https://www.youtube.com/watch?v=2ZpENZiv8z8) | Escena final de 2002, doblada | **Oír la frase «es chiquita y rota, pero es buena»** en latino |
| [«Ohana: la familia nunca te abandona ni te olvida»](https://www.youtube.com/shorts/GED3bZM-to8) | Corto con la frase | Confirmar la frase latina |
| [Final con «Burning Love»](https://www.youtube.com/watch?v=r4aor3FulOU) | El montaje de fotos del final | **Referencia principal de las fotos** |
| [Inter-Stitch-als, los cuatro](https://www.youtube.com/watch?v=Oh5SvyCX9QE) · [otra subida](https://www.youtube.com/watch?v=4y7bWHobD7U) | Tráileres de 2002 | Stitch «colándose» en la foto |
| [Teaser de La Bella y la Bestia, 4K](https://www.youtube.com/watch?v=0EPdOPhwpUA) | Uno de los cuatro | Ídem, en alta |
| [¿Por qué Lilo saca fotos a turistas?](https://www.youtube.com/watch?v=iy8S-8lTFEs) · [corto](https://www.youtube.com/shorts/xqxWUiF9ZQw) | Análisis en español | La afición de Lilo, la escena eliminada |
| [Doblaje de Lilo y Stitch, Draquio](https://www.youtube.com/watch?v=-_9cimLHdaA) | Repaso de voces latinas | Cruzar nombres del §10 |
| [¿Quién es el abogado que hace la voz de Stitch?](https://www.youtube.com/watch?v=Uv8OUN-9-ok) | Gerardo Becker | Voz de 2025 |
| [Stitch en Dreamlight Valley, misiones](https://www.youtube.com/watch?v=YOwDJajoil8) | Guía del juego | Ver su caja de diálogo |
| [TikTok: fotos a turistas](https://www.tiktok.com/discover/lilo-and-stitch-lilo-pictures-of-tourist) · [«Lilo y Stitch fotos a turistas»](https://www.tiktok.com/discover/lilo-y-stitch-fotos-a-turistas) | Tendencia | La escena de la cámara es reconocible |
| [TikTok: Stitch de Elvis, 2025](https://www.tiktok.com/discover/2025-lilo-and-stitch-stitch-being-elvis) | Tendencia | Pose de Elvis |
| [TikTok: «blue punch buggy»](https://www.tiktok.com/@never_grow_up_vacations_/video/7249023615801363754) | Meme | §14 |

---

## 13 · Videojuegos de la franquicia

| Juego | Qué es | Útil para la lámina | Estado |
|---|---|---|---|
| **Disney Dreamlight Valley** | Stitch es vecino desde la actualización «Missions in Uncharted Space» (**6 de diciembre de 2022**). Le pone voz Chris Sanders. Su primera misión empieza con **un cartel vandalizado** y un «control de bondad»; la de nivel 10, «Making Music», es **montar una banda** | La caja de diálogo del juego ⚠️ no la vi. Idea: **Stitch y los carteles pintarrajeados** | ✅ [wiki DDV](https://disneydreamlightvalley.fandom.com/wiki/Stitch), [Prima Games](https://primagames.com/tips/how-to-unlock-stitchs-friendship-quests-in-disney-dreamlight-valley-hidden-requirement-guide), [Pro Game Guides](https://progameguides.com/disney-dreamlight-valley/how-to-complete-stitchs-level-ten-friendship-quest-in-dreamlight-valley/) |
| **Kingdom Hearts** | En Birth by Sleep, mundo **Deep Space** (la parte espacial de la película). Stitch es invocación; su remate «**Ohana Beat**» convierte la llave espada en **ukelele** | Nada de fotos | ✅ [KH Wiki](https://www.khwiki.com/Stitch), [Deep Space](https://www.khwiki.com/Deep_Space) |
| **Lilo & Stitch: Hawaiian Adventure** (PC, 2002) | Minijuegos: aprender hula, buscar aparatos, controlar el **nivel de maldad** de Stitch, enseñarle ohana y ganar el **premio al Ciudadano Modelo de Cobra Bubbles** | La idea del «ciudadano modelo» (00:42:07) | ✅ [Disney Wiki](https://disney.fandom.com/wiki/Lilo_%26_Stitch:_Hawaiian_Adventure), [Giant Bomb](https://giantbomb.com/wiki/Games/Lilo_And_Stitch_Hawaiian_Adventure), [TCRF](https://tcrf.net/Disney's_Lilo_&_Stitch:_Hawaiian_Adventure) |
| **Trouble in Paradise** (PS1 y PC, 2002, Blitz Games) | Plataformas. En 2023 salió un prototipo y el código fuente | — | ✅ [TCRF, prototipo](https://tcrf.net/Proto:Disney's_Lilo_&_Stitch:_Trouble_in_Paradise_(PlayStation)) |
| **Stitch: Experiment 626** (PS2, 2002) | Stitch en el espacio. Tenía una galería «SECRETS» con imágenes de la película, sin usar | — | ✅ [TCRF](https://tcrf.net/Disney's_Stitch:_Experiment_626) |
| **Lilo & Stitch** (GBA, 2002, Digital Eclipse) | Plataformas de lado | — | ✅ [TCRF](https://tcrf.net/Disney's_Lilo_&_Stitch_(Game_Boy_Advance)) |
| Otros en TCRF | Pinball de Lilo & Stitch; categoría completa | — | [TCRF, categoría](https://tcrf.net/Category:Lilo_&_Stitch_series) |

**Conclusión**: ningún juego da un cuadro de diálogo propio y famoso.
**No lo uses** en esta lámina (ver §7.4).

### 13.1 Lista completa y lo que se vio (Nuevo, 2.ª pasada)

Sacada del wikitext de la ficha de franquicia
([Disney Wiki](https://disney.fandom.com/wiki/Lilo_%26_Stitch_(franchise)))
y cruzada con [Wikipedia](https://en.wikipedia.org/wiki/Lilo_%26_Stitch_(franchise)) ✅:

| Juego | Año | Plataforma | Nota |
|---|---|---|---|
| *Lilo & Stitch* | 2002 | GBA | **pantalla de título vista**: logo en una tabla de surf, «PRESS START» amarillo con contorno negro, letra de bloque pixelada ([captura 480×320](https://archive.org/download/stitch_gba/screenshot_12.png)) ✅ |
| *Lilo & Stitch Pinball* | 2002 | PC | — |
| *Trouble in Paradise* · *Hawaiian Adventure* · *Stitch: Experiment 626* | 2002 | PS1/PC · PC · PS2 | ya arriba |
| *Lilo & Stitch 2: Hämsterviel Havoc* | 2005 | GBA/PC | secuela |
| *Kingdom Hearts II* | 2005 | PS2 | Stitch es **invocación** con el «Encanto de Ukulele»: no pisa el campo, **lame la pantalla** para rellenar vida y magia y para proyectiles; lleva su traje espacial rojo ✅ ([KH Wiki](https://www.khwiki.com/Stitch), [GameFAQs](https://gamefaqs.gamespot.com/ps2/915410-kingdom-hearts-ii/answers/115138-missed-stitch-summon)) |
| *Kingdom Hearts: Birth by Sleep* | 2010 | PSP | aquí debuta **Sparky (Experimento 221)**: el primer personaje nacido en una serie de TV de Disney que llega a KH |
| ***Motto! Stitch! DS*** | 2008 | Nintendo DS | **sólo en Japón**; nuevo |
| *Disney Magical World* 1 y 2 | 2013/2017 | 3DS | Stitch vecino |
| *Disney Infinity* 1 y 2.0 | 2013/2014 | varias | figura de Stitch (hoja 3, n.º 546) |
| *Disney Heroes: Battle Mode* | 2018 | móvil | Stitch estilo chibi |
| *Disney Dreamlight Valley* | 2022 | varias | caja de diálogo **sigue sin ver** ⚠️ |
| *Disney Speedstorm* | 2023 | varias | Stitch piloto de carreras |
| *Stitch Jam* | — | móvil | — |

- **No se vieron capturas de juego** (sólo la pantalla de título del
  GBA): MobyGames y TCRF dieron 403 en la 2.ª pasada ⚠️.
- **Cruce con Big Hero 6**: el **Experimento 619 «Splodyhead»** sale en
  *Big Hero 6* (2014) ✅ (Disney Wiki). Hay biblia de Big Hero 6 en el
  servidor (`08-big-hero-6-grandes-h-roes`).

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todos reconocen

- **«Ohana significa familia…»** (00:36:13 y 00:54:34) ✅. Es la frase.
- **Stitch de Elvis** con tupé y traje (00:44) ✅, vuelve en 2025 ✅.
- **«Blue punch buggy!»** (01:01:38, Lilo pega a Stitch al ver un
  escarabajo azul) ✅ subtítulo. Meme vivo en TikTok, «no punch backs» ✅.
- **Stitch Day, el 26 de junio** (6/26, su número) ✅ (etiqueta #626day
  en TikTok; [Disney Latino, Día de Stitch](https://www.disneylatino.com/novedades/dia-de-stitch-que-significa-ohana)).
- **«Era un collie antes de que lo atropellaran»** (00:32:54, «He used
  to be a collie before he got ran over») ✅ inglés; latino ⚠️.
- **Pleakley con peluca** ✅ (§8).
- **La pared de turistas** de Lilo ✅ (§2): el fandom la comenta, con
  cariño y con debate
  ([Feminist Disney](https://feministdisney.tumblr.com/post/23475837856/in-your-critique-of-lilo-and-stitch-you-didnt),
  [filmboards](https://filmboards.com/board/t/Lilos-obsession-with-fat-people-1118389/)).
- **El Patito Feo** y «Lost» (00:55:31): el momento que hace llorar ✅.
- **2.ª pasada**: la **hamaca** (Nani canta «Aloha ʻOe», 00:52:51) es para
  el fandom el momento de «representación emocional»: alguien tomó una
  familia real, desordenada y sin filtro, y la volvió algo hermoso ✅
  (hilo de Reddit citado en [gonewith.substack.com](https://gonewith.substack.com/p/lilo-and-stitch-is-the-movie-2025)).
  Sirve para una pose **tranquila**, no dramática.
- **2.ª pasada**: el fan ve a Stitch como metáfora universal, «era todos
  los que conozco: buscando aprobación, queriendo ser amado» ⚠️ (cita de
  segunda mano, sin el hilo original).
- **Memes hispanos**: los fandubs del chiste «**¡está tocándome!**»
  (Nani le busca pulgas a Stitch): al menos 4 versiones de distintos
  creadores (Punto 22).

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Separar a Lilo de Nani** o insinuarlo: el final de 2025, en el que
  Nani deja la tutela, fue **lo más criticado** ✅ ([TheWrap](https://www.thewrap.com/lilo-and-stitch-nani-gives-up-lilo-remake/),
  [Slate](https://slate.com/culture/2025/05/lilo-and-stitch-2025-movie-live-action-ending-vs-original-2002-controversy.html),
  [ComicBook](https://comicbook.com/movies/news/lilo-stitch-live-action-changes-nani-backlack-fan-response-criticism/),
  [Cinemablend](https://www.cinemablend.com/movies/as-lilo-and-stitch-remake-receives-backlash-for-its-ending-director-breaks-silence)).
- Poner a **Pleakley sin peluca** si sale disfrazado: el fan lo quiere
  con ella.
- **Mezclar el Stitch de 2002 con el de 2025** en la misma lámina: son
  dos acabados (dibujo en acuarela y 3D con pelo).
- **Stitch con seis patas a la vista** cuando está «de perro»: en la
  Tierra esconde los brazos de más, las antenas y las púas.
- **Hawái de postal**: palmeras de neón, letras de bar tiki, collares
  de plástico. La película mira a los turistas **desde dentro**.
- **Ojos grandes y brillantes de anime** o proporciones estilizadas:
  el estilo Sanders es **pesado abajo y redondo**.
- Lilo **sonriendo dulce** todo el rato: es seria y rara; su sonrisa
  es rara y por eso vale.
- Stitch **hablando mucho**: dice tres palabras.
- Poner la marca de la cámara (Kodak u otra): no está confirmada, y es
  una marca real.
- **2.ª pasada: burlarse de los turistas con saña.** Disney **cortó** la
  escena en que Lilo les hace creer que viene un tsunami (uno le había
  preguntado si «sabe hablar inglés») porque tocaba temas difíciles de
  leer para niños: turismo excesivo, gentrificación, apropiación ✅
  ([Cultura Colectiva](https://culturacolectiva.com/entretenimiento/cine-series/escena-eliminada-lilo-y-stitch/),
  [Sensacine México](https://www.sensacine.com.mx/noticias/noticia-1000146758/)).
  Lilo hace fotos a los turistas con cariño, no para reírse.
- **2.ª pasada: calcar patrones hawaianos** (kapa/tapa, estampados
  tradicionales): son patrones culturales con dueño y no hay ninguno
  CC0 (Punto 19). Dibujarlos a mano mirando fotos de museo, nunca
  calcar.
- **2.ª pasada: dar por hecha a Stitch en Fortnite**: sólo es una
  filtración (Punto 23).
- **2.ª pasada: «Stitch desordena la casa» como idea central**: se
  parece demasiado a Doraemon, que ya tiene biblia (Punto 24).

---

## 15 · Poses analizadas por personaje

> [!note] Cómo leer esta sección
> El **minuto y la frase** salen del subtítulo ✅. La **postura, las
> manos y la mirada** las describo **de memoria** ⚠️: abre el fotograma
> de ese minuto en el PC y corrige antes de dibujar.

### Lilo

| Minuto | Momento | Postura, manos, mirada ⚠️ | Sirve para |
|---|---|---|---|
| 00:22:54 | «My camera's full again» | Levanta la cámara con las dos manos, hacia Nani | **Presentar** (la cámara) |
| 00:22:57 | «Aren't they beautiful?» | Señala la pared, mira las fotos con cara de embeleso, susurra | **Presentar** el canal, **celebrar** |
| 00:42:30 | «Elvis Presley was a model citizen» | De pie, con su lista en la mano, seria de maestra | **Explicar** (la lista) |
| 00:42:44 | «Hands on your hips» | Manos en la cadera, enseña el paso | **Explicar** con el cuerpo |
| 00:43:15 | «Hold it like this» | Coloca los dedos de Stitch en el ukelele | **Explicar** paso a paso |
| 00:44:24 | «It's all you! Knock 'em dead!» | Empuja a Stitch al escenario, brazos hacia delante | **Animar** |
| 00:14:25 | «This is Scrump.» | Sentada en el porche, enseña la muñeca | Presentar algo propio |
| 00:15:17 | «Stupidhead!» | Grita desde la acera, puños abajo | **Regañar** |
| 00:23:42 | El deseo en la ventana | Codos en el alféizar, mira al cielo | **Pensar** |
| 01:15:45 | «See this stamp? I own him.» | Enseña el papel, muy seria | Norma seria |

### Stitch

| Minuto | Momento | Postura ⚠️ | Sirve para |
|---|---|---|---|
| 00:01:37 | Presentado en el juicio | Gruñe en su celda, seis extremidades | Nada (demasiado alien) |
| 00:02:23 | «Meega, nala kweesta!» | Se ríe, mueca | Humor |
| 00:40:27 | Escucha el Patito Feo | Sentado, mira el libro | **Pensar** |
| 00:43:40 | Toca el ukelele «expertly» | De pie, ukelele cruzado | **Celebrar** |
| 00:44:30 | Elvis en el escenario | Tupé, traje blanco, micrófono | **Celebrar**, presentar |
| 00:55:31 | «Lost.» en el bosque | Sentado, libro abierto, orejas caídas | Emoción, «Sin editar» |
| 01:14:31 | «My name Stitch.» | De pie, erguido, mira a la Gran Concejal | **Presentar** |
| 01:15:00 | «This is my family» | Junto a Lilo, mano en ella | Foto de familia |
| Créditos | Fotos del final | Posa con la familia | **Posar** para la cámara |

### Nani

| Minuto | Momento | Postura ⚠️ | Sirve para |
|---|---|---|---|
| 00:15:29 | «Lilo! Open the door» | Golpea la puerta, frustrada | **Regañar** |
| 00:21:19 | «Go to your room!» | Señala, brazo estirado | **Regañar** |
| 00:21:42 | Trae pizza a Lilo | Se agacha, voz baja | Consolar |
| 00:36:13 | «'Ohana means family» | Cede, suspira | Norma con cariño |
| 00:43:07 | «I am all about coffee» | Sonrisa forzada de entrevista | Humor |
| 00:46 | Surf | En la tabla, riendo | **Celebrar** |
| 00:52:51 | «Aloha ʻOe» | En la hamaca con Lilo | Ternura |

### Jumba

| Minuto | Momento | Postura ⚠️ | Sirve para |
|---|---|---|---|
| 00:01:28 | Presenta a 626 | Brazos abiertos, orgulloso | **Presentar** (feria de ciencias) |
| 00:02:37 | «Evil genius!» | Dedo arriba, pecho fuera | Humor |
| 00:39:35 | «6-2-6 was designed to be a monster» | Observa de lejos con Pleakley | **Pensar**, analizar |
| 01:00:44 | «I'll put you back together» | Con herramientas | Detrás de cámara |

### Pleakley

| Minuto | Momento | Postura ⚠️ | Sirve para |
|---|---|---|---|
| 00:07:39 | «Agent Pleakley at your service» | Firme, saludo | **Presentar** |
| 00:07:45 | Explica la Tierra | Señala el holograma | **Explicar** |
| 00:38:40 | «I'm pretty!» | Con peluca, mano en la cadera | Humor |
| 00:38:44 | El mosquito | Quieto, mira su brazo embelesado | **Naturaleza, macro** |

### 15.1 Poses vistas en vídeo (Nuevo, 2.ª pasada) ✅

Éstas **sí están miradas** en el fotograma (partes de vídeo y de voz),
con minuto y enlace de cada vídeo. Las de arriba siguen siendo de
memoria ⚠️ salvo las que coinciden con éstas.

| Personaje | Vídeo y minuto | Postura, manos, mirada | Sirve para |
|---|---|---|---|
| Lilo | película, [14:35](https://archive.org/details/lilo-stitch-2002_202609?t=875) | Enseña a Scrump de camino a la escuela, sonrisa torcida, un ojo entornado | **Presentar** algo suyo, con timidez |
| Lilo | película, [22:10](https://archive.org/details/lilo-stitch-2002_202609?t=1330) | Sentada en la cama, abraza el peluche verde, mirada baja a la pared de fotos | **Pensar**, tono triste |
| Lilo | película, [36:56](https://archive.org/details/lilo-stitch-2002_202609?t=2216) | Sonríe de lado, ceño relajado, mira a Stitch en su caja | **Animar** con cariño |
| Lilo | luau, [0:36](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p?t=36)-1:12 | Sentada a la mesa, libro abierto compartido con Stitch | **Explicar**, textos largos |
| Lilo | tráiler 2002, [1:24](https://archive.org/details/LiloStitchTrailer?t=84) | Silueta contra luz azul, brazo alzado, boca abierta | Miedo, susto |
| Stitch | tráiler 2002, [0:36](https://archive.org/details/LiloStitchTrailer?t=36) | Encogido tras una malla verde azulada, cuerpo bajo, mira a cámara | Vulnerable; «Sin editar» |
| Stitch | tráiler 2002, [1:36](https://archive.org/details/LiloStitchTrailer?t=96)-1:42 | Sentado a la mesa con Lilo, come con cubiertos | **Pensar**, en familia |
| Stitch | tráiler 2002, [2:06](https://archive.org/details/LiloStitchTrailer?t=126) | De pie junto a un tocadiscos verde con Lilo, los dos animados | **Celebrar**, bailar |
| Stitch | créditos, [1:20](https://archive.org/details/lilo-stitch-3?t=80) | Sentado solo en la esquina de una foto de familia ajena, fuera del marco | **Colarse**, el gag del canal |
| Stitch | película, [38:00](https://archive.org/details/lilo-stitch-2002_202609?t=2280) | A oscuras, construye una maqueta de ciudad | **Pensar**, crear |
| Stitch | película, [55:27](https://archive.org/details/lilo-stitch-2002_202609?t=3327) | Sentado de noche con el libro, orejas caídas, mano en la barbilla | Emoción; confirma la fila 00:55:31 de arriba |
| Stitch | tráiler 2025, [1:44](https://www.dailymotion.com/video/x9fzrlk?start=104) | Sobre la tabla, cuerpo bajo, orejas atrás por el viento | **Celebrar**, acción (sólo 2025) |
| Nani | luau, [0:48](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p?t=48)-1:00 | De pie, bandeja en una mano, sirviendo; vestido verde jade de tirantes, flor en el pelo | **Presentar**, servir |
| Nani | tráiler 2002, [2:12](https://archive.org/details/LiloStitchTrailer?t=132) | Entra corriendo, boca y ojos muy abiertos, un brazo hacia Stitch | **Regañar**, sorpresa |
| Nani | película, [20:50](https://archive.org/details/lilo-stitch-2002_202609?t=1250) | Arrastra a Lilo del brazo hacia casa | **Regañar** (confirma 00:21:19) |
| Jumba y Pleakley | película, [28:37](https://archive.org/details/lilo-stitch-2002_202609?t=1717) | Agachados entre arbustos, ojos muy abiertos | Espiar, miedo cómico |
| Jumba y Pleakley | película, [38:40](https://archive.org/details/lilo-stitch-2002_202609?t=2320) | Ríen con los brazos arriba, de noche, con aparatos | **Celebrar** |
| Pleakley | película, [39:00](https://archive.org/details/lilo-stitch-2002_202609?t=2340) | De perfil, sonrisa traviesa, lleno de mosquitos | Naturaleza, humor (confirma 00:38:44) |

- **Cuál para qué**: presentar → Lilo con Scrump (14:35) o Nani con la
  bandeja; explicar → Lilo y Stitch con el libro en el luau; celebrar →
  el tocadiscos (2:06) o Jumba y Pleakley (38:40); regañar → Nani (2:12
  o 20:50); pensar → Stitch con la maqueta (38:00); animar → Lilo sonriendo
  a Stitch (36:56).
- **Faltan en vídeo** ⚠️: la lista de Elvis (00:42), el ukelele (00:43)
  y el Stitch-Elvis (00:44): no se encontraron clips; siguen de memoria.

---

## 16 · Vestuario

| Personaje | Ropa icónica | Otras | Estado |
|---|---|---|---|
| **Lilo** | **Muumuu rojo con hojas blancas**, sandalias azules | En la serie, muumuu verde claro con las mismas hojas; traje de hula con falda de hojas ⚠️ | ✅ la ropa ([wiki](https://liloandstitch.fandom.com/wiki/Lilo_Pelekai), [disfraz oficial](https://www.amazon.com/Toddler-Deluxe-Disney-Stitch-Costume/dp/B0C422L9PQ)) |
| **Nani** | **Top corto coral con corazón rosa**, shorts vaqueros, calcetines blancos, botas marrones | Tops verde azulado, azul oscuro, blanco; tirantes azul polvo con pantalón caqui | ✅ un resumen de la wiki; ⚠️ colores exactos |
| **Stitch** | Azul lavanda, sin ropa | **Traje de Elvis** (00:44); **traje espacial rojo** del principio ✅ ([KH Wiki](https://www.khwiki.com/Stitch)) | ✅ |
| **Pleakley** | Disfraz de mujer: **peluca, vestido, sombrero** ⚠️ | Uniforme de la Federación | ✅ la peluca |
| **Jumba** | Ropa de turista con camisa hawaiana ⚠️ | Mono de preso al principio ⚠️ | ⚠️ |
| **Cobra Bubbles** | Traje negro, gafas negras, pendiente ⚠️ | — | ⚠️ |
| **David** | Bañador y camisa suelta ⚠️; bailarín de fuego en el luau ⚠️ | — | ⚠️ |

### 16.1 Colores medidos y ropa vista (Nuevo, 2.ª pasada)

La parte de imagen midió con Pillow (`getpixel`, puntos concretos) en
imágenes oficiales que **miró**; la de vídeo describió la ropa vista en
los fotogramas.

| Personaje y prenda | Hex medido | De dónde | Estado |
|---|---|---|---|
| Stitch, pelaje (sombra → luz) | `#003D63` → `#167DB1` | key visual «promo art 2», 3523×5000 (luz de atardecer, pintado con degradado) | ✅ la familia de azul; el tono **plano** del cel sigue sin medir ⚠️ |
| Stitch, pecho claro | `#B4FEF1` | traje de Disney on Ice («DOI - Jumba, Stitch & Pleakley.jpg», 3607×2400) | ⚠️ una fuente, luz de espectáculo |
| Stitch, traje espacial rojo | estrella o triángulo del pecho `#F9E03E`; el rojo sale granate `#680004` con luz de escenario; cinturón negro con ribete dorado | Disney on Ice | ⚠️ para pintar, un rojo saturado entre `#CC1F1F` y `#E4241F` (**sin medir**, sólo orientación): comprobar en un fotograma |
| Lilo, falda de hula (hojas de ti) | `#559B73` claro · `#146243` pliegues | key visual | ✅ |
| Lilo, pelo | `#030308`, casi negro puro | key visual | ✅ |
| Lilo, traje de baño | franjas diagonales `#7A1030` rojo y `#8F5030` naranja | fotograma limpio «Nani, Lilo, and Stitch enjoying a big wave», 3000×1782 | ✅ otra variante, no el muumuu |
| Nani, traje de baño | franjas diagonales `#1B2C52` azul marino y `#4F7350` verde, sobre agua turquesa | mismo fotograma | ✅ otra variante, no el top coral |
| Nani, uniforme del luau | vestido **verde jade de tirantes** y flor en el pelo (sin hex) | [clip del luau, 0:48](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p?t=48) | ✅ visto |
| Pleakley, su cuerpo real (sin disfraz) | amarillo `#F8FD3E` a `#EF870E` según la luz; uniforme azul con hombrera naranja | Disney on Ice | ✅ es su traje de alienígena de un ojo, canon, distinto del disfraz de mujer |
| Jumba | camisa **amarilla con estampado rojo** (sin hex) | vista en hoja 2, n.º 53 y 90-91 (*Stitch! The Movie*) y hoja 3, n.º 539 (personaje de parque) | ⚠️ sin medir; de la secuela y del parque, no de 2002 |
| Cobra Bubbles | traje negro y gafas negras (sin hex) | visto en hoja 2, n.º 88 (*Stitch! The Movie*) | ⚠️ sin medir |
| David | — | — | ⚠️ sin imagen limpia |

- **Nota de método** (parte de imagen): key visual y Disney on Ice no
  son un fotograma plano. Para hex 100 % fieles al cel, sacar un
  fotograma de la película con `fotogramas.py` y medir ahí. Queda como
  pendiente menor: ya hay dos fuentes de color por prenda en Stitch,
  Lilo y Nani.
- **El vestuario cambia por escena** ✅: Lilo lleva muumuu rojo, traje de
  hula y bañador de franjas; Nani, top coral, uniforme verde del luau y
  bañador de franjas.

---

## 17 · Paisajes y fondos de pantalla

- **Sitios y su luz**: §5.
- **Kauai real** para fotos de fondo (hay que buscarlas con licencia
  libre): **Hanapepe** y su puente colgante; **Nā Pali** y **Kalalau**;
  **Hanalei** ✅ que existen (§5.1).
- ~~Fondos de pantalla oficiales en alta: no encontré ninguno~~ →
  **corregido en la 2.ª pasada**: sí hay; la red cerrada no dejaba
  verlos.
- Fan art: §4.3.

### 17.1 Fondos oficiales (Nuevo, 2.ª pasada) ✅

Tamaño real medido por la API `imageinfo` de la wiki de Disney.

| Fondo | Tamaño | Qué es |
|---|---|---|
| [Stitch! The Movie promo wallpaper](https://static.wikia.nocookie.net/disney/images/6/66/Stitch%21_The_Movie_promo_wallpaper.jpg) | **3000×1535** | promocional oficial de *Stitch! The Movie* (2003); hoja 1, n.º 24 |
| [Stitch experiments wallpaper](https://static.wikia.nocookie.net/disney/images/6/66/Stitch_experiments_wallpaper.jpg) | **1575×1093** | todos los experimentos como papel pintado |
| [Motto! Stitch! DS](https://static.wikia.nocookie.net/disney/images/5/54/Motto%21_Stitch%21_DS_wallpaper.jpg) | 1280×1024 | web japonesa de Disney, juego de DS |
| [Stitch! DS - Ohana to Rhythm de Daibouken](https://static.wikia.nocookie.net/disney/images/8/87/Stitch%21_DS_-_Ohana_to_Rhythm_de_Daibouken_wallpaper.jpg) | 1280×1024 | juego de ritmo de DS |
| [Stitch! Good Deed Counter](https://static.wikia.nocookie.net/disney/images/d/da/Stitch%21_Good_Deed_Counter_wallpaper.jpg) | 1280×1024 | anime *Stitch!* |
| [Stitch and Angel in kimonos](https://static.wikia.nocookie.net/disney/images/8/86/Stitch_and_Angel_in_kimonos_wallpaper.jpg) | 1280×1024 | Stitch y Angel en kimono |
| [Stitch painted Japanese](https://static.wikia.nocookie.net/disney/images/4/45/Stitch_painted_Japanese_wallpaper.jpg) | 1280×1024 | pincelada de pintura japonesa |
| [Tenugui Stitch](https://static.wikia.nocookie.net/disney/images/a/a6/Tenugui_Stitch_wallpaper.jpg) | 1280×1024 | motivo de *tenugui* (toalla japonesa estampada) |

Los seis japoneses (2008-2015) enseñan un **estilo pictórico japonés**
(kimono, *tenugui*, pincel) que no estaba en la biblia.

### 17.2 Fondos de fans en alta (Wallhaven, con autor) ✅

Tamaño y autor que da Wallhaven (juntados por `recolectar.py`). Sólo
referencia: el © es de sus autores y de Disney.

| Fondo | Tamaño | Autor u origen |
|---|---|---|
| [playa con Stitch](https://w.wallhaven.cc/full/we/wallhaven-wez757.jpg) | 5120×2880 | subido por AronDark, sin origen |
| [Stitch 3D, serie de 5](https://w.wallhaven.cc/full/gp/wallhaven-gpolge.jpg) ([2](https://w.wallhaven.cc/full/vq/wallhaven-vqwrl3.jpg), [3](https://w.wallhaven.cc/full/yx/wallhaven-yxyrod.jpg), [4](https://w.wallhaven.cc/full/5g/wallhaven-5g28o8.jpg), [5](https://w.wallhaven.cc/full/l8/wallhaven-l857pp.jpg)) | 3840×2160 | **Juan Hernández**, [ArtStation](https://www.artstation.com/artwork/4NP6o4) |
| [interior, cuarto](https://w.wallhaven.cc/full/yq/wallhaven-yq8grx.jpg) · [mujer en el cuarto](https://w.wallhaven.cc/full/5y/wallhaven-5y7k87.jpg) | 3840×1655 | **Mauger Baptiste**, [ArtStation](https://www.artstation.com/maugerbaptiste3) |
| [Stitch y Loki](https://w.wallhaven.cc/full/e8/wallhaven-e8zwzl.jpg) | 1920×1799 | **Ognjen Sporin**, [ArtStation](https://www.artstation.com/artwork/RyJZze) |
| [Stitch y Desdentao](https://w.wallhaven.cc/full/4y/wallhaven-4ypleg.jpg) | 1920×1080 | **tsaoshin**, [DeviantArt](https://www.deviantart.com/tsaoshin/art/Stitch-and-Toothless-453739840) |
| [pixel art azul](https://w.wallhaven.cc/full/gj/wallhaven-gjy6j7.png) · [pixel art 2](https://w.wallhaven.cc/full/yj/wallhaven-yj9mkl.png) | 1920×1080 | AceAtomz · teddyklad, sin origen |

- **Kauai real con licencia libre**: la parte de imagen pidió fotos de
  Hanapepe a Wikimedia Commons y dio **429**; no se insistió ⚠️. Las
  fotos de Flickr que sí hay son de parques (Punto 23).

---

## 18 · Guía para generar con IA (Firefly, Canva)

> [!warning] Antes de nada
> Firefly y Canva suelen **negarse a dibujar personajes con marca**
> (Disney) o los deforman ⚠️ (lo sé por uso general, no lo probé aquí).
> Úsalas **para fondos, objetos y luz**. Los personajes, de **fotogramas
> o arte oficial** recortados con `v3/integrar.py`.

### 18.1 El estilo en una frase

Animación 2D a mano de Disney, 2002, estilo **Chris Sanders**: formas
**redondas, blandas y pesadas abajo**, sin esquinas, «como un saco de
harina» ✅ (así lo resume [IndieWire](https://www.indiewire.com/features/craft/lilo-stitch-live-action-remake-dean-fleischer-camp-vfx-1235129089/), sobre cómo el remake siguió el «manual» de Sanders; no sé quién dice la frase).
Fondos **en acuarela de verdad**, con bordes de agua y papel que se ve ✅.

### 18.2 Reglas de la guía «Surfing the Sanders Style» ✅

([Scribd](https://www.scribd.com/document/552265347/Lilo-Stitch-Style-Guide-by-Sue-Nichols-Maciorowski), resumen del buscador)
- **Una sola forma simple** para cada pose.
- **La «ola»**: una curva suave en cuello, ojo, brazo y antebrazo que
  echa el peso hacia delante o hacia el suelo.
- **Las manos como patas** de animal, con peso.
- El torso con **tripa hacia arriba**, como una bolsa, sin parecer gordo.

### 18.3 Rasgos que nunca cambian (1.ª pasada de memoria; 2.ª pasada vistos, §18.7)

- **Stitch**: azul lavanda; orejas enormes, rosas por dentro, con
  muescas; ojos negros grandes; nariz ancha azul marino; boca de lado a
  lado; en la Tierra, **dos brazos y dos piernas** a la vista (anda a
  cuatro patas); el otro par de brazos, las antenas y las púas, escondidos.
- **Lilo**: pelo negro largo y liso; piel morena; cabeza grande y
  redonda; **muumuu rojo con hojas blancas**; descalza o sandalias.
- **Nani**: pelo negro largo; top coral; shorts vaqueros.
- **Pleakley**: verde, un ojo, antena; con peluca y vestido si está
  disfrazado.
- **Jumba**: grande, morado, varios ojos ⚠️.

### 18.4 Paleta, línea, luz y encuadre

- **Paleta**: §5.4 (propuesta sin medir).
- **Línea**: fina y oscura en personajes; **sin línea** en los fondos,
  que son manchas de acuarela.
- **Sombreado**: una sombra plana en personajes; degradados de agua en
  fondos.
- **Luz**: sol tropical suave; atardeceres cálidos; noches **azules**,
  nunca negras.
- **Encuadre**: cámara baja, a la altura de una niña.

### 18.5 Palabras que ayudan y palabras que lo estropean

- **Ayudan**: `hand-painted watercolor background`, `2002 hand-drawn
  animation`, `soft rounded shapes`, `Kauai plantation town`, `wooden
  house with peeling paint`, `golden hour`, `warm lamp light`, `photo
  prints with white borders pinned to a wall`, `masking tape`,
  `cork board`.
- **Estropean**: `3D`, `Pixar`, `anime`, `chibi`, `kawaii`, `neon`,
  `tiki bar`, `photorealistic`, `hyper-detailed`, `live action`,
  `glossy`.

### 18.6 Qué referencias usar

| Para | Usar |
|---|---|
| Estilo de fondo | [Andreas Deja: fondos en acuarela](http://andreasdeja.blogspot.com/2016/10/watercolor-backgrounds.html), [AV Club](https://www.avclub.com/read-this-lilo-stitch-disney-watercolor-animation-1849681724) |
| Estilo de personaje | guía de Sue Nichols (§18.2), [hojas de modelo](https://afterhoursanimationschool.tumblr.com/post/142262804364/lilo-and-stitch-model-sheets-part-2) |
| Cómo son las fotos | [pins de los créditos](https://pinandpop.com/series/lilo-stitch-end-credits-snapshot-photos), [final con «Burning Love»](https://www.youtube.com/watch?v=r4aor3FulOU) |
| Pose de Lilo con cámara | fotograma 00:22:54 a 00:22:57 |
| Pose de Stitch | fotogramas de §15; modelos 3D de §4.2 para girar |

### 18.7 IA de imagen, puesta al día (Nuevo, 2.ª pasada)

**Correcciones a lo de arriba**, con lo que ya se ha visto y medido:

- **Rasgos fijos, ahora vistos** en las hojas y fotogramas: Stitch azul
  con **orejas que dicen la emoción** (arriba, alerta o contento;
  caídas, triste, [55:27](https://archive.org/details/lilo-stitch-2002_202609?t=3327));
  Lilo con pelo casi negro `#030308` y cabeza grande y redonda; Nani con
  su top coral o el vestido verde jade del luau; Pleakley de un ojo y
  antena, verde lima amarillento (hoja 2, n.º 84-87); Jumba **morado**
  (hoja 2, n.º 90-91). Cuántos ojos tiene Jumba: sin contar ⚠️.
- **Paleta**: usa la **medida** (§5.4b y §16.1), no la propuesta de §5.4.
  Noche de interior morada y roja (`#432626`, `#62414D`, `#6A1B1B`), no
  azul; luau cálido de fuego (`#8D4232`, `#813B2D`).
- **Línea y sombreado** (entrevistas del Punto 18): personaje **plano por
  dentro**, línea de tinta con temblor, formas «chubbed up» (infladas),
  sin esquinas ni rectas; **toda la textura en el fondo**. **Nunca blanco
  puro**: la luz es el papel crema.
- **Luz**: cálida de lámpara o antorcha dentro; atardecer dorado fuera;
  luna azul para lo triste. Detrás del personaje, una fuente de luz
  cálida (antorchas del luau) para que no quede plano.
- **Encuadre**: decidido como en *storyboard*: miniatura primero, cámara
  baja a la altura de Lilo.

**Plantilla de *prompt*** (para fondos y objetos; los personajes, de
arte oficial o fotograma):
`hand-painted watercolor background, 2002 Disney hand-drawn animation,
soft rounded shapes, no white paint, paper grain, coarse salt texture on
lava rocks, wooden plantation house in Kauai at golden hour, a photo
album and a film camera on a table, photo prints with white borders
taped at angles, warm lamp light, low camera`.

**Palabras que ayudan, nuevas**: `watercolor granulation`, `paper
white as light`, `chubby rounded silhouettes`, `weighted to the ground`,
`taped snapshots on blue background` (el *collage* de los créditos),
`tiki torches warm light`, `droopy ears`, `lopsided smile`,
`bared teeth`.
**Estropean, nuevas**: `sharp angles`, `vector clean lines`,
`white highlights`, `glossy fur` (eso es el Stitch de 2025),
`kawaii sparkles`, `sweat drop`, `chibi`.

**Vocabulario de gestos** (no es anime: no hay gotas de sudor, ni fondos
de emoción, ni *chibi* en la película; si la IA los pone, está mal):

| Emoción | Cómo se ve en esta película | Imagen de referencia |
|---|---|---|
| Alegría | boca muy abierta, carcajada, cuerpo echado atrás | [cohete, 31:44](https://archive.org/details/lilo-stitch-2002_202609?t=1904) |
| Cariño | sonrisa de lado, ceño relajado | [Lilo, 36:56](https://archive.org/details/lilo-stitch-2002_202609?t=2216) |
| Rabia | dientes enseñados, ojos entornados, gruñido | [Stitch, 2:25](https://archive.org/details/lilo-stitch-2002_202609?t=145) |
| Tristeza | orejas caídas, mano en la barbilla, mirada baja | [Stitch, 55:27](https://archive.org/details/lilo-stitch-2002_202609?t=3327) |
| Vergüenza | sonrisa torcida, un ojo entornado | [Lilo, 14:35](https://archive.org/details/lilo-stitch-2002_202609?t=875) |
| Miedo | ojos como platos, boca apretada, agachado | [Jumba y Pleakley, 28:37](https://archive.org/details/lilo-stitch-2002_202609?t=1717) |

**Referencias de estilo y de pose** (las mejores de `referencias.json`):
luz y color → key visual «promo art 2» (3523×5000); proporciones →
hoja de modelo de Pleakley (2048×1319) y arte de desarrollo de Stitch
(3338×2160); poses de Lilo → «LiloHulaAD» y «LiloStudyAD»; color plano
→ el fotograma «big wave» (3000×1782); el álbum → créditos a
[1:20](https://archive.org/details/lilo-stitch-3?t=80); caras → §8.2.

### 18.8 IA de texto: cómo escribir en su voz (Nuevo, 2.ª pasada)

**Reglas por personaje** (de los subtítulos con minuto de §7.2 y del
doblaje de §10):

- **Lilo**: frases cortas y **muy serias**, con lógica propia; explica
  con **listas numeradas** («Número uno…»); lo que ama lo **susurra**
  (puntos suspensivos); se enfada con un insulto de niña y un portazo.
  Nada de diminutivos cursis.
- **Stitch**: **una a tres palabras**, sin artículos ni verbos («My name
  Stitch»); ríe a carcajadas de loco; gruñe; de vez en cuando su idioma
  («¡Meega, nala kweesta!»). En latino de 2002 sólo dice frases cortas
  en español («Hola», «Así me gusta», «Tierno y esponjoso») ⚠️ una fuente.
- **Nani**: órdenes secas con exclamación («Go to your room!»); cuando se
  ablanda, **voz baja y preguntas** («We're a broken family, aren't
  we?»). Sarcasmo cuando está cansada.
- **Jumba**: fino y teatral, **sin artículos**, orgulloso («prefiero que
  me llamen genio malvado»).
- **Pleakley**: pedante y chillón, **dato de «experto en la Tierra»** y
  pánico por nada; se maravilla con cualquier bicho.

**Frases reales por emoción** (inglés con minuto de la película; las
latinas documentadas, marcadas):

| Emoción | Frases |
|---|---|
| **Alegre** | Lilo: «A falling star!» (00:23:10) · Stitch: «I like fluffy!» (01:00:46) · Pleakley, de un mosquito: «She's so beautiful» (00:38:48) |
| **Enfadado** | Lilo: «Stupidhead!» (00:15:17) · Nani: «Go to your room!» (00:21:19) · Stitch: «Meega, nala kweesta!» (00:02:23) |
| **Explicando** | Lilo: «Elvis Presley was a model citizen. I've compiled a list of his traits for you to practice. Number one is dancing.» (00:42:30-00:42:36) · «Hold it like this, and put your fingers here.» (00:43:15) · Pleakley: «Earth is a protected wildlife reserve» (00:07:23) |
| **Animando** | Lilo: «It's all you! Knock 'em dead!» (00:44:24) · David: «There's no better cure for a sour face than a couple of boards and some choice waves» (00:45:52) · Nani: «Sometimes you try your hardest but things don't work out the way you want them to…» (00:58:54) |
| **Triste** | Stitch: «Lost.» «I'm lost.» (00:55:31, 00:55:41) · Lilo: «I remember everyone that leaves.» (00:54:57) · Nani: «We're a broken family, aren't we?» (00:21:46) |
| **Familia (latino ✅)** | «Ohana significa familia, y tu familia nunca te abandona ni te olvida» · Stitch: «Esta es mi familia, la encontré, estaba aquí. Es chiquita y rota, pero es buena» (§10.3) |

- **Vocabulario del mundo** para que suene a la serie: *ohana*,
  *kuleana* (responsabilidad), *mālama ʻāina* (cuidar la tierra), «626»,
  «primos» (los otros experimentos), «Federación Galáctica», «Gran
  Concejal», «Pato el pez» (así se llama Pudge en latino).
- **Puntuación**: ¡! en las órdenes de Nani y en los gritos de Pleakley;
  «…» en los susurros de Lilo; Stitch sin puntuación compleja.
- **No inventar** frases latinas: sólo las dos con ✅ son textuales del
  doblaje. «¡Mi cámara está llena otra vez!» es una **adaptación** ⚠️.

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo (2.ª pasada)

No existía en la 1.ª pasada. Sale de la parte de texto, con entrevistas
de producción.

### Cómo se hizo de verdad

- **Fondos en acuarela, no gouache**: la primera de Disney desde *Dumbo*;
  *La Sirenita*, *Aladdín*, *El Rey León* y *La Bella y la Bestia* se
  pintaron en gouache opaco ✅ ([AV Club](https://www.avclub.com/read-this-lilo-stitch-disney-watercolor-animation-1849681724),
  [Animation Obsessive](https://animationobsessive.substack.com/p/the-shape-and-color-of-lilo-and-stitch)).
- El director de arte **Ric Sluiter** propuso la acuarela; tuvieron que
  redescubrirla (los pigmentos y papeles de los 40 ya no existían): **7
  meses de talleres**, pintando al aire libre casi a diario. Sólo **Peter
  Moehrle**, de 8-9 fondistas, sabía acuarela, y enseñó al resto ✅ (AV
  Club).
- **Maurice Noble**, veterano de los 40-50, les dio el truco de la **sal
  marina gruesa** sobre la pintura húmeda para las rocas de lava ✅ (AV
  Club, Animation Obsessive).
- **David Wang** mezclaba el pigmento con **mucha agua en un platito
  aparte**: el pigmento grueso se posa en el papel y da grano ✅
  (Animation Obsessive).
- **Cita de Sluiter**: «*We didn't use any white paint, which tends to
  kill a color, and instead we allowed the white of the paper to act as
  a light*» ✅ (Animation Obsessive). Nada de blanco: la luz es el papel.
- **Personajes**, otra vez Sluiter: «*soft, rounded shapes, suggestive
  of little loaves of home-baked bread… chubbed up*»; **Byron Howard**:
  «*no hard edges, no straight lines*»; **Sue Nichols**: cada pose es
  **una sola forma**, «*weighted to the earth*»; **Paul Felix**: «*mood
  and basic shapes*», sin texturas ni luces complicadas en el personaje
  ✅ (Animation Obsessive).
- Estudio de **Disney en Orlando (Florida)**, unos **350** animadores y
  fondistas, entre ellos **William Silvers** y **Barry Kooser** ✅ (AV
  Club, [Wikipedia, William Silvers](https://en.wikipedia.org/wiki/William_Silvers)).
- ***Storyboard*** con luz y encuadre ya decididos, que pasaban «casi
  exactamente» a pantalla; **Dean DeBlois**: «*composition and lighting
  are vital in storytelling*» ✅ ([AWN, Revisited Part I](https://www.awn.com/animationworld/lilo-stitch-revisited-part-i)).
- Tras el **11-S** se cambió el final: rascacielos → **cañones de
  montaña**, avión 747 → **nave espacial** ✅ (AWN).
- Chris Sanders miraba revistas de fauna, **nutrias marinas**, para los
  gestos de Stitch ✅ ([AWN](https://www.awn.com/animationworld/lilo-toothless-and-totoro-too)).
- **No encontrado** ⚠️: el nombre del programa de tinta y color digital
  (CAPS se estaba dejando); las fuentes sólo dicen «coloreado
  digitalmente».

### Cómo replicarlo en Photoshop

1. **Nunca pintes blanco puro como luz**: capa de papel crema (no
   `#FFFFFF`) y máscaras para **revelar** el papel.
2. Pinceles de acuarela con **bordes húmedos** (los de Kyle T. Webster
   que trae Photoshop) para el pigmento acumulado en el borde.
3. **El truco de la sal**: pincel granulado, o textura CC0 de roca de
   [ambientCG](https://ambientcg.com/api/v2/full_json?type=Material&q=rock)
   en Multiplicar, sólo en rocas y lava.
4. **Grano de papel** bajo la línea, en Multiplicar o Superponer suave.
5. **Línea de tinta con temblor**, nunca vectorial; siluetas redondas e
   infladas, sin ángulos rectos.
6. **Personaje plano por dentro**; el detalle, en el fondo (regla de
   Paul Felix). Es lo que evita que parezca «hecho por IA».
7. **Grano final** muy suave y 1-2 px de aberración cromática, para el
   aire de copia de cine de 2002.
8. **Recortes** de personajes: siempre por `v3/integrar.py` (regla 3 del
   dueño).

### Cómo replicarlo en Blender

1. **Contorno**: Freestyle sobre formas redondas, o Solidify con normales
   invertidas; grosor bastante uniforme y algo suave.
2. **Sombreado**: *Shader to RGB* → *ColorRamp* de 2-3 escalones, sin
   especular.
3. **El fondo lleva la textura**: imágenes pintadas en acuarela como
   textura del *set*; para la lava, *bump* con ruido Voronoi grueso
   imitando la sal.
4. **Rigs libres** (CC Attribution por API): Stitch 626 de werasik2aa1,
   Stitch KH3 de guinavarro.al, Pleakley de ArbitraryCanary (260 220
   caras: cuidado con el PC, regla 9) y Nani de werasik2aa1 (§4.2). **No
   hay rig libre de Lilo ni de Jumba** ⚠️.
5. **Objetos** (CC BY por API): álbum de mnaglak, corcho de rickmaolly,
   Canon AE-1 de Marc Sawyer (§4.1).
6. **Tutoriales** genéricos del método: [cel shader, TipTut](https://www.youtube.com/watch?v=rHeMWkfMpME),
   [Grease Pencil, Kevandram](https://www.classcentral.com/course/youtube-blender-grease-pencil-beginner-tutorial-2d-3d-toon-shaded-scene-part-2-2-133917).

### Encuadres y composición

- **Todo se decide en miniatura** antes de pintar: dónde va el
  personaje, el texto y la luz (así trabajaba el equipo de DeBlois).
- **Personaje limpio y plano, fondo con toda la textura**: si Lilo o
  Stitch van delante de un fondo con detalle, el personaje se queda
  simple para no competir.
- Cómo se enmarca cada emoción, en lo visto: **tristeza** en plano
  cerrado, luz de luna y silencio (55:27); **alegría** en plano medio con
  los dos personajes juntos (31:44); **susto** en plano general, con el
  personaje entrando por un lado (tráiler, 2:12).

---

## Punto 19 · Texturas 2D (2.ª pasada)

Junto con §4.4 (3D y HDRI) y §5.5 (texturas reales), para que no falte
ninguna capa.

- **Emblema de Stitch**: la estrella o triángulo dorado `#F9E03E` del
  pecho de su traje espacial, con cinturón negro de ribete dorado. Sale
  igual en Funko, Disney Infinity y el traje de Disney on Ice ✅ (tres
  fuentes). Sirve de **sello o pin** en una esquina del álbum.
- **Estampado del vestido de Lilo** (hojas blancas sobre rojo) repetido
  como patrón: las mochilas **Loungefly** lo usan ✅
  ([Disney Store](https://www.disneystore.com/lilo-stitch-loungefly-mini-backpack-442090260726.html),
  [BoxLunch](https://www.boxlunch.com/brands/loungefly/lilo-stitch/)).
  Con ©: para mirar, no para calcar. Idea: el borde de una foto tipo
  Polaroid.
- **Camisa hawaiana** (la de Jumba de turista): no hay textura libre ya
  hecha. Base CC0: telas lisas `Fabric030`, `Fabric061`, `Fabric083` de
  [ambientCG](https://ambientcg.com/list?type=Material&q=fabric), y el
  estampado pintado a mano encima ✅ la base, ⚠️ el estampado.
- **Tela kapa o tapa hawaiana** (el motivo de la portada de *Greatest
  Hawaiian*, hoja 2, n.º 72): **ninguna CC0**; sólo fotos de museo sin
  licencia de descarga ([Kapa Hawaii](https://kapaiastitchery.com/hawaiian-quilting-history/),
  [RISD Museum](https://risdmuseum.org/exhibitions-events/exhibitions/pacific-islands-tapa-cloth)) ⚠️.
  Son patrones culturales con dueño: dibujarlos a mano, nunca calcar.
- **Patrón infinito de Disney**: el puzle «Stitch and Experiments»,
  2137×1000, con Stitch y más de 100 experimentos repetidos
  ([imagen](https://static.wikia.nocookie.net/disney/images/2/29/Stitch_and_Experiments_puzzle.jpg); hoja 2, n.º 81) y el
  fondo «Stitch experiments wallpaper» (§17.1) ✅.
- **Motivos japoneses oficiales**: *tenugui* y pincelada japonesa en los
  fondos de §17.1 ✅.
- **El cómic Dynamite no usa tramas**: color digital plano con
  degradados suaves, sin puntos de semitono ✅ (portadas miradas). Si se
  imita el cómic, sin trama.
- **Grano de papel y acuarela**: capa de papel crema y granulación (Punto
  18); sal gruesa en las rocas; roca CC0 de ambientCG.
- **Borde de foto y cinta**: el *collage* de los créditos (fotos de
  borde blanco pegadas en ángulo con cinta sobre azul liso, [1:20](https://archive.org/details/lilo-stitch-3?t=80)) ✅.

---

## Punto 20 · Gustos y detalles de cada personaje (2.ª pasada)

Fuente principal: las fichas «likes/dislikes» de la
[Lilo & Stitch Wiki](https://liloandstitch.fandom.com) (una wiki de fans:
⚠️). Marco ✅ lo que además sale en la película con su minuto.

| Personaje | Le gusta | No le gusta | Fuente |
|---|---|---|---|
| **Lilo** | su *ohana*, Stitch, tener amigos, **Elvis** ✅ (00:40:56), Regis Philbin, el hula, el surf, **hacer fotos a turistas** ✅ (00:22:54) | los abusones, **Mertle**, que Nani la regañe o la sobreproteja, que le griten | ⚠️/✅ [Lilo Pelekai](https://liloandstitch.fandom.com/wiki/Lilo_Pelekai) |
| **Stitch** | divertirse, la *ohana*, sus «primos», Lilo, Angel, **comer, sobre todo pastel de coco, y el café** ✅ (Lilo le da café, 00:36:51), naves, **tortugas** (dibuja dos en los créditos; abraza una de peluche tras una pesadilla) ⚠️ | el agua, la nieve al principio, la soledad y el rechazo, Mertle | ⚠️/✅ [Stitch (626)](https://liloandstitch.fandom.com/wiki/Stitch_(626)) |
| **Nani** | surfear ✅ (00:46:05), Lilo, su familia, **pizza** (trae pizza a Lilo, 00:21:42), el hula, el **chocolate** | la mala suerte, la desobediencia, perder a Lilo, perder el trabajo, gritarle a Lilo, los inventos de Jumba | ⚠️ [Nani Pelekai](https://liloandstitch.fandom.com/wiki/Nani_Pelekai) |
| **Jumba** | crear experimentos «malvados», su propio genio, **«Hound Dog» de Elvis**, su madre, **bailar**; en su planeta los nutrientes se absorben por la piel y masticar le parece molesto, pero acaba cogiéndole gusto a comer | que fallen sus experimentos, que lo arresten, que le llamen «científico idiota», su ex esposa, Mertle | ⚠️ [Jumba Jookiba](https://liloandstitch.fandom.com/wiki/Jumba_Jookiba) (dato de la serie, no de 2002) |
| **Pleakley** | la limpieza, la seguridad, **disfrazarse de mujer** ✅, coser, estudiar la Tierra, **los mosquitos** ✅ (00:38:44) | la suciedad, el peligro, los agujeros negros, que su madre le riña, **su nombre de pila, «Wendy»** | ⚠️/✅ [Wendy Pleakley](https://liloandstitch.fandom.com/wiki/Wendy_Pleakley) |

- **Edad y cumpleaños**: ninguno de los cinco tiene **fecha de
  nacimiento oficial** publicada (no hay campo en las fichas) ⚠️. Lilo
  cumple **7** durante la película (7 velas en el montaje final) ⚠️ un
  wiki. Nani, **18** en la primera película ⚠️ un wiki (§8).
- **Altura**: Stitch mide **alrededor de 1 metro** (3 pies y 6 pulgadas)
  ⚠️ una fuente, [Sideshow](https://www.sideshow.com/blog/disney-learn-about-stitch);
  no hay ficha oficial en centímetros. Del resto, no encontré.
- **El objeto que siempre lleva**: Lilo, su **cámara** (marca sin
  confirmar ⚠️) y **Scrump**; Stitch, el **libro del Patito Feo** cuando
  está triste; Pleakley, su **antena** (le sirve de oído y olfato) y la
  peluca de disfraz; Cobra, sus gafas negras; Jumba, sus herramientas
  (01:00:44).
- **Cómo se ve a sí mismo**: Stitch, «perdido» (00:55:41) hasta que dice
  «es chiquita y rota, pero es buena»; Lilo, alguien a quien todos dejan
  (00:54:57); Jumba, «genio malvado» (00:02:37); Pleakley, guapo («I'm
  pretty!», 00:38:40).

---

## Punto 21 · Por qué la gente la ama (2.ª pasada)

- **La *ohana*, la familia encontrada**, es la razón que más repiten las
  reseñas: familia no es sólo sangre, y eso llega a quien no encaja en la
  suya ✅ ([Box Office Mojo, «'Ohana' Means Family»](https://www.boxofficemojo.com/article/ed2859467780)).
- **Cifras de cariño**: 1.038 millones de dólares de taquilla en 2025 y
  Stitch entre lo más vendido de Disney (más de 4.000 millones en
  productos, §9) ✅.
- **Con quién se identifica el público**: con **Stitch**, por sentirse
  «raro» y no encajar; con **Lilo**, quien fue un niño solo o
  «diferente» ⚠️ (resúmenes de foros, no una encuesta).
- **Representación**: una familia hawaiana de verdad, rota e intentando
  arreglarse tal cual es ✅ (hilo de Reddit citado en
  [gonewith.substack.com](https://gonewith.substack.com/p/lilo-and-stitch-is-the-movie-2025)).

### Las escenas que hacen llorar (y reír)

| Escena | Minuto | Qué pasa y por qué duele | Música y cómo está hecha | Reacción |
|---|---|---|---|---|
| **El Patito Feo, «I'm lost»** | [55:27](https://archive.org/details/lilo-stitch-2002_202609?t=3327)-55:31 (00:55:31 en subtítulo) | Stitch, que sólo destruye, se ve en un pato que no tiene grupo; está solo, de noche | **Sin música**: sólo el bosque. Plano cerrado, luz azul de luna, orejas caídas ✅ visto | es «la escena que te hizo llorar» en TikTok ✅ ([TikTok, búsqueda](https://www.tiktok.com/discover/la-escena-que-hizo-llorar-en-la-pel%C3%ADcula-de-lilo-y-stitch)) |
| **La hamaca, «Aloha ʻOe»** | 00:52:51 | Nani le canta a Lilo sabiendo que se la pueden quitar | **a capela**, sin instrumentos | Reddit: el momento de «representación emocional» ✅ |
| **La pared de fotos y el abrazo** | [22:10](https://archive.org/details/lilo-stitch-2002_202609?t=1330) → 22:55 | Lilo llora con el peluche ante sus fotos; Nani entra y se duermen abrazadas; «I like you better as a sister than a mom» (00:22:06) | cuarto de noche, luz morada y roja ✅ visto | ⚠️ sin comentarios medidos |
| **«Es chiquita y rota, pero es buena»** | 01:15:00 | Stitch presenta a su familia ante la Federación | ✅ subtítulo; latino ✅ (§10.3) | frase de las listas oficiales de Disney Latino ✅ |
| **Ríe: el cohete de monedas** | [31:44](https://archive.org/details/lilo-stitch-2002_202609?t=1904) | Lilo y Stitch a carcajadas | exterior de día ✅ visto | — |
| **Ríe: «Blue punch buggy!»** | 01:01:38 | Lilo pega a Stitch al ver un escarabajo azul | ✅ subtítulo | meme vivo en TikTok (§14) |
| **Ríe: Pleakley y los mosquitos** | [39:00](https://archive.org/details/lilo-stitch-2002_202609?t=2340) | «She's so beautiful» | ✅ visto | «Put Pleakley in the wig, cowards» (§8) |

- **Vídeos de reacción con votos**: no se midieron ⚠️ (YouTube pedía
  iniciar sesión y TikTok no abre desde el servidor).

---

## Punto 22 · Fan dubs y comunidad hispana (2.ª pasada)

Título, canal, vistas y fecha **medidos con `yt-dlp -j`** (sin bajar el
vídeo) ✅:

| Fandub | Canal | Vistas | Fecha y duración |
|---|---|---|---|
| [«Fandub Lilo & Stitch Español Latino. Con participación especial de Saii y Yumi»](https://www.youtube.com/watch?v=kofTIv15aL4) | Dotachin96 | **147 762** | 26-jun-2012 · 9:48 |
| [«Lilo y Stitch ¡ESTÁ TOCANDOME!»](https://www.youtube.com/watch?v=C53YBpJ8I_k) | Lucymar | 512 | 21-oct-2020 · 1:31 |
| [«LILO Y STITCH FANDUB (Doblaje) · Vane Ochoa»](https://www.youtube.com/watch?v=fTEk021IYKQ) | Érase Una Voz | 202 | 22-may-2023 · 1:32 |

- **Meme hispano recurrente**: «¡está tocándome!» (Nani le busca pulgas a
  Stitch). La parte de voz encontró **al menos 4 versiones** de
  distintos creadores ✅. Sirve para un evento de doblaje del servidor.
- **Retos de doblaje con la voz oficial**: el TikTok de SDV con **Anaís
  Portillo** (Lilo 2002) ([enlace](https://www.tiktok.com/@sdv_serviciosdevoz/video/7143761341776497925))
  y otro con Raúl Aldana (§10.1) ✅.
- **Covers en español** de «Hawaiian Roller Coaster Ride» y «He Mele No
  Lilo»: varios, casi todos del estreno de 2025 ✅
  ([ejemplo en YouTube](https://www.youtube.com/watch?v=qcMfcIHcJXk)); vistas
  del cover sin medir (yt-dlp no devolvió datos) ⚠️.
- **Escenas del fandub**: la de Dotachin96 dura 9:48 (varias escenas);
  qué escena exacta dobla cada uno, sin anotar ⚠️.
- **No encontré** parodias o memes hispanos grandes como «Ohana» o
  «blue punch buggy» en inglés ⚠️ (puede existir; búsquedas en español e
  inglés en la bitácora).

---

## Punto 23 · Colaboraciones y cruces (2.ª pasada)

Su arte trae **poses y ropa nuevas**. Las imágenes vistas llevan su
número de hoja.

### Juegos y cartas

- **Disney Lorcana** (cartas, Ravensburger): set precon «Lilo & Stitch»
  (enero de 2026). Nani en tinta Ámbar; Stitch en varias, entre ellas
  **«Stitch — Covert Agent»**, n.º 89/204, tinta Esmeralda: pose de
  **espía** ✅ ([Lorcana Player](https://lorcanaplayer.com/card/stitch-covert-agent/),
  [Dreamborn.ink](https://dreamborn.ink/decks/khfanjJj1HSJ3eTO0Yny)).
  Vistas en la hoja 3: **Lilo «Galactic Hero»** (n.º 529) con traje
  espacial y **Jumba «Renegade Scientist»** (n.º 530).
- **Kingdom Hearts II**: Stitch invocación que lame la pantalla (§13.1)
  ✅; manga de KH II con Stitch (hoja 3, n.º 553). La parte de imagen
  dijo que KH III incluye «Stitch's Great Escape» de Shanghái (hoja 3,
  n.º 535): **no se sostiene**, el n.º 535 es una foto de **Stitch
  Encounter en Shanghai Disneyland**, no del juego. Dato
  retirado.
- **Disney Infinity** (hoja 3, n.º 546), **Disney Heroes: Battle Mode**,
  **Tsum Tsum 15.º aniversario** (hoja 3, n.º 547), **Dreamlight Valley**
  ✅ (§13.1).
- **Fortnite**: sólo una **filtración** de febrero de 2026 (Stitch como
  acompañante, no *skin*); Epic no lo ha anunciado ⚠️
  ([Vice](https://www.vice.com/en/article/leak-disneys-stitch-is-coming-to-fortnite-but-theres-a-catch/),
  [esports.gg](https://esports.gg/news/fortnite/fortnite-x-disney-a-complete-list-of-all-collaboration-skins/)).
  **No usar como hecho.**

### Cómics y libros

- **«Stitch Crashes the Marvel Universe»** (Marvel, septiembre de 2025):
  Stitch invade las portadas de *Amazing Spider-Man* n.º 11 (Luciano
  Vecchio), *Avengers* n.º 30 (Humberto Ramos), *Captain America* n.º 3
  (Ben Su), *Fantastic Four* n.º 3 (Paco Medina) y *X-Men* n.º 22 (Phil
  Noto) ✅ ([Marvel.com](https://www.marvel.com/articles/comics/stitch-crashes-the-marvel-universe-in-new-comic-book-covers),
  [AIPT](https://aiptcomics.com/2025/06/26/stitch-marvel-comics/),
  [Bleeding Cool](https://bleedingcool.com/comics/disney-stitches-stitch-to-the-covers-of-the-marvel-universe/)).
  Vistas en la hoja 1, n.º 25 y 29-34 (también las «Holiday» de Marvel).
- **«Stitch Crashes Disney»** (2021-2022): peluches mensuales de Stitch
  colado en 12 clásicos ✅ ([How To Disney](https://howtodisney.com/stitch-crashes-disney-history-co1/)),
  y los libros «Stitch Day Crashes Disney» (hoja 2, n.º 49-51). Es la
  misma broma que los Inter-Stitch-als de 2002 (§3.1): **Stitch se cuela
  en la foto**, el gag del canal.

### Figuras oficiales (pose = referencia 3D)

- **Funko Pop**: Stitch es el n.º 12 de Pop! Disney; variantes Aloha y
  Elvis; y **Stitch disfrazado** de Bestia (n.º 1459), Gato de Cheshire
  (1460), Simba (1461) y Pongo (1462) ✅ ([Pop Shop Guide](https://www.popshopguide.com/funko-pop-series/pop-disney/lilo-and-stitch/),
  [Cardboard Connection](https://www.cardboardconnection.com/funko-pop-lilo-and-stitch-figures)).
- **Britto** pop-art (hoja 1, n.º 12) y **Jim Shore «'Ohana»** tallada
  (hoja 2, n.º 74), líneas oficiales de Enesco ✅ vistas.
- **Tortuga de resina** «StitchSeaTurtleGK» (hoja 3, n.º 531) y figura de
  aula «StitchLiloSchoolGK» (hoja 2, n.º 71): *garage kits* de fans, **no
  oficiales** ⚠️, sólo pose.

### Moda y accesorios

- **Loungefly**: mochilas con el estampado del vestido de Lilo y línea
  «Stitch y Scrump» ✅ (Punto 19).
- **Crocs Jibbitz**: packs «Stitch Tropical», «Wild», «Curious», «Sweet»,
  con caras de Stitch en distintas expresiones ✅
  ([Crocs](https://www.crocs.com/p/stitch-tropical-5-pack/10012920.html)).

### Parques, espectáculos y cafés

- **Stitch's Great Escape!** (Magic Kingdom): abrió el 16-nov-2004 en el
  sitio de *ExtraTERRORestrial Alien Encounter* (cerrada el 12-oct-2003)
  y cerró en 2018 ✅ ([D23](https://d23.com/a-to-z/stitchs-great-escape/),
  [Wikipedia](https://en.wikipedia.org/wiki/Stitch%27s_Great_Escape!)); foto
  en la hoja 3, n.º 534.
- **Stitch Encounter** (Hong Kong, Tokio, Shanghái): Stitch habla con el
  público en directo ✅ (hoja 1, n.º 3; hoja 3, n.º 535).
- **Disney on Ice** con Stitch, Jumba y Pleakley (hoja 1, n.º 8-9) ✅: de
  ahí salen los hex del traje espacial (§16.1).
- **Fab 50**: estatua dorada de Stitch mordiendo su medallón, en
  Tomorrowland ✅ ([MiceChat](https://www.micechat.com/322514-fab-50-character-collection-walt-disney-world/),
  [Disney Wiki](https://disney.fandom.com/wiki/Disney_Fab_50_Character_Collection)); hoja 2, n.º 54.
- **Desfiles**: «Dreams Come True Parade» 2008 y «DJ Stitch» (hoja 1, n.º
  21-22); «Stars and Motor Cars» (hoja 3, n.º 532) ✅.
- **Lilo y Jumba de parque** (hoja 3, n.º 536-540): el vestido rojo y la
  camisa de Jumba en tela y volumen reales, la mejor referencia de
  **cosplay oficial** ✅. Fotos con licencia libre de la fiesta «Stitch's
  Hawaiian Paradise Party» en Flickr, **CC BY-ND 2.0** ([una de ellas](https://live.staticflickr.com/3178/5868563609_52d1cf1406_b.jpg),
  el resto en `referencias.json`).
- **Disney Cruise Line**: «Catch Stitch!», Stitch suelto en el barco
  (hoja 3, n.º 559) ✅ visto.
- **Cafés**: pop-up de **OH MY CAFE / BOX cafe&space** en Tokio (20-jun a
  27-jul-2025) y Nagoya (10-jul a 3-ago-2025) ✅
  ([TDR Explorer](https://tdrexplorer.com/limited-time-stitch-pop-up-cafe-launching-soon-in-tokyo-and-aichi/),
  [Japan Web Magazine](https://jw-webmagazine.com/tips/stitch-cafe-in-japan-2025/));
  Shanghái (Zhang Yuan, 26-jun a 19-jul); **Primark** Manchester con
  murales ([Brand License](https://www.indianretailer.com/brandlicense/archives/news/primark-x-disney-launch-exclusive-stitch-collection-cafe-experience.n3923));
  **MINISO** en el American Dream Mall de Nueva York, casi 200 productos
  ([License Global](https://www.licenseglobal.com/retail-news-trends/minso-debuts-world-first-stitch-pop-up-experience-in-u-s-));
  **Tropical Smoothie Cafe**, batido «'Ohana Breeze» (mayo de 2025)
  ([nota de prensa](https://www.counton2.com/business/press-releases/cision/20250512CL84550/tropical-smoothie-cafe-debuts-first-ever-disney-collaboration-featuring-the-new-ohana-breeze-smoothie-inspired-by-lilo-stitch/)).

### Cosplay

- No encontré un tutorial **de Stitch** con materiales exactos firmado
  por un cosplayer conocido; sólo guías genéricas de *fursuit* (pelo
  sintético, espuma de alta densidad) ⚠️. Para volumen real: los trajes
  de parque y de Disney on Ice de arriba.

---

## Punto 24 · Obras parecidas y temas relacionados (2.ª pasada)

### Influencias que reconocen los autores

- ***Mi vecino Totoro*** (Miyazaki, 1988): DeBlois, «*You've got these
  fantastic elements and yet you feel like you watched a story that
  really existed between a family*» ✅ ([AWN](https://www.awn.com/animationworld/lilo-toothless-and-totoro-too),
  [Wikipedia](https://en.wikipedia.org/wiki/Lilo_%26_Stitch)).
- ***E.T.***: Sanders puso a Stitch un «croac» a lo E.T. para molestar a
  sus animadores ✅ ([Wikipedia, Stitch](https://en.wikipedia.org/wiki/Stitch_(Lilo_%26_Stitch))).
  El paralelo de fondo (alien escondido, adoptado por un niño solo) lo
  hace la crítica, no el director ⚠️.
- Nutrias marinas para los gestos de Stitch (Punto 18).

### La misma historia en otras culturas

La franquicia es **más popular en Asia que en Occidente desde 2006** ✅
([Disney Wiki](https://disney.fandom.com/wiki/Lilo_%26_Stitch_(franchise))):

- ***Stitch!*** (anime, Madhouse, 2008-2015): isla ficticia **Izayoi**,
  inspirada en **Okinawa**; la niña **Yuna Kamihara**; la abuela Obaa y
  los espíritus **kijimuna** ✅ ([Ryukyu Shimpo](https://ryukyushimpo.jp/culture/entry-3182982.html),
  [castel.jp](https://castel.jp/p/6965), [Wikipedia en japonés](https://ja.wikipedia.org/wiki/%E3%82%B9%E3%83%86%E3%82%A3%E3%83%83%E3%83%81!)).
- ***Stitch & Ai*** (China, 2017): la niña **Wang Ai Ling** en la China
  rural ✅ (Disney Wiki); póster en la hoja 3, n.º 551.
- ***Tono-sama to Stitch* / *Stitch & the Samurai*** (manga, Kodansha,
  2020; en inglés por Tokyopop, 3 tomos): Stitch en el **Japón Sengoku**
  con el señor **Yamato** ✅ ([Disney Wiki](https://disney.fandom.com/wiki/Stitch_%26_the_Samurai),
  [ANN](https://www.animenewsnetwork.com/news/2020-01-13/disney-character-stitch-gets-manga-set-in-feudal-japan/.155297)).
  Su autor, **Hiroto Wada**, murió en julio de 2021 ✅ (ANN). Páginas
  interiores sin ver ⚠️.
- Idea: «Stitch + niña sola + cultura local» es una fórmula que Disney
  repite. Una lámina 2 «Stitch en Okinawa» ya tendría arte real.

### Otras láminas del servidor que se le parecen

- **Doraemon** (`19-doraemon`): **el más parecido**: ser no humano que
  un niño adopta y que desordena la casa. **No** apoyar la lámina en
  «Stitch lo rompe todo»; apoyarla en **las fotos de Lilo**, que Doraemon
  no tiene.
- **Big Hero 6** (`08-big-hero-6-grandes-h-roes`): Disney, familia
  encontrada tras una pérdida, compañero no humano. **Mismo universo**:
  el Experimento 619 sale en *Big Hero 6*. Su concepto A es una tabla de
  dolor plastificada: no se pisa.
- **Scooby-Doo** (`26-scooby-doo`): familia encontrada y humor; su
  concepto A usa un **tablero de corcho** de pistas. El concepto de corcho
  de aquí (§19) debe diferenciarse: fotos, no pistas.
- **No hay** ninguna biblia de Hawái, fotografía o álbumes: el objeto es
  único en el servidor ✅ (repasado el listado de `biblias/`).

---

## Punto 25 · El mundo, la historia y sus símbolos (2.ª pasada)

### Las reglas del mundo, en cinco líneas

1. Hay un gobierno espacial, la **Federación Galáctica Unida**, con sede
   en el planeta **Turo** y dirigida por la **Gran Concejal** ✅
   ([Disney Wiki](https://disney.fandom.com/wiki/Grand_Councilwoman)).
2. **Jumba** crea **626 experimentos** genéticos ilegales y numerados;
   Stitch es el **626**, el último. La Federación los llama
   «abominaciones» ✅ ([Disney Wiki, Experiments](https://disney.fandom.com/wiki/Experiments)).
3. La Tierra es **reserva natural protegida** por la Federación
   (00:07:23): por eso los alienígenas se disfrazan de humanos ✅.
4. ***Ohana***, «nadie se queda atrás ni se olvida», es la regla que
   convierte un arma en familia ✅ (película y cómic de 2024, §7.6).
5. ***Kuleana*** (responsabilidad) y ***mālama ʻāina*** (cuidar la
   tierra) son la *ohana* de los mayores: cuidar también de la
   comunidad y del lugar (David en el cómic) ✅.

### La historia por arcos

- **La película (2002)**: juicio y exilio del 626; cae en Kauai; Lilo lo
  adopta creyendo que es un perro; Nani lucha por la custodia; Cobra
  vigila; Stitch entra en la *ohana* ✅. Momentos: la pared de fotos
  (00:22), la lección de Elvis (00:42), el Patito Feo (00:55), «chiquita
  y rota» (01:15), el álbum final (01:17).
- **La caza de los primos (2003-2006)**: *Stitch! The Movie* (2003,
  Gantu y el 625 **Reuben**) → *Lilo & Stitch: la serie* (buscar y
  **rehabilitar** a los demás experimentos) → *Stitch en cortocircuito*
  (2005, un fallo le devuelve a su programa destructivo) → *Leroy y
  Stitch* (2006, el clon malo **Leroy**) ✅ ([Disney Wiki](https://disney.fandom.com/wiki/Lilo_%26_Stitch_(franchise))).
- **Relecturas en Asia, sin Lilo (2008-2021)**: *Stitch!* (Okinawa),
  *Stitch & Ai* (China), *Stitch & the Samurai* (Japón feudal) ✅
  (Punto 24).
- **Imagen real (2025-)**: remake con **Maia Kealoha** de Lilo; segunda
  parte anunciada para **2028** ✅ (Disney Wiki). En ella Jumba acaba de
  malo y Nani deja la tutela (§8, §14.2).

### Emblemas, objetos y palabras que un fan reconoce al instante

- **626**: de número de arma a nombre propio; el **26 de junio** es su
  día ✅.
- **Scrump**: la muñeca que Lilo se cosió; se inspira en un **muñeco
  vudú y el monstruo de Frankenstein** ✅ ([Disney Wiki](https://disney.fandom.com/wiki/Scrump);
  [imagen, 1806×1080](https://static.wikia.nocookie.net/disney/images/9/9d/Lilo_%26_Stitch_-_Lilo_holding_Scrump.png/revision/latest?cb=20230820215155)).
  Lilo fabrica sus cosas y las quiere: como quien hace sus fotos con lo
  que tiene.
- **El libro del Patito Feo**: el patito dice «I'm lost!» y en la página
  siguiente vuelve con su familia; es el espejo de Stitch y de Lilo ✅
  ([ScreenRant](https://screenrant.com/lilo-and-stitch-ugly-ducking-im-lost-scene-left-out/),
  [Disney Wiki](https://disney.fandom.com/wiki/The_Ugly_Duckling_(character))).
- **La cámara y la pared de fotos** de Lilo; **la foto de sus padres**;
  **el papel de adopción con sello** («See this stamp? I own him»,
  01:15:48) ✅.
- **La cápsula azul** de Stitch con la fotito de Lilo dentro (tráiler,
  [1:48](https://archive.org/details/LiloStitchTrailer?t=108)) ✅.
- **El emblema** dorado del traje espacial (`#F9E03E`) ✅; **escudo de la
  Federación**: no encontrado ⚠️.
- **Glosario corto** (para el bot o las etiquetas): *ohana*, *kuleana*,
  *mālama ʻāina*, 626, «primos», Federación Galáctica, Gran Concejal,
  «Pato el pez», «Meega, nala kweesta!», «blue punch buggy».

---

## Las hojas de contacto (2.ª pasada)

Salen de `herramientas/investigar_serie.py` sobre la wiki `disney`
(12 hojas en `herramientas/referencias/lilo-stitch/`). La parte de
imagen eligió estas 3; el redactor las **miró** y corrigió dos números.
Cada número lleva debajo el tamaño y el nombre del archivo en la wiki
(`https://disney.fandom.com/wiki/File:<nombre>`).

### `hojas/imagen_01_arte-oficial.jpg` (n.º 1-48)

| N.º | Qué es | Sirve para |
|---|---|---|
| **2** | key visual «promo art 2», 3523×5000 | **luz y color**; pose de complicidad (concepto A) |
| 7 · 17 | portadas Dynamite: Stitch surfeando · Stitch de agente con traje y gafas | poses nuevas; guiño «detrás de cámara» |
| **10** | arte de la serie: Lilo y Stitch en el **coche rojo** | objeto real, viaje |
| 12 · 13-14 | figura Britto · playsets de figuritas | pose 3D |
| 16 | arte de desarrollo de Stitch, 3338×2160 | proporciones |
| 18 · 19 | pósteres: «There's one in every family» · los tres surfeando | encuadre de cartel |
| **20** | fotograma «big wave», 3000×1782 | **color plano** medido (§16.1) |
| 24 | fondo oficial de *Stitch! The Movie*, 3000×1535 | fondo (§17.1) |
| 25 · 29-34 | portadas de Marvel con Stitch colado | gag de colarse (Punto 23) |
| 26 · 28 · 35-36 | libros «Agent Stitch» | poses de acción |
| 37 | peluche de Lilo, Animators' Collection | volumen de Lilo |
| 39-47 | revistas *Disney Adventures* | arte de época |
| 3 · 8-9 · 21-22 | Stitch Encounter, Disney on Ice, desfiles | trajes reales (cosplay) |

### `hojas/imagen_02_concept-y-crossovers.jpg` (n.º 49-96)

| N.º | Qué es | Sirve para |
|---|---|---|
| 49-51 | «Stitch Day Crashes Disney» (Big Hero 6, El Rey León, Winnie the Pooh) | gag de colarse |
| 53 | la *ohana* Pelekai en *Stitch! The Movie* | foto de familia, Jumba con camisa |
| 54 | estatua dorada Fab 50 | emblema |
| 55 · 82 | Stitch con traje espacial y de peluche en el parque | traje espacial en 3D |
| 59 | portada Dynamite: Lilo con el vestido rojo | vestido de Lilo |
| **62** | Stitch con Scrump, el sándwich y Pato, firmado por Sanders | **estilo Sanders puro** |
| **63** | **hoja de modelo de Pleakley** («Rough Model Sheet») | proporciones y caras de Pleakley |
| 72 | *Greatest Hawaiian*: Stitch con ukelele sobre kapa | textura hawaiana (Punto 19) |
| 74 | Jim Shore «'Ohana» | figura, abrazo |
| 76 · 81 | experimentos y *ohana* · puzle de experimentos | patrón |
| 77 | Nani sacando la lengua | cara de Nani |
| 83-93 | fotogramas de *Stitch! The Movie* (Nani y David, Pleakley cocinando, Jumba, Lilo) | ropa de Jumba y Cobra (n.º 88, 90-91) |

### `hojas/imagen_03_colaboraciones.jpg` (n.º 529-559)

| N.º | Qué es | Sirve para |
|---|---|---|
| **529 · 530** | cartas de Lorcana: Lilo «Galactic Hero» y Jumba «Renegade Scientist» | poses nuevas con objeto |
| 531 | tortuga de resina de fan | pose (no oficial) |
| 532 · 542 | desfiles | movimiento |
| 534 | Stitch's Great Escape (Magic Kingdom) | parques |
| 535 | Stitch Encounter Shanghai (**no** Kingdom Hearts III, corregido) | parques |
| 536-540 | Lilo y Jumba de parque (Florida, París, Tokio) | **cosplay oficial** |
| 546 · 547 | Disney Infinity · Tsum Tsum 15.º aniversario | colaboraciones |
| 551 | póster de *Stitch & Ai* | Punto 24 |
| 553 | manga de Kingdom Hearts II con Stitch | cruce |
| 558 | boceto a lápiz de Lilo y Stitch | línea de producción |
| 559 | «Catch Stitch!», Disney Cruise Line (**no** el n.º 554, corregido) | colaboración |

- Correcciones del redactor al mirarlas: la figura Britto es el **n.º
  12** (no el 4, que son figuritas de «It's a Small World»); Disney Cruise
  Line es el **n.º 559** (el 554 es Stitch y Angel de picnic); el 535 no
  es de Kingdom Hearts III.

---

## 19 · Tres conceptos para la lámina de #fotos

Las tres cumplen las reglas del dueño: **objeto real en un sitio real**,
**hecho en Blender**, personaje con **pose que va con lo que dice**,
**sin burbuja blanca**, texto corto en la voz de la serie.

> [!note] Qué cambió en la 2.ª pasada
> Los tres siguen, pero **con imágenes vistas** en vez de memoria:
> - **A**: la pared ya tiene fotograma ([22:10](https://archive.org/details/lilo-stitch-2002_202609?t=1330));
>   la luz del cuarto de noche es **morada y roja con lámpara cálida**,
>   no azul (tráiler, [2:12](https://archive.org/details/LiloStitchTrailer?t=132)),
>   y en la mesilla va la **lámpara verde con base de piña**.
> - **B**: gana la mejor referencia de todas: **el *collage* de los
>   créditos**, fotos de borde blanco pegadas en ángulo con cinta y
>   **Stitch sentado fuera del marco** de una foto de familia
>   ([1:20](https://archive.org/details/lilo-stitch-3?t=80)). Luz del
>   key visual «promo art 2» (hoja 1, n.º 2).
> - **C**: poses de Pleakley de su **hoja de modelo** (hoja 2, n.º 63) y
>   del fotograma de Jumba y Pleakley riendo ([38:40](https://archive.org/details/lilo-stitch-2002_202609?t=2320)).
> - Licencias leídas en la API de Sketchfab: álbum, corcho y Canon AE-1
>   son **CC BY**; el carrete de 35 mm sigue sin licencia vista ⚠️.

### Concepto A — «La pared de Lilo» (el cuarto de Lilo, de noche)

- **Objeto y sitio**: **la pared de fotos del cuarto de Lilo**, la de
  00:22:57. En Blender: un trozo de pared de madera pintada (Poly Haven,
  §4.4) con **unas 40 fotos** de borde blanco, algunas curvadas, sujetas
  con **chinchetas de colores** y **cinta de carrocero**. A la derecha,
  la **ventana** con la noche azul y la **«estrella fugaz»** cruzando
  (00:23:10).
- **Personaje**: **Lilo**, de pie en la cama, **levantando la cámara**
  hacia el que mira (pose de 00:22:54). **Stitch** asomado por el borde
  de la cama, mirando las fotos (es el más querido; no habla).
- **Cómo habla**: sin globo. Su frase va en **un trozo de cinta de
  carrocero escrito con rotulador**, pegado junto a ella: «**¡Mi cámara
  está llena otra vez!**» (Gochi Hand; ⚠️ adaptación, §10.3).
- **Dónde va cada texto**:
  - «**Fotos**»: letrero de cartulina hecho por Lilo, clavado arriba en
    el centro (Lilita One con textura de rotulador).
  - «**Fotos que hagan ustedes**»: en la foto más grande, en su borde.
  - «**Lo que ven**», «**Dónde graban**», «**Cómo se montan su
    rincón**»: cada uno en el borde de una foto que lo muestra (un
    paisaje, un escritorio con micrófono, un rincón con luces).
  - «**Un hilo por foto**», «**O uno por serie**», «**Ponle su
    etiqueta**»: la **lista de Lilo** en hoja de cuaderno pegada con
    cinta: «Número uno…», «Número dos…», «Número tres…» (Short Stack).
- **Para que no quede plano**: la **lámpara** de la mesilla da luz
  rasante: las fotos curvadas y las chinchetas echan **sombra**. La
  ventana pone **luz azul** de contra. En primer plano, **desenfocada**,
  la oreja de Stitch o la esquina de la colcha. La cámara de Lilo, con
  la correa colgando hacia el que mira.
- **Referencias**: fotograma 00:22:54-00:22:57; [filmboards](https://filmboards.com/board/t/Lilos-obsession-with-fat-people-1118389/)
  (la pared); [Cork Board de rickmaolly](https://sketchfab.com/3d-models/cork-board-9534ee2ad4344ea6b02b95b61bd4a913);
  [cámara de Marc Sawyer](https://sketchfab.com/3d-models/canon-ae-1-program-35mm-film-camera-03b0ac7d99c44197a09640179f360f3c) sin marca.
  **2.ª pasada**: la pared vista ([22:10](https://archive.org/details/lilo-stitch-2002_202609?t=1330));
  cara de Lilo orgullosa y tímida para enseñar algo suyo
  ([14:35](https://archive.org/details/lilo-stitch-2002_202609?t=875));
  poses de Lilo en «LiloStudyAD» (1600×1058); paleta del cuarto
  `#432626`, `#62414D`, `#954D2D` (§5.4b); edredón rojo y blanco de
  flores. La pose de «levantar la cámara» (00:22:54) **sigue sin
  fotograma** ⚠️; no hay *rig* libre de Lilo, así que va en 2D sobre
  «LiloStudyAD».

### Concepto B — «El álbum de ohana» (el porche, al atardecer)

- **Objeto y sitio**: **el álbum de fotos de la familia**, el del
  montaje final (01:17:18), **abierto en las tablas del porche** de la
  casa Pelekai, con el mar detrás a la hora dorada. En Blender: álbum
  de páginas de cartulina con **esquineras**, fotos pegadas, un
  **carrete** suelto y la cámara al lado ([Photo Album de mnaglak](https://sketchfab.com/3d-models/photo-album-b891198a35a64b2c9c3c1a26338b1a48),
  [35mm Film Roll](https://sketchfab.com/3d-models/35mm-film-roll-6d8a6d290de043e898420a04072a3a1e)).
  Es el objeto del plan, mejorado.
- **Personaje**: **Stitch** (el más querido), sentado junto al álbum,
  **con la cámara de Lilo en la cara**, haciéndole una foto al que
  mira. **Lilo** tumbada boca abajo al otro lado, **escribiendo los
  pies de foto** con rotulador.
- **Cómo habla**: Stitch sólo dice **una palabra**, escrita por Lilo en
  un pósit pegado a la cámara: «**¡Foto!**». La frase grande va como pie
  de la foto de familia de la última página: «**Es chiquita y rota,
  pero es buena**» (frase latina ✅ de Stitch, §10.3), debajo de una
  foto algo movida: **se aceptan fotos imperfectas**.
- **Dónde va cada texto**:
  - «**Fotos**»: letras recortadas de papel en la página de la izquierda.
  - Temas y reglas: pies de foto a mano (Gochi Hand), uno por foto.
  - «**Ponle su etiqueta**»: en una etiqueta de papel atada al lomo.
- **Para que no quede plano**: sol de **contraluz** desde el mar; la
  **sombra de la barandilla** cruza el álbum en rayas; las páginas se
  levantan con el viento; una **flor de hibisco** desenfocada delante;
  la correa de la cámara cae hacia el que mira.
- **Referencias**: [final con «Burning Love»](https://www.youtube.com/watch?v=r4aor3FulOU);
  [pins de los créditos](https://pinandpop.com/series/lilo-stitch-end-credits-snapshot-photos);
  [la foto de familia comparada](https://www.deviantart.com/danielnewton/journal/Lilo-s-Family-Photo-Comparison-872752082);
  HDRI [Secluded Beach](https://polyhaven.com/a/secluded_beach).
  **2.ª pasada**: el *collage* de los créditos ([0:00](https://archive.org/details/lilo-stitch-3?t=0)-1:20)
  para cómo se pegan las fotos (borde blanco, cinta, en ángulo); en la
  última página, **Stitch colado fuera del marco** de la foto de familia,
  como en [1:20](https://archive.org/details/lilo-stitch-3?t=80); y,
  escondida entre las fotos, la **fotito de Lilo que Stitch llevaba en su
  cápsula** ([tráiler, 1:48](https://archive.org/details/LiloStitchTrailer?t=108)),
  para el fan que se fije. Luz de atardecer del key visual
  ([3523×5000](https://static.wikia.nocookie.net/disney/images/1/1b/Lilo_%26_Stitch_promo_art_2.jpg)).
  Stitch en 3D con el [rig de werasik2aa1](https://sketchfab.com/3d-models/stitch-626-from-lilo-and-stitch-rigged-5ae4cd66c67d42c49202f2003fe7f559)
  (CC BY) para girar la pose de la cámara; no hay fotograma de Stitch con
  cámara ⚠️.

### Concepto C — «Las diapositivas del experto» (el salón, de noche)

- **Objeto y sitio**: un **proyector de diapositivas de carrusel** en
  la mesa del salón Pelekai (Jumba y Pleakley viven allí tras la
  película) proyectando sobre **una sábana colgada**. En Blender: el
  proyector, el haz de luz con **polvo** y la sábana con **arrugas**
  (la imagen proyectada sigue los pliegues, como le gusta al dueño).
- **Personaje**: **Pleakley**, con **peluca y vestido** (como lo quiere
  el fan, §14), con un puntero, en pose de explicar (00:07:45, «experto
  en la Tierra»). **Jumba** pasa las diapositivas. **La sombra de Stitch
  se cuela en el haz**: la broma de los Inter-Stitch-als (§3.1).
- **Cómo habla**: Pleakley, pedante, en **fichas de conferencia** que
  sostiene (Special Elite): «**Los humanos hacen fotos de todo.**»
  ⚠️ adaptación.
- **Dónde va cada texto**: cada diapositiva proyectada es un texto:
  «**Fotos**», «**Lo que ven**», «**Dónde graban**», «**Cómo se montan
  su rincón**». Las reglas, en la pizarra de corcho detrás del sofá.
- **Para que no quede plano**: el **haz del proyector** atraviesa la
  escena; delante, en silueta, **las cabezas de Lilo y Nani** en el
  sofá; la luz de la imagen rebota en la cara de Pleakley.
- **Por qué es distinto**: es **de noche**, es de **secundarios** y es
  **cómico**. Sirve también para la etiqueta «Nocturna» y para
  «Detrás de cámara».
- **Referencias (2.ª pasada)**: hoja de modelo de Pleakley firmada por
  Sanders ([2048×1319](https://static.wikia.nocookie.net/disney/images/7/7b/Pleakley_concept_art.jpg));
  Jumba y Pleakley riendo, [38:40](https://archive.org/details/lilo-stitch-2002_202609?t=2320);
  escondidos, [28:37](https://archive.org/details/lilo-stitch-2002_202609?t=1717);
  [rig de Pleakley](https://sketchfab.com/3d-models/pleakley-lilo-stitch-3a4305debb52451a8ba5ccb8a174e7ef)
  (CC BY, **260 220 caras**: regla 9, no saturar el PC). Letra de las
  diapositivas: **Actor** (pantallas de la Federación, §6.3). Ojo: la
  broma de Stitch colado también la usa B; si se hacen las dos, en C
  quitar la sombra de Stitch.

### Lámina 2 (las 11 etiquetas)

- Si se elige **A** o **C**: una **página doble del álbum** (el objeto
  de B) con **11 fotos**, una por etiqueta, en cuatro grupos (§0): «Qué
  sale», «Con qué», «Cómo quedó», «Detrás de cámara».
- Si se elige **B**: **la pared de Lilo** con las 11 fotos clavadas.
- Alternativa: **una caja de luz** con 11 diapositivas en una hoja de
  fundas, cada etiqueta escrita en el marco de su diapositiva.

### ¿Cuál primero?

**A.** Es la escena exacta de la película («mi cámara está llena»), la
dice **la fotógrafa**, y Stitch también sale. **B** va segunda: es el
álbum del plan, con Stitch en primer plano y la frase latina segura.
**C** es la más arriesgada, pero la más original.

---

## 20 · Lo que no pude verificar

Estado tras la 2.ª pasada. Tachado = resuelto (dice dónde).

- ~~Cualquier imagen~~ → vistas: película entera, tráiler, créditos,
  luau, tráiler 2025, 3 hojas de contacto (§2.4, §8.2, §15.1). Las
  posturas de la tabla vieja de §15 que no están en §15.1 siguen de
  memoria ⚠️.
- **La cámara de Lilo**: ¿compacta de carrete, Kodak, o instantánea?
  Sigue sin fotograma de 00:22:54 ⚠️.
- **Qué es el «TIMER DINGS»** de 01:17:56 ⚠️ (el vídeo de créditos
  empieza con el *collage* ya avanzado).
- Si en 00:44 **los turistas le hacen fotos con flash** a Stitch ⚠️ (no
  hay clip de la lección de Elvis).
- **Si Lilo hace fotos en la película de 2025**: no lo encontré ⚠️.
- **Frase latina de «My camera's full again» / «Aren't they
  beautiful?»** ⚠️: la parte de voz lo dejó en su «Sigue:» y ya no se
  relanza. Hay que oírla en Disney+.
- ~~Voces latinas de Nani, Pleakley, Cobra y David~~ → ✅✅ Claudia
  Garzón, Rubén Trujillo, Rubén Moya, Noé Velázquez (§10.1).
- ~~Qué se oyó en cine como voz de Stitch~~ → Aldana, sólo los diálogos
  en español; los ruidos, Sanders (Doblaje Wiki, §10.1) ⚠️ una fuente.
- ~~Estudio~~ → ✅✅ Doblaje Audio Traducción. **Director del doblaje de
  2002**: Ricardo Tejedo (ficha de Doblaje Wiki) o José Carlos Moreno
  (1.ª pasada) ⚠️; está en el «Sigue:» de la parte de voz.
- ~~Lilo 2025 en latino~~ → ✅✅ Aurora Villegas Romero. Corregidos
  Nani (Alicia Vélez) y Pleakley (Armando Guerrero).
- ~~Intérprete de «Muero de amor por ti»~~ → Bandana (Argentina) ⚠️ una
  fuente.
- **La letra Buka Bird**: licencia personal, tildes sin comprobar ⚠️.
- ~~Licencias de Sketchfab~~ → leídas en la API (una corregida, §4.1);
  quedan sin ver Low Poly Camera, 35mm Film Roll y los dos Corkboard ⚠️.
- **Caja de diálogo de Dreamlight Valley**: no la vi ⚠️. Tampoco
  capturas de juego del GBA (MobyGames y TCRF, 403).
- ~~Fondos de pantalla oficiales~~ → 7 con tamaño (§17.1).
- **Encuesta oficial** de popularidad por personaje: no la encontré
  tras buscar otra vez en español e inglés ⚠️.
- **Caras por emoción que faltan** (§8.2): 11 de 25 ⚠️.
- **Hex planos** de Stitch (sin luz de atardecer), Jumba, Cobra y David
  ⚠️ (§16.1).
- **Carátulas de Blu-ray** sin mirar ⚠️. **Emblema de la Federación** no
  encontrado ⚠️. **Rig libre de Lilo o Jumba**, no hay ⚠️.
- **Vídeos de YouTube y TikTok** de la tabla §12.2: sin mirar (YouTube
  pedía iniciar sesión; TikTok no abre) ⚠️. Vistas de reacciones y del
  cover de «Hawaiian Roller Coaster Ride», sin medir ⚠️.

---

## Cumplimiento del encargo

Estado al cerrar la 2.ª pasada (25-sep-2026). ✅ hecho · ⚠️ a medias ·
❌ no hecho. Cada ⚠️ dice por qué. Las partes de **voz** y **vídeo**
acabaron sus 2 tandas y no se relanzan: lo que dejaron pendiente va
aquí como ⚠️.

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Artbook confirmado, key visual de 3523×5000, hoja de modelo de Pleakley, poses de hula de Lilo, arte de desarrollo, más de 15 portadas de Dynamite, revistas, pósteres, figuras, cartas de Lorcana; 3 hojas miradas (§3.6, hojas) |
| 2 · Fotogramas de escenas icónicas en 1080p con minuto | ⚠️ | Película entera, tráiler, créditos y luau mirados, con minuto y enlace `?t=` (§2.4, §8.2). Pero **sólo el luau está en 1080p**; la película es una copia de 85 min con fotogramas de 1280 px y el tráiler de 2002, 640×346. Sin fotograma de la cámara (00:22:54), del «TIMER DINGS» ni de la lección de Elvis (lo que falta de vídeo) |
| 3 · Fan art y 3D con licencia | ✅ | Licencias leídas en la API de Sketchfab (una corregida a CC BY-NC-SA), 4 *rigs* CC BY con caras contadas, fondos de fans con autor (§4, §17.2). Fan art de Lilo con cámara: no encontrado, dicho |
| 4 · Sitios, luz, paleta y texturas | ✅ | Luau, cuarto, bosque y mar 2025 vistos y **medidos** con `estilo.py` (§5.3, §5.4b); texturas CC0 de ambientCG y Poly Haven. Foto libre de Hanapepe: Wikimedia dio 429 (§17.2) |
| 5 · Tipografía por uso, con letra libre y tildes | ✅ | 9 usos con su letra libre y tildes, ñ, ¿ ¡ comprobadas con fontTools (§6.3); variantes del logo vistas. Buka Bird sin comprobar (no se puede bajar) |
| 6 · Cómo hablan en pantalla (cuadro de diálogo) | ✅ | Bocadillo real del cómic Dynamite visto (óvalo, borde grueso, mayúsculas, cursiva), cartela azul, globos vacíos de 2006, el globo del libro del Patito Feo (§7.6) |
| 7 · Personajes y popularidad | ✅ | Stitch el más querido (ventas, taquilla, rankings japoneses); Pleakley el secundario más querido; no hay encuesta oficial y se dice (§9) |
| 8 · Doblaje latino y frases textuales | ⚠️ | Reparto 2002 y 2025 con dos fuentes (Doblaje Wiki y The Dubbing Database), 2 nombres de 2025 corregidos (§10). Pero **la frase de la pared de fotos en latino no se encontró** y **el director de 2002 sigue en duda** (Tejedo o Moreno): quedaron en el «Sigue:» de la parte de voz. Sólo 2 frases latinas textuales, de listas oficiales de Disney Latino, no de clip con minuto |
| 9 · Música y sonido | ✅ | Créditos leídos en pantalla (intérpretes, coro y su directora, orquestadores), tema por escena con minuto, silencio del Patito Feo, *featurette* 2025 (§11, §11.1). Onomatopeyas: la película casi no tiene; dicho |
| 10 · Vídeos y tendencias con minuto | ⚠️ | 6 vídeos mirados con minuto (§12.1). Los de YouTube y TikTok de §12.2 siguen **sin mirar** (YouTube pedía iniciar sesión; TikTok no abre desde el servidor) |
| 11 · Videojuegos | ✅ | Lista completa con dos fuentes (§13.1); pantalla de título del GBA vista; ningún juego tiene cuadro de diálogo propio. Capturas de juego y la caja de Dreamlight Valley, sin ver (403) |
| 12 · Lo que ama el fandom y qué no hacer | ✅ | Memes, Stitch Day, la hamaca, «está tocándome»; qué no hacer ampliado con la escena cortada de los turistas y los patrones hawaianos (§14) |
| 13 · Personajes a fondo y su cara en cada emoción | ⚠️ | Carácter, arco, miedos, qué transmite y dinámicas, hecho (§8, §8.1). **Caras con fotograma: 14 de 25** (§8.2). Faltan miedo y vergüenza de Jumba y Pleakley, rabia y miedo de Lilo, miedo y vergüenza de Nani, y el resto de Jumba y Pleakley: el «Sigue:» de la parte de voz, que ya no se relanza. Stitch no muestra miedo ni vergüenza en pantalla |
| 14 · Poses analizadas con minuto | ⚠️ | 18 poses **vistas** con minuto y enlace, con su uso (presentar, explicar, celebrar, regañar, pensar, animar) (§15.1). Las de la lista de Elvis, el ukelele y Stitch-Elvis siguen de memoria (sin clip) y Jumba tiene pocas |
| 15 · Vestuario con hex medidos | ⚠️ | Hex medidos de Stitch, Lilo, Nani y Pleakley, y variantes por escena (§16.1). Sin hex de Jumba, Cobra y David, y el azul plano de Stitch sin medir (sólo con luz de atardecer o de escenario) |
| 16 · Paisajes y fondos de pantalla con tamaño y autor | ✅ | 8 fondos oficiales con tamaño de la API y 10 de fans con autor y tamaño (§17.1, §17.2) |
| 17 · Guía para IA de imagen y de texto | ✅ | Rasgos, paleta medida, línea, luz, encuadre, *prompt*, palabras que ayudan y estropean, gestos por emoción con fotograma, referencias de estilo y pose; voz de cada personaje y frases reales por emoción (§18, §18.7, §18.8) |
| 18 · Estilo de dibujo y cómo replicarlo | ✅ | Entrevistas con citas (Sluiter, Howard, Nichols, Felix, DeBlois), receta para Photoshop y Blender, encuadres. Falta sólo el nombre del programa de color digital (Punto 18) |
| 19 · Texturas 2D | ⚠️ | Emblema, estampado del vestido, patrones oficiales, papel y sal (Punto 19). **No hay estampado hawaiano ni kapa CC0**: sólo bases de tela lisa |
| 20 · Gustos y detalles | ⚠️ | Tabla de gustos de los 5 con fuente y cruces con la película (Punto 20). Todo de una wiki de fans; **sin cumpleaños oficiales** y sólo la altura de Stitch (una fuente) |
| 21 · Por qué la aman | ⚠️ | Razones con fuente y 7 escenas con minuto, música y cómo están hechas (Punto 21). Falta la reacción medida (vídeos de reacción y comentarios con votos): YouTube y TikTok no dejaron |
| 22 · Fan dubs y comunidad hispana | ⚠️ | 3 fandubs con vistas medidas con yt-dlp y el meme «está tocándome» (Punto 22). Vistas del cover y escena exacta de cada fandub, sin medir |
| 23 · Colaboraciones y cruces | ✅ | Más de 12 colaboraciones con fuente: Lorcana, KH, Marvel, Funko, Loungefly, Crocs, parques, cafés; figuras y cosplay oficial vistos en hojas (Punto 23). Fortnite sólo filtración, dicho. Un dato de la parte de imagen retirado (KH III) |
| 24 · Obras parecidas | ✅ | Totoro y E.T. con cita, las tres relecturas asiáticas con fuentes en japonés, y las láminas del servidor que se parecen (Doraemon, Big Hero 6, Scooby-Doo) (Punto 24) |
| 25 · Mundo, historia y símbolos | ✅ | Reglas en cinco líneas, historia por arcos, objetos y glosario (Punto 25). Sin escudo de la Federación |
| Conceptos de lámina (3) | ✅ | A la pared de Lilo, B el álbum de *ohana*, C las diapositivas de Pleakley, con referencias vistas (§19) |
| Fuentes distintas (mínimo 40) | ✅ | Más de 120 webs distintas enlazadas (`revisar.py`) |
| Tipos de fuente de «Profundidad exigida» | ⚠️ | Oficiales, entrevistas del staff, japonés, chino y coreano, wikis, TV Tropes, arte, vídeo, GitHub, Sketchfab, doblaje: sí. **Reddit** sólo citado de segunda mano; **Wayback Machine** no se usó; **TCRF** y MobyGames dieron 403 en la 2.ª pasada; **ANMTV**, no |
| Hojas de contacto (3) | ✅ | 3 JPEG de menos de 1 MB, miradas, con qué número sirve para qué («Las hojas de contacto») |
| `referencias.json` (mínimo 20) | ✅ | Todas las útiles de las partes y de `datos.json`, las mejores primero, con tamaño medido donde se pudo |

---

## 21 · Bitácora de búsqueda

### 21.1 Estado de la red (24-sep-2026)

| Sitio | Resultado |
|---|---|
| doblaje.fandom.com (API y web), BreezeWiki, antifandom | 403 por curl; WebFetch «bloqueado» |
| Wikipedia, IMDb, YouTube, TikTok | 403 (sólo vistos en el buscador) |
| clip.cafe, eldoblaje.com, ANMTV, Disney Latino, sdpnoticias | 403 / bloqueado |
| Game UI Database, TCRF, archive.org, Animation Obsessive, AV Club | 403 / bloqueado |
| Sketchfab, Poly Haven | 403 |
| andreasdeja.blogspot.com | 403 |
| **raw.githubusercontent.com y git clone** | **funciona** |
| **Buscador web (WebSearch)** | **funciona** |
| **Búsqueda de código de GitHub** (herramienta MCP) | **funciona** |

`herramientas/investigar_serie.py` no se corrió (Fandom cerrado): **no
hay hojas de contacto** ni carpeta `hojas/`.

### 21.2 Búsquedas web (51)

| # | Idioma | Búsqueda (resumida) | Qué dio |
|---|---|---|---|
| 1 | es | doblaje latino 2002, reparto | Doblaje Wiki (páginas), José Carlos Moreno, Raúl Aldana |
| 2 | es | doblaje latino 2025, reparto | reparto 2025 (sdpnoticias, Nuestro Diario) |
| 3 | en | Lilo, cámara, turistas, «Aren't they beautiful» | filmboards, clip.cafe, Cinemablend, Feminist Disney |
| 4 | en | montaje final, fotos, «Burning Love» | TV Tropes (foto final), DeviantArt, YouTube |
| 5 | es | reparto (sólo doblaje.fandom.com) | Anaís Portillo, Maynardo Zavala |
| 6 | es | voz de Stitch, Raúl Aldana | Fernanda Robles, TikTok de SDV, DVD |
| 7 | es | abogado voz de Stitch 2025 | Gerardo Becker (ABC Noticias, MG Noticias) |
| 8 | es | Jumba, Maynardo Zavala | su ficha; Armando Réndiz |
| 9 | es | Stitch cine vs DVD (Doblaje Wiki) | las dos versiones |
| 10 | en | modelo de la cámara de Lilo | «Kodak» (un resumen) |
| 11 | en | acuarela, Ric Sluiter | AV Club, historia oral, Andreas Deja |
| 12 | en | cámara de Lilo en 2025 | **nada** |
| 13 | en | «The Shape and Color», estilo Sanders | IndieWire, Gold Derby |
| 14 | en | Hanapepe, Kauai | wiki, Only In Your State, SFGate, Beat of Hawaii |
| 15 | en | «The Art of Lilo & Stitch» | concept art; **no** el libro |
| 16 | en | letra del logo | Buka Bird (FontMeme y otras) |
| 17 | en | Dreamlight Valley, Stitch | wiki DDV, Prima Games |
| 18 | en | cómic de Dynamite | Bleeding Cool, AIPT |
| 19 | en | ventas de Stitch | Sherwood, WDWNT, THR |
| 20 | ja | スティッチ 人気 ランキング | みんなのランキング, Magmix |
| 21 | en | personaje favorito, encuesta | Screen Rant, Fanpop; **ninguna oficial** |
| 22 | ja | ランキング de personajes de la película | Stitch 1.º (un resultado) |
| 23 | en | THR, taquilla | 1.000 millones (THR, Variety, Deadline) |
| 24 | es | «Ohana significa familia», versiones | Disney Latino, TikTok |
| 25 | es | frases latinas | Disney Latino, El Tiempo, sitios de frases |
| 26 | es | «Las 7 frases…» (Disney Latino, El Tiempo) | las siete frases |
| 27 | es | «cámara llena», «¿no son…?» | **no** la frase latina |
| 28 | en | fotos de Lilo, escena eliminada | Cinemablend, lista de personajes |
| 29 | en | lista de videojuegos | Wikipedia, Giant Bomb |
| 30 | en | The Cutting Room Floor | páginas de TCRF |
| 31 | en | Hawaiian Adventure | Disney Wiki, Giant Bomb |
| 32 | en | Kingdom Hearts, Stitch | KH Wiki |
| 33 | en | créditos 2025, álbum | pins «End Credits Snapshot Photos» |
| 34 | en/es | banda sonora, versiones en español | «Muero de amor por ti», «Ardiente amor» |
| 35 | en | críticas al remake | TheWrap, Slate, Screen Rant |
| 36 | en | memes | «blue punch buggy», Elvis, #626day |
| 37 | en | Sketchfab, cámara de carrete | Canon AE-1, low-poly |
| 38 | en | Sketchfab, álbum y corcho | Photo Album, Cork Board |
| 39 | en | Poly Haven, playa y madera | HDRIs y texturas |
| 40 | es | voces 2002 de Nani, Pleakley, Cobra | **no** encontradas; estudio (un resumen) |
| 41 | en | personalidad de Nani, Pleakley, Jumba | wikis, Deadline, Gizmodo, The Mary Sue |
| 42 | es | tráileres y clips latinos | YouTube (tráiler, clip final) |
| 43 | zh | 史迪奇 人气 | Tencent, The Paper |
| 44 | ko | 릴로 스티치 인기 | Maxmovie, Brunch |
| 45 | en | «Surfing the Sanders Style» | Scribd, Tumblr |
| 46 | en | ropa de Lilo y Nani, colores | wiki; **sin** hex |
| 47 | en | fan art de Lilo con cámara | ArtStation, DeviantArt; **no** con cámara |
| 48 | en | Inter-Stitch-als | TV Tropes, YouTube |
| 49 | en | Sketchfab, Stitch y Lilo | modelos de fans |
| 50 | es | Karen Vallejo, Sergio Gutiérrez Coto… | confirma 2025 (la-lista, ANMTV) |
| 51 | es | Anaís Portillo, Lilo | TikTok de SDV, Facebook |

### 21.3 GitHub (sin cupo)

- Búsqueda de código: `"Ohana means family" extension:srt` →
  **subtítulos de 2002** en [alfredlu1986/movie-english-sub](https://github.com/alfredlu1986/movie-english-sub).
- `"Ohana" "camera" filename:Lilo` → segundo subtítulo en
  [imkira3/imkira3Keys](https://github.com/imkira3/imkira3Keys), y otros
  en [anasistac/final_project](https://github.com/anasistac/final_project),
  [jblinder/subtext](https://github.com/jblinder/subtext) y
  [aryankadam1256/StreamSage](https://github.com/aryankadam1256/StreamSage)
  (este trae también *Stitch Has a Glitch*).
- Subtítulos en español: `"significa familia" Lilo extension:srt` →
  **nada**. `"nadie se queda atrás" ohana` → sólo páginas de fans.
- 2025: sólo un subtítulo en azerí (tt11655566), inútil.
- `"Anaís Portillo" Lilo` y `"Raúl Aldana" Stitch` → nada útil.
- Letras: clon parcial de [google/fonts](https://github.com/google/fonts)
  con 25 familias, revisadas con fontTools (§6.2).

### 21.4 Fuentes consultadas por tipo

- **Oficiales**: Disney Latino, Disney (web 2025), Disney Japón, Disney+
  HK, la FAQ y web de Chris Sanders.
- **Staff y producción**: AV Club (Sluiter), historia oral (AUB),
  Andreas Deja, IndieWire (2025), Gold Derby, guía de Sue Nichols
  (Scribd y Tumblr), Fumettologica (entrevista a Sanders, sólo en el
  buscador), TheWrap (retrospectiva de Sanders, sólo en el buscador).
- **Otros idiomas**: japonés (ranking.net, Magmix), chino (Tencent,
  The Paper, Douban), coreano (Maxmovie, Brunch, Namuwiki en el
  buscador).
- **Wikis**: Doblaje Wiki, Lilo & Stitch Wiki, Disney Wiki, Dreamlight
  Valley Wiki, KH Wiki, TV Tropes, **The Cutting Room Floor**.
- **Foros**: filmboards, DISboards, Fanpop (en el buscador). Reddit y
  Arctic Shift, cerrados.
- **Arte**: ArtStation, DeviantArt, Tumblr, Pinterest (sólo como pista).
- **Vídeo**: YouTube y TikTok (sólo títulos del buscador).
- **3D y texturas**: Sketchfab, Poly Haven.
- **Doblaje latino**: Doblaje Wiki, sdpnoticias, Nuestro Diario, ABC
  Noticias, MG Noticias, la-lista, ANMTV, Merca2.0, TikTok de SDV.
- **Wayback Machine**: cerrada; no se usó.

### 21.5 Lo que NO encontré

- Imágenes: nada descargado; **sin hojas de contacto**.
- La frase latina de la escena de la cámara.
- Voces latinas de 2002 de Nani, Pleakley, Cobra y David.
- Un artbook oficial con ficha clara.
- Fondos de pantalla oficiales con tamaño.
- Fan art concreto de Lilo con su cámara.
- Hex medidos de la película.
- La caja de diálogo de ningún juego vista con mis ojos.
- Subtítulos en español (latino o de España) con tiempos.

(Lista de la 1.ª pasada. En la 2.ª se resolvieron las hojas, las voces
de 2002, el artbook, los fondos oficiales y los hex medidos; ver 21.6.)

### 21.6 Segunda pasada (24-25 de septiembre de 2026, red abierta)

Juntada de las bitácoras de `partes/imagen.md`, `video.md`, `voz.md` y
`texto.md`. Punto de partida: `herramientas/recolectar.py` (Doblaje
Wiki, Fandom, Wallhaven, Sketchfab, Openverse/Flickr, Dailymotion,
Internet Archive, MusicBrainz, Steam; AniList y Danbooru no aplican: es
una película y no tiene etiqueta), en `partes/datos-*.md`.

**Estado de la red en la 2.ª pasada**

| Sitio | Resultado |
|---|---|
| Fandom (disney, liloandstitch, doblaje, dubdb) por API | ✅ abrió |
| Sketchfab API, ambientCG API, Google Fonts `css2` | ✅ |
| Internet Archive, Dailymotion | ✅ (vídeos mirados) |
| YouTube | pedía iniciar sesión para bajar; `yt-dlp -j` sí dio metadatos |
| Wikimedia Commons | 429, un intento |
| TCRF, MobyGames, TV Tropes (página general) | 403 (Cloudflare), dos intentos como mucho |
| Disney Wiki web normal | 402 (se usó la API) |
| Hollywood Reporter | redirige a pago; se usó el resumen del buscador |
| TikTok | no abre desde el servidor |

**Parte de imagen** (14 búsquedas web + 5 de API), en inglés: Stitch en
Fortnite; «Stitch Crashes» Marvel; Lorcana Lilo & Stitch; Fab 50; colcha
hawaiana en la película (no hay escena de colcha); Loungefly; Crocs
Jibbitz; cosplay y *fursuit*; artbook oficial; fondos oficiales de
movies.disney.com (nada; sí los de la wiki); invocación de KH II; tapa y
kapa CC0 (nada); Stitch's Great Escape; Funko Pop. APIs: Sketchfab (3
modelos), ambientCG (fabric, paper), Wikimedia (429).

**Parte de vídeo** (0 búsquedas web): `advancedsearch.php` de Internet
Archive (`title:(Lilo Stitch)`, `mediatype:movies`) y `archive.org/metadata`
de cada vídeo; `fotogramas.py` sobre 6 vídeos (tráiler 2025 doblado,
créditos 2002, luau 1080p, tráiler 2002, «Part 1 HD» descartado,
*featurette* musical en francés); `estilo.py --colores` sobre 6
fotogramas. Sin resultado: «Elvis lesson», «camera wall photos», «Lilo
Stitch storyboard».

**Parte de voz** (7 búsquedas web, español e inglés): popularidad
oficial de Disney, cumpleaños y altura de Stitch, fandub español latino,
escena que hace llorar, por qué la ama el público, covers en español,
encuesta de Stitch Day. Además: película entera `lilo-stitch-2002_202609`
con `fotogramas.py` (más de 25 fotogramas en 3 hojas: 14:10-15:40,
20:50-23:15, 1:00:30-1:02:00), luau 1080p (48 fotogramas); Doblaje Wiki
(Nani Pelekai, Jumba Jookiba, Lilo y Stitch 2025); The Dubbing Database
(2002 y 2025); Lilo & Stitch Wiki (5 fichas); `yt-dlp -j` en 4 vídeos;
WebFetch de The Walt Disney Company, Box Office Mojo y Wikipedia.

**Parte de texto** (~13 búsquedas web): en inglés, Deep Canvas y
acuarela, gouache y director de arte, influencias de Sanders (Totoro,
E.T.), rotulación del cómic, «Ohana means family» exacta, simbolismo del
Patito Feo, Sketchfab con licencia, Game UI Database de Kingdom Hearts,
GBA 2002, Dreamlight Valley, *rig* y *toon shader* en Blender, cita de
DeBlois sobre Totoro, *kuleana* y *mālama ʻāina*, páginas de *Stitch & the
Samurai*; en **japonés**, 「スティッチ! アニメ 沖縄 設定 世界観」 y
「殿とスティッチ 漫画 comic days ページ」. En español no dio mejores
resultados que en inglés para lo técnico. Red directa: API de Fandom
(wikitext de Grand Councilwoman, Experiments, Scrump, la franquicia,
Stitch & the Samurai; búsquedas de Ohana, Deep Canvas, Aumākua, Galactic
Federation), Sketchfab `v3`, 8 letras con fontTools, capturas del GBA,
páginas del cómic en DuckTalks, portada en Tokyopop.

**Redactor**: comprobó con `curl` la imagen de la hoja de modelo de
Pleakley (la ruta `/7/74/` de la parte de imagen da 404; la buena es
`/7/7b/`) y miró las 3 hojas: corrigió los números de Britto, Disney
Cruise Line y el falso Kingdom Hearts III.

**Lo que NO se encontró en la 2.ª pasada**: la frase latina de la
cámara; el director del doblaje de 2002 con dos fuentes; 11 caras por
emoción; fotograma de 00:22:54 (la cámara) y del «TIMER DINGS»; la
lección de Elvis en vídeo; hex planos de Stitch, Jumba, Cobra y David;
estampado hawaiano o kapa CC0; cosplay de Stitch con materiales;
Fortnite oficial; la letra Buka Bird descargable; páginas interiores del
manga; capturas de juego y la caja de Dreamlight Valley; software de
color de 2002; *rig* libre de Lilo o Jumba; escudo de la Federación;
encuesta oficial de popularidad; cumpleaños oficiales; vistas de
reacciones y del cover; memes hispanos grandes; foto libre de Hanapepe.
