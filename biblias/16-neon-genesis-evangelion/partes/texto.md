# Parte de TEXTO, JUEGOS Y TÉCNICA · Neon Genesis Evangelion (repaso)

Investigador de texto, EQUIPO.md. Puntos 5, 6, 11, 18, 24 y 25 de ENCARGO.md.
Modo **repaso**: `biblia.md` (hecho antes del 24-sep-2026) ya tiene los puntos
5, 6 y 11 muy trabajados (secciones antiguas «6 · Tipografía», «7 · Cómo
hablan…» y «13 · Videojuegos»). Los puntos 18, 24 y 25 **no existen** en
`biblia.md`: son los «añadidos el 24-sep» (COMPLEMENTO.md). Esta parte
confirma lo dudoso de 5/6/11 y escribe de cero 18, 24 y 25.

## 5 · Tipografía

Ya está muy hecho en `biblia.md` §6 (Matisse EB/UB, Helvetica, Times
comprimida, Chicago, 12 letras libres de Google Fonts comprobadas con
fontTools, todas OFL). Sólo añado lo que faltaba.

- **Chicago (números de los monolitos de SEELE) comprobado con fontTools**:
  bajé `ChiKareGo2.woff` (recreación libre de Chicago, licencia **Creative
  Commons** ⚠️ una fuente) y le pasé `TTFont(f).getBestCmap()` yo mismo.
  Resultado real, carácter por carácter: **trae** á é í ó ñ Ñ Á É Í Ó Ú Ü ¿ ¡ ·
  **le faltan** ú y ü (minúsculas) ✅ (comprobado con fontTools,
  [fuente del .woff en GitHub](https://github.com/lowercasename/helloedit/blob/master/resources/fonts/ChiKareGo2.woff),
  descripción de la fuente en [suppertime.co.uk](http://www.suppertime.co.uk/blogmywiki/2017/04/chicago/)).
  Esto **resuelve el ⚠️** que dejó la primera pasada («no lo comprobé»): sí
  sirve para el número del monolito («SEELE 01», «02»…, todo mayúsculas), pero
  si un texto necesita «ú» o «ü» en minúscula hay que evitar esta letra o
  ponerla en VERSALITAS.
  · fuente(s): GitHub (helloedit/ChiKareGo2.woff), suppertime.co.uk · ✅ · —

## 6 · Cómo hablan y piensan en pantalla

También muy hecho en `biblia.md` §7 (cartela negra, pantallas de NERV,
monolitos SOUND ONLY, logo NERV, avance del próximo episodio). Añado lo que
quedó ⚠️ o sin mirar.

- **El manga (Sadamoto) no tiene un globo propio reconocible**, confirmado de
  nuevo: la crítica que lo analiza habla de su **composición de viñetas**
  (paneles que se estrechan hacia el centro para forzar la mirada al Eva,
  bordes afilados que repiten la línea «arrugada» de su dibujo) pero **no
  describe un bocadillo especial**; usa el bocadillo redondo estándar del
  manga con texto japonés vertical ⚠️ (una fuente de análisis, sin ver la
  página) · [aiptcomics: «Revisiting Sadamoto's Evangelion Manga»](https://aiptcomics.com/2021/02/04/revisiting-sadamotos-evangelion-manga-p1/)
  · ⚠️ · —. **Sigue pendiente ver una página real** (lo hace el investigador
  de imagen, con hojas de la wiki del manga).
  · fuente: aiptcomics · ⚠️ · —

## 11 · Videojuegos de la franquicia

`biblia.md` §13 ya tiene la tabla de juegos (Girlfriend of Steel, Ayanami
Raising Project, Shinji Ikari Raising Project, *Cross Reflections*…) con la
nota «no vi capturas de sus cajas de diálogo. TCRF no respondía». Lo comprobé
otra vez con **The Cutting Room Floor** (mi tarea específica) y con Wayback.

- **TCRF sí tiene páginas de Evangelion**, pero **bloquea curl y el
  navegador sin ventana** (Cloudflare; también me bloqueó a mí con
  `net::ERR_CERT_AUTHORITY_INVALID` en TCRF **y en TV Tropes**: parece un
  fallo del proxy con el certificado de Cloudflare para todo el contenedor,
  no sólo TCRF). Wayback Machine también falló de forma repetida al bajar
  esas páginas archivadas (`ws_closed_mid_exchange`, fallo del túnel, no del
  sitio: lo dejo anotado para que el jefe o un repaso posterior lo reintente).
  Aun así, **confirmo que las páginas existen** (por el resumen del buscador,
  no por la página abierta):
  - [`Neon_Genesis_Evangelion:_Koutetsu_no_Girlfriend_(PlayStation)`](https://tcrf.net/Neon_Genesis_Evangelion:_Koutetsu_no_Girlfriend_(PlayStation))
    (*Girlfriend of Steel*, PS1, 1998): «material de depuración» (*debugging
    material*) ⚠️ (resumen de búsqueda, no la página).
  - [`Shin_Seiki_Evangelion:_Koutetsu_no_Girlfriend_Special_Edition_(PlayStation_2)`](https://tcrf.net/Shin_Seiki_Evangelion:_Koutetsu_no_Girlfriend_Special_Edition_(PlayStation_2))
    (*Special Edition*, PS2, 2006-2007, TamTam/GeneX): texto de desarrollo
    oculto y **gráficos sin usar** ⚠️ (resumen de búsqueda).
  - Copias en Wayback confirmadas por `archive.org/wayback/available` (no
    pude abrirlas): [PS1 (23-ago-2025)](http://web.archive.org/web/20250823031232/https://tcrf.net/Neon_Genesis_Evangelion:_Koutetsu_no_Girlfriend_(PlayStation)),
    [PS2 SE (26-ago-2025)](http://web.archive.org/web/20250826032103/https://tcrf.net/Shin_Seiki_Evangelion:_Koutetsu_no_Girlfriend_Special_Edition_(PlayStation_2)).
  · fuentes: TCRF (por resumen de búsqueda) + Wayback (existencia confirmada) · ⚠️ · —
- **No hay página de TCRF** para *Shinji Ikari Raising Project* ni para
  *Ayanami Raising Project*: sólo Wikipedia y EvaWiki las documentan (ya en
  `biblia.md`). No lo encontré, busqué «"Cutting Room Floor" Evangelion
  Shinji Ikari Raising Project» en inglés.
- **Interfaz confirmada por descripción, no por captura**: *Girlfriend of
  Steel* y sus secuelas son **novelas visuales** (texto sobre fondo con
  retrato del personaje, caja de diálogo inferior, como toda *visual novel*
  de la época) ⚠️; *Ayanami/Shinji Raising Project* son de **cría** (menú
  semanal con estadísticas, más parecido a una hoja de cálculo con retrato)
  ⚠️. Sigue sin haber una captura verificada: **usa la cartela y la pantalla
  de NERV de la serie (punto 6) para la lámina**, como ya dice `biblia.md`.
  · fuentes: Wikipedia (EN) de cada juego, EvaWiki · ⚠️ · —

## 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Rigs y tramas: ver puntos 3 y 19** (modelos 3D, rigs libres y texturas de
trama las trae el investigador de imagen). Aquí sólo la técnica y cómo
reproducirla en Photoshop y Blender.

### 18.1 Cómo se hizo la serie (según entrevistas y análisis)

- **Animación limitada a propósito, no sólo por presupuesto**: los primeros
  episodios (combates mecha) se llevaron gran parte del presupuesto; hacia el
  final, la clave de animación de algunos capítulos se hizo en **3 semanas**
  y Anno recurrió a **fotogramas fijos sostenidos como si fueran un plano de
  cámara detenida** (el ascensor con Rei y Asuka; Unit-01 sosteniendo a
  Kaworu). Hay debate de si fue presupuesto o **tiempo**, pero ambas fuentes
  coinciden en el resultado visual: quietud como recurso dramático, no sólo
  ahorro ⚠️ (dos fuentes que se citan entre sí: [CBR](https://www.cbr.com/neon-genesis-evangelion-other-anime-ran-out-of-budget-quality-decline/),
  [foro EvaGeeks «Did Evangelion really run out of budget?»](https://forum.evageeks.org/thread/19083/Did-Evangelion-really-run-out-of-budget/)).
- **Animación por capas densas en las escenas de acción**: animadores clave
  como **Mitsuo Iso** superponían muchas capas de línea para dar movimiento
  «orgánico» a los Eva (no rígido como un robot normal) ⚠️ (una fuente,
  resumen de búsqueda sin acceso a la entrevista original).
- **Maquetas físicas** de General Products (la tienda de *garage kits* de
  Gainax) se usaban de referencia de luz, pose y perspectiva al hacer el
  storyboard ⚠️ (una fuente).
- **Composición: el «vocabulario compositivo» de Anno** (análisis de
  aficionados especializados, no entrevista directa, pero muy citado):
  - **Primer plano de la parte del cuerpo que actúa** (una mano en el
    interruptor, un pie en el pedal) en vez de mostrar a la persona entera.
  - **Corte de la conversación al objeto del que se habla**: alguien nombra
    algo y el siguiente plano ES ese algo.
  - **Sobre-el-hombro «aislante»**: primer plano y fondo en tensión de
    tamaño o de luz para marcar la distancia emocional entre los dos.
  - Fuente: [AnnoCinema (Medium): «Anno's Compositional Vocabulary»](https://medium.com/@annocinema/annos-compositional-vocabulary-f28ef87d45f7)
    y su blog de análisis en [Tumblr](https://annocinema.tumblr.com/post/159747328453/a-type-of-shot-that-anno-uses-in-all-of-his-works)
    ⚠️ (análisis de fans, coincide entre las dos, no es entrevista al staff).
- **Línea de Sadamoto** (diseño de personajes, y dibujante del manga): línea
  **«arrugada» (crinkled), afilada pero orgánica**, curva las líneas de
  movimiento para dar dinamismo ⚠️ (una fuente, [aiptcomics](https://aiptcomics.com/2021/02/04/revisiting-sadamotos-evangelion-manga-p1/)).
- **Sombreado de la serie de TV**: **plano por capas** (cel clásico de 1995,
  sin degradado real, sombra dura con un solo tono más oscuro) con **grano
  de película** y **aberración/artefactos** en los cortes de la mente
  (episodios 25-26) — descripción de memoria de lo ya mirado por el equipo de
  vídeo en fotogramas.py ⚠️; el investigador de imagen mide el hex exacto.

### 18.2 Cómo reproducirlo en Photoshop

1. **Línea**: pincel de tinta duro (0-2 px de *jitter*), color **no negro
   puro**: un gris muy oscuro o un tono cercano al de la sombra (así hacía el
   cel clásico). Capa de línea en **Multiplicar**, encima del color.
2. **Color**: **una** capa base plana por zona (piel, pelo, plugsuit), sin
   degradado; capa de **sombra** en **Multiplicar** con un solo tono más
   oscuro y **bordes duros** (no difuminados) — así se ve el cel de los 90,
   no el anime moderno con degradados suaves.
3. **Grano de película**: capa nueva llena de blanco → `Filtro > Ruido >
   Añadir ruido` (25-30 %, uniforme, monocromático) → modo **Multiplicar**,
   opacidad 15-30 %. Es el «noise + multiply» que usan los tutoriales de
   *cel look* ([guía en zombiebass.portfolio.site](https://zombiebass.portfolio.site/anime-cel-tutorial),
   [MicahBuzan.com «Cel Shading Tutorial»](https://www.micahbuzan.com/cel-shading-tutorial/)).
4. **Orden de capas** recomendado por esas mismas guías: fondo → color base →
   luces → sombras → **línea** → texto/decals → grano encima de todo, en
   Multiplicar.
5. **Para las pantallas de NERV** (punto 6): capa de **glow** verde/naranja
   en modo Trama de color o Lineal-Dodge sobre fondo negro, más una trama de
   **scanlines** (líneas horizontales finas al 10 % de opacidad) para el
   efecto CRT de 1995.
   · fuentes: MicahBuzan.com, zombiebass, [Adobe: «Cel Shading — A
   Comprehensive Guide»](https://www.adobe.com/uk/creativecloud/animation/discover/cel-shading.html)
   · ⚠️ (técnica general de cel-shading, no un tutorial oficial de Eva) · —

### 18.3 Cómo reproducirlo en Blender

1. **Contorno**: dos formas equivalentes, ambas gratis en Blender:
   - **Modificador Solidify** con grosor pequeño en negativo, normales
     invertidas (*Flip Normals*) y un material plano negro con
     *Backface Culling* activado (el truco clásico de contorno barato).
   - **Grease Pencil → Line Art** (moderno, no necesita activar Freestyle;
     da más control de grosor por objeto) o **Freestyle** clásico en
     `Propiedades de render`.
   · fuente: [«Outlines in Blender»: Freestyle, Line Art y Inverted Hull](https://www.youtube.com/watch?v=cO4BDrdUHc0),
   [StraySpark: «How to Get an Anime/Toon Look in Blender»](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender)
   ⚠️ (tutoriales generales, no específicos de Eva) · —
2. **Sombreado tipo cel**: nodo **Shader to RGB** → **Color Ramp** en modo
   **Constante** (no lineal): con **dos** paradas sale el clásico luz/sombra
   de dos tonos; con **tres**, un tono medio (más parecido al cel plano de la
   serie de 1995, que casi no usa medios tonos). Motor **EEVEE** (tiempo
   real) con `Color Management > View Transform: Standard` (si no, Blender
   suaviza los cortes y se pierde el look plano).
   · fuente: mismos tutoriales de arriba · ⚠️ · —
3. **Render final**: pasa el render por **Compositor** y añade grano
   (`Filter Glare` + un nodo de ruido) para igualar el grano de película de
   la serie, igual que en el flujo de Photoshop del punto 18.2.
4. **Qué programas usó el propio estudio** (para que quede claro que Blender
   es *nuestra* forma de reproducirlo, no la original): en 1995 Gainax **no**
   usaba Clip Studio ni Toon Boom (no existían aún); era **cel tradicional +
   fotografía con cámara de tinta y grano de película real**, con retoques
   digitales incipientes en escenas puntuales (los créditos y algunos
   *glitches* mentales) ⚠️ (de memoria del equipo, sin entrevista concreta
   de producción digital de NGE; **no encontré** una fuente que diga qué
   programa exacto usaron para los pocos efectos digitales de 1995-96).

## 24 · Obras parecidas y temas relacionados

### 24.1 Influencias que el propio Anno reconoce (verificado en japonés)

- **Ultraman**: Anno dijo en público que la idea de los Ángeles como
  «alienígenas» le vino de ver, en el manga *BASTARD!! -暗黒の破壊神-*, a un
  ángel **con cara de Ultraman**, y pensó «¡así que Ultraman era un ángel!»
  ✅ (citado igual en dos blogs japoneses de análisis:
  [500type-eva.jp](https://www.500type-eva.jp/evangelion-ultraman-relationship-explained/),
  [evamania.net](https://evamania.net/archives/1833)). Es una anécdota muy
  repetida en el fandom japonés, con la misma redacción en varias fuentes.
- **Space Runaway Ideon** (伝説巨神イデオン, Yoshiyuki Tomino, 1980-81):
  homenaje directo. El final de **The End of Evangelion** («Magokoro wo,
  Kimi ni») es una **parodia del final de «Ideon: Be Invoked»** (ambos:
  destrucción total y renacimiento cósmico) ✅ (buscado en japonés,
  coincide en [chiebukuronews.blog.jp](https://chiebukuronews.blog.jp/archives/31803850.html)
  y [ameblo.jp: «エヴァに影響を与えた…イデオン»](https://ameblo.jp/maumau21floyd/entry-12661092996.html)).
  Anno y Tomino además se entrevistaron en *Animage* (07/1994), antes de que
  saliera Eva ⚠️ (mencionado por [Wave Motion Cannon](https://wavemotioncannon.com/2016/11/08/interview-hideaki-anno-vs-yoshiyuki-tomino-animage-071994/),
  no leí la traducción completa).
- **Devilman** (Go Nagai) y **Nausicaä del Valle del Viento** (manga, no la
  película): citadas junto a Ultraman e Ideon como influencias directas en
  varios repasos japoneses del tema ⚠️ (mismo grupo de fuentes de arriba,
  sin entrevista directa de Anno sobre estas dos).
- **Kunihiko Ikuhara** (director de *Revolutionary Girl Utena*, 1997):
  **amistad personal** con Anno; el fandom compara ambas series todo el
  tiempo por el tono psicológico y simbólico parecido, aunque son obras de
  estudios y equipos distintos hechas casi a la vez ⚠️ (una fuente,
  [TV Tropes: Creator/HideakiAnno](https://tvtropes.org/pmwiki/pmwiki.php/Creator/HIDEAKIANNO)
  vía resumen de búsqueda, TV Tropes me bloqueó al abrirlo directo).

### 24.2 Series parecidas según el público (para no repetir sus láminas)

De las recomendaciones de usuarios en AniList (ya en `datos-texto.md`, no lo
repito entero): **Serial Experiments Lain**, **Puella Magi Madoka Magica**,
**Gurren Lagann**, **Akira**, **Devilman Crybaby**, **FLCL**, **Gunbuster**,
**Sonny Boy**, **Revolutionary Girl Utena**, **Mobile Suit Gundam**,
**Berserk**, **RahXephon** (a veces llamado «el Evangelion pobre» por lo
parecido de su premisa), **Space Runaway Ideon**, **Darling in the Franxx**.
Todas comparten: mecha + trauma psicológico + preguntas existenciales.
· fuente: AniList (recomendaciones de usuarios) · ⚠️ (votos de usuarios, no
lista oficial) · votos en `datos-texto.md`

### 24.3 Qué otras láminas del servidor se le parecen

Ninguna biblia terminada usa el canal **#demos** ni una estética de
**terminal militar/HUD** como concepto de lámina (grep en `biblias/*/biblia.md`
por «demos»: los que salen son coincidencias con otras palabras, «podemos»,
«demostr…», ninguno con foro de fichas de doblaje). En **tono** (mecha +
psicológico + distopía) sí hay parecido parcial con `02-attack-on-titan` y
`27-cyberpunk-edgerunners`, pero sus láminas van a canales de trivia/juegos,
no a un foro de fichas de voz: no hay riesgo real de repetir la idea.
· fuente: búsqueda propia en el repositorio (`grep -rl "demos"
biblias/*/biblia.md`) · ✅ (comprobado en el propio repositorio) · —

## 25 · El mundo, la historia y sus símbolos

Todo lo de esta sección lo comprobé leyendo directamente las páginas de
**EvaWiki (wiki.evageeks.org)**, que sí se deja abrir con `curl` (a
diferencia de Fandom y TV Tropes) y cita sus fuentes primarias en cada
artículo.

### 25.1 Las reglas del mundo, en cinco líneas

1. En **2000** un cataclismo, el **Segundo Impacto**, derritió el casquete
   antártico e inundó las costas del mundo; la ONU dijo que fue un meteorito
   en el monte Markham, pero fue en realidad el despertar de **Adán**, el
   Primer Ángel ✅ ([EvaWiki: Second Impact](https://wiki.evageeks.org/Second_Impact)).
2. Los **Ángeles** (使徒, *Shito*, literalmente «apóstoles») son seres gigantes
   que atacan Tokio-3 buscando llegar a **Lilith**, en las profundidades de
   NERV; sus nombres vienen de **ángeles judeocristianos del Libro de
   Enoc/tradición apócrifa** (Sachiel = ángel del agua, guardián del jueves;
   Gaghiel = ángel de los peces) ✅ (buscado en japonés, coincide en
   [note.com: guía de los 18 使徒](https://note.com/bunnygirlman/n/na6197925aea9)
   y en la [Wikipedia japonesa](https://ja.wikipedia.org/wiki/%E4%BD%BF%E5%BE%92_(%E6%96%B0%E4%B8%96%E7%B4%80%E3%82%A8%E3%83%B4%E3%82%A1%E3%83%B3%E3%82%B2%E3%83%AA%E3%82%AA%E3%83%B3))).
   **La propia humanidad (Lilin) es contada como el 18.º Ángel** en la lista
   completa ✅ (mismas dos fuentes japonesas).
3. Sólo los **Eva** (organismos gigantes con un «alma» humana dentro, no
   robots) pueden generar un **Campo AT** (*Absolute Terror Field*) capaz de
   frenar el de un Ángel; casi ninguna arma convencional atraviesa un Campo
   AT, salvo otro Campo AT o el **Lanza de Longinus** ✅ ([EvaWiki: AT
   Field](https://wiki.evageeks.org/AT_Field), [EvaWiki: Spear of
   Longinus](https://wiki.evageeks.org/Lance_of_Longinus)).
4. **NERV** (agencia secreta de la ONU) pilota los Eva en público; **SEELE**
   (el «Comité de Instrumentalización Humana», 12 ancianos que sólo se
   muestran como monolitos negros) controla a NERV en la sombra para lograr
   el **Proyecto de Instrumentalización Humana** ✅ ([EvaWiki: Human
   Instrumentality Project](https://wiki.evageeks.org/Human_Instrumentality_Project)).
5. Ese proyecto busca el **Tercer Impacto**: fundir todas las almas humanas
   en una sola, borrando el concepto mismo de individuo («ni siquiera se
   podría llamar "conjunto", porque no habría individuos que juntar») ✅
   (mismo EvaWiki, cita textual traducida del artículo).

### 25.2 La historia por arcos (con sus momentos clave)

- **Arco 1 · Los Ángeles clásicos** (ep. 1-6 aprox.): Shinji llega a
  Tokio-3, pilota el Eva-01 por primera vez (ep. 1), aparece Rei; combates
  «de monstruo de la semana» que van revelando que los Eva **sienten dolor**
  ✅ (estructura de episodios, EvaWiki + AniList).
- **Arco 2 · Llega Asuka y se complica el misterio** (ep. 8-15): Asuka y el
  Eva-02 (ep. 8), aparece el Eva-03 posesionado por un Ángel y Toji queda
  mutilado (ep. 18, spoiler que ya está en `biblia.md` §2) ✅.
- **Arco 3 · Colapso psicológico** (ep. 16-24): cada personaje se enfrenta a
  su propio Campo AT interior; Kaworu llega y muere en el ep. 24 ✅.
- **Cierre: Instrumentalización** (ep. 25-26 de TV, reinterpretado en **The
  End of Evangelion**): el Tercer Impacto y sus dos finales alternativos, el
  psicológico (TV) y el literal/apocalíptico (EoE) ✅ (EvaWiki: Human
  Instrumentality Project, apartado «Seele's Plans» / «Gendo's plans»).

### 25.3 Emblemas, objetos icónicos y vocabulario (glosario para el fandom)

| Término | Qué es | Fuente |
|---|---|---|
| **NERV** | Agencia de la ONU, logo con hoja de higuera y la frase de Browning «God's in his heaven, all's right with the world» | ya en `biblia.md` §7 |
| **SEELE** | Comité en la sombra, 12 monolitos negros «SOUND ONLY» | ya en `biblia.md` §7 |
| **MAGI** | Los 3 superordenadores que gobiernan NERV y el gobierno de Tokio-3 por mayoría; cada uno es un aspecto de la personalidad de la Dra. **Naoko Akagi** (madre de Ritsuko): **Melchior** (ella como científica), **Balthasar** (como madre), **Caspar** (como mujer) ✅ ([EvaWiki: MAGI](https://wiki.evageeks.org/MAGI)) |
| **Children** (Primero a Quinto) | Como se llama a los pilotos de 14 años (Rei=1.º, Asuka=2.ª, Shinji=3.º, Toji=4.º, Kaworu=5.º); en japonés «children» se usa igual en singular, el doblaje inglés de ADV lo cambió a «Child» | ✅ ([EvaWiki: Children](https://wiki.evageeks.org/Children)) |
| **Campo AT** | Ver §25.1.3 | ✅ EvaWiki |
| **Lanza de Longinus** | Arma bífida roja del tamaño de un Eva, atraviesa cualquier Campo AT | ✅ EvaWiki |
| **Instrumentalización** | Ver §25.1.5 | ✅ EvaWiki |
| **Árbol de la Vida / Sefirot** | Aparece en el opening y tras el Tercer Impacto; **18 Ángeles en total** puede aludir a las **10 Sefirot** más otras figuras cabalísticas, pero **no hay una fuente que lo confirme del staff** — Anno dijo en Newtype (1997) que «usamos símbolos cristianos porque se veían bien, sin significado profundo» | ⚠️ (una fuente de la cita, [ScreenRant: «There's No Hidden Meaning»](https://screenrant.com/neon-genesis-evangelion-pretentious-hidden-meaning-philosophical-factoid/); la propia EvaWiki **no tiene** página de «Sephirot», señal de que ni el wiki más académico del fandom lo da por confirmado) |
| **LCL** | Líquido naranja que llena el habitáculo del Eva y respira el piloto | ya en referencias previas del equipo (⚠️, de memoria) |

**Nota de método**: Anno **niega explícitamente** que el simbolismo
judeocristiano/cabalístico tenga un significado teológico real («no hay
significado oculto»), aunque hay tesis académicas que sí intentan un análisis
serio (citadas arriba, ResearchGate). Para la lámina: **usa los símbolos
como estética** (el logo, los monolitos, el árbol en el opening), **no como
lore que haya que explicar** — es fiel a cómo el propio autor lo trata.
· fuente de la negación: [ScreenRant](https://screenrant.com/neon-genesis-evangelion-pretentious-hidden-meaning-philosophical-factoid/) · ⚠️ (una fuente cita la entrevista de Newtype 1997, no la traducción completa) · —

## Lo mejor para la lámina

- La **cartela negra con Matisse EB comprimida** (punto 5-6, ya en
  `biblia.md`) sigue siendo lo más reconocible: título del canal en blanco
  sobre negro, sin bocadillo.
- Para la **pantalla de NERV** (fondo del panel de estado del foro #demos):
  glow verde/naranja + scanlines finas, receta de Photoshop en 18.2.
- **«SEELE 01... SOUND ONLY»** (los monolitos) es la metáfora perfecta para
  una ficha de voz: **sólo se oye, no se ve la cara**. Usa Chicago
  (ChiKareGo2, ✅ comprobado) en el número, todo en mayúsculas.
- La **relación con Ideon** (parodia del final en EoE) y con **Ultraman**
  (Ángel = alienígena con cara de superhéroe) dan una frase corta para el
  texto del canal: «un piloto adolescente contra ángeles caídos».
- El **glosario de §25.3** (MAGI, Children, Campo AT, Instrumentalización)
  es material listo para textos del bot o tooltips del canal.

## No encontré

- **Una página real del manga** (bocadillo, tramas) para confirmar el punto
  6.1.7: sólo tengo análisis de crítica, no la vi yo mismo. Búsquedas:
  «Evangelion manga Sadamoto speech bubbles panel layout» (inglés).
- **Capturas verificadas** de las cajas de diálogo de *Girlfriend of Steel*,
  *Ayanami Raising Project* y *Shinji Ikari Raising Project*: TCRF y TV
  Tropes me dieron `net::ERR_CERT_AUTHORITY_INVALID` con el navegador sin
  ventana (`herramientas/navegar.py`) **en cualquier sitio con Cloudflare**,
  no sólo Eva — parece un fallo del proxy del contenedor con esos
  certificados, no un bloqueo específico. Wayback Machine también falló
  (`ws_closed_mid_exchange`, confirmado con `/__agentproxy/status`) al bajar
  las copias archivadas de esas páginas de TCRF, aunque `archive.org` (sin
  «web.») sí respondía. Búsquedas: «Cutting Room Floor Evangelion Girlfriend
  of Steel prerelease» y «"Cutting Room Floor" Evangelion Shinji Ikari
  Raising Project» (inglés).
- **Qué programa** usó Gainax para los pocos efectos digitales de 1995-96
  (créditos, *glitches* mentales): no hay entrevista de producción digital
  de esa época que lo diga. Búsqueda: «Evangelion production Gainax limited
  budget still frames cel animation analog making of interview» (inglés).
- **Confirmación oficial** del staff de que los 18 Ángeles se inspiran en
  las 10 Sefirot: ni la Wikipedia japonesa ni EvaWiki lo dan por probado (la
  página «Sephirot» de EvaWiki ni existe). Búsqueda: «新世紀エヴァンゲリオン
  使徒 名前 天使 由来 セフィロト» (japonés).
- **Detalle de la entrevista Anno-Tomino** de *Animage* 07/1994 completa:
  sólo tengo el resumen de Wave Motion Cannon, no la traducción entera.

## Bitácora

- WebSearch (inglés): «Cutting Room Floor Evangelion Girlfriend of Steel
  prerelease»; «"Cutting Room Floor" Evangelion Shinji Ikari Raising
  Project»; «Hideaki Anno interview Kabbalah Sephirot Evangelion symbolism
  "no particular meaning"»; «Hideaki Anno influences Yoshiyuki Tomino Ideon
  Kunihiko Ikuhara interview Evangelion»; «Evangelion production Gainax
  limited budget still frames cel animation analog making of interview»;
  «Blender Freestyle Line Art modifier anime outline toon shader tutorial
  settings»; «Photoshop anime cel shading tutorial layers multiply screen
  grain halation brushes»; «Evangelion manga Sadamoto speech bubbles panel
  layout style analysis»; «"Anno shot" OR "Anno-shot" Hideaki Anno signature
  framing composition style analysis»; «ChiKareGo2 font free download ttf».
- WebSearch (japonés): «庵野秀明 エヴァンゲリオン 影響を受けた作品 イデオン
  ウルトラマン»; «新世紀エヴァンゲリオン 使徒 名前 天使 由来 セフィロト».
- Bajado y comprobado con **fontTools** (`TTFont.getBestCmap()`):
  `ChiKareGo2.woff` (GitHub, helloedit/resources/fonts).
- Leído directo con `curl` (sí responde, a diferencia de Fandom/TV Tropes):
  `wiki.evageeks.org` — páginas Human_Instrumentality_Project, MAGI,
  Second_Impact, AT_Field, Lance_of_Longinus, Children, Kabbalah (vacía),
  Sephirot (no existe), Statements_by_Evangelion_Staff.
- Intentado y **bloqueado**: `tcrf.net` (Cloudflare, 403 en WebFetch,
  `ERR_CERT_AUTHORITY_INVALID` en navegar.py); `tvtropes.org` (mismo error
  de certificado); `web.archive.org` (túnel del proxy se cerró 3 veces,
  `ws_closed_mid_exchange` según `/__agentproxy/status`; `archive.org` sin
  «web.» sí funcionó).
- Repositorio propio: `grep -rl "demos" biblias/*/biblia.md` para el punto
  24.3 (ningún canal #demos repetido).
- Ya estaba en `datos-texto.md` y no repetí la consulta: AniList (obra,
  equipo creativo, obras parecidas y relacionadas).

## Cumplimiento de mis puntos (5, 6, 11, 18, 24, 25)

| Punto | Estado | Por qué |
|---|---|---|
| 5 · Tipografía | ✅ | Ya muy hecho en `biblia.md` §6; añadí la comprobación con fontTools que faltaba (Chicago/ChiKareGo2) |
| 6 · Cuadros de diálogo | ✅ (con 1 ⚠️ heredado) | Ya muy hecho en `biblia.md` §7; el bocadillo del manga sigue sin verse en una página real |
| 11 · Videojuegos | ⚠️ | Tabla ya hecha; TCRF existe pero no pude abrirlo (bloqueo de certificado del contenedor) ni Wayback (fallo de túnel); dejo los enlaces para que se reintente |
| 18 · Estilo y cómo replicarlo | ✅ | Sección nueva completa: producción real (fuentes) + receta concreta de Photoshop y de Blender (Solidify/Line Art/Freestyle, Shader to RGB); rigs y tramas remitidos a los puntos 3 y 19 |
| 24 · Obras parecidas | ✅ | Influencias confirmadas en japonés (Ultraman, Ideon) + recomendaciones de AniList + comprobación de que ningún canal del servidor repite la idea |
| 25 · Mundo y símbolos | ✅ | Reglas del mundo, arcos e historia y glosario, todo con EvaWiki (fuente primaria citada) como base |
