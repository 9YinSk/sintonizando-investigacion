---
tags: [biblia, serie, laminas, biblioteca]
serie: "Jujutsu Kaisen (呪術廻戦)"
canal: "sin canal: propuesta ➕ CREAR SALA (SALAS PROPIAS) y 🍟 General (LA SALA)"
fecha: 2026-09-24
---

# Biblia · Jujutsu Kaisen — para la biblioteca

> [!important] Cómo se hizo, y sus límites
> La hicieron **dos ayudantes seguidos**. El primero escribió §2-§13 y
> §15-§17 y montó las 3 hojas; el límite de uso lo cortó y **su carpeta
> de trabajo se perdió** (vídeos, fotogramas, subtítulos y su registro
> de búsquedas). El segundo (24-sep-2026) **volvió a mirar** 10 vídeos
> con `herramientas/fotogramas.py` (§12.0), comprobó en ellos los
> minutos del primero, añadió lo nuevo (la caja de diálogo del modo
> historia de *Cursed Clash*, el lobby en línea, la pantalla en blanco
> de Gojo, las poses de Sukuna y Panda, las muestras de voz latinas de
> Doblaje Wiki pasadas por Whisper) y escribió §0, §1, §14, §18-§21 y
> `referencias.json`. YouTube no deja bajar vídeos ni subtítulos desde
> este contenedor («confirma que no eres un bot»): los vídeos se
> miraron en copias de **Dailymotion** del mismo montaje, a 512×288.
> Minutos de episodio: subtítulos japoneses con tiempos (±5 s).
> Un **3.er ayudante** (24-sep) repasó y resolvió ⚠️: las tres imágenes
> #N sin nombre, el signo del dominio de Sukuna, 6 poses más de Todo, el
> premio de 2021 en dos fuentes y el tráiler de *Ejecución* con el logo
> en español (§21.5).

## Índice

0. Jujutsu Kaisen no tiene canal: dónde encaja mejor
1. Resumen para quien tenga prisa
2. Las escenas que sirven (con minuto)
3. Arte oficial y hojas de contacto
4. Fan art y 3D (sólo como referencia)
5. Sitios, luz, paleta y texturas
6. Tipografía
7. Cómo hablan y piensan en pantalla (el cuadro de diálogo)
8. Los personajes
9. ¿Quién es el más querido?
10. Doblaje latino
11. Música
12. Vídeos
13. Videojuegos de la franquicia
14. Lo que ama el fandom, y qué NO hacer
15. Poses analizadas por personaje
16. Vestuario
17. Paisajes y fondos de pantalla
18. Guía para generar con IA
19. Tres conceptos de lámina
20. Lo que no pude verificar
- Cumplimiento del encargo
21. Bitácora de búsqueda

---

## 0 · Jujutsu Kaisen no tiene canal: dónde encaja mejor

El encargo dice que JJK está en la **biblioteca**: es un fenómeno, pero
no tiene canal. Miré `servidor/inventario.md` y lo que proponen las
biblias 01-34 (`grep '^canal:' biblias/*/biblia.md`, 24-sep-2026).

**La clave de JJK para este servidor**: su gran idea es la
**Expansión de Dominio** (領域展開). Gojo la explica así en T1-7:
«**construyes a tu alrededor tu propio espacio**, con tu técnica
dentro» («術式を付与した生得領域を呪力で周囲に構築する», 12:08 ✅
subtítulo) y «cuando hay dos dominios a la vez, **manda el más
cuidado**» (13:57-14:09 ✅). Y la serie tiene un segundo invento que
**abre un espacio aparte**: el **velo** (帳, *tobari*), una cúpula
negra que cae del cielo, esconde lo de dentro y **se puede configurar**
(quién entra y quién no) ✅ ([wiki, «Curtain»](https://jujutsu-kaisen.fandom.com/wiki/Curtain),
y Ijichi lo baja en T1-4, 4:32 ✅ subtítulo). Es, con otras palabras,
lo que hace **➕・CREAR SALA**: entras y se abre **tu** sala.

El tercer tema es **la voz**: Inumaki manda con la voz, **con megáfono,
por teléfono y hasta grabado** en una grabadora ✅ (§8).

### La propuesta, de un vistazo

| # | Canal | Por qué | Personaje | Estado del canal |
|---|---|---|---|---|
| **1** | **➕・CREAR SALA** (SALAS PROPIAS, voz) | la **Expansión de Dominio** es «tu espacio, tus reglas»; el **velo** es «cerrar la sala» | **Gojo** (1.º en la 4.ª encuesta oficial, con más del doble de votos que el 2.º) | **libre** ✅: ninguna biblia lo propone (grep de «CREAR SALA» y «Crear sala» en `biblias/`) |
| **2** | **🍟・General** (LA SALA, voz) | Inumaki **sólo habla con ingredientes de onigiri** y Panda lo traduce: la sala donde se habla de lo que sea | **Inumaki** (4.º en la 1.ª encuesta) con **Panda** | casi libre: la biblia 30 (Naruto) la nombra sólo **de reserva** |
| 3 | 🎙️・Grabación (idea, sin concepto) | la voz de Inumaki **grabada sigue funcionando** (manga, cap. 262 ✅ wiki) | Inumaki | la biblia 29 la da a Monsters, Inc. |

Del inventario (textos reales):

> **➕・CREAR SALA** (voz), sección **SALAS PROPIAS**. **No tiene
> descripción** en el inventario.

> **🍟・General** (voz), sección **LA SALA**. **Sin descripción**. Su
> vecino de texto, **#general**: «_La plaza: aquí se habla de lo que sea.
> Del oficio se habla en general-doblaje; tu voz grabada va a demos._»

### Los textos de ➕ CREAR SALA (propuesta: no tiene descripción)

⚠️ **Confírmalos con el dueño**: no sé qué bot crea las salas ni qué deja
cambiar. Lo normal en Discord es «entras y se crea tu sala; al vaciarse,
se borra», pero **no lo comprobé** en este servidor.

| # | Texto | Idea |
|---|---|---|
| 1 | **Crear sala** | nombre |
| 2 | **Entra aquí y se abre tu propia sala** | qué es |
| 3 | **Es tuya: ponle nombre** | qué puedes hacer |
| 4 | **Tú decides quién entra** | las reglas |
| 5 | **Cuando se vacía, desaparece** | cómo se cierra |
| 6 | Frase de Gojo, en su voz (§19) | gancho |

**Lámina 2** (concepto B, §19): si el bot tiene comandos (límite,
candado, ocultar, echar), cada uno en un **talismán** del velo.

### Los textos de 🍟 General (propuesta: no tiene descripción)

| # | Texto | Idea |
|---|---|---|
| 1 | **General** | nombre |
| 2 | **La sala de voz de la plaza** | qué es |
| 3 | **Entra y habla de lo que sea** | qué va aquí |
| 4 | **Saluda al entrar** | la costumbre |
| 5 | **Del oficio se habla en general-doblaje** | a dónde va lo otro |
| 6 | El gag de Inumaki y Panda (§19, concepto C) | gancho |

### Las que descarté, y por qué

| Canal | Por qué no |
|---|---|
| #general-doblaje, 🎙️ Grabación | encajan con Inumaki (la voz, el jarabe para la garganta), pero **ya los propone** la biblia 29 (Monsters, Inc.) |
| #memes | JJK tiene memes enormes («Nah, I'd win»), pero #memes es de JoJo (biblia 28) |
| 🔊 Aula | Gojo profesor encaja, pero la propone Demon Slayer (biblia 31) |
| #reglas | Sukuna y los «votos vinculantes» darían reglas, pero #reglas es de Attack on Titan (biblia 02) |

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Qué es | Manga de **Gege Akutami** en la *Weekly Shōnen Jump*, del **5-mar-2018 al 30-sep-2024**, **30 tomos** ✅ ([ficha de la wiki](https://jujutsu-kaisen.fandom.com/wiki/Jujutsu_Kaisen) + portada del tomo 30, #22). Anime de **MAPPA**: T1 dirigida por **Sunghoo Park**, T2 y T3 por **Shōta Goshozono**; guion **Hiroshi Seko**; diseño **Tadashi Hiramatsu** ✅ (wiki + créditos del tráiler 1, 0:16-0:28, visto). **59 episodios** en 3 temporadas (T3: 9-ene a 27-mar-2026) y la peli *Jujutsu Kaisen 0* ✅ |
| Tono | **Oscuro**: maldiciones nacidas del miedo de la gente, sangre, Tokio de noche. Pero con **mucha comedia** entre combates (Gojo payaso, Todo, Panda, los Juju-Cortos). Una lámina puede ser **de día** (la escuela en el monte, el aula) sin traicionar el tono |
| Por qué CREAR SALA | La **Expansión de Dominio** es «construir tu propio espacio a tu alrededor» (T1-7, 12:08 ✅) y Gojo **la enseña en una «clase extra»** («課外授業», T1-7, 9:19 ✅) |
| El objeto | La **pizarra del aula** de la Escuela de Tokio, con tiza y el **puntero** de Gojo. Es el formato oficial «Gojo explica» del juego *Cursed Clash* (tráiler «Special Lecture», 0:18 y 3:22, **visto**). Se hace en Blender en una tarde (pizarra CC BY en Sketchfab, §4) |
| El más querido | **Gojo** en la 4.ª encuesta oficial (2024, 113.392 votos, más del doble que Yuji) ✅. Pero **Megumi** ganó la 2.ª y la 3.ª, y **Yuji** la 1.ª. Para un servidor de voz, el secundario clave es **Inumaki** (4.º en la 1.ª) ✅ (§9) |
| Quién habla en la lámina | CREAR SALA: **Gojo** con puntero. 🍟 General: **Inumaki** (que sólo dice «¡Alga kombu!») y **Panda** traduciendo |
| Cuadro de diálogo propio | **No es un globo blanco**. JJK habla con: **título de episodio en Mincho blanca abajo a la derecha**; **hora y lugar** igual («22:20 井之頭線 渋谷駅»); **técnicas en vertical entre 「」**; la **pizarra de tiza** del «Special Lecture»; y en el modo historia de *Cursed Clash*, **dos viñetas de anime con el borde roto** sobre **tinta azul petróleo** `#314953` y el texto en blanco al lado (tráiler, 3:09, **visto**). Ver §7 |
| Letras | **Shippori Mincho B1** (títulos), **Dela Gothic One** (técnicas), **Zen Antique** (diálogo), **Yuji Syuku** (talismanes): todas con tildes, ñ, ¿ y ¡ comprobadas con fontTools. **Ojo**: la letra del generador de logos «estilo JJK» tiene las tildes **vacías** (§6) |
| Voz latina | Yuji **Enzo Fortuny**, Gojo **Pepe Vilchis**, Megumi **Víctor Ruiz**, Nobara **Ayari Rivera**, Sukuna **Osvaldo Trejo** (T1) y **Alfredo Gabriel Basurto** (T2), Inumaki **Ángel Rodríguez**, Nanami **Carlos Hernández** ✅ (dos fuentes cada uno). Audiomaster Candiani; dirección **Patricia Acevedo** (T1) y **Octavio Campos** (T2-T3) (§10) |
| Juegos | ***Cursed Clash*** (2024, Bandai Namco; textos en español de Hispanoamérica) y ***Phantom Parade*** (móvil 2023; Steam 2026) ✅ (§13) |
| Lo que NO hacer | Gojo sin venda **y** sin gafas en una lámina «amable» (los ojos se reservan para el golpe fuerte); spoilers (Nanami, Nobara, Gojo en Shinjuku); globos blancos; Sukuna de guía simpático (§14) |

## 2 · Las escenas que sirven (con minuto)

**Cómo se numera.** «T1-7» = temporada 1, episodio 7. La T1 son los
episodios 1-24; la T2 (Gojo del pasado + Shibuya), los 25-47; la T3
(Juego del Sacrificio, 1.ª parte), los 48-59 ✅ (Doblaje Wiki: 59
episodios; la T3 tiene 7 + 5). «JJK0» = la película *Jujutsu Kaisen 0*.

**De dónde salen los minutos.** De los **subtítulos japoneses con
tiempos** del espejo de kitsunekko en GitHub (T1: Erai-raws, versión
web; T2: Judas; JJK0: Netflix). Son minutos del episodio, ±5 s según
la versión. La traducción al español es mía, salvo donde digo «doblaje»
o «sub. oficial».

### 2.1 Las diez escenas que todo fan reconoce

| # | Escena | Dónde | Minuto | Lo que se oye (japonés → español) | Sirve para |
|---|---|---|---|---|---|
| 1 | El abuelo de Yuji, en el hospital | T1-1 | 10:52 | «お前は強いから人を助けろ» → «Tú eres fuerte. Ayuda a la gente». Y en 11:07: «Muere rodeado de mucha gente» | el porqué de Yuji ✅ |
| 2 | Yuji se come el dedo de Sukuna | T1-1 | ~21:10 | «両面宿儺の指 特級呪物だぞ» (Megumi, 21:53: «¡Es el dedo de Sukuna, un objeto de grado especial!») | el giro del episodio 1 ✅ |
| 3 | Gojo se presenta ante Sukuna | T1-2 | 1:29 | «大丈夫 僕 最強だから» → «Tranquilo. Soy el más fuerte» | presentar a Gojo ✅ |
| 4 | Nobara llega a Tokio | T1-3 | 3:06 | «釘崎野薔薇 喜べ男子 紅一点よ» → «Nobara Kugisaki. Alégrense, chicos: soy la única chica» | presentar a Nobara ✅ |
| 5 | La **Expansión de Dominio** de Gojo contra Jogo | T1-7 | 14:25-14:30 | «領域展開… 無量空処» → «Expansión de Dominio… Vacío Infinito» | la escena más famosa del anime ✅ |
| 6 | Todo: «¿Qué tipo de chica te gusta?» | T1-8 | 5:54 | «答えろ伏黒 どんな女がタイプだ？» | el meme de Todo ✅ |
| 7 | Nanami: «trabajar es un asco» | T1-9 | 8:49 | «労働はクソということです» | el meme de Nanami ✅ |
| 8 | Nanami se quita la corbata: **horas extra** | T1-10 | 21:12 | «時間外労働です» → «Esto ya son horas extra» | Nanami en acción ✅ |
| 9 | **Destello Negro** y «Congratulations, brother» | T1-19 | 12:25 y 15:57 | «黒閃！» / «コングラチュレーション ブラザー» | Yuji y Todo, celebrar ✅ |
| 10 | Gojo despierta: «En el cielo y en la tierra, sólo yo soy el honrado» | T2-4 (ep. 28) | 16:54 y 17:44 | «天上天下 唯我独尊» / «虚式 茈» → «Técnica Imaginaria: Púrpura» | Gojo joven, el meme ✅ |

### 2.2 Más escenas con minuto

| Escena | Dónde | Minuto | Para qué |
|---|---|---|---|
| Megumi: «Salvo a la gente de forma injusta» («俺は不平等に人を助ける») | T1-5 | 9:50 | la voz de Megumi |
| Gojo: «Te voy a enseñar la Expansión de Dominio» («領域展開について教えてあげる») | T1-7 | 9:22 | **Gojo profesor** |
| Inumaki: «¿Atún con mayonesa?» Megumi explica: «su vocabulario son sólo ingredientes de onigiri» | T1-5 | 16:48 y 17:06 | presentar a Inumaki |
| Kamo explica el **Habla Maldita**: «el poder va en el sonido» («呪言は言霊 音に呪力を乗せる») | T1-17 | 7:42 | **la voz como técnica** |
| «A mi senpai se le rompió la garganta» («先輩の喉が潰れた») | T1-19 | 2:08 | Inumaki, voz dañada |
| JJK0: Yuta ve a Inumaki comprar **jarabe para la garganta** («のど薬？») | JJK0 | 35:39 | el objeto de Inumaki |
| JJK0: Ijichi baja el **velo**: «では“帳”を下ろします» | JJK0 | 35:52 | el velo que crea un espacio |
| JJK0: «¡Revienta!» y después: «¡Tiene la voz destrozada!… Ah, por eso el jarabe» | JJK0 | 37:07-37:26 | Inumaki, cuidar la voz |
| Inumaki en Shibuya, **con megáfono**: se oye el **acople** («ハウリング») y luego «¡No se muevan!» («動くな») | T2-13 (ep. 37) | 0:46-1:03 | el megáfono ✅ (subtítulo con tiempos) |
| Geto a Gojo: «¿Eres el más fuerte porque eres Satoru Gojo, o eres Satoru Gojo porque eres el más fuerte?» | T2-5 (ep. 29) | 16:56 | el meme |
| Gojo abre su dominio en Shibuya (0,2 s) | T2-9 (ep. 33) | 14:43 | Gojo en Shibuya |
| Sukuna: «Santuario Malévolo» («伏魔御廚子») | T2-17 (ep. 41) | 15:08 | Sukuna |
| Nanami a Yuji: «Lo demás te lo dejo a ti» («後は頼みます») | T2-18 (ep. 42) | 13:30 | la escena que hizo llorar al fandom |
| Nobara: «No estuvo tan mal» («悪くなかった») | T2-19 (ep. 43) | 21:24 | Nobara |
| Todo: «Y mi hermano, Yuji Itadori» («そして マイブラザー 虎杖悠仁») | T1-24 | 22:02 | cierre de la T1 |
| Ijichi: «Bajo el velo» («帳を下ろします») y el conjuro «闇よりいでて闇より黒く その穢れを禊ぎ祓え» («Sal de la oscuridad, más negro que la oscuridad; purifica lo impuro») | T1-4 | 4:32-4:39 | **cerrar la sala** ✅ (sub. con tiempos, 2.º ayudante) |
| Yuji: «¡Se está haciendo de noche!» Megumi: «Es un velo. Como hay casas cerca… una barrera que nos esconde de fuera» | T1-4 | 4:47-4:54 | explicar el velo ✅ |
| Gojo: «Nos vamos, Yuji. **Clase extra** (課外授業). La cumbre del combate de hechicería: te voy a enseñar la Expansión de Dominio» | T1-7 | 9:16-9:27 | **Gojo profesor**, concepto A ✅ |
| Gojo: «**Esto es una Expansión de Dominio**. Con energía maldita construyes a tu alrededor tu dominio interior, con tu técnica dentro» | T1-7 | 12:05-12:08 | la definición de «crear sala» ✅ |
| Gojo: «Contra un dominio, lo más eficaz es **desplegar el tuyo**. Si hay dos a la vez, **manda la técnica más refinada**. Aunque también cuentan la afinidad y la energía» | T1-7 | 13:57-14:13 | lámina 2 ✅ |

### 2.3 Lo que VI en los fotogramas (no sólo leído)

Detalle en §12. Lo más útil para la lámina:

- **Gojo profesor**, en el juego *Cursed Clash*: delante de una
  **pizarra verde oscura con un puntero**, «Special Lecture», y la tiza
  escribe «Cursed Energy Is the Key to Battle» (tráiler, 0:18-0:24 y
  1:24). Es **la forma oficial de «Gojo explica algo»**.
- **La celda de los talismanes**: Yuji encadenado en una sala llena de
  **ofuda de papel** y **farolillos hexagonales** amarillos; Gojo
  **sentado al revés en una silla**, con los brazos colgando por el
  respaldo y la venda (clip doblado, 0:08-0:47; es el final de T1-1 /
  principio de T1-2; lo **volví a mirar**: [0:49](https://www.dailymotion.com/video/x7xmacu?start=49)).
- **La caja de diálogo del modo historia** de *Cursed Clash* (nuevo):
  **dos viñetas de anime con el borde roto**, en diagonal, sobre una
  mancha de **tinta azul petróleo**, y el texto blanco al lado de cada
  una (tráiler «Special Lecture», [3:09](https://www.dailymotion.com/video/x8scngs?start=189)).
- **Gojo y la pantalla en blanco** (nuevo): Gojo con el puntero junto a
  una **pantalla de proyección enrollable vacía**, en un aula de madera
  ([3:22](https://www.dailymotion.com/video/x8scngs?start=202)). Es el hueco
  perfecto para los textos de una lámina.
- **El ending 1** («LOST IN PARADISE»): cada personaje **sale por una
  puerta** con ropa de calle, sobre un color plano: Yuji en turquesa,
  Megumi en amarillo, Nobara en rojo, Gojo en gris (0:10-0:58).
- **El hanami del opening 1**: todos de picnic bajo los cerezos; Gojo
  tumbado, Panda, Nanami con gafas, Todo sin camisa (1:16).
- **El cartel «定員未達» (Not Enough Members)**: pincel negro enorme con
  un tachón rojo, en el club de ocultismo (T1-1; clip doblado, 0:19).

## 3 · Arte oficial y hojas de contacto

### 3.0 Lo que bajé y miré ✅

- `herramientas/investigar_serie.py` sobre la **Jujutsu Kaisen Wiki**
  (`jujutsu-kaisen.fandom.com`, comprobada: responde y tiene las
  páginas) con 19 páginas (Yuji, Gojo, Megumi, Nobara, Sukuna, Nanami,
  Maki, Inumaki, Panda, Yuta, Geto, Todo, Toji, Mahito, la escuela, el
  anime, el manga, JJK0 y Shibuya): **3.367 imágenes enlazadas, 2.658
  grandes, 56 hojas** en `herramientas/referencias/jujutsu-kaisen/`
  (no se sube). Miré las hojas 1-3 (las más grandes) y busqué el resto
  por título en `indice.json`.
- **«#N»** en esta biblia = número en ese `indice.json`. Con él se baja
  el original: `python herramientas/investigar_serie.py --bajar jujutsu-kaisen N`.
- Bajé 67 originales para montar **mis tres hojas** y medir colores.
- ⚠️ **Aviso del 2.º ayudante**: ese `indice.json` **se perdió** con la
  carpeta de trabajo. Lo rehíce con las mismas 19 páginas (24-sep: 3.424
  imágenes enlazadas, 2.717 grandes; la wiki ha crecido) y **los números
  ya no coinciden** a partir del #23. Así que **«#N» es sólo una
  etiqueta**: para bajar el original, busca el **nombre del archivo**
  (tabla de abajo, medidos por la API) o mira `referencias.json`.

| #N | Archivo en la wiki | Tamaño |
|---|---|---|
| 1 | `Satoru Gojo (Prequel Anime).png` | 2886×5255 |
| 3 | `Sukuna (JUMP 38-2023).png` | 3277×3736 |
| 6 | `Anime Key Visual 9-10.png` | 4096×2895 |
| 7 | `Hidden inventory premature death stage play art by gege akutami.png` | 2892×4096 |
| 9 | `Maki Zenin Anime Concept Art.png` | 4032×2729 |
| 11 | `Megumi Fushiguro Anime Concept Art.png` | 3860×2687 |
| 15 | `Toge Inumaki Anime Concept Art.png` | 3802×2630 |
| 18 | `Nikkei Entertainment! November 2025.png` | 2740×3508 |
| 19 | `Nobara Kugisaki Anime Concept Art.png` | 3736×2566 |
| 20 | `Yuji Itadori Anime Concept Art.png` | 3680×2493 |
| 22 | `Yuji Itadori (Volume 30).png` | 2598×3450 |
| 31 | `Yuta Okkotsu and Cursed Rika.png` | 2296×2914 |
| 37 | `Anime Key Visual 2.png` | 2024×2867 |
| 64 | `Anime Key Visual.png` | 2000×2829 |
| 71 | `Megumi Fushiguro.png` | 2074×2640 |
| 78 | `Jujutsu Kaisen Cursed Clash Key Visual.png` | 1930×2739 |
| 82 | `BD & DVD Volume 9 Cover.png` | 1876×2680 |
| 87 | `Nobara Kugisaki.png` | 1847×2633 |
| 95 | `Give it back Limited Cover.png` | 2247×2000 |
| 99 | `Jujutsu High Big 3.png` | 1860×2266 |
| 106 | `Playful Cloud (Anime).png` | 1920×2067 |
| 115 | `Nobara introduces herself (Anime).png` | 1920×1934 |
| 123 | `Sukuna annoyed by Yuji's switch (Anime).png` | 1960×1815 |
| 132-136 | `Phantom Parade <Personaje> Artwork.png` | 2465×1376 |
| 141 | `Kento Nanami (Volume 11).png` | 1600×2062 |
| 297 | `Kento Nanami Anime Concept Art.png` | 1807×1293 |
| 303 | `Aoi Todo (Anime).png` | 985×2252 |
| 503 | `Tour of Tokyo (Anime).png` | 1920×1080 |
| 637 | `Jujutsu students realize they forgot about the curtain (Anime).png` | 1920×1080 |
| 817 | `School Celebration (Ao no Sumika).png` | 1920×1080 |
| 834 | `Shibuya Station Exit 13 (Anime).png` | 1920×1080 |
| 857 | `Sukuna's fingers (Anime).png` | 1920×1080 |
| 906 | `Shibuya Mark City (Anime).png` | 1920×1080 |
| 961 | `Shibuya Station Inokashira Line Gate (Anime).png` | 1920×1080 |
| 1177 | `Tokyo Jujutsu High dorms (Anime).png` | 1920×1080 |
| 1178 | `Tokyo Jujutsu High landscape (Anime).png` | 1920×1080 |
| 1180 | `Tokyo Metropolitan Jujutsu Technical School (Anime).png` (vista aérea; 3.er ayudante) | 1920×1080 |
| 139 | `Yuji and Megumi's school uniforms (Anime).png` (3.er ayudante) | 1920×1750 |
| 1085 | `Aoi Todo calls Yuji his best friend (Anime).png` (3.er ayudante) | 1920×1080 |
| 1540 | `Yuta's Jujutsu High ID (Anime).png` | 1920×803 |
| 1579 | `Geto summons a curtain over Jujutsu High (Anime).png` | 1920×803 |
| 1277 | `Jujutsu Kaisen Phantom Parade Key Visual (Cleaned).png` | 1919×1079 |
| P29 | `Toge's Cough Syrup (Anime).png` | 1920×803 |
| P30 | `Toge Inumaki with a megaphone.png` | 457×519 |
| F29 | `Toge Inumaki in class (Anime).png` | 1920×803 |

(Emparejados por tamaño exacto y por lo que se ve en las hojas; los de
1920×1080, por título. #139, #1085 y #1180 los encontró el 3.er
ayudante (24-sep): los bajó por la API y los **comparó a ojo** con las
celdas P27, P20 y F2. Son la misma imagen ✅.)

### 3.1 Las tres hojas de esta carpeta (`hojas/`)

**`personajes_01.jpg`** (30 celdas, P1-P30). Las que más sirven:

| Celda | Qué es | Para qué |
|---|---|---|
| **P1** | Gojo, hoja de modelo del anime de JJK0 (#1, 2886×5255), **mano abierta hacia delante** | presentar a Gojo; la pose de «alto, aquí mando yo» |
| **P2** | Gojo con **doble «V» de la paz** abrazando a Yuji (portada *Nikkei Entertainment!*, nov-2025, #18) | celebrar, saludar |
| **P3** | Gojo **se sube las gafas redondas** con las dos manos, fondo cian (BD vol. 9, #82) | pose de «mira esto»; cara pícara |
| P4-P7 | Gojo, Yuji (Phantom Parade), Yuji tomo 30 (manos en rezo), arte conceptual de Yuji | acción y caras |
| **P8** | Megumi haciendo el **perro con las manos** (#71) | el gesto de Megumi |
| P9, P11, P21 | **arte conceptual del anime** de Megumi, Nobara y Maki: **hojas de expresiones** | caras: enfado, risa, cansancio |
| **P10** | Nobara con **martillo y clavos** (#87) | presentar a Nobara |
| **P12** | Nobara **mano en la cadera**, uniforme con falda, calle de Tokio (T1-3, #115) | presentar, regañar |
| P13-P14 | Sukuna (JUMP) y **Sukuna en la cara de Yuji** (#123) | Sukuna |
| **P15** | Nanami **tapándose la boca**, reloj y corbata de leopardo (tomo 11, #141) | pensar, «qué fastidio» |
| P16-P17 | Nanami en Phantom Parade y arte conceptual | Nanami en acción |
| **P18** | Inumaki, arte conceptual: **cuello subido**, gestos de «pulgar arriba» y ojos | Inumaki |
| P19-P20 | Todo con camiseta morada; Todo **sonríe como a un hermano** (#1085) | Todo |
| P22 | Maki con la **Nube Juguetona** en la playa (#106) | Maki |
| P24 | Gojo y Geto jóvenes, arte de **Gege Akutami** sobre amarillo (#7) | los del pasado |
| P25 | Portada de «give it back» (ED2): los tres **con abrigos de invierno** (#95) | ropa de calle |
| **P27** | Yuji y Megumi **sentados en una valla**, uniformes (#139) | poses relajadas |
| **P29** | Inumaki enseña el **espray para la garganta** (JJK0) | el objeto de Inumaki |
| **P30** | Inumaki **saltando con un megáfono** y la «V» (manga) | Inumaki con megáfono |

**`fondos_objetos_01.jpg`** (30 celdas, F1-F30):

| Celda | Qué es | Para qué |
|---|---|---|
| **F1-F3** | la **Escuela de Tokio**: templos de madera en el monte, la **vista aérea** del complejo (pagoda, edificio central de madera, pista de atletismo) y los dormitorios (#1178, #1180, #1177) | fondo de día, «la casa» |
| F4 | almacén maldito, de noche (#1176) | fondo oscuro |
| **F5** | el «paseo por Tokio» en estilo **cómico chibi** con «東京» grande (#503) | el tono de las escenas de risa |
| F6 | los de 1.er año **de compras** (#445) | calle de día |
| **F7-F11** | **Shibuya**: cruce de noche, salida 13, Mark City, torniquetes del Inokashira, calle vacía al atardecer | el sitio real de la T2 |
| F12-F13 | Okinawa; **aula con pizarra** decorada (festival escolar, #817) | fondo de aula |
| F14-F16 | key visuals de la T1, 17 (rojo con ventana) y 9-10 | estilo de póster |
| **F17** | **los dedos de Sukuna** (#857) | objeto |
| **F18** | el **Reino de la Prisión**, un cubo (#648) | objeto |
| F19 | **credencial de estudiante** de Yuta (#1540) | objeto de «ficha» |
| **F20-F21** | el **velo** (帳): el gag de «se nos olvidó bajarlo» (#637) y Geto bajándolo sobre la escuela (#1579) | el concepto de «crear sala» |
| F22 | Yuji se come el dedo (#578) | escena |
| **F23** | la **celda de ofuda y farolillos**, vista desde arriba (clip, 0:45) | sitio para una lámina |
| **F24** | **Gojo ante la pizarra** (Cursed Clash) | «Gojo explica» |
| **F25** | el **hanami** del opening 1 | todos juntos |
| F26, F30 | ED1: Nobara y Gojo **saliendo por su puerta** | ropa de calle, color plano |
| F27 | el Vacío Infinito (T1-7) | el dominio |
| F28 | estación de Shibuya con **Hachikō** (PV) | sitio real |
| **F29** | **aula de la escuela** con ventanas de madera (JJK0) | fondo de aula |

**`pantalla_y_letras_01.jpg`** (30 celdas, T1-T22 y L1-L8): cómo se
escribe en pantalla y las letras libres probadas. Explicada en §6 y §7.

### 3.2 Arte oficial grande, para la pose (no para pegar)

Todo © Gege Akutami / Shueisha / JUJUTSU KAISEN Project, alojado en la
wiki. Tamaños medidos por la API (`imageinfo`).

| # | Qué es | Tamaño | Enlace |
|---|---|---|---|
| 1 | Gojo, hoja de modelo (JJK0) | 2886×5255 | [png](https://static.wikia.nocookie.net/jujutsu-kaisen/images/f/f3/Satoru_Gojo_%28Prequel_Anime%29.png) |
| 64 | Key visual de la T1 | 2000×2829 | en `indice.json` |
| 6 | Key visual 9-10 (Gojo del pasado + Shibuya) | 4096×2895 | en `indice.json` |
| 20 | Yuji, arte conceptual del anime | 3680×2493 | en `indice.json` |
| 11 | Megumi, arte conceptual | 3860×2687 | en `indice.json` |
| 19 | Nobara, arte conceptual | 3736×2566 | en `indice.json` |
| 15 | Inumaki, arte conceptual | 3802×2630 | en `indice.json` |
| 297 | Nanami, arte conceptual | 1807×1293 | en `indice.json` |
| 78 | Key visual de *Cursed Clash* | 1930×2739 | en `indice.json` |
| 132-136 | Arte de *Phantom Parade* (Yuji, Gojo, Megumi, Nobara, Nanami) | 2465×1376 | en `indice.json` |

(Las URL exactas de las 30 mejores, en `referencias.json`.)

### 3.3 Qué NO usar como arte

- **Las páginas del manga** (T13-T18): sirven para ver **cómo se
  rotulan** las técnicas, no para recortar personajes (blanco y negro,
  otra línea).
- **Las celdas de 320×180** (sacadas de hojas de vídeo): sólo para
  mirar pose y luz.
- **Wallpapers de fans** (§17): referencia, nunca pegar.

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D en Sketchfab (licencia leída en la API) ✅

Búsquedas con `downloadable=true` en la [API de Sketchfab](https://api.sketchfab.com/v3/search?type=models&q=megaphone&downloadable=true).
**CC Attribution** = se puede usar citando al autor. **NC** = no comercial.

| Objeto | Modelo | Autor | Licencia | Enlace |
|---|---|---|---|---|
| **Megáfono** (Inumaki) | «Megáfono / Megaphone» | cuadot | CC BY | [modelo](https://sketchfab.com/3d-models/c7852e2237f24728b45ef842b078ec1b) |
| Megáfono | «Megaphone» | 321Blender | CC BY | [modelo](https://sketchfab.com/3d-models/2b28e57e7f594b3d87d7d52db04ce43b) |
| **Espray / jarabe** (Inumaki) | «Cough Syrup» | zeeldee | CC BY | [modelo](https://sketchfab.com/3d-models/542aa2118bac4521bcefcf6305a3b4c0) |
| Frasco (alternativa) | «Simple Medicine Bottle» | EthanfromEngland | CC BY | [modelo](https://sketchfab.com/3d-models/c5c360e292be4e8fb957991bbfff3a1a) |
| **Dedo de Sukuna** | «Sukuna Finger» | henriquebbarcellos | CC BY | [modelo](https://sketchfab.com/3d-models/7b052eddf63a4716995ff59381f1667b) |
| Dedo de Sukuna | «Sukuna's finger» | asouza | **CC BY-NC-ND** (no modificar) | [modelo](https://sketchfab.com/3d-models/0094c76440e3447a900797ede9bad5bf) |
| **Reino de la Prisión** (cubo) | «Prison Realm \| Jujutsu Kaisen» | NexusB | CC BY | [modelo](https://sketchfab.com/3d-models/64b2d10cdf6d41cea6a9d7ff4bb5930d) |
| **Santuario Malévolo** | «Malevolent Shrine \| Jujutsu Kaisen» | NexusB | CC BY | [modelo](https://sketchfab.com/3d-models/efcf94d9cf03434db7b0978144b500b6) |
| Gafas de Nanami | «Kento Nanami's Glasses» | lxhdwf | CC BY | [modelo](https://sketchfab.com/3d-models/394afa70469e4ee4b733014c564987ec) |
| **Farolillo japonés** (la celda) | «Japanese Paper Lantern» | WIsEman_Tavern | CC BY | [modelo](https://sketchfab.com/3d-models/f993239d99304992aef9701af1f31a3c) |
| **Pizarra** (Gojo) | «Chalkboard» | hellfa | CC BY | [modelo](https://sketchfab.com/3d-models/84c2350e2e54442ea4b7066014759e97) |
| **Pantalla de proyección** (Gojo, *Cursed Clash* 3:22) | «Projector Screen (Low Poly)» | filththemutt | CC BY | [modelo](https://sketchfab.com/3d-models/ad904b77975c44a98a4c33d78a1d5c2b) ✅ API, 24-sep |
| **Aula japonesa** | «The Japanese School Classroom» | volvor | CC BY | [modelo](https://sketchfab.com/3d-models/d9fc039ba0b6433db91ec129abe86b52) |
| **Onigiri** (Inumaki) | «Onigiri - midpoly» | Pierre.Bourdon | CC BY | [modelo](https://sketchfab.com/3d-models/e7db392d6d3a4664becaea75c17e972a) |
| Calle japonesa de noche | «Japanese street at night» | afx_cgmotion | CC BY | [modelo](https://sketchfab.com/3d-models/fb1bdcd71a5544d699379d2d13dd1171) |

**Crédito exacto** para la lámina (CC BY): «"<nombre>" de <autor>,
Sketchfab, CC BY 4.0». No encontré modelos libres de **talismanes
ofuda** ni de **grabadora de voz** con el tema de JJK: se hacen con un
plano y una textura de papel (§5.3).

### 4.2 Fan art 2D (mirar, nunca pegar)

| Obra | Autor | Enlace | Para qué |
|---|---|---|---|
| Gojo y Sukuna con signos de mano, rojo | dazu_sugar__ | [X](https://twitter.com/dazu_sugar__) · [wallhaven 856k82](https://wallhaven.cc/w/856k82) | los **signos de mano** |
| Choso con olas ukiyo-e | BH20647 | [X](https://x.com/BH20647/status/2010271510620217836) | fusión con grabado japonés |
| Megumi y Mahoraga en tinta | KyeZzzz | [X](https://x.com/KyeZzzz/status/1973791228320952556) | tinta y papel |
| Inumaki | michelrodrigues | [ArtStation](https://www.artstation.com/artwork/YG8gBq) | Inumaki en otra pose |
| Inumaki | brunofrenda | [ArtStation](https://www.artstation.com/artwork/8wJnYn) | idem |
| Aoi Todo en 3D | sidness | [ArtStation](https://www.artstation.com/artwork/QX09LZ) | Todo modelado |
| Gojo y Geto | liuxiang_art | [ArtStation](https://www.artstation.com/artwork/JegBqZ) | la pareja del pasado |

**Aviso**: en DeviantArt, la búsqueda «popular + Inumaki» devuelve
sobre todo **imágenes hechas con IA** (cuentas como «RynxieAi»). No
sirven de referencia y el dueño no quiere que la lámina «parezca de IA».

### 4.3 Código y datos en GitHub

| Repositorio | Qué da | Uso aquí |
|---|---|---|
| [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror) | **subtítulos japoneses con tiempos** de la T1, T2, T3 y JJK0 | todos los minutos de §2 |
| [h0tcat/JujutsuKaisenLogoGenerator](https://h0tcat.github.io/JujutsuKaisenLogoGenerator/) | generador de logos «estilo JJK» con la fuente Aoyagi Reisho | ver §6 (ojo: sin tildes) |

## 5 · Sitios, luz, paleta y texturas

### 5.1 Los sitios de la serie

| Sitio | Cómo es | Luz y hora | Imagen |
|---|---|---|---|
| **Escuela Superior de Hechicería de Tokio** (呪術高専) | un complejo de **templos de madera** en el monte, con pagoda, torii y bosque; parece un santuario, no un colegio | **día claro**, cielo azul, verdes | F1-F3 (#1178, #1180, #1177) |
| **Aula de la escuela** | aula de madera vieja, **ventanas de cuadrícula**, cortinas blancas, pupitres | luz de mañana lateral, **tonos malva** | F29 (JJK0), F13 (#817, con pizarra) |
| **La celda de los talismanes** | sala cerrada con **cientos de ofuda** en las paredes y **farolillos hexagonales** en el suelo; Yuji encadenado a una silla | **amarillo intenso** de los farolillos, sombras marrones | F23; clip doblado 0:08-0:47 |
| **Shibuya** (T2) | el cruce, la estatua de **Hachikō**, las salidas del metro, Mark City, los torniquetes del Inokashira: **sitios reales** de Tokio dibujados con detalle | **noche del 31 de octubre** (Halloween), neón, un **velo negro** sobre el barrio | F7-F11, F28 |
| Colegio de Yuji en Sendai | edificio escolar corriente; el **club de ocultismo** en una sala con estanterías | tarde | clip del club (0:00-0:45) |
| El «paseo por Tokio» | versión **cómica chibi**, fondo de colores con «東京» | colores pop | F5 (#503) |
| **El Vacío Infinito** (dominio de Gojo) | un **espacio** negro con **estrellas y nebulosa** azul-blanca | contraluz frío | F27 |
| **Santuario Malévolo** (dominio de Sukuna) | un **santuario budista** con bocas y cráneos, sobre un charco de sangre | rojo y negro | T14 de la hoja; Sketchfab (§4) |

### 5.2 Paleta medida con Pillow ✅

(Paleta por cuantización de la imagen dicha; margen ±5 por canal.)

| Sitio | Colores | De dónde |
|---|---|---|
| Escuela, paisaje | cielo `#6CBACD` y `#D0E5ED`, bosque `#476A4F`, madera en sombra `#1B1913` | #1178 |
| Escuela, vista aérea | verdes `#487A4E` `#809D83`, piedra `#C3C4BC` | #1180 (re-medido por el 3.er ayudante: `#46794D`, `#C5C6BF` ✅) |
| Aula (JJK0) | sombras `#2F2831`, luz `#D3D0CF`, malvas `#7C6372` `#AA9AA2` | fotograma de JJK0 (wiki) |
| **Celda de talismanes** | **amarillo farolillo `#EBD430` y `#FAF441`**, ocre `#C09E1C`, marrón `#523010` | clip doblado, 0:15 |
| Shibuya de noche | azules casi negros `#111625` `#20293B`, gris `#616F76` | #1272 |
| Salida 13 de Shibuya | verdes oliva `#38442C` `#4C6648`, luz `#BEC49C` | #834 |
| Vacío Infinito | negro azul `#0B0D1E`, azul noche `#1D233D`, blanco estrella `#F9F7F9` | T1-7 (copia, 3:39) |
| Hanami del OP1 | luz rosada `#D7D3CD` `#E2DEDA`, troncos `#6A5C4C` | OP1, 1:16 |
| **Fondos del ED1** | Yuji **`#50CDCF`**, Megumi **`#FBE63B`**, Nobara **`#DF4456`**, Gojo **`#515151`** | ED1, 0:10-0:58 |
| **Pizarra de *Cursed Clash*** | pizarra `#36362F`, tiza `#DDD2CC`, marco `#30241E` | tráiler, 1:24 |
| Interfaz de *Cursed Clash* | cian `#12A2E4`, azul noche `#181E2A`, rojo `#9C001E` | tráiler, 1:30 |
| Logo en el OP1 | trazo `#D4D48C`, relleno `#142218` | OP1, 0:14 |

**Para contrastar** (paletas de fans, sin medir): hay muchas en Pinterest
y coolors; no las usé.

### 5.3 Texturas reales equivalentes (CC0)

| Para | Textura | Fuente | Licencia |
|---|---|---|---|
| Ofuda y papel de talismán | Paper001-Paper006 | [ambientCG](https://ambientcg.com/list?q=paper) | CC0 |
| Suelo de madera del aula / templo | `wood_floor_deck`, `dark_wooden_planks` | [Poly Haven](https://polyhaven.com/textures) | CC0 |
| Mesa de madera | `wood_table_001` | Poly Haven | CC0 |
| Andén y calle de Shibuya | `concrete_floor_worn_001`, `asphalt_02`, `painted_concrete` | Poly Haven | CC0 |
| Pared de la escuela | `rough_plasterbrick_05`, `clay_plaster` | Poly Haven | CC0 |
| Tejado de templo | `ceramic_roof_01`, `clay_roof_tiles_02` | Poly Haven | CC0 |
| Pizarra | no hay pizarra en Poly Haven; `painted_concrete` oscurecido a `#36362F` + polvo de tiza | Poly Haven | CC0 |

(Nombres comprobados en la API de Poly Haven y de ambientCG.)

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

| Dónde | Cómo es | Fuente |
|---|---|---|
| **Logo 呪術廻戦** | letra dibujada a mano sobre base de **篆書 (escritura de sello)**, la de los sellos chinos y los *hanko*. Se retocó para que **se lea** y para que sea **simétrica** (el 呪). Es la misma idea que el logo de *Ghost in the Shell* | ✅ [artículo de «しじみ» en note.com](https://note.com/shijimiota/n/n8a524b4ddbb5) + [いいフォント](https://goodfreefonts.com/3116/) (lo llama «parecido a 隷書/篆書») |
| Logo en el OP1 | trazo **amarillo pálido `#D4D48C`** con relleno casi negro `#142218`, sobre un mapa de Tokio de noche con luces rosas | ✅ medido en el fotograma 0:14 |
| Logo de la T2 | el mismo, en **dorado sobre negro**, con «渋谷事変» debajo en Mincho | ✅ visto (PV Shibuya, 1:12) |
| Logo en inglés | «Jujutsu Kaisen» en romaji con **letras que imitan el sello**, bajo el logo japonés | ✅ visto (tráiler 1, 1:10; *Cursed Clash*) |
| **Logo en español** (película *Ejecución*, 2025) | «JUJUTSU KAISEN» en romaji **blanco, a mano, con trazos de pincel afilados**; debajo, «**— EJECUCIÓN —**» en **serif clásica de mayúsculas** (tipo Trajan) **con tilde**; encima, en la misma serif pequeña, «ESTRENO DE LA TERCERA TEMPORADA EN EXCLUSIVA». Fondo en degradado **morado `#3C005B` → magenta `#5B004A`** → rojo | ✅ visto y medido (3.er ayudante: tráiler subtitulado, [x9s6mua, 1:14](https://www.dailymotion.com/video/x9s6mua?start=74)) |
| **Cartelas del tráiler en español** | serif de mayúsculas **morado oscuro sobre violeta `#5A10AD`**, dos líneas, la 2.ª más pequeña: «UNA COMPILACIÓN ESPECIAL / DEL INCIDENTE DE SHIBUYA», «REVÍVELO EN LA GRAN PANTALLA»; y sobre negro, en blanco: «SE ABRE EL TELÓN A / UN NUEVO ARCO» | ✅ visto (x9s6mua, [0:14](https://www.dailymotion.com/video/x9s6mua?start=14) y 0:48). **La franquicia rotula en español con serif clásica y tildes**: la Shippori Mincho B1 encaja (§6.2) |
| **Título de cada episodio** | **Mincho negrita blanca**, abajo a la derecha: «第1話 両面宿儺», «第7話 急襲» | ✅ [título ep. 1](https://static.wikia.nocookie.net/jujutsu-kaisen/images/6/63/Episode_1_Title_Card.png), ep. 7, 9 y 24 (wiki, 1920×1080) |
| **Hora y lugar** (Shibuya) | igual: Mincho blanca abajo a la derecha, «22:20 井之頭線 渋谷駅 アベニュー口», «同刻 都心メトロ渋谷駅 13番出口側（帳外）» | ✅ #961 y #834 (T6-T7 de la hoja) |
| **Técnicas en el manga** | kanji **muy gruesos y verticales, entre 「」**: 「黒閃」, 「蒼」, 虚式「茈」; el dominio en **caja vertical** («領域展開 伏魔御廚子») | ✅ T13-T18 de la hoja |
| *Cursed Clash* | serif clásica **tipo Trajan** en tiza (pizarra); interfaz en sans condensada blanca con acentos cian | ✅ visto (tráiler, 1:24 y 1:30) |

### 6.2 Letras libres comprobadas por mí con fontTools ✅

Probé las tildes **áéíóú ÁÉÍÓÚ**, la **ñ Ñ**, **¿ ¡** y **ü**, y los
corchetes japoneses 「」 (muestra en `pantalla_y_letras_01.jpg`, L1-L8).
No basta con mirar el mapa de caracteres: **dibujé cada letra** y medí
su contorno, porque una fuente puede «tener» la á y dejarla vacía.

| Letra | Dónde | Licencia | Tildes, ñ, ¿ ¡ | Para qué |
|---|---|---|---|---|
| **Shippori Mincho B1** | Google Fonts | OFL | ✅ todas + 「」 | **títulos de episodio, hora y lugar** (la Mincho blanca) |
| **Zen Old Mincho** / **Kaisei Tokumin** | Google Fonts | OFL | ✅ todas | lo mismo, más gruesa (Tokumin trae peso 800) |
| **Yuji Syuku** | Google Fonts | OFL | ✅ todas | pincel fino: talismanes, títulos cortos |
| **Yuji Boku** | Google Fonts | OFL | ✅ todas | pincel más suelto, «maldito» |
| **Zen Antique** | Google Fonts | OFL | ✅ todas | la **antigua** de los globos del manga japonés |
| **Dela Gothic One** | Google Fonts | OFL | ✅ todas | **nombres de técnica** gruesos (el 「黒閃」 del manga) |
| **Anime Ace 2.0 BB** | [Blambot en dafont](https://www.dafont.com/anime-ace-bb.font) | gratis (ver `font info.txt`) | ⚠️ tildes y ñ sí, **faltan ¿ y ¡** | globo de cómic occidental. **No sirve** para preguntas en español sin trucos |
| **Sudoku** (Vladimir Nikolic) | [dafont](https://www.dafont.com/sudoku.font), único resultado para «jujutsu» | uso personal ⚠️ | ❌ **sin tildes, ñ, ¿ ni ¡** (93 glifos) | sólo 1-2 palabras en mayúscula sin tildes |
| **青柳隷書しも** (Aoyagi Reisho Shimo) | la que usa el [generador de logos «呪術廻戦風»](https://h0tcat.github.io/JujutsuKaisenLogoGenerator/) (código en GitHub, trazo `#e7e70c`, relleno `#000f00`) | libre (autor «しも») ⚠️ leer su licencia | ❌ **trampa**: el mapa dice que tiene tildes, pero **los glifos están vacíos** (salen en blanco; comprobado dibujándolos y con `BoundsPen`) | sólo kanji y letras sin tilde; L2 de la hoja |
| 白舟篆古印 / 白舟隷書 | Hakusyu (Japón) | libres con pocos caracteres | ⚠️ no probadas | kanji tipo logo; la versión libre trae pocos kanji |

**Letras de pago que se parecen al logo** (no usar sin comprar):
HOT-Hakushu Tensho Kyokan, Dynafont 新篆書体 ⚠️ (según los artículos).

### 6.3 Qué letra para qué

| Texto de la lámina | Letra |
|---|---|
| Nombre del canal | **Shippori Mincho B1** ExtraBold, blanca, abajo a la derecha, como un título de episodio |
| Nombre de la técnica / consigna fuerte | **Dela Gothic One**, vertical, entre 「」 |
| Diálogo del personaje | **Zen Antique** o **Kaisei Tokumin** (lleva ¿ ¡) |
| Letra de pizarra (concepto con Gojo) | una serif con tiza: **Shippori Mincho B1** con textura de tiza |
| Etiqueta del jarabe o talismán | **Yuji Syuku** |
| El logo | **no se imita con una fuente**: se usa el logo oficial como referencia, o no se pone |

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

**Resumen**: Jujutsu Kaisen **no habla con globos blancos**. Habla con
**Mincho blanca abajo a la derecha** (títulos y hora-lugar), con
**técnicas verticales entre 「」**, con **cajas de explicación** larguísimas
(el famoso «Gege explica las reglas») y, en los juegos, con **una
pizarra**, **placas hexagonales cian** o **dos viñetas con el borde roto
sobre tinta azul petróleo** (el modo historia de *Cursed Clash*).

### 7.1 Lo que la serie pone en pantalla (visto)

| Recurso | Cómo es | Dónde lo vi |
|---|---|---|
| **Título de episodio** | «第7話 急襲» en Mincho blanca negrita, abajo a la derecha, sobre un fotograma de la escena | wiki: título ep. 1, 7, 9, 24 |
| **Hora y lugar** | «22:20 井之頭線 渋谷駅 アベニュー口»: Mincho blanca, abajo a la derecha. En Shibuya **cada escena lleva su reloj** | #961, #834 |
| **Cartel de pincel con tachón** | «定員未達» (cupo sin cubrir) en pincel negro enorme, con **una línea roja** que lo tacha y un rótulo pequeño en inglés («Not Enough Members») | club de ocultismo, T1-1 (clip, 0:19) |
| **Muro de palabras** | kanji negativos (憎い, 苦しい, 死にたい…) llenando la pantalla | tráiler 1, 0:48 |
| **Cartela del tráiler** | Mincho blanca centrada sobre negro: «少年は戦う―「正しい死」を求めて» | tráiler 1, 1:18 |
| **Ofuda (talismanes)** | papeles verticales con escritura, pegados por cientos en la pared de la celda | clip doblado, 0:18-0:21 |
| **Etiquetas del mundo** | la placa «虎杖» en la puerta del hospital; la cinta «KEEP OUT / 立入禁止»; el jarabe «のどナオール» | títulos ep. 1 y 9; JJK0 |
| **Juju-Cortos** (じゅじゅさんぽ) | minicapítulos tras el ending, con los personajes en **dibujo simple** charlando | Doblaje Wiki; arte #165 de Gege |
| **Tabla dibujada a mano** | Panda explica cómo ve a cada alumno con **una tabla de rangos** (1級, 準1級, 2級…) y **caras chibi** pegadas en cada fila | [wiki, «How Panda thinks the students rank (Anime)»](https://static.wikia.nocookie.net/jujutsu-kaisen/images/9/91/How_Panda_thinks_the_students_rank_%28Anime%29.png), 1920×1080 (2.º ayudante) |

### 7.2 Cómo piensan

- **Voz en off con explicación**: los personajes **explican su técnica
  en voz alta** en mitad de la pelea (Gojo a Jogo: «el infinito está en
  todas partes», T1-7; Todo explica el Destello Negro, T1-19). Es parte
  del estilo, y **un meme del fandom**.
- **Narrador** en Shibuya: «現代最強の呪術師は…» (T2-9, 17:10).
- **Recuerdos** con la frase del abuelo repetida: «人を助けろ» vuelve en
  T1-1, 2, 4 y 11 (§2).

### 7.3 En los videojuegos

| Juego | Cómo explica o habla | Estado |
|---|---|---|
| ***Cursed Clash*** (Bandai Namco, 2024) | **«Special Lecture»**: Gojo con venda y **puntero** ante una **pizarra** gris verdosa `#36362F`, con marco de madera `#30241E` y tiza `#DDD2CC` en serif. En combate: nombre en **placa hexagonal** con borde **cian `#12A2E4`** y fondo azul noche `#181E2A`; caja de ayuda con título cian («Cursed Energy Gauge») y texto blanco; acentos **rojo `#9C001E`** | ✅ visto y medido (tráiler, 0:21, 1:24, 1:30) |
| ***Phantom Parade*** (móvil, 2023) | arte horizontal por personaje con fondos de energía (azul, rojo) | ✅ arte visto (#132-136); la caja de diálogo ⚠️ no la vi |
| **Caja de diálogo del modo historia de *Cursed Clash*** | **dos fotogramas del anime recortados con el borde roto** (como papel rasgado), uno arriba a la izquierda y otro abajo a la derecha; cada frase va **al lado de su viñeta**, en sans blanca, sobre un fondo de **tinta azul petróleo** difuminada (`#314953`, `#202C33`, `#4C656D`). Sin nombre del que habla: se sabe por la cara. Ejemplo: Megumi «I don't mind, but are you okay with being among ordinary people, Panda?» / Panda «It's the zoo, so people'll probably just assume I'm a guy in a suit» | ✅ **visto y medido** (tráiler, [3:06-3:09](https://www.dailymotion.com/video/x8scngs?start=189)) |
| **Frases rápidas del lobby** (*Cursed Clash*) | lista de 8 casillas numeradas con icono de bocadillo cian: «Let's do this!», «Not bad at all!», «Don't worry about it!», «Thanks.», «Sorry.»; fondo azul noche `#121D2A` | ✅ visto (tráiler, [2:39](https://www.dailymotion.com/video/x8scngs?start=159)) |
| **«Online Lobby»** | la sala de espera en línea: los jugadores andan por un Shibuya morado; menú «Stamp / Tactics / Talk / Unique» | ✅ visto ([2:25](https://www.dailymotion.com/video/x8scngs?start=145)): **un «lobby» oficial de JJK**, para CREAR SALA |

### 7.4 Cómo se traduce a una lámina fija

1. **Pizarra de Gojo** (el «Special Lecture»): los textos del canal
   escritos **con tiza**, numerados, y Gojo con el puntero. Es el
   formato oficial de «Gojo explica».
2. **Título de episodio**: el nombre del canal en Mincho blanca abajo a
   la derecha, **como si la lámina fuera un fotograma** («第1話» →
   «Sala 1»).
3. **Técnica vertical**: la acción clave en 「」 vertical y gruesa
   («「Expansión de Dominio」»).
4. **Ofuda**: cada norma escrita en un **talismán de papel** vertical,
   pegado en la pared (la celda de F23).
5. **Etiqueta de objeto**: el texto en la etiqueta del jarabe o en la
   credencial de estudiante (F19).

### 7.5 Qué NO hacer con el texto

- **Un globo blanco redondo** con cola: no es JJK.
- **Imitar el logo con una fuente** (no existe una igual; se nota).
- **Letras alegres o redondas** (tipo Comic Sans o Hachi Maru Pop): el
  tono es oscuro.
- **Poner el texto vertical en español** letra por letra: el vertical
  sólo para 2-3 palabras (nombre de técnica); el resto, horizontal.
- **Usar Anime Ace** para preguntas: no trae ¿ ni ¡.

## 8 · Los personajes

Fuentes de cada ficha: la **Jujutsu Kaisen Wiki** (secciones
«Appearance» y «Personality», leídas por la API) + los **subtítulos
con minuto** (§2) + lo que **vi** en los vídeos (§12). ✅ = wiki y
subtítulo o vídeo. Cuidado con los **spoilers** (§14.2).

### Satoru Gojo — el profesor, «el más fuerte» (1.º en la 4.ª encuesta oficial)

- **Quién es**: profesor de los de 1.er año en la Escuela de Tokio. Es
  **el hechicero más fuerte**. Lleva **una venda negra** en los ojos
  (en JJK0, vendas de tela; de paisano, **gafas de sol redondas**).
  Pelo **blanco**, ojos **azules** (los «Seis Ojos») ✅.
- **Carácter**: juguetón, **presumido**, burlón con los jefes del mundo
  hechicero; **frío** en combate. Quiere cambiar el sistema **formando
  alumnos fuertes** ✅ (wiki).
- **Qué le importa**: sus alumnos. Vilchis: «a veces los ve como sus
  hijos» (§10.5).
- **Con quién**: Yuji, Megumi y Nobara (sus alumnos); **Geto** (su único
  amigo de verdad, luego enemigo); Nanami (le hace bromas); Utahime (la
  pica).
- **Cómo habla**: tranquilo, con **chistes en mitad del peligro**:
  «Tranquilo. Soy el más fuerte» (T1-2, 1:29). **Explica como un
  profesor**: «Te voy a enseñar la Expansión de Dominio» (T1-7, 9:22).
- **Cuerpo**: muy alto, **manos en los bolsillos**, se inclina hacia
  el otro; **junta las manos** sonriendo; **señala con el índice**; se
  **sube la venda** con dos dedos (vistos en T1-7, §12.2).
- **Cómo saluda**: con **la «V» de la paz** (P2) o levantando la mano.

### Yuji Itadori — el protagonista (1.º en la 1.ª encuesta, 2.º en la 4.ª)

- **Quién es**: chico de pueblo (Sendai) con **fuerza sobrehumana**. Se
  come un dedo de Sukuna para salvar a sus amigos y **lo lleva dentro**.
  Pelo **rosa con los lados rapados**, **sudadera roja con capucha**
  bajo la chaqueta del uniforme ✅.
- **Carácter**: noble, **alegre**, algo ingenuo, aprende rápido. Cree en
  **«la muerte correcta»** para cada persona ✅ (wiki; cartela del tráiler).
- **Qué le importa**: la frase de su abuelo: «**Tú eres fuerte. Ayuda a
  la gente**» (T1-1, 10:52). Le pesa **lo que Sukuna hace con su cuerpo**.
- **Miedo**: morir solo, sin haber servido de nada («muere rodeado de
  gente», T1-1, 11:07).
- **Con quién**: Megumi y Nobara (su trío); Gojo (su profe); **Todo**
  (su «hermano»); Nanami (su mentor); Junpei (su amigo perdido).
- **Cómo habla**: directo, informal, entusiasta («¡Tokio! ¡Tokio!» con
  Nobara, T1-3, 5:26). En latino, **Enzo Fortuny** lo hace con «saltos»
  de lo serio a lo juguetón (§10.5).
- **Cuerpo**: **puños**, se sube la capucha (T1-19), carcajada abierta
  (OP1, 1:18).
- **Mote latino**: «**gallo**» (Doblaje Wiki, ep. 52).

### Megumi Fushiguro — el serio (1.º en la 2.ª y la 3.ª encuesta)

- **Quién es**: compañero de Yuji, invoca **perros y animales de sombra
  con las manos** (el **perro** es su gesto, P8). Pelo negro **en
  pinchos** («erizo de mar») ✅.
- **Carácter**: **frío, callado, calculador**; siempre «un poco
  enfadado» (según Yuji). Muy correcto ✅ (wiki).
- **Qué le importa**: su hermana **Tsumiki**. «Salvo a la gente de forma
  injusta» (T1-5, 9:50).
- **Con quién**: Yuji y Nobara (le sacan de quicio); Gojo (su tutor
  desde niño; le molesta su actitud).
- **Cómo habla**: poco, seco. Explica las cosas a los demás (el
  vocabulario de Inumaki, T1-5, 17:06).
- **Cuerpo**: **manos juntas** para invocar; mirada de lado; brazos
  cruzados.

### Nobara Kugisaki — la de pueblo con martillo (6.ª en la 1.ª encuesta)

- **Quién es**: chica de un pueblo pequeño que se va a Tokio. Pelea con
  **martillo y clavos**, y un **muñeco de paja** ✅.
- **Carácter**: **segura, descarada, bocona**, le encanta arreglarse y
  **ir de compras**; en el fondo, **muy leal** ✅ (wiki).
- **Qué le importa**: **ser ella misma** («Esto es para poder seguir
  siendo quien soy», tráiler) y reencontrar a su amiga Saori.
- **Cómo habla**: gritona, se burla: «**Alégrense, chicos: soy la
  única chica**» (T1-3, 3:06). Con Yuji hace el payaso.
- **Cuerpo**: **mano en la cadera** (P12), martillo al hombro, clavos
  entre los dedos (P10); en el ED1, **cargada de bolsas** (0:40).

### Sukuna — el Rey de las Maldiciones (el villano que todos citan)

- **Quién es**: el «**Espectro de Dos Caras**» en el doblaje. Vive
  dentro de Yuji. Cuando sale: **marcas negras** en la cara (doble raya
  bajo los ojos, **segundo par de ojos**), sonrisa enorme ✅.
- **Carácter**: **egoísta, sádico, burlón**; sólo le importa su placer ✅.
- **Cómo habla**: con desprecio, **voz grave**. En latino la T1 la hizo
  Osvaldo Trejo, y los fans comentan **el bajo** de su voz (Reddit:
  «What the heck is that bass on the Spanish one?», 54 votos) ⚠️.
- **Uso en lámina**: **no como guía amable**. Sirve para una amenaza
  cómica («¿Otra vez pidiendo ayuda?») o para una lámina de reglas.

### Kento Nanami — el oficinista que odia las horas extra (5.º en la 1.ª y 2.ª encuesta)

- **Quién es**: hechicero de 1.er grado, **ex oficinista**. **Traje
  beige**, camisa azul, **corbata de leopardo**, **gafas sin patillas**,
  reloj; espada envuelta en tela ✅ (wiki + P15).
- **Carácter**: **serio, práctico, puntual**; «trabajar es un asco»;
  no trabaja **ni un minuto de más**. En el fondo, **amable y
  responsable** con Yuji ✅.
- **Cómo habla**: frases cortas y educadas, **usted**. «**Lo primero es
  saludar**» (doblaje, §10.4). A las 18:00, se afloja la corbata:
  «**Esto ya son horas extra**» (T1-10, 21:12).
- **Cuerpo**: **se tapa la boca** pensando (P15), **se enrolla la
  corbata en la mano** (#948), mira el reloj.
- **Por qué es tan querido**: el adulto responsable; su final en
  Shibuya («Lo demás te lo dejo a ti», T2-18) hizo llorar a medio fandom.

### Toge Inumaki — el de las palabras malditas (4.º en la 1.ª encuesta)

- **Quién es**: 2.º año. Su técnica es el **Habla Maldita** (呪言): **lo
  que dice, pasa** («¡Duerme!», «¡No te muevas!», «¡Revienta!»). Por eso
  **no habla normal**: sólo dice **ingredientes de onigiri** (salmón,
  bonito, atún con mayonesa, algas…) ✅ (wiki + subtítulos).
- **Marcas**: el **sello «ojos de serpiente y colmillos»** en la lengua
  y las mejillas; por eso lleva el **cuello del uniforme subido** hasta
  la nariz ✅.
- **Su punto débil**: si abusa, **se le destroza la garganta**: tose
  sangre o **se queda sin voz** (T1-19, 2:08; JJK0, 37:24). Lleva
  **espray para la garganta** («のどナオール», P29) ✅ (wiki: «carries
  cough syrup»).
- **Técnica y aparatos**: su voz funciona **con megáfono** (Shibuya,
  T2-13) y **por teléfono**, y **se puede grabar** en una grabadora
  (manga, cap. 262, págs. 20-23) ✅ (wiki, «Cursed Speech»; el 1.er ayudante había puesto 269).
- **Carácter**: parece distante, pero es **amable y protector**; hace
  el tonto con Panda ✅.
- **Por qué importa aquí**: es **el personaje de la voz**. Cuida la
  garganta, habla poco y bien, y su voz grabada sigue funcionando. Los
  fans preguntan en broma «¿por qué no usa texto a voz?» (Reddit, 1.057
  votos) ⚠️.

### Aoi Todo — el «mejor amigo» (8.º en la 1.ª encuesta)

- **Quién es**: el gigante de Kioto, **sin camisa** casi siempre,
  moño alto y **cicatriz** en la cara ✅.
- **Carácter**: **excéntrico**, fan de la idol **Takada-chan**. Pregunta
  a todos **«¿Qué tipo de chica te gusta?»** (T1-8, 5:54); si la
  respuesta le gusta, se inventa recuerdos de una amistad de toda la vida
  con Yuji ✅.
- **Cómo habla**: a gritos, **«¡Brother!»**, «Congratulations, brother»
  (T1-19, 15:57). Explica técnicas como un maestro de artes marciales.
- **Cuerpo**: **da una palmada** (su técnica, Boogie Woogie), brazos
  abiertos, lágrimas de emoción.

### Maki Zenin, Panda y Yuta Okkotsu (2.º año)

- **Maki**: **gafas**, coleta, **armas** (la lanza roja, la Nube
  Juguetona); no tiene energía maldita y se hace fuerte a pulso ✅.
  Seria, mandona, protectora.
- **Panda**: un **panda de verdad** que habla (un cadáver maldito). **De
  buen humor, sarcástico**; «traduce» a Inumaki ✅ (wiki; ED1 con
  globos, 1:14).
- **Yuta**: protagonista de JJK0. Tímido, luego muy fuerte; su amiga
  **Rika** es una maldición. **Anillo** (tráiler de JJK0) ✅.

### Suguru Geto — el amigo perdido (4.º en la 2.ª, 3.ª y 4.ª encuesta)

- **Quién es**: el mejor amigo de Gojo en la escuela; luego, el
  villano de JJK0. **Moño y flequillo**, **pendientes grandes**, túnica
  de monje ✅. Sonrisa suave (tráiler JJK0, 1:28).
- **Cómo habla**: amable y frío a la vez. Suya es la frase de «¿Eres el
  más fuerte porque eres Satoru Gojo…?» (T2-5, 16:56).

### Los otros que salen en las láminas

| Personaje | Rasgo | Para qué |
|---|---|---|
| **Kiyotaka Ijichi** | el ayudante con gafas, siempre agobiado; **baja el velo** («では“帳”を下ろします», JJK0 35:52) | el que «abre la sala» |
| **Kogane** | el shikigami dorado que **anuncia las reglas** del Juego del Sacrificio; en latino, «¡Eso es todo, amigos!» | reglas, anuncios |
| **Takada-chan** | la idol de Todo; canta «Climax☆JUMPING!» (Tomoyo Kurosawa) | chiste |
| **Masamichi Yaga** | el director, hace muñecos malditos (Panda) | fondo |

## 9 · ¿Quién es el más querido?

### 9.1 Las cuatro encuestas oficiales de la *Weekly Shōnen Jump* ✅

Fuente A: [Jujutsu Kaisen Wiki, «Popularity Polls»](https://jujutsu-kaisen.fandom.com/wiki/Popularity_Polls)
(API). Fuente B (4.ª encuesta): [eiga-manga.com](https://eiga-manga.com/entry/jujutsu-popularity-vote4)
y [hadashinoarukikata](https://hadashinoarukikata.com/entry/2024/10/20/220156);
convocatoria en la [web de la Jump](https://www.shonenjump.com/j/vote_jujutsu_kaisen/).

| Puesto | 1.ª (2019, 163.066 votos) | 2.ª (2022, 97.860) | 3.ª (2023, 96.704) | 4.ª (2024, 264.298) |
|---|---|---|---|---|
| 1 | **Yuji** (21.735) | **Megumi** (19.393) | **Megumi** (30.059) | **Gojo** (113.392) |
| 2 | Megumi (21.193) | Gojo (14.359) | Yuji (24.038) | Yuji (48.131) |
| 3 | Gojo (16.923) | Yuji (13.265) | Gojo (11.591) | Megumi (28.502) |
| 4 | **Inumaki** (12.088) | Geto (10.345) | Geto (6.487) | Geto (19.156) |
| 5 | **Nanami** (11.644) | Nanami (5.548) | Yuta (2.942) | Naoya (11.731) |
| 6 | Nobara (9.590) | Inumaki (5.052) | Naoya (2.858) | Choso (6.247) |
| 7 | Yuta (7.934) | Choso (4.757) | Nanami (2.541) | Yuta (5.991) |
| 8 | Todo (7.791) | Yuta ⚠️ | Inumaki (2.459) | Nanami (4.162) |
| 9 | Junpei (7.481) | Toji (3.384) | Maki (2.056) | Sukuna (4.077) |
| 10 | Sukuna (5.860) | Naoya (2.935) | Choso (1.748) | Toji (3.218) |

⚠️ En la 2.ª, la wiki da a Yuta 7.791 votos en el 8.º puesto, más que
el 7.º: es una errata de la wiki (el número es el de Todo en la 1.ª).

### 9.2 Lo que dice el público de internet

- **Gojo** es la cara de la franquicia fuera de Japón: la 4.ª encuesta
  (con votos de todo el mundo por la web) le dio **más del doble** que
  al 2.º. Sus memes («Nah, I'd win», «Throughout Heaven and Earth…»)
  son los más compartidos (Reddit: «Gojo is still doing the "nah I'd
  win" pose on the cover…») ⚠️.
- **Nanami**: en r/JuJutsuKaisen, «Nanami Kento - Overtime» tiene
  **3.783 votos** y «Typical day of Nanami working overtime» 1.980 ✅
  ([Arctic Shift](https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=JuJutsuKaisen&title=nanami%20overtime)).
- **Inumaki**: siempre alto en las encuestas japonesas (4.º en la 1.ª)
  y muy querido por su diseño; «Why doesn't Inumaki just use TTS»
  (1.057 votos) muestra que el fandom **juega con su voz** ✅.
- **Premios del público**: la serie ganó **Anime del Año** en los 5.º
  Crunchyroll Anime Awards (19-feb-2021) ✅ (Cultura Geek + [Wikipedia en
  inglés, «Crunchyroll Anime Awards»](https://en.wikipedia.org/wiki/Crunchyroll_Anime_Awards),
  3.er ayudante). La **T2 lo volvió a ganar** en los 8.º (2-mar-2024), y
  *JJK0* ganó la película del año en los 7.º (2023) ✅ (Wikipedia; misma
  tabla). Encuesta latina propia: ⚠️ no la encontré.

### 9.3 Qué sale de todo esto

| Para… | Personaje | Por qué |
|---|---|---|
| **la más reconocible** | **Gojo** | 1.º en la última encuesta, el meme, el profesor |
| **el protagonista** | Yuji | 1.º en la 1.ª, 2.º en la 4.ª |
| **el secundario más querido** para un servidor de **voz** | **Inumaki** | su técnica **es la voz**; alto en las encuestas japonesas |
| el adulto que explica | **Nanami** | el «jefe» cansado, muy querido, sus reglas |
| la chica | Nobara | la única del trío; carácter fuerte |

## 10 · Doblaje latino

**Sí hay doblaje latino**, hecho en México para **Crunchyroll**, desde
el 20-nov-2020 ✅ ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Jujutsu_Kaisen)
por la API + [Cine Premiere](https://cinepremiere.com.mx/crunchyroll-doblajes-jujutsu-kaisen-otono-2020.html)).

### 10.1 La producción ✅

| Dato | Valor | Fuentes |
|---|---|---|
| Estudio | **Audiomaster Candiani** (T1); T2 en **Bita Dubbing Studios**, de Candiani; T3 otra vez Candiani | Doblaje Wiki + [Dubbing Database](https://dubdb.fandom.com/wiki/Jujutsu_Kaisen_(Latin_American_Spanish)) + [Hero Network](https://www.beahero.gg/jujutsu-kaisen-temporada-3-doblaje-latino-llega-a-crunchyroll/) |
| Dirección | **Patricia Acevedo** (T1 y JJK0); **Octavio Campos** (T2 y T3) | las tres |
| Adaptación | **Jaime Chaparro** (T2, T3 y JJK0) | Doblaje Wiki + Hero Network |
| Guion | la T1 se dobló **desde los subtítulos de Crunchyroll en inglés**; desde la T2, **desde el japonés** | Doblaje Wiki |
| Dónde se ve | Crunchyroll; Netflix Latinoamérica (T1 desde 31-may-2024, T2 desde 1-may-2026); HBO Max; Claro video; Adult Swim; Disney+ México (T2) | Doblaje Wiki |
| JJK0 | **primera película de Crunchyroll con doblaje en cines** (24-mar-2022 en Latinoamérica) | Doblaje Wiki + [Somos Kudasai](https://somoskudasai.com/noticias/la-pelicula-jujutsu-kaisen-0-revela-su-elenco-de-doblaje-al-espanol-latino/) |

### 10.2 Las voces (cada una en **dos fuentes**)

Fuente A = Doblaje Wiki (API). Fuente B = otra, dicha en la tabla.

| Personaje | Voz latina | Seiyū | Fuente B |
|---|---|---|---|
| **Yuji Itadori** | **Enzo Fortuny** (Inuyasha, Drake Parker) | Junya Enoki | Cine Premiere, Televisa, Hero Network |
| **Megumi Fushiguro** | **Víctor Ruiz** (Saitama) | Yūma Uchida | Cine Premiere, Televisa |
| **Nobara Kugisaki** | **Ayari Rivera** | Asami Seto | Cine Premiere, Televisa |
| **Satoru Gojo** | **José Gilberto «Pepe» Vilchis** (Shun de Andrómeda, Hércules) | Yūichi Nakamura | Cine Premiere, Cultura Geek |
| **Sukuna** (T1) | **Osvaldo Trejo** (falleció en 2021) | Junichi Suwabe | Cine Premiere, Televisa |
| **Sukuna** (T2 en adelante) | **Alfredo Gabriel Basurto** (Levi, Zoro, Tengen) | Junichi Suwabe | Dubbing Database, [Anime Argentina](https://animeargentina.net/gabriel-basurto-doblaje/) |
| **Yuta Okkotsu** | **Diego Ramora** | Megumi Ogata | Somos Kudasai, Hero Network |
| **Maki Zenin** | **Anette Ugalde** | Mikako Komatsu | Dubbing Database, Hero Network (la nota de Crunchyroll de JJK0 dice «Anette García» ⚠️) |
| **Toge Inumaki** | **Ángel Rodríguez** | Kōki Uchiyama | Somos Kudasai, Dubbing Database |
| **Panda** | **Roberto Cuevas** | Tomokazu Seki | Somos Kudasai, Dubbing Database |
| **Kento Nanami** | **Carlos Hernández** | Kenjirō Tsuda | Hero Network, [Chirchi](https://www.chirchi.com/tercera-temporada-jujutsu-kaisen-doblaje-latino/) |
| **Aoi Todo** | **Carlos Mireles** | Subaru Kimura | Hero Network, Chirchi |
| **Suguru Geto** | **Christian Strempler** | Takahiro Sakurai | Dubbing Database |
| **Mahito** | **Ricardo Bautista** | Nobunaga Shimazaki | Dubbing Database |
| **Toji Fushiguro** | **Erick Selim** | Takehito Koyasu | Dubbing Database |
| **Choso** | **Fabián Rétiz** | Daisuke Namikawa | Hero Network, Chirchi |
| **Rika Orimoto** | **Itzel Mendoza** | Kana Hanazawa | Somos Kudasai, Hero Network |
| **Naoya Zenin** (T3) | **José Luis García** | Kōji Yusa | Hero Network, Chirchi |

**Tercera fuente** (2.º ayudante): [ANMTV, elenco de JJK0](https://www.anmtvla.com/2022/03/jujutsu-kaisen-0-conoce-el-elenco.html)
(mar-2022) confirma **Gojo (José Vilchis), Yuta (Diego Ramora), Rika
(Itzel Mendoza), Inumaki (Ángel Rodríguez), Panda (Roberto Cuevas) y
Geto (Christian Strempler)**, con Audiomaster Candiani, dirección de
Patricia Acevedo y adaptación de Jaime Chaparro ✅. Para Maki escribe
«**Anette García**», como la nota de Crunchyroll; Doblaje Wiki y Dubbing
Database dicen «Anette Ugalde» ⚠️.

**Cambios de voz que el fandom comenta** ✅ (Doblaje Wiki):
- **Sukuna**: tras la muerte de Osvaldo Trejo, la voz nueva se eligió
  **con sugerencias de los fans en redes**, que llegaron al director.
- **Mechamaru**: Patricio Pedret dejó el papel (ahora trabaja en Amazon
  Studios); lo hace Pablo Mejía.
- **Kirara**: polémica porque lo dobla un hombre (Luis Leonardo Suárez).

### 10.3 Cómo se tradujo (lo que un fan latino reconoce)

| En japonés | Doblaje latino | Fuente |
|---|---|---|
| 領域展開 | **Extensión de Dominio** (T1) → **Expansión de Dominio** (T2) | Doblaje Wiki |
| 無量空処 | **Vacío Infinito** (T1) → **Vacío Inconmensurable** (T2) | Doblaje Wiki |
| 呪術 | **Hechicería** (T1) → **Brujería** (T2) | Doblaje Wiki |
| 両面宿儺 | **el Espectro de Dos Caras** | sinopsis oficial de Crunchyroll (Cine Premiere) y sub. del tráiler |
| 東京都立呪術高等専門学校 | **Preparatoria de Hechicería de Tokio** (en la sinopsis: «Escuela Técnica de Hechicería de Tokio») | Doblaje Wiki + Cine Premiere |
| 無下限 | **Infinito** (serie) / **Sin límites** (JJK0) | Doblaje Wiki (JJK0) |
| じゅじゅさんぽ | **Juju-Cortos** (los minicapítulos tras el ending) | Doblaje Wiki |
| 黒閃 | **Destello Negro** | Doblaje Wiki (errores, ep. 45) |

**Apoyo indirecto** al cambio «Extensión» → «Expansión» (3.er ayudante;
son **subtítulos** de Crunchyroll, no el doblaje): el clip oficial de la
T1 se titula «[La Extensión de Dominio de Mahito](https://www.youtube.com/watch?v=quOC25SCykg)
(sub. español)», y el tráiler de 2025 de *Ejecución* subtitula
«**Expansión de Dominio.**» ([x9s6mua, 0:12](https://www.dailymotion.com/video/x9s6mua?start=12)).
Cuadra con Doblaje Wiki, pero el doblaje en sí ⚠️ sigue sin oírse.

### 10.4 Frases del doblaje, textuales

Cómo las saqué: **subtítulos automáticos de YouTube** de los clips
oficiales de *Crunchyroll en Español* (tienen errores; corrijo sólo lo
obvio y lo marco) y **Whisper** (reconocimiento de voz) sobre el audio
de dos clips doblados de Dailymotion. ✅ = lo dicen dos
transcripciones distintas o el vídeo lo confirma.

| Quién (voz) | Frase | Vídeo y minuto | Estado |
|---|---|---|---|
| Gojo (Vilchis), en la celda | «**Satoru Gojo. Me encargo de los de primer año de la Preparatoria de Hechicería.**» | [x7xmacu, 0:28](https://www.dailymotion.com/video/x7xmacu) | ✅ Whisper *small* y *medium* coinciden |
| Gojo (Vilchis) | «**No puedes darte el lujo de pensar en otros, Yuji Itadori. Tu ejecución secreta ya se determinó.**» | [x7xmacu, 0:43-0:49](https://www.dailymotion.com/video/x7xmacu) | ✅ las dos pasadas |
| Gojo (Vilchis), a Yuji | «Buenos días. ¿Y cuál de los dos serás ahora?» | [x7xmacu, 0:02](https://www.dailymotion.com/video/x7xmacu) | ✅ las dos pasadas |
| Nanami (Hernández) | «Lo primero es saludar. Mucho gusto.» | [HSZPNTXO-cw, 0:26](https://www.youtube.com/watch?v=HSZPNTXO-cw&t=26) | ⚠️ subtítulo automático |
| Nanami (Hernández) | «Al estudiar en la preparatoria de hechicería **descubrí que los hechiceros son un asco**. Y tras trabajar en cierta compañía, **descubrí que trabajar es un asco**.» | [HSZPNTXO-cw, 0:28-0:46](https://www.youtube.com/watch?v=HSZPNTXO-cw&t=28) | ✅ lo confirma el título oficial del clip: «Trabajar es un asco» |
| Nanami (Hernández) | «Detesto cómo actúan los peces gordos, pero sí creo en las reglas y las normas.» | [HSZPNTXO-cw, 1:09](https://www.youtube.com/watch?v=HSZPNTXO-cw&t=69) | ⚠️ automático |
| Gojo (Vilchis), a Jogo | «Aunque el infinito está presente en todos lados, mi hechicería siempre lo trae a la realidad.» | [5Cvr1rxoD9Y, 0:55](https://www.youtube.com/watch?v=5Cvr1rxoD9Y&t=55) | ⚠️ automático |
| Gojo (Vilchis), a Jogo | «No paras, sino que vas más lento cuanto más te acercas.» | [5Cvr1rxoD9Y, 0:10](https://www.youtube.com/watch?v=5Cvr1rxoD9Y&t=10) | ⚠️ automático |
| Yuji (Fortuny), club de ocultismo | «Sé que puse Club de Ocultismo.» / el entrenador: «¡Itadori! ¡Debe ir por el Campeonato Nacional!» | [x7xm8gi, 0:21-0:28](https://www.dailymotion.com/video/x7xm8gi) | ⚠️ una pasada de Whisper |
| El presentador (ep. 52) | «**Nuestro querido gallo Itadori**» («gallo» es el mote de los fans latinos para Yuji) | T3, ep. 52 | ✅ Doblaje Wiki |
| Kogane (ep. 54) | «**¡Eso es todo, amigos!**» (guiño a Porky) | T3, ep. 54 | ✅ Doblaje Wiki |
| Momo (ep. 17) | llama al mazo de juguete de Nobara «un **chipote chillón**» | T1-17 | ✅ Doblaje Wiki |
| Geto a Gojo (ep. 25) | «**Qué otaku te oíste**» (Gojo nombra a Koromon y MetalGreymon) | T2-1 | ✅ Doblaje Wiki |
| Hazenoki (ep. 57) | «El jutsu más importante fue… las mil sombras del siempre sucio» (guiño a Naruto) | T3, ep. 57 | ✅ Doblaje Wiki |

**Muestras de voz de Doblaje Wiki** (2.º ayudante): la ficha de la
serie trae **un audio corto por personaje**, sacado del doblaje. Los bajé
por la API (`imageinfo`) y los pasé por **Whisper *small* y *medium***
(`faster-whisper`, en español). ✅ = las dos pasadas dicen lo mismo. La
ficha **no dice de qué episodio** es cada audio.

| Quién (voz) | Frase textual | Estado |
|---|---|---|
| **Inumaki** (Ángel Rodríguez) | «**Copos de bonito, salmón, atún, huevas de salmón, atún y mayonesa, hojuelas de bonito**» | ✅ «copos de bonito», «salmón», «huevas de salmón», «hojuelas de bonito»; ⚠️ «atún» (las pasadas oyen «matún», «batún», «tuna») |
| **Panda** (Roberto Cuevas) | «**En realidad, el primer día son combates grupales y el segundo individuales.**» | ✅ (Panda **explicando** el evento de intercambio) |
| **Gojo** (Vilchis) | «Puede comunicarse claramente pese a ser un espíritu maldito, y ni hablar de su cantidad de energía maldita. ¿Una categoría especial sin registrar?» | ✅ |
| Gojo joven (Vilchis) | «Sí, la barrera de esa maldición también alteraba el tiempo. Son raras, pero a veces hay de esas.» | ✅ |
| **Yuji** (Fortuny) | «Por ciertas circunstancias, últimamente veo muchas películas. Eso sí, no las veo en el cine.» | ✅ |
| **Nobara** (Rivera) | «¿Y qué se hace en ese evento? ¿Juegan a Smash Bros? En el de Wii los destrozaré. **Volarán y no volverán.**» | ✅ salvo «de Wii» ⚠️ |
| **Sukuna** (Trejo, T1) | «¡Qué bien se siente la luz contra la piel! La carne de un espectro no tiene gracia. ¿Dónde está la gente? ¿Y las mujeres?» | ✅ |
| **Todo** (Mireles) | «Olvídalo. A diferencia de ti, tengo asuntos importantes en Tokio. Voy a estrechar la mano de mi linda Takada.» | ✅ salvo «Takada» ⚠️ (oyen «atacada» y «tacada») |
| Ijichi | «Son funcionarios de la preparatoria capaces de ver maldiciones.» | ✅ |

**Otra frase textual del doblaje, en dos fuentes** ✅: el presentador
del club de lucha (T3): «Por un lado, el joven sicario que más bien
parece becario. **Nuestro querido gallo, Yuji Itadori**»
([3DJuegos LATAM, 20-feb-2026](https://www.3djuegos.lat/anime/doblaje-jujutsu-kaisen-hizo-canon-meme-popular-fandom-mexico-gallo-itadori-realidad)
+ Doblaje Wiki). Doblaje Wiki dice **ep. 52**; 3DJuegos, «capítulo 6
con doblaje de la tercera temporada» ⚠️ (numeración distinta).

**Subtítulos oficiales en español** (no doblaje) del tráiler 1, leídos
en pantalla: «No te preocupes. **No hay nadie más fuerte que yo**»
(Gojo), «Ayudaré a las personas como quiera» (Megumi), «Esto es para
poder seguir siendo quien soy» (Nobara), «No quiero tener que
arrepentirme por cómo viví» (Yuji), «Adelante. **Elige el infierno que
prefieras**» ([Dailymotion x88ah25, 0:38-1:06](https://www.dailymotion.com/video/x88ah25)) ✅ visto.

**Lo que NO encontré**: un clip oficial doblado del «¿Qué tipo de chica
te gusta?» de Todo, ni la frase latina de Inumaki en su escena de T1-5
(16:48). Sus **palabras de onigiri en latino** sí salen en la muestra de
Doblaje Wiki (arriba): **«salmón», «huevas de salmón», «copos de
bonito», «hojuelas de bonito»**. Antes de rotular «atún con mayonesa» en
una lámina, hay que oírlo en Crunchyroll (T1-5, 16:48).

### 10.5 Los actores cuentan su trabajo

De la entrevista de [Cultura Geek](https://culturageek.com.ar/jujutsu-kaisen-termino-la-primer-temporada-y-sus-actores-de-doblaje-en-espanol-latino-nos-cuentan-sus-secretos/) (2021) ✅:
- **Enzo Fortuny**: con la directora, Paty Acevedo, decidió que Yuji
  **no sonara nada a Inuyasha**. Los «saltos» de tono son a propósito:
  «está muy reflexivo y de pronto está jugando».
- **Pepe Vilchis**: Gojo «es bonachón, le gusta hacer bromas», pero en
  pelea da «un giro de 180 grados». «Nunca nos hubiéramos imaginado
  que tuviera ojos, porque siempre los tiene tapados».
- Vídeo: [Entrevista al elenco, Crunchyroll VIVO](https://www.youtube.com/watch?v=IjONEwQpsMU) (1 h 10 min; no la pude ver desde aquí).

## 11 · Música

Lista de la [Jujutsu Kaisen Wiki](https://jujutsu-kaisen.fandom.com/wiki/Jujutsu_Kaisen_(Anime)) ✅,
cruzada con los títulos de los vídeos de TOHO animation en YouTube ✅.

| Tramo | Opening | Ending |
|---|---|---|
| T1, 1.ª parte (eps. 1-13) | «**Kaikai Kitan**» (廻廻奇譚), Eve | «**LOST IN PARADISE** feat. AKLO», ALI |
| T1, 2.ª parte (eps. 14-24) | «**VIVID VICE**», Who-ya Extended | «**give it back**», Cö shu Nie |
| T2, Gojo del pasado (eps. 25-29) | «**Ao no Sumika**» (青のすみか), Tatsuya Kitani | «**Akari**» (燈), Soushi Sakiyama |
| T2, Shibuya (eps. 30-47) | «**SPECIALZ**», King Gnu | «**more than words**», Hitsujibungaku |
| T3, Juego del Sacrificio (eps. 48-59) | «**AIZO**», King Gnu | «**Yoake no Uta**», jo0ji |
| Película JJK0 | «**Ichizu**» (一途), King Gnu: el tema de la peli ✅ (wiki, 2.º ayudante) | «**Sakayume**» (逆夢), King Gnu ✅ (wiki: la ficha pone los dos como temas de cierre) |

**Canciones de dentro de la serie** ✅ (wiki): «Stand In The Darkness»
(Steve Memmolo), «REMEMBER» (Masato Hayakawa) y «Climax☆JUMPING!»,
que canta **Tomoyo Kurosawa**, la voz de la idol **Takada-chan**, la
obsesión de Todo.

**Banda sonora** ✅ (wiki, ficha del anime): T1, **Hiroaki Tsutsumi,
Yoshimasa Terui y Arisa Okehazama**; T2 y T3, **Yoshimasa Terui**.

### 11.1 Qué ambiente dan (lo que vi en los vídeos)

- **Kaikai Kitan**: nervioso y urbano. Tokio de noche como un **mapa de
  circuitos**, trenes, pasillos vacíos, luces rosas y verdes. Termina en
  un **picnic bajo los cerezos**: la familia que se pierde después.
- **LOST IN PARADISE**: el contrapunto. **Jazz-rap relajado**, colores
  planos, ropa de calle, cada uno sale por su puerta. Es el JJK
  «de descanso» ⚠️ (el género, de oídas).
- **SPECIALZ**: Shibuya de noche, rojo y cian, todo roto. El tono de la
  T2.
- **Pistas de la banda sonora** que suben fans a Dailymotion (repyh13):
  «**Working Overtime**» (el tema de Nanami, x9gpjoi), «Blood»,
  «Takagi vs Itadori». El título «Working Overtime» confirma que
  Nanami tiene **su propio tema de horas extra** ⚠️ (subida de fan).

### 11.2 Qué música pega a cada lámina

| Lámina | Música que evoca | Por qué |
|---|---|---|
| ➕ Crear sala (dominio) | el momento del **Vacío Infinito** (T1-7) | silencio, espacio, estrellas |
| Inumaki y el megáfono | SPECIALZ | Shibuya, la T2 |
| 🍟 General (voz), el picnic | LOST IN PARADISE / el final de Kaikai Kitan | descanso, amigos |

## 12 · Vídeos

**Cómo los miré.** YouTube no dejó bajar vídeo desde aquí (403 y «no
soy un robot»), pero **sí** dejó bajar **subtítulos** a ratos.
Dailymotion sí dejó bajar vídeo: con `herramientas/fotogramas.py` saqué
hojas con número y minuto, **las abrí y las miré**, y saqué fotogramas
grandes de lo importante. Cada vídeo lleva **el enlace oficial** (si
existe) y **la copia que miré** (mismo montaje; el minuto puede variar
±1 s). Los vídeos se borraron después.

### 12.0 Lo que volví a mirar yo (2.º ayudante, 24-sep-2026) ✅

`python3 herramientas/fotogramas.py "<url>" --cada 2` (o 3) sobre las
copias de Dailymotion; **abrí cada hoja** y saqué en grande lo
importante (`--fotograma`). YouTube dio «Sign in to confirm you're not
a bot» a `yt-dlp`, así que no hubo copia oficial.

- **Resolución**: desde aquí Dailymotion sólo da **512×288** (`yt-dlp -F`
  lista un único formato). Los fotogramas sirven para **pose, luz,
  color y minuto**, **no para recortar**: para recortar, el arte de la
  wiki (§3) o el episodio en Crunchyroll a 1080p.
- **Enlaces con minuto**: en Dailymotion el parámetro es `?start=<segundos>`
  (el 2.º ayudante cambió los `?t=` del 1.º a `?start=`).

| Vídeo | Copia | Hoja | Lo que confirmé o encontré |
|---|---|---|---|
| Opening 1 | [x84iff2](https://www.dailymotion.com/video/x84iff2) | 46 fotogramas cada 2 s | ✅ todos los minutos del 1.er ayudante (logo 0:12-0:16, Nanami en el café 0:34, Gojo 0:42 y 0:52, Megumi 1:06, Yuji 1:12, hanami [1:16](https://www.dailymotion.com/video/x84iff2?start=76), Sukuna 1:22). Nuevo: **Inumaki grita con el sello en la mejilla** ([1:02](https://www.dailymotion.com/video/x84iff2?start=62)); Maki en un parque (0:36) |
| Ending 1 | [x80jy2b](https://www.dailymotion.com/video/x80jy2b) | 51 cada 2 s | ✅ las puertas y colores (Yuji 0:06-0:22, Megumi 0:24-0:38, Nobara 0:40-0:54, Gojo 0:56-1:10). Nuevo: Gojo **se prueba gafas de una estantería** (1:02); Maki (1:12); Panda con globos (1:14); **Inumaki comiendo un onigiri**, con arroz en la mejilla, sudadera verde azulado sin mangas y mochila ([1:16](https://www.dailymotion.com/video/x80jy2b?start=76)); Nanami cenando **filete con copa de vino**, corbata roja (1:18); Ijichi **quitando el polvo a su coche negro con un plumero**, mano en la frente (1:24) |
| Tráiler «Special Lecture» (*Cursed Clash*) | [x8scngs](https://www.dailymotion.com/video/x8scngs) | 83 cada 3 s + 10 grandes | ✅ pizarra (0:18-0:54, 1:24). Nuevo: **caja de diálogo del modo historia** (3:06-3:09), **«Relationship Chart»** en la pantalla (3:12), **pantalla en blanco** con Gojo y puntero (3:21-3:24), **Online Lobby** (2:25), **frases rápidas** (2:39), elección de ropa (2:36) y el lema «**Master a New Domain**» (3:45) |
| Gojo en la celda (doblaje latino) | [x7xmacu](https://www.dailymotion.com/video/x7xmacu) | 29 cada 2 s | ✅ farolillos (0:14-0:16), pared de ofuda (0:18-0:20), vista cenital (0:44). **Corrijo**: Gojo está **sentado al revés en la silla** ([0:49](https://www.dailymotion.com/video/x7xmacu?start=49)), no «de lado» |
| Gojo contra Jogo (T1-7, sub. inglés) | [x7yt0gp](https://www.dailymotion.com/video/x7yt0gp) | 90 cada 3 s | ✅ manos juntas (0:30), apretón de manos (1:27), índice (1:39), «This is Itadori Yuuji-kun» (2:12), mano en la venda (3:03), ojos (3:39). La frase de la venda es la clave: «**The most effective way to deal with a Domain is to lay out your own Domain**» (3:00-3:03) |
| Dominio de Gojo (T1-7, otra copia) | [x7xhwib](https://www.dailymotion.com/video/x7xhwib) | 60 cada 2 s | nuevo: el **signo de manos del dominio**: mano derecha a la altura de la cara, **índice y corazón cruzados**, venda bajada al cuello ([0:33](https://www.dailymotion.com/video/x7xhwib?start=33)) |
| Yuji y Todo contra Hanami (T1-19) | [x80pjbn](https://www.dailymotion.com/video/x80pjbn) | 86 cada 3 s | ✅ tejados rojos, Maki (0:48), Yuji y la capucha (1:42), las manos de Todo (2:18). Nuevo: **Inumaki con sangre en la boca** y el sello (0:09) y Megumi que le sujeta: «Inumaki-senpai…» (0:33): **la voz dañada** |
| Tráiler 1 (sub. oficial en español, Crunchyroll) | [x88ah25](https://www.dailymotion.com/video/x88ah25) | 55 cada 2 s | ✅ todas las frases de §10.4. Nuevo: Gojo, «**Es un buen momento para enseñarte… qué significa "jujutsu" en realidad**» (1:14-1:20); créditos: Park Sunghoo (0:16), Seko Hiroshi (0:22), Hiramatsu Tadashi (0:28), MAPPA (0:32) |
| Tráiler de JJK0 (sub. en español, Tomatazos) | [x8x3x96](https://www.dailymotion.com/video/x8x3x96) | 44 cada 3 s | Yuta **en la misma celda de ofuda** (0:45, 0:48); **Panda, Maki e Inumaki** en el aula de madera, Inumaki **subiéndose la bufanda de cuadros** (0:51): «No es un lugar para los malditos»; Geto ante un muro de caligrafía (1:03) |
| «Yuji Meets Inumaki» | [x9830ho](https://www.dailymotion.com/video/x9830ho) | 29 cada 2 s | **no sirve**: es un montaje vertical de fans con letras rosas y azules. Lo descarto |
| Tráiler de ***JUJUTSU KAISEN: Ejecución*** (subtítulos en español; 3.er ayudante) | [x9s6mua](https://www.dailymotion.com/video/x9s6mua) (oficial: [Crunchyroll en Español, OknvvwMcXa4](https://www.youtube.com/watch?v=OknvvwMcXa4), 1:26) | 43 cada 2 s + 4 grandes | es la **película recopilatoria de Shibuya + preestreno de la T3** (en Japón, 『劇場版 呪術廻戦「渋谷事変 特別編集版」×「死滅回游 先行上映」』, en cines desde el 7-nov ✅ título del PV en la wiki). Visto: Gojo **se tapa un ojo con la mano** y el subtítulo «**Expansión de Dominio.**» con el crédito «King Gnu「SPECIALZ」» en serif abajo a la derecha ([0:12](https://www.dailymotion.com/video/x9s6mua?start=12)); cartelas en serif sobre violeta (0:14-0:18); Yuji con sangre: «Itadori, encárgate tú desde ahora» (0:34); Yuta: «Vamos, Rika» (1:12); el **logo en español** (1:14, §6.1). ⚠️ El giro «¡Vamos a darle más caña, Itadori!» (0:26) suena a subtítulo **de España**, no latino |

Los `video.mp4` se borraron al terminar las hojas.

### 12.1 Los que miró el 1.er ayudante fotograma a fotograma

| Vídeo | Oficial | Copia mirada | Lo que se ve (minuto de la copia) |
|---|---|---|---|
| **Opening 1** «Kaikai Kitan» (Eve), sin créditos | [TOHO animation](https://www.youtube.com/watch?v=v8bZVdTgXoY) (1:31) | [Dailymotion x84iff2](https://www.dailymotion.com/video/x84iff2) | Yuji sentado en un vagón vacío (0:02); **logo 呪術廻戦 amarillo sobre un mapa de Tokio con luces rosas** ([0:14](https://www.dailymotion.com/video/x84iff2?start=14)); Nobara de perfil (0:28); Panda (0:32); Nanami leyendo en un café (0:34); Gojo con la venda en un puente, de noche (0:42 y 0:52); Megumi haciendo el **perro con las manos** (1:06); Yuji con la palma abierta (1:12); **hanami con todos** ([1:16](https://www.dailymotion.com/video/x84iff2?start=76)); Yuji riendo con Junpei (1:18); Sukuna sonriendo (1:22) |
| **Ending 1** «LOST IN PARADISE» (ALI feat. AKLO) | [TOHO animation](https://www.youtube.com/watch?v=AWEm4tA2hMc) (1:31) | [Dailymotion x80jy2b](https://www.dailymotion.com/video/x80jy2b) | dibujo de línea suelta con **manchas de color**, ropa de calle. Yuji sale por una puerta sobre turquesa `#50CDCF` ([0:10](https://www.dailymotion.com/video/x80jy2b?start=10)); Megumi sobre amarillo `#FBE63B` (0:28); Nobara con **bolsas de compras** sobre rojo `#DF4456` ([0:40](https://www.dailymotion.com/video/x80jy2b?start=40)); Gojo sobre gris `#515151`, **probándose gafas de sol** (0:58-1:02); Maki (1:12); **Panda con globos** (1:14); Inumaki comiendo un onigiri (1:16); **Nanami cenando con copa de vino** (1:18) |
| **Tráiler 1** de la serie (Crunchyroll, subtítulos en español) | [Crunchyroll en Español](https://www.youtube.com/watch?v=aPBUUJbrAWo) (1:49) | [Dailymotion x88ah25](https://www.dailymotion.com/video/x88ah25) (Sensacine México) | **farolillos y ofuda** en la celda (0:16); Gojo: «No te preocupes. No hay nadie más fuerte que yo» (0:38-0:40); Megumi: «Ayudaré a las personas como quiera» (0:42); Nobara: «Esto es para poder seguir siendo quien soy» (0:46); Yuji: «No quiero tener que arrepentirme por cómo viví» (0:50); **muro de kanji negativos** (0:48); logo con «Jujutsu Kaisen» en romaji (1:10); cartela «少年は戦う―「正しい死」を求めて» → «Un joven lucha… por "la muerte correcta"» (1:18) |
| **Tráiler de Shibuya** (T2, PV 3, con «SPECIALZ») | [TOHO animation](https://www.youtube.com/watch?v=PKHQuQF1S8k) (1:26) | [Dailymotion x8ngqml](https://www.dailymotion.com/video/x8ngqml) | Shibuya de noche, sitios reales: el cruce (0:14), la **estatua de Hachikō** junto a la estación ([0:10](https://www.dailymotion.com/video/x8ngqml?start=10)); Gojo sin venda y con sangre (0:36); Nanami con gafas (0:54); Yuji gritando (1:08); logo dorado con «渋谷事変» (1:12) |
| **Tráiler de JJK0** (versión de **España**, no latina) | — | [Dailymotion x8ake5m](https://www.dailymotion.com/video/x8ake5m) | Rika niña con el anillo (0:04-0:14); **puerta torii de la escuela** (0:32); Gojo con la venda de tela (0:46); Panda, Maki e Inumaki (0:52); Geto sonriendo (1:28). Transcrito con Whisper: «¿vale?», «tened cuidado»: **es el doblaje de España** |
| **Tráiler «Special Lecture»** del juego *Cursed Clash* | Bandai Namco | [Dailymotion x8scngs](https://www.dailymotion.com/video/x8scngs) | **Gojo con puntero ante una pizarra** ([0:21](https://www.dailymotion.com/video/x8scngs?start=21)); tiza «Cursed Energy Is the Key to Battle» ([1:24](https://www.dailymotion.com/video/x8scngs?start=84)); la interfaz: placas **hexagonales cian** `#12A2E4` (1:30); menú «Online Versus» (2:03); tabla de niveles (2:15) |

### 12.2 Tres escenas icónicas, miradas

| Escena | Oficial | Copia mirada | Lo que se ve |
|---|---|---|---|
| **Gojo contra Jogo** (T1-7) | [Crunchyroll, sub.](https://www.youtube.com/watch?v=fcxZDSA8rPs) · [doblaje](https://www.youtube.com/watch?v=5Cvr1rxoD9Y) | [Dailymotion x7yt0gp](https://www.dailymotion.com/video/x7yt0gp) (sub. inglés) | Gojo **junta las manos** sonriendo (0:30); **le da la mano** a Jogo (1:27); **señala con el índice**: «el infinito está en todas partes» (1:39); carga a Yuji del cuello de la ropa: «Él es Yuji, viene a mirar» (2:12); **se tapa la venda con la mano** antes del dominio (3:03); **sin venda, ojos azules** (3:39); el ojo en primerísimo plano (3:45) |
| **Gojo despierta** (T2-4, ep. 28) | — | [Dailymotion x8yav0m](https://www.dailymotion.com/video/x8yav0m) | Gojo de uniforme viejo, **brazos abiertos** en luz dorada (0:10); **ojo azul enorme** (0:14); mariposa verde (0:24); **mano en la frente, riéndose**: «Throughout Heaven and Earth…» ([0:36](https://www.dailymotion.com/video/x8yav0m?start=36)); Púrpura (1:26) |
| **Yuji y Todo contra Hanami** (T1-19) | [Crunchyroll, sub.](https://www.youtube.com/watch?v=ZmC2sN9VhPo) | [Dailymotion x80pjbn](https://www.dailymotion.com/video/x80pjbn) | tejados rojos de la escuela (0:00-0:15); Maki con la lanza roja (0:48); Todo de espaldas, **sin camisa** (1:33); Yuji se sube la capucha (1:42); **Todo junta las manos: «Congratulations, brother»** ([2:48](https://www.dailymotion.com/video/x80pjbn?start=168)) = T1-19 15:57; los dos lado a lado, listos (2:57) |
| **Nanami, el final** (T2-18, ep. 42) | — | [Dailymotion x8upb66](https://www.dailymotion.com/video/x8upb66) | estación de Shibuya con carteles amarillos; Nanami medio quemado, sonriendo: «Lo demás te lo dejo a ti» (0:18) |

### 12.3 Clips con **doblaje latino** (los que tienen texto)

| Clip | Enlace | Cómo saqué el texto |
|---|---|---|
| «Trabajar es un asco» (Nanami, T1-9) | [Crunchyroll en Español](https://www.youtube.com/watch?v=HSZPNTXO-cw) | subtítulos automáticos de YouTube |
| «Gojo vs Sukuna» (T1-2) | [Crunchyroll en Español](https://www.youtube.com/watch?v=BxJZhkxnQHE) | subtítulos automáticos (muy malos) |
| «Gojo vs Jogo» (T1-7) | [Crunchyroll en Español](https://www.youtube.com/watch?v=5Cvr1rxoD9Y) | subtítulos automáticos |
| «Comida de dedo» (T1-1) | [Crunchyroll en Español](https://www.youtube.com/watch?v=r9IZGchjcO8) | subtítulos automáticos |
| Gojo visita a Yuji en la celda (T1-1/2) | [Dailymotion x7xmacu](https://www.dailymotion.com/video/x7xmacu) | **vídeo mirado** + audio transcrito con Whisper |
| El club de ocultismo (T1-1) | [Dailymotion x7xm8gi](https://www.dailymotion.com/video/x7xm8gi) | **vídeo mirado** + Whisper |

Las frases, en §10.4.

### 12.4 Otros vídeos útiles (sólo datos)

| Vídeo | Enlace | Para qué |
|---|---|---|
| Episodio 1 completo, **doblaje latino** (24:15) | [Crunchyroll en Español](https://www.youtube.com/watch?v=6Tn55tBUdOE) | bloqueado por país desde aquí; en Latinoamérica se ve gratis |
| Tráiler de streaming de JJK0, **doblaje latino** (2:01) | [Crunchyroll en Español](https://www.youtube.com/watch?v=6h632Vnn4yo) | bloqueado por país desde aquí |
| «¡Me gusta ser fuerte!» (doblaje, 2:00) | [Crunchyroll en Español](https://www.youtube.com/watch?v=midsxR9BLD0) | YouTube pidió «no soy un robot» |
| Entrevista al elenco (Crunchyroll VIVO, 1 h 10 min) | [YouTube](https://www.youtube.com/watch?v=IjONEwQpsMU) | para oír a los actores |
| Openings sin créditos T1-T3 | [VIVID VICE](https://www.youtube.com/watch?v=8nNujr378EA) · [Ao no Sumika](https://www.youtube.com/watch?v=gcgKUcJKxIs) · [SPECIALZ](https://www.youtube.com/watch?v=5yb2N3pnztU) · [AIZO](https://www.youtube.com/watch?v=Xr032EhUDPw) | todos de TOHO animation, 1:31 |

### 12.5 Tendencias (TikTok y YouTube)

- **El baile del ending 1**: hay versiones «en la vida real» del baile
  de «LOST IN PARADISE» ([ejemplo en YouTube](https://www.youtube.com/watch?v=obN-3JaQVO8)) ⚠️ una fuente.
- **«Domain Expansion»**: el gesto de las manos de Gojo (índice y
  medio cruzados) es un reto de TikTok y de fotos ⚠️ (visto en las
  búsquedas de Dailymotion: «Domain Expansion OR Ryoiki Tenkai», x9k0va4).
- **Edits y AMV** de Gojo, Sukuna y Nanami: son la mayoría de los
  resultados en Dailymotion (Animity, AK_Anime, VenomXGaming).

## 13 · Videojuegos de la franquicia

Datos de la **API de la tienda de Steam** (México, en español) ✅ y de
lo que vi.

| Juego | Año, estudio | Idioma | Lo que importa para la lámina |
|---|---|---|---|
| ***Jujutsu Kaisen Cursed Clash*** | 1-feb-2024; Byking, Bandai Namco ([Steam 1877020](https://store.steampowered.com/app/1877020/)) | textos en **español de Hispanoamérica**; voces sólo en inglés y japonés | tráiler **«Special Lecture»**: **Gojo profesor** con puntero ante una pizarra; placas **hexagonales cian**; menú «Online Versus». Tiene un DLC: **«Conjunto de ropa del tema final 1 del anime»** (la ropa de calle del ED1) y otro de la ropa de 1.er año de la «Preparatoria de Hechicería» |
| ***Jujutsu Kaisen Phantom Parade*** | móvil 2023; en Steam desde 27-feb-2026 (Bilibili, [Steam 4224240](https://store.steampowered.com/app/4224240/)) | textos en **español de Hispanoamérica** | historia del anime **con voces nuevas**; arte horizontal por personaje (#132-136) |
| ***JUJUTSU KAISEN RUMBLE: SURVIVATON*** | 2027; poncle (los de *Vampire Survivors*), Shueisha Games ([Steam 4753290](https://store.steampowered.com/app/4753290/)) | español de España, no latino | aún no sale |

**Cómo es la caja de *Cursed Clash*** (medida en el tráiler, 1:30) ✅:
placa del jugador **hexagonal alargada** con borde **cian `#12A2E4`**,
retrato a la izquierda y nombre en blanco («Kento Nanami»), sobre azul
noche `#181E2A`. La ayuda sale en una banda: título cian con icono
(«Cursed Energy Gauge») y la frase en blanco. Es **muy «videojuego»**:
para una lámina 2 (etiquetas, niveles), no para la principal.

**La pizarra de la «Special Lecture»** ✅: gris verdosa `#36362F`, marco
de madera `#30241E`, tiza `#DDD2CC` en **serif clásica**, el logo del
juego arriba; Gojo con **venda**, de medio cuerpo, con un **puntero
largo** en la mano derecha (tráiler, 0:18-0:54).

**La caja del modo historia de *Cursed Clash*** ✅ (2.º ayudante,
tráiler [3:06-3:09](https://www.dailymotion.com/video/x8scngs?start=189)):
**dos fotogramas del anime recortados con el borde rasgado**, en
diagonal, y la frase **al lado de cada uno**, en sans blanca, sobre
**tinta azul petróleo** (`#314953`, `#202C33`, `#4C656D`). Es la caja
**más propia** de la franquicia que encontré: sirve de cuadro de
diálogo en una lámina (concepto C).

**El lobby en línea** ✅ ([2:25](https://www.dailymotion.com/video/x8scngs?start=145)):
«ONLINE / Online Lobby», los jugadores andan por un cruce morado de
noche, con un menú «Stamp · Tactics · Talk · Unique»; y **frases
rápidas** numeradas del 1 al 8 en casillas azul noche `#121D2A` con un
icono de bocadillo cian ([2:39](https://www.dailymotion.com/video/x8scngs?start=159)).
Es **la «sala» oficial** del juego: otra idea para CREAR SALA.

**The Cutting Room Floor**: 403 desde aquí, y la Wayback Machine está
bloqueada por la red del contenedor (el 2.º ayudante lo reintentó dos
veces: el túnel se corta). ⚠️ No pude mirar contenido descartado.

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todo fan reconoce (con su minuto)

| Meme o momento | Dónde | Por qué gusta | Fuentes |
|---|---|---|---|
| **«Tranquilo. Soy el más fuerte»** | T1-2, 1:29 | Gojo en una frase | sub. con tiempos ✅; sub. oficial ES del tráiler: «No hay nadie más fuerte que yo» (0:38, visto) ✅ |
| **«Nah, I'd win»** (勝つさ, «Ganaría») | T1-2, **14:32** (Yuji: «¿Perderías?» Gojo: «勝つさ»); en el manga vuelve en el **cap. 221**, antes de su pelea con Sukuna | la frase se volvió **chiste** porque en el manga pierde. El fandom la pone en todo | sub. ✅ + [pixiv百科「勝つさ」](https://dic.pixiv.net/a/%E5%8B%9D%E3%81%A4%E3%81%95) y [ciatr (ja)](https://ciatr.jp/topics/326274) + [Sportskeeda](https://sportskeeda.com/anime/nah-i-d-win-jujutsu-kaisen-fans-turn-one-iconic-dialogues-cursed-meme) ✅ |
| **«En el cielo y en la tierra, sólo yo soy el honrado»** (天上天下 唯我独尊) | T2-4 (ep. 28), 16:54 | Gojo joven renace, **mano en la frente riéndose** (visto en copia, 0:36) | sub. ✅ + vídeo ✅ |
| **«¿Eres el más fuerte porque eres Satoru Gojo…?»** | T2-5 (ep. 29), 16:56 | Geto; el fandom lo reescribe con cualquier cosa (Fandom: «Are you the nah id win because…») | sub. ✅ + [foro de la wiki](https://jujutsu-kaisen.fandom.com/f/p/4400000000000048141) ✅ |
| **«Siéntete orgulloso»** («Stand proud», 誇れ) | T2-16 (ep. 40), **21:09**: Sukuna a Jogo, «de los que luché hace mil años, fuiste de los mejores» | el villano que **reconoce** al rival | sub. ✅ + [Sportskeeda](https://www.sportskeeda.com/anime/stand-proud-strong-sukuna-s-famous-quote-jujutsu-kaisen-explained) ✅ |
| **«¿Qué tipo de chica te gusta?»** | T1-8, 5:54 | Todo; en Reddit, «THINK YUJI, THINK. WHAT TYPE OF WOMAN IS YOUR TYPE?» tiene **2.516 votos** | sub. ✅ + [Arctic Shift](https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=JuJutsuKaisen&title=what%20type%20of%20woman) ✅ |
| **Las horas extra de Nanami** | T1-9, 8:49 y T1-10, 21:12 | el oficinista cansado; «Nanami Kento - Overtime», **3.783 votos** | sub. ✅ + Arctic Shift ✅ |
| **El conjuro de Megumi** (布瑠部由良由良, «With this treasure I summon…») | T1-5, 10:19 (lo corta); **T2-17 (ep. 41), 3:06-4:05** invoca a **Mahoraga** | el fandom lo usa para «sacar el arma secreta» | sub. ✅; el meme en inglés ⚠️ (una búsqueda sin explicación) |
| **Inumaki y sus onigiri** | T1-5, 16:48 | todos quieren saber qué significa «¡salmón!»; «Why doesn't Inumaki just use TTS», **1.057 votos** | wiki (lista oficial del tomo 0, pág. 104) ✅ + Reddit ✅ |
| **«Brother»** | T1-19, 15:57; «Thank you so much, best friend!» (copia x80pjbn, 2:21, visto) | la amistad inventada de Todo | sub. ✅ + vídeo ✅ |
| **El gesto del dominio** | T1-7 (índice y corazón cruzados, visto en x7xhwib 0:33) | la gente lo imita en fotos y TikTok | vídeo ✅; la tendencia ⚠️ (sólo títulos de Dailymotion y TikTok) |
| 🇲🇽 **«El gallo Itadori»** | T3 (ep. 52 según Doblaje Wiki) | mote **latino** de los fans; el doblaje lo hizo oficial | Doblaje Wiki + 3DJuegos LATAM ✅ |
| 🇲🇽 **Guiños del doblaje** | «chipote chillón» (ep. 17), «Qué otaku te oíste» (ep. 25), «¡Eso es todo, amigos!» (ep. 54) | el público latino los celebra | Doblaje Wiki ✅ (una fuente cada uno) |

### 14.2 Qué NO hacer (lo que un fan notaría)

- **Spoilers** en una lámina de uso diario: Nanami (T2-18), Nobara
  (T2-19), Gojo sellado en Shibuya y lo que pasa en el manga después.
  El servidor pide marcar spoilers en #que-estas-viendo. Usar el
  **look de la T1** (uniforme, venda) y nada de parches ni cicatrices.
- **Gojo sin venda por gusto**. Los ojos son **el golpe fuerte** (T1-7,
  3:39 de la copia). En la lámina «de profe» va con **venda** (como en
  *Cursed Clash*) o con **gafas redondas** (P3).
- **Inumaki hablando normal**. Sólo dice **ingredientes de onigiri**; si
  da una orden, le sangra la garganta (T1-19, visto: 0:09 y 0:33 de la
  copia). En la lámina, **Inumaki dice «¡Salmón!» y otro traduce**.
- **Sukuna de guía simpático**: es un sádico. Si sale, que sea amenaza
  cómica o lámina de reglas.
- **Megumi sonriendo mucho** o **Nobara modosita**: él es seco; ella,
  descarada.
- **Yuji pelirrojo**: su pelo es **rosa claro** (`#D8A8A0`, medido en
  #139) con la nuca **oscura y rapada**. Las **marcas negras** en la cara
  sólo cuando sale Sukuna.
- **Mezclar las traducciones del doblaje**: la T1 dijo «**Extensión** de
  Dominio» y «Hechicería»; la T2, «**Expansión** de Dominio» y
  «Brujería» (Doblaje Wiki). Elegir **la de la T2** y no mezclar.
- **El título mal escrito**: es **呪術廻戦**, con **廻**. «咒术回战» es el
  chino simplificado (sale en títulos de vídeos chinos).
- **Globo blanco redondo**, letras redondas o alegres, **Comic Sans**.
- **Arte hecho con IA**: en DeviantArt abunda (§4.2). El dueño lo nota.
- **Cambiar el gesto del dominio**: cada uno tiene el suyo, y la wiki lo
  dice: «hace falta un signo de manos propio de cada usuario»
  ([«Domain Expansion»](https://jujutsu-kaisen.fandom.com/wiki/Domain_Expansion)).
  - **Gojo**: **índice y corazón cruzados** junto a la cara (visto,
    x7xhwib 0:33) ✅.
  - **Sukuna**: el **«sello de la palma de Enma»** (閻魔天の掌印): las
    dos manos juntas delante de la cara, **las puntas de índice y corazón
    tocándose arriba** y el resto de los dedos entrelazados, como un
    tejado ✅ (3.er ayudante: visto en el fotograma
    [True Jujutsu (Anime)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/9/9b/True_Jujutsu_%28Anime%29.png),
    1920×1080, y en la viñeta del manga
    [Sukuna uses Domain Expansion against Mahoraga](https://static.wikia.nocookie.net/jujutsu-kaisen/images/8/80/Sukuna_uses_Domain_Expansion_against_Mahoraga.png);
    el nombre, en [«Malevolent Shrine»](https://jujutsu-kaisen.fandom.com/wiki/Malevolent_Shrine),
    cap. 255, págs. 15-16).
  - **Megumi**: **manos cerradas y apretadas una contra otra, dedos
    entrelazados**, delante del pecho ⚠️ (una sola fuente: el fotograma
    [Megumi satisfied with Domain Expansion (Anime)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/1/16/Megumi_satisfied_with_Domain_Expansion_%28Anime%29.png)).

## 15 · Poses analizadas por personaje

Todas **vistas**: en fotogramas de los vídeos (§12, con minuto de la
copia mirada) o en imágenes de la wiki (#N) o de mis hojas (P·, F·).
«Uso» = presentar, explicar, celebrar, regañar, pensar o animar.

### Gojo

| # | Dónde | Postura, manos, mirada | Uso |
|---|---|---|---|
| 1 | P1 (#1) | de pie, **mano derecha abierta hacia el espectador**, la otra baja; venda | **presentar** («alto, aquí se hace así») |
| 2 | T1-7, copia [0:30](https://www.dailymotion.com/video/x7yt0gp?start=30) | **manos juntas** a la altura del pecho, sonrisa ladeada | **explicar** con calma |
| 3 | T1-7, [1:39](https://www.dailymotion.com/video/x7yt0gp?start=99) | **señala con el índice**, brazo estirado | **explicar** una regla |
| 4 | T1-7, [2:12](https://www.dailymotion.com/video/x7yt0gp?start=132) | sujeta a Yuji del cuello de la ropa, cara neutra | presentar a otro («él es…») |
| 5 | T1-7, [3:03](https://www.dailymotion.com/video/x7yt0gp?start=183) | **se tapa la venda con la mano**, cabeza baja | antes de lo importante |
| 6 | T1-7, [3:39](https://www.dailymotion.com/video/x7yt0gp?start=219) | sin venda, **ojos azules**, sonrisa de lado, mirada al espectador | **el gancho** |
| 7 | *Cursed Clash*, [0:21](https://www.dailymotion.com/video/x8scngs?start=21) | medio cuerpo, **puntero** en la mano, sonrisa | **explicar** (¡la pizarra!) |
| 8 | P2 (#18) | **«V» doble**, abraza a Yuji | **celebrar**, saludar |
| 9 | P3 (#82) | **se levanta las gafas redondas** con las dos manos | «mira esto», animar |
| 10 | #618 | **brazo por encima del hombro** de Nanami, carcajada; fondo cómico con rayas | presentar a otro en broma |
| 11 | *Cursed Clash*, [3:22](https://www.dailymotion.com/video/x8scngs?start=202) | de pie a la derecha de una **pantalla en blanco**, **puntero en la mano derecha**, brazo izquierdo cruzado, sonrisa | **explicar** (el mejor para la lámina A) ✅ visto |
| 12 | celda, [0:49](https://www.dailymotion.com/video/x7xmacu?start=49) | **sentado al revés en una silla**, piernas abiertas, brazos por el respaldo, sonrisa | charlar, «a ver, cuéntame» ✅ visto |
| 13 | T1-7, [x7xhwib 0:33](https://www.dailymotion.com/video/x7xhwib?start=33) | **signo del dominio**: índice y corazón cruzados junto a la cara, ojos azules, media sonrisa | **abrir el dominio** = «crear sala» ✅ visto |

### Yuji

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | OP1, [1:18](https://www.dailymotion.com/video/x84iff2?start=78) | **carcajada** con los ojos cerrados, sentado en la hierba | **celebrar** |
| 2 | OP1, [1:12](https://www.dailymotion.com/video/x84iff2?start=72) | **palma abierta** hacia delante, luz naranja | animar, «¡vamos!» |
| 3 | T1-19, copia [1:42](https://www.dailymotion.com/video/x80pjbn?start=102) | **se sube la capucha** con las dos manos, cejas firmes | prepararse |
| 4 | T1-19, [2:57](https://www.dailymotion.com/video/x80pjbn?start=177) | **puños arriba**, al lado de Todo | animar |
| 5 | ED1, [0:10](https://www.dailymotion.com/video/x80jy2b?start=10) | **sale por la puerta**, piernas abiertas, camiseta amarilla | presentar, «¡hola!» |
| 6 | P27 (#139) | **sentado en una valla**, pierna subida, relajado | charlar |
| 7 | #707 | mirada de reojo, capucha roja | desconfiar |
| 8 | P5 (#22) | **manos unidas** frente a la cara, en tensión | pensar |

### Megumi

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | P8 (#71) | **manos en forma de perro**, mirada seria | presentar su técnica |
| 2 | OP1, [1:06](https://www.dailymotion.com/video/x84iff2?start=66) | el mismo gesto, con sombras | idem |
| 3 | ED1, [0:28](https://www.dailymotion.com/video/x80jy2b?start=28) | sale por la puerta **con auriculares rojos** y mochila, andar tranquilo | presentar sin ganas |
| 4 | #785 | **manos entrelazadas** frente a la boca, sonrisa rara | pensar |
| 5 | #501 | en fila con todos, **manos en los bolsillos** | grupo |
| 6 | P27 (#139) | de pie junto a Yuji, **mano en el bolsillo**, mira de lado | «no me mires a mí» |

### Nobara

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | P12 (#115, T1-3) | **mano en la cadera**, barbilla alta | **presentar**, **regañar** |
| 2 | P10 (#87) | **martillo en una mano, clavos entre los dedos** | amenaza cómica |
| 3 | ED1, [0:40](https://www.dailymotion.com/video/x80jy2b?start=40) | **brazos abiertos con bolsas de compras**, pierna levantada | **celebrar** |
| 4 | ED1, 0:52 | **bebiendo un batido**, guiño | relajada |
| 5 | #502 | en ropa de calle, comiendo con los chicos | charla |
| 6 | P25 (#95) | abrigo de invierno, entre Yuji y Megumi | grupo tranquilo |

### Inumaki

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | #1017 | **cuello subido hasta la nariz**, ojos tranquilos | **presentar** (en silencio) |
| 2 | P29 (JJK0) | **enseña el espray** para la garganta a la cámara | **cuidar la voz**, explicar |
| 3 | P30 (manga) | **salta con el megáfono** en alto y hace la **«V»** | **animar**, celebrar |
| 4 | #974 | **grita con la boca abierta**, se ven los **sellos** en las mejillas | la orden fuerte |
| 5 | #972 | **se baja el cuello** con un dedo, marca en la mejilla | «voy a hablar» |
| 6 | #839 | **mano en el hombro** de Megumi, sangre en la boca | proteger, animar |
| 7 | #973 | (Kasumi) con **el teléfono** en la oreja: Inumaki manda **por teléfono** | la voz a distancia |
| 8 | P18 (#15) | arte conceptual: **pulgar arriba**, ojos cerrados de gusto | celebrar |
| 9 | tráiler JJK0, [x8x3x96 0:51](https://www.dailymotion.com/video/x8x3x96?start=51) | **se sube la bufanda de cuadros** con los dedos, mirada de lado, seria | «callado, pero atento» ✅ visto |
| 10 | OP1, [1:02](https://www.dailymotion.com/video/x84iff2?start=62) | **boca abierta gritando**, sello de la mejilla a la vista | la orden fuerte ✅ visto |

### Nanami

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | P15 (#141) | **mano tapando la boca**, reloj visible | **pensar**, desaprobar |
| 2 | #923 | de frente, serio, las gafas brillando | **regañar** |
| 3 | #939 | de lado, **explicando** con la boca abierta | **explicar** |
| 4 | #948 | **se enrolla la corbata en la mano** | «se acabó el horario» |
| 5 | #920 | brazo extendido, aura de energía, de pie | animar a la acción |
| 6 | ED1, [1:18](https://www.dailymotion.com/video/x80jy2b?start=78) | **cenando**, cuchillo y tenedor, copa | descanso |
| 7 | T2-18, copia [0:18](https://www.dailymotion.com/video/x8upb66?start=18) | sonrisa cansada | despedirse (**spoiler**) |

### Todo

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | T1-19, copia [2:48](https://www.dailymotion.com/video/x80pjbn?start=168) | **manos juntas** delante del pecho: «Congratulations, brother» | **celebrar** |
| 2 | #1085 = [calls Yuji his best friend](https://static.wikia.nocookie.net/jujutsu-kaisen/images/3/3f/Aoi_Todo_calls_Yuji_his_best_friend_%28Anime%29.png) | **manos abiertas** junto a la cara, sonrisa de loco, bosque | presentar con fuerza |
| 3 | #1095 | **carcajada** enorme | celebrar |
| 4 | #405 | **brazos cruzados**, camiseta morada, en un cuarto | preguntar («¿qué tipo de chica…?») |
| 5 | #531 | junto a Yuji, **brazos arriba** | animar |
| 6 | [Aoi Todo (Anime 2)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/5/59/Aoi_Todo_%28Anime_2%29.png) (943×1094) | de cuerpo entero, sin camisa, **brazo derecho estirado hacia arriba** con la mano abierta, puño izquierdo cerrado, sonrisa; faja blanca y pantalón ancho azul noche | **presentar** a lo grande, saludar ✅ visto (3.er ayudante) |
| 7 | [interrupts the Tokyo first-years](https://static.wikia.nocookie.net/jujutsu-kaisen/images/9/9a/Aoi_Todo_interrupts_the_Tokyo_first-years_%28Anime%29.png) | **brazos cruzados** apoyado en la cama, camiseta morada, ojos entornados; Yuji, Megumi y Nobara de espaldas | **preguntar**, meterse en la charla ✅ visto |
| 8 | [encourages Yuji to keep fighting](https://static.wikia.nocookie.net/jujutsu-kaisen/images/0/06/Aoi_Todo_encourages_Yuji_to_keep_fighting_%28Anime%29.png) | uniforme abierto en la estación de Shibuya (cartel amarillo), **puño cerrado delante del pecho**, gritando | **animar** («¡arriba!»; T2, ojo con el spoiler) ✅ visto |
| 9 | [crying over his memories with Yuji](https://static.wikia.nocookie.net/jujutsu-kaisen/images/5/5a/Aoi_Todo_crying_over_his_memories_with_Yuji_%28Anime%29.png) | **cabeza hacia atrás, llorando a chorros** de emoción | **celebrar** en broma ✅ visto |
| 10 | [ready to guide Yuji further](https://static.wikia.nocookie.net/jujutsu-kaisen/images/4/40/Aoi_Todo_ready_to_guide_Yuji_further_%28Anime%29.png) | **palma abierta levantada**, media sonrisa, chispas negras del Destello Negro | **explicar**, «te enseño» ✅ visto |
| 11 | [first appearance](https://static.wikia.nocookie.net/jujutsu-kaisen/images/1/1a/Aoi_Todo_first_appearance_%28Anime%29.png) (853×480) | **mirada de reojo**, ceño fruncido, camiseta morada | desconfiar, amenaza ✅ visto |

### Sukuna (añadido por el 2.º ayudante; imágenes de la wiki, 1920×1080 salvo la 1)

| # | Dónde | Postura, manos, mirada | Uso |
|---|---|---|---|
| 1 | [Sukuna realizes that he has control](https://static.wikia.nocookie.net/jujutsu-kaisen/images/4/41/Sukuna_realizes_that_he_has_control_%28Anime%29.png) (1961×1658) | de perfil, **sonrisa enorme** con todos los dientes, ojo rojo muy abierto | amenaza |
| 2 | [Sukuna tells Jogo to stand proud](https://static.wikia.nocookie.net/jujutsu-kaisen/images/9/91/Sukuna_tells_Jogo_to_stand_proud_%28Anime%29.png) | en el cuerpo de Yuji, de pie, **mirada de lado** y media sonrisa, fondo blanco | **reconocer** a otro («Siéntete orgulloso») |
| 3 | [Sukuna looking down on Yuji](https://static.wikia.nocookie.net/jujutsu-kaisen/images/6/62/Sukuna_looking_down_on_Yuji_%28Anime%29.png) | **recostado en su trono de huesos**, mano en la mejilla, kimono blanco | **el rey aburrido**: lámina de reglas |
| 4 | [Sukuna proposes a Binding Vow to Yuji](https://static.wikia.nocookie.net/jujutsu-kaisen/images/a/a1/Sukuna_proposes_a_Binding_Vow_to_Yuji_%28Anime%29.png) | **levanta dos dedos** hacia la cámara, sonrisa ladina | **proponer un trato**, explicar una regla |
| 5 | [Sukuna demands … bow to him](https://static.wikia.nocookie.net/jujutsu-kaisen/images/3/36/Sukuna_demands_Jogo%2C_Mimiko%2C_and_Nanako_bow_to_him_%28Anime%29.png) | **se echa el pelo hacia atrás** con la mano, ojos entornados | presentarse con chulería |
| 6 | [Sukuna bored with Yuji](https://static.wikia.nocookie.net/jujutsu-kaisen/images/f/f1/Sukuna_bored_with_Yuji_%28Anime%29.png) | **cara de aburrimiento**, ojos a medio cerrar | desdén, «qué pesados» |
| 7 | [Sukuna sitting on Yuji](https://static.wikia.nocookie.net/jujutsu-kaisen/images/0/0b/Sukuna_sitting_on_Yuji_%28Anime%29.png) | **sentado encima de Yuji**, en su dominio rojo | burla (no para lámina amable) |
| 8 | OP1, [1:22](https://www.dailymotion.com/video/x84iff2?start=82) (visto) | sonrisa torcida, cabeza ladeada, marcas en la cara | el gancho |
| 9 | [True Jujutsu (Anime)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/9/9b/True_Jujutsu_%28Anime%29.png) (1920×1080; 3.er ayudante) | **sello de la palma de Enma**: manos juntas delante de la nariz, puntas de índice y corazón tocándose; ojos rojos de reojo, capucha roja | **abrir su dominio** = «mi sala, mis reglas» (lámina de reglas) ✅ visto |

### Panda (añadido por el 2.º ayudante)

| # | Dónde | Postura, manos, mirada | Uso |
|---|---|---|---|
| 1 | [Panda (Anime)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/c/c5/Panda_%28Anime%29.png) (751×1050) | de pie, de frente, **una mano levantada** | **presentar**, saludar |
| 2 | [How Panda thinks the students rank](https://static.wikia.nocookie.net/jujutsu-kaisen/images/9/91/How_Panda_thinks_the_students_rank_%28Anime%29.png) | Panda junto a **una tabla de rangos dibujada a mano** (1級, 準1級, 2級…) con **caras chibi** de cada alumno | **explicar** con una tabla: lámina 2 de rangos |
| 3 | [Panda first appearance](https://static.wikia.nocookie.net/jujutsu-kaisen/images/b/b0/Panda_first_appearance_%28Anime%29.png) | de perfil, **mano en la barbilla**, mejilla sonrojada | **pensar** |
| 4 | [Nobara and Panda taunt Momo](https://static.wikia.nocookie.net/jujutsu-kaisen/images/5/50/Nobara_and_Panda_taunt_Momo_%28Anime%29.png) | **sonrisa burlona** enseñando los dientes, junto a Nobara | picar, animar en broma |
| 5 | [Panda fakes his defeat](https://static.wikia.nocookie.net/jujutsu-kaisen/images/f/f8/Panda_fakes_his_defeat_%28Anime%29.png) | agachado, **cara de pillo** | la broma |
| 6 | [Panda in class](https://static.wikia.nocookie.net/jujutsu-kaisen/images/d/d3/Panda_in_class_%28Anime%29.png) (1920×803) | sentado en el aula, serio, de perfil | escuchar |
| 7 | [Maki, Toge, and Panda waiting for Yuta](https://static.wikia.nocookie.net/jujutsu-kaisen/images/7/71/Maki%2C_Toge%2C_and_Panda_waiting_for_Yuta_%28Anime%29.png) (1920×803) | con **chaqueta amarilla** de invierno, entre Inumaki y Maki con bufandas | ropa de calle, grupo |
| 8 | ED1, [1:14](https://www.dailymotion.com/video/x80jy2b?start=74) (visto) | de pie con **un ramo de globos** | celebrar |

### Resumen: qué pose para qué

| Uso | Pose recomendada |
|---|---|
| **Presentar** | Gojo mano abierta (P1) · Nobara mano en la cadera (P12) · Inumaki con el cuello subido (#1017) · Todo con el brazo en alto (Todo 6) |
| **Explicar** | **Gojo con puntero y pizarra** (*Cursed Clash* 0:21 y 3:22) · Gojo señalando (T1-7 1:39) · Inumaki enseñando el espray (P29) · **Panda con su tabla de rangos** · Todo con la palma levantada (Todo 10) |
| **Celebrar** | Todo «Congratulations» (T1-19) · Yuji riendo (OP1 1:18) · Nobara con bolsas (ED1 0:40) · Inumaki con megáfono y «V» (P30) |
| **Regañar** | Nanami de frente (#923) · Nobara con martillo (P10) · Sukuna con el sello de Enma (Sukuna 9), sólo en lámina de reglas |
| **Pensar** | Nanami mano en la boca (P15) · Megumi manos entrelazadas (#785) · Panda mano en la barbilla |
| **Animar** | Yuji palma abierta (OP1 1:12) · Gojo con las gafas (P3) · Inumaki pulgar arriba (P18) |

## 16 · Vestuario

**El uniforme de la escuela** (lo icónico): chaqueta **tipo gakuran**
(cuello alto, botones dorados con espiral) y pantalón, **azul marino
casi negro** `#202030` (medido en #139). **Cada alumno lo lleva
personalizado** ✅ (wiki):

| Personaje | Ropa icónica | Colores medidos | Otras ropas (vistas) |
|---|---|---|---|
| **Yuji** | uniforme + **sudadera roja con capucha** asomando por el cuello; **zapatillas rojas** | pelo `#D8A8A0`, capucha `#C04048`, uniforme `#202030` (#139) | T1-1: **sudadera amarilla** y vaqueros (club, 0:00); ED1: **camiseta amarilla y bermudas azules** sobre turquesa; T2: **cicatriz** bajo el ojo |
| **Megumi** | uniforme clásico, camisa blanca; pantalón corto hasta la espinilla | pelo `#304050` (#139) | ED1: **camiseta blanca, auriculares rojos al cuello** y mochila sobre amarillo |
| **Nobara** | uniforme con **falda**, medias negras, **cinturón marrón con clavos** | pelo cobrizo `#B07858` en sombra, uniforme `#3B416C` en luz (#115) | ED1: **peto blanco, camiseta verde agua**, bolsas de compras; T2: **parche en el ojo** (spoiler) |
| **Gojo** | chaqueta de **cuello alto** azul noche, **venda negra**; botas | pelo `#F0F0F0`, venda `#000000`, ropa `#201828` (#1) | JJK0: **vendas de tela blanca**; de paisano: **gafas de sol redondas** (P3); ED1: camisa caqui y pantalón verde; T2 joven: uniforme con **gafas redondas** |
| **Sukuna** | en Yuji: la misma ropa + **marcas negras** (dos rayas bajo los ojos, tatuaje en la frente) | marcas `#102018` | forma real: **kimono blanco** y cuatro brazos (manga) |
| **Nanami** | **traje beige**, camisa azul, **corbata de leopardo**, **gafas sin patillas** | pelo `#A8A058`, lente `#C8D060` (#923) | ED1: traje, **cenando con vino** |
| **Inumaki** | uniforme con **cuello subido con cremallera** hasta la nariz | pelo platino, ojos morados (wiki) | JJK0: **cuello de punto verde azulado a rayas** (P29); entrenamiento: camiseta blanca sobre cuello negro |
| **Todo** | **sin camisa** o camiseta **morada** `#683068`, pantalón ancho `#302838`, **faja azul** | (#303) | uniforme abierto y roto |
| **Maki** | uniforme con pantalón, **gafas**, coleta; **lanza** o bolsa de armas | — | chándal |
| **Panda** | nada, o un brazalete; en el ED1, **globos** | — | — |

**Qué ropa reconoce todo el mundo**: Gojo **con venda** (o con las
gafas redondas); Yuji con **la capucha roja**; Nanami con **traje y
corbata de leopardo**; Inumaki con **el cuello tapándole la boca**.

## 17 · Paisajes y fondos de pantalla

### 17.1 Los sitios, con su luz (vistos en `hojas/fondos_objetos_01.jpg`)

| Sitio | Hora y luz | Celda |
|---|---|---|
| Escuela de Tokio | **mediodía**, cielo azul con nubes, sombras duras | F1-F3 |
| Aula | **mañana**, luz lateral por ventanas de cuadrícula | F29, F13 |
| Celda de talismanes | **sin ventanas**: sólo la luz amarilla de los farolillos | F23 |
| Shibuya | **noche**, neón y un velo negro; hora en pantalla («22:20») | F7-F11 |
| Picnic del OP1 | **tarde de primavera**, luz rosada entre cerezos | F25 |
| ED1 | **sin luz**: colores planos | F26, F30 |

### 17.2 Fondos de pantalla en alta (de fans, sólo referencia)

De [wallhaven](https://wallhaven.cc/search?q=jujutsu%20kaisen&sorting=favorites),
por favoritos (API consultada el 24-sep-2026). Tamaño y autor según la
API. **No pegar**: el autor es quien lo subió o la fuente que enlaza.

| Id | Qué es | Tamaño | Autor / fuente |
|---|---|---|---|
| [mlzoy1](https://wallhaven.cc/w/mlzoy1) | Naoya y Choso, fotograma | 3840×2160 | subido por ThorRagnarok |
| [qr3mk7](https://wallhaven.cc/w/qr3mk7) | Megumi y Mahoraga, tinta beige | 3597×2064 | [KyeZzzz en X](https://x.com/KyeZzzz/status/1973791228320952556) |
| [pkopvj](https://wallhaven.cc/w/pkopvj) | Yuji en el vagón (OP1) con las marcas de Sukuna | 1920×1080 | EdwardKenwayEzio |
| [856k82](https://wallhaven.cc/w/856k82) | Gojo y Sukuna, signos de mano, rojo | 4096×1994 | [dazu_sugar__](https://twitter.com/dazu_sugar__) |
| [yq5g1k](https://wallhaven.cc/w/yq5g1k) | Choso con olas estilo ukiyo-e | 3840×2160 | [BH20647 en X](https://x.com/BH20647/status/2010271510620217836) |
| [rqo8km](https://wallhaven.cc/w/rqo8km) | **key visual oficial** rojo con ventana (= #60) | 3840×2160 | oficial (subido por Marnak) |
| [9mg5zd](https://wallhaven.cc/w/9mg5zd) | Nobara con rosas | 7680×4320 | [Nji04358659 en X](https://twitter.com/Nji04358659/status/1375719661770276864) |
| [m9opdm](https://wallhaven.cc/w/m9opdm) | Gojo con gafas redondas, primer plano | 3840×2160 | bubbleboba |

**Oficiales en alta** (mejor que los de fans): los key visuals de la
wiki (#64, #6, #60, #37) y el arte de *Phantom Parade* (#132-136, 2465×1376).

## 18 · Guía para generar con IA

Sirve para **fondos, objetos y pruebas de pose**. Al personaje final se
le **recorta de arte oficial** (P1-P30, §3) y se integra con
`v3/integrar.py` (regla 3 del dueño). La IA **no** inventa a Gojo ni a
Inumaki: se nota enseguida (pelo, venda, cuello).

### 18.1 Lo que no cambia nunca (visto en las hojas y los vídeos)

| Personaje | Rasgos fijos |
|---|---|
| **Gojo** | pelo **blanco en punta hacia arriba** cuando lleva la venda (cae liso sin ella, T1-7 3:39); **venda negra** ancha; chaqueta de **cuello alto** azul noche casi negra (`#1F2026` medido en *Cursed Clash* 3:22), sin botones a la vista; muy alto y delgado |
| **Yuji** | pelo **rosa claro** con **nuca oscura rapada**; **capucha roja** sobre el uniforme; cara redonda y cejas gruesas |
| **Megumi** | pelo **negro en pinchos** que sale hacia todos lados; uniforme cerrado; cara seria |
| **Nobara** | melena **cobriza a la barbilla**; uniforme con **falda**; clavos y martillo |
| **Inumaki** | pelo **platino** en punta; **cuello subido hasta la nariz** (con cremallera en la serie; **bufanda de cuadros verde azulado** `#475465` en JJK0, 0:51 visto); ojos violeta tranquilos; sellos en mejillas y lengua |
| **Panda** | panda gigante que anda de pie, ojos pequeños, a veces con la chaqueta del uniforme; cara expresiva (se enfada, se ríe) |

**Estilo del anime** (MAPPA): contorno **fino y uniforme**, sombra de
**dos tonos** con el borde duro, **fondos pintados casi fotográficos**
(Shibuya real, F7-F11), **luz lateral** fuerte y contraluces; paleta
**apagada** con **un acento** (el rojo de Yuji, el azul de los ojos de
Gojo, el amarillo de los farolillos).

Lo que dice el director de la T1 y de JJK0, **Sunghoo Park**, en una
entrevista en coreano ([Xportsnews, 22-feb-2022](https://www.xportsnews.com/article/1540502)):
quiso «**una paleta variada**, la que permite el cine» y probó «desde el
**storyboard** varias formas de que **el miedo se sienta real**»
(«리얼한 공포를 느낄 수 있게끔 콘티 단계부터 여러가지 흐름을 시도했다»). Y
«mostrar **las cuatro estaciones**» para que se note el paso del tiempo ⚠️
(resumen de la página, una fuente).

### 18.2 Palabras que ayudan (en inglés)

`2020s TV anime screenshot`, `clean thin lineart, two-tone cel shading`,
`muted colors`, `old wooden Japanese classroom`, `green chalkboard with
chalk writing`, `grid wooden windows, white curtains, morning side light`,
`Buddhist temple buildings on a forested mountain, blue sky`,
`paper talismans (ofuda) covering the walls, hexagonal paper lanterns on
the floor, warm yellow light`, `cherry blossom picnic, soft pink haze`,
`onigiri wrapped in nori on a picnic blanket`, `pull-down projector
screen, wooden pointer stick`.

### 18.3 Palabras que lo estropean

`speech bubble` (saca el globo blanco), `manga panel`, `chibi` (salvo que
se quiera la escena cómica), `cursed energy` (saca fuego morado y lo
llena todo), `blood`, `demon`, `neon cyberpunk` (Shibuya es de noche,
pero no es ciberpunk), `kawaii pastel`, `3D render`, `glowing eyes`,
`ninja` (saca Naruto), `samurai`.

### 18.4 Qué imágenes darle como referencia

| Para… | Imagen |
|---|---|
| fondo de día | [Tokyo Jujutsu High landscape (Anime)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/9/9b/Tokyo_Jujutsu_High_landscape_%28Anime%29.png) (F1) |
| el aula con pizarra | [School Celebration (Ao no Sumika)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/4/4e/School_Celebration_%28Ao_no_Sumika%29.png) (F13) y [Toge Inumaki in class (Anime)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/9/9b/Toge_Inumaki_in_class_%28Anime%29.png) (F29) |
| la celda de talismanes | clip x7xmacu, [0:20 y 0:49](https://www.dailymotion.com/video/x7xmacu?start=49) (F23) |
| el picnic | OP1, [1:16](https://www.dailymotion.com/video/x84iff2?start=76) (F25) |
| pose que explica | *Cursed Clash*, [3:22](https://www.dailymotion.com/video/x8scngs?start=202) |

(Las URL exactas y su tamaño medido, en `referencias.json`.)

### 18.5 Encuadre

- 1200×800 (3:2). **El personaje en un tercio**; el objeto con los textos
  en los otros dos.
- **Algo delante**, desenfocado: el borde de un pupitre, un farolillo,
  un onigiri.
- Cámara **a la altura de un alumno sentado**: así el aula se ve desde
  el pupitre, como en F29.

## 19 · Tres conceptos de lámina

Los tres son **distintos**: sitio, objeto, personaje y cuadro de diálogo
cambian. A y B son para **➕・CREAR SALA** (B puede ser su lámina 2); C
es para **🍟・General**. Las frases de los personajes son **adaptación
mía** de la línea japonesa con su minuto, **no el doblaje**, salvo donde
lo digo. Los textos del canal son **propuesta** (§0): no tienen
descripción en el inventario.

### Concepto A — «Clase extra» (➕ CREAR SALA) ⭐ el recomendado

- **Objeto real en un sitio real**: **la pizarra verde del aula de
  madera** de la Escuela de Tokio. Es el aula del opening «Ao no Sumika» (T2), con la
  pizarra escrita a tiza, ventanas de cuadrícula y el cuadro «天上天下»
  encima ([School Celebration (Ao no Sumika)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/4/4e/School_Celebration_%28Ao_no_Sumika%29.png),
  1920×1080, F13), con la luz del aula de JJK0 ([Toge Inumaki in class](https://static.wikia.nocookie.net/jujutsu-kaisen/images/9/9b/Toge_Inumaki_in_class_%28Anime%29.png),
  F29). **Se hace en Blender**: pizarra CC BY de hellfa (§4.1), tiza con
  relieve, un borrador, un trozo de tiza en el canto y el **puntero**.
  Pizarra `#36362F`, tiza `#DDD2CC`, marco `#30241E` (medidos en
  *Cursed Clash*, 1:24).
- **Por qué**: es la forma **oficial** de «Gojo explica» (tráiler
  «Special Lecture», 0:18 y 3:22, visto) y Gojo **da una clase extra**
  de Expansión de Dominio (T1-7, 9:19: «課外授業», «Clase extra»).
- **Personaje**: **Gojo** (1.º en la 4.ª encuesta), con **venda**, a la
  derecha de la pizarra, el **puntero tocando la pizarra** (pose 11 de
  §15, *Cursed Clash* 3:22). Para el recorte, el cuerpo de **P1** (hoja
  de modelo de JJK0, 2886×5255, mano abierta hacia delante) y el puntero
  modelado. Detrás, sentados en los pupitres, de espaldas, **Yuji,
  Megumi y Nobara** (P27 para Yuji y Megumi).
- **Cómo habla**: **sin globo**. La voz de Gojo **es la tiza**, como en
  el «Special Lecture». Arriba, en tiza grande: «**Clase extra**» y, al
  lado, pequeño, «課外授業». Su frase, escrita a tiza con su letra
  rápida y un dibujito: «**Hoy te enseño a abrir tu propio dominio**»
  (de «領域展開について教えてあげる», T1-7, 9:22). El **nombre del canal**,
  como **título de episodio**: **Mincho blanca** abajo a la derecha,
  sobre la imagen (Shippori Mincho B1 ExtraBold).
- **Dónde va cada texto**:
  - pizarra, arriba: **Clase extra** (y 課外授業)
  - pizarra, numerados a tiza (Shippori Mincho B1 con textura de tiza):
    1. **Entra aquí y se abre tu propia sala**
    2. **Es tuya: ponle nombre**
    3. **Tú decides quién entra**
    4. **Cuando se vacía, desaparece**
  - pizarra, abajo a la derecha, con la letra de Gojo: su frase
  - abajo a la derecha de la lámina, en Mincho blanca: **Crear sala**
- **Que no quede plano**: un **pupitre en primer plano**, abajo a la
  izquierda y desenfocado, con una tiza y el borrador; **luz de mañana**
  por las ventanas de cuadrícula que raya la pizarra; **polvo de tiza**
  en el aire; Gojo **proyecta sombra** sobre la pizarra y la punta del
  puntero la toca (regla 7 del dueño: la mano se apoya en algo).
- **Luz y paleta**: mañana; madera en sombra `#2F2831`, luz `#D3D0CF`,
  malvas `#7C6372` `#AA9AA2` (aula de JJK0, §5.2); chaqueta de Gojo
  `#1F2026`.

### Concepto B — «Baja el velo» (➕ CREAR SALA, lámina 2 o alternativa)

- **Objeto real en un sitio real**: **los talismanes de papel (ofuda)**
  de **la celda** donde encierran a Yuji (y a Yuta en JJK0): paredes
  cubiertas de papeles verticales escritos y **farolillos hexagonales**
  amarillos en el suelo (clip x7xmacu, [0:18-0:20 y 0:44](https://www.dailymotion.com/video/x7xmacu?start=18);
  tráiler de JJK0, 0:45-0:48; F23; **visto**). En la serie, el velo **se
  encarga con talismanes** y se le ponen condiciones ✅ ([wiki, «Curtain»](https://jujutsu-kaisen.fandom.com/wiki/Curtain)):
  aquí **cada talismán es una opción de la sala**. **Se hace en Blender**:
  planos de papel *washi* (ambientCG, CC0) con la tinta que sigue la
  curva del papel; farolillos hexagonales por prisma y luz emisiva.
- **Personajes**: **Megumi** (1.º en la 2.ª y la 3.ª encuesta) explica,
  **mano en el bolsillo** y mirada de lado (P27); **Yuji** mira arriba
  con la boca abierta ⚠️ (esa pose no la tengo: hay que sacarla de T1-4,
  4:47, en Crunchyroll). Es la escena de T1-4: Yuji,
  «¡Se está haciendo de noche!» (4:47); Megumi, «Es un velo. Una barrera
  que nos esconde de fuera» (4:49-4:54) ✅ subtítulo.
- **Cómo habla**: con **texto vertical entre 「」**, como las técnicas del
  manga (T13-T18). Arriba a la derecha, en vertical y a pincel (Yuji
  Syuku): el conjuro 「闇より出でて闇より黒く」 y, debajo, en horizontal
  pequeño: «**Sal de la oscuridad, más negro que la oscuridad**» (T1-4,
  4:35). La frase de Megumi va en **su propio talismán**, más ancho, en
  Zen Antique: «**Es un velo. Lo de dentro es tuyo**».
- **Dónde va cada texto** (cada uno en un talismán; ⚠️ **hay que
  confirmar qué deja hacer el bot**):
  - talismán grande del centro: **Crear sala**
  - **Ponle nombre a tu sala**
  - **Pon un límite de gente**
  - **Ciérrala con candado**
  - **Escóndela de los demás**
  - **Echa a quien moleste**
  - **Pásasela a otro al irte**
  - el guiño de fans, en un talismán pequeño y torcido: «**¿Y el velo?**»
    (el olvido de Gojo y Geto, T2-1, 13:57 ✅; ver [la imagen de la wiki](https://static.wikia.nocookie.net/jujutsu-kaisen/images/f/f5/Jujutsu_students_realize_they_forgot_about_the_curtain_%28Anime%29.png))
- **Que no quede plano**: **farolillos en primer plano**, desenfocados y
  muy brillantes (como en 0:14-0:16 del clip); luz **desde abajo**,
  amarilla `#EBD430` `#FAF441`, sombras marrones `#523010`; los
  talismanes **ondulados**, cada uno con su sombra; cámara un poco
  **picada**, como la vista cenital de 0:44.

### Concepto C — «¡Salmón!» (🍟 General)

- **Objeto real en un sitio real**: **un mantel de picnic con onigiri**
  bajo los cerezos, el **hanami** con el que termina el opening 1 (OP1,
  [1:16](https://www.dailymotion.com/video/x84iff2?start=76), visto: todos
  sentados en un mantel beige `#A99C7E` con comida y botellas; luz rosada
  `#DBD8D4`). Cada onigiri lleva una **etiqueta de papel** con su palabra.
  **Se hace en Blender**: onigiri CC BY de Pierre.Bourdon (§4.1), mantel
  con tela simulada, pétalos.
- **Por qué**: 🍟 General es la sala **para hablar de lo que sea**, e
  Inumaki **sólo habla con ingredientes de onigiri**. La lista oficial
  (tomo 0, pág. 104, en la wiki): **kombu = saludo**, **salmón = sí**,
  **copos de bonito = no** ✅ (wiki + [Sohu, en chino](https://www.sohu.com/a/452092226_532686)),
  **mentaiko = ¡ánimo!**, **atún = mira** (wiki). **Atún con mayonesa**:
  la wiki dice «hablar de lo que sea»; la fuente china, «esto es
  importante, atención» ⚠️. Y en el ED1 sale **comiendo un onigiri**
  (1:16, visto).
- **Personajes**: **Inumaki** de pie, **levantando la mano abierta**
  para saludar, con el cuello subido ([Toge Inumaki introduced (Anime)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/4/43/Toge_Inumaki_introduced_%28Anime%29.png),
  1920×803); **Panda** sentado en el mantel, **brazos cruzados**, el que
  traduce ([Tokyo Jujutsu High second-years (Anime)](https://static.wikia.nocookie.net/jujutsu-kaisen/images/d/d7/Tokyo_Jujutsu_High_second-years_%28Anime%29.png),
  1920×1080). En el doblaje, Panda es **el que explica** («En realidad,
  el primer día son combates grupales…», muestra de Doblaje Wiki ✅).
- **Cómo habla**: con la **caja del modo historia de *Cursed Clash***:
  **dos viñetas con el borde roto**, en diagonal, sobre **tinta azul
  petróleo** `#314953` `#202C33`, y el texto blanco al lado (tráiler,
  3:09, visto; ¡allí habla justo **Panda**!). Viñeta 1, Inumaki:
  «**¡Salmón!**» («salmón» sale en su muestra del doblaje latino ✅).
  Viñeta 2, Panda: «**Dice que sí, que entres. Aquí se habla de lo que
  sea**». Letra: Zen Antique blanca.
- **Dónde va cada texto**:
  - un **cartel de madera** colgado del cerezo, a pincel (Yuji Boku):
    **General**
  - onigiri de **kombu** (el saludo): **Saluda al entrar**
  - onigiri de **atún con mayonesa** (de lo que sea): **Entra y habla de
    lo que sea**
  - onigiri de **salmón** (sí): **La sala de voz de la plaza**
  - onigiri de **copos de bonito** (no): **Del oficio se habla en
    general-doblaje**
  - la caja de dos viñetas, abajo a la izquierda: Inumaki y Panda
- **Que no quede plano**: un **onigiri en primer plano**, abajo y
  desenfocado; **pétalos** cayendo por delante; **contraluz rosado**
  entre los troncos (como en 1:16); Panda **tapa parte del mantel**;
  Inumaki proyecta sombra sobre la hierba.
- ⚠️ Antes de rotular: comprobar en Crunchyroll cómo dice el doblaje
  latino «kombu», «atún con mayonesa» y «mentaiko» (§10.4).

### ¿Cuál primero?

**A**. Junta lo que pide el dueño: un **objeto real que se hace en
Blender** (la pizarra con tiza), un **sitio real** del anime, el
personaje **más votado** y un **formato oficial** de la franquicia («Gojo
explica» con puntero) en vez de un globo. Y dice justo lo que hace el
canal: **abrir tu propio espacio**. **B** es su lámina 2 si el bot tiene
opciones. **C** es la más tierna y la que más gustará a los fans de
Inumaki.

## 20 · Lo que no pude verificar

- **Los textos de ➕ CREAR SALA y 🍟 General** (§0): ninguno de los dos
  tiene descripción en el inventario, y **no sé qué bot crea las salas**
  ni qué opciones da (nombre, límite, candado…). Son una propuesta: hay
  que confirmarlos con el dueño antes de dibujar.
- **Frases del doblaje latino**: las de §10.4 salen de subtítulos
  automáticos, de **Whisper** sobre las muestras de Doblaje Wiki (que no
  dicen el episodio) y de dos clips de Dailymotion. **Ningún clip oficial
  de YouTube** se pudo bajar desde aquí («confirma que no eres un bot»).
  El 3.er ayudante (24-sep) consiguió metadatos, búsquedas y subtítulos
  de YouTube a ratos (con `--js-runtimes node`), pero **el audio y el
  vídeo dan 403** (tres intentos): sin audio no hubo segunda
  transcripción con Whisper. Cómo dice el doblaje «kombu», «atún con
  mayonesa» y el «¿Qué tipo de chica te gusta?» de Todo: ⚠️ sin oír.
- **Los términos del doblaje** («Extensión» en la T1, «Expansión» en la
  T2; «Hechicería» → «Brujería»): Doblaje Wiki, y los **subtítulos**
  oficiales de Crunchyroll dicen lo mismo («La Extensión de Dominio de
  Mahito» en la T1; «Expansión de Dominio» en el tráiler de 2025), pero
  el doblaje en sí ⚠️ sin oír (§10.3).
- **Resolución de los vídeos**: Dailymotion sólo sirve 512×288 aquí. Los
  colores medidos en fotogramas son aproximados (±10 por canal).
- **Web oficial** `jujutsukaisen.jp`: 403 (Cloudflare) con `curl` y con
  el lector web; su sección de entrevistas (hay una del director
  Goshozono, según el buscador) quedó sin leer ⚠️. La **Wayback Machine**
  responde a la API de disponibilidad pero **corta el túnel** al bajar la
  página (dos intentos). **TV Tropes** y **The Cutting Room Floor**: 403.
- **La caja de diálogo de *Phantom Parade*** y la del modo historia de
  *Cursed Clash* **en español**: no las vi (sólo la versión inglesa del
  tráiler).
- **El gesto del dominio de Megumi**: visto sólo en un fotograma de la
  wiki ⚠️ (el de Sukuna ya está confirmado en tres fuentes, §14.2). El
  vídeo de su dominio en la T3 que había en Dailymotion (xa2smw6) ya no
  existe.
- **Los números «#N»** del 1.er ayudante: su índice se perdió. §3.0
  tiene ya **todas** las equivalencias con el nombre de archivo (el 3.er
  ayudante encontró #139, #1085 y #1180).
- **Encuesta latina propia** de popularidad: no la encontré.
- **Tendencias de TikTok** (el baile del ED1, el gesto del dominio):
  sólo títulos de búsqueda, TikTok no se abre desde aquí ⚠️.
- **Quién pregunta «¿Y el velo?»** en T2-1 (13:57): el subtítulo no
  marca quién habla ⚠️.

## Cumplimiento del encargo

| Punto de `ENCARGO.md` | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial en cantidad y variado | ✅ | la wiki entera por `investigar_serie.py` (3.367 imágenes la 1.ª vez, 3.424 al rehacer el índice); 3 hojas propias con 90 celdas numeradas; tabla #N → archivo (§3) |
| 2 · Fotogramas de escenas icónicas con capítulo y minuto | ⚠️ | minutos de los subtítulos japoneses con tiempos (§2) ✅ y 12 vídeos mirados en fotogramas (§12) ✅; pero los fotogramas propios son de **512×288** (Dailymotion); a 1080p sólo los de la wiki (1920×1080) |
| 3 · Fan art, renders 3D y modelos libres | ✅ | 15 modelos de Sketchfab con licencia de la API (6 recomprobados el 24-sep, más la pantalla de proyección), 7 obras de fan art con autor, wallhaven (§4, §17) |
| 4 · Fondos y sitios, paleta y texturas | ✅ | 8 sitios con luz, paleta medida con Pillow (más la de la celda, el picnic y la caja de *Cursed Clash*), texturas CC0 (§5) |
| 5 · Tipografía y letras libres con tildes | ✅ | 10 letras probadas con fontTools; la trampa de la letra del generador de logos (tildes vacías); el **logo oficial en español** de *Ejecución* (serif con tildes) (§6) |
| 6 · Cómo hablan y piensan en pantalla | ✅ | títulos de episodio, hora y lugar, técnicas verticales, pizarra, **caja del modo historia de *Cursed Clash*** (nueva), tabla de Panda (§7) |
| 7 · Personajes y encuestas | ✅ | las 4 encuestas oficiales; la 4.ª en dos fuentes (§9) |
| 8 · Doblaje latino: reparto en dos fuentes y frases | ✅ reparto / ⚠️ frases | 18 voces en dos fuentes; frases textuales de 3 vías (subtítulos automáticos, Whisper sobre muestras de Doblaje Wiki, 3DJuegos). Sin clips oficiales de YouTube (bloqueado) (§10) |
| 9 · Música | ✅ | los 10 temas de las 3 temporadas y JJK0 (comprobados en la wiki), canciones internas (§11) |
| 10 · Vídeos con minuto exacto | ✅ | 15 vídeos con enlace y minuto (`?start=` o `&t=`); 11 mirados el 24-sep con hojas numeradas (10 del 2.º ayudante y el tráiler de *Ejecución* del 3.º), 10 útiles (§12) |
| 11 · Videojuegos: interfaz y cajas | ✅ | *Cursed Clash*: pizarra, HUD hexagonal, lobby, frases rápidas y **caja del modo historia** (vistos y medidos); *Phantom Parade*: sólo arte ⚠️ (§13) |
| 12 · Lo que ama el fandom y qué NO hacer | ✅ | 13 memes con minuto y fuente, 11 «no hacer» (§14) |
| 13 · Descripción profunda de cada personaje | ✅ | 12 personajes y 4 de apoyo, con cómo hablan y su minuto (§8) |
| 14 · Poses analizadas (6-10 por personaje) | ✅ | Gojo 13, Todo 11 (6 nuevas del 3.er ayudante), Inumaki 10, Sukuna 9, Yuji 8, Panda 8, Nanami 7, Megumi 6, Nobara 6 (§15) |
| 15 · Vestuario con hex | ✅ | 10 personajes, colores medidos donde se pudo (§16) |
| 16 · Paisajes y fondos de pantalla | ✅ | sitios con hora y luz; 8 fondos de fans en alta con autor y tamaño (§17) |
| 17 · Guía para IA | ✅ | rasgos fijos, estilo, palabras que ayudan y que estropean, referencias con enlace, encuadre (§18) |
| 3 conceptos de lámina | ✅ | §19: A y B para ➕ CREAR SALA, C para 🍟 General; objeto, personaje, cuadro, textos y profundidad |
| 40 fuentes distintas | ✅ | 47 en la bitácora (§21.4; el 3.er ayudante añadió Wikipedia en inglés) |
| Tipos: oficiales | ⚠️ | tráileres y clips oficiales (en copias), Steam, web de la Jump ✅; **web oficial 403** y sin entrevistas del staff japonés leídas; sí una del director Sunghoo Park (en coreano) |
| Tipos: otros idiomas | ✅ | japonés (subtítulos, pixiv百科, ciatr, note, eiga-manga), coreano (Xportsnews), chino (Sohu) |
| Tipos: wikis, TV Tropes, TCRF, Wayback | ⚠️ | Fandom (JJK, Doblaje, Dubbing Database) y su foro ✅; Wikipedia en inglés ✅; TV Tropes y TCRF 403; Wayback corta el túnel (el 3.er ayudante lo probó otra vez: «Connection reset») |
| Tipos: foros y comunidades | ✅ | Reddit por Arctic Shift, foro de la wiki |
| Tipos: arte (Pixiv, ArtStation, DeviantArt) | ✅ | ArtStation, X de artistas, DeviantArt (aviso de IA), pixiv百科 |
| Tipos: vídeo | ✅ | §12 |
| Tipos: código y recursos | ✅ | kitsunekko-mirror (GitHub), generador de logos (GitHub Pages), Sketchfab, Poly Haven, ambientCG, Google Fonts, dafont |
| Tipos: doblaje latino | ✅ | Doblaje Wiki (API y audios), Dubbing Database, **ANMTV**, Cine Premiere, Somos Kudasai, Hero Network, Chirchi, Cultura Geek, 3DJuegos LATAM |
| Hojas de contacto (máx. 3, < 3 MB) | ✅ | `personajes_01.jpg` 0,80 MB, `fondos_objetos_01.jpg` 0,70 MB, `pantalla_y_letras_01.jpg` 0,78 MB (2400×1780 cada una) |
| `referencias.json` (20-40, medidos, url = imagen) | ✅ | 40 entradas: 30 imágenes de la wiki (tamaño por la API y HTTP 200 comprobado) y 10 fotogramas de vídeo con `?start=` (512×288, medido con ffprobe) |

## 21 · Bitácora de búsqueda

**Aviso**: el registro de búsquedas del 1.er ayudante **se perdió** con
su carpeta de trabajo. Lo que sigue es: (a) lo que hizo el 2.º ayudante,
paso a paso, y (b) las fuentes que el 1.º **dejó citadas** en la biblia.

### 21.1 Red (24-sep-2026)

- **Funcionó**: Jujutsu Kaisen Wiki y Doblaje Wiki (API, también los
  audios), Dailymotion (API y vídeos, sólo a 512×288), GitHub (clon
  parcial), Sketchfab (API), Arctic Shift (a ratos), archive.org (sólo la
  API de disponibilidad), ANMTV, 3DJuegos, Xportsnews.
- **Bloqueado**: YouTube («Sign in to confirm you're not a bot»);
  `jujutsukaisen.jp` (403, Cloudflare, con `curl` y con el lector web);
  `web.archive.org` (el túnel se corta, dos intentos); TV Tropes (403);
  Arctic Shift con búsquedas de frase («Timeout. Maybe slow down a bit»,
  varias veces). Del 1.º: The Cutting Room Floor (403).
- **Un error mío**: al parar mi primera tanda de vídeos usé `pkill -f
  fotogramas.py`, que pudo cortar descargas de otros ayudantes que
  corrían a la vez. Si a alguno le faltó una hoja, fue por eso.

### 21.2 Búsquedas web del 2.º ayudante (7 del cupo de 50)

| # | Idioma | Búsqueda | Qué dio |
|---|---|---|---|
| 1 | en | Jujutsu Kaisen memes explained "Nah, I'd win" "Stand proud" "with this treasure i summon" | Sportskeeda (dos artículos), foro de la wiki |
| 2 | es | Jujutsu Kaisen "gallo" Itadori doblaje latino meme | 3DJuegos LATAM (frase textual), Facebook, TikTok |
| 3 | ja | 呪術廻戦 ミーム 「ナー、勝つさ」 五条 流行語 | pixiv百科「勝つさ」, ciatr, mynavi |
| 4 | ja | 呪術廻戦 御所園翔太 監督 インタビュー 渋谷事変 演出 | la página de entrevistas de la web oficial (403), Natalie, Real Sound |
| 5 | ko | 주술회전 박성후 감독 인터뷰 | Xportsnews, Daum, Hanryu Times |
| 6 | zh | 咒术回战 狗卷棘 饭团语 含义 鲑鱼 木鱼花 海带 | Sohu, 163, Zhihu, Moegirl |
| 7 | es | ANMTV Jujutsu Kaisen doblaje latino reparto Ángel Rodríguez… | ANMTV (elenco de JJK0), Somos Kudasai, Crunchyroll News |
| — | — | lector web: 3DJuegos, Xportsnews, ANMTV (bien); jujutsukaisen.jp (403) | — |

### 21.3 Sin cupo (API, git, descargas)

- `herramientas/fotogramas.py` sobre **10 vídeos** de Dailymotion (§12.0)
  y 23 fotogramas en grande; colores con Pillow.
- API de Dailymotion: 12 búsquedas («inumaki megaphone», «jujutsu kaisen
  latino», «gojo domain expansion hand sign»…).
- Jujutsu Kaisen Wiki `action=parse`: *Toge Inumaki*, *Cursed Speech*,
  *Curtain*, *Jujutsu Kaisen*, *Jujutsu Kaisen (Anime)*, *Jujutsu Kaisen
  0: The Movie*; *Juju Sanpo* no existe. `imageinfo` de ~55 archivos;
  `allimages` por prefijo; el índice rehecho con las funciones de
  `investigar_serie.py` (3.424 / 2.717).
- Doblaje Wiki `action=parse` de la serie y `imageinfo` de **11 audios**,
  pasados por **faster-whisper** *small* y *medium* (instalado en la
  carpeta de trabajo y borrado después).
- `git clone --filter=blob:none --sparse` de kitsunekko-mirror: T1
  (Erai-raws), T2 (Judas y Erai-raws), JJK0 (Netflix); `grep` de 帳,
  領域展開, 勝つさ, 誇れ, 布瑠部, 天上天下.
- Sketchfab: 6 modelos por UID y 2 búsquedas (pizarra, pantalla de
  proyección).
- Arctic Shift: 15 consultas (la mitad con «Timeout»).
- `yt-dlp -F` (Dailymotion: un único formato 512×288); `ffprobe`.

### 21.4 Fuentes consultadas (47)

**Oficiales (7)**: [Crunchyroll en Español, tráiler 1](https://www.youtube.com/watch?v=aPBUUJbrAWo) ·
[Crunchyroll en Español, clips doblados](https://www.youtube.com/watch?v=HSZPNTXO-cw) ·
[TOHO animation, OP y ED sin créditos](https://www.youtube.com/watch?v=v8bZVdTgXoY) ·
[TOHO animation, PV de Shibuya](https://www.youtube.com/watch?v=PKHQuQF1S8k) ·
Bandai Namco, tráiler «Special Lecture» de *Cursed Clash* ([copia](https://www.dailymotion.com/video/x8scngs)) ·
[Steam](https://store.steampowered.com/app/1877020/) (3 fichas por la API) ·
[web de la Jump, votación](https://www.shonenjump.com/j/vote_jujutsu_kaisen/).

**Wikis (6)**: [Jujutsu Kaisen Wiki](https://jujutsu-kaisen.fandom.com/) ·
[Wikipedia en inglés, «Crunchyroll Anime Awards»](https://en.wikipedia.org/wiki/Crunchyroll_Anime_Awards) (3.er ayudante) ·
[su foro](https://jujutsu-kaisen.fandom.com/f/p/4400000000000048141) ·
[Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Jujutsu_Kaisen) ·
[Dubbing Database](https://dubdb.fandom.com/wiki/Jujutsu_Kaisen_(Latin_American_Spanish)) ·
[pixiv百科事典「勝つさ」](https://dic.pixiv.net/a/%E5%8B%9D%E3%81%A4%E3%81%95) (ja).

**Prensa y artículos (17)**: [Cine Premiere](https://cinepremiere.com.mx/crunchyroll-doblajes-jujutsu-kaisen-otono-2020.html) ·
[Somos Kudasai](https://somoskudasai.com/noticias/la-pelicula-jujutsu-kaisen-0-revela-su-elenco-de-doblaje-al-espanol-latino/) ·
[Hero Network](https://www.beahero.gg/jujutsu-kaisen-temporada-3-doblaje-latino-llega-a-crunchyroll/) ·
[Chirchi](https://www.chirchi.com/tercera-temporada-jujutsu-kaisen-doblaje-latino/) ·
[Anime Argentina](https://animeargentina.net/gabriel-basurto-doblaje/) ·
[Cultura Geek](https://culturageek.com.ar/jujutsu-kaisen-termino-la-primer-temporada-y-sus-actores-de-doblaje-en-espanol-latino-nos-cuentan-sus-secretos/) ·
[ANMTV](https://www.anmtvla.com/2022/03/jujutsu-kaisen-0-conoce-el-elenco.html) ·
[3DJuegos LATAM](https://www.3djuegos.lat/anime/doblaje-jujutsu-kaisen-hizo-canon-meme-popular-fandom-mexico-gallo-itadori-realidad) ·
[Sportskeeda](https://www.sportskeeda.com/anime/stand-proud-strong-sukuna-s-famous-quote-jujutsu-kaisen-explained) ·
[ciatr](https://ciatr.jp/topics/326274) (ja) ·
[eiga-manga.com](https://eiga-manga.com/entry/jujutsu-popularity-vote4) (ja) ·
[hadashinoarukikata](https://hadashinoarukikata.com/entry/2024/10/20/220156) (ja) ·
[note, «しじみ»](https://note.com/shijimiota/n/n8a524b4ddbb5) (ja) ·
[いいフォント](https://goodfreefonts.com/3116/) (ja) ·
[Xportsnews](https://www.xportsnews.com/article/1540502) (ko) ·
[Sohu](https://www.sohu.com/a/452092226_532686) (zh) ·
Sensacine México (la copia del tráiler 1, [x88ah25](https://www.dailymotion.com/video/x88ah25)).

**Comunidad (2)**: [Reddit r/JuJutsuKaisen por Arctic Shift](https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=JuJutsuKaisen&title=nanami%20overtime) ·
DeviantArt (búsqueda del 1.er ayudante; sobre todo IA).

**Arte (3)**: [ArtStation](https://www.artstation.com/artwork/YG8gBq) (4 obras) ·
X/Twitter de artistas ([dazu_sugar__](https://twitter.com/dazu_sugar__), [KyeZzzz](https://x.com/KyeZzzz/status/1973791228320952556)…) ·
[wallhaven](https://wallhaven.cc/search?q=jujutsu%20kaisen&sorting=favorites).

**Vídeo (4)**: [Dailymotion](https://www.dailymotion.com/video/x84iff2) (12 vídeos mirados) ·
[YouTube](https://www.youtube.com/watch?v=obN-3JaQVO8) (metadatos y tendencias) ·
Tomatazos (la copia del tráiler de JJK0, [x8x3x96](https://www.dailymotion.com/video/x8x3x96)) ·
[Crunchyroll VIVO, entrevista al elenco](https://www.youtube.com/watch?v=IjONEwQpsMU) (sólo la ficha).

**Código, 3D y texturas (8)**: [kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror) ·
[JujutsuKaisenLogoGenerator](https://h0tcat.github.io/JujutsuKaisenLogoGenerator/) ·
[Sketchfab](https://sketchfab.com/) · [Poly Haven](https://polyhaven.com/textures) ·
[ambientCG](https://ambientcg.com/list?q=paper) · Google Fonts ·
[dafont](https://www.dafont.com/anime-ace-bb.font) · archive.org (API de disponibilidad).

### 21.5 Lo que hizo el 3.er ayudante (24-sep-2026, sin cupo de búsquedas web)

Llegó con §0-§21 ya escritas. Repasó y resolvió ⚠️:

| Qué | Cómo | Resultado |
|---|---|---|
| «Anime del Año» 2021 | API de Wikipedia (en), «Crunchyroll Anime Awards» (la 1.ª petición dio «too many requests»; con otro agente, bien) | ✅ 5.º premio, 19-feb-2021; también T2 (2024) y *JJK0* película (2023) |
| #139, #1085, #1180 | API de la wiki (`list=search` en ficheros, `allimages`, `imageinfo`), bajados y comparados a ojo con P27, P20 y F2 | ✅ los tres; F2 era una **vista aérea**, no la entrada (corregido en §3.1 y §5); paleta re-medida |
| Signos del dominio | wiki: «Malevolent Shrine», «Domain Expansion», «Unlimited Void» (`action=parse`); 8 imágenes miradas | ✅ Sukuna (3 fuentes); ⚠️ Megumi (1) |
| Poses de Todo | 12 imágenes de la wiki bajadas y **miradas** en una hoja propia | 6 poses nuevas (§15) |
| Frases del doblaje | `yt-dlp`: búsqueda de clips de Crunchyroll en Español (2 búsquedas), subtítulos del clip de Jogo (iguales a los del 2.º ayudante), audio de Nanami (403, tres intentos); `faster-whisper` instalado en la carpeta de trabajo y **sin usar** | ⚠️ sin segunda transcripción |
| Dailymotion | API: 5 búsquedas; `fotogramas.py` sobre el tráiler de *Ejecución* (x9s6mua; xacz22o y xa2smw6 «Not found») | tráiler **mirado**: logo en español y cartelas (§6.1, §12.0) |
| pixiv百科 «嵌合暗翳庭» | `curl` | 403 (un intento) |
| Wayback Machine | `curl` a `web.archive.org` | «Connection reset» (un intento) |

`referencias.json` pasa de 37 a 40 (logo de *Ejecución*, Sukuna con el
sello de Enma, Todo de cuerpo entero). El `video.mp4` se borró.

### 21.6 Lo que NO encontré

- **Clips oficiales doblados de Inumaki y de Todo** en un sitio que
  cargue desde aquí (YouTube bloqueado).
- **La web oficial** y sus entrevistas (403) ni una copia en la Wayback.
- **The Cutting Room Floor** y **TV Tropes** (403).
- **Una encuesta latina** de popularidad.
- **La caja de diálogo de *Phantom Parade***.
- **Cómo funciona el bot de ➕ CREAR SALA** en este servidor (no está en
  el inventario).
- **Audio o vídeo de YouTube** (403 al bajar, 24-sep, 3.er ayudante):
  sin él no pude pasar Whisper a los clips doblados de Crunchyroll.
- **El dominio de Megumi en vídeo** (la copia de Dailymotion ya no existe).
