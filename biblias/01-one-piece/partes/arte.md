# Parte · arte — One Piece (#bienvenidas)

Investigador de **arte** (equipo de 8, repaso). Puntos 1, 15 y 16 de ENCARGO.md y hojas de contacto.
Parte de lo que ya está en `biblia.md` (§3, §6, §9): aquí va **lo que faltaba**, lo dudoso confirmado y lo más hondo.
Formato: `- dato · fuente(s) con enlace · ✅ (dos fuentes) o ⚠️ (una) · tamaño medido`.
Tamaños medidos con la API de la wiki (`imageinfo`) o abriendo la imagen con Pillow. Hex medidos con Pillow (mediana de una zona, ±5 por canal).

## Hallazgos

### 1 · Arte oficial variado (key visuals, tomos, cuenta atrás, juegos, grupo, acción)

**Qué había en la biblia (§3):** 72 imágenes de la wiki en 3 hojas (eyecatchers, Color Walk, infobox, carteles) y 24 ilustraciones de *Treasure Cruise*. **Qué faltaba:** arte de la web oficial, cartones de cuenta atrás, key visuals del anime, portadas de tomos, carteles de película, hojas de modelo (settei) y arte de juegos de consola. **Añadido: P25-P54**, al final de `hojas/personajes_01.jpg` (P1-P24 no cambian de número). Todas miradas.

**Web oficial one-piece.com (fuera de la wiki).** Piden la cabecera `Referer: https://one-piece.com/`; sin ella el servidor devuelve siempre la misma imagen de Luffy (la bajé 16 veces igual hasta darme cuenta).
- P25-P30 · **Dibujos oficiales de cuerpo entero, fondo blanco**, de la ficha de cada personaje: `https://one-piece.com/o/assets/images/anime/character/data/<luffy|nami|zoro|sanji|chopper|robin>/img.jpg` · one-piece.com + etiquetas WD14 de `estilo.py` (reconoce a cada uno con 0,99-1,00) · ✅ · 1200×998 (Chopper 1200×713, Robin 1200×863)
- P26 · **Nami saluda con el brazo derecho en alto y la otra mano en la cadera, boca abierta**: es la pose de «¡hola!» más clara de todo lo reunido, y oficial · one-piece.com; WD14: `arm_up`, `hand_on_own_hip`, `jumping`, `open_mouth`, `looking_at_viewer` · ✅ · 1200×998
- P29 · **Chopper salta con los dos brazos arriba y la boca abierta**, mochila azul · one-piece.com; WD14: `open_mouth`, `smile`, `backpack` · ✅ · 1200×713
- P28 · Sanji apoyado de lado, **manos en los bolsillos**, pelo sobre un ojo · one-piece.com; WD14: `hands_in_pockets`, `cigarette`, `curly_eyebrows` · ✅ · 1200×998
- P31 · **La tripulación en fila, con Jinbe** (versión actual de los diez), fondo blanco · [one-piece.com/img/strawhatpirates/strawhatpirates_01.jpg](https://one-piece.com/img/strawhatpirates/strawhatpirates_01.jpg) · ✅ (WD14: `everyone`, reconoce a 7 de 10) · 1200×960
- P32 · **Luffy de pie en un bote, los dos brazos al cielo**: la pose de «¡zarpamos!» · [one-piece.com/img/character/luffy/luffy_05.jpg](https://one-piece.com/img/character/luffy/luffy_05.jpg) · ⚠️ (no sé el episodio) · 1200×675
- P54 · Nami enseña el tatuaje del hombro (molinillo y mandarina) · [one-piece.com/img/character/nami/nami_09.jpg](https://one-piece.com/img/character/nami/nami_09.jpg) · ✅ (el tatuaje está en la wiki) · 1200×675
- Cada ficha trae 8 escenas más (`/img/character/<nombre>/<nombre>_02…09.jpg`, 1200×675): Luffy llorando con Shanks, Sanji con ojos de corazón, Robin en la escalera del Merry con Luffy y Chopper, Chopper con algodón de azúcar… · one-piece.com · ✅ · 1200×675
- La web va por el **episodio 1171 «エルバフの大罪人 冥界のロキ解放!?»** (24-sep-2026): el anime está en **Elbaph** · [one-piece.com/anime](https://one-piece.com/anime/index.html) + [Toei, 28-oct-2025](https://x.com/ToeiAnimation/status/1983160636679786887): «parón de tres meses desde enero; vuelve en abril de 2026 con el arco de Elbaph, en dos partes al año» · ✅

**Cartones de cuenta atrás (lo que pedía el encargo).**
- P33-P37 · **#ONEPIECE1000LOGS**: la cuenta atrás al capítulo 1000 (dic-2020). Cada cartón = una viñeta del manga en blanco y negro + **fondo plano del color del personaje** + el número gigante en blanco + el hashtag en blanco inclinado · [wiki](https://onepiece.fandom.com/wiki/File:Chapter_1000_Countdown_1_Luffy.png) + [tuit de @Eiichiro_Staff, 20-dic-2020, «1000話まであと【1話】»](https://x.com/Eiichiro_Staff/status/1340673498142818305) (leído por la API de sindicación de X: 17.554 «me gusta», imagen 1601×900) · ✅ · 1600-1601×900
- Las frases de cada cartón son de su primera aparición: Nami, «私は海賊からお宝を盗む泥棒っ!» («¡soy una ladrona que roba tesoros a los piratas!»); Zoro, atado, «もう九日間もこのままだ…» · leído en la imagen · ⚠️ (traducción mía)
- **Cada Sombrero de Paja tiene «su» color oficial**, medido en el fondo (moda de píxeles): Luffy `#FF321D`, Zoro `#A8BB7E`, Nami `#FFA001`, Sanji `#2269E5`, Chopper `#FE9FAA` (cuenta atrás) · y lo repiten los carteles de *Film Red* (P38-P42): Luffy `#E70013`, Zoro `#17AC55`, Nami `#EE7602`, Sanji `#3B82C5`, Chopper `#EA79AD` · ✅ (dos campañas oficiales distintas, Shueisha 2020 y Toei 2022) · **rojo, verde, naranja, azul, rosa**: sirve para dar a cada personaje su franja o su marco en la lámina.

**Carteles y hojas de modelo de *Film Red* (2022).**
- P38-P42 · Un cartel por Sombrero de Paja: cuerpo entero con la ropa de la película, **fondo plano de su color**, una frase suya en vertical, y la calavera del sombrero sobre el logo RED · [wiki, «Film Red Posters»](https://onepiece.fandom.com/wiki/Category:Film_Red_Posters) (fuente: [@OP_FILMRED](https://twitter.com/OP_FILMRED)) · ✅ · Luffy 1446×2048, Nami 1554×2186, Chopper 2427×3436, **Zoro 2912×4096**, Sanji 1704×2413
- P40 · El de Chopper dice «あっちに本がいっぱいの部屋があるって» («dicen que allí hay un cuarto lleno de libros»): va vestido de explorador, con gafas · leído en la imagen · ⚠️ (traducción mía)
- P50-P51 · **Hojas de modelo (settei) de la ropa de «festival»**: Luffy y Nami de frente, perfil y espalda, en línea sin color, con caras aparte · [web oficial de Film Red](https://www.onepiece-film.jp/en/info-en/63/) vía wiki · ✅ · 1200×900 (hay también Zoro, Sanji y Chopper, y las de «batalla» a 2000×1500)

**Key visuals del anime y portadas.**
- P43 · **Eyecatcher del episodio 1000**: Luffy sonríe con los ojos cerrados, **de cara, delante de su cartel de SE BUSCA** · [wiki, Episode 1000](https://onepiece.fandom.com/wiki/File:1000th_Episode_Eyecatcher_2.png) · ✅ · **2560×1440** (la sonrisa de bienvenida más grande que hay; mejor que P1 si se quiere Luffy «oficial» y no la estatua de cera)
- P44 · **Color spread de los capítulos 999-1000**: los diez apiñados sobre un montón de tesoro, con el marco dorado «ONE PIECE 1000 LOGS» · wiki · ✅ · 2485×1851
- P45 + P46 · **Tomo 1 y tomo 61 son pareja**: en el 1, Luffy, Zoro y Nami «zarpan celebrando, rodeados de gaviotas»; en el 61 («ROMANCE DAWN for the new world», el reencuentro tras dos años) la tripulación entera repite la escena en la cubierta del Sunny · [wiki, Volume 1](https://onepiece.fandom.com/wiki/Volume_1) y [Volume 61](https://onepiece.fandom.com/wiki/Volume_61) (descripción de la portada) · ✅ · 640×1016 y 756×1200 · **es la imagen oficial de «empieza la aventura»: la más temática para #bienvenidas**
- P47 · Tomo 100: Luffy sonriendo en el centro, fondo arcoíris · wiki · ✅ · 2038×3240
- Las 115 portadas existen en la wiki a 640-2044 px de ancho (`File:Volume_<n>.png`; la 116 aún no) · API de la wiki · ✅ · las del 90 en adelante pasan de 2000 px de alto
- P48 · **Key visual de Egghead (2.ª parte)**: Luffy en Gear 5 con la mano abierta hacia la cámara, la tripulación con los trajes del futuro · [wiki](https://onepiece.fandom.com/wiki/File:Egghead_Arc.png) 2188×3096 + [tuit de @ToeiAnimation, 23-dic-2024](https://x.com/ToeiAnimation/status/1871272025517588963) (original 2895×4096; «vuelve el 6 de abril de 2025») · ✅
- P49 · **Portada del tomo 111 («Aventura en Elbaph»)**: Luffy salta con un hacha naranja y los seis primeros Sombrero de Paja corren con él; Loki encadenado detrás · [wiki, Volume 111](https://onepiece.fandom.com/wiki/Volume_111) · ✅ · 1536×1925
- **Visual del anime de Elbaph** (Toei, oct-2025): **un Luffy diminuto, con casco vikingo y capa roja, camina por la nieve dejando huellas**; fondo blanco y logo gris · [pbs.twimg.com/media/G4WaE6kWsAA7m5x.jpg](https://pbs.twimg.com/media/G4WaE6kWsAA7m5x.jpg?name=orig) · ✅ (tuit oficial) · 1457×2064 · (no cabe en la hoja: enlace directo)
- **Cumpleaños de Luffy 2026** (5 de mayo): Luffy Gear 5 con los ojos cerrados, el Sunny y un dragón (Momonosuke), luna llena, fondo negro · [@OPcom_info, 4-may-2026](https://x.com/OPcom_info/status/2051317197562384413) (93.689 «me gusta») · ✅ · 1200×630 en X; [Wallhaven](https://wallhaven.cc/w/ly2yg2) tiene una copia de 7680×4032 ⚠️ (no sé de dónde sale ese tamaño)

**Videojuegos (arte de portada, por la API de Steam).**
- P52 · *One Piece Odyssey*: Luffy de espaldas, pequeño, ante una cascada y ruinas verdes · [Steam 814000](https://store.steampowered.com/app/814000) (`library_600x900_2x.jpg`; también `library_hero.jpg` 1920×620 y 9 capturas 1920×1080) · ✅ · 600×900
- P53 · *Pirate Warriors 4*: Luffy en Gear 4 y Kaido, rayos · [Steam 1089090](https://store.steampowered.com/app/1089090) · ✅ · 600×900 (y `library_hero.jpg` 1920×620)

**Lo ya reunido que sigue sirviendo (no lo repito):** eyecatchers en cartel P6/P9/P15/P19/P21, Color Walk P2/P13/P17/P20, CD *Island Song Collection* P7/P11 (son los **singles**), DVD *Log Collection* P10 y las 24 de *Treasure Cruise* (§3.1).

### 15 · Vestuario por arco (hex medidos con Pillow)

_(pendiente)_

### 16 · Ciudades, paisajes y fondos de pantalla

_(pendiente)_

### Hojas de contacto

_(pendiente)_

## Lo mejor para la lámina

_(pendiente)_

## No encontré

_(pendiente)_

## Bitácora

_(en curso)_
