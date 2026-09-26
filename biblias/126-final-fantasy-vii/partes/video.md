# Parte de VÍDEO · Final Fantasy VII (encargo 126)

Investigador de vídeo: puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Libreta de datos, no prosa.
Sin serie hermana para este encargo (único encargo de Final Fantasy VII en `encargos/`).
Es un videojuego (1997, con Remake/Rebirth 2020-2024): no hay "capítulos" de anime ni doblaje
cantado de opening/ending. Se tratan como: la cinemática de introducción del juego (opening),
la cinemática final del juego (ending), el tráiler oficial más reciente (Rebirth) y varias
escenas icónicas de la trama. YouTube pide iniciar sesión en este servidor: todo se vio con
`fotogramas.py` sobre clips oficiales de prensa en Dailymotion (canal «JeuxVideo.com», medio
francés con licencia para publicar cinemáticas del juego completo, y «3djuegos» en español para
el tráiler de Rebirth). Hojas de contacto en `/tmp/claude-0/trabajo/126-final-fantasy-vii-video/`.

## 2 · Fotogramas de escenas icónicas

Vistas fotograma a fotograma con `herramientas/fotogramas.py`. **Límite de resolución real**:
comprobado con `yt-dlp -F` sobre el clip x89nb1q, Dailymotion sólo sirve estos clips de prensa a
512×288 (formato único `hls-380`); no hay manera de pasar de ahí sin iniciar sesión en YouTube.
⚠️ No se llegó a 1080p (lo pide el punto), ver «No encontré».

- **Opening** — «FINAL FANTASY VII REMAKE - Opening Movie» (JeuxVideo.com, 13 071 vistas) · https://www.dailymotion.com/video/x89nb1q · ✅ (vídeo oficial Square Enix, coincide con la cinemática real de apertura del Remake 2020, comprobado también en la ficha de MobyGames) · 5:21, cada 10 s
  - 0:00-0:50 desierto/yermo, niebla, luego la torre del reactor de mako perfilándose entre el humo · &t=0
  - 1:00-1:10 calle del Sector 7, coches viejos, gente caminando (barrio bajo de Midgar) · &t=60
  - 1:20 niños en bicicleta jugando en la calle · &t=80
  - 1:40 parque infantil oxidado con el reactor de fondo · &t=100
  - 2:10-2:50 Aerith en el sótano de la iglesia, luciérnagas verdes de mako flotando, coge una flor amarilla · &t=130
  - 3:00-3:50 calle nocturna, Aerith vende la flor, plano aéreo de la Torre Shinra iluminada sobre la ciudad · &t=180
  - 4:00 primer plano de Cloud de perfil, pelo rubio de punta · &t=240
  - 5:00 Cloud desenvainando la Buster Sword agachado, listo para saltar del tren · &t=300
- **Opening (versión técnica 2005)** — «Final Fantasy VII : Cinématique d'introduction» (JeuxVideo.com) · https://www.dailymotion.com/video/x89cm28 · ✅ (el propio vídeo se identifica en pantalla como «FINAL FANTASY VII TECHNICAL DEMO FOR PS3», el famoso tech demo de E3 2005 que mostró la misión de bombardeo con gráficos de PS3 años antes del Remake real) · 1:36, cada 4 s
  - 0:04-0:08 destello de energía verde/azul de mako, tubos del reactor · &t=4
  - 0:16-0:40 Aerith en el pasillo del reactor, cae de rodillas, se agarra la muñeca (secuencia de captura) · &t=16
  - 1:12-1:20 ciudad de Midgar vista desde arriba, luces verdes de mako en la noche · &t=72
  - 1:32 primer plano de Cloud, ojos mako brillantes, mirando serio · &t=92
- **Ending** — «Final Fantasy VII : Fin Partie 4» (JeuxVideo.com) · https://www.dailymotion.com/video/x89clzs · ✅ (parte final de la cinemática de cierre real del juego; el logo «FINAL FANTASY VII» aparece a los 1:20, confirma que es el final oficial) · 3:19, cada 8 s
  - 0:56 Nanaki (Red XIII) aúlla sobre un peñasco, con dos cachorros a su lado · &t=56
  - 1:04-1:12 la cámara se aleja y revela Midgar en ruinas, 500 años después, cubierta de bosque · &t=64
  - 1:20 logo «FINAL FANTASY VII» sobre fondo blanco, cierre de marca · &t=80
  - 1:28-3:19 pantalla negra con destellos verdes (Lifestream) para los créditos finales · &t=88
- **Escena icónica 1 — muerte de Aerith** «Final Fantasy VII : Adieu Aerith» (JeuxVideo.com) · https://www.dailymotion.com/video/x89cm2f · ✅ (coincide con la secuencia documentada en todas las guías del juego, Ciudad Olvidada/altar) · 1:37, cada 4 s
  - 0:08-0:20 el grupo camina hacia un altar circular sobre el agua, iluminado desde arriba · &t=8
  - 0:44-0:48 una silueta cae en picado con una espada larga (Sephiroth/Masamune) hacia Aerith arrodillada rezando · &t=44
  - 0:52-1:04 imágenes del gigante blanco óseo (criatura de la Corriente Vital) entre árboles nevados · &t=52
  - 1:08 primer plano del rostro de Aerith, ya inerte, sostenida por Cloud · &t=68
  - 1:12-1:32 Cloud hunde el cuerpo de Aerith en el lago; ella queda flotando, un halo de luz azul-verde la envuelve · &t=72
  - 1:36 plano cenital, el cuerpo se hunde en el agua turquesa · &t=96
- **Escena icónica 2 — Nibelheim en llamas (flashback de Sephiroth)** «Final Fantasy VII : Sephiroth à Nibelheim» (Gameblog, versión PC/Steam re-master con subtítulos en inglés) · https://www.dailymotion.com/video/x2yc6on · ✅ (coincide con el flashback documentado del Disco 1, biblioteca de la mansión Shinra + incendio del pueblo) · 10:25, cada 20 s
  - 0:40-2:40 Sephiroth lee en voz alta, en la biblioteca de la mansión Shinra, sobre los Cetra y el Proyecto Jenova («The Jenova Project wanted to produce people with the pow[er of the Ancients]») · &t=40
  - 3:00-3:40 desciende a la cámara del reactor bajo el pueblo, ambiente morado/verdoso oscuro · &t=180
  - 4:00-6:00 el pueblo de Nibelheim entero en llamas, casas de madera ardiendo, Sephiroth camina entre el fuego con la Masamune al hombro · &t=240
  - 6:00 Tifa acusa a Cloud/pregunta «Sephiroth did this to you, didn't he?!» · &t=360
  - 6:20-8:00 cámara de especímenes Jenova, cápsulas verdes con criaturas flotando en fila · &t=380
  - 9:00 primer plano del rostro de Sephiroth, pelo plateado, ojo verde mako · &t=540
  - 9:20-10:20 combate final de esa secuencia en la sala del reactor, energía azul brillante alrededor de Sephiroth · &t=560
- **Escena icónica 3 — caída de la placa del Sector 7** «Final Fantasy VII : Les ruines du secteur 7» (JeuxVideo.com) · https://www.dailymotion.com/video/x89clz1 · ✅ (coincide con la misión documentada «Sector 7 Plate Fall», capítulo 8-9 del Disco 1) · 3:55, cada 8 s
  - 0:00-0:56 sala de control de la Torre Shinra, Heidegger y Tseng ordenan desactivar el sistema de emergencia de la placa · &t=0
  - 1:04-1:20 explosión en el pilar de soporte, un helicóptero dispara cohetes contra la estructura · &t=64
  - 2:08-2:24 la placa entera se desploma sobre el barrio bajo entre fuego y humo · &t=128
  - 2:48-3:04 Cloud y Barret caminan entre los escombros humeantes del Sector 7 destruido · &t=168
  - 3:20-3:28 cuadro de diálogo: Barret grita «Biggs!» y «MINCE, MINCE, MINCE!!!» (interjección francesa del doblaje de subtítulos) al encontrar a su compañero herido · &t=200

## 4 · Fondos y sitios (luz y paleta)

Paleta y luz **medidas con `herramientas/estilo.py --colores 5`** sobre fotogramas extraídos con
`ffmpeg` de los vídeos de arriba (no de wallpapers; eso es del investigador de imagen).

| Sitio | Fuente del fotograma | Luz | Paleta medida (hex) |
|---|---|---|---|
| Torre del reactor / Midgar (plano aéreo nocturno) | Opening Remake, 3:30 · https://www.dailymotion.com/video/x89nb1q&t=210 | Nocturna, contraluz industrial, casi sin color cálido | #141618 36% · #2C302E 34% · #474F47 19% · #6F7E6E 8% |
| Sector 7, barrio bajo (parque infantil de día) | Opening Remake, 1:20 · https://www.dailymotion.com/video/x89nb1q&t=80 | Diurna nublada, gris-azulada, poco contraste | #484952 31% · #716F71 24% · #272524 21% · #A09A92 18% |
| Nibelheim ardiendo (casas de madera en llamas) | Flashback Sephiroth, 4:00 · https://www.dailymotion.com/video/x2yc6on&t=240 | Fuego intenso, naranja-amarillo muy saturado | #6E3133 36% · #351417 27% · #D0633A 17% · #F8CA56 12% · #FEF9AE 7% |
| Ciudad Olvidada, altar sobre el lago | Muerte de Aerith, 1:16 · https://www.dailymotion.com/video/x89cm2f&t=76 | Azul-turquesa, luz difusa bajo el agua | #39423A 38% · #748285 20% · #C5E1E0 15% · #75ADDD 14% · #345EC9 13% |
| Cámara de especímenes Jenova (reactor de Nibelheim) | Flashback Sephiroth, 6:20 · https://www.dailymotion.com/video/x2yc6on&t=380 | Roja-marrón muy oscura, apenas un verde-azul de acento (cápsulas) | #35120F 52% · #61251D 25% · #39332F 14% · #3CB6AD 2% (acento cápsulas) |
| Sala de control de la Torre Shinra | Caída del Sector 7, 0:08 · https://www.dailymotion.com/video/x89clz1&t=8 | Verde industrial, luz artificial fría | #30361B 31% · #0E1504 29% · #585C3A 24% · #7D8C6E 12% |

- Estilo detectado por `estilo.py` en los 6 fotogramas: sombreado degradado/pintado con línea de
  contorno débil o normal (nada de línea negra dura, coherente con los renders 3D pre-hechos de
  PS1 y los remasters posteriores). ✅ (6 fotogramas medidos, mismo patrón).
- Texturas reales equivalentes para capas: madera quemada/carbonizada (Nibelheim) → «charred wood»
  o «burnt planks» en ambientCG; metal industrial oxidado verde (sala de control Shinra) →
  «rusted metal green» o «patina copper» en ambientCG; piedra húmeda azulada (altar Ciudad
  Olvidada) → «wet stone blue» o «marble tile». ⚠️ (identificado el tipo, no se bajó ningún
  archivo concreto de ambientCG por presupuesto de la tanda).

## 9 · Música y sonido

Tracklist real del álbum oficial (Internet Archive, coincide con MusicBrainz).

- «Final Fantasy VII Soundtrack» (Nobuo Uematsu/植松伸夫), 1997, 90 pistas · https://archive.org/details/final_fantasy_vii_soundtrack · ✅ (dos fuentes: Archive.org con tracklist completo + MusicBrainz confirma el álbum) · https://musicbrainz.org/release-group/7fab854c-8d2f-31f3-aa82-ad7cbf7532eb
  - Pista 02 «Opening ~ Bombing Mission»: suena en el arranque del juego, mientras Cloud salta del tren (coincide con el minuto 5:00 del vídeo de opening de arriba).
  - Pista 06 «Tifa's Theme»: melodía suave de piano, tema personal de Tifa.
  - Pista 25 «Main Theme of Final Fantasy VII»: el tema orquestal más reconocible de la saga, usado en momentos de esperanza/viaje.
  - Pista 38 «J-E-N-O-V-A»: tema de combate contra las formas de Jenova, ritmo urgente con coro.
  - Pista 47 «Life Stream»: ambiente etéreo, suena en las secuencias dentro de la Corriente Vital (la escena de los «recuerdos de Tifa», punto 14).
  - Pista 65 «Aeris' Theme»: tema de Aerith, suena en la Ciudad Olvidada y en su muerte (coincide con el clip del punto 2). El más citado por los fans como «la música que hace llorar».
  - Pista 87 «One-Winged Angel»: tema del combate final contra Safer∙Sephiroth, coro latino cantado, el más famoso de toda la banda sonora de Final Fantasy.
  - Pista 89 «Staff Roll»: tema de los créditos finales (coincide con el tramo negro/verde del final, punto 2).
- «Final Fantasy VII Remake Original Soundtrack» (Square Enix, arreglos de Uematsu + equipo) 2020-05-27 · https://musicbrainz.org/release-group/860ef6e3-5c3e-465b-861f-a2899b74b59d · ⚠️ (una fuente, MusicBrainz; no se escuchó pista a pista por presupuesto de la tanda).
- «FINAL FANTASY VII REBIRTH Original Soundtrack» 2024-04-10 · https://musicbrainz.org/release-group/beb22d58-426c-424a-8ed6-6b4859f3c1e0 · ⚠️ (una fuente, no escuchada).
- Ambiente sonoro confirmado al mirar los vídeos: cuando Barret grita «Biggs!» en el Sector 7 destruido (punto 2), la música se detiene por completo unos segundos antes de que entre el tema dramático — mismo recurso narrativo que en el clip de Nibelheim al oír «Sephiroth did this to you, didn't he?!» (silencio → grito → música). ✅ (visto en dos clips distintos, mismo patrón) · https://www.dailymotion.com/video/x89clz1&t=200 y https://www.dailymotion.com/video/x2yc6on&t=360
- Onomatopeya reconocible por el fandom: el «¡Kweh!» de los chocobos (pista 30-32 del OST, «Waltz/Electric/Cinco de Chocobo» llevan el sonido de fondo) ⚠️ (de memoria del ambiente del juego, no medido en espectrograma con `voz.py` porque no es una frase hablada).

## 10 · Vídeos (tráileres, escenas, tendencias)

- **Tráiler oficial** «Tráiler final de Final Fantasy VII: Rebirth» (3djuegos, en español, 43 325 vistas) · https://www.dailymotion.com/video/x8sb9z6 · ✅ (mismo tráiler también listado en JeuxVideo.com como «FINAL FANTASY VII REBIRTH Trailer», 34 354 vistas, https://www.dailymotion.com/video/x8lmfpp) · 4:08, visto fotograma a fotograma cada 12 s
  - 0:48 Aerith corriendo por un prado, con un ataque mágico rosa detrás (gameplay) · &t=48
  - 1:24-1:36 primer plano de Aerith, luego una escena tierna con Tifa acariciándole el pelo · &t=84
  - 1:48 una forma roja demoníaca con cuernos (jefe/forma de Sephiroth transformado) · &t=108
  - 2:00-2:12 Cloud de perfil con la Buster Sword al hombro; Tifa y Aerith en traje de playa, tomadas de la mano (Costa del Sol) · &t=120
  - 2:24 Yuffie con su shuriken al hombro · &t=144
  - 2:48 Cait Sith y soldados Shinra con emblemas rojos · &t=168
  - 3:00 Aerith y un hombre de uniforme (Cid) hablan de perfil · &t=180
  - 3:36 primer plano final del rostro de Aerith, ojos verdes, mirando a cámara · &t=216
  - 3:48 destello de una espada plateada partiendo el aire (Sephiroth) · &t=228
- **Tráiler narrativo del Remake** «Final Fantasy VII : Trailer cinématiques» (JeuxVideo.com, 49 598 vistas) · https://www.dailymotion.com/video/x89cm5z · ⚠️ (una fuente, no mirado fotograma a fotograma por presupuesto; sirve como referencia adicional de tráiler) · 1:58
- **Escena de análisis** «Final Fantasy VII: Cloud Strife's Origins» (WatchMojo, versión en inglés, vídeo de análisis del personaje) · https://www.dailymotion.com/video/x6tkb5f · ⚠️ (una fuente, canal de análisis de tercero, no mirado a fondo por presupuesto) · 5:26
- **Tendencias del fandom** (r/FinalFantasyVII, muestra de 100 posts recientes ordenados por puntuación con la API pública de Arctic Shift, no hay acceso a TikTok desde este servidor) · https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=FinalFantasyVII · ✅ (dato directo de la API, confirmado con la fecha de la consulta 2026-09-26)
  - «Made out of legos» (recreación de una escena en LEGO), 1199 puntos, 40 comentarios · https://reddit.com/r/FinalFantasyVII/comments/1wn8dkf/made_out_of_legos/
  - «Collection of enhanced OG FF7 background» (fondos del juego original mejorados con IA/upscale), 805 puntos, 46 comentarios · https://reddit.com/r/FinalFantasyVII/comments/1wmrhcg/collection_of_enhanced_og_ff7_background/
  - «Tifa cosplay by JaharaJayde», 618 puntos, 12 comentarios · https://reddit.com/r/FinalFantasyVII/comments/1wn8cfp/tifa_cosplay_by_jaharajayde/
  - «Yuffie Cosplay from FF7 Rebirth», 492 puntos, 37 comentarios · https://reddit.com/r/FinalFantasyVII/comments/1wmrhrt/yuffie_cosplay_from_ff7_rebirth_ig_riiyuukii_cos/
  - «Barret got some fast hands! 👊» (clip de gameplay viral), 412 puntos, 34 comentarios · https://reddit.com/r/FinalFantasyVII/comments/1wob0oh/barret_got_some_fast_hands/
  - «Restoration of the 1997 Promo Poster in high resolution!», 375 puntos, 4 comentarios · https://reddit.com/r/FinalFantasyVII/comments/1wmipqm/restoration_of_the_1997_promo_poster_in_high/
  - Patrón claro: el cosplay y el arte/recreaciones de fans (LEGO, posters restaurados, fondos con IA) dominan las publicaciones más votadas, más que los memes o el debate — dato útil para «qué ama el fandom» (punto 12, del investigador de voz/personajes).
  - TikTok: `herramientas/navegar.py` sobre `tiktok.com/tag/finalfantasy7rebirth` devolvió sólo «Iniciar sesión» (200, 14 caracteres) — bloqueado sin sesión, como en encargos anteriores. No se insistió más (regla de 2 intentos).

## 14 · Poses analizadas por personaje

Personajes para empezar (`encargos/126-final-fantasy-vii.md`): Cloud, Tifa, Aerith, Sephiroth.
6-10 fotogramas por personaje, enlace `&t=` al segundo exacto.

### Cloud

| Pose | Episodio (vídeo) | Minuto | Sirve para |
|---|---|---|---|
| Agachado, desenvaina la Buster Sword, luz azulada de neón detrás | https://www.dailymotion.com/video/x89nb1q&t=300 | 5:00 | Presentar / portada |
| Primer plano de perfil, pelo rubio de punta, mirada decidida | https://www.dailymotion.com/video/x89nb1q&t=240 | 4:00 | Presentar |
| Primer plano frontal, ojos mako brillantes (tech demo PS3) | https://www.dailymotion.com/video/x89cm28&t=92 | 1:32 | Presentar (silueta reconocible) |
| Entrega una materia verde a Tifa con la mano abierta | https://www.dailymotion.com/video/x7at6qi&t=50 | 0:50 | Animar / ayudar a un aliado |
| Salta en plena acción con la Buster Sword en alto, cámara baja | https://www.dailymotion.com/video/x7at6qi&t=150 | 2:30 | Celebrar / acción |
| Sostiene el cuerpo de Aerith y la hunde en el lago, cabeza agachada | https://www.dailymotion.com/video/x89cm2f&t=72 | 1:12 | Pensar / dolor (referencia emocional, no para lámina alegre) |
| De pie junto a Barret en la sala de control de Shinra, hablando | https://www.dailymotion.com/video/x89clz1&t=56 | 0:56 | Explicar |

✅ (visto en 4 vídeos oficiales/de medios distintos, mismo diseño de pelo y Buster Sword) · 7 poses.

### Tifa

| Pose | Episodio (vídeo) | Minuto | Sirve para |
|---|---|---|---|
| Recibe la materia de Cloud con la mano extendida, guantes de pelea puestos | https://www.dailymotion.com/video/x7at6qi&t=50 | 0:50 | Animar / recibir |
| Postura de combate, puño lanzado hacia delante (artes marciales) | https://www.dailymotion.com/video/x7at6qi&t=130 | 2:10 | Celebrar / acción |
| Patada giratoria en el aire, chispas alrededor | https://www.dailymotion.com/video/x7at6qi&t=170 | 2:50 | Celebrar (ataque, pose dinámica) |
| Sentada en una plataforma flotante de la Corriente Vital, hablando con Cloud | https://www.dailymotion.com/video/x89cm3e&t=80 | 1:20 | Explicar / pensar |
| Sentada junto a Cloud en otra plataforma, gesto más cercano | https://www.dailymotion.com/video/x89cm3e&t=128 | 2:08 | Explicar |
| De la mano con Aerith caminando por la playa, trajes de Costa del Sol | https://www.dailymotion.com/video/x8sb9z6&t=120 | 2:00 | Presentar (grupo/amistad) |
| De perfil, mirando a otro personaje (Cid), pelo suelto | https://www.dailymotion.com/video/x8sb9z6&t=180 | 3:00 | Explicar |

✅ (visto en 3 vídeos distintos, mismo diseño: coletas altas, guantes de pelea) · 7 poses.

### Aerith

| Pose | Episodio (vídeo) | Minuto | Sirve para |
|---|---|---|---|
| Primer plano de perfil en el sótano de la iglesia, luciérnagas de mako alrededor | https://www.dailymotion.com/video/x89nb1q&t=130 | 2:10 | Presentar |
| Sostiene una flor amarilla recién cogida, luz cálida | https://www.dailymotion.com/video/x89nb1q&t=170 | 2:50 | Presentar (objeto icónico: la flor) |
| Camina hacia el altar circular con el grupo, vestido rosa ondeando | https://www.dailymotion.com/video/x89cm2f&t=8 | 0:08 | Presentar (grupo) |
| Arrodillada, manos juntas, rezando en el altar | https://www.dailymotion.com/video/x89cm2f&t=48 | 0:48 | Pensar |
| Corre entre calles con humo, vestido claro ondeando (gameplay Remake) | https://www.dailymotion.com/video/x7at6qi&t=80 | 1:20 | Celebrar / acción |
| Primer plano final, ojos verdes mirando a cámara | https://www.dailymotion.com/video/x8sb9z6&t=216 | 3:36 | Explicar / cierre emotivo |
| Corre con el vestido rosa suelto entre edificios (tugurios del Sector 7) | https://www.dailymotion.com/video/x89nb1q&t=80 | 1:20 | Celebrar (huyendo/jugando) |

✅ (visto en 3 vídeos oficiales distintos, mismo diseño: trenza, vestido rosa) · 7 poses.

### Sephiroth

| Pose | Episodio (vídeo) | Minuto | Sirve para |
|---|---|---|---|
| Sentado leyendo documentos en la biblioteca de la mansión Shinra | https://www.dailymotion.com/video/x2yc6on&t=40 | 0:40 | Explicar / pensar |
| Silueta caminando entre las llamas de Nibelheim, la Masamune al hombro | https://www.dailymotion.com/video/x2yc6on&t=240 | 4:00 | Presentar (amenaza, silueta reconocible) |
| Primer plano del rostro, pelo plateado, ojo mako verde, expresión fría | https://www.dailymotion.com/video/x2yc6on&t=540 | 9:00 | Explicar (monólogo) |
| Cae en picado con la Masamune en alto, a punto de atravesar a Aerith | https://www.dailymotion.com/video/x89cm2f&t=44 | 0:44 | Regañar / atacar (la pose más icónica de la escena) |
| Silueta encapuchada de pie, de espaldas (tráiler Rebirth) | https://www.dailymotion.com/video/x8sb9z6&t=36 | 0:36 | Presentar |
| Forma transformada, roja y demoníaca, cuernos (jefe final) | https://www.dailymotion.com/video/x8sb9z6&t=108 | 1:48 | Regañar / amenazar |

✅ (visto en 2 vídeos oficiales distintos, mismo diseño: gabardina negra, Masamune, pelo plateado largo) · 6 poses, cumple el mínimo del encargo (6-10).

## Lo mejor para la lámina

- Sephiroth cayendo con la Masamune en alto sobre Aerith (0:44 de https://www.dailymotion.com/video/x89cm2f&t=44): la pose más reconocible de toda la saga, sirve de silueta de amenaza sin ser gráfica.
- Aerith sosteniendo la flor amarilla en el sótano de la iglesia (2:50 del opening del Remake, &t=170): pose serena, con su objeto icónico, luz cálida de mako.
- Paleta de Nibelheim en llamas (#6E3133/#D0633A/#F8CA56) medida en fotograma: ideal si el canal pide un fondo de «crisis, calidez peligrosa», con mucho contraste.
- Tema «One-Winged Angel» (pista 87 del OST) como referencia de música de ambiente para una lámina de tono dramático o de combate (coro latino, el tema más famoso de toda la saga).
- Cuadro de diálogo francés con interjección de Barret «MINCE, MINCE, MINCE!!!» (3:20 de https://www.dailymotion.com/video/x89clz1&t=200): ejemplo real de caja de diálogo del juego con emoción explosiva, no genérica.

## No encontré

- Fotogramas a 1080p o más (lo pide el punto 2): los clips de prensa en Dailymotion sólo sirven
  512×288 (comprobado con `yt-dlp -F`, único formato `hls-380`) y YouTube pide iniciar sesión en
  este servidor. No se probó una cuenta secundaria de YouTube (`YT_COOKIES`) por no estar
  disponible en este contenedor. ⚠️
- Vídeo de análisis largo en profundidad (tipo video-ensayo) de un canal grande de habla hispana
  sobre FFVII: probé «Final Fantasy VII análisis» y «Final Fantasy VII video ensayo» en la API de
  Dailymotion (es), sólo salieron gameplays y reseñas cortas de medios franceses. Se usó como
  sustituto el vídeo de WatchMojo (en inglés) sin mirarlo fotograma a fotograma.
- Tendencias de TikTok: `herramientas/navegar.py` sobre `tiktok.com/tag/finalfantasy7rebirth` (1
  intento) devolvió sólo la página de inicio de sesión (200, 14 caracteres). No se insistió más.
- Efectos de sonido y onomatopeyas medidos en espectrograma (el «¡Kweh!» de los chocobos, el
  sonido de invocar materia): documentado de oído/memoria del juego, no medido con `voz.py`
  porque no son frases habladas.
- Pistas sueltas del OST de Remake y Rebirth escuchadas una a una: sólo se confirmó el álbum en
  MusicBrainz (⚠️ una fuente), no se llegó a escuchar por presupuesto de la tanda.

## Bitácora

- `herramientas/fotogramas.py` sobre 8 clips de Dailymotion (opening Remake, opening tech-demo
  PS3, ending Fin Partie 4, muerte de Aerith, flashback de Nibelheim, caída del Sector 7,
  gameplay de Tifa en Remake, recuerdos de Tifa en la Corriente Vital, tráiler final de
  Rebirth): 8 hojas de contacto miradas con Read, más de 190 fotogramas en total.
- `ffmpeg` para extraer 6 fotogramas sueltos de los vídeos ya bajados (sin volver a descargar) +
  `herramientas/estilo.py --colores 5` sobre esos 6 fotogramas para el punto 4.
- API de Dailymotion (`api.dailymotion.com/videos?search=…`): búsquedas en francés e inglés —
  «Final Fantasy VII bombing mission», «Aerith death», «Sephiroth Nibelheim», «opening movie
  FMV», «Midgar plate falls Sector 7», «Cloud vs Sephiroth final battle», «La chute du secteur
  7», «generique de fin», «cinematique finale», «Fin Partie 1», «Tifa Cloud puits», «Tifa combat
  Corel», «Cloud presente Buster Sword» (12 búsquedas en total).
- `archive.org/metadata/final_fantasy_vii_soundtrack`: tracklist completo de 90 pistas del OST
  original, para el punto 9.
- `musicbrainz.org`: confirmación de 3 álbumes oficiales (original, Remake, Rebirth).
- `arctic-shift.photon-reddit.com`: 100 posts recientes de r/FinalFantasyVII, ordenados por
  puntuación en el propio análisis, para el punto 10 (tendencias).
- `herramientas/navegar.py` sobre `tiktok.com/tag/finalfantasy7rebirth`: bloqueado (login).
- `yt-dlp -F` sobre un clip de Dailymotion para comprobar la resolución máxima real (512×288).
- Ya recolectado por `recolectar.py` y **no repetido**: los clips de Dailymotion de
  `datos-video.md` (opening/ending/trailer/escena genéricos), Internet Archive (soundtracks,
  Advent Children) y MusicBrainz (13 álbumes) — se usaron esos datos como punto de partida y se
  añadió lo que faltaba (clips concretos con escena identificada, minuto exacto y paleta medida).
