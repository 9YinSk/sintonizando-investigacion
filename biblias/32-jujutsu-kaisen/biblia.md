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
> de Gojo) y escribió §0, §1, §14, §18-§21 y `referencias.json`.
> YouTube no deja bajar vídeos ni subtítulos desde este contenedor
> («confirma que no eres un bot»): los vídeos se miraron en copias de
> **Dailymotion** del mismo montaje. Minutos de episodio: subtítulos
> japoneses con tiempos (±5 s).

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
  sentado de lado, con la venda (clip doblado, 0:08-0:47; es el final
  de T1-1 / principio de T1-2).
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
| **F1-F3** | la **Escuela de Tokio**: templos de madera en el monte, la entrada y los dormitorios (#1178, #1180, #1177) | fondo de día, «la casa» |
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
| Escuela, entrada | verdes `#487A4E` `#809D83`, piedra `#C3C4BC` | #1180 |
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
pizarra** o **placas hexagonales cian**.

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
| Caja de diálogo del modo historia de *Cursed Clash* | ⚠️ no encontré captura | — |

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
  (manga, cap. 269) ✅ (wiki, «Cursed Speech»).
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
- **Latinoamérica**: la serie ganó **Anime del Año** en los Crunchyroll
  Anime Awards (2021) ⚠️ (una fuente: Cultura Geek). Encuesta latina propia: ⚠️ no
  la encontré.

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

**Subtítulos oficiales en español** (no doblaje) del tráiler 1, leídos
en pantalla: «No te preocupes. **No hay nadie más fuerte que yo**»
(Gojo), «Ayudaré a las personas como quiera» (Megumi), «Esto es para
poder seguir siendo quien soy» (Nobara), «No quiero tener que
arrepentirme por cómo viví» (Yuji), «Adelante. **Elige el infierno que
prefieras**» ([Dailymotion x88ah25, 0:38-1:06](https://www.dailymotion.com/video/x88ah25)) ✅ visto.

**Lo que NO encontré**: un clip oficial doblado de **Inumaki** (sus
palabras de onigiri en latino) ni del «¿Qué tipo de chica te gusta?»
de Todo. No invento su versión latina: hay que oírla en Crunchyroll
(T1-5 16:48 y T1-8 5:54) antes de escribirla en una lámina.

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
| Película JJK0 | «**Ichizu**» (一途), King Gnu ⚠️ de memoria | «**Sakayume**» (逆夢), King Gnu ⚠️ de memoria |

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

### 12.1 Los que miré fotograma a fotograma

| Vídeo | Oficial | Copia mirada | Lo que se ve (minuto de la copia) |
|---|---|---|---|
| **Opening 1** «Kaikai Kitan» (Eve), sin créditos | [TOHO animation](https://www.youtube.com/watch?v=v8bZVdTgXoY) (1:31) | [Dailymotion x84iff2](https://www.dailymotion.com/video/x84iff2) | Yuji sentado en un vagón vacío (0:02); **logo 呪術廻戦 amarillo sobre un mapa de Tokio con luces rosas** ([0:14](https://www.dailymotion.com/video/x84iff2?t=14)); Nobara de perfil (0:28); Panda (0:32); Nanami leyendo en un café (0:34); Gojo con la venda en un puente, de noche (0:42 y 0:52); Megumi haciendo el **perro con las manos** (1:06); Yuji con la palma abierta (1:12); **hanami con todos** ([1:16](https://www.dailymotion.com/video/x84iff2?t=76)); Yuji riendo con Junpei (1:18); Sukuna sonriendo (1:22) |
| **Ending 1** «LOST IN PARADISE» (ALI feat. AKLO) | [TOHO animation](https://www.youtube.com/watch?v=AWEm4tA2hMc) (1:31) | [Dailymotion x80jy2b](https://www.dailymotion.com/video/x80jy2b) | dibujo de línea suelta con **manchas de color**, ropa de calle. Yuji sale por una puerta sobre turquesa `#50CDCF` ([0:10](https://www.dailymotion.com/video/x80jy2b?t=10)); Megumi sobre amarillo `#FBE63B` (0:28); Nobara con **bolsas de compras** sobre rojo `#DF4456` ([0:40](https://www.dailymotion.com/video/x80jy2b?t=40)); Gojo sobre gris `#515151`, **probándose gafas de sol** (0:58-1:02); Maki (1:12); **Panda con globos** (1:14); Inumaki comiendo un onigiri (1:16); **Nanami cenando con copa de vino** (1:18) |
| **Tráiler 1** de la serie (Crunchyroll, subtítulos en español) | [Crunchyroll en Español](https://www.youtube.com/watch?v=aPBUUJbrAWo) (1:49) | [Dailymotion x88ah25](https://www.dailymotion.com/video/x88ah25) (Sensacine México) | **farolillos y ofuda** en la celda (0:16); Gojo: «No te preocupes. No hay nadie más fuerte que yo» (0:38-0:40); Megumi: «Ayudaré a las personas como quiera» (0:42); Nobara: «Esto es para poder seguir siendo quien soy» (0:46); Yuji: «No quiero tener que arrepentirme por cómo viví» (0:50); **muro de kanji negativos** (0:48); logo con «Jujutsu Kaisen» en romaji (1:10); cartela «少年は戦う―「正しい死」を求めて» → «Un joven lucha… por "la muerte correcta"» (1:18) |
| **Tráiler de Shibuya** (T2, PV 3, con «SPECIALZ») | [TOHO animation](https://www.youtube.com/watch?v=PKHQuQF1S8k) (1:26) | [Dailymotion x8ngqml](https://www.dailymotion.com/video/x8ngqml) | Shibuya de noche, sitios reales: el cruce (0:14), la **estatua de Hachikō** junto a la estación ([0:10](https://www.dailymotion.com/video/x8ngqml?t=10)); Gojo sin venda y con sangre (0:36); Nanami con gafas (0:54); Yuji gritando (1:08); logo dorado con «渋谷事変» (1:12) |
| **Tráiler de JJK0** (versión de **España**, no latina) | — | [Dailymotion x8ake5m](https://www.dailymotion.com/video/x8ake5m) | Rika niña con el anillo (0:04-0:14); **puerta torii de la escuela** (0:32); Gojo con la venda de tela (0:46); Panda, Maki e Inumaki (0:52); Geto sonriendo (1:28). Transcrito con Whisper: «¿vale?», «tened cuidado»: **es el doblaje de España** |
| **Tráiler «Special Lecture»** del juego *Cursed Clash* | Bandai Namco | [Dailymotion x8scngs](https://www.dailymotion.com/video/x8scngs) | **Gojo con puntero ante una pizarra** ([0:21](https://www.dailymotion.com/video/x8scngs?t=21)); tiza «Cursed Energy Is the Key to Battle» ([1:24](https://www.dailymotion.com/video/x8scngs?t=84)); la interfaz: placas **hexagonales cian** `#12A2E4` (1:30); menú «Online Versus» (2:03); tabla de niveles (2:15) |

### 12.2 Tres escenas icónicas, miradas

| Escena | Oficial | Copia mirada | Lo que se ve |
|---|---|---|---|
| **Gojo contra Jogo** (T1-7) | [Crunchyroll, sub.](https://www.youtube.com/watch?v=fcxZDSA8rPs) · [doblaje](https://www.youtube.com/watch?v=5Cvr1rxoD9Y) | [Dailymotion x7yt0gp](https://www.dailymotion.com/video/x7yt0gp) (sub. inglés) | Gojo **junta las manos** sonriendo (0:30); **le da la mano** a Jogo (1:27); **señala con el índice**: «el infinito está en todas partes» (1:39); carga a Yuji del cuello de la ropa: «Él es Yuji, viene a mirar» (2:12); **se tapa la venda con la mano** antes del dominio (3:03); **sin venda, ojos azules** (3:39); el ojo en primerísimo plano (3:45) |
| **Gojo despierta** (T2-4, ep. 28) | — | [Dailymotion x8yav0m](https://www.dailymotion.com/video/x8yav0m) | Gojo de uniforme viejo, **brazos abiertos** en luz dorada (0:10); **ojo azul enorme** (0:14); mariposa verde (0:24); **mano en la frente, riéndose**: «Throughout Heaven and Earth…» ([0:36](https://www.dailymotion.com/video/x8yav0m?t=36)); Púrpura (1:26) |
| **Yuji y Todo contra Hanami** (T1-19) | [Crunchyroll, sub.](https://www.youtube.com/watch?v=ZmC2sN9VhPo) | [Dailymotion x80pjbn](https://www.dailymotion.com/video/x80pjbn) | tejados rojos de la escuela (0:00-0:15); Maki con la lanza roja (0:48); Todo de espaldas, **sin camisa** (1:33); Yuji se sube la capucha (1:42); **Todo junta las manos: «Congratulations, brother»** ([2:48](https://www.dailymotion.com/video/x80pjbn?t=168)) = T1-19 15:57; los dos lado a lado, listos (2:57) |
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

**The Cutting Room Floor**: 403 desde aquí, y la Wayback Machine está
bloqueada por la red del contenedor. ⚠️ No pude mirar contenido descartado.

## 14 · Lo que ama el fandom, y qué NO hacer

(pendiente)

## 15 · Poses analizadas por personaje

Todas **vistas**: en fotogramas de los vídeos (§12, con minuto de la
copia mirada) o en imágenes de la wiki (#N) o de mis hojas (P·, F·).
«Uso» = presentar, explicar, celebrar, regañar, pensar o animar.

### Gojo

| # | Dónde | Postura, manos, mirada | Uso |
|---|---|---|---|
| 1 | P1 (#1) | de pie, **mano derecha abierta hacia el espectador**, la otra baja; venda | **presentar** («alto, aquí se hace así») |
| 2 | T1-7, copia [0:30](https://www.dailymotion.com/video/x7yt0gp?t=30) | **manos juntas** a la altura del pecho, sonrisa ladeada | **explicar** con calma |
| 3 | T1-7, [1:39](https://www.dailymotion.com/video/x7yt0gp?t=99) | **señala con el índice**, brazo estirado | **explicar** una regla |
| 4 | T1-7, [2:12](https://www.dailymotion.com/video/x7yt0gp?t=132) | sujeta a Yuji del cuello de la ropa, cara neutra | presentar a otro («él es…») |
| 5 | T1-7, [3:03](https://www.dailymotion.com/video/x7yt0gp?t=183) | **se tapa la venda con la mano**, cabeza baja | antes de lo importante |
| 6 | T1-7, [3:39](https://www.dailymotion.com/video/x7yt0gp?t=219) | sin venda, **ojos azules**, sonrisa de lado, mirada al espectador | **el gancho** |
| 7 | *Cursed Clash*, [0:21](https://www.dailymotion.com/video/x8scngs?t=21) | medio cuerpo, **puntero** en la mano, sonrisa | **explicar** (¡la pizarra!) |
| 8 | P2 (#18) | **«V» doble**, abraza a Yuji | **celebrar**, saludar |
| 9 | P3 (#82) | **se levanta las gafas redondas** con las dos manos | «mira esto», animar |
| 10 | #618 | **brazo por encima del hombro** de Nanami, carcajada; fondo cómico con rayas | presentar a otro en broma |

### Yuji

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | OP1, [1:18](https://www.dailymotion.com/video/x84iff2?t=78) | **carcajada** con los ojos cerrados, sentado en la hierba | **celebrar** |
| 2 | OP1, [1:12](https://www.dailymotion.com/video/x84iff2?t=72) | **palma abierta** hacia delante, luz naranja | animar, «¡vamos!» |
| 3 | T1-19, copia [1:42](https://www.dailymotion.com/video/x80pjbn?t=102) | **se sube la capucha** con las dos manos, cejas firmes | prepararse |
| 4 | T1-19, [2:57](https://www.dailymotion.com/video/x80pjbn?t=177) | **puños arriba**, al lado de Todo | animar |
| 5 | ED1, [0:10](https://www.dailymotion.com/video/x80jy2b?t=10) | **sale por la puerta**, piernas abiertas, camiseta amarilla | presentar, «¡hola!» |
| 6 | P27 (#139) | **sentado en una valla**, pierna subida, relajado | charlar |
| 7 | #707 | mirada de reojo, capucha roja | desconfiar |
| 8 | P5 (#22) | **manos unidas** frente a la cara, en tensión | pensar |

### Megumi

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | P8 (#71) | **manos en forma de perro**, mirada seria | presentar su técnica |
| 2 | OP1, [1:06](https://www.dailymotion.com/video/x84iff2?t=66) | el mismo gesto, con sombras | idem |
| 3 | ED1, [0:28](https://www.dailymotion.com/video/x80jy2b?t=28) | sale por la puerta **con auriculares rojos** y mochila, andar tranquilo | presentar sin ganas |
| 4 | #785 | **manos entrelazadas** frente a la boca, sonrisa rara | pensar |
| 5 | #501 | en fila con todos, **manos en los bolsillos** | grupo |
| 6 | P27 (#139) | de pie junto a Yuji, **mano en el bolsillo**, mira de lado | «no me mires a mí» |

### Nobara

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | P12 (#115, T1-3) | **mano en la cadera**, barbilla alta | **presentar**, **regañar** |
| 2 | P10 (#87) | **martillo en una mano, clavos entre los dedos** | amenaza cómica |
| 3 | ED1, [0:40](https://www.dailymotion.com/video/x80jy2b?t=40) | **brazos abiertos con bolsas de compras**, pierna levantada | **celebrar** |
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

### Nanami

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | P15 (#141) | **mano tapando la boca**, reloj visible | **pensar**, desaprobar |
| 2 | #923 | de frente, serio, las gafas brillando | **regañar** |
| 3 | #939 | de lado, **explicando** con la boca abierta | **explicar** |
| 4 | #948 | **se enrolla la corbata en la mano** | «se acabó el horario» |
| 5 | #920 | brazo extendido, aura de energía, de pie | animar a la acción |
| 6 | ED1, [1:18](https://www.dailymotion.com/video/x80jy2b?t=78) | **cenando**, cuchillo y tenedor, copa | descanso |
| 7 | T2-18, copia [0:18](https://www.dailymotion.com/video/x8upb66?t=18) | sonrisa cansada | despedirse (**spoiler**) |

### Todo

| # | Dónde | Postura | Uso |
|---|---|---|---|
| 1 | T1-19, copia [2:48](https://www.dailymotion.com/video/x80pjbn?t=168) | **manos juntas** delante del pecho: «Congratulations, brother» | **celebrar** |
| 2 | #1085 | **manos abiertas** junto a la cara, sonrisa de loco | presentar con fuerza |
| 3 | #1095 | **carcajada** enorme | celebrar |
| 4 | #405 | **brazos cruzados**, camiseta morada, en un cuarto | preguntar («¿qué tipo de chica…?») |
| 5 | #531 | junto a Yuji, **brazos arriba** | animar |

### Resumen: qué pose para qué

| Uso | Pose recomendada |
|---|---|
| **Presentar** | Gojo mano abierta (P1) · Nobara mano en la cadera (P12) · Inumaki con el cuello subido (#1017) |
| **Explicar** | **Gojo con puntero y pizarra** (*Cursed Clash* 0:21) · Gojo señalando (T1-7 1:39) · Inumaki enseñando el espray (P29) |
| **Celebrar** | Todo «Congratulations» (T1-19) · Yuji riendo (OP1 1:18) · Nobara con bolsas (ED1 0:40) · Inumaki con megáfono y «V» (P30) |
| **Regañar** | Nanami de frente (#923) · Nobara con martillo (P10) |
| **Pensar** | Nanami mano en la boca (P15) · Megumi manos entrelazadas (#785) |
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

(pendiente)

## 19 · Tres conceptos de lámina

(pendiente)

## 20 · Lo que no pude verificar

(pendiente)

## Cumplimiento del encargo

(pendiente)

## 21 · Bitácora de búsqueda

(pendiente)
