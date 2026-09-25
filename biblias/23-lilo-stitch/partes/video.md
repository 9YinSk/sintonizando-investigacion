# Parte de VÍDEO · 23-lilo-stitch (puntos 2, 4, 9, 10, 14)

Repaso sobre una biblia ya escrita (`revisar.py`: 11 de 15 minutos citados). El
motivo: casi todos los minutos de la biblia van en formato `00:22:54` (con la
hora delante), que el contador de `revisar.py` no reconoce como «minuto
citado» (sólo cuenta `M:SS` o `&t=`). YouTube pedía iniciar sesión: todo lo de
abajo se miró de verdad en Dailymotion e Internet Archive con `fotogramas.py`
y se midió con `estilo.py`. Vídeos borrados tras sacar las hojas.

## 2 · Escenas que sirven para #fotos — lo que confirmé mirando vídeo

La biblia ya tenía la tabla de escenas por subtítulo (✅ texto y minuto,
⚠️ lo visual «de memoria»). Esto es lo que añado **mirando vídeo real**:

- **El póster final es literalmente una foto con Stitch colado en la esquina.**
  En los créditos de cierre (2002, emisión de Disney Channel 2004) se ve una
  foto de familia (madre, padre con bigote y gafas de sol, dos chicas, un bebé
  con ukelele) pegada con cinta en un fondo azul, y Stitch sentado FUERA del
  marco blanco, en la esquina inferior derecha, como si se hubiera colado ·
  fuente: [Internet Archive, «Lilo & Stitch (2002) End Credits (Disney Channel
  2004)»](https://archive.org/details/lilo-stitch-3), minuto 1:20 (visto con
  `fotogramas.py`) · ✅ (visto directamente) · 854×480.
- **Los créditos son en sí un álbum**: fotos con borde blanco fotográfico,
  pegadas en ángulo con cinta adhesiva sobre un fondo azul liso, algunas
  tapando parcialmente a otras — coincide con lo que la biblia proponía de
  memoria para el «borde de foto» (`#F7F3E8`) y el estilo de collage ✅ (visto
  en los minutos 0:00, 0:10, 0:20 y 1:20 del mismo vídeo).
- **La cápsula de Stitch lleva una foto de Lilo pegada por dentro**: en el
  tráiler original de 2002 se ve, en primer plano, la cápsula azul con
  correas en la que llega Stitch a la Tierra, y dentro tiene **una fotito
  dibujada de una niña con vestido rosa (Lilo) pegada** junto a un garabato
  tipo tela de araña · fuente: [Internet Archive, «Lilo Stitch Trailer»
  (2002)](https://archive.org/details/LiloStitchTrailer), minuto 1:48 ✅
  (visto) · 640×346. Es otro objeto-foto para la lámina, más pequeño que el
  álbum.
- **«TIMER DINGS» (01:17:56) sigue sin resolver**: no encontré el tramo del
  montaje final con el temporizador de cámara; el clip de créditos que sí miré
  probablemente empieza ya avanzado el *collage* (las canciones ya están en
  créditos a los 0:50), así que no puedo decir si son las mismas fotos del
  minuto 01:17:18-01:20:13 de la película o arte de créditos aparte ⚠️. Lo
  dejo con el aviso de la biblia.
- **La cámara de Lilo, sin resolver**: no localicé el fotograma 00:22:54 en
  ningún vídeo disponible por Dailymotion/Internet Archive (ni el DVD-rip de
  8 min de «Part 1 HD» llega tan lejos, sólo cubre 0:00-7:59). Sigue ⚠️ carrete
  Kodak vs. polaroid, como ya avisaba la biblia.

## 4 · Sitios, luz y paleta — medido con `estilo.py` sobre fotogramas reales

### El restaurante del luau (donde Nani trabaja de camarera)

Escena real de la película (no es un descarte: es donde Nani pierde el
trabajo), 1080p · fuente: [Internet Archive, «Lilo Stitch Luau Nani Loses Her
Job HD 1080p»](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p)
(1824×1080, mirado con `fotogramas.py`, 17 fotogramas cada 12 s) ✅:

- Noche, interior de cabaña de madera con antorchas encendidas; un bailarín
  hace el número de fuego (0:12-0:24) mientras Nani sirve mesas con bandeja,
  vestido verde jade de tirantes con flor en el pelo (0:48-1:00) — pose de
  **servir/presentar**.
- Lilo y Stitch sentados a una mesa, comiendo y leyendo un libro juntos
  (0:36, 1:12, 1:24, 2:00) — pose de **pensar/juntos**, útil para «Sin
  editar».
- Paleta medida (fotograma 0:48, `estilo.py --colores 8`): `#234543` 17%
  `#150311` 15% `#8D4232` 15% `#662F30` 15% `#351930` 14% — dominan **terracota
  quemado y madera oscura** sobre azul-negro de noche, no el azul liso que
  proponía la biblia de memoria (`#1F2E52`); corrijo: la noche del luau es
  **cálida** (antorchas), no fría.
- Paleta a 1:00 (surtido más amplio): `#813B2D` 27% `#02042A` 26%
  `#5F3421` 10% `#0E0103` 9% — confirma el patrón: madera/fuego cálido +
  fondo casi negro-azulado.
- Estilo (`estilo.py`): sombreado degradado/pintado, poca línea, saturación
  66-74%, brillo 29-32%. Coincide con la acuarela de la película (§5.2 de la
  biblia).

### El dormitorio de Lilo, de noche (susto de Nani al ver a Stitch)

- Fuente: [tráiler original 2002, Internet Archive](https://archive.org/details/LiloStitchTrailer),
  minuto 2:12 ✅ (visto, 640×346). Cama con edredón rojo y blanco de flores,
  cómoda de madera oscura, **lámpara con pantalla verde y base de piña**
  (detalle nuevo, no estaba en la biblia), collares colgados de un clavo.
- Paleta medida: `#0C1F2A` 25% `#432626` 25% `#62414D` 16% `#954D2D` 13%
  `#6A1B1B` 12% — violeta-rojo oscuro de noche con un cálido naranja de
  cómoda; **corrige** el azul puro `#1F2E52` que proponía la biblia: la
  noche en interiores es más morada/roja que azul.
- Escena: Nani entra, boca abierta, ojos muy abiertos (susto), Stitch se
  yergue junto a la cama de Lilo dormida — pose de **regañar/sorprender**
  para Nani, nueva (no estaba descrita en la biblia).

### El mar del surf (versión 2025)

- Fuente: [tráiler oficial 2025 en español, Dailymotion, Sensacine
  ](https://www.dailymotion.com/video/x9fzrlk), minuto 1:44 ✅ (visto,
  512×288 nativo, la hoja de contacto a 1280 px). Paleta medida: `#2F6867`
  38% `#497B7E` 16% `#255757` 10% — **turquesa apagado**, no el `#2E8FA8`
  más saturado que proponía la biblia; el remake usa un grado de color más
  gris/natural (imagen real, CGI) que el 2002 en acuarela.
- La toma es un plano general con dron: Stitch va sobre la tabla con dos
  personas más, estela blanca — pose de **celebrar/acción**.

### Texturas confirmadas mirando vídeo

- Madera de cabaña con vetas oscuras y quemada (luau) — coincide con la
  «madera pintada y saltada» que ya proponía la biblia §5.5.
- Edredón floral rojo-blanco con textura de tela gruesa (dormitorio).
- Antorchas de fuego real, útil para un efecto de luz cálida detrás del
  personaje en la lámina (evita que quede plano, como pide el encargo).

## 9 · Música — confirmado leyendo los créditos reales del vídeo (no un resumen)

Fuente única y directa: [Internet Archive, «Lilo & Stitch (2002) End Credits
(Disney Channel 2004)»](https://archive.org/details/lilo-stitch-3), minutos
0:50 y 4:20-4:40 (fotograma en grande con `fotogramas.py --fotograma`) ✅ **visto
el cartel de créditos**, no un resumen de wiki:

| Canción | Escrita por | Interpretada por | Minuto del vídeo de créditos |
|---|---|---|---|
| «He Mele No Lilo» y «Hawaiian Roller Coaster Ride» | Alan Silvestri y Mark Keali'i Ho'omalu | — (coro, ver abajo) | 0:50 |
| «Can't Help Falling in Love» | Luigi Creatore, Hugo Peretti y George David Weiss | **The A*Teens**, producida por Mark Hammond | 4:20 |
| «Burning Love» | Dennis Linde | **Wynonna** (cortesía de Curb/Universal) | 4:30 |
| «Suspicious Minds» | Mark James | (créditos cortados en el fotograma, no leído) | 4:20 |
| «Stuck On You» | (créditos cortados) | Elvis Presley (cortesía RCA/BMG) | 4:20 |
| «Hound Dog» | Jerry Leiber y Mike Stoller | Elvis Presley (cortesía RCA/BMG) | 4:30 |
| «Heartbreak Hotel» | Elvis Presley, Mae Axton y Tommy Durden | Elvis Presley (cortesía RCA/BMG) | 4:30 |
| «You're The Devil In Disguise» | Bernie Baum, Bill Giant y Florence Kaye | Elvis Presley (cortesía RCA/BMG) | 4:30 |
| «Blue Hawaii» | Ralph Rainger y Leo Robin | Elvis Presley (cortesía RCA/BMG) | 4:30 |

- **Coro**: Kamehameha Schools Children's Chorus, dirigido por **Lynell K.
  Bright** ✅ (visto en créditos, 4:30-4:40). Corrige/confirma la biblia, que
  sólo decía «coro infantil de las Kamehameha Schools» sin director.
- **Partitura**: arreglos de coro de Alan Silvestri y Mark Keali'i Ho'omalu;
  coordinador de grabación David Bifano; orquestaciones de **Mark McKenzie**
  y **William Ross**; editor de música **Ken Karman** ✅ (visto, 4:20).
- **A*Teens** son suecos (créditos «cortesía de Stockholm Records»): la
  versión de «Can't Help Falling In Love» de los créditos es la del grupo
  pop sueco, no una versión latina — sigue sin encontrarse el intérprete de
  «Muero de amor por ti» (versión en español) ⚠️, como ya avisaba la biblia.
- **2025 (remake)**: la música sigue siendo Elvis Presley + tradición
  hawaiana, confirmado por un featurette oficial de Disney Francia con
  entrevistas al compositor y a una cantante hawaiana que graba «Hawaiian
  Roller Coaster Ride» de nuevo («no puede haber Lilo y Stitch sin Elvis
  Presley», dice un entrevistado) ✅ (visto) · fuente:
  [Dailymotion, NoPopCorn, «La musique de Lilo & Stitch»](https://www.dailymotion.com/video/x9jtp6m),
  minutos 0:00-3:01, en francés.
- **Ambiente para #fotos**: los créditos (el «álbum» en sí) suenan con «Can't
  Help Falling In Love»; el montaje familiar suena con «Burning Love». Los
  dos son el tono exacto del canal: cálido, casero, de cierre feliz.

## 10 · Vídeos — vistos de verdad (no reseñas), todos sin YouTube

| Vídeo | Fuente | Qué se ve | Minuto útil |
|---|---|---|---|
| Tráiler original 2002 | [Internet Archive](https://archive.org/details/LiloStitchTrailer) (640×346) | Cameo de clásicos Disney (Bambi, El Rey León) antes de revelar «STITCH»; cápsula con foto de Lilo dentro; Nani y una amiga en una ventana; criatura alienígena narradora; «INDESCRIBABLE»; sombra de monstruo asustando a Lilo; cena Lilo-Stitch; título «Walt Disney LILO & STITCH»; Lilo y Stitch bailan con un tocadiscos; Nani descubre a Stitch en la cama de Lilo | 0:36 (Stitch enjaulado), 1:06 (playa de noche), 1:36-1:42 (cena), 1:48 (cápsula con foto), 2:00 (título), 2:06 (tocadiscos), 2:12 (susto de Nani) |
| Tráiler oficial 2025, doblado latino | [Dailymotion, Sensacine](https://www.dailymotion.com/video/x9fzrlk) (512×288) | Castillo Disney, Stitch CGI mojado en casa, coche, playa, surf con dron, portal con Jumba/agente, niña llorando junto a Stitch | 0:40 (Stitch en cocina), 1:04-1:20 (playa, coche, Stitch corriendo), 1:44-1:52 (surf) |
| Créditos finales 2002 (emisión TV 2004) | [Internet Archive](https://archive.org/details/lilo-stitch-3) (854×480) | El «álbum» de fotos con Stitch colado, ficha técnica completa, créditos de canciones | 0:00-1:20 (fotos), 0:50 y 4:20-4:40 (canciones) |
| Escena del luau, «Nani Loses Her Job» | [Internet Archive, 1080p](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p) | Bailarín de fuego, Nani sirviendo, Lilo y Stitch cenando juntos | 0:12-1:00 |
| Featurette de la música (2025), en francés | [Dailymotion, NoPopCorn](https://www.dailymotion.com/video/x9jtp6m) | Entrevistas al compositor, a una cantante hawaiana grabando, estudio de grabación | 0:00-3:01 |

- **No encontré en Dailymotion/Internet Archive** (con las búsquedas de
  `datos-video.md` y las que hice yo): la escena de Lilo enseñando a Stitch a
  bailar como Elvis (00:42-00:44), la pared de fotos de turistas (00:22:57), ni
  tendencias de TikTok propias (no tengo acceso a TikTok desde aquí; la
  biblia ya cita 3 enlaces de TikTok sin verlos, los dejo tal cual con ⚠️).
- El «Part 1 HD» de Internet Archive (480×360, muy degradado, con barras de
  seguimiento de VHS) sólo llega a 7:59 y no coincide con ninguna escena
  descrita por subtítulo con precisión suficiente para citarlo; lo descarto
  como fuente (calidad insuficiente para confirmar nada).

## 14 · Poses analizadas — nuevas, confirmadas mirando vídeo (con minuto y enlace)

Éstas se suman a las que ya tenía la biblia (que eran de memoria, marcadas
⚠️). Todas vistas directamente:

### Nani

| Fuente | Minuto | Pose |
|---|---|---|
| [Luau HD, Internet Archive](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p) | 0:48-1:00 | De pie, bandeja en una mano, sirviendo mesas; vestido verde de tirantes, flor en el pelo — **presentar/servir** |
| [Tráiler 2002, Internet Archive](https://archive.org/details/LiloStitchTrailer) | 2:12 | Entra corriendo, boca abierta, ojos muy abiertos, un brazo extendido hacia Stitch — **regañar/sorprender** (el susto clásico) |

### Stitch

| Fuente | Minuto | Pose |
|---|---|---|
| [Tráiler 2002](https://archive.org/details/LiloStitchTrailer) | 0:36 | Encogido tras una reja/malla verde azulada, mirando hacia la cámara, cuerpo bajo — **encerrado/vulnerable**, sirve para «Sin editar» |
| [Tráiler 2002](https://archive.org/details/LiloStitchTrailer) | 1:36-1:42 | Sentado a la mesa con Lilo, comiendo con cubiertos — **pensar/en familia** |
| [Tráiler 2002](https://archive.org/details/LiloStitchTrailer) | 2:06 | De pie junto a un tocadiscos verde con Lilo, ambos animados — **celebrar/bailar** |
| [Créditos 2002](https://archive.org/details/lilo-stitch-3) | 1:20 | Sentado, solo, en la esquina de una foto familiar ajena a él — **colarse/gracioso**, gag de «Inter-Stitch-al» dentro de la propia película |
| [Tráiler 2025 latino, Dailymotion](https://www.dailymotion.com/video/x9fzrlk) | 1:44 | Sobre la tabla de surf, cuerpo bajo, orejas hacia atrás por el viento — **celebrar/acción** |

### Lilo

| Fuente | Minuto | Pose |
|---|---|---|
| [Tráiler 2002](https://archive.org/details/LiloStitchTrailer) | 1:24 | Silueta contra luz azul, brazo alzado, boca abierta (grito de susto) — **miedo**, útil para expresiones |
| [Luau HD](https://archive.org/details/lilo-stitch-luau-nani-loses-her-job-hd-1080p) | 0:36-1:12 | Sentada a la mesa, libro abierto compartido con Stitch — **pensar/explicar** |

### Otros (no en mi lista de personajes pero salen en el material)

- Bailarín de fuego del luau (0:12-0:24 del clip del luau): torso descubierto,
  antorcha girando — referencia de acción/pose dinámica para fondos con
  personajes secundarios de ambiente.

## Lo mejor para la lámina

1. **La cápsula de Stitch con la foto de Lilo pegada dentro** (tráiler 2002,
   1:48): un objeto real y pequeño, perfecto para dibujar en Blender como
   «marco de foto» del canal, con la propia lógica del álbum de la serie.
2. **El collage de créditos** (0:00-1:20 de `lilo-stitch-3`): fotos con borde
   blanco, pegadas con cinta en ángulos distintos sobre azul — es literalmente
   el fondo que pide el encargo para #fotos, y ya viene con Stitch colado en
   una esquina.
3. **Nani sirviendo en el luau, de noche, con antorchas** (0:48 del clip del
   luau): luz cálida real detrás del personaje — resuelve el «que no quede
   plano» del encargo sin inventar nada.
4. **El susto de Nani en el dormitorio** (2:12 del tráiler 2002): pose de
   cuerpo entero con expresión fuerte, y de paso confirma la lámpara con
   base de piña como objeto de attrezzo.
5. **La mesa del luau, Lilo y Stitch leyendo juntos**: pose tranquila,
   contraste con el ajetreo de Nani sirviendo alrededor — sirve para textos
   largos del canal («cómo se usa»).

## No encontré ⚠️ (extra, no obligatorio)

- Tendencias reales de TikTok sobre la escena de la cámara o el «blue punch
  buggy»: no hay acceso a TikTok desde este servidor; dejo los 3 enlaces que
  ya traía `datos-video.md`/la biblia sin verificar.
- Storyboards oficiales (plan C del encargo): no fue necesario, Dailymotion e
  Internet Archive dieron material suficiente y de mejor calidad que un
  storyboard.
- AnimeThemes: no aplica (Lilo & Stitch no es anime, la fuente no tiene la
  obra).
- El vídeo completo de la película (2002) en buena calidad: no está en
  Internet Archive con licencia clara; lo que hay o es TV-rip degradado
  («Part 1 HD», descartado) o el VHS fanmade de 1,9 GB de 132 minutos (no
  descargado por tamaño/tiempo — si hace falta más adelante, el identificador
  es `lilo-stitch-2002-fanmade-vhs`).
- «Aloha From Hollywood» (especial de ABC 2002 con Wynonna, 42 min, 1,3 GB en
  Internet Archive, id `disneys-lilo-stitch-aloha-from-hollywood-2002`): no
  descargado por tamaño; podría tener más metraje real de Hawái y la
  actuación de «Burning Love» en directo.

## Sigue

(vacío — puntos 2, 4, 9, 10 y 14 completos con vídeo mirado de verdad;
sólo quedan los ⚠️ de «No encontré», que son extra, no obligatorio)

## Bitácora de búsqueda (vídeo)

- Internet Archive, `advancedsearch.php` (`title:(Lilo Stitch)`,
  `mediatype:movies`): localicé `LiloStitchTrailer`, `lilo-stitch-3`,
  `lilo-stitch-luau-nani-loses-her-job-hd-1080p`, `LiloAndStitchPart1HD`,
  `disneys-lilo-stitch-aloha-from-hollywood-2002`.
- `archive.org/metadata/<id>` por cada uno, para ver duración y formato de
  archivo antes de bajar (evita bajar cosas gigantes sin mirar).
- `fotogramas.py` sobre 6 vídeos: tráiler 2025 doblado (Dailymotion),
  créditos 2002 (Internet Archive), luau 1080p (Internet Archive), tráiler
  original 2002 (Internet Archive), «Part 1 HD» (descartado por calidad),
  featurette musical 2025 en francés (Dailymotion).
- `estilo.py --colores` sobre 6 fotogramas sueltos (luau ×2, dormitorio ×1,
  cápsula/mar 2025 ×2) para los hex medidos de §4.
- Búsquedas de texto en `archive.org/advancedsearch.php` para «Elvis lesson»,
  «camera wall photos», «Lilo Stitch storyboard»: sin resultados útiles.
- No usé el cupo de buscador web (WebSearch): todo salió de `datos-video.md`
  y de la API de Internet Archive/Dailymotion directamente, tal y como pide
  «Ahorra sin recortar».
