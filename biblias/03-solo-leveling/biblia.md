---
tags: [biblia, serie, laminas]
serie: "Solo Leveling"
canal: "#guia (foro de 14 hilos)"
fecha: 2026-09-24
---

# Biblia · Solo Leveling — para #guia

> [!important] Cómo se hizo (léelo primero)
> - **Dos pasadas.** La primera (24-sep-2026, mañana) se hizo con la red cerrada: sólo buscador web y **GitHub** (subtítulos con tiempos, fichas de ANN, MAL y AniList, texto de Wikipedia, Google Fonts). Sin hojas de contacto.
> - **Segunda pasada, 24-sep-2026, con la red abierta.** Se pudo usar:
>   - **Wiki de Fandom** (`solo-leveling.fandom.com`) por su API: 3 tandas de `investigar_serie.py` (**673 + 305 + 635 imágenes**, 36 hojas numeradas). **Las miré.** Monté 3 hojas propias en `hojas/` (§10.0). Los tamaños son los reales de la API.
>   - **Doblaje Wiki** por la API (`action=parse`): reparto, equipo técnico, datos de interés y **60 muestras de audio del doblaje**. Pasé 15 por reconocimiento de voz (Whisper) para sacar frases textuales del doblaje (§12).
>   - **YouTube con yt-dlp**: 21 vídeos comprobados (título, canal, fecha, duración, visitas). YouTube no deja bajar el vídeo (pide iniciar sesión) y `fotogramas.py` falla; **miré los vídeos por sus *storyboards*** (fotogramas de 320×180, uno por segundo): opening, ending, tráiler doblado y 5 escenas (§14).
>   - **Sketchfab** (licencias por su API), **Poly Haven** y **ambientCG** (texturas CC0), **Arctic Shift** (Reddit), **fontTools** (13 letras más: 12 de Google Fonts y la de dafont) y webs que antes daban 403 (ANMTV, TVLaint, CBR).
>   - Colores **medidos con Pillow** en capturas de la wiki, *storyboards* y arte oficial.
> - **Siguen cerradas:** TV Tropes, The Cutting Room Floor y Game UI Database (403 de Cloudflare), Bilibili (412) y la web de noticias de Crunchyroll (sólo carga con JavaScript).
> - **Repaso corto, 24-sep-2026 (noche): los puntos 18-25 nuevos del encargo.** Tres investigadores (imagen: 19 y 23; voz: 20, 21 y 22; texto: 18, 24 y 25) dejaron sus notas en `partes/`; el redactor las pasó a la biblia, en su sitio (puntos 18-25, después de §18). Se usó: la API de la wiki de la serie y la del juego *ARISE*, *The Dubbing Database*, `estilo.py` sobre dos imágenes, Arctic Shift, `oembed` de YouTube y TikTok, Pillow para medir tamaños, y entrevistas del equipo (VFX Voice, Anime Corner, Sony XYN, CBR). YouTube seguía pidiendo iniciar sesión.

**Leyenda**
- ✅ **confirmado**: dos fuentes, o un archivo que abrí o medí.
- ⚠️ **dudoso**: una sola fuente, o lo sé de memoria. Míralo antes de dibujar.
- «ep. 12 · 17:39» = capítulo y minuto. Los de la temporada 1 salen de los subtítulos de Netflix; los de la 2, de los de Crunchyroll. En otra plataforma el minuto puede moverse unos segundos.
- «hoja P·7» = número 7 de `hojas/personajes_01.jpg`; «S·3» = `sistema_01.jpg`; «F·5» = `fondos_01.jpg`. La tabla de §10.0 enlaza cada original.

## Segunda pasada · qué cambió

**Corregido (antes → ahora)**
- **Cha Hae-In:** «armadura clara» (dudoso) → **uniforme rojo `#BC2B47` con blanco, pelo rubio corto y espada negra de guarda plateada** ✅ (wiki + CV oficial, hoja P·17-18).
- **Igris:** en el anime japonés y en su visual oficial se llama **«IGRIT»** (P·11). Los subtítulos latinos dicen casi siempre «Igris» y una vez «Igrit» (ep. 20 · 09:01). Se mantiene «Igris».
- **La primera ventana del Sistema (ep. 3)** no es un panel oscuro: es **gris azulada muy clara, casi transparente**, con la cabecera y el icono «!» en dos recuadros (S·1). Las oscuras (`#112A39`) llegan después (S·3, S·10).
- **Frase «Just open the message box»:** la dice **Sung Jinah** ✅ (subtítulo de Netflix + muestra del doblaje: «Lo normal sería abrir la caja de mensajes»).
- **Kim Chul (Iron):** «Olin Alejandro Garcés» (dudoso) → **Gamaliel Quintana en la T1 (ep. 5) y Olín Garcés en la T2** (Doblaje Wiki + ANMTV).
- **Traducción del doblaje:** sólo se citaba a Ilse Santillán → **Ilse Santillán (T1) y Samuel Oseguera (T2)**.
- **ARISE:** «¿18-mar o 8-may-2024?» → **8 de mayo de 2024** ✅ (wiki + prensa coreana).
- **Película:** su título latino es **«Solo Leveling: Segundo despertar»** ✅ (Doblaje Wiki).
- **Licencias de Sketchfab:** «según un README ajeno» (dudoso) → **comprobadas por la API** ✅.
- **Descripción de «DARK ARIA»:** suena en el ep. 6 **y en el ep. 23** ✅.

**Añadido**
- 3 hojas de contacto propias (§10.0). `referencias.json` rehecho: **40 entradas**, todas con la imagen misma (o el vídeo con `&t=`) y 37 con tamaño medido; sólo quedan las 2 KV de la primera pasada.
- La ventana del Sistema **medida en 10 capturas** (§4.2): colores, cabecera, icono, botones, la palabra en rojo.
- El **vocabulario latino de los carteles** en un clip oficial doblado: «ADVERTENCIA: No cumplir la misión te detendrá el corazón», «[Perjuicio] Parálisis».
- **Frases textuales del doblaje latino** (§12.3), de las muestras de audio de Doblaje Wiki.
- Minutos y enlaces `&t=` de opening, ending, tráiler y 5 clips (§14).
- Modelos 3D nuevos con licencia CC BY: **el salón de Igris**, Cha Hae-In, esfera de cristal, mostrador y tablón (§11).
- Tabla **«Cumplimiento del encargo»** (antes de la bitácora).
- Noticia: **«Solo Leveling: Beyond the System»**, película nueva en producción (Crunchyroll, 3-jul-2026).

**Marcas de duda (⚠️):** había **55**; quedan **36**, contadas con `grep` (31 son datos dudosos; 5 son la leyenda, este resumen y la tabla de cumplimiento). El porqué de cada una va a su lado y resumido al final de la bitácora.

### Repaso corto (puntos 18-25) · qué cambió

**Corregido (antes → ahora)**
- **Emblema de Ahjin:** «círculo morado con aguijón dorado» (nota de la parte de imagen) → **llama o fénix violeta en círculo, sin dorado** ✅ (mirado en una hoja propia y medido con Pillow, punto 19).
- **Emblema del Gremio de Cazadores:** «insignia circular dorada» → **escudo blanco y gris con una espada vertical** ✅ (mirado, punto 19).
- **La guía para IA (§18):** decía «línea fina y limpia» para el anime → **casi sin línea negra, con luz de borde de color y fondo desenfocado**; la línea negra es del webtoon ✅ (medido con `estilo.py`, punto 18). Se añadieron las palabras que lo estropean *super deformed, sweat drop, comedic expression, screentone*.

**Añadido**
- **Punto 18:** quién lo hizo, la regla del director (nada de gestos de dibujo animado, «como imagen real»), 2D y 3D mezclados, captura de movimiento con mocopi, cómo replicarlo en Photoshop y Blender, y un encuadre por emoción.
- **Punto 19:** no hay tramas; líneas de velocidad, grabado de metal CC0, grano de papel. **5 emblemas de gremio** con tamaño y color.
- **Punto 20:** cumpleaños de Jinwoo (8-mar) y Cha Hae-In (24-dic) con dos fuentes; la historia humana de Igris (**Sian Halat**); por qué Beru habla florido (ve doramas de época); Cha Hae-In, atleta retirada por una lesión.
- **Punto 21:** 9 premios y **51 millones de votos** en los Crunchyroll Anime Awards 2025; la escena del hospital del ep. 21, vista en un fotograma.
- **Punto 22:** 6 covers latinos de los openings, un meme de TikTok y *The Dubbing Database* como **tercera fuente del reparto** (Daniel Lacy como Beru).
- **Punto 23:** Fortnite, *ARISE* × *Frieren*, Grand Summoners, la exposición de Seúl, el pop-up «System Sync», el Nendoroid (trae **el panel del Sistema como pieza**) y dos cosplays con tamaño medido.
- **Punto 24:** obras parecidas (AniList y prensa), la cita de Chugong sobre el Itarim y las láminas vecinas del servidor (el tablón de corcho ya es de Solo Leveling).
- **Punto 25:** el mundo en cinco líneas, **14 arcos del anime con sus episodios**, objetos icónicos y el vocabulario latino.
- **Conceptos (§20):** siguen los tres; se añade cómo los mejora el repaso y una **lámina 2 «De qué va esto»** con los 14 arcos.
- `referencias.json`: **148 entradas** (antes 40): emblemas, colaboraciones, figura, cosplay y lo útil de `datos.json`.
- La tabla de cumplimiento ya tiene **los 25 puntos**.

**Marcas de duda (⚠️):** eran **36** antes del repaso; ahora **102** con `grep`. Suben porque los puntos nuevos traen muchos datos de una sola fuente (la wiki, un blog, una nota de prensa), marcados uno a uno. Lo que no se pudo cerrar va en §21 y en la tabla.

---

## 0 · Lo esencial

- **El más querido es el protagonista, Sung Jinwoo.** Gana todas las encuestas ([§3](#3--quién-es-el-más-querido)).
- **La secundaria más querida es Cha Hae-In.** Entre las sombras, **Igris** va por delante de **Beru**.
- **El cuadro de diálogo propio es la ventana del Sistema.** Es un panel translúcido azul noche con filete fino claro, una barra de luz cian arriba y abajo, y la cabecera en un recuadro con el icono «!» en otro (NOTIFICACIÓN, QUEST INFO…). Nunca un globo blanco. Míralo en la hoja S·1-10.
- **La palabra que amenaza va en rojo carmesí** (`#9F205C`): «penalización», «te detendrá el corazón» (S·3, [clip del ep. 6 · 0:07](https://www.youtube.com/watch?v=Vzyw9z9F57M&t=7)).
- **La ventana va proyectada sobre un objeto real** (un mostrador, un cristal, un trono), no suelta en el aire. En la serie Jinwoo la sostiene como una tableta (S·7) o la tiene al lado mientras piensa (S·2).
- **Vocabulario latino oficial** (subtítulos de Crunchyroll): *portal*, *mazmorra*, *Asociación de Cazadores*, *rango E*, *gremio*, *soldados sombríos*, *Perjuicio* (debuff), y **«Surge.»** para el famoso *Arise*.
- **En el doblaje, Beru trata a Jinwoo de «mi rey» y de usted** (muestra de audio de Doblaje Wiki, §12.3).
- **La letra de la ventana:** Lato o Nunito para el texto, Exo 2 u Oxanium para los números. Todas traen tildes, ñ, ¿ y ¡.
- **La idea para los 14 hilos:** un sitio de la serie por hilo, con la ventana del Sistema dentro ([§19](#19--los-14-hilos-un-sitio-por-hilo)).

---

## 1 · El canal: #guia (textos reales del inventario)

- **Nombre:** `ıı・🗺️・guia` · foro · 14 hilos.
- **Etiquetas:** Primeros pasos · Roles y zonas · Si te atascas · Bots y comandos · Doblaje · Normas.
- **Descripción:** «El mapa del servidor. Cada hilo responde una pregunta. Filtra con las etiquetas de arriba o usa el buscador del foro. Si no encuentras lo q…»
  - ⚠️ El inventario la corta ahí (lo comprobé otra vez en la segunda pasada: `servidor/inventario.md`, línea 83, acaba en «lo q_»). No hay otra copia en el repositorio y no tengo acceso al Discord. Hay que copiar el texto entero antes de maquetar.

| # | Hilo | Adjunto actual |
|---|---|---|
| 1 | Cómo se entra | guia_1.png |
| 2 | 📌 La guía, de un vistazo | guia.png |
| 3 | 📌 De qué va esto | guia.png |
| 4 | Los roles que se ganan | guia_4.png |
| 5 | De dónde sale un rol | guia_4b.png |
| 6 | Reuniones y eventos | guia_6.png |
| 7 | Lo que pasa en vivo | guia_2c.png |
| 8 | Los roles que te pones tú | guia_3.png |
| 9 | El staff | guia_5.png |
| 10 | Cómo pedir algo | guia_7.png |
| 11 | Tus zonas: abre y cierra lo que veas | zonas.png |
| 12 | Los talentos | guia_4c.png |
| 13 | Dónde se trabaja | guia_2b.png |
| 14 | Lo que hay que leer | guia_2a.png |

Los hilos 2 y 3 comparten hoy `guia.png`. Con Solo Leveling cada uno tendría su lámina.

---

## 2 · La serie en datos

| Qué | Dato | Fuente |
|---|---|---|
| Novela web | Chugong, KakaoPage, desde el 25-jul-2016 | [Wikipedia][wp], [copia del texto][wp-txt] ✅ |
| Webtoon | Dubu (Jang Sung-rak, de Redice Studio), 2018-2021, 179 capítulos. Dubu murió en 2022 | [Wikipedia][wp-txt] ✅ |
| Anime T1 | A-1 Pictures, 12 cap., 7-ene a 31-mar-2024 | [ANN][ann-data1], [MAL][jk1] ✅ |
| Anime T2 | «Arise from the Shadow», 13 cap., 5-ene a 30-mar-2025 | [ANN][ann-data2], [MAL][jk2], [Wikipedia][wp-s2] ✅ |
| Título latino T2 | «Solo Leveling: **Surge desde las sombras**» | [ANMTV][anmtv-t2], [Arata][arata2], [DroideTV][droidetv] ✅ |
| Película | «ReAwakening»: resumen de la T1 más los cap. 1-2 de la T2. En latino: **«Solo Leveling: Segundo despertar»** (VSI, grabada de agosto a octubre de 2024) | [Wikipedia][wp-txt], [Aniplex][aniplex-kv2], [Doblaje Wiki][dw-film] ✅ |
| Película nueva | **«Solo Leveling: Beyond the System»**, en producción para cines. Sigue tras la T2. Aniplex, D&C Media y Crunchyroll | [vídeo conceptual de Crunchyroll en Español, 3-jul-2026][yt-beyond], [Variety][variety-beyond] ✅ |
| Dirección | Shunsuke Nakashige | [ANN][ann-data1], [Wikipedia][wp-s1] ✅ |
| Diseño de personajes | Tomoko Sudo | [ANN][ann-data1], [Wikipedia][wp-s1] ✅ |
| Dirección de arte | Yasuhiro Okumura (奥村泰浩) | [ANN][ann-data1], [descripción del PV 2 de Aniplex][yt-tr1] ✅ |
| **Gráficos en movimiento** (las ventanas del Sistema) | **Takemune Ōshiro, de Production I.G** (大城丈宗) | [PV 2 de Aniplex][yt-tr1], [ANMTV][anmtv-24] («gráficos en movimiento de Production I.G») ✅ |
| Diseño de monstruos · de objetos | Hirotaka Tokuda · Sōtarō Shiraishi | [PV 2 de Aniplex][yt-tr1] ✅, [ANMTV][anmtv-24] (Tokuda) |
| Música | Hiroyuki Sawano | [ANN][ann-data1], [Wikipedia][wp-txt] ✅ |
| Juegos | ARISE (Netmarble, 2024) y ARISE OVERDRIVE (Steam, 24-nov-2025) | [Wikipedia][wp-txt], [PC Gamer][pcgamer], [Steam][steam] ✅ |
| Premios | 9 premios en los Crunchyroll Anime Awards 2025, entre ellos **Anime del Año** y **Mejor Protagonista** (Jinwoo) | [Kakao][kakao], [THR][thr], [Gold Derby][goldderby] ✅ |

**Nombres:** el doblaje japonés usa nombres japoneses (Jinwoo es «Shun Mizushino», Cha Hae-In es «Shizuku Kōsaka»; así lo escriben sus CV oficiales, hoja P·3 y P·17). El latino usa los **coreanos**: «Sung Jinwoo», «Cazadora Cha». Así sale en los [subtítulos latinos][es13] y lo explica [Doblaje Wiki][dw] ✅. Doblaje Wiki añade dos detalles: el latino pone el nombre antes del apellido, y los personajes menores de la T2 sí llevan nombres japoneses. **En la lámina, nunca «Shun».**

---

## 3 · ¿Quién es el más querido?

| Encuesta | Resultado | Fuente |
|---|---|---|
| Favoritos en MyAnimeList | Jinwoo **19 223** · Cha Hae-In **3 602** · Igris **886** · Esil 589 · Beru **516** | [Jikan T1][jkc1], [Jikan T2][jkc2] ✅ |
| Top 1000 de MAL | Jinwoo, puesto 100 · Cha Hae-In, puesto 580 | [lista MAL][mal-top] ✅ |
| Nlab (Japón, abril 2024) | 1.º Jinwoo · **2.º Cha Hae-In** (向坂雫) | [nlab][nlab-res] ✅ |
| Dengeki Online (Japón, abril 2024) | 1.º Jinwoo, con cerca de 1,5 veces los votos del 2.º | [Dengeki][dengeki-res], [convocatoria][dengeki-vote] ✅ |
| Crunchyroll Anime Awards 2025 | Jinwoo, **Mejor Protagonista**. 51 millones de votos | [Wikipedia][wp-awards], [Inquirer][inquirer] ✅ |
| Anime!Anime! (Japón, 9-13 ene., 1366 votos): el personaje favorito de **Reina Ueda**, su voz japonesa | Cha Hae-In **no entró en el top 10**; ganaron Reze y Kanao | [CBR][cbr-cha] (leído entero en la 2.ª pasada) ⚠️ (una fuente) |
| Reddit r/sololeveling, tras el final de la T2 (29-31 mar-2025) | Los posts más votados: la pregunta «¿es más fuerte que Jinwoo?» (6021 votos, 1043 comentarios), el arte de fans de Cha Hae-In y Jinwoo (2257) y «la vida diaria de las sombras» (345) | [Arctic Shift][as-sl] ✅ |

**Conclusión**
- Aquí el protagonista **sí** es el más querido. Jinwoo narra.
- La **secundaria** más querida es **Cha Hae-In**. Va para los hilos «sociales» (eventos, reuniones).
- Entre las sombras gana **Igris** (886 frente a 516 de Beru). Beru llegó al final de la T2, pero es el rey de los memes ([TikTok][tt-king]). Mejor en una lámina 2.
- Ojo: en Japón la serie gusta menos que fuera. En la encuesta TAAF de fans japoneses la T2 quedó en el puesto 61 ([CBR][cbr-cha] ⚠️). Para un servidor latino da igual: aquí manda Crunchyroll, donde ganó todo.

---

## 4 · El Sistema: cómo «habla» la serie (lo más importante)

### 4.1 Qué es
- Es un programa misterioso que elige a Jinwoo como su único **Jugador**. Solo él puede subir de nivel ([Wikipedia][wp-txt] ✅).
- Aparece como una **pantalla holográfica** que solo ve Jinwoo. En el webtoon los mensajes van **entre corchetes** ([wiki: System][wiki-system], guía de cuadros del repo ✅).
- Sus primeras frases son de manual de normas (ep. 3 · 07:34, [subs][nf03] ✅):
  - «This system is designed to assist the development of the player.»
  - «Failure to comply with the system may result in a penalty.»
  - Es decir: el Sistema **ayuda al Jugador**, y si no se cumple hay **penalización**. Encaja perfecto con el hilo «Lo que hay que leer».

### 4.2 Cómo es la ventana (medida en el anime)
Datos de la guía del repo, medidos en una captura oficial ✅:
- **Panel rectangular oscuro**, azul violáceo `#211B32`, translúcido.
- **Doble filete fino**, blanco azulado.
- **Título dentro de un recuadro** (STATUS, NOTIFICACIÓN…).
- Texto en blanco, con los números grandes y finos. Las subidas van en **verde** («+55»).
- Versión «Monarca» (T2): marco de neón violeta `#9229F9` y magenta `#ED77F3`, hecho de líneas de circuito.

**Segunda pasada: lo que vi en 10 capturas de la T1** (hoja `sistema_01.jpg`; hex medidos con Pillow) ✅
- **Quién la hace:** las ventanas son **gráficos en movimiento de Production I.G** (Takemune Ōshiro), no del estudio A-1 ([PV 2][yt-tr1], [ANMTV][anmtv-24]).
- **La primera (ep. 3, S·1; resumen del capítulo en la [wiki][wiki-ep3]):** «NOTIFICATION» con el texto en espejo, porque la vemos desde detrás. Casi transparente: en el hospital se ve gris azulada (`#5D646C` de media) y deja ver la cama. Encima y debajo, **una barra de luz** blanco-cian (`#D4EDFF`).
- **La de aviso (ep. 10, S·10):** panel azul noche translúcido (`#112A39`) sobre fondo azul (`#233E53`). Esquinas de circuito cian brillante (`#82F3FA`). Cabecera **«NOTIFICATION»** en blanco (`#E7F5FA`) dentro de un recuadro, y **el icono «!» en un círculo, en otro recuadro a la izquierda**. Texto: «A ***job-change quest*** can now be ordered.»: la palabra clave va en negrita cursiva.
- **La de misión (ep. 6, S·3):** «QUEST INFO» con el «!» a la izquierda. Debajo, entre corchetes, **[Urgent Quest: Defeat the Enemies.]**, y «GOAL» subrayado. Termina con «WARNING: … you will receive an appropriate **penalty**»: **«penalty» va en rojo carmesí** (`#8B1F5E` en la captura pequeña).
- **La de estado (ep. 5, S·2):** panel oscuro vertical (`#1E2D37`) de pie junto a Jinwoo, con una barra de luz blanca arriba (`#F0FBFE`). Él la mira **con la mano en la barbilla**: la pose de «pensar».
- **La de compra (ep. 12, S·6):** negra (`#0B0905`), filete gris fino. «Would you like to purchase?» y el objeto **[Knight Killer]** en negrita cursiva entre corchetes. Botones **CANCEL · BUY** en mayúsculas muy espaciadas, cada uno en su rectángulo. El precio lleva un punto blanco (la moneda).
- **La tienda (ep. 12, S·7):** Jinwoo la sujeta **como una tableta**, inclinada, con el atardecer detrás. **Esto es lo que pide el dueño: la ventana como objeto que se sostiene.**
- **El temporizador (ep. 12, S·8):** un rótulo pequeño con marco de pinchos cian flota **sobre la cabeza** de Jinwoo («04:29:16»).
- **Los estados negativos (ep. 6, S·4):** barras anchas «[Debuff] Paralysis Lv.–» y «[Debuff] Drain». En latino, **«[Perjuicio] Parálisis»** y «[Perjuicio] Drenaje» (cartel del [clip oficial doblado, 0:46][yt-clip6-46]).
- **La receta (ep. 7, S·5):** «FORMULA: Elixir of Life», con un icono de pergamino en su propio recuadro.
- **El aviso del mundo real (ep. 8, S·9):** no es el Sistema: es **el móvil de Jinwoo**. Tarjeta blanca «Notice · New message: 1 · From: **Hunter's Association** · Urgent: **Request to Participate in D-rank gate** · Clear | View». Es el otro cuadro de diálogo de la serie: el de la Asociación, blanco y de oficina.
- **La barra roja del miedo (ep. 6, [clip 0:07-0:15][yt-clip6-7]):** «WARNING: If you do not complete this quest, **YOUR HEART WILL STOP.**» en blanco cian (`#CFF2F9`) y **rojo carmesí** (`#9F205C`). El cartel latino: **«ADVERTENCIA: No cumplir la misión TE DETENDRÁ EL CORAZÓN.»**
- **Resumen de la paleta de la ventana T1:** fondo `#112A39`, filete y esquinas `#82F3FA`, barra de luz `#D4EDFF`-`#F0FBFE`, texto `#E7F5FA`, amenaza `#9F205C`.

### 4.3 El vocabulario oficial en español latino
Sale de los carteles de los subtítulos latinos de Crunchyroll, T2 ✅ (archivo abierto; traducción de Iris de la Fuente y Nicolás Sepúlveda):

| Título de la ventana | Dónde |
|---|---|
| **NOTIFICACIÓN** | ep. 13 · 17:28 · [subs][es13] · y ep. 14, 15 y 18 |
| **INVENTARIO** | ep. 13 · 14:37 · [subs][es13] |
| **[Título]** «El que superó las adversidades» / «Asesino de Lobos» | ep. 13 · 15:33 · [subs][es13] |
| **HABILIDADES** | ep. 15 · 12:45 · [subs][es15] |
| **FABRICAR** · Objeto: Elíxir de la Vida | ep. 15 · 08:11 · [subs][es15] |
| **OBJETO:** Permiso de entrada | ep. 15 · 10:36 · [subs][es15] |
| **[Colmillo Nv. 1]** (la sombra de Kargalgan) | ep. 18 · 18:14 · [subs][es18] |
| «Misión diaria completada.» | ep. 22 · 20:29 · [subs][es22] |
| «Intercambio de sombras.» | ep. 21 · 03:37 · [subs][es21] |
| «Habilidad: Dominio del Rey.» | ep. 18 · 08:09 · [subs][es18] |

**Otras palabras de esos subtítulos ✅:**
- *portal* (gate) y *portal rojo*.
- *mazmorra* y *mazmorra doble*.
- *Cazador de rango E*.
- *Asociación de Cazadores* y *Supervisión*.
- *Gremio de Cazadores* y *Gremio Tigre Blanco*.
- *soldados sombríos* y *Rey de las Sombras* (la clase de Jinwoo, ep. 13 · 01:24).
- Ojo: en estos subtítulos, Shadow Monarch se dice «Rey de las Sombras», no «Monarca». Monarca solo aparece en «Monarca Demoníaco Baran».

### 4.4 Cómo hablan los personajes en pantalla
- **Pensamientos de Jinwoo:** van en **cursiva**, sin globo. Así los marcan los subtítulos (`<i>`) ([subs Netflix][nf12], [subs latinos][es13] ✅). En la lámina, su pensamiento sería una línea en cursiva junto a la ventana.
- **Las sombras casi no hablan.** Solo las de grado comandante o superior pueden hablar ([Wikipedia][wp-txt] ✅). Igris **no tiene actor de voz** en MAL ([Jikan][jkc1] ✅). Igris «dice» con gestos: se arrodilla ante su amo tras cada batalla ([Wikipedia][wp-txt] ✅).
- **Beru sí habla**, porque es de grado General y esas sombras pueden hablar ([wiki: Shadows][wiki-shadows] ✅). En el ep. 25 (09:04-10:01, [subs VI][vi25] ✅) se arrodilla y pide un nombre. En el doblaje latino dice, textual: **«Mi rey… necesito que usted me dé un nombre. Se equivoca, yo no morí, mi rey. Es gracias a su mano que yo he podido renacer. Todo mi ser se encuentra lleno de júbilo. Juro que voy a servirle por la eternidad. Ahora, por favor, concédame un nombre.»** ([muestra de audio de Doblaje Wiki][dw-beru-sombra], transcrita con Whisper ✅ contenido; ⚠️ alguna palabra puede fallar). Su frase inglesa «My King is the greatest being in this universe…» sigue con [una sola fuente][rslm-beru] ⚠️ (es de la novela o el webtoon, no la oí en el anime).
- **La orden «Arise»** es una sola palabra, seca. En los subtítulos latinos es **«Surge.»** (ep. 14 · 12:48, ep. 18 · 17:49, ep. 21 · 02:33, [subs][es14] ✅). En los ingleses, «Arise.» en el mismo minuto ([subs EN][en14] ✅). En el ep. 25 · 10:07 vuelve a sonar tras nombrar a Beru ([subs VI][vi25]: «Trỗi dậy đi!»).
  - ⚠️ Sigo sin poder **oír** si el doblaje dice «Surge» o «Levántate»: YouTube no deja bajar el audio y Doblaje Wiki no tiene muestra de esa escena. Lo que sí es seguro: Crunchyroll Latinoamérica usa **«SURGE»** como verbo de marca («🔥SURGE🔥 con los secretos detrás del doblaje», [descripción del vídeo][yt-bts]) y el título latino de la T2 es «Surge desde las sombras». En la lámina, «Surge.»

### 4.5 El cuadro para la lámina
- **Forma:** rectángulo de esquinas rectas, sin cola. El Sistema no «sale» de nadie. Las esquinas llevan **piezas de circuito** cian (S·10), no redondeos.
- **Relleno:** `#112A39` (T1, medido en S·10) o `#211B32` (guía del repo) al 70-80 % de opacidad, con un leve degradado hacia `#1C254E` (el azul del abrigo en la KV de la T2).
- **Borde:** doble filete de 1-2 px en blanco azulado `#C5E8EE`, con un brillo exterior suave cian `#89BAD3`. Esquinas en `#82F3FA`.
- **Barra de luz:** una línea horizontal muy brillante (`#D4EDFF`) que sobresale arriba y abajo del panel (S·1, S·5). Es lo que hace que parezca proyectada.
- **Cabecera:** la palabra en MAYÚSCULAS dentro de un recuadro propio (NOTIFICACIÓN, MISIÓN, INVENTARIO), y **el icono «!» en un círculo, en su propio recuadro a la izquierda** (S·3, S·10). Línea fina debajo.
- **Texto:** blanco, frases cortas. Los nombres de objeto o de rango van **entre corchetes y en negrita cursiva**: ***[Rango E]***, ***[Colmillo Nv. 1]***.
- **La amenaza en rojo:** sólo una palabra o frase por ventana, en carmesí `#9F205C`: «penalización», «te detendrá el corazón». Sirve para las normas.
- **Botones:** dos rectángulos con MAYÚSCULAS muy espaciadas (CANCELAR · ACEPTAR), como en S·6.
- **Dos variantes:**
  - **Azul (novato):** para los hilos de primeros pasos.
  - **Violeta Monarca** (`#9229F9` / `#ED77F3`): para staff, roles altos y talentos.
- **Pegado al mundo:** la ventana debe proyectar luz sobre la escena (reflejo en el mostrador, brillo en la cara del personaje). Al dueño no le gustan los paneles sueltos.

### 4.6 En los videojuegos
- **Solo Leveling: ARISE** cuenta la historia con **viñetas del webtoon animadas** (cómic en movimiento) más escenas en 3D. Predominan las viñetas ([Siliconera][silic], [Sportskeeda][sk-review], [CBR][cbr-review] ✅).
- En el juego repiten las voces del anime. En inglés, Aleks Le hace de Jinwoo ([Siliconera][silic]; y la tarjeta oficial de cuenta atrás del anime con su firma, [wiki][wiki-aleks] ✅).
- **Game UI Database** sigue en 403 (Cloudflare) también con la red abierta. Las cajas de diálogo exactas del juego quedan sin medir ⚠️.

---

## 5 · Tipografía

| Uso | Letra original (según fans) | Libre parecida | ¿Tildes, ñ, ¿ ¡? |
|---|---|---|---|
| Logo «SOLO LEVELING» | **Eternal** (FG Studios), gratis solo para uso personal ([FontBolt][fontbolt], [Free Fonts Vault][ffv]) ⚠️ | **Cinzel** (mayúsculas afiladas) o **Michroma** (ancha, técnica) | Cinzel ✅ · Michroma ✅ |
| Títulos del Sistema | **Trueno Round** / **Circe Rounded ExtraBold** ([FontBolt][fontbolt]) ⚠️ | **Nunito** Black o **Varela Round** | ✅ · ✅ |
| Texto del Sistema | **Lato** ([FontBolt][fontbolt]) ⚠️ | **Lato** (es libre) | ✅ |
| Números del Sistema | **Caros Soft** ⚠️ | **Exo 2**, **Oxanium** o **Rajdhani** | ✅ · ✅ · ✅ |
| Logo del juego ARISE | parece **Metal Mania** ([designbeep][designbeep]) ⚠️ | **Metal Mania** es libre (OFL) | ✅ (comprobado en la 2.ª pasada) |
| Logo del anime en pantalla (final del opening, [OP · 1:24][yt-op1-84]; visuales F·18-19) | **serifa clásica en MAYÚSCULAS muy espaciadas**, «S O L O  L E V E L I N G», con un adorno en la V | **Cinzel** o **Marcellus** | ✅ · ✅ |
| Rótulos del tráiler latino («ESTE INVIERNO», «ENERO DE 2024», [tráiler · 1:29][yt-trailer-89]) | palo seco geométrico, MAYÚSCULAS muy espaciadas, blanco sobre una rejilla azul de interfaz (`#08152E`) | **Michroma** o **Josefin Sans** | ✅ · ✅ |
| Título del ending de la T2 ([ED · 0:37][yt-ed2-37]) | palo seco muy grueso y estrecho, **rojo `#AA033D`** | **Anton** o **Bebas Neue** | ✅ · ✅ |
| Letras coreanas (carteles) | — | **Noto Sans KR** | ✅ |
| Letras coreanas gruesas | — | ❌ **Black Han Sans no trae tildes ni ñ** | ❌ (comprobado) |
| «Solo Level» (dafont, de Esa Nugroho) | letra de fan inspirada en el logo | solo uso personal ([dafont][dafont-sololevel], [1001 Fonts][1001]) | **trae tildes y ñ, pero no ¿ ni ¡** (114 glifos; comprobado con el archivo `SoloLevelDemo.otf`) |

**Cómo se comprobó:** cada `.ttf` se bajó del repositorio oficial de Google Fonts ([Lato][gf-lato], [Nunito][gf-nunito], [Exo 2][gf-exo2], [Oxanium][gf-oxanium], [Cinzel][gf-cinzel], [Varela Round][gf-varela], [Noto Sans KR][gf-notokr], [Black Han Sans][gf-bhs]). Luego se buscaron á é í ó ú ñ ¿ ¡ ü en su tabla de caracteres. Black Han Sans dice «latin» en su ficha, pero **no trae** ninguno de esos signos. En la segunda pasada repetí la prueba con fontTools para **Metal Mania, Anton, Bebas Neue, Michroma, Josefin Sans, Marcellus, Rajdhani, Oxanium, Exo 2, Nunito, Lato y Cinzel: las 12 traen todo**, y todas son SIL Open Font License.

**Por qué siguen dudosas Eternal, Trueno Round, Circe Rounded y Caros Soft:** son letras comerciales que citan los fans. Ni Aniplex ni Production I.G publican qué letra usa la ventana. Lo que sí vi: las cabeceras son **palo seco geométrico en MAYÚSCULAS espaciadas** (S·3, S·10) y los botones igual (S·6). Nunito Black y Michroma encajan.

**Recomendación:** Nunito Black en MAYÚSCULAS para la cabecera, Lato Regular para el texto y Exo 2 para cifras y rangos.

---

## 6 · Personajes a fondo

### 6.1 Sung Jinwoo (protagonista, el más querido)
- **Quién es:** empieza como cazador de **rango E**, «el Cazador más débil de la humanidad» (ep. 1 · 05:55, [subs][nf01] ✅). Tras la mazmorra doble, el Sistema lo elige como Jugador. Sube de nivel sin límite y se convierte en el **Rey de las Sombras** ([Wikipedia][wp-txt], [AniList][anilist] ✅).
- **Qué le importa:** su familia. Su madre está en coma («Sueño Eterno») y su hermana Jinah va al instituto. Es humilde y quiere hacerse fuerte ([AniList][anilist], [Wikipedia][wp-txt] ✅).
- **Miedo:** volver a ser el débil que ve morir a los demás. Así lo dicen sus monólogos: «I need to become stronger» (ep. 7 · 15:09, [subs][nf07] ✅).
- **Cómo habla:** frases cortas, secas, sin presumir. Ejemplos con minuto:
  - «I'm already used to it.» (ep. 1 · 07:08, [subs][nf01] ✅)
  - «Como yo te traje, me haré responsable de ti. A cambio, no preguntes nada.» (ep. 13 · 15:05, [subs][es13] ✅)
  - «Sí, algo así.» / «Puedo invocar otros cien.» (ep. 19 · 06:03 y 06:23, [subs][es19] ✅)
  - «Lo siento, tengo planes.» (a Cha Hae-In, ep. 19 · 07:27, [subs][es19] ✅)
  - «Creo que mi lugar está en las mazmorras.» (ep. 16 · 11:46, [subs][es16] ✅)
- **Cómo convence:** explica con calma y luego ordena. Su discurso a Igris (ep. 12 · 20:00-20:25, [subs][nf12] ✅): «You are a warrior… Fight for me. Don't guard that empty throne. Protect me, who stand before you. **Arise.**»
- **Cómo habla en el doblaje latino** (muestras de audio de [Doblaje Wiki][dw], transcritas): de novato, cansado y resignado. «Pero este cuchillo barato es lo único que pude comprar.» «Así es como suelo vivir, un día tras otro.» De rango B ya calcula en frío: «Siempre golpean al clavo que sobresale. Mejor lo olvido.»
- **Cuerpo (visto en la 2.ª pasada):**
  - De novato va **encorvado, con la mochila a la espalda y la mano en la nuca** (ep. 1, captura de la wiki [P262][w-p262]). Se tapa la cara con vendas y tiritas ([tráiler · 0:39][yt-trailer-39]).
  - Cuando piensa, **mano en la barbilla y media sonrisa** delante de su ventana (ep. 5, S·2).
  - Ya fuerte, **mirada fría con la cara en sombra y los ojos encendidos** en azul ([clip ep. 6 · 0:21][yt-clip6-21]) o en violeta en la T2 ([captura oficial del ep. 19][w-e593]). **Casi no sonríe**; cuando lo hace es de lado (CV de la T2, P·3).
  - En la T2 **ofrece la mano abierta hacia cámara** (P·3) o camina **con una mano en el bolsillo y la daga en la otra** (P·2).
- **Voz latina:** Fernando Moctezuma ✅ ([§12](#12--doblaje-latino)).

### 6.2 Igris (el caballero, la sombra más querida)
- **Quién es:** «Knight Commander, Igris the Bloodred», el comandante de sangre. Guarda un **trono vacío** en la mazmorra del cambio de clase (ep. 11 · 10:18 y 10:29, [subs][nf11] ✅).
- **Cómo se une:** Jinwoo falla dos extracciones y le convence al tercer intento (ep. 12 · 19:08, 19:32 y 20:25, [subs][nf12] ✅, [AniList][anilist] ✅).
- **Carácter:** leal, gran espadachín, **se arrodilla ante su amo tras cada batalla**. Le molesta la torpeza de Iron. En la novela discute con Bellion sobre la escuela de Suho ([Wikipedia][wp-txt] ✅).
- **Cómo se expresa:** no habla. Postura, espada y reverencia. Sube de rango en la T2: «Igrit y Tank ascendieron al subir de nivel» (ep. 20 · 09:01, [subs][es20] ✅). El cartel vietnamita dice «Caballero de élite» ([subs VI][vi20] ✅).
- **Cómo es (visto):** como jefe, **armadura roja sangre con un penacho rojo muy largo** y espada larga de filo dorado, en un salón de columnas violeta con alfombra roja ([clip del ep. 11 · 0:03-0:19][yt-papu-3]). Como sombra, **armadura negra con líneas cian** (`#5DE3EC`, brillo `#AEFDFF`), capa rota y el mismo penacho rojo (P·11, P·20). En el anime la **cicatriz está en el ojo derecho** ([wiki][wiki-igris] ✅).
- **Su nombre:** en japonés es **Igrit** (イグリット), y así lo rotula su visual oficial (P·11). Los subtítulos latinos dicen «Igris» (ep. 13 · 20:00) y una vez «Igrit» (ep. 20 · 09:01). En la lámina, «Igris».
- **El chiste de los fans:** Igris siempre le trae a Jinwoo **las cabezas de sus presas** y le molesta que Iron lo copie ([wiki][wiki-igris] ✅, [Wikipedia][wp-txt] ✅). En la novela defiende que Suho **estudie en la escuela** en vez de pelear.
- **Uso en la guía:** el **staff**. Guarda, sirve y no discute.

### 6.3 Beru (el Rey Hormiga)
- **Quién es:** la sombra del **Rey Hormiga** de la isla de Jeju. Fue el jefe final de la incursión y dejó fuera de combate a Cha Hae-In ([Wikipedia][wp-txt], [namu.wiki][namu-beru] ✅).
- **Cuándo sale:** recibe su nombre en el ep. 25 · 09:56-09:59: «Beru. … Tu nombre es Beru.» El cartel dice «General · Nv. 1» ([subs VI][vi25] ✅).
- **Carácter:** lealtad exagerada, casi cómica, con Jinwoo ([Wikipedia][wp-txt], [DualShockers][dualshockers] ✅: las dos lo dicen). En la novela adora a Suho, el hijo de Jinwoo ([Wikipedia][wp-txt] ✅).
- **Antes de ser sombra** (ep. 24): el Rey Hormiga busca «al rey de los humanos». «¿Eres el rey de los humanos?» (07:58) es el título del capítulo ([subs VI][vi24], traducción mía ✅). A las 19:27 se oye «¡Pero si yo soy el rey!» (⚠️ el subtítulo no dice quién habla; puede ser él o Jinwoo). En el doblaje: «¡Debo vivir! ¡Debo sobrevivir!» ([muestra][dw-beru-trans]).
- **Cómo habla ya como sombra** (ep. 25 · 09:04-10:47, [subs VI][vi25] + [muestra del doblaje][dw-beru-sombra] ✅): de usted, «mi rey» en cada frase, solemne. Tras recibir el nombre: «Gracias, es un honor.» Ante una orden: «Si es la voluntad de mi rey. Dé la orden.» Jinwoo sólo contesta: «Hazlo.»
- **Diseño:** en el anime, A-1 lo mejoró respecto al webtoon ([Sportskeeda][sk-beru] ⚠️, una opinión). Como sombra: cuerpo de hormiga negra muy estilizado con **alas de luz azul** (P·16).
- **Voz japonesa:** Akira Ishida ✅ ([Anime Corner][animecorner], [MAL][jkc2]). **Latina:** **Daniel Lacy** ✅ ([Doblaje Wiki][dw] + [MAL][jkc2]).
- **Uso en la guía:** «Los talentos», en lámina 2. Es el que presume de su rey.

### 6.4 Cha Hae-In (la secundaria más querida)
- **Quién es:** cazadora **rango S**, vicemaestra del **Gremio de Cazadores** y novena cazadora del país ([AniList][anilist] ✅; «la novena Cazadora S del país», ep. 16 · 18:52, [subs][es16] ✅).
- **Apodo:** «**Cha Hae-in, la Bailarina**» (ep. 16 · 18:56, [subs][es16] ✅), por su estilo con la espada.
- **Rasgo único:** huele el maná. El olor de los cazadores le da asco, salvo el de Jinwoo ([AniList][anilist], [Wikipedia][wp-txt] ✅).
- **Cómo habla:** directa, protectora, sin rodeos (ep. 17 · 02:01-02:20, [subs][es17] ✅):
  - «Esa es la sala del jefe. Aléjate.»
  - «Sal cuanto antes.»
  - «Provocar al jefe ahora conllevaría la muerte de todos los mineros.»
- **Cómo es (visto):** **rubia, melena corta**, ojos grises que brillan en amarillo al pelear. **Uniforme rojo** (`#BC2B47`, sombra `#6D273B`) con blanco (`#F4EFE7`), hombreras doradas y **espada negra de guarda plateada** ([wiki][wiki-cha] ✅, CV oficial P·17 y render P·18 ✅). Pelo medido `#E2D2B4`.
- **Carácter (wiki):** seria, tranquila y atenta. Patrulla la sala del jefe para que no mueran los mineros. Sigue tomando clases de kendo aunque ya es rango S ([wiki][wiki-cha] ✅).
- **Cómo habla en el doblaje:** formal, de usted, sin adornos. «Entonces, ¿cómo puedo ayudarle?» «Con permiso.» «Pensé que debería saberlo.» «Le dije que no estaba interesada.» ([muestra de Doblaje Wiki][dw-cha]).
- **Poses oficiales:** desenvainando con los dos brazos arriba y la mirada de lado (P·17); de pie, espada baja, capa al viento (P·18); de perfil bajo luz azul (P·19, ep. 16).
- **Relación:** se enamora de Jinwoo. En el webtoon se casan ([Wikipedia][wp-txt] ✅; spoiler, no usar).
- **Voz latina:** Sofía Huerta, que además dirige el doblaje ✅.

### 6.5 El Sistema (como personaje)
- Es frío, burocrático e inapelable. Premia, castiga y no explica.
- Da la «misión diaria» (100 flexiones, 100 abdominales, 100 sentadillas y 10 km, en 24 horas). Si no la cumples, te manda a la **Zona de Penalización**, un desierto con ciempiés gigantes ([wiki][wiki-prep], [wiki][wiki-penaltyq], [Epicstream][epic] ✅).
- **Voz en la lámina:** sin sujeto, en imperativo o impersonal. Por ejemplo: «Misión aceptada.», «Se ha concedido el rol.», «El incumplimiento conlleva penalización.»

### 6.6 Secundarios útiles para la guía
- **Yoo Jinho:** rango D, hijo rico, fiel ayudante de Jinwoo. Siempre con armaduras caras, que es un chiste recurrente ([Wikipedia][wp-txt] ✅; «Yoo Jinho shining armor», captura del ep. 5 en la wiki). Le llama «**jefe**» y le trata de usted: «¿Qué hará usted, jefe?» (ep. 15 · 03:46, [subs][es15] ✅). En el doblaje se presenta así (ep. 5 · 09:02, [subs][nf05] ✅): **«Soy Yoo Jinho, 21 años y rango D.»** «No te preocupes, yo voy a mantenerte a salvo.» «Disculpa, es que nunca he sido muy bueno en las cuestiones sociales.» ([muestra][dw-jinho]). Habla mucho y se disculpa. Va para «Cómo pedir algo».
- **Go Gunhee:** presidente de la Asociación de Cazadores, rango S y anciano ([AniList][anilist] ✅). «Soy Go Gunhee, presidente de la Asociación de Cazadores.» (ep. 16 · 09:00, [subs][es16] ✅). En el doblaje explica como un profesor: «Todos los cazadores vivimos de la venta de los recursos que hay dentro de las mazmorras.» ([muestra][dw-gunhee]). En el opening sale **de brazos cruzados ante una ciudad en ruinas** ([OP · 0:54][yt-op1-54]). Traje negro y corbata (P·22). Va para «De qué va esto».
- **Woo Jinchul:** rango A. Fue **jefe inspector del equipo de Supervisión** de la Asociación con Go Gunhee, y luego presidente ([wiki][wiki-jinchul] ✅ + la frase «En Supervisión vigilamos a los Cazadores», ep. 16 · 08:22, [subs][es16] ✅). Traje negro, pelo rubio peinado atrás (P·23). En el doblaje, seco y de informe: «El trabajo de un cazador es un trabajo peligroso, pero es raro ver un resultado tan trágico.» ([muestra][dw-jinchul]). Va para «El staff» y «Normas».
- **Sung Jinah:** la hermana, que no es cazadora ([Wikipedia][wp-txt] ✅). Es la voz del recién llegado. En el hospital (ep. 3 · 07:06-07:12, [subs][nf03] ✅) Jinwoo le pregunta por los videojuegos. **Ella contesta**: «Just open the message box». En el doblaje: **«Sí, es cierto. Lo normal sería abrir la caja de mensajes.»** Antes le riñe: «Oye, necesitas tener más cuidado. ¿Tienes idea de lo preocupada que estaba?» ([muestra][dw-jinah] ✅). Uniforme escolar azul y coleta (P·24).
- **Song Chiyul:** rango C, el veterano amable del ep. 1. Es **el líder que presenta la incursión**: en el doblaje, «Hola a todos, soy el líder de la incursión del día de hoy… me llamo Song Chiyul. Un gusto conocerlos.» y «¡Entremos!» (ep. 1 · 07:20 y 07:37, [subs][nf01] ✅; [muestra][dw-chiyul]). Luego propone votar (ep. 1 · 12:42). Va perfecto para «Cómo se entra».
- **Iron, Tank, Colmillo y Kaisel:** sombras con nombre, en el ep. 14 · 13:10, el ep. 15 · 11:32, el ep. 18 · 18:10 y el ep. 20 · 12:57 ([subs][es14], [subs VI][vi20] ✅). Iron copia a Igris y le trae cabezas, para disgusto de Igris ([Wikipedia][wp-txt] ✅). Kaisel es un wyvern (dragón volador) que casi solo sirve de montura ([Wikipedia][wp-txt] ✅).

---

## 7 · Poses analizadas

Cada pose lleva capítulo y minuto, o un enlace. «Uso» = presentar, explicar, celebrar, regañar, pensar o animar. En la segunda pasada **las miré**: en las hojas de la wiki (P·, S·, F·) y en los *storyboards* de los clips oficiales (§14). Los minutos «ep. N · mm:ss» son del capítulo; los de «clip · m:ss» son del vídeo de YouTube enlazado.

### Jinwoo
1. **KV T1, arriba** ([imagen][kv1], 948×1280 ✅ medida): de pie sobre ruinas, una pierna flexionada en alto, un brazo extendido con una daga roja, abrigo claro abierto al viento. Mirada al frente, por encima del hombro. → **presentar** (el cazador ya fuerte).
2. **KV T1, abajo** ([imagen][kv1] ✅): sentado entre monstruos muertos, sudadera azul, cuchillo en una mano y la otra sobre la rodilla, mirada hacia arriba, tenso. → **pensar** (el novato; hilo «Cómo se entra»).
3. **KV T2** ([imagen][kv2], 1308×1848 ✅): perfil mirando hacia arriba, cuello estirado, ojos violeta, borde de luz roja, abrigo negro. El ejército de sombras sale de su espalda. → **presentar** o **celebrar** (portada de la guía).
4. **ep. 3 · 07:34-08:07** ([subs][nf03] ✅; visto en S·1 y en el [tráiler · 1:10][yt-trailer-70]): **sentado en la cama del hospital, con bata azul clara, mirando de frente la ventana «NOTIFICATION»** que flota entre él y la cámara; una mano levantada hacia ella. → **pensar** / **explicar** («Lo que hay que leer»).
5. **ep. 5, captura de la wiki (S·2)**: **de pie, de perfil, camiseta blanca, dos dedos en la barbilla y media sonrisa** frente a su ventana de estado. → **pensar** / **explicar**. Es la mejor pose para una ventana grande al lado.
6. **ep. 6 · 02:47** «The real hunt begins now.» ([subs][nf06] ✅). En el clip oficial: **de pie en la cueva de cristal azul, sudadera cian abierta, daga en la mano baja, cara en sombra y ojos brillando** ([clip · 0:21-0:27][yt-clip6-21]). → **animar** / **advertir**.
7. **ep. 12 · 17:39** primer «Arise» ([subs][nf12] ✅). ⚠️ El gesto exacto de la mano no lo vi: la wiki sólo tiene la captura de la extracción de Igris ([índice P 250, «Jinwoo extracts Igris shadow»][w-p250]: agachado, mano hacia el suelo). → **celebrar**.
8. **ep. 12 · 20:00-20:25** discurso a Igris ([subs][nf12] ✅): de pie frente al trono vacío, habla de frente. Tras vencer: **de pie, sudadera gris, daga baja, Igris derrotado detrás** ([clip ep. 11 · 1:29-1:31][yt-papu-89]). → **explicar** o **regañar** con calma.
9. **ep. 12, tienda (S·7):** **sujeta la ventana como una tableta** con una mano, inclinada, a contraluz de un atardecer naranja. → **explicar** («Los roles que te pones tú»).
10. **ep. 16 · 03:47** reevaluación en la Asociación: «Ponga la mano sobre ese cristal negro.» El medidor no puede calcular su poder (04:27-04:35) ([subs][es16] ✅). Oficina con funcionarios de traje (S·15-16). → **explicar** («De dónde sale un rol»).
11. **ep. 19 · 06:48-07:00** «Aquí tienes tu nueva licencia.» «Ahora eres oficialmente un cazador de rango S.» ([subs][es19] ✅) → **celebrar** («Los roles que se ganan»).
12. **ep. 22 · 20:29** «Misión diaria completada.» ([subs][es22] ✅) → **animar** (el ritual diario, un guiño para los fans).
13. **CV de la T2 (P·3):** **brazo estirado hacia cámara, mano abierta**, media sonrisa, abrigo azul noche con capucha. → **presentar** / **invitar** («Cómo se entra», «La guía, de un vistazo»).
14. **Cuenta atrás de la T2 (P·7, P·8, P·9):** de pie, relajado, **con su sombra detrás** (Igris o Tank) enorme. → **presentar al equipo** («El staff», «Los talentos»).

### Igris
1. **ep. 11 · 10:18-10:31** presentación en el salón del trono vacío ([subs][nf11] ✅). En el clip: **de pie ante el trono, espada vertical, penacho rojo cayendo** ([clip · 0:03-0:11][yt-papu-3]). → **presentar**.
2. **ep. 12 · 20:25** acepta a Jinwoo y se arrodilla ([Wikipedia][wp-txt] y [wiki][wiki-igris] ✅ que es su gesto). ⚠️ El minuto exacto del gesto no sale en los subtítulos (no hay diálogo); búscalo entre 20:25 y 20:45.
3. **KV T2** ([imagen][kv2] ✅): caballero negro de contorno cian, casco con penacho y espadón en vertical. → **guardar** («El staff»).
4. **CV «IGRIT» (P·11):** de frente, hombros anchos, **líneas cian por la armadura negra** sobre fondo rojo. → **presentar** (ficha del staff).
5. **ep. 14, en la nieve (P·20):** **de pie detrás de Jinwoo, como un guardaespaldas**, capa y penacho al viento. → **acompañar**, «El staff».
6. **ep. 13 · 20:00** invocado por su nombre: «Igris.» ([subs][es13] ✅). → **animar** o **actuar**.
7. **ep. 20 · 09:01** asciende de rango ([subs][es20] ✅). → **celebrar** («Los roles que se ganan»).
8. **ep. 20 · 15:28** «¡Colmillo! ¡Igrit!» en combate ([subs latinos][es20] ✅). → acción.
9. **Modelos 3D CC BY** para posarlo en Blender: [Igris de missafe][sk-igris] y el [salón de Igris de Jp André][sk-igrishall] (§11).

### Beru
1. **ep. 24 · 07:18-07:59** el Rey Hormiga busca «al rey de los humanos» ([subs VI][vi24] ✅). En el clip oficial: **cuerpo de insecto negro de ojos rojos, alas plegadas, en una cueva oscura** ([clip · 2:37][yt-ant-157]). → **amenazar**.
2. **ep. 24, la pelea** ([clip de 9:41, «Sung Jinwoo vs El rey hormiga»][yt-ant]; [noticia de IMDb][imdb-ep12]): el puño de Jinwoo contra el caparazón ([clip · 1:38][yt-ant-98]), Jinwoo con los ojos encendidos entre llamas ([clip · 8:12-8:32][yt-ant-492]). → acción.
3. **ep. 25 · 09:04-09:50** **arrodillado**, pide un nombre ([subs VI][vi25] ✅ + [doblaje][dw-beru-sombra]). → **presentar** / **servir**.
4. **ep. 25 · 09:56** recibe su nombre; cartel «General · Nv. 1» ([subs VI][vi25] ✅). → **celebrar**.
5. **ep. 25 · 10:42** «Si es la voluntad de mi rey. Dé la orden.» ([subs VI][vi25] ✅). → **esperar órdenes** («Cómo pedir algo», lámina 2).
6. **Captura de la wiki (P·16):** Beru de sombra con **alas de luz azul abiertas**, de frente. → **presentar** en «Los talentos».

### Cha Hae-In
1. **ep. 1 · 15:00** primera aparición como rango S, entre gritos de fans ([subs][nf01] ✅). → **presentar**.
2. **ep. 16 · 18:42-18:59** sale de la mazmorra: «la segunda al mando… Cha Hae-in, la Bailarina» ([subs][es16] ✅). Captura oficial: **perfil a contraluz azul, pelo al viento** (P·19). → **presentar**.
3. **ep. 17 · 02:01-02:24** avisa a Jinwoo: «Aléjate» ([subs][es17] ✅). → **regañar** o **advertir**.
4. **ep. 17 · 21:11-21:26** pregunta por Jinwoo en su día libre ([subs][es17] ✅). → **pensar** o preocuparse.
5. **ep. 18 · 00:58** «¿De verdad entrará desarmada?» ([subs][es18] ✅). → **animar** o **actuar**.
6. **ep. 22 · 05:44** combate amistoso entre rangos S ([subs][es22] ✅). → acción.
7. **CV de la T2 (P·17):** **desenvainando por encima del hombro**, mirada de lado, labios apretados. → **advertir** / **actuar**.
8. **Render de cazadora (P·18):** de pie, piernas en paso, espada baja en la derecha. → **presentar** (recorte limpio sobre verde).

### Resumen: qué pose para qué
| Uso | La mejor | Dónde |
|---|---|---|
| Presentar | Jinwoo con la mano abierta hacia cámara | P·3 |
| Explicar | Jinwoo con la ventana como tableta | S·7 |
| Pensar | Jinwoo con dos dedos en la barbilla junto a su ventana | S·2 |
| Advertir / regañar | Cha Hae-In desenvainando | P·17 |
| Celebrar | Beru arrodillado recibiendo su nombre | ep. 25 · 09:56 |
| Guardar / staff | Igris de pie detrás de Jinwoo | P·20 |
| Animar | Jinwoo novato con la daga cruzada | P·1 |

## 8 · Vestuario y paleta (hex medidos en arte oficial y capturas, ±5 por canal)

| Qué | Colores | Fuente |
|---|---|---|
| Jinwoo novato: sudadera | azul gris `#4C7288`, sombra `#172631`, cuello naranja por dentro | [KV T1][kv1] ✅ |
| Jinwoo novato: piel y pelo | piel `#D7CAAF` · pelo `#434649` | [KV T1][kv1] ✅ |
| Jinwoo fuerte (T1): abrigo | abierto, azul claro `#63ADD9` / `#3E6D98`, camiseta `#182435` | [KV T1][kv1] ✅ |
| Jinwoo Monarca (T2): abrigo | negro azulado `#1C254E`, borde de luz roja `#CF5678` | [KV T2][kv2] ✅ |
| Jinwoo T2: ojos y sombras | iris `#D3A5D3` · sombra de piel violeta `#3640A7` | [KV T2][kv2] ✅ |
| Sombras (T2) | negro `#151F31` / `#0D1629`, contorno cian `#C5E8EE` → `#89BAD3` | [KV T2][kv2] ✅ |
| Fondo KV T2 | blanco lavanda `#F2EEEB`, violeta `#6A5B8F` | [KV T2][kv2] ✅ |
| Ruinas y cielo T1 | piedra `#626B72` / `#343C48`, noche `#0C1721`, cielo `#68A8C5` / `#295171` | [KV T1][kv1] ✅ |
| Ventana del Sistema | `#211B32` · marco Monarca `#9229F9` / `#ED77F3` | guía del repo ✅ |
| Ventana del Sistema T1 (2.ª pasada) | fondo `#112A39`, esquinas `#82F3FA`, barra de luz `#D4EDFF`, texto `#E7F5FA`, amenaza `#9F205C` | capturas S·3, S·10 y [clip ep. 6][yt-clip6-7] ✅ |
| Jinwoo T2 (render y CV) | abrigo con capucha azul noche `#2C2F4F` / `#303354`, sombra `#1D1E33`, camiseta blanca `#F5F2EA`, pantalón negro azulado | P·2, P·3 ✅ |
| Cha Hae-In | uniforme rojo `#BC2B47` (CV `#CC2D4B`), sombra `#6D273B`, blanco `#F4EFE7`, pelo rubio `#E2D2B4`, dorados en hombros | P·17, P·18 ✅ |
| Igris sombra (CV) | negro `#010004`, líneas cian `#5DE3EC` → brillo `#AEFDFF`, fondo rojo `#620001` | P·11 ✅ |
| Igris jefe (ep. 11) | armadura roja sangre, salón `#242234` con alfombra `#6A232B` | [clip · 0:11][yt-papu-11] ✅ |

**Ropa icónica (vista en la 2.ª pasada):**
- Jinwoo novato (T1): **sudadera con capucha** (gris en el cartel semanal P·1; azul con cuello naranja en la KV; cian en la cueva del ep. 6), **pantalón negro, zapatillas** y **tiritas en la cara** ([tráiler · 0:39][yt-trailer-39]). A veces **mochila verde** (ep. 1).
- Jinwoo fuerte (T1, ep. 7-12): **chaqueta abierta, camiseta** y la **daga de Kasaka**, la del veneno.
- Jinwoo T2: **abrigo largo azul noche con capucha**, camiseta blanca, pantalón negro (P·2, P·3). En la nieve, **chaqueta marrón con cuello de borrego** (P·20).
- Jinwoo en el ending de la T2: **túnica blanca** en un palacio de mármol ([ED · 0:05-0:58][yt-ed2-5]). Sólo para ambientes, no es su ropa de diario.
- Igris: armadura con **penacho rojo**. **Roja sangre como jefe** ✅ (visto en el [clip del ep. 11][yt-papu-3]). **Negra con líneas cian** como sombra ✅ (KV T2, P·11).
- Cha Hae-In: **uniforme rojo y blanco con hombreras doradas** y espada ✅ (wiki, P·17-18).
- Go Gunhee y Woo Jinchul: **traje negro, camisa blanca, corbata negra** (P·22-23). Es el «uniforme» de la Asociación.
- Jinah: uniforme escolar **azul con lazo rojo** (P·24).

---

## 9 · Sitios, luz y fondos

| Sitio | Luz y hora | Paleta | Hilo que le va |
|---|---|---|---|
| **Portal en la calle** (Seúl) | noche; el vórtice azul blanco ilumina a contraluz a los cazadores, que se ven como siluetas ✅ (F·5, F·6). Delante, **cinta amarilla y vallas metálicas de la Asociación** (F·5, F·7). En el ep. 1, **el portal va dentro de una valla de obra roja** con cazadores esperando (F·20) | `#0C1721` · `#56A3D2` · centro `#EFF5FB` (medido en F·6) | Cómo se entra |
| **Portal rojo** (ep. 13) | vórtice rojo con rayos magenta; siluetas negras delante de una barandilla (F·9) | rojo `#CF5678`, magenta | Normas (lámina 2) · lo prohibido |
| **Asociación de Cazadores** (sede en Guro, Seúl, [wiki][wiki-kha] ✅) | oficina con fluorescentes, madera y moqueta; funcionarios de traje con papeles (S·15-16). Cristal negro medidor (ep. 16 · 03:47 ✅). Un despacho con sofás de cuero al atardecer (F·12; es el del Gremio de Cazadores, ep. 8) | `#E1D1C4` (pared) · `#452718` (madera) · `#191517` (traje) | De qué va esto · De dónde sale un rol · El staff |
| **Rascacielos al atardecer** (ep. 8, F·13) | edificio de oficinas, luz rosa y crema | `#EDD8B8` · `#9F7674` · sombra `#4B3435` | La guía, de un vistazo |
| **Hospital** (ep. 3, F·14) | **habitación de día, blanca y luminosa**, cama con barandilla, luz de ventana. La ventana del Sistema se ve casi transparente (S·1) ✅ | `#E6E6E1` · `#D3CFC3` · pelo y sombras `#464555` | Lo que hay que leer |
| **Mazmorra doble / templo de Cartenon** (ep. 1-2) | **sala circular azul con un anillo de luces**, niebla a ras del suelo y la **estatua del Dios sonriendo** (F·1, F·2; [clip · 0:03-0:07][yt-templo-3]). Mandamientos grabados («First, worship the God», ep. 2 · 01:13 ✅) | azul `#3F5484` / `#1A2B57`, estatua `#375AAB`, negro `#05101E` | Normas (lámina 2) |
| **Salón del trono vacío** (ep. 11-12) | **columnas violeta oscuro, arcos góticos, lámparas doradas, alfombra roja**, trono con adorno dorado al fondo ✅ ([clip · 0:01-0:21][yt-papu-1]) | `#1E121B` · `#2C151D` · alfombra `#6A232B` · velas doradas | Los roles que se ganan · El staff |
| **Mazmorra del cambio de clase** (ep. 11, F·3) | **pasillo infinito de columnas con antorchas**, bóveda de arcos | `#212134` · `#0E121E` y fuego naranja | Lo que hay que leer · Dónde se trabaja |
| **Cueva de cristales azules** (ep. 6) | cristales cian que brillan solos; es la luz del Sistema hecha sitio ([clip · 0:25-1:10][yt-clip6-25]) | `#2B9DD9` · `#57D9F3` · `#112D50` | Si te atascas |
| **Zona de Penalización** (ep. 3, F·4) | desierto rojo y naranja bajo un cielo de fuego | rojos y ocres | Normas (lo que pasa si no cumples) |
| **Castillo del Demonio** (ep. 7, F·15) | fuego y cadenas | naranja, negro | — |
| **Tienda e inventario del Sistema** (ep. 12 · 06:18 «Store.» ✅) | sin sitio físico: Jinwoo la sujeta al atardecer (S·7) | violeta / naranja | Los roles que te pones tú |
| **Vestíbulo con cartel de reclutamiento** (ep. 16 · 15:46 ✅) | cartel oficial: «Buscamos mineros para entrar al portal de rango A de la Asociación de Cazadores» | azul institucional | Cómo pedir algo · Reuniones y eventos |
| **Isla de Jeju** (T2, cuarta incursión, ep. 22-25 ✅) | **isla verde vista desde el aire en un mar azul** («3 YEARS AGO», F·10); dentro, **cuevas oscuras de tierra** donde vive el Rey Hormiga ([clip · 0:19-2:57][yt-ant-19]) | mar `#226A9E` · `#3799C6` · profundo `#091E33`; cueva marrón negra | Reuniones y eventos · Lo que pasa en vivo |
| **Cámara de prensa de la incursión** (ep. 22 · 16:54 «Como cámara de prensa de los Cazadores» ✅) | transmisión en directo | pantallas | Lo que pasa en vivo |
| **Palacio blanco del ending T2** ([ED · 0:47-0:54][yt-ed2-47]) | mármol blanco, columnas clásicas, luz de ventanal; ejército de sombras en fila; trono vacío tras una reja | `#545E5F` · `#939891` · `#DDDED5` · rojo `#AA033D` | La guía, de un vistazo (alternativa elegante) |

**Un dato de oro:** en Seúl hay una **exposición oficial** montada como el **«Centro de Entrenamiento de la Asociación de Cazadores de Corea»**. El visitante entra como **cazador de rango E novato** y empieza en la **oficina de registro** ([Trip-cut][expo1], [Trip.com][expo2] ✅). Es justo la idea de #guia: el recién llegado se registra.

**Texturas reales equivalentes** (CC0, comprobadas en la 2.ª pasada con las API de [Poly Haven][ph-api] y [ambientCG][acg-api]):
- piedra tallada del templo: [Granite Wall](https://polyhaven.com/a/granite_wall), [Castle Wall Slates](https://polyhaven.com/a/castle_wall_slates), [Stone Tiles](https://polyhaven.com/a/stone_tiles);
- metal pavonado negro (armadura de sombra): [Metal 046 A](https://ambientcg.com/a/Metal046A), [Metal Plate](https://polyhaven.com/a/metal_plate);
- corcho del tablón: [Cork 004](https://ambientcg.com/a/Cork004), [Cork 002](https://ambientcg.com/a/Cork002);
- asfalto de la calle del portal: [Asphalt 025 C](https://ambientcg.com/a/Asphalt025C), [Asphalt 02](https://polyhaven.com/a/asphalt_02);
- suelo de mármol del palacio o la Asociación: [Tiles 074](https://ambientcg.com/a/Tiles074), [Marble 01](https://polyhaven.com/a/marble_01);
- Ojo, cristal ahumado: ambientCG no dio resultado para «Glass frosted»; se hace con el material de vidrio de Blender (rugosidad 0,3 y tinte gris).

---

## 10 · Arte oficial y fondos de pantalla

### 10.0 Las hojas de contacto (lo que vi en la wiki) ✅

Corrí `investigar_serie.py` tres veces sobre `solo-leveling.fandom.com`:
- `herramientas/referencias/solo-leveling/`: 14 páginas de personajes y sombras, **673 imágenes, 15 hojas**.
- `herramientas/referencias/solo-leveling-objetos/`: 19 páginas de sitios, objetos y temporadas, **305 imágenes, 7 hojas**.
- `herramientas/referencias/solo-leveling-episodios/`: los 25 episodios y sus galerías, **635 imágenes, 14 hojas**.

**Las miré.** Mucho no sirve: unas 150 son **storyboards y genga** del ep. 6, 7 y 11 (dibujo a lápiz, «©SLANM»), y unas 250 son **viñetas del webtoon** (otro estilo, no el del anime). Por eso monté **3 hojas propias** con Pillow, con lo mejor de las tres tandas. En cada celda va el tamaño real y el código del índice de origen (P = personajes, O = objetos, E = episodios).

**`hojas/personajes_01.jpg`** (P·): arte oficial y renders

| N.º | Qué es | Tamaño | Para qué | Original |
|---|---|---|---|---|
| 1 | Jinwoo T1 novato, daga (cartel semanal) | 1440×2460 | Jinwoo novato, **daga cruzada**: animar, «Cómo se entra» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/6/6a/Sung_Jinwoo_Anime_Season_1_Cour_1_Design.webp) |
| 2 | Jinwoo T2 render, abrigo y daga | 727×1179 | Jinwoo T2 de cuerpo entero, **mano en el bolsillo y daga**: recorte limpio | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/c/cc/Sung_Jinwoo_Anime.png) |
| 3 | Jinwoo T2 CV: mano abierta | 900×1200 | **Mano abierta hacia cámara**: presentar, invitar | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/b/ba/Sung_Jinwoo_Anime_S2_CV.jpeg) |
| 4 | Jinwoo T2 ilustración neón | 2304×4096 | Estilo neón de la T2 (sólo referencia) | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/2/23/Season_2_anime_Sung_Jinwoo_illustration.jpg) |
| 5 | ReAwakening KV 2 | 2434×3440 | Portada de la película: Jinwoo y sombras en diagonal | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/8/8d/Solo_Leveling_ReAwakening_Key_Visual_2.jpeg) |
| 6 | ReAwakening portada | 2000×3000 | Perfil mirando arriba con abrigo rojo: portada de la guía | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/7/70/Solo_Leveling_ReAwakening_Cover_Visual.jpeg) |
| 7 | Cuenta atrás 1 día: Jinwoo e Igris | 2000×2248 | **Jinwoo con Igris detrás**: «El staff» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/f/fa/Season_2_Countdown_1_Day.jpeg) |
| 8 | Cuenta atrás 2 días: abrigo de piel | 2000×2248 | Jinwoo con abrigo de piel e Igris gigante detrás | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/a/a5/Season_2_Countdown_2_Days.jpeg) |
| 9 | Cuenta atrás 3 días: Jinwoo y Tank | 2000×2246 | **Jinwoo sonriente con Tank**: «Los talentos» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/c/c4/Season_2_Countdown_3_Days.jpeg) |
| 10 | Cuenta atrás «hoy»: Jinwoo firma | 2000×2248 | Jinwoo firma el cartel: celebrar | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/5/54/Season_2_Countdown_Anime_Airs_Today.jpeg) |
| 11 | Igris CV («IGRIT») | 707×999 | Igris de frente, líneas cian: ficha del staff | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/7/73/Igris_CV.jpg) |
| 12 | Igris sombra, ojos (ep. 12) | 2415×1354 | Los ojos de Igris al despertar: detalle para un fondo | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/6/6d/Anime_Episode_12_Igris_shadow_soldier.jpg) |
| 13 | Kaisel CV | 1460×2064 | Kaisel: «Tus zonas» (volar de una a otra) | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/a/a5/Kaisel_CV.jpg) |
| 14 | Tank CV | 1460×2064 | Tank: «Los talentos» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/8/8f/Tank_CV.jpg) |
| 15 | Colmillo (Kiba) CV | 1076×1521 | Colmillo (Kiba): «Los talentos» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/5/55/Tusk_CV.jpg) |
| 16 | Beru (ep. 25) | 1920×1080 | Beru con alas de luz: «Los talentos», lámina 2 | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/f/fe/Beru_Anime1.png) |
| 17 | Cha Hae-In CV T2, desenvaina | 900×1200 | **Cha Hae-In desenvainando**: advertir, «Normas», «Reuniones y eventos» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/8/8b/Cha_Hae-in_Anime_S2_CV.jpeg) |
| 18 | Cha Hae-In render cazadora | 816×1073 | Cha Hae-In de cuerpo entero sobre verde: recorte | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/9/97/Cha_Hae-In_%28Hunter%29_Anime_Alt.png) |
| 19 | Cha Hae-In ep. 16 | 1200×675 | Cha Hae-In de perfil, luz azul: presentar | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/8/84/Solo_Leveling_Anime_Episode_16_Img_1.jpg) |
| 20 | Jinwoo e Igris en la nieve (ep. 14) | 1200×675 | **Igris como guardaespaldas** en la nieve: «El staff» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/c/c0/Solo_Leveling_Anime_Episode_14_Img_3.jpg) |
| 21 | Yoo Jinho (ep. 19) | 1200×675 | Jinho con su mochila, alegre: «Cómo pedir algo» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/6/62/Solo_Leveling_Anime_Episode_19_Img_5.jpg) |
| 22 | Go Gunhee render | 494×1526 | Go Gunhee de cuerpo entero: «De qué va esto» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/6/6f/Go_Gunhee_Anime.png) |
| 23 | Woo Jinchul render | 425×1510 | Woo Jinchul de cuerpo entero: «El staff», «Normas» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/c/ca/Woo_Jinchul_Anime.png) |
| 24 | Sung Jinah render | 470×1460 | Jinah saludando: la recién llegada | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/2/21/Sung_Jinah_Anime.png) |

**`hojas/sistema_01.jpg`** (S·): la ventana del Sistema y los objetos

| N.º | Qué es | Tamaño | Para qué | Original |
|---|---|---|---|---|
| 1 | NOTIFICATION en el hospital (ep. 3) | 1196×649 | **La primera ventana**: «Lo que hay que leer» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/b/b3/Anime_Episode_3_Jinwoo_receives_a_quest_from_the_System.png) |
| 2 | STATUS: mano en la barbilla (ep. 5) | 1366×768 | **Jinwoo pensando junto a su ventana**: explicar | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/6/6b/Anime_Episode_5_Jinwoo_increasing_his_stats.png) |
| 3 | QUEST INFO: WARNING en rojo (ep. 6) | 1366×768 | Ventana de misión con la palabra roja: «Normas» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/d/d3/SoloLeveling_Anime_Episode_6_Picture_22.png) |
| 4 | [Debuff] Parálisis (ep. 6) | 1366×768 | Barras de estado negativo: lámina 2 de normas | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/f/fa/SoloLeveling_Anime_Episode_6_Picture_38.png) |
| 5 | FORMULA: Elixir of Life (ep. 7) | 1366×768 | Ventana con icono en recuadro: plantilla | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/f/f3/Anime_Episode_7_Screenshot_70.png) |
| 6 | ¿Comprar? [Knight Killer] (ep. 12) | 1366×768 | **Botones CANCEL · BUY**: «Los roles que te pones tú» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/7/77/Anime_Episode_12_Jinwoo_buys_Knight_Killer.png) |
| 7 | Tienda como tableta (ep. 12) | 1366×768 | **La ventana sujeta como tableta**: el objeto real | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/b/bd/Anime_Episode_12_Jinwoo_uses_shop_in_system.png) |
| 8 | Temporizador sobre Jinwoo (ep. 12) | 1366×768 | Temporizador sobre la cabeza: «Reuniones y eventos» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/a/a5/Anime_Episode_12_Jinwoo_finished_job_change_quest.png) |
| 9 | Móvil: aviso de la Asociación (ep. 8) | 1920×1080 | **El móvil con el aviso de la Asociación**: «Cómo pedir algo» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/f/fa/Anime_Episode_8_picture_25.png) |
| 10 | Aviso misión de cambio de clase (ep. 10) | 1366×768 | **La mejor plantilla**: panel, cabecera, «!» y esquinas | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/b/b4/Anime_Episode_10_notification_for_job_change_quest.png) |
| 11 | Ventana en el parque (ep. 7) | 1366×768 | Ventana a pleno sol: cómo se ve de día | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/b/bd/Anime_Episode_7_Screenshot_35.png) |
| 12 | «Another key?» llave roja (ep. 7) | 1366×768 | Llave roja en la mano: objeto de recompensa | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/1/1f/Anime_Episode_7_Screenshot_38.png) |
| 13 | Barra del Sistema en la cueva (ep. 6) | 1366×768 | Barra del Sistema a la altura del pecho | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/f/f8/SoloLeveling_Anime_Episode_6_Picture_10.png) |
| 14 | El Sistema reflejado en el ojo (ep. 7) | 1366×768 | El Sistema en el ojo: detalle | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/5/55/Anime_Episode_7_Screenshot_43.png) |
| 15 | Oficina de la Asociación (ep. 16) | 1200×675 | **Funcionario de la Asociación con papeles**: «El staff» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/c/ce/Solo_Leveling_Anime_Episode_16_Img_5.jpg) |
| 16 | Asociación: reevaluación (ep. 16) | 1200×675 | Oficina de reevaluación: «De dónde sale un rol» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/9/98/Solo_Leveling_Anime_Episode_16_Img_4.jpg) |

**`hojas/fondos_01.jpg`** (F·): sitios y fondos

| N.º | Qué es | Tamaño | Para qué | Original |
|---|---|---|---|---|
| 1 | Estatua del Dios, templo (ep. 1) 4K | 3840×2160 | **Estatua del Dios**: lámina 2 de «Normas» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/c/cb/Statue_of_God_Smile_Anime_Episode_1.png) |
| 2 | Sala circular del templo (ep. 1) | 1366×768 | Sala circular del templo | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/1/1f/Anime_Episode_1_Screenshot_15.png) |
| 3 | Mazmorra del cambio de clase (ep. 11) | 1366×768 | Pasillo de antorchas: «Dónde se trabaja» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/0/08/Anime_Episode_11_Job_Change_Quest_Dungeon.png) |
| 4 | Zona de Penalización (ep. 3) | 1366×768 | Zona de Penalización | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/c/c8/Anime_Episode_3_Penalty_Zone.png) |
| 5 | Portal con cinta policial (ep. 8) | 1366×768 | **Portal con cinta y cazadores**: «Cómo se entra» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/b/be/Anime_Episode_8_picture_49.png) |
| 6 | Portal azul de noche (ep. 8) | 1366×768 | Portal azul de noche con siluetas | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/6/6d/Anime_Episode_8_picture_60.png) |
| 7 | Valla de la Asociación (ep. 8) | 1366×768 | **Vallas de la Asociación**: «Cómo se entra» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/d/d5/Anime_Episode_8_picture_41.png) |
| 8 | Portal en la cueva (ep. 5) | 1366×768 | Portal dentro de una cueva | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/b/b5/Anime_Episode_5_Hwangs_squad_at_the_dungeon_gate1.png) |
| 9 | Portal rojo (ep. 13) | 1920×1080 | Portal rojo: lo prohibido | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/d/d7/Red_Gate_-_S2_Episode_13.png) |
| 10 | Isla de Jeju desde el aire | 1920×1080 | Jeju desde el aire: «Reuniones y eventos» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/9/94/Jeju_Island_Anime_-_Episode_1.png) |
| 11 | Gremio de Cazadores (ep. 11) | 1920×1080 | Gremio de Cazadores: «Los roles que se ganan» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/b/b1/Anime_Episode_11_Hunters_Guild.png) |
| 12 | Despacho al atardecer (ep. 8) | 1920×1080 | Despacho con sofás: «De qué va esto» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/f/fb/Anime_Episode_8_Baek_and_Choi_meeting.png) |
| 13 | Rascacielos al atardecer (ep. 8) | 1920×1080 | Rascacielos: «La guía, de un vistazo» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/2/25/Anime_Episode_8_picture_34.png) |
| 14 | Hospital: Jinah y Jinwoo (ep. 3) | 1366×768 | Habitación del hospital: «Lo que hay que leer» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/5/5a/Anime_Episode_3_Jinha_visits_Jinwoo1.png) |
| 15 | Castillo del Demonio (ep. 7) | 1366×768 | Castillo en llamas | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/5/52/Anime_Episode_7_Demon_Castle.png) |
| 16 | Tanque, espada y mago en la cueva (ep. 1) | 1366×768 | **El equipo típico** a contraluz, espada en diagonal: «Dónde se trabaja» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/4/46/Anime_Episode_1_Hunters_Introduction.png) |
| 17 | El equipo entra a la mazmorra | 1315×738 | El equipo entra: «Dónde se trabaja» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/9/9a/Jinwoo_and_his_squad_enters_the_dungeon_%28Anime%29.png) |
| 18 | Visual grande T2 | 1920×1080 | Visual grande T2: portada | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/0/0e/Anime_Season_2_large_visual_1.png) |
| 19 | Visual grande T1 (2) | 1200×675 | Visual grande T1 | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/4/47/Anime_Season_1_Large_Visual_2.jpg) |
| 20 | Equipo de la mazmorra doble (ep. 1) | 1920×1080 | **Portal dentro de una valla de obra**: «Cómo se entra» | [enlace](https://static.wikia.nocookie.net/solo-leveling/images/1/1e/Anime_Episode_1_Double_Dungeon_Strike_Team.png) |

**Otras joyas de los índices** (no caben en las hojas):
- **Tarjetas de cuenta atrás de la T1** de Crunchyroll con firmas de los actores (Aleks Le, Michelle Rojas…): índice P 438-450. Llevan el logo «S O L O  L E V E L I N G» en serifa espaciada.
- **«Special art» de final de capítulo** (1080×1920, P 113-136): mini cómics en blanco y negro dentro de un **marco de circuitos cian**, como una ventana del Sistema. Referencia para el marco de la lámina.
- **Layouts de Yoshihiro Kanno** (director de acción) y fotogramas clave del ep. 11 (P 68-79, O 5-8, 4096×1156): la pelea con Igris, a lápiz.
- **La estatua del Dios** en 4K (O 3, 3840×2160; es F·1).
- **Dibujo de agradecimiento de Yoshihiro Kanno**, director de acción, al acabar la T2: Jinwoo de pie con las manos en los bolsillos y Kaisel detrás, a tinta gris, «ありがとうございました!! Thank you!!» ([imagen, 870×1222][rd-kanno], compartida en Reddit el 30-mar-2025 ✅ medida). Referencia de pose relajada.

### 10.1 Arte oficial fuera de las hojas

- **KV T1** (dos Jinwoo, ruinas): [archivo 948×1280][kv1] ✅. La presentaron [Natalie][natalie-kv1], [Animate Times][animate] y [Collabo Cafe][collabo].
- **KV T2** (Jinwoo y el ejército de sombras, lema 「覇者の目醒め」): [archivo 1308×1848][kv2] ✅, [Aniplex][aniplex-kv2], [X oficial][x-kv2], [ANN][ann-kv2].
- **Visuales de sombras T2:** [Kiba][kiba-vis] y [Kaisel][kaisel-vis] (anitrendz). Hay una por sombra y son las mejores para «Los talentos».
- **Otra KV de la T2** (enero 2025): [Fandom Post][fandompost].
- **Arte conceptual** (Aniplex Online Fest 2022): [Sportskeeda][concept22].
- **Capturas oficiales por capítulo:** la web oficial tiene una página de historia por capítulo, con unas 6 imágenes cada una ([ejemplo][ofi-story21], [scraper que lo documenta][scraper] ✅). Hay además páginas de los 4 tomos de Blu-ray y DVD.
- **Pósteres en ANN:** [T1 y T2, 550×780][ann-data1] ✅ (medidas según ANN).
- **Logo en SVG:** [Wikimedia Commons][logo-svg].
- **Visuales grandes en horizontal (sirven de fondo de pantalla, 1920×1080):** [Visual grande T2][w-o188] (F·18) y [Visual grande T1 (2)][w-o262] (1200×675, F·19) ✅.
- **Ilustraciones verticales enormes:** [Jinwoo T2 neón, 2304×4096][w-p003] (P·4), [Igris, 2880×5184][w-p001] y [Igris, 2880×5124][w-p002] (índice P 1-2; ⚠️ la wiki no dice el autor: parecen del webtoon o del juego, no del anime).
- **Fondos de pantalla de fans en alta (2.ª pasada, por Reddit):** [«The daily life of shadows»][rd-shadows] (2897×4096, cómic de las sombras como criados; autor sin identificar en el post) y el arte de [RichyukiYuki en X][x-richyuki] (1125×1042, Cha Hae-In y Jinwoo; [post de Reddit][rd-richyuki], 2257 votos). **Sólo referencia.**
- **Fondos de pantalla de fans en DeviantArt** (su RSS público responde; tamaño = el que declara la propia web):
  - [«Solo Leveling (Sung Jin-Woo) Animated Wallpaper», de Favorisxp][da-favorisxp]: **3840×2160**.
  - [«Wallpaper (Solo Leveling)», de Renacars][da-renacars]: original de hasta **3840×2160**.
  - [«Sung Jinwoo Cold Mask Wallpaper», de Antractos][da-antractos]: original muy grande (hasta 9216×6144).
  - [«Son Jin-Woo and Igris», de Wespion9][da-wespion]: Jinwoo e Igris juntos, 1196×668 de vista previa.
  - Pixiv y ArtStation: no los probé (Pixiv pide sesión).

---

## 11 · Modelos 3D y fan art (solo referencia)

**Segunda pasada:** cada licencia se comprobó en la **API de Sketchfab** (`/v3/models/<id>`, campo `license`) el 24-sep-2026 ✅. «CC Attribution» = CC BY 4.0: se puede usar citando al autor. Ojo: los modelos de **personajes** son fan art de una obra con copyright; la licencia CC es la del autor del modelo, no la de la serie. Para el servidor (uso no comercial) vale como apoyo, siempre con crédito.

| Modelo | Autor | Licencia (API) | Sirve para |
|---|---|---|---|
| [**Hall of Blood-Red Commander Igris**][sk-igrishall] (143 922 caras, 202 me gusta) | Jp André | CC BY ✅ | **El salón del trono de Igris, hecho por un fan de la serie.** Mejor que el genérico para el concepto C |
| [Igris Solo Leveling][sk-igris] (3944 caras) | missafe | CC BY ✅ | Igris arrodillado (ligero, fácil de posar) |
| [Igris - Solo Leveling][sk-igris2] (33 970 caras) | shrithik | CC BY ✅ | Igris con más detalle |
| [Igris broadsword][sk-igrissword] | afonichiev | CC BY ✅ | **La espada de Igris** en primer plano (dice basarse en el diseño del juego ARISE) |
| [Cha Hae-In - Solo Leveling][sk-cha] (118 me gusta) | Casttelan2 | CC BY ✅ | Volumen y pose de Cha Hae-In |
| [Epilogue Dagger][sk-dagger] | hudibaba | CC BY ✅ | Una daga de Jinwoo (la del epílogo del webtoon) |
| [Shadow Dagger Inspired by Solo Leveling][sk-shadowdagger] | sasahhrkv | CC BY ✅ | Daga de sombra |
| [Throne Room][sk-throne] | Uğur Yakışık | CC BY ✅ | Salón del trono genérico (alternativa) |
| [Stone Book Lectern][sk-lectern] | ambrosia04 | CC BY ✅ | Atril de normas |
| [Old Roman-style Treasure Chest][sk-chest] | Theo Kain | CC BY ✅ | Cofre = INVENTARIO |
| [Pile of Coins 3][sk-coins] | SebastianSosnowski | CC BY ✅ | Recompensas |
| [Sword of the Defeated][sk-sword] | Bunny-HungTD | CC BY ✅ | Espada en primer plano |
| [**Crystal Ball**][sk-crystal] (142 me gusta) | Randall_3D | CC BY ✅ | **El cristal medidor** de la Asociación (concepto A); quitar las ramas de la peana |
| [**Reception Desk**][sk-desk] (207 me gusta, 600 caras) | Yvonne DeBandi | CC BY ✅ | **El mostrador de registro** (concepto A) |
| [ID Card Model][sk-idcard] | Johana-PS | CC BY ✅ | La **licencia de cazador** (tarjeta) |
| [**Bulletin Boards + Geometry Node System**][sk-board] | Unreal Designer | CC BY ✅ | **El tablón** con papeles y chinchetas (concepto B) |
| [Magic Portal][sk-portal] (885 me gusta) | SGTorresJ | CC BY ✅ | Un **portal** en 3D para «Cómo se entra» |
| [sung S solo leveling][sk-sung] | bgang0892 | Free Standard (no es CC) | solo referencia de pose |
| [Igris-Boss (Solo Leveling Arise)][sk-igrisboss] | 20062020year | CC BY | ❌ **No usar**: el autor agradece a quien lo sacó, parece extraído del juego |

**Crédito exacto (formato CC BY):** «"Hall of Blood-Red Commander Igris" (https://sketchfab.com/3d-models/a3ac78d429f04340937af8e365f4de32) by Jp André, licensed under CC BY 4.0». Igual para los demás.

**Diseños de interfaz de fans** (referencia, no copiar): [Figma Community][figma], [Dribbble][dribbble], [Behance][behance], [tema de Firefox][ffx-theme], [sololevelingsystemui][gh-digi], [keanteng/solo-leveling][gh-kean]. En GitHub hay **unos 492 proyectos** para «solo leveling system» (búsqueda de repositorios de GitHub, 24-sep-2026). El fandom convierte el Sistema en aplicaciones de hábitos ([HabitForge][habitforge], [Notion][notion]).

**Fan art con autor (2.ª pasada, por Reddit con Arctic Shift):**
- [RichyukiYuki][x-richyuki] (X): Cha Hae-In al atardecer y Jinwoo con traje bajo la lluvia, con sus sombras detrás. Estilo muy cinematográfico, buen ejemplo de luz.
- [«The daily life of shadows»][rd-shadows]: las sombras (Igris con su penacho, Tank, Iron) en versión chibi, de criados de Jinwoo. Muestra cómo las quieren los fans.
- DeviantArt: ver los fondos de pantalla de §10.1 (Favorisxp, Renacars, Antractos, Wespion9).

---

## 12 · Doblaje latino

### 12.1 La producción ✅

| Dato | Temporada 1 (2024) | Temporada 2, «Surge desde las sombras» (2025) | Fuentes |
|---|---|---|---|
| Estudio | **VSI México** (VSI Mexico City) | VSI México; los diálogos de J Balvin, en **Crunchyroll Dallas** | [Doblaje Wiki][dw], [ANMTV][anmtv-24], [ANMTV T2][anmtv-t2], [TVLaint][tvlaint25] ✅ |
| Dirección | **Sofía Huerta** | Sofía Huerta | las mismas + [Crunchyroll][cr-elenco25] ✅ |
| Traducción y adaptación | **Ilse Santillán** | **Samuel Oseguera** | Doblaje Wiki + ANMTV (Santillán) ✅; Oseguera sólo Doblaje Wiki ⚠️ |
| Grabación | Raúl Martínez | Alejandro Espinosa; Manny Aragon en Dallas | [Doblaje Wiki][dw] ⚠️ (una fuente) |
| Mezcla | **Óscar Galván** | Mikel (Miguel) Andrade | Galván: Doblaje Wiki + ANMTV ✅; Andrade ⚠️ |
| Productor ejecutivo | **Carlos Villasana** | Carlos Villasana | Doblaje Wiki + ANMTV ✅ |
| Guiones base | los de Crunchyroll (inglés), con el audio japonés de referencia | igual | [Doblaje Wiki][dw] |
| Estreno en Crunchyroll | **20-ene a 20-abr-2024** | **25-ene a 15-feb-2025** (ep. 1-4) y **1-mar a 19-abr-2025** (ep. 5-13) | [Doblaje Wiki][dw], [ANMTV T2][anmtv-t2], [TVLaint][tvlaint25] ✅ |
| Película | «Solo Leveling: **Segundo despertar**», grabada de agosto a octubre de 2024; traducción de Samuel Oseguera | | [Doblaje Wiki][dw-film] ⚠️ |

**Datos de interés** ([Doblaje Wiki][dw]):
- VSI dobló también al alemán, italiano y castellano, cada uno en su sede.
- Es **el primer protagónico de anime de Fernando Moctezuma** ✅ (también [Infobae][infobae-fm]).
- J Balvin hizo de Kargalgan **en español latino y en inglés** ✅ ([ANMTV][anmtv-balvin]).
- **Un fallo de adaptación:** el gremio de Baek se llama «**Tigre Blanco**» hasta el ep. 6 y «**Baekho**» desde el ep. 8.
- **Un error:** ep. 16 · 07:22, Choi Jong-in dice que el gremio Baekho no está muy «lejos» cuando quería decir «cerca».

### 12.2 Las voces (cada nombre con dos fuentes)

| Personaje | Voz latina | Fuentes | Estado |
|---|---|---|---|
| Sung Jinwoo | **Fernando Moctezuma** (de niño: Karina Altamirano, ep. 21) | [Doblaje Wiki][dw], [ANN][ann-data1], [MAL][jkc1], [Infobae][infobae-fm], [ANMTV][anmtv-24] | ✅ |
| Cha Hae-In | **Sofía Huerta** | Doblaje Wiki, ANN, MAL, [Infobae][infobae-sh] | ✅ |
| Yoo Jinho | **Brandon Montor** | Doblaje Wiki, ANN, MAL, [TVLaint][tvlaint25] | ✅ |
| Woo Jinchul | **Armando Guerrero** | Doblaje Wiki, ANN, MAL, TVLaint | ✅ |
| Sung Jinah | **Ixchel León** | Doblaje Wiki, ANN, MAL, TVLaint | ✅ |
| Go Gunhee (y el **narrador**) | **Santos Alberto** | Doblaje Wiki, ANN, MAL, [WDN][wdnes] | ✅ |
| Lee Joohee | **Gabriela Ortiz** | Doblaje Wiki, ANN, MAL, ANMTV | ✅ |
| Song Chiyul | **Jorge Badillo** | Doblaje Wiki, ANN, [TVLaint][tvlaint24], ANMTV | ✅ |
| Kargalgan (luego Colmillo) | **J Balvin** (grabó en Dallas) | Doblaje Wiki, [ANMTV][anmtv-balvin], [SDP Noticias][sdp], [Excélsior][excelsior] | ✅ |
| **Beru** | **Daniel Lacy** | [Doblaje Wiki][dw], [MAL][jkc2] | ✅ (antes dudoso) |
| Choi Jong-in | **Erick Selim** ([ficha][dw-selim]) | Doblaje Wiki, [ANMTV][anmtv-24], [ANMTV T2][anmtv-t2], MAL | ✅ (antes dudoso) |
| Baek Yoonho | **Gamaliel Quintana** | Doblaje Wiki, ANMTV, TVLaint, MAL | ✅ (antes dudoso) |
| Han Song-Yi | **Vianney Monroy** | Doblaje Wiki, ANMTV T2, TVLaint, MAL | ✅ (antes dudoso) |
| Kim Chul | T1 (ep. 5): **Gamaliel Quintana**; T2: **Olín Garcés** | Doblaje Wiki; ANMTV T2 y TVLaint (Garcés) | ✅ T2 · ⚠️ T1 (sólo Doblaje Wiki) |
| Iron (Kim Chul como sombra) | **Olín Garcés** | [Doblaje Wiki][dw] | ⚠️ (una fuente) |
| Tank | sin identificar | [Doblaje Wiki][dw] | — |
| Baruka | **Óscar Rangel** | Doblaje Wiki, ANMTV T2, TVLaint | ✅ |
| Hwang Dongsoo | **Jerry Garza** | Doblaje Wiki, ANMTV T2 | ✅ |
| Park Heejin | T1: Juana Saucedo · T2: **Miriam Aceves** | Doblaje Wiki (y su ficha de la película); ANMTV T2 (Aceves) | ✅ T2 |
| Esil Radiru | Montserrat Aguilar | [Doblaje Wiki][dw] | ⚠️ (una fuente) |
| **Igris** | no habla | [MAL][jkc1] sin actor + [Wikipedia][wp-txt]; Doblaje Wiki no lo lista | ✅ |

- **Ojo con el castellano:** en España, Jinwoo lo dobla Masumi Mutsuda ([ANN][ann-data1], [MAL][jkc1]). No mezclar. Los clips de Crunchyroll en Español marcan cuál es cuál: «(Doblaje **en español**)» = latino; «(Doblaje **castellano**)» = España.

### 12.3 Frases propias del doblaje latino (textuales)

**De dónde salen.** YouTube no deja bajar audio ni subtítulos de los clips oficiales (no tienen subtítulos, lo comprobé con `yt-dlp --list-subs`). Pero **Doblaje Wiki guarda 60 muestras de audio del doblaje**, de 20-40 segundos. Bajé 15 y las pasé por **Whisper** (modelo *small*, en español). Corregí a mano sólo las palabras rotas obvias («masmorra» → «mazmorra»). Cada frase lleva su muestra; el capítulo y minuto sale de cruzarla con los subtítulos ingleses de Netflix o vietnamitas de Crunchyroll. ✅ = el sentido coincide con esos subtítulos.

| Personaje | Frase del doblaje latino | Dónde | Estado |
|---|---|---|---|
| **Beru** | «**Mi rey**… necesito que usted me dé un nombre. Se equivoca, yo no morí, mi rey. Es gracias a su mano que yo he podido renacer. Todo mi ser se encuentra lleno de júbilo. Juro que voy a servirle por la eternidad. Ahora, por favor, **concédame un nombre**.» | ep. 25 · 09:04-09:50 ([muestra][dw-beru-sombra], [subs VI][vi25]) | ✅ |
| Beru (Rey Hormiga) | «¡Debo vivir! ¡Debo sobrevivir!» | ep. 24 · 19:38 ([muestra][dw-beru-trans], [subs VI][vi24]: «Để sống sót…») | ✅ |
| **Sung Jinah** | «Oye, necesitas tener más cuidado. ¿Tienes idea de lo preocupada que estaba?» · «Estuviste fuera tres días. ¿Por qué estás sonriendo?» · «Sí, es cierto. **Lo normal sería abrir la caja de mensajes.**» | ep. 3 · 06:55-07:12 ([muestra][dw-jinah], [subs][nf03]) | ✅ |
| **Sung Jinwoo** (rango E) | «Ya he estado al borde de la muerte en repetidas ocasiones.» · «Pero este cuchillo barato es lo único que pude comprar.» · «**Así es como suelo vivir, un día tras otro.**» | ep. 1, monólogo inicial ([muestra][dw-jinwoo-e]) | ✅ sentido |
| **Sung Jinwoo** (rango B) | «Tal vez podría ser reevaluado.» · «**Siempre golpean al clavo que sobresale.** Mejor lo olvido.» | ep. 5 · 06:29 ([muestra][dw-jinwoo-b], [subs][nf05]: «Should I go for a re-evaluation?») | ✅ |
| **Song Chiyul** | «Hola a todos, soy el líder de la incursión del día de hoy. Para los que no me conocen, me llamo Song Chiyul. **Un gusto conocerlos.**» · «¿Ya están todos listos? **¡Entremos!**» · «Hagamos una votación.» | ep. 1 · 07:20, 07:37 y 12:42 ([muestra][dw-chiyul], [subs][nf01]) | ✅ |
| **Yoo Jinho** | «**Soy Yoo Jinho, 21 años y rango D.**» · «¿Tu primera vez en una mazmorra C? No te preocupes, yo voy a mantenerte a salvo.» · «Disculpa, es que nunca he sido muy bueno en las cuestiones sociales.» | ep. 5 · 09:02 ([muestra][dw-jinho], [subs][nf05]) | ✅ |
| **Cha Hae-In** | «Entonces, ¿cómo puedo ayudarle?» · «Con permiso.» · «Pensé que debería saberlo.» · «**Le dije que no estaba interesada.**» | ep. 8 · 13:30-14:20, en el despacho de Choi ([muestra][dw-cha], [subs][nf08]) | ✅ |
| **Go Gunhee** | «Pues ya sabes, siempre dicen lo mismo. No puede haber brechas en la mazmorra.» · «Todos los cazadores vivimos de la venta de los recursos que hay dentro de las mazmorras.» | ep. 1 · 08:25-08:44 ([muestra][dw-gunhee], [subs][nf01]) | ✅ |
| **Baek Yoonho** | «Estoy seguro de que no me hiciste venir solamente para escuchar mis quejas, ¿verdad?» | ep. 8 · 11:26 ([muestra][dw-baek], [subs][nf08]) | ✅ |
| **Woo Jinchul** | «Sólo hubo seis sobrevivientes…» · «El trabajo de un cazador es un trabajo peligroso, pero es raro ver un resultado tan trágico.» | ep. 3, en el hospital ([muestra][dw-jinchul]) | ✅ sentido |
| **Choi Jong-in** | «Nunca puedo olvidarme de esa isla… Por eso tengo planeado despejar esa isla en un futuro no muy lejano.» | ep. 8 · 14:29-15:05, sobre Jeju ([muestra][dw-choi], [subs][nf08]) | ✅ |

**Carteles en latino** (vistos en el [clip oficial doblado del ep. 6][yt-clip6]):
- «**ADVERTENCIA: No cumplir la misión TE DETENDRÁ EL CORAZÓN.**» ([0:07-0:15][yt-clip6-7]) ✅.
- «**[Perjuicio] Parálisis**» y «[Perjuicio] Drenaje» ([0:46][yt-clip6-46]) ✅.

**De los subtítulos latinos** (no son el guion del doblaje, pero son la traducción oficial):
- «**Surge.**» (ep. 14 · 12:48; ep. 18 · 17:49; ep. 21 · 02:33) ✅.
- «Colmillo. Te llamarás Colmillo.» (ep. 18 · 18:10) ✅.
- «No eres de rango E, ¿verdad?» (ep. 13 · 12:16) ✅. Es el título del capítulo ([Crunchyroll][cr-e13]).
- «Ahora eres oficialmente un cazador de rango S.» (ep. 19 · 07:00) ✅.

**Títulos oficiales de los clips latinos** (canal Crunchyroll en Español, comprobados con yt-dlp): «[La presa se convierte en cazador][yt-clip6]», «[Aquí Sung Jinwoo demuestra quien es el más papu de los papus][yt-papu]» (usa jerga mexicana), «[Eres fuerte… pero no lo suficiente][yt-eresfuerte]», «[SIEMPRE sigue las reglas del templo…][yt-templo]», «[Sung Jinwoo vs El rey hormiga][yt-ant]».

### 12.4 Entrevistas en vídeo (comprobadas con yt-dlp)

| Vídeo | Qué es | Datos |
|---|---|---|
| [IGN Latinoamérica: «Conoce a los actores detrás del doblaje latino»][ign-latam] | Reparto | 8:30, 11-abr-2024 ✅ |
| [Crunchyroll en Español: «El poder oculto de Solo Leveling · Detrás de escenas»][yt-bts] | **El detrás del doblaje, oficial** («SURGE con los secretos detrás del doblaje») | 2:30, 6-abr-2024 ✅ |
| [Malditos Nerds (Infobae): entrevista a Fernando Moctezuma][yt-fm-infobae] | Doblar un anime de webtoon frente a uno de manga | 15:33, 12-dic-2024 ✅ |
| [Pratz: «Detrás de la voz de Sung Jinwoo», con Fernando Moctezuma][yt-fm-pratz] | Entrevista | 20:49, 25-may-2025 ✅ |
| [Antov: «Las voces de Solo Leveling»][voces] | Resumen del reparto | 3:27, 28-mar-2025 ✅ |
| Actores diciendo «¡Despierten!» ([TikTok][tt-despierten]) | Promo | ⚠️ sin comprobar (TikTok no lo abrí) |

Ninguno de estos vídeos tiene subtítulos ni capítulos (comprobado con yt-dlp): los minutos de lo que dicen quedan sin poner.

## 13 · Música

| Tema | Intérprete | Dónde | Fuente |
|---|---|---|---|
| OP T1 «**LEveL**» | SawanoHiroyuki[nZk]:TOMORROW X TOGETHER | cap. 2-12 (y ED del cap. 1) | [ANN][ann-data1], [MAL][jk1] ✅ |
| ED T1 «**request**» | krage | cap. 2-12 | [ANN][ann-data1], [MAL][jk1] ✅ |
| OP T2 «**ReawakeR**» | LiSA feat. Felix (Stray Kids) | T2 | [ANN][ann-data2], [MAL][jk2], [ANN noticia][ann-kv2] ✅ |
| ED T2 «**UN-APEX**» | TK from Ling tosite sigure | T2 | [ANN][ann-data2], [MAL][jk2] ✅ |
| Inserción «DARK ARIA» | SawanoHiroyuki[nZk]:XAI | ep. 6 (la caza en la cueva) y ep. 23 | [anisoncharts][anison], [wiki][wiki-darkaria] ✅ |
| Inserción «4eVR» | SawanoHiroyuki[nZk]: Laco, Benjamin & mpi | ep. 10 (Jinwoo limpia mazmorras C) | [anisoncharts][anison], [wiki][wiki-4evr] ✅ |
| Inserción «SHADOWBORN» | Hiroyuki SAWANO feat. Benjamin & mpi | ep. 13 (contra los osos de hielo), 18 (contra Kargalgan) y 25. Estribillo: «Be my Shadowborn» | [anisoncharts][anison], [wiki][wiki-shadowborn] ✅ |
| Inserción «REVIVƎЯ» | SAWANO feat. SennaRin | ep. 21 | [anisoncharts][anison], [wiki ep. 21][wiki-ep21] ✅ |
| Inserción «H∅WL» | SAWANO feat. Aimee Blackschleger | ep. 24 | [anisoncharts][anison] ⚠️ (la wiki no lo lista en el ep. 24) |

- La banda sonora salió el 27-mar-2024 (Aniplex; Milan Records en EE. UU.) y en vinilo el 4-oct-2024 ([Wikipedia][wp-txt] ✅).
- **Ambiente:** coros épicos, sintetizadores graves y percusión de tráiler, oscuro y en crescendo ⚠️ (de memoria: sin audio no pude oírlo). Lo que sí se ve: el **opening de la T1** va de azul circuito y noche de Seúl a rojo y violeta en la pelea con Igris ([OP · 0:01][yt-op1-1], [0:25][yt-op1-25], [1:06][yt-op1-66]); el **ending de la T2** es un palacio de mármol blanco con rojo ([ED · 0:37][yt-ed2-37]). La lámina debe «sonar» así: nada de pastel.
- **Otras piezas de la banda sonora** ([wiki][wiki-ost] ✅): «[Solo-Leveling]SymphonicSuite-Lv.1» a «Lv.10», «DunGeoN», «KSK→GATE», «Hunter→Monster», «everydayLV.0». Los títulos juegan con niveles y flechas, como el Sistema.
- «DARK ARIA» suena en el ep. 6 en la escena «Kill or Be Killed» (la caza en la cueva de cristal, [wiki][wiki-darkaria] ✅), la del «The real hunt begins now». ⚠️ El minuto exacto en que entra la canción no lo sé (no hay audio).

---

## 14 · Vídeos

**Cómo los miré (2.ª pasada).** `herramientas/fotogramas.py` no puede bajar de YouTube: pide «iniciar sesión para confirmar que no eres un robot». Con yt-dlp (cliente `mweb`) sí salen los datos y los ***storyboards***: las miniaturas oficiales de YouTube, **un fotograma cada segundo, a 320×180** (en los vídeos largos, uno cada ~5 s). Con Pillow los monté en hojas numeradas con su minuto y **las miré** (quedan en mi carpeta de trabajo, `vid/<nombre>/hoja_01.jpg`). Resolución baja: sirven para pose, encuadre, luz y color; para recortar, las capturas grandes de la wiki (§10.0).

### 14.1 Los que miré fotograma a fotograma

| Vídeo (canal, fecha, duración) | Lo que se ve, con su minuto |
|---|---|
| **Opening T1** «LEveL» ([Crunchyroll, 1:40][yt-op1]) | [0:01][yt-op1-1] suelo de **líneas de circuito azules** (el mismo dibujo del marco del Sistema; `#143572` · `#79BAEA`). [0:05-0:07][yt-op1-5] Seúl de noche, trenes. [0:09][yt-op1-9] Jinwoo de espaldas con abrigo en un parque de día. [0:11][yt-op1-11] **Jinah en un columpio**. [0:25][yt-op1-25] Jinwoo cae junto a un rascacielos rojo y rosa. [0:43][yt-op1-43] **coches de policía cortando una calle de noche** (un portal). [0:54][yt-op1-54] **Go Gunhee de brazos cruzados ante la ciudad en ruinas**. [1:06-1:12][yt-op1-66] pelea con Igris rojo. [1:22][yt-op1-82] Jinwoo con ojos violeta, mano en la cara. [1:24][yt-op1-84] **logo «S O L O  L E V E L I N G» en serifa espaciada**, blanco sobre negro violeta |
| **Ending T2** «UN-APEX» ([Crunchyroll, 1:41][yt-ed2]) | [0:05][yt-ed2-5] Jinwoo de espaldas **con túnica blanca** entre columnas de mármol. [0:11][yt-ed2-11] **trono vacío tras una reja**. [0:17-0:29][yt-ed2-17] mesa de banquete blanca, copa de vino tinto. [0:37][yt-ed2-37] **«SOLO LEVELING» en letras rojas gruesas** (`#AA033D`). [0:49-0:54][yt-ed2-47] **ejército de sombras en fila en el palacio blanco** (`#DDDED5` · `#545E5F`). [1:24][yt-ed2-84] **Jinwoo sentado en el trono**, manos en los brazos |
| **Tráiler latino** «Solo Leveling en ESPAÑOL» ([Crunchyroll en Español, 2:11, 16-ene-2024][yt-trailer]) | [0:03][yt-trailer-3] **créditos dentro de recuadros blancos** («CHUGONG», «DUBU», «H-GOON») sobre la ciudad. [0:31][yt-trailer-31] Jinwoo novato con la espada al hombro y cielo azul. [0:39][yt-trailer-39] cara con tiritas, apretando los dientes. [0:58][yt-trailer-58] **estatuas con líneas de luz azul** (el templo). [1:10][yt-trailer-70] **la ventana NOTIFICATION en el hospital**. [1:29][yt-trailer-89] **«ESTE INVIERNO»** en mayúsculas espaciadas sobre una **rejilla de interfaz azul** (`#08152E`). [2:09][yt-trailer-129] «ANIME PARA TELEVISIÓN · ESTRENO EN ENERO DE 2024» |
| **Clip ep. 6** «La presa se convierte en cazador» ([doblaje latino, 1:23, 14-mar-2024][yt-clip6]) | [0:07-0:15][yt-clip6-7] **ventana WARNING en rojo con su cartel latino**. [0:21-0:23][yt-clip6-21] **Jinwoo con la cara en sombra y los ojos azules encendidos**. [0:27][yt-clip6-27] de pie en la cueva de cristal, sudadera cian abierta. [0:46][yt-clip6-46] **[Perjuicio] Parálisis**. [1:06-1:10][yt-clip6-66] **de pie entre los caídos**, de espaldas |
| **Clip ep. 11** «Aquí Sung Jinwoo demuestra quien es el más papu…» ([doblaje latino, 1:44, 23-abr-2024][yt-papu]) | [0:01][yt-papu-1] **el salón del trono**: columnas violeta, alfombra roja, trono al fondo. [0:03-0:11][yt-papu-3] **Igris rojo con penacho**, espada en alto. [0:27][yt-papu-27] choque de espadas con chispas. [0:55][yt-papu-55] Jinwoo con fuego azul en la mano. [1:31][yt-papu-91] **Jinwoo de pie, sudadera gris, daga baja, Igris vencido detrás** |
| **Clip ep. 2** «SIEMPRE sigue las reglas del templo…» ([1:35, 4-sep-2025][yt-templo]) | [0:03][yt-templo-3] **la estatua del Dios sonriendo**, ojos blancos. [0:07][yt-templo-7] **la sala circular con anillo de luces azules** y los cazadores diminutos. [0:37][yt-templo-37] manos juntas rezando. [1:19][yt-templo-79] los supervivientes bajo las estatuas |
| **Clip ep. 24** «Sung Jinwoo vs El rey hormiga» ([9:41, 15-may-2025, 3 millones de visitas][yt-ant]) | [0:19][yt-ant-19] cueva de tierra. [2:37][yt-ant-157] **el Rey Hormiga** de frente, ojos rojos. [3:16][yt-ant-196] Jinwoo con **abrigo azul noche y camiseta blanca**, sereno. [8:12-8:32][yt-ant-492] **ojos azules encendidos entre llamas**. [9:11][yt-ant-551] los cazadores coreanos rango S juntos |
| **Clip ep. 6** «Eres fuerte… pero no lo suficiente» ([1:26, 26-mar-2024][yt-eresfuerte]) | [0:17-0:21][yt-eresfuerte-17] Jinwoo sangrando, **cara impasible**. [0:53-1:01][yt-eresfuerte-53] **ojos en blanco brillante en la sombra**: la cara de miedo que da |

### 14.2 Otros vídeos (existen: comprobados con yt-dlp el 24-sep-2026)

| Vídeo | Qué sirve | Datos |
|---|---|---|
| [PV 2 de Aniplex][yt-tr1] (el que enlaza MAL) | Ficha del staff en la descripción | 2:00, 10-dic-2023, 654 139 visitas ✅ |
| [PV 2 de la T2, Jeju][yt-tr2] ([noticia de ANN][ann-jeju]) | Beru y la incursión | 1:59, 4-mar-2025 ✅ |
| [Opening T1 sin créditos, Aniplex][yt-op1-aniplex] | El opening limpio | 1:31, 4 millones de visitas ✅ |
| [Opening T2 «ReawakeR», Aniplex][yt-op2-aniplex] | El opening de la T2 | 1:31, 14 millones ✅ |
| [Tráiler oficial de Crunchyroll en Español (2023)][yt-tr-es-2023] | Primer tráiler | 1:36, 906 677 visitas ✅ |
| [«Solo Leveling: Beyond the System», vídeo conceptual][yt-beyond] | La película nueva | 1:28, 3-jul-2026 ✅ |
| [«De cazador más débil a ser una leyenda»][yt-leyenda] | Resumen oficial de la T1 | 8:59, 333 333 visitas ✅ |
| [Reacción al ep. 3][yt-react] | La primera ventana, con capítulos: «Awakening as a player» en [1:20][yt-react-80], «Penalty zone» en [7:24][yt-react-444] | 19:01 ✅ |
| [Entrevista a los desarrolladores de OVERDRIVE][yt-od] (canal oficial) | Interfaz del juego | 8:11, 15-oct-2025 ✅ |
| Reto «Daily Quest» en TikTok ([vídeo][tt-daily]) · «Who's my king» ([búsqueda][tt-king]) | Tendencias | ⚠️ TikTok no lo abrí |

**Minutos exactos dentro de los capítulos** (los más útiles, de los subtítulos ✅):
- ep. 1 · 07:20, Song Chiyul se presenta; 07:37, «¡Entremos!».
- ep. 3 · 07:10, «Lo normal sería abrir la caja de mensajes»; 07:34, el Sistema aparece.
- ep. 11 · 10:18, Igris.
- ep. 12 · 17:39 / 19:08 / 19:32 / 20:25, los cuatro «Arise».
- ep. 25 · 09:04-10:07, Beru pide un nombre, lo recibe y «Surge».

## 15 · Videojuegos

- **Solo Leveling: ARISE** (Netmarble; móvil y PC). Juegas como Jinwoo, extraes sombras y formas escuadrones ([Netmarble][nm-site], [Google Play][gplay] ✅).
  - Fecha: **8 de mayo de 2024** en todo el mundo ✅ ([wiki][wiki-arise] + las entrevistas coreanas que hablan del lanzamiento «el 8», [The Value News][valuenews], [Nate][nate]). El 18-mar-2024 que da Wikipedia no lo pude confirmar ⚠️ (quizá una prueba previa).
  - La historia se cuenta con **viñetas del webtoon animadas** ([Siliconera][silic], [CBR][cbr-review] ✅). En el foro oficial hay un hilo sobre la nueva interfaz ([hilo][nm-ui]).
- **ARISE OVERDRIVE** (Netmarble Neo): salió en Steam y Xbox PC el 24-nov-2025. PS5 y Xbox Series en 2026 ([PC Gamer][pcgamer], [Steam][steam-news] ✅). Es un juego aparte de ARISE ✅: tiene su propia ficha de Steam (app 2373990) y su propio canal oficial, con una [entrevista a los desarrolladores][yt-od] sobre combate, narración y sonido ([GameMeca][gamemeca]).
- **Solo Leveling: Unlimited:** coleccionables Web3, sin interés para la lámina ([Wikipedia][wp-txt]).
- **Lo que la lámina puede tomar del juego:** las viñetas de webtoon como marco cuando Jinwoo recuerda algo. La ventana del Sistema vale igual que en el anime.
- ⚠️ No pude medir menús ni cajas del juego: Game UI Database y The Cutting Room Floor siguen en 403 (Cloudflare) con la red abierta. La portada del juego sí está en la wiki (índice P 428, «Solo Leveling Arise Visual Cover 1», 849×1200).

---

## 16 · Lo que ama el fandom

- **«Arise» / «Surge»:** la orden de extracción. Es el momento más citado del anime (ep. 12). La pelea con Igris se considera de lo mejor de la serie y dura más que en el original ([namu.wiki][namu-eval] ✅, [Sportskeeda][spk-igris]).
- **El reto de la misión diaria:** 100 flexiones, 100 abdominales, 100 sentadillas y 10 km. Es tendencia de gimnasio ([TikTok][tt-daily], [ComicBook][comicbook], [Kovo][kovo] ✅). Es la rutina de *One-Punch Man*, y los fans lo saben ([Epicstream][epic]).
- **«El Cazador más débil de la humanidad»:** el apodo que todos repiten ([subs][nf01] ✅).
- **De rango E a rango S:** la reevaluación en la que el medidor no puede con él (ep. 16 y 19 ✅).
- **Igris arrodillado** e **Iron trayendo cabezas** ([Wikipedia][wp-txt] ✅).
- **Beru y su «mi rey»** ([TikTok][tt-king]).
- **Las armaduras carísimas de Jinho** ([Wikipedia][wp-txt] ✅).
- **El Sistema en la vida real:** apps y plantillas que te dan «misiones» ([HabitForge][habitforge], [Notion][notion], cientos de repos en GitHub).
- **J Balvin como Kargalgan:** noticia muy comentada en Latinoamérica ([ANMTV][anmtv-balvin], [Sopitas][sopitas]).
- **Latinoamérica cuenta:** los productores de Aniplex y Crunchyroll llevaron la serie a **La Mole 2024 (México)** y a la **CCXP24 (Brasil)**, y dicen que el anime crece mucho en Latinoamérica ([entrevista de Cocotame, en japonés][cocotame] ✅).
- **«Mi rey»:** Beru arrodillado pidiendo un nombre (ep. 25 · 09:04) es la escena que más se cita de él; en latino dice «mi rey» y habla de usted ([§12.3](#123-frases-propias-del-doblaje-latino-textuales)).
- **Las sombras como criados:** los fans dibujan a Igris, Tank e Iron en versión chibi, como mayordomos de Jinwoo ([«The daily life of shadows»][rd-shadows], 345 votos en Reddit tras el final de la T2 ✅ Arctic Shift).
- **La pregunta eterna: ¿quién es más fuerte?** El post más votado tras el final de la T2 (6021 votos, 1043 comentarios) es «¿este tipo es más fuerte que Jinwoo?» ([Arctic Shift][as-sl] ✅). Los rangos son tema de charla: sirve para «Los roles que se ganan».

---

## 17 · Qué NO hacer

- ❌ **Globo blanco con cola.** El Sistema no sale de la boca de nadie.
- ❌ **Verde de terminal tipo Matrix** o esquinas redondas y monas. Es una ventana de juego, fría.
- ❌ **Colores alegres o pastel.** El mundo es noche, piedra y neón azul o violeta.
- ❌ **Igris hablando.** No habla: gesto y espada. (Beru sí habla: es de grado General.)
- ❌ **Igris dorado o plateado.** Como sombra es **negro con líneas cian**; como jefe, **rojo**. Nada más.
- ❌ **Cha Hae-In morena o con armadura plateada.** Es **rubia y va de rojo y blanco** (P·17-18).
- ❌ **Ventana del Sistema con esquinas redondas o letra de cómic.** Esquinas rectas con piezas de circuito, palo seco en mayúsculas espaciadas (S·10).
- ❌ **«Shun Mizushino»** u otros nombres japoneses. En latino son coreanos.
- ❌ **Jinwoo sonriente o haciendo el payaso.** Es contenido y serio. Beru es el exagerado.
- ❌ **Mezclar la ventana azul del novato con el violeta del Monarca sin lógica.** Azul para quien empieza, violeta para el poder.
- ❌ **«Monarca de las Sombras»** si se copia el latino de Crunchyroll: ahí es «**Rey de las Sombras**».
- ❌ **Black Han Sans** para textos en español: no tiene tildes.
- ❌ **Spoilers del final** (la boda con Cha Hae-In, Suho, Ashborn).

---

## 18 · Guía para generar con IA (Firefly, Canva)

**Rasgos que nunca cambian**
- **Jinwoo:** pelo negro corto y despeinado, flequillo sobre los ojos, cara fina, gesto serio. De novato, sudadera con capucha (gris o azul), pantalón negro, zapatillas y tiritas en la cara. De fuerte (T2), **abrigo largo azul noche con capucha** (`#2C2F4F`), camiseta blanca y ojos que brillan (azul en la T1, violeta en la T2).
- **Igris:** armadura completa con casco cerrado y **penacho rojo largo**. Sin cara visible. Sombra: negro con **líneas cian** `#5DE3EC`.
- **Cha Hae-In:** **rubia, melena corta**, uniforme **rojo `#BC2B47` y blanco** con hombreras doradas, espada negra.
- **Sombras:** siluetas negras con contorno cian y humo azul.
- **La ventana del Sistema:** panel azul noche translúcido `#112A39`, esquinas de circuito cian `#82F3FA`, barra de luz arriba, cabecera en recuadro con icono «!».

**Paleta**
- Noche `#0C1721`, azul `#1C254E`, cian `#89BAD3` y `#C5E8EE`.
- Violeta `#6A5B8F` / `#9229F9`, acento rojo `#CF5678`.

**Línea y sombreado:** anime de A-1. **Casi sin contorno negro**: la poca línea es fina y de color (`#693D56` en el fotograma de Igris del ep. 11). Sombras duras de dos tonos y **luz de borde de color** (rim light roja, rosa o cian). Mucho contraste. La línea negra continua es del webtoon, no del anime (punto 18).

**Luz:** fuente fría desde abajo (la ventana del Sistema o el portal), contraluz y humo.

**Encuadre:** contrapicado, el personaje mirando arriba o a cámara, con profundidad (ruinas o columnas delante).

**Palabras que ayudan:**
- *anime key visual, A-1 Pictures style, dark fantasy Seoul, holographic game UI window, cyan rim light, shadow soldiers with glowing blue outlines, low angle, cinematic*.

**Palabras que lo estropean:**
- *cute, chibi, pastel, kawaii, speech bubble, comic balloon, green terminal, cartoon*.
- También *webtoon* a secas: saca color plano coreano, no el anime.

**Palabras para la ventana:** *translucent navy holographic panel, thin cyan border, circuit-line corners, glowing horizontal light bar, header in a boxed label, exclamation icon in a circle, wide-tracked uppercase sans-serif*.

**Palabras para los sitios:** *blue swirling portal at night behind yellow police tape*; *circular stone temple hall with a ring of blue lights and floor fog*; *gothic throne room, dark violet pillars, red carpet, golden candelabras*; *crystal cave glowing cyan*.

**Imágenes de referencia (de las hojas):**
- Estilo general: la [KV T2][kv2] y el visual grande de la T2 (F·18).
- Pose del novato: P·1 y la [KV T1][kv1]. Pose del fuerte: P·2 y P·3.
- Pose de pensar con la ventana: S·2. La ventana como objeto: S·7.
- Sombras: P·11 (Igris), P·13-15 (Kaisel, Tank, Colmillo).
- Luz y paleta de sitio: F·2 (templo azul), F·5-6 (portal), el salón del trono del [clip del ep. 11][yt-papu-1].
- **No uses** las viñetas del webtoon de la wiki (unas 250 del índice P): son otro estilo, más brillante y de color plano.

**Aviso:** el dueño no quiere que la lámina «parezca IA». La IA solo para bocetos. El personaje final, recortado de arte oficial por `v3/integrar.py`.

### Lo que añade el repaso (punto 18) a la IA de imagen
- **Regla del director:** nada de gestos de dibujo animado. Añade *cinematic depth of field, subtle film grain, colored rim light, minimal black outlines* para el anime.
- Añade a las que estropean: *super deformed, sweat drop, comedic expression, screentone*.
- **Si quieres el webtoon** (no el anime): *clean black lineart, flat cel shading, saturated digital gradients, speed lines*. La viñeta de referencia: [cap. 50](https://static.wikia.nocookie.net/solo-leveling/images/3/3c/Chapter_50.png). Para el anime, el [fotograma de Igris del ep. 11](https://static.wikia.nocookie.net/solo-leveling/images/c/c0/Anime_Episode_11_Picture_5.png).
- **Tristeza:** *extreme close-up, cold blue light, hand on cheek, tears on chin, not idealized* (ep. 21, punto 21).

### Para una IA de texto: sus diálogos, en su voz
**Reglas de la serie**
- **Frases cortas y secas.** Nadie explica de más. El tono es serio: sin chistes de Jinwoo (§17).
- **Puntos suspensivos** para la duda, el peso o la devoción: «Mi rey…», «Sólo hubo seis sobrevivientes…».
- **Exclamación sólo en el grito:** «¡Entremos!», «¡Debo vivir! ¡Debo sobrevivir!».
- **De usted** Cha Hae-In con quien no conoce, y Beru siempre con Jinwoo. De tú, la familia y los amigos (Jinah, Jinho).
- **Pensamientos de Jinwoo:** en cursiva, sin globo (§4).
- **El Sistema** no «habla»: rotula. Cabecera en mayúsculas («NOTIFICACIÓN», «ADVERTENCIA»), la amenaza en mayúsculas y rojo («TE DETENDRÁ EL CORAZÓN»), los nombres entre corchetes y en negrita cursiva: ***[Perjuicio] Parálisis***, ***[Rango E]***.
- **Beru exagera** (habla florido porque ve doramas de época, punto 20). **Igris no habla nunca.**
- **Onomatopeyas:** no las documenté ⚠️. Mejor no inventarlas: la serie usa líneas de velocidad y luz, no letras de sonido.

**Frases reales del doblaje latino, por emoción** (todas de §12.3, con su minuto allí)
| Emoción | Frase | Quién |
|---|---|---|
| Alegre, devoto | «Todo mi ser se encuentra lleno de júbilo. Juro que voy a servirle por la eternidad.» | Beru |
| Enfadado, cortante | «Le dije que no estaba interesada.» | Cha Hae-In |
| Enfadado, preocupado | «Oye, necesitas tener más cuidado. ¿Tienes idea de lo preocupada que estaba?» | Jinah |
| Explicando | «Todos los cazadores vivimos de la venta de los recursos que hay dentro de las mazmorras.» | Go Gunhee |
| Explicando, presentándose | «Hola a todos, soy el líder de la incursión del día de hoy. Un gusto conocerlos.» | Song Chiyul |
| Animando | «¿Ya están todos listos? ¡Entremos!» | Song Chiyul |
| Animando, protector | «¿Tu primera vez en una mazmorra C? No te preocupes, yo voy a mantenerte a salvo.» | Yoo Jinho |
| Triste, resignado | «Así es como suelo vivir, un día tras otro.» | Jinwoo (rango E) |
| Triste | «Sólo hubo seis sobrevivientes…» | Woo Jinchul |
| Orden, poder | «Surge.» | Jinwoo (subtítulos latinos) |

**Vocabulario de la serie:** el del punto 25 (portal, mazmorra, rango E… S, gremio, soldados sombríos, Perjuicio, «Surge», Rey de las Sombras).

**Para la IA de imagen, cada gesto** (de §7): poder = ojos violeta brillando, contrapicado, contraluz (KV T2); extraer una sombra = agachado, mano hacia el suelo (índice P 250; el gesto del ep. 12 no lo vi ⚠️); pensar = de perfil, dos dedos en la barbilla, la ventana al lado (S·2); invitar = brazo estirado y mano abierta (P·3); tristeza = primer plano con luz azul fría (ep. 21). Sin gotas de sudor, sin fondos de emoción de comedia y sin *chibi*.

---

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

> Repaso corto del 24-sep-2026 (parte de texto). Resumen: **el webtoon entinta en negro; el anime casi no usa línea negra y la cambia por luz de borde de color**. Nada de gestos de dibujo animado.

### Quién lo hizo
- **Anime:** A-1 Pictures. Dirección, **Shunsuke Nakashige**; diseño de personajes, **Tomoko Sudo** ([VFX Voice, entrevista al equipo](https://vfxvoice.com/maximizing-the-strength-of-anime-for-solo-leveling/) + [AniList, staff](https://anilist.co/anime/151807/staff)) ✅.
- Director de CG, **Toshitaka Morioka**; dirección de fotografía, **Daichi Iseki**; color, **Naomi Nakano**; logo, **Tsubasa Ōtaki** ([AniList, staff](https://anilist.co/anime/151807/staff)) ⚠️ (una fuente, la ficha de créditos).
- **Ventanas del Sistema:** gráficos en movimiento de Takemune Ōshiro, de Production I.G (§2) ✅.
- **Webtoon:** Jang Sung-rak, «**DUBU**», de Redice Studio (murió en julio de 2022). Estilo «afilado, limpio y empapado de color intenso» ([KoreaLore](https://www.korealore.com/2026/08/solo-leveling-webtoon-profile.html)) ⚠️.

### La regla del director ✅
- Nakashige: «Esta obra pedía el acabado de alta gama que se lleva ahora. Por eso **evité todo lo posible las expresiones de dibujo animado**. Usé composición, color y un **procesado de cámara parecido a la imagen real**». Dice que costó tiempo y que lo ajustaron con cada sección ([CBR](https://www.cbr.com/solo-leveling-director-original-cartoon-expressions-anime-why-cut/), [FandomWire](https://fandomwire.com/solo-leveling-director-reveals-reason-behind-change/)).
- **Para la lámina:** nada de caras deformadas de comedia, gotas de sudor gigantes ni *chibi*. Sí profundidad de campo, grano fino y contraste.

### Cómo se ve, medido (con `estilo.py`, en dos imágenes de la wiki) ✅
- **Anime** ([Igris, ep. 11](https://static.wikia.nocookie.net/solo-leveling/images/c/c0/Anime_Episode_11_Picture_5.png), 1366×768): **casi sin contorno negro**. El volumen lo da una **luz de borde rosa-violeta** (`#8B5469`, `#E790B7`) sobre negro casi puro (`#08080F`, `#0F121B`). La poca línea que hay es de color (`#693D56`). Saturación 55 %, brillo 16 %: oscuro y contrastado. **Fondo totalmente desenfocado.**
- **Webtoon** ([cap. 50, Jinwoo en la nieve](https://static.wikia.nocookie.net/solo-leveling/images/3/3c/Chapter_50.png), 574×778): **línea negra limpia y continua** (`#3F3F47`). Sombra plana en el pelo con un solo golpe de luz. Nieve con pincel suave por encima. Azules fríos (`#858EA5`, `#98BACD`) contra el marrón cálido del abrigo.
- **No hay tramas de punto.** El webtoon es a todo color, con **degradados digitales saturados**. Sus efectos son **aberración cromática** (poderes), **desenfoque de movimiento** y **líneas de velocidad radiales** con humo y escombros ([canmom.art, análisis del manhwa](https://canmom.art/crit/comics/solo-leveling)) ⚠️ (una fuente leída entera).

### 2D y 3D mezclados
- El productor **Atsushi Kaneko**: la base es 2D a mano, pero no escala para masas. **El ejército de sombras se probó en 2D y pasó a 3D** porque «no tenía impacto» ([VFX Voice](https://vfxvoice.com/maximizing-the-strength-of-anime-for-solo-leveling/)) ✅.
- Los Altos Orcos van en CG, tratados «para que parezcan más 2D». El estudio decide por escena: «**2D First**» o «**3D First**» ([Anime Corner, cómo se hizo](https://animecorner.me/how-the-solo-leveling-anime-was-made-behind-the-scenes-at-a-1-pictures-ahead-of-the-season-2-finale/)) ✅.
- Los personajes de fondo comparten modelo y cambian tatuajes o colores (Morioka, Anime Corner) ⚠️.
- **Captura de movimiento:** usaron **mocopi** de Sony (6 sensores de 8 g) para los caballeros y las multitudes de los **ep. 11-12**. Grabaron al aire libre: en el estudio no cabía el espadazo. Flujo: **3ds Max** (rig CAT) → **MotionBuilder** → BVH ([Sony XYN, caso de estudio](https://xyn.sony.net/en/case/sololeveling-anime)) ⚠️ (una fuente oficial).
- El storyboardista **Takayuki Kikuchi** unió los planos de Igris contra Iron en **un solo corte de 26 segundos** (Anime Corner) ⚠️.
- **Programa 2D del estudio: no lo encontré.** En la tele japonesa lo común es RETAS; Clip Studio lo usan otros estudios ([Clip Studio ASK](https://ask.clip-studio.com/en-us/detail?id=57247)) ⚠️. Es dato de la industria, no de esta serie.
- **Filtros por su nombre** (aberración, *bloom*, grano) en el anime: ninguna fuente técnica los nombra. Lo de abajo sale de la cita del director ⚠️ (traducción propia).

### Cómo replicarlo en Photoshop
- **Cuadro «anime»** (poder, Monarca, acción): casi sin línea negra. El contorno es una capa de **luz de borde** en modo Trama o Sobreexposición lineal (Añadir), del tono de la escena: cian del Sistema `#82F3FA`, violeta Monarca `#9229F9`/`#ED77F3` o rosa como Igris. Sombra en Multiplicar, oscura y con poco degradado (`#08080F`-`#15262D`). Encima, **grano fino** (Ruido 2-3 %) y un **viñeteado suave** ⚠️ (traducción propia de la cita).
- **Cuadro «webtoon»:** pincel redondo duro, **línea negra continua** (`#3F3F47`-`#1A222C`), sombra plana de un tono por zona, luces con pincel suave.
- **Líneas de velocidad** para acción e invocación: el pack libre del punto 19.

### Cómo replicarlo en Blender
- **Contorno:** para el anime, **sin Line Art visible**. En su lugar, un nodo *Fresnel* o *Layer Weight* que alimente un *Emission* del color de la escena: es la luz de borde medida. Para un cuadro tipo webtoon, **Line Art** (Grease Pencil) o **Freestyle** fino y constante; **Solidify** para objetos sueltos.
- **Sombreado (Eevee):** *Shader to RGB* → *Color Ramp* en **Constante**. Dos bandas para piel y objetos; tres para pelo o energía (con la banda media rosa clara del fotograma de Igris).
- **Luz y cámara:** luz fría desde abajo (la ventana o el portal) y luz de borde de color. **Profundidad de campo** en la cámara para desenfocar el fondo, y grano en el compositor ⚠️ (traducción propia de «como imagen real»).
- **Modelos para posar** (no para pegar): Igris ([shrithik][sk-igris2], CC BY, 33 970 caras), Cha Hae-In ([Casttelan2][sk-cha], CC BY, 35 694 caras) y la espada de Igris ([sk-igrissword]), todos en §11 y comprobados por la API de Sketchfab ✅.
- **Texturas encima:** el emblema de Ahjin (punto 19) como calcomanía en ropa, escudos o el mostrador; metal y madera, los de §9.

### Encuadres y cómo se enmarca cada emoción
- **Poder:** contrapicado y silueta a contraluz. Go Gunhee de brazos cruzados ante la ciudad en ruinas ([OP · 0:54][yt-op1-54]); Jinwoo con ojos violeta y la mano en la cara ([OP · 1:22][yt-op1-82]).
- **Diálogo tranquilo:** primer plano con el **fondo desenfocado**, como una cámara real (el fotograma de Igris de arriba).
- **Acción:** plano largo que sigue la pelea sin cortar (los 26 s de Igris contra Iron).
- **Tristeza:** primer plano sin embellecer, **luz azul fría** y una mano en la cara (Jinwoo llorando, ep. 21, punto 21).
- **Explicar:** Jinwoo pensando con la ventana al lado (S·2, §18).
- **Para la lámina:** si el personaje habla desde un fotograma, fondo desenfocado y luz de borde de color; nunca fondo nítido y plano.

---

## Punto 19 · Texturas 2D (tramas, pinceladas, patrones y emblemas)

> Parte de imagen, más una hoja de los emblemas que monté y miré yo (redactor) para comprobar sus colores.

### Qué textura tiene la serie
- **Ninguna trama de manga.** DUBU colorea con degradados digitales saturados, pensados para pantalla. La «textura» son **líneas de velocidad radiales**, humo, escombros, desenfoque y aberración ([canmom.art](https://canmom.art/crit/comics/solo-leveling)) ⚠️ (una fuente leída entera; otras reseñas dicen lo mismo, sin abrirlas).
- La línea: limpia, muy estudiada en los pliegues y la musculatura. En el anime, grano y brillo de posproducción (punto 18).
- **Patrón de tela** en la ropa de Jinwoo o Cha Hae-In: **no lo encontré**. La wiki describe colores y cortes, no tejidos ⚠️.

### Pinceles y texturas libres
| Capa | Recurso | Licencia | Para qué |
|---|---|---|---|
| **Líneas de velocidad** (la que sí usa la serie) | [«Manga Speedlines», 20 pinceles .ABR](https://myphotoshopbrushes.com/resources/3816/manga-speedlines) (valen en Procreate, Affinity, GIMP y Krita) | **Uso comercial libre, con atribución** ✅ (leída en la página) | acción, invocar sombras, «Surge» |
| **Grabado en metal** | [«Metal Armor Pattern 001»](https://3dtextures.me/2026/01/28/metal-armor-pattern-001/), 4096×4096 | **CC0** ✅ | armaduras de Igris y Beru, placas, empuñaduras |
| **Tramas de manga** | [«[FREE] Manga Screentone Pack 1»](https://assets.clip-studio.com/en-us/detail?id=2142037), Clip Studio 1.10.10 o más | gratis (0 $), dentro de Clip Studio ✅ | sólo para un cuadro «manga»: la serie no las usa |
| **Grano de papel** | [CC0 Textures, papel](https://cc0-textures.com/c/paper) | CC0, sin registro ⚠️ (no bajé un archivo concreto) | viñeta impresa, portada del manhwa |
| **Texturas reales** (corcho, madera, piedra, metal) | Poly Haven y ambientCG, ya en §9 | CC0 ✅ | los sitios |
| **Aberración y grano** | no es una textura: ajustes de capa en Photoshop (punto 18) | — | — |

### Emblemas y logos del mundo
Tamaños por la API de la wiki. **Los miré en una hoja propia** y medí el color con Pillow.

| Emblema | Cómo es | Tamaño | Enlace |
|---|---|---|---|
| **Ahjin** (el gremio de Jinwoo) | **llama o fénix violeta** en círculo, violeta oscuro `#402080`-`#5030A0` | 700×700 | [Ahjin.png](https://static.wikia.nocookie.net/solo-leveling/images/8/88/Ahjin.png/revision/latest?cb=20210529014242) ✅ |
| Ahjin, como sale en el cap. 141 del webtoon | variante del mismo | 725×803 | [Ah-Jin Logo Ch.141](https://static.wikia.nocookie.net/solo-leveling/images/c/ca/Ah-Jin_Logo_Ch.141.PNG/revision/latest?cb=20210904095011) ⚠️ (sólo la wiki) |
| **Gremio de Cazadores** (Choi Jong-In, Cha Hae-In) | **escudo blanco y gris con una espada vertical**, gótico | 480×480 | [Insignia Hunters](https://static.wikia.nocookie.net/solo-leveling/images/8/89/Insignia_Hunters.png) ✅ |
| **Tigre Blanco** (Baek Yoonho) | cabeza de tigre en trazos blancos | 140×140 | [Insignia White Tiger](https://static.wikia.nocookie.net/solo-leveling/images/e/ee/Insignia_White_Tiger.png) ✅ |
| **Caballería** | trazo en forma de «人», azul acero oscuro (`#102030`) | 529×471 | [Insignia Chivalry](https://static.wikia.nocookie.net/solo-leveling/images/d/d7/Insignia_Chivalry.png) ✅ |
| Carroñero (Scavenger, Thomas Andre) | la wiki no tiene símbolo (campo `Symbol=` vacío en su ficha) | — | wikitext de la wiki ⚠️ |
| **Asociación de Cazadores** | **no encontré emblema**; puede que sólo use texto o sello | — | ⚠️ |

- **Corrección:** la parte de imagen describía el de Ahjin como «círculo morado con aguijón dorado» y el del Gremio de Cazadores como «insignia dorada». **Mirados, no llevan dorado**: el de Ahjin es una llama violeta y el otro un escudo blanco con espada.
- Son diseños **con derechos** (Chugong, DUBU, D&C Media): referencia para dibujar, no para vender.
- **Para la lámina:** el de Ahjin va con la paleta Monarca (§8) y se puede grabar en madera o metal (una puerta, un mostrador, una placa). El grabado de metal CC0 y las líneas de velocidad son las dos capas libres más útiles.

---

## Punto 20 · Gustos y detalles de cada personaje

> Parte de voz. **Aviso:** Solo Leveling **no tiene *databook* oficial**: no hay alturas, pesos ni comidas favoritas oficiales. Lo dicen dos webs de fans por separado ([readsololevelingmanga.us](https://readsololevelingmanga.us/solo-leveling-character-heights-and-ages/), que marca todas las alturas como «estimadas», y [DualShockers](https://www.dualshockers.com/solo-leveling-characters-age-height-class/)) ✅. Las alturas que circulan son de fans.
>
> ⚠️ **Spoilers:** Suho y lo que viene tras la T2 (Bellion, Kandiaru, Ashborn) son del final. Sirven para escribir bien al personaje, **no para ponerlos en la lámina** (§17).

### Sung Jinwoo
- **Cumpleaños: 8 de marzo** ([AniList](https://anilist.co/character/129928) + [X oficial de *ARISE*](https://x.com/Sololv_ARISE_GL/status/1766225772581363774), citado por la [wiki del juego](https://solo-leveling-arise.fandom.com/wiki/Sung_Jinwoo#Trivia)) ✅.
- **Edad:** 23-24 (AniList) ⚠️. **Altura:** sin dato oficial; los fans dan de 179 a 190 cm ⚠️.
- **Lo que le importa:** su familia (AniList: «se preocupa muchísimo por su familia»). Su madre, Park Kyung-Hye, lleva cuatro años en coma por el «Sueño Eterno» ([wiki: Park Kyung-Hye](https://solo-leveling.fandom.com/wiki/Park_Kyung-Hye#History)) ✅.
- **Cómo se veía antes:** tímido e inseguro por la pobreza y por ser rango E. Le escondía a Lee Joohee por qué seguía de cazador ([wiki: Personality](https://solo-leveling.fandom.com/wiki/Sung_Jinwoo#Personality)) ⚠️.
- **Cómo se ve después:** el más fuerte del mundo, pero educado y sencillo. Le da igual lo material: se va a Jeju sin dudar a salvar a otros cazadores (wiki) ⚠️.

### Cha Hae-In
- **Cumpleaños: 24 de diciembre** ([wiki: Trivia](https://solo-leveling.fandom.com/wiki/Cha_Hae-In#Trivia) + [X oficial de *ARISE*](https://x.com/Sololv_ARISE_GL/status/1871420538591277239)) ✅.
- **Edad:** 23 (AniList) ⚠️. **Altura:** estimación de fans, 160-170 cm ⚠️.
- **Cargo:** vicepresidenta del Gremio de Cazadores, rango S, 9.ª cazadora de Corea; discípula del dojo de Song Chiyul ([AniList](https://anilist.co/character/138789)) ⚠️.
- **Afición: el kendo.** Sigue yendo a clase dos años después de ser rango S (wiki) ⚠️.
- **Lo que odia:** puede **oler el maná**, y le desagrada el olor de casi todos los cazadores. **El de Jinwoo, no** (AniList; se repite en reseñas) ⚠️.
- **Cómo se ve a sí misma:** de joven fue **atleta de pista**. Una lesión de tobillo acabó con su carrera y sintió un vacío. Al despertar como cazadora encontró «una nueva pista» ([*ARISE*, Dossier #01-#05](https://solo-leveling-arise.fandom.com/wiki/Cha_Hae-In#Dossier) + [Poggers](https://poggers.com/blogs/anime/solo-leveling-chae-hae-in)) ✅.

### Igris
- **Nombre humano: Sian Halat.** Caballero plebeyo, famoso por su espada, con esposa e hijos. Los nobles, celosos, **mataron a su familia delante de él** y luego a él. Murió consumido por la sed de sangre y oyó «Arise» ([*ARISE*, Secret File](https://solo-leveling-arise.fandom.com/wiki/Igris#Secret_File) + [CBR](https://www.cbr.com/solo-leveling-arise-igris-backstory-hunter-origin/) + [GameRant](https://gamerant.com/solo-leveling-from-human-to-shadow-the-untold-tale-of-igris/)) ✅.
- **Manía:** le trae a Jinwoo **las cabezas de los enemigos como trofeo**. Iron le copia y a Igris le molesta ([wiki: Trivia](https://solo-leveling.fandom.com/wiki/Igris#Trivia)) ⚠️ (también en §16).
- **Cómo se ve:** leal, respetuoso, caballeroso. **Valora la educación**: discutió con Bellion para que Suho fuera a la escuela (wiki, spoiler) ⚠️.
- Sin cumpleaños, altura ni comida: **no existen** en la wiki ni en el juego.

### Beru
- **Afición: los doramas coreanos de época.** De ahí su forma de hablar **arcaica y florida** ([wiki: Personality](https://solo-leveling.fandom.com/wiki/Beru#Personality)) ⚠️. Encaja con el doblaje: «mi rey» y siempre de usted (§12.3) ✅.
- **Cómo se ve:** nació «para liderar a las hormigas» con una orden: exterminar a los humanos. Devoró todo, hasta a los suyos. Esa misma lealtad absoluta la pasa a Jinwoo ([*ARISE*, Secret File](https://solo-leveling-arise.fandom.com/wiki/Beru#Secret_File)) ⚠️.
- **A quién quiere:** a Suho, el hijo de Jinwoo. Casi llora al saber que el niño lo olvidaría (wiki, spoiler) ⚠️.

### Secundarios
- **Yoo Jinho:** se compra **armaduras carísimas e inútiles** (gag). Ve a Jinwoo como a un hermano mayor y quiso dejar la empresa de su padre para seguirlo ([wiki](https://solo-leveling.fandom.com/wiki/Yoo_Jinho#Personality)) ⚠️. AniList le da 22 años; en el doblaje del ep. 5 dice «21 años y rango D» (§12.3).
- **Go Gunhee:** odiaba hacerse mayor y no poder pelear. Trabajaba hasta dañar su salud ([wiki](https://solo-leveling.fandom.com/wiki/Go_Gunhee#Personality)) ⚠️.
- **Sung Jinah:** cuando se enfada, le da patadas a Jinwoo… y se hace daño ella, porque él es duro como una piedra ([wiki](https://solo-leveling.fandom.com/wiki/Sung_Jinah#Personality)) ⚠️.
- **El Sistema:** no tiene gustos. Es un programa del Arquitecto (Kandiaru) hecho para Ashborn y su recipiente humano ([wiki: System](https://solo-leveling.fandom.com/wiki/System#Trivia), spoiler) ⚠️.

**Para la lámina:** la historia de Igris (un caballero que lo perdió todo y ahora sirve) da peso a su silencio. Beru habla florido porque ve doramas: eso justifica su «mi rey». Cha Hae-In, atleta que perdió su carrera por una lesión, sirve para un texto sobre superar un límite del cuerpo (la voz también se lesiona).

---

## Punto 21 · Por qué la gente la ama (y la escena que hace llorar)

> Parte de voz, más lo que ya estaba en §3 y §16.

### Los números
- **Crunchyroll Anime Awards 2025** (25-may-2025, Tokio): **9 premios de 13 nominaciones**, entre ellos **Anime del año**, Mejor serie nueva, Mejor acción, Mejor banda sonora, **Mejor protagonista** y Mejor ending ([Hollywood Reporter](https://www.hollywoodreporter.com/tv/tv-news/2025-crunchyroll-anime-awards-winners-list-1236230002/) + [Kakao Entertainment](https://newsroom.kakaoent.com/news/solo-leveling-wins-top-honor-at-crunchyroll-anime-awards-2025/)) ✅. Kakao, dueña de la obra, lo presenta como la primera obra coreana que gana el premio mayor ⚠️.
- **51 millones de votos**, récord de esos premios ([eeo Media](https://eeo.today/media/2025/06/02/229291/) + [ASCII.jp](https://ascii.jp/elem/000/004/277/4277087/), en japonés) ✅. **México, Chile y España** están entre los 10 países que más votaron (ASCII.jp) ⚠️.
- El director, al recibirlo: «Este logro es del equipo apasionado, del reparto y de los fans que la abrazaron» (eeo Media, traducido del japonés) ⚠️.
- **Más reseñas que One Piece en Crunchyroll** con sólo 23 episodios: 60 300 frente a 59 600 (17-mar-2025) ([Atento a Música](https://atentoamusicamedia.substack.com/p/solo-leveling-rompe-el-record-de), en español) ⚠️ (un blog).
- **Oricon:** el tomo 24 del manhwa fue **n.º 1 de ventas de manga en Japón** su primera semana (~50 967 copias, marzo de 2026), por delante de One Piece y JoJo ([CBR](https://www.cbr.com/solo-leveling-volume-24-oricon-sales-ranking-win/)) ⚠️.
- **El juego *ARISE* recaudó más de 100 millones de dólares en 3 meses** (Corea 33 %, EE. UU. 19 %) ([Sensor Tower](https://sensortower.com/blog/solo-leveling-arise-revenue-surpasses-usd100-million-in-3-months)) ⚠️.

### Por qué se identifican con Jinwoo
- **Del más débil del mundo al más fuerte.** Es la «fantasía de poder» que más citan reseñas y foros ([reseñas de MyAnimeList](https://myanimelist.net/profile/GRG3/reviews), [IMDb](https://m.imdb.com/news/ni65093385)) ⚠️.
- **«Si quiere hacer algo, lo hace»:** un protagonista sin dudas eternas ni angustia de más (mismas fuentes) ⚠️.
- Y lo hace **por su familia** (punto 20): la fuerza tiene un porqué.

### La escena que hace llorar: «Lo valió todo» (ep. 21)
- **Qué pasa:** Jinwoo conquista el Castillo de los Demonios, consigue el **Agua Sagrada de la Vida** y va directo al hospital. Su madre despierta tras cuatro años de coma. Lo primero que pregunta es cómo está Jinah ([wiki: Episode 21](https://solo-leveling.fandom.com/wiki/Episode_21) + [wiki: Park Kyung-Hye](https://solo-leveling.fandom.com/wiki/Park_Kyung-Hye#History); cap. 90 del webtoon) ✅.
- **Cómo está dibujada** (fotograma visto en un [post de Reddit con 631 votos](https://www.reddit.com/r/sololeveling/comments/1j17hlz/i_cried_during_this/), [imagen](https://i.redd.it/vth9mmvyp4me1.jpeg)): **primer plano** de Jinwoo llorando, **luz azul fría**, una mano en la mejilla, lágrimas cayendo de la barbilla ✅ (visto).
- **Por qué duele:** el comentario que lo resume: «**Está llorando feo.** Los animadores no quisieron que se viera varonil ni guapo. Me encanta esta escena» ✅ (citado textual).
- **Cómo reaccionó la gente:** en algunos sitios el capítulo recibió votos negativos por mostrarlo «débil»; muchos lo defendieron: «fue hermoso y mostró cuánto había valido la pena hacerlo todo por su madre» ([Reddit, 75 votos](https://www.reddit.com/r/sololeveling/comments/1q64i1a/)) ⚠️.
- **Música:** el ep. 21 tiene el tema de inserción «REVIVƎЯ» (SAWANO feat. SennaRin, §13) ⚠️: no sé si suena justo en ese momento.
- **Minuto exacto: no lo tengo** ⚠️. El avance oficial del ep. 21 en Dailymotion (`x9fcj74`) da «Not found» y YouTube pide iniciar sesión.

### Las que hacen gritar y reír
- **Gritar de emoción:** cada «**Surge.**» (ep. 14 · 12:48; ep. 18 · 17:49; ep. 21 · 02:33, §12.3) y la pelea con Igris (ep. 12, §16) ✅. La exposición de Seúl tiene una estación para **invocar sombras gritando «Arise»** (punto 23): es el momento que todos reconocen ✅.
- **Beru arrodillado pidiendo un nombre** (ep. 25 · 09:04, §12.3) ✅.
- **Reír:** Iron copiándole a Igris lo de las cabezas, las armaduras inútiles de Jinho, Jinah pateando a su hermano (punto 20) y las sombras en *chibi* como mayordomos (§16).

**Para la lámina:** el gancho es «la más votada del año» (51 millones de votos). La escena del ep. 21 es la emoción más fuerte, pero es triste: úsala sólo en un hilo que lo pida.

---

## Punto 22 · Fan dubs y comunidad hispana

> Parte de voz. Cada vídeo, comprobado por `oembed` (existe, título y canal). **Las vistas no las pude leer** ⚠️: YouTube y TikTok no las dan por `oembed` y `yt-dlp` pide iniciar sesión.

### Covers de los openings en español latino
| Opening | Canal | Enlace |
|---|---|---|
| OP 1 «LEveL» | David Delgado (@daviddelgadocovers) | [YouTube](https://www.youtube.com/watch?v=TSMWCpek2vo) ✅ |
| OP 1 «LEveL» | Edgardo Artieda, «André - A!» (@andreartieda) | [YouTube](https://www.youtube.com/watch?v=tPRRCivyjvI) ✅ |
| OP 1 «LEveL» | The Covers Duo (@TheCoversDuo) | [YouTube](https://www.youtube.com/watch?v=6GpGXTykyjo) ✅ |
| OP 1 «LEveL» | Yukisei (@Yukiseif) | [YouTube](https://www.youtube.com/watch?v=AweBtioFOIQ) ✅ |
| OP 2 «REAWAKER» | Danie Green (@DanieGreen) | [YouTube](https://www.youtube.com/watch?v=rBylGc6RmlI) ✅ |
| OP 2 «REAWAKER» | «André - A!» (el mismo del OP 1) | [YouTube](https://www.youtube.com/watch?v=edOetiCihSQ) ✅ |

### Memes y parodias hispanas
- **@yerastian** en TikTok, «Para lo que duran nememes» (#sololeveling #humor #sung #jinwoo) ([TikTok](https://www.tiktok.com/@yerastian/video/7484697888203771142)) ✅ (autor y título por `oembed`).
- Tendencia «me vi TODO Solo Leveling pero creo que me perdí el mejor capítulo», atribuida a **@naruto_dominiicano** ⚠️: no encontré el enlace directo al vídeo.

### La comunidad hablando del doblaje
- **Antov**, «Las voces de Solo Leveling | Doblaje latino» ([YouTube](https://www.youtube.com/watch?v=LRy-ClfLQ_k), ya en §12.4) ✅. No es un fandub: es un fan presentando al reparto oficial.
- **Nueva fuente del reparto:** *The Dubbing Database* tiene su ficha latina ([dubdb.fandom.com](https://dubdb.fandom.com/wiki/Solo_Leveling_(Latin_American_Spanish))): VSI México, Fernando Moctezuma, Sofía Huerta, Brandon Montor y **Daniel Lacy como Beru** ✅. Es una tercera fuente para esos nombres (§12.2).
- **México, Chile y España** entre los 10 países que más votaron en los premios de Crunchyroll (punto 21) ⚠️.

### Fandub con grupo propio: no lo encontré
- Busqué fandubs latinos de episodios enteros (Frikidoblaje, SakuraDubs, Kudasai Fandub, AS Fandub) y revisé [Fandub Database](https://fandubdb.fandom.com/) y *The Dubbing Database*. En la de fandubs **sólo hay versiones en filipino e indonesio**.
- Lo que sale son copias piratas de la temporada oficial mal etiquetadas como «fandub» y un fandub para adultos (no apto). **No digo que no exista**: no encontré uno limpio y comprobable.

**Para la lámina y el servidor:** los covers son material listo para un post de «covers de la comunidad» en el canal de canto. En #guia, el hilo con etiqueta **Doblaje** puede enlazarlos. Un fandub propio del servidor sería el primero en español de esta serie que yo haya podido encontrar.

---

## Punto 23 · Colaboraciones, figuras y cosplay

> Parte de imagen. Tamaños medidos con Pillow.

### Videojuegos (cada cruce trae poses y ropa nuevas)
- **Fortnite × *Solo Leveling: ARISE*:** tres trajes oficiales, **Sung Jinwoo, Cha Hae-In e «Igris, comandante rojo sangre»**, del 20-feb al 2-mar-2026 (antes, la «Arise Cup», 19-20 feb). El de Jinwoo es **reactivo**: cambia al eliminar rivales, como su paso a Monarca ([tienda de Fortnite](https://www.fortnite.com/item-shop/offers/sung-jinwoo-ed689683), [lote](https://www.fortnite.com/item-shop/offers/solo-levelingarise-bundle-bf68c9e7); [VideoGamer](https://www.videogamer.com/news/fortnite-solo-leveling-crossover-sung-jinwoo/) + [ExitLag](https://www.exitlag.com/news/solo-leveling-in-fortnite/)) ✅.
- ***ARISE* × *Frieren*** (oct-2025): Frieren, Fern y Stark jugables, con misión especial ([imagen oficial, 1280×720](https://cdn5.idcgames.com/storage/image/1577/frieren-collaboration-update-pv/default.jpg); [IDC Games](https://idcgames.com/en/solo-levelingarise/news/frieren-joins-solo-leveling-arise-in-an-epic-collaboration-with-beyond-journey%E2%80%99s-end-2025-10-23-11-00-11653) + [Inven Global](https://www.invenglobal.com/articles/19808/solo-leveling-arise-announces-collaboration-with-frieren-beyond-journeys-end)) ✅. También en la biblia de Frieren (33).
- **Grand Summoners × Solo Leveling** (desde el 12-jun-2026): Jinwoo, Choi Jong-In, Cha Hae-In e Igris jugables, con sus armas ([ANN, nota de prensa](https://www.animenewsnetwork.com/press-release/2026-06-12/grand-summoners-x-solo-leveling-now-available-in-many-territories-worldwide/.238449) + [CBR](https://www.cbr.com/solo-leveling-grand-summoners-game-crossover-collaboration/)) ✅.
- ***ARISE* × (G)I-DLE** (K-pop): MIYEON y SHUHUA como cazadoras jugables (Game8) ⚠️. **Interesa al servidor: es de canto.**
- ***ARISE* × OVERDRIVE** (código cruzado; dotgg.gg) ⚠️ y **Seven Knights Re:BIRTH × Solo Leveling** (gamefragger.com) ⚠️: una fuente cada uno.

### Eventos, cafés y tiendas
- **Exposición inmersiva en Seúl** (la primera de la serie): 22-nov-2025 a 1-mar-2026, DUEX Hongdae. Zonas del **templo de Cartenon**, **Jeju** y la **mazmorra de la estación de Hongdae**; **figuras a tamaño real de Jinwoo, Igris y el Rey Hormiga**; una estación para **invocar sombras gritando «Arise»**; café temático y licencias de cazador de mentira en la tienda ([visual, 1107×622](https://static.animecorner.me/2025/09/1759182098-938fb7693a9c38ba777e1cf5b0a4bc41.png); [Anime Corner](https://animecorner.me/solo-leveling-gets-first-visual-for-immersive-new-exhibition-in-korea/) + [The Korea Herald](https://www.koreaherald.com/article/10589225)) ✅.
- **Café *ARISE* × ANIPLUS:** 22-ago a 6-oct-2024, Hapjeong, Seúl (web de reservas, world.nol.com) ⚠️.
- **«System Sync»,** tienda temporal de **Solo Leveling × *Omniscient Reader's Viewpoint*** (las dos las publica Ize Press en inglés): 14-30 ago-2026, Manhattan, junto a Anime NYC. Ropa que brilla en la oscuridad ([ANN](https://www.animenewsnetwork.com/news/2026-07-17/solo-leveling-omniscient-reader-viewpoint-pop-up-store-to-open-in-new-york-in-august/.239721) + [Yen Press](https://yenpress.com/news/system-sync) + [CBR](https://www.cbr.com/solo-leveling-omniscient-readers-viewpoint-system-sync/)) ✅.
- **Colaboración con marcas de ropa o bebidas** (tipo Uniqlo o 7-Eleven): **no la encontré** ⚠️.

### Figuras oficiales (pose en 3D de verdad)
- **Nendoroid Sung Jinwoo n.º 2597** (Good Smile): unos 10 cm, **3 caras** (mando, batalla, *chibi*) y piezas: **Knight Killer**, un soldado de sombra y **el panel del Sistema**. Salió en abril de 2025; se reedita en marzo de 2027 ([foto oficial, 750×1000](https://www.goodsmile.com/gsc-webrevo-sdk-storage-prd/product/image/34792/u5732DjFSANprK9bicHCL4kxQ0RzWZUm.jpg); [Good Smile](https://www.goodsmile.com/en/product/34792) + [CBR](https://www.cbr.com/solo-leveling-sung-jinwoo-good-smile-company-nendoroid-concept-art-reveal/)) ✅. **Sirve de referencia 3D:** de pie, arma al hombro. La cara *chibi* **no** va en la lámina (punto 18).
- Un peluche de Jinwoo de Good Smile se agotó enseguida (ScreenRant) ⚠️.

### Cosplay bien hecho (volumen y materiales reales)
- **Esil Radiru**, armadura roja y dorada hecha a mano, con relieve real en hombreras, peto y guantes ([foto, 4096×2731](https://i.redd.it/i917f5bdst6h1.jpg), de u/_Mikomihokina_, [post en r/SoloLeveling](https://www.reddit.com/r/sololeveling/comments/1u3r1le/)) ✅ (vista; autora identificada).
- **Igris** sin casco: placas superpuestas de espesor real (goma EVA o worbla), capa, y el casco aparte en un pie ([foto, 4016×6016](https://i.redd.it/mv4qi4hnqjcg1.jpg), de u/Halfangel66, [post](https://www.reddit.com/r/sololeveling/comments/1q980kq/)) ⚠️ (una fuente, vista). **Enseña cómo brilla el metal grabado con luz de estudio.**
- Con más votos, sin abrir: «Igris Cosplay» (5925 puntos, vídeo) y «Peak Igris Cosplay» (1635) ⚠️.
- **Descartados:** un cosplay de Cha Hae-In con peluca rubia pero **ropa de calle**, no el uniforme; y el viral «Perfect cosplay of Jinwoo» (5598 puntos), que es un chico que se parece a Jinwoo y se enmarca la cara con una copa de vino: es un meme, no un disfraz.

**Para la lámina:** la exposición demuestra que **invocar sombras es el gesto que todos reconocen**. El Nendoroid enseña el panel del Sistema como objeto físico: encaja con la idea del encargo (la ventana dentro de un sitio real). El cosplay de Igris, para el brillo del metal.

---

## Punto 24 · Obras parecidas y láminas vecinas

> Parte de texto, más `datos-texto.md` (AniList).

### Las que recomiendan los fans y la prensa
- **AniList** (votos de usuarios): *Sword Art Online* (166), ***Tower of God*** (88), ***The Eminence in Shadow*** (60), *I Got a Cheat Skill in Another World…* (56), ***The God of High School*** (55), *Tomb Raider King* (52), *Shangri-La Frontier* (16) ([AniList](https://anilist.co/anime/151807)) ✅.
- **La prensa repite los mismos** ([MovieWeb](https://movieweb.com/best-action-anime-like-solo-leveling/), [Dexerto](https://www.dexerto.com/anime/best-anime-like-solo-leveling-2463795/), [ScreenRant](https://screenrant.com/best-anime-like-solo-leveling-watch/)) ✅:
  - ***Tower of God***: subir piso a piso, con más misterio.
  - ***The Eminence in Shadow***: el mismo gancho del poder oculto y un «ejército» propio, pero en parodia. Al revés de Solo Leveling, que va en serio.
  - Mazmorras y «sistema»: *Shangri-La Frontier*, *DanMachi*, *Overlord*, *Noblesse*.
  - Frase de uno de ellos: «**la trinidad del webtoon** (*Tower of God*, *God of High School*, *Noblesse*) es el ADN más parecido».
- **La pareja segura** si se hace una encuesta o un evento cruzado: *Tower of God* y *The Eminence in Shadow*.

### Influencias del autor
- **Chugong** casi no da entrevistas. Un blog de una tienda francesa dice que es fan de los RPG y de la «fantasía de progresión», y que el Sistema viene de juegos como **Diablo, Skyrim o World of Warcraft** ([solo-leveling.fr](https://solo-leveling.fr/en/blogs/blog-solo-leveling/chugong-le-genie-creatif-derriere-le-phenomene-solo-leveling)) ⚠️. **No encontré** una entrevista suya que lo diga (busqué en coreano e inglés).
- Lo que sí dijo, citado: simplificó el trasfondo cósmico (el **Itarim**, un dios por universo) para no ser «demasiado sombrío» con lectores jóvenes ([CBR, entrevista](https://www.cbr.com/solo-leveling-chugong-interview-removed-itarim-light-novel-bleak/)) ✅.

### Obras relacionadas
- ***Solo Leveling: Ragnarok***, la continuación en manhwa, con su propia lista de arcos ([wiki: Story Arcs (Ragnarok)](https://solo-leveling.fandom.com/wiki/Story_Arcs_(Ragnarok))) ✅.
- La película resumen ***ReAwakening*** («Segundo despertar» en latino, §12.1) y ***Beyond the System***, en producción (§2).
- ***Omniscient Reader's Viewpoint***, el otro gran fantástico coreano: comparte editorial en inglés y la tienda «System Sync» (punto 23). En Safebooru sale junto a Solo Leveling (su protagonista, Kim Dokja, aparece en la búsqueda de fan art).

### Láminas vecinas del servidor (para no repetir)
- **One Piece (01) y Attack on Titan (02)** avisan en sus biblias de que su tablón debe **distinguirse del de Solo Leveling**: «Que no parezca el tablón de Solo Leveling: madera de barco y clavos, nunca corcho» ✅ (leído en sus biblias). **El tablón de corcho del Concepto B es ya de Solo Leveling**: si se rehace, que siga siendo corcho.
- **Jujutsu Kaisen (32), Demon Slayer (31), Naruto (30), My Hero Academia (25) y One Punch Man (35)**: ninguna usa un mostrador de recepción, una ventana de juego ni un salón del trono. **No hay choque** con los tres conceptos (revisado por el índice de cada biblia).
- **Frieren (33)** tiene la colaboración con *ARISE* y una partida grabada con la caja de diálogo del juego ✅.

---

## Punto 25 · El mundo, la historia por arcos y sus símbolos

> Parte de texto. Fuente base: la wiki por su API ([Class Ranks](https://solo-leveling.fandom.com/wiki/Class_Ranks), [Guilds](https://solo-leveling.fandom.com/wiki/Guilds), [Story Arcs](https://solo-leveling.fandom.com/wiki/Story_Arcs)), cruzada con los títulos de episodio de [Wikipedia](https://en.wikipedia.org/wiki/List_of_Solo_Leveling_episodes) ✅.

### El mundo en cinco líneas
1. Hace unos **8-9 años** se abrieron **portales** a **mazmorras** llenas de monstruos. A la vez, algunas personas despertaron con **maná**: son los **cazadores**.
2. Cada cazador tiene un **rango, de E (el más débil) a S**. Fija el sueldo y el respeto, y **es de por vida**, salvo un «segundo despertar» rarísimo.
3. Los **gremios** son empresas que limpian mazmorras. La **Asociación de Cazadores** de cada país lo regula todo (la coreana, en Guro, Seúl, §9).
4. **Jinwoo es la excepción:** el **Sistema** lo elige como «Jugador» y le deja subir de nivel sin techo.
5. Detrás del Sistema hay un **Arquitecto** y una guerra entre **Monarcas** y **Gobernantes** que llega a la Tierra (spoiler, sin animar).

### La historia por arcos
*En el anime (T1-T2, ep. 1-25). Nombres de arco de la wiki, traducidos por mí: no son títulos oficiales latinos.*
1. **Mazmorra de rango D** (ep. 1-3): la mazmorra doble; muere casi todo el grupo.
2. **El despertar** (ep. 3): despierta en el hospital y ve el Sistema.
3. **Mazmorra instantánea** (ep. 3-4): su primera cacería solo.
4. **Mazmorra y lagartos** (ep. 5-6): la encerrona de Kang Taeshik.
5. **Mazmorra y presos** (ep. 7-9).
6. **El grupo de Yoo Jinho** (ep. 10): forma equipo con Jinho.
7. **Cambio de clase** (ep. 11-12): el caballero rojo del trono vacío (**Igris**) y el primer «Surge».
8. **Red Gate** (ep. 13-14): la trampa en la incursión del Tigre Blanco.
9. **Castillo de los Demonios** (ep. 15): a por el agua de la vida.
10. **Reevaluación** (ep. 16): el medidor no puede con él.
11. **Portal del Gremio de Cazadores** (ep. 16-18): de minero en un portal de rango A.
12. **Vuelta al Castillo** (ep. 18-21): Esil Radiru y **Baran**, el Rey Demonio. El agua sagrada para su madre (punto 21).
13. **Isla de Jeju** (ep. 21-25): la incursión y **el Rey Hormiga** (Beru).
14. **Reclutamiento** (ep. 25).

*Sin animar (webtoon y novela):* Gremio Ahjin, vuelta a la mazmorra doble, crisis de Japón, Conferencia Internacional de Gremios (aparecen **Monarcas y Gobernantes**), Guerra de los Monarcas, batalla final contra **Antares**, el Rey Dragón, epílogo ([wiki: Story Arcs](https://solo-leveling.fandom.com/wiki/Story_Arcs)) ✅. No van en la lámina (§17).

### Emblemas
- Los de los gremios, **mirados y medidos**, están en el **punto 19**. El más útil es el de **Ahjin** (llama violeta, 700×700), el gremio de Jinwoo.
- Los **grados de las sombras** (Normal → Élite → Caballero → Caballero de élite → General → Mariscal) ya están en el Concepto C (§20).

### Objetos icónicos
- **La ventana del Sistema** (§4). Y el **panel del Sistema como pieza física** del Nendoroid (punto 23).
- **Espada del Rey Demonio:** la usaba **Baran**; Jinwoo se la da a **Igris** y, años después, es de **Cha Hae-In**. Hoja clara con una línea negra central y guarda arqueada ([wiki](https://solo-leveling.fandom.com/wiki/Demon_King%27s_Longsword)) ✅.
- **Knight Killer**, la daga que compra en la tienda del Sistema (ep. 12; §10 y Nendoroid) ✅.
- **La Ira de Kamish:** dos dagas del colmillo del dragón Kamish, naranjas con filo rojo (webtoon) ([wiki](https://solo-leveling.fandom.com/wiki/Kamish%27s_Wrath)) ✅. **Aún no sale en el anime**: no usarla.
- **La Estatua del Dios:** su nombre coreano es un juego de palabras, **신상 (Shin-Sang)** = «dios» + «estatua» ([wiki: Statue of God](https://solo-leveling.fandom.com/wiki/Statue_of_God)) ✅. Curiosidad para un texto del bot.

### Vocabulario que un fan reconoce al instante
| Latino (Crunchyroll, §4 y §12.3) ✅ | Original | Nota |
|---|---|---|
| **Portal** | Gate | |
| **Mazmorra** | Dungeon | |
| **Asociación de Cazadores** | Hunters Association | |
| **Rango E… S** | E-Rank… S-Rank | |
| **Gremio** | Guild | |
| **Licencia de cazador** | Hunter's License | |
| **Soldados sombríos** | Shadow soldiers | |
| **Perjuicio** | debuff | |
| **«Surge.»** | «Arise.» | la orden de extracción: lo más citado |
| **Rey de las Sombras** | Shadow Monarch | **no** «Monarca de las Sombras» |
| **Monarca** | Monarch | sólo para otros: «Monarca Demoníaco Baran» |

*Sin nombre latino comprobado* ⚠️ (en inglés; los cuatro primeros son de arcos sin animar): Architect (Kandiaru, el «moderador» del Sistema), Monarchs / Rulers, Dungeon Break (la mazmorra que revienta al mundo), Itarim (un dios por universo; [CBR](https://www.cbr.com/solo-leveling-chugong-interview-removed-itarim-light-novel-bleak/)). Estos dos **sí salen en el anime**, pero no comprobé cómo los dice el doblaje: Red Gate (el portal-trampa de los ep. 13-14, que no se puede cerrar desde fuera) y Essence Stone / Mana Crystal (lo que se vende de las mazmorras).

**Para la lámina:** los 14 arcos, uno por renglón, son una línea de tiempo lista para el hilo **«De qué va esto»**. Los rangos E→S y los grados de las sombras dan la escalera de roles.

---

## 19 · Los 14 hilos: un sitio por hilo

La ventana del Sistema va siempre dentro de un sitio real de la serie. Su cabecera usa el vocabulario oficial latino.

⚠️ La columna «Etiqueta» es una **propuesta**: el inventario no dice qué etiqueta lleva cada hilo.

| Hilo | Sitio (objeto real) | Personaje (imagen) | Cabecera | Etiqueta |
|---|---|---|---|---|
| Cómo se entra | **portal azul dentro de una valla de obra de la Asociación**, con cinta amarilla (F·20, F·5, F·7) | **Song Chiyul presenta la incursión** («Hola a todos… ¡Entremos!», ep. 1 · 07:20) o Jinwoo novato (P·1) | MISIÓN | Primeros pasos |
| 📌 La guía, de un vistazo | rascacielos de la Asociación al atardecer (F·13) con un plano en el vestíbulo | Jinwoo T2, **mano abierta a cámara** (P·3) | MAPA | Primeros pasos |
| 📌 De qué va esto | despacho del presidente (de modelo, el despacho con sofás de F·12, que es el de Choi en el ep. 8) | Go Gunhee de pie, traje negro (P·22) | NOTIFICACIÓN | Primeros pasos |
| Los roles que se ganan | escalones del trono vacío, un rango por escalón (E→S) | Igris arrodillado ([clip ep. 11 · 1:31][yt-papu-91]) | ASCENSO | Roles y zonas |
| De dónde sale un rol | mostrador de reevaluación con el **cristal negro** (S·16) | Jinwoo, mano en el cristal (ep. 16 · 03:47) | [Licencia de Cazador] | Roles y zonas |
| Reuniones y eventos | sala de mando de la incursión de Jeju; la isla en pantalla (F·10) | Cha Hae-In (P·17) | MISIÓN · OPERACIÓN | Si te atascas |
| Lo que pasa en vivo | monitor de la cámara de prensa (ep. 22) | Jinah viendo a su hermano en la tele (ep. 19 · 07:45) | EN DIRECTO | Bots y comandos |
| Los roles que te pones tú | **la tienda del Sistema sujeta como tableta** (S·7) y el cofre = INVENTARIO | Jinwoo eligiendo; botones CANCELAR · ACEPTAR (S·6) | INVENTARIO | Roles y zonas |
| El staff | sala de Supervisión de la Asociación (S·15) | Woo Jinchul (P·23) + Igris de guardaespaldas (P·20) | NOTIFICACIÓN | Normas |
| Cómo pedir algo | **el móvil con el aviso de la Asociación** (S·9) o el tablón con el cartel de reclutamiento (ep. 16 · 15:46) | Yoo Jinho con su mochila (P·21; «¿Qué hará usted, jefe?») | AVISO | Si te atascas |
| Tus zonas: abre y cierra lo que veas | portales que se abren y cierran (F·6, F·9); Intercambio de sombras | Kaisel sobrevolando (P·13) | HABILIDADES | Roles y zonas |
| Los talentos | desfile del ejército de sombras (ED T2 · 0:49) | Beru, Tank, Colmillo, Iron (P·14-16) | HABILIDADES | Doblaje |
| Dónde se trabaja | puerta de la mazmorra con el equipo de ataque (F·17), pasillo de antorchas (F·3) | Jinwoo y Jinho | NOTIFICACIÓN | Primeros pasos |
| Lo que hay que leer | habitación del hospital (ep. 3, F·14) | Jinwoo leyendo su primera ventana (S·1) | «ADVERTENCIA: …» con la palabra en rojo | Normas |

## 20 · Tres conceptos de lámina

### Concepto A · «El mostrador de registro de la Asociación»
- **Objeto real y sitio:** el **mostrador de reevaluación** de la Asociación de Cazadores. Sobre la mesa, el **cristal negro** medidor sobre su peana (ep. 16 · 03:47, «Ponga la mano sobre ese cristal negro») y una **licencia de cazador** de plástico. Detrás, una mampara de cristal. Todo en Blender, **con modelos CC BY comprobados** (§11): [Reception Desk][sk-desk] (Yvonne DeBandi), [Crystal Ball][sk-crystal] (Randall_3D, teñida de negro), [ID Card Model][sk-idcard] (Johana-PS). La oficina real se ve en S·15-16: madera, fluorescentes, gente de traje.
- **Personaje:** Jinwoo T2, de pie, con la mano abierta sobre el cristal. **Pose: el CV de la T2 (P·3)**, que ya tiene la mano abierta hacia delante; la cara, de la KV T2. Detrás, fuera de foco, **un funcionario con papeles (S·15)**.
- **Cómo habla:** la ventana del Sistema **sale del cristal** como lectura del medidor, **igual que la de S·10**: panel `#112A39`, esquinas de circuito `#82F3FA`, barra de luz arriba, cabecera «NOTIFICACIÓN» en su recuadro y el «!» en otro. Cabecera en Nunito Black (o Michroma). Texto en Lato. Rangos en Exo 2, **en negrita cursiva y entre corchetes**: ***[E]*** → ***[S]***. El comentario de Jinwoo va en cursiva, sin globo, junto a su hombro: «Aquí te registras. Luego, a subir.»
- **Dónde va cada texto:**
  - **Título del hilo** en la cabecera de la ventana.
  - **Pasos** como líneas de la ventana (1, 2, 3).
  - **Etiqueta del hilo** impresa en la licencia de cazador.
  - Aviso de **normas** en el cartel de la mampara, con la palabra clave en **rojo `#9F205C`**.
- **Para que no quede plano:** la esfera ilumina desde abajo la cara y la mano de Jinwoo (cian `#89BAD3`). La mampara de cristal va **delante**, con reflejos. En primer plano, desenfocada, una segunda licencia sobre la mesa. La barra de luz de la ventana deja un reflejo en la madera del mostrador.
- **Hilos que cubre:** Cómo se entra, De dónde sale un rol, Los roles que se ganan, Lo que hay que leer.

### Concepto B · «El tablón de misiones del vestíbulo»
- **Objeto real y sitio:** un **tablón de corcho y pantalla** en el vestíbulo de la Asociación, con carteles oficiales como el de ep. 16 · 15:46 («Buscamos mineros para entrar al portal de rango A…»). Al fondo, por las cristaleras, el rascacielos al atardecer (F·13) o la noche de Seúl. Se hace en Blender con [Bulletin Boards + Geometry Nodes][sk-board] (CC BY) y corcho [Cork 004][acg-cork] (CC0). **Variante más fiel:** en vez del tablón, **el móvil con el aviso de la Asociación** (S·9: «From: Hunter's Association · Urgent: Request to Participate…» con los botones Clear | View), en grande, sujeto por una mano.
- **Personaje:** **Cha Hae-In**, la secundaria más querida. **Rubia, uniforme rojo `#BC2B47` y blanco, espada negra** (no armadura clara: eso era un error de la primera pasada). Pose: **la del render de cazadora (P·18)**, de pie con la espada baja, girada hacia el tablón; o **desenvainando (P·17)** si el hilo avisa de algo. Luz de perfil como en P·19.
- **Cómo habla:** el cartel que señala se «activa» y proyecta una ventana del Sistema **azul**, con cabecera «MISIÓN». Su frase va en una línea corta, en cursiva, estilo subtítulo, **y de usted**, como habla en el doblaje («Pensé que debería saberlo»): «Apúntese aquí. Salga a tiempo.»
- **Dónde va cada texto:**
  - **Eventos** = carteles del tablón, uno por evento.
  - **Horarios** en la pantalla.
  - **Cómo pedir algo** en la ventana (o en la tarjeta del móvil, en la variante).
  - **Etiquetas** como chinchetas de colores.
- **Para que no quede plano:** papeles sueltos en primer plano, desenfocados. Luz fría del monitor en su perfil y reflejo de la ciudad en el cristal del fondo.
- **Hilos que cubre:** Reuniones y eventos, Lo que pasa en vivo, Cómo pedir algo, Dónde se trabaja.

### Concepto C · «El salón del trono vacío»
- **Objeto real y sitio:** el **salón del trono vacío** de Igris (ep. 11-12). **Base en Blender: [Hall of Blood-Red Commander Igris][sk-igrishall]** (Jp André, CC BY, hecho a propósito de este salón; antes proponía el [Throne Room][sk-throne] genérico). Los colores, medidos en el [clip del ep. 11 · 0:01][yt-papu-1]: columnas `#1E121B`-`#2C151D`, **alfombra roja `#6A232B`**, velas y lámparas doradas. Los **escalones del estrado** llevan grabados los grados de las sombras: Normal → Élite → Caballero → Caballero de élite → General → Mariscal ([wiki: Shadows][wiki-shadows] ✅). Así cada rol del servidor es un escalón.
- **Personaje:** **Igris arrodillado**, ahora **sombra negra con líneas cian** en el salón donde antes fue rojo: el contraste cuenta su historia. Modelo para posarlo: [Igris de missafe][sk-igris] o [el de shrithik][sk-igris2] (CC BY). Espada: [Igris broadsword][sk-igrissword]. Jinwoo de pie en el escalón alto, **sudadera gris y daga baja, como en el [clip · 1:31][yt-papu-91]**, o con el abrigo de la T2 (P·2).
- **Cómo habla:** ventana **violeta Monarca** (`#9229F9` / `#ED77F3`) proyectada sobre el respaldo del trono. Cabecera «ASCENSO». Igris no habla: su «texto» es el nombre del rol en su placa, en negrita cursiva y entre corchetes: ***[Igris · Caballero de élite]***. Jinwoo cierra con una sola palabra grande: «Surge.»
- **Dónde va cada texto:**
  - **Rangos** en los escalones.
  - **Cómo se gana cada uno** en la ventana.
  - **Staff** en placas junto a Igris.
  - **Etiquetas** grabadas en las columnas.
- **Para que no quede plano:** humo de sombras a ras de suelo, en cian. La **hoja de la espada de Igris en primer plano**, cortando el cuadro. Contraluz violeta desde el trono y velas cálidas a los lados, frías contra calientes.
- **Hilos que cubre:** Los roles que se ganan, Los roles que te pones tú, El staff, Los talentos.

### Lámina 2 (si no cabe)
- **«Los talentos»:** desfile de sombras con nombre (Beru, Tank, Colmillo, Kaisel, Iron), cada una con su ficha [Nombre Nv.], usando sus visuales oficiales (P·13-16). **Beru al frente, arrodillado, con su frase del doblaje: «Mi rey… concédame un nombre.»** Fondo: el palacio blanco del ending T2 (ED · 0:49), con el ejército en fila.
- **«Normas»:** los **mandamientos grabados** del templo de Cartenon (ep. 2 · 01:10: «First, worship the God. Second, praise the God…») convertidos en las normas del servidor, **bajo la estatua del Dios sonriendo** (F·1, 3840×2160) en la sala del anillo de luces azules (F·2). Es piedra tallada: no hace falta globo. El castigo, en una ventana roja: «ADVERTENCIA: no cumplir la norma…» (como en el [clip del ep. 6 · 0:07][yt-clip6-7]).

### Lo que añade el repaso (puntos 18-25) a los tres conceptos
Los tres se mantienen. Mejoran así:
- **En los tres, el acabado (punto 18):** si el personaje sale de un fotograma o un render, **casi sin línea negra**, con **luz de borde de color** (cian de la ventana, violeta Monarca) y el **fondo desenfocado**. Grano fino por encima. Nada de caras de comedia.
- **A · El mostrador:** la Asociación **no tiene emblema** que yo encontrara (punto 19). La mampara lleva sólo texto. Si el hilo es de roles, la licencia de cazador puede llevar el sello de **Ahjin** (llama violeta, 700×700), que va con la paleta Monarca.
- **B · El tablón:** **se queda de corcho**: One Piece y Attack on Titan ya lo esquivan en sus biblias (punto 24). Para posar a Cha Hae-In en Blender, el [modelo de Casttelan2][sk-cha] (CC BY). Su «usted» del doblaje sigue siendo la voz justa.
- **C · El salón del trono:** Igris fue **Sian Halat**, un caballero que perdió a su familia (punto 20). Arrodillado y en silencio es su gesto justo. Para la armadura, el **grabado de metal CC0** (punto 19); para el brillo del metal con luz de estudio, el [cosplay de Igris](https://i.redd.it/mv4qi4hnqjcg1.jpg).
- **Lámina 2 nueva, «De qué va esto»:** la **historia en 14 arcos** (punto 25) como una ventana del Sistema de **misiones completadas**, una línea por arco (***[Completada]*** Mazmorra doble · ep. 1-3…). Jinwoo de perfil con dos dedos en la barbilla (S·2). Sin spoilers de lo no animado.

---

## 21 · Lo que no pude verificar

Tras la segunda pasada quedan:
- **Si el doblaje dice «Surge» o «Levántate»** en los «Arise»: YouTube no deja bajar el audio de los clips y Doblaje Wiki no tiene muestra de esas escenas. Todo apunta a «Surge» (título de la T2 y la marca de Crunchyroll LA), pero no lo oí.
- **Varias frases del doblaje** salen de un reconocimiento de voz automático (Whisper) sobre muestras de 30 s: el sentido está cruzado con subtítulos, pero **alguna palabra puede estar mal**. Antes de rotularlas, escúchalas en la [página de Doblaje Wiki][dw] (tiene reproductor).
- **El gesto exacto del primer «Arise»** (ep. 12 · 17:39) y **el minuto en que Igris se arrodilla**: no hay clip oficial de esa escena en YouTube y la wiki sólo tiene la captura de la extracción.
- **Fotogramas grandes de los clips:** los *storyboards* son de 320×180. Sirven para mirar, no para recortar. Para recortar, las capturas de la wiki (§10.0) o el vídeo en Crunchyroll.
- **Interfaz del juego ARISE:** Game UI Database y The Cutting Room Floor siguen en 403.
- **TV Tropes:** 403 (Cloudflare).
- **TikTok** (reto de la misión diaria, «Who's my king»): no lo abrí.
- **Pixiv y ArtStation:** no probados (DeviantArt y Reddit sí).
- **Descripción del canal:** está cortada en el inventario.
- **Letras de la ventana** (Trueno Round, Circe Rounded, Caros Soft, Eternal): nadie oficial dice cuáles son; sólo fans.

**Tras el repaso de los puntos 18-25 (24-sep-2026) quedan además:**
- **El minuto de la escena del hospital** (ep. 21, la madre despierta): el avance en Dailymotion da «Not found» y YouTube pide iniciar sesión.
- **Las vistas** de los 6 covers y del meme de TikTok: `oembed` no las da.
- **El vídeo de @naruto_dominiicano:** sin enlace directo.
- **Un fandub latino con grupo propio:** no lo encontré.
- **Qué programa 2D usó A-1 Pictures** y los nombres de sus filtros: sin fuente.
- **Una entrevista de DUBU** sobre su técnica y **una de Chugong** sobre sus influencias: no las encontré.
- **Emblema de la Asociación de Cazadores** y **patrones de tela** de la ropa: no los encontré.
- **Alturas y comidas favoritas:** no hay *databook* oficial.
- **TV Tropes** (403, sin copia en Wayback) y **namu.wiki** (403; sólo fragmentos del buscador).

## Cumplimiento del encargo

| Punto de `ENCARGO.md` | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial, en cantidad y variado | ✅ | 1613 imágenes de la wiki revisadas; 60 escogidas en 3 hojas (KV, CV, cuentas atrás, renders, visuales de sombras) (§10) |
| 2 · Fotogramas de escenas icónicas con capítulo y minuto | ✅ | capturas de la wiki (S·, F·) y *storyboards* de 8 vídeos con minuto y `&t=` (§7, §14). Sólo 320×180 en los clips |
| 3 · Fan art y 3D con licencia | ✅ | 18 modelos de Sketchfab con licencia por API; fan art de Reddit y DeviantArt con autor (§11) |
| 4 · Fondos y sitios, luz, paleta, texturas | ✅ | 16 sitios con luz y hex medidos; texturas CC0 con enlace (§9) |
| 5 · Tipografía con tildes | ✅ | 20 letras comprobadas con fontTools (§5). Falta: la letra real de la ventana no es pública |
| 6 · Cómo hablan en pantalla | ✅ | la ventana del Sistema medida en 10 capturas, carteles latinos, pensamientos en cursiva, el móvil de la Asociación (§4) |
| 7 · Personajes y popularidad | ✅ | encuestas de MAL, Nlab, Dengeki, Crunchyroll, Anime!Anime! y Reddit (§3) |
| 8 · Doblaje latino, dos fuentes | ✅ | 21 personajes; 17 con dos fuentes. Frases textuales de 12 muestras de audio (§12). Falta: oír si dice «Surge» |
| 9 · Música | ✅ | OP, ED e inserciones con capítulo, confirmadas en la wiki (§13). Falta: oír el audio |
| 10 · Vídeos con minuto | ✅ | 21 vídeos comprobados; 8 mirados fotograma a fotograma (§14). Falta: TikTok |
| 11 · Videojuegos: interfaz y cajas | ⚠️ | fechas y formato confirmados; la interfaz no se pudo medir (Game UI Database y TCRF en 403) (§15) |
| 12 · Lo que ama el fandom y qué NO hacer | ✅ | Reddit por Arctic Shift, memes, chistes internos (§16-17) |
| 13 · Descripción profunda y forma de hablar | ✅ | carácter de la wiki y frases del doblaje por personaje (§6, §12.3) |
| 14 · Poses analizadas (6-10 por personaje) | ✅ | Jinwoo 14, Igris 9, Beru 6, Cha Hae-In 8, con minuto o número de hoja (§7) |
| 15 · Vestuario con hex | ✅ | medido en CV, renders y clips (§8) |
| 16 · Paisajes y fondos de pantalla con tamaño y autor | ✅ | visuales oficiales 1920×1080 y fondos de fans de DeviantArt con autor y tamaño (§10.1) |
| 17 · Guía para IA | ✅ | imagen: rasgos fijos, paleta medida, línea y luz medidas, palabras que ayudan y que estropean, qué hoja usar; texto: reglas de puntuación y trato, 10 frases reales del doblaje por emoción, vocabulario (§18). Falta: onomatopeyas (no las documenté) |
| 18 · Estilo de dibujo y técnica, y cómo replicarlo | ✅ | staff con fuente, regla del director (CBR, FandomWire), línea y color medidos con `estilo.py` en anime y webtoon, 2D + 3D y mocopi (VFX Voice, Anime Corner, Sony XYN), Photoshop y Blender paso a paso, encuadre por emoción (punto 18). Falta: el programa 2D del estudio y el nombre de sus filtros (sin fuente) |
| 19 · Texturas 2D | ✅ | no hay tramas (canmom.art); líneas de velocidad (uso comercial con atribución), grabado de metal CC0, tramas gratis de Clip Studio, grano de papel CC0; 5 emblemas mirados y medidos (punto 19). Falta: patrón de tela y emblema de la Asociación (no los encontré) |
| 20 · Gustos y detalles | ⚠️ | cumpleaños de Jinwoo y Cha Hae-In con dos fuentes; historia de Igris con tres; aficiones, manías y cómo se ven, casi todo de una fuente (wiki) (punto 20). Comidas y alturas oficiales: no las encontré; dos webs de fans dicen que no hay *databook* |
| 21 · Por qué la aman y la escena que hace llorar | ⚠️ | premios, 51 millones de votos, ventas y razones con fuente; la escena del ep. 21 vista en un fotograma, con reacciones de Reddit; gritar y reír con minuto (punto 21). Falta: **el minuto** de la escena del hospital y si suena «REVIVƎЯ» justo ahí (YouTube pide iniciar sesión) |
| 22 · Fan dubs y comunidad hispana | ⚠️ | 6 covers latinos de los openings y 1 meme de TikTok, comprobados por `oembed`; Antov y *The Dubbing Database* (punto 22). Falta: **las vistas** (no las da `oembed`), el enlace de @naruto_dominiicano y un fandub con grupo propio (no lo encontré) |
| 23 · Colaboraciones, figuras y cosplay | ✅ | Fortnite, *ARISE* × *Frieren*, Grand Summoners, exposición de Seúl, pop-up de Nueva York con dos o tres fuentes; Nendoroid oficial; 2 cosplays mirados con tamaño medido (punto 23). Una fuente: (G)I-DLE, OVERDRIVE, Seven Knights, el café de 2024. Falta: marcas de ropa o bebidas (no las encontré) |
| 24 · Obras parecidas y láminas vecinas | ✅ | AniList + 3 medios; cita de Chugong (CBR); obras relacionadas; biblias vecinas revisadas por su índice (punto 24). Falta: una entrevista de Chugong sobre sus influencias (sólo un blog) |
| 25 · Mundo, historia por arcos y símbolos | ✅ | el mundo en 5 líneas, 14 arcos del anime con episodios (wiki + Wikipedia), emblemas (punto 19), objetos icónicos y vocabulario latino (punto 25). Sin nombre latino comprobado: Arquitecto, Monarcas y Gobernantes, Red Gate, piedras de maná |
| 3 conceptos de lámina | ✅ | actualizados con las imágenes y los modelos nuevos (§20); el repaso añade el acabado del punto 18, el emblema de Ahjin, el modelo de Cha Hae-In, la historia de Igris y una lámina 2 con los 14 arcos |
| 40 fuentes distintas | ✅ | 436 enlaces de 111 sitios distintos, contados por `revisar.py` (antes del repaso: 336 de 76) |
| Tipos de fuente: oficiales | ✅ | Aniplex, web oficial, Crunchyroll, entrevista de Cocotame (Sony Music); en el repaso, Sony XYN, Kakao, Good Smile, Yen Press, la tienda de Fortnite y el X de *ARISE* |
| Tipos de fuente: otros idiomas | ✅ | japonés (Aniplex, Natalie, Cocotame; en el repaso ASCII.jp y eeo Media), coreano (namu.wiki, prensa, Korea Herald), vietnamita (subtítulos), francés (solo-leveling.fr) |
| Tipos de fuente: wikis, TV Tropes, TCRF, Wayback | ⚠️ | Fandom (la de la serie y la de *ARISE*), Doblaje Wiki, *The Dubbing Database* y Fandub Database sí; TV Tropes y TCRF en 403; Wayback respondió en el repaso, pero TV Tropes no tiene copia y la de namu.wiki da 403 |
| Tipos de fuente: foros | ✅ | Reddit por Arctic Shift |
| Tipos de fuente: arte (Pixiv, ArtStation, DeviantArt) | ⚠️ | DeviantArt sí (RSS), Safebooru y cosplays de Reddit con autor; Pixiv y ArtStation no se probaron |
| Tipos de fuente: vídeo con minuto | ✅ | YouTube por yt-dlp y *storyboards* |
| Tipos de fuente: código y recursos | ✅ | GitHub (subtítulos, fichas), Sketchfab, Poly Haven, ambientCG, Google Fonts; en el repaso, 3dtextures.me, CC0 Textures, Clip Studio Assets y myphotoshopbrushes |
| Tipos de fuente: doblaje latino | ✅ | Doblaje Wiki (API y audios), ANMTV, TVLaint, Infobae, IGN Latinoamérica |
| Hojas de contacto | ✅ | 3 hojas propias en `hojas/`, miradas, con tabla y enlaces (§10.0) |
| `referencias.json` (mínimo 20, sin máximo, medidas) | ✅ | 148 entradas, las mejores primero: las de las partes (`imagen.json`, `voz.json`, `texto.json`) y lo útil de `datos.json`. Todas las imágenes con ancho y alto medidos; sin tamaño sólo 3 vídeos con `&t=` y 3 páginas de pinceles y texturas. Fuera: el retrato del «Narrator» de AniList (sin tamaño) y 6 fan arts de Kim Dokja (es de otra obra) |

---

## Bitácora de búsqueda

### Primera pasada (24-sep-2026, red cerrada)

**Red:** `curl community.fandom.com` → 000 (403 del proxy). Respondían solo `raw.githubusercontent.com`, la API de GitLab, PyPI y el MCP de GitHub. WebFetch estaba bloqueado (Infobae y Wikipedia dieron EGRESS_BLOCKED).

**Búsquedas web (≈40, hasta agotar el cupo compartido de 200):**
- **Español:**
  - reparto latino de Solo Leveling; Beru, voz latina; «Levántate»/Arise en latino.
  - `doblaje.fandom.com` y `anmtvla.com` filtrados; Brandon Montor y Armando Guerrero.
  - J Balvin, qué personaje; Crunchyroll anuncia el reparto; «voz de Beru».
  - elenco T2 (Beru, Thomas Andre, Choi); Santos Alberto, Ixchel León y Jorge Badillo; elenco y staff en `crunchyroll.com`.
- **Inglés:**
  - KV de la T2; fuente de la ventana del Sistema; Hunter Association.
  - encuesta de popularidad; Anime Awards 2025; MAL, favoritos (y `myanimelist.net` filtrado).
  - Beru «My King»; wiki del Sistema y Daily Quest; «Congratulations on becoming a Player».
  - ARISE (UI y diálogo, reseñas, cómic webtoon); ARISE OVERDRIVE en Steam; fuente del logo; rotulación del webtoon.
  - dafont «Solo Level» y foro de dafont; voz de Beru en japonés e inglés; Reddit (dio error 400: dominio no accesible).
- **Japonés:** キービジュアル; 人気投票; ねとらぼ; 電撃 ランキング. Sin cupo para 澤野弘之 インタビュー ni 中重俊祐 インタビュー.
- **Coreano:** 인기투표; 개발자 인터뷰 (넷마블네오); 로고 폰트 / 말풍선.

**GitHub (búsqueda de código y archivos en bruto):**
- subtítulos: Netflix en inglés de la T1 ([foxofice/sub_share][nf12]), Crunchyroll en vietnamita de la T2 ([Senki3567/Drive][vi25]) y latinos de la T2 ([aymen-sh/tryme][es13]), con el dialecto comprobado por «ustedes», «oigan» y «miren»;
- fichas: ANN ([ToshY][ann-data1]), MAL por Jikan ([purplegummy][jkc1]) y AniList ([char-lib][anilist]); Wikipedia ([TruthScope][wp-txt]); música ([anisoncharts][anison]);
- web oficial ([anime-web-scraper][scraper]) y KV ([ACGNTaiwan][kv1]);
- modelos de Sketchfab ([codeonym][codeonym]); fuentes (`google/fonts`, comprobadas con fontTools).

**No encontré (primera pasada; revisado abajo):**
- el actor latino de Beru en dos fuentes;
- frases del audio latino;
- fan art con autor;
- interfaz del juego medida;
- entrevistas japonesas al staff sobre el Sistema (sin cupo);
- TV Tropes, TCRF y Wayback;
- hilos de Reddit;
- texturas concretas.


### Segunda pasada (24-sep-2026, red abierta)

**Herramientas y lo que dieron:**
- `investigar_serie.py` × 3 sobre `solo-leveling.fandom.com` (personajes, sitios, 25 episodios): 1613 imágenes, 36 hojas. Montaje propio de 3 hojas con Pillow (`hojas.py` en mi carpeta de trabajo).
- API de la wiki: texto de 30 páginas (System, Shadows, Igris, Cha Hae-In, Beru, Korean Hunters Association, Woo Jinchul, episodios 3, 12, 13, 16, 18, 19, 21, 24, 25, DARK ARIA, 4eVR, SHADOWBORN, UN-APEX, Solo Leveling: ARISE, Original Soundtracks…) y búsqueda de texto (`srwhat=text`) para las canciones.
- **Doblaje Wiki (API):** «Solo Leveling» y «Solo Leveling: Segundo despertar»; 60 muestras de audio listadas, 15 bajadas y transcritas con **faster-whisper** (modelo *small*, instalado en un entorno aparte de mi carpeta de trabajo).
- **yt-dlp** (cliente `mweb`): 21 vídeos con título, canal, fecha y visitas; búsquedas `ytsearch` en español, inglés y japonés («ノンクレジットオープニング»). Ningún vídeo tenía subtítulos. `fotogramas.py` falló («Sign in to confirm you're not a bot»); usé los *storyboards* (`sb.py`, en mi carpeta de trabajo).
- **Subtítulos de GitHub:** Netflix inglés T1 (12 episodios), Crunchyroll latino y en inglés de la T2 (ep. 13-22) y vietnamita de la T2 (ep. 23-25, por un clon parcial de `Senki3567/Drive`).
- **Sketchfab API:** 7 licencias comprobadas y 12 búsquedas («solo leveling», «igris», «crystal ball stand», «reception desk», «notice board cork», «magic portal», «ID card»…).
- **Poly Haven y ambientCG (API):** texturas CC0.
- **fontTools:** 12 letras de Google Fonts y «Solo Level» de dafont.
- **Arctic Shift:** la búsqueda por texto dio «Timeout»; por fechas (29-31 mar-2025, tras el final de la T2) sí respondió.
- **DeviantArt:** su RSS público (`backend.deviantart.com/rss.xml`) con «solo leveling igris» y «solo leveling wallpaper».
- **Webs que antes daban 403 y ahora no:** ANMTV (3 artículos), TVLaint, CBR, Cocotame.
- **Colores:** Pillow sobre capturas de la wiki, CV oficiales y *storyboards* (mediana o paleta por cuantización; se dice de cuál en cada hex).

**Búsquedas web (2 de ~50):**
- Español: «Solo Leveling doblaje latino Jinwoo "Levántate" o "Surge" frase Igris» → sólo un fandub y la marca «SURGE» de Crunchyroll LA.
- Japonés: «俺だけレベルアップな件 アニメ インタビュー システム画面 モーショングラフィックス 大城丈宗» → la entrevista de Cocotame a los productores (hablan de La Mole 2024 en México y de CCXP en Brasil); ninguna entrevista sobre el diseño de la ventana.

**Siguen cerrados o fallan:** Game UI Database, TV Tropes y The Cutting Room Floor (403 de Cloudflare); Wayback Machine (conexión cortada, 2 intentos); Bilibili (412); noticias de Crunchyroll (sólo JavaScript); descarga de vídeo y audio de YouTube.

**Los «no encontré» de la primera pasada, revisados:**
- el actor latino de Beru en dos fuentes → **encontrado** (Doblaje Wiki + MAL);
- frases del audio latino → **encontradas** (muestras de Doblaje Wiki);
- fan art con autor → **encontrado** (Reddit, DeviantArt);
- hilos de Reddit → **encontrados** (Arctic Shift);
- texturas concretas → **encontradas** (Poly Haven, ambientCG);
- interfaz del juego medida → sigue sin encontrar (403);
- entrevistas japonesas al staff sobre el Sistema → sigue sin encontrar: sólo la ficha (Production I.G hace los gráficos en movimiento) y la entrevista de producción;
- TV Tropes, TCRF y Wayback → siguen fallando.

**Marcas de duda:** había **55** al empezar. Quedan **36** con `grep` (31 de datos; 5 de la leyenda, el resumen del principio y la tabla de cumplimiento). Los que quedan son, sobre todo: datos con una sola fuente (grabación y mezcla de la T2, Esil, Iron), frases del doblaje sacadas por reconocimiento de voz, lo que no se pudo oír («Surge», la música), la interfaz del juego y las letras comerciales que citan los fans.

### Repaso corto: puntos 18-25 (24-sep-2026, noche)

Juntado de las bitácoras de `partes/imagen.md`, `partes/voz.md` y `partes/texto.md`. Cada investigador tenía su cupo de ~50 búsquedas web; ninguno lo agotó.

**Imagen (puntos 19 y 23)**
- **API de la wiki** (inglés): `srsearch` con *collaboration*, *emblem OR logo*, *Ahjin Guild*, *Hunters Association emblem seal*, *magic circle*, *hunter license card*; `imageinfo` de `Ahjin.png`, `Ah-Jin Logo Ch.141.PNG` e `Insignia Hunters.png` ([ficha de Ahjin.png](https://solo-leveling.fandom.com/wiki/File:Ahjin.png), [Hunters Guild](https://solo-leveling.fandom.com/wiki/Hunters_Guild)).
- **Búsquedas web** (inglés, 11): estilo de DUBU y Redice, técnica de color, pinceles de trama y de líneas de velocidad, papel CC0, tramas gratis de Clip Studio, grabado de metal CC0, colaboraciones de 2026, café y exposición en Corea, Fortnite, cruces de *ARISE*, cosplay.
- **Páginas leídas:** canmom.art (análisis entero), KoreaLore, Good Smile, IDC Games, Anime Corner. **ANN dio 403**: se usó el resumen del buscador.
- **Arctic Shift** (r/SoloLeveling): `title=cosplay` (15 posts) y `posts/ids` para sacar el tamaño real de las fotos.
- **Medido con curl y Pillow:** emblemas, visual de la exposición, imagen de la colaboración con *Frieren*, foto del Nendoroid y dos cosplays; la licencia del pack de líneas de velocidad (JSON-LD de su página) y el precio (0 $) de las tramas de Clip Studio.
- **No encontré:** entrevista técnica de DUBU o Redice; emblema propio de la Asociación de Cazadores; patrón de tela en la ropa; colaboraciones con marcas de ropa o bebidas (*Solo Leveling brand collaboration fashion*, *Solo Leveling 7-Eleven*).

**Voz y personajes (puntos 20, 21 y 22)**
- **API de Fandom, sin buscador:** wikitext de Jinwoo, Cha Hae-In, Igris, Beru, Yoo Jinho, el Sistema, Go Gunhee, Jinah y Park Kyung-Hye en la wiki de la serie; Jinwoo, Cha Hae-In, Igris y Beru en la del juego *ARISE* (Dossier, Secret File, Trivia; [Trivia de Cha Hae-In en *ARISE*](https://solo-leveling-arise.fandom.com/wiki/Cha_Hae-In#Trivia)); la ficha latina de *The Dubbing Database*; «Solo Leveling» en Fandub Database (sólo filipino e indonesio).
- **Búsquedas web:**
  - Inglés: fichas de personaje, cumpleaños, gustos, *databook*, historia de Igris, premios de Crunchyroll, ventas del webtoon, por qué la aman en Reddit, fandub y covers latinos, memes, Frikidoblaje, SakuraDubs, Kudasai Fandub, AS Fandub, @naruto_dominiicano.
  - Coreano: «성진우 좋아하는 음식 취미 프로필» (nada útil) y «나 혼자만 레벨업 크런치롤 어워드 수상 한국 애니메이션 최초» (prensa coreana).
  - Japonés: «俺だけレベルアップな件 クランチロール アワード 受賞 感想» (prensa japonesa).
- **Páginas leídas:** myanimeguru, readsololevelingmanga.us, DualShockers, Kakao, Atento a Música (español), eeo Media y ASCII.jp (japonés), CBR (Oricon), Sensor Tower. **natalie.mu dio 403.**
- **curl directo:** `oembed` de YouTube (6 covers y 2 vídeos) y de TikTok (1 de 2); Arctic Shift (posts con *cried* y *relatable*, y los comentarios del post 1j17hlz); el fotograma de ese post, **bajado y mirado**.
- **Bloqueados:** `yt-dlp` («Sign in to confirm you're not a bot», un intento por vídeo) y reddit.com (403).
- **No encontré:** comidas, cumpleaños y alturas oficiales de Igris, Beru, Jinho, Go Gunhee y el Sistema (campos vacíos en las dos wikis); el minuto de la escena del hospital; las vistas de covers y meme; un fandub latino con grupo propio.

**Texto, técnica y mundo (puntos 18, 24 y 25)**
- **API de la wiki:** `Story Arcs`, `Guilds`, `Class Ranks`, `Statue of God`, `Kamish's Wrath`, `Demon King's Longsword`, `Architect` e `imageinfo` de 9 insignias de gremio.
- **Búsquedas web** (la parte dice 9; lista 12):
  - Inglés: *making of* de A-1 (3DCG, *toon shader*, ventana del Sistema); entrevistas e influencias de Chugong; obras parecidas; TV Tropes; análisis de encuadres; aberración, grano y *bloom*; entrevista de Dubu; programas de A-1 (RETAS, Toon Boom, Clip Studio).
  - Japonés: «ソロレベリング アニメ 制作 インタビュー システムウィンドウ CG 監督» y «"Solo Leveling" anime director Nakashige interview 演出 カメラ 構図».
  - Coreano: «추공 인터뷰 나 혼자만 레벨업 영감 게임» (dos variantes).
- **Páginas leídas:** Sony XYN, Anime Corner, Awards Radar, VFX Voice, CBR (dos). **namu.wiki y TV Tropes dieron 403.**
- **Sketchfab API:** `q=solo leveling`, descargables (24 resultados), y licencia de 4 modelos.
- **Wayback Machine:** TV Tropes sin copia; namu.wiki con copia, pero 403 al leerla.
- **Medido y mirado:** el fotograma de Igris (ep. 11, 1366×768) y la viñeta del cap. 50 (574×778) con `estilo.py --colores 6`; 4 insignias en una hoja propia.
- **Biblias vecinas** revisadas por su índice (`seccion.py --indice`): One Piece, Attack on Titan, Jujutsu Kaisen, Demon Slayer, Naruto, My Hero Academia, One Punch Man y Frieren.
- **No encontré:** entrevista directa de Chugong sobre sus influencias (sólo el blog de solo-leveling.fr); entrevista de Dubu sobre su proceso; el programa 2D de A-1 y el nombre de sus filtros.

**Redactor**
- Leí las tres partes y pasé cada dato a su punto (18-25, después de §18). Los emblemas de gremio se miraron en una hoja propia (parte de texto y redactor): **se corrigieron los colores** que daba la parte de imagen (no llevan dorado).
- `referencias.json`: junté `imagen.json`, `voz.json`, `texto.json` y lo útil de `datos.json` (148 entradas). Dejé fuera el retrato de «Narrator» (sin tamaño) y 6 fan arts de Kim Dokja, que es de *Omniscient Reader's Viewpoint*.
- Las 3 hojas de `hojas/` siguen siendo las de la segunda pasada (§10.0).

---

## Fuentes

**436 enlaces distintos de 111 sitios** (143 de la primera pasada; 336 tras la segunda; el resto, del repaso de los puntos 18-25), citados arriba en cada dato. Aquí están sus direcciones: en la vista de lectura no se ven, pero en el editor sí.

[wp]: https://en.wikipedia.org/wiki/Solo_Leveling
[wp-s1]: https://en.wikipedia.org/wiki/Solo_Leveling_season_1
[wp-s2]: https://en.wikipedia.org/wiki/Solo_Leveling_season_2
[wp-txt]: https://raw.githubusercontent.com/hpeter11/TruthScope/main/backend/wikipedia_top_1000/378_Solo_Leveling.txt
[wp-awards]: https://en.wikipedia.org/wiki/9th_Crunchyroll_Anime_Awards
[ofi-story21]: https://sololeveling-anime.net/story/?id=21
[aniplex-kv2]: https://www.aniplex.co.jp/lineup/sololeveling/news/detail/?id=66194
[natalie-kv1]: https://natalie.mu/comic/news/517533
[animate]: https://animatetimes.com/news/details.php?id=1694327065
[x-kv2]: https://x.com/sololeveling_pr/status/1835520942203867271
[collabo]: https://collabo-cafe.com/events/collabo/sololeveling-anime2024-add-info-pv-kv/
[ann-kv2]: https://www.animenewsnetwork.com/news/2024-09-15/solo-leveling-season-2-arise-from-the-shadow-anime-reveals-new-visual-january-2025-premiere/.215573
[ann-jeju]: https://www.animenewsnetwork.com/news/2025-03-04/solo-leveling-season-2-arise-from-the-shadow-anime-trailer-previews-jeju-island-raid-arc/.221929
[kiba-vis]: https://anitrendz.net/news/2025/02/08/solo-leveling-season-2-highlights-the-powerful-kiba-in-new-shadow-visual/
[kaisel-vis]: https://anitrendz.net/news/2025/03/01/kaisel-takes-flight-in-new-solo-leveling-season-2-shadow-visual/
[fandompost]: https://www.fandompost.com/2025/01/12/solo-leveling-season-2-arise-from-the-shadow-anime-reveals-new-key-visual/
[concept22]: https://sportskeeda.com/anime/news-solo-leveling-anime-reveals-release-window-brand-new-concept-art-aniplex-online-fest-2022
[logo-svg]: https://commons.wikimedia.org/wiki/File:Solo_Leveling_anime_logo.svg
[ann-data1]: https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/main/encyclopedia/anime/26000.json
[ann-data2]: https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/main/encyclopedia/anime/32617.json
[jk1]: https://raw.githubusercontent.com/purplegummy/RecommenAnime/main/data/jikan/anime_52299_full.json
[jk2]: https://raw.githubusercontent.com/purplegummy/RecommenAnime/main/data/jikan/anime_58567_full.json
[jkc1]: https://raw.githubusercontent.com/purplegummy/RecommenAnime/main/data/jikan/anime_52299_characters.json
[jkc2]: https://raw.githubusercontent.com/purplegummy/RecommenAnime/main/data/jikan/anime_58567_characters.json
[mal-top]: https://raw.githubusercontent.com/yiren54610/project_5/main/top_1000_mal_characters_scraped.csv
[anilist]: https://raw.githubusercontent.com/LyeZinho/char-lib/main/data/manga/solo-leveling/characters.json
[anison]: https://raw.githubusercontent.com/anisoncharts/anisoncharts.github.io/master/anime/ore-dake-level-up-na-ken.html
[scraper]: https://raw.githubusercontent.com/tetrix1993/anime-web-scraper/master/anime/anime_2024_1.py
[kv1]: https://raw.githubusercontent.com/ACGNTaiwan/Anime-List/master/anime-data/img/2024/01/653e88f1476224423d4a73a1fcdf67cebd2b6dcccbdcc69ab4eafecdacfac46f.png
[kv2]: https://raw.githubusercontent.com/ACGNTaiwan/Anime-List/master/anime-data/img/2025/01/a75ede5e839f28fc879bfd8d16edebb958775c00c608b107e8a9516498de617b.jpg
[nf01]: https://raw.githubusercontent.com/foxofice/sub_share/master/subs_list/animation/2024/%282024.1.6%29%E6%88%91%E7%8B%AC%E8%87%AA%E5%8D%87%E7%BA%A7%20S1/BD/Netflix/en/Ore%20dake%20Level%20Up%20na%20Ken%20-01.Netflix.en.srt
[nf03]: https://raw.githubusercontent.com/foxofice/sub_share/master/subs_list/animation/2024/%282024.1.6%29%E6%88%91%E7%8B%AC%E8%87%AA%E5%8D%87%E7%BA%A7%20S1/BD/Netflix/en/Ore%20dake%20Level%20Up%20na%20Ken%20-03.Netflix.en.srt
[nf06]: https://raw.githubusercontent.com/foxofice/sub_share/master/subs_list/animation/2024/%282024.1.6%29%E6%88%91%E7%8B%AC%E8%87%AA%E5%8D%87%E7%BA%A7%20S1/BD/Netflix/en/Ore%20dake%20Level%20Up%20na%20Ken%20-06.Netflix.en.srt
[nf07]: https://raw.githubusercontent.com/foxofice/sub_share/master/subs_list/animation/2024/%282024.1.6%29%E6%88%91%E7%8B%AC%E8%87%AA%E5%8D%87%E7%BA%A7%20S1/BD/Netflix/en/Ore%20dake%20Level%20Up%20na%20Ken%20-07.Netflix.en.srt
[nf11]: https://raw.githubusercontent.com/foxofice/sub_share/master/subs_list/animation/2024/%282024.1.6%29%E6%88%91%E7%8B%AC%E8%87%AA%E5%8D%87%E7%BA%A7%20S1/BD/Netflix/en/Ore%20dake%20Level%20Up%20na%20Ken%20-11.Netflix.en.srt
[nf12]: https://raw.githubusercontent.com/foxofice/sub_share/master/subs_list/animation/2024/%282024.1.6%29%E6%88%91%E7%8B%AC%E8%87%AA%E5%8D%87%E7%BA%A7%20S1/BD/Netflix/en/Ore%20dake%20Level%20Up%20na%20Ken%20-12.Netflix.en.srt
[vi20]: https://raw.githubusercontent.com/Senki3567/Drive/main/Crunchyroll/Solo%20Leveling/Solo%20Leveling%20Season%202%20-Arise%20from%20the%20Shadow-/20%20-%20Looking%20Up%20Was%20Tiring%20Me%20Out.vi-VN.ass
[vi25]: https://raw.githubusercontent.com/Senki3567/Drive/main/Crunchyroll/Solo%20Leveling/Solo%20Leveling%20Season%202%20-Arise%20from%20the%20Shadow-/25%20-%20On%20to%20the%20Next%20Target.vi-VN.ass
[es13]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd1sp.vtt
[es14]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd2sp.vtt
[es15]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd3sp.vtt
[es16]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd4sp.vtt
[es17]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd5sp.vttt
[es18]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd6sp.vtt
[es19]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd7sp.vtt
[es20]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd8sp.vtt
[es21]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd9sp.vtt
[es22]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd10sp.vtt
[en14]: https://raw.githubusercontent.com/aymen-sh/tryme/main/SLd2en.vtt
[codeonym]: https://raw.githubusercontent.com/codeonym/portfolio/main/scripts/assets/README.md
[sk-igris]: https://sketchfab.com/3d-models/igris-solo-leveling-0eeb4795c56d4a5cbca69ba2bd340c6a
[sk-throne]: https://sketchfab.com/3d-models/throne-room-247c37e6a9694ae891398911876f0c14
[sk-lectern]: https://sketchfab.com/3d-models/stone-book-lectern-821ec86f606a40f5b819bafc3ad013d4
[sk-chest]: https://sketchfab.com/3d-models/old-roman-style-treasure-chest-animated-a4f29fc04137433e8eb5470ddb75d311
[sk-coins]: https://sketchfab.com/3d-models/pile-of-coins-3-8c7efafa0470436688b67c90a5b423fb
[sk-sword]: https://sketchfab.com/3d-models/sword-of-the-defeated-224a05d7ec8e4d1b990545128055d865
[sk-sung]: https://sketchfab.com/3d-models/b477120b0c8642e9b94a7c347362dd75
[gf-lato]: https://raw.githubusercontent.com/google/fonts/main/ofl/lato/METADATA.pb
[gf-nunito]: https://raw.githubusercontent.com/google/fonts/main/ofl/nunito/METADATA.pb
[gf-exo2]: https://raw.githubusercontent.com/google/fonts/main/ofl/exo2/METADATA.pb
[gf-oxanium]: https://raw.githubusercontent.com/google/fonts/main/ofl/oxanium/METADATA.pb
[gf-cinzel]: https://raw.githubusercontent.com/google/fonts/main/ofl/cinzel/METADATA.pb
[gf-varela]: https://raw.githubusercontent.com/google/fonts/main/ofl/varelaround/METADATA.pb
[gf-notokr]: https://raw.githubusercontent.com/google/fonts/main/ofl/notosanskr/METADATA.pb
[gf-bhs]: https://raw.githubusercontent.com/google/fonts/main/ofl/blackhansans/METADATA.pb
[fontbolt]: https://www.fontbolt.com/font/solo-leveling-font/
[ffv]: https://freefontsvault.com/solo-leveling-font/
[designbeep]: https://designbeep.com/2025/10/29/solo-leveling-font/
[dafont-sololevel]: https://www.dafont.com/solo-level.font
[1001]: https://www.1001fonts.com/solo-level-demo-font.html
[figma]: https://www.figma.com/community/file/1480447290080535122/solo-leveling
[dribbble]: https://dribbble.com/shots/25916934-Solo-Leveling-UI-Concept-Figma-Design
[behance]: https://www.behance.net/search/projects/solo%20leveling%20ui
[ffx-theme]: https://addons.mozilla.org/en-US/firefox/addon/leveling-theme/
[gh-digi]: https://github.com/digishivam/sololevelingsystemui
[gh-kean]: https://github.com/keanteng/solo-leveling
[habitforge]: https://habitforge.io/solo-leveling-app/
[notion]: https://www.notion.com/templates/solo-leveling-system-turn-your-life-into-an-rpg-with-notio
[wiki-system]: https://solo-leveling.fandom.com/wiki/System
[wiki-prep]: https://solo-leveling.fandom.com/wiki/The_Preparation_To_Become_Powerful
[wiki-penaltyq]: https://solo-leveling.fandom.com/wiki/Penalty_Quest
[wiki-kha]: https://solo-leveling.fandom.com/wiki/Korean_Hunters_Association
[epic]: https://epicstream.com/article/what-is-solo-leveling-daily-quest-sung-jin-woo-workout
[comicbook]: https://comicbook.com/anime/news/solo-leveling-jinwoo-training-real-life/
[kovo]: https://www.kovofitness.com/blog/solo-leveling-workout
[tt-daily]: https://www.tiktok.com/@michaelh_h2o/video/7332164626043604270
[tt-king]: https://www.tiktok.com/discover/tf-you-mean-whos-my-king-solo-leveling-meme
[tt-despierten]: https://www.tiktok.com/@miichelland_o/video/7489656761176132869
[expo1]: https://trip-cut.blogspot.com/2026/01/solo-leveling-exhibition-seoul-2026.html
[expo2]: https://www.trip.com/travel-guide/attraction/seoul/solo-leveling-exhibition-153983053/
[dw]: https://doblaje.fandom.com/es/wiki/Solo_Leveling
[dw-selim]: https://doblaje.fandom.com/es/wiki/Erick_Selim
[anmtv-24]: https://www.anmtvla.com/2024/01/solo-leveling-crunchyroll-anuncia-la.html
[anmtv-t2]: https://www.anmtvla.com/2025/01/solo-leveling-surge-desde-las-sombras.html
[anmtv-balvin]: https://www.anmtvla.com/2025/02/solo-leveling-surge-desde-las-sombras.html
[tvlaint25]: https://www.tvlaint.com/2025/01/crunchyroll-confirma-la-fecha-de.html
[tvlaint24]: https://www.tvlaint.com/2024/01/crunchyroll-revela-el-trailer-y-reparto.html
[wdnes]: https://www.wdnes.com/2024/01/este-es-el-elenco-del-doblaje-latino-de.html
[infobae-fm]: https://www.infobae.com/malditos-nerds/2024/12/11/entrevistamos-a-fernando-moctezuma-actor-de-doblaje-de-solo-leveling/
[infobae-sh]: https://www.infobae.com/malditos-nerds/2025/02/14/solo-leveling-temporada-2-conversamos-con-sofia-huerta-voz-de-chae-hae-in-y-directora-de-doblaje/
[cr-elenco25]: https://www.crunchyroll.com/es/news/announcements/2025/1/24/elenco-staff-doblaje-latino-solo-leveling-2-arise-from-the-shadow
[cr-e13]: https://www.crunchyroll.com/watch/GEVUW3W5G/you-arent-e-rank-are-you
[sdp]: https://www.sdpnoticias.com/geek/j-balvin-presta-su-voz-al-doblaje-en-espanol-latino-de-solo-leveling/
[excelsior]: https://www.excelsior.com.mx/funcion/j-balvin-sera-actor-doblaje-solo-leveling-anime/1698424
[sopitas]: https://www.sopitas.com/cine-y-tv/entrevista-j-balvin-solo-leveling/
[ign-latam]: https://www.youtube.com/watch?v=9v9Y5hK6SWs
[voces]: https://www.youtube.com/watch?v=LRy-ClfLQ_k
[yt-clip6]: https://www.youtube.com/watch?v=Vzyw9z9F57M
[yt-react]: https://www.youtube.com/watch?v=ypDDBqRB02U
[yt-od]: https://www.youtube.com/watch?v=K4aM0pBmcrk
[yt-tr1]: https://www.youtube.com/watch?v=1kQwjK4rGYg
[yt-tr2]: https://www.youtube.com/watch?v=GDMXGzjJzS4
[animecorner]: https://animecorner.me/akira-ishida-joins-solo-leveling-voice-cast-as-ant-king-beru/
[dengeki-vote]: https://dengekionline.com/articles/224920/
[dengeki-res]: https://dengekionline.com/article/202404/2389
[nlab-res]: https://nlab.itmedia.co.jp/research/articles/2517411/
[cbr-cha]: https://www.cbr.com/solo-leveling-cha-hae-in-top-ranking-miss/
[dualshockers]: https://www.dualshockers.com/solo-leveling-best-characters/
[kakao]: https://newsroom.kakaoent.com/news/solo-leveling-wins-top-honor-at-crunchyroll-anime-awards-2025/
[thr]: https://www.hollywoodreporter.com/tv/tv-news/2025-crunchyroll-anime-awards-winners-list-1236230002/
[goldderby]: https://www.goldderby.com/tv/2025/2025-crunchyroll-anime-awards-complete-winners-list-solo-leveling/
[inquirer]: https://entertainment.inquirer.net/611907/crunchyroll-anime-awards-2025-solo-leveling-emerges-as-biggest-winner
[namu-beru]: https://namu.wiki/w/%EB%B2%A0%EB%A5%B4(%EB%82%98%20%ED%98%BC%EC%9E%90%EB%A7%8C%20%EB%A0%88%EB%B2%A8%EC%97%85)
[namu-eval]: https://namu.wiki/w/%EB%82%98%20%ED%98%BC%EC%9E%90%EB%A7%8C%20%EB%A0%88%EB%B2%A8%EC%97%85/%EC%95%A0%EB%8B%88%EB%A9%94%EC%9D%B4%EC%85%98/%ED%8F%89%EA%B0%80
[valuenews]: https://www.thevaluenews.co.kr/news/183014
[nate]: https://news.nate.com/view/20240505n03346
[gamemeca]: https://www.gamemeca.com/view.php?gid=1762612
[nm-site]: https://sololeveling.netmarble.com/en
[gplay]: https://play.google.com/store/apps/details?id=com.netmarble.sololv
[nm-ui]: https://forum.netmarble.com/slv_en/view/21/74407
[silic]: https://www.siliconera.com/review-solo-leveling-arise-presentation-impresses/
[sk-review]: https://www.sportskeeda.com/esports/solo-leveling-arise-review
[cbr-review]: https://www.cbr.com/solo-leveling-arise-review/
[steam]: https://store.steampowered.com/app/2373990/Solo_Leveling_ARISE_OVERDRIVE/
[steam-news]: https://store.steampowered.com/news/app/2373990/view/594039665469686060
[pcgamer]: https://www.pcgamer.com/games/action/solo-leveling-arise-overdrive-release-date-times/
[imdb-ep12]: https://m.imdb.com/news/ni65188174
[rslm-beru]: https://readsololevelingmanga.us/beru-solo-leveling/
[spk-igris]: https://www.sportskeeda.com/anime/a-1-pictures-treatment-igris-proves-beru-solo-leveling-season-2-will-break-the-internet
[sk-beru]: https://www.sportskeeda.com/anime/a-1-pictures-surpasses-manhwa-beru-s-design-solo-leveling-season-2
[arata2]: https://arata.lat/el-doblaje-en-espanol-de-solo-leveling-surge-desde-las-sombras-estrena-su-temporada-2-en-crunchyroll/
[droidetv]: https://www.droidetv.com/post/solo-leveling-surge-desde-las-sombras-temporada-2-con-doblaje-en-espa%C3%B1ol-en-crunchyroll
[wiki-ep3]: https://solo-leveling.fandom.com/wiki/Episode_3

**Enlaces añadidos en la segunda pasada:**

[dw-film]: https://doblaje.fandom.com/es/wiki/Solo_Leveling:_Segundo_despertar
[dw-baek]: https://static.wikia.nocookie.net/doblaje/images/0/0b/Baek_Yoonho_%28Audio%29_Solo_Leveling.ogg
[dw-beru-sombra]: https://static.wikia.nocookie.net/doblaje/images/5/57/Beru_%28Sombra%29_%28Audio%29_Solo_Leveling.ogg
[dw-beru-trans]: https://static.wikia.nocookie.net/doblaje/images/e/ed/Beru_%28Transformaci%C3%B3n%29_%28Audio%29_Solo_Leveling.ogg
[dw-cha]: https://static.wikia.nocookie.net/doblaje/images/9/96/Cha_Hae-In_%28Audio%29_Solo_Leveling.ogg
[dw-chiyul]: https://static.wikia.nocookie.net/doblaje/images/f/f3/Song_Chiyul_%28Audio%29_Solo_Leveling.ogg
[dw-choi]: https://static.wikia.nocookie.net/doblaje/images/7/7b/Choi_Jong-In_%28Audio%29_Solo_Leveling.ogg
[dw-gunhee]: https://static.wikia.nocookie.net/doblaje/images/3/3d/Go_Gunhee_%28Audio%29_Solo_Leveling.ogg
[dw-jinah]: https://static.wikia.nocookie.net/doblaje/images/5/5b/Sung_Jinah_%28Audio%29_Solo_Leveling.ogg
[dw-jinchul]: https://static.wikia.nocookie.net/doblaje/images/0/0d/Woo_Jinchul_%28Audio%29_Solo_Leveling.ogg
[dw-jinho]: https://static.wikia.nocookie.net/doblaje/images/b/bf/Yoo_Jinho_%28Audio%29_Solo_Leveling.ogg
[dw-jinwoo-b]: https://static.wikia.nocookie.net/doblaje/images/0/08/Sung_Jinwoo_%28Rango_B%29_%28Audio%29_Solo_Leveling.ogg
[dw-jinwoo-e]: https://static.wikia.nocookie.net/doblaje/images/2/27/Sung_Jinwoo_%28Rango_E%29_%28Audio%29_Solo_Leveling.ogg
[wiki-shadows]: https://solo-leveling.fandom.com/wiki/Shadows
[wiki-igris]: https://solo-leveling.fandom.com/wiki/Igris
[wiki-cha]: https://solo-leveling.fandom.com/wiki/Cha_Hae-In
[wiki-jinchul]: https://solo-leveling.fandom.com/wiki/Woo_Jinchul
[wiki-arise]: https://solo-leveling.fandom.com/wiki/Solo_Leveling:_ARISE
[wiki-darkaria]: https://solo-leveling.fandom.com/wiki/DARK_ARIA
[wiki-4evr]: https://solo-leveling.fandom.com/wiki/4eVR
[wiki-shadowborn]: https://solo-leveling.fandom.com/wiki/SHADOWBORN
[wiki-ep21]: https://solo-leveling.fandom.com/wiki/Episode_21
[wiki-ost]: https://solo-leveling.fandom.com/wiki/Original_Soundtracks
[wiki-aleks]: https://solo-leveling.fandom.com/wiki/File:Aleks_Le_Sung_Jinwoo%27s_English_voice_actor%27s_signature_and_drawing.webp
[w-p001]: https://static.wikia.nocookie.net/solo-leveling/images/a/a9/Igris_2.jpg
[w-p002]: https://static.wikia.nocookie.net/solo-leveling/images/6/6d/Igris_1.jpg
[w-p003]: https://static.wikia.nocookie.net/solo-leveling/images/2/23/Season_2_anime_Sung_Jinwoo_illustration.jpg
[w-p250]: https://static.wikia.nocookie.net/solo-leveling/images/d/de/Anime_Episode_12_Jinwoo_extracts_Igris_shadow.png
[w-p262]: https://static.wikia.nocookie.net/solo-leveling/images/3/34/Anime_Episode_1_Screenshot_1.png
[w-e593]: https://static.wikia.nocookie.net/solo-leveling/images/e/e4/Solo_Leveling_Anime_Episode_19_Img_1.jpg
[w-o188]: https://static.wikia.nocookie.net/solo-leveling/images/0/0e/Anime_Season_2_large_visual_1.png
[w-o262]: https://static.wikia.nocookie.net/solo-leveling/images/4/47/Anime_Season_1_Large_Visual_2.jpg
[nf05]: https://raw.githubusercontent.com/foxofice/sub_share/master/subs_list/animation/2024/%282024.1.6%29%E6%88%91%E7%8B%AC%E8%87%AA%E5%8D%87%E7%BA%A7%20S1/BD/Netflix/en/Ore%20dake%20Level%20Up%20na%20Ken%20-05.Netflix.en.srt
[nf08]: https://raw.githubusercontent.com/foxofice/sub_share/master/subs_list/animation/2024/%282024.1.6%29%E6%88%91%E7%8B%AC%E8%87%AA%E5%8D%87%E7%BA%A7%20S1/BD/Netflix/en/Ore%20dake%20Level%20Up%20na%20Ken%20-08.Netflix.en.srt
[vi24]: https://raw.githubusercontent.com/Senki3567/Drive/main/Crunchyroll/Solo%20Leveling/Solo%20Leveling%20Season%202%20-Arise%20from%20the%20Shadow-/24%20-%20Are%20You%20the%20King%20of%20Humans.vi-VN.ass
[sk-igrishall]: https://sketchfab.com/3d-models/a3ac78d429f04340937af8e365f4de32
[sk-igris2]: https://sketchfab.com/3d-models/98c049a047da440b80a45f29f574dc09
[sk-igrissword]: https://sketchfab.com/3d-models/a915a103299a4613b2235b548a90f81f
[sk-igrisboss]: https://sketchfab.com/3d-models/ec6c37cb8d31456ea7acaf1a443a73aa
[sk-cha]: https://sketchfab.com/3d-models/b07a938c74a84bfe8caab58a97e3b305
[sk-dagger]: https://sketchfab.com/3d-models/bae21ff0300b43b494a9629f048e2f50
[sk-shadowdagger]: https://sketchfab.com/3d-models/104847cbdc2b469687893443a6d12552
[sk-crystal]: https://sketchfab.com/3d-models/30618a3f909a4376af013a1d1de1cbba
[sk-desk]: https://sketchfab.com/3d-models/d23cfdf8128345d7b886ebb9affad2e8
[sk-idcard]: https://sketchfab.com/3d-models/5addf1256a404b7a82c380bb2d22f186
[sk-board]: https://sketchfab.com/3d-models/4e2609119dfa478d8b0337b049050d7c
[sk-portal]: https://sketchfab.com/3d-models/50f5030139de4d94a5adcfe90c0ba1ac
[ph-api]: https://api.polyhaven.com/assets?t=textures
[acg-api]: https://ambientcg.com/api/v2/full_json?type=Material&q=Cork
[acg-cork]: https://ambientcg.com/a/Cork004
[as-sl]: https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=sololeveling&after=2025-03-29&before=2025-03-31&limit=100
[rd-richyuki]: https://www.reddit.com/r/sololeveling/comments/1jni1q7/
[rd-shadows]: https://i.redd.it/lgiu97zbuure1.jpeg
[rd-kanno]: https://i.redd.it/flyseada0ure1.jpeg
[x-richyuki]: https://x.com/RichyukiYuki/status/1906344318106792372
[da-favorisxp]: https://www.deviantart.com/favorisxp/art/Solo-Leveling-%28Sung-Jin-Woo%29-Animated-Wallpaper-1182239456
[da-renacars]: https://www.deviantart.com/renacars/art/Wallpaper-%28Solo-Leveling%29-1280965951
[da-antractos]: https://www.deviantart.com/antractos/art/Solo-Leveling%3A-Sung-Jinwoo-Cold-Mask-Wallpaper-1362311417
[da-wespion]: https://www.deviantart.com/wespion9/art/Son-Jin-Woo-and-Igris---Solo-Leveling-1368144060
[cocotame]: https://cocotame.jp/series/109911/
[yt-beyond]: https://www.youtube.com/watch?v=J4XD23c8Of8
[variety-beyond]: https://variety.com/2026/film/news/solo-leveling-movie-beyond-the-system-in-production-1236801606/
[yt-bts]: https://www.youtube.com/watch?v=eagTHK8pMBs
[yt-fm-infobae]: https://www.youtube.com/watch?v=UB85ukGDcVA
[yt-fm-pratz]: https://www.youtube.com/watch?v=PkoPI1GVY-c
[yt-leyenda]: https://www.youtube.com/watch?v=kiK2C0PwDcw
[yt-tr-es-2023]: https://www.youtube.com/watch?v=Kjta12rmtkA
[yt-op1-aniplex]: https://www.youtube.com/watch?v=9KBl_UurkEc
[yt-op2-aniplex]: https://www.youtube.com/watch?v=sgnYEfM7U2U
[yt-op1]: https://www.youtube.com/watch?v=XqD0oCHLIF8
[yt-op1-1]: https://www.youtube.com/watch?v=XqD0oCHLIF8&t=1
[yt-op1-5]: https://www.youtube.com/watch?v=XqD0oCHLIF8&t=5
[yt-op1-9]: https://www.youtube.com/watch?v=XqD0oCHLIF8&t=9
[yt-op1-11]: https://www.youtube.com/watch?v=XqD0oCHLIF8&t=11
[yt-op1-25]: https://www.youtube.com/watch?v=XqD0oCHLIF8&t=25
[yt-op1-43]: https://www.youtube.com/watch?v=XqD0oCHLIF8&t=43
[yt-op1-54]: https://www.youtube.com/watch?v=XqD0oCHLIF8&t=54
[yt-op1-66]: https://www.youtube.com/watch?v=XqD0oCHLIF8&t=66
[yt-op1-82]: https://www.youtube.com/watch?v=XqD0oCHLIF8&t=82
[yt-op1-84]: https://www.youtube.com/watch?v=XqD0oCHLIF8&t=84
[yt-ed2]: https://www.youtube.com/watch?v=KxeHOxO3A3I
[yt-ed2-5]: https://www.youtube.com/watch?v=KxeHOxO3A3I&t=5
[yt-ed2-11]: https://www.youtube.com/watch?v=KxeHOxO3A3I&t=11
[yt-ed2-17]: https://www.youtube.com/watch?v=KxeHOxO3A3I&t=17
[yt-ed2-37]: https://www.youtube.com/watch?v=KxeHOxO3A3I&t=37
[yt-ed2-47]: https://www.youtube.com/watch?v=KxeHOxO3A3I&t=47
[yt-ed2-84]: https://www.youtube.com/watch?v=KxeHOxO3A3I&t=84
[yt-trailer]: https://www.youtube.com/watch?v=dR7DW4ykE8k
[yt-trailer-3]: https://www.youtube.com/watch?v=dR7DW4ykE8k&t=3
[yt-trailer-31]: https://www.youtube.com/watch?v=dR7DW4ykE8k&t=31
[yt-trailer-39]: https://www.youtube.com/watch?v=dR7DW4ykE8k&t=39
[yt-trailer-58]: https://www.youtube.com/watch?v=dR7DW4ykE8k&t=58
[yt-trailer-70]: https://www.youtube.com/watch?v=dR7DW4ykE8k&t=70
[yt-trailer-89]: https://www.youtube.com/watch?v=dR7DW4ykE8k&t=89
[yt-trailer-129]: https://www.youtube.com/watch?v=dR7DW4ykE8k&t=129
[yt-clip6-7]: https://www.youtube.com/watch?v=Vzyw9z9F57M&t=7
[yt-clip6-21]: https://www.youtube.com/watch?v=Vzyw9z9F57M&t=21
[yt-clip6-25]: https://www.youtube.com/watch?v=Vzyw9z9F57M&t=25
[yt-clip6-27]: https://www.youtube.com/watch?v=Vzyw9z9F57M&t=27
[yt-clip6-46]: https://www.youtube.com/watch?v=Vzyw9z9F57M&t=46
[yt-clip6-66]: https://www.youtube.com/watch?v=Vzyw9z9F57M&t=66
[yt-papu]: https://www.youtube.com/watch?v=Zk5Xz1dR6bY
[yt-papu-1]: https://www.youtube.com/watch?v=Zk5Xz1dR6bY&t=1
[yt-papu-3]: https://www.youtube.com/watch?v=Zk5Xz1dR6bY&t=3
[yt-papu-11]: https://www.youtube.com/watch?v=Zk5Xz1dR6bY&t=11
[yt-papu-27]: https://www.youtube.com/watch?v=Zk5Xz1dR6bY&t=27
[yt-papu-55]: https://www.youtube.com/watch?v=Zk5Xz1dR6bY&t=55
[yt-papu-89]: https://www.youtube.com/watch?v=Zk5Xz1dR6bY&t=89
[yt-papu-91]: https://www.youtube.com/watch?v=Zk5Xz1dR6bY&t=91
[yt-templo]: https://www.youtube.com/watch?v=-O5dX2OdHl0
[yt-templo-3]: https://www.youtube.com/watch?v=-O5dX2OdHl0&t=3
[yt-templo-7]: https://www.youtube.com/watch?v=-O5dX2OdHl0&t=7
[yt-templo-37]: https://www.youtube.com/watch?v=-O5dX2OdHl0&t=37
[yt-templo-79]: https://www.youtube.com/watch?v=-O5dX2OdHl0&t=79
[yt-ant]: https://www.youtube.com/watch?v=W2PxXsVM_pY
[yt-ant-19]: https://www.youtube.com/watch?v=W2PxXsVM_pY&t=19
[yt-ant-98]: https://www.youtube.com/watch?v=W2PxXsVM_pY&t=98
[yt-ant-157]: https://www.youtube.com/watch?v=W2PxXsVM_pY&t=157
[yt-ant-196]: https://www.youtube.com/watch?v=W2PxXsVM_pY&t=196
[yt-ant-492]: https://www.youtube.com/watch?v=W2PxXsVM_pY&t=492
[yt-ant-551]: https://www.youtube.com/watch?v=W2PxXsVM_pY&t=551
[yt-eresfuerte]: https://www.youtube.com/watch?v=ZHlnSNDpvQs
[yt-eresfuerte-17]: https://www.youtube.com/watch?v=ZHlnSNDpvQs&t=17
[yt-eresfuerte-53]: https://www.youtube.com/watch?v=ZHlnSNDpvQs&t=53
[yt-react-80]: https://www.youtube.com/watch?v=ypDDBqRB02U&t=80
[yt-react-444]: https://www.youtube.com/watch?v=ypDDBqRB02U&t=444
