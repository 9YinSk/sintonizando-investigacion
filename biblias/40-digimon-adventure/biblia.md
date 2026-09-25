---
tags: [biblia, serie, laminas, biblioteca]
serie: "Digimon Adventure (デジモンアドベンチャー, Digimon: Digital Monsters)"
canal: "sin canal: propuesta #que-estas-escuchando (alternativas 🍟 General y #config-bots, ver §0)"
fecha: 2026-09-24
---

# Biblia · Digimon Adventure — para la biblioteca

> [!important] Cómo se hizo, y sus límites
> - La escribió el **redactor** sólo con las partes del equipo
>   (`partes/imagen.md`, `video.md`, `voz.md`, `texto.md` y, para
>   completar, los `datos-*.md` y los `.json`). Nada nuevo sin fuente.
> - **YouTube pidió iniciar sesión** (la descarga dio 403) y AnimeThemes
>   dio 522. Los vídeos se miraron en **Internet Archive** (episodios de
>   la serie de 1999, a 640×480) y **Dailymotion** (tráileres de *tri.*
>   y opening, a 512×288-384). **No hay fotogramas en 1080p.**
> - **Frases del doblaje latino**: 5 muestras de audio oficiales de
>   Doblaje Wiki oídas con `voz.py`, más frases del narrador que cita
>   Doblaje Wiki con su episodio (§10).
> - El redactor **miró las 3 hojas de `hojas/` número a número** y
>   corrigió la ropa de Tai, Matt y Sora, que la parte de imagen
>   describía mal (§16, §28).
> - **Punto 13 incompleto**: el investigador de voz agotó sus 2 tandas.
>   Faltan la alegría de Matt, la tristeza y la vergüenza de Gabumon y la
>   rabia y la tristeza de Agumon (§8.6).
> - ✅ = dos fuentes o visto por nosotros. ⚠️ = una sola fuente, o algo
>   que hay que comprobar. Lo que falta está en §28 y en la tabla final.

## Índice

Entre corchetes, el punto de `ENCARGO.md` que cubre cada sección.

0. Digimon Adventure no tiene canal: dónde encaja mejor
1. Resumen para quien tenga prisa
2. Las escenas que sirven, con minuto [2]
3. Arte oficial y hojas de contacto [1]
4. Fan art y 3D, sólo como referencia [3]
5. Sitios, luz, paleta y texturas reales [4]
6. Tipografía: una letra para cada uso [5]
7. Cómo hablan en pantalla: el cuadro de diálogo [6]
8. Los personajes: qué transmiten, su cara y sus dinámicas [13]
9. ¿Quién es el más querido? [7]
10. Doblaje latino y frases textuales [8]
11. Música y sonido [9]
12. Vídeos y tendencias [10]
13. Videojuegos de la franquicia [11]
14. Lo que ama el fandom, y qué NO hacer [12]
15. Poses analizadas por personaje [14]
16. Vestuario, con hex medidos [15]
17. Paisajes y fondos de pantalla [16]
18. Guía para generar con IA: imagen y texto [17]
19. Estilo de dibujo, técnica, Blender y encuadres [18]
20. Texturas 2D [19]
21. Gustos y detalles de cada personaje [20]
22. Por qué la gente la ama, y las escenas que hacen llorar [21]
23. Fan dubs y comunidad hispana [22]
24. Colaboraciones, figuras y cosplay [23]
25. Obras parecidas y láminas vecinas [24]
26. El mundo, la historia por arcos y sus símbolos [25]
27. Tres conceptos de lámina
28. Lo que no pude verificar, y lo que corregí de las partes
- Cumplimiento del encargo
29. Bitácora de búsqueda

---

## 0 · Digimon Adventure no tiene canal: dónde encaja mejor

El encargo dice por qué está: **nostalgia de toda una generación**. Las
partes lo concretan en un momento: la **despedida del episodio 54**. La
**armónica de Matt** y el **silbato de Kari** son lo que la gente
recuerda con más cariño, incluso sin acordarse del capítulo
([LEVEL UP](https://www.levelup.com/noticias/la-aventura-digievoluciona-a-19-anos-de-la-emision-del-ultimo-episodio-de-digimon-adventure/) ✅).

Miré los textos reales de `servidor/inventario.md`, lo que proponen las
otras biblias (`grep '^canal:' biblias/*/biblia.md`) y los avisos de
`lotes/D.md`. En 37, 38 y 39 ya chocan **#general-doblaje, #destacados,
🎲 Juegos, #eventos, 🎭 Escenario, 🎚️ Mesa de Trabajo, 🎙️ Grabación y
🎶 Karaoke**. Ninguna de mis tres propuestas está en esa lista.

### 0.1 La propuesta

| Orden | Canal o sala | Texto real del inventario | Por qué Digimon | Choca con |
|---|---|---|---|---|
| **1 (recomendado)** | **ıı・🎧・que-estas-escuchando** (LA SALA) | «La canción que llevas en bucle. Pega el enlace y di por qué.» | la melodía de la **armónica de Matt** es el recuerdo más querido de la serie (§22); en esa despedida suena «Butter-Fly» (Doblaje Wiki ⚠️). Una canción en bucle, dicha por quien la toca | Demon Slayer (31) lo pide **de segunda opción** (Zenitsu y el shamisen). K-On! (10) apunta un guiño de lámina 2. **Ninguna de 37-39** |
| 2 | **🍟・General** (LA SALA, voz) | sin descripción en el inventario: la sala de voz para hablar de lo que sea | Tai **llama desde un teléfono público** del Mundo Digital con Agumon impaciente detrás (IA, min 30:00, §15). Entrar a una sala de voz es hacer una llamada | Jujutsu Kaisen (32) la pide **de segunda opción** (Inumaki) |
| 3 | **ıı・🔧・config-bots** (PRIVADOS) | «Checklist de bots y qué configurar en cada uno.» | el **Digimon Analyzer** es una ficha técnica por criatura: nombre en cápsula, nivel, tipo y ataque (§7). **Una ficha por bot** | **nadie**. Pero es privado: sirve si los privados llevan lámina. Reserva pública: **#noticias-anime** (el ticker rojo del Analyzer), que pide Bleach (29) |

**Mi recomendación: la 1.** Es el recuerdo más fuerte de la serie, su
protagonista (Matt) es el **2.º más votado** en la encuesta oficial de
Toei, por delante de Tai (§9), y el objeto (una armónica) se hace en
Blender.

### 0.2 Los canales que miré y descarté

| Canal | Por qué no |
|---|---|
| #general-doblaje | el dato de Gloria Rocha es perfecto «del oficio»: pidió a cada actor que **eligiera su Digimon**, y Circe Luna eligió primero a Gabumon (§10). Pero lo piden 29, 37 y 39 (y 38 de reserva). No sumo un cuarto choque |
| #castings | el mismo dato encajaría («cada actor eligió su papel»), pero #castings es de Oshi no Ko (05) |
| 🎲 Juegos | *Digimon World* (PS1) tiene caja de diálogo propia (§13), pero chocan Ralph (29), Sailor Moon (38) y One Punch Man (35) |
| #destacados | los Emblemas brillan, pero lo piden 29, 37, 38 y 39 |
| 🎙️ Grabación, 🎶 Karaoke | en el ep. 25 Mimi canta «I Wish» con la voz de Marisa de Lille (Doblaje Wiki); chocan con 29 y 38 |
| #demos, #presentaciones | la ficha del Analyzer sería ideal, pero tienen serie (Evangelion, Spy x Family) |
| #a-que-juegas | Cyberpunk: Edgerunners (27) |
| #staff, #postulaciones | los proponen FMA (37) y Haikyuu (34) |
| 📻 RADIO EN VIVO | musical como la 1: los tres conceptos tienen que ser distintos |

---

## 1 · Resumen para quien tenga prisa

- **Qué es.** Anime de **Toei Animation**, 54 episodios, del 7 de marzo
  de 1999 al 26 de marzo de 2000 en Fuji TV. Dirección de **Hiroyuki
  Kakudou** (§19). Siete niños de un campamento de verano cruzan al
  **Mundo Digital**; cada uno tiene su **Digimon compañero** (§26).
- **Doblaje latino.** Intertrack (México), dirección de **Gloria Rocha**
  (ep. 1-9) y **Alma Moreno** (ep. 10-54). Tai: **Miguel Ángel Leal**
  (ep. 1-9) y luego **Gerardo Meza**. Matt y Agumon: **Uraz Huerta**.
  Sora y Gabumon: **Circe Luna**. Cada actor dobló a un niño y al
  Digimon de **otro** niño (§10).
- **El más querido.** Encuesta oficial de Toei: **Kari 1.ª (969 votos),
  Matt 2.º (662), Tai 5.º (366)**. En AniList y Danbooru, Tai va primero
  entre los humanos del encargo (§9).
- **Cómo hablan en pantalla.** No hay globo de cómic. La voz visual de
  la serie es el **Digimon Analyzer**: ficha oscura con rejilla y el
  nombre en una **cápsula de color**. En el juego *Digimon World* (PS1),
  una caja **azul petróleo #39464B** con borde cian, nombre en
  amarillo verdoso y texto blanco en píxel (§7).
- **Objetos estrella.** La **armónica** de Matt, la **Etiqueta con el
  Emblema** (colgante dorado; hay modelo 3D libre), el **Digivice** y
  las **goggles** de Tai (§26).
- **Qué NO hacer.** Tai sin goggles; los Digimon como mascotas; mezclar
  el diseño de 1999 con el de *tri.* (§14).
- **Límites.** Vídeo a 640×480 como mucho; punto 13 incompleto (§8.6);
  sin *databook* (§21).

---

## 2 · Las escenas que sirven, con minuto

Todo mirado de verdad con `fotogramas.py` o `ffmpeg` sobre el vídeo,
no de memoria. Dos archivos de Internet Archive con el metraje de Toei
(el audio es el inglés de Saban):

- **IA-V1**: [*Digimon: Digital Monsters – Volume 1*](https://archive.org/details/digimon-digital-monsters-volume-1-1999-vhs),
  640×480, 62:54. Trae una introducción de personajes y los episodios 1
  y 2. Los minutos son de este archivo.
- **IA-C**: la [colección completa](https://archive.org/details/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent),
  un archivo por episodio. Los minutos son del episodio.

⚠️ **Resolución.** Nada llega a 1080p. El tráiler oficial de *tri.* sí
existe en 1080p en [YouTube](https://www.youtube.com/watch?v=JOK5aPOeo2I),
pero la descarga dio 403 (pide iniciar sesión).

### 2.1 La serie de 1999 ✅ visto

| Escena | Dónde y minuto | Qué se ve | Para qué |
|---|---|---|---|
| **Primera digievolución: Agumon → Greymon** | IA-V1, **~38:20** («The Birth of Greymon») | destello blanco que sale de Agumon, con la cartela japonesa アグモン encima | la escena más reconocible de la franquicia |
| **Tai carga a Agumon** | IA-V1, **20:00** | Tai lo lleva en brazos, los dos sonriendo; asoma un ala blanca y naranja (probablemente Biyomon ⚠️) | cariño, bienvenida |
| **El grupo entre plantas gigantes** | IA-V1, **11:30** | Tai, Matt, Sora, Izzy y T.K. de pie, mirada expectante | grupo |
| **Tai al teléfono público** | IA-V1, **30:00** | aprieta el botón; Agumon asoma detrás, impaciente | concepto B |
| **La fogata con el pez** | IA-V1, **48:00** | Tai enseña un pez recién pescado, orgulloso; Matt, de pie con los brazos atrás, escéptico | Tai presumiendo, Matt dudando |
| **Garurumon sale de la nieve** | IA-V1, **58:10** | entre carámbanos, fauces abiertas | acción de Gabumon |
| **Tai asustado con Koromon** | IA-C ep. 1, [**9:16**](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x01%20-%20And%20So%20It%20Begins....mp4?t=556) | ojos muy abiertos, abraza a Koromon mientras ataca Kuwagamon | miedo |
| **Tai pierde los nervios** | IA-C ep. 16, [**7:50**](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x16%20-%20The%20Arrival%20of%20Skullgreymon%20%5Ba.k.a.%20The%20Arrival%20of%20Scar%20Greymon%5D.mp4?t=470) | ceño fruncido, mandíbula tensa, antes de patear el balón | rabia |
| **Tai pide perdón a Koromon** | IA-C ep. 16, [**19:40**](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x16%20-%20The%20Arrival%20of%20Skullgreymon%20%5Ba.k.a.%20The%20Arrival%20of%20Scar%20Greymon%5D.mp4?t=1180) | lo abraza con la mirada baja, tras SkullGreymon | culpa |
| **Sora escondida del grupo** | IA-C ep. 26, [**10:56**](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x26%20-%20Sora%27s%20Crest%20of%20Love.mp4?t=656) | mirada baja, evita a Tai y Matt | vergüenza |
| **Gabumon muerde a Matt** | IA-C ep. 44, [**14:40**](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x44%20-%20Trash%20Day.mp4?t=880) | colmillos fuera, ojos entrecerrados; le riñe por compararse con Tai | rabia leal |
| **Matt en la cueva oscura** | IA-C ep. 51, [**5:25**](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x51%20-%20The%20Crest%20of%20Friendship.mp4?t=325) | agachado, abrazándose las rodillas, sin mirar a Gabumon | vergüenza |
| **La despedida: Matt** | IA-C ep. 54, [**13:28**](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x54%20-%20The%20Fate%20of%20Two%20Worlds%20(2).mp4?t=808) | ojos cerrados, recuerda a Garurumon | concepto A |
| **La despedida: Tai y Agumon** | IA-C ep. 54, [**14:00**](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x54%20-%20The%20Fate%20of%20Two%20Worlds%20(2).mp4?t=840) | se abrazan en la playa, sonrisa enorme | alegría |
| **La despedida: Sora en el tren** | IA-C ep. 54, [**14:28-14:48**](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x54%20-%20The%20Fate%20of%20Two%20Worlds%20(2).mp4?t=868) | ojos muy abiertos y brillantes, a punto de llorar | tristeza |

### 2.2 *Digimon Adventure tri.* (2015-2018) ✅ visto

| Escena | Dónde y minuto | Qué se ve |
|---|---|---|
| **Tai golpea a Matt** | tráiler del cap. 5, [0:54](https://www.dailymotion.com/video/x5zbgmg) | en una duna, explosión de arena; Matt echa la cabeza atrás. El momento más polémico de *tri.* |
| **Matt grita, pantalla partida con Tai** | mismo tráiler, 0:45 | boca muy abierta, alarma |
| **Cartelas de nombre de cada uno** | tráiler del cap. 1, [1:24-2:08](https://www.dailymotion.com/video/x8x2nx4) | retrato con su nombre en japonés: 武之内空 (1:52), 石田ヤマト (2:00), 八神太一 (2:04) |
| **Tokio de noche** | tráiler de los caps. 2-3, [0:42](https://www.dailymotion.com/video/x3rmlro) | luces de ciudad, violeta y amarillo (§5) |

---

## 3 · Arte oficial y hojas de contacto

### 3.1 Las tres hojas (miradas enteras por el redactor)

Las montó el investigador de imagen con `investigar_serie.py` desde la
wiki [digimon.fandom.com](https://digimon.fandom.com/wiki/Digimon_Adventure).
**Ojo:** la wiki mezcla toda la franquicia. Abajo, sólo lo que es de
*Adventure* (1999), de *02*, de *tri.* o de *Kizuna*.

**`hojas/personajes_01.jpg`** (39 imágenes)

| Nº | Qué es | Para qué |
|---|---|---|
| 1 | Tai con goggles y su cartela 八神太一 (ficha de *Xros Wars*) | presentar |
| 4 | Matt y T.K. de noche (película 1) | los hermanos |
| 5 | Sora niña en una ventana (película 1) | Sora sola |
| 10 | página del manga *V-Tamer* en blanco y negro | trama de puntos (§20) |
| 11 | los **8 Emblemas** del reboot 2020, en neón | color de cada uno (§26) |
| **12, 13** | **Etiquetas doradas** «Crest of Destiny» y «Crest of Miracles» (560×560, recuerdo oficial) | **el objeto** (§27) |
| 15 | Digivice de Kari | objeto |
| 16-28 | **epílogo adulto de *02***. Destacan: **19** Tai con traje y maletín junto a Agumon con pajarita, ante un edificio con banderas; **23** Matt **astronauta** con Gabumon en traje espacial, sobre suelo rojo; **25** Koushiro con Tentomon ante un ordenador | versiones adultas |
| **29** | Sora de cuerpo entero (juego *Re:Digitize*): gorro azul, top amarillo sin mangas, guantes rojos, vaqueros | ropa icónica de Sora |
| **30** | Tai de cuerpo entero (*Re:Digitize*): goggles, camisa azul con estrella naranja, guantes blancos, pantalón corto marrón, puño en alto | ropa icónica de Tai |
| **32** | Matt (captura de Fox Kids): camiseta **verde sin mangas de cuello alto**, sonrisa | ropa icónica de Matt |
| 35-39 | ropa de verano de *02* (Sora «CIRCLE» rosa, Tai «TRIANGLE» azul, Matt camisa negra, Koushiro, Mimi) | otra época |

No usar: 2, 3 (otras series), 33 (manga de *Xros Wars*).

**`hojas/fondos_01.jpg`** (39 imágenes)

| Nº | Qué es | Para qué |
|---|---|---|
| **3** | **key visual de *tri.* «Reunión»** (1476×2080): Tai y Matt de uniforme sobre la espada de Omegamon, mirando arriba | pose viva: personaje pequeño y Digimon gigante |
| 4, 5, 10, 11, 12, 24 | pósters de *tri.* (grupo saltando, grupo junto a un autobús, Tai y Matt con Agumon y Gabumon en la escuela, Tai pequeño con Agumon) | grupo |
| 19, 20, 21, 36 | pósters «Loss», «Future», «Coexistence», «Confession» | composición en diagonal |
| 1, 17, 23 | pósters de broma de April Fool (amarillo y rojo) | humor |
| 13, 22 | pósters de *Last Evolution Kizuna* (22: el grupo adulto con «WE'LL ALWAYS BE TOGETHER») | adultos |
| 14, 15 | logos de *Kizuna* (serif rojo) y de *tri.* (líneas finas azules) | §6 |
| 9 | cartela **勇気の紋章** («El Emblema del Valor») en blanco sobre negro | ⚠️ el archivo es de la lista de episodios de *Digimon Adventure:* (2020), no de 1999 |
| **16, 39** | **la Isla File** vista desde arriba (1024×854 y la del ep. 8, 640×480) | toda la isla de un vistazo |
| **25-30** | los 6 fondos pintados de *Digimon Story* (Binary Castle, Fluorescent Cave, Gravel Wasteland, Powdery Cliff, Railroad Plains, Signpost Forest) | fondos (§5) |
| 6-8, 33-35 | Analyzer del reboot 2020: nombre en blanco sobre **barra roja**; enciclopedia con HUD cian | §7 |
| 37 | arte de carta con **caja de narración** blanca de borde negro («ここはとあるサル山…») | §7 |
| 38 | manga *V-Tamer* a color: Gabumon, mapa con «FOLDER» y «FILE», onomatopeya どーん | §6 y §7 |
| 32 | película *Our War Game* (secuela directa, AniList) | Tai e Izzy |

No usar: 2, 18, 31 (otras series).

**`hojas/objetos_01.jpg`** (48 imágenes)

| Nº | Qué es | Para qué |
|---|---|---|
| **3** | **Digivice clásico blanco** en primer plano (*tri.*, 1920×1090) | **el objeto** |
| 13 | Digivice de *tri.* con la pantalla en rojo | objeto con luz |
| 2, 12 | D-3 de T.K. y de Kari (*02*) | |
| 18 | Digivice en forma de móvil de T.K. (*Kizuna*) | |
| 15 | **Digimon Twin**: mascota virtual, dibujo técnico | el origen de juguete (§26) |
| **16** | **LB Pop-Up Theater «デジモンショップ Part2»** (Shibuya PARCO, 21-feb a 16-abr-2020): arte de grupo nuevo | §24 |
| 20 | Tai con la cartela 八神太一 | |

**No usar el resto** (4-11, 14, 17, 19, 21-45, 47-48): App Drive, Fusion
Loader, Darkness Loader y *Seekers* son de otras series.

### 3.2 Fuera de las hojas

- Portada oficial de AniList: [460×690](https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx552-zad0ts5hylQJ.jpg). Banner: [1280×371](https://s4.anilist.co/file/anilistcdn/media/anime/banner/552-xAHaRMpoco2e.jpg) ✅.
- Key visual «Reunión» en grande: [1476×2080](https://static.wikia.nocookie.net/digimon/images/f/f7/Reunion_%28Promotional_Poster%29.jpg) ✅ (la fecha 2015.11.21 y los créditos de Toei van impresos).
- Renders de *Re:Digitize*: [Tai](https://static.wikia.nocookie.net/digimon/images/4/4e/Taichi_%22Tai%22_Kamiya_%28Re-Digitize%29_b.jpg) y [Sora](https://static.wikia.nocookie.net/digimon/images/a/af/Sora_Takenouchi_%28Re-Digitize%29_b.jpg), 438×640 ✅.
- Retratos oficiales de AniList (230×344-368): [Tai](https://s4.anilist.co/file/anilistcdn/character/large/b1907-ZWmX1dVGPfqn.png), [Matt](https://s4.anilist.co/file/anilistcdn/character/large/b1909-BFIYnrdbeLhB.png), [Sora](https://s4.anilist.co/file/anilistcdn/character/large/b2276-edQsS9qzUbm5.png), [Agumon](https://s4.anilist.co/file/anilistcdn/character/large/b4950-7ABdx6j3jmdE.png), [Gabumon](https://s4.anilist.co/file/anilistcdn/character/large/b9952-mI01ix3dEKMp.png).
- Hojas de modelo de la wiki (320×320): [Agumon](https://static.wikia.nocookie.net/digimon/images/6/68/Agumon_b.jpg), [Gabumon](https://static.wikia.nocookie.net/digimon/images/d/d1/Gabumon_b.jpg).
- Etiqueta dorada: [Crest of Destiny](https://static.wikia.nocookie.net/digimon/images/2/2c/Crest_of_Destiny_%28Memorial_Goods%29.jpg) (560×560) ✅.

---

## 4 · Fan art y 3D, sólo como referencia

### 4.1 Modelos 3D con licencia libre (Sketchfab) ✅

Licencia y autor leídos en la API de Sketchfab. Crédito: «<modelo> by
<autor>, CC BY 4.0».

| Modelo | Autor | Licencia | Para qué |
|---|---|---|---|
| [**Digimon Adventure Tag and Crest**](https://sketchfab.com/3d-models/none-e3c40eec7aea44ad9bbf438612bb05ff) | TriumphantBass | CC BY | **la Etiqueta con su Emblema**: el objeto de la lámina, ya en 3D |
| [**Agumon (Bond of Bravery)**](https://sketchfab.com/3d-models/agumon-bond-of-bravery-4c7acf3383624e90a73b9397f4ecf780) | drewsdigitaldesigns | CC BY 4.0, uso comercial con crédito | **con *rig* y 13 animaciones**, 11 978 caras: se puede posar |
| [Agumon](https://sketchfab.com/3d-models/none-a5680622539345a9a0471682e5498d40) | AndriyVladykin | CC BY | otra versión (♥19) |
| [Agumon](https://sketchfab.com/3d-models/none-9926ba8c8bad4978b2a8b072c6094b4a) | hdbanks1 | CC BY | otra versión |
| [Greymon](https://sketchfab.com/3d-models/none-94f00275d03f4eca82dcf1c88d1d688a) | McNaught Design | CC BY | la digievolución |
| [WarGreymon](https://sketchfab.com/3d-models/none-ab4b4b2df874430992709e5986415857) | hdbanks1 | CC BY | el nivel Mega |
| [Botamon](https://sketchfab.com/3d-models/none-8c960d46fc134612ab4b286788de9d45) y [Botamon Happy](https://sketchfab.com/3d-models/none-fde9375d74144981b503c8474597026d) | Mega_Jimjims | CC BY | la forma bebé de Agumon: ternura |

No sirven: Terriermon (es de *Tamers*) y BlitzGreymon (*Digimon
Masters*). Poly Haven no tiene nada de la serie (búsqueda hecha).

### 4.2 Fotos con licencia libre (Openverse / Flickr), miradas por el redactor

| Foto | Autor | Licencia | Qué es |
|---|---|---|---|
| [1](https://live.staticflickr.com/65535/51340134422_a27633dbe9_b.jpg), [2](https://live.staticflickr.com/65535/51341867700_876e88815e_b.jpg), [3](https://live.staticflickr.com/65535/51341597154_ffd4b69f61_b.jpg), [4](https://live.staticflickr.com/65535/51341077408_5713aa442a_b.jpg), [5](https://live.staticflickr.com/65535/51340856696_7b09745464_b.jpg) | moggymawee | CC BY 2.0 | **figura de Matt con Gabumon a la espalda**, base azul «YAMATO & GABUMON», desde 5 ángulos. Confirma la ropa de Matt: **camiseta verde sin mangas de cuello alto, vaqueros azules, zapatos marrones** |
| [1](https://live.staticflickr.com/65535/51341077183_e653baf8fb_b.jpg), [2](https://live.staticflickr.com/65535/51341867570_7507d8b08e_b.jpg), [3](https://live.staticflickr.com/65535/51341867480_6d107c2dbb_b.jpg) | moggymawee | CC BY 2.0 | peluche de Matt y regalos del 20.º aniversario |
| [tarta](https://live.staticflickr.com/833/39782045630_d52f89ea5d_b.jpg) | Dan Lundberg | CC BY-SA 2.0 | tarta en forma de **Etiqueta azul con el Emblema del Valor** dorado: objeto casero real |
| [1](https://live.staticflickr.com/751/22168147451_d39aa32dbf_b.jpg), [2](https://live.staticflickr.com/723/21971044679_ef36d4e617_b.jpg), [3](https://live.staticflickr.com/625/21971044159_f1cdbfa422_b.jpg), [4](https://live.staticflickr.com/5721/22131748556_2757f37905_b.jpg) | ThanhQuan_95 | CC BY-NC-SA 2.0 | figura S.H.Figuarts de **MetalGarurumon** y su caja |
| [cosplay](https://live.staticflickr.com/65535/48767031176_aba35f5b2f_b.jpg) | esurientt | CC BY-NC-ND 2.0 | Tai de *tri.* y Kari con peluches de Agumon y Gatomon |
| [Angewomon](https://live.staticflickr.com/7036/6917296453_a60bba0b20_b.jpg), [Lillymon](https://live.staticflickr.com/7037/6947883105_7b7717ebca_b.jpg) | greyloch | CC BY-NC-ND 2.0 | cosplay con alas de volumen real |
| [Wizardmon](https://live.staticflickr.com/8348/8170609984_8b1e0c6646_b.jpg) | _casterclass | CC BY-NC 2.0 | cosplay, capa azul en movimiento |

### 4.3 Fan art (sólo para mirar, nunca para pegar)

Del [Safebooru](https://safebooru.org) (puntuación y origen en
`datos-imagen.md`). Siempre con su autor:

- Tai en grupo, [2520×2520](https://safebooru.org/images/4619/14fcd3507038cb1636e15d640de74c13deac4fa3.png), 16 puntos, de [@totototo0507](https://twitter.com/totototo0507/status/1807802641482985883).
- Agumon, Gabumon y compañía, [1000×779](https://safebooru.org/images/4155/23ef8211864ffd88e2d27020adeec945b17efa51.jpg), de [@WithTheWill](https://twitter.com/WithTheWill/status/1632838625129033728).
- Agumon, [1920×1200](https://safebooru.org/images/655/c60e439be0f0c62595071041e5f2e3e82c4c67f6.png), de hajime-ill-1st (Pixiv).
- Sora, [826×1748](https://safebooru.org/images/3054/fe465ebbec50aebc0400f259b5d1c8cbb62033d3.jpg), de [maro05](https://maro05.tumblr.com/post/154787030697).
- Kari con Gatomon, [1280×1300](https://safebooru.org/images/1269/d673c740663e2fbcdcec0b3a1a525c9c9e7830a8.jpg), 11 puntos, de superhamasuke (Pixiv).
- Angewomon en vuelo, [2500×1642](https://safebooru.org/images/1323/c6b93ffec957ffcd266569934706d69e21bda7ba.jpg) (Pixiv).

### 4.4 Cómo etiqueta el fandom a cada uno ([Danbooru](https://danbooru.donmai.us/posts?tags=digimon_adventure)) ✅

- **Tai**: `brown_hair`, `goggles_on_head`, `blue_shirt`, `white_gloves`, `brown_shorts`, `star_print`, `blue_headband`, `spiked_hair`.
- **Sora**: `orange_hair`, `short_hair`, `helmet`, `hat`, `yellow_shirt`, `sleeveless_shirt`, `red_gloves`, `jeans`.
- **Agumon**: `green_eyes`, `sharp_teeth`, `claws`, `orange_scales`, `dinosaur`, `tail`.
- **Gabumon**: `single_horn`, `blue_fur`, `yellow_skin`, `red_eyes`, `belt`, `fangs`.

---

## 5 · Sitios, luz, paleta y texturas reales

### 5.1 Medidos en fotogramas del anime (`estilo.py`) ✅

| Sitio | Fuente y minuto | Paleta medida | Luz |
|---|---|---|---|
| **Selva con flor gigante** (Mundo Digital) | IA-V1, 11:30 | #7E9272 20% · #58736E 15% · #765444 13% (tronco) · #C2BAA4 12% | difusa, blanquecina, sin sol: niebla vegetal |
| **Exterior diurno, Tai y Agumon abrazados** | IA-V1, 20:00 | #F4FDF9 32% (cielo casi blanco) · #D3DABE 15% · #EAF3D8 15% · #604E37 6% | sobreexpuesta, muy clara: la suavidad de 1999 |
| **Bosque tranquilo** | IA-V1, 13:00 | #D1F6E3 17% · #EDFDF3 16% · #BEE0D2 14% (mentas claros) | suave, sin sombras marcadas |
| **Bosque al atardecer rosado** | IA-V1, 45:00 | #D58D98 19% (rosa) · #FCFCF9 15% · #F7F7CD 14% · #8E4C67 6% (sombra violeta) | atardecer cálido, degradado rosa a amarillo; **un cartel de tráfico en silueta delante** |
| **Tokio de noche** (*tri.*) | [tráiler x3rmlro](https://www.dailymotion.com/video/x3rmlro), 0:42 | #ECE4E1 37% · #1E140E 18% · #AA73C0 12% (violeta neón) · #DEE250 10% (luces) | nocturna, mucho contraste |

La línea de 1999 es **gris suave** (#8F8B71, #ACC2AF), con sombreado
mixto. *tri.* casi no tiene línea. El fondo real del anime es **más
pálido** que el arte promocional.

### 5.2 Los fondos pintados de *Digimon Story* (miden la Isla File) ✅

Arte de fondo de los juegos, con línea de boceto visible (no es
fotograma). 812×574 cada uno. Nº 25-30 de `hojas/fondos_01.jpg`.

| Sitio | Qué es | Paleta medida | Luz |
|---|---|---|---|
| [Binary Castle](https://static.wikia.nocookie.net/digimon/images/c/c8/Binary_Castle_b.jpg) | bóveda dorada; **cientos de televisores turquesa colgando de cables**; trono al fondo; una silueta diminuta da la escala | #333B34 32% · #232925 25% · #66E3DD 4% (pantallas) | cálida arriba, turquesa abajo |
| [Fluorescent Cave](https://static.wikia.nocookie.net/digimon/images/b/bb/Fluorescent_Cave_b.jpg) | cristales que brillan | #232E41 28% · #2E4C67 20% · #D5A550 5% | azul violeta con puntos ámbar |
| [Gravel Wasteland](https://static.wikia.nocookie.net/digimon/images/2/2b/Gravel_Wasteland_b.jpg) | desierto naranja con **engranajes enterrados**; trama cruzada en la roca | #A16541 25% · #5B4839 20% · #EFFBFB 10% (cielo) | mediodía, sombras cortas |
| [Powdery Cliff](https://static.wikia.nocookie.net/digimon/images/b/b5/Powdery_Cliff_b.jpg) | acantilado nevado con niebla | #587F96 · #6999B1 · #22282C | fría |
| [Railroad Plains](https://static.wikia.nocookie.net/digimon/images/a/ae/Railroad_Plains_b.jpg) | campo verde con **vías de tren y torres eléctricas** | #7D8E46 · #5AA2D7 (cielo) · #4B6432 | día |
| [Signpost Forest](https://static.wikia.nocookie.net/digimon/images/9/90/Signpost_Forest_b.jpg) | bosque oscuro con **carteles clavados** entre los árboles | #4A583A · #34432E · #0E1B1A | tenue, casi de noche |

Lo que se repite: **objetos humanos fuera de lugar** en la naturaleza
(televisores, vías, postes, carteles, un teléfono público). Es la marca
del Mundo Digital y la clave de los conceptos (§27).

### 5.3 Texturas reales equivalentes

- Tela y madera, CC0: [ambientCG](https://ambientcg.com/api/v2/full_json?type=Material&q=fabric) (`q=fabric` para el verde de la selva, `q=wood` para troncos). ⚠️ La parte sólo dejó la búsqueda, sin elegir una textura concreta.
- Rejilla digital, CC0: [CC0 Textures, etiqueta «grid»](https://cc0-textures.com/tag/grid) ✅ (licencia CC0 en la portada).

---

## 6 · Tipografía: una letra para cada uso

### 6.1 Los logos ✅

- **Logo japonés** デジモンアドベンチャー ([512×195](https://static.wikia.nocookie.net/digimon/images/5/59/Digimon_Adventure_Logo.png/revision/latest?cb=2014121322)),
  medido con `estilo.py`: relleno en degradado de amarillo **#FAD30A**
  a naranja **#EA6F0B**, contorno grueso azul **#1164A7**, línea oscura
  #392903 y #211510. El borde va **recortado en zigzag**, como una
  descarga digital.
- **Logo internacional** «DIGIMON DIGITAL MONSTERS» (Fox Kids, 1999,
  [269×143](https://static.wikia.nocookie.net/digimon/images/5/5c/LOGODIGIMON.jpg/revision/latest?cb=20080227233316)):
  parche redondo; «DIGIMON» en letras gruesas, condensadas e inclinadas,
  naranja con contorno azul y negro; «DIGITAL MONSTERS» en el anillo.
- *tri.*: mayúsculas finas en línea azul (nº 15 de `fondos_01.jpg`).
  *Kizuna*: serif fino rojo (nº 14).

### 6.2 La letra libre para cada uso ✅

Cada una se bajó en `.ttf` y se abrió con `fontTools`
(`getBestCmap()`): **todas traen á é í ó ú ñ Ñ ¿ ¡**. Truco que
encontró la parte: en Fontsource el subconjunto **«latin»** trae los
acentos; el «latin-ext» no.

| Uso | Letra libre | Licencia | Por qué |
|---|---|---|---|
| Logo o título | [**Anton**](https://fonts.google.com/specimen/Anton), inclinada 8-10° a mano | OFL | gruesa y condensada como el parche de 1999 |
| Logo, versión «juguete de los 90» | Titan One | OFL | más redonda |
| Globo normal | [**Baloo 2**](https://fonts.google.com/specimen/Baloo+2) 700 | OFL | redondeada, amable |
| Grito («¡Agumon, digievoluciona!») | [**Bangers**](https://fonts.google.com/specimen/Bangers) | OFL | cómic en cursiva |
| Pensamiento | [**Patrick Hand**](https://fonts.google.com/specimen/Patrick+Hand) | OFL | rotulador suave |
| Onomatopeya | [**Luckiest Guy**](https://fonts.google.com/specimen/Luckiest+Guy) | OFL | muy gruesa |
| Cartel del mundo (carteles de madera, File City) | [**Permanent Marker**](https://fonts.google.com/specimen/Permanent+Marker) | OFL | marcador a mano |
| Interfaz de juego | [**Press Start 2P**](https://fonts.google.com/specimen/Press+Start+2P) | OFL | píxel, como *Digimon World* |
| Pantalla de Digivice o terminal | VT323 | OFL | monitor CRT verde |
| Subtítulos y créditos | [**Nunito**](https://fonts.google.com/specimen/Nunito) | OFL | limpia en el celular |

⚠️ **No usar** la fuente de fans [«Digimon World DS»](https://www.dafont.com/digimon-world-ds.font)
(dafont): comprobada con fontTools, **no trae tildes, ñ, ¿ ni ¡**. Sólo
valdría para la palabra «DIGIMON».

---

## 7 · Cómo hablan en pantalla: el cuadro de diálogo

*Digimon Adventure* es anime: **no tiene manga propio con globos**. El
manga de la franquicia, *V-Tamer 01* (Hiroshi Izawa, V-Jump, 1998-2003),
cuenta otra historia con otro Tai ([wiki](https://digimon.fandom.com/wiki/Digimon_Adventure_V-Tamer_01) ✅).
Tampoco hay nube de pensamiento: lo interior va en voz en off.

Por eso el cuadro propio de la serie es **una pantalla de datos**, no
un globo.

### 7.1 El Digimon Analyzer, primera versión ✅ (visto y medido)

Sale cuando entra un Digimon nuevo, desde la llegada al Mundo Digital
hasta la derrota de Etemon ([wiki](https://digimon.fandom.com/wiki/Digimon_Analyzer)).
Captura de [Tanemon](https://static.wikia.nocookie.net/digimon/images/f/f2/TanemonAnalyzer.jpg/revision/latest?cb=20091229024613) (300×240):

- fondo negro con **rejilla**;
- el Digimon en un recuadro negro;
- el nombre en **letras azules sobre una etiqueta verde redondeada**
  («TANEMON»);
- a la derecha, una **caja rosa** con el nivel (幼年期) y una tabla de
  datos (レッサーデジモン / タイプ / データ / 必殺技).
- Paleta: negro **#030302** (51%), gris verdoso #324632, turquesa
  **#42B9AC**, verde **#319F41**. Brillo bajo: todo negro menos la ficha.

### 7.2 El Analyzer, segunda versión ✅ (visto y medido)

Se lo da Gennai a Izzy; luego lee los Digivices de los demás. Captura
de [MagnaAngemon](https://static.wikia.nocookie.net/digimon/images/5/52/Magnaangemon.jpg/revision/latest?cb=20091229025009) (300×240):

- fondo negro con un **ticker rojo en bucle** arriba y abajo:
  «ANALYZER DIGIMON ANALYZER DIGIMON…»;
- nombre en **letras verdes sobre una cápsula** negra y verde;
- etiqueta rosa con el nivel (完全体) y tres cajas negra, naranja y plata.
- Paleta: #362E1E 17%, #1B0A02, beige #A69584 y #817060, rojo #79231F.

**Quién lo lee.** Casi siempre **el propio Digimon** da los datos en voz
alta mientras sale la ficha ✅. En el doblaje latino lo lee un
**narrador**; Doblaje Wiki cita dos frases suyas (§10.4).

**En Latinoamérica** hubo dos másters de Cloverway: en Fox Kids y
Jetix los nombres del Analyzer iban **en japonés**; en señal abierta,
**en español** ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Digimon:_Digital_Monsters) ⚠️).

### 7.3 La caja de *Digimon World* (PS1, 1999) ✅ (vista y medida)

Fotograma del minuto 2:47 del [gameplay en Internet Archive](https://archive.org/details/digimon-world-play-station-pal-gameplay-full-demostration)
(1280×960):

- rectángulo **azul petróleo translúcido**, fondo **#39464B**;
- **borde fino cian**, más claro que el fondo;
- el **nombre de quien habla en amarillo verdoso**, arriba a la
  izquierda, con una rayita debajo;
- el texto en **blanco**, letra de píxel;
- un icono redondo abajo a la derecha (seguir);
- el personaje pequeño e iluminado **sobre negro total**.

El menú (2:37) es una rejilla verde tipo *wireframe* sobre negro; la
opción activa va en un rectángulo azul oscuro semitransparente.

### 7.4 Otros de la franquicia ✅

- **Reboot 2020**: nombre en blanco sobre una **barra roja** abajo a
  la derecha (nº 6-8 de `fondos_01.jpg`, visto por el redactor).
- ***Digimon Survive*** (2022): **sin caja**. Texto blanco sobre la
  escena, nombre en blanco grueso con una línea fina debajo y una
  flechita ▽ ([captura](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/871980/ss_c893c6fe0bab058e3365e424b92afbebe)).
  Las decisiones van en **pastillas alargadas** con flecha de dirección;
  la de más «Empatía», en **verde claro** ([captura](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/871980/ss_9e339ca540a05de07e53037c54864ed8a)).
- ***Cyber Sleuth***: el nombre de la técnica en un **banner con doble
  filete azul**, arriba al centro (§13).
- **Arte de carta** (nº 37 de `fondos_01.jpg`): caja de narración blanca
  con borde negro, texto japonés y una marca amarilla.

### 7.5 La receta para la lámina

1. **Caja oscura semitransparente** (#39464B o negro con rejilla).
2. **Borde fino de color**: cian (#42B9AC) o el color del Emblema de
   quien habla (§26).
3. **El nombre en una cápsula redondeada de color vivo**, arriba: verde
   (#319F41) como el Analyzer, o amarillo verdoso como *Digimon World*.
4. Texto claro debajo: **Nunito** o **Baloo 2** para leer bien;
   **Press Start 2P** sólo para el nombre o frases muy cortas.
5. Si hay datos (nivel, tipo), **etiqueta rosa** aparte, como el nivel
   del Analyzer.
6. Opcional: el **ticker rojo** en bucle en el borde (Analyzer 2).

### 7.6 Qué NO hacer

- Una burbuja blanca de cómic con cola: no existe en la serie.
- Globos de manga con trama: el manga es otra historia.
- Letra de píxel para párrafos largos: cansa en el celular.

---

## 8 · Los personajes: qué transmiten, su cara y sus dinámicas

Fichas de [AniList](https://anilist.co/anime/552) y de la wiki (wikitext
en inglés y español). La voz se midió con `voz.py` sobre las muestras
latinas oficiales de Doblaje Wiki (registro en Hz, expresividad en
semitonos, velocidad en palabras por segundo).

### 8.1 Tai (Taichi Yagami) — el que se lanza primero

- **Quién es.** El protagonista. **Emblema del Valor**, compañero de
  Agumon, **hermano mayor de Kari** ✅.
- **Carácter.** Enérgico y aventurero. Actúa por impulso y sin medir
  las consecuencias, sobre todo si un amigo está en peligro. Pero
  **admite rápido que se equivocó** y hace lo que sea por arreglarlo.
  Muy protector ([AniList](https://anilist.co/character/1907) ✅).
- **Con quién.** Compañero de clase de Sora desde primero y del club de
  fútbol (wiki en inglés ⚠️ una fuente).
- **Qué transmite.** Valor que a veces se pasa de la raya. El ep. 16 lo
  resume: presiona tanto a Agumon que lo hace digievolucionar mal en
  **SkullGreymon**; luego pide perdón y Koromon lo perdona (wikitext ✅).
- **Cómo habla.** Muy agudo (368 Hz), muy expresivo (23.7 semitonos),
  rápido (3.58 palabras/s). Encaja con su energía.
- **De adulto** (epílogo de *02*): traje y maletín junto a Agumon con
  pajarita (nº 19 de `personajes_01.jpg`).

### 8.2 Agumon — el valiente tranquilo

- **Quién es.** Un dinosaurio pequeño y robusto. **Muy valiente,
  relajado y gracioso** ([AniList](https://anilist.co/character/4950) ✅).
- **Cadena.** Koromon → Agumon → Greymon → MetalGreymon → WarGreymon;
  con MetalGarurumon forma **Omnimon** ✅.
- **Cómo habla.** Muy agudo (337 Hz), 26.6 semitonos. En latino lo
  dobla **Uraz Huerta**, el mismo actor de Matt (§10).
- **Qué transmite.** Confianza sin condiciones: se deja cargar, perdona
  a Tai tras SkullGreymon, lo abraza al despedirse.

### 8.3 Matt (Yamato Ishida) — el solitario que protege

- **Quién es.** **Emblema de la Amistad**, compañero de Gabumon,
  **hermano mayor de T.K.** Sus padres se divorciaron: él vive con su
  padre, Hiroaki; T.K., con su madre, Natsuko ✅.
- **Carácter.** Empieza como un chico solitario, de fachada fría.
  Maduro y reflexivo: piensa antes de actuar (al revés que Tai). Hará lo
  que sea por un amigo y **protege mucho a T.K.** Tiende a la
  autocrítica ([AniList](https://anilist.co/character/1909) ✅).
- **Su objeto.** La **armónica** (§22).
- **Arco.** Choca con Tai por el liderazgo. En el arco de los Amos
  Oscuros se pone contra Sora (ep. 43), Gabumon le muerde la pierna
  para que deje de compararse con Tai (ep. 44) y se encierra en una
  cueva oscura creyendo que Tai es mejor hermano para T.K. (ep. 51).
  Sale de ahí con Gabumon: se prometen ser amigos para siempre
  (wikitext ✅). En el epílogo se casa con Sora ✅.
- **Cómo habla.** Agudo (307 Hz), **el más rápido** (3.92 palabras/s).
  Sus frases latinas retratan su carácter: «Tú jamás entenderás cómo me
  siento» (§10).
- **Qué transmite.** Perseverar en silencio. Una fan chilena con cáncer
  le escribió a Uraz Huerta que Matt la ayudó a superarlo
  ([El Universal](https://www.eluniversal.com.mx/espectaculos/magia-de-digimon-toca-sus-actores/) ✅).
- **De adulto:** **astronauta**, con Gabumon en traje espacial (nº 23).

### 8.4 Gabumon — el leal hasta el extremo

- **Quién es.** Un Digimon de piel amarilla, con aspecto de lobo, de
  unos 75 cm (2,5 pies), con un cuerno y cola; lleva encima un **pelaje
  azul** como de perro ([AniList](https://anilist.co/character/9952) ✅).
- **Cadena.** Tsunomon → Gabumon → Garurumon → WereGarurumon →
  MetalGarurumon; con WarGreymon, Omnimon ✅.
- **Carácter.** Fiel sin condiciones. Cuando Matt quiere estar solo, le
  dice: «Está bien, haré lo que me pides… siempre y cuando sea tu deseo,
  Matt» (muestra oficial ✅). Pero también le planta cara: le muerde
  (ep. 44).
- **Cómo habla.** Muy agudo (351 Hz), **el menos expresivo** (16.6
  semitonos): sobrio y contenido. Lo dobla **Circe Luna**, la voz de Sora.
- **Popularidad.** 7.º en la encuesta oficial de compañeros. La propia
  Toei comenta que **no comparte la popularidad de Matt** (§9).

### 8.5 Sora Takenouchi — la que cuida de todos

- **Quién es.** **Emblema del Amor**, compañera de Piyomon (Biyomon en
  el doblaje). Su padre es profesor en la Universidad de Kioto; vive con
  su madre, que tiene una **floristería**. De niña vivió en Hikarigaoka
  y en 1995 vio la pelea de Greymon contra Parrotmon ([AniList](https://anilist.co/character/2276) ✅).
- **Carácter.** Muy fiable; cuida de los demás **como una madre** ✅.
- **Arco.** En el ep. 26 se esconde del grupo; luego se niega a soltar
  a Biyomon ante Myotismon. En el ep. 51 la misma oscuridad que atrapó a
  Matt la alcanza a ella (wikitext ✅).
- **Cómo habla.** Agudo (320 Hz), **la más expresiva** (28.6
  semitonos), velocidad normal. Tono cálido y protector.

### 8.6 Su cara en cada emoción ⚠️ (19 de 25 con fotograma y minuto)

Vistos de verdad fotograma a fotograma con `ffmpeg` sobre IA-C
(minutos del episodio; enlaces con `?t=` en §2 y en `referencias.json`).

| | Alegría | Rabia | Tristeza | Miedo | Vergüenza |
|---|---|---|---|---|---|
| **Tai** | ep. 54, 14:00 ✅ | ep. 16, 7:50 ✅ | ep. 16, 19:40 ✅ | ep. 1, 9:16 ✅ | ep. 16, 19:40 (culpa) ✅ |
| **Agumon** | ep. 54, 14:00 ✅ | **falta** | **falta** | ep. 1, 5:20 (como Koromon) ✅ | ep. 16, 19:00 (como Koromon) ✅ |
| **Matt** | **falta** | ep. 44, 14:15 ✅ (y ep. 43, 18:45) | ep. 54, 13:28 ✅ | ep. 51, 7:00 ✅ | ep. 51, 5:25 ✅ |
| **Gabumon** | ep. 51, 9:00 ⚠️ (plano general del abrazo) | ep. 44, 14:40 ✅ | **falta** | ep. 51, 6:35 ✅ | **falta** |
| **Sora** | ep. 1, 11:46 ✅ | ep. 26, 16:25 ✅ | ep. 54, 14:28-14:48 ✅ | ep. 51, 14:30 ✅ | ep. 26, 10:56 ✅ |

**Lo que falta, con lo que se buscó** (el investigador de voz agotó
sus 2 tandas):

- **Matt, alegría**: revisados enteros los eps. 43, 44 y 51, y el 54
  del minuto 0 al 18. Siempre sale serio, tenso o triste. Pendiente: ep.
  52 o ep. 25 («Princess Karaoke»). **Mientras tanto, sin minuto**: la
  sonrisa del nº 32 de `personajes_01.jpg` y la media sonrisa del
  tráiler de *tri.* ([x5zbgmg](https://www.dailymotion.com/video/x5zbgmg), 0:30).
- **Gabumon, tristeza y vergüenza**: buscado en los eps. 44 y 51
  enteros, sin plano limpio. Su alegría queda ⚠️ porque es un plano
  general del abrazo, no de su cara.
- **Agumon, rabia y tristeza**: en esta copia de Saban la pelea contra
  Kuwagamon del ep. 1 queda **tapada por un rótulo del doblaje** justo
  en esos segundos. Pendiente: ep. 2 («The Birth of Greymon»). **Mientras
  tanto**: de perfil con los colmillos a la vista, alerta
  ([x405gc9](https://www.dailymotion.com/video/x405gc9), 0:45), que es
  tensión de pelea, no rabia.

### 8.7 Los secundarios más queridos (sólo ficha)

- **Kari (Hikari Yagami)**: dulce, inocente y alegre; ve lo mejor de
  cada uno; no pelea, pero se pone seria cuando hace falta. **Emblema de
  la Luz**, compañera de Gatomon. Llega en el arco de Myotismon. Su
  objeto: el **silbato**. **1.ª en la encuesta oficial** ✅.
- **T.K. (Takeru Takaishi)**: alegre y amable; no soporta ver a nadie
  pelear. Esperanza, Patamon (**el compañero más votado**) ✅.
- **Izzy (Koushiro Izumi)**: experto en ordenadores, siempre con su
  portátil «PiBook». Conocimiento, Tentomon ✅.
- **Mimi**: parece mimada; en el fondo, dulce y sensible. Palmon ✅.
- **Joe (Jou Kido)**: el mayor; nervioso por su sentido de la
  responsabilidad. Gomamon. En latino le dicen **«Superior Joe»** ✅.
- **El Narrador** (Hiroaki Hirata) tiene **2232 favoritos en AniList**,
  más que ningún niño. Dato curioso, sin imagen.

### 8.8 Dinámicas para láminas en grupo ✅

| Pareja | Cómo es | Para qué lámina |
|---|---|---|
| **Tai y Matt** | chocan por el liderazgo y acaban siendo mejores amigos; en *tri.*, Tai le pega. El fandom la compara con Yugi y Kaiba ([Reddit](https://www.reddit.com/r/digimon/comments/1dr90ze/which_anime_rivalry_do_you_think_is_more_iconic/), 198 votos ⚠️) | discutir con respeto |
| **Matt y Gabumon** | lealtad total, pero Gabumon lo muerde si hace falta | apoyo sincero |
| **Tai y Agumon** | presión y perdón (ep. 16); el abrazo de la despedida | aprender del error |
| **Matt y T.K.** | lo protege; teme perderlo: «Pensé que él me quitaría a mi hermano menor» | cuidar al nuevo |
| **Tai y Kari** | hermanos; el fandom los ve icónicos ([Reddit](https://www.reddit.com/r/digimon/comments/15fjbft/what_makes_tai_and_karis_sibling_relationship_to/), 159 votos ⚠️) | familia |
| **Sora y Mimi** | Sora la cuida: «Después de todo, eres una buena niña, Mimi» | animar |
| **Matt y Sora** | él se pone contra ella (ep. 43); de adultos, casados | reconciliarse |

---

## 9 · ¿Quién es el más querido?

### 9.1 Los números

| Fuente | Resultado |
|---|---|
| [**Encuesta oficial de Toei**](https://www.toei-anim.co.jp/tv/dejimon/ranking/result29.html), «¿Quién te gusta más de los niños elegidos?» (+3000 votos, hacia 2001) | **1.ª Kari 969**, **2.º Matt 662**, 3.º T.K. 563, 4.º Ken 546, **5.º Tai 366**, 6.º Davis 186, 7.º Izzy, **8.ª Sora**, 9.º Joe ✅ |
| [**Encuesta oficial de Toei**](https://www.toei-anim.co.jp/tv/dejimon/ranking/result30.html), «¿Qué compañero te gusta más?» (2267 votos) | **1.º Patamon 335**, 2.º Gatomon 272, **5.º Agumon 146**, **7.º Gabumon 108** ✅ |
| [AniList](https://anilist.co/anime/552), favoritos | Narrador 2232, **Tai 435**, **Matt 297**, Kari 292, **Agumon 239**, Mimi 229, Gatomon 218, T.K. 193, Izzy 185, **Sora 165**, **Gabumon 161** ✅ |
| [Danbooru](https://danbooru.donmai.us/posts?tags=digimon_adventure), dibujos de fans (2430) | Angewomon 1246, **Kari 1035**, **Tai 959**, Gatomon 809, **Agumon 770**, Mimi 652, T.K. 548, Omnimon 522, **Matt 507**, Patamon 502, **Sora 497**, **Gabumon 439** ✅ |

### 9.2 Qué significa para la lámina

- **El protagonista no es el favorito.** En Japón gana Kari y Matt
  supera a Tai. En AniList y en dibujos, Tai va por delante de Matt.
  Dos fuentes (Toei y Danbooru) coinciden en que **Kari y Gatomon
  superan a Tai y Agumon** ✅.
- Toei lo comentó con humor: Kari **«les gana por mucho»** a los
  hermanos Ishida ✅.
- **Decisión:** el concepto recomendado lo protagoniza **Matt**, el más
  querido de los cinco del encargo en la encuesta oficial, con Gabumon.
  Tai lleva el concepto B (el favorito en AniList y en dibujos). Kari
  no está en el encargo: se deja para una lámina 2 (§27).
- No hay encuesta latinoamericana en las partes ⚠️.

---

## 10 · Doblaje latino y frases textuales

### 10.1 La ficha ✅

Del wikitext de [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Digimon:_Digital_Monsters)
(API `action=parse`):

- Título: ***Digimon: Digital Monsters***. Estudio **Intertrack**
  (México), 1999-2000, 54 episodios.
- Dirección: **Gloria Rocha** (ep. 1-9) y **Alma Moreno** (ep. 10-54).
  Traducción: Brenda Nava. Adaptación musical: Israel Magaña. Dirección
  musical: Oliver Magaña. Mezcla: Arturo Vélez.
- Se dobló **desde el japonés**, pero con algunos nombres y los logos
  de la versión de Saban.
- Tres másters: **Cloverway V1** (2000, opening y primer ending en
  español; Fox Kids, Jetix y Crunchyroll), **Cloverway V2** (2001, más
  textos en español; señal abierta) y **Toei 2021** (desde los Blu-ray
  japoneses).

### 10.2 Quién dobla a cada uno

| Personaje | Voz japonesa | Voz latina | Verificación |
|---|---|---|---|
| **Tai** | Toshiko Fujita | **Miguel Ángel Leal** (ep. 1-9) → **Gerardo Meza** (ep. 13-54) | ✅ Doblaje Wiki + [El Universal](https://www.eluniversal.com.mx/espectaculos/magia-de-digimon-toca-sus-actores/) |
| **Matt** | Yūto Kazama | **Uraz Huerta** | ✅ Doblaje Wiki + [Toei Animation LA](https://x.com/ToeiAnimationLA/status/1796360947251982648) + [ANN](https://www.animenewsnetwork.com/encyclopedia/people.php?id=23450) |
| **Sora** | Yūko Mizutani | **Circe Luna** | ✅ Doblaje Wiki + [AnimeArgentina](https://animeargentina.net/circe-luna-doblaje/) + El Universal |
| **Agumon** | Chika Sakamoto | **Uraz Huerta** | ✅ Doblaje Wiki + Toei Animation LA + ANN |
| **Gabumon** | Mayumi Yamaguchi | **Circe Luna** | ✅ Doblaje Wiki + AnimeArgentina |
| Izzy | Umi Tenjin | Mónica Estrada | ⚠️ sólo Doblaje Wiki |
| Mimi | Ai Maeda | Isabel Martiñón | ⚠️ |
| Joe | Masami Kikuchi | Víctor Ugarte | ⚠️ |
| T.K. | Hiroko Konishi | Lupita Leal | ⚠️ |
| Kari | Kae Araki | Cristina Hernández | ⚠️ |
| Greymon, MetalGreymon, WarGreymon | — | Héctor Moreno | ⚠️ |
| Garurumon | — | Enrique del Olmo (ep. 3 y 5) → Marco Guerrero (ep. 8-54) | ⚠️ Doblaje Wiki corrige a ANN, que acreditó a «Emilio Guerrero» |
| Devimon | Kaneto Shiozawa | Gerardo Reyero | ⚠️ |
| Myotismon | Ryūzaburō Ōtomo | Roberto Mendiola | ⚠️ |
| Etemon | Yasunori Masutani | José Arenas | ⚠️ |

⚠️ Tai en los episodios 10-12: las partes no dicen quién lo dobló.
AniList pone a **Blanca Rada** como voz «Spanish» de Tai: es de
**España**, no del doblaje latino.

### 10.3 Lo que un fan del doblaje sabe ✅

- **Cada actor dobló a un niño y al Digimon de otro niño** (salvo
  Cristina Hernández). Gloria Rocha les pidió **elegir su Digimon**;
  **Circe Luna eligió la primera: Gabumon**. Por eso Circe Luna es Sora
  y Gabumon, y Uraz Huerta es Matt y Agumon (Doblaje Wiki, contado por
  Circe Luna en Toonlandya y en el foro Pikaflash ✅, cuadra con el
  reparto).
- **Grababan juntos en el atril**, primero los niños y luego los
  Digimon; todos menos Gerardo Meza (Doblaje Wiki ⚠️).
- Víctor Ugarte y Cristina Hernández son los únicos que doblan a su
  Digimon **en todas sus etapas** (Doblaje Wiki ⚠️).
- **Gerardo Meza** estuvo **15 años retirado** y volvió para *Last
  Evolution Kizuna* (2020): «mucha emoción, mucha felicidad pero a la
  vez… muy nervioso» (El Universal ✅).
- **Circe Luna** dirigió el doblaje de *Kizuna* (AnimeArgentina ⚠️).
- Detalles de pronunciación: la terminación **«-món»** con tilde se usa
  en toda la serie, salvo en algunos de los 12 primeros episodios; en
  el ep. 5 Matt dice **«Teká»** en vez de «Tikei» (Doblaje Wiki ⚠️).

### 10.4 Frases textuales, con su audio ✅

Oídas con `voz.py` (Whisper en local) sobre las **muestras oficiales**
de Doblaje Wiki. Los nombres propios se corrigieron a oído (Whisper
escribió «coromona», «Mati», «Tikei»). El minuto es **de la muestra**:
las partes **no dicen de qué episodio** es cada una ⚠️.

| Quién (actor) | Frase | Minuto de la muestra |
|---|---|---|
| **Tai** (Gerardo Meza), [audio](https://static.wikia.nocookie.net/doblaje/images/9/9a/Digimon-_Digital_Monsters.ogg) | «¡Juntos lo logramos!» | 0:05 |
| | «Esta cosa tuvo la culpa de mandarme al otro mundo» | 0:12 |
| | «Este Digibus no es útil, no sirve para nada» | 0:14 |
| **Sora** (Circe Luna) | «¡Vamos, huyan de aquí cuanto antes!» | 0:04 |
| | «¡Por supuesto que sí! ¡Tú eres una de mis mejores amigas!» | 0:10 |
| | «Después de todo, eres una buena niña, Mimi» | 0:14 |
| **Matt** (Uraz Huerta) | «Tú jamás entenderás cómo me siento» | 0:00 |
| | «Pensé que él me quitaría a mi hermano menor» | 0:06 |
| | «Tai es un niño muy decidido y también tiene la habilidad para ser un líder» | 0:08 |
| **Agumon** (Uraz Huerta) | «Lo que pasa es que digievolucionamos, yo cambié de Koromon a lo que soy ahora, soy Agumon» | — |
| **Gabumon** (Circe Luna) | «Además, yo no sabría qué hacer en este Digimundo si tú no estás a mi lado» | 0:18 |
| | «¿De verdad quieres estar solo?» | 0:27 |
| | «Está bien, haré lo que me pides… siempre y cuando sea tu deseo, Matt» | 0:30 |

Las de Gabumon son del momento en que Matt se aparta del grupo.

**Frases del narrador** que cita Doblaje Wiki (⚠️ una fuente; la wiki
las cita como errores de traducción, pero son textuales):

- Ep. 3, ante los Monochromon: «Pertenece a la familia de los
  dinosaurios».
- Ep. 3, cuando ataca Seadramon: «Seadramon es un Digimon adulto. Su
  apariencia es muy parecida a la de un dinosaurio».
- Al final del ep. 2, el narrador llama a los Digimon **«animales»**.
- Ataque de MetalGreymon en latino: **«Gigas Destructoras»** (en el
  ep. 20, una vez, «Giga Blasters»).

⚠️ **No hay clip oficial doblado con minuto**: YouTube pidió iniciar
sesión y Crunchyroll no se puede usar. El vídeo de Dailymotion
«[Digimon Adventure 01 - Opening Latino](https://www.dailymotion.com/video/x61sy9p)»
**no está doblado**: es el opening japonés con la letra encima
(comprobado por la parte de vídeo).

---

## 11 · Música y sonido

### 11.1 Opening y ending ✅

| Tema | Voz | Letra y música | Fuente |
|---|---|---|---|
| **Opening «Butter-Fly»** | **Kouji Wada** (和田光司) | letra y música **Hidenori Chiwata** (千綿偉功); arreglos Cheru Watanabe (渡部チェル) | cartela del [opening en Dailymotion](https://www.dailymotion.com/video/x6cdxot), 0:43, cruzada con la wiki ✅; [single de 1999 en Internet Archive](https://archive.org/details/butter-fly-digimon-single) ✅ |
| **Ending «I wish»** | **Ai Maeda** (前田愛, la voz japonesa de Mimi) | letra Noriko Miura; música Haruhisa Shirakawa; arreglos Katsumi Horii | misma cartela ✅ |
| **Ending latino** | **Marisa de Lille** | título «**Tengo la Fé**» ⚠️ (sólo la cartela del [vídeo](https://www.dailymotion.com/video/x3342x6), 0:05) | cantante ✅ (cartela + Doblaje Wiki: en el ep. 25 Mimi canta «I Wish» con la voz de Marisa de Lille) |

«Butter-Fly» vuelve en *tri.* y en *Kizuna*. El opening latino existe
(Cloverway V1), pero **las partes no dan su título ni su cantante** ⚠️.
Los covers de fans lo llaman «Si Tú Lo Deseas» (§23).

### 11.2 Lo que suena en las escenas clave

- **En la despedida** (ep. 54) suena **«Butter-Fly»** cantada por
  Kouji Wada. En el doblaje latino **se dejó en japonés**, igual que el
  tema de inserto **«Brave Heart»** y una versión de «Butter-Fly» al
  piano: el cliente sólo pidió doblar el opening y el primer ending
  (Doblaje Wiki ⚠️ una fuente).
- Los **avances** del siguiente episodio usan «Butter-Fly» instrumental
  (Doblaje Wiki ⚠️).
- **Mundo Digital tranquilo**: cuerdas suaves y un coro casi de cuna
  (IA-V1, 20:00). **Peleas**: percusión tribal y metales (IA-V1, 38:00)
  ⚠️ oído, sin nombre de pista.
- ***tri.*, la pelea Tai-Matt**: cuerdas graves, sin melodía y sin
  batería; conflicto emocional, no acción ([x5zbgmg](https://www.dailymotion.com/video/x5zbgmg), 0:54) ⚠️.
- **Banda sonora en inglés** (Saban): [Internet Archive](https://archive.org/details/digimon-digital-monsters-the-original-english-soundtrack);
  discos en [MusicBrainz](https://musicbrainz.org/release-group/bccfa5df-a909-4dbe-abc2-ce83d567c6de) (2000).

### 11.3 Efectos que todos reconocen ✅ (oídos)

- El **brillo de la digievolución**: tono que sube, como campanas, con
  coro (IA-V1, 38:00).
- El **grito con el nombre** de la evolución: «¡Greymon!».
- El verbo del doblaje es **«digievolucionar»** (Agumon, en su muestra:
  «digievolucionamos»). La fórmula completa de cada evolución en latino
  **no está en las partes** ⚠️: en el ep. 20, para MetalGreymon,
  Doblaje Wiki cita «Greymon Super Digivolves a…», frente al «Ultra
  Digivolves a…» de las demás evoluciones a nivel perfeccionado (así lo
  escribe la wiki).
- En comerciales de juguetes de 2001-2002 sonó un **«Digi-Rap» en
  español**, que la serie nunca usó (Doblaje Wiki ⚠️).

---

## 12 · Vídeos y tendencias

### 12.1 Mirados de verdad (`fotogramas.py`, `ffmpeg`)

| Vídeo | Duración | Lo que sirve, con minuto |
|---|---|---|
| [Opening japonés «Butter-Fly»](https://www.dailymotion.com/video/x6cdxot) | 1:36 | créditos 0:43; Tai con el puño en alto junto a Greymon 0:58; los compañeros en fila 1:30 |
| [Tráiler de reparto de *tri.* cap. 1 «Saikai»](https://www.dailymotion.com/video/x8x2nx4) (otra copia: [x88ob2a](https://www.dailymotion.com/video/x88ob2a)) | 4:04 | cartelas de nombre con cada *seiyū*, 1:24-2:08 |
| [Tráiler de *tri.* caps. 2-3 «Ketsui» y «Kokuhaku»](https://www.dailymotion.com/video/x3rmlro) | 2:37 | Tai alarmado 0:08; Tokio de noche 0:42; Sora preocupada 1:00; estreno 12-mar-2016 en pantalla, 2:04 |
| [Tráiler de *tri.* cap. 5 «Kyōsei»](https://www.dailymotion.com/video/x5zbgmg) | 1:20 | Agumon de cerca 0:18; Sora 0:27; Matt de perfil 0:30; Gabumon de pesadilla 0:39; Matt grita 0:45; **Tai golpea a Matt 0:54**; estreno 30-sep-2017 en pantalla, 1:03 |
| [«Agumon y Gabumon Warp digievolucionan»](https://www.dailymotion.com/video/x405gc9) (fans, metraje de *02*) | 7:08 | Matt serio 0:15; Agumon y Gabumon alerta 0:45; ficha del Analyzer de MetalGarurumon 2:30; Sora con casco de bici 4:45 ⚠️ canal de fans |
| [Ending latino completo](https://www.dailymotion.com/video/x3342x6) | 4:02 | cartela con la cantante 0:05; imagen fija de fans, pero el audio es el ending oficial |
| IA-V1 y 8 episodios de IA-C | — | todo el §2 y el §8.6 |
| [Gameplay de *Digimon World*](https://archive.org/details/digimon-world-play-station-pal-gameplay-full-demostration) | — | menú 2:37; caja de diálogo 2:47; pantalla de nombre 3:15-3:51 |

### 12.2 Otros útiles, sin mirar

- [Tráiler de la película de 1999](https://www.dailymotion.com/video/x93qmh2) (JustWatch, 1:21).
- [Tráiler en español de *Last Evolution Kizuna*](https://www.dailymotion.com/video/x7x75gz) (HobbyConsolas, 1:30, 2493 vistas).
- [Tráiler en español de *02: The Beginning*](https://www.dailymotion.com/video/x8pwwkp) (FilmAffinity).
- [Tráiler de *tri.* en YouTube, en 1080p](https://www.youtube.com/watch?v=JOK5aPOeo2I): existe, pero la descarga dio 403.
- [«Digivolving Greymon Review»](https://www.dailymotion.com/video/x8lv6xh) (5:20): el único análisis que salió; no se miró ⚠️.
- **Descartado**: «[Digimon Adventure 02 (Analizador)](https://www.dailymotion.com/video/x63wsqe)» no es un análisis: son fichas de decenas de Digimon con el texto espejado.

### 12.3 Tendencias ⚠️

- TikTok en español: **«esta será la última digievolución»** y el chiste
  «digievoluciono al saltar cuando cumplo 30 años»
  ([etiqueta](https://www.tiktok.com/discover/esta-sera-la-ultima-digievolucion-2024)).
  Sólo se abrió la página de la etiqueta: **sin vídeo concreto, sin
  vistas y sin autor**.
- Reddit: la rivalidad Tai-Matt (198 votos) y los hermanos Tai y Kari
  (159 votos) (§8.8).

---

## 13 · Videojuegos de la franquicia

- **Steam no encuentra «Digimon Adventure»** (el juego de PS1 no está);
  con «Digimon» salen 10 juegos ✅.

| Juego | Año y plataforma | Interfaz y cajas | En español |
|---|---|---|---|
| ***Digimon World*** | 1999, PS1, Bandai | **caja azul petróleo #39464B** con borde cian, nombre amarillo verdoso, texto blanco en píxel; menú en rejilla verde; teclado en pantalla para poner nombre a ti y a tu Digimon (§7.3) ✅ visto | no |
| [***Digimon Story: Cyber Sleuth***](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1042550/ss_b85abb30e749ea91b3f3827b895e0cea) | 2015 (PC 2019), Bandai Namco | HUD holográfico cian: #182B49 33%, #6B799B, #72B0D5, #CBE1F3, #1C5AA3. Técnica en banner con doble filete; fichas con icono redondo y barras verdes y cian en marco con esquinas en bisel; turnos en cápsulas | no (inglés, alemán, japonés, coreano, chino) |
| [***Digimon World: Next Order***](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1530160/ss_fe455bbe5e3d876be318b7941a0e90ad) | 2016, Bandai Namco | arena de **baldosas hexagonales**; barras de vida flotantes con una letra (R, L, LY), sin caja. Gris pizarra #8A8A8F, #9F989B, celeste #D7E9F1 | **sí, latino** |
| [***Digimon Survive***](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/871980/ss_c893c6fe0bab058e3365e424b92afbebe) | 2022, Bandai Namco / Witch Craft | texto sin caja; decisiones en pastillas (§7.4) | **sí, latino** |
| [***Digimon Story: Time Stranger***](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1984270/ss_e119215706a1b0469c756c0ec2148d09) | 2025, Bandai Namco | Shinjuku y el Mundo Digital flotando sobre el mar; HUD **verde neón** con círculos de mira | **sí, latino** |

Idiomas leídos en `store.steampowered.com/api/appdetails` ✅. También
hay renders de *Digimon Adventure* para el juego *Re:Digitize* (§3).

- El **Digimon Analyzer** es, en el anime, la pantalla de estadísticas
  de un juego de rol: la serie nació de un **juguete** (mascota virtual)
  antes que del anime (§26).
- ⚠️ **The Cutting Room Floor** ([tcrf.net/Digimon_World](https://tcrf.net/Digimon_World))
  dio 403 (Cloudflare) por la API y por la página, y la copia en
  [Wayback Machine](http://web.archive.org/web/2023/https://tcrf.net/Digimon_World)
  cortó la conexión. Sin textos de betas.

---

## 14 · Lo que ama el fandom, y qué NO hacer

### 14.1 Lo que todo fan reconoce ✅

- **Las goggles de Tai**: la seña del líder. Después de *Adventure*,
  casi todos los protagonistas de Digimon las llevan ([wiki: Goggles](https://digimon.fandom.com/wiki/Goggles) ✅).
- **La despedida del ep. 54**: la armónica de Matt, el silbato de Kari,
  Mimi corriendo tras el tren para decirle adiós a Palmon (LEVEL UP ✅).
- **La rivalidad Tai-Matt** (Reddit ⚠️).
- **La digievolución**: destello, nombre gritado, campanas (§11.3).
- **Los Emblemas y las Etiquetas** colgadas al cuello (§26).
- En latino: **«Superior Joe»**, la tilde de **«-món»**, el Digimundo.

### 14.2 Qué NO hacer ✅

1. **Tai sin goggles.** Es su símbolo, más que el pelo.
2. **Tratar a Agumon y Gabumon como mascotas.** Son compañeros con
   voluntad propia: Gabumon muerde a Matt para hacerle entrar en razón.
3. **Mezclar épocas.** El diseño de 1999 (11 años en Japón, **12 en el
   doblaje latino**) no es el de *tri.* (17 años, uniforme escolar)
   ([wiki en español](https://digimon.fandom.com/es/wiki/Yamato_Ishida) ✅).
4. **Poner a Tai y Matt como amigos sin más** en una escena de tensión:
   su amistad sale de chocar.
5. **Sacar Digivices o criaturas de otras series** (App Drive, Fusion
   Loader, Terriermon): un fan lo nota enseguida (§3).
6. **Una burbuja blanca de cómic** (§7.6).
7. **Colores pastel**: el diseñador quería colores vivos y nítidos (§19).
8. Dibujar a Sora sin su **gorro azul**, o a Matt con otra ropa que la
   **camiseta verde de cuello alto** si la lámina es de 1999 (§16).

No se pudo leer la página de memes de TV Tropes (403) ⚠️.

---

## 15 · Poses analizadas por personaje

Vistas en fotogramas (IA-V1 o los enlaces de Dailymotion) o en arte
oficial. Minuto y para qué sirve cada una.

### 15.1 Tai (9)

| # | Pose | Dónde | Sirve para |
|---|---|---|---|
| 1 | **puño en alto** junto a Greymon, mirando arriba | [opening](https://www.dailymotion.com/video/x6cdxot), 0:58 | celebrar |
| 2 | **carga a Agumon en brazos**, sonrisa, caminando | IA-V1, 20:00 | animar, cariño |
| 3 | **al teléfono público**, aprieta el botón | IA-V1, 30:00 | explicar, pedir ayuda (concepto B) |
| 4 | **enseña un pez** sobre la fogata, orgulloso | IA-V1, 48:00 | presentar un logro |
| 5 | primer plano de perfil **con las goggles puestas**, serio | IA-V1, 43:20 | pensar, decidir |
| 6 | de pie con el grupo, brazos a los lados | IA-V1, 11:30 | presentar en grupo |
| 7 | mira por encima del hombro, alarmado (uniforme) | [x3rmlro](https://www.dailymotion.com/video/x3rmlro), 0:08 | alertar |
| 8 | **lanza un puñetazo** contra Matt | [x5zbgmg](https://www.dailymotion.com/video/x5zbgmg), 0:54 | regañar, confrontar |
| 9 | retrato con su cartela 八神太一, decidido | [x8x2nx4](https://www.dailymotion.com/video/x8x2nx4), 2:04-2:08 | presentar |

Y en arte: puño en alto de cuerpo entero (nº 30 de `personajes_01.jpg`).

### 15.2 Agumon (6)

| # | Pose | Dónde | Sirve para |
|---|---|---|---|
| 1 | en fila con los demás compañeros, sonrisa tranquila | [opening](https://www.dailymotion.com/video/x6cdxot), 1:30 | presentar |
| 2 | en brazos de Tai, relajado y feliz | IA-V1, 20:00 | animar |
| 3 | asomado junto a Tai en la cabina, ceño un poco fruncido, esperando | IA-V1, 30:00 | acompañar, impaciencia (concepto B) |
| 4 | primer plano apoyado en el brazo de Tai, ojo verde grande, curioso | [x5zbgmg](https://www.dailymotion.com/video/x5zbgmg), 0:18 | observar, pensar |
| 5 | de perfil junto a Gabumon, colmillos a la vista, alerta | [x405gc9](https://www.dailymotion.com/video/x405gc9), 0:45 | prepararse |
| 6 | envuelto en luz blanca antes de ser Greymon | IA-V1, 38:20 | transformarse |

### 15.3 Matt (8)

| # | Pose | Dónde | Sirve para |
|---|---|---|---|
| 1 | retrato con su cartela 石田ヤマト, serio, mirando de lado | [x8x2nx4](https://www.dailymotion.com/video/x8x2nx4), 2:00 | presentar |
| 2 | **de perfil con media sonrisa**, luz cálida de fuego o atardecer | [x5zbgmg](https://www.dailymotion.com/video/x5zbgmg), 0:30 | reflexionar con seguridad |
| 3 | grita con la boca muy abierta, pantalla partida con Tai | x5zbgmg, 0:45 | alertar |
| 4 | recibe el puñetazo, cabeza atrás | x5zbgmg, 0:54 | reaccionar |
| 5 | **junto a la fogata, brazos atrás**, escéptico | IA-V1, 48:00 | escuchar, dudar |
| 6 | con el grupo, distante, serio | IA-V1, 11:30 | reservado |
| 7 | primer plano con el ceño fruncido (*02*) | [x405gc9](https://www.dailymotion.com/video/x405gc9), 0:15 | concentrarse |
| 8 | sobre la espada de Omegamon junto a Tai, mirando arriba | key visual «Reunión» (nº 3 de `fondos_01.jpg`) | asombro, decisión |

Y en 3D: **figura de Matt con Gabumon a la espalda**, 5 ángulos (§4.2).

### 15.4 Gabumon (6) ⚠️ el más flojo

En más de 20 minutos de vídeo casi siempre sale **detrás de Matt o en
grupo**.

| # | Pose | Dónde | Sirve para |
|---|---|---|---|
| 1 | asoma en la fila de compañeros, detrás de Patamon | [opening](https://www.dailymotion.com/video/x6cdxot), 1:30 | presentar en grupo |
| 2 | primer plano de **pesadilla**, colmillos, ojo muy abierto | [x5zbgmg](https://www.dailymotion.com/video/x5zbgmg), 0:39 | ⚠️ versión distorsionada, no su aspecto normal |
| 3 | de perfil junto a Agumon, alerta | [x405gc9](https://www.dailymotion.com/video/x405gc9), 0:45 | prepararse |
| 4 | ya como Garurumon, sale de la nieve | IA-V1, 58:10 | atacar |
| 5 | retrato oficial de pie, tres cuartos, alerta | [AniList](https://s4.anilist.co/file/anilistcdn/character/large/b9952-mI01ix3dEKMp.png) | presentar |
| 6 | la misma pose en la hoja de modelo de la wiki | [Gabumon_b](https://static.wikia.nocookie.net/digimon/images/d/d1/Gabumon_b.jpg) | confirma colores |

Más: **muerde a Matt** (ep. 44, 14:40) y **abrazado a Matt** (ep. 51,
9:00), del §8.6.

### 15.5 Sora (6)

| # | Pose | Dónde | Sirve para |
|---|---|---|---|
| 1 | retrato con su cartela 武之内空, sonrisa suave | [x8x2nx4](https://www.dailymotion.com/video/x8x2nx4), 1:52-1:56 | presentar |
| 2 | primer plano preocupado, en interior | [x3rmlro](https://www.dailymotion.com/video/x3rmlro), 1:00 | preocuparse |
| 3 | de perfil con casco de bici, mirando arriba, boca abierta | [x405gc9](https://www.dailymotion.com/video/x405gc9), 4:45 | alertar |
| 4 | con el grupo, gorro puesto, tranquila y segura | IA-V1, 11:30 | serenidad |
| 5 | medio rostro junto a Tai, en un pasillo | [x5zbgmg](https://www.dailymotion.com/video/x5zbgmg), 0:27 | ⚠️ recortada |
| 6 | cuerpo entero de *Re:Digitize*, guantes rojos en alto | nº 29 de `personajes_01.jpg` | presentar entera |

### 15.6 Qué pose para qué

| Para… | La mejor |
|---|---|
| presentar | Tai 9 o Matt 1 (cartela), Sora 6 |
| explicar | **Tai 3** (al teléfono) |
| celebrar | **Tai 1** (puño en alto) |
| regañar | Tai 8; Gabumon mordiendo (ep. 44) |
| pensar | Tai 5, **Matt 2**, Agumon 4 |
| animar | **Tai 2** con Agumon en brazos |

---

## 16 · Vestuario, con hex medidos

Hex medidos con `estilo.py` sobre los retratos de AniList (con su % de
área). **La ropa la corrigió el redactor mirando las hojas** (§28): la
parte de imagen describía otra.

| Personaje | Ropa icónica de 1999 | Colores medidos | Lo que nunca falta |
|---|---|---|---|
| **Tai** | **camisa azul de manga corta** con una **estrella naranja** y ribetes amarillos; **pantalón corto marrón**; **guantes blancos**; muñequera oscura; **goggles** en la frente con correa azul (nº 30; Danbooru `blue_shirt`, `brown_shorts`, `white_gloves`, `blue_headband`, `star_print`) | **#1951A9** azul 25% · #DB8F51 piel y naranja 17% · #C1CA4F 14% | goggles, Digivice |
| **Matt** | **camiseta verde sin mangas de cuello alto**, vaqueros azules, zapatos marrones (nº 32 de `personajes_01.jpg` y la figura de Flickr, §4.2) | ⚠️ **sin medir**: el único fotograma medido era de noche (#0C1A25, #16373E, luz azul de la escena) | armónica, Digivice |
| **Sora** | **gorro azul** con cintas, **top amarillo sin mangas**, **guantes rojos**, **vaqueros** (nº 29; Danbooru `helmet`, `yellow_shirt`, `sleeveless_shirt`, `red_gloves`, `jeans`) | #6693FA cielo 22% · #F8BC95 piel 18% · #99DFFC 18% · **#EBD639** amarillo 9% | el gorro |
| **Agumon** | escamas naranjas, panza clara, ojos verdes (Danbooru `orange_scales`, `green_eyes`) | **#F8AE02** naranja 31% · #FFFFFE blanco 44% · #2D2C1C línea 4% | garras, dientes |
| **Gabumon** | pelaje azul con franjas blancas encima, piel amarilla debajo, **un cuerno**, cinturones (Danbooru `blue_fur`, `yellow_skin`, `single_horn`, `belt`) | #E5E8F3 19% · **#DED74F** amarillo 13% · #4D4967 línea 13% · #A76177 boca 5% | el cuerno |

### 16.1 Por época ✅ (vistas en las hojas)

- **1999**: la de arriba. Es la que se repite en el arte promocional
  de 1999 a 2020: **si sólo hay un traje, es éste**.
- ***02*, verano** (nº 35-39): más ligera y de colores vivos. Sora con
  camiseta rosa «CIRCLE», Tai con camiseta azul «TRIANGLE», Matt con
  camisa negra, Mimi con vestido blanco.
- ***tri.*** (2015-2018): **uniforme escolar** gris y beige, paleta
  apagada (nº 3 y 10 de `fondos_01.jpg`).
- **Epílogo adulto de *02*** (nº 16-28): Tai con traje y maletín; Matt
  astronauta; Koushiro ante un ordenador; Mimi en una cocina.
- **Reboot 2020**: paleta más saturada y plana; sólo visto en los
  Emblemas ⚠️.

⚠️ Sora con **guantes rosas** en IA-V1 (11:30) según la parte de vídeo:
es una copia en VHS a 640×480; el arte oficial y Danbooru dicen rojos.

---

## 17 · Paisajes y fondos de pantalla

### 17.1 Sitios con su luz y su hora ✅

| Sitio | Hora y luz | Fuente |
|---|---|---|
| Selva con flor gigante | día con niebla, luz blanquecina | IA-V1, 11:30 (§5.1) |
| Exterior del abrazo Tai-Agumon | día, sobreexpuesto | IA-V1, 20:00 |
| Bosque tranquilo | día suave, verdes menta | IA-V1, 13:00 |
| **Bosque al atardecer** | atardecer rosa y amarillo, cartel de tráfico en silueta | IA-V1, 45:00 |
| **La playa de la despedida** | día (Tai y Agumon se abrazan en la playa) ⚠️ sin paleta medida | IA-C ep. 54, 14:00 |
| Tokio (*tri.*) | noche, neón violeta y amarillo | x3rmlro, 0:42 |
| Binary Castle | penumbra, televisores turquesa | §5.2 |
| Fluorescent Cave | oscuridad con cristales | §5.2 |
| Gravel Wasteland | mediodía | §5.2 |
| Powdery Cliff | frío, niebla | §5.2 |
| Railroad Plains | día claro | §5.2 |
| Signpost Forest | casi noche | §5.2 |
| **Isla File entera** | día; forma de espiral con playa, selva, montaña nevada y volcán | [ep. 8](https://static.wikia.nocookie.net/digimon/images/2/28/1-08_File_Island.png) (640×480) y [vista aérea](https://static.wikia.nocookie.net/digimon/images/e/e7/File_Island_%28Crusader%29_b.jpg) (1024×854) |

### 17.2 Fondos de pantalla ⚠️

- **Oficiales en alta**: los pósters de la wiki sirven de fondo
  vertical: «Confession» de April Fool en **3420×4836** (nº 1 de
  `fondos_01.jpg`), «Reunión» 1476×2080, «Determinación» 1419×2000. No
  hay fondo oficial apaisado en alta en las partes.
- **De fans (Wallhaven)**: el único resultado apto de 1920×1080 es un
  collage de dibujos de los 90 (Bob Esponja, Los Simpson…), **no de
  Digimon**. Se descarta.
- Los 6 fondos de *Digimon Story* (812×574) sirven de fondo, pero son
  pequeños.

---

## 18 · Guía para generar con IA: imagen y texto

La hizo el redactor con todo lo anterior. Sirve para Firefly, Canva o
cualquier IA de imagen, y para una IA de texto que escriba los diálogos.

### 18.1 Rasgos que nunca cambian (época de 1999)

- **Tai**: pelo castaño **muy puntiagudo y abultado**, ojos marrones,
  **goggles en la frente**, camisa azul con una estrella, pantalón corto
  marrón, guantes blancos.
- **Matt**: pelo **rubio en mechones**, ojos azules, **camiseta verde
  sin mangas de cuello alto**, vaqueros. Casi nunca sonríe abierto.
- **Sora**: pelo corto castaño anaranjado, **gorro azul**, top amarillo
  sin mangas, **guantes rojos**, vaqueros.
- **Agumon**: dinosaurio pequeño de pie, naranja, **ojos verdes
  grandes**, dientes afilados, garras.
- **Gabumon**: piel amarilla, **pelaje azul y blanco encima como una
  capucha**, **un solo cuerno**, ojos rojos, cinturones.
- Todos se reconocen **en silueta negra** (regla del diseñador, §19).
- Son **niños de 11-12 años**. Nada de cuerpos adolescentes (eso es
  *tri.*).

### 18.2 Paleta (medida, §5, §7 y §16)

- Personajes: azul de Tai **#1951A9**, naranja de Agumon **#F8AE02**,
  amarillo de Sora **#EBD639**, amarillo de Gabumon **#DED74F**.
- Mundo Digital de día: pálido y sobreexpuesto (#F4FDF9, #D1F6E3,
  #7E9272). Atardecer: #D58D98 y #F7F7CD con sombra #8E4C67.
- Pantallas y datos: negro **#030302**, turquesa **#42B9AC**, verde
  **#319F41**, azul petróleo **#39464B**.
- Logo: **#FAD30A** a **#EA6F0B** con contorno **#1164A7**.

### 18.3 Línea, sombreado, luz y encuadre

- **Línea** dibujada a mano, oscura pero **no negra pura** (#2D2C1C en
  Agumon, #4D4967 en Gabumon); en los fondos, gris suave (#8F8B71).
- **Sombreado**: *cel* digital de 1999, colores planos y **una sola
  sombra por zona**, del mismo color más oscuro. Sin degradados.
- **Luz**: día pálido y difuso; nada de contraluces dramáticos salvo en
  la digievolución (destello blanco).
- **Encuadre**: Digimon grandes en **contrapicado**; el miedo y la
  sorpresa, en **primer plano cerrado** de la cara (§19).

### 18.4 Palabras que ayudan (en inglés)

`1999 anime screencap, Toei Animation style, digital cel shading, flat
colors, one-tone shadows, hand-drawn outline, soft pale daylight,
Digital World, jungle, summer camp kids` + las etiquetas de Danbooru de
cada uno (§4.4): `goggles_on_head, blue_shirt, brown_shorts,
white_gloves, star_print` (Tai), `helmet, yellow_shirt, red_gloves,
jeans` (Sora), `orange_scales, green_eyes, sharp_teeth` (Agumon),
`single_horn, blue_fur, yellow_skin` (Gabumon).

### 18.5 Palabras que lo estropean

- `3D render`, `realistic`, `photorealistic`: el CGI de la serie es
  tosco y sólo en las digievoluciones.
- `pastel colors`, `soft gradient shading`: son colores vivos y planos.
- `school uniform`, `teenager`: es *tri.*, no 1999.
- `speech bubble`, `comic panel`, `manga screentone`: no es su forma de
  hablar.
- `Pokémon`, `Tamers`, `Terriermon`, `Fusion Loader`: otra franquicia u
  otra serie.
- **Nunca** etiquetas sexualizadas. En Danbooru la etiqueta de Sora
  arrastra una etiqueta de ese tipo: **no copiarla**. Son niños.

### 18.6 Imágenes de referencia

- **Estilo**: los retratos de AniList (§3.2), los nº 29, 30 y 32 de
  `personajes_01.jpg` y los fotogramas de IA-V1.
- **Pose**: Tai al teléfono (IA-V1, 30:00), Tai con Agumon en brazos
  (20:00), Matt de perfil (x5zbgmg, 0:30), la figura de Matt con
  Gabumon a la espalda (§4.2), el key visual «Reunión».
- **Objetos**: Etiqueta dorada (nº 12 de `personajes_01.jpg`),
  Digivice (nº 3 de `objetos_01.jpg`), la tarta del Emblema del Valor
  (§4.2).
- **Fondos**: Railroad Plains y Signpost Forest (§5.2), el bosque al
  atardecer (IA-V1, 45:00).

### 18.7 Para una IA de texto: cómo escribir en su voz

**Cómo habla cada uno** (de sus frases reales y su voz medida, §10):

| Quién | Cómo | Puntuación |
|---|---|---|
| **Tai** | frases cortas, directas; se queja sin rodeos; celebra en plural («juntos») | muchos **¡…!** |
| **Matt** | seco, en primera persona; lo íntimo le sale duro; reconoce a los demás aunque le cueste | punto y seguido; casi sin exclamaciones |
| **Sora** | cálida; manda para proteger; afirma con fuerza | **¡Por supuesto que sí!**; órdenes con «¡Vamos…!» |
| **Agumon** | explica simple, habla de sí mismo por su nombre | frases largas con comas, sin adornos |
| **Gabumon** | suave; condicionales de lealtad; pregunta en vez de ordenar | **puntos suspensivos** y preguntas |

**Frases reales, por emoción** (doblaje latino, muestras oficiales):

- **Alegre**: «¡Juntos lo logramos!» (Tai). «¡Por supuesto que sí! ¡Tú
  eres una de mis mejores amigas!» (Sora).
- **Enfadado**: «Esta cosa tuvo la culpa de mandarme al otro mundo» y
  «Este Digibus no es útil, no sirve para nada» (Tai). «Tú jamás
  entenderás cómo me siento» (Matt).
- **Explicando**: «Lo que pasa es que digievolucionamos, yo cambié de
  Koromon a lo que soy ahora, soy Agumon» (Agumon). «Tai es un niño muy
  decidido y también tiene la habilidad para ser un líder» (Matt). El
  narrador: «Seadramon es un Digimon adulto».
- **Animando**: «¡Vamos, huyan de aquí cuanto antes!» (Sora, con
  urgencia). «Después de todo, eres una buena niña, Mimi» (Sora).
- **Triste**: «Pensé que él me quitaría a mi hermano menor» (Matt).
  «Además, yo no sabría qué hacer en este Digimundo si tú no estás a mi
  lado» y «¿De verdad quieres estar solo?» (Gabumon).

**Vocabulario de la serie** en latino: *Digimundo*, *digievolucionar*,
*Niños Elegidos*, *Emblema del Valor / de la Amistad / del Amor*,
*Etiqueta*, *Digivice*, *Superior Joe*, la tilde de **«-món»**.

**Cómo exageran**: el grito con el nombre en la digievolución; Tai
alza la voz; Matt se calla y mira a otro lado; Gabumon baja la voz.

### 18.8 Vocabulario visual de las expresiones

Lo visto en los fotogramas (§8.6). Las etiquetas en inglés son las
normales de Danbooru, para pedirlas a la IA:

| Gesto en la serie | Dónde | Para la IA |
|---|---|---|
| ojos muy abiertos, pupila chica | Tai ep. 1, 9:16 | `wide-eyed`, `shocked` |
| **gota de sudor** | Gabumon ep. 51, 6:35 | `sweatdrop` |
| ojos cerrados, cara apagada | Matt ep. 54, 13:28 | `closed eyes`, `sad` |
| mirada baja, evita mirar | Sora ep. 26, 10:56 | `looking down`, `embarrassed` |
| ceño fruncido, dientes apretados | Matt ep. 44, 14:15 | `clenched teeth`, `angry` |
| ojos brillantes, a punto de llorar | Sora ep. 54, 14:28 | `teary eyes` |
| destello blanco que envuelve | Agumon, IA-V1 38:20 | `glowing`, `white light` |

⚠️ No hay en las partes ejemplos de *chibi* ni de fondos de emoción
(rayas, flores) de la serie.

---

## 19 · Estilo de dibujo, técnica, Blender y encuadres

### 19.1 Quién lo hizo ✅

- **Toei Animation**, dirección de **Hiroyuki Kakudou**; Fuji TV, del
  7-mar-1999 al 26-mar-2000 (wikitext y Wikipedia, según la parte).
- **Kenji Watanabe**, diseñador de los Digimon desde 1997 (entrevista
  traducida por *digi-lab.blog*, «Digimon Continues to be Loved Thanks
  to its Creator's Commitment»):
  - se inspiró en **cómics infantiles americanos**, raro en el Japón de
    los 90; sus primeras propuestas «monas» se rechazaron por parecerse
    a otras;
  - **«dibujar cosas familiares»**: *«Son Monstruos Digitales, pero
    también quiero que la gente sienta que existen de verdad»*. Por eso
    pone **bolsillos, cinturones y cremalleras** (le interesa la moda);
  - los ojos imitan **ojos de animal**, con mirada ambigua;
  - **cada Digimon se reconoce en silueta negra**: su primer filtro;
  - **colores vivos y nítidos**, no pasteles.
- Animación clave (AniList, 54 episodios): Masahiro Naoi, Yoshitaka
  Yashima, Tomoko Fukui, Setsuko Nobuzane, Yasuhiro Yamaguchi, entre
  otros ([staff](https://anilist.co/anime/552/staff)).

### 19.2 Cómo se pintaba ✅

- Toei usaba entintado y coloreado digital **Celsys RETAS! (RETAS
  PRO)** desde 1996 y **terminó de digitalizar** su departamento en
  **abril de 1999**: la serie empezó justo en el cambio (las películas
  siguieron en celuloide hasta 2000). Resultado: **línea a mano,
  color en capas planas digitales**, una sombra por zona.
- **El CGI de las digievoluciones y del opening lo hacía el director**:
  *«Al principio las hacía todas yo mismo. Las máquinas que usábamos
  eran muy lentas, y pensé que me iba a morir»* (Kakudou, *Digimon
  Series Memorial Book*, vía *digi-lab.blog*). Dormía una hora al día
  los dos primeros meses. **No hubo presupuesto de CGI** hasta *Tamers*.
- Medido en las partes: fondos con línea gris suave (#8F8B71,
  #ACC2AF) y sombreado mixto; *tri.* casi sin línea (§5.1).

### 19.3 Cómo reproducirlo en Photoshop

1. Color **plano** por zonas, sin degradados.
2. Sombras en capa **Multiplicar**, con el **mismo color más oscuro**
   (nunca gris ni negro).
3. Contorno con pincel a mano alzada, grueso y **un poco irregular**
   (era un dibujo escaneado, no un vector).
4. **Grano fino** y **viñeta suave**: aspecto de tele de 1999 (VHS,
   DVD).
5. Para fondos al estilo *Digimon Story*: lápiz duro en capa
   Multiplicar al 30-40 % encima del color (§20).

### 19.4 Cómo reproducirlo en Blender

- **Personajes y Digimon**: *toon shader* de **2 tonos** (luz y
  sombra), poca subdivisión.
- **Contorno**: **Freestyle** o **Solidify invertido** (normales hacia
  dentro, material negro); para lo 2D (caras, cartelas), **Line Art**
  de Grease Pencil, 2-3 px constantes.
- **Digievolución**: polígonos simples, texturas planas y la **cámara
  girando rápido** alrededor del Digimon envuelto en luz: tosco a
  propósito.
- **Modelos libres**: Agumon con *rig* y 13 animaciones (CC BY 4.0), la
  Etiqueta con su Emblema, Greymon, WarGreymon (§4.1).
- **Objetos para la lámina**: la armónica, la cabina telefónica y el
  portátil no tienen modelo libre en las partes ⚠️: se modelan (son
  formas simples).

### 19.5 Encuadres y composición

- **Contrapicado** para los Digimon grandes (tamaño y poder).
- **Primer plano cerrado** en la cara para miedo o sorpresa.
- **Personaje pequeño, Digimon enorme**: el key visual «Reunión».
- Los pósters de *tri.* van **en diagonal**, con los personajes cayendo
  o saltando (nº 11, 19, 20 de `fondos_01.jpg`).
- Un **objeto humano delante** del paisaje (cartel de tráfico en el
  atardecer, IA-V1 45:00; televisores en Binary Castle): da profundidad
  y dice «Mundo Digital».

---

## 20 · Texturas 2D

| Capa | Qué | Enlace y licencia |
|---|---|---|
| **Trama de manga** | el manga *V-Tamer* usa trama de puntos estándar (nº 10 de `personajes_01.jpg`) | [«[FREE] Manga Screentone Pack 1»](https://assets.clip-studio.com/en-us/detail?id=2142037), gratis en Clip Studio Assets ✅ |
| **Lápiz sobre pintura** | la línea de boceto visible de los fondos de *Digimon Story* (sobre todo Gravel Wasteland, con **trama cruzada** en la roca) | a mano: lápiz duro en Multiplicar al 30-40 % |
| **Rejilla digital** | el fondo del Analyzer y del menú de *Digimon World* | [CC0 Textures, «grid»](https://cc0-textures.com/tag/grid), CC0 ✅ |
| **Emblemas** | los 8 en neón sobre azul marino (reboot 2020, [768×432](https://static.wikia.nocookie.net/digimon/images/9/97/Digimon_Adventure_2020_Crests.png)) | ⚠️ colores a ojo: los iconos son demasiado finos para `estilo.py` |
| **Estrella** | el único estampado de la ropa: la estrella de Tai (Danbooru `star_print`) | sacarla del Emblema del Valor |
| **Letrero pintado a mano** | la cartela 勇気の紋章, blanca sobre negro (nº 9 de `fondos_01.jpg`) | ⚠️ puede ser del reboot 2020 |
| **Metal dorado** | las Etiquetas de recuerdo (nº 12-13) | ambientCG, CC0 (§5.3) |

- **Ropa**: casi toda **lisa**, sin estampados: no hace falta textura
  de tela compleja.
- ⚠️ **Sin grano de papel**: no apareció ninguna portada de tomo en
  alta (buscado en la wiki y en With the Will).

---

## 21 · Gustos y detalles de cada personaje

| | Tai | Matt | Sora | Agumon | Gabumon |
|---|---|---|---|---|---|
| **Emblema** | Valor | Amistad | Amor | — | — |
| **Compañero** | Agumon | Gabumon | Piyomon (Biyomon) | Tai | Matt |
| **Familia** | hermano mayor de Kari | hermano mayor de T.K.; padres divorciados, vive con su padre | vive con su madre (floristería); su padre, profesor en Kioto | — | — |
| **Edad** (*Adventure*) | 11 en Japón, **12 en el doblaje latino** | igual | igual | — | — |
| **Cumpleaños** | ⚠️ sin dato | ⚠️ | **25 de octubre** (AniList) | — | — |
| **Su objeto** | **goggles**, Digivice | **armónica**, Digivice | **gorro azul**, guantes rojos | — | un cuerno |
| **Afición** | fútbol (con Sora) ⚠️ | la música (toca la armónica) | fútbol ⚠️ | — | — |
| **De adulto** | traje y maletín (epílogo) | astronauta; casado con Sora | casada con Matt | con traje y pajarita | en traje espacial |

Fuentes: [AniList](https://anilist.co/anime/552) y el wikitext de la
wiki en inglés y [en español](https://digimon.fandom.com/es/wiki/Yamato_Ishida) ✅.

⚠️ **Faltan** comida favorita, altura, tipo de sangre, lo que odian y
cómo se ven a sí mismos. No hay *databook* navegable en las partes
(*Digimon Reference Book*, *V-Jump*). [Wikimon](https://wikimon.net/)
cita el *Character File Book* y el *Memorial Book*, pero sin esos
campos. Agumon y Gabumon no tienen gustos documentados.

---

## 22 · Por qué la gente la ama, y las escenas que hacen llorar

### 22.1 Las razones

1. **La despedida.** LEVEL UP: *«incluso sin memoria directa del
   episodio, ciertos elementos evocan una emoción cuyo origen muchos
   fans no recuerdan»*. La escena pasó de generación en generación
   ([LEVEL UP](https://www.levelup.com/noticias/la-aventura-digievoluciona-a-19-anos-de-la-emision-del-ultimo-episodio-de-digimon-adventure/) ✅).
2. **Te identificas con un secundario.** Kari gana la encuesta oficial;
   Matt supera al protagonista (§9) ✅.
3. **Matt ayuda de verdad.** Una fan chilena con cáncer le escribió a
   Uraz Huerta que Matt la ayudó a superarlo. Matt es perseverar en
   silencio ([El Universal](https://www.eluniversal.com.mx/espectaculos/magia-de-digimon-toca-sus-actores/) ✅).
4. **Las voces de la infancia vuelven.** Gerardo Meza dejó 15 años el
   doblaje y volvió para *Kizuna* (2020) ✅.
5. **Los Digimon hablan y piensan**, y digievolucionan por el **vínculo
   emocional** con su niño («la Digivolución canaliza la energía
   emocional del Niño Elegido», wikitext) ⚠️ sin reseña que lo diga así.
6. Cifras en AniList: nota media **76**, popularidad **71 686**, **2599
   favoritos** ✅.

### 22.2 Las escenas que hacen llorar

| Escena | Minuto | Qué pasa | Cómo está hecha | Música |
|---|---|---|---|---|
| **La despedida** (ep. 54) | IA-C, [13:28](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x54%20-%20The%20Fate%20of%20Two%20Worlds%20(2).mp4?t=808) a [14:48](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x54%20-%20The%20Fate%20of%20Two%20Worlds%20(2).mp4?t=868) | los niños vuelven a la Tierra sin sus Digimon. Matt toca la armónica ante Gabumon; Kari con el silbato; Mimi corre tras el tren | de día, en la playa; primeros planos: Matt con los ojos cerrados (13:28), Tai y Agumon abrazados (14:00), Sora con los ojos brillantes en el tren (14:28) | «Butter-Fly» de Kouji Wada, que el doblaje latino dejó en japonés (Doblaje Wiki ⚠️) |
| **Tai pide perdón** (ep. 16) | IA-C, [19:40](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x16%20-%20The%20Arrival%20of%20Skullgreymon%20%5Ba.k.a.%20The%20Arrival%20of%20Scar%20Greymon%5D.mp4?t=1180) | tras SkullGreymon, Tai abraza a Koromon, que se disculpa por el destrozo y lo perdona | mirada baja, cara apagada; Koromon le sujeta la cara (19:00) | ⚠️ sin dato |
| **Matt y Gabumon en la cueva** (ep. 51) | IA-C, [5:25](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x51%20-%20The%20Crest%20of%20Friendship.mp4?t=325) a [9:00](https://archive.org/download/digimon-digital-monsters-the-complete-seasons-1-4-collection-1999-2003-saban-ent/Digimon%201x51%20-%20The%20Crest%20of%20Friendship.mp4?t=540) | Matt se aísla, echa a Gabumon; al final se abrazan y se prometen ser amigos para siempre | cueva **oscura**; Matt encogido abrazándose las rodillas | ⚠️ sin dato |

### 22.3 Las que hacen gritar de emoción

- **La primera digievolución** de Agumon en Greymon: destello blanco,
  cartela, campanas (IA-V1, ~38:20).
- **Omnimon**: WarGreymon y MetalGarurumon se funden ([x405gc9](https://www.dailymotion.com/video/x405gc9), metraje de *02*).
- **Tai le pega a Matt** en *tri.* ([x5zbgmg](https://www.dailymotion.com/video/x5zbgmg), 0:54): la más comentada y polémica.

### 22.4 Las que hacen reír ⚠️

Poco en las partes: Tai presumiendo el pez ante un Matt escéptico
(IA-V1, 48:00) y los pósters de broma de April Fool (§3).

### 22.5 Cómo reaccionó la gente ⚠️

**Sin comentarios con más votos ni vídeos de reacción**: en Arctic
Shift, «cry» no dio resultados válidos y «goodbye» dio *timeout*;
YouTube y TikTok, bloqueados.

---

## 23 · Fan dubs y comunidad hispana

- **Covers del opening en español**, con el título «**Si Tú Lo
  Deseas**»: [David Delgado](https://www.youtube.com/watch?v=n_UaGJmKa_U),
  César Franco y Claudio Carrizo ⚠️ **sin vistas** (YouTube pide
  iniciar sesión; sólo catalogados por título).
- **Fandub latino de *tri.*** (Gomamon), canal Jose Alejandro, 166
  vistas ([Dailymotion](https://www.dailymotion.com/video/x3y8eso)) ✅.
- **Tendencia de TikTok** «esta será la última digievolución» (§12.3) ⚠️.
- **«Digi-Rap» en español** en comerciales de juguetes de 2001-2002: la
  serie nunca lo usó (Doblaje Wiki ⚠️).
- **La comunidad todavía lo celebra**: Toei Animation LA felicitó a
  Uraz Huerta ([X](https://x.com/ToeiAnimationLA/status/1796360947251982648));
  prensa de México (El Universal, LEVEL UP) y Argentina (AnimeArgentina);
  en 2021 **La Tele de Paraguay** estrenó un máster remasterizado con
  textos en español (Doblaje Wiki).
- ⚠️ **Sin parodias ni memes hispanos concretos**: TikTok sin cuenta y
  sin foros hispanos de doblaje en las partes.

---

## 24 · Colaboraciones, figuras y cosplay

### 24.1 Colaboraciones

| Qué | Cuándo y dónde | Fuente |
|---|---|---|
| **Hypland × Digimon** (ropa de calle): sudaderas, chaquetas acolchadas y camisetas con Agumon, Gabumon, Greymon, Angewomon, Biyomon, Palmon | EE. UU., catálogo activo | [hypland.com](https://hypland.com/collections/digimon) + [Toy People](https://www.toy-people.com/en/?p=107062) ✅ |
| **Animate Cafe** de Seúl-Hongdae: 8 bebidas, una por pareja (Tai y Agumon: naranja con perlas de fresa; Matt y Gabumon: curaçao azul y lichi), posavasos, galletas, latte con dibujo | 5-jun a 7-jul-2026, Corea | [With the Will](https://withthewill.net/threads/digimon-adventure-collaboration-at-animate-cafe-in-korea-starting-june-5th-new-art-drinks-cookies-more.36204/) ⚠️ una fuente, con menú y precios |
| **LB Pop-Up Theater «デジモンショップ Part2»**: arte de grupo nuevo con *Adventure*, *02* y *Tamers* | Shibuya PARCO, 21-feb a 16-abr-2020 | nº 16 de `objetos_01.jpg` ⚠️ (la imagen) |
| **Café de *Last Evolution Kizuna*** | Tokio y Osaka, feb-2020 | [Anime Anime Global](https://animeanime.global/2020/01/31/51239.html) ⚠️ |
| **Bandai × BEAMS**: camisetas por *tri.* | Japón, 2015 | ⚠️ repost en Tumblr; la nota original ya no está |
| **Uniqlo**: mascota virtual con forma de Digivice | — | ⚠️ sólo anuncios de reventa |
| Ropa con Digimon de la marca «@Cuidadoconelperro», menos de 99 pesos | México, sep-2024 | El Heraldo de México ⚠️ (no dice si es licencia oficial) |

**Sin Fortnite ni gachas ajenos**: buscado en inglés y japonés
(«デジモン フォートナイト コラボ»), sin resultado. Digimon tiene sus
propios juegos de gacha (*ReArise*).

### 24.2 Figuras (referencia de pose en 3D)

- **Tamashii Nations «Digivolving Spirits 01»**: Agumon que se
  transforma en WarGreymon, 155 mm ([ficha oficial](https://www.shfiguarts.com/products/detail/7160/) ✅).
- **MegaHouse G.E.M.**: Tai y Agumon juntos, en acción ([Amazon](https://www.amazon.com/Megahouse-Digimon-Adventure-Kamiya-Taichi/dp/B00FQCWHL2) ⚠️).
- **Matt con Gabumon a la espalda** y **S.H.Figuarts MetalGarurumon**:
  fotos con licencia libre (§4.2).

### 24.3 Cosplay bien hecho

- **WarGreymon en goma EVA**, armadura completa con volumen real, de
  u/TDR1411 ([ComicBook](https://comicbook.com/anime/news/digimon-adventure-wargreymon-anime-cosplay/) ✅).
- **Tai con un Agumon de tela** ([ComicBook](https://comicbook.com/anime/news/digimon-cosplay-tai-agumon-bromance/) ⚠️ mismo medio).
- Angewomon y Lillymon con alas de volumen real; Wizardmon con capa;
  Tai de *tri.* y Kari (Flickr, §4.2).

---

## 25 · Obras parecidas y láminas vecinas

### 25.1 Parecidas, según la comunidad de AniList ✅

Pokémon (79 votos), Digimon Tamers (50), Digimon Frontier (29),
Yu-Gi-Oh! (21), Monster Rancher (19), Medabots (12), Dinosaur King
(12), Beyblade (8). Todas: **niño + criatura compañera que se
transforma**.

### 25.2 Influencias ✅

- **Tamagotchi**: «Akiyoshi Hongo», el creador acreditado, es un
  seudónimo colectivo que incluye a **Aki Maita** (cocreadora del
  Tamagotchi), a **Hiroshi Izawa** (autor del manga *V-Tamer*) y a
  **Takeichi Hongo** (marketing de Bandai) ([wiki](https://digimon.fandom.com/wiki/Akiyoshi_Hongo) + búsqueda web ✅).
  El ADN de Digimon es **criar y cuidar**, no sólo coleccionar.
- **Cómics infantiles americanos**: los reconoce Kenji Watanabe (§19) ✅.
- **Frente a Pokémon**, lo que más repite el fandom: los Digimon
  **hablan y razonan** y digievolucionan **por el vínculo, y no para
  siempre**. ⚠️ Sin reseña o entrevista que lo diga así; sólo el
  wikitext de *Digivolution* lo apoya. [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Anime/DigimonAdventure)
  dio 403.
- No hay entrevista de Izawa o del equipo Hongo con otras influencias
  en las partes ⚠️.

### 25.3 Láminas vecinas del servidor (para no repetir)

Comprobado con `grep` en las demás biblias (24-sep-2026). La parte de
texto decía que no había lámina de Pokémon: **sí la hay** (§28).

| Biblia | Canal | Qué hay que no repetir |
|---|---|---|
| **Pokémon (07)** | #autoroles | «La Pokédex en la Ruta 1»: una ficha de criatura. El concepto C (el Analyzer) **no puede parecer una Pokédex**: pantalla oscura con rejilla y cápsula de color, nada de aparato rojo |
| **Demon Slayer (31)** | propone #que-estas-escuchando de 2.ª opción | «Zenko y el shamisen»: **otro personaje con instrumento**. Si el dueño le da ese canal a Demon Slayer, el concepto A repetiría la idea |
| **Jujutsu Kaisen (32)** | propone 🍟 General de 2.ª opción | «¡Salmón!» (Inumaki y sus palabras de onigiri): otra idea, no choca en lo visual |
| **Sailor Moon (38)** y **Saint Seiya (39)** | varios | las otras dos series de Toei de los 90 del lote D: cuidado con repetir pósters de grupo |
| Dragon Ball (`_ya_hechas`) | — | otra de Toei; no hay otras de Yu-Gi-Oh!, Beyblade ni Monster Rancher |

---

## 26 · El mundo, la historia por arcos y sus símbolos

### 26.1 Las reglas del mundo, en cinco líneas ✅

1. El **Mundo Digital** es un universo paralelo **hecho de datos**,
   nacido de las redes de telecomunicaciones de la Tierra.
2. Copia la geografía de la Tierra, pero es **maleable**: se puede
   levantar una montaña o deshacer una isla en segundos.
3. Lo habitan los **Digimon**, criaturas de datos conscientes, que a
   veces cruzan al Mundo Real por portales.
4. Casi nadie en la Tierra sabe que existe.
5. Está ligado al **inconsciente colectivo**: hay Digimon con forma de
   seres del folclore.

(Wikitext de *Digital World* y de la página de la serie.)

### 26.2 La historia por arcos ✅

| Arco | Episodios | Qué pasa | Momento clave |
|---|---|---|---|
| **Isla File** | 1-13 | siete niños de un campamento de verano cruzan al Mundo Digital con sus Digivices; conocen a sus compañeros; Devimon | la primera digievolución (ep. 2) |
| **Etemon** | 14-20 | cruzan al **Continente Server**; buscan sus **Emblemas** uno a uno; Andromon ayuda | **SkullGreymon** (ep. 16) |
| **Myotismon** | 21-39 | Myotismon invade la Tierra por **Odaiba**; aparece la octava niña, **Kari**, con Gatomon y el Emblema de la Luz; cae VenomMyotismon | Sora y su Emblema del Amor (ep. 26) |
| **Los Amos Oscuros** | 40-53 | de vuelta al Mundo Digital, derrotan a MetalSeadramon, Puppetmon, Machinedramon y Piedmon | Matt en la cueva (ep. 51) |
| **Apocalymon** | 54 | Apocalymon, que creó a los villanos con el odio de los Digimon destruidos, cae; los niños vuelven **sin sus compañeros** | **la despedida** |

### 26.3 Objetos y emblemas que un fan reconoce al instante

- **Los 8 Emblemas** (紋章, *monshō*), cada uno en su **Etiqueta**
  colgada al cuello. Forma según la wiki y color según la versión 2020
  (⚠️ a ojo):

| Emblema | Quién | Forma | Color (2020) |
|---|---|---|---|
| **Valor** | Tai | sol de puntas | naranja |
| **Amistad** | Matt | remolino con forma de ala | azul |
| **Amor** | Sora | corazón con espiral | rojo |
| Sinceridad (la parte también dice «Pureza») | Mimi | gota | verde |
| Conocimiento | Izzy | gafas con un cristal más grande | violeta |
| Fiabilidad (la parte también dice «Sinceridad») | Joe | cruz con cuatro triángulos | blanco |
| Esperanza | T.K. | estrella fugaz | amarillo |
| Luz | Kari | estrella | magenta |

- **Etiqueta dorada** de recuerdo con el Emblema grabado (nº 12-13 de
  `personajes_01.jpg`) y en 3D (§4.1). En la tarta de Flickr, azul con
  el Emblema del Valor dorado (§4.2).
- **Digivice**: canaliza la emoción del niño para digievolucionar (nº 3
  de `objetos_01.jpg`).
- **Las goggles** de Tai, la **armónica** de Matt, el **silbato** de
  Kari, el **portátil «PiBook»** de Izzy.
- **Objetos humanos en la naturaleza**: teléfonos públicos (IA-V1,
  30:00), cartel de tráfico (45:00), televisores de Binary Castle, vías
  de Railroad Plains.
- **El Digimon Analyzer** (§7).
- El origen: **mascota virtual** de bolsillo (Digimon Twin, nº 15 de
  `objetos_01.jpg`).

### 26.4 El vocabulario propio ✅

- **Digievolución** (進化, *shinka*): **Bebé** (幼年期I) → **En
  entrenamiento** (幼年期II) → **Novato** (成長期) → **Campeón**
  (成熟期) → **Máximo** (完全体, «forma perfecta») → **Mega** (究極体,
  «forma definitiva»). ⚠️ Los nombres de nivel en el doblaje latino no
  están en las partes; el narrador dice «Digimon **adulto**» (§10.4) y
  Doblaje Wiki habla de «nivel **perfeccionado**».
- **Niños Elegidos** (DigiDestined), **Digimundo**, **Mundo Real**,
  **Continente Server**, **Isla File**, **Montaña Espiral**, **DigiCore**
  (el núcleo de datos de un Digimon).

---
