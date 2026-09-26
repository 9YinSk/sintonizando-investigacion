# Texto, juegos y técnica · Sakamoto Days

Investigador de texto, juegos y técnica (puntos 5, 6, 11, 18, 24, 25 de ENCARGO.md). Parte de
`partes/datos-texto.md` (recolectar.py, 25-sep-2026); no repite esas consultas, las comprueba y
profundiza. Sin serie hermana en este encargo (`encargos/46-sakamoto-days.md` no la menciona).

## 18 · Estilo de dibujo y técnica, y cómo replicarlo

Sakamoto Days tiene dos capas de estilo: el manga (Yuuto Suzuki, Weekly Shōnen Jump) y el anime
(TMS Entertainment, dir. Masaki Watanabe). Las fuentes confirman técnica concreta en ambos.

- Autor del manga, Yuuto Suzuki, formado en la Facultad de Pintura Japonesa (Nihonga) de la
  Universidad de Artes de Tokio (Geidai); antes de mangaka trabajó haciendo *storyboards* para
  audiovisuales, de ahí su composición cinematográfica · https://mediadogs.jp/2026/03/03/yuto-suzuki-sakamoto-days-career-fixed-2026/ · ⚠️ (una fuente, biografía verificable) · —
- Su estilo de acción usa ángulos de cámara variados, encuadres múltiples para guiar la lectura,
  y contraste deliberado entre tramos serios y cómicos («ver anime en papel»); admira a Takehiko
  Inoue (Slam Dunk) · https://mediadogs.jp/2026/03/03/yuto-suzuki-sakamoto-days-career-fixed-2026/ · ⚠️ (una fuente) · —
- Serie de charlas técnicas del propio Suzuki en el portal de premios de Shūeisha (Jump Manga
  Shō) sobre «los principios letales del manga de acción»: encuadre cinematográfico, claridad
  visual, contexto de combate, ritmo cómico-acción, caracterización en pelea · https://www.jump-mangasho.com/chair/category/shinsekai/suzuki_jump_no056/ · ✅ (fuente oficial de Shūeisha) · —
- Anime (TMS Entertainment, 2025): capa de **textura de papel** superpuesta a toda la imagen,
  idea del director de fotografía para «animar las ilustraciones a color» del manga; son
  rayones sutiles tipo pergamino que **no se mueven** con los personajes (quedan fijos, como si
  la escena pasara tras un cristal); da tonos oscuros y amenazantes en peleas y calidez en
  escenas familiares · https://www.awn.com/animationworld/masaki-watanabe-talks-sakamoto-days · ✅ (entrevista al director, AWN) · —
- Software de producción del anime: **Clip Studio Paint y Adobe** (director Masaki Watanabe,
  entrevista) · https://www.awn.com/animationworld/masaki-watanabe-talks-sakamoto-days · ✅ · —
- Las armas se dibujan con brillo y filo deliberadamente realzados («un arma sin brillo o un
  cuchillo sin filo perdería la tensión»); a veces se altera su funcionamiento real (la Mosin-Nagant
  de Heisuke se anima como automática, sin serlo) para «la showmanía del personaje» · https://www.awn.com/animationworld/masaki-watanabe-talks-sakamoto-days · ✅ · —
- El episodio 3 (montaña rusa) combinó modelo 3D, animación 2D y rotoscopiado; tardó el triple
  que una escena normal por la dificultad de coordinar creadores freelance manteniendo estilo
  coherente · https://www.awn.com/animationworld/masaki-watanabe-talks-sakamoto-days · ✅ · minuto: escena ep. 3
- Producción distribuida: la última entrega de temporada usó 23 estudios distintos de animación
  para completarse a tiempo, según prensa especializada tras retrasos de producción · https://screenrant.com/sakamoto-days-anime-production-delay-studio-issues/ · ⚠️ (una fuente, prensa) · —
- Estudio: TMS Entertainment (no Toei, aunque a veces se confunde); dirección Masaki Watanabe,
  guion Taku Kishimoto, diseño de personajes You Moriyama, dirección de arte Yukiko Maruyama,
  dirección de fotografía Bolun Cai, música Yuuki Hayashi · https://anilist.co/anime/177709/staff (datos-texto.md) · ✅ (AniList + créditos oficiales del ED) · —

**Rigs y tramas: ver puntos 3 y 19** (los trae el investigador de imagen: modelos 3D con
licencia libre y texturas 2D equivalentes).

### Cómo replicarlo en Photoshop
- Base del *line art*: pincel de tinta con grosor variable (más grueso en contorno exterior,
  fino en detalle interior), como hace la mayoría del manga shōnen de acción; en Photoshop,
  pincel «Kyle's Real Chalk/Ink» o el pincel Hard Round con *Pen Pressure* activado en Opacidad y
  Tamaño da un resultado cercano al trazo de Suzuki (grueso, algo irregular, sin uniformidad
  vectorial) · deducido de las páginas de la wiki (hoja de imagen) · ⚠️ (análisis propio sobre
  las páginas oficiales, sin entrevista de materiales del manga) · —
- Capa de textura de papel del anime: crear una capa de textura (scan de papel, grano fino claro)
  en modo de fusión **Multiplicar** u **Overlay** al 15-25% de opacidad, **sin animar/mover** esa
  capa entre fotogramas —replica el efecto «cristal fijo» descrito por el director de fotografía
  · técnica derivada de la entrevista AWN · ✅ (entrevista, aplicación práctica propia) · —
- Paleta de combate: sombras duras con tinte frío (azules/violetas) en interiores de acción;
  escenas domésticas (la tienda Sakamoto) con luz cálida y contraste bajo — usar un ajuste de
  Curvas/Color Balance por escena, no un LUT global, para lograr ese contraste tonal descrito
  en la entrevista · https://www.awn.com/animationworld/masaki-watanabe-talks-sakamoto-days · ⚠️ (aplicación práctica derivada de la entrevista) · —
- Brillo de armas: capa de *Dodge* o superposición blanca con máscara sólo en filos y cañones,
  con un *Outer Glow* sutil; details de metal en Overlay al 30-40% siguiendo lo que dice el
  director sobre reforzar el brillo del arma · https://www.awn.com/animationworld/masaki-watanabe-talks-sakamoto-days · ⚠️ · —

### Cómo replicarlo en Blender
- Para un *toon shader* que imite la mezcla 2D/3D del anime (ep. 3 usó 3D + rotoscopiado):
  Freestyle para el contorno (grosor variable, no uniforme, para imitar el pincel del manga) +
  un shader tipo *Shader to RGB* con 2-3 bandas de sombra (no degradado suave) para plano de
  color, y una capa de compositing final con textura de papel fija superpuesta (igual que en
  Photoshop) usando un nodo Mix por encima del render, sin animar su UV · técnica derivada de la
  entrevista AWN aplicada a Blender · ⚠️ (aplicación práctica propia) · —
- Encuadres: cámaras con distancia focal corta y ángulos bajos/contrapicados para las escenas de
  pelea (coincide con lo que describe Suzuki sobre ángulos variados); usar *Depth of Field* leve
  para separar personaje de fondo en primeros planos de acción · deducido de la entrevista y del
  estilo de manga de acción de Jump · ⚠️ · —

### Encuadres y composición típicos
- Primeros planos y contrapicados para maximizar intensidad y velocidad en peleas; uso de
  encuadres múltiples/viñetas partidas para guiar la lectura de la acción · https://mediadogs.jp/2026/03/03/yuto-suzuki-sakamoto-days-career-fixed-2026/ · ⚠️ (una fuente) · —
- Momentos de impacto resueltos con pocos fotogramas «congelados» muy estilizados («pastel chalk
  freeze-frame» / «postcard memory»), en vez de animación fluida continua · citado en resultados
  de búsqueda sobre lettering/estilo (fuente secundaria, sin artículo único verificable) · ⚠️ (dato de búsqueda agregada, no artículo propio) · —

## Bitácora
- Búsqueda (ES/JA): «Sakamoto Days logo font typeface», «Sakamoto Days 鈴木祐斗 インタビュー 作画 画材», «Sakamoto Days manga onomatopoeia sound effects lettering», «SAKAMOTO DAYS アニメ 制作 東映アニメーション TMS clip studio 3DCG making».
- Fuentes consultadas: AniList (datos-texto.md), jump-mangasho.com (Shūeisha oficial), mediadogs.jp, awn.com (entrevista director), screenrant.com.
