---
tags: [biblia, serie, laminas]
serie: "Assassination Classroom (暗殺教室)"
canal: "#avisos-clases"
fecha: 2026-09-24
---

# Biblia · Assassination Classroom — para #avisos-clases

> [!important] Cómo se hizo, y sus límites
> - **Primera pasada** (24-sep-2026): la red estaba cerrada casi entera:
>   Fandom, Doblaje Wiki (también su API), la web oficial, ANMTV, pixiv,
>   Namuwiki, Sketchfab, YouTube, Twitter y **todos los servidores de
>   imágenes** daban conexión rechazada. No se pudo correr
>   `herramientas/investigar_serie.py` ni ver ninguna imagen.
>   Hice **47 búsquedas web** en español, inglés, japonés, coreano y
>   chino (lista en §21).
> - **Segunda pasada** (25-sep-2026): **red abierta**, con el método de
>   equipo (`EQUIPO.md`): el recolector gratuito (`recolectar.py`) y cuatro
>   investigadores (imagen, vídeo, voz, texto). Sus notas están en
>   `partes/`. Lo nuevo va marcado **«2.ª pasada»**. Resumen de lo que
>   cambió justo debajo.
> - **Qué se pudo usar ahora**: la wiki de Fandom de la serie (el
>   subdominio bueno es **`ansatsukyoshitsu`**; el del encargo,
>   `assassinationclassroom`, da 404), **3 hojas de contacto** en `hojas/`,
>   la API de Doblaje Wiki (reparto completo), la API de Sketchfab
>   (licencias), ambientCG (texturas CC0), y **vídeos mirados de verdad**:
>   el episodio 1 y 6 episodios de la temporada 2 en Internet Archive, el
>   PV de la T2 y el *featurette* de la película de 2016 en Dailymotion.
>   Esos minutos van en formato `7:21` (minuto:segundo del archivo).
> - **Colores medidos** con `estilo.py` y Pillow sobre fotogramas y arte
>   oficial (cada tabla dice de cuál).
> - **Lo que siguió cerrado**: YouTube pide iniciar sesión (403 al bajar:
>   ni tráiler ni clips doblados), TikTok, pixiv, TV Tropes (Cloudflare),
>   AnimeThemes (403). Los vídeos vistos están en **480p**, no 1080p.
> - GitHub sí respondía. De
>   [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror)
>   saqué **los subtítulos japoneses de la temporada 2** (Netflix, con el
>   nombre de quien habla, y Blu-ray), **del 課外授業編** y **de la
>   película de 2026**. Con ellos doy **el minuto de cada escena**. De la
>   temporada 1 **no hay subtítulos** en el espejo.
> - De [google/fonts](https://github.com/google/fonts) bajé las letras
>   propuestas y comprobé con fontTools si traen á é í ó ú ñ ¿ ¡.
> - **Cómo leo los episodios**: «2×06» es temporada 2, episodio 6 (el 28
>   de 47). «KJ-3» es el episodio 3 del **課外授業編**. «peli» es la
>   película de 2026. El minuto va así: 00:12:37 (es el del archivo: puede
>   moverse uno o dos minutos según la plataforma).
> - **Redactor de la 2.ª pasada**: editó en su sitio cada sección con las
>   partes, montó la 3.ª hoja (`fotogramas_01.jpg`) y juntó
>   `referencias.json`. La tabla «Cumplimiento del encargo» va antes de
>   la bitácora.
> - ✅ **confirmado**: dos fuentes, o lo dice el subtítulo con su minuto,
>   o se vio en el fotograma. ⚠️ **dudoso**: una sola fuente, o de
>   memoria. ❌ **no encontrado**.

---

## Segunda pasada · qué cambió

Repaso del 25-sep-2026 con la red abierta. Sólo con lo que trajeron las
partes (`partes/imagen.md`, `video.md`, `voz.md`, `texto.md` y los
`datos-*.md`). Nada inventado: lo que no se encontró sigue con ⚠️ o ❌.

**Corregido (antes → ahora)**

- **La wiki de Fandom**: `assassinationclassroom` (la del encargo) → da
  404; la buena es **`ansatsukyoshitsu.fandom.com`** ✅ (API `siteinfo`).
  Y el apellido de Irina lleva tilde: **«Irina Jelavić»**; sin la ć la
  wiki no encuentra la página.
- **La paleta**: aproximada, «NO medida» → **medida** con Pillow y
  `estilo.py`. Koro-sensei `#FFF661` (arte del 10.º aniversario) y
  `#FCFF6D` (fotograma del ep. 1, 1:35); su toga es gris carbón
  `#2D2D2D`, no negro puro; el forro es rojo `#A2393C` (§16).
- **Nagisa**: corbata «¿roja o negra?» ⚠️ → **negra** ✅ (hoja de modelo
  de Lerche y arte del 10.º aniversario). Chaleco azul marino `#2E355C`.
- **Karma**: uniforme abierto sin corbata «de memoria» → confirmado con
  su hoja de modelo firmada (30-may-2014) ✅. Su bebida: «zumo de cartón»
  → **bebidas lácteas de la serie «～煮オ・レ»** ✅ (wiki).
- **Irina**: «vestidos ceñidos» ⚠️ → **traje sastre azul verdoso pálido
  `#90AFBA`**, gargantilla negra, pintalabios-arma ✅ (render oficial).
  El vestido morado con sombrero de bruja es del juego *Koro-Sensei
  Quest!*, no del anime.
- **Kayano enamorada de Nagisa**: ⚠️ «de memoria» → ✅ canon (infobox de
  la wiki; caps. 142 y 144 del manga).
- **Koro-sensei cotilla y tacaño**: ⚠️ → ✅ (wiki; manga vol. 16,
  cap. 137: «un poco pervertido, listo, torpe, algo tacaño y terco»).
- **Voces latinas** de Karasuma (**Juan Carlos Román**), Kayano (**María
  García**) y Ritsu (**Leyla Rangel**): «no encontré» → ✅ dos fuentes
  (reparto de Doblaje Wiki + página propia del actor o AniList).
- **Padre e hijo** (Carlos Segundo y Carlos Olízar) y **madre e hija**
  (Yanelly Sandoval y María José Moreno): ⚠️ extracto → ✅ texto literal
  de Doblaje Wiki. Irina se grabó en **Mérida, Yucatán** (dato nuevo).
- **Cajas de diálogo de los juegos de 3DS**: ❌ «no encontré capturas» →
  vistas en 7 capturas de prensa: **etiqueta amarilla `#FFEA62`** con el
  nombre, **caja crema `#F5F7E2`** y gótica negra ✅ (§7, §13).
- **Modelos 3D de Sketchfab**: 2 de 7 con licencia comprobada → **los 7
  CC BY**, leídos en la API ✅ (§4).
- **Ending «欠けた月»**: una fuente → ✅ (wiki + créditos vistos en
  2×06, 21:16).
- **Las dos películas animadas**: el tema «始業のベル» es de la de **2016**
  («365日の時間»), no de la de 2026 («みんなの時間», tema «Teacher»).
- **Koro-sensei en 2×06, 0:05** (el aviso del examen): «postura
  probable» → **visto**: traje ceremonial oscuro con cuello dorado y
  sombrero de paja, no su toga (§2.5, §15).
- **Pasar lista (2×24)**: «en el aula» → **de noche y al aire libre**, en
  el monte (7:05-9:45) ✅.
- **Una hoja de modelo mal rotulada en la wiki**: `Lerche Design Sketches
  Karma Akabane.webp` **no es Karma**: su rótulo dice 「烏丸惟臣」;
  probablemente es Karasuma ⚠️. No usarla para Karma.
- **Koro-sensei en *J-Stars Victory VS***: ⚠️ de memoria → ✅ jugable
  (Kanzenshuu y GameFAQs).
- **La lista final (2×24, 7:21)**: «con una carpeta amarilla» (parte de
  vídeo) → **con el libro de asistencia negro «出席簿»** ✅ (visto por el
  redactor en `fotogramas_01` n.º 7).
- **La pizarra**: «verde `#2E4A3B`» y «no pintarla negra» → es **verde
  casi negra `#272726`** ✅ (medida en 2×06, 0:02). Corregidos §5, §14 y la
  guía para IA.
- **El nombre de Koro-sensei**: «juego de palabras, de memoria» → ✅ y
  **se lo puso Kayano** (manga cap. 1).
- **Voces de Carlos Olízar, Yanelly Sandoval y del director** (⚠️
  extracto) → ✅ con el wikitext completo de Doblaje Wiki.
- **Hoja de la wiki n.º 64** (`personajes_02`): no es la encuesta del
  tomo 12 sino otra votación («スペシャルテーマ決定総選挙») ⚠️.
- **Arcos**: la parte de texto ponía el viaje a Kioto en otoño; es de la
  T1 (web oficial), así que va en primavera ⚠️ (§18.8).

**Añadido**

- **3 hojas de contacto** en `hojas/` y la sección §3.0 (qué número
  sirve para qué): `personajes_01` y `personajes_02` (wiki, 80 imágenes)
  y **`fotogramas_01`**, 16 fotogramas del anime con su minuto, montada
  por el redactor con `ffmpeg` sobre Internet Archive.
- **Formatos de texto reales** para la lámina: tiza de tres colores
  (rosa, blanco, amarillo) y la cartela «Ⅲ-E〔7〕茅野カエデ» (§7.4).
- **§2.5**: 16 escenas vistas en vídeo con episodio y minuto (Internet
  Archive y Dailymotion), y la hoja `fotogramas_01.jpg`.
- Encuesta oficial de Jump hasta el 9.º puesto, con el reparto chicas y
  chicos del voto (§9).
- La campaña de temas de la reemisión del 10.º aniversario (2025-26), el
  tema de la película 2026 y el *insert* de la muerte de Koro-sensei,
  «旅立ちの歌» (§11).
- Los **puntos 18 a 25** de `ENCARGO.md`, que no existían: técnica y cómo
  replicarla, texturas 2D, gustos de cada personaje, por qué la aman
  (ventas, premios, reseñas), fan dubs, colaboraciones (cafés 2026,
  figuras, J-Stars), obras parecidas y el mundo por arcos (§18.1-18.8).
- La guía para IA (§18) con **IA de texto**: frases reales por emoción.
- La tabla **«Cumplimiento del encargo»** (antes de la bitácora).
- `referencias.json`: **35 → 157** referencias (99 con tamaño medido);
  **102 webs distintas** enlazadas en la biblia.

**Los ⚠️**: había **99** en la 1.ª pasada. Se resolvieron unos **30**
(los de arriba), pero la biblia casi duplicó su contenido y cada dato
nuevo de una sola fuente lleva su ⚠️: en las secciones de la 1.ª pasada
(§0-§17 y §19) las **líneas con ⚠️ pasan de 89 a 88**; las nuevas §18.1-
§18.8 suman 18; y el archivo entero tiene **149 marcas ⚠️** contando la
tabla y §20, que las repiten. Lo que sigue dudoso: frases latinas con
minuto (YouTube bloqueado), vídeo en 480p, fan dubs sin vistas, varias
caras por emoción sin fotograma (Irina enfadada, Nagisa y Karma tristes),
emblema de la 3-E y fondos oficiales sin encontrar.

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección **LA ACADEMIA**):

> **ıı・📣・avisos-clases** (anuncios) · 0 fijados · 0 de personas en los
> últimos 15 — _Cuándo hay clase y de qué. Clases de doblaje y de canto.
> Activa el aviso que te interese en Canales y roles._

Función según el encargo: **horarios y avisos de las clases**.

Su vecino en LA ACADEMIA es el foro **ıı・📚・material-de-clase**
(«Lo que se da en clase y los ejercicios de cada alumno. Un hilo por tema
o por alumno. Etiqueta si es de doblaje o de canto.»). Las dos láminas
deberían parecer **del mismo colegio**.

### Los textos de la lámina 1 (qué es el canal)

Una idea por texto, sin «·», «—» ni paréntesis (regla 4 del dueño):

| # | Texto | Idea |
|---|---|---|
| 1 | **Avisos de clases** | nombre del canal |
| 2 | **Cuándo hay clase y de qué** | para qué es |
| 3 | **Clases de doblaje** | tipo 1 |
| 4 | **Clases de canto** | tipo 2 |
| 5 | **Activa el aviso que te interese** | qué hacer |
| 6 | **Lo tienes en Canales y roles** | dónde se hace |
| 7 | **Aquí sólo escriben los profes** | es un canal de anuncios (el inventario lo marca «anuncios»); ⚠️ confirmar con el dueño que sólo publica el staff |
| 8 | Frase del personaje, en su voz (ver §7 y §19) | gancho |

### Lámina 2 (si la 1 se satura)

El inventario **no trae el horario real** de las clases (qué día, a qué
hora, quién da cada una). **No lo invento.** Propuesta: una lámina 2 con
**el horario semanal de la pizarra** (el «時間割», la tabla de horas que
hay en todo aula japonesa), con dos columnas de color, **Doblaje** y
**Canto**, y los huecos en blanco para que el dueño los rellene. Encaja
con la serie: Koro-sensei anuncia las fechas de examen al empezar la
clase (ver §2, 2×06, 00:00:02).

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Por qué encaja | Es **una serie sobre una clase y su profesor**. Koro-sensei **anuncia los exámenes al empezar la clase** («２週間後は…中間テストですよ», 2×06, 00:00:02) y en la última escena **Nagisa, ya profe, dice «¡empieza la clase!»** (2×25, 00:22:50) ✅. |
| Cuadro de diálogo propio | **La cara de Koro-sensei**: naranja con **◯ rojo** si está bien, morada con **✕** si está mal, rayas verdes si se burla ✅ (4 fuentes japonesas). Y **la pizarra verde** con tiza. |
| Título en la voz de la serie | En latino los capítulos se llaman «**Hora de…**» («Hora de asesinar», «Hora de Karma») ✅ Crunchyroll. Para la lámina: **«Hora de clase»**. |
| Aviso oficial que imitar | «**#殺せんせーの抜き打ちテスト**», el aviso semanal de la cuenta oficial: 🎓🌕, «ヌルフフフフ〜♪», ⏰ plazo, 🎯 cómo ✅ (§7.7). |
| Objeto para la lámina | **La pizarra del aula de madera** (concepto A). Alternativas: **la guía de 2.400 páginas** que Koro-sensei escribe a mano (B) y **la caja de Ritsu con los móviles de la clase** (C). |
| El más querido | **Karma**, 1.º en la encuesta oficial de Jump (432 votos). Nagisa 2.º, **Koro-sensei 3.º**, Karasuma 4.º, Irina 5.ª ✅. |
| Voz latina | Koro-sensei **Carlos Segundo** ✅, Nagisa **María José Moreno** ✅, Karma **Iván Fernández** (también director) ✅, Irina **Cristina Hernández** ✅, Karasuma **Juan Carlos Román** ✅, Kayano **María García** ✅, Ritsu **Leyla Rangel** ✅. Estudio **The Kitchen** (Cuernavaca), para Funimation; hoy en Crunchyroll ✅. |
| Letras | **Yusei Magic** (tiza), **Klee One** (a mano), **Kalam**, **M PLUS Rounded 1c** (pantalla de Ritsu), **Dela Gothic One** (onomatopeya). Todas con tildes, ñ, ¿ y ¡: comprobado en el archivo. |
| Tono | **Luminoso, cálido y cómico**, con momentos muy emotivos. Nada sombrío. |
| Novedad | **Película de 2026**, «劇場版「暗殺教室」みんなの時間» (20 de marzo), y reemisión por el **10.º aniversario** ✅. |

---

## 2 · Las escenas que sirven para #avisos-clases (con minuto)

**De dónde salen los minutos.** Del repositorio
[Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror)
(clon parcial en el scratchpad, nunca en el repositorio):

- **Temporada 2**: subtítulos japoneses de **Netflix** (con el nombre de
  quien habla entre paréntesis) y los del Blu-ray (grupo Kamigami).
  Comprobé con un script que el episodio N de Netflix es el episodio N del
  Blu-ray (coinciden 90-214 líneas por episodio). **«2×06» es temporada 2,
  episodio 6** (el 28 de 47 en total: la temporada 1 tiene 22).
- **Película 2026** «劇場版「暗殺教室」みんなの時間» (*Our Time*):
  subtítulo japonés de Amazon. La cito como «peli».
- **Temporada 1: no hay subtítulos** en el espejo (la carpeta sólo tiene
  la lista de archivos ignorados). Sus escenas van **sin minuto** ⚠️.
- **«第2期 課外授業編»** (*Kagai jugyō-hen*, «clases extraescolares»):
  8 episodios con capítulos del manga que la serie no adaptó; van después
  del 2×01 y del 2×19 ✅ ([Hulu Japón](https://www.hulu.jp/assassination-classroom-second-season-kagai-jugyo-hen),
  [Filmarks](https://filmarks.com/animes/4791/6492/vod)). Para el estreno
  de la película se subieron enteros al YouTube oficial
  ([«第1話～第8話イッキ見»](https://www.youtube.com/watch?v=iETpifp-27Y)).
  Varias frases se repiten en la película. Lo cito como «KJ-n».

El texto y el minuto están comprobados ✅. **2.ª pasada**: ahora sí se
miraron en vídeo (Internet Archive, 480p) el ep. 1 y los 2×01, 2×06,
2×07, 2×21, 2×24 y 2×25: lo que se ve está en **§2.5** y en la hoja
`hojas/fotogramas_01.jpg`.

### 2.1 Anunciar una clase o un examen (lo que hace el canal)

| Escena | Minuto | Qué se dice (japonés, y traducción mía) | Para qué sirve |
|---|---|---|---|
| **2×06** | 00:00:02 | 殺せんせー: «さあさ 皆さんさん ２週間後は ２学期の中間テストですよ … 熱く行きましょう！ 熱く 熱く！» (¡Vamos, vamos, todos! En dos semanas es el examen parcial del segundo trimestre… ¡con ganas! ¡Con ganas!). Maehara: «暑苦しい！» (¡Qué pesado!) | **El anuncio perfecto**: fecha, de qué es, y el entusiasmo de Koro-sensei |
| **2×23** | 00:00:02 | 殺せんせー: «皆さん さっきの授業で 言い忘れていたことがあります» (Todos: hay algo que olvidé decirles en la clase de antes) | Tono de «aviso de última hora» (en la serie precede a la pelea final: úsese sólo la frase) |
| **2×19** | 00:00:01 | 殺せんせー: «そう！ 暗殺教室 季節外れの自由研究テーマ！» (¡Eso es! Aula de asesinato: ¡tema de investigación libre fuera de temporada!) | Presentar «de qué» es la clase |
| **peli** | 00:49:25 | 殺せんせー a Terasaka: «人生は 365日 勉強です 卒業の１秒前まで 授業は続きますよ» (La vida es estudiar los 365 días. Hasta un segundo antes de graduarse, la clase sigue) | Frase de apertura del canal |
| **peli** | 00:49:35 | 殺せんせー: «はい じゃあ 今日の日直は… 律さん». **Ritsu** (律): «スリープモードを解除 起動 … はい 本日の日直は 私ー 自立思考固定砲台 律が務めさせていただきます それでは 皆さん 起立！» (Salgo del modo reposo… Hoy la encargada del día soy yo, Ritsu, la batería fija de pensamiento autónomo. ¡Todos de pie!) | **Ritsu hace de anunciadora** (ver concepto C) |
| **2×24** | 00:07:18 | 殺せんせー: «最後に出欠を取ります 一人一人 先生の目を見て 大きな声で返事をしてください» (Por último, voy a pasar lista. Cada uno, mirándome a los ojos, responda en voz alta). Pasa lista de 00:07:51 (Karma) a más de 00:09:24 (Nagisa) | **La lista de clase**: la escena más emotiva de la serie. Sirve de modelo para «apúntate»; no para bromear |
| **2×25** | 00:01:04 | Isogai: «全員 起立！» → «烏間先生 ビッチ先生 本当にいろいろ教えていただき ありがとうございました！» (¡Todos de pie! Profesor Karasuma, profesora Bitch: ¡gracias por enseñarnos tanto!) | Los otros dos profes (Karasuma e Irina) tratados como profesores |
| **2×25** | 00:21:33 → 00:22:50 | **Nagisa ya es profesor** en un instituto de gamberros: «チャイムが鳴ったから席に着いて…» → «殺せるといいね！ 卒業までに» → «席に着いて 授業を始めます！» (Suena el timbre, a sus asientos… ¡Ojalá puedan matarme antes de graduarse! A sus asientos. **Empieza la clase.**) | **Nagisa profesor**: la última frase de la serie es literalmente «empieza la clase» |
| **KJ-1** y **KJ-5** | 00:00:01 | Nagisa narra: «３年Ｅ組は暗殺教室» (La clase 3-E es el aula de asesinato) | La frase-rótulo que abre los capítulos |

### 2.2 Cómo da clase Koro-sensei

| Escena | Minuto | Qué pasa | Para qué sirve |
|---|---|---|---|
| **KJ-3** | 00:01:09 | Takebayashi compara: en la clase A el profesor «早口で黒板に書いては消し 生徒の都合は一切無視» (escribe en la pizarra a toda prisa, lo borra y le da igual el alumno). En la E, Koro-sensei le hace **una canción con su anime favorito** para que aprenda la fórmula (00:01:19 a 00:02:00) | Koro-sensei adapta la clase **a cada alumno**: la idea de «activa el aviso que te interese» |
| **2×02** | 00:11:06 | 殺せんせー: «全員 捕まったら 宿題２倍デシタネ» (Si los pillo a todos, deberes dobles, ¿eh?) | Tono de profe juguetón |
| **KJ-7** | 00:03:28 | «決めました！ 先生から宿題をあげましょう» (¡Decidido! Les voy a poner deberes). En la peli, 00:42:52 | Anunciar tarea |
| **2×25** | 00:14:15 | «汚れたら手入れするのが この校舎のルールだよ» (La regla de este edificio: si se ensucia, se cuida) | El viejo edificio como algo que se cuida entre todos |

### 2.3 La risa y los ruidos de Koro-sensei (para escribir su voz)

- **«ヌルフフフフ…»** (*nurufufufu*): su risa. Sale **13 veces en la
  película** y en casi todos los capítulos de la temporada 2 (2×01,
  00:00:37; 2×04, 00:16:34: «ヌルフフフフ で どうでした？», y ¿qué tal?) ✅.
- **«にゅやッ！»** (*nyuya!*): el susto (peli 00:07:43, 00:15:24) ✅.
  «にゅ！» y «にゅおおおお～！» cuando le atacan (2×23, 00:00:32 y
  00:00:43). En total 51 líneas con «にゅ» ✅.
- **«手入れ»** (*teire*, «cuidar», «dar un repaso»): su palabra para
  corregir, peinar o reformar a alguien. En la película un personaje lo
  grita como un ataque: «殺し屋への報復… 手入れ！» (01:15:04) ✅. La
  versión inglesa lo llama *care*; la latina ⚠️ no la encontré.

### 2.4 Otras escenas y datos que sirven

| Escena | Minuto o fuente | Qué pasa | Para qué sirve |
|---|---|---|---|
| **T1 ep. 7** «修学旅行の時間・1時間目» | sin minuto ⚠️ ([ABEMA](https://abema.tv/video/episode/19-140_s1_p7)) | Koro-sensei reparte **la guía del viaje escolar** (修学旅行のしおり) hecha a mano: tan gorda que la llaman «diccionario». Trae todos los sitios con dibujos, un top 100 de recuerdos y hasta defensa personal. Un secuestro pasa en **la página 1243**, «más o menos a la mitad». La usan para pegar a unos gamberros ✅ ([アニヲタWiki](https://w.atwiki.jp/aniwotawiki/pages/15882.html), [pixiv百科](https://dic.pixiv.net/a/%E6%AE%BA%E3%81%9B%E3%82%93%E3%81%9B%E3%83%BC)) | **Objeto para el concepto B**: el horario hecho libro |
| **2×01** | 00:00:30 | Nagisa: «月を破壊し 来年３月には 地球を破壊すると予告した超生物 殺せんせー» (destruyó la Luna y avisa de que destruirá la Tierra en marzo) | La **luna en creciente fijo** es parte del paisaje: siempre sale así de noche |
| **2×04** | 00:16:47 | Ritsu: «“萌え箱”とは どういう意味ですか？» (¿Qué significa «caja moe»?) | Ritsu es **una caja** con pantalla: objeto de Blender |
| **2×07** | 00:06:00 → 00:06:22 | Karasuma le da un regalo a Irina por su cumpleaños (00:06:06 «誕生日 おめでとう»). Irina: «やば… 超うれしい» (Ay… qué feliz) | Irina fuera de su pose de femme fatale |
| **2×11** | 00:15:39 / **2×21** 00:00:18 | «第二の刃» (*el segundo filo*): la lección de Koro-sensei. Tener siempre un segundo plan. En 2×21 es **aprobar el examen de acceso al instituto** (todos entran «como mucho en su segunda opción») ✅; que para él el segundo filo sea estudiar en general ⚠️ | Lema posible para las clases ⚠️ (no sé cómo lo dice el latino) |
| **2×24** | 00:17:08 | Nagisa repite sus últimas palabras: «“卒業おめでとう”» (felicidades por graduarse). En el manga es el cap. 176 (lista) y 177 (despedida) ✅ ([萌娘百科](https://zh.moegirl.org.cn/%E6%9D%80%E8%80%81%E5%B8%88)) | **No usarla de broma**: es el final |

### 2.5 Escenas miradas en vídeo (2.ª pasada)

Fuente: Internet Archive, episodio 1 suelto
([`AnsatsuKyoushitsuEpisode001480pX264`](https://archive.org/details/AnsatsuKyoushitsuEpisode001480pX264))
y los 25 episodios de la T2
([`ansatsu-kyoushitsu-2x-23_20260520`](https://archive.org/details/ansatsu-kyoushitsu-2x-23_20260520)),
854×480 ⚠️ (no hay 1080p fuera de YouTube, que pide iniciar sesión).
Minuto del archivo. El n.º es el de `hojas/fotogramas_01.jpg`.

| N.º | Escena | Lo que se ve | Para qué sirve |
|---|---|---|---|
| 1-2 | **2×06, 0:02-0:09** | Pizarra verde-negra `#272726`. Tiza **rosa** («対», dentro de un estallido), **blanca** («二学期中間テスト») y **amarilla** («苦手科目強化特訓»). Koro-sensei no lleva su toga: **traje ceremonial oscuro con cuello dorado y sombrero de paja**, tentáculos en alto ✅ visto | **El aviso de examen**: modelo directo de la lámina |
| 3 | **2×06, 1:18** | Opening «QUESTION» con animación; cartela de créditos en placas grises translúcidas con letra mincho | Estilo de rótulo de créditos |
| 4 | **2×06, 21:38** | Ending «欠けた月»: dibujos a crayón blanco sobre fondo **sepia-naranja** `#E8744C`, que pasa a dorado | Fondo cálido «de cuaderno» |
| 5 | **2×21, 0:13** | Edificio viejo de la 3-E de día: cielo `#2964DC`, monte `#2D372A` | Fondo exterior |
| 6 | **2×21, 0:18** | Koro-sensei **celebrando**: mejillas sonrojadas, boca enorme, tentáculos juntos como aplaudiendo, burbujas blancas; pizarra negra detrás ✅ | Pose **celebrar** («¡todos aprobados!») |
| 7 | **2×24, 7:21** | Koro-sensei con la toga, el cordón amarillo y la luna al cuello, sosteniendo **el libro de asistencia negro, rotulado «出席簿»** (visto por mí en la hoja; la parte de vídeo lo llamó «carpeta amarilla») ✅ | **El objeto del canal**: la lista de clase |
| 8 | **2×24, 7:29** | Toda la clase de espaldas, de noche, al aire libre, ante el edificio viejo | Composición en grupo |
| 9 | **2×24, 7:51** | Karma en primer plano, noche azul: cejas bajas, boca recta, chándal con «E» | Karma serio |
| 10 | **2×24, 8:50** | Kayano con los ojos húmedos y, en pantalla, la cartela **«Ⅲ-E〔7〕茅野カエデ»** (clase, número de lista, nombre) en gris claro ✅ visto | **Formato de texto real** para nombres |
| 11 | **2×24, 9:29** | Aula de madera vacía, luz de día cálida: `#CAC1AA`, `#8B7F69`, `#5F5038` | Fondo interior |
| 12 | **2×01, 14:31** | Irina **muerta de vergüenza**: cara rosa `#E29ECB`, ojos «＞＜», boca dentada gritando, manos en el pelo ✅ | Cara de vergüenza |
| 13 | **2×07, 6:22** | Ojos de Irina: iris verde-azulado, rayitas de sonrojo | Irina emocionada (el regalo) |
| 14 | **2×25, 21:33** | Aula de instituto llena de grafitis («HEAVEN», «Die»); Nagisa de camisa, chaleco gris y corbata, manos juntas | Nagisa profesor |
| 15-16 | **2×25, 22:28 y 22:50** | Nagisa, sonrisa lateral tranquila (pelo `#ABC6D5`) | «Empieza la clase» |

Además, en el **episodio 1** (T1) no hay opening animado: de 3:15 a 4:30
sale un **título-crédito** («暗殺教室 ASSASSINATION CLASSROOM» sobre rojo,
3:30), una cuadrícula de siluetas con los nombres de los alumnos (3:45),
«三日月» (4:00) y el rótulo «オープニング‥» (4:15) ✅. Y el ending «Hello,
Shooting Star» abre con una silueta en el tejado y la **luna creciente**
(21:16-21:28) ✅. Fuente: `partes/video.md`.

---

## 3 · Arte oficial y referencias visuales

> [!note] 2.ª pasada: ahora sí hay imágenes
> En la primera pasada todos los servidores de imágenes estaban cerrados.
> Ahora hay **3 hojas de contacto** en `hojas/` (§3.0), y los colores de
> §5 y §16 están **medidos**. La wiki buena es
> **`ansatsukyoshitsu.fandom.com`**: `assassinationclassroom.fandom.com`
> da 404 ✅. Las imágenes de `static.wikia.nocookie.net` piden la cabecera
> `Referer: https://www.fandom.com/`.

### 3.0 Las hojas de contacto (2.ª pasada)

Salen de `investigar_serie.py --wiki ansatsukyoshitsu --paginas
"Korosensei" "Nagisa Shiota" "Karma Akabane" "Irina Jelavić"` (el
apellido **lleva la ć**: sin ella la wiki da 0 imágenes). 80 imágenes
grandes. Miradas una a una.

**`hojas/personajes_01.jpg`** (n.º 1-48)

| N.º | Qué es | Para qué |
|---|---|---|
| 2 | `Season2.jpg`, 1920×3039: Irina en vestido, de pie junto a un taburete, fondo cálido | Irina en pose de campaña |
| 3 | Hoja de modelo de Lerche **de Karma**, cuerpo entero, frente, 3/4 y espalda (30-may-2014), 2400×1700 | Ropa de Karma exacta |
| 4 | Hoja de expresiones rotulada «烏丸惟臣» (subida como «Karma» por error; probablemente Karasuma ⚠️) | **No usar para Karma** |
| 5 | Hoja de modelo de Lerche **de Nagisa**, cuerpo entero, «決定稿» (2-jun-2014) | Ropa de Nagisa exacta |
| 6 | Hoja de **expresiones de Nagisa** (19-sep-2014): sonrisa, enfado, sorpresa, «cara de demonio» | **Caras de Nagisa** |
| 9 | Nagisa y Kayano con el cuaderno, 2048×1146 | Nagisa apuntando |
| 11 | Koro-sensei sonriendo en el aula de madera, 1920×1080 | Koro-sensei en su sitio |
| 16, 17, 18 | Arte del **10.º aniversario** de Karma, **Koro-sensei** y Nagisa, cuerpo entero, fondo liso, 1000×1456 | **Las mejores para recortar**; de aquí salen los hex |
| 21 | Irina adulta (timeskip), 1224×1080 | Irina de cerca |
| 28 | Irina de bruja morada: es del juego ***Koro-Sensei Quest!***, no del anime ⚠️ | No usar como ropa del anime |
| 39, 40 | Koro-sensei disparando / con la pistola de Karma, 1280×720 | Acción |
| 41 | Koro-sensei con papeles de nombres en clave, 1280×720 | Koro-sensei **repartiendo papeles** |
| 42 | Koro-sensei vestido de militar con gafas de sol (archivo «Ep17») | Disfraces |
| 10 | Página del manga, cap. 43 (piscina), 1765×1300 | Trama y viñetas (§18.2) |

**`hojas/personajes_02.jpg`** (n.º 49-80)

| N.º | Qué es | Para qué |
|---|---|---|
| 49 | Logo «暗殺教室 ASSASSINATION CLASSROOM» (svg), 1920×443 | Logo |
| 53 | Manga: Nagisa quiere ser profesor | Final |
| 58 | Koro-sensei en blanco y negro con la toga y la luna | Silueta |
| 62, 63 | **Película de imagen real** (2015): Koro-sensei con cabeza esférica física, toga y birrete; y de **policía azul**, 1000×600 | Volumen real para Blender |
| 64 | Votación «スペシャルテーマ決定総選挙 結果発表!!» ilustrada (896×656). Es otra votación, no la encuesta del tomo 12 ⚠️ | Arte de grupo |
| 65 | `Bitch sensei transparent.png`: **Irina de cuerpo entero**, traje sastre, 535×1098 | Recorte de Irina |
| 69 | `Korosensei transparent.png`, tentáculos abiertos, 775×727 | Recorte de Koro-sensei |
| 70 | Koro-sensei **cara de póquer** (blanca) ante la pizarra | Cara neutra |
| 71 | `Karma transparent.png`, cuerpo entero, 535×1047 | Recorte de Karma |
| 72 | Koro-sensei (OVA) con **un libro gordo** en un tentáculo y **pilas de libros** detrás, 990×557 | **Concepto B** |
| 75, 76 | Nagisa y Karma chibi de *Koro-Sensei Quest!* | Estilo SD |

**`hojas/fotogramas_01.jpg`** (16 fotogramas del anime, montada en esta
pasada con ffmpeg sobre Internet Archive): lista en §2.5. Los mejores:
**n.º 1-2** (pizarra del aviso), **6** (celebrar), **7** (el libro de
asistencia 出席簿), **10** (la cartela «Ⅲ-E〔7〕») y **11** (aula de
madera vacía).

**Ojo con las hojas de Lerche (n.º 3-6)**: llevan escrito
«この制作資料の一切の公表、複製…を固く禁じます» (prohibido publicar o copiar).
Son material filtrado del estudio: **sólo para estudiar ropa y
silueta**, nunca para pegar.

Otros oficiales: [portada de AniList](https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx20755-dWrhs569YGUO.jpg)
y [banner](https://s4.anilist.co/file/anilistcdn/media/anime/banner/20755-D4ipww9U8YkC.jpg) ✅;
la ficha de Lerche de Karma («成績優秀だが素行不良», buenas notas y mala
conducta; CV 岡本信彦), 771×466 ✅. Fuente: `partes/imagen.md`.

### 3.1 Webs oficiales (empezar aquí)

| Qué | Enlace | Estado |
|---|---|---|
| Web oficial actual (película 2026) | [ansatsu-anime.com](https://www.ansatsu-anime.com/) | ✅ existe |
| Web de la serie 2014-2016 (fichas, capítulos, discos) | [ansatsu-anime.com/2014-2016/staff_cast/](https://www.ansatsu-anime.com/2014-2016/staff_cast/) | ✅ |
| **Ficha oficial de Koro-sensei** («担任殺せんせー») | [chara_1.php](https://www.ansatsu-anime.com/2014-2016/character/chara/chara_1.php) | ✅ |
| **Ficha oficial de Ritsu** («E-27律»: cada alumno tiene su número, **E-1 a E-28**) | [chara_e27.php](https://www.ansatsu-anime.com/2014-2016/character/chara/chara_e27.php) | ✅ la ficha; el rango E-1 a E-28 ⚠️ lo deduzco |
| Entrevista al director Seiji Kishi | [special0001.php](https://www.ansatsu-anime.com/2014-2016/special/special0001.php) | ⚠️ no la pude leer |
| Web del 10.º aniversario («10周年の時間») | [ansatsu-anime.com/10th/](https://www.ansatsu-anime.com/10th/news/detail.php?id=1128449) · [MISSION.1](https://www.ansatsu-anime.com/mission1/) | ✅ |
| Discos Blu-ray y DVD (portadas) | [discografía](https://www.ansatsu-anime.com/2014-2016/discography/archive.php?a=disco_archive&c=dvd) · [T2 vol. 1](https://www.ansatsu-anime.com/2014-2016/discography/detail.php?id=1011342) · [T1 vol. 2](https://www.ansatsu-anime.com/2014-2016/discography/detail_1st.php?id=1009496) · [課外授業編](https://www.ansatsu-anime.com/2014-2016/discography/detail.php?id=1014292) | ✅ |
| Cuenta oficial en X | [@ansatsu_anime](https://x.com/ansatsu_anime) | ✅ |

### 3.2 Portadas y visuales con poses VIVAS (no «de pie con una ropa»)

- **Blu-ray T2, vol. 1: Karma y Nagisa.** Vol. 2: **Maehara e Isogai, con
  Isogai de camarero** ✅ ([にじめん](https://nijimen.kusuguru.co.jp/topics/3378)).
  Las ediciones especiales traen **una funda dibujada a propósito por el
  diseñador de personajes** ✅.
- **Película 2026, visual «teaser»**: **Nagisa y Karma caminan por el
  pasillo del edificio viejo**, con las paredes llenas de los carteles
  de la serie y de los eventos ✅
  ([Animate Times](https://www.animatetimes.com/news/details.php?id=1757254250),
  [アニメハック](https://anime.eiga.com/news/124624/)).
  **Es la referencia más útil**: un pasillo de madera **con papeles
  clavados en la pared**, que es justo lo que es un canal de avisos.
- **Tienda de la película** (láminas, acrílicos):
  [goods](https://www.ansatsu-anime.com/goods/detail.php?group=1002704) ⚠️ sin mirar.
- **Tomos del manga**: la lista oficial de Jump está en
  [shonenjump.com](https://www.shonenjump.com/j/rensai/list/ansatsu_2.html) ⚠️ sin mirar.
- **Objeto oficial real: los libros de estudio «殺たん»** (*Korotan*).
  Existen de verdad, los edita Shueisha (JUMP j BOOKS). El segundo,
  «殺たん 基礎単語でわかる！熟語の時間», salió el **1 de mayo de 2015**
  con el tomo 14: **256 páginas**, tamaño bolsillo, una novela corta
  supervisada por Matsui, y de regalo **una «hoja roja» (赤い殺シート)
  para tapar las respuestas** y memorizar ✅
  ([Shueisha](https://www.shueisha.co.jp/books/items/contents.html?isbn=978-4-08-703357-1),
  [JUMP j BOOKS](https://j-books.shueisha.co.jp/books/ansatukyositu_korotan_kisotango.html),
  [Natalie](https://natalie.mu/comic/news/146019)). Sus capítulos también
  son «〜の時間» (時間 = hora, clase).

### 3.3 Staff (para buscar su arte)

| Cargo | Nombre | Estado |
|---|---|---|
| Autor del manga | **Yūsei Matsui** (松井優征) | ✅ |
| Director (TV) | **Seiji Kishi** (岸誠二) | ✅ |
| Guion y composición | **Makoto Uezu** (上江洲誠) | ✅ |
| Diseño de personajes (TV) | **Kazuaki Morita** (森田和明) | ✅ |
| Jefe de animación | Kōji Yamagata (山形孝二) | ✅ |
| Diseño de color | Tarō Kaguchi (加口大朗) | ✅ |
| Dirección de arte (fondos) | **Ayumu Miyakoshi** (宮越歩) y Kazuto Shimoyama (下山和人) | ✅ (1.ª pasada; en la 2.ª, la parte de texto sólo halló Shimoyama en una fuente ⚠️) |
| Estudio | **Lerche** | ✅ |
| Película 2026: director | Masaki Kitamura (北村真咲), su primera película | ✅ |
| Película 2026: diseño de personajes | Aya Hikami (樋上あや) | ✅ |

Los **kanji** están comprobados; la **lectura en letras latinas** de
algunos nombres es mía ⚠️.

Fuentes: [web oficial, staff](https://www.ansatsu-anime.com/2014-2016/staff_cast/),
[TVガイド](https://www.tvguide.or.jp/db/anime/ansatsu/),
[CAST&STAFF 2026](https://www.ansatsu-anime.com/castStaff/),
[アニメハック](https://anime.eiga.com/news/124624/).

### 3.4 Lo que dijo Matsui del diseño de Koro-sensei

- «Tenía que ser **simple, simple, simple**. Cuanto más simple, más
  universal». Con **ojos y boca** basta: «lo que puedes hacer no tiene
  límite» ✅ ([Anime News Network, 2016](https://www.animenewsnetwork.com/interview/2016-10-18/assassination-classroom-yusei-matsui/.107576),
  [ScreenAnarchy](https://screenanarchy.com/2016/10/interview-assassination-classroom-creator-matsui-yusei-on-movie-adaptations-and-saying-goodb.html)).
- El pulpo es «muy fácil de dibujar» y **sin forma fija**: sirve para
  cualquier situación ✅ ([FandomWire](https://fandomwire.com/he-has-no-hands-to-draw-yusei-matsui-had-the-most-lazy-reasoning-behind-koro-senseis-design-in-assassination-classroom/)).
- Consecuencia para la lámina: **la emoción la da el color de su cara**,
  no la postura (ver §7).

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D con licencia para la escena (Sketchfab)

| Modelo | Autor | Licencia | Para qué |
|---|---|---|---|
| [Japanese Classroom](https://sketchfab.com/3d-models/japanese-classroom-2a1e3b294c1e4e91bed794bfa520c4f4) | T I A N (@Tian96) | **CC BY** ✅ (API) | **Aula entera**: base para la del concepto A. Hay que envejecerla (madera) |
| [School Desk and Chair](https://sketchfab.com/3d-models/school-desk-and-chair-004b95391e4e48a797ee8d0cf612b5cf) | T I A N (@Tian96) | **CC BY** ✅ (API) | Pupitres en primer plano |
| [Japanese School Desk (JIS S 1021:2011)](https://sketchfab.com/3d-models/japanese-school-desk-jis-s-10212011-2758bff4dead4db5aada8a216ed0869d) | omiyaio | **CC BY** ✅ (API, 2.ª pasada) | Pupitre japonés de norma |
| [Japanese School Desk and Chair](https://sketchfab.com/3d-models/japanese-school-desk-and-chair-07e29a89e99e42e3bfd67989671a9d24) | woopossum | **CC BY** ✅ (API) | Alternativa |
| [The Japanese School Classroom](https://sketchfab.com/3d-models/the-japanese-school-classroom-d9fc039ba0b6433db91ec129abe86b52) | volvor | **CC BY** ✅ (API) | Alternativa de aula |
| [Anime School Desk Model](https://sketchfab.com/3d-models/anime-school-desk-model-5c013e3454ad458e83803ab5b332ef02) | 3DGhost903 | **CC BY** ✅ (API) | Pupitre de estilo anime |
| [Koro Sensei (llavero)](https://sketchfab.com/3d-models/koro-sensei-2c02fdcefbce4abc9333bff674795331) | roman.benvenuto80 | **CC BY** ✅ (API) | **Sólo para mirar volumen**; el personaje es de Matsui, no se pega |

Crédito tipo para CC BY: «"Japanese Classroom" by T I A N (@Tian96),
CC Attribution, sketchfab.com/3d-models/<slug>». **2.ª pasada**: las 7
licencias se leyeron en `api.sketchfab.com/v3/models/<uid>`: todas CC
Attribution y descargables ✅ (`partes/imagen.md`).

**Texturas**: [ambientCG](https://ambientcg.com/) y Poly Haven son CC0
(libres del todo) ✅. **2.ª pasada**, por la API de ambientCG, CC0:
madera de tablones [WoodFloor043](https://ambientcg.com/view?id=WoodFloor043)
y [PaintedWood009C](https://ambientcg.com/view?id=PaintedWood009C) para el
edificio viejo, papel [Paper006](https://ambientcg.com/view?id=Paper006)
para la guía y el cuaderno ✅. **Pizarra**: `q=chalkboard` da 0
resultados en ambientCG ❌: hay que pintarla (verde-negro `#272726`,
`#423E3B`, medido en 2×06, 0:02).

### 4.2 Fan art (mirar, nunca pegar)

- Pinterest junta tableros de fan art de Koro-sensei
  ([1](https://jp.pinterest.com/maekawaneo/%E6%AE%BA%E3%81%9B%E3%82%93%E3%81%9B%E3%83%BC/),
  [2](https://jp.pinterest.com/hkkhate/%E6%AE%BA%E3%81%9B%E3%82%93%E3%81%9B%E3%83%BC/)).
  Sirven para **encontrar al autor original** en pixiv, no como fuente.
- **pixiv** sigue pidiendo iniciar sesión (302 a login, 2.ª pasada) ❌.
- **Fan art con autor** (Safebooru, del recolector): Nagisa 3249×3778,
  [imagen](https://safebooru.org/images/4619/1e82191bee4a152a1e5566e3e31df79df3c3bf54.jpg),
  de [@tentenchan2525](https://twitter.com/tentenchan2525/status/1826627085143884022);
  Nagisa 2016×1512, [imagen](https://safebooru.org/images/1663/0aa8b1a5e2e742cdb26f2da0dff0df4bfd10d816.jpg),
  de pixiv 56790462 ⚠️ (sólo mirar; derechos del autor).
- **Cosplay con licencia libre** (Wikimedia, CC BY 2.0, Farhan Ahmad
  Tajuddin): [Karma y Koro-sensei, Comic Fiesta 2015](https://upload.wikimedia.org/wikipedia/commons/9/9a/Cosplay_of_Karma_Akabane_and_Koro-sensei_from_Assassination_Classroom_at_Comic_Fiesta_2015%2C_Day_1_013_%2823314146343%29.jpg)
  y [Kayano, AniManGaki 2015](https://upload.wikimedia.org/wikipedia/commons/a/aa/Cosplay_of_Kaede_Kayano_from_Assassination_Classroom_at_AniManGaki_2015%2C_Day_1_020_%2821527861662%29.jpg),
  2760×4912 ✅.
- **Cómo se construye la cabeza de Koro-sensei** en cosplay: esfera de
  poliestireno pintada ([Behance](https://www.behance.net/gallery/43165327/How-to-make-Koro-sensei-cosplay-mask-DIY));
  tentáculos con churros de piscina, alambre y tela
  ([cosplay.com](https://cosplay.com/archive/thread/6oeo0n/koro-sensei-tentacles)) ✅.
  Útil para el volumen en Blender.
- **Arte de pizarra (黒板アート)**: en Japón los alumnos dibujan anime con
  tiza en la pizarra de clase, sobre todo en la graduación. Hay vídeos y
  tableros ([TikTok 黒板アート卒業アニメ](https://www.tiktok.com/discover/%E9%BB%92%E6%9D%BF%E3%82%A2%E3%83%BC%E3%83%88%E5%8D%92%E6%A5%AD%E3%82%A2%E3%83%8B%E3%83%A1),
  [Pinterest 黒板アート アニメ](https://jp.pinterest.com/ideas/%E9%BB%92%E6%9D%BF%E3%82%A2%E3%83%BC%E3%83%88-%E3%82%A2%E3%83%8B%E3%83%A1/953614767184/)).
  **Referencia de cómo queda la tiza** para el concepto A ✅ que existe;
  uno de Koro-sensei concreto ❌ no lo encontré.
- Figuras para imprimir en 3D de Koro-sensei (sólo para ver volumen):
  [MakerWorld](https://makerworld.com/en/models/2281774-koro-sensei),
  [Cults3D](https://cults3d.com/en/tags/korosensei) ⚠️.

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Cómo es | Estado |
|---|---|---|
| **El edificio viejo de la clase 3-E** (旧校舎) | **Casa escolar de madera en lo alto de un monte**, lejos del edificio nuevo del Colegio Kunugigaoka (私立椚ヶ丘中学校). A la clase la llaman «**la E del final**» (エンドのE組): los peores alumnos ✅ ([pixiv百科: エンドのE組](https://dic.pixiv.net/a/%E3%82%A8%E3%83%B3%E3%83%89%E3%81%AEE%E7%B5%84)) | ✅ |
| El aula de la 3-E | Pizarra verde-negra, suelo y paredes de madera, ventanas grandes de cuarterones. Al fondo, **la caja de Ritsu** (desde que llega) | ✅ aula y pizarra vistas (2×06, 0:02; 2×24, 9:29; hoja `fotogramas_01` n.º 1, 11); la caja de Ritsu ⚠️ sin fotograma |
| El edificio nuevo | Moderno y frío; allí están la clase A y el director Asano | ⚠️ de memoria |
| El monte de detrás (裏山) y la piscina hecha por Koro-sensei | Bosque; entrenamientos con Karasuma | ✅ salen como escenarios del juego de 3DS ([4Gamer](https://www.4gamer.net/games/278/G027887/20150227043/)) |
| **El cielo de noche** | **La Luna, rota en un creciente fijo** (Koro-sensei destruyó el 70 %) | ✅ (2×01, 00:00:30; [EMIRA](https://emira-t.jp/fantasy/24953/)) |

**Lugar real**: el **antiguo colegio de primaria Irisugawa** (旧入須川小学校),
en Minakami (Gunma), fue **el rodaje de la película de imagen real**
«暗殺教室〜卒業編〜», y el pueblo lo usa para turismo ✅
([訪日ラボ](https://honichi.com/news/2017/01/26/chihoyuchihaikonokank/),
[asikotz](https://asikotz.com/entertainment/movie/ansatsu/)).
Que fuera también el modelo del anime ⚠️ lo dice un resumen de búsqueda,
sin fuente clara. Sirve como **foto real de un aula de madera**.

### 5.2 Luz (2.ª pasada: vista en fotogramas)

- **Edificio de día** (2×21, 0:13): cielo azul muy saturado, sol alto,
  monte verde oscuro detrás, tierra clara delante ✅ visto.
- **Aula de día** (2×24, 9:29): luz blanca y cálida por la ventana del
  fondo, madera beige y marrón; muy luminosa ✅ visto. Es una serie
  **luminosa y de colores vivos**, no sombría.
- **Noche** (2×24, 7:05-9:45): azul marino con nubes moradas, luz fría
  en las caras; luna creciente ✅ visto.
- **Tarde**: dorado, sombras largas ⚠️ de memoria (no hay fotograma).
- Brillo medio de los fotogramas medidos: 22-45 (ni oscuro ni quemado)
  ✅ (`partes/texto.md`, §18.3).

### 5.2b Paleta medida (2.ª pasada)

Con `estilo.py` sobre fotogramas de Internet Archive (`partes/video.md`)
y con Pillow sobre arte oficial (`partes/imagen.md`, `partes/voz.md`).
**Usar éstos, no la tabla aproximada de abajo.**

| Qué | Hex medido | De dónde |
|---|---|---|
| Koro-sensei, amarillo | `#FFF661` (arte) · `#FCFF6D` (anime) · `#E8EA49` (anime, pizarra) | 10.º aniv. · ep. 1, 1:35 · 2×21, 0:18 |
| Koro-sensei, burla (rayas verdes) | `#57DE54` | ep. 1, 3:00 |
| Toga | `#2D2D2D` (gris carbón, no negro) | 10.º aniv. |
| Forro de la toga | `#A2393C` | 10.º aniv. |
| Pizarra | `#272726` · `#423E3B` · `#1E1F1B` | 2×06, 0:02 · 2×21, 0:18 |
| Cielo de día | `#2964DC` · `#3779E4` | 2×21, 0:13 |
| Monte | `#2D372A` · `#4B5645` · `#B4BA90` | 2×21, 0:13 |
| Cielo de noche | `#14214E` · `#0D193F` · `#1B2547` | 2×24, 7:09 |
| Aula de madera de día | `#CAC1AA` · `#8B7F69` · `#5F5038` | 2×24, 9:29 |
| Ending a crayón | `#E8744C` · `#AC7B4F` → `#E0C62D` · `#F4E941` | 2×06, 21:38 y 22:40 |
| PV T2, noche / bosque | `#0B2348` · `#092040` / `#2E5548` · `#446C71` · `#DDC337` | Dailymotion x3kret1, 0:24 / 1:24 |
| Juegos de 3DS: etiqueta / caja | `#FFEA62` / `#F5F7E2` | capturas de Famitsu |

### 5.3 Paleta aproximada de la 1.ª pasada ⚠️ (NO medida; sustituida por 5.2b)

Estos hex son **orientativos** y sólo sirven donde 5.2b no tiene dato
(caras naranja, morada y rosa, tizas, luna).

| Qué | Hex aprox. |
|---|---|
| Koro-sensei, amarillo normal | `#F5D22E` |
| Toga y birrete negros | `#1C1C22` |
| Luna de la corbata | `#F2C94C` |
| Cara «correcto»: naranja / círculo rojo | `#F08A24` / `#D8322A` |
| Cara «incorrecto»: morado | `#6A3D9A` |
| Burla: rayas verdes sobre amarillo | `#6DBE45` |
| Cara de «pervertido»: rosa | `#F4A7C3` |
| Pizarra verde | `#2E4A3B` |
| Tiza blanca / amarilla / roja | `#EEEBDF` / `#F4D54B` / `#E26A5E` |
| Madera del aula vieja | `#9C7552` (pared) · `#6B4E36` (suelo) |
| Pelo de Nagisa (azul claro) | `#7FA7D6` |
| Pelo de Karma (rojo) | `#C8322B` |
| Pelo de Irina (rubio) | `#F1D68A` |

### 5.4 Texturas reales equivalentes

- **Pizarra verde de tiza** con restos de borrado (no negra: la de un aula
  japonesa es verde).
- **Madera vieja** de tablones para suelo y paredes; **papel de
  cuaderno** para las notas de Nagisa; **cartulina y grapas** para la
  guía de Koro-sensei; **plástico negro mate** para la caja de Ritsu.
- Fuentes CC0: [ambientCG](https://ambientcg.com/) (ver §4.1):
  WoodFloor043, PaintedWood009C, Paper006 ✅. Pizarra: no hay en
  ambientCG ❌, se pinta.
- **Ojo**: la pizarra del anime se ve **verde muy oscuro, casi negro**
  (`#272726`), no el verde medio `#2E4A3B` que se suponía ✅ (medido).

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **Logo japonés** 暗殺教室: rotulado propio. **No encontré** qué letra es ❌.
- **Logo inglés** «ASSASSINATION CLASSROOM»: en el foro de dafont lo
  identifican como **Futura** ✅ (2.ª pasada, dos fuentes:
  [dafont](https://www.dafont.com/forum/read/347871/assasination-classroom)
  y [FontMeme, «Famous logos created with Futura»](https://fontmeme.com/famous-logos-created-with-futura-font/)).
- **Títulos de episodio en pantalla y web** («〜の時間»): **gótica de
  trazo grueso sin remates**; nombre exacto no encontrado ❌. La libre
  más parecida: **Dela Gothic One** ⚠️ (`partes/texto.md`).
- **Logo japonés**: 2.ª pasada, sigue sin diseñador ni letra base ❌
  (búsquedas 「暗殺教室 ロゴ デザイン 書体」 y 「タイトルロゴ フォント」;
  [la misma pregunta en Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14170560814)
  sin respuesta). Parece rotulado a mano.
- **Títulos de capítulo**: siempre **«〜の時間»** («la hora de…»). En
  **latino, Crunchyroll los traduce «Hora de…»**: «Hora de asesinar»,
  «Hora de Karma», «Hora de la isla», «Hora de L y R» ✅
  ([ep. 1](https://www.crunchyroll.com/es/watch/GD9UVDXEN/assassination-time),
  [Karma](https://www.crunchyroll.com/es/watch/G0DUN48M1/karma-time),
  [isla](https://www.crunchyroll.com/es/watch/G50UZW53D/island-time),
  [L y R](https://www.crunchyroll.com/es/watch/GQJUG72WE/l-and-r-time)).
  Las partes de un arco son «2時間目» (**segunda hora de clase**).
  **Esto es oro para el canal**: «Hora de clase».

### 6.2 Letras libres comprobadas por mí

Bajé cada archivo de [google/fonts](https://github.com/google/fonts) y miré
con fontTools si trae **á é í ó ú ñ Á É Í Ó Ú Ñ ¿ ¡ ü**, y además
**暗殺教室** (por si hace falta un kanji). Hice una prueba sobre verde
pizarra para verlas.

| Letra | Tildes, ñ, ¿ ¡ | Kanji | Para qué |
|---|---|---|---|
| **Yusei Magic** | ✅ | ✅ | **Tiza gruesa / rotulador**: el título en la pizarra. La mejor para el concepto A |
| **Klee One** (SemiBold) | ✅ | ✅ | **Letra a lápiz**: el cuaderno de Nagisa, la guía de Koro-sensei |
| **Zen Kurenaido** | ✅ | ✅ | Rotulador fino: notas al margen |
| **Kalam** (Bold) | ✅ | ❌ | Tiza redonda y clara para texto largo en la pizarra |
| **Schoolbell** (Apache 2.0) | ✅ | ❌ | Tiza infantil, dibujitos de Koro-sensei |
| **Gochi Hand** | ✅ | ❌ | Alternativa a la anterior |
| **Mochiy Pop One** | ✅ | ✅ | Rótulos redondos y alegres (etiquetas «Doblaje» «Canto») |
| **Dela Gothic One** | ✅ | ✅ | Onomatopeya gorda: «ヌルフフフ», «にゅやッ!» |
| **M PLUS Rounded 1c** (ExtraBold) | ✅ | ✅ | **Pantalla de Ritsu** y del móvil: letra de interfaz |
| **DotGothic16** | ✅ | ✅ | Pantalla de Ritsu si se quiere un toque de píxel |
| **Jost** | ✅ | ❌ | **La Futura libre**: el logo inglés y rótulos rectos |
| Yomogi | ✅ pero **la í sale con un hueco** detrás | ✅ | ❌ no usar con texto en español |
| Hachi Maru Pop | ✅ | ✅ | ⚠️ muy infantil; la «l» es rara |
| Kosugi Maru | ❌ **no trae tildes ni ñ** | ✅ | ❌ no usar |

Todas son **OFL** salvo Schoolbell y Kosugi Maru (**Apache 2.0**): libres,
también para uso comercial. La elección es **de estilo, no un calco** ⚠️.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 El «cuadro» de esta serie es la cara de Koro-sensei

Koro-sensei **siempre sonríe**; lo que cambia es **el color de su cara** ✅
([pixiv百科](https://dic.pixiv.net/a/%E6%AE%BA%E3%81%9B%E3%82%93%E3%81%9B%E3%83%BC),
[暗殺教室設定資料集](https://manga-data.com/assassinationclassroom-9/),
[昭和平成アニメ漫画倶楽部](https://sh-manga-anime.hatenablog.com/entry/ansatugyousitu_6),
[Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10160785065)):

| Cara | Qué significa | Uso en la lámina |
|---|---|---|
| Amarilla | normal | presentar |
| **Naranja con un círculo rojo (◯)** | **¡correcto!** | «Activa el aviso» = bien hecho |
| **Morada con una X** | **incorrecto** | «Aquí no se escribe» |
| Amarilla con **rayas verdes** | se burla, «lo tiene fácil» | «¿Te lo perdiste? No haber activado el aviso» |
| Rosa | pervertido | ❌ no usar |
| Blanca | serio | aviso importante |
| **Negra** | furia extrema | ❌ no en un canal de avisos |

La guía de cuadros del proyecto ya lo recogía (§30), marcado ⚠️; con
cuatro fuentes japonesas pasa a ✅.

### 7.2 Otros soportes de texto que tiene la serie

| Soporte | Dónde | Estado |
|---|---|---|
| **La pizarra verde** de la 3-E | toda la serie; en KJ-3 00:01:09 se habla de «escribir en la pizarra y borrar» | ✅ que existe; su letra ⚠️ |
| **Títulos «〜の時間» / «Hora de…»** | cada capítulo | ✅ |
| **La guía del viaje** (しおり), un libro de 2.400 páginas | T1 ep. 7 | ✅ |
| **El cuaderno de Nagisa** con los **puntos débiles de Koro-sensei**, numerados («弱点その…»). Llegan a **más de 30**; el 37, «si le sujetan muchos a la vez, se le puede atrapar», decide el final | manga y anime | ✅ ([ciatr](https://ciatr.jp/topics/315489), [情報サーガ](https://jouhousaga.com/assassination-classroom-koro-sensei-weak), [設定資料集](https://manga-data.com/assassinationclassroom-2/)); el número 37 ⚠️ |
| **La pantalla de Ritsu** y **Ritsu en los móviles** (モバイル律): se copia a los teléfonos de toda la clase para avisarles | T2 | ✅ ([pixiv百科](https://dic.pixiv.net/a/%E8%87%AA%E5%BE%8B%E6%80%9D%E8%80%83%E5%9B%BA%E5%AE%9A%E7%A0%B2%E5%8F%B0), [アニヲタWiki](https://w.atwiki.jp/aniwotawiki/pages/46313.html)) |
| **Pasar lista** (出欠) y **encargado del día** (日直: «起立！») | 2×24 00:07:18; peli 00:49:35 | ✅ |
| Los **exámenes personalizados** y las **clases con clones**: Koro-sensei se divide a Mach 20 y da clase de lengua, mates, sociales, ciencias e inglés a cada alumno a la vez | T1 | ✅ ([ficha oficial](https://www.ansatsu-anime.com/2014-2016/character/chara/chara_1.php), [Yahoo!ニュース](https://news.yahoo.co.jp/expert/articles/27738276398a6cb12bd7480651e0004560d0e32c)); que cada clon lleve **una cinta en la frente con la asignatura** ⚠️ de memoria |

### 7.3 Cómo habla cada uno (por el subtítulo)

| Quién | Cómo habla | Ejemplo (minuto) |
|---|---|---|
| **Koro-sensei** | Muy educado («〜です», «〜ですねえ»), exclamaciones de profe entusiasta, **se ríe «ヌルフフフ»**, se asusta «にゅやッ!». Dice «先生» de sí mismo («el profe») | 2×06, 00:00:02; 2×04, 00:16:34 |
| **Nagisa** | Narrador tranquilo, frases cortas, piensa en voz alta | 2×01, 00:00:30; 2×25, 00:22:07: «僕らにとっては 勇気をくれる魔法の言葉» (para nosotros, una palabra mágica que da valor) |
| **Karma** | Burlón y perezoso: «へ～え», «まっ いいけど» (bah, vale), «〜ちゃん» a las chicas | 2×01, 00:16:52; 2×02, 00:05:35: «やるね 茅野ちゃん» |
| **Irina** | Chula y mandona, llama «**ガキども**» (mocosos) y «**あんたたち**» a la clase; se derrite con Karasuma | 2×04, 00:05:14: «あんたたち 寄り道しないで帰りなさいよ» (ustedes, a casa sin entretenerse) |
| **Karasuma** | Seco, militar, frases cortas | 2×02, 00:13:33, a Koro-sensei, que ha soltado a los «presos» del juego de policías y ladrones a cambio de una revista: «物で釣られたな！» (¡te han sobornado!) |
| **Ritsu** | Educadísima, «はい！», datos exactos | peli, 00:14:38: «26秒08»; 2×07, 00:12:58: «はい 皆さん どうか ご無事で» |

### 7.4 Cómo se traduce a una lámina fija

1. **El texto principal va escrito con tiza en la pizarra**, no en un
   globo. Letra: Yusei Magic o Kalam.
2. **La emoción de cada aviso la pone la cara de Koro-sensei**: ◯ naranja
   para «activa el aviso», X morada para «aquí no se escribe».
3. **El título en formato de capítulo**: «Hora de clase» o «Hora de los
   avisos», como los títulos latinos de Crunchyroll.
4. Si habla Ritsu, su texto va **en su pantalla** o en **la notificación
   de un móvil**, con letra de interfaz redonda.
5. Si habla Nagisa, va **en su cuaderno**, con letra a lápiz (Klee One).
6. Las onomatopeyas «ヌルフフフ» pueden ir pequeñas, en katakana, junto a
   Koro-sensei (Dela Gothic One).
7. **2.ª pasada · la tiza tiene tres colores** con función: **rosa** para
   la palabra que avisa («対», dentro de un estallido dentado), **blanco**
   para el qué («二学期中間テスト»), **amarillo** para lo importante
   («苦手科目強化特訓») ✅ visto (2×06, 0:02; hoja `fotogramas_01` n.º 1).
   Así: «Clases de doblaje» en blanco, el día en amarillo, «¡Aviso!» en
   rosa.
8. **2.ª pasada · la cartela de lista**: en 2×24 (8:50) cada alumno sale
   con un rótulo gris claro abajo: **«Ⅲ-E〔7〕茅野カエデ»** (clase, número
   de lista entre corchetes, nombre) ✅ visto (hoja n.º 10). En la
   lámina: «Ⅲ-E〔1〕Clases de doblaje», «Ⅲ-E〔2〕Clases de canto».

### 7.5 En los videojuegos de la franquicia

**2.ª pasada: encontradas y miradas** en 7 capturas de prensa (Famitsu,
4Gamer), `partes/texto.md` ✅:

| Elemento | Cómo es |
|---|---|
| Etiqueta del nombre | Rectángulo **amarillo `#FFEA62`**, arriba a la izquierda de la caja, nombre en negro |
| Caja de texto | Fondo **crema `#F5F7E2` / `#FBFEED`** (no blanco puro), gótica negra gruesa, 2 líneas |
| Retrato | Busto **SD/chibi** (2 cabezas de alto) sobre el fondo del sitio |
| HUD de combate (2015) | «AP» en número arriba a la izquierda, arma en placa oscura arriba a la derecha, **globo verde lima** sobre el personaje, radar circular abajo |
| Combos | Texto grande en diagonal con contorno: «Critical Hit!», «2 HIT COMBO!!», «2 TRAP&CHAINS» |
| Estadísticas (2016) | **Radar rojo** (pentágono-heptágono): 気力, スタミナ, 腕力, スピード, 元気, 集中力, ワナLV |

Para la lámina: **etiqueta amarilla + caja crema + gótica negra** es la
«notificación» propia de la franquicia, mejor que inventar una burbuja.
Más en §13.

### 7.6 Qué NO hacer con el texto

- Una **burbuja blanca redonda** flotando.
- Una pizarra **negra** con tiza: en el aula japonesa es **verde**.
- Poner la cara **negra** o **rosa** de Koro-sensei en un aviso normal.
- Escribir «Bitch-sensei» en la lámina: es el mote, pero en un servidor
  hispano es un insulto y **no sé cómo lo dice el latino** (§10).

### 7.7 El aviso oficial de la franquicia (un modelo real)

Durante la reemisión del 10.º aniversario, la cuenta oficial publicó
**cada semana un aviso firmado por Koro-sensei**: el
**«#殺せんせーの抜き打ちテスト»** (el examen sorpresa de Koro-sensei).
Salía **los jueves a las 20:00**, desde el 2×01 (2 de octubre de 2025)
hasta el último capítulo, con premio para 10 acertantes ✅
([web del 10.º aniversario](https://www.ansatsu-anime.com/10th/news/detail.php?id=1128444),
[USEN encore](https://e.usen.com/news/news-release/tv-endergenic-infinity-karat.html),
[X, un aviso](https://x.com/ansatsu_anime/status/1973704527426552176),
[X, el último](https://x.com/ansatsu_anime/status/2037122482550038691)).

Así están escritos (texto de los resultados, sin abrir la imagen) ✅:

> 🎓🌕《 殺せんせーの抜き打ちテスト》🌕🎓
> ヌルフフフフ〜♪ みなさんがアニメ「#暗殺教室」再放送をちゃんと見ているか、
> 抜き打ちテストをおこないます✍️
> 🎯回答方法 …

> ⏰第25回テスト解答期間：第25話放送後～4/1(水)23:59
> 🎯解答方法 #殺せんせーの抜き打ちテスト をつけてXに解答を投稿

Traducción: «🎓🌕 Examen sorpresa de Koro-sensei 🌕🎓. ¡Nurufufufu~♪!
Voy a comprobar si están viendo la reemisión… ⏰ Plazo: … 🎯 Cómo
responder: …».

**Es el molde perfecto para el canal**: **la risa para abrir**, el
**birrete y la luna** (🎓🌕) como sello, y **⏰ cuándo / 🎯 cómo** en
líneas cortas. La lámina puede llevar esos dos iconos, dibujados con
tiza, junto a «Cuándo hay clase» y «Activa el aviso».

---

## 8 · Los personajes

Datos de carácter: resultados de búsqueda del
[Assassination Classroom Wiki](https://ansatsukyoshitsu.fandom.com/wiki/Korosensei)
(**ojo: la wiki de Fandom es `ansatsukyoshitsu`, no
`assassinationclassroom`** como decía el encargo),
[pixiv百科](https://dic.pixiv.net/a/%E6%BD%AE%E7%94%B0%E6%B8%9A),
la [ficha oficial](https://www.ansatsu-anime.com/2014-2016/character/chara/chara_1.php)
y los subtítulos. Lo que describo de memoria va con ⚠️.

### Koro-sensei (殺せんせー) — el profesor, 3.º en votos ✅

- **Qué es**: un ser amarillo con forma de pulpo, de **unos 3 metros**,
  que vuela a **Mach 20**. Destruyó el 70 % de la Luna y anuncia que
  destruirá la Tierra en marzo. Mientras, **pide ser profesor de la
  clase 3-E**, los peores del colegio, y el Gobierno ofrece **10.000
  millones de yenes** a quien lo mate ✅ (ficha oficial;
  [萌娘百科](https://zh.moegirl.org.cn/%E6%9D%80%E8%80%81%E5%B8%88);
  2×01, 00:00:30; KJ-2, 00:02:41 «賞金100億»).
- **Su nombre** es un juego: «殺せない» (no se puede matar) + «先生»
  (profesor). **Se lo puso Kayano** ✅ (2.ª pasada: manga cap. 1, pág. 48,
  citado por la [wiki](https://ansatsukyoshitsu.fandom.com/wiki/Korosensei), Etymology). En China le llaman **杀老师** o **黄老师**
  («el profe amarillo») ✅ (萌娘百科).
- **Carácter**: el **mejor profesor posible**. Se entrega a cada alumno,
  les prepara exámenes a medida, usa sus aficiones para enseñar (le hace
  a Takebayashi una canción con su anime favorito, KJ-3, 00:01:19) ✅.
  Es **un poco pervertido**: se deja sobornar con una revista (2×02,
  00:13:31) ✅. Goloso «casi al extremo», cotilla y algo mezquino ✅ (2.ª
  pasada: wiki, Personality; manga cap. 4). Aguri lo resume así si fuera
  humano: «un poco pervertido, listo, torpe, algo tacaño y terco» ✅
  (manga vol. 16, cap. 137). Odia conducir: tiene que seguir las normas
  de tráfico y es más lento que volar ✅ (wiki, Trivia). Un resultado
  chino cuenta que **vuela a Sichuan a comer mapo tofu** ⚠️
  ([萌娘百科](https://zh.moegirl.org.cn/%E6%9D%80%E8%80%81%E5%B8%88)).
- **Lo que le importa**: que sus alumnos **crezcan y se gradúen**. Su
  frase: «la vida es estudiar los 365 días» (peli, 00:49:27) ✅.
- **Su secreto** (spoiler del final): era un asesino humano, **el
  Segador** (死神), convertido en esto por un experimento. La profesora
  **Aguri Yukimura** le enseñó a enseñar; **la corbata con la luna** es
  regalo suyo ✅ ([Fandom](https://ansatsukyoshitsu.fandom.com/wiki/Korosensei),
  [Jump Database](https://jump.fandom.com/wiki/Korosensei); 2×16, 00:00:03).
- **Cómo se expresa**: con **el color de la cara** (§7.1). Se ríe
  «ヌルフフフ». Se asusta «にゅやッ!». Habla con cortesía de profe.
  Cuando se emociona, repite: «熱く！ 熱く！» (2×06, 00:00:10) ✅.
- **Lenguaje corporal** (2.ª pasada, visto en `fotogramas_01` n.º 1-2, 6
  y 7): sonrisa enorme fija ✅, ojillos pequeños, tentáculos juntos al
  celebrar (2×21, 0:18) ✅, **dos tentáculos como brazos** con dos
  «dedos» cada uno ✅ (Fandom); el resto le sirve de piernas. Levanta un
  tentáculo como un dedo índice para explicar ⚠️ de memoria.
- **Su cara en cada emoción** (2.ª pasada): amarilla lisa y contenta
  `#FCFF6D` (ep. 1, 1:35, «Sin retrasados. ¡Estupendo!») ✅; **rayas
  verdes** `#57DE54`, tono tranquilo pero amenazante (ep. 1, 3:00) ✅;
  celebrando con mejillas rosas (2×21, 0:18) ✅; cara blanca de póquer
  (hoja `personajes_02` n.º 70) ✅. Rabia, tristeza y miedo **sin
  fotograma** ⚠️ (las figuras DXF de Banpresto traen versión roja y negra,
  §18.6).
- **Datos** (§18.3): comida favorita **botan-ebi** en sushi; se dibuja a
  sí mismo como un pulpo; 3 m; cumpleaños 13 de marzo ✅.
- **Con quién**: con **toda la clase**. Rivalidad cómica con Karasuma;
  con Irina, bromas.

### Nagisa Shiota (潮田渚) — el protagonista, 2.º en votos ✅

- **Carácter**: tranquilo, observador y **subestimado**. Tiene **un
  talento natural para el asesinato** que nadie ve venir ✅
  ([ciatr](https://ciatr.jp/topics/315489)).
- **Qué hace**: **lleva un cuaderno** con los **puntos débiles de
  Koro-sensei** (más de 30) ✅ (§7.2). Es **el narrador** de la serie ✅.
- **Aspecto**: pelo **azul claro en dos coletas** (`#B8E1FC` luz,
  `#6B8CB4` sombra), bajito (159 cm), cara de chica ✅ (2.ª pasada: hoja de
  modelo de Lerche, `personajes_01` n.º 5; arte del 10.º aniv., n.º 18). El director del doblaje latino eligió
  **una voz femenina** porque el personaje es **andrógino y misterioso**
  ✅ (Doblaje Wiki).
- **Miedos y familia**: una madre controladora (Hiromi) ✅ (en latino, la
  dobla la madre real de su actriz, §10).
- **Al final**: **se hace profesor** y dice «授業を始めます！»
  (¡empieza la clase!) en la última escena (2×25, 00:22:50) ✅.
- **Cómo se expresa**: voz baja, frases cortas, sonrisa amable que
  **de repente da miedo** (2×25, 00:22:28: «殺せるといいね！») ✅ el texto y ✅ la
  cara (2.ª pasada: sonrisa lateral serena, `fotogramas_01` n.º 15).
- **Su cara en cada emoción**: la hoja de expresiones de Lerche
  (`personajes_01` n.º 6) trae **sonrisa, enfado, sorpresa y «cara de
  demonio»** (dientes afilados, ojos en blanco) ✅. **Tristeza, miedo y
  vergüenza sin fotograma** con minuto ⚠️ (no se hallaron en el material
  visto).
- **Datos** (2.ª pasada, wiki): le gusta el **inglés**, no las ciencias;
  su afición es **investigar** los puntos débiles de Koro-sensei; con la
  recompensa quiere **crecer**; lo describen como «herbívoro» (草食系,
  poco lanzado en el amor) ✅.
- **Con quién**: **Karma** (su mejor amigo y opuesto), **Kayano** (su
  compañera de asiento; **Kayano está enamorada de él en el canon** ✅,
  2.ª pasada: infobox de la wiki y caps. 142 y 144 del manga), Koro-sensei.

### Karma Akabane (赤羽業) — **el más votado**, 1.º ✅

- **Carácter**: listo, **burlón y un poco sádico**; buscabroncas. **Es el
  primer alumno que consigue herir a Koro-sensei** ✅
  ([Anime-Planet](https://www.anime-planet.com/characters/karma-akabane),
  [aniSearch](https://www.anisearch.com/character/48141,karma-akabane)).
- **Aspecto**: **pelo rojo**, ojos amarillos, **uniforme desabrochado**,
  **chaqueta negra abierta sin corbata**, camisa blanca, cinturón de
  hebilla cuadrada ✅ (2.ª pasada: hoja de modelo firmada de Lerche,
  30-may-2014, `personajes_01` n.º 3). Pelo `#D84646`-`#E86060`.
- **Manías**: bebe **las bebidas lácteas «～煮オ・レ»** (no zumo) ✅ (2.ª
  pasada, wiki); lleva un **cuchillo mariposa de espuma anti-sensei hecho
  por él** ✅; colecciona especias ✅. Las bromas con **wasabi y mostaza**
  y grabar con el móvil ⚠️ de memoria.
- **Su cara**: seria, cejas bajas, boca recta (2×24, 7:51, `fotogramas_01`
  n.º 9) ✅; sonrisa burlona en el arte del 10.º aniv. ✅. Tristeza, miedo
  y vergüenza sin fotograma ⚠️.
- **Futuro**: acaba de funcionario en el Ministerio de Economía (ep. 47)
  ✅.
- **Cómo se expresa**: arrastra las palabras («へ～え», «まっ いいけど»),
  llama «〜ちゃん» a las chicas (2×02, 00:05:35) ✅. En la última lista
  **es el primero en contestar** (2×24, 00:07:51) ✅.
- **Con quién**: **Nagisa**; rival de **Gakushū Asano** (clase A) ✅;
  hace equipo con Okuda (2×01, 00:05:37) ✅, la de química ⚠️.

### Irina Jelavić (イリーナ・イェラビッチ) — 5.ª en votos ✅

- **Qué es**: **asesina profesional** que entra como **profesora de
  inglés** de la 3-E para matar a Koro-sensei ✅
  ([Fandom](https://ansatsukyoshitsu.fandom.com/wiki/Irina_Jelavi%C4%87),
  [anihk](https://anihk.com/en/character/irina-jelavic-assassination-classroom)).
- **Su arma**: la seducción y **hablar muchos idiomas** (una fuente dice
  diez ⚠️). Su lema: «Life is nudity; admire it» ✅ (manga vol. 4,
  cap. 27). Primer asesinato a los 12 años ✅ (wiki).
- **El mote «Bitch-sensei» (ビッチ先生)**: los alumnos le cambian el
  apellido (Jela**vić** → «bitch»). Sale **39 veces** en los subtítulos
  de la T2 ✅. **Lo empieza Karma** ✅ (wiki, Trivia). En el doblaje
  inglés es «Professor Bitch» ✅ (2.ª pasada: infobox de la wiki). **En
  latino no sé cómo le llaman** ❌ (2.ª pasada: no está en el wikitext de
  Doblaje Wiki ni en las búsquedas).
- **Carácter**: al principio **cruel y creída**; cuando se le cae la
  máscara es **infantil, torpe y enamoradiza** ✅ (Fandom).
- **Aspecto**: **rubia**, pelo ondulado hasta la cadera con raya al
  medio, **ojos azul claro**, alta ✅ (Fandom).
- **Con quién**: **Karasuma**, de quien se enamora y con quien **acaba
  casada** ✅ (Fandom); lo celebra en 2×07, 00:06:22 («やば… 超うれしい»).
  Con la clase, pasa de despreciarlos a **quererlos**.
- **Cómo se expresa**: grita «キ～ッ！» (peli, 00:12:04), insulta a la
  clase («ガキども»), se ríe «ウフフフフ» cuando trama algo (2×02,
  00:12:17), y pasa a «バカバカバカ 死ね 私！» (¡tonta, tonta, tonta!)
  cuando se avergüenza (2×01, 00:14:30) ✅. **2.ª pasada, visto**: a las
  14:31 la cara entera rosa `#E29ECB`, ojos «＞＜», boca dentada
  gritando, manos tirándose del pelo (`fotogramas_01` n.º 12) ✅.
  Emocionada con el regalo: ojos verde-azulados con rayitas de sonrojo
  (2×07, 6:22, n.º 13) ✅. **Enfadada** («キ～ッ！», peli 2016, 12:04) sin
  fotograma: la película entera no está en Internet Archive ni
  Dailymotion ⚠️.
- **Ropa de trabajo**: traje sastre **azul verdoso pálido `#90AFBA`**,
  gargantilla negra, pelo `#E3AD67` ✅ (render oficial, `personajes_02`
  n.º 65).

### Tadaomi Karasuma (烏間惟臣) — 4.º en votos ✅

- **Qué es**: agente del Ministerio de Defensa que hace de **profesor de
  educación física** y entrena a la clase para matar ⚠️ de memoria el
  ministerio; ✅ que da «体育» (2×02, 00:10:58).
- **Datos** (2.ª pasada, wiki): lema «si es posible, sigue el plan; si no,
  hazlo igual» (manga vol. 1, extra) ✅; le gustan los perros pero le
  ladran ✅; come hamburguesas o fideos instantáneos ✅; su sonrisa asusta
  hasta a perros entrenados ✅; con Irina tiene **una hija** (databook
  *Graduation Album*) ✅. Llama a Irina «Sweetheart» en inglés ✅.
- **Carácter**: serio, justo, el adulto responsable ✅ (§7.3).
- **Con quién**: Irina (§ arriba), Koro-sensei (le exaspera).

### Ritsu (律, «自律思考固定砲台») — la alumna máquina

- **Qué es**: **un arma con inteligencia artificial** mandada desde
  **Noruega**, matriculada como alumna; la clase la llama **Ritsu** ✅
  ([pixiv百科](https://dic.pixiv.net/a/%E8%87%AA%E5%BE%8B%E6%80%9D%E8%80%83%E5%9B%BA%E5%AE%9A%E7%A0%B2%E5%8F%B0),
  [ficha E-27](https://www.ansatsu-anime.com/2014-2016/character/chara/chara_e27.php)).
- **Aspecto**: **una caja negra alta con una pantalla** donde se ve a una
  chica de pelo largo ⚠️ el color (no hay fotograma en las hojas).
  Koro-sensei se gastó en remodelarla 17 009 000 ¥ en el anime (100 000
  en el manga) y **se quedó con 5 ¥** ✅ (2.ª pasada, wiki). Los alumnos la llaman «**caja moe**»
  (萌え箱) ✅ (2×04, 00:16:47).
- **«Ritsu móvil» (モバイル律)**: se copia en **los móviles de toda la
  clase** para comunicarse con todos, y **se cambia mucho de ropa** en el
  móvil ✅ ([pixiv百科](https://dic.pixiv.net/a/%E8%87%AA%E5%BE%8B%E6%80%9D%E8%80%83%E5%9B%BA%E5%AE%9A%E7%A0%B2%E5%8F%B0),
  [アニヲタWiki](https://w.atwiki.jp/aniwotawiki/pages/46313.html)).
  **Es literalmente un sistema de notificaciones.**
- En la película **hace de encargada del día** y manda «¡de pie!» (peli,
  00:49:39 a 00:49:50) ✅.

### Los secundarios que conviene tener a mano

| Personaje | Por qué | Estado |
|---|---|---|
| **Kaede Kayano** (茅野カエデ) | compañera de pupitre de Nagisa; **le puso el nombre a Koro-sensei**; esconde un secreto que estalla en la T2 (2×14-2×15): es **Akari Yukimura**, hermana de Aguri, actriz con el nombre Haruna Mase. **Spoiler: no usar en la lámina.** Le gusta el pudín y el karaoke. Sale llorando en la lista (2×24, 8:50) | ✅ (2.ª pasada: wiki, infobox y Trivia) |
| **Yūma Isogai** (磯貝悠馬) | delegado: es quien dice «全員 起立！» (2×25, 00:01:04) | ✅ |
| **Gakushū Asano** (浅野学秀) | el primero de la clase A, rival de Karma | ✅ ([namu](https://namu.wiki/w/%EC%95%94%EC%82%B4%EA%B5%90%EC%8B%A4/%EC%9D%B8%EA%B8%B0%ED%88%AC%ED%91%9C): 5.º en votos) ⚠️ |
| **Terasaka** (寺坂) | el bruto que acaba siendo buena gente | ✅ (peli 00:49:25) |
| **Takebayashi** (竹林) | el otaku de las gafas; protagonista del «竹林の時間» | ✅ (KJ-1 a KJ-3) |

---

## 9 · ¿Quién es el más querido?

**Encuesta oficial de personajes (Weekly Shōnen Jump)** ✅
([マンバ](https://manba.co.jp/topics/11417/comments/23411),
[暗殺教室設定資料集](https://manga-data.com/assassinationclassroom-3/),
[ジャンプ速報](http://jumpsokuhou.com/archives/40224817.html)):

| Puesto | Personaje | Votos |
|---|---|---|
| 1 | **Karma Akabane** | **432** (81 chicos, 331 chicas) |
| 2 | Nagisa Shiota | 315 |
| 3 | **Koro-sensei** | 292 (el más votado por chicos: 138) |
| 4 | Tadaomi Karasuma | 209 |
| 5 | Irina Jelavić | 143 |
| 9 | Kaede Kayano | 63 (2.ª pasada) |

**2.ª pasada · reparto del voto** (extra del tomo 12, citado por la wiki
en cada ficha) ✅: Karma **80 % chicas** (jumpsokuhou daba 81 chicos y
331 chicas, que no suma 432 ⚠️: me quedo con el porcentaje del tomo);
Nagisa 67 % chicas; Karasuma 72 % chicas; **Irina 61 % chicos**; Kayano
58 % chicos. Los chicos del podio los votan chicas, y al revés.

**Otras medidas** (2.ª pasada, `partes/voz.md` y `datos-voz.md`) ✅:
- **AniList, favoritos**: 1.º Karma (10 568), 2.º Koro-sensei (9 729),
  3.º Nagisa (6 882), 4.º Karasuma, 5.º Irina, 6.º Kayano.
- **Danbooru, dibujos de fans** (1003): **1.º Nagisa (520)**, 2.º Karma
  (220), 3.º Koro-sensei (165), 4.º Kayano (152). **El fandom
  internacional dibuja más a Nagisa**, aunque vote a Karma.

- Hubo pocos votos porque **sólo dejaban votar una vez por persona** ✅
  (ジャンプ速報). Una fuente japonesa dice que fue **la única** encuesta
  oficial ⚠️; **Namuwiki (coreano) habla de más encuestas**, y en la
  quinta ganó **Nagisa** ⚠️ ([namu](https://namu.wiki/w/%EC%95%94%EC%82%B4%EA%B5%90%EC%8B%A4/%EC%9D%B8%EA%B8%B0%ED%88%AC%ED%91%9C)).
- **Encuesta de fans** (にじめん, «con quién quieres ser amigo» y «el más
  popular»): **1.º Karma** ✅
  ([にじめん](https://nijimen.kusuguru.co.jp/topics/558964),
  [Excite](https://www.excite.co.jp/news/article/Nijimen_0000000000510401/)).

**Conclusión para la lámina**: el protagonista (Nagisa) **no es el más
votado**: lo es **Karma**. Pero la cara de la serie, la que reconoce
cualquiera, es **Koro-sensei**, y para un canal de clases **el profesor
es el que habla**. Propuesta: **Koro-sensei habla, Karma y Nagisa
reaccionan** (ver §19).

---

## 10 · Doblaje latino

**Sí hay doblaje latino.** Lo encargó **Funimation** (anunciado en
**septiembre de 2020**) y se hizo en **The Kitchen**, que tiene estudio en
**Cuernavaca (México)** y en Miami ✅
([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Assassination_Classroom),
[ANMTV](https://www.anmtvla.com/2020/09/funimation-mexico-assassination.html),
[Otaku Press](https://www.otakupress.pe/2020/09/assassination-classroom-doblaje-funimation.html)).
Hoy está en **Crunchyroll**, las dos temporadas ✅
([T1](https://www.crunchyroll.com/es/watch/GD9UVDXEN/assassination-time),
[T2](https://www.crunchyroll.com/es/watch/G14U42MWP/reaper-time-part-2)).

**2.ª pasada**: la API de Doblaje Wiki **sí respondió** (22 509
caracteres de wikitext). Cada nombre, con la tabla de reparto y la
página propia del actor o AniList (`partes/voz.md`):

| Personaje | Voz latina | Fuentes | Estado |
|---|---|---|---|
| **Koro-sensei** | **Carlos Segundo** (Piccolo, Woody, Snape) | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Assassination_Classroom) · [ANMTV](https://www.anmtvla.com/2020/09/funimation-carlos-segundo-interpretara.html) · [TierraGamer](https://tierragamer.com/noticias/assassination-classroom-doblaje-latino-koro-sensei/) · [YouTube](https://www.youtube.com/watch?v=BnvoCg6wLLI) | ✅ |
| Koro-sensei humano (el Segador) | **Carlos Olízar**, hijo de Carlos Segundo | Doblaje Wiki: reparto + «Datos de interés», texto literal | ✅ (2.ª pasada) |
| **Nagisa Shiota** | **María José Moreno** | [Doblaje Wiki: M. J. Moreno](https://doblaje.fandom.com/es/wiki/Mar%C3%ADa_Jos%C3%A9_Moreno) · [aniSearch](https://www.anisearch.com/character/48184,nagisa-shiota) · [YouTube](https://www.youtube.com/watch?v=LlL2IJ8F3FA) | ✅ |
| Hiromi Shiota (madre de Nagisa) | **Yanelly Sandoval**, madre de María José Moreno en la vida real | Doblaje Wiki, «Datos de interés», texto literal | ✅ (2.ª pasada) |
| **Karma Akabane** | **Iván Fernández** | [Doblaje Wiki: Iván Fernández](https://doblaje.fandom.com/es/wiki/Iv%C3%A1n_Fern%C3%A1ndez) · [aniSearch](https://www.anisearch.com/character/48141,karma-akabane) · [YouTube](https://www.youtube.com/watch?v=bdtsyXTrIac) | ✅ |
| **Irina Jelavić** | **Cristina Hernández** (Sakura Card Captor); sus diálogos se grabaron en **Mérida, Yucatán** | [Doblaje Wiki: C. Hernández](https://doblaje.fandom.com/es/wiki/Cristina_Hern%C3%A1ndez) · [YouTube](https://www.youtube.com/watch?v=GyvKeiQklRw) · infobox (`pais2`) | ✅ |
| **Ritsu** | **Leyla Rangel** | reparto de Doblaje Wiki + AniList + [YouTube](https://www.youtube.com/watch?v=Rf0CQagzmKg) | ✅ (2.ª pasada) |
| **Tadaomi Karasuma** | **Juan Carlos Román** | reparto + [su página](https://doblaje.fandom.com/es/wiki/Juan_Carlos_Rom%C3%A1n) + AniList + [YouTube](https://www.youtube.com/watch?v=_LWQ5nIwOH4) | ✅ (2.ª pasada) |
| **Kaede Kayano** | **María García** | reparto + [su página](https://doblaje.fandom.com/es/wiki/Mar%C3%ADa_Garc%C3%ADa) + AniList | ✅ (2.ª pasada) |
| Ryoma Terasaka | **Luba Flores**, acreditada como «Benjamín Flores» | reparto + AniList | ✅ |
| Rio Nakamura · Hiroto Maehara · Yuma Isogai | Nadia Yanin Lujambio · Emiliano Montaño · Elliot Leguizamo | reparto + AniList | ✅ |
| Hinata Okano · Megu Kataoka · Hinano Kurahashi | Camila Vázquez · Jessica Monzón · Estephania «Effy» Estrada | reparto (+ AniList en Kataoka y Kurahashi) | ✅ / ⚠️ Okano sólo una |
| Tomohito Sugino · Yukiko Kanzaki | Erick Padilla · Dayana Santiaguillo | reparto + AniList | ✅ |
| Itona Horibe · Gakushū Asano · Gakuhō Asano | Carlos Siller · Eduardo Martínez · Arturo Mercado Jr. | sólo AniList («Spanish» mezcla España y Latinoamérica) | ⚠️ |
| Padre de Nagisa | Ignacio Pineda (eps. 23 y 47) | reparto | ⚠️ una |
| **Director de doblaje** | **Iván Fernández** (el mismo de Karma) | infobox de Doblaje Wiki + «Datos de interés» | ✅ (2.ª pasada) |

**Ficha técnica** (infobox de Doblaje Wiki, 2.ª pasada): estudio **The
Kitchen, L.L.C.**, Cuernavaca (Morelos); supervisión creativa **Enrique
Garduza**; traducción y adaptación **Denisse Leguizamo** (y **Elizabeth
Hernández** en la 2.ª mitad de la T2); gerencia **Diego Cabra Becerril**;
grabado en **2020**; 47 episodios ✅ (una fuente estructurada + ANMTV en
la fecha).

**Datos del doblaje** (Doblaje Wiki, «Datos de interés», texto literal
leído en la 2.ª pasada ✅):
- Nagisa tiene **voz femenina** porque, según el director, es un
  personaje misterioso y andrógino: «quitar las etiquetas y valorar las
  habilidades de cada persona».
- Ep. 18: se dice «marica». En ese mismo ep., insertos hablados traducen
  el título como «**Aula de Asesinato**»; en el último, «Assassination
  Classroom».
- Ep. 21: «**Me amarraron como puerco**» (guiño a *El Show de la
  Barandilla*).
- Ep. 32: Koro-sensei **silba la canción de Gohan** de *Dragon Ball Z:
  Goku es un Super Saiyajin*.
- Ep. 46: algunos gritos de Koro-sensei y Nagisa se dejan **en inglés**.
- En Funimation y Bitme hay **letreros en español** para los kanji en
  pantalla; en Crunchyroll no.
- Koro-sensei, **ep. 43**: «**Eres mi alguacil favorito**», guiño a Woody,
  que también es Carlos Segundo. El ep. 43 en total es el **2×21**.
- Terasaka, **ep. 39** (2×17): «**Es como la llave del Santo**».
- Hay un **blog de fans** que imagina el reparto si se hubiera doblado en
  Ciudad de México ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Usuario_Blog:SavageShadowX/Si_Assassination_Classroom_fue_doblada_en_la_Ciudad_de_M%C3%A9xico_en_lugar_de_Cuernavaca)):
  el doblaje de Cuernavaca **tuvo críticas** entre los fans ⚠️ (lo deduzco
  del título, no lo leí).
- Al estrenar la T2 en Crunchyroll, el **ep. 15 salió desincronizado** ⚠️.

**Los títulos latinos**: «**Hora de…**» ✅ (ver §6.1).

**Frases latinas de Koro-sensei**: aparte del «alguacil», **no encontré
con fuente** cómo dice el latino «ヌルフフフ», «手入れ» o «ビッチ先生».
**2.ª pasada**: tampoco. YouTube pide iniciar sesión (403 al bajar), las
muestras de audio de Doblaje Wiki vienen vacías para esta serie y no hay
clips oficiales doblados en Dailymotion ❌. **No hay frases latinas
textuales con minuto** en esta biblia: sólo las de «Datos de interés»,
con episodio.
Para oírlo: [«Voz de Koro-Sensei»](https://www.youtube.com/watch?v=BnvoCg6wLLI),
[«KORO-SENSEI | ESPAÑOL LATINO»](https://www.youtube.com/watch?v=g17J4SG2fOw),
[short](https://www.youtube.com/shorts/xdoGsTdEPOc).
**Minutos sin verificar.**

**Para un servidor de doblaje**: Carlos Segundo va a convenciones y
saluda como Koro-sensei (TikTok, [EXPOMAC Veracruz 2022](https://www.tiktok.com/@rebecavirgen/video/7186783988743261446)) ⚠️ sin ver.

Otros: hay **doblaje de España** (ficha en [eldoblaje.com T1](https://www.eldoblaje.com/datos/FichaPelicula.asp?id=48203),
[T2](https://www.eldoblaje.com/datos/FichaPelicula.asp?id=53461)) ⚠️ sin
abrir. De la **película de 2026 no encontré doblaje latino** ❌ (2.ª
pasada: tampoco en ANMTV, Doblaje Wiki ni eldoblaje.com).

---

## 11 · Música

| Tema | Canción | Intérprete | Estado |
|---|---|---|---|
| T1, opening 1 | **«青春サツバツ論»** (*Seishun Satsubatsu-ron*) | **3年E組うた担** (las voces de Nagisa, Kayano, Karma, Sugino y Okajima ⚠️) | ✅ |
| T1, opening 2 | «自力本願レボリューション» (*Jiriki Hongan Revolution*) | 3年E組うた担 | ✅ |
| T2, opening 1 | «QUESTION» | 3年E組うた担 | ✅ |
| T2, opening 2 | «バイバイ YESTERDAY» | 3年E組うた担 | ✅ |
| T1, ending | «Hello, Shooting Star» | moumoon | ✅ (visto en ep. 1, 21:16) |
| T2, endings | «欠けた月» y «また君に会える日» | 宮脇詩音 (Shion Miyawaki) | ✅ (2.ª pasada: wiki + créditos vistos en 2×06, 21:16; «また君に会える日» cierra el ep. 47, infobox de la wiki) |
| Canción de despedida | «旅立ちのうた» | 3年E組うた担 | ✅ (2.ª pasada: es el **insert del ep. 46**, cuando muere Koro-sensei; infobox [Episode 46](https://ansatsukyoshitsu.fandom.com/wiki/Episode_46)) |
| Película de **2016** «365日の時間» | ending **«始業のベル»** | 宮脇詩音 | ✅ (2.ª pasada: la wiki no dice de qué película es; es la de 2016, visto en la tarjeta del featurette oficial, [Dailymotion x8o319m](https://www.dailymotion.com/video/x8o319m), 0:42) |
| Película de **2026** «みんなの時間» | tema **«Teacher»** (4-mar-2026) | 友成空 (Tomonari Sora), letra, música y arreglo | ✅ ([avex](https://avexnet.jp/news/1031557), [OTOTOY](https://ototoy.jp/news/127524)) |
| Reemisión 10.º aniversario (T2, desde octubre 2025) | OP «ENDER» / ED «Infinity karat» | GENIC / 七海うらら | ✅ ([LisAni!](https://www.lisani.jp/0000289326/), [avex](https://avex.jp/genic/news/detail.php?id=1127328)) |

**2.ª pasada · la reemisión del 10.º aniversario entera** (abr-2025 a
mar-2026; wiki + webs oficiales, `partes/video.md`):

| Tramo | Original | Reemisión |
|---|---|---|
| T1 ep. 1-11, OP | «青春サツバツ論» | «Kiiro Shingo» · 友成空 ⚠️ una fuente, sin kanji comprobado |
| T1 ep. 12-22, OP | «自力本願レボリューション» | **«ラストルック» (Last Look)** · 須田景凪, en antena 26-jun-2025 ✅ ([animatetimes](https://www.animatetimes.com/news/details.php?id=1750317224), [web del artista](https://www.tabloid0120.com/news/2025/06/19/5336/)) |
| T1, ED | «Hello, Shooting Star» | **«ツキノフネ» (Moon Ship)** · ATARAYO, 9-abr-2025 ✅ ([ANN](https://www.animenewsnetwork.com/press-release/2025-04-09/anime-series-lsquo-assassination-classroom-rsquo-new-ending-theme-song-lsquo-moon-ship-rsquo-by-/.223371), [Tokyohive](https://www.tokyohive.com/article/2025/04/atarayo-releases-new-single-moon-ship-theme-song-for-assassination-classroom-rebroadcast)) |
| T2 ep. 23-36 | «QUESTION» / «欠けた月» | «ENDER» · GENIC / «Infinity karat» · 七海うらら ✅ |
| T2 ep. 37-47 | «バイバイ YESTERDAY» / «また君に会える日» | «Setsuna Blossom» / «Spica» ⚠️ una fuente (wiki); «Spica» sonó en el ep. 47 ✅ (infobox) |

**La escena que hace llorar** (ep. 46, la muerte de Koro-sensei) suena
con **«旅立ちの歌»** ✅. Para un aviso especial de «fin de curso».

Fuentes: [Fandom](https://ansatsukyoshitsu.fandom.com/wiki/Assassination_Classroom_Openings_and_Endings),
[animate](https://www.animate-onlineshop.jp/pd/1391684/),
[CDJournal](https://www.cdjournal.com/i/i_disc.php?dno=4116030386),
[アニソンライブラリー (13 temas)](https://japan-anime-song.com/ansatsukyoushitsu-anison/).

**Del subtítulo del Blu-ray** (letras con su minuto) ✅:
- El opening de 2×01 empieza en **00:00:54**: «君のことばかり思ってる …
  必ずそのハートを射止める 誓う» (sólo pienso en ti… juro que te
  acertaré en el corazón). **Canción de amor que es de asesinato**: el
  tono de toda la serie.
- El ending de 2×01 (00:21:36): «夜空に泳ぐ月だって 手を伸ばせば届くの»
  (hasta la luna que nada en el cielo se alcanza si estiras la mano).
- El ending de 2×24 (00:15:43): «風が吹いてる 僕の肩押すよう … 進むべき
  道は今 せんせー(アナタ)の先へと» (sopla el viento como empujándome…
  el camino sigue más allá de ti, **profe**).

**Qué ambiente dan**: los openings son **pop alegre y cantado por la
clase**, con una **coreografía** que los fans imitan (§14). Los endings,
baladas nostálgicas. **Para #avisos-clases**: el tono del opening
(alegre, de grupo), no el de los endings.

---

## 12 · Vídeos

> [!note] 2.ª pasada: vídeos mirados de verdad
> YouTube sigue pidiendo iniciar sesión (lista formatos hasta 1080p, pero
> la descarga da 403) y TikTok no se abre. Se miraron en **Internet
> Archive** y **Dailymotion** (tabla de abajo y §2.5). Los enlaces de
> YouTube de la tabla siguiente siguen **sin minuto** salvo que se diga.

| Vídeo mirado (2.ª pasada) | Minuto | Qué se ve |
|---|---|---|
| [PV oficial de la T2](https://www.dailymotion.com/video/x3kret1) (Dailymotion, 2:24, 512×288 ⚠️) | 0:24 | Luna creciente de noche |
| | 0:42 | Tarjeta de **Karma (赤羽業), CV 岡本信彦** |
| | 1:00 | Irina en una cafetería |
| | 1:24 | **Koro-sensei con gafas de sol haciendo un globo de chicle**, en el bosque |
| | 1:30 | «大波乱の二学期が始まる» (empieza un segundo trimestre caótico) |
| | 2:00-2:18 | Reparto y estreno: **7-ene-2016**, Fuji TV y otras |
| [Featurette de la película de 2016](https://www.dailymotion.com/video/x8o319m) (1:15) | 0:18-0:36 | Un personaje pelirrojo adulto mira el aula vieja vacía |
| | 0:42 | Tarjeta «始業のベル 宮脇詩音» |
| | 1:06 | Se proyecta junto a «殺せんせーQ!» |
| [Episodio 1 entero](https://archive.org/details/AnsatsuKyoushitsuEpisode001480pX264) (Internet Archive, 23:17) | 0:00-1:15 | Aula apuntando a Koro-sensei; se regenera de un disparo |
| | 3:15-4:30 | Título-crédito en vez de opening (§2.5) |
| | 21:16 | Ending, luna creciente |
| [T2, episodios 1, 6, 7, 21, 24 y 25](https://archive.org/details/ansatsu-kyoushitsu-2x-23_20260520) | ver §2.5 | Pizarra, celebrar, lista, Nagisa profesor |

**Tráiler de la película de 2026** fuera de YouTube: no lo encontré
(Dailymotion y Internet Archive) ⚠️.

| Vídeo | Para qué |
|---|---|
| [【本予告】 película 2026](https://www.youtube.com/watch?v=Mbc1i7QZW9E) (15-dic-2025) | Estilo actual, luz, el edificio viejo |
| [【公開直前PV】](https://www.youtube.com/watch?v=DzyXvNclj6c) (16-mar-2026) | Idem |
| [【本編冒頭映像】 el principio de la película](https://www.youtube.com/watch?v=HtOZQ0pYyWk) | **El aula**, primeros minutos |
| [Prime Video, escena 1](https://www.youtube.com/watch?v=TSYV_SCpiLg) · [tráiler 1](https://www.youtube.com/watch?v=32jmT2zLyQY) | Escenas sueltas |
| [**課外授業編, los 8 episodios**](https://www.youtube.com/watch?v=iETpifp-27Y) (oficial) | **Las escenas KJ de §2** con su minuto sumando la duración ⚠️ |
| [Película «365日の時間» entera](https://www.youtube.com/watch?v=fu96ROh7FH8) (oficial, tiempo limitado; [Famitsu](https://www.famitsu.com/article/202603/69932)) | Resumen de la serie |
| [Todos los openings 1-4](https://www.youtube.com/watch?v=LgstopNj7Lo) · [OP y ED completos + película](https://www.youtube.com/watch?v=vUL0DyNsnZI) | **La coreografía del opening** |
| Voces latinas: [Koro-sensei](https://www.youtube.com/watch?v=BnvoCg6wLLI), [Nagisa](https://www.youtube.com/watch?v=LlL2IJ8F3FA), [Karma](https://www.youtube.com/watch?v=bdtsyXTrIac), [Irina](https://www.youtube.com/watch?v=GyvKeiQklRw), [Ritsu](https://www.youtube.com/watch?v=Rf0CQagzmKg) | Cómo suena cada uno en latino |
| TikTok: [risa de Koro-sensei](https://www.tiktok.com/discover/koro-sensei-laugh-scene?lang=en), [«intro meme»](https://www.tiktok.com/discover/assassination-classroom-intro-meme), [edits](https://www.tiktok.com/discover/koro-sensei-edits), [voz de Karma en español](https://www.tiktok.com/discover/voz-de-karma-akabane-en-espa%C3%B1ol) | Tendencias (§14) |

---

## 13 · Videojuegos de la franquicia

| Juego | Qué es | Estado |
|---|---|---|
| **暗殺教室 殺せんせー大包囲網!!** (*Grand Siege on Koro-sensei*), 3DS, Bandai Namco, **12-mar-2015** | Acción: con la clase, **trampas y armas anti-Koro-sensei** contra el reloj. Con todos rodeándole se activa la «**Fever Time**». Escenarios: **el edificio viejo, el nuevo, el monte y la piscina**. Hay conversaciones y eventos de vida escolar; también puedes ser Koro-sensei y huir | ✅ ([4Gamer](https://www.4gamer.net/games/278/G027887/20150227043/), [Nintendo](https://www.nintendo.co.jp/titles/50010000030916), [電撃](https://dengekionline.com/elem/000/000/982/982279/)) |
| **暗殺教室 アサシン育成計画!!** (*Assassin Training Plan*), 3DS, **24-mar-2016** | **Eres un alumno nuevo de la 3-E**: exámenes, eventos y asesinatos **de la matrícula a la graduación**. Modo en el que **eres Koro-sensei y «cuidas» (お手入れ) a los alumnos** | ✅ ([Famitsu](https://www.famitsu.com/news/201512/14095312.html), [Nintendo](https://www.nintendo.co.jp/titles/50010000039635), [web](https://ansatsu-game.bn-ent.net/)) |

- **La interfaz y las cajas de diálogo**: 2.ª pasada, **vistas** en 7
  capturas de [4Gamer](https://www.4gamer.net/games/278/G027887/20150227043/)
  y [Famitsu](https://www.famitsu.com/news/201603/18101425.html) ✅. Tabla
  completa en §7.5. En el de 2015: persecución en tercera persona por las
  calles, **conos de tráfico**, cronómetro arriba a la izquierda,
  «HIT COMBO» y «TRAP&CHAINS». En el de 2016: diálogos con retrato SD
  (viaje a Kioto) y el mismo motor de combate. La caja del juego de 2015
  es **verde y amarilla** ✅.
- Ninguno salió fuera de Japón ⚠️ (no hay ficha en MobyGames).
- Koro-sensei es **jugable en *J-Stars Victory VS*** (Bandai Namco, 2014),
  el único de la serie ✅ (2.ª pasada: [Kanzenshuu](https://www.kanzenshuu.com/2013/12/18/j-stars-victory-vs-assassination-classroom-and-neuro-additions/),
  [GameFAQs](https://gamefaqs.gamespot.com/boards/694309-j-stars-victory-vs/68113308)).
  En *Jump Force* no está confirmado ⚠️.
- **Koro-Sensei Quest!** (殺せんせーQ!): juego de móvil con chibis; la
  ropa de bruja de Irina (`personajes_01` n.º 28) y los chibis de Nagisa y
  Karma (`personajes_02` n.º 75-76) son de ahí ✅ (wiki + featurette 2016,
  1:06).

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen

- **La risa «Nurufufufu»** (en TikTok hay búsquedas enteras de ella) ✅
  ([TikTok](https://www.tiktok.com/discover/koro-sensei-laughing?lang=en)).
- **Las caras de colores** de Koro-sensei, sobre todo **las rayas
  verdes** (la cara de «qué fácil») y el **◯ / ✕** ✅.
- **El baile del opening** con las armas ✅ ([TikTok](https://www.tiktok.com/discover/assassination-classroom-intro-meme)).
- **Koro-sensei hecho piñata** por los alumnos ⚠️ (un resumen de TikTok).
- **2.ª pasada · el duelo hispano en TikTok**: «La muerte de Koro Sensei
  me jodió la vida 😭» ([@tuotako](https://www.tiktok.com/@tuotako/video/7535555036768718102)),
  «nunca podré superar la muerte de koro-sensei»
  ([@otaku_caricaturas](https://www.tiktok.com/@otaku_caricaturas/video/7221695944784416005)) ✅;
  etiquetas `#korosenseideathedit` y `#assassinationclassroomedit`; un
  género entero de «Koro Sensei Edits» ✅ (vistas sin contar ⚠️).
- **El gusto por los dulces** «casi al extremo» ✅ (wiki, manga cap. 4).
- **Karma** y sus bromas; la pareja **Karma y Nagisa** (el visual de la
  película 2026 los pone juntos) ✅.
- **La lista del final** (2×24) y el **«felicidades por graduarse»**: la
  escena que hace llorar a todos ✅ (§2.1, 2×24).
- Koro-sensei como **el profesor ideal**: hay artículos para profes de
  verdad ([selfsg](https://www.selfsg.com/post/ansatsukyoshitu)) ⚠️.

### Qué NO hacer (lo que un fan notaría)

- **Koro-sensei sin su sonrisa**: nunca la pierde, ni enfadado.
- **Cinco dedos** en sus tentáculos: tiene **dos** por «mano».
- **La luna de la corbata** en el birrete: va **en la corbata**.
- **La Luna llena** en el cielo de noche: siempre **creciente**.
- **Pizarra blanca**, aula moderna de cristal: la 3-E es **de madera y
  vieja**. (2.ª pasada: la pizarra **sí se ve casi negra**, verde muy
  oscuro `#272726`; lo que no va es una pizarra blanca o verde clara.)
- **Koro-sensei conduciendo tan tranquilo**: odia conducir ✅ (wiki).
- **Nagisa y Kayano «sólo amigos»**: ella está enamorada de él en el
  canon ✅. Y **no revelar** que Kayano es Akari Yukimura: es un giro de la
  T2.
- **Nagisa con cara de malo** o de chica en sentido sexual: es un chico
  andrógino, tímido.
- **Karma serio y formal** con el uniforme abrochado (va con la chaqueta
  abierta y sin corbata, hoja de modelo ✅).
- **Irina con la ropa de bruja morada** como si fuera del anime: es del
  juego *Koro-Sensei Quest!* ✅.
- **Irina sin Karasuma cerca** si se la pone enamorada; y **sin el mote
  en inglés** en la lámina (§7.6).
- **Burlarse de la escena final**: para el fandom es sagrada.
- **Colores apagados y tristes**: la serie es luminosa, de colegio.

---

## 15 · Poses analizadas por personaje

> [!warning] Cómo leer esta sección
> El **minuto y lo que se dice** están comprobados en el subtítulo ✅.
> **2.ª pasada**: las filas marcadas **«visto»** se miraron en el
> fotograma (Internet Archive, 480p; hoja `fotogramas_01.jpg`). Las demás
> siguen con la postura deducida ⚠️. Antes de recortar, mira el fotograma
> en ese minuto.

### Koro-sensei

| # | Escena | Qué dice | Postura probable ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 2×06, 00:00:02 | «さあさ 皆さんさん ２週間後は…中間テストですよ… 熱く！» | **visto**: delante de la pizarra, **traje ceremonial oscuro con cuello dorado y sombrero de paja**, tentáculos en alto como puños (`fotogramas_01` n.º 1-2) ✅ | **presentar / animar** |
| 2 | 2×21, 00:00:13 → 0:18 | «第２志望以内で全員合格！ おめでとうございます … 本来 この後 進路相談の予定でしたが» (¡Todos aprobados! Felicidades… después tocaba orientación) | **visto** (0:18): primer plano, **tentáculos juntos como aplaudiendo**, mejillas rosas, boca enorme, burbujas, pizarra detrás (n.º 6) ✅ | **celebrar** y **anunciar un cambio de plan** |
| 3 | 2×23, 00:00:02 | «皆さん さっきの授業で 言い忘れていたことがあります» | serio, de frente | **explicar** algo importante |
| 4 | 2×24, 00:07:18 → 7:21 | «最後に出欠を取ります» | **visto**: con el **libro de asistencia negro «出席簿»** en los tentáculos, toga y cordón amarillo; de noche y **al aire libre**, en el monte, no en el aula (n.º 7-8) ✅ | **pasar lista** (serio) |
| 5 | 2×04, 00:16:34 | «ヌルフフフフ で どうでした？» | pícaro, se inclina hacia el alumno | **preguntar** |
| 6 | 2×02, 00:11:06 | «全員 捕まったら 宿題２倍デシタネ» | amenaza de broma; cara de rayas verdes probable | **regañar** en broma |
| 7 | peli, 00:49:25 | «人生は 365日 勉強です» | a Terasaka, con un tentáculo en alto | **explicar / regañar** |
| 8 | KJ-3, 00:01:35 → 00:01:58 | «そこで！» … «おっほん» y canta mal | pose de cantante; ideal para **clases de canto** | **animar** |
| 9 | peli, 00:07:43 | «にゅやッ！ いいんですか？» | sobresalto, tentáculos abiertos | **sorpresa** |

### Nagisa

| # | Escena | Qué dice | Postura probable ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 2×25, 00:21:33 | «チャイムが鳴ったから席に着いて…» | **visto**: de pie en un aula con grafitis, **manos juntas por delante**, rodeado de alumnos; camisa blanca, chaleco gris, corbata oscura (n.º 14) ✅ | **presentarse** con calma |
| 2 | 2×25, 00:22:28 | «殺せるといいね！ 卒業までに» | **visto**: perfil, **sonrisa lateral suave**, mirada de reojo (n.º 15) ✅ | **animar** con carácter |
| 3 | 2×25, 00:22:50 | «席に着いて 授業を始めます！» | **visto**: de frente, sonrisa tranquila, pelo `#ABC6D5` (n.º 16) ✅ | **presentar**: «empieza la clase» |
| 4 | 2×21, 00:00:05 | «う… 受かったあ～» | alivio, mirando el resultado | **celebrar** |
| 5 | 2×24, 00:09:22 | responde «はい» en la lista | llorando y de pie | emoción (no para avisos) |
| 6 | 2×17, 00:00:05 | «殺せんせーの命を助ける方法を» | propone algo a la clase | **pensar / proponer** |
| 7 | T1 (cuaderno) | apunta los puntos débiles | escribiendo, cabeza baja | **tomar nota** (concepto B) |

### Karma

| # | Escena | Qué dice | Postura probable ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | 2×24, 00:07:51 | primer «はい» de la lista | **visto**: primer plano nocturno, cejas bajas, boca recta, chándal con «E» (n.º 9) ✅ | seriedad |
| 2 | 2×01, 00:16:42 | «はあ？ 祭り？» | desganado, manos en los bolsillos | **pereza** («¿otra clase?») |
| 3 | 2×02, 00:05:35 | «やるね 茅野ちゃん» | sonrisa de lado | **elogiar** |
| 4 | 2×02, 00:20:05 | «真犯人は別にいた» | detective, señala | **explicar** |
| 5 | 2×03, 00:07:30 | «シロの性格は大体分かった» | analiza, mano en la barbilla | **pensar** |
| 6 | KJ-5, 00:02:00 | «寺坂さあ 政治家なんなよ» | burla a un amigo | **picar / animar** |
| 7 | 2×01, 00:19:09 | «返金のために 5000円も投資したんじゃないのよ» | tramando algo | **tramar** |

### Irina

| # | Escena | Qué dice | Postura probable ⚠️ | Sirve para |
|---|---|---|---|---|
| 1 | peli, 00:08:16 | «夏場の露出と 女を駆使する暗殺者は…» | pose de seducción (verano) | ❌ no para este canal |
| 2 | 2×04, 00:05:14 | «あんたたち 寄り道しないで帰りなさいよ» | se despide de las alumnas, mandona | **avisar / regañar** con cariño |
| 3 | 2×02, 00:12:17 | «ウフフフフ» | trama, escondida | **pensar** |
| 4 | 2×07, 00:06:22 | «やば… 超うれしい» | **visto**: primerísimo plano de los ojos, iris verde-azulado, rayitas de sonrojo (n.º 13) ✅ | **celebrar** |
| 5 | 2×01, 00:14:30 → 14:31 | «バカバカバカ 死ね 私！» | **visto**: cara rosa `#E29ECB`, ojos «＞＜», boca dentada abierta, **manos en el pelo** (n.º 12) ✅ | vergüenza |
| 6 | peli, 00:12:04 | «キ～ッ！» | rabieta | **enfado cómico** |
| 7 | 2×01, 00:08:13 | «あー やってらんない！» | harta | hartazgo |

### Ritsu

| # | Escena | Qué dice | Sirve para |
|---|---|---|---|
| 1 | peli, 00:49:39 → 00:49:50 | «スリープモードを解除 起動 … それでは 皆さん 起立！» | **presentar el aviso** (concepto C) |
| 2 | 2×02, 00:11:53 | «岡島さん 速水さん 千葉さん 不破さん アウト～» | **anunciar resultados** |
| 3 | 2×07, 00:12:58 | «はい 皆さん どうか ご無事で» | despedirse |
| 4 | 2×13, 00:17:49 | «離婚届です» | **explicar con datos** |

**Poses de las hojas de la wiki** (2.ª pasada): Koro-sensei de cuerpo
entero con tentáculos abiertos (`personajes_02` n.º 69) y con papeles en
la mano (`personajes_01` n.º 41); Karma de pie, relajado (`personajes_01` n.º 16)
y con un brazo extendido al frente (`personajes_02` n.º 71; visto a
tamaño de hoja ⚠️); Nagisa señalando con el
brazo extendido (`personajes_01` n.º 18); Irina de pie, cadera ladeada
(`personajes_02` n.º 65) ✅.

**Para presentar**: Koro-sensei 1 o Nagisa 3. **Explicar**: Koro-sensei 3
o 7. **Celebrar**: Koro-sensei 2, Irina 4. **Regañar**: Koro-sensei 6,
Irina 2. **Pensar**: Karma 5. **Animar**: Koro-sensei 8, Nagisa 2.

---

## 16 · Vestuario

| Quién | Ropa icónica | Estado |
|---|---|---|
| **Koro-sensei** | **Toga académica** gris carbón `#2D2D2D` (no negro puro) con **forro rojo** `#A2393C`, **vivos morados en los puños** (sin medir ⚠️), **birrete con borla amarilla**, **cordón dorado** y **corbata con la luna creciente** (regalo de Aguri). Cuerpo `#FFF661` | ✅ ([Fandom](https://ansatsukyoshitsu.fandom.com/wiki/Korosensei), [Jump Database](https://jump.fandom.com/wiki/Korosensei); 2.ª pasada: hex medidos en el arte del 10.º aniv., `personajes_01` n.º 17) |
| Koro-sensei, traje ceremonial | **traje oscuro con cuello ancho dorado y sombrero de paja** al anunciar el examen | ✅ visto (2×06, 0:02) |
| Koro-sensei, verano | **gafas de sol** y globo de chicle | ✅ visto (PV T2, 1:24) |
| Koro-sensei, disfraces | se viste de mujer y de mil cosas para disimular | ✅ (萌娘百科) |
| **Uniforme de Kunugigaoka, chicos** | **americana gris**, camisa blanca; se permite chaqueta de punto o chaleco | ✅ una fuente ([アニメ！アニメ！](https://animeanime.jp/article/2018/11/29/41744.html)); hay uniforme oficial de COSPA ([chaqueta chico](https://www.geestore.com/detail/id/00000061474)) |
| **Uniforme, chicas** | chaqueta con **ribete negro** en cuello y puños, falda | ✅ la prenda existe ([COSPA chaqueta](https://www.cospa.com/cospatio/detail/id/00000061484), [falda](https://www.geestore.com/detail2/id/00000061486)); el color ⚠️ |
| **Nagisa** | **chaleco azul marino** `#2E355C`-`#384068`, camisa blanca `#F0F0F0` remangada, **corbata negra**, pantalón gris `#A0A0B0` con bolsillos, botines; coletas azules `#B8E1FC`/`#6B8CB4` | ✅ (2.ª pasada: hoja de modelo de Lerche y arte del 10.º aniv., `personajes_01` n.º 5 y 18; la corbata es **negra**, no roja) |
| **Nagisa adulto** (profesor) | camisa blanca, chaleco gris, corbata oscura | ✅ visto (2×25, 21:33) |
| **Karma** | **chaqueta negra `#403C3C` abierta, sin corbata**, camisa blanca, cinturón de hebilla cuadrada, pantalón gris `#A0A0B0`/`#6E6B7D`, botines; pelo `#D84646`-`#E86060` | ✅ (2.ª pasada: hoja de modelo firmada de Lerche, 30-may-2014, `personajes_01` n.º 3) |
| **La clase en la T2** | el «**超体育着**» (supertraje de gimnasia): traje de combate que les dan para las misiones | ✅ (se vende como disfraz: [ITOCOS](https://www.itocos.com/assassination-classroom-nagisa-karma-super-pe/p3206.html), [COSTOWNS](https://www.costowns.com/nagisa-shiota-p_12768.html)); cuándo sale ⚠️ |
| **Irina** | **traje sastre azul verdoso pálido `#90AFBA`** (chaqueta entallada abierta, falda corta), **gargantilla negra**, medias y tacones, pintalabios-arma; pelo `#E3AD67`; chal (2×01, 00:12:27: «こんなショール») | ✅ (2.ª pasada: render oficial, `personajes_02` n.º 65) |
| Irina, otras | vestido de la campaña de la T2 (`personajes_01` n.º 2) ✅; **bruja morada = juego *Koro-Sensei Quest!*, no anime** ✅ | |
| **Karasuma** | traje oscuro y corbata | ⚠️ de memoria |
| **Ritsu** | en la pantalla, uniforme; en el móvil **cambia mucho de ropa** | ✅ que cambia; el resto ⚠️ |

**Lo que todos reconocen**: Koro-sensei con **toga, birrete y la corbata
de la luna**; Nagisa con **chaleco azul y coletas**; Karma **pelirrojo con
el uniforme abierto**. En la lista final (2×24) la clase lleva **chándal
oscuro con una «E»** ✅ visto (n.º 8-10).

---

## 17 · Paisajes y fondos de pantalla

### Los sitios, con su luz (2.ª pasada: vistos los marcados; ver §5)

| Sitio | Hora y luz |
|---|---|
| Aula de la 3-E | día: blanca y cálida por las ventanas, madera `#CAC1AA`/`#8B7F69` ✅ visto (2×24, 9:29) |
| Edificio viejo por fuera | día: cielo `#2964DC`, monte `#2D372A` ✅ visto (2×21, 0:13) |
| Pasillo de madera del edificio viejo | tarde: dorado; **es el sitio del visual de la película 2026** ✅ |
| El monte y el bosque | verde intenso, sol entre árboles |
| Noche en el monte | azul marino `#14214E` con nubes moradas, **luna creciente** ✅ visto (2×24, 7:09) |
| Edificio nuevo (clase A) | blanco y frío, luz de fluorescente ⚠️ de memoria |
| Instituto de Nagisa adulto | aula gris llena de grafitis, pupitres revueltos ✅ visto (2×25, 21:33) |

### Fondos de pantalla con tamaño real (2.ª pasada, API de Wallhaven)

Todos de fans (licencia de uso personal de Wallhaven; no oficiales):

| Enlace | Tamaño | Autor | Qué |
|---|---|---|---|
| [wallhaven-8311qo](https://w.wallhaven.cc/full/83/wallhaven-8311qo.jpg) | 3000×2000 | SamUerto | Koro-sensei solo |
| [wallhaven-vmo1q3](https://w.wallhaven.cc/full/vm/wallhaven-vmo1q3.jpg) | 3508×2294 | CrisEVA01 | Koro-sensei |
| [wallhaven-k9qo3d](https://w.wallhaven.cc/full/k9/wallhaven-k9qo3d.png) | 1920×1080 | RaidyHD | Nagisa, «imagen en imagen», fácil de recortar |
| [wallhaven-yjelxl](https://w.wallhaven.cc/full/yj/wallhaven-yjelxl.png) | 1920×1200 | CrisEVA01 | Nagisa, Karma, Kayano |
| [wallhaven-w86kex](https://w.wallhaven.cc/full/w8/wallhaven-w86kex.jpg) | 1920×1080 | CrisEVA01 | Nagisa, Karma, Koro-sensei, Kayano |
| [wallhaven-0q567q](https://w.wallhaven.cc/full/0q/wallhaven-0q567q.jpg) | 1920×1080 | (borrado) | cara sonriente sobre amarillo, minimalista |
| [wallhaven-r2zz8j](https://w.wallhaven.cc/full/r2/wallhaven-r2zz8j.png) | 1920×1080 | SamUerto | hojas y cuchillo |
| [wallhaven-5dwgd9](https://w.wallhaven.cc/full/5d/wallhaven-5dwgd9.png) | 1920×1080 | Warezed | Koro-sensei inquietante |

**Fondos oficiales para descargar**: 2.ª pasada, **siguen sin
aparecer** ❌ (`ansatsu-anime.com/10th/wallpaper/` da 404; la sección
`/2014-2016/special/` no tiene «壁紙» ni «wallpaper»).

### Fondos de la 1.ª pasada (sin descargar; medidas según el sitio)

| Enlace | Tamaño | Autor |
|---|---|---|
| [WallpaperFlare: Koro-sensei y Nagisa](https://www.wallpaperflare.com/assassination-classroom-wallpaper-anime-koro-sensei-nagisa-shiota-wallpaper-qukei) | 2560×800 (panorámico) | sin autor ⚠️ |
| [WallpaperFlare: búsqueda «assassination classroom»](https://www.wallpaperflare.com/search?wallpaper=assassination+classroom) | hay de 3840×2160 ⚠️ | varios |
| [WallpaperFlare: búsqueda «koro-sensei»](https://www.wallpaperflare.com/search?wallpaper=koro-sensei) | varios | varios |
| [アニメ壁紙.com, id 1456482781](https://animekabegami.com/detail?id=1456482781) | 1158×1600 (vertical) | ⚠️ |
| [tsundora: 殺せんせー](https://tsundora.com/122245) | ⚠️ | ⚠️ |
| [getwallpapers (79 imágenes)](https://getwallpapers.com/collection/assassination-classroom-wallpapers) | varios | ⚠️ |

Muchos de estos «fondos» son **arte oficial sin crédito** (portadas,
visuales). **Buscar siempre el original** en la web oficial (§3.1).
**Fondos oficiales para descargar: no encontré** ❌. Para el 10.º
aniversario hay **ilustraciones nuevas de los endings** de la
reemisión (se venden en acrílico) ⚠️ ([Mercari](https://jp.mercari.com/item/m24912068683)).

---

## 18 · Guía para generar con IA (Firefly, Canva)

> Sólo para **fondos, objetos y poses de apoyo**. Los personajes se
> recortan de fotogramas u oficiales (regla 3 del dueño), no se inventan.

**Rasgos que nunca cambian**
- Koro-sensei: **cabeza redonda amarilla y lisa** (`#FFF661`), **sonrisa
  enorme fija con muchos dientes**, **ojos de punto negro pequeños**,
  toga gris carbón `#2D2D2D` con forro rojo `#A2393C`, birrete con borla
  amarilla, cordón dorado, corbata con luna creciente. **Dos dedos** por
  tentáculo-brazo. Nunca pierde la sonrisa.
- Nagisa: pelo azul claro `#B8E1FC` en **dos coletas cortas**, ojos
  azules, chaleco azul marino `#2E355C`, camisa blanca remangada,
  **corbata negra**. Bajito, cara andrógina.
- Karma: pelo rojo `#D84646`, ojos ámbar, **chaqueta negra abierta sin
  corbata**, cinturón de hebilla cuadrada, sonrisa de lado.
- Irina: rubia `#E3AD67`, pelo largo ondulado con raya al medio, ojos
  verde-azulados, traje sastre `#90AFBA`, gargantilla negra.
- Aula 3-E: **madera vieja**, **pizarra verde casi negra** (`#272726`),
  ventanas grandes de cuarterones, pupitres de madera y metal.
- Cielo nocturno: **luna en creciente fijo**, azul marino `#14214E`.

**Estilo de dibujo (medido, §18.1)**: anime de TV de 2015. En los
personajes, **sombreado plano de dos tonos** (82-86 % de la imagen) y
**línea de color, no negra** (gris-marrón `#5C4C4D`, `#4E5358`), poca
línea. En los fondos, **pintura con degradados suaves** y casi sin línea.
Colores **saturados y claros**, brillo medio.

**Palabras que ayudan** (inglés para Firefly):
`old wooden Japanese classroom, very dark green chalkboard with pink,
white and yellow chalk writing, warm daylight through large paned
windows, wooden desks, dust in the light, anime background art, 2015 TV
anime style, flat two-tone cel shading, colored lineart, soft painted
background, wooden school building on a forested mountain, deep blue
night sky with crescent moon`.
Para personajes de apoyo, el vocabulario de Danbooru que entienden las
IA (del recolector): Nagisa `blue_hair, short_twintails, blue_eyes, vest,
black_necktie, white_shirt, kunugigaoka_middle_school_uniform`; Karma
`red_hair, yellow_eyes, black_jacket, open_jacket, white_shirt,
black_belt, grey_pants, knife`; Irina `blonde_hair, long_hair,
wavy_hair, parted_bangs, choker, suit, pencil_skirt`.

**Palabras que lo estropean**: `white board`, `modern classroom`,
`glass walls`, `realistic photo`, `dark gritty`, `horror`, `octopus`
(sale un pulpo de verdad), `full moon`, `3D render`, `black lineart`
(la línea es de color), `crossdressing` (etiqueta frecuente de Nagisa
en Danbooru: **evitarla**), `chibi` salvo que se quiera el estilo de
*Koro-Sensei Quest!*.

**Encuadre**: plano medio desde los pupitres, con uno desenfocado
delante; cámara a la altura de un alumno sentado. Las emociones fuertes
de Koro-sensei se cierran mucho en su cara (para que se vea el color)
✅ (visto en 2×21, 0:18).

**Vocabulario de expresiones** (para pedir cada gesto):
- **La cara de Koro-sensei cambia de color** (§7.1): amarilla lisa =
  normal; **rayas verdes** `#57DE54` = se burla («qué fácil»); naranja
  con ◯ rojo = correcto; morada con ✕ = mal; rosa = pervertido; negra =
  furia. Mejillas rosas y **burbujas blancas** = celebra (2×21, 0:18).
- **Ojos «＞＜»** y cara entera rosa = vergüenza cómica (Irina, 2×01,
  14:31). **Rayitas diagonales de sonrojo** bajo los ojos = emoción
  tímida (Irina, 2×07, 6:22).
- **«Cara de demonio»** de Nagisa: dientes afilados, ojos en blanco (hoja
  de Lerche, `personajes_01` n.º 6).
- **Sonrisa lateral serena** = calma que da miedo (Nagisa, 2×25, 22:28).
- **SD/chibi** (2 cabezas): el estilo de los juegos (retratos de 3DS y
  *Koro-Sensei Quest!*).

**Referencias de estilo**: arte del 10.º aniversario (`personajes_01`
n.º 16-18), aula vacía (`fotogramas_01` n.º 11), edificio de día (n.º
5), pizarra con tiza (n.º 1-2), el visual de la película 2026 (pasillo,
§3.2). **Referencias de pose**: §15 (filas «visto») y los recortes
`personajes_02` n.º 65, 69 y 71.

### Guía para una IA de texto (cómo escriben en su voz)

**Koro-sensei**: profe cortés y entusiasta. Habla en «です/ます», repite
cuando se anima («¡Con ganas! ¡Con ganas!»), ríe «**Nurufufufu**»
(ヌルフフフ), se asusta «**¡Nyuya!**» (にゅやッ), convierte todo en
lección. Signos: muchos **¡!**, alguna tilde alargada («～»). En latino,
guiños a su actor (Woody). Títulos «**Hora de…**».
**Nagisa**: frases cortas, suaves, observador; a veces una frase amable
que da miedo. **Karma**: arrastra las palabras («Heeee…», «Bueno, da
igual»), llama «-chan» a las chicas, se burla. **Irina**: mandona y
creída, grita «¡Kiii!» cuando se enfada, se ríe «Ufufufu» cuando trama.
**Karasuma**: seco, militar, frases cortas. **Ritsu**: educada, de
máquina («Salgo del modo reposo»).

**Frases reales, por emoción** (japonés con su minuto, §2 y §15;
traducción de la biblia):

| Emoción | Quién | Frase | Dónde |
|---|---|---|---|
| Alegre | Koro-sensei | «第２志望以内で全員合格！ おめでとうございます» (¡Todos aprobados! ¡Felicidades!) | 2×21, 0:13 |
| Alegre | Irina | «やば… 超うれしい» (Ay… qué feliz) | 2×07, 6:22 |
| Alegre | Karma | «やるね 茅野ちゃん» (Bien hecho, Kayano-chan) | 2×02, 5:35 |
| Enfadado | Irina | «キ～ッ！» / «あー やってらんない！» (¡Ya no aguanto!) | peli 2016, 12:04 / 2×01, 8:13 |
| Enfadado | Karasuma | «物で釣られたな！» (¡Te han sobornado!) | 2×02, 13:33 |
| Explicando | Koro-sensei | «人生は 365日 勉強です 卒業の１秒前まで 授業は続きますよ» (La vida es estudiar los 365 días; hasta un segundo antes de graduarse, la clase sigue) | peli 2026, 49:25 |
| Explicando | Karma | «真犯人は別にいた» (El verdadero culpable era otro) | 2×02, 20:05 |
| Animando | Koro-sensei | «熱く行きましょう！ 熱く 熱く！» (¡Con ganas! ¡Con ganas!) | 2×06, 0:02 |
| Animando | Ritsu | «それでは 皆さん 起立！» (Bien, todos, ¡de pie!) | peli 2026, 49:35 |
| Animando | Nagisa | «席に着いて 授業を始めます！» (A sus asientos. Empieza la clase) | 2×25, 22:50 |
| Triste | Koro-sensei | «最後に出欠を取ります 一人一人 先生の目を見て…» (Por último, voy a pasar lista…) | 2×24, 7:18 |
| Triste | Nagisa | «卒業おめでとう» (Felicidades por graduarse) | 2×24, 17:08 |
| Vergüenza | Irina | «バカバカバカ 死ね 私！» (¡Tonta, tonta, tonta!) | 2×01, 14:30 |

**Frases del doblaje latino** (textuales, con episodio, de Doblaje Wiki;
**sin minuto** ⚠️): Koro-sensei «**Eres mi alguacil favorito**» (ep. 43);
«**Me amarraron como puerco**» (ep. 21); Terasaka «**Es como la llave del
Santo**» (ep. 39); título «**Aula de Asesinato**» (ep. 18). No se
encontraron más (§10).

**No hacer**: burlarse de la lista final o de la muerte de Koro-sensei;
poner «Bitch-sensei» en un texto del servidor; revelar el secreto de
Kayano.

---

### 18.1 · Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Quién lo hizo** ✅: estudio **Lerche**; director **Seiji Kishi**;
guion **Makoto Uezu**; diseño de personajes **Kazuaki Morita**
([AniList](https://anilist.co/anime/20755/staff), [web oficial](https://www.ansatsu-anime.com/2014-2016/special/special0001.php));
manga de **Yūsei Matsui** (antes *Neuro*, después *El joven Ashigaru
astuto*; [にじめん](https://nijimen.kusuguru.co.jp/topics/605488)).
Entrevista Kishi y Uezu en [Comic Natalie](https://natalie.mu/comic/pp/ansatsu)
⚠️ (sólo el titular: el cuerpo dio 403).

**Cómo dibuja Matsui**: imaginó primero la escena clave del cap. 1
(págs. 2-3) y construyó la historia alrededor ⚠️ (paráfrasis de
にじめん). Cuida mucho **el blanco** (余白) de la página
([Oricon](https://www.oricon.co.jp/news/2069215/), «松井優征が語る"白"のこだわり»;
el texto completo es de pago ⚠️). Qué programa usa: **no lo encontré** ❌.
En las páginas miradas (cap. 43 y 59): **viñetas cortadas en diagonal**,
una viñeta en **estallido dentado**, agua con **trama de puntos
gruesa**, sombras en **negro sólido**, follaje con **rayado a mano** ✅
(`partes/imagen.md`; `personajes_01` n.º 10).

**Cómo está pintado el anime, medido con `estilo.py`** ✅:

| Imagen | Sombreado | Línea | Color de línea |
|---|---|---|---|
| Arte del 10.º aniversario (3 piezas) | plano, 82-86 % | poca (2,3-3,2 %) | gris-marrón `#5C4C4D`, `#3A392A`, `#4E5358` |
| Fondo del edificio (2×24) | degradado, 60-72 % | 0-2,4 % | verdoso `#9DAF97` o nada |
| Interior con luz (2×06) | mixto: 29-50 % degradado | 3,9-4,8 % | marrón `#7F704B`, `#605E50` |

**En Photoshop**: línea de 2-4 px (a 2000 px de ancho) en **gris-marrón
`#4E4A4A`**, no negra; sombra en capa Multiplicar con **borde duro**, un
solo tono por zona; en la cabeza de Koro-sensei un brillo oval blanco al
40-60 % en Trama arriba a la izquierda; los fondos, en cambio, con
aerógrafo suave en varias capas.
**En Blender**: Freestyle 1,5-2,5 px en gris-marrón (o Solidify
invertido); **Shader to RGB + Color Ramp de 2-3 escalones** sobre un
Principled mate; luz de área grande y suave más un relleno tenue; Eevee
con Bloom suave para ventanas y luna. Modelos: el aula y los pupitres CC
BY de §4.1. Para Koro-sensei como objeto, la cabeza esférica de la
película de imagen real (`personajes_02` n.º 62-63) y el cosplay de
poliestireno (§4.2) dan el volumen ✅.

**Encuadres**: plano medio desde los pupitres; primeros planos muy
cerrados de la cara de Koro-sensei en las emociones; la clase de
espaldas en fila para los momentos solemnes (2×24, 7:29) ✅.

### 18.2 · Punto 19 · Texturas 2D

- **Trama de manga**: [*[FREE] Manga Screentone Pack 1*](https://assets.clip-studio.com/en-us/detail?id=2142037)
  (CLIP STUDIO ASSETS, gratis con cuenta) ✅; generador de trama libre
  [evestera/svg-halftone](https://github.com/evestera/svg-halftone)
  (MIT) ✅. Qué trama usa Matsui: no confirmado ⚠️.
- **Papel y madera** (CC0, ambientCG): Paper006, WoodFloor043,
  PaintedWood009C ✅ (§4.1).
- **Tiza**: se pinta (no hay pizarra en ambientCG ❌); tres colores rosa,
  blanco y amarillo (§7.4).
- **Crayón del ending**: trazo blanco sobre sepia `#E8744C` (2×06, 21:38)
  ✅, para un fondo «de cuaderno».
- **Emblema de Kunugigaoka o de la 3-E**: **no lo encontré** ❌
  (búsquedas 「椚ヶ丘中学校 校章」, 「E組 エンブレム」). Lo que usa el fandom es
  la **letra «E»** (va en el chándal de la clase, visto en 2×24) y
  «Ⅲ-E» en las cartelas.
- **Luna creciente** de la corbata y del cielo: el símbolo de la serie.

### 18.3 · Punto 20 · Gustos y detalles de cada personaje

Wiki de la serie (cita volumen y capítulo del manga) + AniList; ✅ donde
coinciden, ⚠️ donde sólo está la wiki (`partes/voz.md`).

| Quién | Cumpleaños | Altura | Sangre | Come / bebe | Afición | Lleva siempre | Odia |
|---|---|---|---|---|---|---|---|
| **Koro-sensei** | 13 de marzo (puesto, no real) | 3 m | AB | **botan-ebi** en sushi; dulces | dibujarse como pulpo | la corbata con la luna, regalo de Aguri | conducir |
| **Nagisa** | 20 de julio | 159 → 160 cm | A | no consta | investigar puntos débiles | su cuaderno | ciencias |
| **Karma** | 25 de diciembre | 175 → 185 cm | AB | bebidas **～煮オ・レ**; colecciona especias | hacer rabiar | cuchillo mariposa de espuma, hecho por él | japonés (asignatura) |
| **Irina** | 10 de octubre | 170 cm | — | no consta | seducir; idiomas | pintalabios-arma | que le recuerden la edad ⚠️ |
| **Karasuma** | 15 de agosto | 180 cm | — | hamburguesas o fideos instantáneos | ninguna declarada | — | — (le ladran los perros) |
| **Kayano** | 9 nov. (real) / 9 ene. (falso) | 143 → 157 cm | AB | **pudín** | puntuar en el karaoke | — | educación física |
| **Ritsu** | 1 de enero (como Gakushū) | 170 cm | — | «recarga» | fabricar objetos de plástico | — | que la hackeen |

**Cómo se ven a sí mismos**: Koro-sensei se dibuja siempre como un pulpo;
Nagisa se sabe el más débil y apuesta por observar; Kayano se ve primero
como un arma de venganza y luego quiere «ser una mujer capaz» ✅ (wiki).

### 18.4 · Punto 21 · Por qué la gente la ama

- **Ventas**: más de **27 millones** de copias (oct-2023) ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Assassination_Classroom));
  7.º manga más vendido de Japón en 2013, 10.º en 2014 y **4.º en 2015**
  (8 605 861) ✅ ([ANN](https://www.animenewsnetwork.com/encyclopedia/manga.php?id=15018)).
- **Premios**: **1.º en *Kono Manga ga Sugoi! 2014*** (lectores
  hombres); nominado al Manga Taishō, al Tezuka (2015) y al Eisner (2016);
  **51.º** en el *Manga Sōsenkyo 2021* de TV Asahi ✅.
- **Qué dicen**: «By the end of episode 1 I was crying like a baby»
  (Kei_z, 10/10); «the sound… made you tear up» (KittyNom, 9/10) ✅
  ([MAL](https://myanimelist.net/anime/26243/Ansatsu_Kyoushitsu_2nd_Season/reviews)).
  El motivo que más se repite: **el contraste** entre la premisa absurda
  y un mensaje real sobre **el valor de cada alumno** ✅
  ([hilo de MAL](https://myanimelist.net/forum/message/46792292?goto=topic)).
- **Con quién se identifican**: con **Nagisa**, el débil que encuentra su
  talento (el más dibujado, §9), y con **Karma** (el más votado) ✅.
- **Las escenas que hacen llorar**:
  - **2×24 (ep. 46), 7:05-9:45: la última lista**. De noche, al aire
    libre, Koro-sensei con el 出席簿; primeros planos de cada alumno
    diciendo «はい», varios llorando (Kayano con su cartela, 8:50) ✅
    visto. Termina en el aula vacía de día (9:29).
  - **Ep. 46: la muerte de Koro-sensei**, con el insert **«旅立ちの歌»**.
    Los alumnos lloran **uno a uno, encadenados** (primero Nagisa, al
    final Nagisa otra vez) y él **se deshace en luz dejando sólo la
    ropa** ✅ ([wiki, Episode 46](https://ansatsukyoshitsu.fandom.com/wiki/Episode_46)).
  - **Ep. 47: siete años después**, Nagisa profesor; suena «また君に会える日»
    ✅.
  - **Reírse**: Irina muerta de vergüenza (2×01, 14:31); Koro-sensei
    sobornado con una revista (2×02, 13:31) ✅.
- **Reddit**: r/AssassinationClassroom no responde en Arctic Shift (0
  resultados) ❌.

### 18.5 · Punto 22 · Fan dubs y comunidad hispana

- *«Assassination Classroom: Escenas de práctica - Fandub Español
  Latino»* ([YouTube](https://www.youtube.com/watch?v=AkbT2qpyz1U)) ⚠️ sin
  abrir ni contar vistas (YouTube pide sesión).
- *«[FANDUB] Assassination Classroom - Ending 1 - Letra Español Latino»*
  ([YouTube](https://www.youtube.com/watch?v=2PJNb3BOsZ8)) ⚠️ igual. Es el
  **único cover en español** hallado; de los openings sólo hay cover en
  inglés ❌.
- TikTok hispano: los vídeos de duelo por Koro-sensei (§14) ✅; cifras sin
  contar ⚠️.
- Dailymotion: **ningún fandub** (634 resultados, todos prensa francesa)
  ✅ comprobado.
- Para el servidor de doblaje: Carlos Segundo saluda como Koro-sensei en
  convenciones ([TikTok](https://www.tiktok.com/@rebecavirgen/video/7186783988743261446))
  ⚠️ sin ver; y en *Los Simpson* T32 hace un guiño a Koro-sensei como Phil
  ✅ (Doblaje Wiki).

### 18.6 · Punto 23 · Colaboraciones, figuras y cosplay

- **Videojuego cruzado**: Koro-sensei jugable en *J-Stars Victory VS*
  (2014) ✅ (§13).
- **Cafés del 10.º aniversario (2026)**, con ilustraciones nuevas ✅:
  **RAKU CAFE** Ikebukuro y Shinsaibashi, 8-ene a 3-feb
  ([アニメ！アニメ！](https://animeanime.jp/article/2026/01/03/94883.html),
  [PR Times](https://prtimes.jp/main/html/rd/p/000000192.000108434.html));
  **Sweets Paradise**, desde 17-mar en Tokio y Osaka
  ([web](https://www.sweets-paradise.jp/collaboration/ansatsu-anime2));
  **Animate Café Stand** Hareza Ikebukuro, desde 27-feb, posavasos con
  arte nuevo **de ajedrez** ([collabo-cafe](https://collabo-cafe.com/events/collabo/ansatsu-movie-takeout-animate-cafe-stand-hareza-ikebukuro-2026/)).
  Las ilustraciones sueltas no se pudieron abrir ⚠️.
- **Figuras**: Banpresto **DXF Koro-sensei vol. 1**, ~17 cm, en 4 colores
  (amarillo, **rojo = enfadado**, **negro = furioso**, rosa) ✅
  ([Tokyo Otaku Mode](https://otakumode.com/shop/566e26ea3c9c45be02d89289/Assassination-Classroom-Koro-sensei-DXF-Figures-Vol-1));
  **Pop Up Parade** de Karma y Nagisa ⚠️ (sólo en tiendas de reventa).
- **Imagen real** (2015-16): cabeza esférica física, toga y birrete, y un
  disfraz de policía azul (`personajes_02` n.º 62-63) ✅.
- **Cosplay**: fotos CC BY y cómo se hace la cabeza (§4.2) ✅.
- **Libros de estudio reales «殺たん»** (§3.2) ✅.

### 18.7 · Punto 24 · Obras parecidas

| Obra | Por qué se parece | Fuente |
|---|---|---|
| **Great Teacher Onizuka** | profesor raro que salva a una clase problemática | AniList (84, 104 votos) ✅; TV Tropes: «GTO con ciencia ficción y espías» ⚠️ |
| **My Hero Academia** | clase con letra, reparto coral, Jump de la misma época | AniList (76, 176 votos) ✅ |
| **Danganronpa** | jóvenes en un «mata o te matan» | AniList (69) + TV Tropes ⚠️ |
| **Classroom of the Elite** | instituto y juegos de poder | AniList (76, 362 votos) ✅ |
| **Talentless Nana** | alumnos con una misión de asesinato secreta | AniList (70) ✅ |
| **Neuro** (mismo autor) | un ser sobrehumano de moral ambigua que mejora a quien toca | TV Tropes + にじめん ✅ |

El manga hace **guiños a Doraemon y a El Puño de la Estrella del Norte**
⚠️ (TV Tropes, sólo vía buscador: la web da 403).
**Otras láminas del servidor**: **25 · My Hero Academia** también es de
aula (canal #material-de-clase, vecino de #avisos-clases): **no repetir
«aula con pizarra al fondo»** en las dos ✅. **19 · Doraemon** ya tiene su
biblia (guiño cruzado posible).

### 18.8 · Punto 25 · El mundo, la historia y sus símbolos

**Las reglas, en cinco líneas**
1. Un ser amarillo con tentáculos **destruye el 70 % de la Luna** y
   avisa de que destruirá la Tierra en marzo ✅.
2. Pide ser profesor de la **3-E de Kunugigaoka**, la clase de los
   peores; el Gobierno paga **100億円 (10 000 millones de yenes)** a quien
   lo mate ✅ ([ja.wikipedia](https://ja.wikipedia.org/wiki/%E6%9A%97%E6%AE%BA%E6%95%99%E5%AE%A4)).
3. **Nunca puede herir a un alumno**; ellos tienen **armas de colores**
   que sólo le hacen daño a él ✅.
4. El plazo es **el fin del curso** ✅. Si alguien cuenta el secreto, le
   borran la memoria ⚠️ (una fuente).
5. Vuela a **Mach 20**, se regenera y el agua lo frena ✅.

**La historia por arcos** (nombres de la web oficial y fuentes
japonesas; **los meses** son de la parte de texto ⚠️: el viaje a Kioto es
de la T1, [web oficial](https://www.ansatsu-anime.com/2014-2016/story/detail_1st.php?id=1000361),
así que va en primavera, no en otoño):

| Arco | Momento clave |
|---|---|
| Llegada de Koro-sensei | la clase decide matarlo |
| Llegada de Irina | la asesina se hace profe de inglés |
| **Viaje a Kioto** (修学旅行の時間) | la guía-diccionario de 2.400 páginas (§2.4) |
| Llegada de **Ritsu** y de **Itona** | la caja que se vuelve alumna |
| Agua y exámenes contra la clase A | se descubre que el agua lo frena |
| **Isla de verano** | un virus pone a la clase en peligro |
| **Festival cultural** | puesto de comida del monte: 3.º del colegio |
| Exámenes finales | toda la 3-E entre los 50 mejores |
| **El pasado de Koro-sensei** (過去の時間) | fue **el Segador** (死神), convertido por **Yanagisawa** (Shiro) |
| **Batalla final y graduación** | contra **群狼** (Manada de Lobos, de Craig Hōjō); lo matan juntos, por cariño |

**Después**: la recompensa sube a **300億円**; pagan estudios y **compran
el monte** del edificio viejo, «el sitio al que siempre pueden volver» ✅
(ja.wikipedia + [blog](https://anime-mahoubako.hatenablog.com/entry/ansatsu-saisyuukai)).

**Símbolos y objetos**: la **luna creciente**; la **pizarra**; el
**cuaderno de puntos débiles** de Nagisa (弱点その…); la **guía de viaje**
gigante; la **caja de Ritsu**; el **出席簿** de la lista final; la
**letra «E»**; las **armas de colores** anti-sensei. Emblema de la clase:
no encontrado ❌.

**Vocabulario que un fan reconoce**: 暗殺教室 (aula de asesinato) ·
殺せんせー · E組 / 3年E組 / «la E del final» (エンドのE組) · 椚ヶ丘 · 死神 ·
群狼 · 弱点 · 手入れ (cuidar) · 第二の刃 (el segundo filo) ·
抜き打ちテスト (examen sorpresa) · «Hora de…» ✅.

---

## 19 · Tres conceptos para la lámina de #avisos-clases

**Idea base, confirmada en la serie**: los títulos latinos son
«**Hora de…**» (§6.1), la clase la anuncia Koro-sensei al empezar
(2×06, 00:00:02) y **la emoción la pone el color de su cara** (§7.1).
Y hay un formato oficial de aviso que imitar (§7.7).

### Concepto A — «La pizarra de la 3-E» (el objeto del plan, mejorado)

- **Objeto y sitio**: **la pizarra verde del aula de madera** del
  edificio viejo. En Blender: la pizarra con el texto de tiza como
  textura (con restos de borrado), **la repisa con tizas de colores y el
  borrador**, imanes, y la pared de tablones. **2.ª pasada**: la pizarra
  del anime es **verde casi negra `#272726`** (medida en 2×06, 0:02), no
  verde medio; y en la repisa puede ir **el 出席簿**, el libro de
  asistencia negro de la lista final (2×24, 7:21). Detalle japonés real ⚠️:
  en el **borde derecho** de la pizarra se escribe en vertical **la
  fecha y el «日直»** (encargado del día).
- **Personaje**: **Koro-sensei** escribiendo con un tentáculo, con
  **dos o tres imágenes fantasma** (va a Mach 20). Cara **naranja con el
  ◯ rojo** apuntando al texto de «activa el aviso». Pose: §15, Koro-sensei
  1 (2×06, 00:00:02, **visto**: `fotogramas_01` n.º 1-2, con su traje
  ceremonial de cuello dorado, perfecto para «anunciar») o 7 (peli,
  00:49:25). Recorte limpio de cuerpo entero: arte del 10.º aniversario
  (`personajes_01` n.º 17) o `personajes_02` n.º 69; para la versión
  «¡todos aprobados!», la pose de celebrar (n.º 6 de `fotogramas_01`).
- **Cómo habla**: **con tiza**, con **los tres colores de la serie**:
  rosa para la palabra que avisa, dentro de un **estallido dentado**
  («¡Aviso!», como el «対» de 2×06), blanco para el qué, amarillo para lo
  importante ✅ visto. Título en **Yusei Magic** blanca; los
  bloques en **Kalam**; el ◯ y la X, dibujados a mano. Un «ヌルフフフ»
  pequeño en **Dela Gothic One** junto a su cabeza.
- **Dónde va cada texto**:
  - Arriba a la izquierda, grande: **«Avisos de clases»**; debajo, en
    tiza amarilla y como título de capítulo: **«Hora de clase»**.
  - Centro, dos columnas con un dibujito cada una (micrófono y nota
    musical): **«Clases de doblaje»** · **«Clases de canto»**.
  - Encima de las columnas: **«Cuándo hay clase y de qué»**.
  - Borde derecho, en vertical (la zona de la fecha): **«Aquí sólo
    escriben los profes»**, con una X morada pequeña.
  - Abajo a la derecha, rodeado por un **◯ rojo de tiza**: **«Activa el
    aviso que te interese»** y **«Lo tienes en Canales y roles»**.
- **Que no quede plano**: un **pupitre desenfocado delante** con el
  cuaderno de Nagisa abierto y una **bebida láctea de cartón «～煮オ・レ»**
  (la de Karma ✅, 2.ª pasada); luz de día blanca y cálida entrando **de
  lado** (paleta del aula, `#CAC1AA`, 2×24, 9:29), con **polvo de tiza** en el haz; la
  pizarra un poco en ángulo, no de frente.

### Concepto B — «La guía de Koro-sensei» (el libro de 2.400 páginas)

- **Objeto y sitio**: **la guía hecha a mano** del viaje escolar (§2.4),
  convertida en **«Guía de clases»**: un tocho de papel grapado **con
  pestañas de colores** («Doblaje», «Canto»), abierto sobre un pupitre
  de la 3-E junto a la ventana. En Blender: libro gordo con **las hojas
  curvadas**, las pestañas, un lápiz y el **cuaderno de Nagisa** al lado.
- **Personajes**: **Karma** (el más votado), echado hacia atrás en la
  silla, con la guía en la mano y cara de «¿esto es un diccionario?»
  (la reacción real de la clase); **Nagisa** al lado, apuntando en su
  cuaderno. Poses: §15, Karma 2 (2×01, 00:16:42) y Nagisa 7. **2.ª
  pasada**: referencia del libro gordo, Koro-sensei con un tomo enorme y
  pilas de libros (`personajes_02` n.º 72); Karma con chaqueta abierta
  (`personajes_01` n.º 16 o `personajes_02` n.º 71); Nagisa con chaleco y
  corbata negra (`personajes_01` n.º 18) y su cuaderno (n.º 9).
- **Cómo habla**: la guía está **escrita por Koro-sensei** con letra a
  mano redonda (**Klee One**) y dibujitos suyos en los márgenes; lo de
  Nagisa, a lápiz en su cuaderno (**Klee One** fina), numerado como sus
  «puntos débiles».
- **Dónde va cada texto**:
  - Portada o página de título: **«Avisos de clases»** y, más pequeño,
    **«Cuándo hay clase y de qué»**.
  - Pestañas: **«Doblaje»** · **«Canto»**; la página abierta:
    **«Clases de doblaje»** y **«Clases de canto»** con un horario en
    blanco (enlaza con la lámina 2).
  - Cuaderno de Nagisa, como nota numerada: **«Nº 1: activa el aviso que
    te interese»** · **«Está en Canales y roles»**.
  - Un pósit de Koro-sensei pegado en la guía: **«Aquí sólo escriben los
    profes»**.
- **Que no quede plano**: la guía **muy en primer plano**, con las
  hojas levantadas; Karma y Nagisa detrás, un poco desenfocados; **luz
  dorada de tarde**; la **luna creciente** visible por la ventana si se
  quiere un guiño.

### Concepto C — «Ritsu, la encargada del día»

- **Objeto y sitio**: **la caja de Ritsu** (la «caja moe»: un armario
  negro alto con pantalla) **al fondo del aula**, y **los móviles de la
  clase sobre los pupitres, encendidos** con «Ritsu móvil». Es **literal
  lo que hace un rol de aviso**: Ritsu se copia en los móviles para
  avisar a todos (§8). En Blender: la caja con la pantalla emisiva y
  tres o cuatro móviles.
- **Personajes**: **Ritsu** en la pantalla, haciendo de **encargada del
  día** (peli, 00:49:39: «起立！»); **Koro-sensei** asomado a la puerta,
  cara amarilla normal. Poses: §15, Ritsu 1 y Koro-sensei 5.
- **Cómo habla**: **en su pantalla y en las notificaciones**. Letra
  **M PLUS Rounded 1c** (o **DotGothic16** para un toque de máquina).
  Barra de título con 🎓🌕 como los avisos oficiales (§7.7). **2.ª
  pasada**: las notificaciones de los móviles pueden copiar **la caja de
  diálogo real de los juegos de 3DS**: etiqueta **amarilla `#FFEA62`** con
  el nombre («Ritsu») y caja **crema `#F5F7E2`** con gótica negra (§7.5)
  ✅. Y cada interruptor puede llevar la cartela de la lista final:
  **«Ⅲ-E〔1〕Doblaje»**, **«Ⅲ-E〔2〕Canto»** (2×24, 8:50) ✅.
- **Dónde va cada texto**:
  - Pantalla de la caja, arriba: **«Avisos de clases»**.
  - Debajo: **«Cuándo hay clase y de qué»**.
  - Dos interruptores dibujados en la pantalla: **«Doblaje»** ·
    **«Canto»**, y el texto **«Activa el aviso que te interese»**.
  - En el móvil de delante, como notificación: **«Lo tienes en Canales y
    roles»**.
  - En otro móvil: **«Aquí sólo escriben los profes»**.
- **Que no quede plano**: los móviles **en primer plano** con su luz
  azulada sobre la madera; la caja al fondo; luz de ventana lateral.
- **Riesgo**: al dueño **no le convencieron los paneles de interfaz
  sueltos**. Aquí la interfaz está **dentro de objetos reales** (la caja
  y los móviles en el aula), pero conviene enseñarle antes un boceto.

### ¿Cuál primero?

1. **A**: es el objeto del plan, se entiende al instante y usa lo más
   reconocible (la cara ◯ de Koro-sensei).
2. **C**: el más original y el que mejor explica «activa el aviso».
3. **B**: el más «de Blender» (papel curvado) y el que usa al más
   querido (Karma).

**Cambió en la 2.ª pasada**: ningún concepto cambia de objeto; ahora
cada uno tiene imagen propia (hojas numeradas), paleta medida y un
formato de texto real de la serie (tiza de tres colores, cartela «Ⅲ-E»,
caja de los juegos). Nota de canal: **25 · My Hero Academia** también es
de aula (§18.7); si las dos láminas se hacen, que A no repita su pizarra.

**Lámina 2** (el horario): en la **pared lateral del aula**, un **tablero
de horario** (時間割表) de corcho o imanes con fichas «Doblaje» y
«Canto» por día. Huecos en blanco hasta que el dueño pase el horario real.

---

## 20 · Lo que no pude verificar

**2.ª pasada · lo que se resolvió** (antes → ahora): imágenes y hojas
(ninguna → 3 hojas, 96 imágenes miradas) ✅; paleta (no medida → medida)
✅; posturas (deducidas → 16 vistas en fotograma) ✅; voces de Karasuma,
Kayano, Ritsu y el director (sin fuente → dos fuentes) ✅; endings de T1
y T2 ✅; Futura del logo inglés ✅; cajas de diálogo de los juegos ✅;
colores de Karma e Irina ✅; J-Stars ✅; Doblaje Wiki (extractos → wikitext
completo) ✅.

**Lo que sigue sin verificar**:
- **Frases del doblaje latino con minuto** ❌: YouTube pide iniciar sesión,
  las muestras de Doblaje Wiki están vacías y no hay clips doblados en
  Dailymotion. Sólo hay frases con episodio (§10).
- **Cómo llaman a Irina en latino** ❌; **doblaje latino de la película
  2026** ❌.
- **Vídeo en 480p**, no 1080p ⚠️ (Internet Archive; los `.mkv` de 5 GB
  por episodio no caben).
- **Caras sin fotograma** ⚠️: Koro-sensei triste, con miedo o furioso
  (hay figuras DXF de colores); Nagisa triste, con miedo o avergonzado;
  Karma triste, con miedo o avergonzado; **Irina enfadada** (la película
  de 2016 entera no está en Internet Archive ni Dailymotion).
- **Temporada 1 sin subtítulos**: la guía del ep. 7, el cuaderno y las
  clases con clones van **sin minuto** ⚠️.
- **Encuestas**: si hubo más de una oficial (sólo namu) ⚠️.
- **Letra del logo japonés** y de los títulos de episodio ❌.
- **Emblema de Kunugigaoka o de la 3-E** ❌ (no encontrado; se usa la «E»).
- **Fondos de pantalla oficiales** ❌ (sólo de fans).
- **Tráiler de la película 2026** fuera de YouTube ⚠️.
- **Fan dubs y covers**: títulos encontrados, **vistas sin contar** ⚠️.
- **Ritsu**: color de pelo y aspecto en pantalla ⚠️ (sin fotograma).
- **Kiiro Shingo, Setsuna Blossom, Spica** (temas de la reemisión): una
  fuente ⚠️.
- **Programa de dibujo de Matsui** y **trama exacta** del manga ❌.
- Pop Up Parade de Karma y Nagisa: sin ficha oficial ⚠️.
- Que el colegio Irisugawa sea el modelo **del anime** ⚠️; que cada clon
  lleve **una cinta con la asignatura** ⚠️; la **fecha y el 日直 en la
  pizarra** de la 3-E ⚠️.
- Reddit (r/AssassinationClassroom): 0 resultados en Arctic Shift ❌.

---

## Cumplimiento del encargo

Estado tras la 2.ª pasada (25-sep-2026). ✅ hecho · ⚠️ a medias · ❌ no
hecho, con el porqué.

| # | Punto de ENCARGO.md | Estado | Por qué / dónde |
|---|---|---|---|
| 1 | Arte oficial variado | ✅ | Hojas de modelo de Lerche, arte del 10.º aniv., visual de la T2, ficha de Karma, imagen real, logo; 80 imágenes en 2 hojas (§3.0) |
| 2 | Fotogramas de escenas icónicas con minuto | ⚠️ | 16 fotogramas con episodio y minuto, vistos (§2.5, `fotogramas_01`); **en 480p, no 1080p** (YouTube bloqueado; los originales pesan 5 GB) |
| 3 | Fan art y 3D con licencia | ✅ | 7 modelos de Sketchfab CC BY por API; fan art con autor (Safebooru); cosplay CC BY (§4). pixiv cerrado |
| 4 | Sitios, luz, paleta medida, texturas | ✅ | Paleta medida en 9 escenas (§5.2b); luz vista; texturas CC0 enlazadas. Pizarra sin textura libre ❌ (se pinta) |
| 5 | Tipografía por uso, con tildes | ⚠️ | Letras libres comprobadas con fontTools (§6.2); Futura ✅. Logo japonés y títulos de episodio sin identificar ❌ |
| 6 | Cómo hablan en pantalla / cuadro de diálogo | ✅ | Cara de colores, tiza de tres colores, cartela «Ⅲ-E〔n〕», caja de los juegos de 3DS medida (§7) |
| 7 | Personajes y popularidad | ✅ | Encuesta oficial hasta el 9.º con reparto por sexo, AniList y Danbooru (§9) |
| 8 | Doblaje latino y frases | ⚠️ | Reparto completo con dos fuentes y ficha técnica ✅ (§10). **Frases latinas sólo con episodio, sin minuto ni clip** ❌ (YouTube pide sesión; muestras vacías) |
| 9 | Música y sonido | ✅ | Todos los temas originales, la reemisión 2025-26, las dos películas (始業のベル = 2016), el insert de la muerte; risas y ruidos (§11, §2.3) |
| 10 | Vídeos con minuto | ⚠️ | PV T2, featurette 2016 y 7 episodios mirados con minuto (§12). Tráiler 2026 y TikTok sin ver |
| 11 | Videojuegos: interfaz y diálogos | ✅ | Dos juegos de 3DS vistos en capturas, J-Stars, Koro-Sensei Quest! (§13, §7.5) |
| 12 | Lo que ama el fandom y qué no hacer | ✅ | §14, con duelo hispano en TikTok y nuevos «no hacer» |
| 13 | Descripción profunda y cara en cada emoción | ⚠️ | Carácter, historia, datos y dinámicas ✅ (§8). **Caras**: faltan tristeza, miedo y rabia de Koro-sensei; tristeza, miedo y vergüenza de Nagisa y Karma; Irina enfadada |
| 14 | Poses analizadas con minuto | ⚠️ | 34 escenas con minuto; **9 vistas** en fotograma (más las poses de las hojas de la wiki), el resto deducidas (§15) |
| 15 | Vestuario con hex | ✅ | Koro-sensei, Nagisa, Karma e Irina medidos (§16); vivos morados de la toga sin hex ⚠️ |
| 16 | Paisajes y fondos de pantalla | ⚠️ | Sitios con luz vista; 8 fondos con tamaño y autor (§17); **oficiales no existen para descargar** ❌ |
| 17 | Guía para IA de imagen y de texto | ✅ | Rasgos fijos, estilo medido, palabras, vocabulario de Danbooru y de expresiones, frases reales por emoción (§18) |
| 18 | Estilo y técnica, cómo replicarlo | ✅ | Staff, manga mirado, sombreado y línea medidos, receta de Photoshop y Blender (§18.1). Programa de Matsui ❌ |
| 19 | Texturas 2D | ⚠️ | Trama libre, papel, crayón, tiza (§18.2); **emblema de la escuela no encontrado** ❌ |
| 20 | Gustos y detalles | ✅ | Tabla de 7 personajes con cumpleaños, altura, comida, afición, objeto (§18.3) |
| 21 | Por qué la aman, escenas que hacen llorar | ✅ | Ventas, premios, reseñas con cita, lista final vista con minuto, ep. 46 con su música (§18.4). Reddit sin datos ❌ |
| 22 | Fan dubs y comunidad hispana | ⚠️ | 2 fandubs y el cover del ending encontrados, **sin vistas** (YouTube pide sesión) (§18.5) |
| 23 | Colaboraciones, figuras, cosplay | ✅ | J-Stars, 3 cafés 2026, DXF, Pop Up Parade ⚠️, imagen real, cosplay (§18.6) |
| 24 | Obras parecidas y láminas cercanas | ✅ | AniList, TV Tropes (vía buscador ⚠️), mismo autor; choque con MHA (§18.7) |
| 25 | Mundo, historia por arcos, símbolos | ✅ | Reglas, 10 arcos, final, símbolos y vocabulario (§18.8); orden por meses ⚠️ |
| — | **3 conceptos de lámina** | ✅ | A pizarra, B guía, C Ritsu, con imagen numerada, letra, textos y profundidad (§19) |
| — | **40 fuentes distintas** | ✅ | **102 webs distintas** enlazadas |
| — | Oficiales | ✅ | ansatsu-anime.com, Shueisha, Nintendo, Bandai Namco, avex, PR Times; entrevistas (Natalie, Oricon) sólo titular ⚠️ |
| — | Otros idiomas (japonés, inglés, coreano, chino) | ✅ | ja.wikipedia, pixiv百科, Famitsu, 4Gamer; Namuwiki; 萌娘百科 |
| — | Wikis, TV Tropes, TCRF, Wayback | ⚠️ | Fandom (dos), Doblaje Wiki, Wikipedia ✅; TV Tropes 403 (sólo vía buscador); TCRF no aplica (sin betas documentadas); Wayback rechazado |
| — | Foros y comunidades | ⚠️ | MyAnimeList, Yahoo!知恵袋, dafont, cosplay.com ✅; Reddit por Arctic Shift sin resultados ❌ |
| — | Arte (pixiv, ArtStation…) | ⚠️ | Safebooru, Wallhaven, Behance ✅; pixiv pide sesión ❌ |
| — | Vídeo con minuto | ✅ | Internet Archive y Dailymotion mirados; YouTube sólo enlazado |
| — | Código y recursos | ✅ | GitHub (kitsunekko, google/fonts, svg-halftone), Sketchfab, ambientCG, Clip Studio Assets |
| — | Doblaje latino | ✅ | Doblaje Wiki por API, ANMTV, Crunchyroll, AniList |
| — | **Hojas de contacto** | ✅ | 3 en `hojas/`: `personajes_01`, `personajes_02`, `fotogramas_01` (nueva), todas < 1 MB (§3.0) |
| — | **referencias.json** | ✅ | **157** referencias (99 con tamaño medido), las mejores primero |

**Resumen**: 16 ✅ y 9 ⚠️ de los 25 puntos; ningún punto sin hacer. Lo
que falta de verdad son **frases latinas con minuto**, **vídeo en
1080p**, **algunas caras por emoción** y el **emblema de la escuela**,
todo por bloqueos o porque no se encontró, no por no buscar.

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- **Cerrados** (conexión rechazada por curl, o «EGRESS_BLOCKED» por
  WebFetch): Doblaje Wiki (y su API), Fandom, ANMTV, Otaku Press,
  eldoblaje.com, la web oficial ansatsu-anime.com, pixiv百科, 暗殺教室設定資料集,
  Famitsu, anime-tourism.jp, Sketchfab, jump.co.jp, shonenjump.com,
  Namuwiki, Game UI Database, la web del juego de Bandai Namco,
  MobyGames, kitsunekko.net, jimaku.cc, animelon, y **todos los
  servidores de imágenes** probados (YouTube, Fandom, Twitter, pixiv,
  WallpaperFlare, MyAnimeList, AniList, Wikimedia).
- **Abiertos**: la herramienta WebSearch, **GitHub por git** y
  `raw.githubusercontent.com`.
- `herramientas/investigar_serie.py` **no se usó** (Fandom cerrado): **no
  hay carpeta `hojas/`**.

### Búsquedas web (47)

| # | Idioma | Búsqueda | Qué saqué |
|---|---|---|---|
| 1 | es | Assassination Classroom doblaje latino reparto Koro-sensei Nagisa Karma Irina | Carlos Segundo, Cristina Hernández; vídeos «Voz de…» |
| 2 | es | «Assassination Classroom» doblaje Funimation México «Nagisa» «Karma» voz | María José Moreno; The Kitchen; madre e hija |
| 3 | es | Karma Akabane doblaje latino voz actor The Kitchen Iván Fernández | Iván Fernández |
| 4 | es | «Iván Fernández» «Karma Akabane» | 2.ª fuente (aniSearch, YouTube) |
| 5 | es | «Cristina Hernández» Irina Jelavić doblaje | 2.ª fuente |
| 6 | es | «María José Moreno» Nagisa Shiota voz | 2.ª fuente |
| 7 | es | … Irina «Bitch-sensei» cómo le dicen en latino | ❌ no sale |
| 8 | en | … official character popularity poll results Weekly Shonen Jump | Karma 1.º (432) |
| 9 | ja | 暗殺教室 人気投票 結果 1位 カルマ 渚 殺せんせー | la tabla completa de 5 |
| 10 | ja | 殺せんせー 顔色 正解 丸 不正解 バツ … | los colores de la cara |
| 11 | ja | 暗殺教室 E組 旧校舎 モデル 木造校舎 聖地 美術監督 | Miyakoshi; Irisugawa (rodaje) |
| 12 | ja | 殺せんせー 修学旅行のしおり 分厚い 何ページ | la guía de 2.400 páginas |
| 13 | ja | 殺たん … 集英社 単語帳 | los libros «殺たん» |
| 14 | ja | 暗殺教室 殺せんせー大包囲網 3DS … | juego de 2015 |
| 15 | ja | «アサシン育成計画» 暗殺教室 3DS 2016 … | juego de 2016 |
| 16 | ja | 暗殺教室 アニメ スタッフ 監督 岸誠二 … | el staff |
| 17 | ja | 劇場版「暗殺教室」みんなの時間 2026年3月20日 … | película 2026 y su visual |
| 18 | en | … openings endings list … | OP 1-2 de la T1 |
| 19 | ja | 暗殺教室 第2期 オープニング エンディング 主題歌 一覧 … | OP y ED de la T2 |
| 20 | ja | 暗殺教室 10周年 再放送 新オープニング … GENIC | ENDER / Infinity karat |
| 21 | ja | «暗殺教室» «課外授業編» 配信 全8話 | qué es el KJ |
| 22 | en | Assassination Classroom logo font name dafont | Futura (una fuente) |
| 23 | ja | 暗殺教室 ロゴ デザイン 書体 フォント … | ❌ nada |
| 24 | ja | 暗殺教室 Blu-ray DVD ジャケット 描き下ろし … | portadas de Blu-ray |
| 25 | en | Yusei Matsui interview Koro-sensei design … | «simple, simple, simple» |
| 26 | en | sketchfab japanese classroom chalkboard school desk CC BY | modelos de aula y pupitres |
| 27 | en | sketchfab Koro-sensei 3D model | llavero CC BY, figuras |
| 28 | en | free chalkboard texture CC0 ambientCG polyhaven | ❌ sin textura concreta |
| 29 | en | Irina Jelavić character personality … | carácter y aspecto de Irina |
| 30 | ja | 律 暗殺教室 自律思考固定砲台 モバイル律 … | Ritsu, E-27, móviles |
| 31 | es | … segunda temporada doblaje latino Crunchyroll … Karasuma Kayano Ritsu | T2 en Crunchyroll; ep. 15 desincronizado |
| 32 | es | crunchyroll «Assassination Classroom» «Hora de» … | **títulos «Hora de…»** |
| 33 | en | … fandom memes … nurufufu … TikTok | risa, opening, piñata |
| 34 | en | Koro-sensei outfit academic gown mortarboard … | vestuario de Koro-sensei |
| 35 | ja | 椚ヶ丘中学校 制服 色 … | americana gris; COSPA |
| 36 | en | Assassination Classroom wallpaper 4K … | WallpaperFlare |
| 37 | ja | 黒板アート 殺せんせー … | ❌ ninguno concreto |
| 38 | ja | 渚 殺せんせーの弱点 メモ 手帳 … | el cuaderno de Nagisa |
| 39 | ko | 암살교실 살선생 인기투표 순위 … | otras encuestas (namu) |
| 40 | zh | 暗杀教室 杀老师 名场面 点名 毕业 … | 杀老师/黄老师; cap. 176-177 |
| 41 | es | Koro-sensei doblaje latino Carlos Segundo risa frases … | Carlos Olízar; «alguacil» |
| 42 | ja | 劇場版「暗殺教室」みんなの時間 本予告 特報 YouTube 公式 | los tráileres |
| 43 | ja | 殺せんせー 分身 ハチマキ 教科 個別指導 … | clases con clones |
| 44 | es | … doblaje latino «Karasuma» voz OR «Kaede Kayano» … | Ritsu (una fuente) |
| 45 | ja | 暗殺教室 10周年 壁紙 ダウンロード … 抜き打ちテスト | webs de fondos |
| 46 | ja | 潮田渚 コスプレ 衣装 ベスト 色 … | chaleco azul; 超体育着 |
| 47 | ja | «殺せんせーの抜き打ちテスト» 暗殺教室 再放送 連動 | **el formato oficial de aviso** |

WebFetch: 4 intentos (ANMTV, Otaku Press, Namuwiki, ansatsu-anime.com),
todos bloqueados.

### GitHub (sin cupo)

- [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror):
  subtítulos japoneses de la T2 (Netflix y Blu-ray), del 課外授業編 y de
  la película 2026. Script propio para buscar frases y cruzar la
  numeración Netflix/Blu-ray. **La T1 no está** (sólo su lista de
  ignorados).
- [google/fonts](https://github.com/google/fonts): 25 familias bajadas y
  comprobadas con fontTools; prueba visual sobre verde pizarra.

### Fuentes consultadas por tipo

- **Oficiales**: ansatsu-anime.com (staff, fichas, discos, 10.º
  aniversario, noticias), X @ansatsu_anime, Shueisha y JUMP j BOOKS,
  Nintendo, Bandai Namco, avex/GENIC, YouTube oficial.
- **Entrevistas**: Matsui en Anime News Network y ScreenAnarchy (2016).
  La del director Kishi existe pero no la pude leer.
- **Prensa japonesa**: Animate Times, アニメハック, Famitsu, 4Gamer,
  電撃, LisAni!, Natalie, USEN encore, にじめん, Excite.
- **Wikis**: Assassination Classroom Wiki (Fandom), Jump Database,
  pixiv百科, アニヲタWiki, 暗殺教室設定資料集, 萌娘百科 (chino), Namuwiki
  (coreano).
- **Foros y fans**: マンバ, ジャンプ速報, Yahoo!知恵袋, dafont (foro),
  blogs japoneses.
- **Doblaje**: Doblaje Wiki (extractos), ANMTV, Otaku Press, TierraGamer,
  Crunchyroll, aniSearch, YouTube.
- **3D y texturas**: Sketchfab, MakerWorld, Cults3D, ambientCG.
- **Arte**: Pinterest (sólo para buscar autores), WallpaperFlare,
  アニメ壁紙.com, tsundora.
- **Vídeo**: YouTube oficial y de fans, TikTok.
- **No existe o no encontré**: TV Tropes (cerrado), The Cutting Room
  Floor (no aplica: no hay juegos con betas documentadas que yo viera),
  Wayback Machine (cerrado), Reddit y Arctic Shift (cerrados).

### Lo que NO encontré

- Una imagen descargada, ni una sola.
- Cómo dice el latino «ヌルフフフ», «手入れ», «ビッチ先生» o «第二の刃».
- La voz latina de Karasuma y de Kayano.
- La letra del logo japonés.
- Capturas de las cajas de diálogo de los juegos.
- Fan art concreto con autor (pixiv cerrado).
- Una textura concreta de pizarra verde con su enlace.
- Los endings de la temporada 1.

### Segunda pasada (25-sep-2026): red abierta y método de equipo

Junta las bitácoras de `partes/imagen.md`, `video.md`, `voz.md` y
`texto.md`, más lo que hizo el redactor.

**Comprobación de red**
- **Ahora responden**: Fandom (`ansatsukyoshitsu`; `assassinationclassroom`
  da 404), Doblaje Wiki por API (`prop=wikitext`), Sketchfab API,
  ambientCG API, Wallhaven, Internet Archive, Dailymotion API, ja y en
  Wikipedia, Famitsu, 4Gamer, Dengeki, Oricon (en Shift-JIS, a mano),
  MusicBrainz, GitHub.
- **Siguen cerrados**: YouTube (lista formatos, pero bajar da 403),
  TikTok, pixiv (302 a login), TV Tropes (403 Cloudflare, dos
  intentos), AnimeThemes (522 y 403), Wayback (rechazado), Comic Natalie
  (403 en el cuerpo), Reddit por Arctic Shift (0 resultados).

**APIs y herramientas (sin cupo de buscador)**
- `investigar_serie.py --wiki ansatsukyoshitsu --paginas "Korosensei"
  "Nagisa Shiota" "Karma Akabane" "Irina Jelavić"` → 80 imágenes, 2 hojas.
- Fandom `api.php?action=parse&prop=wikitext` sobre Korosensei,
  Nagisa_Shiota, Karma_Akabane, Irina_Jelavić, Tadaomi_Karasuma,
  Kaede_Kayano, Ritsu, Episode_46, Episode_47 y «Assassination Classroom
  Openings and Endings».
- Doblaje Wiki: `Assassination_Classroom` (22 509 caracteres), páginas
  de Juan Carlos Román y María García.
- `api.sketchfab.com/v3/models/<uid>` ×7; ambientCG `q=wood planks`,
  `old wood`, `paper` (con resultado), `chalkboard` (0).
- Internet Archive: `AnsatsuKyoushitsuEpisode001480pX264`,
  `anime-kage-assassination-classroom-01-ro-sub` y
  `ansatsu-kyoushitsu-2x-23_20260520` (2×01, 06, 07, 21, 24, 25) con
  `fotogramas.py` y `ffmpeg -ss` (sólo segundos sueltos); vídeos borrados.
- **Redactor**: 16 fotogramas sueltos con `ffmpeg -ss` sobre los mismos
  mp4 de Internet Archive → `hojas/fotogramas_01.jpg`, mirada entera (de
  ahí el 出席簿 de 2×24, 7:21 y la cartela «Ⅲ-E〔7〕» de 8:50).
- Dailymotion API en japonés: «暗殺教室 PV» → `x3kret1`; «暗殺教室
  みんなの時間» → sólo `x8o319m` (película 2016); «fandub español» → 634
  resultados, ninguno fandub.
- `estilo.py` ×5 sobre fotogramas y sobre el arte del 10.º aniversario;
  Pillow para hex de vestuario, de caras y de los juegos.
- `referencias.json`: tamaños medidos bajando cada imagen (99 de 157).

**Búsquedas web (47 de la 1.ª pasada + 47 nuevas: 12 + 4 + 13 + 18)**
- Imagen (12; es, en, ja): cafés 2026 (「暗殺教室 コラボ カフェ 2026」),
  figuras, J-Stars, cosplay de la cabeza, tramas gratis, emblema
  (「椚ヶ丘中学校 校章 エンブレム」).
- Vídeo (4; ja): temas de la reemisión («Last Look», «月の舟» de ATARAYO,
  友成空) y el tema de la película 2026.
- Voz (13; es, en, ko): reparto latino, «Bitch-sensei» en latino, fandubs,
  covers, ventas, *Kono Manga ga Sugoi*, reseñas «made me cry», encuestas
  de namu.wiki.
- Texto (18; ja, en): staff y técnica de Lerche, TV Tropes, vocabulario,
  recompensa (100億円, 300億円), arcos, 群狼, logo (Futura, 書体),
  entrevista de Matsui sobre el «blanco».

**Fuentes nuevas por tipo**
- **Oficiales**: ansatsu-anime.com (historia, 10.º aniv.), avex, PR Times,
  Sweets Paradise, Famitsu, 4Gamer, Dengeki.
- **Otros idiomas**: ja.wikipedia, pixiv百科, アニメ！アニメ！, にじめん,
  OTOTOY, animatetimes, utaten (japonés); Namuwiki (coreano).
- **Wikis**: ansatsukyoshitsu.fandom.com, Doblaje Wiki, en.wikipedia.
- **Foros y fans**: MyAnimeList (reseñas y foro), cosplay.com, Kanzenshuu,
  GameFAQs, blogs japoneses.
- **Arte y recursos**: Safebooru, Wallhaven, Openverse/Wikimedia, Behance,
  Sketchfab, ambientCG, Clip Studio Assets, GitHub (svg-halftone).
- **Vídeo**: Internet Archive, Dailymotion, TikTok (enlaces).

**Lo que NO encontré en la 2.ª pasada** (con la búsqueda hecha)
- Frases del doblaje latino con minuto (YouTube 403; muestras de Doblaje
  Wiki vacías; Dailymotion sin clips doblados).
- El apodo latino de Irina («profesora bitch», «Bitch-sensei apodo
  latino», wikitext de Doblaje Wiki).
- Doblaje latino de la película 2026 (ANMTV, Doblaje Wiki, eldoblaje.com).
- La película de 2016 entera (Internet Archive: `365日の時間`,
  `ansatsu kyoushitsu graduation`; Dailymotion) → sin Irina enfadada.
- Tráiler de la película 2026 fuera de YouTube.
- Fondos oficiales (`/10th/wallpaper/` 404).
- Emblema de la escuela («校章», «エンブレム»).
- Diseñador del logo japonés y programa de dibujo de Matsui.
- Hilos de r/AssassinationClassroom (Arctic Shift, tres variantes).
