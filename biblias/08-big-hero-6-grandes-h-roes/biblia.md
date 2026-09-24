---
tags: [biblia, serie, laminas]
serie: "Big Hero 6 (Grandes Héroes)"
canal: "#soporte"
fecha: 2026-09-24
---

# Biblia · Grandes Héroes (Big Hero 6) — para #soporte

> [!important] Cómo se hizo esta investigación
> - **Primera pasada (red cerrada)**: Fandom, Doblaje Wiki, Wikipedia,
>   YouTube, TV Tropes, IMP Awards, Poly Haven, Sketchfab, audiofrases,
>   la web de Wong-Baker y la de la CMU daban error 403 o 000. Se usó el
>   buscador web (**49 búsquedas**, en español, inglés, japonés, chino y
>   coreano) y GitHub: la ficha de Anime News Network del manga y **24
>   letras de Google Fonts** comprobadas letra a letra (Kosugi Maru **no**
>   trae tildes). No se vio ninguna imagen ni vídeo.
> - **Segunda pasada (24-sep-2026, red abierta)**: un equipo de **cuatro
>   investigadores** (imagen, vídeo, voz, texto) y un redactor. Se pudo
>   usar: las APIs de Fandom (`disney` y `bighero6`), Doblaje Wiki, The
>   Dubbing Database, Sketchfab, Wallhaven, ambientCG, Wikipedia y
>   Dailymotion; **7 hojas de contacto** (299 imágenes de la wiki,
>   miradas todas); **9 clips de Dailymotion e Internet Archive mirados**
>   con `fotogramas.py` (el tráiler latino entero, 92 fotogramas);
>   **3 clips doblados oídos** con `voz.py` (frases textuales con minuto);
>   **colores medidos** con Pillow y `estilo.py`; 9 letras comprobadas con
>   fontTools.
> - **Lo que no se pudo**: YouTube pidió iniciar sesión todo el día
>   («Sign in to confirm you're not a bot»), TikTok no deja ver vídeos,
>   TV Tropes y Memedroid dieron 403, Wayback Machine cortó la conexión.
>   Por eso los minutos son **del clip citado**, no de la película entera.
> - ✅ = confirmado en dos fuentes o visto. ⚠️ = dudoso, una sola fuente o
>   de memoria. ❌ = no hecho o no sirve.

> [!note] Segunda pasada · qué cambió
> (se completa al terminar el repaso)

> [!tip] Índice
> 1 El canal · 2 El más querido · 3 Arte oficial y **hojas de contacto**
> (§3.0) · 4 Escenas con minuto · 5 3D y fan art · 6 Sitios, luz y
> paleta · 7 Tipografía · 8 Cuadro de diálogo · 9 Personajes · 10 Doblaje
> latino · 11 Música · 12 Vídeos · 13 Videojuegos · 14 Fandom y qué no
> hacer · 15 Poses · 16 Vestuario · 17 Fondos · **A** Técnica (punto 18)
> · **B** Texturas 2D (19) · **C** Gustos (20) · **D** Por qué la aman
> (21) · **E** Fan dubs (22) · **F** Colaboraciones (23) · **G** Obras
> parecidas (24) · **H** El mundo (25) · 18 Guía para IA de imagen y de
> texto (punto 17) · 19 Tres conceptos · 20 Lo no verificado · 21
> Fuentes · Cumplimiento del encargo · 22 Bitácora.

---

## 1 · El canal y lo que tiene que decir

**Canal:** `ıı・🎫・soporte`, en la categoría ✦ EMPIEZA AQUÍ ✦.
Texto real del canal: *«Abre un ticket: solo lo vemos tú y el staff.»*
Tiene 0 mensajes fijados ([inventario](../../servidor/inventario.md)).

**Función del encargo:** abrir un ticket privado con el staff, y una
**tabla del dolor** para decir cuán grave es.

**Por qué Grandes Héroes encaja tan bien:** Baymax es un robot enfermero.
Su manía es preguntar **del 1 al 10 cuánto te duele** y en su pecho
sale una **escala de caras** del dolor, la escala Wong-Baker de los
hospitales reales ✅ ([TV Tropes, Funny](https://tvtropes.org/pmwiki/pmwiki.php/Funny/BigHero6),
[Rated PT](https://ratedpt.wordpress.com/2021/02/16/big-hero-6-on-a-scale-of-1-10/)).
Y **no se apaga hasta que el paciente dice «estoy satisfecho con mi
cuidado»**. Eso es un ticket: se abre con un dolor y se cierra cuando la
persona queda bien. En el doblaje latino, Baymax lo dice así: **«Puedo
desactivarme si dices que estás satisfecho con tu cuidado.»** ✅ (oído,
[Dailymotion x5hvz3y, 0:55](https://www.dailymotion.com/video/x5hvz3y?t=55); punto 10).

**La tabla del dolor de verdad existe y se vio** (segunda pasada):
- **Película**: al activarse, el pecho de Baymax enciende la escala de
  10 caras ✅ (visto, [clip «Meet Baymax», 1:02](https://www.dailymotion.com/video/x2553ox?start=62)).
- **Serie de TV**: su pecho proyecta una **cajita blanca redondeada con
  10 caritas en 2 filas de 5**, numeradas del 1 al 10 debajo, de
  **amarillo** (sin dolor) a **naranja** y **rojo** ✅ (visto y medido,
  [Scale_8.png, 1280×720](https://static.wikia.nocookie.net/bighero6/images/2/28/Scale_8.png)).
  Hex medidos: fondo `#FDF9EF` / `#FAE8D7`, cara 1 `#F1E815`, caras 6-7
  `#EDB413`, cara 10 `#F0764E`.
- Baymax la presenta con su frase de guion: «On a scale of 1 to 10, how
  would you rate your pain?» ✅ ([transcripción](https://bighero6.fandom.com/wiki/Big_Hero_6_(film)/Transcript)).
  En latino circula «En una escala del uno al diez, ¿cómo calificarías
  tu dolor?» ⚠️ (sin oír; punto 10).
- La tabla vive **proyectada sobre el vinilo**: Baymax tiene un proyector
  en el pecho ✅ ([ficha de Baymax](https://bighero6.fandom.com/wiki/Baymax)).

> [!warning] Falta un dato del servidor
> El inventario no dice **cómo** se abre el ticket (botón de un bot,
> comando, mensaje). Hay que preguntarlo antes de rotular el paso 1.

### Textos propuestos (voz de Baymax, una idea cada uno)

| Pieza | Texto exacto |
|---|---|
| Título | **¿CUÁNTO TE DUELE?** |
| Baymax, saludo | **Hola. Estoy aquí para ayudarte.** |
| Paso 1 | **Abre un ticket.** |
| Paso 2 | **Solo lo vemos tú y el staff.** |
| Paso 3 | **Dinos del 1 al 10 cuánto te duele.** |
| Pie | **El ticket se cierra cuando digas que estás satisfecho con tu cuidado.** |

- El saludo y la escala son **adaptaciones**, no citas. Las frases
  latinas reales están en el punto 10, con su estado.
- El pie imita la frase de Baymax en el doblaje latino: «…si dices que
  estás satisfecho con **tu** cuidado» ✅ (oída, punto 10). Hiro, al
  final, responde en primera persona: «Estoy satisfecho con mi cuidado»
  (dos fuentes de texto, ⚠️ sin oír en el clip).
- **Del 1 al 10**, no del 0: así la cuenta Baymax en pantalla y en su
  frase (antes decía «del 0 al 10»).
- Sin «·», «—» ni paréntesis. Cada texto va en su sitio del objeto.

### La tabla del dolor del servidor (propuesta, falta su sí)

Se copia **la forma de la tabla de la serie**: caja blanca redondeada,
10 caritas en 2 filas de 5, números del 1 al 10 debajo y el degradado
amarillo → naranja → rojo con los hex medidos arriba. Los cinco niveles
del servidor son parejas de caritas. La escala numérica de dolor de los
hospitales va del 0 al 10 ([Nurse-Link, Corea](https://nurse-link.co.kr/community/campus_talk/108851764));
aquí se empieza en 1, como Baymax. Las caras se dibujan **al estilo de
Baymax** (dos puntos y una raya), no se copian las de Wong-Baker (ver
aviso de licencia en el punto 3).

| Nivel | Cara | Nombre | Ejemplos |
|---|---|---|---|
| 1 a 2 | tranquila | **Una duda** | No encuentras un canal. No sabes cómo va algo. |
| 3 a 4 | leve | **Algo no funciona** | Un rol que no te sale. Un bot que no responde. |
| 5 a 6 | molesta | **Me incomoda** | Un roce con alguien. Algo que te sentó mal. |
| 7 a 8 | mucho | **Urgente** | Acoso. Spam. Algo que no debería estar. |
| 9 a 10 | máximo | **Emergencia** | Amenazas. Datos personales expuestos. Cuenta robada. |

**Los ejemplos son míos.** El dueño tiene que decir qué entra en cada
nivel y si el staff responde antes a los niveles altos.

### Lámina 2 (si la primera se llena)

«La ficha completa del paciente»: la tabla con los cinco niveles y sus
ejemplos, más dos avisos que ya existen en el servidor:
- **Si es una idea y no un dolor**, va a **#sugerencias**
  («Propón mejoras para el servidor», foro con etiquetas Nueva, En
  estudio, Aprobada, Rechazada, Hecha) ([inventario](../../servidor/inventario.md)).
- **Si no estás de acuerdo con una sanción**, se habla por soporte. Lo
  dice ya la biblia de #reglas (Attack on Titan, lámina 2, pendiente de
  su sí) ([biblia AoT](../_ya_hechas/Attack%20on%20Titan.md)).

---

## 2 · ¿Quién es el más querido?

**Respuesta corta: Baymax.** No es el protagonista de la historia (es
Hiro), pero sí la cara de todo.

- **No encontré ninguna encuesta oficial** de Disney por personajes.
- **Japón:** la película se llama allí **«ベイマックス» (Baymax)**, no
  «Big Hero 6» ✅ ([ANN en GitHub](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/manga/16985.json),
  [Wikipedia JA](https://ja.wikipedia.org/wiki/%E3%83%99%E3%82%A4%E3%83%9E%E3%83%83%E3%82%AF%E3%82%B9)).
  Recaudó **91,8 億円 (unos 9.180 millones de yenes) y 7,2 millones de espectadores**;
  en Disney sólo la supera Frozen ⚠️ (dato del resumen del buscador,
  sin abrir la página; [Wikipedia JA](https://ja.wikipedia.org/wiki/%E3%83%99%E3%82%A4%E3%83%9E%E3%83%83%E3%82%AF%E3%82%B9),
  [eiga.com](https://eiga.com/movie/80460/)).
- **Encuesta de fans japonesa** (みんなのランキング), **abierta entera**
  el 24-sep-2026 (la web dice «última actualización: 2026/09/21»; sigue
  recibiendo votos) ✅ ([ranking.net](https://ranking.net/rankings/best-baymax-characters)):

| Puesto | Personaje | Puntos | Evaluadores | Voz japonesa |
|---|---|---|---|---|
| 1.º | **Baymax** | 97,4 | 99 | 川島得愛 |
| 2.º | Hiro | 90,9 | 70 | 本城雄太郎 |
| 3.º | **GoGo** | 80,2 | 44 | 浅野真澄 |
| 4.º | Tadashi | 79,5 | 47 | 小泉孝太郎 |
| 5.º | **Mochi, el gato** | 79,4 | 25 | — |

  La primera pasada vio por el buscador 97,9 con 86 votos: los números
  se mueven, el orden no. **Hasta el gato Mochi queda casi empatado con
  Tadashi.**
- **Taquilla mundial**: 657,8 millones de dólares, la animada más
  taquillera de 2014; **Japón aportó 76 millones** ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Big_Hero_6_(film)),
  [Box Office Mojo](https://www.boxofficemojo.com/release/rl2708621313/)). Más en §D.
- **China:** allí le llaman **«大白» (el Gran Blanco)**. Los peluches se
  agotaron en internet ([China News](https://www.chinanews.com.cn/m/cul/2015/03-02/7092799.shtml),
  [China Daily](http://china.chinadaily.com.cn/shizheng/2015-03/06/content_19740449.htm)).
  La prensa le llamó **«暖男»** (el chico tierno) y **«大众情人»** (el
  amor de todos) ✅ ([36Kr](https://36kr.com/p/1478767128599810),
  [People's Daily](http://paper.people.com.cn/rmrbhwb/html/2015-04/03/content_1549893.htm),
  [Sanlian](https://www.lifeweek.com.cn/article/149429)).
  Estrenó el 28 de febrero de 2015: 85 millones de yuanes el primer fin
  de semana, más de 500 millones después ⚠️ (resumen del buscador).
- **La tabla del dolor ya es un objeto de fans**: hay pines oficiales y
  mercancía con «Baymax Pain Scale» ✅ ([Hot Topic](https://www.hottopic.com/product/disney-big-hero-6-baymax-pain-scale-3-pin/10396449.html),
  [BoxLunch](https://www.boxlunch.com/product/loungefly-big-hero-6-baymax-pain-scale-retractable-lanyard---boxlunch-exclusive/16997490.html),
  [PinPics, pin de Japón](https://pinpics.com/pin/162835/)).
- **Tadashi es el más llorado.** En Pixiv la etiqueta «タダシ» tiene 272
  ilustraciones y 34 novelas ⚠️ ([Pixiv, diccionario](https://dic.pixiv.net/a/%E3%82%BF%E3%83%80%E3%82%B7%E3%83%BB%E3%83%8F%E3%83%9E%E3%83%80)).
  En 2026 su voz latina, **Alexis Ortega, murió** (24 de enero), y hubo
  vídeos homenaje ✅ ([El Imparcial](https://www.elimparcial.com/espectaculos/2026/01/27/fallece-alexis-ortega-voz-de-spider-man-en-espanol-latino-y-tadashi-en-grandes-heroes/),
  [Infobae](https://www.infobae.com/mexico/2026/01/27/muerte-de-alexis-ortega-a-que-personajes-dio-voz-el-actor-ademas-de-spider-man-de-tom-holland/),
  [TikTok homenaje](https://www.tiktok.com/@lavidadeldoblaje_/video/7600428235201006868)).
- Un fan de Fanpop pone primero a Honey Lemon: es una opinión suelta, no
  una encuesta ([Fanpop](https://www.fanpop.com/clubs/big-hero-6/articles/252355/title/review-big-hero-6-characters));
  revisado otra vez: no tiene conteo de votos.
- **Encuesta oficial de Disney por personajes**: se volvió a buscar en
  inglés y japonés («ビッグヒーロー6 人気投票 公式») y **no la encontré**.

**Para #soporte:** Baymax habla. Hiro puede ser «el paciente» que abre
el ticket. Tadashi, como mucho, un guiño (su gorra), por respeto.

---

## 3 · Arte oficial reunido (y las hojas de contacto)

### 3.0 · Las hojas de contacto (segunda pasada) ✅

`investigar_serie.py` bajó **299 imágenes** de las galerías de Baymax,
Hiro y Tadashi en `disney.fandom.com` y montó 7 hojas numeradas. El
investigador de imagen las miró todas y eligió tres; el redactor las
volvió a mirar. Cada número lleva debajo su tamaño real y su archivo.
Los originales de todas están en `herramientas/referencias/big-hero-6-grandes-h-roes/indice.json`.

**`hojas/arte_oficial_01.jpg`** (números 1-48: pósters, libros, renders)

| N.º | Qué es | Tamaño | Sirve para |
|---|---|---|---|
| **44** | **Póster latino oficial «Un consejo saludable traído por GRANDES HÉROES»**: Baymax **señala con el índice su pecho encendido**, que muestra un icono y el aviso «¡NO USES TU CELULAR MIENTRAS CONDUCES!» | 1433×2048 | **el mejor precedente para #soporte**: Baymax ya dio avisos en español con su pecho como pantalla ([original](https://static.wikia.nocookie.net/disney/images/3/32/Big-Hero-6-107.jpg)) |
| 19 | Hiro señala hacia arriba con el índice, sudadera abierta y camiseta roja | 3000×1996 | **explicar / señalar** ([original](https://static.wikia.nocookie.net/disney/images/4/4a/Hiro_at_Disney%27s_Hollywood_Studios.jpg)) |
| 16 | Fotograma: Baymax abraza a Hiro | 4096×1716 | consuelo, ticket cerrado ([original](https://static.wikia.nocookie.net/disney/images/4/4d/BH6_still_Baymaxhug.jpg)) |
| 17 | Hiro sentado sobre Baymax, fondo blanco | 2053×3383 | presentar al dúo ([original](https://static.wikia.nocookie.net/disney/images/c/c1/Hiro_and_Baymax.jpg)) |
| 1 | El equipo entero de civil, de pie, fondo blanco | 5000×3273 | láminas de grupo ([original](https://static.wikia.nocookie.net/disney/images/b/ba/BigHero6Team2.jpg)) |
| 29 · 30 | Páginas de *The Essential Guide*: Baymax y Baymax 2.0 **con rótulos y flechas** | 2560×1674 | **modelo de la lámina 2** con etiquetas ([29](https://static.wikia.nocookie.net/disney/images/0/03/Big_Hero_6_Essential_Guide_Bay%2Cax_2.0.jpg), [30](https://static.wikia.nocookie.net/disney/images/b/b6/Big_Hero_6_Essential_Guide_Baymax.jpg)) |
| 33 | Todos los personajes en fila, a escala | 3509×1195 | alturas relativas ([original](https://static.wikia.nocookie.net/disney/images/e/e4/Big_Hero_6_Characters.png)) |
| 20 · 21 · 22 · 43 | Pósters: internacional (Hiro con cuaderno morado y Baymax con armadura), Baymax blanco de cerca, coreano «빅 히어로» con Tadashi, japonés «ベイマックス» | 1985×2835 · 1984×2835 · 1978×2835 · 1448×2048 | vestuario y tono ([20](https://static.wikia.nocookie.net/disney/images/c/ca/Big_Hero_6_poster_2.jpg), [22](https://static.wikia.nocookie.net/disney/images/9/9f/Hiro_Baymax_Tadashi_International_Poster.jpg)) |
| 40 · 41 | Pósters «de estilo» japonés retro, con «S.F.» y katakana | 1583×2048 | cartel del mundo ([40](https://static.wikia.nocookie.net/disney/images/a/af/Big_Hero_6_Baymax_style_poster.jpg), [41](https://static.wikia.nocookie.net/disney/images/e/ea/Big_Hero_6_Hiro_style_poster.jpg)) |
| 35 · 36 | Renders: Baymax con armadura (KH3) e Hiro con armadura agachado | 2210×1846 · 2076×1773 | poses de acción ([35](https://static.wikia.nocookie.net/disney/images/f/fd/KH3_-_Baymax_Render.png), [36](https://static.wikia.nocookie.net/disney/images/7/7e/Hiro_Pose.png)) |
| 4-13 | Capturas de Disney Infinity 2.0 | 3840×2160 | sólo colaboraciones (§F) |

**`hojas/vestuario_concept_01.jpg`** (números 49-96: arte conceptual, serie, parques)

| N.º | Qué es | Tamaño | Sirve para |
|---|---|---|---|
| **92** | **Nota a mano de Tadashi** en el diario de Hiro, con su foto sujeta con un clip: «You have lots of great ideas! Here is a place to keep track of them… NEVER stop inventing! Love, Tadashi» | 1191×1671 | **objeto de papel real** para un concepto (§19) ([original](https://static.wikia.nocookie.net/disney/images/d/de/Tadashi_in_hiros_journal.png)) |
| **93** | Baymax saluda con la mano, fondo gris | 1318×1500 | **saludar / presentar** ([original](https://static.wikia.nocookie.net/disney/images/2/29/Baymax_waving.jpg)) |
| 51 | Portada del libro «Hiro's Journal» («DO NOT TOUCH!», «KEEP OUT!») | 1280×1869 | cuaderno como objeto ([original](https://static.wikia.nocookie.net/disney/images/7/76/Hiro%E2%80%99s_Journal.jpg)) |
| 72 | Primer plano de Hiro preocupado | 1380×1600 | cara de «me duele» ([original](https://static.wikia.nocookie.net/disney/images/2/21/Profile_-_Hiro_Hamada.jpeg)) |
| 78 · 79 | Fotos reales: Baymax de parque junto a visitantes | 1920×1080 | escala humana real ([78](https://static.wikia.nocookie.net/disney/images/6/6e/Baymax_and_Hiro_in_Disney%27s_Hollywood_Studios.jpg), [79](https://static.wikia.nocookie.net/disney/images/3/34/Hiro_and_Baymax_at_a_special_event.jpg)) |
| 55 · 75-77 | Arte conceptual de Hiro firmado por Shiyoon Kim | 1242×1920 · 1086×1920 | estilo de diseño |
| 53 · 74 | Bocetos tempranos de Baymax (uno sentado junto a un gato) | 1242×1920 · 1280×1671 | volumen y pliegues |
| 60 | La noticia «San Fransokyo Loses Local Hero TADASHI HAMADA» en una pantalla (serie) | 2048×1147 | tono; no usar en #soporte ([original](https://static.wikia.nocookie.net/disney/images/0/02/Hiro_the_Villain_%2812%29.jpg)) |
| 89 · 59 | Tadashi sonriente con gorra (serie) | 1920×1080 · 2048×1147 | guiño a Tadashi |
| 94-96 | Arte conceptual de San Fransokyo de noche y del cuarto de Hiro | 2000×981 | fondos |

**`hojas/colaboraciones_01.jpg`** (números 193-240: juegos, cartas, promos, manga)

| N.º | Qué es | Tamaño | Sirve para |
|---|---|---|---|
| **240** | Página de revista japonesa: Baymax de pie con **etiquetas redondas de color** (FACE verde, HEART rojo, BODY naranja, STYLE azul) unidas por **flechas de puntos** | 700×1053 | **lámina 2**: así se rotula a Baymax en Japón. El inglés es de un escaneo de fans ([original](https://static.wikia.nocookie.net/disney/images/d/d9/Baymax_Manga_Diagram.jpg)) |
| 201 | Cartel «Meet Baymax at booth #3635A» (SDCC 2014) con Baymax saludando | 960×960 | cartel de aviso ([original](https://static.wikia.nocookie.net/disney/images/c/c0/MeetBaymaxSDCC2014.png)) |
| 199 | Baymax sostiene una rosa, fondo rojo | 960×960 | tierno ([original](https://static.wikia.nocookie.net/disney/images/3/3b/Baymax_with_a_Rose_in_his_hand.png)) |
| 213 | Arte conceptual: el equipo en el Lucky Cat Café («OPEN») | 1280×710 | sitio cálido ([original](https://static.wikia.nocookie.net/disney/images/2/25/Big_hero_6_team_enjoying_themselves_concept_art.jpg)) |
| 204 | Hiro en *Disney Heroes: Battle Mode* con sus **SKILLS** (Megabot Call, Megabot Spin, Microbot Stun, Analyze) | 960×960 | interfaz de juego ([original](https://static.wikia.nocookie.net/disney/images/2/2e/Hiro_Hamada_DHBM_Promo.jpg)) |
| 214-216 · 228-229 · 232-233 | Cartas de **Disney Lorcana** (Hiro, Honey Lemon, Baymax con armadura) | 744-800 × 1024-1118 | poses nuevas (§F) ([Baymax](https://static.wikia.nocookie.net/disney/images/0/0d/Baymax_-_Armored_Companion_lorcana.jpg)) |
| 236 | Conceptos de ropa de Tadashi: gorra negra, chaqueta verde | 682×1099 | vestuario de la película (§16) ([original](https://static.wikia.nocookie.net/disney/images/f/fc/Tadashi_outfit_concepts_3.png)) |
| 238 | Portada japonesa del capítulo 0 del manga «ベイマックス» | 700×1057 | manga ([original](https://static.wikia.nocookie.net/disney/images/2/20/Baymax_Chapter_0_Cover.jpg)) |
| 220 | Portada de *The Art of Big Hero 6* | 1024×833 | libro de arte |
| 226 | Baymax atascado en la puerta de un tren (promo) | 1024×779 | gag de volumen |
| 230 | Hoja de modelo de Hiro niño, firmada «Modeler Suzan Kim» | 1024×750 | modelo 3D |

Medido en el **póster latino n.º 44** con Pillow: cielo `#B1CCE7`,
caja del logo `#C1151A`, raya roja del icono `#D41932`, icono azul
`#496CA2`, texto del pecho rojo salmón que brilla ≈ `#E08080`, pantalla
del pecho `#FFFFFF`, vinilo en luz `#E8F2FA`.

### Pósters de cine (IMP Awards, 20 versiones)
La galería tiene **20 pósters oficiales**. Tamaños que da el buscador
([galería](http://www.impawards.com/2014/big_hero_six_gallery.html)):

| Póster | Tamaño | Enlace |
|---|---|---|
| n.º 1 | 1023×1517 | [ver](http://www.impawards.com/2014/big_hero_six.html) |
| n.º 2 | 1432×2048 | [ver](http://www.impawards.com/2014/big_hero_six_ver2.html) |
| n.º 6 | 1125×1500 | [ver](http://www.impawards.com/2014/big_hero_six_ver6.html) |
| n.º 7 | 1024×1444 | [ver](http://www.impawards.com/2014/big_hero_six_ver7.html) |
| n.º 13 | 1433×2048 | [ver](http://www.impawards.com/2014/big_hero_six_ver13.html) |
| n.º 17 | 1080×1920 | [ver](http://www.impawards.com/2014/big_hero_six_ver17.html) |
| n.º 20 | 1978×2835 | [ver en grande](http://www.impawards.com/2014/big_hero_six_ver20_xxlg.html) |

Los de IMP Awards siguen sin abrirse desde aquí. **Los mismos pósters
están en la wiki y sí se vieron** en la hoja `arte_oficial_01.jpg`
(n.º 20, 21, 22, 39-45), con tamaño medido por la API (§3.0).
Más pósters de otros países, vistos: japonés «ベイマックス» **1024×1444**
([archivo](https://static.wikia.nocookie.net/disney/images/9/9b/BH6_-_Japanese_Poster.jpg)),
coreano «빅 히어로» (n.º 22) y chino «大白你好» con promo cruzada de
*Zootopia* (n.º 68) ✅.

### Hojas de modelo y arte firmado (vistos en las hojas)
- **Turnarounds de Shiyoon Kim**: Hiro saltando en snowboard con
  mochila, 6 variantes, 1242×1920; bocetos de «Ninja Hiro» con traje
  oscuro y casco ✅.
- **Hojas de modelo 2015** (para la serie) firmadas «Modeler Brandon
  Lawless», «Modeler Suzan Kim» y «Modeler Dylan Ekren»: Hiro, Tadashi,
  GoGo y Cass ✅ ([Tadashi y GoGo, 1024×1225](https://static.wikia.nocookie.net/disney/images/3/32/Tadashi_and_Go_Go_character_model.jpg)).
- **Libros**: «Hiro and Tadashi» 2770×3338, *Big Golden Book* 2062×2560,
  *Read Along* 2560×2559 ✅ (tamaños de la API).
- **Parches de fieltro japoneses** «Hiro & Baymax» (Disney Store Japón),
  arte chibi con puntada visible, 800×800 ✅ ([archivo](https://static.wikia.nocookie.net/disney/images/2/2d/Wappen_Hiro_and_Baymax.jpg)).

### El libro de arte
**The Art of Big Hero 6**, de Jessica Julius (Chronicle Books, octubre de
2014, 160 páginas). Prólogo de Don Hall y Chris Williams ✅
([Google Books](https://books.google.com/books/about/The_Art_of_Big_Hero_6.html?id=WNmqBwAAQBAJ),
[reseña de AWN](https://www.awn.com/animationworld/book-review-art-big-hero-6)).
**60 de sus 160 páginas son diseño de personajes** ⚠️
([Character Design blog](https://characterdesign.blogspot.com/2016/08/the-art-of-big-hero-6.html)).
Hay copias del libro subidas a visores de páginas: no son oficiales y no
se usan.

### Bocetos del equipo (blogs de los artistas)
- **Kevin Nelson** (Disney) colgó bocetos tempranos de Baymax, **Baymax
  con el esqueleto a la vista** en varias poses (sobre dibujos de Shiyoon
  Kim) y arte con Baymax ✅
  ([bocetos tempranos](http://artofkevinnelson.blogspot.com/2014/12/some-really-early-baymax-sketches-from.html),
  [poses con esqueleto](http://artofkevinnelson.blogspot.com/2014/11/baymax-poses-with-visible-skeleton-from.html),
  [Baymax, Togo y Yama](http://artofkevinnelson.blogspot.com/2014/11/big-hero-6-artwork-with-baymax-togo-and.html),
  [GoGo temprana](http://artofkevinnelson.blogspot.com/2014/11/early-gogo-from-big-hero-6.html)).
  **Son lo mejor para saber cómo dobla el cuerpo Baymax.**
- Diseño de personajes: **Shiyoon Kim, Jin Kim y Lorelay Bove**;
  diseño de producción: **Paul Felix**; con Scott Watanabe y otros ✅
  ([Escape Studios](https://escapestudiosanimation.blogspot.com/2017/10/big-hero-6-character-design-secrets.html),
  [Character Design blog](https://characterdesign.blogspot.com/2016/08/the-art-of-big-hero-6.html),
  [Walt Disney Animation Wiki](https://walt-disney-animation-studios.fandom.com/wiki/Paul_Felix)).
- Hojas de modelo y arte conceptual recopilados en
  [Cartoon Concept Design](http://cartoonconceptdesign.blogspot.com/2015/03/disney-big-hero-6-concept-art-and-model.html)
  y en la [categoría de arte conceptual de la wiki](https://bighero6.fandom.com/wiki/Category:Concept_art).
- Arte de Paul Felix expuesto en «Disney: The Magic of Animation»
  ([Food For Thought](https://foodforthought.com.my/disney-magic-of-animation-exhibition-at-marina-bay-sands/big-hero-6-2014-concept-art-paul-felix-disney-food-for-thought/)).

### El manga japonés
Dibujado por **Haruki Ueno** (Kodansha). Prólogo en Weekly Shōnen
Magazine el 6-08-2014; serie en Magazine Special del 20-08-2014 al
20-03-2015. **Dos tomos** en inglés (Yen Press, 2015). Fue el primer
filme de Disney anunciado con un manga ⚠️ (una sola fuente, ANN)
([ANN en GitHub](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/manga/16985.json)).
**Segunda fuente para los tomos** ✅: Yen Press lo licenció el 31-08-2014
y lo sacó desde el 25-03-2015; tomo 1 con los capítulos 1-4 más el 0
al final, tomo 2 con el 5-8, y la historia queda en suspenso
([ANN, noticia](https://www.animenewsnetwork.com/news/2014-08-31/yen-press-licenses-manga-version-of-disney-big-hero-6-film/.78236),
[Internet Archive, tomo 1](https://archive.org/details/bighero6vol10000ueno),
[wiki de BH6](https://bighero6.fandom.com/wiki/Big_Hero_6_(manga))).
**Página de muestra del capítulo 0, vista** ✅: Baymax dice «Hello! I am
ベイマックス» con furigana, tres viñetas de reacción de Hiro y una de
acción con líneas de velocidad; fondo de trama de puntos
([archivo, 1000×1436](https://static.wikia.nocookie.net/disney/images/2/22/Baymax-manga-preview-ch-0.jpg)).
Portada del tomo en la ficha: **640×982**
([imagen](https://cdn.animenewsnetwork.com/images/encyc/A16985-2330226621.1429842580.jpg)).

### Galerías de las wikis (en la segunda pasada, leídas por su API)
[Baymax, galería](https://bighero6.fandom.com/wiki/Baymax/Gallery) ·
[Hiro, fotogramas](https://disney.fandom.com/wiki/Hiro_Hamada/Gallery/Screenshots) ·
[Hiro, galería](https://bighero6.fandom.com/wiki/Hiro_Hamada/Gallery) ·
[Tadashi, galería](https://bighero6.fandom.com/wiki/Tadashi_Hamada/Gallery) ·
[imágenes de Baymax](https://bighero6.fandom.com/wiki/Category:Baymax_images).

### La serie «¡Baymax!» (Disney+, 2022)
Seis episodios cortos de Don Hall: **Baymax ayuda a gente corriente**, sin
superhéroes, «como nuestros sanitarios» ✅
([Disney+ Press](https://press.disneyplus.com/news/disney-plus-to-debut-new-series-baymax),
[IndieWire](https://www.indiewire.com/features/general/baymax-big-hero-6-disney-plus-1234737544/),
[Disney News](https://news.disney.com/baymax-animated-series),
[The Illuminerdi](https://theilluminerdi.com/2022/06/27/baymax-creators-healthcare-focus/)).
**Es el tono justo para #soporte.** Kit de prensa con imágenes:
[dmedmedia](https://dmedmedia.disney.com/disney-plus/baymax).

### ⚠️ Aviso de licencia: la escala Wong-Baker
La escala de caras de verdad **tiene derechos**. Para usarla hay que
pedir permiso y a veces pagar; si se usa sin cambios va con el texto
«Copyright 1983, Wong-Baker FACES Foundation… Used with permission» ✅
([condiciones](https://wongbakerfaces.org/resources/usage-guidelines/),
[uso en publicaciones](https://wongbakerfaces.org/licensing-dashboard/publishing-use/),
[preguntas frecuentes](https://wongbakerfaces.org/us/faq/)).
Existe la hoja oficial **en español**
([PDF](https://wongbakerfaces.org/wp-content/uploads/2016/06/FACES_Spanish_Blue_w-instructions.pdf)).
**Propuesta:** caras propias al estilo de Baymax y números del 1 al 10,
con la forma de la tabla que sale en la serie (§1). Así es «de verdad»
(una escala clínica) sin copiar la suya. Los colores de los pines
oficiales de la escala no se pudieron ver (YouTube pidió sesión) ⚠️.

---

## 4 · Escenas icónicas (con su enlace)

La tabla de abajo es de la primera pasada (enlaces de YouTube, **minuto
sin verificar**: YouTube sigue pidiendo sesión). **Lo visto de verdad en
la segunda pasada está en §4.1**, con fotograma y minuto del clip.

| Escena | Qué pasa | Enlace |
|---|---|---|
| Baymax se enciende | Hiro dice «¡ay!» en su cuarto; Baymax se infla, saluda y pregunta el dolor | [clip](https://www.youtube.com/watch?v=cPwT1-2ZHgM) · [otro](https://www.youtube.com/watch?v=jlY-dEzTl0M) · [otro](https://www.youtube.com/watch?v=99RzToAF55Y) |
| Las figuras que caen | A Hiro le caen figuras una a una; Baymax repite la pregunta y **su pecho enseña la escala de caras cada vez** | [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Funny/BigHero6) |
| Batería baja (película) | Baymax baja la escalera tambaleándose y choca con Hiro en la cocina; **sin gato** (visto, §4.1) | [Dailymotion, «Low Battery»](https://www.dailymotion.com/video/x283k45) |
| Batería baja con Mochi (**otro corto, no la película**) | Mochi ayuda a meter a Baymax en su cargador: es el corto ***Big Chibi 6: «Low Battery»*** (2019, dir. Ben Juwono, de la serie) | [wiki de BH6, guion del corto](https://bighero6.fandom.com/wiki/Low_Battery) · [vídeo de Disney Channel](https://youtu.be/vmy5afLiIVc) |
| El choque de puños | Hiro le enseña el puño; Baymax hace «ba-la-la-la-la» con los dedos | [clip oficial HD](https://www.youtube.com/watch?v=yl8yriCIzCE) |
| La mejora de Baymax | Hiro le pone chips y armadura | [clip](https://www.youtube.com/watch?v=wILlTsjnYYw) · [placa del vientre](https://www.youtube.com/watch?v=BlPMfo1gaoo) |
| El primer vuelo | Hiro y Baymax vuelan sobre San Fransokyo | [clip](https://www.youtube.com/watch?v=HKwkOrFFEpg) |
| Los microbots | Hiro construye en su garaje (4K, a cámara lenta) | [clip](https://www.youtube.com/watch?v=3S3NadJwEQI) |
| El vídeo de Tadashi | Baymax proyecta en su torso las pruebas de Tadashi: 1.ª, 7.ª, 33.ª y **84.ª** («This is Tadashi Hamada, and this is the 84th… test. What do you say, big guy?»). En latino: «Aquí Tadashi Hamada y este es el octogésimo cuarto ensayo» | [transcripción original](https://bighero6.fandom.com/wiki/Big_Hero_6_(film)/Transcript) · [audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397715) |
| El final | «Estoy satisfecho con mi cuidado» | [audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397730) · [YouTube](https://www.youtube.com/watch?v=F8zuGaDxwkk) |

Todos los clips de la película juntos: [YouTube](https://www.youtube.com/watch?v=EEYsgRgHGfI).
Serie 2D, Baymax vuelve: [YouTube](https://www.youtube.com/watch?v=yDnKLLac5Nk).

### 4.1 · Escenas vistas en la segunda pasada (fotograma y minuto del clip) ✅

Clips bajados de Dailymotion e Internet Archive y mirados con
`fotogramas.py --cortes`. **El minuto es del clip citado**, no de la
película entera (102 min): la película completa está en Internet Archive
(`1080_20260525`, 6112 s) pero no se recortó.

**«Meet Baymax»** (CGMeetup, 2:02, [x2553ox](https://www.dailymotion.com/video/x2553ox)): la activación en el cuarto de Hiro.
- [0:09](https://www.dailymotion.com/video/x2553ox?start=9): primer plano del **botón rojo redondo** de encendido en el pecho.
- [1:02](https://www.dailymotion.com/video/x2553ox?start=62): el pecho **enciende la escala de dolor de 10 caras**.
- [1:12](https://www.dailymotion.com/video/x2553ox?start=72): Baymax escanea a Hiro, **cabeza inclinada y una mano en su hombro**.
- 1:17: Hiro agachado tras la cama, susto cómico.
- 1:53: **interfaz azul de escaneo** en pantalla («SYMPTOMS», signos vitales en números).

**«Low Battery»** (oficial, 1:04, [x283k45](https://www.dailymotion.com/video/x283k45); la misma en francés, [x31z3kn](https://www.dailymotion.com/video/x31z3kn)):
- 0:22-0:30: Baymax baja la escalera de madera de la casa Hamada, de noche, tambaleándose.
- [0:40-0:44](https://www.dailymotion.com/video/x283k45?start=44): en la cocina, la tía Cass friega; Baymax choca con Hiro («andar de borracho», brazos sueltos). **No hay gato.**

**«Fist Bump»** (0:31, [x3wn7x2](https://www.dailymotion.com/video/x3wn7x2?start=21)):
- 0:21: el choque de puños **del final**: Baymax con la armadura nueva, sala con biombo japonés en el SFIT; Hiro extiende el puño, Baymax lo imita despacio y sonríen. El de mitad de película («ba-la-la-la-la») no apareció como clip suelto ⚠️.

**Batalla final** («Last Fighting Scene», 4:58, [x7vbgp7](https://www.dailymotion.com/video/x7vbgp7)):
- [0:24](https://www.dailymotion.com/video/x7vbgp7?start=24): Fred escupe fuego, agachado.
- 0:30-0:33: Honey Lemon lanza bolas químicas rosas.
- 0:56-1:06: Baymax e Hiro caen en picado hacia el portal, sujetos por el brazo del traje (la escena que hace llorar, §D).
- [1:26](https://www.dailymotion.com/video/x7vbgp7?start=86): el equipo de pie tras la batalla; Baymax saluda con el puño.

**Escena eliminada** «Hamada Brother Robotics» (storyboard en blanco y negro, [Internet Archive](https://archive.org/details/youtube-wnDrECylMOU)):
- 0:42: Tadashi, de espaldas, enseña algo a Hiro en el garaje (boceto, ±2 s).

**Serie de TV**, «Big Hero Battle» (1:28, [x7x6uz7](https://www.dailymotion.com/video/x7x6uz7?start=1)):
- 0:01: el equipo en pose de combate junto a la autocaravana; colores **más saturados** que en la película (rojo puro, verde lima, naranja).

---

## 5 · 3D y fan art (sólo referencia o con su licencia)

### Modelos de Baymax en Sketchfab (licencia CC BY, según el buscador)
| Modelo | Autor | Fecha | Enlace |
|---|---|---|---|
| Baymax! | ᗰOᑎKEY ᗪ. ᒪᑌᖴᖴY (@KingOfThePirates) | mayo 2023 | [Sketchfab](https://sketchfab.com/3d-models/baymax-59007b633de1431290ff71afd8e66aaf) |
| Baymax (Big Hero 6) | theamazingdonovan207 | sept. 2024 | [Sketchfab](https://sketchfab.com/3d-models/baymax-big-hero-6-9a96e8526d5a4abaaa184830c20ab4ec) |
| Baymax | jasonballingham | marzo 2020 | [Sketchfab](https://sketchfab.com/3d-models/baymax-03bd50cd3998407aa8097bccb6f5c921) |
| Baymax! 3D Model | omer41_faruk (@kangal9990) | julio 2022 | [Sketchfab](https://sketchfab.com/3d-models/baymax-3d-model-09848c1567104556b7ce3440548a790d) |

Otros con descarga gratis. **Segunda pasada: dos confirmados por la API
de Sketchfab** (el usuario de la API no siempre es el nombre que enseña
la web; el ID del modelo es el mismo):
- [Eshtiaque Ahmad](https://sketchfab.com/3d-models/baymax-418c455a35d24bcdacf853ebf18ae2ee) → usuario `etamal1234`, **CC Attribution** ✅.
- [Koyo_Sikato](https://sketchfab.com/3d-models/baymax-29a502f7c45c4b5e82f74e6d0b5f0066) → usuario `yohyoh`, **CC Attribution** ✅.
- **«Baymax (Rigged)»** de DownbeatFusion, **ya montado con huesos**,
  **CC Attribution** ✅ ([Sketchfab](https://sketchfab.com/3d-models/baymax-rigged-be0f190b63d546af8fdd53f49da0e8b6)): el mejor para posar (§A).
- «Chibi Baymax» de Takoyakixote, **CC BY-NC-SA** ⚠️: sólo referencia de
  volumen chibi, no se reutiliza ([Sketchfab](https://sketchfab.com/3d-models/none-a6dab787e9094c348cd5ba77e8627b03)).
- [BlendSwap #13951](https://blendswap.com/blend/13951), «Baymax» de
  DoodleNotes, con rig, **CC BY-NC** ⚠️ (no se bajó para ver el rig).
- Sin comprobar: [Xasanov Amir](https://sketchfab.com/3d-models/baymax-40815e80d02f4fa5a45a39449b7cfa69),
  [J1G4R](https://sketchfab.com/3d-models/baymax-bdd68308a896406daa709ac9e5faffa1).
Todos: [etiqueta baymax](https://sketchfab.com/tags/baymax).

> [!note] Crédito si se usa uno CC BY
> «"Baymax" por jasonballingham, Sketchfab, CC BY 4.0». La CC BY cubre
> el trabajo del modelador, **no el personaje** (es de Disney): sirve
> para sacar pose y volumen, y la lámina sigue siendo fan art sin venta.

### Objetos y luces libres (para Blender)
- **Carrito de herramientas**, CC0: [Poly Haven, Tool Cart](https://polyhaven.com/a/tool_cart).
- **Carritos médicos** gratis en Sketchfab (licencia a comprobar):
  [NicolasVB](https://sketchfab.com/3d-models/medical-cart-2a0a574f9e374702af8c415fce296f45),
  [CarlosTorresVFX, oxidado](https://sketchfab.com/3d-models/rusty-medical-cart-508d17d0d77c4d10a3a9ddc043241d31),
  [set médico de daonware](https://sketchfab.com/3d-models/realistic-medical-equipment-and-accessories-set-5460fb2767c6468eb88466d2555d273b).
- **Portapapeles** gratis: [Console Art Cybernetic](https://sketchfab.com/3d-models/clipboard-4ddbcd71243441499bbc4e124570e736).
- **HDRI de Poly Haven** (CC0):
  [habitación de hospital](https://polyhaven.com/a/hospital_room) (luz fría de techo),
  [hospital infantil](https://polyhaven.com/a/childrens_hospital) (luz amarilla suave),
  [quirófano](https://polyhaven.com/a/surgery),
  [garaje](https://polyhaven.com/a/garage) (fluorescente cálido, hormigón naranja),
  [taller](https://polyhaven.com/a/autoshop_01),
  [garaje con claraboya](https://polyhaven.com/a/skylit_garage).
- **Texturas** CC0: [suelo de garaje](https://polyhaven.com/a/garage_floor),
  [puerta de garaje de madera](https://polyhaven.com/a/wooden_garage_door).

### Fan art (enlace y autor, nunca para pegar)
- Pixiv: [ベイマックスとヒロ](https://www.pixiv.net/en/artworks/98296721),
  [ベイマックスまとめ](https://www.pixiv.net/en/artworks/47830127),
  [Hiro, 24-09-2021](https://www.pixiv.net/en/artworks/92978228).
  Autores sin ver ⚠️.
- DeviantArt: **Catel23**, Hiro y Baymax en 2D al estilo Disney clásico
  ([enlace](https://www.deviantart.com/catel23/art/Big-hero-6-Hiro-and-Baymax-2D-old-Disney-style-635327313)).
- ArtStation: **Brandon Lawless**, GoGo y Tadashi ([enlace](https://www.artstation.com/artwork/wPY56)).
  Su nombre sale también firmando hojas de modelo oficiales de 2015
  («Modeler Brandon Lawless», §3); el autor del fan art sigue ⚠️ sin
  segunda fuente.
- **Qué NO calcar**: un «Gundam Baymax» de fans (hoja 06, n.º 245) lo
  rediseña como un robot de placas duras. Baymax **no** lleva paneles ni
  detalle mecánico: es vinilo liso ⚠️ (una fuente, sin autor).
- **Fondos de pantalla** con tamaño y autor: §17.
- Construcción de un Baymax «mecha» de POP MART (juguete real, sirve
  para ver volúmenes) ([YouTube](https://www.youtube.com/watch?v=dyKWzaD1H-8)).

---

## 6 · Sitios, luz, paleta y texturas

### San Fransokyo
- Mezcla de **San Francisco y Tokio**. Se hizo con los **mapas catastrales
  reales de San Francisco**, con las cuestas más empinadas ✅
  ([Gizmodo](https://gizmodo.com/a-tour-of-san-fransokyo-the-hybrid-city-disney-built-f-1642066794),
  [fxguide](https://www.fxguide.com/fxfeatured/disneys-new-production-renderer-hyperion-yes-disney/)).
- **83.000 edificios y 216.000 farolas**. Todo con luz rebotada de verdad
  (el motor Hyperion), sin fondos pintados. El director quería **luz de
  cine**: distorsión de lente, aberración cromática y desenfoque ✅
  ([Cartoon Brew](https://www.cartoonbrew.com/tech/disney-explains-its-powerful-new-hyperion-rendering-engine-117152.html),
  [Disney Animation](https://disneyanimation.com/technology/hyperion/),
  [Vice](https://www.vice.com/en/article/heres-how-disney-built-its-biggest-world-ever-for-big-hero-6/),
  [Engadget](https://www.engadget.com/2014-10-18-disney-big-hero-6.html)).
- Vídeo de cómo se hizo: [YouTube](https://www.youtube.com/watch?v=syWg8-uYHwY).

### El Lucky Cat Café y la casa Hamada
- Edificio de **tres pisos en la esquina de una calle en cuesta** ✅
  ([wiki de BH6](https://bighero6.fandom.com/wiki/Lucky_Cat_Caf%C3%A9),
  [wiki de Disney](https://disney.fandom.com/wiki/Lucky_Cat_Caf%C3%A9)).
- **Planta baja:** la cafetería de la tía Cass. Peces, flores de cerezo,
  farolillos japoneses y gatos por todas partes. Fuera, **gatos
  maneki-neko** y macetas en las ventanas.
- **Segundo piso:** salón y cocina. **Tercero:** el cuarto de Hiro y
  Tadashi.
- **El garaje:** el taller de los hermanos, donde Hiro trasnocha.
- El gato **Mochi** es un bobtail japonés, como el gato de la suerte
  ([Mochi](https://disney.fandom.com/wiki/Mochi)).

### El laboratorio de Tadashi (SFIT)
San Fransokyo Institute of Technology. Allí Tadashi crea a Baymax ✅
([Tadashi, wiki de Disney](https://disney.fandom.com/wiki/Tadashi_Hamada)).
Cómo es por dentro: ⚠️ de memoria (un taller luminoso con cristal). En
el choque de puños final se ve **una sala con biombo japonés** en el
SFIT ✅ (visto, [Fist Bump, 0:21](https://www.dailymotion.com/video/x3wn7x2?start=21)).
El sello del SFIT, medido: §7 y §H.

### Paleta medida en fotogramas (segunda pasada) ✅
Medida con `estilo.py` sobre fotogramas de los clips vistos (§4.1).
Porcentaje = parte de la imagen.

| Sitio y toma | Hex medidos (de más a menos) | Clip y minuto |
|---|---|---|
| Cuarto de Hiro, tarde con persiana | `#C5B9AA` 32% · `#241203` 29% · `#4C2F11` 14% · `#3B4B37` 12% · `#F6F5E3` 9% | [x2553ox, 1:02](https://www.dailymotion.com/video/x2553ox?start=62) |
| Mismo cuarto, escaneo (más sombra) | `#322820` 31% · `#0C0705` 25% · `#554D40` 18% · `#88816F` 12% · `#E6F0F6` 5% (el blanco azulado de Baymax) | [x2553ox, 1:12](https://www.dailymotion.com/video/x2553ox?start=72) |
| Cocina Lucky Cat, noche, plano general | `#66462F` 29% · `#392721` 27% · `#975B44` 14% (madera, terracota) · `#3F4C59` 11% (ventana) · `#BFBA89` 11% · `#848E6E` 10% (alacena verde agua) | [x283k45, 0:30](https://www.dailymotion.com/video/x283k45?start=30) |
| Cocina, mesa de la tía Cass | `#35241D` 45% · `#543C31` 23% · `#7E5E4C` 12% · `#98977C` 9% · `#D5C29F` 7% · **`#DA3F3D` 3% (encimera roja)** | [x283k45, 0:40](https://www.dailymotion.com/video/x283k45?start=40) |
| Vuelo nocturno entre nubes | `#4C1F25` 28% · `#986461` 18% · `#B68370` 16% · `#65505B` 16% · `#220B17` 12% · `#971E24` 10% (armadura) | [tráiler latino x889whz, 1:48](https://www.dailymotion.com/video/x889whz?start=108) |
| El grupo vuela al atardecer | `#6954A7` 24% · `#514B94` 22% · `#404174` 20% · `#8262BD` 14% · `#5657D0` 12% · `#A57CDE` 9% | [x889whz, 1:55](https://www.dailymotion.com/video/x889whz?start=115) |

- La cocina, vista: **alacenas verde menta, pared amarillo verdosa,
  encimera roja, lámpara de techo cálida**.
- El atardecer de esa toma es **morado azulado, no dorado** (corrige lo
  de memoria). El dorado puede salir en otras tomas de ciudad, sin medir ⚠️.
- `estilo.py` clasifica las seis tomas como **sombreado degradado, poca
  línea**, saturación 43-50%, brillo 34-65%: render 3D de Hyperion, no
  dibujo plano.
- Faltan tomas de día de la ciudad y del garaje ⚠️ (no hubo clip).

### Luz por sitio
| Sitio | Luz | Estado |
|---|---|---|
| Hospital o consulta | fluorescente fría de techo | HDRI [hospital_room](https://polyhaven.com/a/hospital_room) |
| Garaje de Hiro, de noche | lámpara cálida, pantallas azules | ⚠️ de memoria (sin clip) |
| Lucky Cat Café y cocina | cálida, madera, verde menta y rojo | ✅ medida arriba (noche) |
| La ciudad | vuelo entre nubes rojizas de noche; atardecer morado azulado | ✅ medida arriba; el «dorado con niebla» sigue ⚠️ |

### Paleta de la primera pasada (a ojo; **usar la medida de arriba y §16**)
Estos hex eran a ojo. Los de Baymax y Hiro ya están **medidos** en §16:
vinilo `#F2F3F5`, sombra cálida `#DAD5D4`, armadura `#DD4630`-`#ED512D`,
sudadera `#3B3D5C`, camiseta `#DB2C2B`. Los de abajo quedan sólo como
historial.

| Qué | Hex aprox. |
|---|---|
| Vinilo de Baymax (luz) | `#F4F3EF` |
| Vinilo de Baymax (sombra; **era azulada, la medida es cálida `#DAD5D4`**) | ~~`#C9CFD6`~~ |
| Ojos y raya de Baymax | `#1B1B1B` |
| Armadura roja de Baymax (**medida: `#DD4630`-`#ED512D`**) | ~~`#C4252B`~~ |
| Armadura de Hiro, morado | `#5B3C8C` |
| Sudadera de Hiro, azul marino | `#2B3550` |
| Camiseta de Hiro, rojo | `#B83A33` |
| Café Lucky Cat, madera | `#8A5A3B` |
| Atardecer de San Fransokyo | `#F2A65A` |

### Texturas reales equivalentes
- **Vinilo blanco inflable** (flotador, colchón hinchable): brillo suave,
  costuras finas. Es el material de Baymax (punto 9).
- **Hormigón de garaje** y **madera** de la puerta: Poly Haven (arriba).
- **Plástico plastificado** para la tabla del dolor de pared: reflejo
  blanco en una esquina, cinta adhesiva en las puntas.
- **Libres CC0 de ambientCG** (licencia leída en su API): vinilo o
  plástico liso [Plastic013A](https://ambientcg.com/view?id=Plastic013A),
  [Plastic010](https://ambientcg.com/view?id=Plastic010); metal cepillado
  para la armadura [Metal063](https://ambientcg.com/view?id=Metal063),
  [Metal049A](https://ambientcg.com/view?id=Metal049A). Papel y tela: §B.
- **Superficie de Baymax bajo luz real**: el disfraz de foam EVA de The
  RPF, sellado con varias capas de Plasti Dip y acabado brillante, es la
  mejor referencia para calibrar el brillo del vinilo en Blender (§F).

---

## 7 · Tipografía (y si trae tildes, ñ, ¿ y ¡)

### El logo
El logo «BIG HERO 6» es un dibujo propio de Disney, no una letra que se
venda. Hay una letra de fan, **«Big Hero»**, que lo imita, pero **sólo
trae mayúsculas y pocos signos**: no sirve para español ✅
([FontMeme](https://fontmeme.com/big-hero-6-font/),
[FontMeme, Big Hero](https://fontmeme.com/fonts/big-hero-font/),
[dafont, hilo del logo](https://www.dafont.com/forum/read/184224/big-hero-6-logo-font),
[otro hilo](https://www.dafont.com/forum/read/185468/big-hero-6-font)).
En dafont también preguntan por la letra del póster y la de los créditos
([póster](https://www.dafont.com/forum/read/226321/big-hero-6-poster-font-not-logo),
[créditos](https://www.dafont.com/forum/read/204389/the-font-used-in-the-credits-of-big-hero-6)),
sin respuesta que pudiera leer.

### El logo, visto y medido (segunda pasada) ✅
- Letras propias **gruesas y redondeadas**, con la base irregular, hechas
  a mano. Mayúsculas blancas con contorno negro sobre rojo; el «6» negro
  con una barra roja en medio ([Big_Hero_6_logo.png, 800×310](https://static.wikia.nocookie.net/bighero6/images/a/aa/Big_Hero_6_logo.png)).
  Medido con `estilo.py`: rojo `#E00318`, negro `#020000`, blanco `#FEFDFE`.
- **La más parecida de las libres: Bungee** (gruesa, redondeada, de
  cómic); luego Baloo 2. Russo One es más recta y se aleja más.
  Comparación mirando las dos imágenes, no superpuestas ⚠️.
- **En latino** el logo se traduce a «GRANDES HÉROES» con la misma
  familia de letra, en rótulo rojo con bisel blanco ✅ (visto, [tráiler
  latino, 2:21](https://www.dailymotion.com/video/x889whz?t=141); y en el
  póster latino n.º 44, §3.0).
- Los rótulos del tráiler latino van en **mayúsculas condensadas**:
  «MUY PRONTO» (0:51), «UN GRAN DESCUBRIMIENTO LLEGARÁ» (0:58), «ÉL NOS
  GUIARÁ» (2:02), «ÉL NOS CUIDARÁ» (2:06), «ÉL CAMBIARÁ NUESTRO MUNDO»
  (2:10) ✅ (vistos).
- **Sello del SFIT**: círculo tipo engranaje con «SAN FRANSOKYO INSTITUTE
  OF TECHNOLOGY» en letras redondeadas gruesas alrededor de un monograma
  «SF». Hex: oro `#FDD340`, azul marino casi negro `#100730`, rojo oscuro
  `#A82512`, naranja quemado `#C4651C` ✅ ([SFIT_Logo.png, 700×700](https://static.wikia.nocookie.net/bighero6/images/7/7e/SFIT_Logo.png)).
- **Portada del manga en inglés** (Yen Press, tomo 1): «BIG HERO 6» en
  letra de palo **blanca, gruesa y recta** en una banda roja, distinta
  del logo del cine ✅ (vista, [Internet Archive](https://archive.org/details/bighero6vol10000ueno)).
  La letra de los globos no se pudo ver (el libro está cifrado).
- Letra estándar del manga traducido al inglés: **WildWords** (de pago)
  ([Comicraft](https://www.comicbookfonts.com/Wildwords-font-p/bl003i.htm));
  que este tomo la use, ⚠️ sin confirmar.

### Letras libres comprobadas una a una
Se bajó cada archivo de `google/fonts` en GitHub y se miró si trae
**á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü**.

| Para qué | Letra | ¿Trae todo? | Licencia |
|---|---|---|---|
| **Pantalla de Baymax** (redonda, de clínica) | **Nunito** | ✅ sí | OFL |
| Pantalla de Baymax, con japonés | **M PLUS Rounded 1c** | ✅ sí | OFL |
| Pantalla de Baymax, alternativa | Varela Round | ✅ sí | OFL |
| Pantalla de Baymax, fina | Quicksand | ✅ sí | OFL |
| Rótulos japoneses redondos | Zen Maru Gothic | ✅ sí | OFL |
| Rótulos japoneses redondos | ❌ **Kosugi Maru** | ❌ **no**: le faltan todas | Apache |
| Cartel del café, gordita | Mochiy Pop One | ✅ sí | OFL |
| Cartel del café, gordita | Baloo 2 | ✅ sí | OFL |
| Rótulo japonés grueso | Dela Gothic One | ✅ sí | OFL |
| Título tipo logo, bloque | Russo One | ✅ sí | OFL |
| Título tipo logo, bloque | Bungee | ✅ sí | OFL |
| Título tipo logo, ancho | Exo 2 (Black Italic) | ✅ sí | OFL |
| Interfaz de Hiro o Krei | Rajdhani | ✅ sí | OFL |
| Interfaz de Hiro o Krei | Chakra Petch | ✅ sí | OFL |
| Interfaz de Hiro o Krei | Titillium Web | ✅ sí | OFL |
| Número de ticket, ticket de caja | Share Tech Mono | ✅ sí | OFL |
| Título técnico | Orbitron | ✅ sí | OFL |
| Título técnico | Saira / Saira Condensed | ✅ sí | OFL |
| Notas a mano de Hiro o Cass | Caveat | ✅ sí | OFL |
| Notas a mano | Kalam | ✅ sí | OFL |
| Notas a mano | Patrick Hand | ✅ sí | OFL |

> [!warning] Kosugi Maru engaña
> Su ficha en Google Fonts dice que trae el juego «latin», pero el archivo
> real **no tiene ninguna letra con tilde, ni ñ, ni ¿ ¡**. Comprobado con
> fontTools en `KosugiMaru-Regular.ttf`. No usarla.

**Segunda comprobación con fontTools** (archivos reales de
`fonts.gstatic.com`): Nunito, Share Tech Mono, Caveat, Russo One y
Bungee siguen ✅; Kosugi Maru sigue ❌ (dos veces). **Nuevas, ✅ con todo:
Comic Neue** (globo de manga), **Bangers** (grito, onomatopeya) y
**Permanent Marker** (cartel a mano).

**Una letra para cada uso** (todas traen á é í ó ú ñ ¿ ¡):

| Uso | Letra libre |
|---|---|
| Logo o título | **Bungee** (la más parecida), o Russo One |
| Lo que dice Baymax en su pecho | **Nunito** ExtraBold/Black |
| Globo normal (manga o juego) | **Comic Neue** |
| Grito | **Bangers** |
| Pensamiento | Caveat |
| Onomatopeya | Bangers o Bungee |
| Cartel del mundo (tienda, calle) | Permanent Marker o Mochiy Pop One |
| Interfaz de juego | Rajdhani, Chakra Petch o Titillium Web |
| Subtítulos o créditos | Titillium Web |
| Número de ticket | Share Tech Mono |

Superponer el logo con Bungee en el PC antes de decidir ⚠️ (aquí se
compararon a ojo).

**Recomendación:** **Nunito** (ExtraBold o Black) para todo lo que dice
Baymax. Es redonda, limpia y de clínica, como él. **Share Tech Mono**
para el número del ticket. **Caveat** si algo va escrito a mano.

---

## 8 · Cómo habla en pantalla (el «cuadro de diálogo» de la serie)

### Baymax no tiene globo: tiene **una pantalla en la barriga**
- Lleva **un proyector en el pecho** que pinta imágenes sobre su vinilo ✅
  ([wiki de BH6](https://bighero6.fandom.com/wiki/Baymax)).
- Cuando pregunta el dolor, **su pecho enseña la escala de caras** de
  Wong-Baker, **cada vez que lo pregunta** ✅
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Funny/BigHero6),
  [Rated PT](https://ratedpt.wordpress.com/2021/02/16/big-hero-6-on-a-scale-of-1-10/)).
- **No tiene boca a propósito.** Al principio iba a tenerla; el diseñador
  **Shiyoon Kim**, diseñador principal de personajes, propuso quitarla
  para que hable con **el cuerpo y el parpadeo** ✅ ([Character Media,
  entrevista a los animadores](https://charactermedia.com/big-hero-6-animators-discuss-their-creative-process/),
  y ねとらぼ abajo; antes decía «Kim, sin saber si Jin o Shiyoon»). El ilustrador japonés
  **Koyama Shigeto** propuso usar los **agujeros del cascabel** como ojos ✅
  ([ねとらぼ](https://nlab.itmedia.co.jp/nl/articles/1501/19/news144.html),
  [Red Bull JP, Koyama](https://www.redbull.com/jp-ja/behind-the-mask-15),
  [eiga.com](https://eiga.com/news/20141201/6/)).

- **La tabla del dolor en pantalla, vista y medida** (§1): cajita blanca
  redondeada, 10 caritas en 2 filas de 5, números del 1 al 10, amarillo
  `#F1E815` → naranja `#EDB413` → rojo `#F0764E`, fondo `#FDF9EF`
  ([Scale_8.png](https://static.wikia.nocookie.net/bighero6/images/2/28/Scale_8.png), serie de TV).
  Frase de guion: «On a scale of 1 to 10, how would you rate your pain?»
  y antes «I was alerted to the need for medical attention when you said,
  "ow."» ✅ ([transcripción](https://bighero6.fandom.com/wiki/Big_Hero_6_(film)/Transcript)).
- **Al escanear, sus ojos cambian**: en la serie los dos puntos se
  vuelven **dos iconos de obturador de cámara girando** ✅ (visto,
  [Baymax_scanning_eyes.png, 1920×1080](https://static.wikia.nocookie.net/bighero6/images/c/cc/Baymax_scanning_eyes.png)).
  En la película, el escaneo sale como **interfaz azul** con «SYMPTOMS» y
  números ✅ (visto, [Meet Baymax, 1:53](https://www.dailymotion.com/video/x2553ox?start=113)).
- **El póster latino oficial ya lo hizo** (§3.0, n.º 44): Baymax **señala
  su pecho encendido** con un icono y un aviso en español en mayúsculas
  redondeadas rojas. Es el formato de #soporte, hecho por Disney ✅ (visto).
- **Sus chips son otro cuadro**: el puerto está en el **lado izquierdo del
  pecho**, con aspecto de insignia, y guarda hasta 4 chips ⚠️ (una fuente,
  [ficha](https://bighero6.fandom.com/wiki/Baymax)). Chip de cuidados
  **verde con un doctor sonriente** (hecho por Tadashi): `#546B60` /
  `#78968B` sobre `#232627` ✅ ([imagen, 1920×808](https://static.wikia.nocookie.net/bighero6/images/c/ce/Baymax%27s_Healthcare_Chip.jpg),
  [ficha de los chips](https://bighero6.fandom.com/wiki/Baymax%27s_Chips)).
  Chip de pelea **rojo con calavera**: `#811A1D` / `#9A3640` sobre
  `#28151C` ✅ ([imagen, 1416×808](https://static.wikia.nocookie.net/bighero6/images/b/b8/Baymax%27s_Fighting_Chip.jpg)).
  Chip de superhéroe: `#0A242D` / `#97BBBA` con `#4B1415` ⚠️ (sólo medido).

**Así que el cuadro de diálogo de Baymax es su barriga:** el texto sale
**proyectado sobre el vinilo**, curvado con él, con un poco de brillo.
Nada de bocadillo de cómic
([guía de cuadros](../_ya_hechas/_Cuadros%20de%20dialogo%20por%20franquicia%20(23-sep-2026).md)).

### Tadashi habla por **sus vídeos de prueba**
Graba su trabajo con Baymax como un diario: «Aquí Tadashi Hamada y este
es el **octogésimo cuarto ensayo**» ⚠️ (frase de audiofrases, sin oír el
doblaje) ([audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397715)).
**Confirmado con el guion original** ✅: «A video appears on Baymax's
torso»; las pruebas 1.ª, 7.ª, 33.ª y 84.ª («This is Tadashi Hamada, and
this is the 84th… test. What do you say, big guy?») se proyectan **en el
torso de Baymax**, no en otra pantalla, justo después de que Baymax dice
«Tadashi is here» ([transcripción](https://bighero6.fandom.com/wiki/Big_Hero_6_(film)/Transcript)).
**Su cuadro:** un vídeo casero con número de ensayo.

### Hiro habla por **su programa de diseño**
Para el juego de 3DS, la diseñadora **Roberta Tam** hizo la interfaz a
partir del **programa con el que Hiro diseña a Baymax** en la película ✅
([Dribbble](https://dribbble.com/shots/3320537-Big-Hero-6-Battle-in-the-Bay-UI)).
El diseñador de hologramas **Jayse Hansen** tiene una página de Big Hero 6
en su web, pero el título dice «coming soon» ⚠️
([jayse.io](https://jayse.io/?portfolio=big-hero-6-coming-soon)).

### En los videojuegos
- **Kingdom Hearts III**: mundo de San Fransokyo; se vuela a lomos de
  Baymax ✅ ([KH Wiki](https://www.khwiki.com/San_Fransokyo),
  [Kingdom Hearts Fandom](https://kingdomhearts.fandom.com/wiki/San_Fransokyo)).
  Sus cajas de diálogo están en [Game UI Database](https://www.gameuidatabase.com/gameData.php?id=596)
  ⚠️ sin abrir (segunda pasada: la página volvió vacía dos veces).
  **Ningún juego de la franquicia tiene una caja de diálogo propia y
  reconocible**: lo reconocible es la barriga de Baymax (§13).
- **Battle in the Bay** (3DS/DS, 2014): **no tiene voces ni escenas
  animadas** ✅ ([Nintendo Life](https://www.nintendolife.com/reviews/3ds/big_hero_6_battle_in_the_bay),
  [Comic Book Video Games](https://comicbookvideogames.com/2014/11/07/review-big-hero-6-battle-in-the-bay-nintendo-3ds/)).

### Qué cuadro usar en #soporte
1. **Baymax:** texto proyectado en su barriga, en **Nunito**, color de
   luz sobre el vinilo. Una frase corta.
2. **La información larga** (pasos, tabla): en un **objeto** (punto 19),
   no en la barriga.
3. **Hiro**, si habla: pantalla de su programa o una nota a mano en
   Caveat. Nunca un globo blanco.

---

## 9 · Personajes: quién es, cómo habla, cómo se mueve y qué lleva

### Baymax — el enfermero (el más querido)
- **Qué es:** un robot **«asistente médico personal»** que construyó
  Tadashi ✅ ([ANN](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/manga/16985.json),
  [wiki de Disney](https://disney.fandom.com/wiki/Baymax)).
- **De dónde sale:** de un **brazo robótico inflable** de la Universidad
  Carnegie Mellon (el laboratorio de Chris Atkeson, hecho por Siddharth
  Sanan) pensado para cuidar enfermos ✅
  ([CMU](https://www.cmu.edu/news/stories/archives/2014/october/october29_baymax.html),
  [Global News](https://globalnews.ca/news/1663166/big-hero-6-star-baymax-inspired-by-robotics-research/),
  [NEXTpittsburgh](https://nextpittsburgh.com/business-tech-news/cmu-soft-robot-inspires-disneys-newest-movie-hero-baymax/),
  [Atkeson, «Why Baymax»](http://www.cs.cmu.edu/~cga/bighero6/why/)).
- **Su cara** sale de **un cascabel (鈴) del santuario Hanazono** de
  Shinjuku, que Don Hall vio en 2011 ✅
  ([Tokyo Location Box](https://www.locationbox.metro.tokyo.lg.jp/location/list/260/),
  [アニメ！アニメ！](https://animeanime.jp/article/2015/01/19/21637.html),
  [ねとらぼ](https://nlab.itmedia.co.jp/nl/articles/1501/19/news144.html)).
  Y lo mono, de **una olla arrocera** de la teletienda japonesa ✅
  ([eiga.com](https://eiga.com/news/20141201/6/)).
- **Cuerpo:** vinilo blanco inflable. Anda **a pasitos** (ヨチヨチ) ⚠️.
  Por dentro, un esqueleto que Kevin Nelson dibujó para saber cómo se
  dobla ([blog](http://artofkevinnelson.blogspot.com/2014/11/baymax-poses-with-visible-skeleton-from.html)).
- **Lo que lleva dentro** ⚠️ (Namuwiki, vía buscador): calefacción para
  el frío, desfibrilador en las manos, espray desinfectante en los dedos
  ([Namuwiki](https://namu.wiki/w/%EB%B2%A0%EC%9D%B4%EB%A7%A5%EC%8A%A4)).
- **Sus chips:** el de Tadashi (cuidar) y el de Hiro (pelear)
  ([wiki de BH6](https://bighero6.fandom.com/wiki/Baymax's_Chips)).
  Verde con un doctor sonriente y rojo con calavera: **medidos** en §8 ✅.
- **Carácter:** tranquilo, literal, amable. Sólo le importa tu salud:
  «Eres mi paciente… tu salud es mi única preocupación» ⚠️
  ([audiofrases](https://audiofrases.com/frases-de-peliculas-disney/audio-frases-de-big-hero-6-2014/eres-mi-paciente-baymax-tu-salud-es-mi-unica-preocupacion)).
  Nunca tiene prisa. Nunca se enfada (salvo con el chip de pelea).
- **Carácter, según su ficha** ✅ ([wiki de Disney, Personality](https://disney.fandom.com/wiki/Baymax#Personality)):
  entregado a sus pacientes, **un poco ingenuo e infantil**, no entiende
  el espacio personal ni si el paciente *quiere* ayuda; muy tranquilo
  incluso en peligro; lento para lo que no es salud; **curioso y se
  distrae**. Su docilidad viene del chip de Tadashi.
- **Cómo se expresa:** voz plana y suave, frases completas y educadas.
  Saluda con «Hola». Explica con datos de su escáner. No se ríe. Con la
  batería baja, habla como borracho ✅. **Medido en el doblaje latino**
  con `voz.py`: registro medio (150 Hz), **13,3 semitonos de
  expresividad, el más bajo** de los medidos, 2,42 palabras por segundo
  ✅ ([x5hvz3y, 0:52-0:55](https://www.dailymotion.com/video/x5hvz3y?t=52)).
  **Nunca exclama.** Frases oídas: «Hola, yo soy Baymax» (tráiler, [0:18](https://www.dailymotion.com/video/x889whz?t=18)),
  «Quiero ayudarte» ([0:52](https://www.dailymotion.com/video/x889whz?t=52)),
  «Tu estado emocional ha mejorado» ([x5hvz3y, 0:52](https://www.dailymotion.com/video/x5hvz3y?t=52)).
  ([TV Tropes, memes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/BigHero6),
  [audiofrases, «Batería baja»](https://audiofrases.com/frases-de-peliculas-disney/audio-frases-de-big-hero-6-2014/bateria-baja)).
- **Cuerpo que habla:** inclina la cabeza, parpadea, mueve las manos
  despacio. **Abraza** como tratamiento: en China la frase fue
  «拥抱暖暖的大白», abrazar al cálido Baymax
  ([Sanlian](https://www.lifeweek.com.cn/article/149429)).
- **Con quién:** Hiro (su paciente y amigo), Tadashi (su creador), el
  gato Mochi, la tía Cass.
- **Robots reales que lo inspiraron**, además del brazo de la CMU: ASIMO y
  **Pepper**, que también abraza y choca los puños ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Baymax)).
  Gustos, altura y lo que odia: §C.

### Hiro Hamada — el genio de 14 años
- Niño prodigio de la robótica; vive con su hermano y su tía. Tras perder
  a Tadashi, Baymax le ayuda a salir adelante ✅
  ([ANN](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/manga/16985.json),
  [Wikipedia, la serie](https://en.wikipedia.org/wiki/Big_Hero_6:_The_Series)).
- **Ropa de siempre:** sudadera azul marino con cremallera, camiseta roja
  de manga corta con un robot, pantalón cargo beige oscuro por debajo de
  la rodilla y zapatillas altas marrón oscuro con **cordones amarillos**.
  Piel clara, ojos marrones, pelo negro corto y revuelto ✅
  ([wiki de Disney](https://disney.fandom.com/wiki/Hiro_Hamada),
  [wiki de BH6](https://bighero6.fandom.com/wiki/Hiro_Hamada)).
- **Armadura:** morada con detalles rojos y negro; **placas magnéticas
  rojas** para engancharse a Baymax ✅
  ([wiki de BH6](https://bighero6.fandom.com/wiki/Hiro's_Super_Armor)).
- **Carácter, según su ficha** ✅ ([wiki de Disney](https://disney.fandom.com/wiki/Hiro_Hamada#Personality)):
  terminó la secundaria a los 13; **descarado y creído** (se aburre en la
  pelea con Yama), pero sin ser odioso; orgulloso de saberlo todo;
  apuesta en peleas de robots aunque Tadashi no lo aprueba.
- **Cómo se expresa**: rápido, listo, algo impaciente y burlón; de pronto
  frágil cuando sale Tadashi. **Medido en el doblaje latino** (Memo
  Aponte): voz aguda (268 Hz), **24,3 semitonos**, 2,45 palabras por
  segundo ✅ ([x2hry42, 0:04-0:11](https://www.dailymotion.com/video/x2hry42?t=4)).
  Su frase de listillo, oída: «Las peleas robóticas no son ilegales.
  Apostar en peleas robóticas, eso es ilegal, pero lucrativo» ✅ ([0:04-0:09](https://www.dailymotion.com/video/x2hry42?t=4)).
  Sobre Baymax: «Parece un gigantesco malvavisco que camina, sin
  ofender» ⚠️ ([audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397135));
  en el tráiler dice «Estoy abrazando un… malvavisco» ⚠️ (cortada,
  [0:59](https://www.dailymotion.com/video/x889whz?t=59)).
- **Su cara en cada emoción** (vista en clips; minuto del clip):

| Emoción | Qué hace | Dónde |
|---|---|---|
| Alegría tranquila | sentado en su cuarto, sonrisa suave mirando a Baymax | ✅ [tráiler latino, 0:48](https://www.dailymotion.com/video/x889whz?t=48) |
| Alegría, celebrar | puño extendido hacia Baymax, torso hacia delante | ✅ [Fist Bump, 0:21](https://www.dailymotion.com/video/x3wn7x2?start=21) |
| Miedo cómico | agachado tras la cama, ojos muy abiertos | ✅ [Meet Baymax, 1:17](https://www.dailymotion.com/video/x2553ox?start=77) |
| Pedir ayuda | manos abiertas sobre el mostrador de la comisaría, hombros caídos | ✅ [tráiler latino, 1:14](https://www.dailymotion.com/video/x889whz?t=74) |
| Preocupación | primer plano, cejas juntas | ✅ hoja `vestuario_concept_01.jpg`, n.º 72 (sin minuto) |
| Tristeza (funeral, vídeos de Tadashi) | solo en lo alto de la escalera, sin hablar | ⚠️ descrita por TV Tropes; **no hubo clip** |
| Rabia (ordena a Baymax matar a Callaghan) | — | ⚠️ sin clip ni fotograma |
| Vergüenza | — | ❌ no encontré fotograma |

### Tadashi Hamada — el hermano mayor (el más llorado)
- Estudiante de robótica en el SFIT y **creador de Baymax**. Amable,
  animoso, trabajador, con humor tonto y alegre ✅
  ([wiki de BH6](https://bighero6.fandom.com/wiki/Tadashi_Hamada),
  [wiki de Disney](https://disney.fandom.com/wiki/Tadashi_Hamada)).
- **Su gorra:** negra, con letras rojas y doradas de **«San Fransokyo
  Ninja»**. Casi nunca se la quita. Se le cae antes del incendio y Hiro
  la guarda ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Tadashi_Hamada),
  [Wikipedia](https://en.wikipedia.org/wiki/Tadashi_Hamada)).
- **Carácter, según su ficha** ✅ ([wiki de Disney](https://disney.fandom.com/wiki/Tadashi_Hamada#Personality)):
  muy amable, animoso y trabajador; humor tonto y alegre; **no cree en
  los «callejones sin salida»**; entiende de salud; le enseñó kárate a
  Hiro; la única figura masculina en la vida de Hiro.
- **Cómo habla**: pausado y cálido, de hermano mayor paciente. Oído en
  latino (Alexis Ortega): «¿Hasta cuándo harás algo de valor con esa mente
  brillante?» ✅ ([x2hry42, 1:26](https://www.dailymotion.com/video/x2hry42?t=86)) y
  «Quizá no evite que vayas, pero no voy a dejarte ir solo» ✅ ([1:49](https://www.dailymotion.com/video/x2hry42?t=109)).
- **Su frase:** «Alguien tiene que ayudar» ⚠️. En la película latina
  **no tuvo traducción fija**: sus últimas palabras fueron «No puedo
  dejarlo, comprende». La serie sí la dice así, dos veces, en «Baymax
  Regresa» ✅ ([Doblaje Wiki, datos de interés](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes)).
- **Ropa de la película**: gorra negra y chaqueta verde (conceptos de
  ropa, hoja `colaboraciones_01.jpg`, n.º 236) ✅; el verde exacto no se
  pudo medir (sus escenas son de noche) ⚠️. §16.
- **Respeto:** muere en la película, y su voz latina murió en 2026. En la
  lámina va como mucho **su gorra**, en un rincón.

### Secundarios
- **Tía Cass:** dueña del Lucky Cat Café
  ([wiki de Disney](https://disney.fandom.com/wiki/Aunt_Cass)). Cocina
  «alitas de pollo con esa salsa picante» ⚠️
  ([audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397309)).
- **Fred:** el fan de los cómics. **GoGo:** la seria. **Honey Lemon:** la
  química. **Wasabi:** el maniático del orden ✅
  ([Wikipedia, la serie](https://en.wikipedia.org/wiki/Big_Hero_6:_The_Series),
  [TV Tropes, personajes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/BigHero6)).
- **Cómo hablan, oído en latino** (segunda pasada):
  - **Tía Cass**: «Las peleas robóticas son ilegales. ¿Quieres que te
    arresten por esto?» ✅ ([x2hry42, 0:00](https://www.dailymotion.com/video/x2hry42?t=0)). Regaña con cariño.
  - **Wasabi** (Alan Bravo): «Cada objeto tiene un lugar y un lugar cada
    objeto» y «¡La sociedad tiene reglas!» ✅ ([3:29](https://www.dailymotion.com/video/x2hry42?t=209), [3:34](https://www.dailymotion.com/video/x2hry42?t=214)).
    Habla **atropellado**, 4,1 palabras por segundo, el más rápido medido.
    Le aterran las alturas.
  - **GoGo** (Erika Ugalde): «Fred, no me hagas callarte con mi láser»,
    rápida y seca ✅ ([x5hvz3y, 3:01](https://www.dailymotion.com/video/x5hvz3y?t=181)).
    En el guion original: «Stop whining. Woman up.» ✅ ([transcripción](https://bighero6.fandom.com/wiki/Big_Hero_6_(film)/Transcript)).
    Pega un chicle a sus vehículos por suerte.
  - **Fred** (Noé Velázquez): «¡Somos nerds!» ✅ ([tráiler, 1:25](https://www.dailymotion.com/video/x889whz?t=85));
    se imagina jefe: «El líder Fred, los ángeles de Fred» ✅ ([x5hvz3y, 2:44](https://www.dailymotion.com/video/x5hvz3y?t=164)).
    En su mansión: «Bienvenidos a **my house**» ✅ (Doblaje Wiki).
  - **Honey Lemon**: se dobló a sí misma, Génesis Rodríguez; de
    ascendencia hispana ✅ (§10, §C).
- **Dinámicas para láminas de grupo**: GoGo calla a Fred; Wasabi se
  agobia con el desorden de los demás; Honey Lemon anima; Hiro y Baymax
  chocan los puños. Gustos de cada uno: §C.
- **Mochi:** el gato de la casa, bobtail japonés
  ([wiki de Disney](https://disney.fandom.com/wiki/Mochi)). Calicó de
  tres colores pero **macho** (rarísimo), por eso Hiro dice «¡Sí que está
  loco ese gato!» ✅ (Doblaje Wiki). **5.º en la encuesta japonesa** (§2).

---

## 10 · Doblaje latino

### Película (2014)
| Personaje | Voz latina | Fuentes | Estado |
|---|---|---|---|
| **Baymax** | **Alan Prieto** | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Alan_Prieto), [SoundCloud «Alan Prieto (Baymax)»](https://soundcloud.com/laredso/alan-prieto-baymax), [TikTok SDV «voz oficial: Alan Prieto»](https://www.tiktok.com/@sdv_serviciosdevoz/video/7227258147939814662) | ✅ |
| **Hiro** | **Memo Aponte** | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Memo_Aponte), [PRODU, entrevista](https://www.produ.com/television/noticias/actor-guillermo-aponte-de-disney-mi-voz-como-hiro-en-grandes-heroes-de-disney-representa-un-trabajo-actoral-muy-fuerte/), [Radio Disney MX](https://www.facebook.com/RadioDisneyMx/photos/memo-aponte-es-la-voz-de-hiro-hamada-en-la-versi%C3%B3n-para-latino%C3%A1merica-de-grandes/819762721380622/?locale=es_LA) | ✅ |
| **Tadashi** | **Alexis Ortega** (1989-2026) | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Alexis_Ortega), [El Imparcial](https://www.elimparcial.com/espectaculos/2026/01/27/fallece-alexis-ortega-voz-de-spider-man-en-espanol-latino-y-tadashi-en-grandes-heroes/), [El Informador](https://www.informador.mx/entretenimiento/alexis-ortega-personajes-iconicos-a-los-que-dio-voz-ademas-de-spider-man-20260127-0116.html), [LatinUS](https://latinus.us/entretenimiento/2026/1/27/fallece-alexis-ortega-actor-de-doblaje-que-le-dio-voz-spider-man-tadashi-hamada-162929.html) | ✅ |
| **Honey Lemon** | **Génesis Rodríguez** (se dobla a sí misma) | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [The Dubbing Database](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes) | ✅ |
| Tía Cass | Patricia Palestino | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ (antes ⚠️ una fuente) |
| **Fred** | **Noé Velázquez Pedroza** | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes) (wikitexto completo), [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ nuevo |
| **GoGo** | **Erika Ugalde** | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ nuevo |
| **Wasabi** | **Alan Bravo** | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ nuevo |
| Callaghan / Yokai | Humberto Vélez | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ |
| Alistair Krei | Idzi Dutkiewicz | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ |
| Abigail Callaghan | Yadira Aedo | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ |
| Padre de Fred | Jesse Conde | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ |
| Heathcliff, el mayordomo | Arturo Mercado Chacón | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ |
| Yama | Octavio Rojas | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ |
| General | Paco Mauri | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ |
| Oficial Gerson | Germán Fabregat | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) («Sargento») | ✅ |
| Réferi | Gabriela Guzmán | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ |
| Reportero | Agustín L. Lezama | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) | ✅ |

**Corrección:** la primera pasada dijo «Fred, GoGo, Wasabi: no lo
encontré». **Sí estaban** en el wikitext de Doblaje Wiki (la tabla
resumida no traía esas filas por un `colspan` distinto), y lo confirman
The Dubbing Database y CHARGUIGOU (archivo de los créditos de Disney
Character Voices International). Hiro, Baymax, Tadashi y Honey Lemon
también salen en esas dos fuentes.

- **Estudio y dirección:** Taller Acústico, S.C., dirigido por **Ricardo
  Tejedo**. Luis Daniel Ramírez eligió el reparto y se fue; se mantuvo su
  reparto ✅ (antes ⚠️; ahora también [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes) y [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html)).
  Equipo completo: traducción Katya Ojeda Iturbide y Ricardo Tejedo;
  **casting Luis Daniel Ramírez**; gerencia de producción Erika Sánchez
  Santarelli; producción Yeri Casanova; edición **Diseño en Audio «DNA»**;
  mezcla **Shepperton International** (Reino Unido); ejecutivo creativo
  Raúl Aldana; versión de Disney Character Voices International ✅.
- **Cómo se dobló** (Doblaje Wiki, datos de interés): **contra
  storyboard**; Tejedo adaptó de oído y lo dejó en sincronía en unas
  3 semanas. Es la primera película de Walt Disney Animation en la que
  **los créditos del doblaje sustituyen a los del reparto en inglés**
  (en cine y Disney+, no en DVD). Memo Aponte y Patricia Palestino ya
  fueron Nemo y Dory con Tejedo en Taller Acústico ⚠️ (una fuente).
- **33 voces adicionales** listadas sólo por CHARGUIGOU (Adriana Casas,
  Berenice Vega, César Filio, Gwendolyne Flores, Herman López, Luis
  Navarro, Pedro D'Aguillón Jr., Ricardo Tejedo, entre otros) ⚠️ (una
  fuente; no dice qué papel hizo cada uno).
- **Doblaje Wiki no tiene muestras de audio** de esta película (cero
  etiquetas `<sm2>` en el wikitext): las frases oídas salen de clips.
- Guion de doblaje subido por un usuario: [Scribd](https://www.scribd.com/document/526731325/DOBLAJE-GRANDES-HEROES) ⚠️ sin abrir.

### Serie 2D y ¡Baymax! (2022)
- **Grandes héroes: La serie** tiene doblaje latino
  ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes:_La_serie),
  [cortos](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes:_La_serie/Cortos)).
  Alexis Ortega (Tadashi) sigue en ella ✅ (Doblaje Wiki y las notas de
  su muerte). Memo Aponte (Hiro) también ⚠️ (sólo Doblaje Wiki).
  **Honey Lemon cambia de voz en la serie**: Génesis Rodríguez no
  repitió; la dobla **Leyla Rangel** ⚠️ (Doblaje Wiki, datos de interés).
  En pocos sitios se llamó «6 Grandes héroes».
- **¡Baymax!** tiene tráiler en latino
  ([YouTube](https://www.youtube.com/watch?v=r8ysizKgmQA)). La actriz
  **Amanda Flores** dice que participó ([TikTok](https://www.tiktok.com/@amandaflores81/video/7114839094596816134),
  [Facebook](https://www.facebook.com/Amandafloresoficial/videos/soy-parte-del-doblaje-de-baymax-de-disney-disney-plus-latinoam%C3%A9rica-baymax-dobla/1044363872860410/)).
  Que Baymax siga siendo Alan Prieto ahí ⚠️ no confirmado.

### No confundir con otros doblajes
- **España** la llama «Big Hero 6». Baymax es **Álvaro Navarro** ⚠️
  (resumen del buscador) ([eldoblaje, película](https://www.eldoblaje.com/datos/FichaPelicula.asp?id=42483),
  [serie](https://www.eldoblaje.com/datos/FichaPelicula.asp?id=52409),
  [¡Baymax!](https://www.eldoblaje.com/datos/FichaPelicula.asp?id=67950)).
  Circula «Estoy satisfecho con **mis cuidados**»: suena a España
  ([TikTok](https://www.tiktok.com/@moviedailyquote/video/7409367458823343392?lang=en)).
- **Japón:** Baymax **川島得愛**, Hiro **本城雄太郎**, Tadashi
  **小泉孝太郎** ✅ ([eiga.com](https://eiga.com/movie/80460/),
  [Animate Times](https://www.animatetimes.com/tag/details.php?id=9720),
  [Oricon](https://www.oricon.co.jp/special/68756/)).

### Frases oídas en el doblaje latino (segunda pasada) ✅
Transcritas con `voz.py` (Whisper, en local) de clips doblados de
Dailymotion; los nombres propios se corrigieron a mano (Whisper oye
«Deimax» por Baymax). **El minuto es del clip.**

**Tráiler oficial en español latino** ([x889whz](https://www.dailymotion.com/video/x889whz), 2:31):

| Minuto | Frase | Quién |
|---|---|---|
| [0:11](https://www.dailymotion.com/video/x889whz?t=11) | «Él es mi hermano mayor, Tadashi.» | Hiro ✅ |
| [0:18](https://www.dailymotion.com/video/x889whz?t=18) · [0:37](https://www.dailymotion.com/video/x889whz?t=37) | «Hola, yo soy Baymax.» | Baymax ✅ |
| [0:52](https://www.dailymotion.com/video/x889whz?t=52) | «Quiero ayudarte.» | Baymax ✅ |
| [0:59](https://www.dailymotion.com/video/x889whz?t=59) | «Estoy abrazando un… malvavisco.» | Hiro ⚠️ (el corte se come una palabra) |
| [1:25](https://www.dailymotion.com/video/x889whz?t=85) | «¡Somos nerds!» | Fred ✅ |
| [1:37](https://www.dailymotion.com/video/x889whz?t=97) | «¿Por qué la ropa interior de fibra de carbono?» | GoGo o Wasabi ⚠️ (no se distingue la voz) |
| [2:16](https://www.dailymotion.com/video/x889whz?t=136) | «¡Es solo una expresión!» | Wasabi ✅ |

**Película doblada, inicio y laboratorio** ([x2hry42](https://www.dailymotion.com/video/x2hry42), 3:59, subido por un usuario):

| Minuto | Frase | Quién |
|---|---|---|
| [0:00](https://www.dailymotion.com/video/x2hry42?t=0) | «Las peleas robóticas son ilegales. ¿Quieres que te arresten por esto?» | Tía Cass ✅ |
| [0:04](https://www.dailymotion.com/video/x2hry42?t=4) | «Las peleas robóticas no son ilegales. Apostar en peleas robóticas, eso es ilegal, pero lucrativo.» | Hiro ✅ |
| [1:26](https://www.dailymotion.com/video/x2hry42?t=86) | «¿Hasta cuándo harás algo de valor con esa mente brillante?» | Tadashi ✅ |
| [1:37](https://www.dailymotion.com/video/x2hry42?t=97) | «¿Qué dirían mamá y papá ahora?» «No lo sé, ya no están. Tenía tres años cuando murieron.» | Tadashi e Hiro ✅ |
| [1:49](https://www.dailymotion.com/video/x2hry42?t=109) | «Quizá no evite que vayas, pero no voy a dejarte ir solo.» | Tadashi ✅ |
| [2:11](https://www.dailymotion.com/video/x2hry42?t=131) | «¡Qué lindo! Conoceré tu nerd lab.» | Hiro ✅ |
| [2:45](https://www.dailymotion.com/video/x2hry42?t=165) | «Bienvenida a la tierra de los nerds.» | Hiro ✅ |
| [3:29](https://www.dailymotion.com/video/x2hry42?t=209) | «Cada objeto tiene un lugar y un lugar cada objeto.» | Wasabi ✅ |
| [3:34](https://www.dailymotion.com/video/x2hry42?t=214) | «¡La sociedad tiene reglas!» | Wasabi ✅ |

**Película doblada, el escaneo y Krei** ([x5hvz3y](https://www.dailymotion.com/video/x5hvz3y), 4:23, subido por un usuario):

| Minuto | Frase | Quién |
|---|---|---|
| [0:39](https://www.dailymotion.com/video/x5hvz3y?t=39) | «Sólo es una expresión.» | Hiro ✅ |
| [0:52](https://www.dailymotion.com/video/x5hvz3y?t=52) | «Tu estado emocional ha mejorado.» | Baymax ✅ |
| [0:55](https://www.dailymotion.com/video/x5hvz3y?t=55) | **«Puedo desactivarme si dices que estás satisfecho con tu cuidado.»** | Baymax ✅ |
| [1:00](https://www.dailymotion.com/video/x5hvz3y?t=60) | «No, no quiero que te desactives.» | Hiro ✅ |
| [2:44](https://www.dailymotion.com/video/x5hvz3y?t=164) | «El líder Fred, los ángeles de Fred.» | Fred ✅ |
| [3:01](https://www.dailymotion.com/video/x5hvz3y?t=181) | «Fred, no me hagas callarte con mi láser.» | GoGo ✅ |
| [4:14](https://www.dailymotion.com/video/x5hvz3y?t=254) | «Amigos, les presento el proyecto Silent Sparrow.» | Alistair Krei ✅ |

**Corrección importante:** la frase de Baymax es **«…satisfecho con TU
cuidado»**, no «mi cuidado», y es más corta que la de audiofrases. La
de Hiro al final («Estoy satisfecho con mi cuidado») sigue sin oírse:
el clímax doblado no apareció en Dailymotion ni en Internet Archive.

### Frases (latino) de la primera pasada
Los sitios de audios no dicen de qué doblaje son. Las que no salen en la
tabla de arriba siguen ⚠️ hasta oírlas en la película latina.

| Frase | Quién | Estado |
|---|---|---|
| «**Estoy satisfecho con mi cuidado.**» | Hiro, al final | ✅ [audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397730), [TikTok #grandesheroes](https://www.tiktok.com/@gabymg82/video/7414332757213498630), [YouTube](https://www.youtube.com/watch?v=F8zuGaDxwkk) |
| «¿Estás satisfecho con tu cuidado?» | Baymax | ⚠️ [TikTok](https://www.tiktok.com/@cold_constellations/video/7189793084861975813) |
| ~~«No pueden desactivarme hasta que digas que estás satisfecho con mi cuidado.»~~ → **«Puedo desactivarme si dices que estás satisfecho con tu cuidado.»** | Baymax | ✅ corregida, oída ([x5hvz3y, 0:55](https://www.dailymotion.com/video/x5hvz3y?t=55)); la versión de [audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397146) no es la del doblaje |
| «Hola, yo soy Baymax, **tu** / **su** asistente médico personal.» | Baymax | ⚠️ circulan las dos: [«tu»](https://audiofrases.com/frases-de-peliculas-disney/audio-frases-de-big-hero-6-2014/hola-yo-soy-baymax-tu-asistente-medico-personal), [«su»](https://audiofrases.com/frases-de-peliculas-disney/audio-frases-de-big-hero-6-2014/hola-yo-soy-baymax-su-asistente-medico-personal) |
| «En una escala del uno al diez, ¿cómo calificarías tu dolor?» | Baymax | ⚠️ [blog de frases](https://frasesdecineparaelrecuerdo.blogspot.com/2015/01/frases-pelicula-big-hero-6.html), doblaje sin decir |
| «Puedes llorar si quieres. Llorar es una respuesta natural al dolor.» | Baymax | ⚠️ mismo blog |
| «Batería baja.» | Baymax | ⚠️ [audiofrases](https://audiofrases.com/frases-de-peliculas-disney/audio-frases-de-big-hero-6-2014/bateria-baja) |
| «Alguien tiene que ayudar.» | Tadashi | ✅ **en la serie** («Baymax Regresa», dos veces); en la película no tuvo traducción fija: Tadashi dice «No puedo dejarlo, comprende» e Hiro «La voy a salvar» ([guía de cuadros](../_ya_hechas/_Cuadros%20de%20dialogo%20por%20franquicia%20(23-sep-2026).md), [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes)) |
| «Bienvenidos a my house.» | Fred | ✅ guía de cuadros + Doblaje Wiki (en inglés es «Welcome a mi casa»: el doblaje lo dio la vuelta) |
| «¡Sí que está loco ese gato!» | Hiro, por Mochi | ⚠️ una fuente (Doblaje Wiki) |

Hay una comparativa de doblajes de Baymax y Tadashi en
[TikTok](https://www.tiktok.com/@zachinin72/video/7353779444345064709) y
un repaso del doblaje latino en
[YouTube, Draquio #72](https://www.youtube.com/watch?v=80-nWgE03aw):
**ahí se pueden oír y cerrar las ⚠️**.

---

## 11 · Música

- **Película:** música de **Henry Jackman**, 19 pistas, **orquestal y
  electrónica a la vez**, con una orquesta de 77 músicos. Y la canción
  **«Immortals» de Fall Out Boy** ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Big_Hero_6_(soundtrack)),
  [AWN](https://www.awn.com/news/big-hero-6-soundtrack-features-score-henry-jackman),
  [Bandcamp de Jackman](https://henryjackman.bandcamp.com/album/big-hero-6-original-motion-picture-soundtrack),
  [Discogs](https://www.discogs.com/master/1833271-Henry-Jackman-Big-Hero-6-Original-Score)).
  **Lista completa confirmada** ✅ (wikitext de [Wikipedia](https://en.wikipedia.org/wiki/Big_Hero_6_(soundtrack))
  y [AllMusic](https://www.allmusic.com/album/big-hero-6-original-motion-picture-soundtrack--mw0002772854);
  también en la [wiki de Disney](https://disney.fandom.com/wiki/Big_Hero_6_(soundtrack))):
  20 temas, 53:57. Immortals (3:16) · Hiro Hamada (1:57) · Nerd School
  (2:12) · Microbots (1:46) · Tadashi (1:46) · **Inflatable Friend** (1:56,
  la activación de Baymax) · **Huggable Detective** (1:35) · The Masked
  Man (1:29) · One of the Family (1:49) · Upgrades (2:27) · The Streets
  of San Fransokyo (4:08) · To the Manor Born (1:15) · So Much More (3:01)
  · First Flight (2:35) · **Silent Sparrow** (4:39) · Family Reunion
  (2:39) · **Big Hero 6** (6:57, la batalla final) · **I Am Satisfied with
  My Care** (5:29, el cierre) · Signs of Life (1:14) · Reboot (1:48).
  Que «Silent Sparrow» sea la música de la muerte de Tadashi se deduce
  por el nombre y el orden ⚠️ (no se oyó sobre la escena).
  La edición japonesa añade «Story» de **AI**, en inglés ✅.
  Reseña de la partitura: [Entertainment Junkie](http://entjunkie.blogspot.com/2014/11/big-hero-6-score-review.html).
- **Qué ambiente da:** cálido y emotivo en lo de Baymax y los hermanos;
  pulso electrónico y épico en la acción ⚠️ (de las reseñas, sin oírla).
- **«Immortals» suena en el montaje** en que los nerds arman sus trajes y
  se vuelven héroes, y otra vez en los **créditos** ✅ ([Dubbing Database](https://dubdb.fandom.com/wiki/Immortals_(Big_Hero_6)),
  vídeos de la escena). Audio del sencillo en
  [Internet Archive](https://archive.org/details/fall-out-boy-immortals-official-music-video-from-big-hero-6-160k).
- **Suena «Eye of the Tiger»** (instrumental), que **no está** en el disco
  ✅ ([The Tufts Daily](http://tuftsdaily.com/arts/2014/11/12/big-hero-6-succeeds-box-office), Wikipedia).
- **El sonido de Baymax**: se evitaron los pitidos de robot para que
  sonara «achuchable»; al moverse suena **una pelota de ejercicio que
  chirría** (Skywalker Sound y Disney) ⚠️ (una fuente, [Disney Digital
  Studio Services](https://www.disneydigitalstudio.com/the-baymax-buzz-behind-the-mix-of-big-hero-6/)).
  Encaja con lo oído en los clips: pasos con chirrido de goma, nunca
  bips.
- **Onomatopeyas que todos reconocen**: el «¡ay!» de Hiro que lo activa
  y el «ba-la-la-la-la» del choque de puños (dicho, no escrito). No
  encontré una onomatopeya de cómic oficial para ese gesto.
- **Kingdom Hearts III** tiene sus propios temas de San Fransokyo:
  «Robot Overdrive» (batalla), «Heroes' Gathering» (día) y «AR
  -Augmented Rhythm-» (noche) ✅ ([khwiki](https://www.khwiki.com/San_Fransokyo)).
- **Serie 2D:** tema de **Adam Berry** ✅
  ([Wikipedia, Adam Berry](https://en.wikipedia.org/wiki/Adam_Berry),
  [tema en YouTube](https://www.youtube.com/watch?v=TeNwMzQEaYk)).
  Pistas nuevas de la serie: [Tumblr](https://multimonorail.tumblr.com/post/652529278925291520/new-big-hero-6-the-series-soundtrack-tracks).
  **El opening de la serie, visto** ✅ («Season 3 Intro», [Dailymotion
  x7we0ri](https://www.dailymotion.com/video/x7we0ri), 0:33): 0:03-0:06
  el círculo rojo del botón de Baymax se ilumina y se funde con su
  silueta; 0:07-0:09 Baymax abraza a Hiro dentro de un **panal hexagonal
  rojo y dorado** (motivo propio de la serie); 0:15-0:25 paneles
  hexagonales con cada héroe (GoGo velocidad, Wasabi cuchillas verdes,
  Fred naranja, Honey Lemon esfera rosa); 0:32 logo «BIG HERO 6 THE
  SERIES» sobre panal rojo.
- **Para #soporte:** el lado tranquilo de Jackman, no «Immortals». Una
  consulta, no una pelea.

---

## 12 · Vídeos

**Minuto sin verificar en los de YouTube y TikTok** (no abren desde
aquí). **Lo visto de verdad va en §12.1.**

| Vídeo | Para qué sirve | Enlace |
|---|---|---|
| Baymax conoce a Hiro | pose de saludo y la escala | [YouTube](https://www.youtube.com/watch?v=cPwT1-2ZHgM) |
| «Hello, I am Baymax» | lo mismo, otro corte | [YouTube](https://www.youtube.com/watch?v=jlY-dEzTl0M) |
| Choque de puños, oficial HD | pose de celebrar | [YouTube](https://www.youtube.com/watch?v=yl8yriCIzCE) |
| Primer vuelo | la ciudad desde arriba | [YouTube](https://www.youtube.com/watch?v=HKwkOrFFEpg) |
| Microbots en el garaje, 4K | el garaje de Hiro con detalle | [YouTube](https://www.youtube.com/watch?v=3S3NadJwEQI) |
| Cómo se hizo San Fransokyo | luz y ciudad | [YouTube](https://www.youtube.com/watch?v=syWg8-uYHwY) |
| Tráiler de ¡Baymax! en latino | tono de enfermero de barrio | [YouTube](https://www.youtube.com/watch?v=r8ysizKgmQA) |
| Doblaje latino, Draquio #72 | oír las voces latinas | [YouTube](https://www.youtube.com/watch?v=80-nWgE03aw) |
| «Estoy satisfecho con mi cuidado» | la frase del final | [YouTube](https://www.youtube.com/watch?v=F8zuGaDxwkk) |
| Tema de la serie 2D | estilo 2D | [YouTube](https://www.youtube.com/watch?v=TeNwMzQEaYk) |
| Reseña del juego de 3DS | cómo se ve el juego | [YouTube](https://www.youtube.com/watch?v=64q5HBDZZjs) |

**TikTok (tendencias latinas):**
- **«Estoy satisfecho con mi cuidado»** es tendencia de nostalgia y
  llanto ✅ ([búsqueda de TikTok](https://www.tiktok.com/discover/baymax-estoy-satisfecho-con-mi-cuidado),
  [vídeo](https://www.tiktok.com/@gabymg82/video/7414332757213498630),
  [otro](https://www.tiktok.com/@soyy_fredy/video/7304854546101193989)).
- **Retos de doblaje** de SDV contra las voces oficiales
  ([Baymax](https://www.tiktok.com/@sdv_serviciosdevoz/video/7227258147939814662),
  [Hiro](https://www.tiktok.com/@sdv_serviciosdevoz/video/7137849402844089605?lang=es)).
  **Esto le va al servidor**: es de doblaje.
- **Homenaje a Alexis Ortega** ([TikTok](https://www.tiktok.com/@lavidadeldoblaje_/video/7600428235201006868)).
- Búsqueda «Hola soy Baymax»: [TikTok](https://www.tiktok.com/discover/hola-soy-baymax).
- Minuto exacto dentro de cada TikTok: ⚠️ sin ver (TikTok no abre aquí).

### 12.1 · Vídeos mirados en la segunda pasada (con minuto) ✅

**Tráiler oficial en español latino** («Grandes Héroes», sensacinemx,
Dailymotion, 2:31, [x889whz](https://www.dailymotion.com/video/x889whz)),
visto entero con `fotogramas.py --cortes` (92 fotogramas). Va pegado a
un avance de *Ralph, el Demoledor*:
- 0:16-0:33: logo de Disney y *Ralph, el Demoledor*.
- [0:39-1:00](https://www.dailymotion.com/video/x889whz?t=39): Baymax en el cuarto de Hiro, la escala de dolor, la interfaz de escaneo **en inglés** (el doblaje no traduce lo escrito en pantalla).
- 1:00-1:16: humo negro y sirenas del incendio del SFIT; Hiro en la comisaría; Baymax aparece detrás del mostrador (gag).
- 1:25-1:49: microbots, hologramas verdes, el traje rojo de Baymax, primer despegue.
- 1:51-2:05: vuelo sobre San Fransokyo, el grupo entero en el aire.
- Rótulos en español: «MUY PRONTO» (0:51), «UN GRAN DESCUBRIMIENTO LLEGARÁ» (0:58), «ÉL NOS GUIARÁ» (2:02), «ÉL NOS CUIDARÁ» (2:06), «ÉL CAMBIARÁ NUESTRO MUNDO» (2:10), logo «GRANDES HÉROES» (2:21).
- Otros tráilers latinos del mismo tipo: [x889whh](https://www.dailymotion.com/video/x889whh), [x2ez5rq](https://www.dailymotion.com/video/x2ez5rq), [Tomatazos, x8x29d6](https://www.dailymotion.com/video/x8x29d6).

**Clips de escenas** (§4.1): «Meet Baymax» [x2553ox](https://www.dailymotion.com/video/x2553ox),
«Low Battery» [x283k45](https://www.dailymotion.com/video/x283k45),
«Fist Bump» [x3wn7x2](https://www.dailymotion.com/video/x3wn7x2),
batalla final [x7vbgp7](https://www.dailymotion.com/video/x7vbgp7),
opening de la serie [x7we0ri](https://www.dailymotion.com/video/x7we0ri) (§11).

**Material del estudio en Internet Archive**:
- Escena eliminada «Hamada Brother Robotics», storyboard ([youtube-wnDrECylMOU](https://archive.org/details/youtube-wnDrECylMOU)).
- Featurette oficial «Animating Baymax», 104 s ([youtube-koKlm22FLk0](https://archive.org/details/youtube-koKlm22FLk0)): anotado, **no se miró fotograma a fotograma** ⚠️.

**Clips doblados oídos** (§10): [x2hry42](https://www.dailymotion.com/video/x2hry42) y [x5hvz3y](https://www.dailymotion.com/video/x5hvz3y).

---

## 13 · Videojuegos

| Juego | Qué hay | Fuentes |
|---|---|---|
| **Kingdom Hearts III** (2019) | mundo de San Fransokyo; se vuela sobre Baymax | [KH Wiki](https://www.khwiki.com/San_Fransokyo), [KH Database](https://www.khdatabase.com/San_Fransokyo), [KHInsider](https://www.khinsider.com/kingdom-hearts-3/worlds/san-fransokyo), [GameFAQs](https://gamefaqs.gamespot.com/ps4/718920-kingdom-hearts-iii/faqs/76812/san-fransokyo), [Game UI Database](https://www.gameuidatabase.com/gameData.php?id=596) |
| **Battle in the Bay** (3DS/DS, 2014) | de lado, sin voces ni escenas; nota 4/10; 1st Playable Productions y GameMill | [Nintendo Life](https://www.nintendolife.com/reviews/3ds/big_hero_6_battle_in_the_bay), [Metacritic](https://www.metacritic.com/game/disney-big-hero-6/critic-reviews/), [MediaMikes](https://mediamikes.com/2014/11/nintendo-3ds-video-game-review-big-hero-6-battle-in-the-bay/), [interfaz de Roberta Tam](https://dribbble.com/shots/3320537-Big-Hero-6-Battle-in-the-Bay-UI) |
| **Bot Fight** (móvil, 3-11-2014) | de Gumi para Disney Interactive | [TouchArcade](https://toucharcade.com/games/big-hero-6-bot-fight), [wiki de BH6](https://bighero6.fandom.com/wiki/Big_Hero_6:_Bot_Fight) |
| **Disney Infinity 2.0** | Baymax como figura jugable | [Videogaming Wiki](https://videogaming.fandom.com/wiki/Baymax) |
| **Disney Mirrorverse** | Baymax como «tanque» (Guardian) | [wiki de Mirrorverse](https://disney-mirrorverse.fandom.com/wiki/Baymax) |

- **The Cutting Room Floor:** tiene página de
  [Kingdom Hearts III](https://tcrf.net/Kingdom_Hearts_III), pero el
  buscador dice que la web estaba caída. **No encontré nada** de Battle
  in the Bay ni de Bot Fight.
- **Cajas de diálogo de los juegos:** no vi ninguna ⚠️. No hay una caja
  propia de Grandes Héroes que el fan reconozca: lo reconocible es la
  **pantalla de Baymax**. **Segunda pasada, reforzado** ✅: de los cinco
  juegos (KH3, Battle in the Bay, Bot Fight, Disney Infinity 2.0,
  Mirrorverse) ninguno tiene caja propia. Game UI Database y el Dribbble
  de Roberta Tam no cargaron (dos intentos cada uno).
- **Interfaces vistas en las hojas**: Hiro en *Disney Heroes: Battle Mode*
  con sus **SKILLS** (Megabot Call, Megabot Spin, Microbot Stun, Analyze),
  en recuadros redondeados sobre rojo (`colaboraciones_01.jpg`, n.º 204)
  ✅; Hiro en *Disney Sorcerer's Arena*, menú de mejora (n.º 234) ✅.
  Vocabulario de habilidades reutilizable para textos del bot.
- **KH3**: los temas del mundo se llaman «Robot Overdrive», «Heroes'
  Gathering» y «AR -Augmented Rhythm-» ✅ ([khwiki](https://www.khwiki.com/San_Fransokyo)).
- Más juegos y apps con Baymax (Lorcana, Fortnite, Sorcerer's Arena,
  Star Smash…): §F.

---

## 14 · Lo que el fandom ama, y qué NO hacer

### Lo que todos reconocen
- **La escala del dolor**: tanto, que hay pines y cordones oficiales
  (punto 2).
- **«Bebé peludo»**: Baymax sin batería con el gato Mochi en brazos. Y
  «¡Saltamos por una ventana!» ✅
  ([TV Tropes, memes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/BigHero6),
  [TV Tropes, momentos graciosos](https://tvtropes.org/pmwiki/pmwiki.php/Funny/BigHero6)).
- **El choque de puños «ba-la-la-la-la»** ([clip oficial](https://www.youtube.com/watch?v=yl8yriCIzCE)).
- **«Estoy satisfecho con mi cuidado»**: la frase que hace llorar en
  TikTok latino (punto 12).
- **El abrazo del «Gran Blanco»** (大白) en China (punto 2).
- **La gorra de Tadashi** como recuerdo (punto 9).
- Más: [TV Tropes, YMMV](https://tvtropes.org/pmwiki/pmwiki.php/YMMV/BigHero6),
  [referencias](https://tvtropes.org/pmwiki/pmwiki.php/ShoutOut/BigHero6),
  [detalles escondidos, Ranker](https://www.ranker.com/list/big-hero-6-fan-details-easter-eggs/sawyer-grant).

### Qué NO hacer (lo que a un fan le parecería falso)
- **Ponerle boca a Baymax** o un globo de cómic. Su cara es sólo dos
  puntos y una raya, a propósito.
- **Hacerlo rápido o agresivo.** Anda a pasitos y habla despacio. La
  armadura roja es para pelear: **en #soporte va blanco**, sin armadura.
- **Copiar las caras de Wong-Baker tal cual**: tienen derechos (punto 3).
- **Mezclar la película (3D) con la serie (2D)** en la misma lámina. La
  serie cambió el dibujo a propósito ✅
  ([TheWrap](https://www.thewrap.com/big-hero-6-the-series-eps-talk-giving-a-beloved-film-a-whole-new-look/)).
- **Frases de España** («Big Hero 6», «mis cuidados»): el servidor es
  latino.
- **Bromas con la muerte de Tadashi** o con la voz de Alexis Ortega.
- Poner el café, la ciudad o el garaje **sin mezcla japonesa**: San
  Fransokyo siempre es mitad San Francisco, mitad Tokio.

---

## 15 · Poses analizadas, por personaje

> [!warning] No pude ver los vídeos
> Lo que hace cada personaje en cada escena es **de memoria ⚠️**. El
> enlace es real; **hay que comprobar la pose en el clip** antes de
> dibujarla. Minuto sin verificar.

### Baymax
| # | Escena y enlace | Postura, manos, mirada | Sirve para |
|---|---|---|---|
| 1 | Se infla y saluda ([clip](https://www.youtube.com/watch?v=cPwT1-2ZHgM)) | de pie, recto; una mano levantada a la altura de la cabeza | **presentar** |
| 2 | Escanea a Hiro ([clip](https://www.youtube.com/watch?v=jlY-dEzTl0M)) | quieto, cabeza un poco inclinada, mira al paciente | **pensar** |
| 3 | La escala en el pecho ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Funny/BigHero6)) | de frente, brazos abajo, el pecho encendido | **explicar** |
| 4 | Choque de puños ([clip](https://www.youtube.com/watch?v=yl8yriCIzCE)) | puño adelante y luego los dedos abiertos, moviéndose | **celebrar** |
| 5 | Batería baja con Mochi ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/BigHero6)) | cuerpo caído, el gato en brazos | chiste de lámina 2 |
| 6 | Abrazo a Hiro | brazos alrededor, cabeza baja | **animar** |
| 7 | Vuelo con armadura ([clip](https://www.youtube.com/watch?v=HKwkOrFFEpg)) | horizontal, Hiro en la espalda | acción (no para soporte) |
| 8 | Poses con esqueleto de Kevin Nelson ([blog](http://artofkevinnelson.blogspot.com/2014/11/baymax-poses-with-visible-skeleton-from.html)) | cómo dobla cintura, brazos y cuello | construir cualquier pose |

**Regañar:** Baymax no regaña. Avisa con calma y se queda firme, brazos
abajo, sin moverse (como cuando no se desactiva). Usar la pose 3.

### Hiro
| # | Escena y enlace | Postura, manos, mirada | Sirve para |
|---|---|---|---|
| 1 | Dice «¡ay!» y Baymax se enciende ([clip](https://www.youtube.com/watch?v=cPwT1-2ZHgM)) | en el suelo o encogido, mano en la cabeza | **el paciente** que abre ticket |
| 2 | Microbots en el garaje ([clip](https://www.youtube.com/watch?v=3S3NadJwEQI)) | concentrado, la diadema de control puesta | **pensar**, explicar |
| 3 | Mejora a Baymax ([clip](https://www.youtube.com/watch?v=wILlTsjnYYw), [placa](https://www.youtube.com/watch?v=BlPMfo1gaoo)) | inclinado sobre él, herramientas en la mano | **explicar** |
| 4 | Choque de puños ([clip](https://www.youtube.com/watch?v=yl8yriCIzCE)) | puño adelante, sonrisa | **celebrar** |
| 5 | Primer vuelo ([clip](https://www.youtube.com/watch?v=HKwkOrFFEpg)) | brazos abiertos, gritando de alegría | **animar** |
| 6 | Final: «estoy satisfecho» ([YouTube](https://www.youtube.com/watch?v=F8zuGaDxwkk)) | ojos húmedos, voz baja | **cerrar el ticket** |

### Tadashi
| # | Escena | Postura | Sirve para |
|---|---|---|---|
| 1 | Presenta a Baymax a Hiro en el laboratorio | brazo tendido hacia Baymax, orgulloso | **presentar** |
| 2 | Su vídeo de prueba ([audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397715)) | sentado ante la cámara, cansado y sonriente | **explicar** |
| 3 | Anima a Hiro | mano en el hombro, gorra puesta | **animar** |
| 4 | Fan art de Brandon Lawless ([ArtStation](https://www.artstation.com/artwork/wPY56)) | con GoGo | referencia de fan |

Las tres de Tadashi son ⚠️ de memoria y no tienen clip.

---

## 16 · Vestuario

| Personaje | Ropa icónica | Colores (hex aprox., sin medir) | Estado |
|---|---|---|---|
| **Baymax, película** | vinilo blanco, sin nada | `#F4F3EF`, sombra `#C9CFD6`, ojos `#1B1B1B` | ✅ forma; ⚠️ hex |
| Baymax con armadura | armadura roja, alas, puño cohete | rojo `#C4252B` | ⚠️ de memoria el detalle |
| **Hiro, de calle** | sudadera azul marino, camiseta roja con robot, cargo beige, zapatillas marrones con cordones amarillos | `#2B3550`, `#B83A33`, `#8C7A5B`, cordones `#E8C547` | ✅ ropa ([wiki](https://disney.fandom.com/wiki/Hiro_Hamada)); ⚠️ hex |
| Hiro con armadura | morado, rojo y negro, placas magnéticas rojas | `#5B3C8C`, `#C4252B`, `#1E1E24` | ✅ ([wiki](https://bighero6.fandom.com/wiki/Hiro's_Super_Armor)) |
| **Tadashi** | gorra negra «San Fransokyo Ninja» en rojo y dorado | `#1B1B1B`, `#B8322E`, `#C9A13B` | ✅ gorra ([wiki](https://bighero6.fandom.com/wiki/Tadashi_Hamada)); resto ⚠️ |
| Serie 2D | los mismos, dibujo plano | — | no mezclar con la película |

**Lo icónico que todos reconocen:** Baymax blanco sin armadura, Hiro con
la sudadera, la gorra de Tadashi.

---

## 17 · Ciudades, paisajes y fondos de pantalla

- **San Fransokyo de día, en cuesta**, con tranvías y rótulos japoneses;
  **de noche**, farolas y neones; **al atardecer**, dorado sobre la bahía
  ⚠️ (de memoria; la luz real, punto 6).
- **Fondos de pantalla** (casi todos son fotogramas oficiales; autor sin
  dato):
  - [«Baymax & Hiro», 3840×2160](https://wall.alphacoders.com/big.php?i=1103184)
  - [«Baymax & Hiro», 3840×2160](https://wall.alphacoders.com/big.php?i=1103186)
  - [Baymax, 4K](https://wall.alphacoders.com/big.php?i=555837)
  - [colección 4K de Wallpaper Abyss](https://wall.alphacoders.com/by_sub_category.php?id=226964&name=Big+Hero+6+Wallpapers&filter=4K+Ultra+HD)
  - [WallpaperAccess 4K](https://wallpaperaccess.com/big-hero-6-4k),
    [Wallpaper Cave](https://wallpapercave.com/big-hero-6-wallpapers),
    [HDQwalls](https://hdqwalls.com/big-hero-6-wallpapers),
    [WallpaperFlare](https://www.wallpaperflare.com/search?wallpaper=big+hero+6).
- Los pósters grandes de IMP Awards (punto 3) sirven también de fondo.

---

## A · Estilo de dibujo y técnica, y cómo replicarlo (punto 18)

(pendiente)

---

## B · Texturas 2D (punto 19)

(pendiente)

---

## C · Gustos y detalles de cada personaje (punto 20)

(pendiente)

---

## D · Por qué la gente la ama (punto 21)

(pendiente)

---

## E · Fan dubs y comunidad hispana (punto 22)

(pendiente)

---

## F · Colaboraciones, figuras y cosplay (punto 23)

(pendiente)

---

## G · Obras parecidas y temas relacionados (punto 24)

(pendiente)

---

## H · El mundo, la historia y sus símbolos (punto 25)

(pendiente)

---

## 18 · Guía para describir el estilo a una IA de imagen

Sólo es una guía que pide el encargo. **Las láminas no se hacen con IA**:
el dueño pide que no parezca IA.

**Rasgos que nunca cambian**
- **Baymax:** cuerpo blanco inflable en forma de pera o campana, cabeza
  pequeña, **cara de dos puntos negros unidos por una raya fina**, sin
  boca ni nariz, brazos gordos y blandos, piernas cortas. Vinilo mate con
  brillo suave.
- **Hiro:** 14 años, pelo negro corto y revuelto, ojos marrones, sudadera
  azul marino, camiseta roja, cordones amarillos.
- **Tadashi:** gorra negra con letras rojas y doradas.

**Estilo:** animación 3D de Disney de 2014, luz rebotada realista,
desenfoque de cine, colores limpios, formas redondas y simples.

**Luz:** hospital fría de techo; garaje cálido de noche; atardecer dorado
en la ciudad.

**Encuadre:** Baymax ocupa mucho; la cámara un poco baja lo hace grande
y suave.

**Palabras que ayudan:** «inflatable white vinyl robot», «two black dots
connected by a thin line», «no mouth», «soft rounded shapes», «Disney 3D
animation 2014», «San Francisco and Tokyo hybrid city», «warm cinematic
lighting».

**Palabras que lo estropean:** «mouth», «smile», «armor» (si no la
quieres), «anime», «2D», «metal robot», «scary», «sharp».

**Qué imágenes dar de referencia:** estilo, los pósters de IMP Awards y
los fondos 3840×2160 de Wallpaper Abyss; pose, los clips del punto 15 y
las poses con esqueleto de Kevin Nelson.

---

## 19 · Tres conceptos de lámina

Los números «ref. n.º» son la posición en `referencias.json` (36
referencias, contando desde 1). Las más usadas: 1 y 2 saludo de Baymax,
3 choque de puños, 5 garaje, 12 y 13 Hiro con Baymax en 4K, 15 poses con
esqueleto, 20 Lucky Cat Café, 21 malla 3D, 23 carrito, 24 y 25 HDRI,
28 escala Wong-Baker real.

### Concepto A — «La tabla del dolor de la consulta» (laboratorio de Tadashi)

- **Objeto real:** una **tabla del dolor plastificada**, como las de las
  consultas de verdad, pegada con cinta en la pared del laboratorio.
  **Se hace en Blender:** un plano con brillo de plástico, una esquina
  levantada y dos tiras de cinta. Las caras son **propias, al estilo de
  Baymax** (dos puntos y una raya que se tuerce), del 0 al 10 en cinco
  franjas. No son las de Wong-Baker (ref. n.º 28, sólo para ver cómo es
  una de verdad).
- **Sitio:** el laboratorio de robótica del SFIT, donde Tadashi creó a
  Baymax. Luz de día por ventanales y relleno frío de fluorescente
  (HDRI de hospital, ref. n.º 24).
- **Personaje:** **Baymax** (el más querido). De pie junto a la tabla,
  **un brazo levantado señalándola** y la cabeza un poco inclinada.
  Pose de saludo de ref. n.º 1 y 2; cómo dobla el brazo, ref. n.º 15.
- **Cómo habla:** su barriga proyecta **«Hola. Estoy aquí para
  ayudarte.»** en Nunito Black, luz clara sobre el vinilo, curvada.
- **Dónde va cada texto:**
  - Cabecera impresa de la tabla: **¿CUÁNTO TE DUELE?**
  - Las cinco franjas: nivel, cara, nombre y un ejemplo corto.
  - Pizarra blanca de Tadashi, al lado, a rotulador (Caveat):
    **Abre un ticket.** y **Solo lo vemos tú y el staff.**
  - Tira impresa al pie de la tabla: **El ticket se cierra cuando digas
    que estás satisfecho con tu cuidado.**
- **Para que no quede plano:** delante, a la izquierda y desenfocado, el
  **carrito de herramientas** (ref. n.º 23) con **la gorra de Tadashi**
  encima, pequeña. El plástico de la tabla refleja la ventana. Al fondo,
  piezas de robot desenfocadas.

### Concepto B — «El escaneo» (el garaje de Hiro, de noche)

- **Objeto real:** **la barriga de Baymax** como pantalla. En Blender se
  **proyecta la tabla sobre su barriga redonda**, así la imagen se curva
  con el vinilo. La malla de Sketchfab (ref. n.º 21, CC BY) sirve sólo
  para calcular esa curva; el Baymax visible sale de fotogramas por
  `v3/integrar.py`.
- **Sitio:** el garaje de Hiro de noche: banco de trabajo, pantallas,
  lámpara cálida (ref. n.º 5; HDRI de garaje, ref. n.º 25).
- **Personajes:** **Baymax** de pie, brazos un poco abiertos, la barriga
  encendida (pose 3 del punto 15). **Hiro** sentado en el taburete,
  **mano en la cabeza**, acaba de decir «¡ay!» y mira la barriga (ref.
  n.º 1). Hiro es el usuario que abre el ticket.
- **Cómo habla:** en la barriga, **«Del 0 al 10, ¿cuánto te duele?»** y
  la escala de cinco caras debajo, en Nunito.
- **Dónde va cada texto:**
  - Título en la barriga: la pregunta.
  - Notas adhesivas de Hiro pegadas en su monitor, a mano (Caveat):
    **Abre un ticket.** / **Solo lo vemos tú y el staff.**
  - Una nota más, en la puerta del garaje: **El ticket se cierra cuando
    digas que estás satisfecho con tu cuidado.**
- **Para que no quede plano:** **el gato Mochi** dormido en el banco, en
  primer plano y desenfocado. Microbots sueltos en la mesa. **La luz de
  la barriga ilumina la cara de Hiro** en frío; la lámpara, cálida, por
  detrás.

### Concepto C — «Ticket cerrado» (el mostrador del Lucky Cat Café)

- **Objeto real:** **una comanda del café**, el papelito del pedido,
  clavada en el pincho del mostrador. Juego de palabras: es un
  **ticket**. **Se hace en Blender:** papel térmico curvado, letras de
  impresora, un sello a mano. El pincho de comandas es un objeto típico
  de café; **no comprobé que salga en la película** ⚠️.
- **Sitio:** el Lucky Cat Café de la tía Cass: madera, farolillos,
  flores de cerezo, gatos de la suerte (ref. n.º 20).
- **Personajes:** **Hiro y Baymax chocan el puño**, «ba-la-la-la-la»,
  detrás del mostrador (ref. n.º 3; los dos juntos, ref. n.º 12 y 13).
  **Celebrar**: el ticket se cerró. La tía Cass saluda al fondo,
  desenfocada.
- **Cómo habla:** la comanda es el cuadro. Texto impreso en **Share Tech
  Mono**, sello y nota a mano en **Caveat**. La barriga de Baymax,
  pequeña: **«¿Estás satisfecho con tu cuidado?»**
- **Dónde va cada texto (en la comanda):**
  - Arriba: **TICKET N.º 0001**
  - **PEDIDO: tu problema.**
  - **MESA: privada. Solo tú y el staff.**
  - **DOLOR: 0 1 2 3 4 5 6 7 8 9 10**, con un número rodeado.
  - Sello rojo a mano: **CERRADO. Estoy satisfecho con mi cuidado.**
  - En la pizarra del café, detrás: **Abre tu ticket aquí.**
- **Para que no quede plano:** **un gato de la suerte** en el mostrador,
  delante y desenfocado. Vapor de una taza. La comanda, nítida, en
  primer plano. Por la ventana, la calle en cuesta con luces
  desenfocadas.

**Lámina 2** (punto 1): la tabla completa con ejemplos, y los avisos de
#sugerencias y de las sanciones. Encaja con el concepto A (otra tabla en
la misma pared) o con el C (el «menú del día» del café).

---

## 20 · Lo que no pude verificar

- **Ninguna imagen ni vídeo visto.** Sin red completa no hubo hojas de
  contacto, ni colores medidos, ni minutos exactos.
- **Cómo es exactamente la escala en el pecho de Baymax** (cuántas caras,
  qué colores): sólo sé que es la Wong-Baker, de feliz a llorando ✅.
  Los colores verde, amarillo y rojo de los pines no los vi.
- **Frases latinas exactas**: sólo «Estoy satisfecho con mi cuidado»
  tiene dos fuentes (de fans). El resto, ⚠️ hasta oírlas.
- **Voces latinas de Fred, GoGo y Wasabi**: no las encontré.
- **Estudio y director del doblaje latino**: sólo Doblaje Wiki.
- **Voz latina de Baymax en ¡Baymax! (2022)**: sin confirmar.
- **Cómo se abre el ticket en el servidor**: el inventario no lo dice.
- **La escala del servidor** (qué entra en cada nivel) es propuesta mía:
  falta su sí.
- **El logo**: no pude compararlo con las letras libres.
- **Cajas de diálogo de los juegos** y **TCRF**: nada visto.
- **Encuestas oficiales** de popularidad: no existen o no las encontré.
- **Reddit** no dejó buscar (el buscador lo rechaza) y Arctic Shift no
  responde desde aquí.

---

## 21 · Fuentes consultadas

En el texto hay **214 enlaces distintos**. Aquí van las fuentes que
sostienen algo, **por tipo** (97). Todas salieron en el buscador o se
abrieron por GitHub.

### Oficiales y del equipo
1. [Disney Animation, motor Hyperion](https://disneyanimation.com/technology/hyperion/)
2. [Disney+ Press, ¡Baymax!](https://press.disneyplus.com/news/disney-plus-to-debut-new-series-baymax)
3. [Disney News, ¡Baymax!](https://news.disney.com/baymax-animated-series)
4. [Kit de prensa de ¡Baymax!](https://dmedmedia.disney.com/disney-plus/baymax)
5. [The Art of Big Hero 6, Google Books](https://books.google.com/books/about/The_Art_of_Big_Hero_6.html?id=WNmqBwAAQBAJ)
6. [Kevin Nelson, bocetos tempranos de Baymax](http://artofkevinnelson.blogspot.com/2014/12/some-really-early-baymax-sketches-from.html)
7. [Kevin Nelson, Baymax con esqueleto](http://artofkevinnelson.blogspot.com/2014/11/baymax-poses-with-visible-skeleton-from.html)
8. [Kevin Nelson, Baymax, Togo y Yama](http://artofkevinnelson.blogspot.com/2014/11/big-hero-6-artwork-with-baymax-togo-and.html)
9. [Kevin Nelson, GoGo temprana](http://artofkevinnelson.blogspot.com/2014/11/early-gogo-from-big-hero-6.html)
10. [Carnegie Mellon, el brazo inflable](https://www.cmu.edu/news/stories/archives/2014/october/october29_baymax.html)
11. [Chris Atkeson, «Why Baymax»](http://www.cs.cmu.edu/~cga/bighero6/why/)
12. [Red Bull JP, Koyama Shigeto](https://www.redbull.com/jp-ja/behind-the-mask-15)
13. [eiga.com, los diseñadores: cascabel y olla arrocera](https://eiga.com/news/20141201/6/)
14. [Roberta Tam, interfaz del juego de 3DS](https://dribbble.com/shots/3320537-Big-Hero-6-Battle-in-the-Bay-UI)
15. [Jayse Hansen, página de Big Hero 6](https://jayse.io/?portfolio=big-hero-6-coming-soon)
16. [Bandcamp de Henry Jackman](https://henryjackman.bandcamp.com/album/big-hero-6-original-motion-picture-soundtrack)
17. [Wong-Baker, condiciones de uso](https://wongbakerfaces.org/resources/usage-guidelines/)
18. [Wong-Baker, uso en publicaciones](https://wongbakerfaces.org/licensing-dashboard/publishing-use/)
19. [Wong-Baker, preguntas frecuentes](https://wongbakerfaces.org/us/faq/)
20. [Wong-Baker, hoja en español (PDF)](https://wongbakerfaces.org/wp-content/uploads/2016/06/FACES_Spanish_Blue_w-instructions.pdf)

### Prensa y análisis
21. [Cartoon Brew, Hyperion](https://www.cartoonbrew.com/tech/disney-explains-its-powerful-new-hyperion-rendering-engine-117152.html)
22. [fxguide, Hyperion](https://www.fxguide.com/fxfeatured/disneys-new-production-renderer-hyperion-yes-disney/)
23. [Gizmodo, San Fransokyo](https://gizmodo.com/a-tour-of-san-fransokyo-the-hybrid-city-disney-built-f-1642066794)
24. [Vice, el mundo más grande de Disney](https://www.vice.com/en/article/heres-how-disney-built-its-biggest-world-ever-for-big-hero-6/)
25. [Engadget, 55.000 núcleos](https://www.engadget.com/2014-10-18-disney-big-hero-6.html)
26. [Global News, robótica](https://globalnews.ca/news/1663166/big-hero-6-star-baymax-inspired-by-robotics-research/)
27. [NEXTpittsburgh, robot blando](https://nextpittsburgh.com/business-tech-news/cmu-soft-robot-inspires-disneys-newest-movie-hero-baymax/)
28. [AWN, reseña del libro de arte](https://www.awn.com/animationworld/book-review-art-big-hero-6)
29. [AWN, banda sonora](https://www.awn.com/news/big-hero-6-soundtrack-features-score-henry-jackman)
30. [TheWrap, por qué la serie es 2D](https://www.thewrap.com/big-hero-6-the-series-eps-talk-giving-a-beloved-film-a-whole-new-look/)
31. [IndieWire, ¡Baymax!](https://www.indiewire.com/features/general/baymax-big-hero-6-disney-plus-1234737544/)
32. [The Illuminerdi, ¡Baymax! y los sanitarios](https://theilluminerdi.com/2022/06/27/baymax-creators-healthcare-focus/)
33. [Rated PT, la escala en la película](https://ratedpt.wordpress.com/2021/02/16/big-hero-6-on-a-scale-of-1-10/)
34. [Nintendo Life, Battle in the Bay](https://www.nintendolife.com/reviews/3ds/big_hero_6_battle_in_the_bay)
35. [Comic Book Video Games, Battle in the Bay](https://comicbookvideogames.com/2014/11/07/review-big-hero-6-battle-in-the-bay-nintendo-3ds/)
36. [MediaMikes, Battle in the Bay](https://mediamikes.com/2014/11/nintendo-3ds-video-game-review-big-hero-6-battle-in-the-bay/)
37. [Metacritic, Battle in the Bay](https://www.metacritic.com/game/disney-big-hero-6/critic-reviews/)
38. [Escape Studios, secretos del diseño](https://escapestudiosanimation.blogspot.com/2017/10/big-hero-6-character-design-secrets.html)
39. [Character Design blog, el libro de arte](https://characterdesign.blogspot.com/2016/08/the-art-of-big-hero-6.html)
40. [Entertainment Junkie, la partitura](http://entjunkie.blogspot.com/2014/11/big-hero-6-score-review.html)

### En otros idiomas
41. 🇯🇵 [Tokyo Location Box, el cascabel de Hanazono](https://www.locationbox.metro.tokyo.lg.jp/location/list/260/)
42. 🇯🇵 [アニメ！アニメ！, Baymax en Hanazono](https://animeanime.jp/article/2015/01/19/21637.html)
43. 🇯🇵 [ねとらぼ, la cara es el cascabel](https://nlab.itmedia.co.jp/nl/articles/1501/19/news144.html)
44. 🇯🇵 [Wikipedia JA, ベイマックス](https://ja.wikipedia.org/wiki/%E3%83%99%E3%82%A4%E3%83%9E%E3%83%83%E3%82%AF%E3%82%B9)
45. 🇯🇵 [eiga.com, ficha y reparto](https://eiga.com/movie/80460/)
46. 🇯🇵 [Animate Times, reparto japonés](https://www.animatetimes.com/tag/details.php?id=9720)
47. 🇯🇵 [Oricon, reparto japonés](https://www.oricon.co.jp/special/68756/)
48. 🇯🇵 [みんなのランキング, personajes](https://ranking.net/rankings/best-baymax-characters)
49. 🇯🇵 [Pixiv, diccionario: Tadashi](https://dic.pixiv.net/a/%E3%82%BF%E3%83%80%E3%82%B7%E3%83%BB%E3%83%8F%E3%83%9E%E3%83%80)
50. 🇨🇳 [China News, peluches agotados](https://www.chinanews.com.cn/m/cul/2015/03-02/7092799.shtml)
51. 🇨🇳 [China Daily, «大白»](http://china.chinadaily.com.cn/shizheng/2015-03/06/content_19740449.htm)
52. 🇨🇳 [People's Daily, «大众情人»](http://paper.people.com.cn/rmrbhwb/html/2015-04/03/content_1549893.htm)
53. 🇨🇳 [Sanlian, abrazar a Baymax](https://www.lifeweek.com.cn/article/149429)
54. 🇨🇳 [36Kr, el fenómeno 大白](https://36kr.com/p/1478767128599810)
55. 🇰🇷 [Namuwiki, 베이맥스](https://namu.wiki/w/%EB%B2%A0%EC%9D%B4%EB%A7%A5%EC%8A%A4)
56. 🇰🇷 [Nurse-Link, la escala NRS](https://nurse-link.co.kr/community/campus_talk/108851764)

### Wikis de fans y TV Tropes
57. [Wiki de BH6, Baymax](https://bighero6.fandom.com/wiki/Baymax)
58. [Wiki de BH6, Lucky Cat Café](https://bighero6.fandom.com/wiki/Lucky_Cat_Caf%C3%A9)
59. [Wiki de BH6, Tadashi](https://bighero6.fandom.com/wiki/Tadashi_Hamada)
60. [Wiki de BH6, armadura de Hiro](https://bighero6.fandom.com/wiki/Hiro's_Super_Armor)
61. [Wiki de BH6, chips de Baymax](https://bighero6.fandom.com/wiki/Baymax's_Chips)
62. [Wiki de Disney, Hiro](https://disney.fandom.com/wiki/Hiro_Hamada)
63. [Wiki de Disney, Lucky Cat Café](https://disney.fandom.com/wiki/Lucky_Cat_Caf%C3%A9)
64. [Wiki de Disney, banda sonora](https://disney.fandom.com/wiki/Big_Hero_6_(soundtrack))
65. [Wiki Grandes Héroes (español), Baymax](https://grandes-heroes.fandom.com/es/wiki/Baymax)
66. [TV Tropes, momentos graciosos](https://tvtropes.org/pmwiki/pmwiki.php/Funny/BigHero6)
67. [TV Tropes, memes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/BigHero6)
68. [TV Tropes, personajes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/BigHero6)
69. [KH Wiki, San Fransokyo](https://www.khwiki.com/San_Fransokyo)
70. [TCRF, Kingdom Hearts III](https://tcrf.net/Kingdom_Hearts_III)
71. [Wikipedia, banda sonora](https://en.wikipedia.org/wiki/Big_Hero_6_(soundtrack))
72. [Wikipedia, la serie](https://en.wikipedia.org/wiki/Big_Hero_6:_The_Series)

### Foros y comunidades
73. [dafont, hilo del logo](https://www.dafont.com/forum/read/184224/big-hero-6-logo-font)
74. [dafont, letra del póster](https://www.dafont.com/forum/read/226321/big-hero-6-poster-font-not-logo)
75. [Fanpop, opinión de un fan](https://www.fanpop.com/clubs/big-hero-6/articles/252355/title/review-big-hero-6-characters)
76. [Tumblr, pistas de la serie](https://multimonorail.tumblr.com/post/652529278925291520/new-big-hero-6-the-series-soundtrack-tracks)

### Arte, 3D y recursos
77. [IMP Awards, 20 pósters](http://www.impawards.com/2014/big_hero_six_gallery.html)
78. [Sketchfab, Baymax de jasonballingham](https://sketchfab.com/3d-models/baymax-03bd50cd3998407aa8097bccb6f5c921)
79. [Sketchfab, Baymax de theamazingdonovan207](https://sketchfab.com/3d-models/baymax-big-hero-6-9a96e8526d5a4abaaa184830c20ab4ec)
80. [Poly Haven, carrito de herramientas](https://polyhaven.com/a/tool_cart)
81. [Poly Haven, HDRI de hospital](https://polyhaven.com/a/hospital_room)
82. [Poly Haven, HDRI de garaje](https://polyhaven.com/a/garage)
83. [Pixiv, Baymax y Hiro](https://www.pixiv.net/en/artworks/98296721)
84. [DeviantArt, Catel23](https://www.deviantart.com/catel23/art/Big-hero-6-Hiro-and-Baymax-2D-old-Disney-style-635327313)
85. [ArtStation, Brandon Lawless](https://www.artstation.com/artwork/wPY56)
86. [Wallpaper Abyss, 3840×2160](https://wall.alphacoders.com/big.php?i=1103184)
87. [Hot Topic, pin de la escala](https://www.hottopic.com/product/disney-big-hero-6-baymax-pain-scale-3-pin/10396449.html)
88. [FontMeme, letra de fan](https://fontmeme.com/big-hero-6-font/)

### Vídeo
89. [YouTube, Baymax conoce a Hiro](https://www.youtube.com/watch?v=cPwT1-2ZHgM)
90. [YouTube, choque de puños oficial](https://www.youtube.com/watch?v=yl8yriCIzCE)
91. [YouTube, cómo se hizo San Fransokyo](https://www.youtube.com/watch?v=syWg8-uYHwY)
92. [TikTok, tendencia «estoy satisfecho»](https://www.tiktok.com/discover/baymax-estoy-satisfecho-con-mi-cuidado)

### Código (GitHub)
93. [ANN, ficha del manga (copia en GitHub)](https://raw.githubusercontent.com/ToshY/anime-news-network-encyclopedia/HEAD/encyclopedia/manga/16985.json)
94. `google/fonts`: 24 letras, metadatos y archivos (punto 7).

### Doblaje latino
95. [Doblaje Wiki, Grandes héroes](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes)
96. [PRODU, entrevista a Memo Aponte](https://www.produ.com/television/noticias/actor-guillermo-aponte-de-disney-mi-voz-como-hiro-en-grandes-heroes-de-disney-representa-un-trabajo-actoral-muy-fuerte/)
97. [El Imparcial, Alexis Ortega](https://www.elimparcial.com/espectaculos/2026/01/27/fallece-alexis-ortega-voz-de-spider-man-en-espanol-latino-y-tadashi-en-grandes-heroes/)

(Más de doblaje en la tabla del punto 10: Infobae, El Informador,
LatinUS, SoundCloud, Radio Disney MX, dubdb, eldoblaje, audiofrases.)

---

## Cumplimiento del encargo

(pendiente)

---

## 22 · Bitácora de búsqueda

### Estado de la red
- `curl https://community.fandom.com` → **000 (403 del proxy)**. Sin red
  completa: **no se usó `investigar_serie.py`, no hay hojas de contacto
  ni carpeta `hojas/`**.
- También dieron 403 o 000: Doblaje Wiki (API), audiofrases, la wiki
  Grandes Héroes, la wiki de BH6, TV Tropes, Wong-Baker, eldoblaje,
  Arctic Shift, Wayback Machine, Game UI Database, IMP Awards, la CDN de
  ANN, jayse.io, Dribbble, cmu.edu y cs.cmu.edu.
- **Sí respondieron:** `raw.githubusercontent.com` y `pypi.org`.
  `api.github.com` pide añadir el repositorio a la sesión; se usó el
  buscador de GitHub (MCP) en su lugar.
- **Buscador: 49 búsquedas** (48 válidas y 1 rechazada). Se paró ahí por
  el cupo.

### Búsquedas hechas (idioma)
1. Reparto latino de la película en doblaje.fandom.com (español)
2. Estudio y dirección del doblaje latino (español)
3. Doblaje latino de la serie 2D (español)
4. Doblaje latino de ¡Baymax! 2022 (español)
5. Reparto latino en dubdb, Behind The Voice Actors e IMDb (inglés)
6. «Baymax» «Alan Prieto» «Memo Aponte» Tadashi (español)
7. La escala Wong-Baker en el pecho de Baymax (inglés)
8. Licencia de Wong-Baker y versión en español (inglés)
9. «En una escala del 1 al 10», frase latina (español)
10. audiofrases, «escala» y «calificarías» (español)
11. Diseño de Baymax: cascabel, CMU, Atkeson (inglés)
12. The Art of Big Hero 6, Paul Felix (inglés)
13. San Fransokyo y Hyperion (inglés)
14. ベイマックス ドン・ホール インタビュー デザイン 鈴 (japonés)
15. 超能陆战队 大白 人气 (chino)
16. Personaje favorito en reddit.com (inglés): **rechazada**, el buscador
    no permite reddit
17. ディズニー キャラクター 人気ランキング ベイマックス (japonés)
18. Memes en TV Tropes y Know Your Meme (inglés)
19. ベイマックスキャラ人気ランキング en ranking.net (japonés)
20. Personajes mejor valorados por fans (inglés)
21. Clip «Hello, I am Baymax» en YouTube (inglés)
22. Clip «Hola, yo soy Baymax» en latino (español)
23. Banda sonora y tema de la serie (inglés)
24. Estilo 2D de la serie (inglés)
25. Kingdom Hearts III, San Fransokyo (inglés)
26. Battle in the Bay, 3DS (inglés)
27. La letra del logo en dafont y FontMeme (inglés)
28. La interfaz del pecho de Baymax (inglés)
29. Baymax en Sketchfab (inglés)
30. Carrito médico, portapapeles y banco CC0 (inglés)
31. Lucky Cat Café y el garaje (inglés)
32. La gorra de Tadashi y el SFIT (inglés)
33. «Alexis Ortega» Tadashi (español)
34. «escala del uno al diez» «calificarías tu dolor» (español)
35. Colores de la escala en el pecho (inglés)
36. Pósters oficiales en IMP Awards (inglés)
37. Arte de desarrollo: Kim, Bove, Nelson (inglés)
38. ベイマックス イラスト pixiv (japonés)
39. ¡Baymax! 2022, entrevistas (inglés)
40. ベイマックス 吹き替え 興行収入 (japonés)
41. Ropa y armadura de Hiro (inglés)
42. Fondos de pantalla 4K (inglés)
43. Wong-Baker y Baymax en la web de la fundación (inglés)
44. Poly Haven: hospital, garaje y texturas (inglés)
45. Bot Fight, Disney Infinity, Mirrorverse, TCRF (inglés)
46. Tendencia de TikTok «estoy satisfecho con mi cuidado» (español)
47. «Memo Aponte» Hiro (español)
48. 베이맥스 통증 척도 (coreano)
49. TCRF: Battle in the Bay y Kingdom Hearts III (inglés)

### Por GitHub (abierto de verdad)
- `ToshY/anime-news-network-encyclopedia`: listas de anime y manga
  (se buscó «Big Hero 6» y «Baymax»; sólo está el manga, n.º 16985) y la
  ficha del manga completa.
- `google/fonts`: `METADATA.pb` y archivo `.ttf` de 24 letras;
  tildes, ñ, ¿ y ¡ comprobadas con fontTools. **Kosugi Maru no las trae.**
- Búsqueda de repositorios «baymax big hero 6»: 23 resultados, casi todo
  asistentes de IA con su nombre. Nada útil de arte o letras.
  `joehsmash/baymax` (README abierto): una interfaz de voz, sin recursos.
- Búsqueda de código con la frase de la escala: sólo bots de fans.

### Lo que NO encontré
- Hojas de contacto, colores medidos y minutos exactos (sin red).
- Encuesta oficial de popularidad.
- Voces latinas de Fred, GoGo y Wasabi; voz de Baymax en ¡Baymax!.
- Frases latinas oídas en la película (salvo «Estoy satisfecho con mi
  cuidado», con dos fuentes de fans).
- Cajas de diálogo de los juegos y datos de TCRF.
- Entrevistas al compositor o a los animadores en japonés o coreano
  (sólo notas de prensa y wikis).
- Comentarios del Blu-ray.
- Hilos de Reddit (el buscador no deja).
