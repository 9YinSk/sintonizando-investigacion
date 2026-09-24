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
