# Parte de TEXTO — Solo Leveling (repaso corto: puntos 18, 24, 25)

Investigador de texto, juegos y técnica. Este repaso sólo cubre los puntos
**18, 24 y 25** de `ENCARGO.md` (nuevos: no estaban en la biblia). Parte de
`datos-texto.md` (no repetí esas consultas: AniList — obra, staff, obras
parecidas, obras relacionadas — ya recolectado ahí). Los puntos 5, 6, 11
(también míos por `EQUIPO.md`) **no se tocan**: ya están en la biblia
(secciones 5, 4/6 y 15).

Leyenda: ✅ dos fuentes (o algo que abrí/medí yo) · ⚠️ una fuente o de memoria.

---

## Hallazgos

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**Quién lo hizo (equipo, de `datos-texto.md` + AniList/staff)**
- Estudio **A-1 Pictures**. Director **Shunsuke Nakashige**; diseño de
  personajes **Tomoko Sudo** (nominada al Emmy por diseño de personajes) ·
  [VFX Voice, entrevista al staff](https://vfxvoice.com/maximizing-the-strength-of-anime-for-solo-leveling/) ✅ (ya en `datos-texto.md`/§2 de la biblia).
- **Gráficos en movimiento** (ventanas del Sistema): Takemune Ōshiro, de
  **Production I.G** (ya en biblia §2) ✅.

**La frase clave del director sobre el estilo** ✅ (dos medios citan la
misma entrevista)
- Nakashige: *«I thought this work required the high-end visuals that are
  trending these days. Therefore, I tried to avoid cartoon-like expressions
  as much as possible, using compositions, colors, and shooting processing
  similar to live-action footage.»* Añade que eso «se come tiempo» y que lo
  ajustaron en reuniones con cada sección y en el chequeo de vídeo — [CBR](https://www.cbr.com/solo-leveling-director-original-cartoon-expressions-anime-why-cut/),
  [FandomWire](https://fandomwire.com/solo-leveling-director-reveals-reason-behind-change/) ✅.
  **Para la guía de estilo:** nada de expresiones «cartoon» (deformación
  cómica); encuadres, color y «procesado de cámara» como imagen real
  (profundidad de campo, grano, contraste).

**2D y 3D mezclados (para grupos y monstruos)** ✅ dos fuentes
- Productor **Atsushi Kaneko** (A-1 Pictures): «We wanted to use 2D
  hand-drawn animation as the foundation, but... it doesn't scale well»
  para masas de enemigos. El **Ejército de las Sombras** se probó en 2D y
  se pasó a 3D porque las formas simples «no tenían impacto visual» — [VFX Voice](https://vfxvoice.com/maximizing-the-strength-of-anime-for-solo-leveling/) ✅.
- Los **Altos Orcos** (High Orcs) se renderizan en CG y se tratan «para
  que parezcan más 2D» (mezcla intencional) — [Anime Corner, «cómo se hizo»](https://animecorner.me/how-the-solo-leveling-anime-was-made-behind-the-scenes-at-a-1-pictures-ahead-of-the-season-2-finale/) ✅.
  El estudio llama a esto **«2D First»** (se dibuja y luego se pasa a CG) o
  **«3D First»** (al revés), según la escena.
- Personajes de fondo repetidos: mismo modelo base, **cambian tatuajes o
  colores** para diferenciarlos (CG Director Toshitaka Morioka) — Anime
  Corner ⚠️ una fuente.

**Captura de movimiento (mocopi, de Sony) — cómo se animó el ep. 11-12** ⚠️
fuente oficial única (caso de estudio de Sony, con cita directa del staff)
- [Sony XYN, caso de estudio](https://xyn.sony.net/en/case/sololeveling-anime):
  usaron **mocopi** (6 sensores inerciales, 3,2 cm, 8 g, vía móvil) para
  animar a los **«Knights»** (monstruo) y escenas de multitud en los
  **episodios 11 y 12**: correr y espadazos. Tuvieron que grabar **al aire
  libre** porque el estudio no tenía espacio para blandir la espada.
- Flujo: **3ds Max** (rig CAT) → **MotionBuilder** (retargeting) → datos en
  formato **BVH** (FBX desde sept-2024). Tres variantes de caballero (A, B,
  C) y un modelo de mago.
- CG Director **Toshitaka Morioka**: «What makes mocopi attractive is that
  I can use it whenever I come up with an idea»; sirve para que los
  animadores junior partan del mismo punto en vez de posar desde cero.

**Un truco de montaje** ⚠️ una fuente
- El storyboardista **Takayuki Kikuchi** propuso unir varios planos de
  Igris contra Iron en **un solo corte de 26 segundos**, que impresionó al
  equipo — Anime Corner.

**Cómo se ve de verdad (medido por mí, `estilo.py`, dos imágenes de la
wiki)** ✅ (imágenes propias)
- **Fotograma del anime** (Igris, ep. 11, [Anime Episode 11 Picture 5](https://static.wikia.nocookie.net/solo-leveling/images/c/c0/Anime_Episode_11_Picture_5.png), 1366×768): **casi sin contorno negro**. El
  volumen se hace con **luz de borde de color** (rosa/violeta `#8B5469` /
  `#E790B7` sobre negro casi puro `#08080F`/`#0F121B`) en vez de línea:
  `estilo.py` mide «sombreado mixto, poca línea» y una línea de color
  `#693D56` (no negra). Saturación baja (55%), brillo muy bajo (16%): es
  **oscuro y contrastado**, no plano.
- **Viñeta del webtoon** ([Chapter 50](https://static.wikia.nocookie.net/solo-leveling/images/3/3c/Chapter_50.png), 574×778, Jinwoo en la nieve): **línea negra limpia
  y continua** (medida: `#3F3F47`, más oscura y definida que en el anime),
  sombreado plano en el pelo con un solo golpe de luz, **nieve pintada con
  pincel suave** encima de todo (partículas blandas, no vector). Paleta
  fría (azul `#858EA5` / `#98BACD`) contra el marrón cálido del abrigo.
- **Diferencia clave para la guía de estilo:** el **webtoon entinta en
  negro** (línea de cómic clásica); el **anime reduce la línea al mínimo y
  la sustituye por luz de borde de color** en las escenas de acción/poder
  — coherente con la cita de Nakashige de arriba («evitar lo cartoon»,
  «como imagen real»). Para la lámina: si el marco es un fotograma del
  anime, casi sin contorno negro; si es un cuadro de manga/webtoon, línea
  negra limpia sí.

**El webtoon (Dubu / REDICE Studio), lo que se sabe sin entrevista de
proceso** ⚠️ una fuente de reseña, no de making-of
- Ilustrador **Jang Sung-rak («Dubu»)**, fundador de Redice Studio, murió
  en jul-2022. Su estilo: «sharp, clean, and soaked with deep, rich hues»;
  suyo es el diseño de Jinwoo con las dagas, las mazmorras y los monstruos
  — [KoreaLore](https://www.korealore.com/2026/08/solo-leveling-webtoon-profile.html).
  **No encontré** una entrevista suya sobre su programa de dibujo (Clip
  Studio, Photoshop…): no hay fuente fiable, así que no lo afirmo (busqué
  en inglés y con «Dubu Redice Studio interview process»; su discreción
  pública puede ser la razón).

**Software de animación 2D (lo que pide el encargo: Clip Studio, Toon Boom,
RETAS…)** ⚠️ no encontré el dato específico del estudio
- Busqué «A-1 Pictures Solo Leveling software Clip Studio Toon Boom RETAS»:
  no hay ninguna fuente que diga **qué programa 2D usó A-1 Pictures** en
  esta serie en concreto. Lo único de contexto general (no específico de
  Solo Leveling): en la industria japonesa de TV, la mayoría de estudios
  usa **RETAS** (Celsys) para el proceso 2D completo (entintado, color,
  cámara); **Clip Studio Paint** lo usan otros estudios (Toei, OLM,
  Yostar) — [Clip Studio ASK](https://ask.clip-studio.com/en-us/detail?id=57247) ⚠️ dato de industria, no de esta serie.
  **No lo afirmo como el programa de Solo Leveling.** Lo que sí está
  confirmado (arriba): **3ds Max + MotionBuilder** para la parte 3D/mocap.
- **Tramas (screentone) no aplica**: el webtoon es **a todo color** desde
  el principio (no es manga en blanco y negro con tramas de punto); el
  «sombreado con trama» del punto 18 del encargo no tiene equivalente
  aquí. Lo que sí hay es la **textura de pincel** en nieve/polvo (viñeta
  de arriba) y el grano fino del anime.
- **Aberración cromática, brillo, grano**: no encontré una fuente técnica
  que los nombre por su nombre (busqué «chromatic aberration film grain
  bloom Solo Leveling»); lo que hay es la cita de Nakashige sobre
  «procesado como imagen real», que es de donde traduzco la recomendación
  de grano y viñeteado de abajo. **Tratar esa traducción como propia, no
  como confirmada.**

**Cómo replicarlo en Photoshop**
- **Para un cuadro «anime» (poder, Monarca, acción):** casi sin línea
  negra; el contorno lo da una capa de **luz de borde** en modo Añadir o
  Trama de color, en el tono de la escena (cian del Sistema `#82F3FA`,
  violeta Monarca `#9229F9`/`#ED77F3`, o rosa como en Igris). Sombra en
  Multiplicar, oscura y con poco degradado (`#08080F`-`#15262D`, medido
  arriba). Encima, una capa de **grano fino** (Filtro > Ruido, 2-3%) y un
  **viñeteado sutil**: es lo que Nakashige llama «procesado como imagen
  real». ⚠️ traducción propia de la técnica a partir de la cita, no de un
  tutorial oficial.
- **Para un cuadro «webtoon/manga»:** pincel redondo duro, línea negra
  continua (`#3F3F47`-`#1A222C` de lo medido), sombra plana de un solo
  tono por zona, luces puntuales con pincel suave (la nieve).

**Cómo replicarlo en Blender**
- **Contorno:** para el estilo «anime con poca línea», mejor **sin
  Freestyle/Line Art visible** y en su lugar un nodo **Fresnel/Capa** que
  alimente un **Emission** del color de la escena (rosa/violeta/cian) para
  imitar la luz de borde medida arriba; para un cuadro «tipo webtoon»
  (línea negra), usar **Line Art** (Grease Pencil) o **Freestyle** con
  grosor fino y constante, como en otras biblias del servidor (Solidify
  para objetos sueltos, Freestyle para un trazo más suelto, Line Art para
  el más fiel a mano — mismo trío que ya usa la biblia de One Punch Man,
  §19.4, útil de referencia porque no hay un tutorial específico de Solo
  Leveling).
- **Sombreado (Eevee):** *Shader to RGB* → *Color Ramp* en **Constante**,
  2 bandas para la piel/objetos, 3 para pelo o efectos de energía (según
  lo medido en el fotograma de Igris, con banda media rosa clara).
- **Texturas encima** (como *decal*, mismo truco que ya usa la biblia de
  One Punch Man §19.4 con su emblema): el **emblema de Ahjin** (violeta,
  700×700, tabla de abajo) o el de otro gremio sirven como calcomanía en
  ropa, escudos o el mostrador de la Asociación; el metal y la madera ya
  medidos en la biblia (§4/§9) para las superficies alrededor.
- **Modelos y *rigs* libres del personaje** (para posar, no para pegar):
  - **Igris**: [Igris - Solo Leveling](https://sketchfab.com/3d-models/98c049a047da440b80a45f29f574dc09)
    (shrithik, CC BY, 33 970 caras) — **ya usado** en el Concepto C de la
    biblia (`sk-igris2`).
  - **Cha Hae-In**: [Cha Hae-In - Solo Leveling](https://sketchfab.com/3d-models/b07a938c74a84bfe8caab58a97e3b305)
    (Casttelan2, CC BY, 35 694 caras, descargable) — **nuevo**, no estaba
    enlazado en la biblia; sirve para posarla en cualquier concepto nuevo
    con ella. Comprobado por la API de Sketchfab (licencia y tamaño) ✅.
  - La **Espada del Rey Demonio** (Demon King's Longsword): el arma que
    Jinwoo le da a Igris tras matar a Baran, y que **décadas después usa
    Cha Hae-In** como arma principal — [wiki, wikitext](https://solo-leveling.fandom.com/wiki/Demon_King%27s_Longsword) ✅.
    Modelos libres de espada ya enlazados en la biblia (`sk-igrissword`).
- **Captura de movimiento como referencia de pose** (no como técnica de
  Blender en sí, pero explica por qué las poses de grupo/monstruo se ven
  «con peso real»): el estudio usó mocopi para los Knights del ep. 11-12
  (arriba). Para la lámina, sirve para justificar posar sombras/monstruos
  con **movimiento capturado real** en vez de a ojo.

**Encuadres y composición típicos** (de lo que ya vieron/midieron los
compañeros de vídeo e imagen en la biblia, más la cita de Nakashige)
- **Contrapicado y silueta a contraluz** para revelar poder: Go Gunhee de
  brazos cruzados ante la ciudad en ruinas (ya en biblia, OP · 0:54);
  Jinwoo con ojos violeta, mano en la cara (OP · 1:22).
- **Primeros planos con fondo desenfocado** (profundidad de campo, «como
  imagen real»): el fotograma de Igris de arriba tiene el fondo
  **totalmente fuera de foco** (planta verde borrosa arriba) mientras la
  cara está nítida — típico de cámara real, no de anime plano.
- **El plano largo de 26 s** de Igris/Iron (arriba): cámara que sigue la
  acción sin cortar, en vez de montar planos cortos — poco común en TV.
- **Para la lámina:** si el personaje «habla» desde un fotograma, mejor
  **fondo desenfocado y luz de borde de color**, no un fondo nítido y
  plano.

---

### Punto 24 · Obras parecidas y temas relacionados

**Recomendaciones de AniList** (ya en `datos-texto.md`, no las repito
enteras): con más votos, **Sword Art Online** (166), **Tower of God**
(88), **The Eminence in Shadow** (60), *I Got a Cheat Skill...* (56), **The
God of High School** (55), *Tomb Raider King* (52) — [AniList](https://anilist.co/anime/151807) ✅.

**Confirmación editorial (fuera de AniList)** ✅ dos tipos de fuente
- Listas «si te gustó Solo Leveling» de varios medios (Screen Rant, Dexerto,
  MovieWeb, MyAnimePulse) repiten los mismos títulos que AniList:
  - **Tower of God**: «power scaling and progression» parecidos; Bam sube
    de piso en piso, con más misterio y desarrollo de personajes.
  - **The Eminence in Shadow**: mismo gancho de «poder oculto» (Jinwoo se
    vuelve el Monarca de las Sombras; el prota de Eminence esconde su
    fuerza y monta su propio «ejército» de subordinados); el tono es
    paródico/chūnibyō, al revés que Solo Leveling.
  - Para mazmorras y «sistema»: **Shangri-La Frontier**, ***Is It Wrong to
    Try to Pick Up Girls in a Dungeon?***, **Overlord**, **Noblesse**.
  - Frase textual de uno de los medios: **«the webtoon trinity — Tower of
    God, God of High School, Noblesse — is the most direct DNA match»**
    (la comparación más citada para webtoons coreanos de progresión).
- Fuentes: [MovieWeb](https://movieweb.com/best-action-anime-like-solo-leveling/),
  [Dexerto](https://www.dexerto.com/anime/best-anime-like-solo-leveling-2463795/),
  [ScreenRant](https://screenrant.com/best-anime-like-solo-leveling-watch/) (leídas agregadas por buscador, mismo patrón en las tres) ✅.

**Influencias que reconoce/sugiere el propio material** ⚠️ una fuente (blog,
no entrevista directa de Chugong)
- Chugong es muy reservado (casi sin entrevistas de prensa). Un perfil en
  francés dice que es **fan de RPG y de la «fantasía de progresión»**, y
  que se inspiró en mecánicas **tipo Diablo, Skyrim o World of Warcraft**
  para el «Sistema»; la idea de partida fue «¿y si el cazador más débil
  consigue un sistema único que lo hace subir sin techo?» — [blog oficial
  de la tienda solo-leveling.fr](https://solo-leveling.fr/en/blogs/blog-solo-leveling/chugong-le-genie-creatif-derriere-le-phenomene-solo-leveling) ⚠️.
  **No encontré** una entrevista primaria de Chugong (coreana o traducida)
  que lo confirme con sus palabras: busqué «추공 인터뷰 게임 영감» y en
  inglés, sin resultado directo. Tratar como **dudoso**.
- Lo que **sí** dice Chugong con cita directa (otro tema, no de estilo):
  simplificó el trasfondo cósmico (el concepto **Itarim**, un dios por
  universo) para no ser «demasiado sombrío» en un género pensado para
  lectores jóvenes — [CBR, entrevista](https://www.cbr.com/solo-leveling-chugong-interview-removed-itarim-light-novel-bleak/) ✅ (coincide con lo que dice la
  propia wiki del concepto).

**Obra derivada, no una serie distinta pero sí «relacionada»**
- **Solo Leveling: Ragnarok**: spin-off/continuación en manhwa (dibujo de
  **Dubu (Redice Studio)** también, guion de un nuevo escritor), con su
  propia lista de arcos separada en la wiki — [Story Arcs (Ragnarok), wiki](https://solo-leveling.fandom.com/wiki/Story_Arcs_(Ragnarok)) ✅
  (comprobado en el índice de la wiki: existen páginas «D-Rank Dungeon Arc
  (Ragnarok)», «Retesting Rank Arc (Ragnarok)»). Para la lámina no hace
  falta, pero si el dueño pregunta por «más Solo Leveling», existe.
- **Crossover ya documentado en otra biblia del servidor**: la colaboración
  oficial **Solo Leveling: ARISE × Frieren** (Netmarble, oct-nov 2025) está
  en `biblias/33-frieren/biblia.md` (arte oficial de Jinwoo+Frieren+Fern+
  Stark, y una partida grabada con la caja de diálogo de ARISE) ✅ (leída
  en su biblia). Es un dato de punto 23 (colaboraciones, no mío), pero
  cuenta como «tema relacionado» entre dos láminas del servidor.

**Láminas vecinas del servidor (para no repetir ideas)** ✅ (leídas en sus
biblias)
- **One Piece (01)** y **Attack on Titan (02)** ya avisan en sus propias
  biblias de que su «tablón de corcho con papeles» debe **distinguirse**
  del de Solo Leveling: *«Que no parezca el tablón de Solo Leveling: madera
  de barco y clavos, nunca corcho»* (One Piece, punto 24) y lo mismo en la
  de Attack on Titan. Esto confirma que el **Concepto B** de la propia
  biblia de Solo Leveling (tablón de corcho del vestíbulo, §20) **ya es el
  objeto de referencia** que otras láminas evitan copiar: no hay que
  cambiarlo, pero si se rehace, no lo lleves a madera ni papel
  envejecido roto (eso ya es de One Piece).
- Comparado con las láminas de otros shonen de acción con sistemas de
  rango ya hechas (**Jujutsu Kaisen** 32, **Demon Slayer** 31, **Naruto**
  30, **My Hero Academia** 25, **One Punch Man** 35): ninguna usa un
  mostrador de recepción, una ventana de sistema tipo videojuego ni un
  salón del trono — usan pizarra de aula, calabazas colgadas, cuaderno de
  héroe. **No hay choque de objeto** con los tres conceptos ya escritos de
  Solo Leveling (mostrador+cristal, tablón/móvil, salón del trono de
  Igris). Revisado por el índice de cada biblia (`seccion.py --indice`),
  no leídas entero.

---

### Punto 25 · El mundo, la historia y sus símbolos

**Las reglas del mundo (datos para las 5 líneas del redactor)** ✅ wiki +
ya confirmado en la biblia (Class Ranks, System, Guilds)
- Desde hace **8-9 años** existen los **portales** (Gates) con
  **mazmorras**: aparecieron junto con personas que manifiestan **maná** y
  se llaman **Cazadores** — [wiki: Class Ranks](https://solo-leveling.fandom.com/wiki/Class_Ranks) ✅.
- **Rango internacional E a S** (E el más débil, S el más fuerte): fija
  casi todo (sueldo, respeto); normalmente es **fijo de por vida** salvo un
  «segundo despertar», rarísimo. Jinwoo es la única excepción conocida
  porque el Sistema lo elige como Jugador — wiki ✅ (ya en biblia §2/§6).
- **Gremios**: empresas de Cazadores que limpian mazmorras; los grandes
  tienen mejor paga y seguridad; los Cazadores independientes pagan más
  impuestos — [wiki: Guilds](https://solo-leveling.fandom.com/wiki/Guilds) ✅.
- La **Asociación de Cazadores** (coreana y de cada país) regula todo: sede
  en Guro, Seúl (ya en biblia §9).
- Detrás del Sistema hay un **Arquitecto** (Kandiaru), su «moderador», y
  una guerra cósmica entre **Monarcas** y **Gobernantes** (Rulers) que
  llega al mundo humano — [wiki: Story Arcs](https://solo-leveling.fandom.com/wiki/Story_Arcs) ✅ (resumen de los arcos
  del final de la novela/webtoon, aún no animados).

**La historia por arcos** (lista oficial de la wiki, con equivalencia a
capítulos de anime cuando existe) ✅ un wiki, pero es la lista estándar que
ya cita el resto de la biblia; contrastada con los títulos de episodio de
[Wikipedia](https://en.wikipedia.org/wiki/List_of_Solo_Leveling_episodes) (ep. 11 «A Knight Who Defends an Empty Throne», ep. 12
«Arise» → coincide con «Job Change Arc», ep. 11-12) ✅

*Cubiertos por el anime (T1-T2, ep. 1-25):*
1. **D-Rank Dungeon** (ep. 1-3): la mazmorra doble-trampa; muere el grupo.
2. **Reawakening** (ep. 3): despierta en el hospital; descubre el Sistema.
3. **Instant Dungeon** (ep. 3-4): primera cacería en solitario.
4. **Dungeon & Lizards** (ep. 5-6): la encerrona del gremio Tigre Blanco.
5. **Dungeon & Prisoners** (ep. 7-9): reencuentro con los supervivientes;
   Kang Taeshik y los presos.
6. **Yoo Jinho Raid Party** (ep. 10): forma equipo legal con Jinho.
7. **Job Change** (ep. 11-12): la mazmorra instantánea, el ejército de
   armaduras y **el caballero rojo del trono vacío** (Igris); primer
   «Arise».
8. **Red Gate** (ep. 13-14): trampa en el examen del Tigre Blanco.
9. **Demon Castle** (ep. 15): mazmorra S para el agua de la vida.
10. **Retesting Rank** (ep. 16): reevaluación de rango.
11. **Hunters Guild Gate** (ep. 16-18): minería en rango A.
12. **Return to Demon Castle** (ep. 18-21): Esil Radiru; Baran, el Rey
    Demonio.
13. **Jeju Island** (ep. 21-25): la incursión, el **Rey Hormiga** (Beru).
14. **Recruitment** (ep. 25): funeral de Min Byung-Gyu; Norma Selner.

*Aún sin animar (sólo webtoon/novela; útil si el dueño pregunta «qué
viene»):* Ahjin Guild, Double Dungeon (vuelta), Japan Crisis, International
Guild Conference (**aparecen los Monarcas y los Gobernantes**), Monarchs
War, Final Battle (contra **Antares**, el Rey Dragón), Epílogo, Academy
Arc. Fuente: [wiki: Story Arcs](https://solo-leveling.fandom.com/wiki/Story_Arcs) ✅.

**Emblemas de gremio** (medidos por su tamaño real vía API; **mirados**) ✅
| Gremio | Emblema | Tamaño | Fuente |
|---|---|---|---|
| **Ahjin** (el de Jinwoo) | fénix/llama violeta estilizada, `#9229F9`-ish, sobre fondo transparente | 700×700 | [wiki](https://static.wikia.nocookie.net/solo-leveling/images/8/88/Ahjin.png) ✅ |
| **Gremio de Cazadores** (Hunters Guild) | escudo gris con espada vertical, gótico | 480×480 | [wiki](https://static.wikia.nocookie.net/solo-leveling/images/8/89/Insignia_Hunters.png) ✅ |
| **Tigre Blanco** (White Tiger) | cabeza de tigre de líneas blancas finas, casi invisible sobre fondo claro | 140×140 | [wiki](https://static.wikia.nocookie.net/solo-leveling/images/e/ee/Insignia_White_Tiger.png) ✅ |
| **Caballería** (Chivalry) | forma de «人» (persona) estilizada en azul oscuro, como alas o cuernos | 529×471 | [wiki](https://static.wikia.nocookie.net/solo-leveling/images/d/d7/Insignia_Chivalry.png) ✅ |
| Fama (Fame), Segadores (Reapers), Carroñero (Scavenger), Japón | insignias propias, sin mirar en detalle (menos relevantes para #guia) | 140×140 / 361×399 / 600×600 | wiki ⚠️ (tamaño sí, diseño no descrito) |

Los vi (montados en una hoja de contacto propia de 4, `/tmp/…/contacto_logos.jpg`,
no subida al repo: es sólo de trabajo). **El de Ahjin (violeta) es el más
útil para la lámina**: coincide con la paleta Monarca ya establecida
(`#9229F9`/`#ED77F3`).

**Objetos icónicos**
- **Ventana del Sistema** y su marco Monarca (ya en biblia §4, no repito).
- **Espada del Rey Demonio** (Demon King's Longsword): la usó **Baran**,
  Jinwoo se la quita y se la da a **Igris**; décadas después pasa a **Cha
  Hae-In**. Hoja clara con línea negra central, guarnición arqueada — [wiki, wikitext](https://solo-leveling.fandom.com/wiki/Demon_King%27s_Longsword) ✅. Ya
  aparece en el anime (Igris la lleva desde el ep. 12).
- **La Ira de Kamish** (Kamish's Wrath): par de dagas hechas con el colmillo
  del dragón Kamish, +1500 ataque; naranjas con filo rojo sangre (webtoon)
  o blanco hielo (novela) — [wiki, wikitext](https://solo-leveling.fandom.com/wiki/Kamish%27s_Wrath) ✅. **Aún no sale en el
  anime** (es del arco de la Conferencia Internacional de Gremios, sin
  animar): para la lámina, sólo si se anima una T3.
- **La Estatua del Dios** (ya en biblia, Normas/lámina 2): el wikitexto
  explica el juego de palabras coreano **신상 (Shin-Sang)** = 神 «dios» +
  像 «estatua» — [wiki: Statue of God](https://solo-leveling.fandom.com/wiki/Statue_of_God) ✅. Dato nuevo para el redactor,
  si quiere una nota de curiosidad.

**Vocabulario que un fan reconoce** (reutilizo el latino ya comprobado en
la biblia §4/§6, más lo que falta)
| Español latino (doblaje, ✅ ya en biblia) | Original | Nota |
|---|---|---|
| **Portal** | Gate | |
| **Mazmorra** | Dungeon | |
| **Asociación de Cazadores** | Hunters Association | |
| **Rango E…S** | E-Rank…S-Rank | |
| **Gremio** | Guild | |
| **Soldados sombríos** | Shadow soldiers | |
| **Perjuicio** | debuff | |
| **«Surge.»** | «Arise.» | orden de extracción; el momento más citado |
| **Rey de las Sombras** | Shadow Monarch | **no** «Monarca de las Sombras» |
| **Monarca** (sólo para otros) | Monarch | p. ej. «Monarca Demoníaco Baran» |
| **Licencia de Cazador** | Hunter's License | |

*Sin doblaje latino todavía (arcos sin animar; en inglés/coreano, para que
el redactor decida si hacen falta)* ⚠️
| Original | Qué es |
|---|---|
| Architect (Kandiaru) | el «moderador» del Sistema |
| Monarchs / Rulers | los dos bandos de la guerra cósmica detrás del Sistema |
| Red Gate | portal-trampa que no se puede cerrar por fuera |
| Essence Stone / Mana Crystal | el «loot» económico de las mazmorras |
| Dungeon Break | cuando una mazmorra revienta al mundo real |
| Itarim | concepto de «un dios por universo»; Chugong lo simplificó a propósito para no ser muy sombrío ([CBR](https://www.cbr.com/solo-leveling-chugong-interview-removed-itarim-light-novel-bleak/) ✅) |

---

## Lo mejor para la lámina

1. **La regla de estilo del director, en una frase**: «como imagen real,
   sin gestos cartoon» → para cualquier cuadro con fotograma del anime,
   casi sin línea negra, fondo desenfocado y grano fino; para un cuadro
   tipo manga/webtoon, línea negra limpia. Es la diferencia medida entre
   el fotograma de Igris y la viñeta de la nieve (arriba).
2. **El emblema de Ahjin** (violeta, 700×700, ya en la paleta Monarca) es
   el logo de gremio más reutilizable: cabría como marca de agua o sello
   en cualquier concepto de #guia.
3. **El aviso cruzado de One Piece y Attack on Titan**: el tablón de
   corcho del Concepto B ya es «territorio ocupado» por Solo Leveling en
   el servidor — no tocarlo, y si se rehace, que siga siendo corcho (no
   madera de barco).
4. **La lista de arcos con su tramo de episodio** sirve directamente para
   una «línea de tiempo» en un hilo tipo «De qué va esto»: 14 arcos del
   anime en un renglón cada uno.
5. **Tower of God / The Eminence in Shadow** son el par que un fan
   mencionará solo; si se hace un evento cruzado o una encuesta, son los
   candidatos más seguros (más votados y más citados en medios).

## No encontré

- ⚠️ Entrevista **directa de Chugong** (coreana o traducida) sobre sus
  influencias de videojuego: sólo un blog de la tienda oficial lo dice de
  pasada. Busqué «Chugong interview influences», «추공 인터뷰 나 혼자만
  레벨업 영감 게임», «Chugong 추공 인터뷰 나 혼자만 레벨업 영감 게임»: nada
  directo. Queda como dudoso.
- ⚠️ Entrevista de **Dubu (Jang Sung-rak)** sobre su proceso de dibujo
  (programa, capas): no hay ninguna en inglés ni coreano que encontrara;
  murió en 2022 y dio muy pocas entrevistas en vida.
- ❌ **TV Tropes** (`Literature/SoloLeveling`, `Anime/SoloLeveling`): sigue
  dando 403 (con WebFetch y con curl); tampoco hay copia en Wayback
  (`archived_snapshots` vacío). Dos intentos, como marca `AYUDANTE.md`; no
  insistí más.
- ⚠️ **namu.wiki** (`.../설정`, la página de «ajustes» del mundo): 403
  directo y por WebFetch. Sí saqué contenido suyo **indirecto**, vía los
  fragmentos que devolvió el buscador (Guilds, Asociación de Cazadores en
  coreano), pero no pude abrir la página entera. Cuenta como una fuente
  coreana adicional, aunque débil.
- No es que falte: **texturas 2D del punto 19** y **videojuegos del punto
  11** son de otros compañeros (imagen y una revisión anterior de texto);
  no los toqué, tal y como pide el encargo de este repaso.

## Bitácora

- **Fandom (`solo-leveling.fandom.com`), API directa** (`action=parse`,
  `action=query&list=search`, `list=allpages`, `list=allimages`): páginas
  `Story Arcs`, `Guilds`, `Class Ranks`, `Statue of God`, `Kamish's Wrath`,
  `Demon King's Longsword`, `Architect`, más `imageinfo` de 9 insignias de
  gremio. Sin límite de búsqueda web gastado.
- **WebSearch** (9 búsquedas de 50): «Solo Leveling anime A-1 Pictures
  making of interview 3DCG toon shader system window» · «ソロレベリング
  アニメ 制作 インタビュー システムウィンドウ CG 監督» · «Chugong Solo
  Leveling author interview influences inspired by» · «추공 인터뷰 나
  혼자만 레벨업 영감 게임» · «Chugong 추공 인터뷰 나 혼자만 레벨업 영감 게임»
  · «anime like Solo Leveling similar recommendations Tower of God
  Eminence in Shadow» · «tvtropes.org Solo Leveling anime tropes
  site:tvtropes.org» · «Solo Leveling anime cinematography camera angles
  composition analysis sakuga» · «"Solo Leveling" anime director
  Nakashige interview 演出 カメラ 構図» · «Solo Leveling anime
  "chromatic aberration" OR "film grain" OR "bloom"» · «Dubu Redice
  Studio Solo Leveling webtoon art interview» · «A-1 Pictures animation
  software RETAS Toon Boom "CLIP STUDIO" digital ink 2D anime
  production».
- **WebFetch**: Sony XYN (caso de estudio oficial), Anime Corner («cómo se
  hizo»), Awards Radar (entrevista al equipo), VFX Voice (entrevista al
  equipo), CBR (dos artículos: expresiones «cartoon», el Itarim), namu.wiki
  (403), tvtropes.org (403).
- **Sketchfab API**: búsqueda `q=solo leveling downloadable=true` (24
  resultados) + `models/<uid>` para licencia y tamaño de 4 modelos.
- **Wayback Machine**: comprobado `tvtropes.org` (sin copia) y
  `namu.wiki/.../설정` (con copia, pero 403 al leerla).
- **Imágenes propias, medidas y miradas**: `Anime_Episode_11_Picture_5.png`
  (1366×768) y `Chapter_50.png` (574×778) con `herramientas/estilo.py
  --colores 6`; 4 insignias de gremio montadas en una hoja de contacto
  propia (`/tmp/.../contacto_logos.jpg`) y miradas con `Read`.
- **Biblias del servidor comprobadas por su índice** (`seccion.py
  --indice`, no leídas enteras): One Piece, Attack on Titan, Jujutsu
  Kaisen, Demon Slayer, Naruto, My Hero Academia, One Punch Man (éste y
  Attack on Titan sí se leyeron sus secciones 25-27 / 24 enteras, por ya
  tener el punto 24/25 hecho, como referencia de formato) y Frieren
  (colaboración con ARISE).
