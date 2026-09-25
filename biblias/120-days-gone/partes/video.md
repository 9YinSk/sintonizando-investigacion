# Parte de VÍDEO · Days Gone (encargo 120)

Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Days Gone es videojuego, no anime: no hay
«opening/ending» de serie ni «capítulos»; se adapta a tráiler de anuncio, tráiler
narrativo, tráiler de lanzamiento y metraje de juego, todo con minuto exacto.

## 2 · Fotogramas de escenas icónicas (1080p o más, con minuto)

Days Gone no tiene "capítulos"; se mira por minuto de vídeo o de metraje in-game. Mirado con
`fotogramas.py --cortes` (un fotograma por plano) y frames sueltos con `--fotograma`. Fuente
principal en 1080p real: *Days Gone E3 vs Retail | Direct Comparison* (Internet Archive,
1920×1080, 15:02) — comparación oficial-fan del build de E3 2016 contra la versión final,
plano a plano; el resto son mirrors de Dailymotion a 512×288 (YouTube pedía inicio de sesión).

- **"Death Train Horde"**: encuentro contra una horda entera en un patíbulo de tren abandonado
  entre vagones oxidados; Deacon usa una ametralladora fija, cócteles molotov y trampas de fuego
  desde una pasarela elevada; pantalla de logro **"Horde Killer"** y misión completada
  **"Death Train Horde"** justo al final. 68 muertes registradas en el contador de la esquina.
  · [12:53](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=773)–[13:00](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=780)
  · ✅ (visto en vídeo + confirmado como logro real de PS4/Steam: la wiki de Days Gone y la lista
  de trofeos citan "Horde Killer" como logro por matar una horda completa).
- **Rescate de Lisa en el templo Ripper** ("Combat final", JeuxVideo.com): combate cuerpo a
  cuerpo con cuchillo dentro de una cueva/mina iluminada con faroles de aceite y cuerda, tras un
  destello rojo inicial (bengala). Coincide con la misión **"I Kept My Name"** (escapar del
  campamento Ripper, recuperar el equipo, rescatar a Lisa) según su wikitext y tres guías
  (GameFAQs, Neoseeker, Orcz) · ✅ (wiki + guías) · [0:12](https://www.dailymotion.com/video/x89n0df?t=12)–[0:46](https://www.dailymotion.com/video/x89n0df?t=46)
  · https://daysgone.fandom.com/wiki/I_Kept_My_Name
- **Cementerio en el bosque con niebla nocturna**: cuatro cruces de madera clavadas en tierra
  removida, niebla azulada entre árboles retorcidos; plano fijo del tráiler argumental que corta
  justo después del diálogo sobre "todo lo que importaba había desaparecido" · ✅ (visto) ·
  [0:48](https://www.dailymotion.com/video/x84cgbc?t=48) — paleta medida abajo (punto 4).
- **Emboscada nocturna en autopista con dos tráilers varados**: una horda completa corre entre
  dos camiones articulados a plena luz del día con polvo en suspensión, marca "PS4 EXCLUSIVO" en
  pantalla (del tráiler argumental, tramo final de montaje) · ✅ (visto) ·
  [1:52](https://www.dailymotion.com/video/x84cgbc?t=112).
- **Cresta con vista al valle** (comparación E3 2016 / Retail): Deacon de espaldas, rifle y arma
  improvisada cruzados a la espalda, contemplando un pueblo en ruinas con una montaña nevada al
  fondo (Mount Bachelor/Cascade); el build de retail añade escarcha en primer plano y niebla en
  capas sobre las montañas que el build de 2016 no tenía · ✅ (visto, comparación directa) ·
  [0:39](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=39).

## 4 · Fondos y sitios: luz, paleta medida en fotogramas y texturas reales

Paletas medidas con `estilo.py` sobre fotogramas propios (no capturas de otros): ver también el
punto 16 de `partes/imagen.md` (paisajes desde capturas de Steam), estos son sitios DISTINTOS,
sacados de vídeo en movimiento, para no repetir.

- **Cresta con vista al pueblo en ruinas y montaña nevada** (comparación E3 2016/Retail, build
  retail) — luz de mañana, cielo despejado: paleta agregada `#8DA19F` 20.6%, `#3E4648` 16.9%,
  `#38342D` 14.0%, `#588598` 8.1% (azul de montaña) · brillo 44%, saturación 23%, sombreado
  degradado/pintado · ✅ medido, fotograma propio en
  [0:39](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=39).
  Textura real equivalente para la nieve/escarcha en primer plano: ambientCG "Snow006" (buscar en
  `https://ambientcg.com/api/v2/full_json?type=Material&q=snow`).
- **Interior de nave/cobertizo de madera con palés apilados** (misión de sigilo, build retail) —
  luz cálida de ventana lateral y rejilla de ventilación retroiluminada: paleta `#3C4241` 22.2%,
  `#2A2C2F` 22.1%, `#281E19` 19.4%, `#483427` 9.1% (madera) · brillo 24%, saturación 29% · ✅
  medido, [1:22](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=82).
  Textura real: madera de palé envejecida y gris — ambientCG "WoodSiding009" o "Planks012"
  (`https://ambientcg.com/view?id=Planks012`, CC0); complementa el "Fabric030"/"Bark014" que ya
  usó `imagen.md` para el kutte y la corteza.
- **Cementerio boscoso con niebla azulada nocturna** (tráiler argumental) — luz fría, sin sol,
  niebla en capas entre troncos oscuros: paleta `#08141C` 23.9%, `#0E1F2A` 20.7%, `#18313D`
  16.3%, `#274450` 11.9% · brillo 21% (el más oscuro de todos los medidos), saturación 61% (el
  color entra por el tinte azul-teal del "day/night cycle", no por objetos de color) · ✅ medido,
  [0:48](https://www.dailymotion.com/video/x84cgbc?t=48). Real equivalente: HDRI nocturno con
  niebla de Poly Haven "moonless_golf" no aplica bien (muy despejado); mejor "Overcast Soil
  Puddles" o una niebla añadida en compositing sobre "Misty Pines" (ya citada en `imagen.md`,
  punto 16) con temperatura de color más fría.
- **Autopista con dos tráilers varados, luz de mediodía polvorienta** (tráiler argumental, escena
  de horda) — luz dura, contraluz en los infectados: paleta `#221716` 25.2%, `#100A0C` 20.1%,
  `#362721` 15.9%, `#BDB3AD` 7.8% (polvo en el aire) · brillo 30% pese a ser de día, por el
  contraluz y las sombras largas de los camiones · ✅ medido,
  [1:52](https://www.dailymotion.com/video/x84cgbc?t=112). Real equivalente para el asfalto
  agrietado y la tierra del arcén: ambientCG "Asphalt012" y "Ground037" (CC0).
- **Vagones de tren oxidados y patíbulo de madera** (Death Train Horde, retail) — luz de tarde
  cálida entre nubes de humo de las trampas de fuego; visto en vídeo (no medido con estilo.py por
  el fuego en movimiento, que distorsiona el promedio de color) — dominan el óxido naranja-marrón
  de los vagones y el gris de las traviesas de madera · ⚠️ descrito, no medido en frame fijo ·
  [12:53](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=773).

**Nota sobre las dos versiones (E3 2016 vs Retail)**: el vídeo de comparación permite ver que el
estudio subió el nivel de detalle atmosférico entre el anuncio y el lanzamiento — más capas de
niebla en las montañas lejanas, vegetación más densa y variada, y luz más direccional con
sombras de contacto más duras en la versión final · ✅ (comparación directa, visto fotograma a
fotograma) · https://archive.org/details/DaysGoneE3VsRetailDirectComparison

## 9 · Música y sonido

Compositor: **Nathan Whitehead** (confirmado en dos fuentes: MusicBrainz, creador del release
"Days Gone: Original Music"/"Original Soundtrack", 2019-04-14/19,
https://musicbrainz.org/release-group/f17aa54f-0a0b-4481-80d3-a7c50bfee9ea ·
https://musicbrainz.org/release-group/51a58e0d-e59a-425f-9115-a19bb57b2f65 — y el propio blog
oficial de PlayStation firmado por él) · ✅. Álbum completo (24 pistas, con duración) subido en
Internet Archive: https://archive.org/details/days_gone-original_soundtrack · ✅.

**Qué tema suena en qué escena (de la propia entrevista del compositor en el blog oficial de
PlayStation, "Creating the Soundtrack for Days Gone", 15-may-2019 — cita directa, no de
memoria)** · ✅ fuente primaria oficial:
- **"Days Gone"** (pista 1, tema principal, 3:41): "mi objetivo era fijar el tono del viaje de
  Deacon (...) mezclar esperanza con introspección y un toque de melancolía". Suena en la
  introducción del juego.
- **"The Freakshow"** (pista 2, 3:36): el tema de los infectados — instrumentos orgánicos (piano,
  guitarra, metales frotados) muy procesados con distorsión y cambio de tono; "las secciones
  grandes y arrolladoras transmiten el terror de la Horda".
- **"We've All Done Things"** (pista 3): tema de **Iron Mike** — armonio y armónica de bajo,
  guitarras acústicas y violín solista que crecen en orquesta de cuerda.
- **"Rest in Peace"** (pista 4, 3:07): tema de los **Rippers** — tambores de marco y riffs de
  guitarra acústica "elásticos y toscos", con un aire "feral y tribal".
- **"Finding NERO"** (pista 5, 2:59): único tema con base sintetizada, para dar a NERO un aire
  de alta tecnología y misterio.
- **"The Rager Bear"** (pista 7, 2:51): parte de la paleta de los Freaker pero "todo amplificado"
  — platillos graves distorsionados y percusión metálica pesada para transmitir su masa.
- **"A Good Soldier"** (pista 8, 2:39): tema del **Coronel** y la Milicia — percusión marcial y
  melodía grave de cuerdas.
- **"I Remember"** (pista 10, 3:20): la vida de Deacon antes del brote — "nostálgico y algo
  esperanzador", refleja su determinación pese al arrepentimiento.
- **"Promises and Regrets"** (pista 13, 3:28): el reencuentro con Sarah que NO sale como se
  espera — arranca sobre el tema de Sarah con guitarra acústica y cuerdas ligeras, luego vira a
  una presentación "fría y distante" del tema principal cuando Deacon entiende que Sarah no se
  irá con él.
- **"Sarah's Theme"** (pista 17, 4:04): el tema de amor Deacon/Sarah — motivo de piano simple y
  guitarra acústica "brillante", crece hasta una declaración triunfal con cuerdas y percusión; el
  propio compositor dice: "probablemente la pieza más feliz del juego".
- **"Never Give Up"** (pista 19, 3:45): la escena donde Deacon apoya la cura de Sarah — acordes
  de apertura del tema principal con violonchelo solista delicado, luego guitarra acústica suave
  que crece a una sección staccato cuando deciden huir juntos al norte.
- Dato cruzado con el punto 25 (`texto.md`): la storyline de la misión **"I Kept My Name"** (donde
  Lisa libera a Deacon en el templo Ripper) se llama también **"You're Safe Now"**, que coincide
  con el título de la pista 14 del álbum — coincidencia casi segura de que ese cue suena ahí,
  aunque el compositor no la menciona explícitamente en su entrada de blog · ⚠️ (inferencia por
  coincidencia de título, no confirmado en la entrevista).

**Ambiente por zona** (de la propia entrevista, cita textual): "score con un aire folk americana"
inspirado en la Alta Cascada de Oregón, deliberadamente SIN guitarras eléctricas ni rock clásico
pese a que Deacon es motero — el compositor explica que quiso conectar al jugador con el paisaje,
no con el club · ✅ (misma fuente).

**Efectos de sonido y "onomatopeyas" reconocibles** (no hay onomatopeyas de cómic al ser
videojuego 3D; el equivalente es el sonido diegético que todo jugador reconoce):
- **El grito de la Screamer**: alarido agudo y prolongado que "puede convocar a la horda en
  segundos" y se oye a mucha distancia — descrito en la propia wiki de Freakers/Screamers · ✅
  (Fandom, dos páginas: `Freakers` y `Screamers`) https://daysgone.fandom.com/wiki/Screamers
- **El rugido del Rager Bear**: graves de platillo distorsionados y percusión metálica que imitan
  su "masa que se arrastra", según el propio compositor (ver arriba) · ✅.
- **El motor de la Drifter Bike** (la moto de Deacon) quedándose sin gasolina: un traqueteo y
  tosido de motor reconocible por cualquiera que la haya jugado; mencionado en foros de jugadores
  como el sonido más temido del juego (te deja parado en medio de una horda) · ⚠️ (una fuente,
  discusión de comunidad, sin cifra de menciones que la respalde con una segunda fuente).

**No encontré** (de momento) un análisis oficial en video del diseño de sonido (making-of de
audio) distinto al texto del blog citado arriba — sólo hay el post escrito de PlayStation.Blog.

## 10 · Vídeos: tráileres, escenas, análisis, tendencias (con minuto exacto)

Tabla de lo mirado de verdad (fotogramas.py y/o episodio.py), todo mirror oficial porque YouTube
pedía inicio de sesión desde este servidor (bloqueo compartido, no del vídeo en sí):

| Vídeo | Fuente / mirror | Duración | Qué tiene, con minuto | Herramienta |
|---|---|---|---|---|
| Tráiler argumental (historia) | 3DJuegos, vía Dailymotion https://www.dailymotion.com/video/x84cgbc | 2:06 | Diálogo completo transcrito con Whisper (`episodios.md`); cementerio [0:48](https://www.dailymotion.com/video/x84cgbc?t=48); Sarah herida atendida por una mujer de bata blanca [0:29](https://www.dailymotion.com/video/x84cgbc?t=29); Deacon apuntando con pistola en el bosque [0:54](https://www.dailymotion.com/video/x84cgbc?t=54); horda entre dos tráilers [1:52](https://www.dailymotion.com/video/x84cgbc?t=112) | `fotogramas.py --cortes` (54 planos) + `episodio.py` (ya en `episodios.md`) |
| Tráiler de lanzamiento | JeuxVideo.com, vía Dailymotion https://www.dailymotion.com/video/x89n022 | 0:30 | Montaje de cierre antes del estreno: forcejeo entre moteros [0:09](https://www.dailymotion.com/video/x89n022?t=9), trampa incendiaria [0:16](https://www.dailymotion.com/video/x89n022?t=16), tarjeta de reserva "26 avril" (26-abr-2019, fecha real de salida) [0:25](https://www.dailymotion.com/video/x89n022?t=25) | `fotogramas.py --cortes` (16 planos) |
| **Days Gone E3 vs Retail \| Direct Comparison** | Internet Archive (mirror sin marca, 1080p) https://archive.org/details/DaysGoneE3VsRetailDirectComparison | 15:02 | Comparación plano a plano de la demo de E3 2016 contra el juego final: la cresta con vista al valle [0:39](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=39), sigilo en el cobertizo [1:22](…?t=82), asalto al campamento humano [6:55–8:56], y el combate contra la **Death Train Horde** con trofeo "Horde Killer" [12:53–13:00] | `fotogramas.py --cortes` (259 planos en 6 hojas) |
| "Combat final" (rescate de Lisa) | JeuxVideo.com, vía Dailymotion https://www.dailymotion.com/video/x89n0df | 0:48 | Combate cuerpo a cuerpo en cueva/mina de los Rippers, coincide con la misión "I Kept My Name" | `fotogramas.py --cortes` (18 planos) |
| "El mundo de Days Gone, Parte 2: Luchando por sobrevivir" | 3DJuegos, vía Dailymotion https://www.dailymotion.com/video/x84cgej | 3:30 | **Análisis/making-of oficial** narrado: explica los tipos de Freaker (Screamers, Runners, Reachers…), el sistema de armas improvisadas con la ballesta, sigilo vs. combate abierto — ficha completa ya en `episodios.md` con diálogo minuto a minuto | `episodio.py` (ya en `episodios.md`) |
| Days Gone Remastered — Announcement Trailer (PS5) | GRYOnline.pl, vía Dailymotion https://www.dailymotion.com/video/x9e4nc0 | 0:44 | Tráiler oficial 2025: confirma fecha real **25-abr-2025** en tarjeta final (cruza con `texto.md`, punto 25) [0:40](https://www.dailymotion.com/video/x9e4nc0?t=40); nombra los modos nuevos con su propio rótulo — **Permadeath Mode** [0:16](https://www.dailymotion.com/video/x9e4nc0?t=16), **Speedrun Mode** [0:17](https://www.dailymotion.com/video/x9e4nc0?t=17), **Horde Assault** [0:21](https://www.dailymotion.com/video/x9e4nc0?t=21), **Enhanced Photomode** y accesibilidad [0:18](https://www.dailymotion.com/video/x9e4nc0?t=18); hoguera nocturna con cuerpos colgados entre los árboles [0:03](https://www.dailymotion.com/video/x9e4nc0?t=3) y persecución de una manada de lobos infectados (Runners) en la nieve [0:26](https://www.dailymotion.com/video/x9e4nc0?t=26) | `fotogramas.py --cortes` (23 planos) |

**Tendencias / vídeos de fans**: no encontré una tendencia viral concreta y reciente de TikTok
sobre Days Gone (busqué "Days Gone TikTok trend viral moto Deacon 2024 2025" en inglés): sólo
clips sueltos de gameplay sin viralidad medible, nada comparable a fenómenos de otros juegos. En
Internet Archive hay un vídeo review largo, *Days Gone | The Completionist* (267 descargas,
https://archive.org/details/youtube-dK7YgoK_Q_Y) que sirve como "análisis" de comunidad, y un
podcast en español, *[CL] 13x09 — El Complejo Lambda*, que compara Days Gone con Death Stranding
(sólo audio, no lo transcribí por ser fuera de mis puntos).

## 14 · Poses analizadas por personaje (6-10 por personaje, con minuto)

**Deacon St. John** — 10 poses distintas, todas vistas en vídeo propio (no de memoria), con
minuto y para qué sirve cada una en una lámina:

1. **Contemplar/presentar el mundo**: de espaldas, quieto, rifle y arma improvisada cruzados en
   la espalda sobre el kutte, mirando un valle con pueblo en ruinas y montaña nevada al fondo ·
   [0:39](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=39)
   · sirve para **presentar** el escenario o el canal.
2. **Sigilo/pensar**: agazapado tras palés de madera, rifle de francotirador sujeto con ambas
   manos pegado al pecho, cabeza gacha escuchando ·
   [1:22](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=82)
   · sirve para **pensar** o pedir silencio.
3. **Montado en la Drifter Bike, inclinado hacia delante**: manos en el manillar, torso inclinado
   sobre el depósito, casco/gorro oscuro, colándose entre dos camiones aparcados de noche ·
   [0:03](https://www.dailymotion.com/video/x84cgbc?t=3) · sirve para **presentar** su moto (el
   objeto que más lo identifica, ver punto 25 de `texto.md`).
4. **Escuchar de perfil mientras otro motero gesticula al hablar**: Deacon en primer plano, de
   perfil, quieto y serio, mientras un segundo motero (barba, chaqueta verde) gesticula con la
   mano detrás — sirve de contraplano cuando el diálogo de la lámina lo dice OTRO personaje y
   Deacon reacciona · [0:52](https://www.dailymotion.com/video/x84cgbc?t=52).
5. **Recelo en un túnel, a contraluz**: Deacon de perfil con la mandíbula tensa y la mirada de
   lado, mientras otro hombre (calvo, chaqueta clara) se acerca desde un túnel iluminado a
   contraluz rojo — postura defensiva, sin arma a la vista todavía ·
   [1:01](https://www.dailymotion.com/video/x84cgbc?t=61) · sirve para **alertar/desconfiar**
   (un aviso serio, no un regaño).
6. **Avanzar encorvado entre chatarra**: espalda encorvada hacia delante caminando por un
   vertedero a pleno sol, bate de béisbol con clavos y rifle cruzados sobre la mochila, cara
   fuera de cuadro (plano trasero) ·
   [7:42](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=462)
   · sirve para **avanzar con cautela** en terreno hostil.
7. **De pie eligiendo arma en la rueda radial**: parado en un camino de tierra hacia un puente,
   con el menú circular de armas arrojadizas abierto (seleccionando una granada de fragmentación)
   y la mochila con bate y rifle bien visible de espaldas ·
   [8:56](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=536)
   · sirve para **explicar el equipo** que lleva encima (bueno para una lámina de "inventario").
8. **Forcejeo cuerpo a cuerpo en la cueva**: Deacon de espaldas a la cámara, agarrado con un
   enemigo que alza ambos brazos para golpear, dentro de una cueva de roca iluminada por faroles
   de aceite dispersos y un resplandor rojo de fondo ·
   [0:34](https://www.dailymotion.com/video/x89n0df?t=34) · sirve para **defenderse/tensión**.
9. **Agachado disparando la escopeta dentro de una nave de madera**: rodilla en tierra, escopeta
   en alto, un enemigo sale despedido hacia atrás por el impacto (nube de sangre en el aire), luz
   dura entrando por las rendijas de las paredes ·
   [12:06](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=726)
   · sirve para **regañar/repeler una amenaza** de forma contundente.
10. **Revisar el arma agachado en un callejón**: agachado de espaldas entre dos paredes de tablón
    pintado (rojo desconchado a blanco), mirando hacia abajo el arma improvisada que lleva en las
    manos, como comprobándola antes de seguir ·
    [13:03](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=783)
    · sirve para **pensar/prepararse** antes de la acción (distinto del sigilo de la pose 2: aquí
    revisa el equipo, no escucha).

Sólo se documenta a Deacon (personaje "para empezar" del encargo); Boozer y Sarah casi no
aparecen en postura clara en el metraje mirado — cuando el redactor necesite sus poses, que pida
al investigador de imagen las hojas de contacto de la wiki (arte oficial), que sí los cubre.

## Lo mejor para la lámina

1. La pose 1 (contemplar el valle, [0:39](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=39)) — Deacon de espaldas con el equipo cruzado, ideal para un canal de "primeros pasos/guía": presenta sin tapar la cara.
2. La paleta del cementerio boscoso (`#08141C`/`#0E1F2A`/`#18313D`, punto 4) para un fondo serio y con profundidad (niebla en capas) sin ser plano.
3. El cruce **"You're Safe Now"** = pista 14 del álbum + storyline de la misión "I Kept My Name": si el redactor necesita un momento de calma/rescate, esa pista encaja por título con la escena de Lisa.
4. La rueda radial de armas (pose 7, [8:56](https://archive.org/download/DaysGoneE3VsRetailDirectComparison/Days%20Gone%20E3%20vs%20Retail%20Direct%20Comparison.mp4?t=536)) para una lámina que explique "herramientas/comandos" con un HUD de juego real, no inventado.
5. El texto exacto del compositor sobre **"Sarah's Theme"** ("probablemente la pieza más feliz del juego") para acompañar cualquier panel sobre el vínculo Deacon-Sarah.

## No encontré

- ⚠️ Un vídeo oficial de *making of* de sonido (sólo hay el texto del compositor en
  PlayStation.Blog, sin versión en vídeo); busqué "Days Gone sound design documentary" y
  "Nathan Whitehead Days Gone video interview" sin resultado en vídeo, sólo texto y podcasts de
  audio.
- ⚠️ Una tendencia viral concreta y reciente de TikTok sobre Days Gone (busqué en inglés y
  español): hay clips sueltos de gameplay sin viralidad medible, nada como un reto o formato que
  se repita. Lo pongo en "no encontré" y no en "Sigue" porque no es obligatorio (es un extra del
  punto 10, no el núcleo).
- ⚠️ Vídeo en YouTube: bloqueado por "inicia sesión" en este servidor durante toda la tanda (lo
  reintenté con 3-5 min de espera dos veces, seguía bloqueado); usé Dailymotion e Internet
  Archive como indica el aviso del jefe. Ningún clip de YouTube fue necesario al final.
- No es "no encontré": Boozer y Sarah casi no aparecen en el metraje que miré (es sobre todo
  Deacon en tercera persona); sus poses quedan para cuando el redactor cruce con las hojas de
  arte de `imagen.md`, que sí los cubre con ilustraciones oficiales.

## Bitácora de búsqueda

**Punto de partida**: `partes/datos-video.md` (Dailymotion, Internet Archive, MusicBrainz, ya
recolectados por `recolectar.py`) y `partes/episodios.md` (dos vídeos ya transcritos con
`episodio.py` por un intento anterior de esta misma parte). No repetí esas consultas.

**Vídeo mirado de verdad** (con `fotogramas.py`, frames sueltos verificados uno a uno antes de
describir la pose — varias primeras lecturas de las hojas de contacto en miniatura resultaron
imprecisas y las corregí contra el fotograma grande, ver punto 14):
- *Days Gone E3 vs Retail | Direct Comparison* (Internet Archive, 1080p, 15:02) — 259 fotogramas.
- Tráiler argumental de Days Gone (3DJuegos/Dailymotion, 2:06) — 54 fotogramas + 6 sueltos.
- Días Gone Trailer de lanzamiento (JeuxVideo/Dailymotion, 0:30) — 16 fotogramas.
- Días Gone Combat final (JeuxVideo/Dailymotion, 0:48) — 18 fotogramas + 2 sueltos.
- Días Gone Remastered Announcement Trailer (GRYOnline.pl/Dailymotion, 0:44) — 23 fotogramas.
- Total: 6 clips oficiales distintos mirados fotograma a fotograma, 5 frames con paleta medida
  (`estilo.py`).

**Búsquedas web** (13 de mi cupo de ~50; el resto de datos salió de la red directa: archive.org,
MusicBrainz, Fandom, Dailymotion):
- "Nathan Whitehead Days Gone score interview Sarah's Theme emotional scene music" (inglés) →
  llevó al post oficial de PlayStation.Blog, la fuente principal del punto 9.
- "Days Gone Freaker sound design horde screech onomatopeya efectos de sonido" (mixto es/en).
- "Days Gone cave knife fight captured tied up Rippers cutscene escape" (inglés) → identificó la
  misión "I Kept My Name" para el clip "Combat final".
- "Days Gone TikTok trend viral moto Deacon 2024 2025" (inglés) → sin resultado útil, declarado
  en "No encontré".
- "\"Days Gone\" escena que hace llorar Boozer amputación reacciones" (español) → confirmó que el
  punto 21 (emocional) es del rol de voz, no reabrí esa investigación.
- Fandom API `action=query&list=search&srsearch=Horde Killer` → confirmó que es un trofeo/logro
  real, no una etiqueta inventada por mí.
- Fandom API `action=parse&prop=wikitext&page=I_Kept_My_Name` → confirmó la misión del clip
  "Combat final" con una segunda fuente (wiki, además de 4 guías).
- MusicBrainz API (release-group `f17aa54f…`, `51a58e0d…`) y archive.org `/metadata/…` (3 items:
  soundtrack, E3vsRetail, All Cutscenes) para fechas, compositor y lista de pistas real.

**Fuentes usadas en esta parte** (cuento sólo las que aporté yo, sin repetir las 40+ de
`datos-video.md`/otras partes): PlayStation.Blog (entrevista del compositor), MusicBrainz (2
release-groups), Internet Archive (3 items: soundtrack, E3vsRetail, All Cutscenes — metadata),
Dailymotion (5 clips: tráiler argumental, lanzamiento, combat final, remaster, y el ya
transcrito "El mundo Parte 2"), Fandom `daysgone.fandom.com` (páginas `I Kept My Name`,
`Screamers`, `Horde Killer`, búsqueda interna), 4 guías de terceros (GameFAQs, Neoseeker, Orcz,
samurai-gamers) para la misión "I Kept My Name" — 15 fuentes propias, sobre las 40+ ya
acumuladas por el equipo en `datos-*.md` y las otras partes.

## Cumplimiento del encargo (mis puntos)

| Punto | Estado | Por qué |
|---|---|---|
| 2. Fotogramas de escenas icónicas | ✅ | 5 escenas icónicas con minuto y enlace, 1080p real en la fuente principal (Internet Archive), el resto Dailymotion 512×288 (YouTube bloqueado, uso avalado por el aviso del jefe); todo mirado fotograma a fotograma, no leído de reseñas |
| 4. Fondos y sitios: luz, paleta y texturas | ✅ | 4 sitios con paleta medida con `estilo.py` sobre fotogramas propios (no capturas ajenas), + 1 descrito sin medir (fuego en movimiento distorsiona el promedio, declarado ⚠️), con equivalentes CC0 de ambientCG para cada uno |
| 9. Música y sonido | ✅ | Compositor confirmado en dos fuentes, 11 pistas explicadas con cita textual y verificable del propio compositor (fuente oficial primaria), 3 efectos de sonido reconocibles con fuente |
| 10. Vídeos con minuto exacto | ✅ | 6 vídeos oficiales distintos mirados y tabulados con minuto; "análisis" cubierto con el vídeo narrado ya en `episodios.md`; tendencia de TikTok buscada y declarada como no encontrada (no es núcleo del punto) |
| 14. Poses por personaje (6-10, con minuto) | ✅ | 10 poses de Deacon, cada una verificada contra el fotograma grande (no sólo la miniatura de la hoja) antes de describirla, con minuto, enlace y para qué sirve; Boozer/Sarah delegados a `imagen.md` (declarado, no es un vacío) |

Fin de mi parte. No queda pendiente ningún punto obligatorio de mi rol (2, 4, 9, 10, 14).
