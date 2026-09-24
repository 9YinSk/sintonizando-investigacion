---
tags: [biblia, serie, laminas, biblioteca]
serie: "One Punch Man (ワンパンマン)"
canal: "sin canal: propuesta pendiente (ver §0)"
fecha: 2026-09-24
---

# Biblia · One Punch Man — para la biblioteca

> [!important] Cómo se hizo, y sus límites
> - (pendiente)

## Índice

0. One Punch Man no tiene canal: dónde encaja mejor
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

## 0 · One Punch Man no tiene canal: dónde encaja mejor

(pendiente)

## 1 · Resumen para quien tenga prisa

(pendiente)

## 2 · Las escenas que sirven (con minuto)

(pendiente)

## 3 · Arte oficial y hojas de contacto

(pendiente)

## 4 · Fan art y 3D (sólo como referencia)

(pendiente)

## 5 · Sitios, luz, paleta y texturas

(pendiente)

## 6 · Tipografía

### 6.1 Los logos (lo que vi y medí) ✅

**Logo del anime** «ONE PUNCH MAN» + ワンパンマン:
- Letras **rojas, altas y estrechas**, de palo recto y esquinas
  apenas redondeadas. Debajo, **ワンパンマン** pequeño en blanco, katakana
  gruesa y algo inclinada.
- En el OP de la T1 sale **sobre la Tierra al amanecer**: primero cromado
  con brillo azul (0:12) y luego **rojo sobre negro** (0:14-0:16)
  ([OP T1](https://www.youtube.com/watch?v=oZU6QvWHBxY&t=14), visto en copia
  de Dailymotion, ±1 s). Igual en el PV3 de 2015 (0:33) y en su cartel final.
- **Rojo medido**: `#D20A31` en el fotograma del OP (copia 512×288, ±10);
  en el logo PNG de V-STORAGE (Bandai Namco) sale `#E00010` a `#B80000`.
  La web oficial dibuja el rojo con un **degradado `#EF3033` → `#B12325`**
  (leído en su SVG `logo_2.svg`) y el título de personajes en `#B60005`.
- En la web oficial el «ONE PUNCH MAN» es **cromado**: degradado de grises
  `#757575` → `#FFFFFF` (mismo SVG).

**Logo del manga** (tomos japoneses de Shūeisha, portadas de capítulo):
- «**ONEPUNCH-MAN**» todo junto, **muy estrecho, gris o negro y gastado**,
  como un sello de goma con los bordes comidos. Debajo: «STORY by ONE &
  DRAW by YUSUKE MURATA» en versalitas con serifa (visto en la portada del
  cap. 100 y en la página «Chapter 64» de la wiki).
- Los capítulos se llaman **«撃目»** («golpe n.º»): una caja negra con
  «100撃目 [ 光 ]» en blanco y rayas verticales como un código de barras.

**Logo del 10.º aniversario (2025-26)**: un **«10» rojo gigante** con la
**cara simple de Saitama** dentro del 0, y «ONE PUNCH MAN ANNIVERSARY» en
rojo estrecho. Rojo medido en la web: `#C81818` a `#E00010`
([web del 10.º aniversario](https://onepunchman-anime.net/10th/)).

**Carteles de personaje de la T3 (2025)**: el nombre va **enorme, en
rojo o blanco**, en una palo seco **cuadrada y muy negra** («SAITAMA»,
«PURI-PURI PRISONER»), y debajo el logo pequeño «ONE PUNCH MAN» en rojo
(visual de Saitama de la wiki, 2481×3508; fondo rojo **`#E40012`**,
medido con Pillow). Cada héroe lleva un **fondo de un color plano**.

**Interfaz del juego *A Hero Nobody Knows* (2020)**: pestañas **rojas
inclinadas** (`#E23137`, `#CE000C`) sobre **gris casi negro** (`#1C1D22`),
con el **emblema de la Asociación de Héroes** de marca de agua; el super de
Saitama escribe **正義執行** («ejecución de la justicia») con **pincel negro**
enorme (capturas oficiales de Steam, 1920×1080, medidas con Pillow).

### 6.2 La letra libre más parecida (comprobada con fontTools)

Abrí cada archivo con `fontTools` y busqué á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü.

| Para imitar… | Letra libre | Licencia | ¿Tildes, ñ, ¿, ¡? | Nota |
|---|---|---|---|---|
| Logo del anime y nombres de la T3 | **Teko** (Bold/SemiBold) | OFL (Google Fonts) | ✅ todas | la más cercana: estrecha, cuadrada, esquinas suaves |
| Lo mismo, más negra | **Saira Condensed Black** / **Saira Extra Condensed Black** | OFL | ✅ todas | |
| Nombres de la T3 más anchos | **Passion One Bold** / **Russo One** | OFL | ✅ todas | cuadradas y gruesas |
| Logo gastado del manga | **Anton** o **Bebas Neue** + textura de sello | OFL | ✅ todas (Bebas sólo mayúsculas) | el desgaste se hace con máscara |
| Katakana del logo (ワンパンマン) y rótulos japoneses | **Dela Gothic One** | OFL | ✅ todas + kana | gruesa, muy de anime |
| Onomatopeyas japonesas dibujadas | **Rampart One** / **Reggae One** | OFL | ✅ todas + kana | |
| Globos de diálogo en español | **Comic Neue Bold** | OFL | ✅ todas | legible, de cómic |
| Globos «a lo manga» | Anime Ace 2.0 BB (Blambot) | gratis sólo sin fines comerciales | ❌ **no trae ¿ ni ¡** | no usar para textos con preguntas |
| Carta a mano (Mumen Rider) | **Kalam Bold** / **Permanent Marker** | OFL / Apache | ✅ todas | |
| Web oficial | **Oswald**, **Ubuntu Condensed**, **Noto Sans JP** | OFL | ✅ (Oswald) | las carga la propia web oficial (Google Fonts) |

⚠️ **Black Han Sans** (parece la de los nombres) **no trae ninguna tilde
ni la ñ**: descartada.

### 6.3 Los globos del manga (Murata) y los rótulos

- **Globos**: óvalos blancos de **línea fina y limpia**; el grito, en
  globo **de pinchos**. Las **onomatopeyas** son **enormes y dibujadas a
  mano** y rompen las viñetas: «INCINERATE!!!» en vertical, «WHOOSH»,
  «BAM» (escaneos de VIZ en la wiki, hojas 1-2).
- La cara de **Saitama «simple»** (óvalo, dos puntos, boca raya) convive con
  el Saitama «serio» muy sombreado **en la misma página**. Es el chiste
  visual base (la wiki: «su diseño cambia según el tono»).
- **Las fichas de la guía oficial** (el *databook* de VIZ) mezclan
  recortes, flechas, etiquetas en caja negra («PERSONALITY», «ABILITY»,
  «PROFILE», «SPECIAL») y letra de máquina: parecen una **revista de
  héroes** (wiki, «Saitama Databook», 1920×1500).
- **Ediciones en español**: ⚠️ no comprobé la letra de los globos de Ivrea
  ni de Panini (ver §20).

### 6.4 Qué NO hacer

- Poner el logo en **amarillo**: el amarillo es del traje, el logo es **rojo**
  (o cromado).
- Usar una letra redonda y alegre (tipo Bangers inclinada) para todo: el
  logo es **recto y serio**; la gracia está en el contraste con la cara de
  Saitama.
- Textos largos en Anime Ace: **sin ¿ ni ¡**.

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

> [!tip] En una línea
> One Punch Man **no tiene una burbuja propia**: tiene **la ficha de
> héroe de la Asociación**. Una **banda oscura inclinada** con filetes
> plateados, el **emblema de la Asociación** detrás, el nombre en
> **amarillo con borde negro** y **«Class S Rank 2 hero»** en gris enorme.
> Es como la serie **presenta** a cada personaje. Y sus **papeles**: el
> aviso de resultados del examen de héroe y el **volante del súper**.

### 7.1 Lo que la serie pone en pantalla (visto, con minuto)

**A · La ficha de héroe** ✅ (el mejor «cuadro» para una lámina)
- **PV3 de la T1** (2015), 0:44-1:45: cada héroe S sale en una **banda
  negra inclinada** con dos filetes plateados finos. A la izquierda, su
  **viñeta del manga en gris**; a la derecha, su **dibujo del anime a
  color**. Detrás, el **emblema circular de la Asociación de Héroes** (alas,
  «HERO» abajo), desenfocado.
- Textos: arriba, el alias en inglés **enorme, gris `#636665`, cursiva
  gruesa** («Terrible Tornado», «King»); abajo, **«ヒーロー協会 S級2位»**
  pequeño en blanco, el nombre **en amarillo `#FFF457` con borde negro**
  («戦慄のタツマキ») y «CV 悠木碧». Cruzando todo, «**Class S Rank 2
  hero**» en gris gigante. Fondo `#0B0C0D`.
  Fuente: [PV3, TOHO/Bandai Namco](https://www.youtube.com/watch?v=RzmFKUDOUgw&t=44)
  (lo vi en la [copia de Filmow en Dailymotion](https://www.dailymotion.com/video/x37ftv3), 512×288; colores ±10).
- **Tráiler de la T3** (2025), 0:02-0:24: la misma idea, más de cartel:
  nombre en inglés **enorme y hueco**, el japonés encima **en color**
  (rojo, amarillo, rosa) y «**CLASS S RANK 14**» debajo. Saitama:
  «**CAPED BALDY / ハゲマント / CLASS B RANK 7**» con el guante rojo
  estirado hacia la cámara (0:24)
  ([tráiler T3 de VIZ](https://www.youtube.com/watch?v=oh7bd-CDY6U), visto en
  [copia de Dailymotion](https://www.dailymotion.com/video/x9fpiio), ±2 s).
- **Rótulos del PV**: «次々と現れ溢れるキャラ達» en letras **metálicas
  plateadas** sobre una banda oscura (0:36-0:42) y el cierre «**日常ノックアウト
  アクション いよいよ開幕!**» («acción de knockout cotidiano») en blanco
  sobre negro (2:00). En la T3: «**最強集結**» («se reúnen los más
  fuertes») en kanji metálico con chispas (0:30).

**B · La cortinilla con silueta** (eyecatch de la T1) ✅
- A mitad de episodio sale **la silueta del protagonista del capítulo**:
  **negra sobre blanco**, y luego **blanca sobre negro**. Sólo **un
  detalle va en color**: las **gafas verdes** de Mumen Rider (y rojas en la
  inversa), el **aura verde** de Tatsumaki.
  Fuente: wiki, «Mumen Rider Ep 9 title card» 1 y 2, «Saitama Ep 1 title
  card», «Tatsumaki Ep 6 title card» (1920×1080). ⚠️ El número de episodio
  que da la wiki a la cortinilla de Tatsumaki («Ep 6») no cuadra con su
  primera aparición (ep. 10): lo anoto tal cual.
- En el ep. 12 la cortinilla es un **estallido radial** amarillo-rojo y
  luego azul-negro con la capa de Saitama en el centro (wiki, «Saitama Ep
  12 title card»).

**C · Los papeles del mundo** ✅ (objetos que se pueden hacer en Blender)
- **El aviso de resultados del examen de héroe** («ヒーロー認定試験 試験結果
  通知書 / サイタマ殿»): una hoja blanca vertical con una **«C» enorme**
  («C級ヒーロー») y «**総得点 71点/100点**». Saitama la sostiene con cara
  de fastidio (wiki, «Results.png», T1-05, 1920×1080).
- **El volante del supermercado** «**あったか鍋セール**» («oferta de
  hot pot calentito») con verduras, precios «99円» y «158円» en rojo y
  amarillo (wiki, «Hotpotflyer.png», 1280×715). Saitama **mata monstruos
  porque llega tarde a las ofertas** (T1-03, Carnage Kabuto; la wiki
  «Saitama when knowing he will miss a bargain sale»).
- **La carta de Mumen Rider**: empieza una carta larga a Saitama, la tacha y
  pone sólo «**Thank you!!**» (manga, cap. 29, tomo 5; wiki «Satoru»).
- **Las cartas de fans** que manda la Asociación: a Genos lo adoran; a
  Saitama le escriben que es un **tramposo** (T1-09, wiki «Episode 9»).
- **La llave del apartamento con el llavero de jirafa** (hoja de modelo
  oficial «k-001 サイタマのアパートの鍵», en la wiki).

**D · El manga** ✅
- Globos **ovalados de línea fina**; gritos en globo **de pinchos**;
  onomatopeyas **gigantes dibujadas** que atraviesan la viñeta (§6.3).
- El panel del «**OK.**» (cap. 34): Saitama en **cara simple** (óvalo, dos
  puntos, boca raya) dice sólo «OK» a Boros. Es **el meme de la serie**
  ([Know Your Meme](https://knowyourmeme.com/memes/saitama-ok)).
- Cabecera de capítulo: **caja negra** «100撃目 [ 光 ]» con rayas de código
  de barras.

**E · El juego *A Hero Nobody Knows*** ✅ (capturas oficiales de Steam)
- Menús con **pestañas rojas inclinadas** y una **mano roja señalando**,
  sobre gris oscuro con el emblema de la Asociación de marca de agua.
- En combate: **retratos redondos** con aro azul (jugador 1) y rojo
  (jugador 2), barras de vida amarillas, «**1 HIT / FIRST ATTACK**» en
  amarillo con letra de pincel, y el super de Saitama escribe **正義執行**
  con pincel negro gigante.

### 7.2 Cómo piensan (y cómo se nota)

- **Saitama piensa en voz baja y plana**: su monólogo interior es corto y
  **seco** («tener fuerza sobrehumana es bastante aburrido», doblaje latino,
  §10.3). Cuando algo le importa de verdad (la oferta del súper, que no le
  reconozcan), **la cara cambia de estilo** y se vuelve «seria» y muy
  sombreada.
- **«En 20 palabras o menos»**: Saitama corta las explicaciones largas de
  Genos y le pide que lo resuma (la wiki: «su número ideal de palabras es 20
  o menos»; T1-02/T1-05 ⚠️ episodio exacto sin comprobar). **Es la
  excusa perfecta para textos cortos en la lámina** (regla 4 del dueño).
- **Genos piensa en datos**: analiza, compara, apunta en su **libreta de
  entrenamiento** (wiki, «Genos writing his training diary», «Genos taking
  notes (OVA)»). Su voz es la del informe.
- **Mumen Rider se da ánimos solo**: «Soy débil, eso lo sé… y aun así tengo
  que intentarlo» (T1-09; subtítulo inglés de la copia vista: «I'm weak. I
  know that much.» / «And yet, I have to try.» / «It's not about winning or
  losing!») ([escena, copia de Dailymotion](https://www.dailymotion.com/video/x8rl50h), 4:00-4:16).
- **King no dice nada: suena**. El «**King Engine**» es el latido de su
  corazón asustado, que todos toman por un rugido de guerra (Dengeki
  Online, comentarios de la encuesta: «キングエンジンが鳴り響くだけでおもしろい»).

### 7.3 En los videojuegos

- ***A Hero Nobody Knows*** (Bandai Namco / Spike Chunsoft, 2020; en Steam
  con **español de Latinoamérica** en textos): ver §7.1 E y §13.
- ***Road to Hero 2.0*** (móvil, OASGames): juego de cartas; ⚠️ no vi sus
  cajas de diálogo.
- **PUBG Mobile × One Punch Man** (colaboración **hasta el 19-oct-2026**:
  trajes de Saitama, Genos, Tornado, Ventisca, Garou; mochila y casco de
  Saitama) ([ANN](https://www.animenewsnetwork.com/press-release/2026-09-21/pubg-mobile-collaborates-with-one-punch-man-to-bring-world-strongest-heroes-to-game/.242058)). ⚠️ no vi su interfaz.

### 7.4 Cómo se traduce a una lámina fija

1. **La ficha de héroe** como marco del texto principal: banda oscura
   inclinada unos **8-10°**, dos filetes plateados, emblema de la
   Asociación desenfocado detrás. El **título** en amarillo `#FFF457` con
   borde negro grueso (Teko Bold o Dela Gothic One); el **rótulo de fondo**
   en gris `#636665` gigante y en cursiva. **No hace falta globo**.
2. **Los textos secundarios**, como **papeles de la Asociación**: el aviso
   de resultados (hoja blanca con la letra de clase enorme) o una **ficha
   de ranking**. En Blender: papel con dobleces, grapado a un corcho.
3. **Si habla Saitama**, un **globo de manga** blanco, ovalado, de línea
   fina, y **una frase corta**. Nada de párrafos: «20 palabras o menos».
4. **Si alguien grita** (Genos, Tatsumaki), globo **de pinchos**.

### 7.5 Qué NO hacer con el texto

- Una **burbuja blanca redonda con sombra**, genérica: la serie no la usa
  para presentar ni para informar.
- **Tipografía cómica inclinada** en todo: la ficha es **seria y
  metálica**; lo cómico es la cara de Saitama al lado.
- Poner la palabra **«Ciclista sin Licencia»** si la lámina va en inglés, o
  «Mumen Rider» si va en latino: en el doblaje se llama **Ciclista sin
  Licencia** (§10). Tatsumaki es **Tornado** y Fubuki **Ventisca**.
- Textos largos en la voz de Saitama: **él no explica**.

## 8 · Los personajes

(pendiente)

## 9 · ¿Quién es el más querido?

(pendiente)

## 10 · Doblaje latino

### 10.1 La producción ✅

- **Sí hay doblaje latino**, de México, de las **3 temporadas**.
- **Estudio**: **Macías Group** (T1-T2 en su filial **IDF**; en la T3
  IDF ya se llama **MCS**). Lo encarga **VIZ Media**.
  Fuentes: [Doblaje Wiki, por la API](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=One%20Punch%20Man)
  y las **tarjetas de créditos** del propio doblaje (las miré: T1-01 en
  Comedy Central, T1-02 en Willax TV, T2 completas): «Estudio: MACÍAS
  GROUP».
- **Dirección**: **Guillermo Rojas** (T1, 2017), **Gabriel Ortiz** (T2,
  grabada en 2020) y **Víctor Ruiz** (T3, 2025-26). Ortiz murió en 2023;
  Víctor Ruiz, la voz de Saitama, dirigió la T3: **su primera dirección de
  anime** (Doblaje Wiki, «Datos técnicos»). Rojas y Ortiz salen en las
  tarjetas de créditos ✅.
- **Traducción**: Emiliano López (T1) y Guillermo Rubio (T2-T3).
  ⚠️ La tarjeta de T2-01 todavía dice «Emiliano López»; de T2-02 en
  adelante, «Guillermo Rubio».
- **Base**: T1 y T2 se doblaron **desde el inglés** de VIZ (Bang Zoom!).
  La T3 es *simuldub*: audio japonés de referencia y guion en inglés.
- **Dónde se ve**: **Netflix** (T1 desde el 1-jul-2017; T2 desde el
  31-dic-2021) y, desde la T3, **también Crunchyroll** (30-nov-2025 al
  15-feb-2026). En TV abierta: **Willax (Perú, 2018)**, Chile (2018) y
  **Comedy Central** (2022-23), donde fue **el primer anime** del canal.
  Fuentes: Doblaje Wiki; [ANMTV](https://www.anmtvla.com/2025/11/one-punch-man-3-temporada-estrenara-su.html?m=1);
  [TVLaint](https://www.tvlaint.com/2025/11/one-punch-man-confirma-la-llegada-de-su.html).
- **Títulos doblados** (tarjetas de créditos): T1-01 «**El Hombre Más
  Fuerte**», T1-02 «**El Cíborg Solitario**». Las tarjetas de la T2
  dejan el título en inglés («Return of the Hero», «The Hunt Begins»…).

### 10.2 Las voces (cada nombre en dos fuentes)

**DW** = Doblaje Wiki (API). **TC** = tarjeta de créditos del doblaje
(imagen de la emisión, en DW; la leí yo). **TV** = TVLaint (nov-2025).
**TG** = [TierraGamer](https://tierragamer.com/especiales/one-punch-man-actores-doblaje-espanol-latino/).
**Web JP** = [web oficial japonesa](https://onepunchman-anime.net/character/) (seiyū).

| Personaje (nombre en el doblaje) | Voz latina | Japonés (seiyū) | Fuentes | Estado |
|---|---|---|---|---|
| **Saitama** | **Víctor Ruiz** (T1-T3) | Makoto Furukawa | DW, TC (T1-01, T1-02, T2), TV, TG | ✅ |
| **Genos** | **Jhonny Torres** (T1-T3) | Kaito Ishikawa | DW, TC (T1-02, T2), TV, TG | ✅ |
| **Tatsumaki** («**Tornado**») | **Azul Valadez** | Aoi Yūki | DW, TC (T2-06), TV, TG | ✅ |
| **Mumen Rider** («**Ciclista sin Licencia**») | **Dan Frausto** (T1-T2) | Yūichi Nakamura | DW, TC (T2-03, T2-04, T2-08) | ✅ |
| **Fubuki** («**Ventisca**») | **Jocelyn Robles** | Saori Hayami | DW, TC (T2-02, T2-03), TV | ✅ |
| **King** | **Jorge H. Palafox** (T1-T2); **Héctor Estrada** (T3) | Hiroki Yasumoto | DW, TC (T2-01…), TV, TG | ✅ Palafox · ⚠️ Estrada sólo DW |
| **Garou** | **Gabriel Ortiz** (T2); **Óscar López** (T3) | Hikaru Midorikawa | DW, TC (T2-03, T2-12) | ✅ Ortiz · ⚠️ López sólo DW |
| **Sonic** («Sonic Velocidad del Sonido») | **Ricardo Loera** | Yūki Kaji | DW, TC (T2-01, T2-02, T2-09) | ✅ |
| **Bang / Silver Fang** | **Pedro D'Aguillón Jr.** (T1-T2); **Salvador Delgado** (T3) | Kazuhiro Yamaji | DW, TC (T2-03, T2-12), TG | ✅ D'Aguillón · ⚠️ Delgado sólo DW |
| **Boros** | **Dafnis Fernández** | Toshiyuki Morikawa (森川智之, web JP) | DW, TC (T1-01, como «Habitante de las profundidades») | ⚠️ en T1-01 dobla a otro; Boros sólo en DW |
| **Metal Bat** | **Eduardo Ramírez** | Wataru Hatano | DW, TC (T2-04, T2-05), TG | ✅ |
| **Prisionero Lindo-Lindo** (Puri-Puri) | **César Beltrán** | Masaya Onosaka | DW, TC (T2-09), TG | ✅ |
| **Atomic Samurai** | **Antonio Gálvez** | Kenjirō Tsuda | DW, TC (T2-07), TV, TG | ✅ |
| **Zombieman** | **Gerson Torrez** | Takahiro Sakurai | DW, TC (T2-09 «Gerson Torres»), TG | ✅ |
| **Kid Emperor** | Darhey Fernández (T1); **Pamela Mendoza** (T2) | Minami Takayama | DW, TC (T2-07, T2-10), TG | ✅ |
| **Metal Knight** | **Guillermo Rojas** (el director de la T1) | Tesshō Genda | DW, TC (T2-10), TG | ✅ |
| **Amai Mask** | **Jaime Alberto Carrillo** | Mamoru Miyano | DW, TC (T2-07) | ✅ |
| **Mosquito Girl** («Chica Mosquito») | **Adriana Núñez** | — | DW, TC (T1-02) | ✅ |
| **Dr. Genus** | **Christian Strempler** (T1); Javi Sánchez (T3) | Daisuke Namikawa | DW, TC (T1-02) | ✅ T1 |
| **Charanko** | **Miguel Ángel Leal** | — | DW, TC (T2-03, T2-04) | ✅ |
| **Tareo** (el niño que admira a Garou) | **Diego Becerril** | — | DW, TC (T2-03, T2-04, T2-11) | ✅ |
| **Sitch** | **Daniel Lacy** | Nobuo Tobita | DW, TC (T2-01, T2-09, T2-10) | ✅ |

**Datos de interés** (Doblaje Wiki, «Datos de interés»; ✅ salvo aviso):
- Es **el primer protagónico de anime de Víctor Ruiz** y el primer
  co-protagónico de **Jhonny Torres** en México. Ruiz es también Draken
  (Tokyo Revengers) y Samwell Tarly y Ramsay Bolton (Game of Thrones)
  (TierraGamer).
- En latino, **Tatsumaki se llama «Tornado»** (viene del inglés de VIZ) y
  **Fubuki, «Ventisca»**. **Mumen Rider es «Ciclista sin Licencia»**.
  Genos le dice a Saitama «**sensei**», no «maestro». «Kaijin» a veces
  se deja y a veces es «monstruo» o «amenaza».
- En la T2 se oyen palabrotas («mierda»).
- **Black Sperm** repite la frase improvisada de Freezer (Gerardo Reyero)
  en DBZ: «¡Quédate quieto, no te muevas, no ves que te voy a matar!».
- Muchos actores repiten de **Mob Psycho 100** (la otra obra de ONE):
  Manuel Campuzano (Reigen) hace a Beast King y Jinzuren; Carlos Siller
  (Mob) hace a Tatsu.
- **Discrepancias** que encontré yo ⚠️: la tarjeta de T1-01 pone
  «Vaccine Man — **Julio Bernal**» y «Fukegao — **Daniel Lacy**», y la
  tabla de Doblaje Wiki pone Emmanuel Bernal y Miguel Ángel Leal. Manda la
  tarjeta.
- Hay una **entrevista al reparto** de ANISON USA (citada en DW) y varios
  saludos de Víctor Ruiz en convenciones (YouTube, §12).

### 10.3 Frases del doblaje latino, textuales (con vídeo y minuto)

(pendiente: depende de que YouTube deje bajar los subtítulos de los clips
de Netflix Latinoamérica; ver §12 y §21)

## 11 · Música

(pendiente)

## 12 · Vídeos

(pendiente)

## 13 · Videojuegos de la franquicia

(pendiente)

## 14 · Lo que ama el fandom, y qué NO hacer

(pendiente)

## 15 · Poses analizadas por personaje

(pendiente)

## 16 · Vestuario

(pendiente)

## 17 · Paisajes y fondos de pantalla

(pendiente)

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
