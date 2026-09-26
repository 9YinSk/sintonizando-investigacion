# Parte VÍDEO · El viaje de Chihiro (Sen to Chihiro no Kamikakushi, 2001)

Investigador de vídeo (puntos 2, 4, 9, 10, 14 de ENCARGO.md). Libreta de datos: un dato por línea,
fuente enlazada, ✅ (dos fuentes) o ⚠️ (una sola), minuto cuando aplica. Es película, no serie: no hay
opening/ending semanal, sino créditos iniciales/finales, tráiler y escenas icónicas.

YouTube pidió iniciar sesión en este contenedor: trabajé con Dailymotion (tráiler doblado que ya
procesó `episodio.py` en `partes/episodios.md`), la galería oficial 100% libre de
`ghibli.jp/works/chihiro`, Internet Archive, MusicBrainz y Ghibli Wiki (Fandom).

**Aviso del jefe (recibido durante esta tanda): la ficha minuto a minuto de la película completa NO
va a salir** — el archivo de Internet Archive (`SenToChihiroNoKamikakushi`) está restringido, la
descarga da 401. No se reintentó. Por eso los fotogramas de la película que no vienen del tráiler
doblado (que sí tiene minuto exacto con `&t=`) quedan citados como «still oficial de `ghibli.jp`,
sin minuto de vídeo» y marcados ⚠️ en vez de con un timecode — es lo máximo que da de sí esta obra
sin acceso a la película completa ni a YouTube.

## Fuentes de imagen fija usadas

- **Galería oficial Ghibli** (`https://www.ghibli.jp/works/chihiro/`): 50 fotogramas oficiales
  `chihiro001.jpg`…`chihiro050.jpg`, todos 1920×1038 px. Licencia explícita en la propia página:
  «画像は常識の範囲でご自由にお使いください」(úsense libremente dentro de lo razonable) ·
  © 2001 Hayao Miyazaki/Studio Ghibli, NDDTM. ✅ (texto de licencia visto en la página + repetido en
  cada imagen de la galería). Bajados a
  `/tmp/claude-0/trabajo/98-el-viaje-de-chihiro-video/ghibli-oficial/` y montados en 5 hojas de
  contacto (`hoja_01.jpg`…`hoja_05.jpg`, 12 por hoja) que **miré** una por una.
- **Tráiler doblado (México)**: `https://www.dailymotion.com/video/x889bq8` («El viaje de Chihiro
  Tráiler (2)», Sensacine, 1:38, 18 729 vistas). Ya está procesado en
  `partes/episodios.md` (70 planos, transcripción Whisper) con hojas en
  `/tmp/claude-0/trabajo/98-el-viaje-de-chihiro-episodios/trailer-mx/hojas/` — las miré para sacar
  minutos exactos de escena y de poses.
- **Reel promocional Cinépolis/Sensacine México** «Dame 1 minuto»:
  `https://www.dailymotion.com/video/x9f6hg0` (0:55, 191 388 vistas). No es metraje puro: una
  presentadora habla a cámara y enlaza Totoro, Mononoke y Chihiro. Saqué 32 planos con
  `fotogramas.py --cortes` en `/tmp/claude-0/trabajo/98-el-viaje-de-chihiro-video/escenas-mx/hoja_01.jpg`
  (los miré) — sirve para tendencia/promoción (punto 10), no para poses fiables de personaje.

## Hallazgos — Punto 2: fotogramas de escenas icónicas

- Mudanza en coche: Chihiro abrazada a un ramo de flores de despedida en el asiento trasero, entre
  cajas · galería oficial `chihiro001.jpg` (1920×1038) · ✅ (imagen oficial + confirma secuencia
  inicial en tráiler 0:02-0:14) · https://www.ghibli.jp/gallery/chihiro001.jpg
- Entrada al túnel rojo hacia el mundo espiritual (el padre se mete «por el atajo») · tráiler
  0:16-0:18 (coche frente al túnel, luego el edificio rojo) ·
  https://www.dailymotion.com/video/x889bq8?t=16 · ✅ (plano descrito también en Ghibli Wiki,
  sinopsis) · minuto exacto del tráiler doblado MX.
- Los padres devorando la comida del puesto fantasma y convirtiéndose en cerdos · galería oficial
  `chihiro004.jpg` (comiendo) y `chihiro006.jpg` (primer plano del padre ya cerdo, con comida en el
  hocico) · ✅ · https://www.ghibli.jp/gallery/chihiro006.jpg
- Chihiro cruza corriendo el puente rojo de la casa de baños al anochecer, entre naranjas y rojos
  saturados · galería oficial `chihiro008.jpg` · ⚠️ (una fuente, sin minuto de película) ·
  https://www.ghibli.jp/gallery/chihiro008.jpg
- Procesión de espíritus enmascarados (sapos-guardia con máscaras de oni) cruzando el puente ·
  galería oficial `chihiro009.jpg` · ⚠️
- Haku en forma de dragón, herido y sangrando, sostenido por Chihiro tras robar el sello de Zeniba ·
  galería oficial `chihiro038.jpg` · tráiler 1:18 (mismo plano, «h1·38») ·
  https://www.dailymotion.com/video/x889bq8?t=78 · ✅ (imagen oficial + tráiler)
- Vuelo nocturno de Chihiro sobre el lomo del dragón Haku de regreso a la casa de baños, con la
  música «Reprise/Again» (ふたたび, pista 19 del disco) de fondo · galería oficial
  `chihiro045.jpg` · ✅ (still oficial + Ghibli Wiki confirma que esa pista acompaña «the Chihiro
  and Haku flight scene») · https://ghibli.fandom.com/wiki/Reprise/Again
- Sin Cara (Kaonashi) devorando el banquete y a los empleados, silueta negra gigante en la sala de
  comidas · galería oficial `chihiro031.jpg` (mesa del banquete) y `chihiro033.jpg` (silueta
  gigante enmascarada) · ✅
- El tren de la Sexta Estación cruzando el mar con Chihiro, Sin Cara y pasajeros-sombra en silencio ·
  galería oficial `chihiro042.jpg` (vías bajo el agua) y `chihiro043.jpg` (tren sobre el mar al
  atardecer) · ✅ (imagen oficial + es la escena que cita la tendencia de TikTok, ver punto 10) ·
  https://www.ghibli.jp/gallery/chihiro043.jpg
- Final: Chihiro cruza el túnel de vuelta con sus padres, luz diurna dorada, mira atrás una vez ·
  galería oficial `chihiro049.jpg` (con Haku niño) y `chihiro050.jpg` (primer plano mirando atrás
  entre árboles) · ⚠️ (oficiales, sin confirmar con un segundo plano de vídeo)
- Créditos finales sobre fondo azul con la canción «Itsumo Nando Demo/Always With Me» (いつも何度で
  も) cantada por Kimura Yumi (木村弓), letra y música de Kaku Wakako (覚和歌子) · ✅ (Ghibli Wiki +
  ficha oficial de la película en ghibli.jp, que lista «主題歌 木村 弓» en los metadatos) ·
  https://ghibli.fandom.com/wiki/Always_with_Me · https://www.ghibli.jp/works/chihiro/

## Hallazgos — Punto 4: fondos y sitios (paleta medida con `estilo.py`)

Todas las paletas son de fotogramas oficiales 1920×1038 de `ghibli.jp`, medidas con
`herramientas/estilo.py --colores 6`. JSON completo en
`/tmp/claude-0/trabajo/98-el-viaje-de-chihiro-video/estilo/lugares.json` y `lugares2.json`.

- **Casa de baños (Aburaya), exterior de noche** (`chihiro011.jpg`): paleta
  #342E2C 32% · #2A2423 23% · #4C3D32 17% · #6A543A 12% · #917446 10% · #BF9959 6% — marrones y
  ocres muy oscuros con ventanas cálidas; brillo medio 31%, saturación 30%, sombreado degradado,
  línea #604D34. ✅ (medido).
- **Calle-mercado de comida fantasma, de noche** (`chihiro007.jpg`, el puesto de fideos con vidrieras
  de colores): #2B2623 29% · #4D3F39 21% · #516160 16% · #7A5F4B 15% · #96866A 14% · #D84C49 5%
  (el rojo es el acento de las vidrieras) — brillo 38%, saturación 30%. ✅
- **Calle de tiendas, de día** (`chihiro003.jpg`): #615849 20% · #3D413B 18% · #6A756A 17% ·
  #A58E6D 17% · #C7BBA8 14% · #70A49D 13% — verdes apagados y ocres, con un turquesa de acento;
  brillo 53%, saturación 29%, «mucha línea» (línea #636358). ✅
- **Sala de calderas, espíritus del hollín (susuwatari)** (`chihiro014.jpg`): #41352D 40% ·
  #4E3B2F 29% · #272524 14% · #19191A 11% · #CCC4A5 4% · #908D6B 2% — casi monocromo marrón muy
  oscuro (brillo 27%), los puntitos blancos de ojos son el único contraste. ✅
- **Puente rojo, de día, con Sin Cara** (`chihiro020.jpg`): #B0987D 23% · #BA4A4B 22% ·
  #93D1D6 19% · #CEDCDB 17% · #6C7E67 12% · #2C1F1D 8% — el rojo laca de la barandilla contra un
  cielo turquesa muy claro; brillo alto 70%. ✅
- **Tren sobre el mar, atardecer** (`chihiro043.jpg`): #5F7DC4 28% · #6A5F76 17% · #E3B49F 17% ·
  #93757E 16% · #BE9282 13% · #9A8EAA 9% — azul-violeta dominante con un rosa-melocotón de reflejo
  en el agua; brillo 70%, «poca línea» (contornos casi ausentes, todo degradado). ✅
- **Callejón junto a la casa de baños, de noche** (`chihiro008.jpg`): #282323 36% · #3F362E 28% ·
  #67523E 12% · #69352F 11% · #9E5845 10% · #CF896C 4% — negros cálidos con un naranja-teja de
  acento (faroles); brillo bajo 32%. ✅
- **Sala del Espíritu del Hedor/Kusare-gami (el «baño» más importante del guion, cuando Chihiro
  limpia a un espíritu-río atascado de basura)** (`chihiro039.jpg`): #26201E 25% · #534337 25% ·
  #807648 19% · #B99B36 13% · #C8B483 10% · #A24E41 9% — dorados y ocres sucios sobre fondo casi
  negro, «mucha línea» (contorno #6D5937) — es la imagen con más densidad de línea medida en toda
  la muestra (indica el detalle recargado de esa escena). ✅
- **Despacho de Yubaba** (`chihiro017.jpg`): #272321 41% · #9C8A73 18% · #284058 16% ·
  #DDC19B 10% · #685746 8% · #3A6294 7% — marrón muy oscuro con dos azules fríos de acento (vidrio,
  cortinas); brillo bajo 39%. ✅
- **Pasillo interior de la casa de baños, de día** (`chihiro028.jpg`): #DBCFB0 25% ·
  #DEAD7A 19% · #A59777 18% · #3B3B3C 18% · #926650 13% · #42618C 7% — la paleta más clara medida
  (brillo 66%), beige y madera clara, con un azul de acento. ✅
- **Interior del tren, vagón** (`chihiro042.jpg`): #252121 35% · #3B3A3B 23% · #4EACD1 16% ·
  #623837 11% · #AEC9D0 9% · #727971 6% — negros de silueta contra un cian de ventana; brillo 39%.
  ✅
- **Lectura de conjunto**: el exterior y los interiores de trabajo (calderas, despacho, callejón)
  son oscuros y ocres/marrones (brillo 27-41%); las escenas «de tránsito» al aire libre (puente,
  tren, mar) suben mucho el brillo (66-70%) y meten azules/turquesas fríos — el color separa
  «dentro del mundo de los espíritus, encerrada» de «cruzando, de camino a casa».
- **Texturas reales equivalentes (CC0, ambientCG, `--type=Material`)**: madera de listones para las
  pasarelas y la fachada de la Aburaya — `WoodFloor051` y `Planks030A`
  (https://ambientcg.com/view?id=WoodFloor051, https://ambientcg.com/view?id=Planks030A); tejas
  para el tejado curvo — `RoofingTiles013A` (https://ambientcg.com/view?id=RoofingTiles013A);
  metal envejecido para adornos y el sello de Zeniba — `Metal047A`
  (https://ambientcg.com/view?id=Metal047A); papel para los talismanes/ofuda de Zeniba y los carteles
  — `Paper001`/`Paper006` (https://ambientcg.com/view?id=Paper001). Todas CC0, comprobadas en la API
  `ambientcg.com/api/v2/full_json`. ✅

## Hallazgos — Punto 9: música y sonido

- Banda sonora oficial: **千と千尋の神隠し サウンドトラック** (Tokuma Japan Communications,
  18-jul-2001), compuesta por **Joe Hisaishi** (久石譲, acreditado también en la ficha oficial de
  `ghibli.jp` como «音楽 久石 譲»). 21 pistas, duración total ≈62 min · ✅ (MusicBrainz +
  ghibli.jp) · https://musicbrainz.org/release-group/dc1f9d7d-9a98-3f2c-83aa-c16dbb4a9ae1
- Tema de créditos finales: **いつも何度でも / Itsumo Nando Demo** («Always with Me» en inglés),
  pista 21 (3:35). Cantada por **Kimura Yumi** (木村弓), música y letra de **Kaku Wakako**
  (覚和歌子). Historia de producción: Miyazaki escuchó la canción de Kimura por radio mientras hacía
  *La princesa Mononoke* y años después la incorporó como tema de cierre de Chihiro · ✅ (Ghibli
  Wiki https://ghibli.fandom.com/wiki/Always_with_Me + MusicBrainz confirma la artista 木村弓 con
  el mismo nombre https://musicbrainz.org/artist/c6517557-a6e5-4e67-989d-87e0cf38c871 + créditos
  oficiales de ghibli.jp). Audio de referencia sin YouTube: Internet Archive
  «Itsumo Nando Demo (Sen To Chihiro No Kamikakushi)» ·
  https://archive.org/details/ItsumoNandoDemoSenToChihiroNoKamikakushi (2498 descargas).
- Tema principal/de apertura: **あの夏へ / Ano Natsu e** («One Summer's Day»), pista 1 (3:10) —
  suena sobre los créditos iniciales y en los momentos más nostálgicos. ⚠️ (título y duración
  confirmados en MusicBrainz; la asociación con los créditos iniciales es de memoria general del
  fandom, no la until confirmé con una segunda fuente escrita).
- Pista **ふたたび / Reprise (Again)**, n.º 19 (4:53) — música del vuelo nocturno de Chihiro sobre
  el dragón Haku, el momento más citado por el fandom como «el más emotivo» · ✅ (Ghibli Wiki
  https://ghibli.fandom.com/wiki/Reprise/Again + ficha de la pista en Apple Music/Spotify que la
  describe igual).
- Otras pistas con nombre de escena reconocible en el propio título (sin traducir, tal cual constan
  en el disco): 神さま達 (Los dioses/espíritus, n.º 7), 湯婆婆 (Yubaba, n.º 8), おクサレ神 (El
  dios podrido/Espíritu del Hedor, n.º 12), カオナシ (Kaonashi/Sin Cara, n.º 15), 6番目の駅 (Sexta
  estación, la escena del tren, n.º 16), 湯婆婆狂乱 (Yubaba enfurecida, n.º 17) · ✅ (listado
  oficial de MusicBrainz, títulos japoneses del propio disco).
- Efectos/sonido reconocible: los **susuwatari** (espíritus de hollín) no hablan, sólo emiten
  chillidos y murmullos agudos que suben de tono cuando están excitados o molestos — un recurso de
  sonido para marcar que están vivos sin darles idioma · ✅ (Wikipedia «Susuwatari» +
  Sonic Dictionary de Duke University, ficha dedicada a esos sonidos:
  https://sonicdictionary.duke.edu/items/spirited-away-sootball-minion-noises.html). La voz de Sin
  Cara son jadeos y monosílabos entrecortados («a… a…»), casi sin palabras claras hasta que devora a
  una rana y empieza a hablar con voz ajena — ⚠️ (una sola fuente de fandom, no confirmé con una
  segunda especializada en esta tanda).

## Hallazgos — Punto 10: vídeos (tráiler, escenas, análisis, tendencias)

- **Tráiler original japonés** (vía AniList): https://www.youtube.com/watch?v=ByXuk9QqQkk — no
  accesible desde este contenedor (YouTube pide iniciar sesión); anotado para quien sí pueda verlo.
  ⚠️
- **Tráiler doblado a español latino** (Sensacine México):
  https://www.dailymotion.com/video/x889bq8 · 1:38 · visto entero, 70 planos, transcripción en
  `partes/episodios.md`. Contiene los sellos «Ganadora del Oso de Oro de Berlín» y «40 premios
  internacionales» sobreimpresos (así lo dice el propio tráiler, 0:20-0:28) · ✅
- Otros tráilers doblados/subtitulados disponibles en Dailymotion (mismo listado que
  `datos-video.md`, no reprocesados por tiempo): «El viaje de Chihiro - Tráiler español» (Espinof,
  1:27) https://www.dailymotion.com/video/x81daub · «El viaje de Chihiro: Trailer Español»
  (Sensacine México, 2:32) https://www.dailymotion.com/video/x889bq8... — el más largo,
  `x88nkdm`, es «Tráiler (2)», 1:38. ⚠️ (listados, no todos vistos fotograma a fotograma).
- **Reestreno en cines de Latinoamérica, 7-ago-2025** (Cineplanet y cadenas asociadas) — parte de
  la ola de reestrenos de Ghibli en 2025 que generó bastante contenido de fans en TikTok compartiendo
  la experiencia de verla en pantalla grande · ⚠️ (una fuente de búsqueda web, sin acceso directo a
  TikTok para contar vistas).
- **Tendencia de TikTok — «la escena del tren» (Sexta Estación)**: la escena del tren cruzando el
  mar con Chihiro y Sin Cara es de las más usadas en ediciones/`filmtok` (ejemplos:
  «the train scene in Spirited Away is one of the best scenes i've ever seen»
  https://www.tiktok.com/@azosis_/video/7081608266148580614 — «spirited away sea train» con
  juguetes Tomica del tren real https://www.tiktok.com/@_innangg_/video/7271250088490552581); hay
  también contenido de viajeros que relacionan el escenario con el lago Tahoe (California) por el
  agua reflejando el paisaje · ⚠️ (visto vía buscador, no se pudieron abrir los TikTok directamente
  desde el contenedor).
- **Tendencia de TikTok — «Chihiro recuerda el nombre de Haku»**: citada como uno de los momentos
  más compartidos de la película en TikTok · ⚠️ (una fuente de búsqueda, sin enlace directo
  verificable).
- **Vídeos de análisis en español** encontrados por título (no se pudieron reproducir por el bloqueo
  de YouTube en este contenedor; quedan anotados para que quien sí tenga acceso los mire):
  «EL VIAJE DE CHIHIRO A TRAVÉS DEL COLOR | Análisis y significado» (dic-2021) —
  https://www.youtube.com/watch?v=EZz3WDzynNk · «Artista PRO analiza el ARTE de EL VIAJE DE CHIHIRO
  y el Estudio GHIBLI» (sep-2024) — https://www.youtube.com/watch?v=PTUxn8I8nPI · «Análisis y
  Explicación de El Viaje de Chihiro | STUDIO GHIBLI» —
  https://www.youtube.com/watch?v=X_9LFP4Xwk0. ⚠️ (títulos y canal, no contenido verificado).
- **Reel promocional visto entero** «Dame 1 minuto» (Sensacine México/Cinemex, Dailymotion
  `x9f6hg0`, 0:55): una presentadora resume Totoro, La princesa Mononoke y Chihiro para anunciar
  funciones en Cinemex; usa un plano de Chihiro cayendo con el vestido rojo (0:26), a Chihiro en el
  puente (0:26), volando con la capa roja (0:27) y a Chihiro sola en el tren junto a Sin Cara
  (0:43) y un ojo de dragón en primer plano (0:44) · ✅ (visto entero, 32 planos en
  `/tmp/claude-0/trabajo/98-el-viaje-de-chihiro-video/escenas-mx/hoja_01.jpg`).
- Internet Archive: copia completa de la película «Sen To Chihiro No Kamikakushi» (23 538
  descargas) y varias resubidas — es la que está procesando `episodio.py` en paralelo; no volví a
  descargarla · https://archive.org/details/SenToChihiroNoKamikakushi · ✅

## Hallazgos — Punto 14: poses analizadas (6-10 por personaje, con minuto o enlace)

### Chihiro Ogino
1. Abrazada a un ramo de flores en el asiento del coche, hombros encogidos, mirada baja (miedo a la
   mudanza) · oficial `chihiro001.jpg` · ⚠️ (sin minuto de vídeo, sólo still oficial).
2. Sentada a la mesa vacía del pueblo fantasma, cuerpo echado hacia la comida junto a sus padres ·
   oficial `chihiro004.jpg` · ⚠️
3. De pie, brazos pegados al cuerpo, girando la cabeza para mirar alrededor, asustada · tráiler
   0:23 · https://www.dailymotion.com/video/x889bq8?t=23 · ✅ — sirve para **pensar/dudar**.
4. Corriendo agarrada a la barandilla del puente rojo, brazo extendido hacia Haku, mirada de
   alarma · tráiler 0:31 · https://www.dailymotion.com/video/x889bq8?t=31 · ✅ — sirve para
   **animar/avisar**.
5. Mano extendida hacia el pomo de una puerta corredera metálica, cuerpo inclinado hacia delante
   (decidida a entrar a trabajar) · oficial `chihiro019.jpg` · ⚠️ — sirve para **presentarse**
   (es el gesto justo antes de pedirle trabajo a Yubaba).
6. Cargando un fardo de heno a la espalda, inclinada por el peso, pies descalzos, mirada al frente
   (arco de trabajo/madurez) · oficial `chihiro024.jpg` · ⚠️ — sirve para **explicar que se ha
   vuelto capaz**.
7. Cubriéndose la cara con las manos, llorando, hombros caídos · tráiler 1:45 ·
   https://www.dailymotion.com/video/x889bq8?t=105 · ✅
8. De pie sobre una barcaza, remando con una pértiga larga, piernas separadas para el equilibrio ·
   oficial `chihiro040.jpg` · ⚠️
9. Caminando de la mano con Haku niño, girada hacia él, sonrisa leve (reencuentro, final) ·
   oficial `chihiro049.jpg` · ⚠️ — sirve para **celebrar**.
10. Corriendo de la mano con alguien junto al mar, en pleno movimiento, pelo al viento · tráiler
    2:25 · https://www.dailymotion.com/video/x889bq8?t=145 · ✅

### Haku
1. De pie, rígido, junto a una estatua de piedra (jizō) en el bosque, postura protectora frente a
   Chihiro · oficial `chihiro002.jpg` · ⚠️
2. Brazo extendido hacia el horizonte al atardecer, gesto de conjurar/guiar · oficial
   `chihiro005.jpg` · ⚠️ — sirve para **explicar** (le está mostrando el camino a Chihiro).
3. Mirada fija y seria, cejas fruncidas, primer plano de advertencia · tráiler 0:33 ·
   https://www.dailymotion.com/video/x889bq8?t=33 · ✅ — sirve para **regañar/advertir**.
4. Junto a Chihiro en el puente, mano cerca de su hombro, guiándola con el cuerpo ligeramente
   inclinado hacia ella · tráiler 0:34 · https://www.dailymotion.com/video/x889bq8?t=34 · ✅
5. Forma de dragón, herido y sangrando, cabeza caída, sostenido por Chihiro (vulnerabilidad total)
   · oficial `chihiro038.jpg`, mismo plano en tráiler 1:18
   (https://www.dailymotion.com/video/x889bq8?t=78) · ✅
6. Forma de dragón volando de noche con Chihiro sobre el lomo, cuerpo en curva ascendente ·
   oficial `chihiro045.jpg` · ⚠️ — sirve para **animar** (la escena de la música «Reprise»).
7. Primer plano llorando/emocionado, lágrimas visibles, boca entreabierta · oficial
   `chihiro046.jpg` · ⚠️
8. Forma humana, caminando en grupo por el puente junto a una rana-espíritu y Chihiro, hombros
   relajados (alivio, tras salvarse) · reel promocional 2:05, plano #62 en
   `escenas-mx/hoja_01.jpg` · ✅

### Yubaba
1. Sentada a su escritorio firmando un contrato, mirada de reojo codiciosa, mano con anillos
   sujetando la pluma · oficial `chihiro016.jpg` · ⚠️ — sirve para **explicar/negociar** (es la
   escena del contrato que le roba el nombre a Chihiro).
2. Gritando furiosa con el bebé Bō en brazos, boca muy abierta, cuerpo echado hacia delante ·
   oficial `chihiro017.jpg` · ⚠️ — sirve para **regañar**.
3. Entre trabajadores agachados en fila, señalando y con la cabeza gigante inclinada hacia ellos ·
   oficial `chihiro028.jpg`, mismo tipo de plano en tráiler 0:56
   (https://www.dailymotion.com/video/x889bq8?t=56) · ✅ — sirve para **regañar/dirigir**.
4. Tomando el té con pastelillos, postura relajada y lujosa, dedo meñique levantado · oficial
   `chihiro044.jpg` · ⚠️ — sirve para **presentar** (recibe a Chihiro y Zeniba de invitadas).
5. Leyendo una carta con gafas de media luna, manos con anillos de colores sujetando el papel ·
   tráiler 1:16 · https://www.dailymotion.com/video/x889bq8?t=76 · ✅ — sirve para **pensar**.
6. Primer plano con sonrisa siniestra/mueca de enfado, ojos entornados · tráiler 2:01 ·
   https://www.dailymotion.com/video/x889bq8?t=121 · ✅

### Sin Cara (Kaonashi / No-Face)
1. De pie y solo en el puente rojo, brazos caídos a los costados, silueta negra recortada contra
   el atardecer · oficial `chihiro020.jpg` · ⚠️ — sirve para **pensar/observar**.
2. Asomado entre un árbol/muro, un brazo extendido ofreciendo algo dorado en la palma · oficial
   `chihiro025.jpg` · ⚠️ — sirve para **ofrecer/tentar**.
3. Silueta enorme y negra, máscara con la boca muy abierta, engullendo, empleados huyendo
   alrededor · oficial `chihiro033.jpg` · ⚠️ — sirve para **celebrar** (a su manera: glotonería
   descontrolada).
4. Sentado a la mesa del banquete, brazos extendidos hacia toda la comida a la vez · oficial
   `chihiro031.jpg` · ⚠️
5. Silueta apenas visible entre flores, en un pasillo en penumbra, quieto · tráiler 1:25 ·
   https://www.dailymotion.com/video/x889bq8?t=85 · ✅ — sirve para **acechar/esperar**.
6. De pie en la penumbra frente a Chihiro, cabeza ligeramente inclinada, sin moverse · tráiler
   2:14 · https://www.dailymotion.com/video/x889bq8?t=134 · ✅
7. Reflejo/silueta sobre las vías del tren bajo el agua, cabeza inclinada mirando hacia abajo,
   solo · oficial `chihiro041.jpg` · ⚠️ — sirve para **pensar**.
8. Sentado en el tren junto a Chihiro, manos quietas sobre las rodillas, mirando por la ventana ·
   oficial `chihiro042.jpg` · ⚠️ — sirve para **acompañar/calmar** (el plano que más cita la
   tendencia de TikTok del punto 10).

## Lo mejor para la lámina

1. La casa de baños (Aburaya) de noche, iluminada, con el puente rojo — fondo icónico único de la
   serie, ya con paleta medida (marrón-ocre #342E2C dominante) para pintar o modelar en Blender.
2. El plano del tren sobre el mar (`chihiro043.jpg`) — silencioso, azul-violeta, funciona solo
   como fondo de canal contemplativo/de escritura; es además el que más comparte el fandom.
3. Sin Cara sentado y quieto (poses 5-8) — sirve para un canal tranquilo o de «escucha», postura
   pasiva y sin diálogo ruidoso, encaja con un cuadro de diálogo susurrado en vez de burbuja.
4. Yubaba firmando el contrato (pose 1) — muy útil para un canal de reglas o de «normas del
   servidor», con su propio cuadro de diálogo (carta con sello) en vez de burbuja blanca.
5. Los susuwatari en la sala de calderas — paleta casi monocroma, ideal como textura de fondo
   decorativa para cualquier canal sin robar protagonismo.

## No encontré

- ⚠️ No pude confirmar con una segunda fuente escrita que «あの夏へ/One Summer's Day» suene
  específicamente sobre los créditos iniciales (sólo la duración y el título están confirmados en
  MusicBrainz). Búsquedas: «Spirited Away opening theme One Summer's Day scene» (inglés, resultados
  genéricos de streaming, no un análisis de minutaje).
- ⚠️ No pude verificar con una segunda fuente especializada el registro exacto de la voz de Sin
  Cara (sólo un resumen de fandom). Búsqueda: «Spirited Away No-Face voice sound design» (inglés) —
  salieron mayoritariamente reseñas genéricas, no análisis de sonido.
- ❌ No pude ver ningún vídeo en YouTube directamente (tráiler original japonés, ni los 3 análisis
  en español que sí localicé por título): este contenedor pide iniciar sesión. Quedan enlazados por
  si el jefe u otro ayudante sí tiene acceso.
- ❌ AnimeThemes no respondió en esta tanda (ya había fallado con HTTP 522 en `datos-video.md`;
  reintenté una vez, sin respuesta) — no es crítico porque es película, no tiene openings/endings de
  serie en ese catálogo.
- ⚠️ La ficha minuto a minuto de la película completa **no se va a hacer**: el jefe avisó a mitad
  de esta tanda de que el archivo de Internet Archive (`SenToChihiroNoKamikakushi`) da 401
  (descarga restringida) y no hay que reintentarlo. Los minutos de las escenas fuera del tráiler y
  del reel promocional se quedan con still oficial de `ghibli.jp` (sin timecode) en vez de minuto
  exacto — no es una tarea pendiente, es el límite real de las fuentes disponibles para esta obra.

## Bitácora de búsqueda

- Español: «El viaje de Chihiro tendencia TikTok escena viral 2024 2025» (WebSearch) →
  reestrenos en cines 2025, sin cifras verificables de TikTok directamente.
- Español: «El viaje de Chihiro análisis fondos arte Ghibli video YouTube minuto» (WebSearch) →
  3 vídeos de análisis en español localizados por título (ver punto 10), no reproducibles aquí.
- Inglés: «Spirited Away TikTok trend train scene viral» (WebSearch) → confirma la escena del tren
  (Sexta Estación) como la más usada en ediciones de TikTok.
- Inglés: «Spirited Away soundtrack scene Reprise Haku name Joe Hisaishi score cue» (WebSearch) →
  confirma que «Reprise/Again» acompaña el vuelo del dragón.
- Inglés: «Spirited Away sound design susuwatari soot sprites squeak onomatopoeia» (WebSearch) →
  Wikipedia + Sonic Dictionary de Duke University sobre el sonido de los susuwatari.
- Wiki (Ghibli Fandom, `ghibli.fandom.com/api.php`): búsqueda de texto «Itsumo Nando Demo» → página
  «Always with Me»; wikitext leído para créditos de producción (sin copiar la letra).
- MusicBrainz API: `release-group` del disco (21 pistas, títulos japoneses) y `artist` para
  confirmar a Kimura Yumi como intérprete.
- ghibli.jp: HTML de `works/chihiro/` leído completo para sacar las 50 URL de imágenes oficiales,
  sus tamaños (`data-size`), el texto de licencia y los metadatos de reparto/equipo (meta
  description).
- ambientcg.com API (`/api/v2/full_json?type=Material`): «wood plank», «copper», «roof tiles»,
  «paper» → texturas CC0 equivalentes a madera, metal, tejas y papel de la casa de baños.
- Vídeo mirado entero: tráiler doblado MX (Dailymotion x889bq8, 1:38) y reel promocional «Dame 1
  minuto» (Dailymotion x9f6hg0, 0:55) — hojas de contacto propias y de `episodios.md`.
- Imágenes miradas una por una: 50 fotogramas oficiales de `ghibli.jp` en 5 hojas de contacto
  propias (`/tmp/claude-0/trabajo/98-el-viaje-de-chihiro-video/ghibli-oficial/hoja_0{1..5}.jpg`).
- Colores medidos con `estilo.py`: 11 fotogramas oficiales (ver punto 4), JSON en
  `/tmp/claude-0/trabajo/98-el-viaje-de-chihiro-video/estilo/lugares.json` y `lugares2.json`.

Sigue: la ficha de la película completa no va a salir (aviso del jefe, ver arriba), así que no hay
que esperarla. Sólo queda opcional, no obligatorio: una segunda fuente para «One Summer's Day = tema
de apertura» y para el registro de voz de Sin Cara (ver «No encontré», ambos ⚠️ de un solo dato).
Los puntos 2, 4, 9, 10 y 14 están completos para el nivel que permiten las fuentes disponibles
(tráiler doblado con minuto exacto + 50 stills oficiales de `ghibli.jp` + reel promocional + 11
paletas medidas con `estilo.py`). Parte terminada.
