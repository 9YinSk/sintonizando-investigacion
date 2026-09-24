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

(pendiente)

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
