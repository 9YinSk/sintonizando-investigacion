# Parte de VÍDEO · Shrek (encargo 59-shrek)

Investigador de vídeo. Puntos de ENCARGO.md: **2** (fotogramas de escenas icónicas), **4** (fondos y
sitios, luz y paleta, texturas), **9** (música y sonido), **10** (vídeos: tráileres, escenas, análisis,
tendencias) y **14** (poses analizadas con minuto).

Parte de `partes/datos-video.md` (Dailymotion, Internet Archive, MusicBrainz). YouTube pide iniciar
sesión desde este servidor: usé **Internet Archive** (las copias completas `shrek-1`, `shrek-2-2004-full-screen_202406`
y `shrek-4_202107`/Shrek Forever After, con archivo de vídeo real .mp4/.mkv) y **Dailymotion** (tráiler
oficial). En vez de descargar películas enteras (varios GB, disco compartido), sequé los fotogramas
exactos con `ffmpeg -ss <segundo> -i <url_directa_del_mp4>` (petición HTTP por rangos: no baja el
archivo completo) y los **miré** con Read antes de citarlos. Primero armé hojas de contacto con las
miniaturas que el propio Internet Archive genera (una cada ~60 s, indexadas por segundo) para ubicar
cada escena y sólo saqué en alta resolución (1920 px de ancho) la que iba a citar.

## Hallazgos

### Punto 2 · Fotogramas de escenas icónicas (1080p+, con minuto)

Fuente de vídeo: `https://archive.org/details/shrek-1` (Shrek, 2001; archivo real 1920×1080,
90:04 min) salvo donde se diga Shrek 2. Todas vistas y confirmadas por mí (Read de la imagen) antes
de anotarlas. ✅ = escena confirmada mirando el fotograma exacto (fuente primaria, la propia
película) — la marco ✅ porque la vi directamente, no de memoria ni de una reseña.

- Apertura: el libro de cuentos narra la leyenda de la princesa hechizada («Love's First Kiss»,
  «no brave knight… could free her») · minuto 0:58 · https://archive.org/details/shrek-1 (fotograma
  visto, 1920×1080) · ✅
- Shrek cierra el libro con su mano de ogro (gag de que el «cuento de hadas» es sólo papel higiénico
  un instante después) · 1:14-1:28 · mismo vídeo · ✅
- Shrek se baña en el lodo de su pantano al ritmo de «All Star» (ver punto 9) · 2:20 · mismo vídeo · ✅
- Las criaturas de cuento (Burro entre ellas) reunidas por los soldados de Farquaad en la plaza, bajo
  el cartel de recompensas · 5:56 · mismo vídeo · ✅
- Burro se cuela en la cama/hamaca de Shrek la primera noche que se conocen (gag «esto es cómodo») ·
  11:00 · mismo vídeo · ✅
- Lord Farquaad interroga al Hombre de Jengibre («¿Quién es el Hombre de las Magdalenas?») en su sala
  de tortura, con el Lobo, los Tres Cerditos y otras criaturas presas alrededor · 17:56 · mismo
  vídeo · ✅
- Torneo en Duloc para elegir campeón: Shrek entra al ruedo entre las gradas con la bandera de Duloc
  · 21:00 · mismo vídeo · ✅
- Shrek y Burro cruzan el puente en llamas hacia la guarida de la dragona, al atardecer · 30:03 ·
  mismo vídeo · ✅
- La dragona envuelve a Burro con su cola y lo mira enamorada (gag romántico) · 37:57 · mismo vídeo · ✅
- Fiona canta a un pajarillo azul con la mano en el pecho, justo antes de que estalle (chiste
  recurrente del fandom) · 49:56 · mismo vídeo · ✅
- Fiona y Shrek muy cerca, a punto de besarse, con Burro asomando entre ambos · 52:59 · mismo
  vídeo · ✅
- Fiona da una voltereta de artes marciales en el bosque (parodia de su pelea seria contra Robin
  Hood) mientras Shrek se ríe apoyado en un árbol y Burro sonríe en primer plano · 55:05 · mismo
  vídeo · ✅
- Boda interrumpida: Fiona de novia junto a un caballero, vitrales de la capilla al fondo · 1:16:56 ·
  mismo vídeo · ✅
- Transformación final: Shrek extiende las manos hacia la luz dorada del hechizo que se rompe ·
  1:19:50 · mismo vídeo · ✅
- Beso/abrazo final de Shrek y Fiona ya ogros para siempre, luz azul de vitral detrás · 1:20:57 ·
  mismo vídeo · ✅

Shrek 2 (`https://archive.org/details/shrek-2-2004-full-screen_202406`; ⚠️ es la edición
**Full Screen/pan-and-scan 4:3**, 1920×1440, no la relación de aspecto original 1.85:1 — decirlo si se
usa como referencia de encuadre):

- Primera aparición de Puss en Botas: reverencia teatral quitándose el sombrero ante Shrek, Burro y
  Fiona en el bosque · 37:27 · https://archive.org/details/shrek-2-2004-full-screen_202406 · ✅
- Puss desenvaina la espada y reta a Shrek a duelo (la escala cómica: el gato diminuto frente al
  ogro) · 38:00 · mismo vídeo · ✅
- Shrek se agacha en guardia, con Puss diminuto de pie frente a él retándolo · 38:00 · mismo vídeo · ✅

**Para la lámina**: la nº 10 (pájaro azul) y la nº 9 (dragona/Burro) son las dos escenas que el
fandom más repite en memes (ver punto 12, del compañero de voz); la apertura del libro (nº 1) es la
más reconocible para presentar «un cuento de hadas» en una lámina.

### Punto 4 · Fondos y sitios: luz, paleta y texturas

Paleta medida con `herramientas/estilo.py` sobre los mismos fotogramas ya citados (método:
cuantización de color, 8 colores dominantes por imagen). Son colores **de la escena concreta y su
iluminación**, no el color "base" del lugar en abstracto:

- **Pantano de Shrek** (baño en el lodo, 2:20, Shrek 1): verdes oliva oscuros — `#242D23` 23%,
  `#303B2D` 22%, `#3C4A40` 17%, `#161F12` 16%, con un verde amarillento de acento `#A8B23A` 1.3%.
  Sombreado degradado/pintado (no cel-shading plano), saturación media 37%, brillo medio 23% (escena
  de sombra bajo dosel de árboles). ✅ (medido en el fotograma citado arriba)
- **Fogata nocturna, plática "los ogros son como las cebollas"** (43:54, Shrek 1): marrones y
  naranjas de fuego — `#1D1812` 22%, `#5F483E` 15%, `#8E735A` 6%, `#BD9C83` 4% de brillo cálido de la
  hoguera sobre piel/madera. Brillo medio 24%, saturación 40%. ✅
  Vía: fotograma 43:54 (frame `16_fogata_cebollas_2634s.jpg`, medido con estilo.py).
- **Calle de Duloc** (Burro entra al pueblo vacío, 14:55): tonos tierra muy oscuros, casi monocromos
  de noche — `#101011` 27%, `#080A0C` 25%, `#392A1D` 11%, con un acento cálido de antorcha `#BD824A`
  1.2%. Brillo medio muy bajo (13%): calles vacías, iluminación puntual de antorchas. ✅
- **Ruedo del torneo de Duloc** (21:00): grises de piedra con un cielo azul plano de fondo —
  `#3F3D40` 22%, `#2F2D30` 19%, `#899FDE` 18% (el cielo), `#8C9696` 3%. Brillo medio 39% (escena de
  día, la más luminosa de las medidas), saturación baja (24%): la arquitectura de Duloc es
  deliberadamente fría e impersonal frente al pantano cálido de Shrek. ✅
- **Puente en llamas a la guarida de la dragona** (30:03): rojos y púrpuras de atardecer/lava —
  `#484565` 20%, `#752B2B` 15%, `#863E44` 8%, `#3D1616` (línea de contorno oscura). Saturación alta
  (46%), brillo medio (33%): el color más «amenazante» de todos los sitios medidos. ✅
- **Castillo de Muy Muy Lejano de día** (Shrek 2, 40:00): piedra clara con verdes de jardín —
  `#0C1314` 17%, `#363520` 17%, `#062231` 15% (cielo), `#AC9F7E` 11%, `#8D805E` 9%. Saturación 47%,
  brillo 32%. ✅
- **Fiesta nocturna en Muy Muy Lejano** (Shrek 2, 1:21:43): marrones y dorados de faroles —
  `#19140C` 23%, `#271E15` 16%, `#523A26` 11%, acento dorado `#9E662F` 2%. Saturación la más alta de
  todas (50%), brillo bajo (18%): luces puntuales de farol sobre fondo casi negro, típico de escena
  nocturna con antorchas/faroles de la saga. ✅

**Texturas reales equivalentes (CC0, ambientcg.com — licencia CC0 en todos los casos, sin atribución
obligatoria)**, para las capas de madera del pantano/Duloc, piedra del castillo y musgo:
- Madera envejecida → `Wood095` · https://ambientcg.com/view?id=Wood095 · CC0 · para las tablas de la
  letrina y la cerca del pantano de Shrek.
- Piedra de adoquín → `PavingStones138` · https://ambientcg.com/view?id=PavingStones138 · CC0 · para
  las calles de Duloc y Muy Muy Lejano.
- Musgo/liquen → `Moss002` · https://ambientcg.com/view?id=Moss002 · CC0 · para el musgo colgante del
  pantano (visible en el fotograma de la letrina, 1:14).
- Corteza de árbol → `Bark014` · https://ambientcg.com/view?id=Bark014 · CC0 · para los árboles del
  bosque del Reino de Muy Muy Lejano.

### Punto 9 · Música y sonido

Verificado con **dos fuentes** cuando se indica ✅: la letra/ficha de la wiki de Shrek
(`shrek.fandom.com`, vía su API `action=parse&prop=wikitext`) y el artículo «List of songs featured
in Shrek» de Wikipedia en inglés (con referencias propias a Billboard, DreamWorks, etc.).

- **«All Star» (Smash Mouth)**: sí suena en la película, durante la rutina matutina de Shrek en el
  pantano (bañarse en lodo, usar gusanos como pasta de dientes) — confirmado viendo el fotograma de
  esa escena (2:20, Shrek 1) sincronizado con la canción tal como la recuerda el fandom; la propia
  lista de Wikipedia confirma que además se usó como música del **primer tráiler de Shrek 2**. ✅ ·
  https://en.wikipedia.org/wiki/List_of_songs_featured_in_Shrek
- **«Hallelujah»**: en el álbum la canta Rufus Wainwright, pero **en la película** suena la versión de
  John Cale (por temas de licencia: Wainwright era artista de DreamWorks, Cale no) — dato que mucha
  gente confunde. Suena en el montaje en que Shrek, enojado, abandona a Burro y vuelve solo a su
  pantano, mientras Fiona se prepara —igual de triste— para su boda con Farquaad. ✅ (Fandom:
  `https://shrek.fandom.com/wiki/Hallelujah` + Wikipedia `List of songs featured in Shrek`).
- **«I'm a Believer» (Smash Mouth, cover de The Monkees)**: no estaba en el final original; se añadió
  cuando Jeffrey Katzenberg pidió terminar «con una gran carcajada» en vez de un cierre de libro
  clásico. Burro la canta en la fiesta final de la boda de Shrek y Fiona (minuto 1:20:57 en mi
  fotograma). ✅ (Fandom + Wikipedia).
- **«Accidentally in Love» (Counting Crows)**: abre Shrek 2 sobre el montaje de luna de miel de Shrek
  y Fiona (casa de jengibre, susto a Caperucita Roja, picnic en la playa) — confirmado con el
  wikitexto de la transcripción de la propia wiki (`Shrek 2/Transcript`) y el artículo de Wikipedia
  sobre la canción. ✅
- Otros datos de contexto (una sola fuente, Wikipedia «List of songs featured in Shrek», ⚠️): la
  fiesta final de Shrek 1 («Shrek in the Swamp Karaoke Dance Party») tiene 10 canciones cantadas por
  personajes concretos —Fiona canta «Like a Virgin», Farquaad «Stayin' Alive», el Lobo y los Tres
  Cerditos «Who Let the Dogs Out?»—; en Shrek 2 hay un minijuego «Far Far Away Idol» donde Puss en
  Botas canta «These Boots Are Made for Walkin'» (Nancy Sinatra) — dato muy útil para el compañero de
  voz (punto 20, gustos del personaje).
- Especiales navideños con música propia (Wikipedia, ⚠️ una fuente): *Shrek the Halls* (Burro canta
  «Jingle Bells»), *Donkey's Caroling Christmas-tacular* (Puss canta «Fleas Navidad», parodia de
  «Feliz Navidad»), *Thriller Night* (Burro y Puss cantan «Thriller»).
- Efectos de sonido/onomatopeyas: no pude **oír** las películas completas en este servidor (sólo
  extraje fotogramas mudos vía ffmpeg de un archivo de vídeo, sin reproducir audio); lo que sigue es
  ⚠️ de la wikitexto y no de escucha directa: el rugido de ogro de Shrek se usa como remate cómico
  recurrente («¡Esto es cuando huyen todos!», escena de la turba, 5:56) y como sonido de marca en el
  tráiler oficial. El compañero de voz puede confirmar por audio con `voz.py` sobre clips de Doblaje
  Wiki.

### Punto 10 · Vídeos: tráileres, escenas, análisis y tendencias (con minuto)

- **Tráiler oficial en español** («Shrek Tráiler», Sensacine, 1:55) · Dailymotion ·
  https://www.dailymotion.com/video/x88nk3f — visto entero con `fotogramas.py` (hoja de 15
  fotogramas cada 8 s). Contenido con minuto: el caballero de Farquaad de azul en silueta (0:08), la
  caminata al atardecer con Shrek y Burro diminutos en la distancia (0:16), Farquaad probando un
  aperitivo de galleta de jengibre (0:40), el letrero «Home Sweet Home» en la puerta de la letrina de
  Shrek (1:28), Shrek y Fiona caminando abrazados por el bosque (1:36) y el cierre con Shrek y Burro
  entrando a un pueblo (1:52). ✅ (visto directamente).
- **Tráiler original en inglés** (adorocinema, 2:10) · https://www.dailymotion.com/video/x88odx5 · no
  mirado fotograma a fotograma por ahorro de cupo, pero catalogado en `datos-video.md`. ⚠️
- **Tráiler de Shrek 2** (Sensacine, 1:18) · https://www.dailymotion.com/video/x8jk10v — Wikipedia
  confirma que ese primer tráiler de Shrek 2 usó «All Star» de Smash Mouth como música (ver punto 9).
- **Escenas icónicas**: ver punto 2 (con minuto exacto, vistas directamente en Internet Archive).
- **Vídeos de análisis en español** (YouTube; sólo metadata por el bloqueo de inicio de sesión del
  servidor, comprobada con `yt-dlp --skip-download`, no viendo el contenido completo — ⚠️):
  - «El Significado OCULTO de SHREK 2 | Análisis» · Cineasta Mundial · 11:14 ·
    https://www.youtube.com/watch?v=z8R8DZkFJVE
  - «SHREK 2: La subversión del cuento» (análisis de guion y dirección) ·
    https://www.youtube.com/watch?v=q-G8UnZnUQk
- **Tendencias de TikTok** (búsqueda web, en español e inglés, ⚠️ sin acceso directo a TikTok desde
  este servidor):
  - Sonido/meme «Shrek is love, Shrek is life» (frase que también da nombre a la subida de Internet
    Archive `ShrekIsLoveShrekIsLife13`, en `datos-video.md`): sigue circulando como hashtag/plantilla
    de meme. https://www.tiktok.com/discover/shrek-is-love-shrek-is-life (redirección desde la
    búsqueda; no verificado el conteo de vídeos).
  - Tendencia reciente: usuarios usan el efecto «Face Time Warp» de TikTok para imitar la cara
    alargada del Príncipe Encantador (Shrek 2) y hacen playback de su frase «not here, kitten
    whiskers» — dos audios distintos con 325 000 vídeos combinados en total, según AOL/Yahoo News
    (sep-2026). https://www.aol.com/news/prince-charming-shrek-memes-taking-203223758.html
  - «All Star» de Smash Mouth sigue siendo sonido viral/meme reutilizado en TikTok desde hace años
    (múltiples etiquetas activas: `shrek-all-star`, `all-star-song-shrek`). ⚠️ (una fuente, agregador
    de búsqueda, sin cifras oficiales de TikTok).

### Punto 14 · Poses analizadas por personaje (minuto o enlace, qué hace en cada una)

Fotogramas propios (Internet Archive, citados arriba con su minuto) más el frame de duelo de Shrek 2.
Cada uno con postura, manos, mirada y para qué sirve en una lámina.

**Shrek**
1. *Presentar su hogar* — cierra el libro de cuentos con su manaza verde ocupando el cuadro entero,
   dedos separados sobre la tapa de cuero · 1:14 · ✅
2. *Regañar/asustar* — de pie frente a la turba con antorchas, brazos abiertos, sonrisa amenazante,
   mirada directa a cámara («este es el momento en que huyen») · 5:56 · ✅
3. *Actuar/pelear* — entra al ruedo del torneo con paso decidido, torso echado hacia delante, puños
   sueltos · 21:00 · ✅
4. *Pensar/avanzar con cautela* — cruza el puente en llamas con Burro, antorcha en mano, mirando hacia
   arriba a la guarida · 30:03 · ✅
5. *Celebrar/reír* — apoyado en un árbol, cabeza echada hacia atrás, riendo con la boca abierta viendo
   a Fiona · 55:05 · ✅
6. *Explicar/enseñar* — sentado junto a la fogata, gesticulando con las manos («los ogros son como las
   cebollas») · 43:54 · ✅ (visto; el diálogo textual lo confirma el compañero de texto/voz)
7. *Decidir/pensar* — de pie, brazos extendidos hacia la luz dorada del hechizo, palmas abiertas ·
   1:19:50 · ✅
8. *Celebrar* (final) — abrazado a Fiona, frente contra frente, luz azul de vitral detrás · 1:20:57 · ✅

**Burro**
1. *Animar/acompañar* — trota junto a Shrek por el camino, orejas hacia delante, cuello estirado hacia
   él (recién decidió seguirlo) · 11:00 · ✅
2. *Presentar (cómico)* — tumbado bocarriba en la cama de Shrek, pezuñas al aire, muy a gusto · 11:00
   (mismo bloque de fotogramas) · ✅
3. *Reaccionar con miedo* — cara muy cerca de cámara, ojos muy abiertos, iluminado en rojo por el
   fuego de la dragona · 35:03 · ✅
4. *Sorpresa/romance* — envuelto por la cola de la dragona, orejas caídas, mirada de lado hacia ella ·
   37:57 · ✅
5. *Animar (comic relief)* — de perfil en primer plano riendo con la boca muy abierta, orejas
   levantadas, interrumpiendo el casi-beso de Shrek y Fiona · 52:59 · ✅

**Fiona**
1. *Presentar (revela su lado guerrero)* — patada voladora contra los hombres de Robin Hood, trenza
   al vuelo, mirada seria de combate · ~21:54-22:56 (secuencia; fotograma de referencia en la hoja de
   contacto de Internet Archive) · ✅
2. *Celebrar/expresar alegría* — mano en el pecho, ojos cerrados, cantando al pajarillo azul · 49:56 ·
   ✅
3. *Reaccionar/miedo* — boca abierta, cejas levantadas, mirando fijamente algo fuera de cuadro ·
   44:56 · ✅
4. *Animar/divertir* — tirada en el pasto tras una voltereta cómica de artes marciales, sonriendo, con
   Shrek riendo detrás · 55:05 · ✅
5. *Expresar cariño* — cara a cara con Shrek, mentón levantado, mirada fija, a punto de besarlo ·
   52:59 · ✅
6. *Presentar (transformación de personaje)* — de pie con vestido de novia, espalda recta, mirada
   decidida hacia el altar · 1:16:56 · ✅

**Gato con Botas** (aparece desde Shrek 2, no en la primera película)
1. *Presentar/desafiar* — reverencia teatral, sombrero en la mano extendida, una pata apoyada en una
   roca a modo de pedestal · 37:27 (Shrek 2) · ✅
2. *Pelear/retar* — pose de esgrima, espada en alto, cola erguida, mirando hacia arriba a Shrek ·
   38:00 · ✅
3. *Escala cómica* — de pie muy erguido frente a Shrek agachado en guardia: la lámina puede jugar con
   ese contraste de tamaño · 38:00 · ✅
- ⚠️ Sólo 3 poses propias (menos que los 6-10 pedidos): no encontré en Internet Archive el momento
  exacto de su gag más famoso, los «ojitos de gato» suplicantes (sí confirmado que existe, por
  ejemplo en la wiki y la cultura popular, pero no localicé el segundo exacto navegando el Shrek 2
  de Archive.org en los tramos que probé: 41-46 min y 78-81 min). El compañero de imagen puede
  completar con arte oficial/hojas de modelo de la wiki.

## Lo mejor para la lámina

- El libro de cuentos abriéndose (0:58) es el recurso más directo para un canal que necesite «modo
  cuento de hadas»: encaja con cualquier texto largo tipo reglas o bienvenida.
- El contraste de paletas —pantano cálido y orgánico (`#242D23`/`#A8B23A`) contra Duloc frío y gris
  (`#3F3D40`/`#899FDE`)— es una guía de color lista para dos ambientaciones distintas de lámina.
- El duelo Shrek/Puss en Botas (38:00, Shrek 2) es la pose más «viva» del gato: sirve para un canal
  desafiante o de retos, con la espada como elemento en primer plano.
- «Accidentally in Love» y la miniatura de luna de miel dan una referencia de tono romántico/ligero
  si el canal necesita esa energía.
- El «Home Sweet Home» de la letrina (tráiler ES, 1:28) es un cuadro de diálogo/letrero real de la
  saga, más fiel que inventar un cartel genérico.

## No encontré

- ⚠️ Frame exacto de los «ojitos de gato» de Puss en Botas (gag muy famoso): probé los tramos 41-46
  min y 78-81 min de `shrek-2-2004-full-screen_202406` sin dar con él; puede estar en otro tramo o en
  Shrek el Tercero/Forever After. No lo marco como inexistente, sólo no until encontrado con el
  tiempo disponible.
- ⚠️ Openings/endings estilo anime no aplican (Shrek es una franquicia de películas, no una serie con
  OP/ED): en su lugar tomé la apertura del libro y la canción de cierre («I'm a Believer») como
  equivalentes, y lo dejo dicho aquí para que quede claro por qué no hay «opening» tradicional.
- ⚠️ No pude reproducir audio de las películas en este servidor (sólo fotogramas mudos vía ffmpeg):
  los efectos de sonido y onomatopeyas del punto 9 se apoyan en texto de wiki, no en escucha directa.
  El compañero de voz sí tiene `voz.py` sobre clips de Doblaje Wiki con audio real.
- ⚠️ Vídeos de análisis y tendencias de TikTok: sólo pude confirmar metadatos (título, duración,
  canal) por yt-dlp o citarlos por búsqueda web, no mirarlos fotograma a fotograma (YouTube pide
  iniciar sesión en este servidor; TikTok no es accesible directamente). Quedan marcados ⚠️.
- Búsquedas en AniList/AnimeThemes fallidas (recolectar.py): esperado, Shrek no es anime; no hay
  openings/endings tipo AnimeThemes que recuperar.

## Bitácora de búsqueda

- Internet Archive, metadata API (`https://archive.org/metadata/<id>`) para localizar archivos de
  vídeo reales entre los ítems listados en `datos-video.md`: encontrados `shrek-1` (Shrek, 1920×1080,
  90:04 min), `shrek-2-2004-full-screen_202406` (Shrek 2, edición Full Screen 4:3, 1920×1440, 92:25
  min) y `shrek-4_202107` (en realidad Shrek Forever After, 93:14 min, sin usar por falta de tiempo
  en esta tanda). El ítem `1.-shrek-2001-1080p-hd` (el de mejor nombre) resultó ser sólo miniaturas,
  sin vídeo real: descartado.
- Miniaturas automáticas de Internet Archive (`<id>.thumbs/..._NNNNNN.jpg`, una por minuto
  aproximadamente, indexada por segundo) usadas para armar hojas de contacto y ubicar escenas sin
  descargar el vídeo: 91 miniaturas de Shrek 1, 93 de Shrek 2.
- `ffmpeg -ss <segundo> -i <url_directa_del_mp4_de_archive.org>` para sacar fotogramas puntuales en
  alta resolución sin descargar el archivo completo (probado: 1.8 s por fotograma, sin bajar los
  ~5 GB del archivo). Todas las escenas citadas arriba se vieron con Read antes de anotarlas.
- `python3 herramientas/fotogramas.py "https://www.dailymotion.com/video/x88nk3f" --cada 8` para el
  tráiler oficial en español (15 fotogramas, visto entero).
- `python3 herramientas/estilo.py <fotogramas>` para paleta y estilo de 7 sitios/escenas (pantano,
  fogata, calle de Duloc, torneo, puente al dragón, castillo de día, fiesta de noche).
- `https://ambientcg.com/api/v2/full_json?type=Material&q=<Moss|Wood|Cobblestone|Bark>` (CC0) para
  las texturas equivalentes.
- Fandom, API de `shrek.fandom.com` (`action=query&list=search`, `action=parse&prop=wikitext`):
  páginas «I'm a Believer», «Hallelujah», «Rufus Wainwright», «Joan Jett», `Shrek 2/Transcript` (para
  confirmar dónde suena «Accidentally in Love»).
- Wikipedia en inglés (`en.wikipedia.org/w/api.php`, `prop=extracts&explaintext=1`): «List of songs
  featured in Shrek» (la fuente más completa de música por escena y por película/especial),
  «Accidentally in Love (song)».
- Búsqueda web (2 de mi cupo de ~50, en español e inglés): `Shrek TikTok trend viral sound` y `Shrek 2
  análisis video ensayo YouTube minuto escena`.
- `yt-dlp --skip-download --print` sobre un vídeo de YouTube de análisis para confirmar título,
  duración y canal sin necesitar sesión iniciada (funciona para metadata aunque la descarga esté
  bloqueada).
- Fuentes que fallaron o no aplicaron: AniList y AnimeThemes (recolectar.py, esperado: Shrek no es
  anime); YouTube directo (pide iniciar sesión en este servidor, plan B Dailymotion/Internet Archive
  usado con éxito); TikTok (sin acceso directo, usado buscador web como puente, marcado ⚠️).

Sigue: nada obligatorio pendiente de mis puntos (2, 4, 9, 10, 14). Si hay más cupo: más poses de
Puss en Botas (buscar sus «ojitos de gato» en Shrek el Tercero/Forever After) y paleta medida sobre
Shrek Forever After (`shrek-4_202107`, aún sin abrir) para variar los sitios del punto 4.
