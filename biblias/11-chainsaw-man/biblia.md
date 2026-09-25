---
tags: [biblia, serie, laminas]
serie: "Chainsaw Man"
canal: "#que-estas-viendo"
fecha: 2026-09-24
---

# Biblia · Chainsaw Man — para #que-estas-viendo

> [!important] Cómo se hizo, y sus límites
> - **Segunda pasada (25-sep-2026), con la red abierta.** La hizo un
>   equipo: 4 investigadores (imagen, vídeo, voz, texto) y un redactor.
>   Se pudo usar: la API de la wiki de Fandom (tamaños reales, wikitext),
>   Doblaje Wiki por su API, AniList, la API de Sketchfab (licencias),
>   Internet Archive y Dailymotion para **mirar de verdad** la película y
>   los episodios con `fotogramas.py` (YouTube seguía pidiendo iniciar
>   sesión), `estilo.py` para **medir colores** en fotogramas y en arte
>   oficial, CGWORLD y Crank-in! en japonés, y las 3 hojas de contacto de
>   `hojas/`. Lo que cambió está en «Segunda pasada · qué cambió», justo
>   debajo. Lo que sigue es la primera pasada (24-sep), corregida en su
>   sitio donde las partes nuevas decían otra cosa.
> - Primera pasada: la red de esta sesión estaba cerrada: `community.fandom.com` daba
>   **000/403**, y también Doblaje Wiki, YouTube, Somos Kudasai y casi todo
>   lo demás por WebFetch. Por eso **no se pudo correr**
>   `herramientas/investigar_serie.py`: **no hay hojas de contacto** ni
>   carpeta `hojas/`.
> - Hice búsquedas web en español, inglés, japonés, coreano y chino (la
>   lista está al final, en la bitácora).
> - GitHub sí respondía, y de ahí salió lo más útil de todo el trabajo:
>   - los **subtítulos de Netflix de la temporada 1**, en inglés y en
>     japonés, de los 12 episodios, con sus tiempos
>     ([foxofice/sub_share](https://github.com/foxofice/sub_share));
>   - los **subtítulos japoneses de la película *Arco de Reze***
>     (versión de Amazon Japón, con acotaciones de sonido)
>     ([Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror)).
>   Con ellos doy el **minuto de cada escena**. Es el minuto de ese archivo:
>   puede moverse uno o dos minutos según la plataforma.
> - Las letras propuestas las comprobé en
>   [google/fonts](https://github.com/google/fonts) (subset `latin` →
>   á é í ó ú ñ ¿ ¡).
> - ✅ **confirmado**: dos fuentes. ⚠️ **dudoso**: una sola fuente, o lo
>   describo de memoria. Lo de memoria siempre va marcado.
> - Lo que cito **de los subtítulos** (frase y minuto) lo marco ✅: es el
>   texto mismo de la obra, y lo crucé con el resumen de alguna fuente
>   cuando la había.

> [!warning] Una corrección al plan
> El plan dice «butacas de cine y entradas (**la cita del ep. 8**)». La cita
> en el cine **no está en el episodio 8** ni en la temporada 1 del anime:
> - Es una cita de **Denji con Makima**, no con Reze ✅ (wikitext del
>   capítulo 39 y la película vista fotograma a fotograma). Reze aparece
>   después, en la cabina de teléfono.
> - En el **manga** es el **capítulo 39**, «Tearjerker» (きっと泣く), primer
>   capítulo del arco de la Chica Bomba ✅ (tomo 5 ⚠️, de memoria)
>   ([Chainsaw Man Wiki: Chapter 39](https://chainsaw-man.fandom.com/wiki/Chapter_39),
>   [Sequential Planet](https://sequentialplanet.com/manga-review-chainsaw-man-chapter-39/),
>   [Top Level Canon](https://www.toplevelcanon.com/reviews/chainsaw-man-39-43-part-one)).
> - En pantalla es **el arranque de la película *Chainsaw Man – La
>   Película: Arco de Reze*** (2025), del **minuto 6:25 al 11:00** ✅
>   (subtítulo japonés de la película, ver §2).
> - El episodio 8 de la serie se llama «Gunfire» / «銃声» (disparos): es el
>   ataque en la calle, nada de cine ✅ (título en los subtítulos de
>   Netflix de kitsunekko-mirror).
> - Lo único de cine en la temporada 1: en el **ep. 7, 6:22-6:37**, Himeno
>   le propone a Aki dejar la caza y «ir al cine de vez en cuando después
>   del trabajo» ✅ (subtítulos de Netflix, inglés y japonés:
>   «帰りは たまに映画行って»).
>
> El objeto (butacas y entradas) **sirve y es el mejor posible** para este
> canal. Sólo cambia de dónde sale: de la película, no del ep. 8.

---

## Segunda pasada · qué cambió

Hecha el **25-sep-2026** con la red abierta, por 4 investigadores
(imagen, vídeo, voz y personajes, texto y técnica) y un redactor. Sus
libretas están en `partes/` (`imagen.md`, `video.md`, `voz.md`,
`texto.md`), con su bitácora.

**Corregido (antes → ahora)**
- **Butacas del cine**: rojo vino `#6E1F24` (propuesto) → **mostaza o
  ámbar** `#544A36` / `#7C6D4A`, medido con `estilo.py` en el fotograma
  de la sala llena (7:44 del corte EN) (§5.3).
- **Haz del proyector**: azul frío `#CFE3F2` (propuesto) → **blanco
  cálido con halo verde-violeta**, visto en el mismo fotograma (§5.3).
- **Pelo de Makima**: rosa salmón para todo → **granate** `#4C201F` en la
  película (6:52 del corte EN); el salmón `#D3978F` es sólo de la serie
  (§16).
- **Uniforme**: «camisa blanca, traje negro» → camisa **crema**
  `#EDEDE3`-`#F0EFE7` y traje **gris pizarra** `#2F393A`-`#30393B`,
  medidos en los 5 diseños oficiales del arco de Reze (§16).
- **Denji celebrando**: brazos arriba (de memoria) → **dos puños tímidos a
  la altura del pecho, ojos cerrados** (7:04 del corte EN) (§15).
- **Opening**: un resultado de búsqueda decía que «KICK BACK» entra a los
  34 s → entra en el **2:02** del ep. 1, tras un prólogo sin música (§11).
- **2.ª encuesta**: Aki 88.568 → **88.868** votos (§9).
- **Voces latinas**: Kobeni ⚠️ → ✅ **Paola García**; Himeno, Kishibe y
  Beam «no encontrado» → **Mireya Mendoza, Víctor Franco e Iván
  Bastidas** ✅ (Doblaje Wiki y AniList). Estudio de la película ⚠️ →
  **Audiomaster Candiani** ✅ (§10).
- **Licencias de Sketchfab**: sin comprobar → **30 modelos confirmados**
  por su API; ojo con Last_Hawk (no comercial) y GinesMartinez (compartir
  igual) (§4).
- **La ropa de la cita**: «no se sabe» → Makima va **de calle**: cárdigan
  claro, falda oscura, medias oscuras, zapatos planos y bolso pequeño
  (viñeta del cap. 39) (§16).
- **Bitácora**: «no existe un cuadro de diálogo propio» → «**no lo
  encontré**» (regla de AYUDANTE.md) (§21).

**Añadido**
- **Vídeos mirados de verdad** (YouTube seguía pidiendo sesión): la
  película entera en Internet Archive (corte EN; los fotogramas citados,
  sacados en **1080p reales** del .mkv), los ep. 1, 2 y 7, y el tráiler
  (Dailymotion) (§2, §11, §15).
- **El cine se llama シネマ座** («Cinema-za»): letras plateadas sobre un
  panel verde azulado, 9:12 del corte EN (§2, §5).
- La **película de dentro** (verde azulado, 9:50), la **flor de la caja
  de donativos** (11:52-12:40) y el **área de descanso** del ep. 2 (§2,
  §5).
- El **ending del ep. 1 no tiene animación**: créditos blancos sobre
  negro (24:00-24:16), como en un cine (§11).
- **Texturas de ambientCG miradas**: Fabric022 y Fabric026 para la
  butaca (recoloreadas), Paper005 y Paper006 para la entrada (§5.4).
- **El premio de Emilio Treviño** (Crunchyroll Anime Awards 2024, voz en
  español latino por Denji), frases del doblaje con episodio, el
  adaptador (Jaime Chaparro) y las fechas de grabación (§10).
- **Crank-in!**: Kusunoki y Toya hablan de grabar la escena del cine
  (§8, §18D).
- Las 3 encuestas oficiales con su **top 10 y sus votos** (§9).
- **Tamaños reales** (API de la wiki) de tomos, revistas y diseños;
  Alpha Coders ya abre (§3, §17).
- El juego **Chainsaw Man Mobile**, anunciado el 19-jun-2026 (§13).
- **Los puntos 18-25**, nuevos: §18A a §18H.
- La tabla **«Cumplimiento del encargo»** y `referencias.json` rehecho:
  de 35 enlaces sin tamaño a **266** referencias (**142** con ancho y alto
  medidos), las mejores primero.

**Los ⚠️**
- **Antes**: el número de la primera pasada **no quedó apuntado** (el
  redactor anterior se cortó por el límite de uso antes de contarlo).
- **Resueltos**, entre otros: las 4 voces latinas, el estudio de la
  película, las licencias de Sketchfab, los hex «propuestos» del cine y
  del vestuario, la ropa de Makima en la cita, las posturas que ya se
  vieron en fotograma, los tamaños de imágenes y fondos.
- **Quedan**: **147** ⚠️ en todo el texto (contados con `grep` al cerrar;
  incluye los de la tabla y los de las secciones nuevas 18A-18H). Los
  principales: la frase latina de Makima en el cine (no la oí), minutos y
  vistas de YouTube y TikTok (piden sesión), caras por emoción y poses de
  §15 sin fotograma, qué cine real inspiró シネマ座, el programa de dibujo
  de Fujimoto (una fuente) y la fecha exacta del final del manga.

**Conceptos de lámina**: los tres se quedan; se afinan con lo medido
(butacas mostaza, haz cálido, pelo granate, el rótulo シネマ座 y los
colores de Reze) (§19).

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección LA SALA):

> **ıı・📺・que-estas-viendo** (texto) · 0 fijados · 0 de personas en los
> últimos 15 — _Series, pelis, anime: lo que estás viendo y si lo
> recomiendas. Con spoilers, marca el texto como spoiler._

Es un canal de texto (no foro): **no tiene etiquetas ni ficha**. Hay que
decir tres cosas y nada más:

1. **Qué se hace aquí**: contar qué series, pelis o anime estás viendo.
2. **Qué se espera**: decir si lo recomiendas.
3. **La regla**: si hay spoilers, se marcan como spoiler.

### Los textos de la lámina (propuesta, en la voz de la serie)

Cortos, una idea cada uno, sin «·», «—» ni paréntesis (regla 4 del dueño):

| Hueco | Texto |
|---|---|
| Título | **¿Qué estás viendo?** |
| Línea 1 | Series, pelis, anime. Cuenta qué estás viendo. |
| Línea 2 | Dinos si lo recomiendas. |
| Regla | ¿Spoilers? Márcalos como spoiler. |
| Guiño (opcional, de Makima) | «Una de cada diez vale la entrada.» (junta dos frases suyas, 9:09 y 10:37; traducción mía ⚠️) |

Cómo marcar spoiler en Discord (para quien no lo sepa): el texto entre
`||dos barras||`. Cabe como línea pequeña en la entrada o en la butaca.
**No hace falta lámina 2**: el canal no tiene etiquetas ni rangos.

---

## 1 · Resumen para quien tenga prisa

- **La escena del canal existe y es perfecta**: Makima lleva a Denji a ver
  películas **de sala en sala, hasta las 12 de la noche**. Entre película y
  película **opinan** («no tuvo gracia», «la música estaba bien», «muy
  normalita»). Makima le dice: «Yo también encuentro **una buena de cada
  diez**. Pero **esa una me cambió la vida**». Al final los dos lloran y
  ella dice: «**Sólo por eso valió la entrada de hoy**». Es literalmente
  «lo que estás viendo y si lo recomiendas» ✅ (§2).
- **El opening de la serie («KICK BACK») es una lista de películas**:
  *Reservoir Dogs*, *Pulp Fiction*, *La masacre de Texas*, *No Country for
  Old Men*, *El gran Lebowski*… ✅ (§11). Sirve de cartelera.
- **El autor ama el cine**: a quien quiere ser mangaka le aconseja
  «**suscríbete a Netflix**» ⚠️ (una fuente, §11).
- **El más querido hoy es Reze**: ganó la 3.ª encuesta oficial (2025) con
  **205.775 votos**, el doble que Makima (101.454) ✅. **Power** ganó la
  1.ª (2020) y la de VIZ en inglés (2022); **Aki** ganó la 2.ª (2021) ✅
  (§9).
- **Doblaje latino** (Crunchyroll, Audiomaster Candiani, dirige **Tavo
  Campos**): Denji **Emilio Treviño**, Makima **Gaby Gris**, Power **Erika
  Langarica**, Aki **Arturo Cataño** ✅; Reze (película) **Jessica
  Ángeles** ✅ (§10).
- **Cuadro de diálogo propio**: la serie no tiene globo propio; el suyo es
  **el subtítulo de cine**: letra blanca con borde negro sobre la pantalla
  de la sala, o las **franjas negras de cine** arriba y abajo (§7).
- **Tono**: sucio, urbano, 1997, luz de tarde, colores apagados. **Nada
  mono ni limpio.** Y **nada de spoilers** en la lámina (§14).

---

## 2 · Las escenas que sirven para #que-estas-viendo (con minuto)

Los minutos salen de los subtítulos. Película: archivo japonés de Amazon
Japón ([kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_movie/Chainsaw%20Man.%20Reze-hen)).
Serie: archivos de Netflix en inglés y japonés
([foxofice/sub_share](https://github.com/foxofice/sub_share/tree/master/subs_list/animation/2022)).
Las frases son **mi traducción del japonés**, no el doblaje latino.

### 2.1 La cita en el cine (película *Arco de Reze*) ✅

| Minuto | Qué pasa | Frase (traducida del japonés) |
|---|---|---|
| 6:25-6:46 | Makima ve a Denji decaído y lo invita a salir mañana. Él grita de alegría. | «¿Mañana, en tu día libre, tenemos una cita?» / «¡Bieeen!» |
| 6:50-7:01 | Makima llega una hora antes y Denji ya está ahí. Él piensa «¡qué linda!». | «¿Denji-kun, ya estás aquí? Falta una hora.» |
| 7:03-7:08 | | «¿A qué hora viniste?» / «No podía dormir. Vine a las 5.» |
| 7:16-7:22 | Makima explica el plan del día. | «Hoy, desde ahora hasta las 12 de la noche, vamos **de sala en sala y vemos películas sin parar**.» |
| 7:24-7:52 | 1.ª película: golpes y gritos en pantalla. La sala se ríe; Denji no. Mira a Makima: tampoco se ríe. | «¿Eso era gracioso?» |
| 7:56-8:03 | A la salida, la crítica. | Denji: «Estuvo medio flojita.» Makima: «**No tuvo gracia.** Eso sí, la pantalla parecía cara.» |
| 8:08-8:32 | 2.ª película, un drama. Toda la sala llora; ellos no. | Makima: «No me gustó que **quisiera hacernos llorar a la fuerza**.» |
| 8:36 | 3.ª película. | Makima: «**La música estaba bien.**» |
| 8:41 | 4.ª película. | «Qué historia tan falsa…» |
| 8:48 | 5.ª película. | Makima: «**Normalita de verdad.**» |
| 8:50-8:59 | Antes de la última. | «La última. Dicen que es **difícil y que no se entiende**… ¿La vemos?» |
| 9:02-9:08 | Denji se sincera. | «La verdad, hasta ahora todas me parecieron **meh**. A lo mejor yo no entiendo de películas.» |
| 9:09-9:19 | **La frase del canal.** | Makima: «Yo también **encuentro una buena de cada diez**. **Pero esa una me ha cambiado la vida.**» |
| 9:21-10:05 | Suena el proyector. Empieza la película. | (sin diálogo) |
| 10:05-10:14 | Denji llora en una escena tonta y se esconde. | «¡Es una escena que no importa nada…! ¡Que no me vea Makima-san!» |
| 10:14-10:32 | Él mira a su lado: **Makima también llora**, en silencio. | (sin diálogo) |
| 10:32-10:41 | A la salida. | Denji: «Ese final no lo olvido hasta que me muera.» Makima: «Yo tampoco. **Sólo por eso valió la entrada de hoy.**» |
| 10:44-10:52 | | Denji: «¿Usted cree que yo tengo corazón?» |

En el manga es el **capítulo 39** ✅. El resumen de la wiki coincide: maratón
de cine hasta medianoche, Denji aburrido, Makima confiesa que siente lo
mismo, y en la última película los dos lloran en una escena «trivial»
([Chapter 39](https://chainsaw-man.fandom.com/wiki/Chapter_39),
[Sequential Planet](https://sequentialplanet.com/manga-review-chainsaw-man-chapter-39/)).

**Qué tiene la escena para la lámina**:
- **Butacas**, la **luz del proyector** sobre las caras, la **sala a
  oscuras**, las **entradas**. Todo real y modelable en Blender.
- **Opinar** y **recomendar** es lo que hacen: nota, crítica, veredicto.
- Es una **cita**, no una pelea: sirve para un canal tranquilo.

### 2.1b La cita, vista en vídeo (segunda pasada) ✅

Mirada con `fotogramas.py` en la película completa subtitulada en inglés
de Internet Archive ([rezearc](https://archive.org/details/rezearc),
100:08 min). Los fotogramas que se citan se volvieron a sacar en
**1920×1080 reales** del .mkv original
([csmrezearc.mkv](https://archive.org/download/rezearc/csmrezearc.mkv)).
Este corte va **15 a 20 s por detrás** del subtítulo japonés de arriba:
el orden y las frases coinciden ✅ (dos fuentes).

| Minuto (corte EN) | Qué se ve |
|---|---|
| 6:20 | Denji y Makima en la biblioteca, antes de la cita |
| 6:52 | Makima de día, luz natural: aquí se midió su pelo (§16) |
| 6:56 | «¿Vamos a una cita mañana?» |
| 7:04 | Denji celebra: ojos cerrados, **dos puños a la altura del pecho** |
| 7:08 | «Llegaste una hora antes» |
| 7:36-7:40 | «De sala en sala hasta medianoche» |
| 7:44 | **Sala llena de espaldas**, luz del proyector arriba; música de acción |
| 8:00-8:16 | Primeras críticas: «no tuvo gracia», «qué cara se ve la pantalla» |
| 8:28-9:08 | 2.ª y 3.ª película, palomitas, «la música estaba bien» |
| 9:12 | **Rótulo del cine: シネマ座** en la marquesina; «dicen que es difícil» |
| 9:28 | Makima, sentada y girada hacia Denji: **«una buena de cada diez, pero esa me cambió la vida»** |
| 9:43-10:22 | La última película: un drama de campo con otro color (verde azulado) |
| 10:25 | Denji llora tapándose la boca: «que no me vea Makima» |
| 10:36-10:37 | **Makima también llora**: de perfil, una lágrima, boca entreabierta |
| 10:43 | Plano general: las dos siluetas en la sala, pantalla en blanco |
| 10:49-10:58 | Saliendo: «nunca voy a olvidar esa última escena» / «yo tampoco» / «esa última película hizo que valiera la pena el precio de la entrada» |
| 11:00 | De noche, caminando: «Makima, ¿tú crees que tengo corazón?» |
| 11:52-12:40 | Al día siguiente Denji **saca una flor de una caja de donativos** para regalársela a Makima: «eso también significa que tengo corazón» |
| 13:00-14:08 | Bajo la lluvia decide pedirle que sea su novia; se cruza con Beam; luego la cabina de teléfono con Reze |

Lo nuevo que da el vídeo:
- **El cine se llama シネマ座** («Cinema-za»): letras plateadas en relieve
  sobre un panel verde azulado metálico, con 4 focos colgantes (9:12) ✅.
- **Cada «película falsa» tiene su propia música**. Los subtítulos de
  sonido lo marcan: «[action music playing]» (7:44), «[viewers
  sniffling]» (8:32), «[classical music playing]» (8:52) ✅.
- **La película que los hace llorar** tiene un color aparte, verde azulado
  y apagado: campo, un soldado con gorra y tirantes, una mujer con pañuelo
  blanco en la cabeza, se abrazan al final (9:50). Paleta medida en §5.3.
  No se sabe qué película real homenajea ⚠️ (no lo encontré).
- **Makima llora en silencio porque así lo pidió la dirección**. Su actriz
  japonesa, Tomori Kusunoki, lo cuenta: el guion decía «llora en silencio,
  sin ruido», y ella no quiso sobreactuar; sólo **a ojos de Denji** tenía
  que parecer tierna ✅
  ([Crank-in!, 14-sep-2025](https://www.crank-in.net/interview/172244/1)).
  Kusunoki dijo además que ella quería ver esa escena **en un cine de
  verdad**.
- La **flor de la caja de donativos** (11:52) es la misma que Power le
  quiere quitar al final de la película (§2.2): da un objeto pequeño para
  una lámina 2.

### 2.2 Otras escenas de la película que sirven

| Minuto | Escena | Para qué |
|---|---|---|
| 0:46-1:30 | El sueño de siempre: Pochita y la puerta que no hay que abrir. | Tono, Pochita |
| 1:58-2:13 | Power despierta a Denji a gritos: «¿¡Qué haces medio dormido!?». | Power en casa |
| 2:54-4:30 aprox. | Opening «IRIS OUT» (letra: «ばら撒く乱心…»). | Música |
| 13:42-15:52 | Lluvia, **cabina de teléfono**. Una chica entra corriendo, se ríe, llora («te pareces a mi perro muerto»). Denji hace el **truco de la flor** («¡Tarán! Sin trampa ni cartón»). Ella: «Trabajo en el **café Futamichi (二道)**, ven.» | Reze, presentar |
| 17:26-18:34 | En el café: «¿Te gusta el café?» / «Sabe a alcantarilla». «Me llamo **Reze**.» | Reze, saludar |
| 24:15 | «¿¡No sabes leer kanji!?» | Reze, explicar |
| 27:52-28:09 | Escuela de noche: Reze hace de maestra: «¡Correcto! ¡Genio!» | Reze, **explicar / celebrar** |
| 30:57-33:11 | La **piscina** de la escuela, de noche. | Reze, luz nocturna |
| 33:34-34:54 | Lluvia bajo techo: el cuento del **ratón de campo y el de ciudad**. | Reze, pensar |
| 44:27-47:12 | **Festival y fuegos artificiales**. «Deja el trabajo y huye conmigo.» | Reze, clímax |
| 1:09:26-1:10:02 | «¡Beam, conviértete en tiburón!» / «¡Correcto! ¡Correcto!» | Beam, humor |
| 1:27:32 | «¡Te espero en ese café!» | Denji |
| 1:37:34-1:39:07 | Escena final, después de la canción «JANE DOE» (1:33:56): el café cierra; entra **Power**: «¡Pa-pa-pa-Power!» «¡Ya volví!» Le quiere quitar la flor. | Power, **celebrar** |

⚠️ **Spoiler**: el minuto 48 en adelante revela quién es Reze. En la lámina
**no se muestra su forma de Bomba** ni se cuenta el final.

### 2.3 Escenas de la temporada 1 que sirven (anime, 2022)

| Ep. · minuto | Escena | Frase (subtítulo Netflix en inglés, traducido) |
|---|---|---|
| 1 · 4:42 | Denji y Pochita en la choza: sólo un pan para hoy. | «Hoy sólo tenemos una tostada.» |
| 1 · 9:12-9:16 | Denji sueña con pan con mermelada con Pochita. | «Comeré muchas tostadas con mermelada con Pochita.» |
| 1 · 23:03-23:50 | **Primera aparición de Makima**: le da a elegir. | «Morir como demonio o que yo te alimente como humano.» «Tostada con mantequilla y mermelada, ensalada, café… quizá un postre.» |
| 2 · 0:21-0:28 | La regla de Makima. | «Desde ahora eres mi perro. Sólo puedes contestar "sí" o "**guau**".» |
| 2 · 5:20-5:32 | Makima le da udon en la boca, en un **área de descanso de carretera al atardecer** (bancas de madera, montañas moradas; visto en el ep. 2 de Internet Archive, 5:30) ✅ | «¿Está rico?» / «**Guau.**» |
| 2 · 19:16-19:21 | **Entrada de Power.** | «¡Inclínate ante mí, humano! ¡Mi nombre es **Power**!» |
| 3 · 14:10-14:45 | Power entrega a Denji al demonio murciélago para recuperar a su gata **Nyako** (ニャーコ, «Meowy» en el sub de Netflix). | «Te traje un humano, como quedamos. Devuélveme a Nyako.» |
| 4 · 20:37-20:42 | Ya en casa de Aki, Power con su gata en brazos. | «Los humanos son un fastidio. ¿Verdad, Nyako?» |
| 7 · 6:22-6:37 | Himeno a Aki, comiendo en un restaurante japonés (mesas bajas, tabique de madera). En el episodio de Internet Archive la escena va de **6:10 a 7:18** ✅ (vista); la frase no se pudo leer ahí (sin subtítulos) ⚠️ | «Podemos comer en sitios así e **ir al cine de vez en cuando** después del trabajo.» |
| 7 · 7:43-7:58 | Power tiene una idea: | «¡Tuve una idea genial! (…) ¡El Nobel es mío!» |
| 12 · 22:52-23:09 | Cierre: el sueño de siempre. | «Es el mismo sueño otra vez.» |

Títulos japoneses de los episodios (de los nombres de archivo de
[kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Chainsaw%20Man)):
1 犬とチェンソー · 2 東京到着 · 3 ニャーコの行方 · 4 救出 · 5 銃の悪魔 ·
7 キスの味 · 8 銃声 · 9 京都より · 10 もっとボロボロ · 11 作戦開始 ·
12 日本刀VSチェンソー ✅.

---

## 3 · Arte oficial y referencias visuales

Primera pasada: sin red completa no se pudieron bajar ni medir imágenes.
**Segunda pasada: ahora sí hay tamaños reales** (API de la wiki), en §3.5
y en `referencias.json`.

### 3.1 La película *Arco de Reze* (2025)
- **Visual teaser, visual principal y «visual de después del estreno»**
  (lema: «誰も知らない、少女の心», «el corazón de una chica que nadie
  conoce») ✅ — [X oficial @CHAINSAWMAN_PR](https://x.com/CHAINSAWMAN_PR/status/1974338691591274782),
  [Dengeki Hobby](https://hobby.dengeki.com/news/2845630/) (los tres
  visuales en cuadro enmarcado).
- **Anuncio y visual teaser** ✅ — [web oficial, 17-dic-2023](https://chainsawman.dog/news/231217_01/).
- **Fecha y visuales de personaje** ✅ — [Animate Times](https://www.animatetimes.com/news/details.php?id=1742716849).
- **Tarjeta dibujada por Fujimoto** (Denji y Reze felices), regalo de
  entrada n.º 2 desde el 4-oct-2025 ✅ — [Anime!Anime!](https://animeanime.jp/article/2025/09/30/92917.html),
  [collabo-cafe](https://collabo-cafe.com/events/collabo/chainsaw-man-movie-attendants-benefits-vol2/).
  También hubo una **tarjeta de Reze dibujada por Kazutaka Sugiyama** ⚠️
  (sólo la cita el resumen de búsqueda).
- **Regalos de entrada** (lista oficial) — [web oficial: NOVELTY](https://chainsawman.dog/movie_reze/novelty/).
- **Tablero dibujado de Denji y Reze** (premio D del Ichiban Kuji) —
  [Dengeki Hobby](https://hobby.dengeki.com/news/3090318/).
- **Staff y reparto** — [web oficial de la película](https://chainsawman.dog/movie_reze/staffcast/).

### 3.2 La serie (2022)
- **Ilustración de Año Nuevo de Pochita**, de Kazutaka Sugiyama
  (diseñador de personajes) — [PASH! PLUS](https://www.pashplus.jp/anime/266414/).
- **Cómo se modeló en 3D la serie** (MAPPA) — [CGWORLD](https://cgworld.jp/article/202303-chainsawman1.html).
- **El opening**: cada plano copia una película (§11). Es la mejor fuente
  de poses de grupo «de cine» ✅.
- Próxima temporada: la web oficial ya tiene la página de **«刺客篇»
  (Arco de los Asesinos)** ✅ — [staff/cast](https://chainsawman.dog/assassin/staffcast/).

### 3.3 El manga
- **Logo japonés en SVG** (Wikimedia Commons) — [File:Chainsaw Man (Japanese) logo.svg](https://commons.wikimedia.org/wiki/File:Chainsaw_Man_(Japanese)_logo.svg).
- La cita del cine: **capítulo 39** ✅. Imágenes del capítulo:
  [Category:Chapter 39 Images](https://chainsaw-man.fandom.com/wiki/Category:Chapter_39_Images)
  (en la primera pasada estaba bloqueado; ya abre: ver §3.5).

- **Portadas de los tomos** que sirven ✅ ([Screen Rant](https://screenrant.com/best-chainsaw-man-covers-ranked/),
  [CBR](https://www.cbr.com/chainsaw-man-best-manga-covers/),
  [IMDb News](https://www.imdb.com/news/ni64523089/)): tomo 1, Chainsaw
  Man; tomo 2, **Power sonriendo con una guadaña**; tomo 3, Himeno; tomo 4,
  **Aki** con su mirada azul; tomo 6, **Reze** en el centro. Hay una
  portada de Makima abrazando a Chainsaw Man entre tripas azules:
  **no sirve** (violenta y con spoiler). Los fans juntaron todas en un
  vídeo: [YouTube](https://www.youtube.com/watch?v=o8QKAU9vyOA). Según esas
  fuentes, el manga va por **24 tomos** ✅
  ([CBR: tomo 24](https://www.cbr.com/chainsaw-man-manga-volume-24-cover-art-denji-analysis/)).

### 3.4 Lo que falta ⚠️
- ~~Las portadas de los demás tomos (5 y del 7 en adelante)~~ → resuelto
  en la segunda pasada: tomos 1, 2 y 4 a 11 con tamaño (§3.5). Siguen
  faltando el **3** y del **12 al 24** ⚠️.
- **Hojas de modelo** internas del estudio: no son públicas ⚠️. Lo más
  cercano son los **diseños de personaje del arco de Reze** (§3.5) y el
  «Denji Prototype» (hoja 3, n.º 427).
- ~~Fotogramas mirados por mí~~ → resuelto: la película y 3 episodios se
  miraron en vídeo (§2.1b, §15).

### 3.5 Lo nuevo de la segunda pasada (con tamaño medido)

**La escena del objeto, en el manga** (capítulo 39) ✅:
- [Chapter 39 Title Page.png](https://static.wikia.nocookie.net/chainsaw-man/images/1/16/Chapter_39_Title_Page.png)
  · 764×1200: la portada del capítulo «Tearjerker» (きっと泣く).
- [Denji and Makima's movie date.png](https://static.wikia.nocookie.net/chainsaw-man/images/9/9f/Denji_and_Makima%27s_movie_date.png)
  · 717×582: la sala vista desde atrás, filas de butacas, y primeros
  planos de Denji y Makima. **El público de fondo tiene caras simples y
  neutras; sólo ellos dos llevan sombra y detalle**. Es la regla para la
  lámina: personaje con detalle, público simple.
- [Makima during her date with Denji.png](https://static.wikia.nocookie.net/chainsaw-man/images/7/7c/Makima_during_her_date_with_Denji.png)
  · 394×1200: **Makima sin uniforme**, con ropa de calle (ver §16).
- Resumen del capítulo en la wiki: maratón «hasta medianoche», los dos
  lloran en la última, al salir Makima le escucha el corazón a Denji ✅
  ([wikitext del cap. 39](https://chainsaw-man.fandom.com/api.php?action=parse&page=Chapter%2039&format=json&prop=wikitext);
  su ficha dice `episode = Chainsaw Man – The Movie: Reze Arc`).

**Ilustraciones de revelado**: cada episodio tuvo una ilustración de un
artista invitado distinto. Por eso hay tanto arte oficial variado ✅ (hoja
1, n.º 5-7 y 9-13; hoja 2, n.º 49-52): Momo Momozawa (ep. 5-7), Shu (ep. 1,
2 y 8), RHYTHM BHATTACH, Daniel Kim, Eekee, TOOBOE («努力 未来 A Beautiful
Star», ep. 1-4 de la 2.ª parte), Aya Yamamoto, Ryu Nakayama, Kanako Nono y
Nonaka Nono (hoja 3, n.º 429-430).

**Portadas de tomo**, todas 1520×2400 ✅ (API de la wiki; hoja 2, n.º
62-71): [t.01](https://static.wikia.nocookie.net/chainsaw-man/images/0/0f/Volume_01.png) ·
[t.02](https://static.wikia.nocookie.net/chainsaw-man/images/6/68/Volume_02.png) ·
[t.04](https://static.wikia.nocookie.net/chainsaw-man/images/e/ef/Volume_04.png) ·
[t.05](https://static.wikia.nocookie.net/chainsaw-man/images/c/cf/Volume_05.png) ·
[t.06](https://static.wikia.nocookie.net/chainsaw-man/images/2/2e/Volume_06.png) ·
[t.07](https://static.wikia.nocookie.net/chainsaw-man/images/3/36/Volume_07.png) ·
[t.08](https://static.wikia.nocookie.net/chainsaw-man/images/1/14/Volume_08.png) ·
[t.09](https://static.wikia.nocookie.net/chainsaw-man/images/f/f3/Volume_09.png) ·
[t.10](https://static.wikia.nocookie.net/chainsaw-man/images/6/6b/Volume_10.png) ·
[t.11](https://static.wikia.nocookie.net/chainsaw-man/images/1/1b/Volume_11.png).
Las versiones **sin letras** (Textless) de los tomos 1, 2, 4 y 11 son la
misma ilustración sin logo, mejores para recortar una pose:
[Volume 11 (Textless)](https://static.wikia.nocookie.net/chainsaw-man/images/c/ce/Volume_11_%28Textless%29.png)
4000×6274 · [Volume 1 (Textless)](https://static.wikia.nocookie.net/chainsaw-man/images/a/a9/Volume_1_%28Textless%29.png)
3056×4800.

**Película *Arco de Reze***, vistos en la hoja 1 y medidos en la API:
- [Key Visual 3](https://static.wikia.nocookie.net/chainsaw-man/images/3/32/Chainsaw_Man_Movie_-_Reze_Arc_Key_Visual_3.png)
  · 2400×3278 (hoja 1, n.º 17): Denji y Reze en el café, ventana con
  cuadrícula de madera, luz cálida.
- [IMAX Poster](https://static.wikia.nocookie.net/chainsaw-man/images/e/e4/Chainsaw_Man_Movie_-_Reze_Arc_IMAX_Poster.png)
  · 2895×4096 (hoja 1, n.º 8).
- **Ilustración de cuenta atrás de Masato Nakazono**
  ([original](https://static.wikia.nocookie.net/chainsaw-man/images/a/a0/Reze_Arc_Countdown_Illustration_%28Masato_Nakazono%29.png),
  1170×1655, hoja 3, n.º 428): Denji con **gafas 3D de cine** y Pochita en
  brazos, dentro de un **marco de tira de película**, «公開まであと2日»
  (faltan 2 días para el estreno). Es arte oficial que ya junta cine y
  personaje: la mejor referencia de tono para este canal (lo vio el
  redactor en la hoja).
- [Reze Arc Illustration (min daifuku)](https://static.wikia.nocookie.net/chainsaw-man/images/1/1f/Reze_Arc_Illustration_%28min_daifuku%29.png)
  · 1692×2048 (hoja 2, n.º 78): **Makima abrazando a Pochita**, fondo
  blanco. Pose tierna y sin sangre.
- Los **diseños de personaje del arco de Reze** (Denji, Makima, Power,
  Aki, Reze), arte plano de MAPPA, de 514 a 694 px de ancho: de ahí salen
  los hex del uniforme (§16).

**Eventos con arte propio**:
- **Jump Festa 2025**: Denji, Aki, Makima y Power en cartel pop de un solo
  color de fondo (naranja, azul, morado, rosa) ✅ (hoja 1, n.º 18-21).
- **Chainsaw Man Buddy Stories** (spin-off): Denji y Yoru en un acuario y
  viñetas de sus 4 capítulos ✅ (hoja 2, n.º 61 y 90-92).
- Portadas de revistas de moda: §18F.

---

## 3A · Las hojas de contacto (qué número sirve)

Tres hojas en `hojas/`, hechas con `investigar_serie.py` sobre la wiki de
Fandom (1063 imágenes grandes). Las miraron el investigador de imagen y el
redactor. Debajo de cada miniatura va su tamaño real y el nombre del
archivo en la wiki.

**`hojas/imagen_01_portadas_y_colabs.jpg`** (n.º 1-48)
- **n.º 4** · [Men's Non-No n.º 464](https://static.wikia.nocookie.net/chainsaw-man/images/8/87/Men%27s_Non-No_No.464_Special_Edition.png)
  3197×4093: Reze y Makima en blanco y negro, **sólo el pelo y los ojos a
  color**. Tratamiento fácil de copiar en Photoshop.
- **n.º 5-7, 9-13** · ilustraciones de revelado de artistas invitados
  (Momo Momozawa, RHYTHM BHATTACH, Eekee, Shu). Poses vivas y variadas.
- **n.º 8** · [cartel IMAX de la película](https://static.wikia.nocookie.net/chainsaw-man/images/e/e4/Chainsaw_Man_Movie_-_Reze_Arc_IMAX_Poster.png)
  2895×4096. Sirve para la **cartelera** del vestíbulo (concepto B).
- **n.º 17** · [Key Visual 3](https://static.wikia.nocookie.net/chainsaw-man/images/3/32/Chainsaw_Man_Movie_-_Reze_Arc_Key_Visual_3.png)
  2400×3278: Denji y Reze en el café. Referencia de luz cálida (concepto C).
- **n.º 18-21** · Jump Festa 2025 (Denji, Aki, Makima, Power): cuerpo
  entero en acción sobre un color plano. **Presentar**.
- **n.º 22** · [CUT oct-2025](https://static.wikia.nocookie.net/chainsaw-man/images/f/f7/CUT_2025-10.png)
  2343×3000: Denji y Reze con una flor.
- **n.º 28-43** · páginas de manga: tinta, negros y rayado (§18A, §18B).
- **n.º 45** · «Aki Makima Prototype»: bocetos de diseño.

**`hojas/imagen_02_tomos_y_revistas.jpg`** (n.º 49-96)
- **n.º 62-71** · portadas de tomo 1, 5, 6, 7, 8, 11, 4, 9, 2 y 10 (en ese
  orden en la hoja), 1520×2400 (enlaces en §3.5). Personaje con objeto,
  arma o en grupo.
- **n.º 77** · [Makima Infobox](https://static.wikia.nocookie.net/chainsaw-man/images/7/7e/Makima_Infobox.png)
  1496×2322: Makima de pie, manos juntas delante, uniforme. **Presentar**.
- **n.º 78** · [Makima con Pochita (min daifuku)](https://static.wikia.nocookie.net/chainsaw-man/images/1/1f/Reze_Arc_Illustration_%28min_daifuku%29.png)
  1692×2048: pose tierna, sin sangre. **Recomendar, animar**.
- **n.º 93, 95, 96** · [UOMO](https://static.wikia.nocookie.net/chainsaw-man/images/f/f0/UOMO_2023-1.png),
  [CUT nov-2022](https://static.wikia.nocookie.net/chainsaw-man/images/0/03/CUT_2022-11.png)
  y [EYESCREAM](https://static.wikia.nocookie.net/chainsaw-man/images/7/74/EYESCREAM_2023-1.png):
  las portadas de moda (§18F).

**`hojas/imagen_03_vestuario_color_anime.jpg`** (n.º 385-432)
- **n.º 385-392** · Power en el anime, 1920×1080: gritos, colmillos,
  cuernos rojos. **Presentar, celebrar**.
- **n.º 393-408** · Makima en el anime, 1920×1080. Las mejores:
  **n.º 406** [«Makima tells Denji the type she likes»](https://static.wikia.nocookie.net/chainsaw-man/images/c/c9/Makima_tells_Denji_the_type_she_likes.png)
  (sentada a una mesa, mentón en la mano, luz cálida: **explicar**) y
  **n.º 408** [«Makima watching Power and Denji arguing»](https://static.wikia.nocookie.net/chainsaw-man/images/f/f8/Makima_watching_Power_and_Denji_arguing.png)
  (mejilla en la mano, sonrisa leve: **escuchar, recomendar**).
- **n.º 412** · [Makima hugging Denji](https://static.wikia.nocookie.net/chainsaw-man/images/4/43/Makima_hugging_Denji.png)
  1320×1549.
- **n.º 414** · [Makita Chainsaw (3).jpg](https://static.wikia.nocookie.net/chainsaw-man/images/b/b2/Makita_Chainsaw_%283%29.jpg)
  1840×1110: una motosierra Makita naranja de verdad, el juego de palabras
  del nombre (§18H). La parte de imagen la dio como n.º 413; en la hoja es
  el **414** (el 413 es la portada del capítulo 177).
- **n.º 427** · «Denji Prototype»: bocetos de caras de Denji.
- **n.º 428** · [cuenta atrás de Masato Nakazono](https://static.wikia.nocookie.net/chainsaw-man/images/a/a0/Reze_Arc_Countdown_Illustration_%28Masato_Nakazono%29.png)
  1170×1655: **Denji con gafas 3D y Pochita, marco de tira de película**.
  La imagen oficial más «de cine» de las tres hojas.
- **n.º 429-430** · ilustraciones de Nonaka Nono y Kanako Nono.

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D de la serie (Sketchfab)
**Segunda pasada: licencias y autores confirmados uno por uno con la API
de Sketchfab** (`/v3/models/<uid>`, fuente primaria) ✅. Todas piden
**atribución**: nombre del autor y enlace.

| Modelo | Autor | Licencia |
|---|---|---|
| [Pochita (Chainsaw Man)](https://sketchfab.com/3d-models/pochitachainsaw-man-9aa235674cce4a69aa735f2406544016) | code_6122 | CC Attribution (11,1 k triángulos) ✅ |
| [Pochita – Chainsaw Man – Character](https://sketchfab.com/3d-models/pochita-chainsaw-man-character-d0c67d0407eb49f3bff32827dbcf8210) | Gines Martinez | CC Attribution-ShareAlike ✅ (obliga a licenciar igual lo que se derive) |
| [Pochita – Chainsaw man Low Poly](https://sketchfab.com/3d-models/pochita-chainsaw-man-low-poly-17ca8dd893ee4a4987c1acb6e67f69c4) | XristinaLadogianni | CC Attribution ✅ |
| [Pochita – Chainsaw man](https://sketchfab.com/3d-models/pochita-chainsaw-man-6959e3043c5841529c1288bb3b0256d5) | AngelLeyend (issac.010609) | CC Attribution ✅ |
| [Pochita from Chainsaw Man](https://sketchfab.com/3d-models/pochita-from-chainsaw-man-40e382985aeb4d05a5881e34247a0c4e) | Josevan Danusastra (JosevanD2) | CC Attribution ✅ |
| [Etiqueta chainsaw-man](https://sketchfab.com/tags/chainsaw-man) | varios | — |

Pochita es **fan art**: sirve para una figurita o un peluche en la
butaca, nunca como personaje principal de la lámina.

### 4.2 Modelos 3D de objetos para la sala de cine (libres)

| Modelo | Autor | Licencia |
|---|---|---|
| [cinema/movie theater_[seat]](https://sketchfab.com/3d-models/cinemamovie-theater-seat-b8bcabfa355d4137910ef2e45b56b9bc) | Comicaroid (@yuuuusukeeee) | CC Attribution ✅ |
| [Cinema chair](https://sketchfab.com/3d-models/cinema-chair-c958af2d31244964a75f4b967d315b93) | Hans Tot (@qwerty14t) | CC Attribution ✅ |
| [Theater Chair – Red Velvet](https://sketchfab.com/3d-models/theater-chair-red-velvet-87815e72aa35450198e1cd98e888d68f) | Glowbox 3D (@glowbox3d), el mismo de Red Plaid | CC Attribution ✅ |
| [Theater Chair – Red Plaid](https://sketchfab.com/3d-models/theater-chair-red-plaid-98e141e7e69e4b42a225b1f8fb4f0b1b) | Glowbox 3D (@glowbox3d) | CC Attribution ✅ |
| [Cinema Seat](https://sketchfab.com/3d-models/cinema-seat-6c44adbc299c4f8ab45e9913d58cfcba) | Connor Wassall | CC Attribution ✅ |
| [Old theatre chair](https://sketchfab.com/3d-models/old-theatre-chair-0e346addc570459481df4d05c6cfb806) | wozniakowski.smierdzi | CC Attribution ✅ |
| [Cinema seat (tienda, de pago)](https://sketchfab.com/3d-models/cinema-seat-f873fc555d414f8ea14bf451d1822038) | ChakkitPP | de pago: no usar |

Las **entradas** no necesitan modelo: son un plano de papel con la
textura de §5.4, doblado un poco en Blender.

Ojo: las butacas de la película son **mostaza/ámbar**, no rojas (§5.3). Los
modelos «Red Velvet» y «Red Plaid» sirven por la forma; el color se cambia
en el shader.

### 4.3 Fan art 2D y 3D (mirar, nunca pegar)
- Pixiv: [Denji](https://www.pixiv.net/en/artworks/104586196),
  [Denji vs Makima](https://www.pixiv.net/en/artworks/115842687),
  etiqueta [デンジ(チェンソーマン)](https://www.pixiv.net/en/tags/%E3%83%87%E3%83%B3%E3%82%B8(%E3%83%81%E3%82%A7%E3%83%B3%E3%82%BD%E3%83%BC%E3%83%9E%E3%83%B3)).
  Autor: el que figura en cada página (no lo pude abrir).
- Pixiv Enciclopedia: [デンマキ (Denji × Makima)](https://dic.pixiv.net/a/%E3%83%87%E3%83%B3%E3%83%9E%E3%82%AD),
  [チェンソーマンレゼ篇](https://dic.pixiv.net/a/%E3%83%81%E3%82%A7%E3%83%B3%E3%82%BD%E3%83%BC%E3%83%9E%E3%83%B3%E3%83%AC%E3%82%BC%E7%AF%87),
  [マキマ](https://dic.pixiv.net/en/a/Makima). Hay incluso una novela de
  fans titulada «映画デート» (cita de cine) con Denji y Asa
  ([pixiv novel](https://www.pixiv.net/novel/show.php?id=18847264)): la
  cita de cine es un tema que el fandom repite.
- ArtStation: [Makima 3D, Victor Porto (Blender, Eevee)](https://www.artstation.com/artwork/3qO44J),
  [Makima, Hunter Mortenson](https://www.artstation.com/artwork/2q4Lde),
  [Reze x Makima](https://www.artstation.com/artwork/4XXyd2),
  [Reze, Ryoma Miyakawa](https://www.artstation.com/artwork/QrJNzZ),
  [WIP Makima en Blender, SteamMonarch](https://www.artstation.com/artwork/d0XmYw).
- **Fan art mejor valorado en Safebooru**, con tamaño y origen (lo juntó
  `recolectar.py`; enlaces en `referencias.json`): Makima 3000×3000 y
  2793×3719, Denji 3840×4096, Power 3000×2000, Reze 2048×1638, Pochita
  2239×1491. Sólo para mirar poses de fans.

### 4.4 Modelos 3D de los personajes (segunda pasada, API de Sketchfab) ✅

| Modelo | Autor | Licencia |
|---|---|---|
| [Denji (Chainsaw-Man) (Yes Rigged bone)](https://sketchfab.com/3d-models/none-bdd7c53adfc54033b47fb8e3f60545b1) | KenzoDkohno22T | CC Attribution, **ya con huesos** |
| [Chainsaw-man and makima (Yes Rigged bone)](https://sketchfab.com/3d-models/none-2d08535cb4d94657976fbfc5d8b45e60) | KenzoDkohno22T | CC Attribution, con huesos |
| [Denji (Chainsaw Man)](https://sketchfab.com/3d-models/none-55234e1109bc40819168fadbf5869fca) | Scorpion4241 | CC Attribution |
| [Denji and Pochita](https://sketchfab.com/3d-models/none-aa07c407793d48dca02f8b27ba79d397) | Hopeful_sage17 | CC Attribution |
| [Makima (Chainsaw Man)](https://sketchfab.com/3d-models/none-c45fe856ba014d6093f0436872732dac) | Scorpion4241 | CC Attribution |
| [Mакима Makima](https://sketchfab.com/3d-models/none-87844679b7d046d889d2062e5f51cd66) | DrOchu-n | CC Attribution |
| [Makima Bean Plushie](https://sketchfab.com/3d-models/none-ba52df496e594546b4c5eab8722f11d9) | Toastily | CC Attribution (peluche: sirve de objeto en la butaca) |
| [Power (Chainsaw Man)](https://sketchfab.com/3d-models/none-e0a51a616135401da76398d8afe52e3f) | Scorpion4241 | CC Attribution |
| [Power from chainsaw man](https://sketchfab.com/3d-models/none-48456a305810436b92eb321c1791cbd7) | ShmeliArt | CC Attribution |
| [Chainsaw Man (korbenhall)](https://sketchfab.com/3d-models/none-374827532dfa4a73aab9f5e15fd8ab8c) | korbenhall | CC Attribution (1,3 millones de caras) |
| [Chainsaw man - Darkness demon](https://sketchfab.com/3d-models/none-8218cc69a7a244ecbe49f842d9d882c7) | kirbycano98 | CC Attribution |
| [Chainsaw Man helmet](https://sketchfab.com/3d-models/none-3d38382f1acb4e69872bcdf6bc7c12c9) | labhijits | CC Attribution |
| [Chainsaw Man (Last_Hawk)](https://sketchfab.com/3d-models/none-1f0214b7063a4bb3ae14fb59a7571ff9) | Last_Hawk | **CC Attribution-NonCommercial**: nada que se venda |

Son **fan art**: la licencia la pone quien sube el modelo, no Shueisha ni
MAPPA. Sirven de base de pose y proporciones, citando autor y enlace. Para
pose fiel, mejor las figuras oficiales (§18F).

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 La sala de cine de la cita
- Es un **cine de barrio de Tokio en 1997** (la serie pasa en un 1997
  alternativo ⚠️, de memoria). Butacas en filas, pantalla, **haz del
  proyector** por encima de las cabezas (en los subtítulos se oye
  «映写機の回る音», «el proyector girando», en el 9:21) ✅.
- **Se llama シネマ座 («Cinema-za»)**: se lee en la marquesina, letras
  plateadas en relieve sobre un panel verde azulado metálico, con 4 focos
  colgantes (película, corte EN, 9:12) ✅ (segunda pasada, visto en vídeo).
- No encontré **qué cine real** sirvió de modelo ⚠️ (tampoco con el nombre
  シネマ座 en la wiki).
- **Butacas mostaza/ámbar envejecido**, no rojo vino: así se ven en la sala
  llena de la película (7:44) ✅ medido. La primera pasada las proponía
  rojo vino sin haberlas visto.
- La luz: **todo oscuro menos las caras**, iluminadas por la pantalla. El
  **haz del proyector es blanco cálido** con un halo de aberración
  cromática **verde-violeta** alrededor (7:44), no azul frío ✅ (una
  escena medida: el halo cambia según el plano ⚠️).

### 5.2 Los sitios de la película, con sus lugares reales ✅
Varios blogs de «peregrinación» coinciden
([furaba](https://furaba-animeseichi.blog.jp/archives/41020580.html),
[note/tamro](https://note.com/tamro/n/na130cbdb5e45),
[shiritoku](https://shiritoku.net/chainsawman-reze-seichi/),
[anitora](https://anitora5050.com/chainsawman-travel/),
[mono-log](https://mono-log.jp/archives/2026/02/reze-pilgrimage.php)):
- **Cabina de teléfono** donde se conocen: Kanda-Jinbōchō 1-44
  (Chiyoda, Tokio), frente al ramen Menya 33. **NTT Este** pidió no dejar
  flores de gerbera en la cabina (la gente las deja en homenaje) ⚠️ (un
  solo resumen).
- **Onna-zaka**, la escalera por la que Reze sube al café: Kanda-Sarugakuchō 2.
- **El café Futamichi (二道)**: en la zona hay un café real, **Trois
  Bagues Vert**, donde los fans hacen cola; los blogs dicen que no es
  seguro que sea el modelo ⚠️.
- **La escuela de noche y su piscina**, el **festival** con fuegos
  artificiales (min. 44-47).

### 5.3 Luz y paleta (segunda pasada: medida)
**Segunda pasada**: la sala se midió con `estilo.py` y Pillow en
fotogramas reales de la película (Internet Archive, corte EN). Los de
personajes, en fotogramas y en los diseños planos del arco de Reze (§16).
Las guías de fans se quedan sólo como contraste
([anime-colors: Makima](https://www.anime-colors.com/chainsaw-man-series/makima),
[anime-colors: Denji](https://www.anime-colors.com/chainsaw-man-series/denji),
[SchemeColor: Makima](https://www.schemecolor.com/makima-chainsaw-man.php),
[color-hex: Power](https://www.color-hex.com/color-palette/1020164),
[color-hex: Chainsaw Man](https://www.color-hex.com/color-palette/1056903)).

**La sala de シネマ座** (fotograma de 7:44, sala llena de espaldas) ✅:

| Qué | Hex | Peso en el fotograma |
|---|---|---|
| Negro de sala | `#020202` | 35 % |
| Penumbra oliva | `#323124` | 23 % |
| Butaca en sombra (mostaza) | `#544A36` | 17 % |
| Butaca iluminada (ámbar) | `#7C6D4A` | 9 % |
| Piel iluminada por la pantalla | `#C2B4A2` | 1 % |
| Fondo de sala a oscuras, verde apagado | `#151815` | — |

**La marquesina シネマ座** (fotograma de 9:12) ✅: panel gris azulado
metálico `#282A2C` / `#464E4D` / `#758382`; letras casi blancas
`#9CADAD` a `#C2B4A2`.

**La película que los hace llorar** (fotograma de 9:50), verde azulado
desaturado ✅: `#030403` 39 % · `#151D1C` 27 % · `#415855` 14 % ·
`#7A8E87` 12 % · `#BAC2BC` 9 %.

**Personajes** (detalle en §16):

| Qué | Hex | De dónde |
|---|---|---|
| Pelo de Makima en la **película** (granate) | `#4C201F` (de `#481D1B` a `#552423`) | fotograma de día, 6:52 ✅ |
| Pelo de Makima en la **serie de TV** (rosa salmón) | `#D3978F` | guía de fans; coincide con la TV ✅ |
| Pelo de Makima en el diseño plano del arco de Reze | `#CF4F48` | diseño de MAPPA, medido ✅ |
| Iris de Makima (anillos ámbar) | `#E6C873` | guía de fans ⚠️ |
| Pelo de Denji (rubio dorado cálido) | `#E1B760` | fotograma 7:04 ✅ |
| Piel de Denji | `#F2C89E` | fotograma 7:04 ✅ |
| Camisa del uniforme (crema, no blanco) | `#EDEDE3` a `#F0EFE7` | 3 diseños ✅ |
| Pantalón y traje (gris pizarra, no negro) | `#2F393A` / `#30393B` | 3 diseños ✅ |
| Pelo de Power (diseño del arco de Reze) | `#E09975` | diseño, medido ✅ |
| Cuernos de Power (rojo) | `#C3544B` | guía de fans ⚠️ |
| Papel de entrada | `#EDE6D6` | propuesto; Paper005/006 dan ese tono (§5.4) ⚠️ |

Lo que cambió respecto a la primera pasada: el haz del proyector
`#CFE3F2` (azul frío, propuesto) → blanco cálido con halo verde-violeta;
las butacas `#6E1F24` (rojo vino, propuesto) → `#544A36`/`#7C6D4A`
(mostaza/ámbar); la sala `#101318` (propuesto) → `#020202`/`#151815`
(medidos); el pelo de Makima en la película `#D3978F` → `#4C201F`.

**Otro sitio medido**: el área de descanso de carretera del ep. 2 (5:30),
al atardecer: cielo malva apagado `#696870`, montañas casi negras
azuladas `#23242F` ⚠️ (un solo fotograma).

La serie de 2022 buscó **colores apagados y luz «de cámara»** ✅ (§11). La
película es **más viva y saturada** (fuegos artificiales, noche azul,
verano) ⚠️ (de memoria).

### 5.4 Texturas reales equivalentes (CC0)
**Segunda pasada: miradas** (hoja de miniaturas oficiales de ambientCG) ✅.
Para la butaca, **Fabric022** (pana azul acanalada) y **Fabric026** (pana
roja acanalada) tienen el **canalado de terciopelo de butaca** correcto:
se usa su mapa de altura y rugosidad y se **cambia el color a
mostaza/ámbar** en el shader de Blender. Fabric004 (carbono), Fabric019
(nube blanca) y Fabric031 (tweed gris) **no sirven**. Para el papel de la
entrada, **Paper005 y Paper006** (crema tostado con grano fino) son
mejores que Paper001/003 (blancos).
En [ambientCG](https://ambientcg.com/) (todo CC0). Lista de la primera
pasada:
[Fabric 004](https://ambientcg.com/view?id=Fabric004),
[Fabric 019](https://ambientcg.com/view?id=Fabric019),
[Fabric 022](https://ambientcg.com/view?id=Fabric022),
[Fabric 026](https://ambientcg.com/view?id=Fabric026),
[Fabric 031](https://ambientcg.com/view?id=Fabric031),
[Carpet 001](https://ambientcg.com/view?id=Carpet001),
[Carpet 008](https://ambientcg.com/view?id=Carpet008),
[Carpet 011](https://ambientcg.com/view?id=Carpet011),
[Carpet 012](https://ambientcg.com/view?id=Carpet012).

Para el **papel de las entradas** (también CC0, ambientCG):
[Paper 001](https://ambientcg.com/view?id=Paper001),
[Paper 003](https://ambientcg.com/view?id=Paper003),
[Paper 005](https://ambientcg.com/view?id=Paper005),
[Paper 006](https://ambientcg.com/view?id=Paper006),
y para una caja o un vaso de cartón
[Cardboard 004](https://ambientcg.com/view?id=Cardboard004) (las moquetas
Carpet y el cartón no se miraron en la segunda pasada ⚠️).

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia
- **El logo es letra dibujada a mano, no una fuente** ⚠️ (lo dice Font In
  Logo; nadie en el foro de dafont encontró una fuente igual)
  ([Font In Logo](https://www.fontinlogo.com/famous-fonts/chainsaw-man-font),
  [logo SVG en Wikimedia](https://commons.wikimedia.org/wiki/File:Chainsaw_Man_(Japanese)_logo.svg)).
  Hay un hilo sin respuesta clara en el [foro de dafont](https://www.dafont.com/forum/read/502386/chainsaw-man-font).
  Descripción de [1000logos](https://1000logos.net/chainsaw-man-logo/):
  letras gruesas con **bordes dentados**, como dientes de motosierra.
- **Los globos del manga** son normales (blancos, ovalados). Lo propio de
  Fujimoto no es el globo: son **viñetas casi mudas** y **viñetas
  repetidas** con un cambio mínimo, como planos de cine ✅
  ([CBR: 15 mejores viñetas](https://www.cbr.com/greatest-chainsaw-man-manga-panels/),
  [CBR: Fujimoto](https://www.cbr.com/chainsaw-man-tatsuki-fujimoto-greatest-manga-creator/)).
- El directorio [Manga Font Directory](https://mangafonts.carrd.co/) sirve
  para buscar letras de rotulación de manga.

### 6.2 Letras libres comprobadas por mí
Bajé cada archivo de [google/fonts](https://github.com/google/fonts) y
comprobé con fontTools **á é í ó ú ñ Á É Í Ó Ú Ñ ¿ ¡ ü**. Todas pasan ✅.

| Uso | Letra libre | Licencia | Tildes, ñ, ¿ ¡ |
|---|---|---|---|
| Subtítulo en la pantalla del cine (texto del canal) | **Zen Kaku Gothic New** Black, o **Noto Sans** Bold | OFL | ✅ |
| Título «¿Qué estás viendo?» con aire del logo | **Dela Gothic One** (gótica japonesa muy gruesa; ensuciar los bordes a mano) | OFL | ✅ |
| Rótulo luminoso del cine (marquesina) | **Limelight** o **Bebas Neue** (sólo mayúsculas) | OFL | ✅ |
| Texto impreso de la entrada | **Space Mono** Bold o **DotGothic16** (impresora de puntos) | OFL | ✅ |
| Nota a mano en la entrada (bolígrafo) | **Yuji Syuku** | OFL | ✅ |
| Letra de manga antigua (antique) | **Zen Antique** | OFL | ✅ |
| La que sugiere Font In Logo para el logo | **Metal Mania** | OFL | ✅ (pero es heavy metal occidental: **no se parece de verdad**, no la uso) |

**Subtítulo de cine japonés**: la letra libre que imita los subtítulos
pintados a mano de los cines de Japón es **しねきゃぷしょん
(Cinecaption)**: gratis, uso comercial permitido avisando al autor
([Madonomori](https://forest.watch.impress.co.jp/docs/serial/font/1002663.html),
[ffont.jp](https://ffont.jp/cinecaption/),
[goodfreefonts](https://goodfreefonts.com/823/)) ✅. Trae kana, kanji y
alfabeto, pero **no sé si trae á é ñ ¿ ¡** ⚠️: úsala sólo para una
palabra japonesa de adorno (por ejemplo «上映中», «en cartelera»), no
para el texto del canal.

---

## 7 · Cómo hablan y piensan en pantalla (el cuadro de diálogo)

### 7.1 Lo que hay de verdad
- **No hay un globo propio de Chainsaw Man** que se pueda verificar. La
  guía de cuadros del proyecto ya lo decía («pocas palabras, cortes de
  cine») y esta investigación lo confirma ✅.
- La serie de 2022 se hizo **como una película de imagen real**: el
  director Ryū Nakayama quería planos «como filmados con cámara», menos
  exageración y menos gestos «de anime» ✅
  ([Famitsu](https://www.famitsu.com/news/202212/03284286.html),
  [Real Sound: por qué es «de cine»](https://realsound.jp/movie/2022/10/post-1155971_2.html),
  [UOMO](https://www.webuomo.jp/culture/archive/t/PENrqQ/265127/)).
- El director de la película, **Tatsuya Yoshihara**, la describe en
  broma como «una película romántica… o de tiburones, según se mire» ⚠️
  (una sola fuente en el resumen), y dice que querían que el público
  sintiera lo mismo que al leer el manga ✅
  ([ANN](https://www.animenewsnetwork.com/interview/2025-10-31/chainsaw-man-the-movie-reze-arc-director-tatsuya-yoshihara-assistant-director-masato-nakazono/.230134),
  [Bollywood Hungama](https://www.bollywoodhungama.com/news/international/exclusive-chainsaw-man-reze-arc-director-tatsuya-yoshihara-staying-true-tatsuki-fujimotos-vision-says-wanted-capture-exact-feel-manga/),
  [MANTANWEB](https://en.mantan-web.jp/e_article/20250919dog00m200003000c.html),
  [CBR](https://www.cbr.com/chainsaw-man-movie-director-fixing-season-1-mistakes/)).
- La película lleva el cine **dentro de la historia**: la cita en la sala
  (§2.1). La canción que suena ahí se llama **«our film»** (Kensuke Ushio) ✅
  ([Natalie](https://natalie.mu/music/pp/chainsawman-reze03),
  [Lisani](https://www.lisani.jp/0000294153/)).
- **Pensamientos**: en el anime, la voz interior va en off, sin globo; en
  los subtítulos de Netflix va en *cursiva* (por ejemplo Himeno en el
  ep. 7, 6:58: «Si Aki pelea con el Demonio Pistola, lo matan seguro») ✅.
  En la película, lo que piensa Denji en el cine («¡Que no me vea
  Makima-san!», 10:11) parece voz en off, porque están en plena
  proyección ⚠️ (el subtítulo no lo dice).

### 7.2 El cuadro de esta lámina: **el subtítulo de cine**
Como la escena es en una sala, el texto va **como subtítulo sobre la
pantalla** o **en las franjas negras** de arriba y abajo:
- Letra blanca con borde negro fino (o amarilla, como los subtítulos
  antiguos), centrada abajo, **dos líneas como máximo**.
- El **nombre del que habla no se pone**: se sabe por quién está en
  escena. Si hace falta, va antes, entre guion corto: «Makima:», pero
  mejor sin nombre.
- **Pensamiento de Denji**: el mismo subtítulo, **en cursiva** (así lo
  hacen los subtítulos de Netflix de la serie) ✅.
- Lo que no es diálogo (la regla del spoiler) va **impreso en la entrada**
  o en el **rótulo de la sala**, no en un globo.
- **La propia serie ya lo hace** (segunda pasada, visto en vídeo): el
  **ep. 1 no tiene animación de ending**. De 24:00 a 24:16 sólo hay
  **texto blanco sobre fondo negro**, créditos de cine, mientras suena
  «CHAINSAW BLOOD» ✅ (episodio en Internet Archive y
  [CBR](https://www.cbr.com/every-end-credit-sequence-chainsaw-man-season-1-explained/)).
  Una lámina con texto blanco sobre negro, como créditos, es fiel.
- **El nombre del cine** para la marquesina es **シネマ座**, letras
  plateadas en relieve sobre panel verde azulado (§5.1).

Esto no es una burbuja blanca: es el propio mundo de la escena (una sala
de cine), y además es literalmente lo que ve el que está en
#que-estas-viendo.

### 7.3 Qué NO hacer con el texto
- Nada de **globo blanco de cómic** flotando.
- Nada de **letras de motosierra/sangre** para el texto del canal: se lee
  mal y el canal es tranquilo.
- Nada de **onomatopeyas de motosierra** («VRRRM») en esta lámina: aquí
  nadie pelea.

---

## 8 · Los personajes

Lo que va con ✅ sale de las fuentes o de los subtítulos (con minuto). Lo
que va con ⚠️ lo describo de memoria: hay que mirarlo en una imagen antes
de dibujarlo.

### Makima — la del cine (2.ª en las tres encuestas oficiales)
- **Qué es**: jefa de la **División Especial 4** de la Seguridad Pública
  de caza de demonios ✅ (subtítulos: «公安対魔特異4課», ep. 2, 19:49; [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/ChainsawManMakima)).
- **Cómo se ve**: pelo **rosa salmón en trenza**, ojos **amarillos con
  anillos**, camisa blanca, **corbata negra**, pantalón negro y abrigo ✅
  ([Carbon Costume](https://carboncostume.com/makima-from-chainsaw-man/),
  [Costumary](https://www.costumary.com/templates/chainsaw-man/makima)).
  **Ojo al color**: rosa salmón en la **serie de TV**; en la **película**
  se ve **granate `#4C201F`** (medido en un fotograma de día, 6:52) ✅.
  En la cita del cine **no lleva uniforme**: cárdigan claro, vestido
  oscuro por la rodilla, medias y zapatos planos oscuros, bolso pequeño
  (manga, cap. 39) ✅ (§16).
- **Cómo habla**: calmada, bajito, siempre sonríe; a él le dice
  **«Denji-kun»** y a Power **«Power-chan»** ✅ (subtítulos: ep. 2, 0:21
  «Denji-kun, desde ahora te voy a tener yo»; película 5:00 «パワーちゃん»).
  Nunca grita.
- **Cómo explica algo**: con una opción cerrada. «Morir como demonio o
  que yo te alimente» (ep. 1, 23:03); «sólo "sí" o "guau"» (ep. 2, 0:26) ✅.
- **Qué ama**: **el cine**. Ve diez películas para dar con una buena, y
  llora en silencio con la que vale (película, 9:09-10:41) ✅. **Por qué**:
  según Fujimoto en la guía oficial *Love, Flower, Chainsaw Guide*, Makima
  no tiene experiencia vivida propia, así que **ve películas para estudiar
  cómo sienten los humanos**; por lo mismo «fuma» cigarrillos «hi-fight»
  (parodia de Hi-Lite) sin fumar de verdad, sólo imita el gesto ✅
  ([wiki: Makima, Trivia](https://chainsaw-man.fandom.com/wiki/Makima#Trivia)).
  Mide **168 cm** ✅ (AniList, que cita la tabla de alturas de la
  exposición oficial del anime).
- **Lenguaje corporal**: quieta, manos juntas, cabeza un poco ladeada,
  mirada fija a los ojos ⚠️.
- **Su actriz japonesa**, Tomori Kusunoki, dice que la interpreta «pensando
  en cómo la ve Denji» ✅ (títulos de entrevista: [MEN'S NON-NO](https://www.mensnonno.jp/lifestyle/culture/256322/),
  [Hominis](https://hominis.media/category/voiceActor/post14781/); y cita
  textual en [Crank-in!](https://www.crank-in.net/interview/172244/1),
  14-sep-2025: en el llanto del cine no quiso sobreactuar, «llora en
  silencio, sin ruido»; sólo a ojos de Denji tenía que parecer tierna).
- ⚠️ **Spoiler grande**: lo que Makima es de verdad. **No se insinúa en la
  lámina** (el canal pide marcar spoilers).

### Denji — el protagonista (4.º en la 2.ª y en la 3.ª)
- **Qué es**: chico de **16 años** ✅ (película, 45:02: «16 años y sin
  dejarte ir a la escuela»), cazador de demonios con el corazón de
  **Pochita**, el demonio motosierra ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/ChainsawManMainCharacters)).
  Creció pagando una deuda de la yakuza ✅ (TV Tropes; «借金», ep. 1).
- **Cómo se ve**: pelo **rubio despeinado** (medido en la película:
  `#E1B760`), dientes afilados, traje de la Seguridad Pública (camisa
  blanca, corbata negra floja), el **cordón de arranque** en el pecho:
  al tirar de él le salen las motosierras ✅ (wiki, páginas de Denji y de
  Pochita; fuera de Fandom no lo encontré llamado «objeto icónico» ⚠️).
  Mide **173 cm** (180 cm transformado) ✅ (AniList).
- **Cómo habla**: bruto, directo, con palabrotas; dice **«最強»
  («lo más fuerte, lo mejor»)** para todo: «¡El pan más poderoso!» (ep. 2,
  13:50), «Estoy poderosamente bien» (película, 6:29) ✅. El café le
  «sabe a alcantarilla» (película, 17:40) ✅.
- **Qué le importa**: comer pan con mermelada, una vida normal, que lo
  quieran. «Yo quiero a quien me quiere» (película, 18:27) ✅.
- **Cómo se ríe / celebra**: a gritos, «¡Bieeen!» (película, 6:44) ✅.
  En vídeo (corte EN, 7:04): **ojos cerrados, sonrisa suave, los dos puños
  a la altura del pecho**, un «yay» tímido ✅. Su actor japonés, Kikunosuke
  Toya, dice que en la cita «se le nota todo»: «¡Sííí!!», «¡Qué linda!!»
  (やったー!! カワイイ!!) ✅ ([Crank-in!](https://www.crank-in.net/interview/172244/1)).
- **En el cine**: se aburre, no entiende las risas, y llora a escondidas
  en la última (§2.1) ✅.

### Power — la que más memes tiene (1.ª en la 1.ª encuesta)
- **Qué es**: **demonio de la Sangre** («血の悪魔», ep. 3) en cuerpo humano
  (Fiend), compañera de Denji ✅ ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/ChainsawManMainCharacters)).
- **Cómo se ve**: pelo largo **rubio rosado**, **dos cuernos rojos**,
  colmillos, **pupilas en forma de aspa, roja y amarilla** ✅ (visto en
  1080p, ep. 2, 19:20; Danbooru la etiqueta `cross-shaped_pupils`);
  sudadera y ropa de casa en el piso de Aki ⚠️. Mide **170 cm** ✅
  (AniList).
- **Cómo habla**: con palabras de anciana, **«ワシ» («yo», de viejo) y
  «〜じゃ»**. Denji se burla: «Eso de "washi" y "nanja", te lo inventas»
  (ep. 3, 1:31) ✅. Fanfarrona y mentirosa ✅ (TV Tropes).
- **Cómo se presenta**: «¡Inclínate ante mí, humano! ¡Mi nombre es
  Power!» (ep. 2, 19:16) ✅.
- **Cómo celebra**: «¡Mírenlo! ¡Es mérito mío!» (ep. 2, 22:13); «¡Tuve
  una idea genial! ¡El Nobel es mío!» (ep. 7, 7:43-7:58); «¡Ya volví!»
  (película, 1:38:20) ✅.
- **Qué le importa**: su gata **Nyako** (ep. 3 y 4) ✅.

### Aki Hayakawa — el hermano mayor (1.º en la 2.ª encuesta)
- **Qué es**: cazador de la División 4, **serio y frío**, al que Makima
  le encarga cuidar de Denji y Power ✅ (TV Tropes).
- **Cómo se ve**: pelo negro azulado `#27323F` con **moño alto**, traje
  gris pizarra `#30393B` (medidos en su diseño del arco de Reze), cigarro,
  katana ✅. En el ep. 7 (7:14) el traje se ve verde oliva por la luz del
  restaurante ✅ (visto). **Piercings en la oreja**, que le hizo Himeno ✅
  (wiki, cap. 31). Mide **182 cm** ✅ (AniList).
- **Qué le importa**: vengarse del Demonio Pistola. Himeno le propone
  dejarlo e ir al cine; él dice que no (ep. 7, 6:22-6:48) ✅.
- **Cómo habla**: poco, seco, con tono de reproche ⚠️.

### Reze — la más querida hoy (1.ª en la 3.ª encuesta)
- **Cómo se ve**: pelo **morado por los hombros**, ojos **verde
  esmeralda**, una **gargantilla (choker)** negra ✅
  ([Game Rant](https://gamerant.com/chainsaw-man-who-is-reze/),
  [Carbon Costume](https://carboncostume.com/reze-from-chainsaw-man/)).
  La primera vez lleva una camiseta holgada con **una campana dibujada** y
  mochila; en la escuela, **camisa blanca y pantalón corto** ✅
  ([Chainsaw Man Wiki: Reze](https://chainsaw-man.fandom.com/wiki/Reze)).
- **Dónde está**: trabaja en el **café Futamichi** ✅ (película, 15:45).
- **Cómo habla**: juguetona, se ríe mucho, se burla con cariño: «¡Mira esa
  cara! ¡Te haces el fuerte!» (17:36), «¡Correcto! ¡Genio!» (27:58),
  «Te enseño» (32:34) ✅.
- **Cómo saluda**: «Me llamo Reze. ¿Y tú?» (18:01) ✅.
- **Cómo explica algo**: con un cuento, el del **ratón de campo y el de
  ciudad** (33:44-34:54) ✅.
- ⚠️ **Spoiler**: lo que Reze es de verdad y su final. **No va en la
  lámina.** Su forma de combate tampoco.
- **Su actriz japonesa**: Reina Ueda. Se habló de la «**Reze-loss**» (la
  pena de los fans al salir del cine) ⚠️ (la actriz ✅ por Oricon y PASH!
  PLUS; la «Reze-loss», sólo
  [Futaman](https://futaman.futabanet.jp/articles/-/129762)).

### Pochita — la mascota
- Perrito demonio rojo anaranjado con **una motosierra saliendo del centro
  de la cabeza**, asas en el cuerpo y **la cola en forma de cordón de
  arranque**; sólo ladra y gime, como un perro ✅ (AniList; wiki). En los
  sueños de Denji le dice: «**No abras nunca esa puerta**» (película,
  0:01:18) ✅.
- Sirve como **peluche o figurita** en una butaca: no habla en la lámina.

### Secundarios que conviene tener a mano
- **Beam** (el demonio tiburón): llama a Denji «**¡Chainsaw-sama!**» y
  grita «¡Correcto! ¡Correcto!» (película, 1:09:58) ✅. 8.º en la encuesta
  de VIZ ✅.
- **Kobeni**: la miedosa (155 cm, AniList); su **coche** quedó 4.º en la
  encuesta de VIZ (¡un coche!) ✅ ([VIZ](https://www.viz.com/blog/posts/chainsaw-man-popularity-poll-results-august-2022)),
  y también 7.º y 15.º en las encuestas oficiales de Jump (§9).
- **Himeno**: la que quería ir al cine con Aki (ep. 7) ✅. Parche en un
  ojo, pelo corto verde menta (visto en el ep. 7, 7:06-7:10 ⚠️ un plano);
  175 cm (AniList). En el diseño original **iba a ser la hermana de Aki**
  ✅ (wiki, entrevista de Jump Festa 2022).
- **Kishibe**: «Soy el cazador de demonios más fuerte» (ep. 10, 11:01) ✅.
  194 cm, bebe de una petaca ✅ (AniList; wiki).
- **Demonio Ángel**: 6.º en la 3.ª encuesta (49.899 votos) ✅.

---

## 9 · ¿Quién es el más querido?

| Encuesta | 1.º | 2.º | 3.º | 4.º | 5.º | Fuente |
|---|---|---|---|---|---|---|
| **1.ª oficial** (Shōnen Jump, votos 22-feb a 8-mar-2020; 231.201 votos) | **Power** (35.268) | Makima (27.224) | Aki (25.704) | Reze (19.079) | Denji (18.302) | [NamuWiki: Power](https://namu.wiki/w/%ED%8C%8C%EC%9B%8C(%EC%B2%B4%EC%9D%B8%EC%86%8C%20%EB%A7%A8)), [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/ChainsawManMainCharacters) ✅ |
| **2.ª oficial** (feb-mar 2021; 620.045 votos) | **Aki** (88.868) | Makima (76.733) | Power (69.850) | Denji (59.130) | Reze (45.741) | [NamuWiki](https://namu.wiki/w/%EC%B2%B4%EC%9D%B8%EC%86%8C%20%EB%A7%A8), [CBR](https://www.cbr.com/chainsaw-man-popularity-poll-manga-character-deaths/) ✅ |
| **VIZ, en inglés** (agosto 2022) | **Power** | Denji | Aki | el coche de Kobeni | Kobeni | [VIZ](https://www.viz.com/blog/posts/chainsaw-man-popularity-poll-results-august-2022) ✅ (una fuente, pero es la oficial) |
| **3.ª oficial** (votos 17-sep a 21-oct-2025; resultado 3-dic-2025; 946.097 votos) | **Reze** (205.775) | Makima (101.454) | Aki (89.804) | Denji (66.175) | Power (61.256) | [X @goodschainsaw33](https://x.com/goodschainsaw33/status/1996464051682214118), [Record China](https://www.recordchina.co.jp/b965495-s25-c30-d0201.html), [ABEMA Times](https://times.abema.tv/articles/-/10192225), [página oficial de la votación](https://www.shonenjump.com/p/sp/2509/vote_chainsaw3/) ✅ |

En Corea se celebró que la votación volviera «después de 4 años»
([FMKorea](https://www.fmkorea.com/index.php?document_srl=8991884037&mid=best&cpage=5));
en China, Record China recogió comentarios como «劇場版のパワーが強すぎる»
(«la película tiene demasiada fuerza», con juego de palabras con Power) ([Record China](https://www.recordchina.co.jp/b965495-s25-c30-d0201.html)).
Hay también una lista de fans en X que no coincide con las oficiales
([@SpyGGhetti](https://x.com/SpyGGhetti/status/1978907742807949530)): **no
la uso** ⚠️.

**Segunda pasada: las tablas completas** salen del wikitext de
[Popularity Polls](https://chainsaw-man.fandom.com/wiki/Popularity_Polls)
en la wiki, cruzado con TV Tropes ✅. Del 6.º al 10.º:
- 1.ª: Ángel 13.374 · **el coche de Kobeni 9.878** · Kobeni 9.580 ·
  Pochita 9.527 · Hirofumi Yoshida 8.593. Kishibe, 17.º (2.283).
- 2.ª: Yoshida 32.161 · Ángel 27.761 · Himeno 27.612 · Pochita 26.722 ·
  Kobeni 22.862. El coche de Kobeni volvió a salir (15.º, 9.269) y
  «**Makima (menú de cerdo al jengibre)**» quedó 14.º con 12.151 votos:
  un gag del propio Fujimoto ✅.
- El más votado se lleva **un manga de una página** dibujado por Fujimoto:
  Aki (con Himeno) en la 2.ª y Reze (con Denji) en la 3.ª ✅.

**Favoritos de usuarios en AniList** (otra medida, de fans de todo el
mundo): Makima 22.272 · Denji 21.029 · Power 20.542 · Aki 14.745 · Reze
10.348 · Pochita 5.431 · Kobeni 5.303 ✅
([AniList](https://anilist.co/anime/127230)).

**El autor también tiene favorito, y cambia**: en 2020 dijo que era Reze;
en 2021, que Denji la había reemplazado ✅ (wiki, páginas de Reze y
Denji).

**Conclusión**:
- **Hoy, Reze**: ganó con **el doble de votos** que la segunda, justo
  cuando se estrenó la película.
- **De siempre, Power**: ganó la primera y la de los lectores en inglés,
  y es la de los memes.
- **El protagonista, Denji, nunca ganó.** Aquí sí pasa lo que advertía el
  dueño: el secundario es más querido.
- **Para este canal, Makima**: es 2.ª en las tres oficiales y 1.ª en
  AniList, y **la escena del cine es suya**. La propuesta es Makima con Denji en la sala, y Reze
  o Power como segunda voz (§19).

---

## 10 · Doblaje latino

**Sí hay doblaje latino**: la serie (Crunchyroll; el reparto se anunció
en octubre de 2022 ✅, fecha exacta del estreno doblado ⚠️) y la
película (cines de Latinoamérica, **23-oct-2025**, Sony Pictures).

| Personaje | Voz latina | Estado | Fuentes |
|---|---|---|---|
| Denji | **Emilio Treviño** | ✅ | [Universo Nintendo](https://universo-nintendo.com.mx/2022/10/30/chainsaw-man-doblaje-espanol-latino-emilio-trevino-gaby-gris-erika-langarica/), [El Comercio](https://elcomercio.pe/saltar-intro/streaming/series/chainsaw-man-ya-se-acaba-pero-el-doblaje-continua-conversamos-con-los-actores-de-denji-y-makima-gaby-gris-emilio-trevino-crunchyroll-mappa-denji-noticia/), [Doblaje Wiki: Denji](https://doblaje.fandom.com/es/wiki/Denji) |
| Makima | **Gaby Gris** | ✅ | Universo Nintendo, El Comercio, [GamerFocus](https://www.gamerfocus.co/anime/chainsaw-man-entrevista-con-la-voz-de-denji-makima-y-el-director-de-doblaje-para-latinoamerica/) |
| Power | **Erika Langarica** | ✅ | Universo Nintendo, [Código Espagueti](https://codigoespagueti.com/noticias/anime/crunchyroll-revela-elenco-principal-voces-en-espanol-latino-para-chainsaw-man/), [LevelUp](https://www.levelup.com/noticias/707306/Crunchyroll-confirma-el-reparto-de-voces-en-espanol-de-Chainsaw-Man) |
| Aki | **Arturo Cataño** | ✅ (nombre); grafía ⚠️ | Código Espagueti, LevelUp, [3DJuegos](https://www.3djuegos.lat/anime/chainsaw-man-confirma-su-elenco-voces-para-doblaje-espanol-latino). La primera pasada escribió «Cartaño»; [AniList](https://anilist.co/character/137081) escribe «Cataño» y se deja así. Mirar la grafía en los créditos |
| Reze (película) | **Jessica Ángeles** | ✅ | [YouTube: «Jessica Ángeles, voz de Reze», ConCo](https://www.youtube.com/shorts/2CrGzJ6Mwdg), [TikTok @jezzylush: nominada en los Crunchyroll Awards por Reze](https://www.tiktok.com/@jezzylush/video/7626946398621027604) |
| Kobeni | **Paola García** (serie y película) | ✅ | [Doblaje Wiki (wikitext)](https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Chainsaw_Man), [Doblaje Wiki: película](https://doblaje.fandom.com/es/wiki/Chainsaw_Man_%E2%80%93_La_Pel%C3%ADcula:_Arco_de_Reze), [AniList](https://anilist.co/character/144594) |
| Himeno | **Mireya Mendoza** (un loop del ep. 7 lo dobló Erika Langarica). Su voz la **propusieron los fans**: el director les dejó sugerir | ✅ | Doblaje Wiki (wikitext, con su nota), [AniList](https://anilist.co/character/144596) |
| Kishibe | **Víctor Franco** | ✅ | Doblaje Wiki (wikitext), [AniList](https://anilist.co/character/144593) |
| Beam | **Iván Bastidas** | ✅ | Doblaje Wiki (wikitext), [AniList](https://anilist.co/character/157232) |
| Ángel | **Luis Leonardo Suárez** («Luigi Suárez» en los créditos de la película) | ✅ | Doblaje Wiki, serie y película |
| Hirokazu Arai | **Cuauhtemoc Miranda** | ✅ | Doblaje Wiki (wikitext), [AniList](https://anilist.co/character/174263) |
| Katana Man (Samurai Sword) | **José Arenas** | ✅ | Doblaje Wiki (wikitext), [AniList](https://anilist.co/character/157241) |
| Akane Sawatari | **Alondra Hidalgo** | ✅ | Doblaje Wiki (wikitext), [AniList](https://anilist.co/character/174264) |
| Michiko Tendo | **Wendy Malvárez** | ✅ | Doblaje Wiki (wikitext), [AniList](https://anilist.co/character/144595) |
| Yutaro Kurose | **Octavio Campos**, el propio director | ✅ | Doblaje Wiki (wikitext), [AniList](https://anilist.co/character/144592) |
| Pochita | **Amellalli Guevara** | ⚠️ (sólo AniList) | [AniList](https://anilist.co/anime/127230) |

Segunda pasada: con el wikitext completo de Doblaje Wiki y las fichas de
AniList ya **no queda ningún personaje con nombre sin voz latina**. Sólo
faltan papeles sin nombre en pantalla, que la propia Doblaje Wiki marca
«¿?».

- **Estudio**: **Audiomaster Candiani** (México) ✅ (resumen de búsqueda
  sobre [GamerFocus](https://www.gamerfocus.co/anime/chainsaw-man-entrevista-con-la-voz-de-denji-makima-y-el-director-de-doblaje-para-latinoamerica/)
  y [ANMTV](https://www.anmtvla.com/2022/10/chainsaw-man-crunchyroll-revela-las.html);
  la guía de cuadros del proyecto dice lo mismo desde Doblaje Wiki). La
  película, también **Audiomaster Candiani** ✅ (ficha propia de la
  película en Doblaje Wiki, segunda pasada). Estudio colaborador de la
  serie: **Bita Dubbing Studios** ⚠️ (sólo Doblaje Wiki).
- **Director de doblaje**: **Tavo (Octavio) Campos** ✅ (GamerFocus,
  Doblaje Wiki). Dice que se ciñeron al guion original; Treviño dice que
  odia «que el doblaje suene a doblaje» ✅ (GamerFocus).
- **Traducción**: Antonio Valdez (serie y película), el de los subtítulos
  de Crunchyroll, que ya había traducido el manga ✅ (Doblaje Wiki, fichas
  de la serie y de la película). **Adaptación**: **Jaime Chaparro** ✅
  (mismas dos fichas).
- **Cuándo se grabó**: la serie, de **octubre de 2022 al 4 de enero de
  2023** (lo dijo Tavo Campos en su
  [X/Twitter](https://twitter.com/TavoCampos80/status/1610785685354708994),
  citado por Doblaje Wiki) ✅; la película, en **septiembre de 2025** ✅
  (Doblaje Wiki).
- **Premio**: **Emilio Treviño ganó «Mejor actuación de voz» en español
  latino** por Denji en los **8.º Crunchyroll Anime Awards** (2024) ✅
  ([Mediotiempo](https://www.mediotiempo.com/otros-mundos/emilio-trevino-gana-premio-en-los-crunchyroll-anime-awards-2024-japon-conoce-lista-completa-ganadores),
  [Plano Informativo](https://planoinformativo.com/987889/mexicano-gana-premio-en-los-anime-awards-2024/amp/espectaculos/),
  [Wikipedia: 8th Crunchyroll Anime Awards](https://en.wikipedia.org/wiki/8th_Crunchyroll_Anime_Awards)).
  El mismo año ganó Ryan Colt Levy en inglés por el mismo Denji. Para un
  servidor de doblaje es el mejor gancho: **el doblaje latino de esta
  serie ganó un premio internacional**.
- **Entrevistas**: [La Verdad Noticias](https://hls.laverdadnoticias.com/anime/Entrevista-al-elenco-en-espanol-latino-de-Chainsaw-Man-20221121-0084.html),
  [Hola: Emilio Treviño](https://www.hola.com/us-es/entretenimiento/20251205871420/emilio-trevino-actor-doblaje-timothee-chalamet-chainsawman/).
- **Voces japonesas** (para comparar): Denji **Kikunosuke Toya**, Makima
  **Tomori Kusunoki**, Aki **Shōgo Sakata**, Power **Fairouz Ai** ✅
  ([Oricon](https://www.oricon.co.jp/news/2244818/full/),
  [Dengeki Online](https://dengekionline.com/articles/143906/)); Reze
  **Reina Ueda** ✅ ([PASH! PLUS](https://www.pashplus.jp/anime/265805/),
  [Oricon](https://www.oricon.co.jp/news/2443674/full/)).

### El estreno en Latinoamérica (lo que la gente del canal fue a ver)
- La película llegó a los cines de Latinoamérica el **23-oct-2025**, en
  **doblaje latino y en japonés con subtítulos**, en Cinépolis y Cinemex;
  fue **n.º 1 en México** ✅
  ([El Financiero](https://www.elfinanciero.com.mx/entretenimiento/2025/10/28/chainsaw-man-el-arco-de-reze-lidera-record-de-taquillas-en-eu-como-le-fue-en-su-debut-en-mexico/),
  [Récord](https://www.record.com.mx/historia/chainsaw-man-arco-de-reze-ya-tiene-fecha-de-estreno-en-mexico-todo-lo-que-debes-saber-2025101310182025636),
  [El Informador](https://www.informador.mx/entretenimiento/chainsaw-man--la-pelicula-arco-de-reze-lo-que-debes-saber-de-la-nueva-entrega-20251027-0090.html),
  [Diario de México](https://www.diariodemexico.com/escena/chainsaw-man-el-arco-de-reze-lidera-la-taquilla-mundial),
  [Somos Kudasai](https://somoskudasai.com/noticias/chainsaw-man-ya-tiene-fechas-en-latinoamerica/)).
- Primer fin de semana: **3,3 millones de dólares en Latinoamérica**, 1,3
  de ellos en México ⚠️ (una fuente, El Financiero según el resumen).
- En Japón: estreno el **19-sep-2025**, n.º 1 dos fines de semana
  seguidos ✅ ([Anime!Anime!](https://animeanime.jp/article/2025/09/30/92917.html),
  [Wikipedia](https://en.wikipedia.org/wiki/Chainsaw_Man_%E2%80%93_The_Movie:_Reze_Arc));
  más de **10.700 millones de yenes** (10.740 millones según Oricon;
  10.810 millones a 30-mar-2026 según la Wikipedia china) ✅
  ([Oricon](https://www.oricon.co.jp/news/2443674/full/),
  [Wikipedia en chino](https://zh.wikipedia.org/zh-cn/%E5%8A%87%E5%A0%B4%E7%89%88_%E9%8F%88%E9%8B%B8%E4%BA%BA_%E8%95%BE%E6%BD%94%E7%AF%87)).
  En todo el mundo, **191,4 millones de dólares** ⚠️ (Wikipedia, según
  el resumen).
- **Ficha en español** de la película:
  [Wikipedia en español](https://es.wikipedia.org/wiki/Chainsaw_Man_-_la_pel%C3%ADcula:_arco_de_Reze),
  [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Chainsaw_Man_%E2%80%93_La_Pel%C3%ADcula:_Arco_de_Reze),
  [The Dubbing Database](https://dubdb.fandom.com/wiki/Chainsaw_Man_-_La_Pel%C3%ADcula:_Arco_de_Reze),
  [JustWatch México](https://www.justwatch.com/mx/pelicula/chainsaw-man-the-movie-reze-arc).

### Frases del doblaje con fuente
- Power, ep. 4: «**Duelo a muerte con cuchillos**», guiño al famoso error
  de *Yu Yu Hakusho* ✅ (de la guía de cuadros del proyecto).
- Clip oficial «**Ahuevooooo**» ✅ ([Crunchyroll en Español](https://www.youtube.com/watch?v=3fW7Heo1qvs), de la guía).
- Clip «**¡Ah, cómo chiflas, Kobeni!**» ✅ ([YouTube](https://www.youtube.com/watch?v=8fIlH-g4p_Y)).
  Doblaje Wiki la transcribe «**Ah, cómo chingas**» (Denji a Kobeni,
  ep. 11) ⚠️: el título del clip y la wiki no coinciden; hay que oírla.
- **Más frases, con episodio** (Doblaje Wiki, «Datos de interés», leído en
  el wikitext) ✅:
  - Ep. 4, Makima a Denji: «**Qué lata tanto papeleo, ¿verdad?**»
  - Ep. 4, Denji a Arai al soltarlo: «La concha de tu madre» (grosería:
    no va en la lámina).
  - Ep. 8, Denji a Himeno: «**Pues no, mi ciela, ya quisieras**» (un meme).
  - Ep. 10, Denji: «Ese mamagüevo viejo alcohólico» (grosería).
  - Ep. 12, Kobeni a Aki, sobre por qué no renuncia: «**Porque aún no han
    depositado el aguinaldo**».
- **Detalles de adaptación** ✅ (Doblaje Wiki): «**Pochita**» se dice con
  acento en la **i** (en japonés, en la o); «**Devil Hunter**» se queda en
  inglés; a Samurai Sword lo llaman «**Katana Man**»; Emilio Treviño dobla
  a Denji también de niño.
- El doblaje lleva **muchas groserías** de varios países ✅ (Doblaje Wiki,
  guía). **No van en la lámina**: el canal es para todos.
- Clips para oír las voces: [Makima, cap. 1](https://www.youtube.com/watch?v=smTzh5VSems),
  [Power](https://www.youtube.com/watch?v=-fAA_0L-lhI),
  [Denji, cap. 1](https://www.youtube.com/watch?v=-ILSKQGeRIw),
  [El trato de Power y Denji](https://www.youtube.com/watch?v=Ky83VhS92Y0),
  [El primer beso de Denji](https://www.youtube.com/watch?v=odtRpzPmcbY)
  (subidas de fans, minuto sin verificar).
- **No encontré** cómo dice Makima en latino la frase del cine («una de
  cada diez»). Lo que pongo en la lámina es **mi traducción** del japonés
  ⚠️. Si se quiere la frase exacta, hay que ver la película doblada en
  Crunchyroll: está allí desde el **30-abr-2026** ✅ (resumen de búsqueda
  sobre [El Universal](https://www.eluniversal.com.mx/espectaculos/la-pelicula-de-chainsaw-man-conquista-a-los-fans-del-anime-y-la-taquilla-global/)
  y sobre el canal de Crunchyroll en YouTube, [tráiler doblado](https://www.youtube.com/watch?v=_bGsoW3hKzw)).
- Un vídeo corto en español se titula «Denji dice que a **la señorita
  Makima** solo le gustan las malas películas?» ([YouTube Shorts](https://www.youtube.com/shorts/CovQhKQhjgk)):
  puede que en el doblaje Denji la llame «señorita Makima» ⚠️ (sólo el
  título; no lo oí).

---

## 11 · Música (y el cine dentro de la serie)

### 11.1 Serie (2022)
- **Opening: «KICK BACK», de Kenshi Yonezu** ✅
  ([Wikipedia: Kick Back](https://en.wikipedia.org/wiki/Kick_Back_(song)),
  [Chainsaw Man Wiki](https://chainsaw-man.fandom.com/wiki/Kick_Back)).
  Rock eléctrico y caótico. Lo dirigió y storyboardeó **Shingo
  Yamashita** ⚠️ (una fuente: [Anime Corner](https://animecorner.me/chainsaw-man-opening-references-a-bunch-of-classic-movies/)).
- **El opening es una cartelera**: más de 15 planos copian películas ✅
  ([Screen Rant](https://screenrant.com/chainsaw-man-every-movie-homage-reference-opening-theme/),
  [CBR](https://www.cbr.com/chainsaw-man-opening-movie-easter-eggs/),
  [Soap Central, en orden](https://www.soapcentral.com/anime/every-movie-reference-chainsaw-man-opening-explained-order),
  [NextShark, lado a lado](https://nextshark.com/chainsaw-man-opening-movie-references),
  [YouTube: análisis en español](https://www.youtube.com/watch?v=Atoh7mCIODw)):

| Plano del opening | Película |
|---|---|
| Makima cruza la calle delante de Aki, Denji y Power | *Reservoir Dogs* (1992) |
| Denji abraza a Pochita en un cementerio | *La masacre de Texas* |
| Kishibe apunta con una pistola | *Pulp Fiction* |
| Chainsaw Man contra el Hombre Katana | *Sadako vs. Kayako* |
| Alguien se quita un zapato | *No Country for Old Men* |
| Denji y Aki salen marcha atrás en coche | *Érase una vez en Hollywood* |
| El que frota la bola de bolos | *El gran Lebowski* |
| (según un TikTok) | *Goodbye, Eri*, del propio Fujimoto ⚠️ ([TikTok](https://www.tiktok.com/@kitotok2/video/7153336711722847490?lang=en)) |

Minuto exacto de cada plano dentro del opening: **sin verificar** plano
por plano. **Segunda pasada, visto completo** en el ep. 1 de Internet
Archive ([EP01CM.mp4](https://archive.org/details/ep-03-cm/EP01CM.mp4)) ✅:
- El ep. 1 empieza con un **prólogo sin música** (0:30-2:00: la choza, el
  bosque, los papeles de la deuda «-38,075,120», Pochita). **El opening
  entra en el 2:02**, no a los 34 s como decía un resultado de búsqueda.
- Planos de acción muy cortados (2:02-3:38), con **una sala de cine con
  público en 2:32-2:44**: el motivo «cine» ya está en el opening.
- Texto «KICK BACK» sobreimpreso (3:08-3:11); logo **チェンソーマン** a
  pantalla completa sobre negro con distorsión digital (3:41-3:44); cierre
  con Denji corriendo hacia cámara (4:05-4:20).
- Que cada plano copia la película **plano a plano** (no sólo el tema) lo
  confirma [Anime Herald](https://www.animeherald.com/2023/06/03/how-the-chainsaw-man-anime-adaptation-grounded-itself-in-filmic-realism/) ✅.

- **Un ending distinto en cada episodio (12)** ✅
  ([Anime Corner](https://animecorner.me/chainsaw-man-listed-with-12-ending-songs-aimer-tk-and-eve-among-performers/amp/),
  [Tokyo Otaku Mode](https://otakumode.com/news/63ad286fc6e6c0002752e273/Every-Single-Chainsaw-Man-Ending-Theme-Song!)):
  1 «CHAINSAW BLOOD» (Vaundy) · 2 «Time Left» (ZUTOMAYO) · 3 «Hawatari
  2-Oku Centi» (Maximum the Hormone) · 4 «Jōzai» (TOOBOE) · 5 «In the
  Back Room» (syudou) · 6 «Rendezvous» (Kanaria) · 7 «All Kinds of Kisses» (ano;
  en japonés «Chu, Tayōsei.» ⚠️ de memoria) · 8 «First Death» (TK) · 9 «Deep Down»
  (Aimer) · 10 «DOGLAND» (PEOPLE 1) · 11 «Violence» (Queen Bee) · 12
  «Fight Song» (Eve).
  Es una **canción** distinta por episodio; **animación de ending no
  tienen todos**:
  - **El ep. 1 no tiene animación de ending** ✅: de **24:00 a 24:16**
    sólo hay **texto blanco sobre fondo negro** (créditos), mientras suena
    «CHAINSAW BLOOD». Visto en el episodio de Internet Archive y
    confirmado por [CBR: «Every End Credit Sequence in Chainsaw Man
    Season 1, Explained»](https://www.cbr.com/every-end-credit-sequence-chainsaw-man-season-1-explained/).
    Son **créditos de cine**: encaja con el canal.
  - **El ep. 2 sí la tiene** («Time Left», 22:16-23:40,
    [EP02CM.mp4](https://archive.org/details/ep-03-cm/EP02CM.mp4)) ✅:
    siluetas en **verde oliva apagado con detalles dorados**, un
    **electrocardiograma que se aplana** (22:28-22:32), Tokio de noche,
    Denji tirado en el suelo mirando la tele solo.
- **Banda sonora**: **Kensuke Ushio** ✅ ([QJWeb](https://qjweb.jp/feature/81444/)).

### 11.2 Película (2025)
- **Opening «IRIS OUT»** (Kenshi Yonezu) y **ending «JANE DOE»** (Kenshi
  Yonezu con Hikaru Utada) ✅ (etiquetas #IRISOUT #JANEDOE del
  [X oficial](https://x.com/CHAINSAWMAN_PR/status/1974338691591274782);
  [ABEMA Times](https://times.abema.tv/en/articles/-/10188155)). En el
  subtítulo japonés, «IRIS OUT» entra en el **2:54** y «JANE DOE» en el
  **1:33:56** ✅.
- **Ushio** divide la película en tres partes: chico conoce a chica, la
  escuela de noche, y la gran batalla ✅. Las piezas que pide escuchar en
  una sala buena: **«our film»** (la del cine con Makima) y **«slow summer
  eve»** (el festival con Reze) ✅
  ([Natalie](https://natalie.mu/music/pp/chainsawman-reze03),
  [Lisani](https://www.lisani.jp/0000294153/),
  [Real Sound](https://realsound.jp/2025/10/post-2167153.html)). Otra
  pieza: «ジェーンは教会で眠った» («Jane durmió en la iglesia») ✅
  ([MANTANWEB](https://mantan-web.jp/article/20260131dog00m200008000a.html)).
- **Ambiente para la lámina**: el de «our film». Tranquilo, de sala a
  oscuras. **No** el rock de «KICK BACK».
- **Cada película de la cita tiene su propia música** (subtítulos de
  sonido del corte EN, segunda pasada) ✅: «[action music playing]» en la
  de peleas (7:44), «[viewers sniffling]» en el drama que hace llorar a la
  sala (8:32), «[classical music playing]» en la que «tenía buena música»
  (8:52). El proyector se oye girar antes de la última (9:21, subtítulo
  japonés «映写機の回る音»).
- **Tráiler de la serie visto completo** (Dailymotion,
  [x8dsw0h](https://www.dailymotion.com/video/x8dsw0h), 92 s) ✅: crédito
  de Fujimoto y logo de MAPPA (0:00-0:16), Power de perfil (0:20), ojos de
  Denji en primer plano (0:36), Chainsaw Man contra un demonio blanco con
  manchas rojas (1:12-1:24), staff y reparto en japonés (1:28).

### 11.3 El autor y el cine
- Fujimoto ve películas mientras dibuja (sólo animadas, porque las de
  imagen real lo distraen); cita *Sharknado*, *No Country for Old Men*,
  *Tiburón*, *Winnie the Pooh* ⚠️ (una fuente)
  ([Screen Rant](https://screenrant.com/chainsaw-man-anime-inspiration-tatsuki-fujimoto-disney-sharknado-pooh-bear/)).
- Ha recomendado en redes *Zigeunerweisen*, *Ceguera*, *Taps*, *El gran
  Lebowski*, *Sicario*, *Prisoners* y *The Wailing*, y su consejo a quien
  quiere ser mangaka fue: «**suscríbete a Netflix**» ⚠️ (una fuente)
  ([The New Manga Canon](https://vasamoto.wordpress.com/2020/09/09/some-nuggets-from-fujimoto-tatsuki-enthusiast-creator/)).
- Hay listas de fans con «las películas de Fujimoto» en Letterboxd
  ([1](https://letterboxd.com/idontrexxall/list/tatsuki-fujimoto-recommends/),
  [2](https://letterboxd.com/red_dlta/list/tatsuki-fujimoto-core/)).

---

## 12 · Vídeos

| Vídeo | Enlace | Qué sirve | Minuto |
|---|---|---|---|
| Tráiler oficial de la película | [YouTube](https://www.youtube.com/watch?v=Zz7Y0MT554k) | tono, luz, Reze | sin verificar |
| Tráiler doblado (Crunchyroll) | [YouTube](https://www.youtube.com/watch?v=_bGsoW3hKzw) | voces | sin verificar |
| Tráiler 2 doblado | [YouTube](https://www.youtube.com/watch?v=1kH7Ne3TcHM) | voces | sin verificar |
| Resumen de la serie (Crunchyroll) | [YouTube](https://www.youtube.com/watch?v=dZUkDVF16lM) | poses de la T1 | sin verificar |
| Análisis del opening, en español | [YouTube](https://www.youtube.com/watch?v=Atoh7mCIODw) | la cartelera del OP | sin verificar |
| «Todas las referencias de cine en la película» | [YouTube Shorts](https://www.youtube.com/shorts/S1aQSXsJGMI) | guiños de cine | corto |
| Clip «Ahuevooooo» (Crunchyroll en Español) | [YouTube](https://www.youtube.com/watch?v=3fW7Heo1qvs) | voz latina de Denji | sin verificar |
| Análisis del doblaje latino de la película | [YouTube](https://www.youtube.com/watch?v=Y8IpYCn31_s) | doblaje | sin verificar |
| Jessica Ángeles (Reze) en la ConCo | [YouTube Shorts](https://www.youtube.com/shorts/2CrGzJ6Mwdg) | actriz latina | corto |
| **Película completa, subtitulada en inglés** (Internet Archive, 1080p) | [rezearc](https://archive.org/details/rezearc) | **la cita del cine, vista** | **6:20-10:58** ✅ (§2.1b) |
| Temporada 1, 12 episodios (Internet Archive, audio japonés) | [ep-03-cm](https://archive.org/details/ep-03-cm) | opening, ending, poses | ep. 1: OP 2:02, créditos 24:00; ep. 2: ED 22:16, Power 19:20; ep. 7: Aki y Himeno 6:10-7:18 ✅ |
| Tráiler final del anime (Dailymotion) | [x8dsw0h](https://www.dailymotion.com/video/x8dsw0h) | tono de la T1 | Power 0:20, Denji 0:36, pelea 1:12 ✅ |
| Fandub latino «La Cafetería de Reze» (LATAM Fandub Studios) | [Dailymotion x9oi0k4](https://www.dailymotion.com/video/x9oi0k4) | comunidad hispana (§18E) | sin verificar |

**La escena que importa** (la cita en el cine) no tiene clip oficial
localizado: su minuto está en §2.1, **7:03-10:52 de la película**, según el
subtítulo. Un análisis la llama «el momento más profundo de toda la
historia»: la escena «trivial» que hace llorar a Denji es **una madre y
su hijo abrazándose** ⚠️ (una fuente: [Anime Fire](https://animefire.com/2025/11/10/the-best-scene-in-chainsaw-man-the-movie-the-reze-arc/)).
**Segunda pasada**: ahora sí se vio (corte EN de Internet Archive,
§2.1b). En la película de dentro se ven un **soldado joven con gorra y
tirantes** y una **mujer con pañuelo blanco** que se abrazan al final
(9:50). Cuadra con «una madre y su hijo», pero la imagen no lo dice ⚠️.
YouTube seguía pidiendo iniciar sesión: los enlaces de YouTube de esta
tabla quedan **sin verificar desde el servidor**, no caídos.

**TikTok**: tendencias con «IRIS OUT» y el «bang bang» ⚠️
([TikTok: trend song](https://www.tiktok.com/discover/chainsaw-man-trend-song),
[TikTok: bang bang](https://www.tiktok.com/en/trending/detail/bang-bang-chainsaw-man-song-goes-viral)).
No pude ver los vídeos: minuto sin verificar.

---

## 13 · Videojuegos de la franquicia

- **No hay todavía un videojuego propio publicado**. MAPPA anunció el
  **primer juego oficial para móvil** en su directo del 15.º aniversario
  (junio de 2026): gacha de personajes, con Denji, Makima, Power y la
  Seguridad Pública, un demonio nuevo (el **Demonio Cubo de Rubik**) y un
  tema de Maximum the Hormone. **Sin fecha** ✅
  ([Gaming on Phone](https://gamingonphone.com/news/mappa-reveals-first-official-chainsaw-man-game-for-mobile-more-details-coming-soon/),
  [Last Word on Gaming](https://lastwordongaming.com/2026/06/20/chainsaw-man-mobile-game/),
  [Game Rant](https://gamerant.com/chainsaw-man-video-game-trailer/),
  [Game8](https://game8.co/articles/release-dates/chainsaw-man-mobile-release-date-and-time)).
- Segunda pasada: el anuncio se confirma con fecha, **19-jun-2026**, gacha
  con apertura animada por MAPPA y modelos 3D propios, iOS y Android, sin
  fecha de salida ✅ ([Pocket Gamer](https://www.pocketgamer.com/chainsaw-man/mobile-game-announced/)).
- Por eso **no hay caja de diálogo de videojuego** que copiar, ni nada en
  The Cutting Room Floor.
- En Steam sale «**Boring Movies - Groovy Chainsaw Man**» (Fishagon LLC,
  5-nov-2024, 1 captura 1920×1080): **no es de la franquicia**, sólo
  comparte el nombre. No usar (lo trajo `recolectar.py` por coincidencia).

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen
- **«Guau» / «Woof»**: Makima trata a Denji como a un perro y le pide
  que ladre; los fans comentan «woof» bajo cualquier dibujo de Makima
  («Makima woofers») ✅ ([Know Your Meme: Makima](https://knowyourmeme.com/memes/makima)).
  En la serie: «sólo "sí" o "guau"» (ep. 2, 0:26) ✅.
- **El «Bang» de Makima** (mata con un gesto de pistola con la mano):
  plantilla de memes ⚠️ (sólo Know Your Meme). ⚠️ Es spoiler: no va.
- **El coche de Kobeni** (quedó 4.º en la encuesta de VIZ) y el **«Sad Cat
  Dance»** de Kobeni (el coche ✅ por VIZ y Know Your Meme; el baile ⚠️
  sólo Know Your Meme: [Know Your Meme: Kobeni](https://knowyourmeme.com/memes/kobeni-chainsaw-man)).
- **La broma de Denji y Power a Aki** ✅: según Fujimoto en Twitter, le
  **pusieron popó en la nariz** mientras dormía, la mañana antes del arco
  del Demonio de la Eternidad
  ([Know Your Meme](https://knowyourmeme.com/photos/2473105-chainsaw-man--2),
  [tuit citado por la wiki](https://twitter.com/nagayama_koharu/status/1590000772221394949),
  trivia de Aki).
- **El coche de Kobeni en las encuestas oficiales**: 7.º en la 1.ª (9.878
  votos) y 15.º en la 2.ª; y «Makima (menú de cerdo al jengibre)» 14.º:
  la propia revista se ríe del fandom ✅ (§9).
- **El destino de Kobeni**: iba a morir ella y no el Ángel. Fujimoto le
  preguntó a su editor, Shihei Lin, quién debía morir; el editor dijo
  Kobeni y **Fujimoto hizo lo contrario** ✅ (wiki, trivia de Kobeni).
  Para un post de trivia, no para la lámina.
- **Yutaro Kurose lo dobla el propio director del doblaje**, Octavio
  Campos ✅ (§10). Dato de trivia para el servidor.
- **Power**: «¡Inclínate ante mí!», mentir sin parar, su gata Nyako ✅.
- **Reze**: la «**Reze-loss**» al salir del cine ⚠️ (sólo Futaman); la
  **cabina de teléfono** de Jinbōchō, donde la gente deja flores ✅ (§5.2).
- **Pan con mermelada**: el sueño de Denji ✅ (ep. 1, 9:12).
- **El opening lleno de películas** ✅ (§11).
- **La cita del cine** ✅: hay fanfics con ese título (§4.3) y análisis
  que la ponen como la mejor escena de la película (§12).

### Qué NO hacer (lo que un fan notaría)
- **Ponerlo mono o limpio**: la serie es sucia, con sangre y colores
  apagados. Pero **tampoco demasiado lavado**: parte del fandom firmó una
  petición (más de 2.000 firmas) contra la serie de 2022 por sus colores
  **pálidos** y su realismo, que para ellos le quitaba fuerza y humor ✅
  ([ANN](https://www.animenewsnetwork.com/interest/2022-12-27/online-petition-to-redo-chainsaw-man-anime-gets-2000-signatures/.193391),
  [LevelUp](https://www.levelup.com/en/news/717321/They-dont-like-it-Chainsaw-Man-fans-open-petition-against-anime/)).
  Término medio: el de la película.
- **Spoilers**: nada de lo que Makima o Reze son de verdad, ni muertes.
  **El propio canal pide marcar spoilers**: la lámina debe dar ejemplo.
- **Makima gritando o riendo a carcajadas**: nunca. Sonríe apenas.
- **Power sin cuernos**, o Power callada y educada, o con **pupilas
  redondas** (son en aspa, roja y amarilla).
- **Butacas rojas de terciopelo**: las de シネマ座 son **mostaza/ámbar**
  (§5.3).
- **Makima con uniforme en la cita**: va de calle (§16). Y con pelo
  rosa claro si la lámina copia la película: ahí es **granate**.
- **Reze en la cita del cine**: la cita es con **Makima** (cap. 39).
- **Reze con otro color de pelo** (es morado) o **sin gargantilla**.
- **Frases con groserías del doblaje**: tienen fuente, pero el canal es
  de entrada general.
- **La motosierra en la lámina de un canal tranquilo**: Denji no necesita
  transformarse para ir al cine.

---

## 15 · Poses analizadas por personaje

Minutos de los subtítulos (§2). En la primera pasada **la postura se
describía de memoria o por el contexto de la frase ⚠️**. **Segunda
pasada**: las filas con ✅ se miraron en fotograma real (película y
episodios de Internet Archive; entre paréntesis, el minuto del corte EN
de la película, que va 15-20 s por detrás), y se añaden las poses de las
hojas de contacto (§3A), con enlace. Lo que sigue con ⚠️ no se ha visto
en imagen.

### Makima
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | Ep. 1, 23:03-23:50 | Agachada frente a Denji; le ofrece comida ⚠️ | **presentar** |
| 2 | Ep. 2, 0:21-0:28 | Le pone las reglas, tranquila ⚠️ | **explicar** una regla |
| 3 | Ep. 2, 5:20-5:32 | Le da udon con palillos: «di "a"» ⚠️ | cuidar, animar |
| 4 | Película, 6:25-6:40 | Lo invita a salir, sonriendo ⚠️ | **animar**, invitar |
| 5 | Película, 7:56-8:03 | Saliendo de la sala: «no tuvo gracia» ⚠️ | opinar |
| 6 | Película, 9:09-9:19 (EN 9:28) | Sentada en la butaca, **girada hacia Denji, mirada tranquila**: «una de cada diez» ✅ visto | **explicar / recomendar** (la mejor) |
| 7 | Película, 10:14-10:32 (EN 10:36, 1920×1080) | **De perfil, una lágrima cayendo, boca entreabierta**, el pelo granate le tapa parte de la cara ✅ visto | **pensar**, emoción |
| 8 | Película, 10:37-10:41 | A la salida: «valió la entrada» ⚠️ | **celebrar** (suave) |
| 9 | Opening | Cruza la calle al frente del grupo (*Reservoir Dogs*) ✅ | presentar (grupo) |
| 10 | [Makima Infobox](https://static.wikia.nocookie.net/chainsaw-man/images/7/7e/Makima_Infobox.png) (hoja 2, n.º 77) | De pie, de frente, **manos juntas delante**, uniforme ✅ | **presentar** |
| 11 | [Hoja 3, n.º 406](https://static.wikia.nocookie.net/chainsaw-man/images/c/c9/Makima_tells_Denji_the_type_she_likes.png) (anime, 1920×1080) | Sentada a una mesa, **mentón apoyado**, luz cálida ✅ | **explicar** |
| 12 | [Hoja 3, n.º 408](https://static.wikia.nocookie.net/chainsaw-man/images/f/f8/Makima_watching_Power_and_Denji_arguing.png) (anime, 1920×1080) | **Mejilla en la mano**, sonrisa leve, mira a Power y Denji ✅ | escuchar, **recomendar** |
| 13 | [Hoja 2, n.º 78](https://static.wikia.nocookie.net/chainsaw-man/images/1/1f/Reze_Arc_Illustration_%28min_daifuku%29.png) (min daifuku) | **Abraza a Pochita**, fondo blanco ✅ | **animar**, ternura |

### Denji
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | Ep. 1, 9:12 | En la choza con Pochita, soñando con pan ⚠️ | pensar |
| 2 | Ep. 2, 13:50-13:58 | Hace «el pan más poderoso» y lo muerde ⚠️ | **celebrar** |
| 3 | Película, 6:44-6:46 (EN 7:04) | «¡Bieeen!»: **ojos cerrados, sonrisa suave, los dos puños a la altura del pecho**. No son brazos arriba, como decía la primera pasada ✅ visto | **celebrar** (contenido) |
| 4 | Película, 6:57-7:01 | Esperando una hora antes; la ve llegar ⚠️ | **animar**, ilusión |
| 5 | Película, 7:33-7:52 | En la butaca, no entiende por qué ríe la sala ⚠️ | **pensar** |
| 6 | Película, 8:11-8:13 | Sorbe su bebida mientras todos lloran (se oye el sorbo) ✅ | humor |
| 7 | Película, 9:02-9:08 | «Todas me parecieron meh» ⚠️ | **explicar** (sincero) |
| 8 | Película, 10:05-10:14 (EN 10:25-10:36) | **De perfil, boca tapada con la mano**, ceño fruncido conteniendo el llanto, mira de reojo ✅ visto | **pensar**, emoción contenida |
| 9 | Película, 15:12-15:20 | El truco de la flor: «¡Tarán!» ⚠️ | **presentar** |
| 10 | Película, 17:36-17:43 | Cara de asco con el café ⚠️ | **regañar** (quejarse) |
| 11 | [Hoja 3, n.º 428](https://static.wikia.nocookie.net/chainsaw-man/images/a/a0/Reze_Arc_Countdown_Illustration_%28Masato_Nakazono%29.png) (Masato Nakazono) | **Gafas 3D de cine**, Pochita en brazos, marco de tira de película ✅ | **presentar** el canal |
| 12 | Hoja 1, n.º 18 (Jump Festa 2025) | Cuerpo entero en salto, fondo naranja ✅ | celebrar, acción |

### Power
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | Ep. 2, 19:16-19:21 (visto en 19:20, 1920×1080) | «¡Inclínate ante mí, humano!»: **primer plano, boca muy abierta con colmillos, cejas bajas, pupila en aspa roja y amarilla** ✅ visto | **presentar** (grito de entrada) |
| 2 | Ep. 2, 22:13 | «¡Es mérito mío!» ⚠️ | **celebrar** |
| 3 | Ep. 3, 1:28-1:31 | Discute con Denji ⚠️ | **regañar** |
| 4 | Ep. 4, 20:37-20:42 | Con su gata en brazos ⚠️ | ternura |
| 5 | Ep. 7, 7:43-7:58 | «¡Idea genial! ¡El Nobel es mío!» ⚠️ | **explicar**, celebrar |
| 6 | Película, 1:58-2:13 | Despierta a Denji a gritos ⚠️ | **regañar** |
| 7 | Película, 1:38:16-1:39:07 | Irrumpe en el café, pide la flor ⚠️ | celebrar, exigir |
| 8 | Tomo 2 del manga | **Sonriendo con una guadaña** ✅ ([Screen Rant](https://screenrant.com/best-chainsaw-man-covers-ranked/), [CBR](https://www.cbr.com/chainsaw-man-best-manga-covers/)) | presentar |
| 9 | Hoja 3, n.º 385-392 (anime, 1920×1080) | Riendo, orgullosa, lista para pelear, negándose a tirar de la cadena ✅ | **celebrar**, regañar |
| 10 | Hoja 1, n.º 21 (Jump Festa 2025) | Cuerpo entero, brazos arriba, fondo rosa ✅ | **celebrar** |

### Reze
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | Película, 14:04-14:46 | Entra corriendo a la cabina, ríe, luego llora ⚠️ | **presentar** |
| 2 | 15:42-15:52 | «¡Paró de llover! Ven al café» ⚠️ | **animar**, invitar |
| 3 | 17:26-17:47 | Con el café, se burla: «¡Qué niño!» ⚠️ | **regañar** con cariño |
| 4 | 18:01-18:14 | «Me llamo Reze. ¿Y tú?» ⚠️ | **saludar** |
| 5 | 24:15 | «¿¡No sabes leer kanji!?» ⚠️ | regañar |
| 6 | 27:52-27:58 | De maestra en la escuela: «¡Correcto! ¡Genio!» ⚠️ | **explicar / celebrar** |
| 7 | 32:34 | En la piscina: «Te enseño» ⚠️ | **animar** |
| 8 | 33:44-34:54 | El cuento de los ratones, mirando la lluvia ⚠️ | **pensar** |
| 9 | Tomo 6 del manga | Portada, ella en el centro ✅ ([Screen Rant](https://screenrant.com/best-chainsaw-man-covers-ranked/)) | presentar |

### Aki
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | Ep. 7, 6:22-6:48 | Comiendo con Himeno; dice que no dejará la caza ⚠️ | pensar, serio |
| 1b | Ep. 7, 7:14 (fotograma real) | De pie, **comisura levantada en una sonrisa leve, mirada de lado**; traje (verde oliva por la luz), camisa blanca, corbata negra ✅ visto | **explicar**, complicidad |
| 1c | Ep. 7, 7:06-7:10 | **Himeno**: primer plano de un solo ojo (el otro, bajo el parche), pelo corto verde menta, mirada de lado ⚠️ (un plano) | personaje secundario |
| 2 | Tomo 4 del manga | Portada, mirada azul intensa ✅ ([Screen Rant](https://screenrant.com/best-chainsaw-man-covers-ranked/)) | presentar |
| 3 | Opening | En el grupo que cruza la calle ✅ | presentar (grupo) |

---

## 16 · Vestuario (hex medidos en la segunda pasada)

**Segunda pasada**: los colores se **midieron con Pillow y `estilo.py`**
sobre los **diseños de personaje del arco de Reze** (arte plano de MAPPA,
en la wiki) y sobre fotogramas de la película. Ya no salen de guías de
fans. Los diseños:
[Denji](https://static.wikia.nocookie.net/chainsaw-man/images/0/0a/Denji_Chainsaw_Man_Reze_Arc_anime_design.png) 694×953 ·
[Makima](https://static.wikia.nocookie.net/chainsaw-man/images/5/54/Makima_Reze_Arc_anime_design.png) 514×857 ·
[Power](https://static.wikia.nocookie.net/chainsaw-man/images/c/c3/Power_Reze_Arc_anime_design.png) 529×881 ·
[Aki](https://static.wikia.nocookie.net/chainsaw-man/images/c/cb/Aki_Reze_Arc_anime_design.png) 583×972 ·
[Reze](https://static.wikia.nocookie.net/chainsaw-man/images/8/8a/Reze_Reze_Arc_anime_design.png) 517×862.

| Personaje | Ropa icónica | Colores medidos | Accesorios, peinado |
|---|---|---|---|
| Makima | Camisa, corbata negra, pantalón oscuro, chaqueta o gabardina ✅ | camisa `#F0EFE6`, pantalón `#2F393A`, zapato marrón `#422313` ✅ | Trenza. Pelo: diseño plano `#CF4F48`; **en la película se ve granate `#4C201F`** (fotograma de día, 6:52); en la serie de TV, rosa salmón `#D3978F` (guía de fans). Ojos con anillos ámbar `#E6C873` ⚠️ (guía de fans) |
| Denji | Traje de la Seguridad Pública: camisa, corbata negra floja, pantalón oscuro ✅ | camisa `#EDEDE3`; hoja de la sierra `#A8B2B8` ✅ | Pelo rubio dorado `#E1B760`, piel `#F2C89E` (fotograma 7:04) ✅; cordón de arranque en el pecho ✅ |
| Power | Traje de la Seguridad Pública; ropa de casa holgada ⚠️ | camisa `#F0EFE7`, pantalón `#30393B` ✅ | Pelo (diseño) `#E09975`; cuernos rojos `#C3544B` ⚠️ (guía de fans); **pupilas en aspa roja y amarilla** ✅ |
| Aki | Traje oscuro, camisa, corbata ✅ | traje `#30393B` ✅ | Pelo `#27323F` (azul casi negro), **moño alto**, katana, piercings ✅ |
| Reze | Blusa y shorts; la primera vez, camiseta holgada con campana y mochila ✅ | blusa `#EDE9F1`, shorts `#323037` ✅ | Pelo `#3F395E` (morado azulado oscuro), ojos verdes `#3FA66B` (propuesto ⚠️), **gargantilla negra** ✅ |

**Hallazgo medido** ✅: la camisa «blanca» del uniforme **no es blanco
puro**: sale `#EDEDE3` / `#F0EFE6` / `#F0EFE7` en tres personajes (crema
muy pálido). El pantalón y el traje **no son negros**: `#2F393A` /
`#30393B`, un **gris pizarra azulado**. Antes la biblia daba `#F2F0EA` /
`#1E1E1E` (propuestos). Los tejidos del uniforme son **lisos**: sin
cuadros, rayas ni lunares ✅ (visto en los 5 diseños).

**Lo «icónico» que todos reconocen**: la **camisa con corbata negra** de
la Seguridad Pública (Makima, Denji, Aki), la **trenza** de Makima, los
**cuernos** de Power y la **gargantilla** de Reze. La tabla de peinados y
accesorios se comprobó mirando los 5 diseños y los fotogramas de la hoja 3
✅.

**En la cita del cine** (segunda pasada, manga cap. 39,
[viñeta](https://static.wikia.nocookie.net/chainsaw-man/images/7/7c/Makima_during_her_date_with_Denji.png)):
**Makima no lleva uniforme**. Lleva **cárdigan claro de botones** sobre un
vestido, **falda o vestido oscuro por la rodilla**, **medias oscuras**,
**zapatos planos oscuros** y un **bolso de mano pequeño** ✅ (visto; es
blanco y negro, sin hex). **Denji**: en las viñetas de cuerpo entero no
lleva el uniforme completo con corbata ⚠️ (una fuente); su ropa exacta no
se ve (casi todo son primeros planos).

---

## 17 · Paisajes y fondos de pantalla

- **Tokio, 1997** (alternativo) ⚠️: calles normales, tiendas pequeñas,
  lluvia de verano, cigarras (se oyen en la película, 18:38 ✅).
- **Sitios de la película con hora y luz** (subtítulos + blogs de §5.2):
  - Sala de cine: **de día**, pero dentro a oscuras; salen **de noche**
    (planean ver películas «hasta las 12») ✅.
  - Cabina de teléfono de Jinbōchō: **tormenta de verano**, luego escampa ✅.
  - Café Futamichi: **tarde**, cigarras ✅.
  - Escuela y piscina: **noche** ✅.
  - Festival: **noche**, fuegos artificiales ✅.
- **Área de descanso de carretera** (ep. 2, 5:30): **atardecer**, cielo
  malva, montañas moradas ✅ (visto).
- **Fondos de pantalla de fans en Wallhaven** (tamaño real de su API,
  segunda pasada) ✅:
  - [Makima, 3840×2160](https://w.wallhaven.cc/full/gp/wallhaven-gpjyvl.png),
    el más guardado (♥866), subido por 性感阿离, origen
    [Pixiv 91666528](https://www.pixiv.net/en/artworks/91666528).
  - [Makima con calavera, 3557×1949](https://w.wallhaven.cc/full/9d/wallhaven-9dm55k.jpg),
    ♥644, origen [@shogo_matsuo](https://twitter.com/shogo_matsuo/status/1600151754838245377/photo/1).
  - [Denji, Power y Aki con gatos y una PlayStation, 2762×1758](https://w.wallhaven.cc/full/o5/wallhaven-o5dj1p.jpg),
    ♥502, subido por mediocreman (origen sin dato). **Escena de casa: sirve
    para una lámina 2.**
  - [Reze con flores, 2526×3568](https://w.wallhaven.cc/full/5g/wallhaven-5gwm39.jpg),
    ♥437, arte de Jenmin12, origen [Pixiv 102441991](https://www.pixiv.net/artworks/102441991).
  - [Paisaje, 5000×2167](https://w.wallhaven.cc/full/kx/wallhaven-kxz1p1.jpg)
    (jrmnt) y [4096×2691](https://w.wallhaven.cc/full/3l/wallhaven-3l6xw6.jpg)
    (drobbe, origen [Pixiv 104580093](https://www.pixiv.net/en/artworks/104580093)):
    los de más resolución.
- **Alpha Coders** (segunda pasada: la página ya abre) ✅: varios en
  **3840×2160**, uno en **5120×2880** y otro en **3600×2400** (tamaños en
  el HTML de la página); autor confirmado en dos: **Jesus Avila**. El
  enlace directo de cada imagen no carga sin JavaScript ⚠️: abrirlo en el
  PC.
- **Otros sitios de fans** (primera pasada; autor y tamaño en cada página
  ⚠️):
  [Alpha Coders 4K](https://alphacoders.com/chainsaw-man-4k-wallpapers),
  [Alpha Coders](https://alphacoders.com/chainsaw-man-wallpapers),
  [4K Wallpapers](https://4kwallpapers.com/chainsaw-man),
  [WallpaperFlare: cementerio](https://www.wallpaperflare.com/chainsaw-man-tatsukifujimoto-mappa-anime-cemetery-4k-wallpaper-ygrwl),
  [WallpaperFlare: búsqueda](https://www.wallpaperflare.com/search?wallpaper=chainsaw+man).
  **Oficiales**: los visuales de la película de §3.1.

---

## 18 · Guía para generar con IA (Firefly, Canva)

> Sólo si el dueño la quiere usar. Esta investigación **no generó ninguna
> imagen**. Todo lo de abajo sale de las secciones de la biblia (con su
> fuente allí). Segunda pasada: rehecha con los colores medidos, las
> etiquetas de Danbooru y las frases reales.

### 18.1 Para una IA de imagen

**Rasgos que nunca cambian** (entre comillas, las etiquetas de Danbooru
que más se repiten al dibujar a cada uno; son el vocabulario que entienden
las IA de imagen, de `datos-imagen.md`):
- **Makima**: trenza única, mechones a los lados, ojos ámbar con **anillos
  concéntricos**, camisa crema metida en el pantalón, corbata negra,
  sonrisa leve, quieta. Pelo **granate** si copia la película, rosa salmón
  si copia la serie. «red_hair, braided_ponytail, single_braid, sidelocks,
  ringed_eyes, yellow_eyes, white_shirt, collared_shirt, black_necktie,
  black_pants, shirt_tucked_in, formal_clothes, closed_mouth, smile».
- **Denji**: pelo rubio corto y despeinado, **dientes afilados**, corbata
  floja, mangas remangadas, cordón en el pecho. «blonde_hair,
  short_hair, sharp_teeth, white_shirt, black_necktie,
  sleeves_rolled_up, open_mouth, tongue_out».
- **Power**: pelo largo rubio rosado con mechón entre los ojos, **dos
  cuernos rojos**, colmillos, **pupilas en aspa**. «long_hair,
  red_horns, demon_horns, cross-shaped_pupils, symbol-shaped_pupils,
  sharp_teeth, hair_between_eyes, open_mouth».
- **Reze**: pelo morado oscuro por los hombros, ojos verdes, **gargantilla
  negra**, blusa sin mangas con lazo al cuello. «purple_hair,
  green_eyes, black_choker, sleeveless_shirt, neck_ribbon». **No usar**
  «grenade_pin»: es spoiler.

**Paleta** (medida, §5.3 y §16):
- Uniforme: camisa `#EDEDE3`-`#F0EFE7` (crema, no blanco), traje
  `#2F393A`-`#30393B` (gris pizarra, no negro).
- Pelo de Makima en la película `#4C201F`; Denji `#E1B760`; Aki `#27323F`;
  Reze `#3F395E`.
- Sala de シネマ座: negro `#020202`, penumbra oliva `#323124`, butacas
  `#544A36`/`#7C6D4A` (mostaza/ámbar), piel iluminada `#C2B4A2`.
- Película de dentro (verde azulado): `#415855`, `#7A8E87`.

**Línea y sombreado** (§18A):
- **Estilo anime** (lo más útil para el canal): línea fina, sombreado
  plano de 2-3 tonos, colores **apagados y naturalistas**, luz de cámara,
  **grano de película** fino, **brillo suave alrededor de las luces**,
  desenfoque de fondo. Un tinte de color complementario por plano
  (naranja sobre azul) que baja contraste y saturación.
- **Estilo manga**: línea **gruesa, suelta, «sucia»**, negros sólidos a
  pincel, **rayado cruzado** en vez de tramas; poca trama de puntos.

**Luz**: en la sala, **todo oscuro menos las caras**; el haz del
proyector, **blanco cálido con un halo verde-violeta**; la pantalla ilumina
de frente. Fuera, tarde de verano o noche de ciudad.

**Encuadre**:
- Formato ancho, **franjas negras de cine**, cámara a la altura de los
  ojos o **baja, como sentado** (el «plano tatami» de Ozu que usa la serie).
- **Desde atrás de las butacas**: el público de espaldas y simple, los
  protagonistas con detalle (así está dibujada la viñeta del cap. 39).
- Para emoción: **primer plano de perfil** (Makima llorando, 10:36).

**Palabras que ayudan**: «1997 Tokyo», «small old movie theater», «rows of
worn mustard velvet seats», «warm projector beam with subtle chromatic
halo», «faces lit by the screen», «seen from behind the seats»,
«cinematic still, letterbox», «35mm film grain», «muted naturalistic
colors», «complementary color grading», «soft glow around lights»,
«shallow depth of field», «flat cel shading», «seinen anime», «background
audience drawn simply».

**Palabras que lo estropean**: «cute», «chibi», «pastel», «sparkles»,
«glossy», «3D render», «neon», «red velvet seats» (son mostaza), «pink
hair» para la Makima de la película, «gore» y «chainsaw» (en este canal),
«grenade» (spoiler de Reze), «anime eyes sparkling».

**Qué imágenes usar de referencia** (de las encontradas):
- **Estilo y tono de cine**: hoja 3, n.º 428 (Denji con gafas 3D y
  Pochita en una tira de película,
  [original](https://static.wikia.nocookie.net/chainsaw-man/images/a/a0/Reze_Arc_Countdown_Illustration_%28Masato_Nakazono%29.png)).
- **Sala y composición**: la viñeta del cap. 39
  ([movie date](https://static.wikia.nocookie.net/chainsaw-man/images/9/9f/Denji_and_Makima%27s_movie_date.png))
  y el fotograma de 7:44 de la película (sala de espaldas).
- **Color de anime**: los diseños del arco de Reze (§16) y la hoja 3,
  n.º 393-408 (Makima) y 385-392 (Power).
- **Pose**: §15, Makima n.º 6, 7, 11 y 12; Denji n.º 3 y 8.
- **No usar** fan art ni wallpapers de fans como referencia de estilo.
- Si la IA no acepta el nombre del personaje, **describir los rasgos** de
  arriba sin el nombre.

**Vocabulario de expresiones** (para que la IA entienda cada gesto):
- La serie **casi no usa** gotas de sudor, venas de enfado ni fondos de
  emoción: la emoción va **en la cara, con luz realista**. Es de lo que
  más la distingue de otros shōnen.
- Las marcas propias están en los ojos y la boca: **anillos** en los ojos
  de Makima, **aspas** en los de Power, **dientes de sierra** en Denji y
  Power, lengua fuera en Denji.
- **Llanto**: Makima, una sola lágrima y boca entreabierta, en silencio;
  Denji, mano tapando la boca, ceño fruncido.
- **Alegría**: Denji, ojos cerrados y puños al pecho; Power, boca abierta
  enorme y colmillos.
- El único «chibi» oficial son ilustraciones de humor sueltas, como la de
  Aya Yamamoto con Power y «パワー!!» en trazo suelto (hoja 2, n.º 51). No
  es el tono de la serie.

### 18.2 Para una IA de texto (sus diálogos, en su voz)

**Reglas generales**
- Frases **cortas y secas**. Mucho subtítulo de cine, poco globo.
- El humor sale del **contraste**: algo tierno dicho con cara seria, o
  algo brutal dicho como si nada.
- **Makima** nunca grita ni usa signos dobles. **Denji** y **Power** sí:
  «¡¿…?!», «¡Bieeen!», alargando vocales.
- Groserías: el doblaje latino tiene muchas (§10), pero **no van en la
  lámina**.
- Onomatopeyas: en el manga, **katakana dibujadas a mano, grandes**, en las
  peleas (hoja 1, n.º 28-43). En un canal tranquilo, sólo «**Guau**» y el
  **ruido del proyector**.
- Makima llama a los demás «**Denji-kun**», «**Power-chan**».
- Power habla de sí misma como una **anciana** («ワシ», «〜じゃ»); cómo lo
  adaptó el latino **no lo encontré** ⚠️.

**Frases reales por emoción** (traducción del japonés de la película o de
los subtítulos de Netflix, salvo las marcadas «latino»):

| Emoción | Quién | Frase | Dónde |
|---|---|---|---|
| Alegre | Denji | «¡Bieeen!» | película, 6:44 |
| Alegre | Power | «¡Pa-pa-pa-Power! ¡Ya volví!» | película, 1:38:20 |
| Alegre | Reze | «¡Correcto! ¡Genio!» | película, 27:58 |
| Alegre | Power | «¡Tuve una idea genial! ¡El Nobel es mío!» | ep. 7, 7:43 |
| Enfadado o regañando | Power | «¡Inclínate ante mí, humano! ¡Mi nombre es Power!» | ep. 2, 19:16 |
| Enfadado o regañando | Makima | «No me gustó que quisiera hacernos llorar a la fuerza.» | película, 8:08-8:32 |
| Enfadado o regañando | Reze | «¿¡No sabes leer kanji!?» | película, 24:15 |
| Enfadado o regañando | Denji | «Sabe a alcantarilla.» | película, 17:40 |
| Explicando | Makima | «Hoy, desde ahora hasta las 12 de la noche, vamos de sala en sala y vemos películas sin parar.» | película, 7:16 |
| Explicando | Makima | «Yo también encuentro una buena de cada diez. Pero esa una me ha cambiado la vida.» | película, 9:09 |
| Explicando | Makima | «Qué lata tanto papeleo, ¿verdad?» (latino) | ep. 4 |
| Explicando | Kobeni | «Porque aún no han depositado el aguinaldo.» (latino) | ep. 12 |
| Animando | Makima | «¿Mañana, en tu día libre, tenemos una cita?» | película, 6:25 |
| Animando | Reze | «¡Paró de llover! Ven al café.» | película, 15:42 |
| Animando | Reze | «Te enseño.» | película, 32:34 |
| Animando | Himeno | «Podemos ir al cine de vez en cuando después del trabajo.» | ep. 7, 6:22 |
| Triste | Denji | «¡Es una escena que no importa nada…! ¡Que no me vea Makima-san!» | película, 10:05 |
| Triste | Denji | «¿Usted cree que yo tengo corazón?» | película, 10:44 |
| Triste | Makima | (no dice nada: llora en silencio, es la dirección) | película, 10:14-10:32 |
| Opinando | Makima | «No tuvo gracia.» / «La música estaba bien.» / «Normalita de verdad.» | película, 7:56-8:48 |
| Opinando | Denji | «La verdad, hasta ahora todas me parecieron meh.» | película, 9:02 |

**Ejemplo de texto del canal en su voz** (propuesta, no cita): Makima,
«Cuéntanos qué estás viendo.» / «¿Lo recomiendas?» / «Si tiene spoilers,
márcalos.» Denji, de réplica: «¡¿Y si es de las malas?!». Makima:
«También cuenta. Una de cada diez vale la entrada.»

---

## 18A · Estilo de dibujo y técnica, y cómo replicarlo (punto 18)

### 18A.1 El manga (Tatsuki Fujimoto)
- **Línea gruesa, suelta y «sucia»**, no la línea limpia y pareja de otros
  shōnen. Se vuelve más nerviosa en el movimiento ✅
  ([Anime News Network](https://www.animenewsnetwork.com/feature/2022-11-18/the-chainsaw-man-anime-style-feels-off/.191720),
  [FandomWire](https://fandomwire.com/chainsaw-mans-6-ugliest-manga-panels-prove-tatsuki-fujimotos-artstyle-can-never-beat-gege-akutamis-jjk/)).
- **Sombreado**: mucho **negro sólido a pincel** y **rayado cruzado**
  (*cross-hatching*); **poca trama de puntos**, y sin fórmula fija de un
  capítulo a otro ✅ (las dos fuentes de arriba, y visto en las páginas de
  manga de la hoja 1, n.º 28-43).
- **Composición**: diálogos con **fondos vacíos** y viñetas casi mudas,
  como planos de cine; en las peleas, sombras cargadas y fondos llenos
  de caos ✅ (ANN; [CBR](https://www.cbr.com/greatest-chainsaw-man-manga-panels/)).
- **Programa**: dibuja en digital. En su charla con Kenshi Yonezu, en la
  web oficial de la película, nombra **Clip Studio Paint**
  ([chainsawman.dog](https://chainsawman.dog/movie_reze/special/)); un
  hilo de [Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14222070749)
  dice que es digital y que sus ayudantes acaban a mano. Digital ✅ (dos
  fuentes); el programa ⚠️ (una sola, aunque oficial).
- En la viñeta del cine (cap. 39,
  [717×582](https://static.wikia.nocookie.net/chainsaw-man/images/9/9f/Denji_and_Makima%27s_movie_date.png))
  **el público es simple y sin sombra**; sólo Denji y Makima llevan
  sombra y detalle ✅ (visto). Es el truco para la lámina.

### 18A.2 El anime (MAPPA, 2022): quién y con qué
- **Equipo** ✅ ([AniList, staff](https://anilist.co/anime/127230/staff)):
  director **Ryū Nakayama**; diseño de personajes **Kazutaka Sugiyama**;
  dirección de arte **Yūsuke Takeda**; diseño de color **Naomi Nakano**;
  dirección de fotografía **Teppei Itō**; dirección de CG **Motoi Okunō**
  y **Kazumasa Yokokawa**; música **Kensuke Ushio**.
- **La idea**: un **3D «pegado al dibujo»** (作画に寄せた3DCG). El
  director pidió que el 3D se fundiera con la animación a mano, no que
  pareciera real ✅ ([CGWORLD, parte 1](https://cgworld.jp/article/202303-chainsawman1.html)).
- **Programas del 3D** ✅ (CGWORLD, parte 1): **3ds Max 2022** (modelado),
  **ZBrush 2021** (escultura de demonios), **Substance 3D Painter 2021**
  (materiales), **Photoshop 2021** (retoque a mano de texturas),
  **Pencil+ 4** (sombreado tipo *toon* y líneas) y **KM-3D Cloth Deform**
  (tela sin simulación completa).
- Chainsaw Man y Samurai Sword tienen **3 niveles de detalle**: plano
  general, medio y primer plano con pupilas. El *rig* mueve **cada diente
  y cada eslabón** por separado ✅ (CGWORLD, parte 1).
- **Fotografía** (撮影) ✅ ([CGWORLD, parte 3](https://cgworld.jp/article/202303-chainsawman3.html)):
  **After Effects** con **Magic Bullet Looks** y **PSOFT CelFX**. Itō
  pone en cada plano un **color complementario** (naranja sobre las
  escenas azules) que **baja contraste y saturación**: da aire de imagen
  real. Añade **brillo alrededor de las luces**, cambios de color del
  aire, humo, sangre y agua de archivo, y **desenfoque de profundidad**
  hasta en detalles pequeños (la espuma de una cerveza).
- **Grano y aberración**: el grano fino se ve en toda la película; en el
  haz del proyector hay un **halo verde-violeta** (7:44 del corte EN) ✅
  visto. Que el estudio use un filtro de aberración cromática **no lo
  dice** CGWORLD ⚠️: Magic Bullet Looks lo trae, pero no está confirmado.

### 18A.3 Encuadres y composición (cómo se enmarca cada emoción)
- **Homenajes de cine** ✅ ([Anime Herald](https://www.animeherald.com/2023/06/03/how-the-chainsaw-man-anime-adaptation-grounded-itself-in-filmic-realism/)):
  plano secuencia con primer plano extremo a lo **Tarantino** (Power
  camino del despacho de Makima); **plano tatami** a lo **Ozu** (el
  primer viaje en coche de Denji y Makima); **cámara subjetiva** en el
  callejón del ep. 12; **planos generales** muy abiertos tras las peleas
  para enseñar el destrozo.
- En el ep. 8 (azotea) la cámara **sube** en primer plano sobre Katana
  Man, **abre** a plano general y **vuelve** a primeros planos antes de la
  carga: composición en capas ✅ (misma fuente).
- El opening copia **plano a plano** escenas de películas reales ✅ (misma
  fuente y §11).
- **Por emoción**, en la escena del cine (§2, §15; vistos en el corte
  EN) ✅: **alegría**, un encuadre que deja ver la cara y los puños al
  pecho (Denji, 7:04); **explicar o recomendar**, ella sentada y girada
  hacia él (Makima, 9:28); **llanto**, **de perfil**, una lágrima, en
  silencio (Makima, 10:36); **final**, **plano general** con las dos
  siluetas y la pantalla en blanco (10:43).

### 18A.4 Cómo reproducirlo en Photoshop y Blender
Guía propia hecha con lo de arriba (no es cita de nadie):
- **Blender, personajes y demonios**: esculpir en *Sculpt Mode* (lo que
  ellos hacían en ZBrush). Contorno grueso con **Solidify con las
  normales invertidas** o con **Freestyle**, más grueso cerca de la cámara
  (como sus 3 niveles de detalle). Ropa suelta con *Cloth*.
- **Blender, sombreado**: *Shader to RGB* + *Color Ramp* de **2 o 3
  tonos**, sin brillo especular duro. Luz de tres puntos suave.
- **Blender, la sala**: todo oscuro menos las caras; el haz del proyector
  como un volumen con **luz cálida**; butacas con Fabric022 o Fabric026
  de ambientCG **recoloreadas a mostaza** (§5.4).
- **Photoshop, color**: capa de **Balance de color o Curvas** con el tono
  complementario (naranja sobre azul, o al revés), como Itō; bajar un poco
  la saturación.
- **Photoshop, textura**: **grano** (Filtro > Ruido, o una capa de grano en
  Superponer al 8-15 %) y una **viñeta** suave; brillo suave alrededor de
  las luces (capa duplicada, desenfocada, en Trama).
- **Photoshop, manga**: pincel de tinta con presión, **rayado cruzado**
  (§18B) y trama al 20-30 % sólo donde haga falta.
- **Aberración** (opcional): mover 1-2 px los canales rojo y azul. Es
  coherente con «cámara real», pero no está documentado como estilo
  oficial ⚠️.

### 18A.5 Modelos y *rigs* libres para partir
Todos **fan art** con licencia **CC Attribution** (confirmada por la API
de Sketchfab): citar autor y enlace, y usarlos para pose y proporción, no
como el personaje final.
- **Denji con huesos**: [Denji (Chainsaw-Man) (Yes Rigged bone)](https://sketchfab.com/3d-models/none-bdd7c53adfc54033b47fb8e3f60545b1),
  de KenzoDkohno22T ✅.
- **Chainsaw Man y Makima con huesos**: [Chainsaw-man and makima (Yes Rigged bone)](https://sketchfab.com/3d-models/none-2d08535cb4d94657976fbfc5d8b45e60),
  de KenzoDkohno22T ✅.
- [Denji (Chainsaw Man)](https://sketchfab.com/3d-models/none-55234e1109bc40819168fadbf5869fca),
  de Scorpion4241, y [Denji and Pochita](https://sketchfab.com/3d-models/none-aa07c407793d48dca02f8b27ba79d397)
  ✅.
- **Butacas**: las de §4.2 (Glowbox 3D, qwerty14t, yuuuusukeeee…), todas
  CC Attribution ✅.
- La lista completa, con licencias, en §4.

### 18A.6 La película (2025)
- La búsqueda en CGWORLD (en japonés) sólo sacó el *making of* de la
  serie (2023); **no encontré** uno técnico de la película ⚠️. Lo que sí
  está medido: su paleta (§5.3) y el pelo granate de Makima (§16),
  distinto del de la serie.

---

## 18B · Texturas 2D (punto 19)

Las capas que hacen falta, de dentro afuera. Las texturas reales (tela,
papel, moqueta) están en §5.4 y los modelos 3D en §4: aquí va lo 2D.

### 18B.1 Qué textura tiene el manga (visto en las hojas)
- Páginas de manga de la hoja 1 (n.º 28-43, 57-59, 72-89) y la hoja 2
  (n.º 94): **negro sólido a pincel** y **rayado cruzado fino** para
  sombra, movimiento y caos; **muy poca trama de puntos** ✅ (visto, y las
  fuentes de §18A.1).
- **Ropa sin estampados**: camisa, corbata y traje del uniforme son de
  **tela lisa** en los 5 diseños medidos (§16) ✅ (visto). No hay cuadros,
  rayas ni lunares que copiar.
- **Papel**: el de los tomos de Jump Comics es **crema**, no blanco puro;
  en color, la camisa también es crema (`#EDEDE3`-`#F0EFE7`, §16).

### 18B.2 Pinceles y texturas libres equivalentes

| Capa | Recurso | Licencia |
|---|---|---|
| **Rayado cruzado** (lo que más usa) | [Cross-hatching](https://assets.clip-studio.com/en-us/detail?id=1750715), 17 texturas, Clip Studio Assets | Gratis ✅ |
| Rayado, pluma y punteado para **Photoshop** | [Manga Brushes](https://myphotoshopbrushes.com/resources/3790/manga-brushes), MyPhotoshopBrushes | Gratis, sin registro (lo dice la página) ⚠️ |
| **Trama de puntos** (poca) | [FREE Manga Screentone Pack 1](https://assets.clip-studio.com/en-us/detail?id=2142037) y [Essential Screentone Brushes](https://assets.clip-studio.com/en-us/detail?id=2087033), Clip Studio Assets | Gratis con cuenta gratuita ✅ |
| **Papel** de la entrada o del tomo | [Paper005](https://ambientcg.com/view?id=Paper005) y [Paper006](https://ambientcg.com/view?id=Paper006) (crema y tostado, grano fino; mejores que Paper001 y 003, que son blancos), ambientCG | **CC0** ✅ |
| **Terciopelo** de butaca (si se pinta en 2D) | [Fabric022](https://ambientcg.com/view?id=Fabric022) o [Fabric026](https://ambientcg.com/view?id=Fabric026), recoloreadas a mostaza | **CC0** ✅ |
| **Grano de película** | Filtro > Ruido de Photoshop, en Superponer al 8-15 % (§18A.4) | propio |

### 18B.3 Emblemas y logos
- **Logo japonés** チェンソーマン en **SVG**:
  [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Chainsaw_Man_(Japanese)_logo.svg)
  ✅. Es marca registrada: mirar la página de Commons antes de usarlo. Su
  forma (letra a mano, bordes dentados) está en §6.
- **Seguridad Pública**: **no encontré** un escudo, parche o insignia
  propia. Busqué «badge», «emblem», «insignia» y «pin» en el texto de la
  wiki, en VS Battles Wiki y en CBR. Se reconoce por el **traje negro con
  corbata** ✅ ([CBR](https://www.cbr.com/chainsaw-man-public-safety-commission-explained/)).
  Su nombre completo: **Tokyo Special Division 4**
  ([VS Battles Wiki](https://vsbattles.fandom.com/wiki/Special_Division_4)).
- El **rótulo del cine**, シネマ座, es el «logo» del sitio de la lámina:
  letras plateadas en relieve sobre panel verde azulado (§5).

### 18B.4 Un tratamiento gráfico fácil de copiar
- La portada de **MEN'S NON-NO** n.º 464 (sep-2025): **todo en blanco y
  negro menos el pelo y los ojos**, a color ✅ (hoja 1, n.º 4,
  [3197×4093](https://static.wikia.nocookie.net/chainsaw-man/images/8/87/Men%27s_Non-No_No.464_Special_Edition.png)).
  En Photoshop: capa en blanco y negro con máscara que deja ver sólo pelo
  y ojos.

---

## 18C · Gustos y detalles de cada personaje (punto 20)

**No encontré un *databook* oficial** con fichas de comida, cumpleaños y
gustos: lo busqué en japonés (`チェンソーマン 公式ファンブック`) y en la
wiki ⚠️. La wiki sí cita una guía oficial, *Love, Flower, Chainsaw
Guide*, para el dato de Makima. Lo de abajo sale de las **fichas de
AniList** (las alturas vienen de la tabla de alturas de la exposición
oficial del anime) y de la **trivia de la wiki** (wikitext completo de
cada personaje). La personalidad de cada uno está en §8.

| Personaje | Altura | Lo que ama, su manía o su objeto | Fuente |
|---|---|---|---|
| **Denji** | 173 cm (180 transformado) | Su sueño de comida **cambia**: pan tostado con mermelada al principio (ep. 1, 9:12), un bistec más adelante. Objeto: el **cordón del pecho** | [AniList](https://anilist.co/character/130102), [wiki: Denji](https://chainsaw-man.fandom.com/wiki/Denji) ✅ |
| **Makima** | 168 cm | **El cine**: ve películas para aprender cómo sienten los humanos. «Fuma» cigarrillos **«hi-fight»** (parodia de Hi-Lite) sin fumar de verdad. Edad: secreto de la trama | [AniList](https://anilist.co/character/137080), [wiki: Makima, Trivia](https://chainsaw-man.fandom.com/wiki/Makima#Trivia) ✅ |
| **Power** | 170 cm | Su gata **Nyako** (ep. 3-4). Presume de lo que no puede hacer. Su nombre viene de las **Potestades**, un rango de ángeles | [AniList](https://anilist.co/character/137079), wiki ✅ |
| **Aki** | 182 cm | **Piercings** en la oreja que le hizo Himeno, que insistió (cap. 31). Katana y moño alto | [AniList](https://anilist.co/character/137081), wiki ✅ |
| **Reze** | no consta | Alias oficial «**Bomb Girl**». Trabaja en el café (§19, concepto C) | [AniList](https://anilist.co/character/148740), wiki ✅ |
| **Himeno** | 175 cm | En el diseño original iba a ser **la hermana de Aki**; Fujimoto pensaba dejarla vivir más (Jump Festa 2022) | [AniList](https://anilist.co/character/144596), wiki ✅ |
| **Kobeni** | 155 cm | Tiene **los mismos lunares** que Togata, de *Fire Punch* (otro manga de Fujimoto). Su **coche**, famoso (§14) | [AniList](https://anilist.co/character/144594), [wiki: Kobeni](https://chainsaw-man.fandom.com/wiki/Kobeni_Higashiyama#Trivia) ✅ |
| **Kishibe** | 194 cm | Bebe **de una petaca** todo el rato | [AniList](https://anilist.co/character/144593), wiki ✅ |
| **Beam** | 165 cm (176 con la aleta) | Adora a Chainsaw Man y sigue a Denji en todo | [AniList](https://anilist.co/character/157232) ✅ |
| **Ángel** | 155 cm | Odia trabajar: dice preferir morir a trabajar | [AniList](https://anilist.co/character/152231) ⚠️ (una fuente) |
| **Pochita** | — | Ladra y gime como un perro; su cola es el **cordón de arranque** de una motosierra | [AniList](https://anilist.co/character/170266) ⚠️ (una fuente) |

**Cómo se ven a sí mismos** ✅ (wiki): Power se cree grandiosa y huye
cuando pierde; Aki se ve como alguien normal que sí siente el duelo;
Makima se hace una **máscara de persona amable** porque, según Fujimoto,
le falta experiencia propia.

**En el café oficial** (Tokio, Nagoya y Osaka, feb-2023) cada uno tuvo
su plato: el **omurice de Denji**, el **parfait de pudín de Pochita** y
la **«Bloody Orange Soda» de Power**, con dos pimientos de cuernos ✅
([Soranews24](https://soranews24.com/2023/01/19/chainsaw-man-cafe-opening-in-three-cities-in-japan-food-looks-bloody-delicious%E3%80%90photos%E3%80%91/),
[Siliconera](https://www.siliconera.com/chainsaw-man-cafe-merchandise-will-open-in-february-2023/)).
Es menú de la colaboración, no de la obra.

**Lo que falta** ⚠️: **cumpleaños** (ni AniList ni las partes los traen),
y la **comida favorita** de Makima, Power, Aki y Reze dicha en la obra.
Edades: Denji, 16 años (cap. 1-82); Kobeni, veintitantos; las demás no
constan (AniList).

---

## 18D · Por qué la gente la ama (punto 21)

### 18D.1 Las razones, con fuente
- **Mezcla rara que funciona**: humor, violencia y fondo emocional a la
  vez. **James Beckett** (*Anime News Network*) le da B+ al tomo 1;
  **Julia Lee** (*Polygon*) alaba la acción y el humor negro; **Sheena
  McNeil** (*Sequential Tart*) le da 9/10 y la compara con *Army of
  Darkness*, *Devilman* y *Dorohedoro*; **Danica Davidson** (*Otaku USA*)
  habla de una obra «rara pero sentida» ✅
  ([Wikipedia, «Critical reception»](https://en.wikipedia.org/wiki/Chainsaw_Man#Critical_reception),
  que enlaza cada reseña).
- **No es unánime**: Ian Wolf (*Anime UK News*) le da 6/10; Katherine
  Dacey (*The Manga Critic*) la llama «polarizante» ✅ (misma fuente).
  Divide, y eso también la hace hablar.
- **Premios** ✅ ([Wikipedia, «Awards»](https://en.wikipedia.org/wiki/Chainsaw_Man#Awards_and_nominations)):
  - **Harvey a Mejor Manga** 2021, 2022 y 2023 (también
    [Sportskeeda](https://www.sportskeeda.com/anime/news-chainsaw-man-manga-wins-harvey-award-announces-new-side-story-days-ahead-anime-s-premiere)).
  - **66.º Premio Shogakukan**, categoría shōnen (2021).
  - **Japan Expo Awards**: «Daruma» al mejor manga (2023).
  - Selección oficial del **Festival de Angulema** (2024); nominada al
    **Eisner** (2022).
  - **Crunchyroll Anime Awards** (8.ª edición, 2024): **Mejor serie
    nueva**, y **Emilio Treviño**, mejor voz en **español latino** por
    Denji ([Wikipedia](https://en.wikipedia.org/wiki/8th_Crunchyroll_Anime_Awards),
    [Mediotiempo](https://www.mediotiempo.com/otros-mundos/emilio-trevino-gana-premio-en-los-crunchyroll-anime-awards-2024-japon-conoce-lista-completa-ganadores)).
    Tuvo 25 nominaciones, récord de esa edición.
- **Ventas**: más de **36 millones** de copias hacia junio de 2026; 2.º
  manga más vendido de 2026 por el empujón de la película ✅
  ([Anime Explained](https://www.animeexplained.com/news/chainsaw-man-reaches-36-million-sales-before-final-volume-release/),
  [ComicBook.com](https://comicbook.com/anime/list/5-highest-selling-manga-of-2026-so-far/)).
  La taquilla de la película está en §10.

### 18D.2 Con quién se identifica el público
- **No hay un favorito fijo**: cada encuesta oficial la ganó otro (Power,
  Aki, Reze; §9) ✅. En Reddit, los hilos «¿cuál es tu favorito?» tienen
  hasta **92 comentarios** y ninguna respuesta domina ✅
  ([r/ChainsawMan](https://www.reddit.com/r/ChainsawMan/comments/1qvuwrv/who_is_your_favorite_chainsaw_man_character_and/)).
- **Lo que más dibujan los fans** (Danbooru): **Makima** 11.069 dibujos,
  **Reze** 10.169, **Denji** 8.144, **Power** 6.727 ✅ (dato medido,
  `datos-voz.md`).
- Por qué cada uno (lectura del redactor a partir de §8, no de una
  encuesta ⚠️): **Denji** quiere cosas pequeñas (pan con mermelada, una
  vida normal); **Makima** atrae por el misterio; **Aki** es el hermano
  mayor que sí sufre el duelo (§18C).
- **Hasta el autor cambia de favorito**: Reze en 2020, Denji en 2021 ✅
  (wiki de Reze y de Denji, que citan cada entrevista).

### 18D.3 La escena que hace llorar: la cita en el cine
- **Qué pasa** (§2.1): tras cinco películas malas, en la última Denji
  llora en una escena «que no importa nada» y se esconde; mira a su lado
  y **Makima también llora**, en silencio. A la salida: «Ese final no lo
  olvido hasta que me muera.» / «Yo tampoco.»
- **Minuto**: película, **10:05-10:41** en el subtítulo japonés (10:25-10:58
  en el corte EN de Internet Archive) ✅.
- **Por qué duele**: Denji, que se pregunta si tiene corazón, descubre que
  sí; y Makima, que ve cine **para aprender a sentir** (§18C), siente algo
  con él ✅ (wiki y Crank-in!).
- **Qué suena**: **«our film»**, de Kensuke Ushio, la pieza que el propio
  compositor pide oír en una sala buena ✅ (§11.2). Antes, el ruido del
  proyector (9:21).
- **Cómo está dibujada**: sala a oscuras, luz sólo de la pantalla;
  **primer plano de perfil**, una lágrima, boca entreabierta (Makima,
  10:36 EN); luego **plano general** de las dos siluetas con la pantalla
  en blanco (10:43 EN) ✅ visto. La película de dentro va en **verde
  azulado desaturado** (9:50) ✅.
- **Cómo se actuó**: la dirección pedía «**llora en silencio, sin
  ruido**». Tomori Kusunoki (Makima) no quiso sobreactuar: sólo **a ojos
  de Denji** ella parece tierna. Kikunosuke Toya (Denji) dice que grabarla
  fue «**un buen recuerdo**» ✅
  ([Crank-in!, 14-sep-2025](https://www.crank-in.net/interview/172244/1)).
- **Cómo reaccionó la gente**: Kusunoki dijo que ella misma quería
  **verla en un cine de verdad** (misma entrevista); un análisis la llama
  la mejor escena de la película ✅
  ([Anime Fire](https://animefire.com/2025/11/10/the-best-scene-in-chainsaw-man-the-movie-the-reze-arc/));
  el fandom la repite en fanfics y dibujos de «cita de cine» (デンマキ,
  «映画デート» en Pixiv Enciclopedia, §4).

### 18D.4 Las que hacen reír y las que hacen gritar
- **Reír**: la **crítica de cine** de Makima y Denji: «No tuvo gracia. Eso
  sí, la pantalla parecía cara.» (película, 7:56-8:03) ✅; **el coche de
  Kobeni**, votado en dos encuestas oficiales (§9, §14); la **broma a
  Aki** (§14); en latino, Kobeni: «Porque aún no han depositado el
  aguinaldo» (ep. 12) ✅ (§10).
- **Gritar de emoción**: el «**¡Bieeen!**» de Denji al aceptar la cita
  (película, 6:44-6:46) ✅; el opening **«KICK BACK»**, que entra en el 2:02
  del ep. 1 tras el prólogo sin música ✅ (§11); en latino, el clip
  «**Ahuevooooo**» (§10).

### 18D.5 Lo que falta ⚠️
- **Otras escenas que hacen llorar** (las muertes de la temporada 1 y la
  2.ª mitad del manga) no tienen minuto ni reacción medida en esta pasada.
- **Los comentarios con más votos** sobre la escena del cine: Arctic
  Shift dio *timeout* dos veces. El hilo de Reddit más votado recogido es
  «¿Cuál es tu momento o personaje favorito?» (173 votos,
  [r/ChainsawMan](https://www.reddit.com/r/ChainsawMan/comments/1mbl89t/whats_your_favorite_moment_or_character_in/)).
- **Vídeos de reacción**: no los encontré (YouTube pide iniciar sesión).

---

## 18E · Fan dubs y comunidad hispana (punto 22)

Interesa mucho: el servidor es de doblaje. YouTube y TikTok piden
iniciar sesión desde el servidor, así que **las vistas de esas dos webs
no están comprobadas** ⚠️; las de Dailymotion sí (por su API).

### 18E.1 Fandubs en español

| Qué | Canal | Dónde | Escena | Vistas |
|---|---|---|---|---|
| «**Makima y Denji en el Cine**» | LATAM Fandub Studios (animación de Maplestar) | TikTok y YouTube | **la misma cita del cine de la lámina** | sin comprobar ⚠️ (el título sale en varias búsquedas independientes ✅) |
| «La Cafetería de Reze (Chainsaw Man) // Doblaje Español Latino» (0:52) | LATAM Fandub Studios | [Dailymotion x9oi0k4](https://www.dailymotion.com/video/x9oi0k4) | Reze en el café (concepto C) | **1.737** ✅ |
| «¿Qué pasaría si Reze llegara al café? // Fandub Español Latino» (4:42) | LATAM Fandub Studios | [Dailymotion x9wjyoi](https://www.dailymotion.com/video/x9wjyoi) | Reze en el café | **578** ✅ |
| «Makima abraza a Denji – Chainsaw Man / Fandub Latino» | sin nombre en la búsqueda | [YouTube](https://www.youtube.com/watch?v=ivDPlCp4N38) | Makima y Denji | sin comprobar ⚠️ (sólo el título) |

LATAM Fandub Studios es el grupo hispano que más ha doblado esta serie
en lo encontrado: **dos de sus vídeos tocan los sitios de los conceptos
A y C** (el cine y el café).

### 18E.2 Covers del opening en español
- **Al menos 8 covers latinos de «KICK BACK»**, subidos entre oct-2022 y
  ene-2023, de **David Delgado, 0uter, Alan Rojas, Iris, CGcover y
  Tricker**, entre otros ✅ (títulos y fechas de los propios vídeos, vía
  buscador). Enlaces y vistas: sin comprobar ⚠️.
- Útil para el canal de canto del servidor: el opening generó comunidad.

### 18E.3 Memes y orgullo hispano del doblaje
- **«Pues no, mi ciela, ya quisieras»** (Denji a Himeno, ep. 8): el
  propio doblaje mete un meme ✅ (Doblaje Wiki, §10).
- **«Ahuevooooo»**: clip oficial de Crunchyroll en Español con la voz de
  Emilio Treviño ✅ (§10).
- **Emilio Treviño**, mexicano, ganó el Crunchyroll Anime Award a la
  mejor voz en español latino por Denji (2024) ✅ (§10, §18D). Es el mejor
  gancho para un servidor de doblaje.
- **Los fans eligieron la voz de Himeno**: el director, Octavio Campos,
  dejó que el público propusiera el reparto ✅ (Doblaje Wiki, dos notas).
  Y Campos se dobla a sí mismo un personaje: **Yutaro Kurose** ✅.
- El estreno de la película en cines de Latinoamérica, **doblada y
  subtitulada** (23-oct-2025, Cinépolis y Cinemex), está en §10.

### 18E.4 Lo que falta ⚠️
- **Vistas y canal** de los fandubs y covers de YouTube y TikTok (piden
  iniciar sesión desde el servidor).
- **Parodias hispanas** propias (fuera de los memes del doblaje): no las
  encontré.

---

## 18F · Colaboraciones, figuras y cosplay (punto 23)

Su arte trae **poses y ropa nuevas**: sirve para salir del uniforme.

### 18F.1 Portadas de revistas de moda (lo más documentado)
Todas ✅ (imagen vista en las hojas y nota de prensa o wiki):
- **MEN'S NON-NO** n.º 464 especial (sep-2025, por la película): Reze y
  Makima, **en blanco y negro con pelo y ojos a color** (hoja 1, n.º 4,
  [3197×4093](https://static.wikia.nocookie.net/chainsaw-man/images/8/87/Men%27s_Non-No_No.464_Special_Edition.png);
  [Mantan Web](https://en.mantan-web.jp/e_article/20250901dog00m200009000c.html)).
- **CUT** (oct-2025): **Denji y Reze abrazados con una flor** (hoja 1,
  n.º 22, [2343×3000](https://static.wikia.nocookie.net/chainsaw-man/images/f/f7/CUT_2025-10.png));
  y la de nov-2022 ([1586×2048](https://static.wikia.nocookie.net/chainsaw-man/images/0/03/CUT_2022-11.png),
  hoja 2, n.º 95).
- **UOMO** (nov-2022): hoja 2, n.º 93
  ([1600×2048](https://static.wikia.nocookie.net/chainsaw-man/images/f/f0/UOMO_2023-1.png)).
- **EYESCREAM** (ene-2023): **Power cubierta de sangre** con adornos en la
  cabeza, de NAKAKI PANTZ (hoja 2, n.º 96,
  [1586×2048](https://static.wikia.nocookie.net/chainsaw-man/images/7/74/EYESCREAM_2023-1.png);
  [Anime Corner](https://animecorner.me/chainsaw-man-animes-power-featured-on-eyescream-magazine-cover/)).
- **Nylon Japan** (feb-2023): Chainsaw Man con sangre en la sierra
  ([CBR](https://www.cbr.com/chainsaw-man-fashion-icon-nylon-cover/)).
- **an·an**: Aki en portada y contraportada, ilustración de MAPPA
  ([Anime Corner](https://animecorner.me/aki-hayakawa-featured-on-the-cover-of-japanese-fashion-magazine-anan/)).

### 18F.2 Ropa: UNIQLO UT (dos veces)
- **2023**: 9 camisetas con el ilustrador **Kosuke Kawamura**, collage
  rasgado sobre escenas del anime ✅
  ([Anime News Network](https://www.animenewsnetwork.com/interest/2023-08-25/uniqlo-launches-chainsaw-man-x-kosuke-kawamura-ut-fashion-collection/.201630)).
- **2025** (por la película): 3 diseños (2 negros, 1 blanco) con Pochita
  y el Demonio Motosierra ✅
  ([UNIQLO UT](https://www.uniqlo.com/us/en/contents/feature/ut-magazine/s188-chainsaw-man/),
  [Hypebeast](https://hypebeast.com/2025/7/chainsaw-man-uniqlo-ut-collaboration-release-info)).

### 18F.3 Cafés temáticos y eventos
- **Feb-2023**: café en Tokio, Nagoya y Osaka, estilo **pastelería de
  lujo**; los personajes dibujados **vestidos de pasteleros** en pósters y
  posavasos ✅ (Soranews24, Siliconera; menú en §18C).
- **Dic-2023 a feb-2024**: otro café temporal ✅ (Tokyo Cheapo, según la
  parte de imagen).
- **2025**: café de la película ✅ ([iwafu](https://www.iwafu.com/en/events/1033042)).
- **Jump Festa 2025**: Denji, Aki, Makima y Power en **cartel pop de un
  solo color de fondo** (hoja 1, n.º 18-21) ✅.
- **Ichiban Kuji** (lotería de premios): tablero dibujado de Denji y Reze
  (premio D) (§3).
- **Exposición del anime**: foto de la zona de Chainsaw Man, con licencia
  **CC BY-SA 4.0** ([Wikimedia Commons, 2400×1800](https://upload.wikimedia.org/wikipedia/commons/a/a0/Cosir_at_Chainsaw_Man_exhibition_area_20221106e.jpg))
  ✅.

### 18F.4 Figuras oficiales (pose 3D real)
Good Smile Company ✅. Una figura es una **pose 3D hecha por escultores**:
mejor referencia de ángulo y apoyo que un render de fan.
- **Nendoroid Denji**, con piezas para pasar a Chainsaw Man y Pochita a
  escala ([Good Smile](https://www.goodsmile.info/en/product/10715/Nendoroid+Denji.html)).
- **Nendoroid Power**: 3 caras, martillo, cuchillos y Nyako en miniatura
  ([Good Smile](https://www.goodsmile.info/en/product/10834/Nendoroid+Power.html)).
- **Nendoroid Makima**: 3 caras, piruleta, gabardina
  ([Good Smile US](https://www.goodsmileus.com/products/nendoroid-makima-59111)).
- **Pop Up Parade**: Aki, Power, Makima, Himeno y Kobeni; Makima mide 16
  cm, con **sonrisa conspiradora**
  ([Good Smile: Chainsaw Man](https://www.goodsmile.info/en/chainsawman)).

### 18F.5 Cosplay bien hecho
- **Vinnegal**, como Makima (varias sesiones, una del arco de Reze) ✅
  ([X de la cosplayer](https://x.com/Vinnegal/status/1547281320816041986),
  [ComicBook.com](https://comicbook.com/anime/news/chainsaw-man-makima-cosplay-best-girls-anime/)).
- **Wiru_Son**, como Denji, con colmillos ⚠️ (sólo el resumen de
  [ComicBook.com](https://comicbook.com/anime/news/chainsaw-man-cosplay-perfect-denji/)).
- Un Denji con **motosierra con motor de verdad** como accesorio ⚠️
  (sólo el titular en ComicBook.com, sin nombre): buena referencia de
  material y volumen.
- Fotos libres de cosplay en Flickr (Openverse): Makima, **CC BY-SA 2.0**
  ([marelywaffle](https://live.staticflickr.com/65535/52618867029_62e8c81ba2_b.jpg));
  Yoru, CC BY-NC-ND 2.0 ([Flickr](https://live.staticflickr.com/65535/52269812384_9b786236fa_b.jpg)).

### 18F.6 Cruces con otros juegos
- **No encontré** ningún *crossover* con otro juego o marca de juegos
  (busqué Fortnite, Identity V y «gacha collaboration», en inglés y
  japonés). Queda como «no lo encontré», no como «no existe».
- La franquicia sí tiene **juego propio anunciado**: **Chainsaw Man
  Mobile** (MAPPA, 19-jun-2026), sin fecha (§13).

---

## 18G · Obras parecidas y temas relacionados (punto 24)

### 18G.1 Lo que dice el propio Fujimoto
- Llamó a su serie **«una copia de *Dorohedoro* y *Jujutsu Kaisen*»**, un
  **«*FLCL* malvado»** y un **«*Abara* pop»** (*Abara*, de Tsutomu Nihei,
  el de *Blame!*) ✅ ([Wikipedia](https://en.wikipedia.org/wiki/Chainsaw_Man));
  ⚠️ cita de segunda mano: no vi la entrevista original en japonés.
- Comparó el tono de la **2.ª parte** con ***El gran Lebowski*** (por su
  final ambiguo) ✅ (misma fuente).

### 18G.2 Influencias directas
- ***La matanza de Texas*** (1974): «la motosierra molaba»; de ahí el
  nombre ✅ ([FandomWire](https://fandomwire.com/tatsuki-fujimoto-took-inspiration-from-iconic-30-9-million-movie-texas-chainsaw-massacre/),
  Wikipedia).
- El clímax de la 1.ª parte sale de la pelea final de
  ***Kizumonogatari III: Reiketsu*** (2016) ✅ (Wikipedia).
- El arco de Reze (manga y película) sale de ***Jin-Roh: La Brigada del
  Lobo*** (tono y alegoría de Caperucita Roja) y de ***Antes del
  amanecer*** (*Before Sunrise*, Linklater: una cita que dura una noche)
  ✅ ([SlashFilm](https://www.slashfilm.com/2020861/chainsaw-man-the-movie-reze-arc-romance-before-sunrise-inspiration/)).
- Además cita, entre lo que le gusta, ***FLCL***, ***Sharknado***,
  ***Interstellar***, ***El club del tifón*** (台風クラブ), ***Hereditary*** y
  hasta *Winnie the Pooh* ✅ ([Real Sound](https://realsound.jp/book/2023/01/post-1229201.html),
  [EpicStream](https://epicstream.com/article/things-that-inspired-chainsaw-man-creator-tatsuki-fujimoto)).
  Su lista de películas recomendadas está en §11.3.

### 18G.3 Con qué la compara la crítica
- ***Devilman*** (Go Nagai): sexo y violencia crudos, un chico que muere y
  vuelve fusionado con un demonio. Varios medios la llaman su heredera ✅
  ([CBR](https://www.cbr.com/devliman-chainsaw-man-anime/),
  [Seize the Press](https://www.seizethepress.com/2024/02/10/rip-and-tear-stp9/)).
- *Army of Darkness* y *Dorohedoro* (Sequential Tart, §18D) ✅.

### 18G.4 Obras parecidas (lo que recomiendan los fans)
Recomendaciones de usuarios de [AniList](https://anilist.co/anime/127230),
de más a menos votos ✅ (dato medido): ***Jujutsu Kaisen*** (1.099),
***Dorohedoro*** (599), ***Devilman Crybaby*** (420), ***Dandadan***
(381), ***Parasyte*** (311), ***Hell's Paradise*** (257), ***Kaiju
No. 8*** (208), ***Tokyo Ghoul*** (161), ***Zom 100*** y ***Undead
Unluck*** (90), ***Attack on Titan*** (89), ***Tatsuki Fujimoto 17-26***
(84, sus historias cortas en anime) y ***FLCL*** (71).

### 18G.5 Del mismo autor
- ***Fire Punch***: Kobeni tiene **los mismos lunares** que Togata ✅
  (wiki, §18C).
- ***Tatsuki Fujimoto 17-26***: antología animada de sus historias cortas
  (AniList, arriba) ⚠️ (una fuente).

### 18G.6 Otras láminas del servidor (para no repetir)
- **Ningún otro encargo** apunta a #que-estas-viendo ✅ (revisados con
  `grep` los más de 130 archivos de `encargos/`).
- En tono (sangre, tema adulto), las más cercanas son **18 Death Note**
  (el cuaderno sobre la mesa) y **02 Attack on Titan** (la estela de
  piedra). Usan otros canales y otros objetos. **El cine y las entradas
  no se repiten** en ningún otro concepto ✅.

---

## 18H · El mundo, la historia y sus símbolos (punto 25)

### 18H.1 Las reglas del mundo, en cinco líneas
✅ en la wiki y en [Wikipedia](https://en.wikipedia.org/wiki/Chainsaw_Man).
1. Los **demonios** nacen en el **Infierno** del miedo humano a algo:
   cuanto más se teme, más fuerte es el demonio ([wiki: Devil](https://chainsaw-man.fandom.com/wiki/Devil)).
2. Un demonio firma un **contrato** con un humano: poder a cambio de algo
   (años de vida, un órgano, obediencia). Romperlo mata, salvo que el
   contrato traiga una salida
   ([wiki: Contract](https://chainsaw-man.fandom.com/wiki/Contract)).
3. Un **endemoniado** (*Fiend*, 魔人) es un demonio dentro de un cadáver,
   como Power; un **híbrido** es un humano fundido con un demonio, como
   Denji con Pochita ([wiki: Fiend](https://chainsaw-man.fandom.com/wiki/Fiend)).
4. La **Seguridad Pública** (gobierno) y el **sector privado** cazan
   demonios en Japón ([wiki: Devil Hunter](https://chainsaw-man.fandom.com/wiki/Devil_Hunter)).
5. Los **Cuatro Jinetes** (Control, Guerra, Hambruna y Muerte) son los
   demonios más fuertes ([wiki: Four Horsemen](https://chainsaw-man.fandom.com/wiki/Four_Horsemen)).
   Quién es cada uno es **spoiler**: no va en la lámina.

### 18H.2 La historia por arcos
✅ ([wiki: Public Safety Saga](https://chainsaw-man.fandom.com/wiki/Public_Safety_Saga),
[Academy Saga](https://chainsaw-man.fandom.com/wiki/Academy_Saga)).

**Parte 1, Seguridad Pública** (cap. 1-97, dic-2018 a dic-2020; la
película adapta la Chica Bomba, cap. 39-52, y la serie de 2022 va antes,
§2):
- **Introducción** (1-4): Denji muere y renace como Chainsaw Man.
- **Demonio Murciélago** (5-13): rescata a la gata de Power.
- **Demonio Eternidad** (14-22): misión por un trozo del Demonio
  Pistola.
- **Katana Man** (23-38): venganza tras el ataque a la División 4.
- **Chica Bomba** (39-52): **empieza con la cita del cine con Makima**
  (cap. 39) y sigue con Reze. Es el arco de la película.
- **Asesinos internacionales** (53-70): Denji, objetivo del mundo.
- **Demonio Pistola** (71-79) y **Demonio Control** (80-97): el final de
  la parte 1 (spoiler).

**Parte 2, la Academia** (cap. 98-232, jul-2022 a mar-2026): Asa Mitaka
y Yoru; las citas con Denji; la Iglesia de Chainsaw Man; el Demonio
Vejez; el Demonio Muerte y el final de la obra.
- **Fin del manga**: **232 capítulos y 24 tomos** ✅; el día no coincide
  entre fuentes: **25-mar-2026** según la wiki, **24-mar-2026** según un
  resumen de búsqueda ⚠️.

### 18H.3 Símbolos y objetos que un fan reconoce al instante
- **El cordón del pecho** de Denji: tira de él y salen las motosierras.
  Es el gesto que define a Chainsaw Man ✅ (wiki: Denji y Pochita; se ve
  en toda la mercancía). Sirve como detalle pequeño, sin sangre (un
  llavero, un tirador).
- **Pochita**: perro naranja con una motosierra en la cabeza y la cola de
  cordón de arranque (§18C).
- **El traje negro con corbata** de la Seguridad Pública ✅ (§18B; **sin
  escudo propio**, no lo encontré).
- **El logo チェンソーマン** a mano, con bordes dentados (§6, §18B).
- **シネマ座**, el cine de la cita (§2, §5): el símbolo de esta lámina.
- **Las entradas de cine y el pan con mermelada** (§14).
- Curiosidad: en la página de Pochita, la wiki guarda una foto de una
  **motosierra Makita** real, naranja (hoja 3, n.º 414; [1840×1110](https://static.wikia.nocookie.net/chainsaw-man/images/b/b2/Makita_Chainsaw_%283%29.jpg))
  ⚠️ (sin explicación oficial).

### 18H.4 Vocabulario propio (para textos y para la IA)
Demonio (*Devil*, 悪魔) · Endemoniado (*Fiend*, 魔人) · Híbrido
(*Hybrid*) · Contrato (*Contract*) · Cazador de Demonios (*Devil
Hunter*; **el doblaje latino lo deja en inglés**, §10) · Seguridad
Pública · sector privado · **División Especial 4** (*Tokyo Special
Division 4*) · Infierno (*Hell*) · Cuatro Jinetes · «**Katana Man**»
(así llaman en latino a Samurai Sword) · «guau» (lo que Makima deja decir
a Denji, §14).

---

## 19 · Tres conceptos para la lámina de #que-estas-viendo

Los tres usan **el subtítulo de cine** como cuadro de diálogo (§7.2) y
**un objeto real** para la información (regla 1 del dueño). Son tres
sitios distintos del mismo mundo.

### Concepto A — «Fila 7» (el objeto del plan, mejorado)
- **Objeto y sitio**: una **fila de butacas** de la sala a oscuras, vista
  **desde atrás y un poco de lado**, y **dos entradas** apoyadas en el
  brazo de una butaca, junto a un vaso de bebida (Denji sorbe su bebida
  en el 8:11 ✅). Todo en **Blender**: butacas de §4.2, tela de §5.4,
  entradas con el papel de §5.4 y una esquina doblada.
  **Segunda pasada**: las butacas son **mostaza o ámbar** (`#544A36` en
  sombra, `#7C6D4A` con luz; Fabric022 o Fabric026 recoloreadas), no rojo
  vino; las entradas, en **Paper005 o Paper006** (crema con grano); el
  público de delante, **simple y sin sombra**, como en la viñeta del
  cap. 39 ([717×582](https://static.wikia.nocookie.net/chainsaw-man/images/9/9f/Denji_and_Makima%27s_movie_date.png))
  (§5, §18A).
- **Personajes**: **Makima y Denji** sentados, de espaldas, sólo se ven
  sus perfiles. Makima **girada hacia él** (pose Makima n.º 6, película
  9:09-9:19); Denji mirándola de reojo (Denji n.º 5). Makima es 2.ª en
  las dos últimas encuestas y la escena es suya. Makima con **pelo
  granate** `#4C201F` (el de la película) y, si se le ve la ropa, la **de
  calle de la cita** (cárdigan claro, falda oscura; §16), no el uniforme.
  Referencia de pose en vídeo: Makima girada hacia él, 9:28 del corte EN
  (§15).
- **Cómo habla**: su frase va **como subtítulo** en la pantalla del cine,
  letra blanca con borde negro (**Zen Kaku Gothic New** Black):
  «Encuentro una buena de cada diez. Pero esa una te cambia la vida.»
  (adaptada de su frase del 9:09-9:19, que dice «me ha cambiado»;
  traducción mía ⚠️).
- **Dónde va cada texto**:
  - Título **«¿Qué estás viendo?»**: en la pantalla, como **título de la
    película**, grande (Dela Gothic One, bordes gastados).
  - «Series, pelis, anime. Cuenta qué estás viendo.» y «Dinos si lo
    recomiendas.»: **impresos en la entrada 1** (Space Mono), donde iría
    el nombre de la película y la sala.
  - «¿Spoilers? Márcalos como spoiler.»: **en la entrada 2**, como la
    advertencia de letra pequeña, o **a mano** con bolígrafo (Yuji Syuku).
- **Para que no quede plano**: el **haz del proyector** con polvo cruza
  por encima de las cabezas, **blanco cálido con un halo verde-violeta**
  (medido, 7:44 del corte EN); la **pantalla da luz de contra**: si es la
  última película, **verde azulada** (`#415855`-`#7A8E87`, 9:50), un borde
  en el pelo de Makima; las **entradas y el vaso en primer
  plano**, nítidos, y los personajes un poco desenfocados; el respaldo
  de la butaca de delante tapa el borde de abajo. Encima, el tratamiento
  de Itō: tinte complementario, grano fino y brillo en las luces (§18A.4).

### Concepto B — «La cartelera» (vestíbulo del cine, con Power)
- **Objeto y sitio**: el **tablero de letras** de la entrada del cine
  (fondo negro con ranuras y letras blancas de plástico que se encajan a
  mano) sobre la **taquilla**. Se hace en Blender: cada letra es una
  pieza con su sombra. **Segunda pasada**: encima, la **marquesina real
  del cine**, con su nombre **シネマ座** en letras plateadas en relieve
  (`#9CADAD`) sobre un **panel verde azulado metálico**
  (`#464E4D`-`#758382`) y **4 focos colgantes** (9:12 del corte EN, §5).
  El tablero de letras es propuesta; la marquesina, no.
- **Personajes**: **Power**, subida a una silla, **encajando letras** y
  señalando el tablero con orgullo (pose Power n.º 1: «¡Inclínate ante
  mí!»); **Denji** abajo sujetando la silla, con cara de fastidio (Denji
  n.º 10). Power ganó la 1.ª encuesta y la de VIZ, y es la de los memes.
  Referencias 3D de pose: el **Nendoroid** y la **Pop Up Parade** de Power
  (§18F.4). Ojo con su **pupila en aspa** roja y amarilla si se ve de
  cerca (ep. 2, 19:20, §15).
- **Cómo habla**: subtítulo en las **franjas negras** de la imagen
  (formato cine): «¡Humanos! ¡Díganme qué están viendo! Si es malo, yo
  lo digo.» y Denji, en cursiva (pensamiento): «Ésta no ha visto ni una.»
  (textos propuestos, en su voz ✅ por los subtítulos: «ワシ», fanfarrona).
- **Dónde va cada texto**:
  - Tablero de letras: **«¿QUÉ ESTÁS VIENDO?»** y debajo, en tres
    líneas, **«SERIES»**, **«PELIS»**, **«ANIME»** (Limelight o Bebas
    Neue).
  - «Dinos si lo recomiendas.»: en un **cartel de papel** pegado en el
    cristal de la taquilla.
  - «¿Spoilers? Márcalos como spoiler.»: **letrero pequeño** de «aviso»
    junto a la ventanilla, como los de «prohibido grabar».
- **Para que no quede plano**: la **luz cálida de los 4 focos de la
  marquesina** de arriba contra el vestíbulo más oscuro; el **cristal de la taquilla**
  con reflejos delante de Denji; una **letra caída** en el suelo en
  primer plano. Los carteles de la pared, **inventados** (siluetas que
  recuerden a las películas del opening, §11), nunca carteles reales.

### Concepto C — «Futamichi» (el café de Reze, con la más querida)
- **Objeto y sitio**: la **pizarra de tiza** del café Futamichi (de pie
  en la acera o colgada en la barra), donde el café apunta «la
  recomendación del día». Encaja con Reze: en la escuela de noche hace de
  **maestra** con la pizarra (27:52 ✅). Pizarra, tiza y dos tazas de café,
  en Blender.
- **Personaje**: **Reze** (1.ª en la 3.ª encuesta, con el doble de votos),
  con la tiza en la mano, **medio girada hacia el que mira**, sonriendo
  con picardía (poses Reze n.º 3 y 6). Denji, de espaldas en la barra,
  con su café sin tocar (le sabe «a alcantarilla», 17:40 ✅). Colores de
  Reze medidos en su diseño oficial (§16): pelo `#3F395E` (morado
  azulado oscuro), blusa `#EDE9F1`, shorts `#323037`. Guiño para el
  servidor: el fandub latino «**La Cafetería de Reze**» pasa en este
  mismo sitio (§18E).
- **Cómo habla**: subtítulo en la franja negra de abajo: «¿Y tú qué
  estás viendo? Cuéntame. ¡Y nada de spoilers, eh!» (propuesto, en su
  tono juguetón ✅: «¡Correcto! ¡Genio!», «Te enseño»).
- **Dónde va cada texto**:
  - Pizarra, arriba: **«¿Qué estás viendo?»** (tiza, letra de mano).
  - Pizarra, en medio: «Series, pelis, anime.» / «Cuéntalo y di si lo
    recomiendas.»
  - Pizarra, abajo, recuadrado: «¿Spoilers? Márcalos como spoiler.»
  - Opcional: dos **entradas de cine** asomando bajo la taza de Denji,
    guiño a la cita con Makima.
- **Para que no quede plano**: **ventana con gotas de lluvia** detrás
  (la tormenta de la cabina, 13:42 ✅) y la **cabina de teléfono**
  desenfocada al otro lado de la calle; **luz de tarde** entrando de lado;
  las **tazas en primer plano**. Nada de su forma de Bomba (spoiler).

### ¿Cuál primero?
**A**. Es el objeto que pidió el plan, la escena existe tal cual (con
minuto), y el cuadro (subtítulo de cine) sale de la propia escena. **C**
es la mejor para «el más querido». **B** es la más divertida y la más
fácil de leer en el celular.

---

## 20 · Lo que no pude verificar

Primera pasada (24-sep), y lo que hizo con ello la segunda (25-sep):
- ~~**Ningún fotograma mirado**~~ → **resuelto en parte**: la película y
  los ep. 1, 2 y 7 se vieron en Internet Archive, y el tráiler en
  Dailymotion. Siguen con ⚠️ las **posturas de §15** que no se vieron en
  fotograma.
- ~~**La ropa de la cita del cine y la sala**~~ → **resuelto**: Makima va
  de calle (§16); la sala, con butacas mostaza y el rótulo シネマ座 (§5).
  Sigue sin verse la ropa de **Denji** de cuerpo entero en la cita ⚠️, y
  las **entradas** no salen en plano (son propuesta).
- **La frase latina de Makima** en el cine: **sigue sin oírse** ⚠️
  (YouTube pide iniciar sesión; la película doblada está en Crunchyroll).
- ~~**Voces latinas** de Kobeni, Himeno, Kishibe y Beam~~ → **resuelto**
  (§10).
- ~~**Licencias de Sketchfab** y la textura de terciopelo~~ →
  **resuelto** (§4, §5.4).
- ~~**Tamaños** de imágenes oficiales y fondos~~ → **resuelto** con la API
  de la wiki y Wallhaven. Alpha Coders: tamaños sí, enlace directo de
  cada imagen no ⚠️.
- **Minuto de cada plano** del opening: **en parte** (entra en el 2:02;
  título «KICK BACK» 3:08-3:11; logo 3:41-3:44) ⚠️.
- ~~**Hex aproximados**~~ → **medidos** en fotogramas y arte oficial
  (§5.3, §16).
- **Cine real** que sirvió de modelo a la sala: **sigue sin encontrarse**
  ⚠️ (buscado también como シネマ座 en la wiki).
- **Reddit**: sólo títulos de hilos (recolector); Arctic Shift dio
  *timeout*. **The Cutting Room Floor**: no aplica (no hay juego
  publicado). **Wayback Machine**: tampoco se usó en la segunda pasada
  (ninguna parte lo anota) ⚠️.
- Nuevos de la segunda pasada: vistas de fandubs y covers en YouTube y
  TikTok (§18E), cumpleaños de los personajes (§18C), el programa de
  dibujo de Fujimoto (§18A) y el día exacto del final del manga (§18H) ⚠️.

---

## Cumplimiento del encargo

Los 25 puntos de ENCARGO.md, «Qué investigar», y lo demás que pide.
✅ hecho · ⚠️ a medias (y por qué) · ❌ no hecho. Revisado el 25-sep-2026,
al cerrar la segunda pasada.

| Punto | Qué pide | Estado | Dónde y por qué |
|---|---|---|---|
| 1 | Arte oficial, en cantidad y variado | ✅ | §3 y §3A: tomos 1-11 (menos el 3) con tamaño, versiones sin texto, revistas, cartel IMAX, *key visuals*, Jump Festa, ilustraciones de revelado. Faltan los tomos 3 y 12-24 (detalle) |
| 2 | Fotogramas de escenas icónicas en 1080p, con capítulo y minuto | ✅ | §2 y §15: la cita del cine vista entera y sus fotogramas en 1080p reales (Internet Archive); Power (ep. 2) y Aki (ep. 7) en fotograma |
| 3 | Fan art y 3D con licencia libre | ✅ | §4: fan art con autor (Pixiv, ArtStation, Safebooru) y 30 modelos de Sketchfab con licencia leída en su API |
| 4 | Fondos y sitios, luz, paleta y texturas reales | ✅ | §5: シネマ座 con paleta medida, área de descanso, lugares reales, texturas de ambientCG miradas. ⚠️ sin encontrar: qué cine real inspiró la sala |
| 5 | Tipografía por uso, letra libre con tildes, ñ, ¿ y ¡ | ✅ | §6: una letra por uso, comprobadas con fontTools |
| 6 | Cómo hablan en pantalla (el cuadro de diálogo) | ✅ | §7: el subtítulo de cine de la propia escena. No hay juego publicado con cajas de diálogo (§13) |
| 7 | Personajes y encuestas de popularidad | ✅ | §8 y §9: 3 encuestas oficiales con top 10 y votos, VIZ, Danbooru y AniList |
| 8 | Doblaje latino: reparto en dos fuentes y frases textuales | ⚠️ | §10: todo el reparto con nombre, ✅ en dos fuentes; frases con episodio (Doblaje Wiki) y clips. Falta el **minuto** de las frases y la **frase latina de Makima en el cine**: YouTube pide iniciar sesión y las muestras de Doblaje Wiki no se pasaron por `voz.py` |
| 9 | Música y sonido | ✅ | §11: opening, endings (el del ep. 1 sin animación), piezas de Ushio para la escena del cine, sonido de cada película |
| 10 | Vídeos y tendencias con minuto exacto | ⚠️ | §12: tráiler, opening y endings mirados con minuto. Los enlaces de YouTube y los de TikTok siguen **sin verificar** (piden sesión) |
| 11 | Videojuegos: interfaz, menús, cajas de diálogo | ✅ | §13: no hay juego publicado (dicho y por qué); *Chainsaw Man Mobile* anunciado el 19-jun-2026, sin interfaz pública aún |
| 12 | Lo que ama el fandom y qué NO hacer | ✅ | §14 |
| 13 | Descripción profunda de cada personaje y su cara en cada emoción | ⚠️ | §8: carácter, historia, cómo habla, dinámicas ✅. Caras con fotograma sólo algunas (alegría de Denji 7:04, llanto de Makima 10:36, grito de Power); **faltan rabia, miedo y vergüenza** en vídeo |
| 14 | Poses analizadas (6-10 por personaje) con minuto | ⚠️ | §15: 49 poses con minuto o enlace; las marcadas ⚠️ salen del subtítulo o del contexto y **no se vieron en fotograma** |
| 15 | Vestuario con hex | ✅ | §16: hex medidos con Pillow en diseños oficiales y fotogramas; ropa de la cita |
| 16 | Ciudades, paisajes y fondos de pantalla | ✅ | §17: 15 fondos de Wallhaven con tamaño y autor, Alpha Coders con tamaños; sitios con luz y hora |
| 17 | Guía para IA de imagen y de texto | ✅ | §18: rasgos, etiquetas, paleta medida, línea, luz, encuadre, palabras que ayudan y que estropean, frases reales por emoción |
| 18 | Estilo de dibujo y técnica, y cómo replicarlo | ✅ | §18A: manga y anime (CGWORLD: programas, *rigs*, fotografía de Itō), encuadres, guía de Photoshop y Blender, *rigs* libres. ⚠️ el programa de Fujimoto (una fuente) |
| 19 | Texturas 2D | ✅ | §18B: rayado, trama, papel, terciopelo, grano, logo, con licencia |
| 20 | Gustos y detalles de cada personaje | ⚠️ | §18C: alturas, manías, objetos, trivia. **No hay *databook*** encontrado: faltan **cumpleaños** y comidas favoritas de varios |
| 21 | Por qué la gente la ama y las escenas que hacen llorar | ⚠️ | §18D: crítica, premios, ventas, identificación y la escena del cine completa (minuto, música, dibujo, actuación). Faltan **otras escenas** con minuto y los **comentarios más votados** (Arctic Shift dio *timeout*) |
| 22 | Fan dubs y comunidad hispana | ⚠️ | §18E: fandubs de LATAM Fandub Studios (vistas de Dailymotion ✅), 8 covers de «KICK BACK», memes y premio del doblaje. **Vistas de YouTube y TikTok sin comprobar** |
| 23 | Colaboraciones, figuras y cosplay | ✅ | §18F: 6 revistas, UNIQLO UT ×2, cafés, figuras de Good Smile, cosplay con nombre. Cruces con otros juegos: no encontré |
| 24 | Obras parecidas y temas relacionados | ✅ | §18G: lo que dice Fujimoto, influencias, crítica, recomendaciones de AniList y otras láminas del servidor |
| 25 | El mundo, la historia y sus símbolos | ✅ | §18H: reglas en cinco líneas, arcos de las dos partes, símbolos y vocabulario. ⚠️ el día exacto del final del manga |
| Conceptos | Tres conceptos de lámina distintos | ✅ | §19: A fila de butacas (Makima y Denji), B cartelera y marquesina シネマ座 (Power), C pizarra del café (Reze) |
| Fuentes | Mínimo 40 fuentes distintas | ✅ | 130 webs distintas enlazadas (`revisar.py`) |
| Tipo | Oficiales (web, redes, entrevistas, *making of*) | ✅ | chainsawman.dog, X oficial, Shōnen Jump, Crank-in!, CGWORLD, Natalie, Good Smile, UNIQLO |
| Tipo | En otros idiomas (japonés, inglés, coreano o chino) | ✅ | japonés (CGWORLD, Crank-in!, Real Sound, Yahoo!知恵袋), coreano (NamuWiki) y chino (Wikipedia china, Douban) en la primera pasada. ⚠️ ningún análisis de técnica en coreano o chino |
| Tipo | Wikis de fans, TV Tropes, The Cutting Room Floor, Wayback Machine | ⚠️ | Fandom, Doblaje Wiki, TV Tropes, VS Battles, NamuWiki ✅. TCRF no aplica (no hay juego). **Wayback Machine no se usó** en ninguna pasada |
| Tipo | Foros y comunidades | ✅ | Reddit (hilos con votos, vía recolector), X, Yahoo!知恵袋, Letterboxd, MyAnimeList. Arctic Shift dio *timeout* |
| Tipo | Arte (Pixiv, ArtStation…) | ✅ | Pixiv, Pixiv Enciclopedia, ArtStation, Safebooru, Danbooru, Wallhaven |
| Tipo | Vídeo con minuto exacto | ⚠️ | Internet Archive y Dailymotion mirados con minuto ✅; YouTube y TikTok sin abrir (piden sesión) |
| Tipo | Código y recursos (GitHub, Sketchfab, texturas) | ✅ | subtítulos en GitHub, Google Fonts, Sketchfab (API), ambientCG, Clip Studio Assets |
| Tipo | Doblaje latino (Doblaje Wiki, ANMTV, entrevistas, créditos) | ✅ | Doblaje Wiki por su API, AniList, ANMTV, entrevistas en prensa latina |
| Hojas | 3 hojas de contacto en `hojas/`, JPEG de menos de 3 MB | ✅ | `imagen_01` (1,1 MB), `imagen_02` (1,2 MB), `imagen_03` (0,85 MB); qué número sirve, en §3A |
| Referencias | `referencias.json`, mínimo 20, las mejores primero | ✅ | 266 referencias, 142 con tamaño medido; primero los fotogramas del cine en 1080p |
| Minutos y hex | 15 minutos citados, 10 colores medidos | ✅ | más de 300 minutos y 45 hex (`revisar.py`) |
| Repaso | «Segunda pasada · qué cambió» y bitácora ampliada | ✅ | arriba del todo y §21 |

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)
- `community.fandom.com` → **000 (CONNECT 403)**. También bloqueados por
  curl o WebFetch: `somoskudasai.com`, `api.sketchfab.com`,
  `polyhaven.com`, `api.polyhaven.com`, `ambientcg.com`,
  `arctic-shift.photon-reddit.com`.
- `api.github.com` responde, pero **sólo para este repositorio**; los
  demás repos se leyeron por `raw.githubusercontent.com` y por la
  búsqueda de código de GitHub.
- **Sin red completa no hay hojas de contacto**: no se creó `hojas/` ni
  se corrió `herramientas/investigar_serie.py`.

### Búsquedas web (46 hechas y 1 rechazada)

**Español (10)**
- n.º 1: Chainsaw Man doblaje latino reparto Denji Power Makima Aki Hayakawa (doblaje.fandom.com)
- n.º 2: Chainsaw Man doblaje latino Crunchyroll voces "Emilio Treviño" Power Makima Aki director estudio
- n.º 3: Chainsaw Man Arco de Reze película doblaje latino reparto voz de Reze "Arturo Cartaño" estudio
- n.º 4: Reze doblaje latino actriz voz Chainsaw Man película Sony Pictures México 23 de octubre Beam Kishibe
- n.º 5: "Chainsaw Man" doblaje "Tavo Campos" "Arturo Cartaño" Himeno Kobeni Kishibe voces latino
- n.º 6: Chainsaw Man doblaje latino frases memes Power Denji "ahuevo" groserías adaptación Tavo Campos entrevista
- n.º 25: Crunchyroll en Español Chainsaw Man doblaje latino clip Makima "guau" OR Power "soy Power" OR "duelo a muerte con cuchillos" (youtube.com)
- n.º 37: Chainsaw Man Arco de Reze taquilla México Latinoamérica estreno cines récord anime Sony Crunchyroll doblaje subtitulada
- n.º 40: Chainsaw Man doblaje latino Kobeni "Paola García" OR Himeno OR Kishibe voz actor latino reparto completo Audiomaster
- n.º 46: análisis Chainsaw Man referencias de películas opening KICK BACK explicado español Makima cita cine Reze (youtube.com)

**Inglés (26)**
- n.º 7: Chainsaw Man official character popularity poll results ranking Power Denji Makima Aki Reze
- n.º 10: Chainsaw Man manga chapter 39 Makima Denji movie date "one in ten" movies cinema chapter title
- n.º 11: Chainsaw Man KICK BACK opening movie references list Reservoir Dogs Pulp Fiction Texas Chainsaw Massacre shot by shot
- n.º 13: Chainsaw Man Reze Arc movie director Tatsuya Yoshihara interview character design IRIS OUT JANE DOE Kenshi Yonezu Hikaru Utada box office
- n.º 14: Chainsaw Man anime 12 ending themes list episode Vaundy CHAINSAW BLOOD Zutomayo Maximum the Hormone ano TOOBOE syudou Kanaria Eve Aimer Queen Bee PEOPLE 1 TK
- n.º 15: Chainsaw Man logo font typeface identify anime title "Chainsaw Man" font similar free
- n.º 16: Tatsuki Fujimoto paneling cinematic widescreen panels silent panels speech bubbles analysis Chainsaw Man manga film influence
- n.º 17: sketchfab Chainsaw Man Pochita chainsaw 3D model free download (sketchfab.com)
- n.º 18: sketchfab cinema seat theater chair red velvet row free download CC Attribution (sketchfab.com)
- n.º 19: velvet fabric texture CC0 red seat upholstery polyhaven OR ambientcg carpet cinema (polyhaven.com, ambientcg.com)
- n.º 21: Chainsaw Man color palette hex codes Makima Power Denji Aki hair colors
- n.º 22: Chainsaw Man most popular memes Know Your Meme Power "Denji" Makima woof Kobeni car Aki (knowyourmeme.com)
- n.º 23: tvtropes Chainsaw Man Power characters Blatant Liar Makima Denji Aki Kobeni tropes (tvtropes.org)
- n.º 24: Chainsaw Man video game Denji playable Jump Assemble OR collaboration game Chainsaw Man mobile game announced dialogue
- n.º 27: Tatsuki Fujimoto interview movies influence watches films favorite movies Chainsaw Man inspired by film
- n.º 29: artstation Chainsaw Man fan art 3D render Makima Power Reze Blender (artstation.com)
- n.º 31: Makima outfit design white shirt black tie braid ringed eyes Denji Public Safety suit Reze choker café outfit cosplay guide colors
- n.º 32: Chainsaw Man official wallpaper download 4K key visual MAPPA Crunchyroll desktop wallpaper Denji Power Aki
- n.º 33: Chainsaw Man TikTok trend viral IRIS OUT dance Reze "JANE DOE" trend Makima woof trend 2025
- n.º 38: Chainsaw Man anime criticism muted colors realistic direction fans petition Nakayama Makima voice too flat what fans disliked season 1
- n.º 39: Reze Chainsaw Man appearance design choker black short purple hair green eyes café outfit festival outfit Sugiyama movie character design
- n.º 42: Chainsaw Man The Movie Reze Arc official trailer Crunchyroll español latino tráiler oficial MAPPA (youtube.com)
- n.º 43: Chainsaw Man manga volume covers list characters volume 1 Denji volume 2 Power volume 5 Makima volume 6 Reze cover art
- n.º 44: (RECHAZADA) reddit ChainsawMan Makima Denji movie date chapter 39 what movie did they watch favorite scene cinema (reddit.com: «not accessible to our user agent»)
- n.º 45: Reze Arc movie Makima Denji movie theater date scene fans reaction best scene analysis "one out of ten" films changed my life
- n.º 47: ambientcg paper texture CC0 cardboard old paper ticket Paper 001 Paper 004 (ambientcg.com, polyhaven.com)

**Japonés (9)**
- n.º 8: チェンソーマン 第3回 人気投票 結果 1位 レゼ マキマ 票数
- n.º 12: 中山竜 監督 インタビュー チェンソーマン 実写映画 のような リアル 演出 杉山和隆 竹田悠介 美術
- n.º 20: チェンソーマン レゼ篇 聖地巡礼 カフェ 二道 モデル 電話ボックス 映画館 場所
- n.º 26: 劇場版 チェンソーマン レゼ篇 キービジュアル 第2弾 公開 描き下ろし 杉山和隆 ティザービジュアル
- n.º 28: pixiv チェンソーマン マキマ デンジ 映画館 デート イラスト (pixiv.net)
- n.º 30: チェンソーマン 声優 戸谷菊之介 楠木ともり ファイルーズあい 坂田将吾 上田麗奈 レゼ キャスト
- n.º 34: 牛尾憲輔 チェンソーマン 劇伴 インタビュー レゼ篇 音楽 ジャズ 映画館 シーン
- n.º 36: しねきゃぷしょん フォント 無料 映画字幕 風 ライセンス 商用 手書き字幕 書体
- n.º 41: 楠木ともり マキマ 演技 インタビュー 声 ささやく ファイルーズあい パワー 口調 ワシ のじゃ 演じ方

**Coreano (1)**
- n.º 9: 체인소 맨 인기투표 1회 2회 결과 파워 1위 아키 1위 레제

**Chino (1)**
- n.º 35: 电锯人 蕾塞篇 中国内地 上映 票房 玛奇玛 电影院 约会 名场面 十部电影 一部

### GitHub (sin cupo)
- Búsqueda de código: `"Makima" "Denji" extension:srt`, `extension:ass`,
  `"Makima" "Denji" "¿" extension:srt` (**sin resultados en español**),
  `"Reze" "Denji" extension:srt`, `"マキマ" "デンジ" extension:srt`,
  `"レゼ" "デンジ" extension:srt`, `"Reze" "Makima" extension:ass`.
- Bajado y usado:
  - Subtítulos de Netflix de la T1, **inglés y japonés, 12 episodios**, de
    [foxofice/sub_share](https://github.com/foxofice/sub_share/tree/master/subs_list/animation/2022).
  - Subtítulo japonés (Amazon, con acotaciones) de **la película Arco de
    Reze**, de [Ajatt-Tools/kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_movie/Chainsaw%20Man.%20Reze-hen).
  - Visto, no bajado: subtítulos japoneses de la T1 con los títulos de
    los episodios en el nombre del archivo, en
    [kitsunekko-mirror](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Chainsaw%20Man);
    subtítulos de la película en polaco
    ([harambe-subtitles/subtitles](https://github.com/harambe-subtitles/subtitles))
    y vietnamita ([HThanh-how/Subtitles](https://github.com/HThanh-how/Subtitles));
    subtítulos de Crunchyroll en [Senki3567/Drive](https://github.com/Senki3567/Drive).
  - 9 letras de [google/fonts](https://github.com/google/fonts)
    (Dela Gothic One, Zen Antique, DotGothic16, Space Mono, Metal Mania,
    Bebas Neue, Limelight, Zen Kaku Gothic New, Yuji Syuku), revisadas con
    fontTools; y el `METADATA.pb` de otras 9 (subset `latin`).

### Fuentes consultadas por tipo
- **Oficiales**: chainsawman.dog (noticias, película, staff del
  «刺客篇»), X oficial @CHAINSAWMAN_PR, página de la votación en
  shonenjump.com, blog de VIZ, canal de Crunchyroll en YouTube.
- **Entrevistas y staff**: Famitsu, UOMO, MEN'S NON-NO, Real Sound
  (guionista Hiroshi Seko), ANN y MANTANWEB (Yoshihara y Nakazono),
  Bollywood Hungama, Natalie, Lisani, QJWeb y Real Sound (Kensuke Ushio),
  CGWORLD (modelado 3D), Hominis (Tomori Kusunoki), Oricon y Futaman
  (Reina Ueda).
- **Otros idiomas**: Animate Times, Anime!Anime!, Dengeki Hobby, Dengeki
  Online, PASH! PLUS, ABEMA Times, Record China, collabo-cafe, blogs de
  peregrinación (japonés); NamuWiki, FMKorea, Daum (coreano); Wikipedia
  en chino, Douban, Zhihu, Baidu (chino).
- **Wikis**: Chainsaw Man Wiki (Fandom), Doblaje Wiki, The Dubbing
  Database, TV Tropes, NamuWiki, Wikipedia (inglés, español, chino),
  Pixiv Enciclopedia, Know Your Meme.
- **Foros y comunidades**: foro de dafont, X/Twitter (@goodschainsaw33,
  @SpyGGhetti), TikTok, MyAnimeList (foros), Letterboxd, Yahoo!知恵袋.
  **Reddit: rechazado** por la herramienta de búsqueda.
- **Arte**: Pixiv, ArtStation, Sketchfab.
- **Vídeo**: YouTube (Crunchyroll, análisis en español, clips del
  doblaje, ConCo), TikTok.
- **3D y texturas**: Sketchfab, ambientCG.
- **Letras**: Google Fonts (GitHub), Font In Logo, 1000logos, Madonomori,
  ffont.jp, goodfreefonts, Manga Font Directory.
- **Doblaje latino**: Doblaje Wiki, ANMTV, LevelUp, Código Espagueti,
  3DJuegos, Universo Nintendo, TVLaint, El Comercio (Perú), GamerFocus,
  La Verdad Noticias, Hola, eldoblaje.com, TikTok y YouTube de Jessica
  Ángeles.
- **Prensa latina (estreno)**: El Financiero, El Universal, El
  Informador, Récord, Diario de México.

### Lo que NO encontré
- Un **cuadro de diálogo propio** de la franquicia: no lo encontré (no
  hay juego publicado; *Chainsaw Man Mobile* sólo está anunciado, §13, y
  el manga usa globos corrientes).
- **La frase latina de Makima** en el cine y la ropa de la cita.
- **Qué cine real** es la sala de la cita.
- **Subtítulos o guiones en español** de la serie o la película en GitHub.
- **Minutos** de los planos del opening y de los vídeos de TikTok.
- Nada en **The Cutting Room Floor** (no hay juego) ni en **Wayback
  Machine** (sin cupo).

### Segunda pasada (25-sep-2026, red abierta)
Resumen de las bitácoras de las 4 partes (el detalle, en cada
`partes/<rol>.md`). Cada investigador tenía su cupo de ~50 búsquedas web;
usaron pocas porque la red directa dio casi todo.

**Recolector gratuito** (`recolectar.py`, 24-sep): AniList (obra, staff,
recomendaciones, fichas), Doblaje Wiki (reparto, muestras de audio,
«Datos de interés»), Fandom (imágenes y texto), Danbooru, Safebooru,
Wallhaven, Sketchfab, Openverse, Dailymotion, Internet Archive,
MusicBrainz, Steam y Reddit. Falló AnimeThemes (HTTP 522).

**Imagen** (puntos 1, 3, 15, 16, 19, 23)
- API de la wiki (inglés): tamaños de tomos 1-2 y 4-11, revistas y
  diseños del arco de Reze; wikitext del cap. 39; categoría «Chapter 39
  Images»; búsquedas «badge OR emblem Public Safety» e «insignia pin
  uniform» (sin resultado).
- API de Sketchfab: licencia y autor de 30 modelos, uno por uno.
- Alpha Coders: ahora abre (HTTP 200); tamaños y un autor del HTML.
- 12 búsquedas web (español, inglés, japonés): revistas de moda, cafés,
  Good Smile, UNIQLO UT, tramas de Fujimoto, 藤本タツキ クリップスタジオ,
  pinceles de Clip Studio y Photoshop, cosplay (Vinnegal, Wiru_Son),
  juego para móvil.
- Colores medidos con `estilo.py` y Pillow en los 5 diseños oficiales.

**Vídeo** (puntos 2, 4, 9, 10, 14)
- Internet Archive: la película (`rezearc`, 100:08, 1920×1080) y los 12
  episodios (`ep-03-cm`); usados el 1, el 2 y el 7. Fotogramas en 1080p
  con `ffmpeg` por salto HTTP, sin bajar los 5,28 GB.
- Dailymotion: tráiler `x8dsw0h`, visto entero.
- `fotogramas.py` 9 veces y `estilo.py` 5 veces; vídeos borrados tras
  sacar las hojas.
- AnimeThemes: 522 en la API y en la CDN (descartado).
- 2 búsquedas web (inglés): minuto del opening y el ending sin animación
  del ep. 1.
- Wiki: `srsearch` de «movie theater scene reference» y «シネマ座» (sin
  resultado).

**Voz y personajes** (puntos 7, 8, 12, 13, 20, 21, 22)
- Doblaje Wiki: wikitext completo de la serie y de la película.
- AniList: 14 fichas de personaje (voz «Spanish» como segunda fuente).
- Wiki en inglés: wikitext de Denji, Makima, Power, Aki, Reze, Himeno,
  Kobeni y «Popularity Polls».
- Wikipedia en inglés: «Critical reception», «Awards» y «8th Crunchyroll
  Anime Awards».
- Crank-in! (japonés): entrevista a Toya y Kusunoki (14-sep-2025).
- 9 búsquedas web (español, inglés, japonés): premios, Emilio Treviño,
  covers de «Kick Back», fandubs, ventas 2026, la frase de Makima,
  楠木ともり マキマ インタビュー.
- Arctic Shift: 2 intentos, los dos con *timeout*.

**Texto y técnica** (puntos 18, 24, 25)
- API de la wiki: `allpages`, «Public Safety Saga», «Academy Saga»,
  «Devil», «Contract», «Fiend», «Devil Hunter», «Four Horsemen»,
  «Pochita», «Denji»; búsquedas «story arc», «ripcord OR pull cord»,
  «Public Safety emblem OR symbol».
- Búsquedas web en inglés (6) y japonés (3): influencias de Fujimoto,
  CGWORLD, *color grading*, estilo del manga, Devilman, División 4;
  チェンソーマン 藤本タツキ 影響 映画, 藤本タツキ 作画 使用ソフト.
- Leídos: Anime Herald, CGWORLD partes 1 y 3, Wikipedia en inglés.
  **medium.com dio 403** (no sirvió).
- `grep` sobre los más de 130 `encargos/` para las láminas parecidas.

**Redactor**: leyó las 4 partes y los `datos-*.md` para completar;
rehízo `referencias.json` con todo lo útil de `partes/*.json` y
`datos.json` (266, las mejores primero); dejó fuera el fan art de otra
serie que coló Danbooru (etiqueta de Bakugou), fotos de Flickr sin
relación (motosierras de verdad) y un juego de Steam ajeno.

**Lo que siguió sin encontrarse en la segunda pasada**
- La frase latina de Makima en el cine (YouTube pide sesión).
- Vistas de fandubs y covers en YouTube y TikTok.
- Qué cine real inspiró シネマ座 y qué película homenajea la película de
  dentro.
- Un emblema de la Seguridad Pública (no hay escudo en la wiki).
- Una segunda fuente para el programa de dibujo de Fujimoto.
- Un *databook* con cumpleaños y comidas.
- Un *crossover* con otro juego (Fortnite, Identity V, gachas).
- Análisis de técnica en coreano o chino.
- Wayback Machine: no se usó.
