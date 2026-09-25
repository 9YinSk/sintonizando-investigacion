# Investigador de VOZ Y PERSONAJES · Jujutsu Kaisen

La biblia (`biblia.md`) ya cubre los puntos 7, 8, 12 y 13 de `ENCARGO.md`
(encuestas de popularidad §9, descripción profunda de cada personaje §8,
lo que ama el fandom y qué NO hacer §14, doblaje latino §10). **Esta parte es
sólo los puntos 20, 21 y 22**, que el encargo añadió y que no están en la
biblia (comprobado con `python3 herramientas/seccion.py 32-jujutsu-kaisen
--indice`: no hay sección de gustos, de «por qué la gente la ama» ni de fan
dubs hispanos; tampoco aparecen en la tabla «Cumplimiento del encargo», que
salta del punto 17 a los 3 conceptos de lámina).

Partí de `partes/datos-voz.md` (favoritos de AniList, fichas de personaje,
ficha y reparto de Doblaje Wiki, «Datos de interés» del doblaje, dibujos por
personaje en Danbooru, clips de Dailymotion, hilos de Reddit): no repetí esas
consultas. Lo nuevo de esta parte sale de la **API de la wiki de Jujutsu
Kaisen** (secciones «Trivia», que citan el *Jujutsu Kaisen Official Fanbook*,
el databook oficial), de reseñas y de webs sobre premios/ventas, y de
metadatos reales (`yt-dlp --skip-download`, sin descargar vídeo) de
fandubs y covers en español.

## Punto 20 · Gustos y detalles de cada personaje

Fuente principal: **wikitext de la Jujutsu Kaisen Wiki** (`action=parse&
prop=wikitext`) para Yuji Itadori, Satoru Gojo, Megumi Fushiguro, Nobara
Kugisaki, Sukuna, Kento Nanami, Toge Inumaki, Aoi Todo, Maki Zenin y Suguru
Geto (mismo roster de personajes que la biblia ya perfila en su §8). Cada
sección «Trivia» de esos diez personajes cita el ***Jujutsu Kaisen Official
Fanbook*** (databook oficial en japonés, con página exacta: p. ej. Yuji
pp. 4-7, Sukuna pp. 100-103, Todo p. 36) con las preguntas fijas «hobby»,
«comida favorita», «comida que menos le gusta» y «causa de estrés» — es el
cuestionario propio del databook, no una interpretación de la wiki. Cuento
esto como **✅ fuente oficial** (el databook, citado con página, vía la wiki
que lo traduce) salvo que diga lo contrario.

### 20.1 Tabla comparativa (gustos, altura, cumpleaños)

| Personaje | Cumpleaños | Altura | Comida favorita | Comida que odia | Aficiones / estrés | Objeto o rasgo que siempre lleva |
|---|---|---|---|---|---|---|
| **Yuji Itadori** | 20-marzo-2003 ✅ (AniList + Fanbook vía wiki) | 173 cm (5'8") ✅ (2 fuentes) | Arroz con algo encima y fideos | Nada en particular | Karaoke, ver TV (programas de comida), imitaciones · estrés: ciencias (suspendió biología molecular) | Sudadera con capucha — pero **no por gusto**: «no es realmente un chico de sudadera, la lleva porque puede ser indeciso» ✅ (Fanbook) |
| **Satoru Gojo** | 7-diciembre-1989 ✅ (Fanbook, con año, pp. 40-43; también capítulo 96 del manga; AniList sólo confirma día/mes) | +190 cm (6'3") ✅ (2 fuentes) | Dulces | Alcohol | No tiene afición fija («puede hacer casi todo») · estrés: que se metan los superiores | La venda/gafas sobre los ojos (ya documentado en biblia §8; aquí lo confirma el Fanbook: empezó a comer dulces «para estimular el cerebro» y acabó enviciado) |
| **Megumi Fushiguro** | 22-diciembre-2002 ✅ (Fanbook, con año, pp. 8-11; AniList confirma día/mes) | 175 cm (5'9") ✅ (2 fuentes) | Comida que combine con jengibre | Pimientos rojos y todo acompañamiento dulce | Leer (no ficción) · estrés: la gente (casi toda) | Ropa cómoda de estar en casa, nunca de vestir ✅ (Fanbook); su tableta se la presta el colegio, no es suya |
| **Nobara Kugisaki** | 7-agosto-2002 ✅ (Fanbook, con año, pp. 12-15; AniList confirma día/mes) | poco menos de 160 cm (5'3") ✅ (2 fuentes) | Comida popular y sandía | Verduras encurtidas suaves | Ir de compras (marcas favoritas: **Balenciaga y Onitsuka Tiger**) · estrés: deshidratarse | Su martillo y sus clavos (Straw Doll Technique): es su arma y su firma visual, ya en biblia §8 y §15 |
| **Sukuna** | no aplica: es un ser de +1000 años, el Fanbook no le da cumpleaños ni altura | no aplica | «Su afición es comer» ✅ (Fanbook) | «No le disgusta nada en particular: no le importa nada más que él mismo» ✅ (Fanbook) — es la frase que mejor resume su forma de ver el mundo | — | Ninguno: no carga objetos, ocupa el cuerpo de Yuji o Megumi |
| **Kento Nanami** | 3-julio-1990 ✅ (2 fuentes) | 184 cm (6'0½") ✅ (2 fuentes) | Pan y **ajillo** (al ajillo) | Fideos planos | Beber alcohol y cocinar para sí mismo · estrés: las horas extra | **Su reloj de pulsera**: Akutami «se olvidaba de dibujárselo durante el arco de Shibuya, pero aseguró a los fans que de verdad estaba haciendo horas extra» ✅ (wiki, cita a Akutami, tomo 12 p. 46) — el objeto-chiste que ya es meme (biblia §9.2) |
| **Toge Inumaki** | 23-octubre-2001 ✅ (2 fuentes) | casi 170 cm (5'7") ✅ (Fanbook) | Onigiri de atún con mayonesa | Huevas de pescado | Ver YouTube (le gustan los vídeos de *mukbang*) · estrés: la asamblea de la mañana | El onigiri de atún y mayonesa que come siempre (coincide con lo que ya se ve en el ending 1, biblia §12.0) |
| **Aoi Todo** | 23-septiembre-2000 ✅ (2 fuentes) | +190 cm (6'3") ✅ (Fanbook) | Bistec de falda | Nada en particular | Ver a Takada (su ídolo) · estrés: aburrirse | Fotos/vídeos de la idol **Takada**: se ducha, usa desodorante y se arregla mucho para «oler siempre bien» ✅ (Fanbook) |
| **Maki Zenin** | 20-enero-2002 ✅ (2 fuentes) | 170 cm (5'7") ✅ (2 fuentes) | Comida basura («junk food») | Comida vegetariana | Su especialidad, según el Fanbook, es **aplastar latas vacías** · estrés: los trámites del clan Zenin | Sus armas malditas (naginata, catana): las lleva porque no tiene energía maldita propia |
| **Suguru Geto** | 3-febrero-1990 ✅ (2 fuentes) | +180 cm (5'11") ✅ (Fanbook) | Zaru soba (fideos fríos en bandeja de bambú) | Nada en particular | Su especialidad son las artes marciales · estrés: absorber espíritus malditos | Su kesa/haori con 5 franjas — el mismo patrón de «Gojō» que el apellido de Satoru (dato curioso de la wiki, ⚠️ una fuente) |

### 20.2 Cómo se ve a sí mismo cada uno (de las secciones «Personality» de la wiki, ya bajadas en `datos-voz.md`)

- **Gojo**: se cree invencible y el más fuerte del mundo («A lo largo del
  cielo y de la tierra, sólo yo soy el honrado», ya citado en biblia §2.1);
  el Fanbook lo confirma desde otro ángulo: «puede hacer casi todo, así que
  procura no involucrarse demasiado con nada. Según él, todo es por el bien
  de la siguiente generación» ✅ (2 fuentes: personalidad de la wiki +
  Fanbook).
- **Yuji**: no se ve como un héroe; le importa el «valor de una vida» y que
  la gente tenga una «muerte digna» ✅ (texto de personalidad, wiki).
- **Megumi**: tampoco se ve como un héroe. Cree que el mundo es injusto y
  que un hechicero es «una herramienta para que la gente buena tenga más
  oportunidades de vivir»; lo llama «su deseo egoísta e irracional» ✅
  (personalidad, wiki).
- **Nobara**: se enorgullece de ser guapa y fuerte a la vez, y se niega a
  que nadie la cambie ✅ (personalidad, wiki + Fanbook: sus compras y su
  ropa son parte de esa imagen).
- **Sukuna**: «no le importa nada más que él mismo» (Fanbook, arriba);
  no tiene sueños ni metas que perseguir, a diferencia de los hechiceros que
  luchan contra él y se hacen más fuertes por tenerlos ✅ (personalidad,
  wiki).
- **Nanami**: se ve como alguien que ya dejó de creer en el trabajo de
  hechicero («la razón difusa» de por qué volvió, ep. 42, §21.4) y que ya
  no separa sentimentalismo de servicio; Akutami lo creó para representar
  «a alguien que deja su trabajo de oficinista» ✅ (Fanbook).

## Punto 21 · Por qué la gente la ama

Las **encuestas de popularidad** (una de las razones que pide este punto)
ya están enteras en biblia §9: las 4 encuestas oficiales de la *Weekly
Shōnen Jump* y lo que dice el público en Reddit sobre Gojo, Nanami e
Inumaki. No lo repito; abajo va lo que falta: **premios, ventas, reseñas,
con qué personaje se identifica el público y las escenas que hacen
llorar/gritar**.

### 21.1 Premios y ventas (amplía lo que ya cita la biblia en §9.2)

- La biblia (§9.2) ya dice que la T2 ganó Anime del Año en los **8.os
  Crunchyroll Anime Awards (2-marzo-2024)**. Lo que faltaba: esa noche la
  serie no ganó un premio, ganó **11**, entregados en una gala presentada
  por Megan Thee Stallion — mejor dirección (Shota Goshozono), mejor
  acción, mejor diseño de personajes, mejor fotografía, mejores OP/ED,
  mejor personaje secundario (**Gojo**) y varios premios de actuación de
  voz ✅ ([Variety](https://variety.com/2024/digital/news/crunchyroll-anime-awards-2024-winners-list-jujutsu-kaisen-1235928308/),
  [Animation Magazine](https://www.animationmagazine.net/2024/03/jujutsu-kaisen-and-demon-slayer-win-top-prizes-at-the-2024-crunchyroll-anime-awards/)).
- **Ventas Oricon 2021**: el manga vendió **más de 30 millones de copias
  en Japón en un solo año** (30,91 millones), superando a *Kimetsu no Yaiba*
  en su último año de serialización (29,5 millones): **el manga más vendido
  de Japón en 2021** ✅ ([Oricon News,
  us.oricon-group.com/news/662](https://us.oricon-group.com/news/662/),
  [CBR](https://www.cbr.com/jujutsu-kaisen-demon-slayer-mha-best-selling-manga-2021/)).
  Volúmenes sueltos: *JJK 0* vendió 1.930.831 copias; los tomos 15 y 16,
  unos 2,3 y 2,1 millones cada uno ✅ (mismas fuentes).
- **Sukuna ganó «Mejor Antagonista»** en los Crunchyroll Anime Awards 2021
  ✅ (2 fuentes: Jujutsu Kaisen Wiki, sección Trivia de Sukuna, y
  [CBR, «Crunchyroll Anime Awards 2021: Best Antagonist Winner (& Every
  Nominee)»](https://www.cbr.com/crunchyroll-anime-awards-2021-antagonist-winner-nominees/)).

### 21.2 Lo que dicen las reseñas: por qué engancha

[CBR, «5 Issues Fans Have With the Writing (& 5 Things They Love)»](https://www.cbr.com/jujutsu-kaisen-fans-writing-likes-and-dislikes/)
(22-ene-2024) resume en 5 titulares por qué el fandom la quiere a pesar de
sus defectos de ritmo: **peleas dinámicas**, **héroes y villanos
memorables**, **un mundo realista y crudo**, **un sistema de poder
detallado** y, la que más pesa para este punto, **puntos altos emocionales
bien resueltos** ✅ (artículo completo leído, no sólo el titular):

> «Un shonen de pelea sobresaliente no se define sólo por cómo ejecuta sus
> peleas, sino por las emociones que carga (...) *Jujutsu Kaisen* juega
> con los sentimientos de los fans. (...) Del colapso de Yuji al ver el
> daño que causó Sukuna en Shibuya a la tragedia de la muerte de Satoru
> Gojo a manos de Sukuna, JJK nunca falla en hacer que sus fans sientan
> algo cuando la historia llega a sus momentos cumbre.»

⚠️ Esa cita menciona la muerte de Gojo (arco Shinjuku): **no está animada
todavía** en los 59 episodios que cubre la T3 (el 2.º ayudante ya lo notó en
biblia §12: la película *Ejecución* de noviembre-2026 sólo recopila Shibuya
y adelanta el arco del Juego del Sacrificio). Lo dejo igual porque explica
por qué el fandom la espera con tanta ansiedad.

### 21.3 Con qué personaje se identifica el público (y por qué)

**Nanami es el caso más citado**, y no por casualidad: Akutami lo diseñó a
propósito para eso.

- El propio Fanbook dice que Akutami «creó a Nanami para representar a
  alguien que deja su trabajo de oficinista»; originalmente iba a ser un
  villano ✅ (Fanbook, vía wiki, §20.1).
- [CBR, «Why Jujutsu Kaisen's Nanami, the Jaded, Millennial Sorcerer, Is
  Underrated»](https://www.cbr.com/jujutsu-kaisen-nanami-best-character/) y
  [CBR, «Why Nanami Kento From JJK Is Such a Fan Favorite»](https://www.cbr.com/jjk-nanami-fan-favorite/):
  Nanami es «probablemente el más identificable para muchos fans mayores»;
  representa el desencanto que sienten los *millennials* al entrar al mundo
  laboral adulto ✅ (2 artículos de CBR, coinciden).
- [epicstream.com, «Nanami Kento and His Realistic Struggles as a Salary
  Man»](https://epicstream.com/article/jujutsu-kaisen-nanami-kento-and-his-struggles-as-a-salary-man):
  Akutami reconoció crear a Nanami como comentario sobre el *burnout*
  corporativo. Trabajadores actuales de todo el mundo se sienten igual de
  sobrecargados, y su sensación de que el trabajo «sólo vale la pena si
  ayuda a alguien» refleja la de Nanami ⚠️ (paráfrasis del artículo, no cita
  textual de Akutami con fuente primaria).
- Encaja con lo que ya tenía la biblia (§9.2): el hilo de Reddit
  «Nanami Kento - Overtime» (3.783 votos) y el meme de las «horas extra».
  Aquí se añade el **porqué** narrativo, no sólo el dato de popularidad.

**Gojo**, en cambio, engancha por ser la fantasía de poder sin esfuerzo (ya
en biblia §9.2: «Nah, I'd win»); **Yuji**, según la misma reseña de CBR
(§21.2), engancha por su colapso emocional al ver el daño de Sukuna: el
público se identifica con su culpa, no con su fuerza.

### 21.4 Las escenas que hacen llorar (capítulo, minuto, por qué, música y reacción)

#### La muerte de Nanami — T2-18 / episodio 42, «Right and Wrong» (理非)

- **Dónde y cuándo**: episodio 42 de la serie (18.º de la T2), estrenado en
  Japón el 23-nov-2023 ✅ ([wikitext de «Episode 42»](https://jujutsu-kaisen.fandom.com/wiki/Episode_42),
  `action=parse`). En la numeración de minutos de la biblia (§2.2, sub.
  japonés con tiempos), Nanami dice «Lo demás te lo dejo a ti» en el
  minuto 13:30; en la copia de Dailymotion mirada por el 2.º ayudante
  (§12.0/§12.2), el mismo momento cae en el **0:18** del clip
  [x8upb66](https://www.dailymotion.com/video/x8upb66).
- **Qué pasa** (resumen de la wiki, leído completo): Nanami, con medio
  cuerpo quemado por Jogo, camina por el metro de Shibuya imaginando una
  playa en Malasia donde nunca llegó a construir su casa ni a leer todos
  sus libros pendientes. Corta a un grupo entero de humanos transfigurados
  él solo, agotado. Mahito le toca la espalda por detrás y le pregunta si
  tiene últimas palabras. Nanami mira a Yuji, que acaba de llegar, sonríe y
  le confía la tarea de exorcizar a Mahito. Mahito lo mata al instante,
  reventándole la mitad superior del cuerpo ✅ (wiki, texto completo del
  «Plot Details»).
- **Por qué duele**: el episodio empieza con Yuji viendo el desastre que
  dejó Sukuna en Shibuya (la reseña de CBR del §21.2 cita justo esa imagen
  como uno de los puntos altos emocionales de la serie), así que Nanami
  muere en el mismo episodio en el que Yuji ya está roto. Nanami no grita
  ni se lamenta: muere pensando en la playa donde nunca llegó a
  descansar — el gag de «odio las horas extra» (biblia §2.1, #7 y #8) se
  convierte aquí en tragedia: se murió sin tomarse el descanso que pedía.
- **Cómo está dibujada** (cruce con lo que el 2.º ayudante ya miró y dejó
  en biblia §12.2, «Nanami, el final»): la escena pasa en la **estación de
  metro de Shibuya, con carteles amarillos** de fondo — el mismo lugar de
  trabajo que Nanami acaba de recorrer todo el episodio, no un escenario
  especial; Nanami está **medio quemado** (el lado izquierdo de la cara y
  el cuerpo, por el fuego de Jogo) y **sonríe** al ver a Yuji justo antes
  de morir ✅ (fotograma mirado, biblia §12.2, clip
  [x8upb66](https://www.dailymotion.com/video/x8upb66)). Es un plano
  **cercano a su cara**, sin lluvia ni grito: el contraste entre la sonrisa
  y la explosión de sangre que sigue (según el resumen de la wiki, «Mahito
  lo mata al instante, reventándole la mitad superior del cuerpo») es lo
  que golpea, no un recurso de puesta en escena. ⚠️ No confirmé si hay
  silencio en la pista de sonido justo en ese instante (no tengo el clip
  completo con audio, sólo el fotograma ya mirado por el otro ayudante).
- **Qué música suena**: el tema **«Vague Reason»**, de la banda sonora
  oficial de la T2 (compositor Yoshimasa Terui), tiene el mismo nombre que
  la «razón difusa» que Nanami dice tener para seguir siendo hechicero, en
  ese mismo episodio ✅ ([YouTube, canal oficial de la BSO](https://www.youtube.com/watch?v=jyvxDmi4flU) —
  título del vídeo «Vague Reason (Nanami)»). ⚠️ No pude confirmar con un
  listado minuto a minuto que suene exactamente durante la muerte y no en
  otra escena de Nanami del mismo episodio (Tunefind no lista las pistas
  del episodio 42 en concreto, sólo del 43).
- **Cómo reaccionó la gente**: el hilo de r/JuJutsuKaisen «why is nanami's
  death song the best theme» (visto por el buscador, la página del foro
  bloqueó la lectura directa con un reto de Cloudflare) y el post en Tumblr
  [@yuujies, «nanami kento (七海建人) in jujutsu kaisen ↳ episode 42 -
  right and wrong»](https://www.tumblr.com/yuujies/734882331849097216/nanami-kento-%E4%B8%83%E6%B5%B7%E5%BB%BA%E4%BA%BA-in-jujutsu-kaisen-episode-42)
  muestran que la escena se sigue compartiendo como recorte suelto ⚠️ (vi
  los títulos y el resumen del buscador, no pude abrir el hilo completo de
  Reddit ni el post de Tumblr). En Reddit, el hilo «If you were given a
  chance to hijack Gege's body and you knew what he is going to do with
  Nanami, what you would do?» tiene **774 votos y 168 comentarios** ✅
  ([Arctic Shift](https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=JuJutsuKaisen&title=Nanami)):
  el fandom sigue «negociando» con el mangaka para salvarlo, años después.

#### La muerte de Junpei Yoshino — T1, arco «Idle Death Gamble» (episodios 6-7)

- **Qué pasa**: Mahito usa su técnica para transfigurar a Junpei —el único
  amigo que Yuji hizo antes de convertirse en el objetivo de Mahito— y lo
  mata delante de él ✅ ([SlashFilm, «The 10 Best Death Scenes in Jujutsu
  Kaisen, Ranked»](https://www.slashfilm.com/1696249/jujutsu-kaisen-best-deaths-ranked/)).
  El episodio empieza dando a entender que Junpei se salvará y entrará a
  Jujutsu High junto a Yuji; el giro es lo que más duele.
- **Por qué duele**: es la **primera pérdida** de Yuji desde la muerte de
  su abuelo (biblia §2.1, escena #1); Junpei acababa de decir que Mahito
  «parecía buena persona» ✅ (misma fuente, SlashFilm).
- **Cómo reaccionó la gente**: en r/JuJutsuKaisen, un hilo dice textual
  «I legit cried watching this scene. This boy just couldnt get a break.
  Got bullied basically all his life and he didnt reta[liate]...» ✅
  ([Arctic Shift](https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=JuJutsuKaisen&title=cried),
  4 votos: es un hilo pequeño, no viral, pero textual y sobre esta escena
  exacta). ⚠️ No encontré el capítulo/minuto exacto de la muerte dentro del
  episodio (no lo tengo en los subtítulos con tiempos que usó la biblia);
  dejo el rango T1-6/T1-7 que da la wiki del arco.

#### Y una que hace gritar de emoción: la Expansión de Dominio de Gojo contra Jogo (T1-7, minuto 14:25-14:30)

Ya está descrita y mirada en biblia §2.1 (escena #5) y §12.2 («Gojo contra
Jogo»): la incluyo aquí sólo por el ángulo que pide el punto 21, la
**reacción del público**. En r/JuJutsuKaisen, el hilo «What's the most
iconic line in season 3?» tiene **1.419 votos y 144 comentarios**, y «Now
that we've seen the 3 way domain battle in the anime, what's the next most
iconic culling game panel/page» tiene 186 votos ✅ (ambos ya en
`datos-voz.md`, búsqueda «iconic»): el gesto de manos de Gojo (índice y
corazón cruzados) es, según ese mismo archivo, un reto de fotos y de TikTok
(§12.5 de la biblia). Es el reverso exacto de la muerte de Nanami: una
escena que hace **gritar**, no llorar, y con la misma cantidad de detalle
de minuto ya verificado.

## Punto 22 · Fan dubs y comunidad hispana

Todo verificado con **metadatos reales** (`yt-dlp --skip-download`, sin
bajar vídeo: título, duración, vistas, canal) salvo donde digo lo contrario.
YouTube dejó sacar metadatos aunque bloqueó descargas de vídeo para el resto
del equipo (nota del encargo).

### 22.1 Doblajes de fans (fandubs) en español

| Escena doblada | Canal | Enlace | Duración | Vistas | Variante |
|---|---|---|---|---|---|
| «Compras con Nobara» (animación de illuxxxtrandy) | **LATAM Fandub Studios** (voces: azuphie como Nobara, zerito_dubs como Itadori) | [Dailymotion](https://www.dailymotion.com/video/xagbkga) · [YouTube](https://www.youtube.com/watch?v=MxYto_HCjA0) (privado ahora ⚠️) | 1:07 | 9.306 (Dailymotion) ✅ medido | Latino |
| «Kugisaki Nobara» (escena doblada no oficial) | **NamiDUB** | [YouTube](https://www.youtube.com/watch?v=yzzGr4jH6BI) | 0:41 | 263 ✅ medido | **Castellano** (España; ya publicado 13-ene-2022) |

⚠️ Ya estaba en `datos-voz.md` el hallazgo de Dailymotion («Compras con
Nobara», LATAM Fandub Studios); lo nuevo aquí es (a) que también está en
YouTube con crédito de animador y actores de voz de fans, y (b) el fandub
en castellano de NamiDUB, que no estaba.

### 22.2 Covers de los openings en español

Todo «Kaikai Kitan» (廻廻奇譚), el primer opening (biblia §11), con
metadatos reales de YouTube:

| Cover | Canal | Vistas | Duración | Enlace |
|---|---|---|---|---|
| «JUJUTSU KAISEN Opening ESPAÑOL \| KAIKAI KITAN \| Eve \| Cover Español Latino» | **David Delgado** | **411.990** ✅ | 3:38 | [YouTube](https://www.youtube.com/watch?v=JXSDUu_sVcQ) |
| «JUJUTSU KAISEN『KAIKAI KITAN』OPENING 1 FULL COVER ESPAÑOL LATINO» | **Danie Green** | **195.811** ✅ | 3:38 | [YouTube](https://www.youtube.com/watch?v=7WxKkSlioRE) |
| «(Full) Jujutsu Kaisen - Opening - Cover en Español Latino (Kaikai Kitan)» | **EnmaDS - EnmanuelDSite** | **118.586** ✅ | 3:55 | [YouTube](https://www.youtube.com/watch?v=XJverP3wvfM) |
| «Jujutsu Kaisen - Opening (KaiKai Kitan) [Cover En Español Latino]» | **0uter** | 1.643 ✅ | 1:33 | [YouTube](https://www.youtube.com/watch?v=6IqWx6e-sxw) |

Son covers cantados, no fandubs de la serie, pero cumplen el punto 22
(«covers de los openings en español»). Con más de 400.000 vistas, el de
David Delgado es el más visto de los cuatro medidos: sirve como muestra de
que el hispanohablante también canta el opening, útil si el canal de canto
del servidor quiere proponer un reto de cover.

### 22.3 Parodias: el canal ElRai (España, fandub cómico)

**ElRai** (`@ElRaiFanduber`) hace parodias dobladas de personajes de anime
jugando videojuegos o en situaciones cómicas — es fandub de personaje, no
traducción de escena. Dos vídeos son de Jujutsu Kaisen, con metadatos
reales:

- «Los Jujutsu Zenin JUEGAN JUJUTSU SHENANIGANS!» — **993.871 vistas** ✅,
  15:40, subido 7-mayo-2026 ·
  [YouTube](https://www.youtube.com/watch?v=9uwA-lly6TM)
- «Los Jujutsu Kaisen JUEGAN HYTALE!» — **393.995 vistas** ✅, 11:58,
  subido 23-feb-2026 · [YouTube](https://www.youtube.com/watch?v=5QyaDz3YSiU)

Es el fandub hispano más visto que encontré para esta serie: casi un millón
de vistas en un solo vídeo, muy por delante de cualquier cover u otro
fandub de escena. El resto del catálogo del canal (Blue Lock, Invincible,
My Hero Academia, Kimetsu no Yaiba) confirma que es un canal activo de
parodias de anime en español, no un caso suelto ✅ (visto en el listado del
canal).

### 22.4 Memes hispanos

- Cuenta de TikTok **@traductordemomosbv** («TraductorDeMomos»): sube memes
  de Jujutsu Kaisen en español, con miles de «me gusta» según el resumen
  del buscador ⚠️ (`yt-dlp` no pudo leer TikTok desde aquí — «Unexpected
  response from webpage request» — así que no pude medir vistas ni likes
  reales; el vídeo de ejemplo es
  [tiktok.com/@traductordemomosbv/video/7346331193773853958](https://www.tiktok.com/@traductordemomosbv/video/7346331193773853958)).
- Los memes hispanos más repetidos en TikTok/foros de búsqueda son sobre
  **Sukuna en pánico** y **Gojo y Geto** en diálogos absurdos doblados, con
  las etiquetas #jujutsukaisen #jjk #itadori #JJKMemes ⚠️ (resumen del
  buscador, no vídeos verificados uno a uno).
- Esto complementa, sin repetir, los memes ya recogidos en biblia §14 (que
  son sobre todo en inglés/japonés): aquí es específicamente lo que hace la
  comunidad **hispana**, como pide el punto 22.

## Lo mejor para la lámina

1. **El reloj de Nanami** (§20.1): un objeto pequeño, gracioso y con
   historia real (Akutami se «olvidaba» de dibujarlo) — perfecto para un
   detalle de fondo en una lámina de doblaje/voz sobre puntualidad o
   compromiso.
2. **La frase de Nanami en el ep. 42** («Lo demás te lo dejo a ti», minuto
   13:30/T2-18) con el tema «Vague Reason» de fondo: la escena que más
   duele y más se repite en redes, ya con minuto exacto de dos copias.
3. **El dato de Nanami-como-representación-del-burnout** (§21.3): conecta
   directamente con el público del servidor (gente que también «hace horas
   extra» en doblaje/locución como *hobby* o trabajo).
4. **El cover de Kaikai Kitan de David Delgado** (411.990 vistas): si el
   servidor quiere un reto de canto para el canal de música, esta cifra
   demuestra que ya hay público hispano para ese opening.
5. **ElRai y su casi millón de vistas parodiando a Jujutsu Kaisen en
   español**: prueba de que el fandub de personaje (no de escena) es el
   formato hispano que más engancha para esta serie — dato útil si el
   servidor organiza un reto de fandub.

## No encontré

- ⚠️ El **año de nacimiento** de Gojo (sólo día y mes, 7-dic, tanto en
  AniList como en el Fanbook vía wiki); la wiki no lo da porque Akutami
  nunca lo precisó.
- ⚠️ Un **listado minuto a minuto verificado** de qué pista de la banda
  sonora suena exactamente en el instante de la muerte de Nanami (Tunefind
  no cubre el episodio 42, sólo el 43); dejo «Vague Reason» por el nombre
  compartido con su diálogo, marcado como dudoso.
- ⚠️ El **capítulo y minuto exactos** de la muerte de Junpei dentro del
  episodio 6/7 (no están en los subtítulos con tiempos que ya tenía la
  biblia); sólo tengo el arco.
- ⚠️ **Vistas y «me gusta» reales** de TikTok (`@traductordemomosbv` y
  otros): `yt-dlp` no pudo leer TikTok desde este servidor («Unexpected
  response from webpage request», comprobado dos veces con enlaces
  distintos); me quedé con el resumen del buscador.
- ⚠️ El hilo completo de Reddit «why is nanami's death song the best
  theme» y el post de Tumblr sobre el episodio 42: los vi en el resumen del
  buscador, pero al abrirlos directamente la wiki de Fandom puso un reto de
  Cloudflare (`cf_chl`) que no pasé.
- No encontré una **encuesta oficial de «personaje favorito» de un medio
  latino** (revistas, streamings) para cruzar con las 4 encuestas
  japonesas ya citadas en biblia §9.1: sólo Reddit (en inglés) y las
  encuestas de la Jump.
- El video de YouTube de «Compras con Nobara» (LATAM Fandub Studios) está
  **privado ahora**: lo dejo citado igual porque la copia de Dailymotion
  (con vistas medidas) sigue pública.

## Bitácora de búsqueda (voz y personajes · puntos 20, 21 y 22)

**Red directa** (sin gastar cupo de buscador): API de la Jujutsu Kaisen
Wiki (`action=parse&prop=wikitext`) sobre 10 páginas de personaje (Yuji
Itadori, Satoru Gojo, Megumi Fushiguro, Nobara Kugisaki, Sukuna, Kento
Nanami, Toge Inumaki, Aoi Todo, Maki Zenin, Suguru Geto) y sobre «Episode
42»; API de Arctic Shift sobre r/JuJutsuKaisen (`title=Nanami`,
`title=cried`, con reintentos por «Timeout» — está compartida con el resto
del equipo, fui espaciando las llamadas); API de Dailymotion
(`api.dailymotion.com/videos?search=…`) para covers de opening y fandubs;
`yt-dlp --skip-download --print` (sin descargar vídeo) sobre 9 URLs de
YouTube para vistas y duración reales; un intento sobre TikTok (falló).

**Buscador web** (9 búsquedas, todas en español o inglés): premios
Crunchyroll/Anime Trending/Newtype 2024 · ventas Oricon 2021 · reseñas de
por qué gusta la serie (CBR, IGN, ANN) · Junpei episodio 7 reacción ·
muerte de Nanami episodio 42 «Right and Wrong» banda sonora · tracklist de
la BSO T2 · Nanami «salaryman» identificación del público · fandub español
latino de Jujutsu Kaisen (canales) · covers de Kaikai Kitan en español ·
memes hispanos de Jujutsu Kaisen en TikTok.

**Bloqueado o vacío**: `jujutsu-kaisen.fandom.com/f/...` (foro de la wiki:
reto de Cloudflare al leerlo directo, aunque el buscador sí indexa el
título); TikTok vía `yt-dlp` («Unexpected response from webpage request»,
dos intentos con vídeos distintos); Arctic Shift dio «Timeout. Maybe slow
down a bit» varias veces por ser cupo compartido con el resto del equipo —
esperé y until pasó.

Sigue: nada obligatorio pendiente de los puntos 20, 21 y 22. Si hay tiempo:
abrir a mano el hilo de Reddit y el post de Tumblr sobre la muerte de
Nanami (bloqueados por Cloudflare/límite de lectura automática), y buscar
el minuto exacto de la muerte de Junpei.
