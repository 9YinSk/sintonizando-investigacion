# Investigación de VÍDEO · Spider-Man: Into/Across the Spider-Verse (puntos 2, 4, 9, 10, 14 de ENCARGO.md)

Repaso del 24-sep-2026. Es una **segunda pasada**: la `biblia.md` ya tenía
las secciones §2 (escenas), §5 (sitios/luz/paleta), §11 (música), §12
(vídeos) y §15 (poses) con **minutos exactos sacados de subtítulos reales**
de las dos películas, pero casi todo lo visual (postura, luz, hex) estaba
marcado «de memoria ⚠️» porque nadie había abierto un fotograma, y el único
clip de Dailymotion en `datos-video.md` (`x8jt3ad`) **da 404** (vídeo
borrado). YouTube sigue pidiendo iniciar sesión desde este servidor
(comprobado hoy). Esta pasada es sólo para **mirar de verdad y medir**, no
para rehacer lo que ya está bien.

**Vídeos reales mirados con `fotogramas.py`** (contactos abiertos con Read,
frame a frame donde hacía falta más detalle), todos en Dailymotion salvo el
último (Internet Archive), con carpeta de trabajo
`/tmp/claude-0/trabajo/21-spiderverse-video/`:

1. ATSV, tráiler oficial (FilmAffinity): [dailymotion.com/video/x8gaz41](https://www.dailymotion.com/video/x8gaz41) (2:30), 26 fotogramas.
2. UNU, tráiler oficial (FilmAffinity): [dailymotion.com/video/x942l02](https://www.dailymotion.com/video/x942l02) (2:40), 27 fotogramas.
3. UNU, clip de película **«Leap of Faith»** (Zero Trailers): [dailymotion.com/video/x6yq9yg](https://www.dailymotion.com/video/x6yq9yg) (2:07) — el salto de fe real, no un tráiler.
4. UNU, clip de película **«Get Up, Spider-Man»** (batalla final contra Kingpin en el colisionador): [dailymotion.com/video/x87pqho](https://www.dailymotion.com/video/x87pqho) (2:36).
5. ATSV, clip de película **«Hanging With Gwen»** (torre del reloj): [dailymotion.com/video/x8l73q0](https://www.dailymotion.com/video/x8l73q0) (0:53) — escena entera, no un recorte de tráiler.
6. ATSV, clip de película **«Stop Spider-Man!»** (persecución en la sede de la Spider-Society): [dailymotion.com/video/x8le5bg](https://www.dailymotion.com/video/x8le5bg) (0:50).
7. ATSV, featurette oficial de Sony **«Designing Spider-Punk»**, con **Kris Anka** (diseñador de personajes), **Kemp Powers** (guionista) y **Mike Lasker** (supervisor de VFX) hablando a cámara: [dailymotion.com/video/x8oez5v](https://www.dailymotion.com/video/x8oez5v) (1:20).
8. ATSV, *storyboards* oficiales comparados con el plano final (imágenes .jfif, resolución real 2550×2564, con marca de agua «Entertainment Access», archivo de tuits): [archive.org/details/fz-kuox-0a-yaa-7-hm-7_202405](https://archive.org/details/fz-kuox-0a-yaa-7-hm-7_202405) — 2 planos: Miles rodeado de líneas triangulares de neón (visión/transformación) y una secuencia con máscara robótica azul y gris.

Los tráileres oficiales de UNU y ATSV en YouTube (los 6 enlaces de la §12 de
la biblia) siguen sin poder comprobarse por el bloqueo; no los repito abajo,
sólo añado los que sí pude ver.

---

## Punto 2 · Escenas icónicas, confirmadas mirando vídeo real (no de memoria)

### 2.1 El salto de fe (UNU, cita de la biblia: 01:23:23) — confirmado con el clip «Leap of Faith» ✅

Mirando el clip 3 completo (no es el mismo corte minuto a minuto que la
película, es un featurette de escena, pero es metraje real de la
secuencia): Miles se asoma al borde de un tejado con la capucha puesta
(0:05), mira abajo (0:25), y salta: sus **piernas caen en silueta roja pura
sobre un fondo casi negro** (0:10, medido con `estilo.py`:
`#3E0005` 52% / `#5A0008` 23% / `#E30014` 7%, sombreado **plano tipo cómic
(cel)**, no degradado — la escena usa un solo rojo saturado sin gradiente
para la silueta). Luego cae en picado entre edificios de noche, en azul muy
oscuro (0:35, medido: `#020210` 52% / `#0B143A` 32%, saturación 89%,
brillo 17%). El plano de las piernas está **invertido de verdad** (cae boca
abajo), confirmando lo que la biblia decía «de memoria» ⚠️ → ahora ✅.
[Clip](https://www.dailymotion.com/video/x6yq9yg?t=10) / [clip, 0:35](https://www.dailymotion.com/video/x6yq9yg?t=35).

### 2.2 Torre del reloj, Miles y Gwen boca abajo (ATSV, cita de la biblia: 00:49:31 a 00:52:14) — confirmado con «Hanging With Gwen» ✅

Escena entera de 53 s, mirada completa. Corrijo un dato de la §5.1/§17 de la
biblia: el cielo **no** es «naranja y morado» ⚠️, medido de verdad es
**violeta-lavanda y azulado** (tres fotogramas medidos con `estilo.py`:
`#3E2D4F`/`#AE8DAA`/`#724764` a 0:09; `#493451`/`#5A6CA5`/`#917D9B` a 0:27;
`#5E5FAF`/`#44426E`/`#0F081B` a 0:48 — el naranja casi no aparece, predomina
el violeta y un azul-lavanda frío). La postura, confirmada: **Gwen está de
pie apoyada boca abajo contra el reloj**, con los pies arriba contra la
pared y la capucha blanca colgando hacia abajo; **Miles está sentado normal**
a su lado en la cornisa, hablando de perfil. El plano final (0:48) los
muestra a **los dos sentados normalmente**, de espaldas, mirando la ciudad al
atardecer — este último encuadre (dos siluetas sentadas de espaldas ante el
horizonte) es casi idéntico al póster oficial de ATSV.
[Clip, 0:09](https://www.dailymotion.com/video/x8l73q0?t=9) ·
[0:27](https://www.dailymotion.com/video/x8l73q0?t=27) ·
[0:48](https://www.dailymotion.com/video/x8l73q0?t=48).

### 2.3 Batalla final contra Kingpin en el colisionador (UNU) — nueva, mirada entera ✅

No estaba en la lista de escenas de la §2 de la biblia. El clip
«Get Up, Spider-Man» (2:36) es la pelea completa: Miles solo, herido, en un
**pasillo rojo intenso** (paredes/luces rojas saturadas, los primeros 30 s),
lucha contra **salpicaduras de pintura azul neón** que marcan los golpes del
colisionador roto (0:55 a 1:50: manchas de tinta azul cian sobre fondo
blanco, muy distinto del resto de la paleta de la película — parece papel
mojado con acuarela azul). Termina con una **explosión naranja/dorada**
(2:00) y el colisionador ardiendo (2:05). Sirve como tercera escena icónica
«de acción» con minuto real, y el contraste **rojo saturado → manchas de
tinta azul → fuego naranja** es un ejemplo perfecto de cómo la película
cambia de paleta según la emoción de la escena (útil para el punto 18, que
no es mío, pero lo dejo anotado). [Clip](https://www.dailymotion.com/video/x87pqho).

### 2.4 Persecución «Stop Spider-Man!» en la sede de la Spider-Society (ATSV) — nueva, mirada entera ✅

Clip de 50 s: muestra la **sala de fichaje** con decenas de Spider-Variantes
reales (no fan art): un Spider-Man azul-armadura (2099), un Spider-Man
naranja con seis brazos extra tipo Pavitr-variante, un Spider-Man con
dinosaurio. Termina con Miles **estrellándose contra el salón de Peter B.**
en su propio universo (0:44), silla y estantería volando. Confirma que la
sede de la Spider-Society tiene salas geométricas amarillas con estructura
triangular (ya citado en §5.1 de la biblia) — aquí se ve **desde dentro, en
movimiento**, no sólo en foto fija. [Clip](https://www.dailymotion.com/video/x8le5bg).

### 2.5 Storyboard oficial vs. plano final: la visión/transformación de Miles — nueva, con imagen oficial ✅

El archivo de Internet Archive (nº 8 de la lista de arriba) trae, lado a
lado, el **storyboard a lápiz** y el **fotograma terminado** de un primer
plano de Miles asustado, rodeado de **líneas triangulares de neón** en
naranja, verde, turquesa y magenta que cruzan el encuadre como una red de
grafo (parece la visión de un colapso dimensional o el ataque de un
glitch). Es un ejemplo real de **cómo se monta un plano desde el boceto**:
útil para el canal #edicion, aunque el «cómo se dibuja» en sí es del punto
18 (rol texto). [Imagen](https://archive.org/download/fz-kuox-0a-yaa-7-hm-7_202405/FzKUOX0aYAA7Hm7.jfif),
2550×2564 px real.

---

## Punto 4 · Sitios, luz y paleta — medidos con `estilo.py` sobre fotogramas reales

Sustituyo/completo la tabla «de memoria ⚠️» de la §5.3 de la biblia, sólo en
lo que me toca (sitios y ambiente, no vestuario — el hex de trajes es del
punto 15, rol imagen):

| Sitio / escena | Hex medidos (`estilo.py`) | Luz real (mirada) | Fuente y minuto |
|---|---|---|---|
| **Torre del reloj (ATSV)**, atardecer | `#3E2D4F` `#AE8DAA` `#724764` `#5A6CA5` `#5E5FAF` `#44426E` | **Violeta-lavanda y azul frío**, casi sin naranja (corrige la biblia) | [Clip, 0:09](https://www.dailymotion.com/video/x8l73q0?t=9) a [0:48](https://www.dailymotion.com/video/x8l73q0?t=48) |
| **Tierra-928 / Nueva York 2099 (Miguel)**, vista aérea nocturna | `#725780` `#4C365D` `#A6879D` `#D3C3C5` | Violeta-malva, no el «azul limpio arriba» que decía la biblia — al menos en este plano concreto es todo violeta | [Tráiler ATSV, 1:06](https://www.dailymotion.com/video/x8gaz41?t=66) |
| **Portada/título UNU**, efecto glitch de imprenta | `#8E0126` `#B00137` `#500314` `#644581` (halo azul-violeta alrededor de las letras negras) | Rojo saturado con **desfase cromático real** (bordes cian/magenta alrededor del texto negro, tipo mala alineación de tinta) | [Tráiler UNU, 2:12](https://www.dailymotion.com/video/x942l02?t=132) |
| **Efecto glitch/anomalía (ATSV)**, primer plano deformado | `#D3AE17` `#BC1B22` `#3BC7DB` `#D096A5` | **Amarillo, rojo/magenta y cian** casi puros — es literalmente la paleta CMYK de imprenta (falta el negro), con triángulos de luz y trazos duplicados en cian/verde como un mal registro de color | [Tráiler ATSV, 2:06](https://www.dailymotion.com/video/x8gaz41?t=126) |
| **Sala de la Spider-Society / colisionador**, splash de energía | (sin medir en Pillow; descrito mirando) manchas de tinta **azul cian** sobre blanco, muy planas, sin degradado | Luz dura, blanco de fondo | [Clip «Get Up, Spider-Man», 0:55–1:50](https://www.dailymotion.com/video/x87pqho?t=55) |
| **Tierra-138 (Hobie)**, referencias reales de diseño confirmadas por el propio estudio | (paleta de las referencias, no del sitio en sí): fondo amarillo ácido, naranja punk-poster, azul tipo fotocopia, magenta/rosa pop-art | Confirma con **fuente oficial directa** (featurette de Sony) lo que ya decía la biblia por Variety/befores&afters: el estilo de Hobie se construyó literalmente pegando **fotocopias en blanco y negro, un collage de periódico y carteles de los Sex Pistols** (los tres primeros de seis paneles, rotulados «one black and white», «two newspaper», «three sex pistols» en el propio vídeo) | [Featurette «Designing Spider-Punk», 0:25](https://www.dailymotion.com/video/x8oez5v?t=25) |

La conclusión de la §5.2 de la biblia («la saga vive de noche y en
interiores oscuros, con el color puesto encima en luces fuertes») se
confirma con estos 5 fotogramas nuevos: **ninguno** es luz natural plana;
todos son focos de color puro (rojo, violeta, cian, amarillo) sobre negro o
casi negro. Las texturas CC0 de la §5.4 no las toqué (no hacía falta,
siguen vivas) salvo comprobar que Poly Haven responde 200 hoy.

---

## Punto 9 · Música

Subo de ⚠️ a ✅ (dos fuentes) los dos títulos de hip-hop de la §11 que la
biblia sólo sacaba de la letra del subtítulo:

- **«Hypnotize»**, The Notorious B.I.G. (1997): confirmado su uso en la
  escena de Miles y el tío Aaron por el wikitext de
  [Marvel Animated Universe Wiki](https://marvelanimated.fandom.com/api.php?action=parse&format=json&prop=wikitext&page=Hypnotize_(Song))
  («The song was used in Spider-Man: Into the Spider-Verse») + la letra en
  el subtítulo real que ya tenía la biblia. ✅✅
- **«The Choice Is Yours»**, Black Sheep (1991): mismo wiki
  ([wikitext](https://marvelanimated.fandom.com/api.php?action=parse&format=json&prop=wikitext&page=The_Choice_Is_Yours_(Song)))
  + subtítulo. ✅✅ Un resumen encontrado en la búsqueda (sin poder abrir la
  página original para citarla textual) añade que en la misma escena del
  túnel suenan además, como popurrí, **«Apache» (Incredible Bongo Band)**,
  **«Mary, Mary» (Run-D.M.C.)** y **«Because I Got It Like That» (Jungle
  Brothers)** — lo dejo con ⚠️ porque sólo tengo una fuente (no pude abrir
  la página primaria que lo lista) y no está en el subtítulo que ya
  teníamos.
- El resto de la tabla de música (Sunflower, What's Up Danger, disco de
  Metro Boomin, partitura de Pemberton) ya estaba bien confirmado; no lo
  repito.

---

## Punto 10 · Vídeos — enlaces comprobados hoy (algunos de la biblia estaban muertos)

- **El único clip de Dailymotion de `datos-video.md` (`x8jt3ad`) da 404**
  (vídeo borrado): lo sustituyo por los 7 de la lista del principio, todos
  comprobados hoy, descargados y mirados fotograma a fotograma.
- Añado a la tabla «12.2 Detrás de las cámaras» de la biblia el featurette
  oficial de Sony **«Designing Spider-Punk»** (con Kris Anka, Kemp Powers y
  Mike Lasker hablando a cámara, con su nombre en pantalla — captura de
  ejemplo en el punto 4), en Dailymotion:
  [dailymotion.com/video/x8oez5v](https://www.dailymotion.com/video/x8oez5v).
- Añado el archivo de *storyboards* oficiales de ATSV en Internet Archive:
  [archive.org/details/fz-kuox-0a-yaa-7-hm-7_202405](https://archive.org/details/fz-kuox-0a-yaa-7-hm-7_202405)
  (4 imágenes .jfif a 2550×2564 px reales, storyboard + plano final lado a
  lado; el crédito visible en pantalla es «Entertainment Access», así que es
  un archivo de tuits reposteando material de prensa/Blu-ray, no la fuente
  primaria directa — lo marco ⚠️ sólo por eso, el contenido en sí es
  oficial).
- Los 6 enlaces de YouTube que ya tenía la §12.1/12.2 de la biblia **siguen
  sin poderse comprobar** (bloqueo de inicio de sesión, confirmado de
  nuevo hoy); no cambio nada ahí, sólo sumo los de Dailymotion/Archive.
- **TikTok**: no pude abrir ninguno de los 3 enlaces de la §12.3 (ni el de
  CapCut ni el de los actores latinos) desde este servidor; sigue como ⚠️,
  igual que ya decía la biblia.

---

## Punto 14 · Poses — confirmadas o corregidas mirando el vídeo real

Corrijo las entradas de la §15 de la biblia que decía «postura de memoria
⚠️» y que sí pude comprobar con los clips de arriba (dejo el resto tal cual
estaba, sin tocarlo, porque no tuve el clip para verlo):

| Personaje | Entrada de la biblia | Confirmado/corregido mirando el vídeo real |
|---|---|---|
| Miles, #6 (UNU 01:23:23-01:24:30, «salto de fe, cayendo boca abajo con los brazos abiertos») | postura de memoria ⚠️ | **Corregido**: en los primeros segundos del salto **no** abre los brazos: cae con las **piernas juntas, silueta vertical, boca abajo**, en rojo plano sobre negro (ver punto 2.1); los brazos se abren más adelante en la caída, ya en plano aéreo nocturno azul. Sirve igual para «animar/celebrar», pero el detalle de postura exacta pasa de ⚠️ a ✅. |
| Gwen, #7 (ATSV 00:49:31-00:52:14, «boca abajo junto a Miles en la torre del reloj») | mirada, sin ⚠️ pero sin detalle de postura | **Ampliado, ✅**: Gwen está de pie **contra la pared del reloj, con los pies apoyados arriba y la cabeza colgando hacia abajo** (no sentada); Miles está sentado normal a su lado. El plano de cierre los pone **a los dos sentados** de espaldas mirando la ciudad — es la pose que más se parece al póster oficial, mejor que el ⚠️ original para un concepto de lámina. |
| Nueva pose, Miles (UNU, colisionador) | no estaba en la lista | **Añadida** ✅: de pie, solo, en un pasillo rojo, puños cerrados, rodeado de salpicaduras de tinta azul — sirve para **«pelear/decidir»**, útil si se necesita una pose de acción que no sea el salto de fe. [Clip](https://www.dailymotion.com/video/x87pqho?t=30). |
| Nueva pose, grupo (Spider-Society) | no estaba en la lista | **Añadida** ✅: decenas de Spider-Variantes en fila/formación dentro de una sala amarilla triangular — sirve para un concepto de lámina «en comunidad» si se quiere mostrar más de 5 personajes a la vez. [Clip](https://www.dailymotion.com/video/x8le5bg?t=8). |

No pude ver ni confirmar el resto de poses de la tabla (Peter B., Miguel,
Hobie, Lyla, ni la mayoría de las de Miles y Gwen): los clips reales que
encontré en Dailymotion no cubren esas escenas exactas. Quedan igual que las
dejó la biblia, con su ⚠️ de «postura de memoria».

---

## Lo mejor para la lámina

1. El plano de cierre de «Hanging With Gwen» (los dos sentados de espaldas
   ante el horizonte violeta, [0:48](https://www.dailymotion.com/video/x8l73q0?t=48))
   es casi el póster oficial: perfecto para una escena de dos personajes
   hablando de edición/creación de contenido.
2. El desfase cromático real del título de UNU (rojo con halo cian/magenta,
   [2:12](https://www.dailymotion.com/video/x942l02?t=132)) es la referencia
   exacta del «glitch y desfase de impresión» que propone el encargo para
   #edicion: no hay que inventarlo, ya existe en la propia franquicia.
3. La silueta roja plana (cel, sin degradado) del salto de fe
   ([0:10](https://www.dailymotion.com/video/x6yq9yg?t=10)) es un recurso de
   composición fácil de replicar: una figura en un solo color saturado sobre
   fondo casi negro, sin relleno de textura.
4. Las 6 referencias de diseño de Hobie mostradas por el propio estudio
   ([0:25](https://www.dailymotion.com/video/x8oez5v?t=25): fotocopia B/N,
   periódico, Sex Pistols) son material listo para justificar un tratamiento
   «collage/fanzine» en cualquier gráfico del canal.
5. El storyboard-vs-final de Internet Archive demuestra en imagen real el
   proceso «boceto → plano terminado»: encaja directo con el tema del canal
   #edicion («de la idea al resultado»).

---

## No encontré

- **AnimeThemes**: no aplica — es un catálogo de openings/endings de series
  de TV japonesas; UNU/ATSV son películas de EE.UU., no están indexadas ahí
  (comprobado: sin resultados para «spider-verse» en animethemes.moe).
- **Doblaje Wiki, muestras .mp3**: no las usé; son del rol de voz, no del
  mío (§9 datos-voz.md), y no aplican a openings/endings porque la
  franquicia no es una serie con OP/ED cantado.
- **YouTube** (tráileres oficiales, análisis, TikToks): bloqueado por
  inicio de sesión durante toda la sesión, reintentado en dos momentos
  distintos sin cambio.
- Vídeo de la escena del **Guggenheim** (Gwen vs. Buitre) en Dailymotion:
  los dos IDs que encontré (`x8l68ns`, `x8l7ilg`, canal ruio333) daban 404
  al bajarlos (retirados por copyright, probablemente). No hay sustituto
  encontrado; la cita de la biblia (subtítulo, ATSV 00:09:31) queda igual,
  sin confirmación visual directa mía.
- **TikTok** de los actores latinos diciendo frases icónicas
  (`chick_flick_of/video/7347184102971297030`, ya citado en la biblia como
  ⚠️): sigue sin poder verse desde aquí.
- El popurrí completo de canciones del túnel del grafiti (Apache, Mary
  Mary, Because I Got It Like That): sólo una fuente (resumen de búsqueda),
  no pude abrir la página original para citarla textual — queda como dato
  nuevo con ⚠️, no como «no encontré».

---

## Bitácora de búsqueda (segunda pasada)

- Dailymotion, API `videos?search=`, en inglés: 7 búsquedas («official
  trailer» ATSV y UNU, «clip» UNU, «Gwen Guggenheim clip», «graffiti
  scene», «Spot chase clip», «Hobie Spider-Punk clip») → encontré y
  descargué 7 vídeos reales (tráileres + clips de película + 1 featurette).
- `fotogramas.py` sobre Dailymotion: 6 tiradas completas (`--cada`) + 4
  tiradas de fotogramas sueltos (`--fotograma`) = 15 llamadas, todas
  correctas salvo el `x8jt3ad` inicial (404) y los dos intentos de
  Guggenheim (`x8l68ns`, `x8l7ilg`, también 404).
- `estilo.py`: 3 tiradas, 11 fotogramas medidos en total, con hex y
  saturación/brillo reales.
- `archive.org/advancedsearch.php`, texto «spider-verse», mediatype
  movies: 1 búsqueda → until until encontré el ítem de *storyboards*
  oficiales; bajé y miré las 2 imágenes más grandes (2550×2564 px).
- WebSearch (2 búsquedas, en inglés): títulos de las canciones de la
  escena del túnel del grafiti.
- `marvelanimated.fandom.com/api.php` (wikitext, 2 llamadas): confirmación
  de «Hypnotize» y «The Choice Is Yours».
- AnimeThemes: 1 comprobación rápida (sin resultados, no aplica).
- YouTube directo: 0 intentos nuevos (ya lo tenía confirmado bloqueado de
  la primera pasada; no repetí para no gastar cupo en algo que ya sé que
  falla).

---

## Cumplimiento de mis puntos (2, 4, 9, 10, 14)

| Punto | Estado | Por qué |
|---|---|---|
| 2 · Escenas icónicas con minuto | ✅ | 5 escenas confirmadas mirando vídeo real (2 ya citadas por la biblia + 3 nuevas), con minuto del clip y color medido. |
| 4 · Sitios, luz, paleta medida | ✅ | 5 fotogramas nuevos medidos con `estilo.py`, 2 corrigen datos «de memoria» de la biblia (torre del reloj, Tierra-928). |
| 9 · Música | ✅ | Los 2 títulos en ⚠️ suben a ✅✅; 1 dato nuevo (popurrí del túnel) queda en ⚠️ por una sola fuente. |
| 10 · Vídeos con minuto exacto | ✅ | 7 enlaces nuevos comprobados hoy (todos abiertos y descargados), reemplazando el único que estaba roto. YouTube sigue bloqueado, igual que en la primera pasada. |
| 14 · Poses analizadas con minuto | ⚠️ | 2 poses corregidas/ampliadas y 2 nuevas con vídeo real; el resto de personajes (Peter B., Miguel, Hobie, Lyla y la mayoría de Miles/Gwen) sigue con la postura «de memoria» de la biblia porque no encontré clip real de esas escenas concretas en Dailymotion. |

No dejo «Sigue:» — hice lo obligatorio de mis 5 puntos con lo que la red
abierta (Dailymotion + Internet Archive) permitió desde este servidor. Lo
que falta (Guggenheim en vídeo, el resto de poses, TikTok, YouTube) está
listado arriba en «No encontré», no oculto.
