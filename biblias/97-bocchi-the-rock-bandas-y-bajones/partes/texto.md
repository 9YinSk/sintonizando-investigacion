# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · Bocchi the Rock: bandas y bajones

Puntos de ENCARGO.md: **5** (tipografía), **6** (cómo hablan y piensan en
pantalla), **11** (videojuegos de la franquicia), **18** (estilo de dibujo y
técnica, y cómo replicarlo — con foco especial en los **estilos cambiantes**
de los «bajones» de Bocchi, según pide el encargo), **24** (obras parecidas),
**25** (el mundo, la historia y sus símbolos). Parto de `partes/datos-texto.md`
(no repito esas consultas: AniList, staff, obras relacionadas, Steam sin
resultados) y de las hojas ya reunidas en `partes/datos-imagen.md` (logo
oficial, modelos 3D). No hay `biblia.md` todavía (primera pasada, el redactor
aún no ha escrito nada): este archivo entrega la investigación en bruto para
que él la use. `partes/episodios.md` no existe todavía (nadie ha corrido
`episodio.py` para esta serie).

YouTube pidió iniciar sesión al probar (ratos de la IP compartida): usé
Internet Archive (el vídeo Opening/Closing del Blu-ray vol. 1, 1920×1080),
Dailymotion (tráilers), la wiki de Fandom (`bocchi-the-rock`, páginas de cada
episodio con su ficha de director/storyboard y su sección Trivia) y fuentes
escritas (Sakuga Blog, entrevistas oficiales, TV Tropes vía el resumen del
buscador porque el fetch directo da 403) para reconstruir minuto a minuto los
cambios de estilo sin poder bajar los 12 episodios completos.

## Hallazgos · Punto 5 — Tipografía

- **El logo/título no es una sola fuente**: cada portada de tomo del manga usa
  una tipografía distinta para «BOCCHI THE ROCK!» — confirmado en dos fuentes
  independientes: [instafonts.io/different-fonts/Bocchi The Rock](https://instafonts.io/different-fonts/Bocchi%20The%20Rock)
  («Every cover... uses a different font for the logo!») y la propia colección
  de portadas de Yen Press/BookWalker (7 tomos, 7 letras distintas) ✅.
- **El logo oficial del anime** (el que usa el sitio bocchi.rocks, diseñado
  por **Tomoyuki Uchikoga** según los créditos de AniList —
  `partes/datos-texto.md`, sección «Equipo creativo» ✅) está en Wikimedia
  Commons: [`Bocchi_the_Rock!_logo.svg`](https://commons.wikimedia.org/wiki/File:Bocchi_the_Rock!_logo.svg),
  **512×159 px** (medido, dato ya en `partes/datos-imagen.md`). La ficha de
  Commons dice que se subió sacándolo de `bocchi.rocks` y que es
  **«a text-logo... created with an unknown SVG tool»**, marcado dominio
  público por no alcanzar el umbral de originalidad de Japón (pero con aviso
  de posible marca registrada) — fuente: página de Commons del archivo ✅.
  Es un bloque **muy grueso, condensado, casi sin curvas** (descripción visual
  ya contrastada en la investigación previa de esta misma serie,
  `biblias/_ya_hechas/Bocchi the Rock.md` §5, con las imágenes numeradas
  `019.png`/`058.png`/`067.png`/`086.png` de esa hoja de contacto) ⚠️ (una
  sola fuente propia sin repetir yo la medición; queda para quien mire de
  nuevo las hojas de imagen).
- **El título japonés a mano** («ぼっち・ざ・ろっく!») se repite como un
  garabato de rotulador grueso, normalmente amarillo o del color de la
  portada — mismo origen (⚠️ una fuente, la investigación previa).
- **Letras libres recomendadas, comprobadas con fontTools una por una**
  (descargué los `.ttf` de Google Fonts con `text=áéíóúñÑ¿¡` y abrí cada uno
  con `TTFont(f).getBestCmap()`): **las 9 traen tildes, ñ, Ñ, ¿ y ¡
  completos** ✅ (comprobado yo mismo, no de memoria):

| Uso (punto 5) | Letra libre | Por qué encaja | Fuente de la letra |
|---|---|---|---|
| Logo / título | **Anton** (Google Fonts) | condensada, muy gruesa, casi sin curvas — como el bloque «BOCCHI THE ROCK» de `058.png` | fonts.google.com/specimen/Anton |
| Rótulos/flyers de concierto | **Bungee** (Google Fonts) | gruesa, redondeada, estilo flyer urbano/gig-poster | fonts.google.com/specimen/Bungee |
| Globo normal (diálogo) | **M PLUS Rounded 1c** (Google Fonts) | gótica redondeada japonesa con juego de latín completo — la familia real de Kirara pasa por redondeadas (ver punto 6) | fonts.google.com/specimen/M+PLUS+Rounded+1c |
| Grito / énfasis | **Titan One** (Google Fonts) | trazo directo y sólido, letras infladas — releva a «Shin Go»/«Comic Reggae» que usa la revista | fonts.google.com/specimen/Titan+One |
| Pensamiento / monólogo | **Baloo 2** (Google Fonts) | redondeada suave, más liviana que el grito — releva a la «Suela» redondeada de Kirara | fonts.google.com/specimen/Baloo+2 |
| Onomatopeya | **Bangers** (Google Fonts) | letra de cómic occidental gruesa e inclinada, la más cercana libre a un SFX de manga sin ser japonesa | fonts.google.com/specimen/Bangers |
| Cartel del mundo (letrero neón de STARRY) | **Monoton** (Google Fonts) | simula tubo de neón, redondeada — coincide con el letrero real (ver punto 25) | fonts.google.com/specimen/Monoton |
| Interfaz de juego (Kotodaman/Kirara Fantasia) | **Zen Maru Gothic** (Google Fonts) | gótica redondeada japonesa de uso real en apps/juegos móviles japoneses | fonts.google.com/specimen/Zen+Maru+Gothic |
| Subtítulos / créditos | **M PLUS 1** (Google Fonts) | sans limpia, muy legible en tamaño pequeño, familia hermana de la anterior | fonts.google.com/specimen/M+PLUS+1 |

  Archivos verificados en `/tmp/claude-0/trabajo/97-bocchi-the-rock-bandas-y-bajones-texto/fonts/`
  (9 `.ttf`, script de comprobación con fontTools ejecutado sobre cada uno).
- **La tipografía real de los globos de manga de Manga Time Kirara** (la
  revista donde se serializa Bocchi the Rock desde dic-2017 — Wikipedia ✅):
  según un análisis específico de rotulación de la revista
  ([note.com/soudakyoto_ikou, «まんがタイムきららの「写植」を読む」」](https://note.com/soudakyoto_ikou/n/nd63330df85d8),
  en japonés) ⚠️ **una sola fuente, sin confirmar en una segunda** — la
  revista pasó de fotocomposición Sha-Ken a DTP hacia 2012-2013 y usa:
  - diálogo normal: combinación **Anticho AN1** (kana) + **太ゴ B101** (kanji);
  - pensamientos/monólogos: **Suela** (redondeada);
  - gritos/enfado: **Shin Go** (Morisawa) o **Comic Reggae** (Fontworks,
    puntiaguda);
  - escenas tristes/flashback: **Mathis** (Fontworks, serif, la misma familia
    que se asocia a Evangelion);
  - momentos cómicos/torpes — **el artículo cita textualmente a Bocchi**:
    **Rodin Happy** (Fontworks, diseño de Sato Yutaka) se usa «cuando
    personajes como Bocchi actúan de forma graciosa o torpe» ✅ dato con
    nombre de personaje citado, aunque de una sola fuente ⚠️.
  Estas fuentes son de pago (Fontworks/Morisawa); las libres de la tabla de
  arriba son la alternativa recomendada para la lámina.

## Hallazgos · Punto 6 — Cómo hablan y piensan en pantalla

- **El pensamiento de Bocchi NO es un globo con nube**: la serie corta a una
  escena aparte («Bocchi time» / imagine spot) que cambia de técnica de dibujo
  cada vez — confirmado en dos fuentes que describen el mismo mecanismo con
  ejemplos distintos: [gamerant.com/bocchi-the-rock-animation](https://gamerant.com/bocchi-the-rock-animation/)
  y [screenrant.com, «10 Anime That Pushed Animation To Its Limit»](https://screenrant.com/10-anime-pushed-animation-to-limit-bocchi-evangelion/)
  ✅. Para una lámina fija (que no puede cortar a otra escena), lo fiel es que
  el bocadillo de Bocchi se vea «roto»/glitcheado en los bordes en vez de un
  globo limpio — ver detalle técnico completo en el punto 18.
- **Cada episodio tiene una «cartela de título» de un color distinto**, sin
  texto encima (sólo color) — confirmado episodio por episodio en la wiki
  (wikitext de cada página, sección Trivia, vía API `action=parse`) ✅:
  Ep.1 «Lonely Rolling Bocchi» = **rosa**; Ep.4 «Jumping Girl(s)» = **azul**;
  Ep.6 «Eight Views» = **verde menta pastel**; Ep.7 «To Your House» = **rosa**;
  Ep.8 «Bocchi the Rock» = **amarillo**. Fuente:
  [bocchi-the-rock.fandom.com](https://bocchi-the-rock.fandom.com), páginas de
  cada episodio ✅ (dato propio, sacado directo del wikitext, no de memoria).
- **Cada episodio termina con una «frase de cierre» (ending quote) atribuida a
  un personaje concreto**, mostrada como texto en pantalla tras el corte —
  mismo origen, confirmado en las mismas 5 fichas de episodio: Ep.1 → Bocchi;
  Ep.4 → Ryo; Ep.6 → Hiroi (Kikuri); Ep.7 → Bocchi; Ep.8 → Nijika ✅. Es un
  recurso gráfico fijo y reconocible: sirve de referencia directa para «un
  cuadro de diálogo propio de la serie» que pide `AYUDANTE.md`.
- **Los pensamientos "normales" (no ansiosos)** de otros personajes no llevan
  ese quiebre de estilo — es un lenguaje visual reservado casi en exclusiva a
  Bocchi (contraste con Kita, que se muestra con destellos/estrellitas cuando
  brilla socialmente, según la investigación previa de esta serie,
  `biblias/_ya_hechas/Bocchi the Rock.md` §6) ⚠️ una sola fuente (no volví a
  comprobarlo con imagen propia; lo confirma el investigador de vídeo/imagen
  si mira las escenas).
- **Los carteles y rótulos del mundo real dentro de la ficción** (parte del
  punto 6 «cartelas»): el episodio 4 usa una parodia real de Instagram
  llamada **«Isosta» (Issta)** en pantalla de móvil — confirmado en el
  wikitext de «Jumping Girl(s)» (`*An SNS online platform Isosta (Issta) is a
  parody of Instagram`) ✅, y también nombrada en el listado de redes
  oficiales de AniList (`partes/datos-video.md`: «SOCIAL · Instagram
  (Japanese): instagram.com/BTR_isosta») ✅ dos fuentes cruzadas.
- **Interfaz de juego real usada por el fandom para «hablar» de Bocchi**: en
  la colaboración con **Kotodaman** (共闘ことばRPG コトダマン, RPG de palabras),
  los eventos llevan títulos-frase sacados de la serie, p. ej. **「転がるぼっち」
  (Rolling Bocchi)**, el mismo título que el episodio 1 — fuente:
  [kotodaman.jp/info/detail/078658NxxMqVeRkt8j.html](https://kotodaman.jp/info/detail/078658NxxMqVeRkt8j.html) ✅
  (oficial, en japonés). Ver ficha completa en el punto 11.

## Hallazgos · Punto 11 — Videojuegos de la franquicia

- **Bocchi the Rock! no tiene un videojuego propio** (ni de consola ni un
  rítmico dedicado): comprobado con `herramientas/recolectar.py` (búsqueda en
  Steam sin resultados, `partes/datos-texto.md`) y con dos búsquedas propias
  adicionales en japonés e inglés: «ぼっち・ざ・ろっく ゲーム», «Bocchi the
  Rock Groove Coaster / Project Sekai / Taiko no Tatsujin collaboration» — sin
  resultado de juego propio o de un tie-in rítmico ✅ (dos búsquedas
  independientes, ninguna encontró nada; no es «no busqué», es «no existe» con
  las búsquedas hechas).
- **Sí existen 2 colaboraciones dentro de juegos móviles japoneses ya
  existentes** (lo más parecido a «interfaz, menús y cajas de diálogo» que
  puede investigarse):
  1. **Kirara Fantasia** (Drecom/Meteorise, Aniplex) — RPG gratuito con
     personajes de toda la línea editorial Manga Time Kirara. Bocchi, Nijika,
     Ryo y Kita se añadieron poco después del episodio 1 del anime — fuente:
     [en.wikipedia.org/wiki/Bocchi_the_Rock!](https://en.wikipedia.org/wiki/Bocchi_the_Rock!) ✅,
     confirmado también por un tuit de la cuenta de reseñas
     [x.com/BocchiTheRockS2](https://x.com/BocchiTheRockS2/status/1669665863128190976)
     («Nijika, Ryo, Kita, and Bocchi were all featured in the game... enjoy
     the special attacks of each Kessoku Band member») ✅. **El juego cerró el
     28-feb-2023**: la interfaz ya no es jugable en vivo, sólo capturas de
     archivo — la wiki de fans sigue viva en
     [kirarafantasia.miraheze.org](https://kirarafantasia.miraheze.org/wiki/Main_Page)
     (la ficha directa dio HTTP 402 al intentar leerla con la herramienta de
     fetch) ⚠️ no pude confirmar visualmente el HUD de batalla, sólo texto.
  2. **Kotodaman** (コトダマン, «共闘ことばRPG», Bandai Namco — RPG cooperativo
     donde se combate formando palabras con kanji): colaboración oficial
     abril-mayo 2024 — fuente primaria oficial:
     [kotodaman.jp/info/detail/078658NxxMqVeRkt8j.html](https://kotodaman.jp/info/detail/078658NxxMqVeRkt8j.html)
     y [.../078690MsBdDJsYPa.html](https://kotodaman.jp/info/detail/078690MsBdDJsYPa.html)
     ✅ (dos anuncios oficiales del propio juego). Personajes confirmados:
     後藤ひとり, 伊地知虹夏, 山田リョウ, 喜多郁代, y **廣井きくり** (Kikuri Hiroi,
     el personaje secundario adulto), con variantes especiales tipo
     «メイドぼっち» (Bocchi maid) y «承認欲求モンスター» (monstruo de la
     necesidad de aprobación, un chiste sobre Bocchi) ✅. Mecánicas
     confirmadas: gacha de colaboración, «クエスト de examen» (misiones-quiz)
     que dan materiales de invocación, un «panel de colaboración»
     (コラボパネル) de recompensas por hitos, y sistema de «nivel de simpatía»
     — resumen de [gamewith.jp/kotodaman/article/show/447030](https://gamewith.jp/kotodaman/article/show/447030),
     una guía de fans japonesa, contrastado con el propio anuncio oficial ✅
     dos fuentes. No pude extraer URLs de captura de pantalla concretas del
     HUD (las imágenes están en `/upload_images/` con hash, sin vista directa
     desde el fetch de texto) ⚠️.
- **No hay minijuegos oficiales en el sitio web** `bocchi.rocks` más allá de
  contenido promocional — comprobado visitando `bocchi.rocks/special/zadankai/`
  (mesa redonda del staff): es sólo texto/entrevista, no una app ✅ (visto
  directamente).

## Hallazgos · Punto 18 — Estilo de dibujo y técnica, y cómo replicarlo

**Estudio y equipo** (ya en `partes/datos-texto.md`, sección «Equipo
creativo», fuente AniList ✅): CloverWorks · director **Keiichirō Saitō** ·
diseño de personajes y **director de animación jefe: Kerorira** · director de
arte **Yasunao Moriyasu** · diseño de color **Asuka Yokota** · CG: productor
**Takashi Ikeda**, director **Katsuaki Miyaji**.

### Filosofía de diseño (de entrevistas directas al staff)

- **Kerorira** (diseñador de personajes) explica que probó diseños con muchas
  líneas, pero el director Saitō pidió **«designs with fewer lines»** para que
  la animación cómica de movimiento rápido fuera viable en producción —
  fuente primaria: entrevista oficial resumida por
  [Sakuga Blog, «Main Staff Interviews»](https://blog.sakugabooru.com/2022/11/26/bocchi-the-rock-main-staff-interviews-series-director-keiichiro-saito-character-designer-kerorira-animation-producer-shouta-umehara/)
  ✅ (cita textual: «you need to take animation into consideration to an
  extent in your designs, or else it leads to challenges during
  production»).
- **La ansiedad de Hitori en el manga** se dibuja con sombras en la cara y
  líneas verticales constantes; para el anime, Kerorira dijo que igualar eso
  **«would end up being too much»**, así que en su lugar usaron **cejas
  ligeramente fruncidas y postura encorvada** — misma fuente ✅.
- **Saitō sobre representar los ataques de ansiedad**: hay que tratarlos con
  cuidado, «porque tomárselo muy en serio lo vuelve grave y deprimente, pero
  usar sólo comedia tampoco es la respuesta» — hay que caminar la línea entre
  cómico y serio sin pasarse a ninguno de los dos lados — misma entrevista ✅.
- **Influencia declarada por el propio Saitō**: dijo en el «1st Bocchi
  Guidebook» oficial que estuvo consciente de **K-On!** (que vio en el
  instituto) durante toda la producción, y que espera que, como K-On!, sea una
  obra que siga en el corazón de la audiencia 10 años después — fuente:
  resumen de esa entrevista en
  [Anime News Network, «Staff Reflect on Growth and Change»](https://www.animenewsnetwork.com/interview/2024-07-12/bocchi-the-rock-staff-reflect-on-growth-and-change/.213092)
  ✅, y confirmado en un segundo idioma (coreano) citando la misma frase del
  director: [ko.wikipedia/나무위키 vía búsqueda](https://namu.wiki/w/%EB%B4%87%EC%B9%98%20%EB%8D%94%20%EB%A1%9D!/%EC%95%A0%EB%8B%88%EB%A9%94%EC%9D%B4%EC%85%98)
  ✅ dos fuentes/idiomas.

### Los «bajones»: técnicas de estilo documentadas, episodio por episodio

| Ep. | Título | Qué cambia | Quién lo hizo / fuente |
|---|---|---|---|
| 1 | Lonely Rolling Bocchi | Bocchi actúa metida en una **caja de cartón de mangos** («Mango Mask») en su primer concierto — atrezzo real, no cambio de técnica, pero es EL gag visual más reconocido de la serie | Ficha de [Hitori Gotoh, wiki](https://bocchi-the-rock.fandom.com/wiki/Hitori_Gotoh) ✅ — corregido ya en la biblia previa: el gag SÍ existe, no es una confusión |
| 4 | Jumping Girl(s) | Bocchi «explota»/**falla como un programa que se cuelga (glitch)** al ponerse ansiosa | [screenrant.com](https://screenrant.com/10-anime-pushed-animation-to-limit-bocchi-evangelion/): «glitches out like a computer program» ✅ |
| 6 | Eight Views | Bocchi entra en espiral por no poder venderle una entrada a su perro → secuencia en **pixel art**, hecha por el estudio/artista **«The Worst Vegetable»** | [Sakuga Blog, notas de producción](https://blog.sakugabooru.com/2022/12/26/bocchi-the-rock-complete-production-notes-and-final-impressions/) + confirmado independiente por reseñas (gamerant, wrongeverytime) ✅ dos fuentes |
| 7 | To Your House | Segmento **«Munions»**, parodia del estilo 3D de *Minions* (2015); segmento **«Thinking of You Kisses Over Flowers»**, parodia del shojo clásico *Boys Over Flowers* (Hana yori Dango) — cambio total de estilo de dibujo y de medio (3D vs. shojo de trazo fino) | Wikitext oficial de la página del episodio en la wiki ✅ (dato propio, confirmado directo en la ficha) |
| 7 | To Your House | **Zoetrope 3D real** («trauma sport zoetrope»), animadores 2D tradicionales haciendo «artefactos divertidos» por encargo directo de Saitō — creado por **Nobuhide Kariya** (también storyboard/director del episodio 4) y **Toshiyuki Sato** | [Sakuga Blog, notas de producción](https://blog.sakugabooru.com/2022/12/26/bocchi-the-rock-complete-production-notes-and-final-impressions/) ✅ |
| 8 | Bocchi the Rock | Bocchi agotada hace la **pose final de Ashita no Joe (Tomorrow's Joe)** — Guitarman y el micrófono bajan del cielo como ángeles gritando «¡Felicidades! ¡Felicidades!» | Resumen de análisis de referencias (TV Tropes vía buscador) ✅, coincide con la mención genérica de «Ashita no Joe» del artículo de gamerant ⚠️→✅ (dos fuentes que apuntan al mismo gag) |
| 9 | Enoshima Escar | Tras ser atacada por pájaros, Bocchi queda tumbada en un **cráter humeante en la pose de Yamcha** (Dragon Ball) | Mismo resumen de referencias, TV Tropes vía buscador ✅ |
| 10 | After Dark | Plano del techo + línea calcada de un plano icónico de **Neon Genesis Evangelion**, minuto **≈04:01** | Mismo resumen de referencias ✅ (⚠️ minuto de una sola fuente indirecta, no confirmado viendo el episodio yo mismo — YouTube bloqueado; el investigador de vídeo debería confirmarlo si accede al episodio) |
| — | (genérico, varios) | **Rotoscopia/mocap real** para las escenas de tocar instrumentos, con datos de actores reales: Bocchi por **Kotone Ushitani**, Kita-chan por **Kisumi Reika** y **Jakko** (todos de SolidCube) — asegura que los dedos caigan en las cuerdas/teclas correctas | [Sakuga Blog, notas de producción](https://blog.sakugabooru.com/2022/12/26/bocchi-the-rock-complete-production-notes-and-final-impressions/) ✅ |
| — | (genérico, escenas de concierto) | **Cámaras virtuales 3D** dentro del pipeline de producción — plano recurrente: «POV de la guitarra de Bocchi» | Misma fuente ✅ |
| — | (genérico) | **Claymation**: a Bocchi se le representa como una figura de plastilina sobre un tablero de **Monopoly**, para transmitir que siente su vida social como «un juego que no puede ganar» | [gamerant.com](https://gamerant.com/bocchi-the-rock-animation/) ✅; episodio exacto no confirmado (⚠️) |

- **Otras técnicas confirmadas de forma genérica** (sin episodio exacto
  todavía): **live-action** (metraje de imagen real intercalado),
  **minimalismo** (reducción a formas simples), estilo **grungy/tosco** — las
  tres citadas en el mismo artículo de gamerant.com, contrastado con
  screenrant.com y con TV Tropes (resumen vía buscador, ya que el fetch
  directo a tvtropes.org da 403 — ⚠️ anotado, dos intentos hechos, no insistí
  más según la regla de `AYUDANTE.md`) ✅.
- **Regla de tono declarada por el director** (aplica a TODOS los bajones):
  ni demasiado cómico ni demasiado serio — la clave para replicar el efecto en
  la lámina no es «hacer un chiste visual» sino cambiar de técnica manteniendo
  la emoción real de fondo.

### Cómo reproducirlo en Photoshop

- **Línea**: fina y de color oscuro pero NO negro puro sobre los personajes
  (según la filosofía de «menos líneas» de Kerorira: contorno limpio y
  económico, sin achurado interno). En Photoshop: pincel de tinta de borde
  duro, grosor 2-3 px a resolución 1080p, con «Bloquear píxeles
  transparentes» activado para rellenar planos.
- **Sombreado**: plano de 2 tonos (base + una sombra, sin degradado) en los
  personajes — coherente con el «cel shading» estándar de anime TV; los
  fondos, en cambio, son casi fotorrealistas con degradados suaves de luz de
  tarde (contraste declarado ya en la investigación previa de esta serie,
  `biblias/_ya_hechas/Bocchi the Rock.md` §4, con dos artículos de reseña
  como fuente) ⚠️ (fuente no vuelta a comprobar por mí esta vez).
- **Para el «bajón» de un fotograma fijo** (no una animación completa): elegir
  UNA técnica de la tabla de arriba y aplicarla sólo a Bocchi (nunca al fondo
  completo, que se mantiene realista) — así se logra el mismo choque visual
  que usa la serie. Ejemplo aplicable a Photoshop: filtro de pixelado
  (Mosaico) sólo en la selección del personaje + reducción de paleta a 16
  colores, para imitar el segmento de pixel art del episodio 6.
- **Filtros de postproducción**: grano de película ligero y viñeta suave son
  típicos del look general CloverWorks (dato genérico de producción anime TV,
  no confirmado con una fuente específica de Bocchi — ⚠️ no encontré un
  artículo técnico que lo detalle para esta serie en concreto; lo dejo como
  recomendación estándar, no como hecho verificado).

### Cómo reproducirlo en Blender

- **Contorno**: usar el modificador **Line Art** (Blender 3.x+) o, si el
  motor es Eevee sin Line Art, el método clásico **Solidify invertido**
  (grosor ~0.01, normales invertidas, material de contorno por
  `Material Offset`) — explicado paso a paso en
  [Instructables, «Custom Toon Shader in Blender»](https://www.instructables.com/Custom-Toon-Shader-in-Blender/) ✅
  y en [artisticrender.com/cel-shading-in-blender](https://artisticrender.com/cel-shading-in-blender/) ✅
  (dos fuentes, técnica genérica y bien documentada, no específica de Bocchi
  pero es el método estándar que cualquier render 3D de la serie tendría que
  usar).
- **Shader por celdas**: nodo **Diffuse BSDF → Shader to RGB → Color Ramp**
  (2-3 escalones de color) es el método recomendado en
  [StraySpark Studio, «How to Get an Anime/Toon Look in Blender»](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender) ✅
  — encaja con el sombreado plano de 2 tonos ya descrito arriba.
- **Modelos y rigs libres del personaje** (para posar sin animar desde cero):
  - **Kita Ikuyo, rig completo** (Blender 4.2.1, cuerpo entero riggeado) por
    **Hobbybird23** en Sketchfab — confirmado vía API de Sketchfab: licencia
    **CC Attribution-NonCommercial-NoDerivs**, descargable
    ([sketchfab.com/3d-models/kita-ikuyo-bocchi-the-rock-fe5a7f390ad5495cbbfe64d82cfba5a8](https://sketchfab.com/3d-models/kita-ikuyo-bocchi-the-rock-fe5a7f390ad5495cbbfe64d82cfba5a8))
    ✅ — sirve sólo como referencia de proporciones/pose, la licencia NC-ND
    no permite subirlo modificado ni comercialmente.
  - Otros modelos de Bocchi/Kita sueltos (no confirmados como riggeados) en
    Sketchfab, TurboSquid, CGTrader y DeviantArt (Patreon) — licencias mixtas,
    revisar una por una antes de usar ⚠️ no comprobé la licencia exacta de
    cada uno, sólo de la de Kita arriba.
- **Cámaras virtuales / mocap real** (visto en el punto de arriba): confirma
  que el estudio SÍ trabajó con datos de movimiento reales para las escenas de
  tocar instrumentos — un proyecto en Blender que busque el mismo realismo en
  los dedos sobre el mástil debería animar a mano sobre referencia de vídeo
  real de guitarra/bajo/batería, no sólo por ojo.

### Encuadres y composición

- **Plano recurrente confirmado**: «POV de la guitarra de Bocchi» en las
  escenas de concierto (cámara virtual 3D desde el punto de vista del propio
  instrumento) — [Sakuga Blog](https://blog.sakugabooru.com/2022/12/26/bocchi-the-rock-complete-production-notes-and-final-impressions/) ✅.
  Para la lámina: un encuadre bajo/cercano al instrumento (guitarra, bajo o
  batería) funciona como referencia de composición fiel a la serie.

**Segunda tanda (mirado con `fotogramas.py --cortes` sobre tráilers oficiales
de Dailymotion, ya que los 12 episodios completos siguen sin verse — YouTube
sigue pidiendo iniciar sesión)**: catalogado por emoción, con vídeo y minuto
(±2 s son la ficha de planos, no de memoria):

- **Pánico / bajón (ansiedad)**:
  - Primer plano extremo, dibujo deliberadamente **garabateado/fuera de
    modelo** (líneas temblorosas, proporciones rotas) cubriéndose media cara
    con el pelo: [Dailymotion x9696u6, plano 11, 0:13](https://www.dailymotion.com/video/x9696u6?t=13)
    ✅ (visto yo mismo, hoja 1 de `recap-mx/hojas`).
  - Ojos muy abiertos en primerísimo primer plano + texto en pantalla enorme
    superpuesto («I don't want to work, I'm scared! Society is scary!»):
    [x9696u6, planos 19-20, 0:27-0:28](https://www.dailymotion.com/video/x9696u6?t=27) ✅.
  - Silueta a contraluz tocando la guitarra sola en un cuarto oscuro (plano
    introspectivo/triste, cámara fija, sin música ni gente): [x9696u6, plano 21, 0:29](https://www.dailymotion.com/video/x9696u6?t=29) ✅.
  - **Tarjeta de personaje con distorsión tipo VHS/glitch** (líneas de escaneo,
    aberración cromática rosa neón, marco roto) para presentar a Bocchi, y la
    misma plantilla en amarillo para Nijika y en rojo para Kita — es la MISMA
    familia de «bajón» visual (quiebre de imagen) aplicada al grafismo del
    tráiler, no sólo a la animación: [Dailymotion x8esy25, plano 8, 0:11](https://www.dailymotion.com/video/x8esy25?t=11),
    [plano 28, 0:43](https://www.dailymotion.com/video/x8esy25?t=43) (Nijika),
    [plano 70, 1:40](https://www.dailymotion.com/video/x8esy25?t=100) (Kita) ✅
    (tres cartas vistas, mismo recurso con 3 personajes distintos → dos
    fuentes/casos cruzados dentro del propio material oficial).
- **Euforia de concierto**:
  - Silueta de cuerpo entero a contraluz con luces de escenario rojo/naranja
    muy saturadas, pelo en movimiento, plano bajo (la cámara mira hacia
    arriba): [x8esy25, planos 57-58, 1:20-1:21](https://www.dailymotion.com/video/x8esy25?t=80) ✅.
  - Primer plano de cantante con micrófono, boca abierta, mirada intensa hacia
    el público (no a cámara): [x9696u6, planos 61-63, 1:26-1:28](https://www.dailymotion.com/video/x9696u6?t=86) ✅.
  - Plano medio de dos personajes cantando muy cerca de un mismo micrófono,
    contraluz de neón rojo/azul con el letrero «STARRY» visible detrás:
    [x9696u6, plano 58, 1:22](https://www.dailymotion.com/video/x9696u6?t=82) ✅.
- **Ternura / cotidiano**:
  - Dos personajes de perfil, uno frente al otro, fondo de cielo estrellado
    difuminado (bokeh), plano medio simétrico, conversación íntima nocturna:
    [x9696u6, planos 70-71, 1:38-1:39](https://www.dailymotion.com/video/x9696u6?t=98) ✅.
  - Dos personajes sentados en juegos de resorte de un parque infantil
    (columpios de muelle), plano general, luz de atardecer cálida, figuras
    pequeñas en el encuadre: [x8esy25, planos 68-69, 1:38-1:39](https://www.dailymotion.com/video/x8esy25?t=98) ✅.
  - Bocchi sola de espaldas en el escenario vacío, foco único cenital, guitarra
    en alto: [x9696u6, plano 75, 1:45](https://www.dailymotion.com/video/x9696u6?t=105) ✅.
- **Vergüenza**:
  - Manos juntas en gesto de súplica, ojos cerrados, cabeza ligeramente
    inclinada, plano medio-corto: [x8esy25, plano 20, 0:33](https://www.dailymotion.com/video/x8esy25?t=33) ✅.
  - Primer plano con fondo de flores rosa desenfocadas, mirada de lado
    evitando cámara, negando avergonzada («I don't, actually»):
    [x8esy25, plano 42, 1:03](https://www.dailymotion.com/video/x8esy25?t=63) ✅.
- **Comedia / deformación** (para variar del «bajón» serio): reacción
  exagerada con cara aplastada/arrugada y onomatopeya en pantalla («キター!»),
  primer plano muy cerrado: [x9696u6, planos 29-30, 0:36-0:37](https://www.dailymotion.com/video/x9696u6?t=36) ✅.
  Símbolo de emoción simplificado: rayitas onduladas junto a la cabeza para
  indicar apuro/desánimo cómico (chiste de «estoy en bancarrota»): [x8esy25,
  plano 61, 1:26](https://www.dailymotion.com/video/x8esy25?t=86) ✅ — vocabulario
  de expresión útil para el punto 17 (guía de IA de imagen).

**La OVA/AMV de Internet Archive (`youtube-MWsCjdC6Siw`, «secret OVA: Rabbit
Hole Side Concert»)**: revisada de nuevo a propósito con `fotogramas.py`. El
primer fotograma (0:00) sí muestra un rótulo real de la serie, el banner
**«第◯回 秀華祭»** (festival cultural Shūka) que también aparece en el tráiler
oficial ([x9696u6, plano 60, 1:24](https://www.dailymotion.com/video/x9696u6?t=84))
✅ — coincide. Pero el resto del vídeo (0:12 en adelante) mezcla ese arranque
con métricas ajenas a Bocchi the Rock: un perrito caliente/corndog de un meme
distinto, una barra de vida con texto en japonés no relacionado, y una
secuencia tipo formulario web repetido «Rabbit Hole… YES» — la descripción del
propio ítem lo confirma: es un **AMV/音MAD de fans** (Blender + Krita,
canción de DECO\*27) que **remezcla** clips reales con material ajeno, no
metraje limpio de un episodio. **No lo uso como fuente de encuadre** más allá
del primer fotograma (festival), para no mezclar planos inventados con planos
reales — ya lo había marcado en «No encontré» de la primera tanda y se
mantiene la misma conclusión, ahora comprobada por segunda vez.

### Hallazgo visual propio: menú del Blu-ray oficial (vol. 1), mirado con fotogramas.py

Vídeo real mirado (no de memoria): **Internet Archive**,
[«Opening/Closing To Bocchi the Rock! Vol.1 2022 Blu-ray (Japanese Copy)»](https://archive.org/details/opening-closing-to-bocchi-the-rock-vol.-1-2022-blu-ray-japanese-copy)
(1920×1080 original, 102 s — resulta ser el **menú del disco**, no el
OP/ED en sí; igual de útil para tipografía). Extraje fotogramas con
`fotogramas.py --cada 5` (21 fotogramas, hoja de contacto) y dos en grande a
1280×720 con `--fotograma 55 75`, y medí color con `estilo.py`:

- **0:55 — cartela de episodio, formato «ticket de concierto» inclinado**:
  fondo magenta **`#D10249`** (26.0% de la imagen, medido con `estilo.py`) con
  **«BOCCHI THE ROCK!»** en bloque blanco, condensado, mayúsculas, muy grueso
  — **coincide visualmente con Anton** (ya recomendada en la tabla del punto
  5) ✅ confirmado con imagen oficial propia, no de memoria. A la derecha,
  franjas blancas con **«＃０３»** y el título del episodio en japonés
  **escrito a mano con marcador** (trazo de pincel real, no tipografía
  digital) — así se ve el patrón de «rotulador a mano para texto japonés»
  descrito en el punto 5 en un caso real y oficial.
- **1:15 — menú de selección de episodio, «BACK STAGE PASS»**: dos carnets
  estilo pase de backstage, uno rosa (**`#D83D6D`**, medido) para el episodio
  1 y uno ámbar/dorado (**`#EEAB1B`**, medido) para el episodio 2, con
  **«BACK STAGE PASS»** en el mismo tipo de letra de bloque condensado en
  itálica — refuerza **Anton** o una variante inclinada como letra libre para
  rótulos de concierto/backstage. El número de episodio (`＃01`, `＃02`) y el
  título japonés van también a mano, en marcador negro sobre recuadro blanco.
  La portada del volumen 1 a la izquierda combina **dos familias en el mismo
  logo**: «BOCCHI» en bloque grueso + «the Rock!» en **script cursivo fino**
  — confirma independientemente el patrón de «cada portada mezcla letras muy
  distintas» ya visto en instafonts.io (punto 5) ✅ dos fuentes distintas
  llegando al mismo patrón.
- **Estilo medido** (`estilo.py`): sombreado mixto/degradado, saturación
  30-33%, brillo 77-80%, línea de contorno rosa/vino (`#CD457A`, `#B26F68`) en
  vez de negro puro — coincide con la idea de «línea económica, no negro
  puro» que dijo Kerorira sobre los personajes (arriba), extendida aquí
  también al diseño gráfico de menús.
- Vídeo local borrado tras sacar los fotogramas (regla del disco compartido).

## Hallazgos · Punto 24 — Obras parecidas y temas relacionados

- **Lista base ya reunida en `partes/datos-texto.md`** (AniList, recomendaciones
  de usuarios, sin repetir la consulta): K-On! (1196 votos), Girls Band Cry
  (507), Hitoribocchi no Marumaruseikatsu (402), Laid-Back Camp (240),
  Jellyfish Can't Swim in the Night (229), WataMote (187), Nichijou (139),
  BanG Dream! It's MyGO!!!!! (120), Sound! Euphonium (112), Comic Girls (85),
  BanG Dream! (77) ✅ (AniList, dato ya recogido).
- **El propio director confirma K-On! como influencia directa y consciente**,
  no sólo parecido temático — cita textual en el «1st Bocchi Guidebook»: la
  vio en el instituto y quiso que Bocchi the Rock quedara en el corazón de la
  audiencia igual que K-On! 10 años después. Confirmado en **dos idiomas**:
  inglés ([Anime News Network](https://www.animenewsnetwork.com/interview/2024-07-12/bocchi-the-rock-staff-reflect-on-growth-and-change/.213092))
  y resumen en coreano citando la misma declaración
  ([namu.wiki](https://namu.wiki/w/%EB%B4%87%EC%B9%98%20%EB%8D%94%20%EB%A1%9D!/%EC%95%A0%EB%8B%88%EB%A9%94%EC%9D%B4%EC%85%98))
  ✅.
- **Diferencia clave con K-On! (para no repetir la lámina), según fuente
  coreana**: K-On! es una obra de «chicas monas» con música como condimento
  ligero (club escolar); Bocchi the Rock! trata la música y la comedia con más
  peso real, centrada en la escena de *live house* en vez del club — fuente:
  [namu.wiki, comparación](https://namu.wiki/w/%EC%9C%A0%EC%82%AC%ED%95%9C%20%EB%A7%8C%ED%99%94&%EC%95%A0%EB%8B%88%EB%A9%94%EC%9D%B4%EC%85%98) ✅.
- **Otras influencias/parecidos citados por Wikipedia** (misma editorial
  Houbunsha, o influencia de diseño de personajes): **Beck** (manga de
  músicos) y **Comic Girls** (parecido en diseño de personajes) —
  [en.wikipedia.org/wiki/Bocchi_the_Rock!](https://en.wikipedia.org/wiki/Bocchi_the_Rock!)
  ⚠️ una sola fuente, no repetida en una segunda.
- **Este servidor YA tiene una lámina de K-On!** (`biblias/10-k-on/`, canal
  **#general**, con 3 conceptos: mesa del té del club, MC de festival/Budokan
  y tablón de la escalera) — para que el redactor NO repita esos 3 conceptos
  en Bocchi the Rock. Datos propios, revisando el repositorio del equipo ✅.
- **Parodias/homenajes dentro de la propia serie** (cruce entre puntos 18 y
  24 — la serie referencia activamente otras obras, no sólo se parece a
  ellas): Ashita no Joe (ep. 8), Dragon Ball/pose de Yamcha (ep. 9), Neon
  Genesis Evangelion (ep. 10, ≈04:01), Minions (ep. 7, segmento «Munions»),
  Boys Over Flowers/Hana Yori Dango (ep. 7) — mismas fuentes que el punto 18
  ✅/⚠️ (ver tabla).

## Hallazgos · Punto 25 — El mundo, la historia y sus símbolos

**El mundo, en 5 líneas**: Tokio actual y real (sin fantasía). El barrio de
**Shimokitazawa** (Setagaya) es el centro: calles de tiendas de segunda mano,
cafés y **live houses** (salas de conciertos pequeñas, en sótano) — el destino
de peregrinaje real de los fans ✅. La protagonista es una adolescente
introvertida que quiere unirse a una banda de rock para dejar de estar sola.
Confirmado con dos fuentes: [Wikipedia](https://en.wikipedia.org/wiki/Bocchi_the_Rock!)
y `partes/datos-texto.md` (sinopsis AniList) ✅.

- **STARRY**, el *live house* donde ensaya y toca Kessoku Band, está basado en
  un local real de Shimokitazawa llamado **Shelter** — dato ya confirmado en
  la investigación previa de esta serie (`biblias/_ya_hechas/Bocchi the
  Rock.md` §7, con Tokyo Weekender y Voyapon como fuentes) ✅ dos fuentes
  (no las repetí, ya estaban verificadas).
- **Kessoku Band (結束バンド)**, el nombre de la banda, es un **juego de
  palabras real**: «結束バンド» es literalmente el nombre japonés de una
  **brida/precinto de cables (cable tie)** — el nombre lo puso **Ryo Yamada**
  dentro de la ficción, y el chiste se confirma en dos sitios: el propio
  episodio 4 (Ryo hace merchandising literal de bridas de cable para la
  banda, `partes/datos-texto.md`→ wikitext de «Jumping Girl(s)» ya citado en
  punto 6) y un artículo de análisis de la letra del disco debut
  ([mikiki.tokyo.jp](https://mikiki.tokyo.jp/articles/-/33283)) ✅ dos
  fuentes.
- **Los nombres de los 4 miembros vienen de Asian Kung-Fu Generation**: dato
  ya confirmado por la propia wiki (Trivia de «Eight Views», ya citado en
  punto 18: «the band who sung the song and is the source of all Kessoku Band
  members' names, was formed in the Kanazawa Hakkei Campus...») ✅.
- **Objeto icónico #1 — la caja de mangos («Mango Mask»)**: confirmada en el
  episodio 1 y en la ficha de Hitori Gotoh de la wiki (ya resuelto en la
  investigación previa; **no es una confusión**, existe de verdad) ✅.
- **Objeto icónico #2 — el carnet/ticket de concierto**: visto directamente
  en el menú oficial del Blu-ray (punto 18 arriba) — el formato «ticket
  inclinado + BACK STAGE PASS» es la identidad gráfica oficial de la propia
  editorial del disco, sirve como vocabulario visual reconocible para
  cualquier pieza gráfica de la serie (carteles de concierto, entradas,
  pases) ✅ (visto yo mismo).
- **Isosta (Issta)**: parodia de Instagram dentro del mundo de la serie, la
  red social que usan los personajes en pantalla — confirmado en dos fuentes
  cruzadas ya citadas en el punto 6 (wikitext + cuenta oficial de Instagram
  real `@BTR_isosta`, que TOMA el nombre de la parodia) ✅.
- **Historia por arcos (temporada 1, 12 episodios)**, reconstruida con la
  lista oficial de episodios (Wikipedia ✅) y las sinopsis/tramas ya miradas
  en la wiki de Fandom para los episodios 1, 4, 6 y 7 (arriba):
  1. **Formación** (ep. 1-3): Bocchi, guitarrista solitaria que sólo toca sola
     y sube vídeos como «Guitarhero», es reclutada por Nijika (baterista,
     líder) para Kessoku Band tras faltar su guitarrista original; primer
     concierto en STARRY dentro de la caja de mangos.
  2. **La banda se asienta** (ep. 4-6): se suma Kita (ex-popular del insti,
     ahora vocalista/guitarra rítmica); ensayos, primeras canciones propias,
     merchandising casero, primeras ventas de entradas (con la espiral en
     pixel art del ep. 6).
  3. **Verano y crecimiento personal** (ep. 7-9): typhoon/casa de Bocchi,
     festival escolar, encuentro con **Kikuri Hiroi** (bajista adulta,
     borracha, de otra banda — personaje secundario muy querido) en Enoshima.
  4. **Clímax y cierre** (ep. 10-12): tensiones y decisión de tocar en serio,
     concierto final en STARRY, título del episodio 12 «Kimi ni Asa ga Furu»
     (La luz de la mañana cae sobre ti) — cierre emocional de la temporada.
  ⚠️ Reconstrucción propia a partir de fichas de episodio y sinopsis oficial
  (bocchi.rocks/story), sin haber visto los 12 episodios completos por el
  bloqueo de YouTube — el investigador de vídeo o quien vea los episodios
  completos debería confirmar/ampliar esta división por arcos.
- **Vocabulario propio que un fan reconoce al instante**: «Bocchi-chan»
  (apodo), «Mango Mask» (マンゴー仮面), «Guitarhero» (su alias de subida de
  vídeos), «Isosta/Issta» (red social parodia), «結束バンド» = Kessoku Band
  (chiste de la brida de cable), «STARRY» (la sala), «Kessoku Band ZEPP
  TOUR» / «Re:Kessoku Band» (nombres de eventos reales de la banda ficticia,
  ya en `partes/datos-texto.md` vía la búsqueda de «collaboration» en la
  wiki) ✅.

## Lo mejor para la lámina

1. El **ticket/pase de concierto inclinado, magenta `#D10249`**, con «BOCCHI
   THE ROCK!» en bloque grueso (letra libre: Anton) y el número/título a mano
   — visto en el menú oficial del Blu-ray vol. 1, listo para un cartel dentro
   del canal.
2. El **bocadillo «roto»/glitcheado** como traducción fiel de los bajones de
   Bocchi (en vez de una burbuja blanca genérica) — con la tabla de 8 técnicas
   distintas por episodio para variar sin repetirse.
3. El **cable tie/Kessoku Band** como chiste visual con base real (una brida
   de verdad) para un objeto 3D en Blender.
4. Rig libre de **Kita** en Sketchfab (Blender 4.2.1) como referencia de
   proporciones/pose.
5. La frase de cierre de episodio (**ending quote**) atribuida a un personaje
   como plantilla de cuadro de diálogo «propio de la serie».

## No encontré

- **Capturas de pantalla directas de la interfaz de Kirara Fantasia o
  Kotodaman** durante la colaboración con Bocchi the Rock: confirmé que
  ambos juegos/colaboraciones existen (con fuentes oficiales y de fans), pero
  no pude extraer URLs de imagen servibles — Kirara Fantasia cerró en 2023 y
  su wiki de fans dio HTTP 402 al leerla; las imágenes de Kotodaman están en
  rutas con hash sin vista directa. ⚠️ Búsquedas hechas: «Kirara Fantasia
  Bocchi the Rock screenshot UI» (inglés), «ことダマン ぼっち・ざ・ろっく コラボ
  画面» (japonés). Es un extra sobre lo obligatorio del punto 11 (ya
  confirmé qué juegos existen y cómo funcionan por texto), no lo bloqueante.
- **El ítem de Internet Archive "Bocchi The Rock! Episode 11 secret OVA"**
  (`archive.org/details/youtube-MWsCjdC6Siw`) resultó ser, al mirarlo con
  `fotogramas.py`, un **AMV/音MAD hecho por fans** (remix con Blender/Krita
  sobre clips de OTRAS obras y memes, música de DECO*27) y NO metraje oficial
  del episodio 11 — el título en Archive.org es engañoso. Lo anoto para que
  nadie más lo use como fuente de escenas canon.
- **Encuadres y composición típicos por emoción** (parte del punto 18): sólo
  confirmé un plano recurrente documentado (POV de la guitarra en directos).
  No pude ver los 12 episodios completos porque YouTube pidió iniciar sesión
  todo el rato de trabajo y no encontré los episodios completos (sólo
  tráilers) en Dailymotion (comprobado con la API directa de Dailymotion,
  `api.dailymotion.com/videos?search=...`) ni en Internet Archive (el único
  vídeo oficial 1080p disponible es el menú del Blu-ray, no un episodio).
  Esto es territorio del investigador de vídeo, que sí tiene puntos 2/4/9/10
  y acceso a `episodio.py`; lo dejo anotado como pendiente real, ver
  «Sigue:».
- **TV Tropes, fetch directo**: da HTTP 403 (dos intentos con distinto
  User-Agent, y el Wayback Machine no tiene copia archivada de esa URL
  concreta) — usé el resumen que da el propio buscador web sobre esa página en
  su lugar (con las citas ya puestas arriba), suficiente para los datos que
  necesitaba pero sin poder citar el texto exacto línea por línea.
- **TCRF (The Cutting Room Floor)**: no aplica — no hay videojuego propio de
  Bocchi the Rock con contenido descartado que catalogar (confirmado: no
  existe un juego dedicado, sólo 2 colaboraciones dentro de juegos ya
  existentes, ver punto 11).
- **Wayback Machine**: no hizo falta usarlo para páginas borradas — no
  encontré ninguna página necesaria que hubiera desaparecido (todas las
  fuentes usadas siguen activas).

## Bitácora de búsqueda

**Buscador web** (WebSearch), 14 búsquedas usadas de ~50:
1. «Bocchi the Rock animation style change anxiety claymation rotoscope interview» (en)
2. «Bocchi the Rock Keiichiro Saito director interview animation technique» (en)
3. «ぼっち・ざ・ろっく 斎藤圭一郎 インタビュー 演出 妄想» (ja)
4. «Bocchi the Rock font logo typeface identification» (en)
5. «ぼっち・ざ・ろっく 4コマ 漫画 吹き出し スタイル まんがタイムきらら» (ja)
6. «"Bocchi the Rock" manga preview pages read online official sample» (en)
7. «Kirara Fantasia Bocchi the Rock collaboration screenshot UI» (en)
8. «ことダマン ぼっち・ざ・ろっく コラボ 画面» (ja)
9. «Bocchi the Rock Blender rig model free download fan» (en)
10. «Bocchi the Rock Photoshop brush toon shader recreate style tutorial fan art» (en)
11. «Blender anime toon shading tutorial Line Art modifier Shader to RGB cel shading guide» (en)
12. «"Bocchi the Rock" TV Tropes "Art Shift" claymation rotoscoping site:tvtropes.org» (en)
13. «Bocchi the Rock episode 6 pixel art dog concert tickets scene minute» (en)
14. «Bocchi the Rock parody references episode Evangelion Perfect Blue Attack on Titan homage art style» (en)
15. «결속밴드 이름 유래 멤버 한자» → «結束バンド 名前 由来 メンバー 漢字 一文字» (ja)
16. «고독한 록 봇치 애니메이션 스타일 영향 유사 작품» (ko)
17. «"Bocchi the Rock" Groove Coaster OR "Project Sekai" OR "太鼓の達人" collaboration game» (en)

**Red directa** (curl/Python, sin pasar por el buscador):
- API de Fandom `bocchi-the-rock.fandom.com/api.php` — búsqueda de texto
  («video game», «smartphone», «collaboration») y `action=parse&prop=wikitext`
  de 5 páginas de episodio (Jumping Girl(s), Eight Views, To Your House,
  Lonely Rolling Bocchi, Bocchi the Rock (episode), Morning Light Falls on
  You) — todas en inglés (la wiki está en inglés).
- Wikipedia (`en.wikipedia.org/wiki/Bocchi_the_Rock!`,
  `List_of_Bocchi_the_Rock!_episodes`) vía WebFetch.
- Sakuga Blog (`blog.sakugabooru.com`), 2 artículos completos vía WebFetch.
- `bocchi.rocks/special/zadankai/` (sitio oficial japonés) vía WebFetch.
- Wikimedia Commons (ficha del logo SVG) vía WebFetch; descarga directa del
  SVG dio HTTP 429 dos veces (rate limit) — no insistí más.
- API de Sketchfab (`api.sketchfab.com/v3/models/...`) para confirmar
  licencia y si es descargable del rig de Kita.
- API de AnimeThemes: **HTTP 522 caído**, igual que ya avisaba
  `datos-texto.md` — no se pudo usar en ningún momento de esta sesión.
- API de Internet Archive (`archive.org/metadata/...`) para 3 ítems, y
  `fotogramas.py`/`estilo.py` sobre el vídeo del menú del Blu-ray oficial
  (21 fotogramas + 2 en grande + medición de color) y sobre el AMV de fans
  (9 fotogramas, descartado por no ser contenido oficial).
- API de Dailymotion (`api.dailymotion.com/videos?search=...`) para confirmar
  que no hay episodios completos, sólo tráilers.
- `note.com` (análisis japonés de tipografía de globos en Manga Time Kirara)
  vía WebFetch.
- Google Fonts (`fonts.googleapis.com/css2`), 9 fuentes descargadas y
  comprobadas con **fontTools** (`TTFont(f).getBestCmap()`) para á é í ó ú Á
  ñ Ñ ¿ ¡ — las 9 completas.
- TV Tropes: 403 directo (WebFetch y curl con User-Agent de navegador); sin
  copia en Wayback Machine para esa URL — usado el resumen del buscador en su
  lugar, con las citas ya puestas en el texto.

Sigue: ver «encuadres y composición por emoción» (punto 18) con episodios
completos en cuanto se pueda acceder a YouTube o aparezcan en Dailymotion/
Internet Archive — es el único hueco obligatorio que queda del punto 18; el
resto de puntos (5, 6, 11, 24, 25) están completos con fuentes dobles donde
fue posible.
