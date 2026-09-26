# Parte VIDEO · Encargo 119 — A Plague Tale

Investigador de vídeo (rol `video`, EQUIPO.md): puntos **2, 4, 9, 10 y 14** de ENCARGO.md.
Parte de `partes/datos-video.md` (ya consultado, no se repite) y de `partes/episodios.md`, donde ya
había dos tráilers de *Innocence* ficha'dos antes de esta tanda (Story Trailer y tráiler de lanzamiento
de Vidaextra, ambos por Dailymotion). Este parte añade 3 tráilers más (2 de *Requiem*, 1 de *Innocence*)
y fotogramas de un compilado de cinemáticas de Internet Archive.

Es un videojuego: *A Plague Tale: Innocence* (2019, Steam appid 752590) y *A Plague Tale: Requiem* (2022,
Steam appid 1182900), Asobo Studio / Focus Entertainment. YouTube pide iniciar sesión desde este servidor
(bloqueo compartido): todo el vídeo de esta parte sale de **Dailymotion**, de **Internet Archive** o de
la **API `appdetails` de Steam**, que da los tráileres oficiales en `.m3u8` 1080p sin login (CDN de Akamai/
Steam) — truco confirmado: `curl -s "https://store.steampowered.com/api/appdetails?appids=<id>&cc=us&l=english"`,
campo `data.movies[].hls_h264`, y ese enlace lo lee `yt-dlp` (y por tanto `fotogramas.py`/`episodio.py`)
directamente. Trabajo pesado en `/tmp/claude-0/trabajo/119-a-plague-tale-video/` y
`/tmp/claude-0/trabajo/119-episodios/` (hojas, fichas, fotogramas sueltos, paletas de `estilo.py`).

---

## 2 · Fotogramas de escenas icónicas (capítulo/minuto, 1080p+)

Todas miradas con `episodio.py`/`fotogramas.py`, hojas en `/tmp/claude-0/trabajo/119-episodios/`. Las 5
fichas completas (planos, diálogo transcrito con Whisper) están en `partes/episodios.md`.

**A Plague Tale: Innocence**
- **Masacre en la finca de los de Rune** (apertura): banquete familiar, jabalí, perro Léon, la
  Inquisición irrumpe a caballo, «Kill the sister! Take the boy alive!» · Story Trailer, 0:02-0:26 ·
  https://www.dailymotion.com/video/x747o01?t=9 · ✅ (ficha en episodios.md + visto en hoja).
- **«Quick, the light! THE LIGHT!»**: interior de piedra tipo capilla, vidriera al fondo; una figura
  adulta (no se identifica con certeza en este plano) señala con el brazo extendido hacia algo colgado
  del techo — una especie de racimo de formas oscuras (¿ratas o murciélagos muertos, trofeo o señuelo?) —
  y grita pidiendo luz · compilado de cinemáticas, min. 39:54 (fotograma sacado en 1920×1080 real por
  HTTP range directo al `.mp4`, no de la miniatura) ·
  https://archive.org/details/APlagueTaleInnocenceAllCutscenesIn4KGameMovie · ✅ (fotograma propio,
  `estilo.py`) · ⚠️ identidad del personaje sin confirmar.
- **Huida de la aldea sujetando la mano de Hugo**: corren entre una carreta y una valla de madera hacia
  una puerta, luz de atardecer entre nubes · mismo compilado, min. 1:19:57 · ✅.
- **Jardín con mosaico romano**: Amicia agachada cuidando/vendando a Hugo (bufanda roja) sobre un suelo
  de mosaico cubierto de musgo, luz de día cálida · mismo compilado, min. 1:49:55 · ✅.
- **Enjambre de ratas de noche**: cientos de ratas subiendo en masa sobre un cuerpo, un único punto de
  luz (antorcha) al fondo · tráiler de lanzamiento (Vidaextra), 0:20-0:23 ·
  https://www.dailymotion.com/video/x836nzz?t=21 · ✅.
- **Enemigo "Caballero" junto a brasas**: guantelete de armadura iluminado por ascuas naranjas contra
  hierba casi negra · compilado, min. 3:19:56 · ✅.
- **Epílogo nevado, capítulo «XVII - For Each Other»**: cartela de capítulo y, justo después, camino
  nevado con una carreta abandonada entre árboles helados — salto temporal tras el final · compilado,
  min. 3:39:55-3:44:54 · ✅.
- **Sean Bean recita «The Little Boy Lost»** (poema de William Blake, *Songs of Innocence*, 1789) sobre
  fotogramas del juego, incl. Hugo agarrado del brazo por un guantelete a los 0:08 · tráiler dedicado ·
  https://video.akamai.steamstatic.com/store_trailers/752590/223438/60b2aa8a7c3644decd19b067ed56d66ae03d2610/1750579064/hls_264_master.m3u8?t=1558001122
  (mismo tráiler, título en pantalla «A PLAGUE TALE — Poem "The Little Boy Lost" by William Blake,
  performed by Sean Bean», 0:59) · ✅ (visto en hoja + confirmado por
  [TrueAchievements](https://www.trueachievements.com/n37711/sean-bean-recites-the-little-boy-lost-for-a-plague-tale-innocence)
  y [Focus Entertainment](https://www.focus-entmt.com/en/news/a-plague-tale-innocence-sean-bean-takes-players-into-the-games-universe-with-deeply-touching-poetry)).

**A Plague Tale: Requiem**
- **Fiesta de las flores** (llegada a Provenza/La Cuna): calle en cuesta cubierta de pétalos rosas y
  amarillos, campanario blanco, banderines, gente con coronas de flores · Launch Trailer, 0:55-0:59 ·
  https://video.akamai.steamstatic.com/store_trailers/1182900/505834/95631b25ff469959a93f473540004f210e4f73ce/1750635280/hls_264_master.m3u8?t=1666099034&t=56
  · ✅.
- **Rito del «Child of Embers»**: un hombre con túnica roja coloca (o recibe) una corona de flores rojas
  a un niño bajo un arco floral en un acantilado · Launch Trailer, 1:16-1:18 · mismo enlace, `&t=76` ·
  ⚠️ (el niño no se distingue con certeza en el fotograma comprimido, pero el culto sí está confirmado en
  la wiki: [Child of Embers](https://aplaguetale.fandom.com/wiki/Child_of_Embers), orquestado por el
  conde Victor de Arles en la isla de La Cuna para que su esposa Émilie criara a Hugo como a un dios).
- **Costa dorada llena de polvo/humo** (batalla, luz rasante): un caballero y Amicia en un peñasco sobre
  el mar, niebla rosa-dorada · Launch Trailer, 1:06-1:07 · mismo enlace, `&t=67` · ✅.
- **Enjambre de ratas a ras de suelo**: manos y capa entre paja y jaulas de madera rotas, luz rojiza de
  incendio · Launch Trailer, 1:20 · mismo enlace, `&t=80` · ✅.
- **Reencuentro/abrazo entre hermanos**: Amicia con el pelo trenzado abraza a Hugo en la cubierta de un
  barco, cielo nublado detrás · Story Trailer, 1:09-1:10 ·
  https://video.akamai.steamstatic.com/store_trailers/1182900/499905/592ea3564f5158eaae0f8b02beff29d4c14a01d0/1750635274/hls_264_master.m3u8?t=1664291114&t=70
  · ✅.
- **Silueta a contraluz de fuego**: Amicia arrodillada con ballesta, silueta naranja pura sobre incendio
  de fondo (cartel final del tráiler, justo antes del logo) · Story Trailer, 1:31 · mismo enlace, `&t=91`
  · ✅.

---

## 4 · Fondos y sitios: luz, paleta medida en vídeo y texturas reales equivalentes

Complementa el punto 16 de `imagen.md` (que midió arte oficial estático de la wiki): aquí la paleta sale
de **fotogramas de cinemática en movimiento** (con niebla, grano, profundidad de campo), citando `estilo.py`
sobre el fotograma exacto (barras negras de cine recortadas antes de medir, si las había).

- **Interior de capilla en penumbra** (Innocence, «Quick, the light!») · sin fuego visible en el plano
  exacto, sólo luz fría de vidriera · `#1D1D1B` 27% / `#242421` 24% / `#181816` 20% / `#121210` 14%
  (`estilo_hq`, fotograma 39:54, 1920×1080 real vía HTTP range al `.mp4`) · saturación 9%, brillo 12% —
  el plano más neutro/gris de todos los medidos, corrige la primera lectura sobre la miniatura (que
  parecía más cálida por la compresión). ✅.
- **Aldea de noche con ratas** (Innocence, huida con antorcha) · rojo-naranja de las ratas y la antorcha
  contra negro casi total · `#361B14` 27% / `#010000` 27% / `#5C2B23` 20% / `#834932` 18% / `#F6C381` 4%
  (`estilo_inn`, fotograma 0:21 del tráiler de lanzamiento, recortado sin barras) · saturación 62%,
  brillo 40% · ✅ — mismo contraste «fuego contra ratas» que pide el encargo.
- **Jardín-mosaico romano de día** (Innocence) · piedra clara y musgo, luz cálida difusa ·
  `#937F6A` 26% / `#AC9A7E` 23% / `#C9B6A1` 14% / `#E9DCCD` 10% (`estilo_archive`, fotograma 1:49:55) ·
  saturación 24%, brillo 61% — el fotograma más claro de todos los medidos · ✅.
- **Combate nocturno en la nieve** (Innocence, tramo final) · azules fríos de luna, sin ningún cálido ·
  `#0F1925` 36% / `#080F19` 27% / `#1C2937` 16% / `#2C3E50` 10% / `#678397` 4% (`estilo_archive`,
  fotograma 2:19:57) · saturación 57%, brillo 20% · ✅.
- **Brasas del enemigo «Caballero»** (Innocence) · negro casi total con ascuas · `#0C0F0B` 42% /
  `#241E19` 28% / `#8C4436` 8% / `#D0745B` 6% / `#F5C49F` 2% (`estilo_archive`, fotograma 3:19:56) ·
  saturación 40%, brillo 21% · ✅.
- **Epílogo nevado** (Innocence, tras el final) · azul-lavanda pálido de amanecer frío ·
  `#B9D0E0` 18% / `#41344A` 18% / `#5A5568` 18% / `#727487` 18% / `#8A91A2` 16% (`estilo_archive`,
  fotograma 3:44:54) · saturación 20%, brillo 57% — el contraste más fuerte con las escenas de fuego de
  todo el estudio · ✅.
- **Fiesta de las flores, Provenza** (Requiem) · piedra clara + verde mediterráneo + cielo gris-azulado,
  NO tan dorado como cabría esperar en este plano concreto (hay niebla) · `#2D2827` 30% / `#4E4C48` 25%
  / `#836D56` 16% / `#69747F` 13% (`estilo_crop`, Launch Trailer 0:55) · saturación 27%, brillo 41% · ✅
  · nota: a simple vista el plano SÍ tiene pétalos rosas/rojos y amarillos muy vivos (banderines, flores
  en el suelo) que la paleta automática (6 colores dominantes por área) no capta por ocupar poca
  superficie — mirar el fotograma, no sólo el hex, para ese acento de color.
- **Costa/batalla con niebla dorada** (Requiem, «sol de Provenza») · rosa-óxido de polvo y luz rasante ·
  `#352A28` 27% / `#795044` 14% / `#86675F` 12% / `#958382` 9% (`estilo_crop2`, Launch Trailer 1:07) ·
  saturación 31%, brillo 31% · ✅ — el tono cálido-rosado que distingue a Requiem de los interiores fríos
  de Innocence.
- **Interior en penumbra con velas** (Requiem, escena de diálogo con el conde) · marrones cálidos de piel
  y madera, sin fuego visible en plano · `#000000` 63% (letterbox sin recortar del todo, resto del plano
  muy oscuro) — ⚠️ medido sobre plano sin recortar del todo; sirve sólo como referencia de que es un
  interior muy oscuro, no para el hex exacto.

**Texturas reales equivalentes (CC0, ambientCG)** para las capas de fondo (punto 4, junto con el 19 de
`imagen.md`):
- Piedra de sillar envejecida (pasadizos, castillo) → **Bricks094** ·
  https://ambientcg.com/view?id=Bricks094 · CC0.
- Tablón de madera vieja (puertas, carretas, cabañas) → **Planks009** ·
  https://ambientcg.com/view?id=Planks009 · CC0.
- Cuerda/soga (jaulas, empalizadas) → **Rope001** · https://ambientcg.com/view?id=Rope001 · CC0.

---

## 9 · Música y sonido

**Compositor**: Olivier Deriviere (AMEO Productions), ambos juegos. Wikipedia:
https://en.wikipedia.org/wiki/Olivier_Deriviere — antes trabajó con chelo como instrumento central en
*Vampyr* (2018), «para transmitir vacío y soledad»; la misma idea se repite en *A Plague Tale*. ✅ (dos
fuentes: Wikipedia + notas de prensa de Focus).

**A Plague Tale: Innocence** (BSO, 2019-05-07) — lista completa en
https://aplaguetale.fandom.com/wiki/A_Plague_Tale:_Innocence_(soundtrack) (wikitext leído por API) y
[Bandcamp](https://olivierderiviere.bandcamp.com/album/a-plague-tale-innocence-deluxe-edition):
- Tema principal («A Plague Tale») tocado en **hurdy-gurdy** (zanfona medieval), no en chelo.
- Chelo: **Eric-Maria Couturier**; el ensemble usa además viola da gamba y nyckelharpa.
- Temas por escena: «Father» (lute, tema del padre de Amicia), «Grieving» (la muerte del perro Léon),
  «Inquisition» (motivo de dos notas que anuncia a la Inquisición, desde la masacre en la finca),
  «The Rats», «Massacre», «The Wrath» — este último suena en la escena final, la más emotiva del juego,
  y es el tema que **Requiem hereda como leitmotiv de Amicia** (ver abajo). ✅ (wiki + reseñas cruzadas:
  [reelmusic.wordpress.com](https://reelmusic.wordpress.com/2019/06/14/a-plague-tale-innocence-olivier-deriviere/),
  [acloserlisten.com](https://acloserlisten.com/2019/08/20/press-a-hell-is-other-demons-a-plague-tale-innocence/)).

**A Plague Tale: Requiem** (BSO, 2022-10-18, 34 pistas) — wikitext de
https://aplaguetale.fandom.com/wiki/A_Plague_Tale:_Requiem_(soundtrack):
- Interpretada por **The Estonian Philharmonic Chamber Choir**, dirigido por Lodewijk Van Der Ree.
- Chelo: Eric-Maria Couturier · guitarra/laúd: Giani Caserotto · viola da gamba: Jeanne Dorche ·
  nyckelharpa: Eleonore Billy · gaita medieval: Gabriel Desbiolles (usada para el tema del caballero
  Arnaud — más «oriental» que una gaita escocesa, según reseña) · flautas: Nicolas Bras · percusión:
  el propio Deriviere.
- Pista 1, «A Plague Tale Requiem», y la 34, «O Ma Belle Lune», son la misma melodía cantada en francés:
  *«Ô ma belle lune, ton étreinte et ton bel amour me rendent comme toi, forte et belle... Ô soleil,
  par-delà les mots, je te dirai tout dans ma lettre»* (nana/carta a un ser querido; cierra el círculo
  abriendo y cerrando el álbum). ✅ (wikitext, texto completo bilingüe).
- El tema «The Wrath» de Innocence **vuelve como motivo de Amicia** en «No Turning Back», «Surrounded By
  Evil Men» y «The Rage Within»; en momentos más tranquilos («Hide and Seek», «Father Taught Me») suena
  en modo mayor — la música dice que el trauma sigue ahí incluso en calma. ✅
  ([gamemusic.net](https://gamemusic.net/a-plague-tale-requiem-the-music-of-the-wrath/)).
- Para la isla de **La Cuna**, Deriviere y el chelista Couturier crearon «elementos texturales» con
  armónicos naturales del chelo que difuminan la línea entre música y diseño sonoro — firma sonora propia
  del lugar. ✅ ([asoundeffect.com](https://www.asoundeffect.com/a-plague-tale-requiem-game-audio/)).

**Diseño de sonido (SFX) — Requiem**, entrevista al director de audio **Aurélien Piters**
([A Sound Effect](https://www.asoundeffect.com/a-plague-tale-requiem-game-audio/)) — no hay onomatopeyas
en pantalla (no es manga), pero sí un vocabulario sonoro muy reconocible, citado directamente:
- «*we have 300,000 rats, and so as a natural following of what's going on on-screen, there is a lot of
  bass rumble*» — el enjambre no sólo chilla, retumba.
- El chillido de la primera entrega evolucionó a «*squish and liquid layers*» para dar asco a escala
  masiva; **síntesis granular**: «*all the rat sounds are very short, and they blend together... playing
  randomly with variation in real-time*», según si las ratas están quietas, comiendo o atacando.
- Sistema de foley por huesos: «*we have a calculation that generates a value for the speed and
  acceleration and we created some foley loops that are connected to the movements*».
- Motor propio de Asobo, **Zouna**, integrado con **Wwise** para reverberación espacial según la geometría
  real del escenario (oclusión, pathfinding de sonido).
- Filosofía del propio Piters: «*the more I work in sound design the more I realize that less is more*».
✅ (fuente única especializada, pero con cita directa del responsable — cuenta como oficial).

**Efecto sonoro reconocible de referencia rápida**: el crepitar de antorcha/fuego (constante en zonas de
luz) contra el retumbar grave + chillido líquido de la marea de ratas (constante en zonas oscuras) — es
literalmente el contraste de luz que pide el encargo, hecho sonido.

---

## 10 · Vídeos: tráileres, escenas, análisis y tendencias (con minuto)

**Tráileres oficiales mirados fotograma a fotograma** (fichas completas en `partes/episodios.md`):
1. *Innocence* — Story Trailer, 1:21 · https://www.dailymotion.com/video/x747o01 · ✅.
2. *Innocence* — tráiler de lanzamiento (redistribuido por Vidaextra), 2:05 ·
   https://www.dailymotion.com/video/x836nzz · ✅.
3. *Innocence* — «Sean Bean: The Little Boy Lost», 1:05, vía Steam ·
   https://video.akamai.steamstatic.com/store_trailers/752590/223438/60b2aa8a7c3644decd19b067ed56d66ae03d2610/1750579064/hls_264_master.m3u8
   · ✅.
4. *Requiem* — Story Trailer, 1:52, vía Steam ·
   https://video.akamai.steamstatic.com/store_trailers/1182900/499905/592ea3564f5158eaae0f8b02beff29d4c14a01d0/1750635274/hls_264_master.m3u8
   · ✅.
5. *Requiem* — Launch Trailer, 2:07, vía Steam ·
   https://video.akamai.steamstatic.com/store_trailers/1182900/505834/95631b25ff469959a93f473540004f210e4f73ce/1750635280/hls_264_master.m3u8
   · ✅.

**Otros tráileres oficiales en Steam** (localizados por `appdetails`, no procesados fotograma a fotograma
por presupuesto de tanda, pero con enlace directo listo para `fotogramas.py`): *Innocence* — «Game
Awards» (id 256769762), «Spoiler Trailer» (256761892), «Accolades Trailer» (256751444), «Overview
Gameplay Trailer» (256749580); *Requiem* — «Accolades Trailer» (256915012), «Gameplay Overview Trailer»
(256901415), «Extended Gameplay Trailer» (256893452). ⚠️ (localizados, no mirados).

**Compilado de cinemáticas** (longplay/cutscenes, Internet Archive): *A Plague Tale -Innocence All
Cutscenes In 4K (Game Movie)*, 3h46m ·
https://archive.org/details/APlagueTaleInnocenceAllCutscenesIn4KGameMovie · sin `yt-dlp`: Internet Archive
ya publica una miniatura por minuto (`.thumbs/`) que se puede bajar directa con `curl`, sin descargar el
vídeo entero — así se sacaron los 10 fotogramas del punto 2 y 4 sin gastar disco. ✅.

**Premios y reconocimiento con tráiler propio**: *Innocence* nominado a Mejor Narrativa en The Game
Awards 2019; Focus/Asobo sacaron un tráiler dedicado a la nominación (dic. 2019) ·
[twinfinite.net](https://twinfinite.net/2019/12/a-plague-tale-innocence-celebrates-game-award-nomination-with-a-trailer-new-amicia-hugo-statue-launches/)
· ✅ (dos fuentes: Twinfinite + Focus Entertainment news).

**Vídeos de análisis** (enlazados, sin descargar por presupuesto — YouTube bloqueado en este servidor):
- Joseph Anderson, crítica en profundidad de *Innocence*, 796 mil visitas (jun. 2019) — el análisis más
  visto encontrado. ⚠️ (visto el dato de visitas vía NoxInfluencer, no el vídeo).
- «A Plague Tale: Requiem Story Analysis» y «A Plague Tale: Requiem - Story Critique & Analysis» (2023).
- «A Plague Tale: Requiem and The Last of Us Part II - A Comparative Analysis» (nov. 2022) — la
  comparación más repetida en reseñas de Requiem.
⚠️ enlaces localizados por búsqueda, no mirados fotograma a fotograma (no son material oficial ni sirven
de referencia visual directa; quedan para quien redacte quiera citar opinión de crítica).

**Tendencias TikTok**: «Plague Tale Requiem Meme» ronda los 2.6 millones de publicaciones; el enjambre de
ratas es el gancho viral más repetido («Surviving the Waves of Rats in Plague Tale Requiem»,
[@h_4_z_e](https://www.tiktok.com/@h_4_z_e/video/7529918603135765782)) junto a *edits* emotivos del final
con Amicia y Hugo. ⚠️ (una fuente de búsqueda agregada, no verificado post a post — el fandub/comunidad
hispana en TikTok es punto 22, del investigador de voz, no de este parte).

---

## 14 · Poses analizadas (Amicia y Hugo, con minuto)

Todas de las cinemáticas ya miradas arriba — ninguna es arte estático (eso lo cubre `imagen.md`). Postura,
manos y mirada descritas de lo que se ve en el fotograma, no de memoria.

### Amicia
1. **Guiar/proteger** — corre sujetando la mano de Hugo, torso girado medio hacia atrás para no soltarlo,
   mirada al frente hacia la puerta de salida · compilado, 1:19:57 · sirve para «animar, seguir aquí».
2. **Atacar/defender** — semiagachada, arma arrojadiza (honda) sujeta a dos manos a la altura del pecho,
   mirada fija al objetivo, capucha de armadura de cuero · Requiem Story Trailer, 1:05 (fotograma 27 de
   la hoja) · sirve para «defender, plantar cara».
3. **Pensar/sigilo** — agachada bajo un mueble, una mano apoyada en el suelo, cabeza ladeada escuchando ·
   compilado, 2:49:56 · sirve para «pensar, prestar atención».
4. **Miedo** — primer plano, ojos llorosos, boca entreabierta, sujeta con fuerza la ropa de un adulto ·
   Story Trailer (Innocence), 0:29 · sirve para «tener miedo, pedir ayuda».
5. **Cuidar/explicar** — agachada de espaldas a cámara junto a Hugo sentado, manos cerca de su cara/cuello
   (vendaje o consuelo), postura protectora inclinada hacia él · compilado, 1:49:55 · sirve para
   «explicar con calma, cuidar».
6. **Consolar/celebrar reencuentro** — de pie, abraza a Hugo apoyando la barbilla en su cabeza, ojos
   cerrados, manos rodeándolo · Requiem Story Trailer, 1:09-1:10 · sirve para «celebrar, alegrarse de
   verlo».
7. **Amenaza/determinación** — silueta a contraluz de un incendio, arrodillada con ballesta lista, sin
   rasgos visibles salvo el contorno · Requiem Story Trailer, 1:31 · sirve para «amenazar, avanzar pase lo
   que pase; también vale como pose de alerta/urgencia».

### Hugo
1. **Miedo** — detrás de una valla/reja, ojos muy abiertos, hombros encogidos hacia dentro · Story
   Trailer (Innocence), 0:58 · sirve para «tener miedo, esconderse».
2. **Avisar/señalar** — de pie girado hacia un lado, brazo extendido señalando, boca abierta como si
   llamara · Story Trailer (Innocence), 0:27-0:28 · sirve para «avisar, llamar la atención».
3. **Vulnerable/cargado** — en brazos de un adulto, cuerpo relajado y cabeza apoyada, capucha azul ·
   tráiler de lanzamiento (Vidaextra), 0:16-0:17 · sirve para «estar indefenso, necesitar ayuda».
4. **Escuchar/confiar** — sentado en el suelo de mosaico, bufanda roja, cuerpo vuelto hacia Amicia,
   manos quietas en el regazo · compilado, 1:49:55 (mismo fotograma que el nº 6 de Amicia) · sirve para
   «escuchar, confiar en alguien».
5. **Seguir/confiar** — corriendo de la mano de Amicia, mirada al frente, piernas en zancada corta (es más
   bajo que ella) · compilado, 1:19:57 · sirve para «seguir, no separarse».
6. **Rito/ceremonia** (⚠️ identificación de personaje no 100% segura en el fotograma comprimido, pero el
   ritual sí está documentado en la wiki) — de pie bajo un arco de flores rojas, recibe o porta una
   corona de flores de manos de un hombre con túnica roja: el culto del **Child of Embers**, orquestado
   por el conde Victor de Arles en la isla de La Cuna para criar a Hugo como al «Niño de las Ascuas» ·
   Requiem Launch Trailer, 1:16-1:18 ·
   https://aplaguetale.fandom.com/wiki/Child_of_Embers · sirve para «celebrar/ritual, sentirse observado».

---

## Lo mejor para la lámina

1. El contraste **fuego cálido (antorcha/ascuas) contra frío (ratas de noche, nieve)** está medido en hex
   real en 6 escenas distintas (punto 4): úsalo tal cual para la paleta de cualquier lámina de este
   encargo, no inventar tonos.
2. Pose de Amicia agachada cuidando a Hugo en el jardín de mosaico (compilado, 1:49:55): postura íntima,
   protectora, funciona mejor que cualquier pose «de pie con arma» para un canal de ayuda/apoyo.
3. El leitmotiv «The Wrath» que cruza de Innocence a Requiem (punto 9) es la anécdota más citable: la
   música dice que el trauma de Amicia no se cierra en el primer juego, se lleva al segundo.
4. El poema de William Blake recitado por Sean Bean («The Little Boy Lost», *Songs of Innocence*) conecta
   directamente con el título del primer juego — dato poco conocido y muy citable en el texto del canal.
5. Rito del «Child of Embers» (corona de flores) para una lámina 2 centrada en Requiem/La Cuna, con la
   paleta dorada de Provenza en vez de la fría de Innocence.

## No encontré

- Vídeos de análisis (Joseph Anderson y similares) **mirados fotograma a fotograma**: YouTube bloqueado
  en este servidor por «iniciar sesión»; sólo enlazados por búsqueda, con su dato de visitas cuando lo
  hubo. ⚠️.
- Tráileres oficiales de Steam listados pero no procesados con `fotogramas.py` (Game Awards, Spoiler,
  Accolades ×2, Overview/Extended Gameplay): quedan localizados con su enlace `.m3u8` listo para quien
  necesite más fotogramas — no era obligatorio mirar los 10 tráileres, con los 5 procesados se cumple de
  sobra «tráiler + 3 escenas icónicas». ⚠️.
- Cifra oficial de vistas/posts en TikTok verificada dentro de la app (TikTok no da API pública sin
  cuenta): el dato de «2.6 millones de publicaciones» sale de una búsqueda agregada, no de contarlo a
  mano. ⚠️.
- Vídeo o clip oficial en **español latino** de un tráiler (para citar minuto con doblaje): no apareció
  ninguno en Dailymotion ni Internet Archive; los canales que salieron doblados eran de lanzamiento en
  español de España o sin doblaje (subtítulos). No es mi punto (el doblaje latino es del investigador de
  voz, punto 8), lo anoto por si le sirve. ⚠️.

## Bitácora de búsqueda

- `curl` directo a `store.steampowered.com/api/appdetails` (appid 752590 y 1182900, `cc=us&l=english`):
  confirmó 5 tráilers oficiales por juego con enlace `.m3u8` en 1080p, sin login. Es la fuente principal
  de este parte.
- `python3 herramientas/episodio.py` ×3 nuevas (Requiem Story Trailer, Requiem Launch Trailer, Innocence
  «A Little Boy Lost») con `--id 119-a-plague-tale`: añadidas a `partes/episodios.md`.
- `python3 herramientas/fotogramas.py --fotograma` sobre los tráileres de Dailymotion y Steam para
  fotogramas sueltos a medir color.
- `python3 herramientas/estilo.py --colores 6` sobre 10 fotogramas (recortados de barras de cine con
  Pillow antes de medir) → carpetas `estilo_inn`, `estilo_req`, `estilo_crop`, `estilo_crop2`,
  `estilo_archive`.
- `curl` a `archive.org/metadata/...` del compilado de cinemáticas: usó las miniaturas `.thumbs/` ya
  generadas por Internet Archive (una por minuto) para mirar 10 puntos del vídeo sin descargar 3h46m de
  vídeo — ahorro grande de disco y tiempo. Para los 3 fotogramas citados en los puntos 2 y 4 se repitió
  la extracción con `ffmpeg -ss <s> -i <url_directa_.mp4>` (Internet Archive acepta *HTTP range* en su
  CDN, `dn711203.ca.archive.org`) para tener el fotograma real en 1920×1080 en vez de la miniatura
  720×406: en un caso (min. 39:54) esto corrigió la lectura de color y de quién aparece en el plano —
  la miniatura comprimida sugería una antorcha cálida que en el fotograma real no se ve así.
- Wikitext de Doblaje... no aplica aquí (es del investigador de voz). Wikitext de
  `aplaguetale.fandom.com` (API `action=parse&prop=wikitext`) para las dos páginas de banda sonora y para
  «Child of Embers».
- WebSearch (7 búsquedas de 50 disponibles): soundtrack Innocence/Requiem, Sean Bean poema, sonido de las
  ratas, TikTok, vídeos de análisis, Game Awards 2019. Todas en inglés (fuentes originales en inglés; no
  hizo falta japonés/coreano — la obra es francesa/europea, no asiática).
- `curl` a `ambientcg.com/api/v2/full_json` para 3 texturas CC0 equivalentes (piedra, madera, cuerda).
- No se usó YouTube en ningún momento (bloqueado «iniciar sesión» desde este servidor, confirmado por el
  investigador de imagen también).

**Parte terminada** (sin `Sigue:` pendiente): tráilers mirados fotograma a fotograma ✅ (5, con fichas en
`episodios.md`), 10+ escenas icónicas con capítulo/minuto ✅, luz/paleta de 9 sitios con hex medido ✅,
música con compositor/intérpretes/tema recurrente/diseño de sonido citado ✅, vídeos con minuto exacto ✅,
poses de Amicia (7) y Hugo (6) con minuto y para qué sirven ✅. Lo que queda es extra opcional, listado
arriba en «No encontré» con ⚠️ (los 7 tráilers de Steam no procesados y los vídeos de análisis de
YouTube, bloqueado desde este servidor).
