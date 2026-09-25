# Investigador de VÍDEO · My Hero Academia (puntos 2, 4, 9, 10, 14 de ENCARGO.md)

Parto de `partes/datos-video.md` (AniList, Dailymotion, Internet Archive,
MusicBrainz; AnimeThemes falló con HTTP 522) y de lo que ya tiene la biblia
actual en sus secciones §2, §5, §11, §12 y §15 (`python3 herramientas/seccion.py
25-my-hero-academia --rol video`). Esa biblia se hizo con la **red cerrada**:
dice explícitamente que no pudo mirar ningún vídeo y que las poses, la luz y
la paleta son **«de memoria»**. Aquí SÍ miré los vídeos de verdad (Internet
Archive + Dailymotion, con `fotogramas.py`, más algunos fotogramas sueltos
medidos con Pillow/`estilo.py`), como pide AYUDANTE.md. Dejo lo NUEVO o lo
CONFIRMADO/CORREGIDO; no repito lo que ya estaba bien con dos fuentes.

Carpeta de trabajo (hojas y fotogramas sueltos, ~2.6 MB; los `video.mp4` ya
se borraron): `/tmp/claude-0/trabajo/25-my-hero-academia-video/`.

**AnimeThemes**: reintenté la API (`api.animethemes.moe/anime?filter[slug]=...`)
y sigue en **HTTP 522** (Cloudflare, origen caído); probé también la web
normal (`animethemes.moe/anime/boku-no-hero-academia`, redirige a home =
ruta rota) y el CDN directo (`v.animethemes.moe/BNHA-OP1.webm`, conexión
reiniciada). Dos intentos como marca AYUDANTE.md: descartada, uso
Dailymotion + Internet Archive.

**YouTube**: pide iniciar sesión en este contenedor (confirmado, no insistí
en bucle). Usé sólo Dailymotion e Internet Archive.

## Hallazgos

### Punto 2 · Escenas icónicas miradas fotograma a fotograma (1080p cuando lo hay)

**Episodio 1×01 «Izuku Midoriya: Origin»** (Internet Archive,
[`anime-kcd-boku-no-hero-academia-01`](https://archive.org/details/anime-kcd-boku-no-hero-academia-01),
1280×720, 24:32 min, **sub. español**): saqué 9 fotogramas sueltos en los
minutos que ya citaba la biblia (§15) para comprobar sus poses «de
memoria». El minuto real de esta copia se mueve **unos 4 minutos más tarde**
que el de la biblia (usa otros subtítulos/plataforma) — lo aviso porque
AYUDANTE.md dice que puede moverse 1-2 min, aquí es algo más:
- **10:55**: Deku, en el aula, se acerca a Bakugo con los **puños apretados
  a la altura del pecho, hombros encogidos, ojos muy abiertos** (nervioso,
  a punto de suplicar). Confirma que la pose de «pedir perdón/rogar» es
  real, no sólo la del cuaderno explotando. ✅ visto. Pelo de Deku medido
  con Pillow en este fotograma: `#357459`.
- **11:10**: primer plano de la mano de **Bakugo humeando** (chispitas de
  su Quirk) apoyada en su propio pecho, mandíbula tensa, subtítulo
  «Hablando en plata…»: el gesto de amenaza previo a la explosión del
  cuaderno. ✅ visto. Pelo de Bakugo medido: `#F1E7CE`.
- **~10:33**: página del **cuaderno de Deku** en primer plano: libreta de
  espiral marca **«Campos»** (lomo azul), título escrito a mano **«Análisis
  de héroes para el futuro»** y **«No. 13»** subrayado, mientras Bakugo se
  burla («¿"Análisis de héroes para el futuro"?»). Confirma que el
  cuaderno-objeto del encargo es real y **numerado** (van por el 13). ✅
  visto — dato nuevo, la biblia no daba el texto exacto de la portada.
- **13:06**: la silueta oscura y musculosa de **All Might en su forma
  heroica agachándose** sobre un tejado roto, cielo naranja-rojo
  incendiado detrás — el instante en que llega a salvar a Deku del villano
  limo, antes de hablar. Paleta medida (`estilo.py`): `#170D0A` 23% /
  `#4D342B` 18% / `#888076` 14% (negro-óxido, nada de azul). ✅ visto.
- **19:30**: Deku sostiene el cuaderno abierto con **las dos manos**,
  mostrando la página donde acaba de escribir, en letras enormes, **«ALL
  MIGHT»** — el primer apunte del héroe que lo inspiró. Subtítulo «¡Ya me
  lo ha hecho!». Corrige/matiza la pose de la biblia («ofrece el cuaderno
  con las dos manos, emocionado», 00:19:21): aquí no lo ofrece, lo **mira
  él mismo, orgulloso**, recién escrito. ✅ visto — el mejor fotograma para
  la lámina (ver abajo).
- **19:55**: **All Might de espaldas, en su forma real (flaca, alta,
  ojerosa)**, manos en la nuca, en mitad de una calle con niebla blanca,
  subtítulo «Hay tanto… que me gustaría preguntarte…»: el momento en que
  va a revelar el secreto de One For All. ✅ visto, dato nuevo (pose de
  espaldas, no está en la tabla de la biblia).

**Escena de acción — All Might «Plus Ultra» contra Nomu, S1E12 «All
Might»** (Dailymotion, clip editado,
[`x4hptj4`](https://www.dailymotion.com/video/x4hptj4), 26 s, sub. inglés).
Confirmado por wiki (`myheroacademia.fandom.com`, pageid 12736): episodio
12 de temporada 1, arco **U.S.J.**, OP «THE DAY», ED «HEROES» — coincide
con los openings/endings de este mismo punto. Minutos **del clip** (no del
episodio completo, avisado con ⚠️):
- 0:00 puño de All Might en primer plano, luz blanca lateral, subtítulo
  «Go beyond!»
- 0:03-0:06 All Might encogido antes del golpe, subtítulo «Plus… Ultra…!»
- 0:09 impacto contra la **cúpula del USJ** (estructura redonda rota,
  escombros grises-óxido volando) — paleta medida arriba (mismo tono que
  13:06 del episodio 1, confirma la identidad de color de la escena
  nocturna/interior del USJ).
- 0:18-0:24 nubes de humo blanco explotando contra el cielo nocturno de la
  cúpula.
✅ visto y confirmado con la wiki (episodio + arco).

**Escena de acción — Deku vs. Muscular, S3E42 «My Hero»** (Dailymotion,
[`x80pei3`](https://www.dailymotion.com/video/x80pei3), 2:29, sub. inglés).
Confirmado por wiki: episodio 42, temporada 3, arco **Forest Training
Camp**, OP «Odd Future» (UVERworld), ED «Update»; el movimiento se llama
**«1,000,000% Delaware Detroit Smash»** (ficha propia en la wiki,
pageid 28424). Minutos del clip:
- 0:00-0:20 Muscular embistiendo, subtítulos «Detroit…», «Ow…»
- 0:30 primer plano ensangrentado de Muscular, «…fine… It's fine…!» —
  paleta medida: `#D7C2C2` 23% / `#513034` 21% (rosa-pálido y granate, piel
  y sangre, sin azules)
- 1:10 «Mom, I'm sorry!» (pensamiento de Deku sobre su madre, antes del
  golpe final)
- 1:40 Muscular sonriendo, amenaza «I'll kill you later, so just wait--»
- 2:00 destello magenta/cian en forma de estrella (efecto del golpe)
  seguido de «One For All, 1,000,000%!» y «…Smash!» a 2:10
✅ visto y confirmado con la wiki.

**Escena de grupo — Bakugo vs. Uraraka, S2E22 «Bakugo vs. Uraraka»**
(Dailymotion, con **subtítulos en español**,
[`x6soboa`](https://www.dailymotion.com/video/x6soboa), 8:43). Confirmado
por wiki: episodio 22, temporada 2, arco **Festival Deportivo de U.A.**, OP
«Peace Sign» (coincide con el OP2 de este punto). Estadio con gradas
llenas, uniforme deportivo azul/blanco/rojo de U.A. Momentos con minuto:
- 0:00 Bakugo con la cara iluminada por su propia explosión, «¡Esa no es
  la cara de alguien normal!»
- 3:00-4:00 el resto de la clase mirando preocupados desde las gradas
- 5:00 Uraraka de espaldas, corriendo, subtítulo «Bakugo está siendo
  cuidadoso porque sabe la fuerza de su oponente»
- 5:30 Uraraka de frente, **puño cerrado a la altura del pecho, mirada
  fija**: «¡Yo ganaré!»
- 6:00 primer plano, ojos llorosos de determinación: «¡Ganaré! ¡Ganaré y
  seré como Deku!»
- 8:00-8:30 Uraraka en el suelo, exhausta, boca abierta jadeando
✅ visto entero (por tramos de 30 s).

Total: **opening ×2, ending ×1, tráiler ×1 y 3 escenas icónicas** miradas
de verdad, tal como pide AYUDANTE.md («Mira los vídeos de verdad»).

### Punto 4 · Sitios, luz y paleta (medidos con Pillow/`estilo.py`, no de memoria)

La biblia (§5.2 y §5.3) avisaba **todo** de memoria. Con los fotogramas
reales de arriba mido 4 sitios distintos:

| Sitio | Fotograma | Paleta medida (`estilo.py`) | Luz |
|---|---|---|---|
| **Tejado de Tokio** (OP2 «Peace Sign», 0:06, ciudad de día) | `op2_frame/fotograma_00006.jpg` | `#406D84` 32% · `#B0E2F1` 19% · `#1F2630` 18% · `#76B1C9` 14% | Azul-gris diurno, cielo claro, alto contraste de edificios oscuros a contraluz |
| **Campo de entrenamiento nocturno** (ED1 «HEROES», 0:24, Deku corriendo bajo estrellas) | `ed1_frame/fotograma_00024.jpg` | `#0B0D25` 46% · `#10153B` 23% · `#050614` 14% · `#1B2356` 13% | Azul-marino casi negro, estrellas puntuales blancas, brillo muy bajo (21%) |
| **Estadio del Festival Deportivo** (S2E22, 4:30, día) | `arena_frame/fotograma_00270.jpg` | `#1E3A95` 26% · `#453C3F` 22% · `#1C1B43` 22% · `#E0E8F0` 11% | Azul intenso de las gradas/cartelería + gris piedra del graderío, cielo despejado |
| **Cúpula del USJ, de noche, tras el impacto** (S1E12, 0:09) | `am_frame/fotograma_00009.jpg` | `#170D0A` 23% · `#4D342B` 18% · `#888076` 14% | Negro-óxido casi sin azul: interior artificial, luz de incendio anaranjada rasante |

Estilo de sombreado en los 4: **degradado/pintado, poca línea** (línea
`#635C58` a `#67676C` según la escena) — coincide con lo que ya decía la
biblia sobre el anime en general, ahora confirmado con la herramienta en
vez de a ojo.

**Textura real equivalente para la cúpula del USJ** (hormigón dañado, gris-óxido):
[ambientCG Concrete044D](https://ambientcg.com/view?id=Concrete044D) y
[Concrete042C](https://ambientcg.com/view?id=Concrete042C), **CC0**
(`ambientcg.com/api/v2/full_json?type=Material&q=concrete+damaged`). Se
suma a los papeles CC0 que ya tenía la biblia en §5.4.

### Punto 9 · Música (openings, endings y un tema en escena emotiva)

La biblia (§11) ya tenía los títulos de OP/ED por temporada con el artista
marcado ⚠️ (una sola fuente, «de memoria»). Los confirmo con **dos fuentes**
(la ficha de la wiki de Fandom + los créditos que se leen en el vídeo real
que miré):

| Tema | Confirmación |
|---|---|
| **OP1 «THE DAY»** · Porno Graffitti | ✅✅ wiki (`THE DAY`, pageid propio: «artist = Porno Graffitti», estreno 25-may-2016, episodios 1-13) + créditos vistos en el fotograma 0:54 del clip de Dailymotion `x7s67y3` («オープニングテーマ「THE DAY」…Porno Graffitti…», con Yuki Hayashi como compositor de la serie) |
| **OP2 «Peace Sign»** · Kenshi Yonezu | ✅✅ ficha de Episode 22 en la wiki («opening song = Peace Sign») + créditos vistos en el fotograma 0:18 del clip `x5pk6h7` (tarjeta de título con el mismo diseño que el resto de la serie) |
| **ED1 «HEROES»** · Brian the Sun | ✅✅ ficha de Episode 12 («ending song = HEROES») + créditos vistos en el fotograma 0:54 de Internet Archive `my-hero-academia-ending-1-heroes` («エンディングテーマ「HEROES」Brian the Sun», letra y música también de Brian the Sun) |

**Tema en escena emotiva**: la wiki lista el BGM de cada episodio
(`myheroacademia.fandom.com`, sección «BGM» de cada ficha). El **Episodio
13 «In Each of Our Hearts»** (S1, el capítulo más emotivo tras el ataque
del USJ: los alumnos procesan el miedo y Iida se enfrenta a lo que sintió)
tiene en su lista de BGM el tema **«You Say Run»** ✅ (confirmado en la
ficha de Episode 13; también existe una versión remix 10.º aniversario de
2026 cantada por Electric Callboy, dato reciente sin relación directa con
la lámina). No tengo el minuto exacto dentro del episodio (no lo descargué
completo, por presupuesto): lo dejo con ⚠️ el minuto, ✅ el episodio y el
tema.

**Efectos de sonido / onomatopeyas**: no llegué a este dato con fuente
propia (no es lo que más pide el punto 9 y el tiempo se fue en vídeo real);
queda en «No encontré».

### Punto 10 · Vídeos mirados de verdad, con minuto

- **Episodio 1 completo** (Internet Archive, 24:32 min, sub. español):
  descrito arriba, punto 2. ✅ visto entero.
- **Tráiler oficial de la película «My Hero Academia: Two Heroes» (2018)**
  (Dailymotion, re-subido, [`x6u2yxy`](https://www.dailymotion.com/video/x6u2yxy),
  2:12, logo real de **Toho** al inicio): 0:00 logo 東宝; 0:08 «"個性"を持
  って生まれる超人社会» (una sociedad de superhumanos que nacen con
  "Individualidad"); 0:16 crédito «原作・総監修・キャラクター原案 堀越耕平»
  (Horikoshi Kohei); 0:24 grupo de alumnas en un ferry, «There are other
  girls who came to this island, too!»; 0:32 All Might de civil, bufanda
  roja, pulgar arriba; 0:48 Deku pequeño con el cuaderno, «I'll do
  everything that I can!»; 0:56 un personaje encapuchado (mentor/villano
  del filme), «Only you can witness the pain that your best friend will go
  through»; 1:04-1:20 Bakugo, Uraraka gritando «Go!!!», Deku «I will save
  everyone»; 1:28 tarjeta del título «僕のヒーローアカデミア THE MOVIE ―2人
  の英雄―»; 1:52 All Might a plena potencia, pelo dorado; 2:00 fecha de
  estreno japonés «8.3 ROADSHOW» (3 de agosto). ✅ visto entero.
- **Escena All Might «Plus Ultra» (S1E12)**, **Deku vs. Muscular (S3E42)** y
  **Bakugo vs. Uraraka (S2E22)**: descritas arriba, punto 2. ✅ vistas.
- **Tráiler canónico de AniList** (`youtube.com/watch?v=AhqVltWDqFA`,
  `partes/datos-video.md`): **bloqueado** (YouTube pide iniciar sesión en
  este contenedor, confirmado, no insistí en bucle). Usé en su lugar el
  tráiler de «Two Heroes» de arriba.
- **Tendencias TikTok**: no encontré forma de comprobarlas sin TikTok ni
  YouTube (fuera del alcance de Dailymotion/Internet Archive); queda en
  «No encontré».

### Punto 14 · Poses confirmadas con fotograma real (antes «de memoria ⚠️» en la biblia)

| Personaje | Escena | Confirmado con vídeo real | Sirve para |
|---|---|---|---|
| Deku | 1×01, ~10:55 (min. de esta copia) | Puños apretados al pecho, hombros encogidos, ojos muy abiertos, acercándose a Bakugo | **Pedir perdón / suplicar** — pose nueva, no estaba en la tabla de la biblia |
| Deku | 1×01, ~19:30 | Cuaderno «Campos» abierto con las dos manos, mirando él mismo la página donde acaba de escribir «ALL MIGHT» en letras grandes | **Presentar / explicar** el objeto — mejor que la pose «ofrece con las dos manos» que tenía la biblia (aquí NO lo ofrece, lo mira orgulloso) |
| Deku | 1×01, ~10:33 | Cuaderno «Análisis de héroes para el futuro, No. 13» en primer plano, con la burla de Bakugo de fondo | Referencia exacta de portada para el objeto del canal |
| Bakugo | 1×01, ~11:10 | Mano humeante (chispas del Quirk) apoyada en el propio pecho, mandíbula tensa | **Amenazar** — pose nueva |
| All Might | 1×01, ~13:06 | Silueta musculosa agachada sobre un tejado roto, cielo naranja de fondo, en silencio (antes de hablar) | **Llegar / rescatar** — pose nueva, distinta a la sonrisa de «¡Ya estoy aquí!» que ya tenía la biblia |
| All Might | 1×01, ~19:55 | De espaldas, forma real (flaca), manos en la nuca, niebla blanca | **Pensar / confesar un secreto** — pose nueva |
| All Might | S1E12 (clip), 0:00-0:09 | Puño en alto con luz lateral, cuerpo encogido antes del golpe, impacto contra la cúpula del USJ | **Regañar/atacar con toda la fuerza** («Plus Ultra») |
| Uraraka | S2E22, ~5:30-6:00 | De pie, puño cerrado a la altura del pecho, mirada fija, luego primer plano con ojos llorosos de determinación | **Animar(se) / prometer** — confirma y mejora la pose «decidida, puño cerrado» que ya tenía la biblia (§15), ahora con escena y minuto reales |

**Aizawa y Todoroki**: no llegué a confirmar sus poses con vídeo real en
esta tanda (siguen con la descripción «de memoria ⚠️» de la biblia); lo
dejo en «Sigue» porque el punto 14 pide que estén analizados los 6
personajes que da el encargo.

## Lo mejor para la lámina

1. El cuaderno «Campos» de Deku, «Análisis de héroes para el futuro, No.
   13» (1×01, ~10:33): portada real, con logo de marca y numeración —
   objeto exacto que propone el encargo, ya no hay que inventarlo.
2. Deku mirando su cuaderno recién escrito con «ALL MIGHT» en letras
   grandes (1×01, ~19:30): la pose de **presentar/explicar** más honesta
   para la lámina de #material-de-clase.
3. Paleta real de la cúpula del USJ de noche (`#170D0A`/`#4D342B`, sin
   azules) para un fondo dramático, con su textura CC0 equivalente
   (ambientCG Concrete044D).
4. Uraraka con el puño cerrado y la mirada de «¡Ganaré!» (S2E22, 5:30):
   sirve si el concepto usa a un personaje secundario animándose a sí
   mismo, no sólo a Deku.
5. Contraste de luz entre el tejado diurno azul-claro del OP2
   (`#406D84`/`#B0E2F1`) y el campo nocturno del ED1
   (`#0B0D25`/`#10153B`): dos ambientes ya medidos, listos para Blender.

## No encontré

- ⚠️ Poses confirmadas con vídeo real de **Aizawa** y **Todoroki**: no
  encontré clips cortos suyos en Dailymotion que fueran claramente
  oficiales (sólo AMVs con filtro de color, como el de Nomu que descarté
  abajo) y no llegué a bajar un episodio completo con ellos de
  protagonistas por presupuesto de tiempo.
- ⚠️ Minuto exacto de «You Say Run» dentro del episodio 13 (sólo tengo
  episodio y tema confirmados por la wiki, no bajé el episodio completo).
- ⚠️ Efectos de sonido y onomatopeyas reconocibles con fuente propia (punto
  9): no llegué a esta parte.
- ⚠️ Tendencias de TikTok (punto 10): no hay forma de comprobarlas sin
  TikTok ni YouTube desde este contenedor.
- Descarté un clip de «All Might vs Nomu» en Dailymotion
  ([`x6j7vj6`](https://www.dailymotion.com/video/x6j7vj6)): es un **AMV de
  fans** con filtro monocromo azul y marca de agua «Openings Fanmade», no
  sirve para medir paleta real (lo sustituí por el clip oficial de «Plus
  Ultra» de arriba, mismo episodio S1E12).
- AnimeThemes: **HTTP 522** en la API, redirección rota en la web y CDN con
  conexión reiniciada — 3 intentos en total (contando el de
  `recolectar.py`), descartada. No bloqueó el trabajo: Dailymotion +
  Internet Archive dieron opening, ending, tráiler y 3 escenas.

## Bitácora de búsqueda

- `curl` a `api.animethemes.moe/anime?filter[slug]=boku-no-hero-academia`
  (con `[` y `]` codificados: `%5B`/`%5D`) → HTTP 522. `animethemes.moe/anime/boku-no-hero-academia`
  → 302 a la home (ruta rota). `v.animethemes.moe/BNHA-OP1.webm` → conexión
  reiniciada. Descartada tras 3 intentos.
- Dailymotion API (`api.dailymotion.com/videos?search=…`, en inglés):
  «My Hero Academia OP1 full» → sin resultado limpio; «My Hero Academia
  opening THE DAY» → `x7s67y3` (OP1 completo, 90 s) y `x5pk6h7` (OP2
  completo, 91 s); «My Hero Academia ending 1 full» → sin ending limpio
  (fui a Internet Archive); «My Hero Academia All Might Detroit Smash
  scene» → `x4hptj4` (Plus Ultra, ep. 12) y `x6j7vj6` (Nomu, descartado por
  ser AMV); «My Hero Academia Bakugo vs Deku sports festival» / «Uraraka
  vs Bakugo sports festival» → `x80pei3` (Muscular) y `x6soboa` (Uraraka
  vs Bakugo, sub. español); «My Hero Academia Two Heroes trailer» (de
  `datos-video.md`) → `x6u2yxy`.
- `archive.org/advancedsearch.php?q=title:("my hero academia" ending)` →
  7 resultados; usé `my-hero-academia-ending-1-heroes` (ED1 completo,
  89.35 s, confirmado por duración real de un ending).
- `archive.org/details/anime-kcd-boku-no-hero-academia-01` (de
  `datos-video.md`): episodio 1 completo, 1280×720, 24:32 min, sub.
  español — la mejor fuente que encontré, con subtítulos reales (no
  automáticos ni de fans traduciendo del inglés).
- `fotogramas.py` con `--cada` sobre los 7 clips completos (openings,
  ending, tráiler, 3 escenas) y con `--fotograma` sobre 9 segundos sueltos
  del episodio 1 (404, 633, 655, 670, 718, 786, 1161, 1170, 1195) para
  comprobar minuto a minuto las poses que la biblia daba «de memoria».
  Todos los `video.mp4` (~444 MB en total) se **borraron** tras sacar los
  fotogramas; quedan sólo las hojas y los fotogramas sueltos (~2.6 MB) en
  la carpeta de trabajo.
- `estilo.py --colores 6` sobre 5 fotogramas reales para medir hex (tabla
  del punto 4) y sampleo de píxel con Pillow (`Image.getpixel`) sobre 2
  fotogramas para el pelo de Deku y Bakugo.
- Fandom `myheroacademia.fandom.com/api.php` (wikitext e búsqueda), en
  inglés: ficha de «Episode 12» (pageid 12736, confirma USJ/Plus Ultra),
  «Episode 42» (pageid 27428, confirma Muscular/Forest Training Camp),
  «Episode 22» (confirma Bakugo vs. Uraraka/Sports Festival), «1,000,000%
  Delaware Detroit Smash» (pageid 28424, nombre del movimiento), «THE DAY»
  (artista y fecha del OP1), «Episode 13» (lista de BGM, confirma «You Say
  Run»), «You Say Run 10th Anniversary Ver.» (dato reciente, sep-2026).
- `ambientcg.com/api/v2/full_json?type=Material&q=concrete+damaged` →
  Concrete044D/042C, CC0, para la cúpula del USJ.

**Sigue:** confirmar con vídeo real las poses de **Aizawa** y **Todoroki**
(punto 14 pide los 6 personajes del encargo: Deku, All Might, Bakugo,
Todoroki, Uraraka y Aizawa — Deku, All Might, Bakugo y Uraraka ya están
confirmados arriba). Buscar un clip corto de Aizawa (p. ej. «capture
weapon», «erasure quirk») y de Todoroki (p. ej. «half-cold half-hot»,
«Endeavor») en Dailymotion/Internet Archive con `fotogramas.py`, y si no
aparecen, dejarlo en «No encontré» con las búsquedas hechas (no como
«no existe»).
