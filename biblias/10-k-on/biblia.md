---
tags: [biblia, serie, laminas]
serie: "K-On! (けいおん!)"
canal: "#general"
fecha: 2026-09-24
---

# Biblia · K-On! — para #general

> [!important] Cómo se hizo, y sus límites
> - **Primera pasada (red cerrada)**: sólo buscador web y GitHub. Fandom,
>   Doblaje Wiki, SomosKudasai, Sketchfab y Poly Haven daban 403. De GitHub
>   salieron **los subtítulos japoneses de las dos temporadas, con sus
>   tiempos** ([Matchoo95/JP-Subtitles, carpeta K-ON!](https://github.com/Matchoo95/JP-Subtitles/tree/master/K-ON!)):
>   la T1 es del Blu-ray; la T2, de la emisión de TBS. De ahí salen los
>   minutos en formato 00:00 (pueden moverse uno o dos según la
>   plataforma). Las letras de [google/fonts](https://github.com/google/fonts)
>   se comprobaron con fontTools.
> - **Segunda pasada (24-25 sep 2026, red abierta)**: un equipo de cuatro
>   investigadores (imagen, vídeo, voz, texto) y un redactor. Se pudo usar:
>   APIs de Fandom (K-On! Wiki), Doblaje Wiki, Sketchfab, ambientCG,
>   Openverse, AniList y Arctic Shift (Reddit); **958 imágenes de la wiki en
>   20 hojas de contacto** (3 en `hojas/`, §3.0); **episodios de la T1 en
>   Internet Archive** y el **tráiler oficial de la película en
>   Dailymotion**, mirados con `fotogramas.py`; `estilo.py` para medir
>   colores; `voz.py` (Whisper) para oír el **piloto latino de Elocuencia
>   Studio**; tesseract y fontTools.
> - **Lo que no se pudo**: YouTube pidió iniciar sesión todo el día (sólo
>   fichas y subtítulos de algunos vídeos). Los vídeos mirados son **SD**
>   (640×360 los episodios, 480×280 el tráiler): sirven para pose, minuto y
>   color, no para calcar en 1080p. AnimeThemes dio 522. Danbooru, ANN
>   directo, GameFAQs, MobyGames y TV Tropes (anime) dieron 403.
>   Crunchyroll no se usa.
> - Los minutos **vistos** en vídeo dicen «visto»; son los de la copia de
>   Internet Archive (`k-on-s1-2`, un MP4 por episodio).
> - ✅ **confirmado**: dos fuentes, o la fuente primaria misma (el
>   episodio, la web o la tienda oficial). ⚠️ **dudoso**: una sola fuente o
>   sin mirar. Todo lo dudoso va marcado.

> [!note] Segunda pasada · qué cambió
> **Corregido (antes → ahora)**
> - «¡El club no es una cafetería!» (T1 ep. 2, 05:32): «Mio, de pie, brazos
>   cruzados» → en el fotograma de ese minuto **las cuatro están sentadas** y
>   quien habla es **Ritsu**; Mio escucha con el codo en la mesa (visto,
>   §2.2 y §15). Falta oír el segundo exacto: queda ⚠️ quién dice la frase.
> - Yui entra al club (T1 ep. 1): «20:13, presentar» → la escena real es la
>   **fiesta de después, 19:55-20:46**: pizarra 「新入部員獲得!!」, foto con
>   ✌️ (20:34) y Mugi con las manos juntas (20:46) (visto).
> - Azu-nyan (T1 ep. 9): «10:59-11:09, de memoria» → **10:57-11:15**, visto
>   gesto a gesto.
> - Blazer de invierno: `#2F3553` (estimado) → **`#4E4963`** (medido en
>   arte oficial, hoja 2 #60).
> - Madera y luz del club: naranja/crema estimado → **marrón grisáceo
>   medido** (`#654436`, `#483531`, `#E4D4BE`) en fotogramas.
> - Doblaje latino: «un doblaje chileno de una sola fuente» → el **episodio
>   1 doblado por Elocuencia Studio existe y se puede oír** (Internet
>   Archive); reparto de 4 actrices en **dos fuentes**; **13 frases
>   textuales con minuto**. Sigue sin haber doblaje latino **oficial**.
> - Dos datos del recolector eran de otra serie: «Kon» de Doblaje Wiki es
>   de *Bleach* y el Reddit «r/Konosuba» es de *Konosuba*. No se usan.
>
> **Añadido**
> - Hojas de contacto (§3.0); licencias de Sketchfab leídas en su API y
>   modelos nuevos (Les Paul, batería, Jazz Bass, «Giita!!!») (§4).
> - Keifont comprobada con fontTools (trae todo) y su licencia Apache 2.0
>   (§6); el cartel de reclutamiento visto; las páginas «bonus» del manga
>   sin bocadillo; la caja de texto del juego de PSP (la burbuja blanca que
>   no hay que copiar) (§7, §13).
> - Opening, ending, tráiler y tres escenas mirados con minuto (§2, §12);
>   compositor Tom-H@ck y ventas de Oricon con segunda fuente (§11).
> - Puntos nuevos del encargo: estilo y técnica (§A), texturas 2D (§B),
>   gustos (§C), por qué la aman (§D), fan dubs (§E), colaboraciones (§F),
>   obras parecidas (§G) y el mundo (§H). Tabla «Cumplimiento del encargo».
> - Anime Grand Prix 2009: mejor serie, Yui mejor personaje (§9).
>
> **Los ⚠️**: había **94**. Quedan los que se dicen en cada sección y en la
> tabla de cumplimiento (el recuento final, al pie de la tabla).

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección **✦ LA SALA ✦**):

> **ıı・🌐・general** (texto) · 1 fijados — _La plaza: aquí se habla de lo
> que sea. Del oficio se habla en general-doblaje; tu voz grabada va a demos._

El encargo añade su función: **es la sala donde se habla de todo, y desde
aquí se manda a la gente a los demás canales.**

Los canales a los que manda (textos reales del inventario):

| Canal | Qué dice el inventario |
|---|---|
| **#general-doblaje** (EL ESTUDIO) | Del oficio: micros, voces, técnica y dudas de novato. |
| **#demos** (EL ESTUDIO, foro) | Tu ficha de DOBLAJE: un hilo con tu nombre, tus demos y tu rango vocal. |
| **#que-estas-viendo** (LA SALA) | Series, pelis, anime: lo que estás viendo y si lo recomiendas. |
| **#que-estas-escuchando** (LA SALA) | La canción que llevas en bucle. |
| **#a-que-juegas** (LA SALA) | Lo que estás jugando, capturas y quién se apunta. |
| **#memes** (LA SALA) | El meme, sin más. Si lo doblas, va a fandub-de-memes. |
| **#comandos-y-sorteos** (LA SALA) | Aquí se usan los bots, para no ensuciar el resto. |
| **#destacados** (LA SALA) | Lo que junta estrellas acaba aquí solo. Aquí no se escribe. |
| **🍟 General** (voz, LA SALA) | La sala de voz de la plaza. |

### Textos de la lámina 1 (propuesta, cortos y en la voz de la serie)

1. **Título:** `general`
2. **Qué es:** «Aquí se habla de lo que sea.»
3. **Redirección 1:** «¿Micros, voces o técnica? Eso va a #general-doblaje.»
4. **Redirección 2:** «¿Tu voz grabada? A #demos.»
5. **Guiño de la serie** (opcional, una línea): «¡Pasa, que hay té!»

Una idea por texto, sin «·», sin «—» y sin paréntesis, como pide la regla 4.

### Lámina 2 (si la 1 se satura): «¿A dónde voy?»

La plaza manda a la gente a los otros rincones de LA SALA. Seis flechas
cortas, una por canal: #que-estas-viendo, #que-estas-escuchando,
#a-que-juegas, #memes, #comandos-y-sorteos y el canal de voz General.
#destacados va aparte, con su aviso: «Aquí no se escribe.»

### Por qué K-On! encaja con #general

K-On! es literalmente una serie sobre **un club de música que casi nunca
ensaya y se pasa la tarde tomando té y hablando de lo que sea**. La propia
Yui lo dice en su presentación: «毎日 楽しくお茶してます» (*todos los días
tomamos té, y lo pasamos bien*), temporada 2, episodio 1, **min 04:55** ✅
(subtítulo). Y Mio, la seria, lo resume al revés:
«軽音部は喫茶店じゃないぞ» (*¡el club de música no es una cafetería!*),
temporada 1, episodio 2, **min 05:32** ✅ (subtítulo). ⚠️ **Quién la dice
sigue sin confirmar**: en la primera pasada se supuso Mio por contexto;
en la segunda se miró el fotograma de ese minuto y **quien tiene la boca
abierta es Ritsu**, con Mio sentada al fondo, seria, escuchando (visto,
§2.2). Hay que oír el segundo exacto antes de ponerla en boca de nadie.
Si va en la lámina, mejor sin dueño o dicha por Mio como guiño («lo diría
ella»). Esa pareja de frases es exactamente el canal: aquí se charla; lo
del oficio, en su sitio.

Además, en el último festival (T2, ep. 20) Yui presenta a cada una y **manda
al público a otro sitio**: «澪ちゃんには ファンクラブもあるんです 入りたい人は
そこにいる 和ちゃんに言ってください» (*Mio tiene club de fans; si quieres
entrar, díselo a Nodoka, que está ahí*), **min 12:17-12:20** (es Yui:
presenta a Nodoka como «mi amiga de la infancia»), y luego
«いつでも部室にお越しください 大歓迎ですから» (*vengan al club cuando quieran,
son muy bienvenidos*), **min 13:17** (⚠️ Yui o Mugi: el subtítulo no lo
dice). Es la función de #general dicha por la serie.

---

## 1 · Resumen para quien tenga prisa

- **Qué es:** manga 4-koma de **kakifly** (Manga Time Kirara, 2007-2012,
  6 tomos) ✅ ([Wikipedia](https://en.wikipedia.org/wiki/K-On!),
  [K-ON! Wiki](https://k-on.fandom.com/wiki/Kakifly)). Anime de **Kyoto
  Animation**, dirigido por **Naoko Yamada**, guion de serie de **Reiko
  Yoshida**, diseño de personajes y jefa de animación **Yukiko Horiguchi**
  ✅ ([ficha oficial de KyoAni](https://www.kyotoanimation.co.jp/works/k-on/),
  [entrevistas traducidas](https://ultimatemegax.wordpress.com/2016/01/07/k-on-staff-interviews-pt-1-director-naoko-yamada-series-composer-reiko-yoshida-dialogue/)).
  T1 en TBS desde el 3 de abril de 2009 ✅ ([TheTVDB](https://thetvdb.com/series/k-on/episodes/1083291)
  y la ficha del ep. 1 en la [K-ON! Wiki](https://k-on.fandom.com/wiki/K-ON!_(Anime))),
  T2 «K-On!!» en 2010 y película en 2011 (viaje a Londres) ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/K-ON!_Movie), [IMDb](https://www.imdb.com/title/tt1909796/)).
- **El sitio:** el club de música ligera del instituto Sakuragaoka. Su
  escuela real es el **antiguo colegio de Toyosato** (Shiga), de William
  Merrell Vories ✅ ([Otaku Japan](https://otakutrips.com/en/spot/2460bd0d-c875-4a89-b3b8-6e8c55222c3f),
  [The Kansai Guide](https://www.the-kansai-guide.com/en/article/item/16198/)).
- **El objeto:** la **mesa del club con el té y el pastel**. Es el centro de
  la serie: la banda se llama «Ho-kago Tea Time» (*té de después de clase*)
  por lo que hacen cada día ✅ ([K-ON! Wiki](https://k-on.fandom.com/wiki/Tea_time)).
- **La más querida:** **Mio Akiyama**. Ganó la International Saimoe League
  2010, el torneo coreano de 2010 y el de PTT (Taiwán) ✅
  ([Saimoe Wiki](https://saimoe.miraheze.org/wiki/Mio_Akiyama),
  [Moegirl](https://zh.moegirl.org.cn/%E7%A7%8B%E5%B1%B1%E6%BE%AA)), y fue
  n.º 1 de Newtype en 2009-2010 ✅ ([LH Yeung](https://blog.lhyeung.net/2009/08/11/top-10-anime-characters-in-septembers-newtype/),
  [NamuWiki](https://en.namu.wiki/w/%EC%95%84%ED%82%A4%EC%95%BC%EB%A7%88%20%EB%AF%B8%EC%98%A4)).
  **Ojo:** en votaciones japonesas más recientes gana **Azusa** (sección 9),
  y en AniList **Yui** va 1.ª por un pelo (6262 favoritos contra 6161 de
  Mio). Yui ganó además el **Anime Grand Prix 2009** a mejor personaje ✅.
- **Doblaje latino oficial: no existe** ✅. Hubo un **piloto chileno no
  oficial** (Elocuencia Studio, 2020): el episodio 1 completo **sigue en
  Internet Archive** y de ahí salen 13 frases textuales con minuto
  (sección 10). Para la lámina: traducción nuestra del japonés, o una
  frase del piloto rotulada como «el doblaje perdido».
- **Cuadro de diálogo propio:** el anime casi no pone texto en pantalla.
  Lo que sí es de la serie son **los papeles del club** escritos a mano
  (el cuaderno de letras de Mio, la pizarra, los carteles para captar
  socios) y **la tira 4-koma** del manga (sección 7). El cartel de
  reclutamiento del ep. 1 se ha **visto**: rotulador rojo y verde, una
  guitarra dibujada y notas ♪. La caja de texto del juego de PSP es la
  burbuja blanca con pico: **eso no** (§7, §13).
- **El estilo:** línea fina marrón cálida, nunca negra; sombra suave,
  degradada; luz de ventana de tarde (§A).

---

## 2 · Las escenas que sirven para #general (con minuto)

Minutos sacados de los subtítulos japoneses con tiempos
([T1, Blu-ray](https://github.com/Matchoo95/JP-Subtitles/tree/master/K-ON!/S1);
[T2, emisión TBS](https://github.com/Matchoo95/JP-Subtitles/tree/master/K-ON!/S2)).
La frase japonesa es literal ✅; la traducción es mía. En la T1 del Blu-ray
el episodio 13 es «Invierno» y el 14 es «¡Live House!» (los especiales).

> [!warning] Quién dice cada frase
> Los subtítulos casi nunca ponen el nombre de quien habla (algunas líneas
> de la T2 sí, entre paréntesis: 「（梓）」, 「（紬）」, 「（さわ子）」). Cuando
> no lo pone, lo deduzco del contexto y del modo de hablar. Si una lámina
> va a citar una frase, **hay que mirar ese minuto** para confirmar quién
> la dice.

### Las cinco mejores para este canal

| # | Escena | Ep. y minuto | Frase literal | Qué dice (traducción) | Sirve para |
|---|---|---|---|---|---|
| 1 | Yui presenta al club, en off | T2 ep. 1, **04:13-04:55** | 〈毎日 楽しくお茶してます〉 | «Todos los días tomamos té y lo pasamos bien.» | Presentar la plaza |
| 2 | ⚠️ ¿Ritsu o Mio? En el fotograma habla Ritsu (visto, §2.2) | T1 ep. 2, **05:32** | 軽音部は喫茶店じゃないぞ | «¡El club no es una cafetería!» | Redirigir, con humor |
| 3 | Sawako regaña… y acepta pastel | T1 ep. 5, **14:19-14:37** | ここは お茶を飲む場所じゃないのよ / ケ…ケーキ いかがですか？ / いただきます | «¡Esto no es sitio para tomar té!» «¿Pastel?» «Gracias.» | El chiste de la charla que siempre gana |
| 4 | Yui presenta a cada una y manda al público a Nodoka | T2 ep. 20, **11:45-14:22** | 入りたい人は そこにいる 和ちゃんに言ってください | «Si quieres entrar, díselo a Nodoka, que está ahí.» | La función exacta de #general |
| 5 | «Vengan cuando quieran» | T2 ep. 20, **13:17-13:31** | いつでも部室にお越しください 大歓迎ですから | «Vengan al club cuando quieran, son muy bienvenidos.» | Bienvenida |

### Otras escenas ancla (para poses y tono)

| Escena | Ep. y minuto | Frase literal |
|---|---|---|
| Yui se despierta tarde y corre | T1 ep. 1, 00:42-00:58 | はッ ８時！ / ちこく～ッ |
| Primer té: «¡Mugi, prepara el té!» | T1 ep. 1, 14:38-15:09 | ようこそ 軽音部へ / よ～し ムギ お茶の準備だ / おいし～い |
| Yui se apunta al club, y la fiesta (visto, §2.2) | T1 ep. 1, 20:13 (frase); 19:55-20:46 (fiesta, visto) | 私 この部に入部します！ / pizarra 「新入部員獲得!!」 |
| Mio con miedo: «no veo, no oigo» | T1 ep. 5, 02:30 | 見えない 聞こえない |
| El cuaderno de letras de Mio | T1 ep. 5, 15:14-16:22 | できた？！ / かッ かゆい (*¡qué cursi, me pica!*) |
| Sawako trae trajes | T1 ep. 6, 08:00 | 衣装 作ってきましたーッ！ |
| Nace «Azu-nyan» (visto, §2.2) | T1 ep. 9, 10:57-11:15 | ニャーって言ってみて / あだ名は あずにゃんで決定だね |
| Azusa: «¿y el ensayo?» | T1 ep. 9, 17:47 | 練習はッ？ |
| «Este salón es nuestro Budokan» | T1 ep. 12, 18:45-19:11 | ここが 今いるこの講堂が 私達の武道館です |
| «¡Amo el club de música!» | T1 ep. 12, 21:57 | けいおん大好きーッ！ |
| Llega Ton, la tortuga | T2 ep. 2, 20:46 | 新入部員のトンちゃんだよー |
| Mugi: «siempre quise hacer esto» | T2 ep. 7, 04:01 | 一度やってみたかったの |
| Tras el último festival, en el club | T2 ep. 20, 18:40-20:27 | でも… すっごく楽しかったよね |
| «Tenshi ni Fureta yo!» para Azusa | T2 ep. 24, 18:20-18:44 | 梓 聴いてほしい曲があるんだ |

> [!note] Por qué la T2 ep. 20 es la escena clave
> En el MC del último festival, Yui va presentando una por una, cuenta
> quién es y **manda a la gente a otro sitio** («si quieres entrar al club
> de fans, díselo a Nodoka»; «vengan al club, allí está Ton»). Es #general
> hecho escena: la plaza que presenta y redirige.

### 2.1 · Opening, ending y tráiler, mirados de verdad (segunda pasada)

YouTube pidió iniciar sesión. Se miró la copia de **Internet Archive**
([`k-on-s1-2`](https://archive.org/details/k-on-s1-2), un MP4 por episodio,
640×360, reedición de Sentai de 2015) recortando sólo el tramo con
`ffmpeg`, y el **tráiler en Dailymotion**. Todo con `fotogramas.py` y las
hojas abiertas una a una. Son **SD**: valen para pose, minuto y color, no
para calcar en 1080p.

**Opening «Cagayake! GIRLS»** ✅ (visto; letra de Shoko Ohmori en los
créditos del propio ep. 1). En el ep. 1 va de **2:10 a 3:40** aprox. ⚠️
(corte a ojo).
- 2:19: logo 「けいおん!」 sobre **lunares rosas**.
- Cada chica con su instrumento, con garabatos de purpurina alrededor.
- 3:10: **las cuatro en bicicleta** por un camino entre arrozales.
- 3:31-3:49: **cerezos en flor**; Yui sola debajo y luego el grupo.
- Después ya es el episodio: la placa del aula 「1-3」 (3:55) y Yui con un
  dulce en la boca junto a Nodoka.

**Ending «Don't Say "Lazy"»** ✅ (visto). En el ep. 1, **21:55-23:35**.
- Un **alter ego gótico**: vestido negro, sombrero de copa o diadema,
  medias de rayas.
- Cada una con **su rótulo de neón**: «DRUMS RITSU», «GUITAR YUI»,
  «KEYBOARD TSUMUGI», «BASS MIO» (22:13-22:49).
- Luego una pompa de jabón en la ventana y Mio flotando en un fondo verde
  brillante, como de noche de neón (22:52-23:37).
- 23:43, avance del próximo episodio 「次回予告」; 24:10-26:12, créditos.

**Tráiler de *K-On! The Movie* (2011)** ✅ (visto entero, 1:28;
[Dailymotion](https://www.dailymotion.com/video/x8hzysi), 480×280). Es
oficial: sale el **logo de Shochiku** (0:02), «Directed by Naoko Yamada»,
«A Kyoto Animation film» (1:00-1:08) y la fecha 「12月3日(土) 全国ロードショー」
con el logo de TBS.
- **0:16: las cinco tazas de té vistas desde arriba, en círculo**
  ([`?start=16`](https://www.dailymotion.com/video/x8hzysi?start=16)). La
  imagen más «tea time» del tráiler: sirve tal cual para #general.
- 0:18-0:22: cartel 「祝★卒業!!」 y el logo 「映画けいおん!」.
- 0:34: cartela 「放課後ティータイムロンドンへ!!」
  ([`?start=34`](https://www.dailymotion.com/video/x8hzysi?start=34)).
- 0:36-0:42: Big Ben, «London rocks!» y 「海外デビュー!？」.
- 1:00: la estación de metro **Camden Town**.
- 1:04-1:10: taza con pastelitos en primer plano, cartela 「一生の宝物」.
- 1:12-1:22: **「HO-KAGO TEA TIME!」** en letras de luces; la banda toca.

### 2.2 · Tres escenas, vistas gesto a gesto (segunda pasada)

**1. La fiesta cuando Yui entra al club** (T1 ep. 1, **19:55-20:46**,
visto; [episodio](https://archive.org/download/k-on-s1-2/K-On%20S1%20E01.mp4)).
- 19:55: Yui, de pie junto a la puerta, oye tocar a las otras tres.
- 19:58-20:04: en la pizarra blanca escriben **「新入部員獲得!!」**
  (*¡nuevo miembro conseguido!*).
- 20:19: Ritsu tira en broma del pelo de Mio y de Mugi a la vez.
- **20:34-20:43: foto de grupo con ✌️**, dos disparos seguidos.
- **20:46: Mugi con las manos juntas**, ojos entornados, emocionada.
- Sirve para **celebrar en grupo**, más que para «presentar».

**2. La merienda que parece cafetería** (T1 ep. 2, **05:00-06:30**,
fotograma exacto en **5:32**, visto;
[episodio](https://archive.org/download/k-on-s1-2/K-On%20S1%20E02.mp4)).
- La mesa está **cubierta de platos de pastel**, con tetera blanca y
  cuatro tazas; al fondo, un amplificador y una funda de guitarra de pie,
  y un piano vertical a la izquierda. La «cafetería» es literal.
- **Las cuatro están sentadas.** Quien habla en 5:32 es **Ritsu** (a la
  derecha, de medio lado); **Mio** está al fondo a la izquierda, codo en
  la mesa, cara seria, escuchando.
- ⚠️ Por eso la frase 「軽音部は喫茶店じゃないぞ」 queda sin dueño seguro:
  falta oír el segundo exacto (la pose «Mio de pie, brazos cruzados» de la
  primera pasada no sale en ese minuto).

**3. Nace «Azu-nyan»** (T1 ep. 9, **10:57-11:15**, visto;
[episodio](https://archive.org/download/k-on-s1-2/K-On%20S1%20E09.mp4)).
- 10:57: **Yui abraza a Azusa por detrás, mejilla con mejilla**; Azusa
  lleva la diadema de orejas de gato.
- 11:06: fondo de burbujas y brillo alrededor de Azusa (vergüenza y
  ternura).
- 11:09-11:15: Azusa dice «nya» a regañadientes, con **gota de sudor** y
  las orejas «caídas».
- 11:21: separador de mitad de episodio: **una cinta de casete rosa** con
  el logo 「けいおん!」, estética de pegatina. Buena textura para #general.

---
## 3 · Arte oficial y referencias visuales

### 3.0 · Las hojas de contacto (segunda pasada) ✅

`investigar_serie.py` bajó **958 imágenes** de las galerías de Yui, Mio,
Ritsu, Mugi, Azusa y Sawako en la [K-ON! Wiki](https://k-on.fandom.com/)
y las montó en 20 hojas numeradas. Quedan tres en `hojas/`, **miradas**.
Cada número enlaza su ficha en la wiki (ahí está el original a tamaño
completo).

**`hojas/personajes_01.jpg`** (hoja 1, n.º 1-48): arte oficial de grupo,
casi todo por encima de 4000 px.
- **#24** [The new LMC](https://k-on.fandom.com/wiki/File:The_new_LMC.jpg) (5938×4078): **las cinco
  alrededor de la mesa del club con té y dulces**. La mejor referencia de
  grupo para #general.
- **#1** [AfterschoolTeaTime(129)](https://k-on.fandom.com/wiki/File:AfterschoolTeaTime(129).jpg)
  (6069×9053): el grupo entre pasteles y tazas, vertical.
- **#16** [Girls with glasses](https://k-on.fandom.com/wiki/File:Girls_with_glasses.jpg) (6012×4103):
  las cinco con gafas sobre la bandera británica.
- **#15** [graduación](https://k-on.fandom.com/wiki/File:Mio,_Mugi,_Ritsu_and_Yui_graduating.jpg)
  (4400×5640) y **#3** [Navidad](https://k-on.fandom.com/wiki/File:HTT_during_christmas.jpg) (7009×4990).
- **#34-37** portadas de *Character Image Songs* (4000×4000): primer plano
  de Azusa, Mio, Ritsu y Yui, con la mano cerca de la cara.
- **#41** [Tsumugi](https://k-on.fandom.com/wiki/File:Tsumugi.jpg) (3265×4064): Mugi con las manos
  juntas, la pose de «qué ilusión».

**`hojas/objetos_01.jpg`** (hoja 2, n.º 49-96): cada una **con su
instrumento**, y el grupo en otros trajes.
- **#71-74 y #76**, de pie, fondo blanco, como hoja de modelo:
  [Azusa con su guitarra](https://k-on.fandom.com/wiki/File:Azusa_with_her_guitar.png) (2452×3834),
  [Ritsu con sus baquetas](https://k-on.fandom.com/wiki/File:Ritsu_with_her_drumsticks.png) (2451×3834),
  [Mugi con su teclado](https://k-on.fandom.com/wiki/File:Mugi_with_her_keyboard.png) (2451×3829),
  [Mio con su bajo](https://k-on.fandom.com/wiki/File:Mio_with_her_bass_2.png) (2448×3832) y
  [Yui con su guitarra](https://k-on.fandom.com/wiki/File:Yui_with_her_guitar.png) (2448×3829). De aquí
  salen los hex medidos del §16.
- **#60** [HTT posing](https://k-on.fandom.com/wiki/File:HTT_posing.jpg) (3833×2521): las cinco en
  uniforme de invierno, de pie en la calle.
- **#56** [HTT group image 3](https://k-on.fandom.com/wiki/File:HTT_group_image_3.png) (3827×2599): el
  grupo en la sala del club, con la pizarra detrás.
- **#82** [HTT group image 2](https://k-on.fandom.com/wiki/File:HTT_group_image_2.png) (3346×2695): con
  todos los instrumentos, sobre verde.
- **#64** trajes de maid (T2), **#87** camisetas con kanji 「桜高軽音部」,
  **#81** Mio de *Death Devil*, **#94-95** Mio y Ritsu con el traje del
  ending «Don't Say Lazy».

**`hojas/vestuario_texturas_01.jpg`** (hoja 20, n.º 913-958): manga, ropa
fuera del anime y fotogramas.
- **#937-939** [páginas reales del manga, cap. 2](https://k-on.fandom.com/wiki/File:Ch_2_-_Pg_2.png)
  (728×1040): línea fina, casi sin trama (§B).
- **#921-922** trajes de escenario de Mio y Ritsu (856×980 y 760×1080).
- **#925-926** tarjetas de Hobunsha: **yukata** y **temporada de lluvias**,
  con paraguas.
- **#935** ilustración del manga a color: el grupo en la mesa con té.
- **#920** ficha de personaje de Sawako; **#943** Ritsu en portada de DVD;
  **#956-957** portadas alternativas de *College* y *High School*.

### 3.1 Fichas oficiales de Kyoto Animation (key visuals)

- [けいおん！ (T1)](https://www.kyotoanimation.co.jp/works/k-on/),
  [けいおん！！ (T2)](https://www.kyotoanimation.co.jp/works/k-on02/) y
  [映画けいおん！](https://www.kyotoanimation.co.jp/works/k-onMovie/): la
  web del estudio. Ahí está la imagen principal de cada una y la lista de
  staff. El **diseño de color** es de **Akiyo Takeda** (竹田明代) y la
  **dirección de arte** de **Seiki Tamura** (田村せいき) en las tres
  producciones ✅ (web de KyoAni y [Wikipedia en japonés](https://ja.wikipedia.org/wiki/けいおん!),
  sección スタッフ).
- **Portada y banner de AniList** ✅:
  [portada](https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx5680-r3AI3Cwfv0Aq.png),
  [banner](https://s4.anilist.co/file/anilistcdn/media/anime/banner/5680-Mc9n4eFI4i0Y.jpg).
- **Fondos de pantalla oficiales de Kyoto Animation** ✅ (Zerochan los
  etiqueta «Official Art» y el archivo circula en servidores de Amazon):
  [1920×1080](https://www.zerochan.net/4395127) y
  [2000×3000 para móvil](https://www.zerochan.net/4375977).

### 3.2 Arte nuevo de Horiguchi (15.º aniversario, 2024)

- **Ilustración nueva de Yukiko Horiguchi, dibujada y pintada toda a mano
  (analógica)**, para productos del 15.º aniversario ✅
  ([Kyoani Shop en X](https://x.com/kyoanishop/status/1868931268374917610?lang=ja)).
- **Memorial Set**: lienzo con las cinco de Ho-kago Tea Time y un librito
  del *making of* de esa ilustración ✅
  ([Kyoani Shop](https://kyoanishop.com/shopdetail/000000003447/)).
  Si se consigue una foto grande, es **la mejor referencia de grupo** que
  hay: las cinco juntas, en pose, dibujadas por la diseñadora.
- Lotería «K-On! × Newtype 15th» (29-ago a 26-sep-2024) con ilustraciones
  nuevas ✅ ([Anime!Anime!](https://animeanime.jp/article/2024/08/29/86250.html),
  [Kujibikido](https://kujibikido.com/lp/k-on-15th/)).
- Productos con la ilustración de grupo de 2024 ✅
  ([Collabo-Cafe](https://collabo-cafe.com/events/collabo/k-on-group-illust-armabianca-anime-store-goods2024/),
  [reloj de Ho-kago Tea Time](https://collabo-cafe.com/events/collabo/k-on-tea-time-after-school-watch-armabianca-anime-store-goods2024/)).

### 3.3 Blu-ray (portadas dibujadas a propósito)

- El **Blu-ray 1** trae **portada dibujada a propósito** (描き下ろし) y una
  púa de Yui ✅ ([Amazon JP](https://www.amazon.co.jp/%E3%81%91%E3%81%84%E3%81%8A%E3%82%93-1-%E5%88%9D%E5%9B%9E%E9%99%90%E5%AE%9A%E7%94%9F%E7%94%A3-Blu-ray-%E8%B1%8A%E5%B4%8E%E6%84%9B%E7%94%9F/dp/B0024DGN70)).
- La **Blu-ray Box** de la T1 ✅ ([Tower Records](https://tower.jp/item/3350921))
  y la de la T2 ✅ ([Amazon JP](https://www.amazon.co.jp/%E3%81%91%E3%81%84%E3%81%8A%E3%82%93-Blu-ray-Box-%E5%88%9D%E5%9B%9E%E9%99%90%E5%AE%9A%E7%94%9F%E7%94%A3-%E8%B1%8A%E5%B4%8E%E6%84%9B%E7%94%9F/dp/B00MF89TRK));
  el tomo 7 de la T2 ✅ ([Animaru](https://animaru.jp/anmr/product/P0078060)).
- Lista de productos oficiales en la wiki japonesa de fans ✅
  ([atwiki keionbu](https://w.atwiki.jp/keionbu/pages/17.html)).
- ⚠️ Las portadas de cada tomo del Blu-ray siguen sin verse una por una
  (sólo la de Ritsu en DVD, hoja 20 #943). De memoria, cada tomo lleva a
  una o dos chicas con su instrumento: mirarlas antes de usarlas.

### 3.4 Galerías de la wiki (ya bajadas: §3.0)

Cada una tiene fotogramas y arte oficial por personaje. En la segunda
pasada se bajaron las seis (958 imágenes):
[Yui](https://k-on.fandom.com/wiki/Yui_Hirasawa's_Gallery),
[Mio](https://k-on.fandom.com/wiki/Mio_Akiyama's_Gallery),
[Ritsu](https://k-on.fandom.com/wiki/Ritsu_Tainaka's_Gallery),
[Mugi](https://k-on.fandom.com/wiki/Tsumugi_Kotobuki's_Gallery),
[Azusa](https://k-on.fandom.com/wiki/Azusa_Nakano's_Gallery),
[Azu-nyan con orejas](https://k-on.fandom.com/wiki/Category:Azu-nyan_2_Images).

Comando usado:

```
python herramientas/investigar_serie.py --serie "K-On!" --wiki k-on --paginas "Mio Akiyama" "Yui Hirasawa" "Azusa Nakano" "Tsumugi Kotobuki" "Ritsu Tainaka" "Sawako Yamanaka" "Tea time" "Sakuragaoka High School Light Music Club"
```

### 3.5 Lo que falta

- ~~Ninguna imagen se abrió ni se midió~~ → resuelto: 958 imágenes con su
  tamaño real; las que se citan van medidas en `referencias.json`.
- ⚠️ No encontré artbook con nombre y ficha verificables (tampoco en la
  segunda pasada: nadie lo buscó con la red abierta).

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D en Sketchfab (licencia leída en su API) ✅

Segunda pasada: la licencia de cada modelo se leyó en la API de Sketchfab
(`/v3/models/<uid>`, campo `license`), no sólo en la página.

| Modelo | Autor | Licencia (API) | Para qué |
|---|---|---|---|
| [K-ON! Clubroom](https://sketchfab.com/3d-models/k-on-clubroom-b08830de23c94c8fbfb1218d79c63fd1) | sodiepoppy | Estándar, no descargable ✅ | **La sala del club en 3D**: sólo mirar dónde van la mesa, la pizarra y las ventanas |
| [Azusa Nakano (K-On!)](https://sketchfab.com/3d-models/azusa-nakano-k-on-f09132fa11d64b8cba8f3bf9036a02c0) | Euan_Chew | Estándar, no descargable ✅ | Pose y proporciones de Azusa (con esqueleto): sólo mirar |
| [Yui Hirasawa](https://sketchfab.com/3d-models/yui-hirasawa-501de09aedc34f1598e3a536e16313df) | dwtornier | **CC BY-NC-SA** ✅ | Yui completa y con *rig*. **No comercial**: referencia de pose y proporción, no render final |
| [«Giita!!!»](https://sketchfab.com/3d-models/giita-87d99d809938482bb95d0f293550f778) | elbert.nathanaeltkg | **CC BY** ✅ | **La Les Paul de Yui** con su apodo. Vale para la lámina, con crédito |
| [Gibson Les Paul](https://sketchfab.com/3d-models/none-0d42458492a1469a80aeaee52ad78c30) | Ismaele.Giraldo | CC BY ✅ | Otra Les Paul, genérica |
| [Drum Kit](https://sketchfab.com/3d-models/none-898f2f4ba1704abe9c784066e2b0f751) | art.katja | CC BY ✅ | La batería de Ritsu |
| [Fender Jazz Sunburst Bass](https://sketchfab.com/3d-models/none-e1c6d381a61040139ac64adee6b6bf93) | boogie4631 | CC BY ✅ | Se parece a **Elizabeth**, el Jazz Bass de Mio (ojo: el de Mio es zurdo) |
| [Etiqueta k-on](https://sketchfab.com/tags/k-on) | varios | — | Buscar más |

También hay, con CC BY según la parte de texto, un peluche de Yui (huwie)
y otra guitarra «Hirasawa Yui Guitar» (kaif.3d) ⚠️ (sin enlace en las
partes).

### 4.2 Objetos libres para la mesa del té (Blender) ✅

| Modelo | Autor | Licencia (API) | Se descarga |
|---|---|---|---|
| [Cute tea pot set (.blend)](https://sketchfab.com/3d-models/cute-tea-pot-set-blend-d6977572a8214af9b3c16fe5750016a2) | iamartzz | **CC BY** ✅ | Sí |
| [Tea set](https://sketchfab.com/3d-models/tea-set-194d8940512b40c591ee4dccaeabcb68) | asiam | **CC BY-SA** ✅ | Sí |
| [Tea set](https://sketchfab.com/3d-models/tea-set-3e6331747fb84794a35ed869e4f65714) | 3dhdscan | **CC BY** ✅ | Sí |
| [Tea Pot and Cups](https://sketchfab.com/3d-models/tea-pot-and-cups-723c265903424b9d8e87cda4d4d63059) | Pouya.majidi | **CC BY** ✅ | Sí |
| [Slice of cake](https://sketchfab.com/3d-models/slice-of-cake-1adc97c8421c4f6da647c77362796327) | marcogodi1 | **CC BY** ✅ | Sí |

Crédito siempre: «"Nombre" de Autor (Sketchfab), CC BY 4.0» (o CC BY-SA
4.0). Lo que diga «NC» o «ND» no va en el render final.

### 4.3 Fan art 2D (mirar, nunca pegar)

- [Houkago Tea Time tocando en el Budokan](https://www.deviantart.com/thedevastatedangel/art/K-ON-Houkago-Tea-Time-Performing-on-Budokan-498067964),
  de TheDevastatedAngel: la banda en un escenario grande.
- [Houkago Tea Time](https://www.deviantart.com/jai-d/art/Houkago-Tea-Time-292779447),
  de Jai-D: acrílico con contorno de bolígrafo de gel.
- [Ho-kago Tea Time](https://www.deviantart.com/brifyjek/art/Ho-kago-Tea-Time-925148088),
  de Brifyjek: versión minimalista.
- [Logo de Ho-kago Tea Time en vector](https://www.deviantart.com/yxero/art/Houkago-Tea-Time-Logo-Vector-278943234),
  de Yxero.
- [Mio y Ho-kago Tea Time en pixiv](https://www.pixiv.net/en/artworks/82675277)
  (autor sin ver).
- Fondos de pantalla de fans con autor y tamaño: §17.
- Hay muchas escenas en **MMD** (MikuMikuDance) en DeviantArt, p. ej.
  [MikeLaruku](https://www.deviantart.com/mikelaruku/art/MMD-K-ON-Houkago-Tea-Time-328626414)
  y [Shin001](https://www.deviantart.com/shin001/art/MMD-Houkago-Tea-Time-337857231):
  sirven para ver a las cinco en 3D desde otros ángulos.

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 La sala del club (concepto A)

- Está **junto al aula de música, en el tercer piso** ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Sakuragaoka_High_School_Light_Music_Club)).
- Tiene: estantería, **mesa de cuatro lados con seis sillas**, banco,
  **pizarra blanca y negra**, fregadero con espejo, armario y cómoda ⚠️
  (sólo la wiki; la pizarra sí se confirma abajo).
- En el edificio real de Toyosato, en el tercer piso está la sala del club
  y **los visitantes pueden escribir en la pizarra** ✅
  ([WIKIMOE](https://www.wikimoe.com/en-US/post/t4d4taba),
  [The Kansai Guide](https://www.the-kansai-guide.com/en/article/item/16198/)).
  Fotos reales para la luz y la madera:
  [Wayfarer Dave](https://www.wayfarerdaves.com/?p=2483),
  [Otaku Pilgrimages](http://otaku-pilgrimages.blogspot.com/2012/07/k-on-pilgrimage-in-toyosato-elementary.html).
- **Ton**, la tortuga del club (スッポンモドキ, tortuga de nariz de cerdo),
  vive allí en su pecera ✅ ([K-ON! Wiki](https://k-on.fandom.com/wiki/Ton);
  subtítulo T2 ep. 20, 13:28).
- **Luz:** la hora es siempre **después de clase**, la tarde. Luz cálida y
  baja entrando por ventanas altas de madera ✅ (fotos de peregrinación y
  **medida** en el fotograma de T1 ep. 1, 20:34: ver §5.4). El color real
  es **más apagado** de lo que se estimaba: marrón grisáceo, no naranja.
- **La mesa, vista** (T1 ep. 2, 5:32): pupitres juntos con mantel, platos
  de pastel apilados, tetera blanca, cuatro tazas; amplificador y funda de
  guitarra al fondo; piano vertical a la izquierda (§2.2).

### 5.2 La escalera de la liebre y la tortuga (concepto C)

- En el colegio real de Toyosato, **las barandillas de la escalera llevan
  figuras de bronce de la fábula «La liebre y la tortuga»**; se pusieron
  para que los niños no se deslizaran y se hicieran daño ⚠️ (lo dice el
  resumen de búsqueda de guías japonesas:
  [Jalan](https://www.jalan.net/kankou/spt_25441ae2182074257/),
  [Waraku](https://intojapanwaraku.com/rock/culture-rock/132755/); no abrí
  las páginas).
- Rincones más fotografiados: **la sala del club**, **el pasillo del
  segundo piso** y **la escalera** ⚠️ (mismo resumen).
- Guía de 38 sitios reales (Toyosato y Kioto) ✅
  ([Pilgrimage Guild](https://libert.co.jp/pilgrimage-guild/keion-anime-pilgrimage/)).

### 5.3 El salón de actos (concepto B)

- Los festivales se tocan en el **講堂** (salón de actos). Yui lo dice:
  «este salón es nuestro Budokan» (T1 ep. 12, 19:08-19:11) ✅ (subtítulo).
- En el especial «¡Live House!» hablan de las luces: «el estribillo de
  Fuwa Fuwa Time, en rosa» (「ふわふわ時間」のサビはピンクで), T1 ep. 14,
  **12:16** ✅ (subtítulo). Luz de escenario rosa para la canción de Mio.

### 5.4 Paleta

#### Medida en fotogramas (segunda pasada) ✅

Con `herramientas/estilo.py` (Pillow, color dominante por área) sobre
fotogramas propios de la copia de Internet Archive. Una escena cada una:
antes de dar un hex por «el» color de un sitio, conviene promediar dos o
tres fotogramas más ⚠️.

| Sitio y fotograma | Colores (porcentaje del área) |
|---|---|
| **Mesa de té del club**, T1 ep. 2, 5:32 | `#654436` madera media 35 % · `#372826` madera en sombra 23 % · `#8D6852` madera clara 15 % · `#39404F` azul apagado (uniforme, amplificador) 11 % · `#EADFC7` mantel y platos 9 % · `#B6A895` pared 7 % |
| **Club con luz de tarde**, T1 ep. 1, 20:34 | `#483531` madera oscura 35 % · `#6D554F` madera media 20 % · `#B9AA9B` pared clara 20 % · `#E4D4BE` pared con luz de ventana 14 % · `#9C8976` madera clara 12 % |
| **Cerezos del opening**, T1 ep. 1, 3:31 | `#E6D4DC` rosa pálido 28 % · `#F7EBF5` blanco rosado 27 % · `#4D4542` uniforme y contorno 24 % · `#CFABCA` rosa 14 % · `#9F8C94` gris malva 7 % |

Para la lámina: madera `#654436` y sombra `#372826` en la mesa, mantel
`#EADFC7`, luz de ventana `#E4D4BE`. La de los cerezos es la paleta de
primavera, distinta a la del club.

#### Estimada en la primera pasada ⚠️ (sólo como contraste)

**Colores de cada una** (los usa el merchandising y los CD, según un blog
de fans ⚠️ una fuente:
[The Light Music Report](https://the-keionbu.tumblr.com/post/57290579266/the-k-on-girls-color-theory-pt-1-basic)):

| Chica | Color | Hex aproximado |
|---|---|---|
| Yui | rojo | `#E0474C` |
| Mio | azul | `#3E6DB5` |
| Ritsu | amarillo | `#F2C230` |
| Mugi | rosa | `#F09BB6` |
| Azusa | verde | `#5CAD6A` |

**Pelo** (paleta de fans en [color-hex.com](https://www.color-hex.com/color-palette/15999),
sin decir qué color es de quién): `#747374`, `#987B47`, `#876945`,
`#D3C29B`, `#222235`. El `#222235` encaja con el negro azulado de Mio y
Azusa; los marrones con Yui y Ritsu; el `#D3C29B` con el rubio de Mugi ⚠️
(mi lectura).

**La sala a media tarde** (estimado; **lo sustituye la tabla medida de
arriba**): madera `#B4855A`, pared crema `#EEE5D0`, luz de ventana
`#FFE7B3`, sombra malva `#8B86A5`, mantel `#FAF7F0`. Son más claros y
saturados que lo medido: no usarlos.

**Instrumentos** (el color del modelo real, hex estimado):
- Gitah, Les Paul **Heritage Cherry Sunburst**: borde `#7E1A1A`, centro `#E0A03C`.
- Elizabeth, Jazz Bass **3-Tone Sunburst**: borde `#1B1410`, rojo `#8A2B15`, centro `#D8993A`.
- Muttan, Mustang **Candy Apple Red**: `#AE1420`.
- Batería de Ritsu, **Mellow Yellow**: `#F2D24A`.

### 5.5 Texturas reales equivalentes (CC0, Poly Haven)

- Mesa: [Wood Table Worn](https://polyhaven.com/a/wood_table_worn) o
  [Wood Table Large](https://polyhaven.com/a/wood_table_large).
- Suelo de madera del edificio viejo: [Old Wood Floor](https://polyhaven.com/a/old_wood_floor),
  [Old Wooden Floor 03](https://polyhaven.com/a/old_wooden_floor_03),
  [Wood Floor Worn](https://polyhaven.com/a/wood_floor_worn).
- Tablón de anuncios o escenario: [Wood Planks](https://polyhaven.com/a/wood_planks),
  [Dark Wooden Planks](https://polyhaven.com/a/dark_wooden_planks).
- Alternativa: [ambientCG Wood Floor 040](https://ambientcg.com/view?id=WoodFloor040).
- Poly Haven y ambientCG son CC0 (dominio público): no piden crédito.
- Papel: [Paper001](https://ambientcg.com/view?id=Paper001) a Paper006
  de ambientCG, CC0 ✅ (licencia leída en su API; más capas 2D en §B).
- ⚠️ Pizarra y corcho: siguen sin buscar.

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia

- **El logo «けいおん!»** es rotulado a medida, no una letra comercial ⚠️
  (nadie la identifica; [resultado de búsqueda](https://jref.com/resources/kei-font.174/)).
- Existe **«けいふぉんと！» (Keifont)**, una letra **gratuita, también para
  uso comercial**, hecha a partir del logo: base **源真ゴシック Heavy** con
  las kanas redibujadas; «け» e «い» rectas como símbolos, «お» y «ん»
  redondas y cómicas ✅
  ([Forest Watch](https://forest.watch.impress.co.jp/docs/review/666547.html),
  [Coliss](https://coliss.com/articles/freebies/freebies-font-keifont.html),
  [Japaaan](https://mag.japaaan.com/archives/17538),
  [descarga](https://font.sumomo.ne.jp/font_1.html)).
  ⚠️ Las tildes y la ñ vienen de la base; no pude bajarla para
  comprobarlo.
- **Los títulos de episodio** son una palabra con «!»: «廃部!» (*¡Se
  disuelve el club!*), «Tea Party!», «Clean-up!», «Instrument!», «New Club
  Member!» ✅ ([TheTVDB](https://thetvdb.com/series/k-on/episodes/1083291),
  [K-ON! Wiki](https://k-on.fandom.com/wiki/Tea_Party!)).
  **Regla de voz para la lámina:** título de una palabra con «¡…!».
- Los subtítulos de fans de la T1 usan **DF Maru Gothic** (redonda)
  ✅ (lo dice el propio archivo `.ass`). Encaja con el tono.

### 6.2 Letras libres comprobadas por mí (fontTools)

Bajé cada archivo de [google/fonts](https://github.com/google/fonts) y
miré si trae **á é í ó ú ñ Ñ ¿ ¡ ü** y la nota **♪**:

| Letra | Para qué | Tildes, ñ, ¿ ¡ | ♪ | Japonés |
|---|---|---|---|---|
| **Mochiy Pop One** | Títulos gordos y redondos, el más parecido a Keifont | ✅ | ✅ | ✅ |
| **Yusei Magic** | **Rotulador**: pizarra, carteles, la setlist | ✅ | ✅ | ✅ |
| **Hachi Maru Pop** | Letra redonda de chica de instituto (Yui, Mugi) | ✅ | ✅ | ✅ |
| **Klee One** SemiBold | Lápiz de cuaderno: las letras de Mio | ✅ | ✅ | ✅ |
| **Yomogi** | Escritura a mano fina, notas | ✅ | ✅ | ✅ |
| **Zen Maru Gothic** Black | Textos de lectura, redonda (como DF Maru Gothic) | ✅ | ✅ | ✅ |
| **M PLUS Rounded 1c** ExtraBold | Alternativa redonda | ✅ | ✅ | ✅ |
| **Kiwi Maru** Medium | Redonda suave | ✅ | ✅ | ✅ |
| **Caveat** | Mano latina rápida | ✅ | ❌ | ❌ |
| **Potta One** | Pincel pop | ✅ | ❌ | ✅ |

Todas son **OFL** (libres, también para uso comercial). Recomendación:
**Mochiy Pop One** para títulos, **Yusei Magic** para lo escrito a
rotulador y **Klee One** para el cuaderno de Mio.

---
## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que hay de verdad

- **El anime casi no escribe en pantalla.** Se habla, y el peso está en los
  gestos: Yamada dice que «la gente muestra sus emociones sobre todo con
  las piernas», y a veces enseña sólo los pies en lugar de la cara ✅
  ([Medium, «Legs as a Language»](https://medium.com/@chowwern/naoko-yamada-legs-as-a-language-e2cfc9456112),
  [AV Club](https://www.avclub.com/naoko-yamada-reiko-yoshida-kensuke-ushio-interview-anime-collaboration)).
  En el ep. 1, Mio y Ritsu aparecen **primero por los pies**: Mio camina
  recta y ordenada, Ritsu va saltando ✅ (mismo artículo y
  [nota de Pixiv](https://dic.pixiv.net/a/%E5%B1%B1%E7%94%B0%E5%B0%9A%E5%AD%90)).
- **La voz en off de Yui** presenta al grupo (T2 ep. 1, 04:13). En los
  subtítulos japoneses va entre 〈 〉 ✅ (subtítulo). Es la forma de
  «narrar» de la serie.
- **El manga es 4-koma** (cuatro viñetas en vertical) de kakifly ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Kakifly),
  [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Manga/KOn)). ⚠️ El
  aspecto exacto de sus globos (óvalos finos, mucho blanco) es de memoria.
- **Los papeles del club**, que salen en pantalla y son objetos reales:
  - el **cuaderno de letras de Mio** (T1 ep. 5, 15:14-16:22): «ふわふわ時間»
    habla de peluches y dulces; la famosa línea es
    «お気に入りのうさちゃん抱いて今夜もオヤスミ» (*abrazo a mi conejito
    favorito y me duermo otra vez*) ✅ (subtítulo T1 ep. 12, 20:15, y
    [Anime UK News](https://animeuknews.net/2011/11/k-on-volume-2/));
  - la **pizarra** de la sala ✅ (sección 5.1);
  - los **carteles para buscar socios** (T1 ep. 12, 19:00: «buscamos
    alumnas de primero que se apunten») ✅ (subtítulo).
- **En el videojuego** (PSP, 2010), entre canción y canción salen escenas
  con las chicas en **versión chibi charlando** ✅
  ([UK Anime Network](https://www.uk-anime.net/Games/K-ON!_Houkago_Live!!_(PSP).html)).
  ⚠️ No pude ver la caja de texto.

### 7.2 El cuadro propio que propongo

**Un papel del club escrito a rotulador**, con dibujitos al margen: una
nota ♪, un trozo de pastel, la tortuga Ton. Nunca una burbuja blanca
genérica.

- Para **frases dichas**: una **tira 4-koma** vertical, fina, con marco
  negro y globos ovalados simples. Es el formato del manga ✅; el estilo
  exacto del globo ⚠️.
- Para **información fija** (a dónde ir): **la tarjeta del menú del té**,
  **la pizarra** o **la setlist pegada al suelo**. Son objetos que existen
  en la serie y se pueden hacer en Blender.
- **Mio avergonzada**: su texto en el cuaderno, en **Klee One**, con una
  tachadura (le da vergüenza lo que escribe).
- **Yui**: rotulador grueso, **Yusei Magic**, con «~» al final
  («¡pasa~!»); es como alarga las palabras en japonés («おいし～い»).
- **Azusa**: letra ordenada, **Zen Maru Gothic**, sin adornos: es la
  seria.

### 7.3 Qué NO hacer con el texto

- Nada de burbuja blanca con pico.
- Nada de estética de rock duro o neón oscuro: K-On! es pastel y tranquilo
  (lo dice ya la [guía de cuadros](../_ya_hechas/_Cuadros%20de%20dialogo%20por%20franquicia%20(23-sep-2026).md)).
- No inventar frases «del doblaje»: no hay doblaje latino oficial.

---

## 8 · Los personajes

Voces japonesas del reparto ✅ en conjunto
([Amazon JP, Blu-ray Box T2](https://www.amazon.co.jp/%E3%81%91%E3%81%84%E3%81%8A%E3%82%93-Blu-ray-Box-%E5%88%9D%E5%9B%9E%E9%99%90%E5%AE%9A%E7%94%9F%E7%94%A3-%E8%B1%8A%E5%B4%8E%E6%84%9B%E7%94%9F/dp/B00MF89TRK)):
Aki Toyosaki, Yōko Hikasa, Satomi Satō, Minako Kotobuki, Ayana
Taketatsu, Asami Sanada. Mio = **Yōko Hikasa** ✅
([IMDb](https://www.imdb.com/title/tt1410218/characters/nm2932868),
[K-ON! Wiki](https://k-on.fandom.com/wiki/Y%C5%8Dko_Hikasa)); el resto de
parejas voz-personaje, ⚠️ de memoria.

Cómo las vio el staff ⚠️ (un blog que traduce las entrevistas del libro
oficial;
[entrevistas traducidas](https://ultimatemegax.wordpress.com/2014/12/02/k-on-movie-interview-chief-animation-director-character-designer-yukiko-horiguchi/)):
Yui «extrañamente mona», Ritsu «viva y a la moda», Mio «sencilla y
segura», Mugi «ropa refinada», Azusa «chica mona». El pelo va **sin
brillos**, salvo el negro de Mio y Azusa ⚠️. Yamada quería **alturas y
pesos reales**: piernas llenas, no finas de anime ✅ (el blog de
entrevistas y
[Medium](https://medium.com/@chowwern/naoko-yamada-legs-as-a-language-e2cfc9456112)).

### Mio Akiyama — la más premiada (bajo, voz 2, letras)

- **Carácter:** amable, **muy tímida** y sensible; reservada y de voz
  baja incluso con sus amigas; le gusta estar sola y escribir letras ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Mio_Akiyama)).
- **Miedos:** es **miedosa** y llora mucho; parece la más madura y es la
  más niña ✅ (misma fuente). Cuando le da miedo, se tapa y repite
  «見えない 聞こえない» (*no veo, no oigo*) (T1 ep. 5, 02:30) ✅
  (subtítulo).
- **Instrumento:** **zurda**; Fender Japan '62 Jazz Bass, 3-Tone Sunburst,
  llamado **«Elizabeth»** (se lo puso Yui; al principio no le gusta).
  El nombre ✅ ([K-ON! Wiki](https://k-on.fandom.com/wiki/Mio_Akiyama);
  subtítulo T2 ep. 6, 18:43); el modelo exacto ⚠️ (sólo la wiki).
- **Relaciones:** amiga de la infancia de Ritsu ✅ (subtítulo T1 ep. 6,
  11:11). Hacen pareja cómica: Ritsu la pica y **Mio le da un coscorrón**
  ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/KOn)).
  Tiene **club de fans** en el instituto, y eso la horroriza ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Mio_Akiyama); subtítulo T1
  ep. 6, 21:50).
- **Cómo se expresa:** habla poco y claro; regaña corto
  («¡El club no es una cafetería!», ⚠️ atribución por contexto). Es
  formal: a Yui la llama «Hirasawa-san» y le cuesta decir «Yui» a secas
  (T1 ep. 2, 05:04-05:18) ✅ (subtítulo). Cuando se avergüenza, se bloquea
  (T1 ep. 6, «ya nadie se casará conmigo», 22:06 ✅ subtítulo y
  [Know Your Meme](https://knowyourmeme.com/forums/just-for-fun/topics/13036-fine-ill-watch-k-on)).
- **Cuerpo:** Yamada pensó en encorvarla por ser alta y decidió que **se
  queda recta** ⚠️ (una entrevista). Pelo **largo, liso, negro** ✅ (arte
  oficial y wikis), ojos grises ⚠️ ([NamuWiki](https://en.namu.wiki/w/%EC%95%84%ED%82%A4%EC%95%BC%EB%A7%88%20%EB%AF%B8%EC%98%A4)).

### Yui Hirasawa — la protagonista (guitarra y voz)

- **Carácter:** despistada, cariñosa, idealista; **no lee partituras** pero
  tiene oído de prodigio ⚠️
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Yui_Hirasawa_Trivia)).
  Se distrae con la comida y con todo lo mono ✅
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/KOn)).
- **Manías:** **abraza a la gente** cuando le apetece, sin pedir permiso;
  no resiste a un perro mono (le encantan los pugs) ⚠️
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Yui_Hirasawa_Trivia)).
  Cuando se decide, suelta «ふんす!» (T2 ep. 1, 06:30) ✅ (subtítulo).
- **Instrumento:** Gibson Les Paul Standard '50s **Heritage Cherry
  Sunburst** ⚠️ (la wiki), a la que llama **«Gitah» (ギー太)** ✅ (wiki y
  subtítulo T1 ep. 12, 18:41: «perdón por olvidarte, Gitah»).
- **Relaciones:** su hermana menor **Ui** la cuida (sus padres viajan
  mucho) ✅ (wiki; subtítulo T1 ep. 1, 00:31: Ui la despierta). Yui le
  escribió «U&I» ✅ (wiki y [ANN](https://www.animenewsnetwork.com/news/2010-09-13/k-on-gohan-wa-okazu/u&i-single-is-no.3-on-weekly-chart)). Pone el mote
  «Azu-nyan» a Azusa y la abraza siempre ✅
  ([Shipping Wiki](https://shipping.fandom.com/wiki/YuiAzu)).
- **Cómo se expresa:** alarga las vocales («おいし～い», «ちこく～ッ»),
  presenta a todas con cariño y **es la que habla al público** en los
  festivales (T1 ep. 12; T2 ep. 20) ✅ (subtítulos).
- **Cuerpo:** Yamada: «mona, no guapa, con el pelo de recién levantada»
  ⚠️ (una entrevista). Pelo castaño a los hombros con **dos horquillas
  amarillas** ⚠️
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/KOn)).

### Azusa Nakano — la «nueva» (guitarra), n.º 1 en votos japoneses recientes

- **Carácter:** la **única sensata** del grupo pese a ser la más joven ✅
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/KOn)).
  Quiere ensayar («練習はッ？», T1 ep. 9, 17:47) ✅ (subtítulo), pero acaba
  en el té.
- **Instrumento:** Fender Mustang **Candy Apple Red**, llamada
  **«Muttan»** (むったん) «porque es una Mustang» ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Azusa_Nakano_Trivia);
  subtítulo T2 ep. 20, 19:24).
- **El mote:** Sawako le trae **orejas de gato**, Yui le pide que diga
  «nya» y nace «Azu-nyan» ✅ (misma wiki; subtítulo T1 ep. 9, 10:59-11:09).
- **Miedo:** quedarse sola cuando las cuatro se gradúen (T2 ep. 24, 17:43:
  «estoy bien, seguiré con el club… está Ton») ✅ (subtítulo).
- **Cómo se expresa:** formal con las mayores («先輩»), protesta en voz
  alta y se sonroja con los abrazos.

### Tsumugi «Mugi» Kotobuki — la del té (teclado)

- **Carácter:** dulce y tranquila; hija de un presidente de empresa, su
  familia tiene villas por todo Japón ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Tsumugi_Kotobuki); el
  «campamento en la villa de Mugi», subtítulo T1 ep. 12, 18:57) ✅.
  **Ella trae el té y los pasteles** ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Tea_time); subtítulo T1 ep. 1,
  14:43).
- **Manía:** le ilusionan las cosas normales: «siempre quise hacer esto»
  (T2 ep. 7, 04:01; T2 ep. 21, 04:15, abrazar a Azusa) ✅ (subtítulos).
  Le encanta ver a dos chicas muy unidas ✅
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/KOn)).
- **Instrumento:** Korg Triton Extreme de 76 teclas ⚠️
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Tsumugi_Kotobuki)).
- **Rasgo:** **cejas gruesas**; Yui dice que parecen *takuan* (rábano
  encurtido) ⚠️ (sólo la wiki). Pelo rubio largo y ondulado ⚠️ (memoria).
- **Cómo se expresa:** muy educada («召し上がって», *sírvanse*), se ríe
  bajito y se emociona sin freno en el MC («¡la banda es divertidísima!»,
  T2 ep. 20, 12:59) ✅ (subtítulo).

### Ritsu Tainaka — la presidenta (batería)

- **Carácter:** presidenta **autoproclamada** del club ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Ritsu_Tainaka)); «porque
  soy la presidenta» es su razón para todo (T1 ep. 5, 15:45) ✅
  (subtítulo).
- **Instrumento:** Yamaha Hipgig, firma Rick Marotta, **Mellow Yellow**
  ⚠️ (sólo la wiki).
- **Relaciones:** pica a Mio y recibe el coscorrón ✅ (TV Tropes). Da la
  orden del té: «¡Mugi, prepara el té!» (T1 ep. 1, 14:43) ✅ (subtítulo).
- **Cómo se expresa:** habla como chico («言っただけだぜ～», T2 ep. 1,
  03:58 ✅ subtítulo), grita, juega a los
  «soldados» («りっちゃん隊員», T1 ep. 3, 18:23) ✅ (subtítulo). Su MC en
  el festival dura dos frases (T2 ep. 20, 14:22: «¡qué corto!») ✅.
- **Cuerpo:** diadema que deja la frente al aire ⚠️ (memoria).

### Sawako Yamanaka — la profesora consejera

- **Carácter:** profesora de música con imagen **dulce**; fue del club y
  tocó guitarra y voz en **Death Devil**, una banda de speed metal, y no
  quiere que se sepa ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Sawako_Yamanaka)).
- **Manía:** **hace trajes** y viste a las chicas, quieran o no ✅ (misma
  wiki; subtítulo T1 ep. 6, 08:00: «¡he hecho trajes!»).
- **El chiste perfecto para #general:** regaña («esto no es sitio para
  tomar té») y a los ocho segundos se come el pastel (T1 ep. 5,
  14:22-14:36) ✅ (subtítulo).
- **Cómo anima:** «みんな 輝いてるわよ！» (*¡brillan todas!*), T2 ep. 20,
  11:37 ✅ (subtítulo).

### Secundarias que conviene tener a mano

- **Ui Hirasawa**, la hermana responsable de Yui: 5.ª en la encuesta de
  Akiba Souken ✅ ([Honey's Anime](https://honeysanime.com/top-5-k-on-characters-japan-poll/)).
- **Nodoka Manabe**, amiga de la infancia de Yui y presidenta del consejo
  estudiantil; en el MC Yui manda a la gente a ella ✅ (subtítulo T2
  ep. 20, 12:20-12:28).
- **Ton**, la tortuga ✅. Es la mascota más fácil de poner en primer plano.

---
## 9 · ¿Quién es la más querida?

**Respuesta corta: Mio, con Azusa pisándole los talones.** Depende de la
época y del país.

| Votación | Resultado | Estado |
|---|---|---|
| Newtype, septiembre de 2009 | **Mio n.º 1** | ✅ [LH Yeung](https://blog.lhyeung.net/2009/08/11/top-10-anime-characters-in-septembers-newtype/) |
| Newtype, 2009 y 2010 seguidos | **Mio n.º 1** | ✅ [NamuWiki](https://en.namu.wiki/w/%EC%95%84%ED%82%A4%EC%95%BC%EB%A7%88%20%EB%AF%B8%EC%98%A4), [Sankaku (2010)](https://news.sankakucomplex.com/2010/12/08/top-10-anime-characters-of-2010-newtype/) |
| International Saimoe League 2010 | **Mio campeona** | ✅ [Saimoe Wiki](https://saimoe.miraheze.org/wiki/Mio_Akiyama), [Moegirl](https://zh.moegirl.org.cn/%E7%A7%8B%E5%B1%B1%E6%BE%AA) |
| Torneo coreano (Korea Best Moe) 2010 | **Mio campeona** | ✅ mismas dos |
| PTT C Chat (Taiwán) 2010 | **Mio campeona** | ⚠️ [Moegirl](https://zh.moegirl.org.cn/%E7%A7%8B%E5%B1%B1%E6%BE%AA) |
| 2channel Saimoe 2010 | **Azusa campeona** | ⚠️ [Saimoe Wiki](https://saimoe.miraheze.org/wiki/Mio_Akiyama) |
| Recochoku, «con quién te casarías», 2009 y 2010 | **Mio n.º 1** | ⚠️ [Wikipedia en coreano](https://ko.wikipedia.org/wiki/%EC%95%84%ED%82%A4%EC%95%BC%EB%A7%88_%EB%AF%B8%EC%98%A4) |
| Akiba Souken (329 votos) | 1 Azusa, 2 Yui, 3 Mio, 4 Ritsu, 5 Ui | ✅ [Honey's Anime](https://honeysanime.com/top-5-k-on-characters-japan-poll/) |
| Minna no Ranking (en curso) | 1 Azusa, 2 Yui, 3 Mio | ⚠️ [ranking.net](https://ranking.net/rankings/best-k-on-characters) |
| Pregunta de fans en Yahoo! Chiebukuro | orden repetido: Mio, Yui, Azusa, Ritsu, Mugi | ⚠️ [Chiebukuro](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1046928525) |
| International Saimoe 2025, por parejas | **Azusa y Yui** campeonas | ⚠️ [Moegirl](https://zh.moegirl.org.cn/%E7%A7%8B%E5%B1%B1%E6%BE%AA) |

- Mio suma **17 títulos**, récord de un personaje de KyoAni, y fue la más
  dibujada en pixiv ⚠️ ([Wikipedia en coreano](https://ko.wikipedia.org/wiki/%EC%95%84%ED%82%A4%EC%95%BC%EB%A7%88_%EB%AF%B8%EC%98%A4)).
- **Para la lámina:** Mio es la cara que el fan reconoce como «la
  favorita», y además **su papel en la serie es poner orden**: perfecta para
  decir «eso va en otro canal». Yui es la anfitriona natural (habla al
  público). Azusa es la segunda opción fuerte.

---

## 10 · Doblaje latino

- **No hay doblaje latino oficial** ✅. Doblaje Wiki sólo tiene
  **propuestas de fans** ([EmmaCar2](https://doblaje.fandom.com/es/wiki/Usuario_Blog:EmmaCar2/K-On!_(Propuesta_de_doblaje_Mexicano)),
  [AnthonyZven](https://doblaje.fandom.com/es/wiki/Usuario_Blog:AnthonyZven/Propuesta_de_doblaje:_K-ON!)),
  y la guía de cuadros ya lo había notado. SomosKudasai confirma que nunca
  salió oficialmente.
- **El doblaje «perdido»** ✅ (estudio y hechos, dos fuentes): **Elocuencia
  Studio**, estudio independiente **chileno** nacido en la pandemia, grabó
  en calidad profesional el ep. 1; se filtró en YouTube a finales de 2020 y
  se borró por derechos de autor
  ([SomosKudasai](https://somoskudasai.com/noticias/el-doblaje-latino-de-k-on-que-quizas-no-conocias/),
  [publicación de FallenSubs en Facebook](https://www.facebook.com/FallenSubsOficial/posts/k-on-episodio-1-en-espa%C3%B1ol-latino-por-elocuencia-studio-compartimos-este-proyect/1780737758752636/)).
- **Reparto de ese doblaje** ⚠️ **dudoso** (una sola fuente,
  [SomosKudasai](https://somoskudasai.com/noticias/el-doblaje-latino-de-k-on-que-quizas-no-conocias/);
  la .org es el mismo medio):

  | Personaje | Actriz | Ficha de la actriz |
  |---|---|---|
  | Yui | Lucía Suárez | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Luc%C3%ADa_Su%C3%A1rez) |
  | Mio | Carolina Cortés | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Carolina_Cort%C3%A9s) |
  | Ritsu | Marlene Pérez | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Marlene_P%C3%A9rez) |
  | Mugi | Bárbara Bustamante | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/B%C3%A1rbara_Bustamante) |

  Las fichas de las actrices existen, pero **no pude abrirlas** para ver si
  nombran K-On!. Un TikTok habla de los responsables
  ([rockeroisrael](https://www.tiktok.com/@rockeroisrael.anime/video/7389514905214340357)),
  sin ver su contenido.
- **Dónde se ve en español:** Crunchyroll, **subtitulado** ✅
  ([Crunchyroll](https://www.crunchyroll.com/es/series/GXJHM3N2E/k-on),
  [JustWatch](https://www.justwatch.com/us/tv-show/k-on)).
- **Consecuencia para la lámina:** las frases van **traducidas del
  japonés por nosotros**, con naturalidad latina. Ninguna se presenta como
  «frase del doblaje». Hay fandubs en YouTube
  ([ejemplo](https://www.youtube.com/watch?v=scal1_PRGh8)), no oficiales.

---

## 11 · Música

| Tema | Dónde | Quién canta | Dato | Ambiente |
|---|---|---|---|---|
| **Cagayake! GIRLS** | OP de la T1 | Yui (Aki Toyosaki) ⚠️ | n.º 4 en Oricon, unas 62 000 copias ⚠️ W | subidón de primer día de clase |
| **Don't say "lazy"** | ED de la T1 | **Mio (Yōko Hikasa)** ⚠️ W | n.º 2 en Oricon, 67 000 ⚠️ W | rock chulo, Mio en modo estrella |
| **GO! GO! MANIAC** | OP 1 de la T2 | Ho-kago Tea Time | **n.º 1**, más de 83 000 ⚠️ W | muy rápido, eufórico |
| **Listen!!** | ED 1 de la T2 | Ho-kago Tea Time | n.º 2 la misma semana ⚠️ W | himno de banda |
| **Fuwa Fuwa Time** | T1 ep. 12, 19:18 | Yui | disco de oro ⚠️ W | la canción del club, dulce |
| **U&I** | T2 | Yui para Ui | single n.º 3 ✅ ([ANN](https://www.animenewsnetwork.com/news/2010-09-13/k-on-gohan-wa-okazu/u&i-single-is-no.3-on-weekly-chart)) | ternura |
| **Tenshi ni Fureta yo!** | T2 ep. 24, 18:44 | las cuatro para Azusa | ✅ (subtítulo) | despedida, llanto |
| Utauyo!! MIRACLE / No, Thank You! | OP 2 y ED 2 de la T2 | — | ⚠️ de memoria | — |

- «W» = sólo Wikipedia (una fuente, dudoso, aunque Wikipedia cita a
  Oricon). Con «GO! GO! MANIAC» y «Listen!!», Ho-kago Tea Time fue el
  **tercer grupo femenino en ocupar a la vez el 1 y el 2** de Oricon, y el
  primero en 26 años ⚠️ W. «Cagayake!» y «Don't say "lazy"» fueron platino
  en descargas ⚠️ W ([Wikipedia](https://en.wikipedia.org/wiki/K-On!),
  [Ho-Kago Tea Time](https://en.wikipedia.org/wiki/Ho-Kago_Tea_Time),
  [discografía](https://en.wikipedia.org/wiki/List_of_K-On!_albums)).
- Letra de «Don't say "lazy"» en el subtítulo: «能ある鷹はそう 見えないとこに
  ピック隠すんです» (*el halcón listo esconde la púa donde no se ve*) ✅.
- **Para #general:** «Fuwa Fuwa Time» es el ambiente (dulce, de merienda).
  Para #que-estas-escuchando (lámina 2), el guiño es «Don't say "lazy"».

---

## 12 · Vídeos

- **Canal oficial de Kyoto Animation:** [KyoaniChannel](https://www.youtube.com/channel/UCpGY2vcoKXf7K6tFzsbSv7w)
  y su [lista de vídeos](https://www.youtube.com/playlist?list=PLQoVKoEXurCsfPK_FZNd3ZFaXHjo1y9nU).
  ⚠️ No localicé el tráiler exacto de K-On!: minuto sin verificar.
- **Análisis:** [K-On | A Kyoto Animation Retrospective](https://www.youtube.com/watch?v=CKn1OgxPK3Y),
  [A Reflection on K-on and Kyoto Animation](https://www.youtube.com/watch?v=q-mjTzzWPak),
  [K-On: Die Krönung Kyoto Animations](https://www.youtube.com/watch?v=fDBb1YRlcx4)
  (alemán). Minuto sin verificar en todos.
- **TikTok:** vídeos en español sobre el doblaje perdido
  ([1](https://www.tiktok.com/@rockeroisrael.anime/video/7330431409305160965),
  [2](https://www.tiktok.com/@rockeroisrael.anime/video/7389514905214340357)).
  **No encontré una tendencia viral** de K-On! en 2024-2026.
- **Lo más útil para la lámina** son los minutos exactos de la sección 2,
  sacados de los subtítulos.

---

## 13 · Videojuegos de la franquicia

- **K-ON! Houkago Live!!** (PSP, SEGA, 30-sep-2010) ✅
  ([UK Anime Network](https://www.uk-anime.net/Games/K-ON!_Houkago_Live!!_(PSP).html),
  [GameFAQs](https://gamefaqs.gamespot.com/psp/997459-k-on-houkago-live)).
  Juego de ritmo; versión **HD para PS3**, 21-jun-2012 ✅
  ([The Cutting Room Floor](https://tcrf.net/K-On!_Houkago_Live!!_(PlayStation_Portable)),
  [GameBrew](https://www.gamebrew.org/wiki/K-ON!_Houkago_Live!!_PSP_-_English_Translation)).
- Cada chica se toca distinto: Yui casi todo con **O**, Azusa con **X** y
  **□**, Mio con las **flechas**, Mugi con **□** y **△** manteniendo,
  Ritsu con **abajo** y **X** ⚠️
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/K-ON!_Ho-kago_Live!!)).
- **Escenas chibi** entre canciones, las chicas charlando antes de
  explicar lo que se ha desbloqueado ✅ (UK Anime Network). **Reloj**: la
  chica que elijas te dice la hora ✅. **Trajes** que se ganan ✅.
  **Bañadores** en el menú chibi ✅ (GameBrew).
- **Idea para la lámina 2:** el menú chibi del juego es un buen precedente
  de «chicas pequeñas señalando opciones». ⚠️ No vi capturas; sin
  interfaz verificada, no copiarla.
- La página de The Cutting Room Floor existe (contenido sin usar), pero no
  pude abrirla.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen

- **El té y el pastel** que trae Mugi; «¡Mugi, el té!» ✅.
- **«Azu-nyan»** y las orejas de gato ✅. **Yui abrazando a Azusa** ✅
  ([Shipping Wiki, YuiAzu](https://shipping.fandom.com/wiki/YuiAzu)).
- **Mio miedosa y avergonzada**; su «no veo, no oigo» ✅.
- **El coscorrón de Mio a Ritsu** ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/KOn)).
- **Gitah** (Yui habla con su guitarra) y **Elizabeth** ✅.
- **Ton**, la tortuga ✅.
- **«Este salón es nuestro Budokan»** (T1 ep. 12) ✅.
- **«Tenshi ni Fureta yo!»** y la graduación (T2 ep. 24) ✅.
- **Sawako y Death Devil** ✅.
- Es **tan de merienda** que el fandom lo llama «moeblob», con cariño y
  con burla ✅ ([Know Your Meme](https://knowyourmeme.com/forums/just-for-fun/topics/13036-fine-ill-watch-k-on));
  existe hasta una parodia, [K-On! The Abridged Series](https://tvtropes.org/pmwiki/pmwiki.php/WebVideo/KOnTheAbridgedSeries).
- **Peregrinación a Toyosato**: los fans van a tomar té en la sala del
  club y a escribir en la pizarra ✅ (sección 5).

### Qué NO hacer (lo que un fan notaría)

- **Piernas finas de anime genérico.** K-On! las tiene llenas, de chica
  real ✅.
- **Brillos en todo el pelo.** Sólo Mio y Azusa tienen brillo ⚠️.
- **Mio encorvada.** Está recta aunque sea tímida ⚠️.
- **Mio diestra.** Es **zurda**: el mástil del bajo va a su derecha ⚠️
  (la wiki; comprobar en un fotograma).
- **Instrumentos cambiados.** Gitah es cereza con centro dorado, no negra;
  Muttan es roja; la batería es amarilla ⚠️ (la wiki; comprobar).
- **Cintas de colores mezcladas** (sección 16).
- **Enseñar la caída de Mio en el festival** (T1 ep. 6, 21:01): es un
  momento famoso, pero es *fanservice*; no va en una lámina.
- **Chistes con fuego o con el estudio.** En 2019 un incendio provocado en
  Kyoto Animation mató a 36 personas ✅; entre ellas, según un resumen de prensa,
  **Junichi Eda**, que animó K-On! ⚠️ ([Wikipedia](https://en.wikipedia.org/wiki/Kyoto_Animation_arson_attack),
  [Japan Times, homenaje de 2026](https://www.japantimes.co.jp/news/2026/07/18/japan/kyoto-animation-memorial-service/)).
- **Rock agresivo, neón, oscuridad.** Es pastel y tranquilo.
- **Presentar frases como «del doblaje latino».** No hay doblaje oficial.

---
## 15 · Poses analizadas por personaje

**Cómo leer esto.** El minuto y lo que pasa salen del subtítulo ✅; quién
habla, por contexto (ver el aviso de la sección 2). **La
postura, las manos y la mirada son de memoria ⚠️**: no pude ver los
fotogramas. Antes de dibujar, hay que capturar ese minuto y mirarlo.
La última columna dice para qué sirve: **presentar, explicar, celebrar,
regañar, pensar, animar**.

### Mio

| Momento | Ep. y min | Qué hace | Pose ⚠️ | Sirve para |
|---|---|---|---|---|
| «¡El club no es una cafetería!» ⚠️ | T1 ep. 2, 05:32 | corta a Yui | de pie, brazos cruzados o mano en la cadera, ceño | **regañar / redirigir** |
| «No veo, no oigo» | T1 ep. 5, 02:30 | se asusta | agachada, manos en las orejas, ojos cerrados | pensar (miedo) |
| Le leen sus letras | T1 ep. 5, 15:14-16:22 | se muere de vergüenza | cara roja, manos delante, quiere quitar el cuaderno | **explicar** con humor |
| Canta «Fuwa Fuwa Time» en su primer festival | T1 ep. 6, 18:19-20:35 | canta y toca | recta, zurda, micro | **celebrar** |
| MC del último festival | T2 ep. 20, 12:00-12:14 | «tocar con todas ha sido lo mejor» | tímida pero firme, bajo colgado | **presentar** |
| Pide que Azusa escuche | T2 ep. 24, 18:20 | anuncia la canción | de pie, seria y cálida | **explicar / anunciar** |
| Miedo en el campamento | T1 ep. 4, 17:35 | «no oigo, no oigo» | acurrucada | pensar |

### Yui

| Momento | Ep. y min | Qué hace | Pose ⚠️ | Sirve para |
|---|---|---|---|---|
| Se despierta tarde | T1 ep. 1, 00:42-00:58 | corre al colegio | carrera, tostada o bolso, pelo revuelto | animar |
| «¡Me apunto!» | T1 ep. 1, 20:13 | entra al club | brazos arriba, sonrisa enorme | **celebrar** |
| Nace «Azu-nyan» | T1 ep. 9, 11:09 | pone el mote | se lanza a abrazar | animar |
| MC «nuestro Budokan» | T1 ep. 12, 18:32-19:11 | habla al público | micro en mano, Gitah colgada, mirada al frente | **presentar / explicar** |
| «¡Amo el club!» | T1 ep. 12, 21:57 | grita de alegría | brazos abiertos | **celebrar** |
| Voz en off, las presenta | T2 ep. 1, 04:13-04:55 | presenta a cada una | (planos de cada chica) | **presentar** |
| «¡Fu-n-su!» | T2 ep. 1, 06:30 | se decide | puños apretados, mofletes | **animar** |
| MC del último festival | T2 ep. 20, 11:45-14:09 | presenta y manda a la gente a Nodoka | señala al público, micro | **redirigir** |

### Azusa

| Momento | Ep. y min | Qué hace | Pose ⚠️ | Sirve para |
|---|---|---|---|---|
| «Nya» con orejas de gato | T1 ep. 9, 11:02 | dice «nya» a su pesar | manitas de gato, cara roja | el meme |
| «¿Y el ensayo?» | T1 ep. 9, 17:47 | protesta | de pie junto a la mesa, puños | **regañar** |
| «Ensayemos ya» | T1 ep. 12, 06:02 | mete prisa | señala los instrumentos | regañar |
| Se presenta en el MC | T2 ep. 20, 13:45 | «soy Azusa Nakano, encantada» | reverencia nerviosa | **presentar** |
| «Muttan, por Mustang» | T2 ep. 20, 19:24 | explica el nombre | guitarra en brazos | **explicar** |
| «¡Quiero pastel!» | T2 ep. 20, 19:29 | pide merienda | alegre, sentada | celebrar |
| Despedida | T2 ep. 24, 17:43 | «estoy bien» | llorando, intenta sonreír | pensar |

### Mugi

| Momento | Ep. y min | Qué hace | Pose ⚠️ | Sirve para |
|---|---|---|---|---|
| «Bienvenida» y primer té | T1 ep. 1, 14:40-14:54 | sirve el té | tetera en la mano, sonrisa suave | **presentar** |
| «¿Un pastel?» a Sawako | T1 ep. 5, 14:30 | calma a la profe | plato en las dos manos | **redirigir con dulzura** |
| «Mi sueño era dormir fuera con todas» | T1 ep. 4, 04:43 | se ilusiona | manos juntas, ojos brillantes | animar |
| «Siempre quise hacer esto» | T2 ep. 7, 04:01 | se disculpa feliz | manos en las mejillas | pensar |
| MC «¡es divertidísimo!» | T2 ep. 20, 12:48-13:03 | se emociona | se inclina, habla rápido | **celebrar** |

### Ritsu

| Momento | Ep. y min | Qué hace | Pose ⚠️ | Sirve para |
|---|---|---|---|---|
| «¡Mugi, el té!» | T1 ep. 1, 14:43 | manda | dedo arriba, sonrisa pícara | **presentar** |
| «Porque soy la presidenta» | T1 ep. 5, 15:45 | exige ver las letras | pecho fuera, mano extendida | explicar (en broma) |
| Recibe el coscorrón | T1 ep. 9, 13:35 | «¡ay!» | mano en la cabeza | el chiste |
| «¡Me encanta dar caña a la batería!» | T2 ep. 3, 20:30 | lo grita | baquetas arriba | **celebrar** |
| MC de dos frases | T2 ep. 20, 14:11-14:22 | «pues siguiente canción» | nerviosa, rápida | el chiste |

### Sawako

| Momento | Ep. y min | Qué hace | Pose ⚠️ | Sirve para |
|---|---|---|---|---|
| «¡Esto no es sitio para tomar té!» | T1 ep. 5, 14:19-14:22 | regaña | inclinada sobre la mesa, dedo | **regañar** |
| «Gracias» (y se come el pastel) | T1 ep. 5, 14:36 | cambia de cara | sentada, tenedor | el chiste |
| «¡He hecho trajes!» | T1 ep. 6, 08:00 | trae ropa | brazos llenos de trajes | explicar |
| «¡Brillan todas!» | T2 ep. 20, 11:37 | anima desde el público | mano en alto | **animar** |

---

## 16 · Vestuario

- **Uniforme de Sakuragaoka:** blazer, camisa blanca y **cinta al cuello
  de color por curso**: **azul, rojo y verde**. Se conserva el color de
  primero hasta graduarse ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/Sakuragaoka_High_School),
  [Danbooru](https://danbooru.donmai.us/wiki_pages/sakuragaoka_high_school_uniform)).
  En el año de la T2, **tercero = azul, segundo = rojo, primero = verde**
  ✅ (misma fuente). **Por tanto: Yui, Mio, Ritsu, Mugi y Nodoka van con
  azul; Azusa, Ui y Jun, con rojo** (deducción mía de esas dos reglas).
- **Colores de la tela** ⚠️ (estimados): blazer azul marino `#2F3553`,
  falda oscura, camisa `#F7F7F5`, cinta azul `#3A5DAE`, cinta roja
  `#C2323A`. Hay réplicas licenciadas para comparar la tela:
  [uniforme de verano](https://b2b.mile-stone.jp/en/products/000378945),
  [uniforme de invierno](https://b2b.mile-stone.jp/en/products/groups/17474)
  (MILESTONE).
- **Lo icónico, lo que todos reconocen:** **el uniforme de invierno con su
  instrumento**. Es la imagen de las portadas y del merchandising ⚠️
  (impresión de las búsquedas, no medida).
- **Trajes de escenario de Sawako** (T1 ep. 6, 08:00; T1 ep. 12, 03:34:
  «elijan traje de aquí») ✅ (subtítulo). ⚠️ Cómo son, sin ver.
- **Orejas de gato de Azusa** ✅ (sección 8).
- **Camisetas del último festival**, regalo sorpresa (T2 ep. 20, 15:56:
  «¡gracias por las camisetas, profe!») ✅ (subtítulo). ⚠️ Diseño sin ver.
- **Accesorios fijos:** horquillas amarillas de Yui ⚠️, diadema de Ritsu
  ⚠️, coletas de Azusa ⚠️ (memoria).

---

## 17 · Paisajes y fondos de pantalla

- **Toyosato** (Shiga): pasillos de madera, escaleras con la liebre y la
  tortuga, sala del club con pizarra ✅/⚠️ (sección 5). Fotos:
  [Wayfarer Dave](https://www.wayfarerdaves.com/?p=2483),
  [Be Wa Shiga](https://www.bewashiga.com/article/toyosato-elementary/),
  [Otaku Japan](https://otakutrips.com/en/spot/2460bd0d-c875-4a89-b3b8-6e8c55222c3f),
  [NamuWiki](https://en.namu.wiki/w/%ED%86%A0%EC%9A%94%EC%82%AC%ED%86%A0%20%EC%B4%88%EB%93%B1%ED%95%99%EA%B5%90).
- **Kioto**: calles reales de la serie en la guía de 38 lugares ✅
  ([Pilgrimage Guild](https://libert.co.jp/pilgrimage-guild/keion-anime-pilgrimage/)).
- **Londres** (película, viaje de graduación) ✅
  ([K-ON! Wiki](https://k-on.fandom.com/wiki/K-ON!_Movie),
  [Analog Housou](https://analoghousou.com/2011/12/12/nonstop-to-london-k-on-the-movie/)).
- **Hora del día:** **después de clase**, la tarde, con luz dorada ⚠️
  (lo pide el nombre de la banda; no medido).
- **Fondos de pantalla en alta:** ⚠️ no encontré ninguno con tamaño y autor
  verificables. El mejor candidato oficial es la ilustración de grupo del
  15.º aniversario (sección 3.2).

---
## 18 · Guía para generar con IA (Firefly, Canva)

Sirve para bocetos de pose o de fondo. **Nunca para la lámina final** (el
dueño pide que no parezca hecho por IA). Lo final se dibuja o se recorta
de fotogramas y se integra con `v3/integrar.py`.

### Rasgos que nunca cambian

- **Mio:** pelo negro, largo y liso, flequillo recto; alta y **recta**;
  bajo **zurdo** sunburst.
- **Yui:** pelo castaño corto a los hombros, algo revuelto, **dos
  horquillas amarillas**; guitarra Les Paul cereza con centro dorado.
- **Azusa:** pelo negro con **dos coletas largas**, la más bajita;
  guitarra Mustang roja.
- **Mugi:** pelo rubio claro, largo y ondulado; **cejas gruesas**;
  teclado; tetera.
- **Ritsu:** pelo castaño claro, **frente al aire con diadema**; batería
  amarilla.
- **Sawako:** adulta, gafas, ropa de profesora ⚠️ (memoria).
- Todas: **uniforme azul marino** ⚠️ con cinta azul (las mayores) o roja
  (Azusa).
- ⚠️ Los peinados de Azusa, Mugi y Ritsu y las gafas de Sawako son de
  memoria: comprobarlos en las galerías de la sección 3.4.

### Estilo

- **Línea:** fina, limpia, marrón oscuro o gris, sin grosor variable
  exagerado ⚠️ (memoria del estilo KyoAni 2009).
- **Sombra:** una sola capa de sombra suave, tono frío lavanda; sin
  brillos en el pelo salvo Mio y Azusa.
- **Cuerpo:** proporciones reales de chica de instituto, **piernas
  llenas**, caras redondas, ojos grandes con pocos reflejos.
- **Luz:** tarde, sol dorado y bajo entrando por ventanas de madera.
- **Encuadre:** planos de pies y manos, cámara a la altura de la mesa;
  profundidad de campo (fondo desenfocado), como en cine.

### Palabras que ayudan

«slice of life», «after school», «afternoon golden light», «wooden
classroom», «tea set and cake», «soft pastel colors», «clean thin line
art», «flat cel shading», «school blazer», «shallow depth of field».

### Palabras que lo estropean

«sexy», «glossy hair», «long thin legs», «neon», «grunge», «rock
concert», «hyper-detailed», «3D render», «dramatic lighting», «dark».

### Qué imágenes usar como referencia

- **Estilo y grupo:** la ilustración del 15.º aniversario de Horiguchi
  (sección 3.2).
- **Sala y mesa:** el [modelo del club en Sketchfab](https://sketchfab.com/3d-models/k-on-clubroom-b08830de23c94c8fbfb1218d79c63fd1)
  y las fotos de Toyosato ([Wayfarer Dave](https://www.wayfarerdaves.com/?p=2483)).
- **Pose de cada una:** los minutos de la sección 15.

---

## 19 · Tres conceptos para la lámina de #general

Textos del canal (sección 0): **título**, «Aquí se habla de lo que sea»,
«¿Micros, voces o técnica? Eso va a #general-doblaje», «¿Tu voz grabada?
A #demos», y el guiño «¡Pasa, que hay té!».

### Concepto A — «¡Hora del té!» La mesa del club (el objeto del plan, mejorado)

- **Objeto y sitio:** la **mesa del club** en la sala del tercer piso, a
  media tarde. En Blender: la mesa, el juego de té (Sketchfab, sección 4.2),
  dos platos con pastel y, lo nuevo, **una carta del té de cartulina
  doblada** escrita a rotulador por Mugi. La tinta sigue el doblez de la
  cartulina. Detrás, **la pizarra** del club.
- **Personajes:**
  - **Mio**, la más querida, de pie junto a la mesa, **señalando la
    carta** con cara de «esto no va aquí». Pose base: T1 ep. 2, 05:32
    («¡el club no es una cafetería!», ⚠️ confirmar que es ella).
  - **Mugi**, sentada, **sirviendo el té**, sonrisa suave. Pose base: T1
    ep. 1, 14:54.
  - **Yui**, en primer plano a la derecha, con el tenedor en la boca.
- **Cómo habla:** no hay globo. **Lo escrito está en la carta y en la
  pizarra**, objetos de la serie. La única frase dicha, la de Mugi, va en
  una **viñeta estrecha de 4-koma** con marco negro fino.
- **Dónde va cada texto:**
  - pizarra: **«¡general!»** en Mochiy Pop One, con una ♪ dibujada;
  - carta, arriba: «Menú de hoy: se habla de lo que sea» (Yusei Magic);
  - carta, abajo, bajo «No se sirve aquí»: «Micros, voces y técnica:
    #general-doblaje» y «Tu voz grabada: #demos», con flechas a mano;
  - viñeta 4-koma de Mugi: «¡Pasa, que hay té!».
- **Para que no quede plano:** sol bajo por la ventana de la izquierda,
  sombras largas de las tazas sobre la mesa; **vapor** de la tetera;
  **taza y pastel desenfocados delante**, abajo a la izquierda; al fondo,
  la pecera de **Ton** con reflejos de agua.

### Concepto B — «Nuestro Budokan» El MC del festival

- **Objeto y sitio:** el **salón de actos** en pleno festival. El objeto
  es **la setlist de papel pegada con cinta al suelo del escenario**,
  junto al pie de micro, escrita a rotulador. En Blender: el papel un poco
  curvado, la cinta americana y un monitor de escenario.
- **Personajes:** **Yui** al micro, con Gitah colgada, **hablando al
  público y señalando** (T1 ep. 12, 18:32-19:11; T2 ep. 20, 11:45). Detrás,
  **Mio** con el bajo, zurda, sonrojada; Ritsu, Mugi y Azusa en sus
  puestos.
- **Cómo habla:** el MC es hablado; la información está **en la setlist**,
  que es como Yui guía al público. Letra: Yusei Magic, con números de
  canción.
- **Dónde va cada texto:**
  - pancarta del festival arriba: **«¡general!»**;
  - setlist: «1. Aquí se habla de lo que sea», «2. Micros, voces y
    técnica: #general-doblaje», «3. Tu voz grabada: #demos»,
    «Bis: ¡pasa y quédate!».
- **Para que no quede plano:** luces **rosa** de escenario (así pidieron
  el estribillo de «Fuwa Fuwa Time», T1 ep. 14, 12:16); **manos del público en
  primer plano**, en silueta; el pie de micro tapa un poco a Yui; algo de
  humo en el haz de luz.

### Concepto C — «¡Se buscan socias!» El tablón de la escalera

- **Objeto y sitio:** un **tablón de corcho** en el pasillo de madera de
  Toyosato, junto a **la escalera con la liebre y la tortuga de bronce**
  en la barandilla. En Blender: el corcho, **tres carteles de papel**
  clavados con chinchetas, con las esquinas levantadas.
- **Personajes:** **Azusa**, la n.º 1 de las votaciones japonesas
  recientes, **clavando el cartel** muy seria. **Yui** la abraza por
  detrás («¡Azu-nyan~!», el gesto que el fandom adora, T1 ep. 9, 11:09).
- **Cómo habla:** los carteles son el cuadro. Azusa deja además **una
  nota adhesiva** con su letra ordenada (Zen Maru Gothic).
- **Dónde va cada texto:**
  - cartel grande: **«¡general!»** y «Aquí se habla de lo que sea»;
  - cartel con flecha hacia arriba: «Micros, voces y técnica:
    #general-doblaje»;
  - cartel con flecha hacia el pasillo: «Tu voz grabada: #demos»;
  - nota de Azusa: «¡Pasa, que hay té!».
- **Para que no quede plano:** la **tortuga de bronce de la barandilla
  en primer plano**, desenfocada; luz de la ventana del rellano con polvo
  en el aire; el pasillo se aleja al fondo.

### Lámina 2 (si hace falta): «¿A dónde voy?»

Sale natural del **concepto C**: el mismo tablón, ahora lleno. Un cartel
por canal de LA SALA: #que-estas-viendo, #que-estas-escuchando,
#a-que-juegas, #memes, #comandos-y-sorteos y la sala de voz General.
#destacados, con su propio aviso: «Aquí no se escribe». Ton, dibujado en
una esquina de un cartel, como sello del club.

### ¿Cuál primero?

**El A.** Es el objeto del plan, es el centro de la serie y lo dice
Mio, la más querida, haciendo lo que hace en pantalla: poner orden con
cariño. El B es el más espectacular. El C deja lista la lámina 2.

---

## 20 · Lo que no pude verificar

- **Ninguna imagen** abierta ni medida: sin hojas de contacto, sin tamaños.
- **Poses concretas** (manos, mirada): de memoria. Los minutos, sí son
  exactos del subtítulo.
- **Reparto del doblaje de Elocuencia Studio:** una sola fuente, dudoso.
- **Portadas del Blu-ray y del manga** una por una.
- **Caja de texto del videojuego:** no vi capturas.
- **Colores hex:** estimados, no medidos.
- **Keifont:** si trae tildes y ñ, sin comprobar.
- **Tráiler oficial** y tendencias de TikTok: no localizados.
- **Reddit:** el buscador no deja entrar en reddit.com y Arctic Shift daba
  error de conexión.
- Los minutos de la T2 salen de la emisión de TBS: en Crunchyroll pueden
  moverse uno o dos.

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)

- `curl https://community.fandom.com` → **000** (el proxy rechaza el túnel, 403).
- WebFetch bloqueado: somoskudasai.com, ultimatemegax.wordpress.com.
- curl bloqueado: api.sketchfab.com, api.polyhaven.com,
  arctic-shift.photon-reddit.com.
- La búsqueda de la API de GitHub también está cerrada (sólo repos de la
  sesión), pero **github.com por WebFetch y raw.githubusercontent.com por
  curl sí funcionan**.
- Sin red completa **no se corrió** `investigar_serie.py` y **no hay
  `hojas/`**.

### Búsquedas web (50 hechas, 1 rechazada)

| # | Búsqueda | Idioma | Dominio |
|---|---|---|---|
| 1 | K-On! doblaje latino | es | — |
| 2 | K-On! popularity poll official results Mio Azusa Yui | en | — |
| 3 | けいおん! 人気投票 結果 澪 梓 | ja | — |
| 4 | Elocuencia Studio K-On! doblaje Lucía Suárez Carolina Cortés Mio | es | — |
| 5 | K-On! doblaje ficha reparto | es | doblaje.fandom.com |
| 6 | Top 5 K-On! Characters Japan Poll Akiba Souken | en | honeysanime.com |
| 7 | "Elocuencia" K-On doblaje chileno Marlene Pérez Bárbara Bustamante | es | — |
| 8 | Mio Akiyama Newtype character ranking first place 2009 2010 Saimoe | en | — |
| 9 | 堀口悠紀子 けいおん キャラクターデザイン インタビュー | ja | — |
| 10 | 山田尚子 けいおん インタビュー 演出 足 芝居 | ja | — |
| 11 | K-On! Naoko Yamada interview character acting legs feet direction | en | — |
| 12 | けいおん! 公式サイト TBS キービジュアル 放課後ティータイム | ja | — |
| 13 | K-On! staff interviews Horiguchi character design colors hair | en | ultimatemegax.wordpress.com |
| 14 | K-On! light music club room tea set cake Mugi tortoise Ton-chan whiteboard | en | k-on.fandom.com |
| 15 | Toyosato elementary school K-On! music room pilgrimage turtle staircase | en | — |
| 16 | K-On! logo font typeface identify | en | — |
| 17 | けいおん ロゴ フォント 似ている 字体 | ja | — |
| 18 | K-ON! Houkago Live PSP rhythm game interface dialogue text box | en | — |
| 19 | K-On! kakifly yonkoma manga art style panels Manga Time Kirara | en | — |
| 20 | K-On! Mio lyrics notebook "Fuwa Fuwa Time" embarrassing lyrics | en | — |
| 21 | Mio Akiyama personality shy left-handed Jazz Bass Elizabeth fan club | en | k-on.fandom.com |
| 22 | Yui Hirasawa Gitah Les Paul Heritage Cherry Sunburst Ui | en | k-on.fandom.com |
| 23 | Ritsu Yamaha Hip Gig; Tsumugi Korg Triton eyebrows | en | k-on.fandom.com |
| 24 | Azusa Mustang Azu-nyan; Sawako Death Devil costumes | en | k-on.fandom.com |
| 25 | K-On! subtitles srt ass episodes repository | en | github.com |
| 26 | Mio Akiyama International Saimoe League 2010 winner Korea | en | saimoe.miraheze.org, en.namu.wiki |
| 27 | K-On! OP/ED Oricon chart GO! GO! MANIAC Listen!! | en | — |
| 28 | K-On 3D model | en | sketchfab.com |
| 29 | tea set teapot teacup cake slice free download CC | en | sketchfab.com, polyhaven.com |
| 30 | Sakuragaoka High School uniform ribbon color year | en | — |
| 31 | K-On! memes Mugi Azunyan Ui Mio | en | knowyourmeme.com |
| 32 | K-On! anime tropes Yui Mio Ritsu Mugi Azusa Sawako | en | tvtropes.org |
| 33 | r/k_on favorite scene tea time Mio Azusa | en | reddit.com (**rechazada**) |
| 34 | K-On! Blu-ray volume cover art Horiguchi jacket list | en | — |
| 35 | けいおん! Blu-ray 1巻 ジャケット 堀口悠紀子 描き下ろし | ja | — |
| 36 | 京都アニメーション けいおん! 作品情報 美術監督 色彩設計 | ja | — |
| 37 | K-On! official trailer PV Kyoto Animation | en | youtube.com |
| 38 | 轻音少女 人气投票 秋山澪 中野梓 萌战 冠军 | zh | — |
| 39 | K-ON! Houkago Live!! screenshots menu chibi dialogue box | en | gamebrew, uk-anime, gamefaqs, tcrf |
| 40 | K-On! Crunchyroll Latinoamérica subtitulado español | es | — |
| 41 | K-On! Movie London key visual Horiguchi 2011 | en | — |
| 42 | K-On! color palette hex hair color codes | en | — |
| 43 | 豊郷小学校旧校舎群 階段 手すり ウサギとカメ けいおん | ja | — |
| 44 | K-On! fan art illustration Houkago Tea Time | en | pixiv, deviantart, artstation, zerochan, wallhaven |
| 45 | けいおん! 15周年 描き下ろし イラスト 京アニ 2024 | ja | — |
| 46 | K-On! TikTok trend 2024 2025 viral edit | en | — |
| 47 | Kyoto Animation arson 2019 victims K-On! staff | en | — |
| 48 | みんなのランキング けいおん キャラ 1位 秋山澪 | ja | ranking.net y otros |
| 49 | 케이온 아키야마 미오 인기 캐릭터 순위 경음부 | ko | — |
| 50 | wood floor planks table wood texture CC0 | en | polyhaven.com, ambientcg.com |

### GitHub (sin cupo)

- [Yeniifan/Anime-Japanese](https://github.com/Yeniifan/Anime-Japanese/tree/main/subtitles):
  no tiene K-On!.
- [Subtitle-Archival-Initiative/anime-subtitle-archival](https://github.com/Subtitle-Archival-Initiative/anime-subtitle-archival):
  no tiene K-On!.
- [Matchoo95/JP-Subtitles](https://github.com/Matchoo95/JP-Subtitles/tree/master/K-ON!):
  **sí**. Bajé los **40 archivos** `.ass` (T1: 14 del Blu-ray; T2: 26 de
  TBS, incluidos los dos especiales), los pasé a texto y busqué las frases.
  Los archivos quedaron en el scratchpad, no en el repositorio.
- [google/fonts](https://github.com/google/fonts): `METADATA.pb` de 16
  letras y 10 archivos `.ttf` revisados con fontTools (sección 6.2).

### Fuentes consultadas por tipo

- **Oficiales:** web de Kyoto Animation (3 fichas), Kyoani Shop (tienda y
  X), Amazon JP y Tower (Blu-ray), Animaru (TBS), Newtype/Kujibikido,
  Anime!Anime!, Collabo-Cafe.
- **Staff:** entrevistas de Yamada, Yoshida y Horiguchi (libros oficiales
  traducidos en ultimatemegax), AV Club, Medium, Pixiv Encyclopedia.
- **Otros idiomas:** japonés (Forest Watch, Coliss, Japaaan, Jalan,
  Waraku, Chiebukuro, ranking.net, atwiki), chino (Moegirl), coreano
  (Wikipedia coreana, NamuWiki).
- **Wikis:** K-ON! Wiki (Fandom), TV Tropes, Wikipedia, Saimoe Wiki,
  Shipping Wiki, Danbooru, The Cutting Room Floor.
- **Foros:** Know Your Meme (foro), Yahoo! Chiebukuro, GameFAQs.
  Reddit **no accesible**.
- **Arte:** DeviantArt (5 obras), pixiv (1), Sketchfab (8 modelos).
- **Vídeo:** KyoaniChannel, 3 análisis en YouTube, 2 TikTok, 1 fandub.
- **Código y recursos:** GitHub (subtítulos y letras), Poly Haven,
  ambientCG, color-hex.
- **Doblaje:** Doblaje Wiki (búsqueda), SomosKudasai, Facebook de
  FallenSubs, Crunchyroll, JustWatch.

### Lo que NO encontré

- Doblaje latino oficial (no existe) ni una segunda fuente para el reparto
  de Elocuencia Studio.
- Tráiler oficial en YouTube con su enlace exacto.
- Artbook con ficha verificable.
- Fondos de pantalla con tamaño y autor.
- Tendencia de TikTok sobre K-On!.
- Capturas de la caja de diálogo del juego de PSP.
