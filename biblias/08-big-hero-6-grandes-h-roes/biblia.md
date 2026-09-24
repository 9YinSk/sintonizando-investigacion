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

## 3 · Arte oficial reunido (dónde está, porque no se pudo bajar)

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

⚠️ **No vi qué sale en cada uno.** Antes de elegir, abrirlos en el PC.

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
Portada del tomo en la ficha: **640×982**
([imagen](https://cdn.animenewsnetwork.com/images/encyc/A16985-2330226621.1429842580.jpg)).

### Galerías de las wikis (no abren desde aquí; sí en el PC)
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
**Propuesta:** caras propias al estilo de Baymax y números 0-10. Así es
«de verdad» (una escala clínica) sin copiar la suya.

---

## 4 · Escenas icónicas (con su enlace)

Todas son de la película de 2014. **Minuto sin verificar** en todas:
no se pudo abrir YouTube.

| Escena | Qué pasa | Enlace |
|---|---|---|
| Baymax se enciende | Hiro dice «¡ay!» en su cuarto; Baymax se infla, saluda y pregunta el dolor | [clip](https://www.youtube.com/watch?v=cPwT1-2ZHgM) · [otro](https://www.youtube.com/watch?v=jlY-dEzTl0M) · [otro](https://www.youtube.com/watch?v=99RzToAF55Y) |
| Las figuras que caen | A Hiro le caen figuras una a una; Baymax repite la pregunta y **su pecho enseña la escala de caras cada vez** | [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Funny/BigHero6) |
| Batería baja | Baymax va «borracho»: coge al gato Mochi y le llama «bebé peludo» | [TV Tropes, memes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/BigHero6) |
| El choque de puños | Hiro le enseña el puño; Baymax hace «ba-la-la-la-la» con los dedos | [clip oficial HD](https://www.youtube.com/watch?v=yl8yriCIzCE) |
| La mejora de Baymax | Hiro le pone chips y armadura | [clip](https://www.youtube.com/watch?v=wILlTsjnYYw) · [placa del vientre](https://www.youtube.com/watch?v=BlPMfo1gaoo) |
| El primer vuelo | Hiro y Baymax vuelan sobre San Fransokyo | [clip](https://www.youtube.com/watch?v=HKwkOrFFEpg) |
| Los microbots | Hiro construye en su garaje (4K, a cámara lenta) | [clip](https://www.youtube.com/watch?v=3S3NadJwEQI) |
| El vídeo de Tadashi | «Aquí Tadashi Hamada y este es el octogésimo cuarto ensayo» | [audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397715) |
| El final | «Estoy satisfecho con mi cuidado» | [audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397730) · [YouTube](https://www.youtube.com/watch?v=F8zuGaDxwkk) |

Todos los clips de la película juntos: [YouTube](https://www.youtube.com/watch?v=EEYsgRgHGfI).
Serie 2D, Baymax vuelve: [YouTube](https://www.youtube.com/watch?v=yDnKLLac5Nk).

---

## 5 · 3D y fan art (sólo referencia o con su licencia)

### Modelos de Baymax en Sketchfab (licencia CC BY, según el buscador)
| Modelo | Autor | Fecha | Enlace |
|---|---|---|---|
| Baymax! | ᗰOᑎKEY ᗪ. ᒪᑌᖴᖴY (@KingOfThePirates) | mayo 2023 | [Sketchfab](https://sketchfab.com/3d-models/baymax-59007b633de1431290ff71afd8e66aaf) |
| Baymax (Big Hero 6) | theamazingdonovan207 | sept. 2024 | [Sketchfab](https://sketchfab.com/3d-models/baymax-big-hero-6-9a96e8526d5a4abaaa184830c20ab4ec) |
| Baymax | jasonballingham | marzo 2020 | [Sketchfab](https://sketchfab.com/3d-models/baymax-03bd50cd3998407aa8097bccb6f5c921) |
| Baymax! 3D Model | omer41_faruk (@kangal9990) | julio 2022 | [Sketchfab](https://sketchfab.com/3d-models/baymax-3d-model-09848c1567104556b7ce3440548a790d) |

Otros con descarga gratis, **licencia sin comprobar**:
[Eshtiaque Ahmad](https://sketchfab.com/3d-models/baymax-418c455a35d24bcdacf853ebf18ae2ee),
[Xasanov Amir](https://sketchfab.com/3d-models/baymax-40815e80d02f4fa5a45a39449b7cfa69),
[J1G4R](https://sketchfab.com/3d-models/baymax-bdd68308a896406daa709ac9e5faffa1),
[Koyo_Sikato](https://sketchfab.com/3d-models/baymax-29a502f7c45c4b5e82f74e6d0b5f0066).
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
Cómo es por dentro: ⚠️ de memoria (un taller luminoso con cristal).

### Luz por sitio
| Sitio | Luz | Estado |
|---|---|---|
| Hospital o consulta | fluorescente fría de techo | HDRI [hospital_room](https://polyhaven.com/a/hospital_room) |
| Garaje de Hiro, de noche | lámpara cálida, pantallas azules | ⚠️ de memoria |
| Lucky Cat Café | cálida de día, madera y rojo | ⚠️ de memoria |
| La ciudad | atardecer dorado con niebla; noche con neones | ⚠️ de memoria |

### Paleta (propuesta de partida, **sin medir**)
No se pudo bajar ninguna imagen para medir colores. Estos hex son a ojo:
**hay que medirlos en un fotograma** antes de usarlos.

| Qué | Hex aprox. |
|---|---|
| Vinilo de Baymax (luz) | `#F4F3EF` |
| Vinilo de Baymax (sombra, un poco azul) | `#C9CFD6` |
| Ojos y raya de Baymax | `#1B1B1B` |
| Armadura roja de Baymax | `#C4252B` |
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

**Cuál se parece a qué** es propuesta ⚠️: no pude poner el logo al lado.
Probar Russo One, Bungee y Exo 2 contra el logo en el PC.

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
  Kim (el buscador no aclara si Jin o Shiyoon ⚠️) propuso quitarla para
  que hable con **el cuerpo y el parpadeo**. El ilustrador japonés
  **Koyama Shigeto** propuso usar los **agujeros del cascabel** como ojos ✅
  ([ねとらぼ](https://nlab.itmedia.co.jp/nl/articles/1501/19/news144.html),
  [Red Bull JP, Koyama](https://www.redbull.com/jp-ja/behind-the-mask-15),
  [eiga.com](https://eiga.com/news/20141201/6/)).

**Así que el cuadro de diálogo de Baymax es su barriga:** el texto sale
**proyectado sobre el vinilo**, curvado con él, con un poco de brillo.
Nada de bocadillo de cómic
([guía de cuadros](../_ya_hechas/_Cuadros%20de%20dialogo%20por%20franquicia%20(23-sep-2026).md)).

### Tadashi habla por **sus vídeos de prueba**
Graba su trabajo con Baymax como un diario: «Aquí Tadashi Hamada y este
es el **octogésimo cuarto ensayo**» ⚠️ (frase de audiofrases, sin saber
el doblaje) ([audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397715)).
Hiro los ve después en la pantalla de Baymax ⚠️ (de memoria).
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
  ⚠️ sin abrir.
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
  Colores verde y rojo ⚠️ de memoria.
- **Carácter:** tranquilo, literal, amable. Sólo le importa tu salud:
  «Eres mi paciente… tu salud es mi única preocupación» ⚠️
  ([audiofrases](https://audiofrases.com/frases-de-peliculas-disney/audio-frases-de-big-hero-6-2014/eres-mi-paciente-baymax-tu-salud-es-mi-unica-preocupacion)).
  Nunca tiene prisa. Nunca se enfada (salvo con el chip de pelea).
- **Cómo se expresa:** voz plana y suave, frases completas y educadas.
  Saluda con «Hola». Explica con datos de su escáner. No se ríe. Con la
  batería baja, habla como borracho ✅
  ([TV Tropes, memes](https://tvtropes.org/pmwiki/pmwiki.php/Memes/BigHero6),
  [audiofrases, «Batería baja»](https://audiofrases.com/frases-de-peliculas-disney/audio-frases-de-big-hero-6-2014/bateria-baja)).
- **Cuerpo que habla:** inclina la cabeza, parpadea, mueve las manos
  despacio. **Abraza** como tratamiento: en China la frase fue
  «拥抱暖暖的大白», abrazar al cálido Baymax
  ([Sanlian](https://www.lifeweek.com.cn/article/149429)).
- **Con quién:** Hiro (su paciente y amigo), Tadashi (su creador), el
  gato Mochi, la tía Cass.

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
- **Cómo se expresa** ⚠️ de memoria: rápido, listo, algo impaciente y
  burlón; de pronto frágil cuando sale Tadashi. Sobre Baymax: «Parece un
  gigantesco malvavisco que camina, sin ofender» ⚠️
  ([audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397135)).

### Tadashi Hamada — el hermano mayor (el más llorado)
- Estudiante de robótica en el SFIT y **creador de Baymax**. Amable,
  animoso, trabajador, con humor tonto y alegre ✅
  ([wiki de BH6](https://bighero6.fandom.com/wiki/Tadashi_Hamada),
  [wiki de Disney](https://disney.fandom.com/wiki/Tadashi_Hamada)).
- **Su gorra:** negra, con letras rojas y doradas de **«San Fransokyo
  Ninja»**. Casi nunca se la quita. Se le cae antes del incendio y Hiro
  la guarda ✅ ([wiki de BH6](https://bighero6.fandom.com/wiki/Tadashi_Hamada),
  [Wikipedia](https://en.wikipedia.org/wiki/Tadashi_Hamada)).
- **Su frase:** «Alguien tiene que ayudar» ⚠️ (una fuente, ver punto 10).
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
- **Mochi:** el gato de la casa, bobtail japonés
  ([wiki de Disney](https://disney.fandom.com/wiki/Mochi)).

---

## 10 · Doblaje latino

### Película (2014)
| Personaje | Voz latina | Fuentes | Estado |
|---|---|---|---|
| **Baymax** | **Alan Prieto** | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Alan_Prieto), [SoundCloud «Alan Prieto (Baymax)»](https://soundcloud.com/laredso/alan-prieto-baymax), [TikTok SDV «voz oficial: Alan Prieto»](https://www.tiktok.com/@sdv_serviciosdevoz/video/7227258147939814662) | ✅ |
| **Hiro** | **Memo Aponte** | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Memo_Aponte), [PRODU, entrevista](https://www.produ.com/television/noticias/actor-guillermo-aponte-de-disney-mi-voz-como-hiro-en-grandes-heroes-de-disney-representa-un-trabajo-actoral-muy-fuerte/), [Radio Disney MX](https://www.facebook.com/RadioDisneyMx/photos/memo-aponte-es-la-voz-de-hiro-hamada-en-la-versi%C3%B3n-para-latino%C3%A1merica-de-grandes/819762721380622/?locale=es_LA) | ✅ |
| **Tadashi** | **Alexis Ortega** (1989-2026) | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Alexis_Ortega), [El Imparcial](https://www.elimparcial.com/espectaculos/2026/01/27/fallece-alexis-ortega-voz-de-spider-man-en-espanol-latino-y-tadashi-en-grandes-heroes/), [El Informador](https://www.informador.mx/entretenimiento/alexis-ortega-personajes-iconicos-a-los-que-dio-voz-ademas-de-spider-man-20260127-0116.html), [LatinUS](https://latinus.us/entretenimiento/2026/1/27/fallece-alexis-ortega-actor-de-doblaje-que-le-dio-voz-spider-man-tadashi-hamada-162929.html) | ✅ |
| **Honey Lemon** | **Génesis Rodríguez** (se dobla a sí misma) | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes), [The Dubbing Database](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes) | ✅ |
| Tía Cass | Patricia Palestino | [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes) | ⚠️ una fuente |
| Fred, GoGo, Wasabi | no lo encontré | — | — |

- **Estudio y dirección:** Taller Acústico, S.C., dirigido por **Ricardo
  Tejedo**. Luis Daniel Ramírez eligió el reparto y se fue; se mantuvo su
  reparto ⚠️ (sólo Doblaje Wiki, dos páginas)
  ([Grandes héroes](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes),
  [Memo Aponte](https://doblaje.fandom.com/es/wiki/Memo_Aponte)).
- Guion de doblaje subido por un usuario: [Scribd](https://www.scribd.com/document/526731325/DOBLAJE-GRANDES-HEROES) ⚠️ sin abrir.

### Serie 2D y ¡Baymax! (2022)
- **Grandes héroes: La serie** tiene doblaje latino
  ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes:_La_serie),
  [cortos](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes:_La_serie/Cortos)).
  Alexis Ortega (Tadashi) sigue en ella ✅ (Doblaje Wiki y las notas de
  su muerte). Memo Aponte (Hiro) también ⚠️ (sólo Doblaje Wiki).
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

### Frases (latino)
Los sitios de audios no dicen de qué doblaje son. Por eso casi todas van
⚠️ hasta oírlas en la película latina.

| Frase | Quién | Estado |
|---|---|---|
| «**Estoy satisfecho con mi cuidado.**» | Hiro, al final | ✅ [audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397730), [TikTok #grandesheroes](https://www.tiktok.com/@gabymg82/video/7414332757213498630), [YouTube](https://www.youtube.com/watch?v=F8zuGaDxwkk) |
| «¿Estás satisfecho con tu cuidado?» | Baymax | ⚠️ [TikTok](https://www.tiktok.com/@cold_constellations/video/7189793084861975813) |
| «No pueden desactivarme hasta que digas que estás satisfecho con mi cuidado.» | Baymax | ⚠️ [audiofrases](https://audiofrases.com/peliculas-disney/big-hero-6-2014/397146) |
| «Hola, yo soy Baymax, **tu** / **su** asistente médico personal.» | Baymax | ⚠️ circulan las dos: [«tu»](https://audiofrases.com/frases-de-peliculas-disney/audio-frases-de-big-hero-6-2014/hola-yo-soy-baymax-tu-asistente-medico-personal), [«su»](https://audiofrases.com/frases-de-peliculas-disney/audio-frases-de-big-hero-6-2014/hola-yo-soy-baymax-su-asistente-medico-personal) |
| «En una escala del uno al diez, ¿cómo calificarías tu dolor?» | Baymax | ⚠️ [blog de frases](https://frasesdecineparaelrecuerdo.blogspot.com/2015/01/frases-pelicula-big-hero-6.html), doblaje sin decir |
| «Puedes llorar si quieres. Llorar es una respuesta natural al dolor.» | Baymax | ⚠️ mismo blog |
| «Batería baja.» | Baymax | ⚠️ [audiofrases](https://audiofrases.com/frases-de-peliculas-disney/audio-frases-de-big-hero-6-2014/bateria-baja) |
| «Alguien tiene que ayudar.» | Tadashi | ⚠️ la película no la tradujo siempre igual; la serie sí ([guía de cuadros](../_ya_hechas/_Cuadros%20de%20dialogo%20por%20franquicia%20(23-sep-2026).md)) |
| «Bienvenidos a my house.» | Fred | ⚠️ una fuente (guía de cuadros) |

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
  Una pista se llama **«Huggable Detective»** ⚠️ (resumen del buscador;
  lista completa en [AllMusic](https://www.allmusic.com/album/big-hero-6-original-motion-picture-soundtrack--mw0002772854)
  y en la [wiki de Disney](https://disney.fandom.com/wiki/Big_Hero_6_(soundtrack))).
  Reseña de la partitura: [Entertainment Junkie](http://entjunkie.blogspot.com/2014/11/big-hero-6-score-review.html).
- **Qué ambiente da:** cálido y emotivo en lo de Baymax y los hermanos;
  pulso electrónico y épico en la acción ⚠️ (de las reseñas, sin oírla).
- **Serie 2D:** tema de **Adam Berry** ✅
  ([Wikipedia, Adam Berry](https://en.wikipedia.org/wiki/Adam_Berry),
  [tema en YouTube](https://www.youtube.com/watch?v=TeNwMzQEaYk)).
  Pistas nuevas de la serie: [Tumblr](https://multimonorail.tumblr.com/post/652529278925291520/new-big-hero-6-the-series-soundtrack-tracks).
- **Para #soporte:** el lado tranquilo de Jackman, no «Immortals». Una
  consulta, no una pelea.

---

## 12 · Vídeos

**Minuto sin verificar en todos** (YouTube y TikTok no abren desde aquí).

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
  **pantalla de Baymax**.

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
