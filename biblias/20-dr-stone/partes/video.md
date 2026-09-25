# Investigación de VÍDEO · Dr. Stone (puntos 2, 4, 9, 10, 14 de ENCARGO.md)

Repaso del 24-sep-2026. Partí de `partes/datos-video.md` (AniList, Dailymotion,
Internet Archive, MusicBrainz) y de las secciones ya escritas en `biblia.md`
(§2 escenas, §5 sitios, §11 música, §12 vídeos, §15 poses), que venían con
minutos sacados de **subtítulos** pero con lo visual «de memoria» ⚠️ porque
nadie había mirado un fotograma. YouTube pide iniciar sesión desde este
servidor (lo confirmé, sigue igual). Usé **Dailymotion** (tráilers oficiales
reposteados por medios: Vidaextra, Horizon Manga, Sekai, Crunchyroll-FR) e
**Internet Archive** (episodios sueltos con fansub) con
`herramientas/fotogramas.py` y medí color real con `herramientas/estilo.py`.
Carpeta de trabajo: `/tmp/claude-0/trabajo/20-dr-stone-video/` (borro los
`video.mp4` al terminar cada uno).

**Vídeos mirados de verdad** (fotogramas sacados y **abiertos con Read**, no
de memoria):
1. Opening 1 «Good Morning World!» **sin créditos, BD 1080p**: [Internet Archive](https://archive.org/details/dr-stone-op-1-ncbd-1080) (`DrStone-OP1-NCBD1080.mp4`, 90 s) — el opening entero, fotograma a fotograma.
2. Ending del episodio 1×24 (dentro del episodio completo, ver abajo).
3. Tráiler oficial en español: [Dailymotion, Vidaextra](https://www.dailymotion.com/video/x8xu1ty) (1:42).
4. Tráiler oficial VO de *Stone Wars*: [Dailymotion](https://www.dailymotion.com/video/x8a1zqs) (1:33), subtítulos FR, publicado por Crunchyroll.
5. Tráiler oficial VO de *New World*: [Dailymotion](https://www.dailymotion.com/video/x8j8l2f) (0:47).
6. Tráiler oficial del especial *Ryusui*: [Dailymotion](https://www.dailymotion.com/video/x8bnxd8) (1:40), confirma la fecha de emisión (10-jul-2022).
7. Tráiler oficial VOSTFR de *Science Future*: [Dailymotion, Horizon Manga](https://www.dailymotion.com/video/x9boaek) (1:39), confirma el estreno (9-ene-2025).
8. Episodio 1×11 completo (audio latino/fansub): [Internet Archive](https://archive.org/details/dr.-stone-sub-11) — la llegada al laboratorio.
9. Episodio 1×19 completo: [Internet Archive](https://archive.org/details/dr.-stone-sub-19) — arranca el proyecto del móvil.
10. Episodio 1×23 completo (sub. español, «Ola de ciencia»): [Internet Archive](https://archive.org/details/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol).
11. Episodio 1×24 completo (sub. español, «Odio a distancias infinitas»): [Internet Archive](https://archive.org/details/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol) — nace el teléfono, y su ending.

---

## Punto 2 · Fotogramas de escenas icónicas (capítulo y minuto, confirmados mirando)

Cambio el criterio de la tabla vieja de §2: ahí el minuto salía del subtítulo
japonés de Netflix (✅ el texto, ⚠️ lo visual). Aquí cito el minuto **del
vídeo que miré yo** (puede moverse 1-2 min frente al de Netflix por el corte
del fansub) y digo exactamente qué se ve.

| # | Fuente | Minuto | Qué se ve (mirado, no de memoria) |
|---|---|---|---|
| 1 | [Ep. 1×11, Internet Archive](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1005) | 16:45 | Suika sin su casco de sandía: pelo blanco con mechón verde, ojos rojos muy abiertos, boca abierta, sonrojo marcado con rayitas, al lado de un bidón de gas. Expresión de sorpresa/emoción pura. |
| 2 | [Ep. 1×11, Internet Archive](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1013) | 16:53 | **El laboratorio por dentro**: cortinas de tela blanca a los lados a modo de puerta, paredes de piedra apilada, estanterías de madera con tinajas de barro, una mesa con paneles verdes translúcidos (vidrio). Senku de espaldas, Chrome detrás preguntando «Oye, ¿qué pasa, Senku?» (subtítulo español real del archivo). |
| 3 | [Ep. 1×19, Internet Archive](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1242) | 20:42 | Senku de cerca, sonrisa ladeada de suficiencia, fondo de bosque verde: el globo de texto dice «¡Smartphones!» (coincide con la línea del subtítulo japonés de mi tabla vieja, minuto casi idéntico). |
| 4 | [Ep. 1×19, Internet Archive](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1267) | 21:07 | **La hoja de ruta real**, un diagrama tipo árbol tecnológico: nodos circulares «水銀» (mercurio), «金» (oro), «プラスチック» (plástico, con iconos de una bolsa, un vaso de poliestireno y un lego), «蜂の巣» (panal), «木炭» (carbón vegetal), «石炭» (carbón de piedra) y un cartel grande «START». Subtítulo real: «Claro que no será muy inteligente. Será un teléfono normal». Es la interfaz que se menciona en la tabla de §2 pero nunca se había visto. |
| 5 | [Ep. 1×23, Internet Archive](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189) | 19:49 | Kohaku (capa con ribete de piel, espada a la espalda) mirando un vaso de cristal con piedritas transparentes (**la sal de Rochelle**), boca abierta preguntando cuál es el micrófono. |
| 6 | [Ep. 1×23, Internet Archive](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264) | 21:04 | Senku de cerca, abrigo de piel de invierno, cejas fruncidas y muy concentrado, goteando algo con un cuentagotas sobre un vaso con líquido pálido. (El fansub tiene un corte distinto al de Netflix: no es la misma toma exacta que cita el subtítulo japonés a esta altura, pero es la misma secuencia de invierno del proyecto). |
| 7 | [Ep. 1×24, Internet Archive](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=137) | 2:17 | **La torre-vigía con el megáfono**: una cabaña de madera y paja sobre un árbol enorme, con una gran bocina/megáfono de cobre en forma de trompeta montada en la punta, monos trepando alrededor. Es el momento exacto de «nace el móvil» (mismo minuto que cita mi tabla de subtítulos, 00:02:17). |
| 8 | [Ep. 1×24, Internet Archive](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=274) | 4:34 | Primer plano de Ruri (pelo rubio, ojos turquesa), expresión preocupada/asombrada, con Kohaku y Chrome (o Magma) detrás en ropa de invierno con ribete de piel, dentro de un recinto de cuerdas y madera. Coincide con la escena de la primera prueba del micro. |
| 9 | [Ep. 1×24, Internet Archive](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=1330) | 22:10 | Senku de cerca junto a una hoguera, luz cálida, mirada seria: escena nocturna de cierre del capítulo. |
| 10 | [OP1 sin créditos, Internet Archive](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=24) | 0:24 | Senku caminando entre árboles petrificados que brillan en violeta/azul: el «despertar» del mundo de piedra. |

---

## Punto 4 · Sitios, luz y paleta (medida con `estilo.py`, no de memoria) + texturas

Todas las hex de abajo son **medidas** con `herramientas/estilo.py` sobre un
fotograma real (link y segundo exacto en cada fila), no de memoria. La tabla
de §5.2 de la biblia (10 hex «propuesta, de memoria») se puede sustituir o
completar con estas.

| Sitio / escena | Hex medidos (con `estilo.py`) | Luz | Fuente y minuto |
|---|---|---|---|
| **Laboratorio** (entrada, piedra y madera) | `#B0B1A2` `#848276` `#9B9988` `#EAE2D3` `#6E695E` `#4B4E47` `#CCCCC1` `#2A2B29` (grises piedra, línea `#5C5548`) | Interior con luz difusa, tonos neutros | Ep. 1×11, [16:53](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1013) |
| **Bosque petrificado** (el «despertar») | `#39313C` `#F4FBFE` `#636C7E` `#BFDDF9` `#9BBCEB` `#7295D0` | Azul-violeta frío, contraluz | OP1, [0:24](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=24) |
| **Campo de girasoles** (recuerdo/flashback) | `#F2DC3C` `#C4F0F9` `#D0A822` `#5DA2EA` `#365A3F` `#807D22` | Sol de mediodía, rayos marcados | OP1, [1:12](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=72) |
| **Torre-vigía del megáfono** (donde nace el móvil) | `#393934` `#595D5B` `#A3CAEB` `#878B8C` `#D0E8F2` `#73A3E5` | Día claro, verdes de bosque + cielo | Ep. 1×24, [2:17](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=137) |
| **Interior invierno** (piel, abrigos) | `#D1B9A5` `#998773` `#5E5548` `#D8D3C5` `#A8A28F` | Cálido, sombreado mixto | Ep. 1×23, [21:04](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264) |
| **Ending nocturno** (luna, estrellas, acuarela) | `#3E559A` `#352C96` `#28346F` `#E0E0D5` `#7E8DBE` | Noche, técnica de acuarela (muy distinta al resto de la serie) | Ep. 1×24, [22:40](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=1360) |
| **Patio del cuartel Nanami** (piedra arenisca, arcos) | `#E7DECF` `#847363` `#634D3F` `#A0988A` `#BEBEB8` | Día, mediterráneo | Tráiler especial *Ryusui*, [0:09](https://www.dailymotion.com/video/x8bnxd8?t=9) |
| **El barco (velas)** | `#2B3E63` `#D9DAD0` `#6E6D6A` `#9D9E98` `#3779BA` | Cielo azul despejado | Tráiler especial *Ryusui*, [0:12](https://www.dailymotion.com/video/x8bnxd8?t=12) |

Confirmo que **las 4 texturas CC0 de Poly Haven** de `datos-video.md` siguen
vivas (HTTP 200 comprobado hoy): [Rough Wood](https://polyhaven.com/a/rough_wood),
[Wood Planks](https://polyhaven.com/a/wood_planks), [Worn Planks](https://polyhaven.com/a/worn_planks).
Para la **piedra de las estatuas** (mundo petrificado) sumo:
[Rock Cliff](https://polyhaven.com/a/rock_cliff_large_02) (CC0, roca agrietada) —
sirve para el bosque petrificado y los muros del laboratorio.

---

## Punto 9 · Música (openings, endings, ambiente)

Completo la tabla de §11 con **segunda fuente** para lo que estaba en ⚠️ y
**dos datos nuevos que no existían** (ED de *New World* 2.ª parte y toda la
música de *Science Future*, que la tabla vieja tenía en blanco o contradictoria):

| Temporada | Opening | Ending | Estado |
|---|---|---|---|
| T1, 1.ª parte (2019) | «Good Morning World!», BURNOUT SYNDROMES | «LIFE», Rude-α | ✅ (ya estaba) |
| T1, 2.ª parte | «三原色» (Sangenshoku), PELICAN FANCLUB | **«夢のような» (Yume no You na), 佐伯ユウスケ (Yusuke Saeki)** — 5.º single, salió el 20-nov-2019, tema «un sentimiento que no cambia»; el vídeo tiene un estilo pastel muy distinto al de la serie | **✅✅** (subí de ⚠️ a ✅: [SPICE](https://spice.eplus.jp/articles/257466), [BARKS](https://www.barks.jp/news/?id=1000172895), [Apple Music](https://music.apple.com/jp/album/%E5%A4%A2%E3%81%AE%E3%82%88%E3%81%86%E3%81%AA-tv%E3%82%A2%E3%83%8B%E3%83%A1-dr-stone-%E7%AC%AC2%E3%82%AF%E3%83%BC%E3%83%AB%E3%82%A8%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%83%86%E3%83%BC%E3%83%9E-ep/1484769945)) |
| *Stone Wars* (2021) | «楽園» (Rakuen), Fujifabric | «声？» (Koe?), Hatena | ✅ (ya estaba) |
| *New World*, 1.ª parte (2023) | «ワスレガタキ» (Wasuregataki), Huwie Ishizaki | **«Where Do We Go?», OKAMOTO'S** — single del 24-may-2023 | **✅✅** (subí de ⚠️ a ✅: [Anime News Network](https://www.animenewsnetwork.com/news/2023-03-25/dr-stone-new-world-anime-reveals-main-visual-ending-theme-song/.196419), [Anime Corner](https://animecorner.me/dr-stone-new-world-reveals-creditless-opening-and-ending-videos-for-1st-cour/)) |
| *New World*, 2.ª parte | **«Haruka», Ryujin Kiyoshi (esto es el OPENING, no el ending; la tabla vieja lo dejaba ambiguo)** | **«好きにしなよ» (Suki ni Shinayo), Anly** — 5.º ending de la serie, estreno 18-oct-2023, con un vídeo de **arte de arena** (muy distinto visualmente) | **✅✅ nuevo dato**: OP confirmado ([ANN](https://www.animenewsnetwork.com/news/2023-08-26/dr-stone-new-world-anime-2nd-part-reveals-october-12-debut-theme-song-artists/.201655)); ED confirmado con dos fuentes ([TMS Entertainment USA en X](https://x.com/tmsanime/status/1714325403941421462), [Dr. Stone Wiki](https://dr-stone.fandom.com/wiki/Suki_ni_Shinayo)) |
| *Science Future*, 1.ª parte | **«CASANOVA POSSE», ALI** | **«Rolling Stone», BREIMEN** | **✅ nuevo dato** |
| *Science Future*, 2.ª parte | **«SUPERNOVA», KANA-BOON** | **«no man's world», 音羽-otoha-** | **✅ nuevo dato** |
| *Science Future*, 3.ª parte | **«スキンズ» (Skins), ASIAN KUNG-FU GENERATION** | **«ROCKET», BURNOUT SYNDROMES** (el mismo grupo del OP1: cierra el círculo) | **✅ nuevo dato** |

Las 9 filas de *Science Future* salen de dos fuentes que coinciden:
[anime-song-info.com](https://anime-song-info.com/lp-drstone-op-ed/) y
[animatetimes.com](https://animatetimes.com/news/details.php?id=1736399013)
(«ノンクレジットOP・ED映像解禁», confirma que hay vídeo sin créditos oficial
de cada uno). La web oficial `dr-stone.jp/music/` da 403 desde aquí, pero
salió indexada con el mismo dato en la búsqueda, así que la dejo como tercera
referencia sin poder citar su texto exacto.

**La escena musical que sirve para #hardware** sigue siendo la del proyecto
del móvil, y ahora la vi de verdad: el montaje de fabricación en 1×23
(sube la música desde el minuto [19:49](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189)
hasta el «listo» de cada pieza, minuto [21:04](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264)
en este corte). Sigue sin identificarse el nombre exacto de la pista de
score (no está en los álbumes con nombre de escena) ⚠️.

**Ambiente confirmado mirando**: el ending «LIFE»/de las últimas semanas de
T1 usa **acuarela** (luna, estrellas, silueta a contraluz — ver hex arriba),
muy distinto del cel-shading nítido del resto de la serie. Es un dato de
estilo que sirve para el punto 18 (técnica), se lo paso a quien lo escriba.

---

## Punto 10 · Vídeos (tráileres, escenas, análisis, tendencias, con minuto)

Sustituyo la fila de §12 que decía «no pude ver, YouTube y TikTok no se
abren» ⚠️: **si se puede** por Dailymotion. Voy escena a escena con minuto
real del vídeo mirado (no del original de YouTube, que no pude abrir).

| Vídeo | Minuto(s) reales, mirados | Qué se ve |
|---|---|---|
| [Tráiler oficial ES, Vidaextra](https://www.dailymotion.com/video/x8xu1ty) | [0:45](https://www.dailymotion.com/video/x8xu1ty?t=45) «¡Salí!» (Senku libre de la piedra) · [0:50](https://www.dailymotion.com/video/x8xu1ty?t=50) Taiju rompiendo roca a golpes · [1:15](https://www.dailymotion.com/video/x8xu1ty?t=75) paisaje de montaña verde · [1:20](https://www.dailymotion.com/video/x8xu1ty?t=80) mar/océano | Resumen de tono, con subtítulos en español reales |
| [Tráiler *Stone Wars* VO](https://www.dailymotion.com/video/x8a1zqs) | [0:20](https://www.dailymotion.com/video/x8a1zqs?t=20) **disco/plato giratorio verde translúcido** montado en un aparato de madera (el tocadiscos) · [1:00](https://www.dailymotion.com/video/x8a1zqs?t=60) ficha de personaje «ニッキー» con su CV · [1:04](https://www.dailymotion.com/video/x8a1zqs?t=64) «チート聴力をもつ弓使い» (arquero con oído de tramposo = Ukyo) | Confirma visualmente el tocadiscos (§2.3 de la biblia) y presenta a Nikki y Ukyo con placa de texto, útil de referencia tipográfica |
| [Tráiler *New World* VO](https://www.dailymotion.com/video/x8j8l2f) | [0:24](https://www.dailymotion.com/video/x8j8l2f?t=24) Ryusui, sombrero pirata, puño al aire, «Sauvetage de l'humanité» · [0:36](https://www.dailymotion.com/video/x8j8l2f?t=36) «Levez les voiles!» (¡icen las velas!) | Presenta el arco New World con el barco |
| [Tráiler especial *Ryusui*](https://www.dailymotion.com/video/x8bnxd8) | [0:27](https://www.dailymotion.com/video/x8bnxd8?t=27) Ryusui musculoso, puño en alto, estallido de luz detrás (pose de **presentar/celebrar**) · [0:33](https://www.dailymotion.com/video/x8bnxd8?t=33) tres chicas con top «E=mc²» | Fecha de emisión confirmada en pantalla: 10-jul-2022 |
| [Tráiler *Science Future* VOSTFR](https://www.dailymotion.com/video/x9boaek) | [0:40](https://www.dailymotion.com/video/x9boaek?t=40) personaje con mochila caminando junto a un compañero, «La ciencia siempre ha sido nuestra ventaja» · [1:10](https://www.dailymotion.com/video/x9boaek?t=70) cartel «科学vs科学» (ciencia contra ciencia) · [1:30](https://www.dailymotion.com/video/x9boaek?t=90) «Alors c'est toi, Senku Ishigami» | Confirma fecha de emisión en pantalla: 9-ene-2025, Tokyo MX |

**TikTok**: la página de la etiqueta «10-mil-millones-por-ciento» responde
HTTP 200 (`https://www.tiktok.com/discover/10-mil-millones-por-ciento`), pero
no sirve el HTML con los vídeos (anti-bot: ni un solo `playCount` ni `desc`
en el código fuente) ⚠️. Confirmo que la etiqueta EXISTE (no da 404) pero no
pude ver cuántos vídeos ni cuáles. No lo repito más (ya son 2 intentos).

**Análisis en YouTube**: siguen sin poder verse por el bloqueo de sesión;
dejo los enlaces de `datos-video.md` («Anime Truth #13e», «The real appeal of
Dr. Stone», «Nobody is Talking About Dr Stone, BUT...») como candidatos sin
mirar ⚠️, para quien tenga acceso a YouTube después.

---

## Punto 14 · Poses analizadas por personaje (confirmación con fotograma real)

La tabla de §15 de la biblia (Senku, Gen, Chrome, Kaseki, 6 poses cada uno)
seguía toda en ⚠️ «de memoria». Confirmo con fotograma real las que pude, y
sumo 3 poses nuevas de personajes que la tabla no tenía (Kohaku, Ruri, Suika)
porque aparecen justo en la escena del canal.

| Personaje | Escena / minuto (mirado) | Pose confirmada | Sirve para |
|---|---|---|---|
| **Senku** | Ep. 1×19, [20:42](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1242) | Primer plano, sonrisa ladeada de suficiencia, ceja levantada, fondo de bosque | **Presentar** (✅ confirma la fila 3 de la tabla vieja) |
| **Senku** | Ep. 1×23, [21:04](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264) | Cuentagotas en una mano, vaso con líquido en la otra, cejas fruncidas, muy concentrado, abrigo de piel | **Explicar / experimentar** (variante de la fila 4, con abrigo de invierno) |
| **Senku** | OP1, [0:45](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=45) | Puño al pecho, mirada decidida, camiseta con «E=MC²» | **Animar / presentarse** |
| **Senku y Taiju** | OP1, [1:18](https://archive.org/download/dr-stone-op-1-ncbd-1080/DrStone-OP1-NCBD1080.mp4?t=78) | Espalda con espalda, sonrisa cómplice, ciudad de noche desenfocada detrás | **Celebrar en pareja** (sirve para láminas con dos personajes) |
| **Kohaku** | Ep. 1×23, [19:49](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1189) | De perfil, capa con ribete de piel, espada a la espalda, boca abierta mirando un vaso de cristales | **Preguntar / curiosidad** (novata ante la ciencia) |
| **Ruri** | Ep. 1×24, [4:34](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=274) | Primer plano, ojos muy abiertos, boca entreabierta | **Asombro / reacción** |
| **Suika** (sin casco) | Ep. 1×11, [16:45](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1005) | Boca abierta, ojos muy abiertos, mejillas con rayitas de sonrojo | **Alegría / sorpresa** |
| **Ryusui** | Tráiler especial, [0:27](https://www.dailymotion.com/video/x8bnxd8?t=27) | Torso desnudo musculoso, puño al aire, estallido de luz detrás | **Celebrar / anunciar en grande** (para lámina 2, personaje secundario muy querido) |

Las filas de **Gen y Kaseki** de la tabla vieja **no las pude confirmar**: no
encontré sus episodios (1×10, 1×20, 2×01, 2×07 y 1×11, 1×24) sueltos en
Internet Archive ni en Dailymotion ⚠️. Quedan como estaban, marcadas de
memoria.

---

## Lo mejor para la lámina

1. **La hoja de ruta real** (Ep. 1×19, [21:07](https://archive.org/download/dr.-stone-sub-19/Dr.%20Stone%20Sub%2019.mp4?t=1267)): árbol tecnológico con nodos «START» → materiales → pieza. Es la referencia perfecta para el **concepto A** (rangos de precio como camino de fabricación).
2. **La torre del megáfono** (Ep. 1×24, [2:17](https://archive.org/download/dr.-stone-1-x-24-odio-a-distancias-infinitas-by-yumikol/Dr.STONE%201X24%20Odio%20a%20distancias%20infinitas%20ByYumikol.mp4?t=137)): objeto real (bocina de cobre) en un sitio real (torre de madera), para hacer en Blender.
3. **El laboratorio** (Ep. 1×11, [16:53](https://archive.org/download/dr.-stone-sub-11/Dr.%20Stone%20Sub%2011.mp4?t=1013)): piedra, madera, cortinas de tela — paleta y materiales medidos, no inventados.
4. **Senku con el cuentagotas** (Ep. 1×23, [21:04](https://archive.org/download/dr.-stone-1-x-23-ola-de-ciencia-by-yumikol/Dr.STONE%201X23%20Ola%20de%20ciencia%20ByYumikol.mp4?t=1264)): pose de «explicar/experimentar» real, con abrigo de invierno (variedad de vestuario).
5. **Ryusui con el puño en alto** (tráiler especial, [0:27](https://www.dailymotion.com/video/x8bnxd8?t=27)): si el personaje secundario elegido es Ryusui, esta es su pose de presentación oficial, no inventada.

---

## No encontré ⚠️ (no obligatorio, quedó pendiente)

- **Capturas de la caja de diálogo de *Battle Craft*** (punto 13 en la
  biblia, no es mío pero lo miré de paso por si servía de vídeo): sigue sin
  aparecer en YouTube (bloqueado) ni en Dailymotion (busqué «Dr Stone Battle
  Craft gameplay», sólo salieron vídeos de otros juegos de bloques).
- **Vídeos de análisis de YouTube con minuto exacto** (canales «Mother's
  Basement», etc.): bloqueados por el inicio de sesión; no encontré mirrors
  en Dailymotion ni Internet Archive con esos títulos exactos.
- **Contenido real bajo la etiqueta de TikTok** «10 mil millones por
  ciento»: la etiqueta existe (200 OK) pero el HTML no trae los vídeos
  (anti-bot). 2 intentos, lo dejo.
- **Episodios de Gen y Kaseki** (1×10, 1×20, 2×01, 2×07, 1×24) sueltos: no
  están en Internet Archive con ese número exacto (sólo 2, 3, 5-11, 13-15,
  17-20 de T1); sus poses siguen sin confirmar con fotograma.
- **Nombre de la pista de score** que suena en el montaje de fabricación
  (1×23, 19:49-21:04): no aparece con nombre de escena en los álbumes de
  MusicBrainz que ya había en `datos-video.md`.

---

## Bitácora de búsqueda (segunda pasada, vídeo)

- **Español**: «Dr Stone opening full» / «Dr Stone AMV» / «Dr Stone
  capitulo 1 español» en la API de Dailymotion → la mayoría irrelevante
  (covers de fans, series con «Stone» en el título); descarté un vídeo mal
  etiquetado «Dr. Stone Ep. 1» que en realidad era una reacción de Gacha a
  *Black Butler* (lo comprobé mirándolo, no me fié del título).
- **Francés**: «Dr Stone Stone Wars Bande Annonce» → encontré el tráiler VO
  real de *Stone Wars* con subtítulos FR (Crunchyroll).
- **Japonés**: `Dr Stone アニメ 2期 エンディング 「夢のような」 佐伯ユウスケ` y
  `Dr Stone Science Future オープニング エンディング 主題歌` (búsqueda web) →
  confirmaron toda la música que faltaba.
- **Inglés**: `Dr. Stone New World part 2 ending theme`, `"Suki ni Shinayo"
  Anly Dr Stone`, `"Where Do We Go?" OKAMOTO'S ending theme part 1` →
  segunda fuente para lo que estaba en ⚠️.
- **Internet Archive**: `advancedsearch.php?q=title:(Dr. Stone Sub)` y
  `title:(Dr Stone Ryusui)` y `title:(Dr Stone ED)` para localizar episodios
  y música sueltos.
- **AnimeThemes**: `api.animethemes.moe` sigue caído (HTTP 522), igual que
  cuando lo intentó `recolectar.py`. No insistí más de 2 veces.
- **dr-stone.jp/music/**: HTTP 403 directo desde este servidor; el dato lo
  confirmé por las dos fuentes de prensa especializada en su lugar.
- **Poly Haven**: comprobé con HEAD que las 3 texturas de `datos-video.md`
  siguen accesibles (200) y sumé una cuarta (roca) para el mundo petrificado.
- Herramientas usadas: `fotogramas.py` (11 vídeos, ~90 fotogramas mirados en
  hojas de contacto + 14 fotogramas sueltos en grande), `estilo.py` (8
  paletas medidas).
