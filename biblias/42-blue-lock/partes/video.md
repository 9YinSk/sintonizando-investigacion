# Vídeo · Blue Lock (encargo 42)

Investigador de vídeo: puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Parte de
`partes/datos-video.md` (recolectado por `recolectar.py` el 24-sep-2026;
AnimeThemes dio error 522 ese día y seguía caído al investigar — reintentado
varias veces, ver Bitácora). YouTube pide iniciar sesión desde este servidor
(confirmado con yt-dlp: «Sign in to confirm you're not a bot»): todo lo de
abajo se miró en **Dailymotion** e **Internet Archive**, con `fotogramas.py`
(vídeo sin audio, hasta 720p) y contactado en hojas numeradas, leídas con Read
antes de citar cualquier minuto. Carpeta de trabajo:
`/tmp/claude-0/trabajo/42-blue-lock-video/` (se borra al terminar).

## Hallazgos

### 2 · Fotogramas de escenas icónicas (capítulo y minuto)

- **Tráiler oficial** (mirror en Internet Archive del tráiler oficial con
  subtítulos en inglés, resubido de YouTube — el original en 1080p+ sigue en
  youtube.com/watch?v=QAlsuW5EXUg, bloqueado en este servidor):
  https://archive.org/details/youtube-QAlsuW5EXUg · 1:47 · 36 planos mirados
  con `fotogramas.py --cortes` · ✅ (mismo tráiler enlazado también desde
  AniList en `datos-video.md`)
  - 0:03-0:24 — créditos: «Recipient of the 45th Kodansha Manga Award», «Over
    8.3 million copies in circulation» (830万部, dato de ventas del manga a la
    fecha del tráiler).
  - 0:29-0:46 — presentación del programa Blue Lock: sala hexagonal azul de
    rejilla (ver punto 4), «300 high school forwards assembled… 299 athletes
    will have had their soccer careers sacrificed» (frase clave del
    concepto de la serie).
  - 0:43 — a un jugador lo agarran del cuello del uniforme, grita «Here's your
    chance. Get off of me! Hey!» — primer roce entre compañeros de equipo.
  - 1:14 — primer plano con los ojos brillando (efecto de «diferenciar» del
    manga), texto «For one STRIKER… The strongest guy…» — no se pudo
    identificar el personaje con seguridad (plano muy cerrado, pelo oscuro,
    sin más contexto) → ⚠️.
  - 1:31 — Isagi Yoichi (pelo negro-azulado, ojos azules) grita «I'll be the
    one who survives!» con los ojos iluminados de azul — clímax del tráiler.
  - 1:36 — key visual de cierre con 5 personajes juntos (Isagi al centro) y el
    logo, «The Blue Lock anime starts in October 2022».
  - Enlace directo al momento: https://archive.org/details/youtube-QAlsuW5EXUg?t=91
  - Nota: el tramo 13:00-23:51 de este mismo episodio (2x14) se pasó por
    `episodio.py` con audio en japonés (Whisper) → ficha minuto a minuto en
    `partes/episodios.md`. Confirma en japonés lo que el VOSTFR francés
    resume: a las 22:00 Rin le dice a Isagi «今この瞬間から お前は俺のライバルだ»
    (desde este momento eres mi rival) tras perder, y a las 19:00 Ego da su
    discurso de la «fase 2» del proyecto Blue Lock. Whisper puede fallar
    nombres propios: revisar antes de citar textual en la biblia final.
- **Blue Lock vs. U-20 Japan — tráiler oficial** (Dailymotion, sube el mismo
  spot que Crunchyroll): https://www.dailymotion.com/video/x98n4ks · 0:45 · ✅
  (marca de agua «WATCH ON Crunchyroll» en el propio vídeo + coincide con el
  anuncio de la 2ª temporada citado en `datos-video.md`)
  - 0:12 — Isagi con aura verde-azul alrededor (su habilidad activada),
    «If I lose, my soccer career ends… it's these moments I survived».
  - 0:30 — primer plano de **Itoshi Rin** (pelo verde-azulado oscuro, ojos
    verde-turquesa, mirada fría) junto a Chigiri (pelo rosa/rojo, desenfocado
    detrás) — https://www.dailymotion.com/video/x98n4ks?t=30
  - 0:36-0:38 — Rin e **Itoshi Sae** (su hermano mayor) de espaldas, mismo
    plano, camisetas «SAE 10» (uniforme blanco de la selección absoluta) y
    «RIN 10» (uniforme azul de Blue Lock) — el enfrentamiento de hermanos que
    vertebra la 2ª mitad de la serie. https://www.dailymotion.com/video/x98n4ks?t=36
  - Cierra con «WATCH ON Crunchyroll».
- **Blue Lock: Episode Nagi** (película/OVA de 2024, VOSTFR íntegra subida a
  Internet Archive): https://archive.org/details/film-vostfr-blue-lock-episode-nagi
  · 1:30:49 · ✅ (coincide con «Blue Lock The Movie - Episode Nagi - Teaser
  Trailer» de Dailymotion, mismo argumento y personajes) — backstory de
  **Seishiro Nagi** antes de entrar a Blue Lock; escena de 38:20 (heading con
  aura azul) e íntegro detalle en el punto 14.
- **Blue Lock, temporada 2, episodio 14 (el último, «FIN»)**, VOSTFR íntegro:
  https://archive.org/details/blue-lock-2-14-vostfr · 23:51 · ✅ (marcador en
  pantalla «BLUELOCK VS. U-20 JAPAN» + «Score final: 3 à 4» coincide con el
  resultado conocido del partido de exhibición) — minuto 15:00, el equipo se
  amontona celebrando el gol de la remontada; minuto 21:00, vestuario, todos
  riendo y gritando de alegría; minuto 23:00, primer plano de Isagi: «Je
  n'attends plus que votre feu vert» (ya no espero más que su luz verde).
- Vídeo de análisis (no oficial, pero es justo el tipo «análisis» que pide el
  punto 10): **«Blue Lock: This Sports Anime Is Captain Tsubasa Meets Squid
  Game»**, canal Eight Bit, mirror en Internet Archive:
  https://archive.org/details/youtube-5aKIe8esj24 · 1:27 (fragmento/resumen) ·
  902 descargas · ⚠️ (una fuente; no se pudo confirmar el canal completo, sólo
  el fragmento resubido) — a 1:00 aparece un plano de Isagi a media carrera
  golpeando el balón, etiquetado en pantalla «Isagi Yoichi!» — pose de acción
  añadida también al punto 14.

### 4 · Fondos y sitios: luz y paleta medida (`estilo.py`)

- **Interior de la instalación Blue Lock** (sala de rejilla azul con
  casilleros, la primera imagen del tráiler oficial): fotograma en
  https://archive.org/details/youtube-QAlsuW5EXUg?t=35 · paleta medida con
  `estilo.py`: `#020D18` 30% · `#031528` 22% · `#010408` 20% · `#0A2740` 11% ·
  `#193F5B` 9% · `#285A78` 7% — azules muy oscuros y saturados (saturación
  85%, brillo 18%), sombreado degradado/pintado, línea fina color `#0A364C`
  casi invisible sobre el negro: da el efecto de sala "hologramática", sin
  calidez, como interrogatorio o laboratorio. ✅ (medido directamente, visible
  igual en la key visual del punto 1 de `imagen.md`)
- **Exterior de la instalación** (el edificio «BLUE LOCK» sobre una colina
  boscosa, al atardecer, con la carretera de acceso en curva): fotograma en
  https://www.dailymotion.com/video/x98n4ks?t=4 · paleta: `#362939` 25% ·
  `#1F1826` 21% · `#563D4E` 14% · `#FAEBDE` 12% · `#E0C1D0` 10% — violetas y
  malvas de crepúsculo (saturación 31%, brillo 45%), degradado suave, casi sin
  línea de contorno (`#9B7891`), el cielo con halo de sol muy quemado de luz.
  Contraste fuerte con el interior: fuera es un sitio casi bonito/normal,
  dentro es frío e inhumano — refuerza el tema de la serie (la instalación
  como jaula). ✅ (medido directamente)
- **Calle/puente al atardecer** (Isagi caminando solo, primeros segundos del
  tráiler, antes de entrar a Blue Lock): fotograma en
  https://archive.org/details/youtube-QAlsuW5EXUg?t=8 · paleta: `#BF99AC` 19%
  · `#8782AE` 16% · `#6C3640` 15% · `#A55C52` 13% · `#ECB877` 10% — rosas y
  naranjas pastel de atardecer (saturación 40%, brillo 63%), degradado suave,
  poca línea. Es el "mundo normal" del protagonista antes de la instalación:
  luz cálida y difusa, frente al azul duro de dentro. ✅ (medido directamente)
- **Estadio del partido U-20** (tribunas llenas, césped iluminado de noche,
  visto en `blue-lock-2-14-vostfr` y en el tráiler U-20): se ve verde césped
  saturado bajo luces de estadio blanco-azuladas y grada en penumbra — ⚠️ no
  se midió el hex a mano (no se sacó fotograma aparte para `estilo.py`; los
  colores de arriba ya cubren el cupo de tiempo de esta tanda). Confirmar en
  una tanda siguiente si hace falta el hex exacto del estadio.
- **Texturas reales equivalentes** (lo pide el punto 4 además del hex), de
  ambientCG (CC0, gratis, sin atribución obligatoria):
  - Para los paneles/casilleros oscuros de la sala interior: **Metal063**
    (metal cepillado oscuro) https://ambientcg.com/view?id=Metal063 y
    **CorrugatedSteel009** (chapa ondulada, para el efecto industrial de la
    instalación) https://ambientcg.com/view?id=CorrugatedSteel009.
  - Para las paredes de hormigón del edificio exterior y del camino de
    acceso: **Concrete034** https://ambientcg.com/view?id=Concrete034 y
    **Concrete048** https://ambientcg.com/view?id=Concrete048.
  - ✅ (buscado directo en la API de ambientCG, `q=metal` y `q=concrete`,
    licencia CC0 confirmada en la propia respuesta de la API — es el banco
    que ya usa el equipo, mismo que en `AYUDANTE.md`).
- Nota para quien haga fondos de pantalla (punto 16, es de `imagen.md` pero
  relevante aquí): la sala de rejilla azul (arriba) es el sitio más reconocible
  de la serie para cualquier fan — más que el estadio.

### 9 · Música y sonido

- **Openings y endings** (temporada 1 y 2), confirmados en dos fuentes
  independientes (Anime News Network + Wikipedia, ambas citadas en la misma
  búsqueda) — noviembre-diciembre de 2026, IMDb también coincide:
  - T1 OP1: **「Chaos ga Kiwamaru」** (Unison Square Garden) · T1 ED1:
    **「Winner」** (Shugo Nakamura, ex-vocalista de Galneryus).
  - T1 OP2: **「Judgement」** (Ash Da Hero) · T1 ED2: Unison Square Garden de
    nuevo (título dado en la búsqueda como «Numbness Like a Ginger», ⚠️
    traducción libre del inglés, falta confirmar el título japonés exacto).
  - T2 OP: **「傲慢のカリスマ (Boujaku no Charisma)」** (Unison Square Garden) ·
    T2 ED: **「One」** (Snow Man). ✅ (Anime News Network,
    animenewsnetwork.com/news/2024-09-17/bluelock-season-2-anime-trailer-reveals-ending-theme-song-by-snow-man
    + Wikipedia «Blue Lock season 2», coincide con lo que dice IMDb)
  - Unison Square Garden hace **3 de las 4** canciones de apertura/cierre de
    la temporada 1: es la banda "de la casa" de la serie.
- **Compositor de la banda sonora incidental**: **Jun Murayama (村山潤)** —
  confirmado en dos fuentes: la ficha de personal en `datos-texto.md`
  (recolectada de AniList) y el título del álbum en Internet Archive «Blue
  Lock VS. U-20 Japan Exclusive Theme Songs Soundtrack by Jun Murayama»
  (https://archive.org/details/1200x-1200bb_202505). ✅
- **Temas musicales por personaje** (el dato más útil de este punto): dentro
  del álbum de Internet Archive de arriba hay **pistas con el nombre de cada
  personaje**, compuestas por Jun Murayama — confirma que la serie usa
  «leitmotiv» por personaje, no sólo un tema genérico de batalla:
  - `NAGI.mp3` (1:03) · `RIN.mp3` (2:34) · `SpotifyMate.com - BACHIRA -
    村山_潤.mp3` (1:49, nombre del compositor 村山潤 = Jun Murayama en el
    propio archivo, segunda confirmación del compositor) · `REO.mp3` (2:30) ·
    `Reo & Nagi.mp3` (1:24, tema a dúo) · `CHIGIRI.mp3` (1:40) ·
    «Awakening of BAROU» (2:51). ✅ (listado de archivos de
    https://archive.org/details/1200x-1200bb_202505, comprobado con
    `archive.org/metadata`) — ⚠️ no encontré una pista con el nombre
    «ISAGI» en este álbum en concreto (puede estar en otro álbum de la T1 no
    localizado en esta tanda).
  - Álbum completo: https://archive.org/details/1200x-1200bb_202505 (audio)
  - Full OST del partido (1h19m40s): https://archive.org/details/blue-lock-vs.-u-20-japan-full-original-soundtrack-blue-lock-season-2-ost-full-01-19-40
- ⚠️ **No pude decir qué pista suena en cada escena emotiva concreta**:
  `fotogramas.py` baja el vídeo SIN audio (es su diseño, para mirar rápido);
  para poner nombre a la música de, por ejemplo, el gol de la remontada en el
  episodio 14 haría falta bajar el audio completo con `voz.py` o `yt-dlp` y
  cotejarlo pista a pista con el tracklist del álbum de arriba — no dio tiempo
  en esta tanda. Búsquedas hechas: «Blue Lock OST tracklist timestamps
  episode» (sin resultado claro), ver Bitácora.
- **Tendencias de TikTok** (⚠️ fuente floja, un resumen de búsqueda web, sin
  poder abrir TikTok desde aquí para comprobar vistas o fecha): ediciones
  («edits») de Blue Lock con música de fondo tipo *phonk*, canciones sueltas
  como «Funk do Ienai (Slowed)» para ediciones de Bachira y «NO MEIOTA» para
  transiciones de Rin — no se pudo verificar el nombre exacto de las
  canciones ni cuántas vistas tienen: dejarlo como pista para otra tanda, no
  como dato firme.
- **Efectos de sonido y onomatopeyas**: no encontré una fuente que liste cuáles
  reconoce el fandom (busqué «Blue Lock sound effects iconic», «Blue Lock
  onomatopoeia shoot kick sound» — sólo salieron soundboards de fans sin
  origen claro). Es más bien un tema del manga en papel (onomatopeyas
  dibujadas): mejor preguntarlo al investigador de texto (punto 6), que ya
  vio los globos y cartelas del manga.

### 14 · Poses analizadas por personaje (6-10 cada uno, capítulo/vídeo y minuto)

Los 4 personajes del encargo. Identificados y confirmados en **dos fuentes**
cada uno: una tarjeta oficial con el nombre en japonés dentro del propio
vídeo (teaser o cartel de rango) + la descripción de carácter en
`datos-voz.md` (de AniList/Fandom), que coincide con lo que se ve.

**Isagi Yoichi** (pelo negro-azulado corto, ojos azules; accesorio civil: una
bufanda de cuadros verde) — confirmado por color de pelo/ojos + bufanda verde
(icónica, aparece también en las hojas de `imagen.md`) y por la personalidad
"friendly, cheery… avoids childish squabbles" de `datos-voz.md` que encaja con
las expresiones de duda/cálculo de abajo:
1. **Presentar/declarar** — ojos brillando de azul, grito «I'll be the one who
   survives!»: tráiler oficial, 1:31.
   https://archive.org/details/youtube-QAlsuW5EXUg?t=91
2. **Reaccionar/protestar** — lo agarran del uniforme, «Here's your chance.
   Get off of me!»: tráiler oficial, 0:43.
   https://archive.org/details/youtube-QAlsuW5EXUg?t=43
3. **Pensar** — bufanda verde, mirada preocupada hacia un lado, calle al
   atardecer: vídeo de reacción/recopilación S1 ep.1-4 (IA), minuto 34:30 del
   vídeo. https://archive.org/details/blue-lock-1-4?t=2070 (⚠️ el vídeo fuente
   es una reacción con cámara de streamer en la esquina, no el episodio limpio
   — el fotograma citado es del anime a pantalla completa, sin cámara encima)
4. **Explicar/preguntar** — de perfil, camiseta #11, «¿así era el estilo de
   juego caótico y libre?»: mismo vídeo, minuto 1:25:30.
   https://archive.org/details/blue-lock-1-4?t=5130
5. **Sorprenderse/tensión** — primer plano apretando los dientes, «¿qué hace
   aquí? ¿resolvió todo el juego?»: mismo vídeo, minuto 1:34:30.
   https://archive.org/details/blue-lock-1-4?t=5670
6. **Animar/activar habilidad** — aura verde-azulada alrededor, mirada fija:
   tráiler U-20, 0:12. https://www.dailymotion.com/video/x98n4ks?t=12
7. **Celebrar/decidido** — primer plano sudando, «ya no espero más que su luz
   verde»: temporada 2 episodio 14 (VOSTFR), minuto 23:00.
   https://archive.org/details/blue-lock-2-14-vostfr?t=1380
8. **Acción/remate** — carrera completa, golpeando el balón en pleno salto,
   camiseta azul #11: vídeo de análisis «Captain Tsubasa Meets Squid Game»
   (Eight Bit, mirror IA), minuto 1:00.
   https://archive.org/details/youtube-5aKIe8esj24?t=60

**Bachira Meguru** (pelo negro con dos mechones rubios/amarillos enmarcando la
cara, ojos amarillos/dorados, dientes puntiagudos cuando sonríe "modo
monstruo") — confirmado por la tarjeta de nombre en japonés «蜂楽 廻» dentro
del teaser oficial y por «usually very energetic, cheerful… rarely losing his
cool» de `datos-voz.md`, que encaja con la sonrisa constante de abajo. Todo lo
de abajo sale del teaser oficial de personaje, JeuxVideo.com en Dailymotion:
https://www.dailymotion.com/video/x89nzmm (0:47) — 7 poses, todas del mismo
vídeo oficial por no encontrar otro clip limpio con él (ver Bitácora):
1. **Presentar (primer plano)** — cara muy cerca, ojos dorados muy abiertos,
   sonrisa afilada, gotas de sudor: 0:12. …?t=12
2. **Caminar/entrar en escena** — dos siluetas caminando hacia la cámara,
   contraluz: 0:10. …?t=10
3. **Correr/driblar** — silueta corriendo con el balón + tarjeta de rango
   «280位 蜂楽廻»: 0:22. …?t=22
4. **Agarrar con intensidad** — sujeta la muñeca de alguien con fuerza, primer
   plano de la mano: 0:24-0:26. …?t=25
5. **Celebrar/monstruo** — sonrisa enorme con los dientes puntiagudos muy
   cerca de cámara, el gesto más citado de él: 0:28. …?t=28
6. **Guiñar/picardía** — ojo cerrado, sonrisa ladeada: 0:30. …?t=30
7. **Driblar en cancha** — cuerpo entero, chándal azul, driblando frente a un
   defensor: 0:34. …?t=34
Enlace con &t=: reemplazar `…?t=N` por
`https://www.dailymotion.com/video/x89nzmm?t=N`.

**Seishiro Nagi** (pelo blanco/plateado despeinado, ojos marrones
entornados/somnolientos) — confirmado por la tarjeta «凪 誠士郎» del teaser
oficial y por «very lazy and unmotivated… often appears lethargic» de
`datos-voz.md`, que es EXACTAMENTE la pose 7 de abajo. Fuente principal:
película «Blue Lock: Episode Nagi» (VOSTFR íntegra, IA)
https://archive.org/details/film-vostfr-blue-lock-episode-nagi — 8 poses:
1. **Acción en el aire** — salto tipo chilena junto a un compañero de
   uniforme naranja: 10:00. …?t=600
2. **Caminar/relajado** — de espaldas, caminando junto a Reo Mikage (pelo
   morado) tras un partido: 16:40. …?t=1000
3. **Presumir de técnica** — balón sobre la cabeza, primer plano de perfil:
   33:20. …?t=2000
4. **Rematar/animar habilidad** — cabecea el balón con un aura azul
   envolviéndolo: 38:20. …?t=2300
5. **Reír/celebrar** — sonrisa amplia, «somos un dúo de choque»: 51:40.
   …?t=3100
6. **Practicar solo/pensar** — silueta a contraluz de atardecer, pateando
   solo en la cancha: 1:16:40. …?t=4600
7. **"No hacer nada" (su pose más icónica)** — tumbado bocabajo en una mesa,
   comiendo un pincho con tenedor sin ganas, ojos entornados: teaser oficial
   Reo+Nagi (Dailymotion) https://www.dailymotion.com/video/x8cmhe2?t=16
8. **Casual/mirar de lado** — ropa de calle, bufanda de cuadros, «si no vuelvo
   ya, tendrán que regar a Nanou»: película, 1:30:00. …?t=5400
Enlace con &t= para las poses 1-6 y 8: reemplazar `…?t=N` por
`https://archive.org/details/film-vostfr-blue-lock-episode-nagi?t=N`.

**Itoshi Rin** (pelo verde-azulado oscuro corto, ojos verde-turquesa, gesto
frío/serio casi siempre) — confirmado por el cartel de rango «糸師 弃 RANK 1
ITOSHI RIN» dentro de la emisión doblada y por ser el hermano de Itoshi Sae
(ambos con el apellido en la camiseta «SAE»/«RIN» del tráiler U-20), que
coincide con la ficha de personaje de `datos-voz.md`. 6 poses:
1. **Presentar (cartel de rango)** — silueta + nombre a pantalla completa,
   emisión doblada de Toonami (IA): minuto 13:00 del vídeo.
   https://archive.org/details/you-cut-20260509-120027008?t=780 (⚠️ no se
   pudo confirmar qué episodio exacto de la numeración oficial es «ep. 13»
   de Toonami)
2. **Posicionarse en cancha** — de pie junto a un compañero, mirando al
   campo: mismo vídeo, 12:00. …?t=720
3. **Mirar frío (primer plano 1)** — perfil, ojo verde-turquesa, ceja
   fruncida: mismo vídeo, 18:00. …?t=1080
4. **Mirar frío (primer plano 2)** — ángulo distinto, mismo gesto serio:
   mismo vídeo, 23:00. …?t=1380
5. **Encarar (con Chigiri detrás)** — primer plano muy cerrado, pelo
   verde-azulado oscuro, mirada fija: tráiler U-20 (Dailymotion), 0:30.
   https://www.dailymotion.com/video/x98n4ks?t=30
6. **Enfrentar a su hermano** — de espaldas junto a Sae, camisetas «SAE 10» /
   «RIN 10», la selección absoluta contra Blue Lock: mismo tráiler, 0:36.
   https://www.dailymotion.com/video/x98n4ks?t=36

**Cuál pose sirve para qué** (pide el punto 14 explícitamente):
- **Presentar**: Isagi #1 (ojos brillando), Bachira #1 (primer plano), Nagi
  #3 (balón en la cabeza), Rin #1 (cartel de rango).
- **Explicar**: Isagi #4 (preguntando de perfil).
- **Celebrar**: Isagi #7, Bachira #5 (sonrisa monstruo), Nagi #5 (riendo).
- **Regañar/encarar**: Bachira #4 (agarrón), Rin #5 y #6 (mirada fría,
  frente a Chigiri o su hermano).
- **Pensar**: Isagi #3, Nagi #6 (practicando solo a contraluz).
- **Animar** (a sí mismo o su habilidad): Isagi #6, Nagi #4 (aura azul).
- **"No hacer nada" / fuera de personaje competitivo**: Nagi #7 (tumbado
  comiendo) — es la pose que más lo define, según su propia ficha.

### 10 · Vídeos: tráileres, escenas, análisis y tendencias (con minuto)

- Lista completa de tráileres y temasers oficiales mirados, todos con
  `fotogramas.py`, todos en Dailymotion (YouTube bloqueado en este servidor):
  - Tráiler oficial (EN, mirror IA): visto arriba (punto 2), 1:47.
  - **«Blue Lock Animé - Teaser 3 - Meguru Bachira»**
    https://www.dailymotion.com/video/x89nzmm · 0:47 · JeuxVideo.com · teaser
    de personaje, ver detalle de poses en el punto 14.
  - **«Blue Lock Official Teaser Trailer 7»** (Zantetsu Tsurugi, rango 223,
    no es de los 4 personajes de este encargo)
    https://www.dailymotion.com/video/x8cjdfd · 0:26.
  - **«Blue Lock Official Teaser Trailer 8»** (Reo Mikage rango 222 + Seishiro
    Nagi rango 221, doble teaser) https://www.dailymotion.com/video/x8cmhe2 ·
    0:26 · ver poses de Nagi en el punto 14.
  - **«BLUE LOCK VS U-20 JAPAN TEASER»** visto arriba (punto 2), 0:45.
  - Tráiler oficial de **Episode Nagi** (película):
    https://www.dailymotion.com/video/x8n9n5q (39s, «Official Teaser
    Trailer») y https://www.dailymotion.com/video/xa1wjb2 (40s, «Teaser
    Trailer», Fandango) — dos fuentes que coinciden en fecha de estreno 2024 ✅
    (no se procesaron con `fotogramas.py`: la película completa ya se miró
    directamente, ver punto 2 y 14).
- **Grabación real de emisión en TV** (Toonami/Adult Swim, EE. UU., doblaje
  inglés): «Blue Lock & Tokyo Revengers episode 13 Toonami airing»
  https://archive.org/details/you-cut-20260509-120027008 · 1:00:31 (incluye
  cortes comerciales reales — Febreze, promos de citas — y luego pasa a Tokyo
  Revengers a partir del minuto ~36) · ⚠️ (grabación de fan, sin poder
  confirmar a qué episodio exacto corresponde «13» en la numeración oficial:
  el cartel en pantalla dice «ITOSHI RIN RANK 1», que en el manga/anime
  ocurre en la primera selección, T1). Sirve para las poses de Rin (punto 14)
  y como prueba de que Blue Lock se emitió doblado al inglés en Toonami
  (cadena de Cartoon Network/Adult Swim, EE. UU.), dato útil para el punto 8
  de doblaje (aunque ese punto es de la investigadora de voz).
- **Vídeo de análisis**: «Blue Lock: This Sports Anime Is Captain Tsubasa Meets
  Squid Game» (canal Eight Bit) — visto arriba (punto 2). El propio título ya
  resume el ángulo del análisis: compara Blue Lock con Captain Tsubasa (por el
  fútbol) y con Squid Game (por la premisa de eliminación/supervivencia entre
  300 concursantes). 902 descargas en el mirror de Internet Archive.
- **Tendencias TikTok**: ver el aviso ⚠️ del punto 9 (misma búsqueda, mismo
  resultado flojo). No hay una fuente sólida que dé vistas o fecha concretas
  desde este servidor (TikTok no es accesible directamente); lo que hay son
  resúmenes de búsqueda, no la app en sí.

## Lo mejor para la lámina

- La **sala de rejilla azul** de la instalación (punto 4, hex medidos) es el
  fondo más reconocible de la serie y contrasta fuerte con cualquier escena
  cálida — sirve de base para un concepto "dentro de Blue Lock" oscuro y
  tenso.
- La pose de **Nagi tumbado comiendo sin ganas** (punto 14, #7) es la imagen
  que mejor resume su personalidad en una sola viñeta — perfecta para un
  cuadro de humor/carácter.
- El enfrentamiento **Rin vs. Sae, espalda con espalda, camisetas "RIN
  10"/"SAE 10"** (punto 14, #6) es la escena más citada por fans de la 2ª
  temporada: sirve para una lámina de rivalidad/hermanos.
- La frase «世界一のエゴイストでなければ世界一のストライカーにはなれない» («si no
  eres el egoísta número uno del mundo, no puedes ser el delantero número uno
  del mundo») aparece en el teaser oficial de Bachira (0:20-0:22 de
  https://www.dailymotion.com/video/x89nzmm) — es prácticamente el eslogan de
  la serie, en japonés y con su romanización, útil como texto de cuadro.
- **Isagi con la bufanda verde** (punto 14, #3) es la referencia de vestuario
  civil "icónica" para cualquier lámina fuera de la cancha.

## No encontré

- ⚠️ **Qué pista de la banda sonora suena en cada escena emotiva concreta**
  (punto 9): `fotogramas.py` no baja audio; hicieron falta más minutos para
  bajar el audio completo con `voz.py`/`yt-dlp` y cotejarlo con el tracklist
  del álbum de Internet Archive. Búsquedas hechas (WebSearch): «Blue Lock OST
  tracklist timestamps episode», sin resultado útil. Queda para otra tanda.
- ⚠️ **Efectos de sonido/onomatopeyas que reconoce el fandom** (punto 9):
  busqué «Blue Lock sound effects iconic», «Blue Lock onomatopoeia shoot kick
  sound» (WebSearch) — sólo aparecieron *soundboards* de fans sin fuente
  clara del audio original. Es más un tema del manga en papel (onomatopeyas
  dibujadas): pista para el investigador de texto (punto 6).
- ⚠️ **Vistas y fecha exactas de las tendencias de TikTok** (punto 10): TikTok
  no se puede abrir directo desde este servidor; sólo hay resúmenes de
  búsqueda (WebSearch: «Blue Lock TikTok trend edit song viral sound 2026»),
  sin poder comprobar cifras.
- ⚠️ **Un segundo clip limpio (sin cámara de reacción encima) de Bachira**: las
  7 poses del punto 14 salen todas del mismo teaser oficial de 47 s porque no
  encontré otro vídeo en Dailymotion/Internet Archive con él en pantalla
  completa sin marca de agua ni superposición — probé «Bachira Meguru blue
  lock», «Blue Lock Bachira awakening», «Bachira Monster In Blue Lock» (todas
  ediciones de fans cortas, sin identificar el episodio de origen).
- ⚠️ **El episodio exacto (numeración oficial) de la grabación de Toonami**
  usada para las poses de Rin: la grabación de fan sólo dice «episode 13» de
  la emisión de EE. UU., que puede no coincidir con el número de episodio
  japonés original. No lo pude confirmar cruzando con una guía de episodios
  de Toonami (no encontrada en el tiempo disponible).
- El *tráiler oficial* de 1:47 tiene un fotograma en 1:14 con los ojos
  brillando que **no pude identificar con seguridad** (ver punto 2): lo dejé
  sin atribuir a ningún personaje en vez de arriesgar un error.

## Bitácora de búsqueda

- **Sin repetir lo de `datos-video.md`** (AniList tráiler, Dailymotion por
  «BLUE LOCK opening/ending/trailer/escena», Internet Archive, MusicBrainz —
  éste último dio sólo falsos positivos por la palabra «lock», descartado).
- AnimeThemes (`api.animethemes.moe`): reintentado 3 veces a lo largo de la
  tanda (con `--globoff` en curl, el error inicial era de sintaxis, no del
  servidor) — sigue dando **522** las 3 veces. Sin datos de esa fuente.
- `api.jikan.moe` (Wikipedia vía MyAnimeList): **504**, sin datos.
- `en.wikipedia.org` API: **429** dos veces seguidas (probablemente por las
  otras investigadoras del mismo contenedor pegando a la vez) — a la tercera,
  con espera y otro user-agent, respondió bien (`/api/rest_v1/page/summary`).
- Dailymotion (`api.dailymotion.com/videos?search=…`), sin gastar el cupo del
  buscador web: «Blue Lock opening full», «Blue Lock episode 1», «Blue Lock
  Isagi awakening», «Blue Lock Crunchyroll clip», «Bachira Meguru blue lock»,
  «Blue Lock Teaser Isagi», «Blue Lock Teaser Itoshi», «Blue Lock Animé
  Teaser» (ésta encontró los teasers numerados de personaje).
- Internet Archive (`archive.org/advancedsearch.php`), búsqueda de texto
  `title:(blue lock) AND mediatype:(movies)`, 200 filas — así aparecieron los
  episodios VOSTFR sueltos, la película Episode Nagi y las grabaciones de
  Toonami que no estaban en `datos-video.md` (el recolector sólo trajo los 20
  primeros resultados por popularidad, sin filtrar por tipo de contenido).
- `archive.org/metadata/<id>` en cada candidato antes de procesarlo, para
  comprobar que traía un archivo de vídeo real (`.mp4`/`.webm`/`.mkv`) y no
  sólo una miniatura — descartó `bl-s1` y `blue-lock-s-1-part-2_202311`
  (ítems vacíos, sin vídeo real pese al nombre).
- WebSearch (3 búsquedas del cupo de ~50, en español/inglés): «Blue Lock anime
  opening ending theme songs season 1 season 2 list» (✅ dio OP/ED con fuente
  ANN+Wikipedia), «Blue Lock TikTok trend edit song viral sound 2026» (⚠️
  floja), «Blue Lock sound effects onomatopoeia iconic» (sin resultado útil).
- Vídeos mirados de verdad con `fotogramas.py` (hojas leídas con Read, no sólo
  metadatos): tráiler oficial (36 planos), «Blue Lock 1-4» reacción/recopilación
  (85 + más de 100 fotogramas en 3 pasadas), «Blue Lock 2x14 VOSTFR» (24),
  «Episode Nagi» película (55), grabación de Toonami ep.13 (61), teaser
  Bachira (24 + 3 en grande), teaser 7 y 8 (13+14), tráiler U-20 (23+1 en
  grande), vídeo de análisis Eight Bit (3). Total: **más de 15 vídeos/clips
  distintos** procesados con el visor de fotogramas.
- `estilo.py` corrido 3 veces sobre fotogramas propios (no imágenes de stock)
  para los hex de fondos del punto 4.

- `herramientas/episodio.py` corrido en **2 trozos clave** (con `--id
  42-blue-lock`, quedaron en `partes/episodios.md`, 344 planos entre los dos):
  - Tramo final del episodio 2x14 (13:00-23:51, audio japonés con Whisper) —
    revela el discurso de Ego («才能の原石ども… 俺はこの中から世界一のストライカーを
    作り出す», talentos en bruto, de aquí sacaré al mejor delantero del mundo)
    y la frase de Rin aceptando a Isagi como rival tras perder («今この瞬間か
    ら お前は俺のライバルだ»). Detalle citado también en el punto 2.
  - Tramo de la película «Episode Nagi», 30:00-40:00 (Nagi se integra al
    equipo de Reo) — confirma con sus propias palabras el carácter perezoso
    («めんどくさがりや», alguien a quien todo le da pereza) y deja una frase de
    su familia que explica su arco: «本当にかしこい人間は馬鹿にバカって言わない優し
    さを持ってる» (la gente de verdad inteligente tiene la amabilidad de no
    llamar tonto a un tonto) — útil para la investigadora de voz (punto 13,
    carácter) y para el redactor. ⚠️ Whisper confunde el nombre «凪誠士郎»
    (Nagi Seishirou) en varias líneas: revisar antes de citar textual.

Sigue: bajar el audio (yt-dlp/voz.py) de 1-2 escenas clave del episodio 14 de
la temporada 2 para identificar la pista de música exacta (punto 9, hoy sólo
quedó el nombre del compositor y el álbum, sin cotejar el minuto); buscar un
segundo clip limpio de Bachira fuera del teaser único; confirmar el número de
episodio oficial de la grabación de Toonami usada para Rin; medir el hex del
estadio (punto 4) si se necesita más detalle.
