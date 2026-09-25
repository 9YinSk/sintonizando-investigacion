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
- No pude ver los 12 episodios completos para catalogar ángulos por emoción de
  forma exhaustiva (YouTube pide login; el vídeo del Blu-ray en Internet
  Archive sólo cubre el OP/ED, 102 s) — **esto queda pendiente**, ver
  «Sigue:» al final.
