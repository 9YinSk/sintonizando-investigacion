# One Piece · parte «musica-videos» (puntos 4, 9 y 10)

Investigador de música y vídeos, repaso del 24-sep-2026. Libreta de datos: un dato por línea.
`dato · fuente · ✅ (dos fuentes) / ⚠️ (una) · minuto o tamaño`.
Parto de lo que ya dice `biblia.md` (§6, §11, §12) y sólo añado o corrijo.
Carpeta de trabajo (fuera del repo): `/tmp/claude-0/trabajo/01-musica-videos`.

## Hallazgos

### Punto 4 · Fondos y sitios (luz, hora, paleta medida, texturas)

**Cómo lo medí.** Bajé las copias (Internet Archive y Dailymotion; YouTube pidió «iniciar sesión»), saqué **un fotograma por plano** con `fotogramas.py --cortes`, miré las hojas y medí cada sitio con `herramientas/estilo.py` (8 colores por cuantización; % = parte de la imagen). Los fotogramas y hojas están en `/tmp/claude-0/trabajo/01-musica-videos/vid/`. La biblia (§6) tenía paletas de arte del juego y de la wiki; **esto es lo del anime en movimiento**.

**Los sitios de #bienvenidas (luz de día, a bordo):**
- **Cubierta del Sunny, la tripulación entera en contrapicado** (Nami con la mano en la cadera, Zoro con la espada al hombro, la vela blanca con la calavera detrás): cielo `#35AAF1` 15 %, sombra de la vela `#A9BCCD` 19 %, blanco de nube `#E7E8ED`, madera del mástil `#B16744` / `#55363D`. Brillo 65 %, saturación 37 %, degradado suave · [opening del ep. 1000, 1:25](https://archive.org/details/one-piece-episode-1000-opening-we-are-straw-hats-edition) (720p, fotograma 20 de la hoja) · ⚠️ (una copia) · **el encuadre y la luz del concepto A**
- **El Sunny navegando a mediodía**: cielo `#2B9FF4` 40 %, nube `#DEEFF8` 17 %, mar turquesa `#31C2E7` 13 % y `#60D1F0`. **Brillo 88 %, saturación 57 %**: la luz más alta de la serie · [ep. 1000, 0:38 y 1:45](https://archive.org/details/one-piece-episode-1000-opening-we-are-straw-hats-edition) · ✅ (los dos planos dan lo mismo: `#21B2EA` / `#2388EA` / `#26D7ED` en 1:45)
- **Luffy en la baranda, girando la moneda**: mar `#1E97E2` y `#19B1D7`, sombra del chaleco `#252936`, rojo `#9E293B`, piel `#DDBF8F` · [ep. 1000, 1:37](https://archive.org/details/one-piece-episode-1000-opening-we-are-straw-hats-edition) · ⚠️
- **La carta náutica del opening del ep. 1000, ahora con el Sunny dibujado** (el del ep. 1 llevaba el Merry): mar `#C8E3D3` / `#B0D0C1`, tierra `#D9CE8E` / `#B1A66A`, sombra de costa `#787959`, tinta `#4B4238`; rótulos a pluma «ELHURLZ PACIFICAT…» (letras inventadas), rosa de los vientos roja, cinta amarilla y banderín azul y rojo. Saturación 24 %, **mucha línea** · [ep. 1000, 1:06](https://archive.org/details/one-piece-episode-1000-opening-we-are-straw-hats-edition) · ✅ (coincide con la del OP 1 que ya medía la biblia: `#B2D8C8` / `#D3D293`) · **fondo para el concepto B**
- **Cubierta de madera del Red Force** (plano bajo, tablones que se van al fondo): `#8F5D44` 23 %, `#81553C`, `#563725`, veta `#311915`; saturación 55 %, brillo 42 % · [clip del ep. 1082, Meristation en Dailymotion, 1:05](https://www.dailymotion.com/video/x8pee1a?start=65) (sale de Crunchyroll; acaba con su cartela naranja) · ⚠️ · **la madera de barco más cálida que vi: sirve para el suelo del concepto A**

**Otros sitios medidos (para láminas de otros canales o eventos):**
- **Loguetown, la plaza del patíbulo, de día**: blancos azulados `#D2DDEC` / `#BBCCE0`, sombra `#769BBF`, cielo `#195087`; saturación 32 % · [OP 28 «Carmine», 1:09](https://www.dailymotion.com/video/x9otrgy?start=69) · ⚠️
- **Loguetown bajo tormenta** (Dragon en la plaza): verde azulado frío `#557B87` / `#385F6B` / `#26434E`, cielo `#A8B8C2`; **brillo 37 %** · [OP 28, 1:07](https://www.dailymotion.com/video/x9otrgy?start=67) · ⚠️ · cuadra con la tormenta del ep. 53 que ya citaba la biblia
- **Egghead** (isla del futuro): ciudad de caramelo, cian `#A8C8D1` / `#7BA5B4`, gris `#D2D6D8`, beige `#C7B2A3`, sombra `#302F3D`; con la tripulación: rojo del traje de Luffy `#C85231`, azul `#38508C`, amarillo `#DBAC52` · [tráiler de Egghead, 0:09-0:10](https://www.dailymotion.com/video/x8r9xak?start=9) · ⚠️. En el OP 26 la isla se vuelve **diseño plano pop**: morado, amarillo y rayas de peligro · [OP 26, 0:17-0:28](https://www.dailymotion.com/video/x8r9tzd?start=17)
- **Elbaf a mediodía** (árbol gigante y castillo): cielo `#63A9F9` / `#85C3F8`, nube `#B0DAF1`, piedra `#D1BDA1`, tronco `#A67A66`; brillo 83 % · [tráiler de Elbaf, 0:03](https://www.dailymotion.com/video/xa0d0cs?start=3) · ⚠️
- **Elbaf, bosque nevado**: todo azul pizarra `#414C58` / `#657287` / `#576477` / `#A5B4CA`; brillo 50 %, saturación 25 % · [segundo tráiler, 0:15](https://www.dailymotion.com/video/xa3ktjs?start=15) · ⚠️
- **Gigantes a contraluz al atardecer** («THE GARGANTUAN SCALE…»): gris `#8C96A5`, rosa `#E0B1B0`, crema `#E5D9C3`, marrón `#B08A72` · [segundo tráiler, 0:08](https://www.dailymotion.com/video/xa3ktjs?start=8) · ⚠️
- **Egghead en llamas** (barcos de la Marina): `#212226` / `#363133`, fuego `#D76D29` y brasa `#833E25`; brillo 26 % · [OP 28, 0:16](https://www.dailymotion.com/video/x9otrgy?start=16) · ⚠️
- **El haki del rey** (Shanks frena a Ryokugyū en Wano, ep. 1082 «新時代到来！赤髪の皇帝の怒り»): rayos rojos sobre negro granate, `#CF2033` / `#A71221` / `#791316`, fondo `#21090C`, halo `#D87A6B`; **saturación 77 %**, la más alta que medí · [clip, 0:39](https://www.dailymotion.com/video/x8pee1a?start=39) · ✅ (episodio confirmado con la [wiki, ep. 1082](https://onepiece.fandom.com/wiki/Episode_1082)) · no es un sitio: es **la luz de amenaza**

**Qué dicen los números (la luz de la serie):**
- **Día a bordo = brillo 85-89 %, saturación 55-60 %**, cielo entre `#2B9FF4` y `#35AAF1`, mar turquesa `#21B2EA`-`#31C2E7`. El `#057FEE` del arte del juego (§6 de la biblia) es **más oscuro y más saturado** que el anime: para la lámina, mejor `#2B9FF4`.
- **Interiores y noche** bajan a brillo 25-40 %. **La carta y el papel** van a saturación 20-25 %.
- estilo.py lee **«degradado / pintado»** en casi todos los fotogramas del anime moderno (ep. 1000 en adelante): el cel plano se suaviza con la compresión y con los degradados del cielo; en la carta náutica sale **«mucha línea»** (tinta).

**Texturas reales (el decorado de Netflix, medido, y bancos libres):**
- **Madera cruda del Baratie en obra**: `#A17F5D`, `#7E5C46`, `#58453B`, veta `#271914` · [«Making-of des décors (Merry, Baratie…)», jeuxvideo.com en Dailymotion, 1:02](https://www.dailymotion.com/video/x8bfvq4?start=62) (vídeo de Netflix) · ⚠️
- **Interior del Baratie**: paredes amarillas `#817336` / `#877F5B`, sirena tallada, ventana octogonal · [1:22](https://www.dailymotion.com/video/x8bfvq4?start=82). **Aparejo de cuerda contra el cielo**: cielo `#87A3D2`, cuerda `#B1AB7C` / `#D3D5BA`, marco dorado · [1:32](https://www.dailymotion.com/video/x8bfvq4?start=92). **Molinos de Foosha a contraluz** · [1:37](https://www.dailymotion.com/video/x8bfvq4?start=97). **Cartel «Partys Bar»** tallado · [1:11](https://www.dailymotion.com/video/x8bfvq4?start=71) · ⚠️
- **Cuerda y red (CC0, ambientCG)**: [Rope001](https://ambientcg.com/view?id=Rope001), [Rope002](https://ambientcg.com/view?id=Rope002), [Net003A](https://ambientcg.com/view?id=Net003A) (red de 220 cm) · API de ambientCG · ✅ (CC0 en toda la web)
- **Metal oxidado para clavos y argollas del cartel (CC0, Poly Haven)**: [rusty_metal_02](https://polyhaven.com/a/rusty_metal_02) (Rob Tuytel, 8K), [rusty_metal_sheet](https://polyhaven.com/a/rusty_metal_sheet) (Amal Kumar, 16K) · API de Poly Haven · ✅
- **Tela de vela** (CC0): [fabric_pattern_05](https://polyhaven.com/a/fabric_pattern_05) (Rob Tuytel, algodón) · ✅
- **Cielo para iluminar en Blender (HDRI, CC0)**: [secluded_beach](https://polyhaven.com/a/secluded_beach) (Greg Zaal y Rico Cilliers; mañana-tarde, nubes sueltas, alto contraste) y [simons_town_harbour](https://polyhaven.com/a/simons_town_harbour) (puerto) · API de Poly Haven · ✅

### Punto 9 · Música

**Lista completa, al día (sep-2026).** La biblia sólo tenía 8 temas. Son **29 openings y 23 endings**.
- 29 openings y 23 endings; OP 29 «Luminous» (AiNA THE END) desde el ep. 1156 y ED 23 «Sono Mirai / その未来» (時速36km) desde el 1157 · [wiki, «One Piece Music»](https://onepiece.fandom.com/wiki/One_Piece_Music) + [one-piece.com, 28-mar-2026](https://one-piece.com/news/78689/index.html) · ✅
- Openings 23-29, con sus episodios: 23 «DREAMIN' ON» (Da-iCE, 935-999 y 1001-1004) · 24 «PAINT» (I Don't Like Mondays., 1005-1073) · 25 «Saikō Tōtatsuten / 最高到達点» (SEKAI NO OWARI, 1074-1088) · 26 «UUUUUS! / あーーっす！» (Hiroshi Kitadani, música de Kōhei Tanaka, 1089-1122) · 27 «Tenshi to Akuma / ANGEL & DEVIL» (GRe4N BOYZ, 1123-1138) · 28 «Carmine / カーマイン» (ELLEGARDEN, 1139-1155) · 29 «Luminous» (1156-) · [wiki](https://onepiece.fandom.com/wiki/One_Piece_Music) + vídeos del [canal oficial ONE PIECE公式](https://www.youtube.com/channel/UCdAHaWcKdpbT5XkN2Er6BUQ) · ✅
- Endings 19-23: 19 «Raise» (Chilli Beans., 1071-1088) · 20 «Dear sunrise» (Maki Otsuki, 1089-1122) · 21 «The 1» (muque, 1123-1136 y 1138) · 22 «PUNKS» (カメレオン・ライム・ウーピーパイ, 1139-1155) · 23 «Sono Mirai» (1157-1162 y 1164-) · wiki + canal oficial · ✅
- **Del ep. 279 al 1070 no hubo endings**: Toei los quitó para alargar los openings; volvieron en el 1071 (el 590 usó «We Go!» de ending) · [wiki](https://onepiece.fandom.com/wiki/One_Piece_Music) · ⚠️ (una fuente; cuadra con la lista: ED 18 acaba en el 278 y ED 19 empieza en el 1071)
- «We Are!» volvió **como opening del ep. 1000** («Straw Hats Edition», toda la tripulación en el Sunny) · [wiki, «We Are!»](https://onepiece.fandom.com/wiki/We_Are!) + [copia en Internet Archive](https://archive.org/details/one-piece-episode-1000-opening-we-are-straw-hats-edition), mirada (§ punto 10) · ✅
- La **música del avance del próximo episodio** (los últimos 30 s): remix de «We Are!» (eps. 1-516), de «We Go!» (517-891), de «OVER THE TOP» (892-1089) y de «UUUUUS!» (1090 en adelante; el 1122 usó «New World» cantada por Brook) · [wiki](https://onepiece.fandom.com/wiki/One_Piece_Music) · ⚠️ (una fuente)
- **Elbaf (2026)**: estreno el **5-abr-2026**, domingos **23:15** en Fuji TV. «Luminous» se estrenó en directo en el parque Nippon Maru de Yokohama el 28-mar-2026, en el AnimeJapan · [one-piece.com](https://one-piece.com/news/78689/index.html) + tráiler de Elbaf, [0:06](https://www.dailymotion.com/video/xa3ktjs?start=6) («OPENING THEME "Luminous" by AiNA THE END») · ✅
- El cambio de horario se ve en la mosca del opening: en el OP 26 dice «毎週日曜 あさ9時30分より» (domingos 9:30); en el OP 28, «毎週日曜 よる11時15分より» (domingos 23:15) · visto en las copias ([OP 26, 0:10](https://www.dailymotion.com/video/x8r9tzd?start=10), [OP 28, 0:24](https://www.dailymotion.com/video/x9otrgy?start=24)) + one-piece.com · ✅
- «Carmine» se estrenó en el aire el **10-ago-2025** · [aviso del canal oficial, «8月10日オンエアより…»](https://www.youtube.com/watch?v=eCTUaaJVODc) · ⚠️ (una fuente)
- Tōhōshinki (TVXQ) sacó «Share The World -RED OCEAN Ver.-» el 15-abr-2026, con portada del Merry y el Sunny · [one-piece.com](https://one-piece.com/news/79045/index.html) · ⚠️

**Visitas de los vídeos oficiales** (búsqueda de yt-dlp, 24-sep-2026; YouTube no dejó bajar el vídeo):
- «UUUUUS!», opening completo: **29.017.632** visitas · [YFbno_aPm0w](https://www.youtube.com/watch?v=YFbno_aPm0w) · dato de YouTube
- «ルミナス - Luminous», aviso de 31 s: **17.998.303**; opening completo: 3.360.228 · [6hRjsvdINgg](https://www.youtube.com/watch?v=6hRjsvdINgg), [X48ZNGHBa8A](https://www.youtube.com/watch?v=X48ZNGHBa8A)
- «CARMINE»: 11.117.963 · [JqUWua4MrIM](https://www.youtube.com/watch?v=JqUWua4MrIM). «ANGEL & DEVIL»: 8.626.195 · [VHxeuLf_eRs](https://www.youtube.com/watch?v=VHxeuLf_eRs)
- Endings: «Raise» 6.561.644 · «The 1» 3.223.702 · «Future / その未来» 885.030 · «PUNKS» 728.202 · [stXbvYGvrxA](https://www.youtube.com/watch?v=stXbvYGvrxA), [DhUWbErUqlg](https://www.youtube.com/watch?v=DhUWbErUqlg), [Qx-XXzEUm-8](https://www.youtube.com/watch?v=Qx-XXzEUm-8), [MHL-JzbTkrY](https://www.youtube.com/watch?v=MHL-JzbTkrY)
- **Hiroshi Kitadani canta «We Are!» en THE FIRST TAKE: 23.782.808 visitas** · [HB4iNVa746E](https://www.youtube.com/watch?v=HB4iNVa746E) · la versión «de estudio» que más se comparte

**Tempo medido** (BPM; con numpy sobre el audio de las copias, tres tramos de 30 s que coinciden; sirve para cortar al ritmo en #edición):
- «We Are!» (versión del ep. 1000): **168 BPM** (84 a medio tiempo) · [copia de Archive](https://archive.org/details/one-piece-episode-1000-opening-we-are-straw-hats-edition) · ⚠️ (medida propia)
- «UUUUUS!»: **182 BPM** · «Carmine»: **144 BPM** · «OVER THE TOP»: **106 BPM** (o su doble) · copias de Dailymotion · ⚠️ (medida propia)

**Cómo suenan y qué ambiente dan (para elegir la de #bienvenidas):**
- «We Are!» y «UUUUUS!»: las dos de Kitadani con música de Kōhei Tanaka; «UUUUUS!» abre con **el Sunny visto desde arriba navegando**, como un eco del primero · [wiki, «UUUUUS!»](https://onepiece.fandom.com/wiki/UUUUUS!) · ⚠️. Visualmente el OP 26 es **plano y pop**: morado, amarillo y rayas de peligro negras y amarillas, letras hinchadas «ONE PIECE» (visto, [0:10-0:21](https://www.dailymotion.com/video/x8r9tzd?start=10)).
- «Carmine»: rock (ELLEGARDEN). Empieza con **la emisión de Vegapunk en una tele que parpadea** ([0:00-0:01](https://www.dailymotion.com/video/x9otrgy)) y es todo **fuego naranja y noche** (visto) · wiki + copia · ✅
- «Luminous»: empieza con **Luffy con la ropa de Elbaf mirando el cielo, admirado** · [wiki, «Luminous»](https://onepiece.fandom.com/wiki/Luminous) · ⚠️ (no pude bajar el vídeo)
- **Música de fondo con ambiente** (One Piece Wiki, [«One Piece Soundtracks»](https://onepiece.fandom.com/wiki/One_Piece_Soundtracks)):
  - **«Minato Mura» (港村, «pueblo del puerto»)**: ragtime alegre de fiestas y finales de arco; suena cuando Shanks y Mihawk celebran la primera recompensa de Luffy · ⚠️ (una fuente; hay versiones de piano con 82.650 visitas, [a8ZsEJwWyWg](https://www.youtube.com/watch?v=a8ZsEJwWyWg)). **Es la música de «bienvenido a bordo».**
  - «Overtaken»: la entrada épica (el paseo hacia Arlong Park, ep. 37) · ✅ (wiki + la copia más vista: **30.552.914** visitas, [daFi4MScfl8](https://www.youtube.com/watch?v=daFi4MScfl8), también en [Archive](https://archive.org/details/youtube-daFi4MScfl8)). La versión épica de Samuel Kim («Drums of Liberation») tiene 24.520.001 · [bfW6dzCFy2A](https://www.youtube.com/watch?v=bfW6dzCFy2A).
  - «Mother Sea»: la tristeza (funeral del Merry, ep. 312) · «The Very, Very, Very Strongest»: la carga (Enies Lobby) · «Fierce battle! Zoro vs. Sanji»: las peleas en broma · ⚠️ (una fuente)
- **«Binks' Sake / ビンクスの酒»**: la canción pirata de Brook, letra de Oda; se oye a trozos desde el ep. 337 y **entera en el ep. 380** (cap. 488); su última frase dice 笑い話 («laugh tale») · [wiki inglesa](https://onepiece.fandom.com/wiki/Binks%27_Sake) + [wiki española, «Sake de Binks»](https://onepiece.fandom.com/es/wiki/Sake_de_Binks) · ✅

**En español latino (lo que más sirve a un servidor de doblaje y canto):**
- En la versión de 4Kids (TV abierta) **«We Are» se cantó en español**: intérprete **Manuel**, coros **Hugo González**, adaptación **Jorge Roig**; «Memories» también se dobló (intérprete sin identificar). El rap de 4Kids lo cantó Hugo González (dirección musical de María Eugenia Toussaint) · [Doblaje Wiki, «One Piece (4Kids)»](https://doblaje.fandom.com/es/wiki/One_Piece_(4Kids)) · ⚠️ (una fuente; el vídeo «[One Piece ending 1 memories latino completo](https://www.youtube.com/watch?v=Bosh8Sgq5AU)» existe, 308.921 visitas)
- El doblaje nuevo **deja los temas en japonés** ✅ (ya estaba). Curioso: **Red Uno (Bolivia)** puso el opening del ep. 1000 con el «We Are» en español de 4Kids · [Doblaje Wiki, «One Piece»](https://doblaje.fandom.com/es/wiki/One_Piece) · ⚠️
- **«El sake de Binks» en latino** lo canta Brook (Óscar Flores): [«Canción completa, Audio Latino, Cap 380»](https://www.youtube.com/watch?v=l4nQYLTvujE) (145.387 visitas) y [la de Sebas García con letra](https://www.youtube.com/watch?v=IlHCsYnNm8A) (**3.833.980**) · ⚠️ (vídeos de fans; en Doblaje Wiki no hay ficha de la canción)
- **Film Red: todas las canciones de Uta se doblaron**, con **Aitza Terán** de voz cantada (Azul Valadez en los diálogos). Títulos: «Nueva génesis», «Invencible», «Contraluz», «Poema fugaz», «Tot Musica», «El mundo continuará», «Donde nace el viento». Dirección musical Rubén Bedolla, adaptación Yang Coutiño · [Doblaje Wiki, «One Piece Film: Red»](https://doblaje.fandom.com/es/wiki/One_Piece_Film:_Red) + [entrevista de X-Tops con Aitza Terán y Yang Coutiño](https://www.youtube.com/watch?v=6mJIpPgO1SU) (1:44:41) · ✅
  - Lo más difícil de adaptar y de cantar fue «Poema fugaz» (según Coutiño y Terán) · Doblaje Wiki · ⚠️
  - Subidas de fans con el audio latino: «New genesis» 476.828 · «Tot musica» 679.458 · «Backlight» 392.034 visitas (canal UTENA Doblaje latino, [hiQkIfhGpms](https://www.youtube.com/watch?v=hiQkIfhGpms), [0ytG1bg1PmQ](https://www.youtube.com/watch?v=0ytG1bg1PmQ))
- **Serie de Netflix**: música de **Sonya Belousova y Giona Ostinelli**; T1 (31-ago-2023) con «My Sails Are Set» feat. AURORA; **T2 «Into the Grand Line» (10-mar-2026)** con «Pray to the Sun» feat. Declan de Barra y The HU y «Whisky Peak Saloon» feat. Leo P · [wiki, «Live-Action Series»](https://onepiece.fandom.com/wiki/One_Piece_(Live-Action_Series)) + canal [Netflix Music](https://www.youtube.com/watch?v=qis5zUBA_sk) («My Sails Are Set», 5.256.902 visitas; [«Pray to the Sun»](https://www.youtube.com/watch?v=Nap2fVKjlpI), 837.702) · ✅
  - En la T2, «Binks's Brew» suena en los recuerdos de Crocus (los Rumbar y Brook) y **Luffy se la canta a Laboon** para calmarlo · wiki + clips de Netflix: [«Brooke Sings Binks Brew To Laboon»](https://www.youtube.com/watch?v=NMQrAvlL3Ks) (1.423.709 visitas) y [«Bink's Brew», Netflix Music](https://www.youtube.com/watch?v=FcRTa65O61c) (774.000) · ✅

### Punto 10 · Vídeos

(pendiente)

## Lo mejor para la lámina

(pendiente)

## No encontré

(pendiente)

## Bitácora

- 17:16 UTC · YouTube (yt-dlp, opening oficial `YoeP9w5UIlg`): 429 y «Sign in to confirm you're not a bot».
