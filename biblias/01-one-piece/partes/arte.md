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

**Cómo se midió:** k-means (10 grupos) sobre los píxeles del personaje, sin fondo ni línea negra, con una máscara de dónde cae cada color para saber qué prenda es (`/tmp/claude-0/trabajo/01-arte/med_*.jpg`); y `estilo.py` sobre los dibujos oficiales (P25-P31) para comprobar. Luz / sombra = los dos tonos planos del *cel*. ±5 por canal. **✅ = el mismo color sale en dos imágenes distintas**; ⚠️ = una sola imagen. Imágenes: **V1-V30** al final de `hojas/objetos_01.jpg` (O1-O24 no cambian) y P25-P30 de `personajes_01.jpg`.

**Lo que corrige o confirma de la biblia (§6, §9):**
- **Sanji no va de negro: su traje es azul marino casi negro** · luz `#151531` / sombra `#0F0F28` en el dibujo oficial P28 (mi medida) y `#151530` / `#0E0E27` con `estilo.py`; en el anime tras el salto (V20), `#12122D` / `#101329` · ✅ · *antes: «traje negro `#27272E`» y «`#2A272B`» (del arte del juego)*. Antes del salto (V19) sí era negro, con camisa azul claro `#BEDCFE` y corbata celeste `#73D5E1` · ⚠️
- Camisa de Luffy tras el salto: `#C3313E` luz / `#9A1822` sombra (P25) y `#C1333E` (P3) · ✅. Faja `#EDD14A` (P25) y `#EBD14A` (P3) · ✅. Piel `#F2C6A5` y `#F0C5A4` · ✅. Pantalón `#527FD8` (P25) y `#506BB3` (P3), azul medio · ✅. Sombrero `#E7B86E` / `#BD8F5B` (P25) y sombra `#BF925A` (P3) · ✅. Cinta `#CA1B39` (P25) y `#BA2E3D` (juego) · ✅. Dobladillo de pelo del pantalón `#E4E5E7` · ⚠️
- Chopper tras el salto: sombrero rosa `#E48B85` (V25) y `#E4797E` (juego 1369); **gorro azul cian `#44BEE0` (V25), `#41BFE2` (P29) y `#3ACEE7` (juego)** · ✅ (tres imágenes)
- Pelo de Nami `#EE8E3E` (P26), `#F18F40` (otra zona de P26) y `#E1823D` (P8) · ✅. Vaquero `#4D82A9` / `#34617F` (P26) y `#5185A1` (V14) · ✅
- Pelo de Zoro: en el dibujo oficial P27 es **verde menta** `#8ADBAA` / `#76937B`; en el anime P14, verde oliva `#8FAC5B` · ⚠️ (el tono cambia según la imagen: elegir uno y no mezclar)

**Monkey D. Luffy**
- **Lo fijo (lo que un fan reconoce):** sombrero de paja con cinta roja, cicatriz bajo el ojo izquierdo, sandalias; tras el salto, cicatriz en X en el pecho · wiki + P25 (WD14: `straw_hat`, `scar_on_chest`, `scar_on_face`, `sandals`, `yellow_sash`) · ✅
- **Antes del salto (V1, anime):** chaleco rojo de botones `#9F3C40` (luz de escena), pantalón corto `#648DC6`, piel `#EAD1C1` / `#C3917F` · ⚠️ · 843×1080
- **Tras el salto (P25, oficial):** camisa roja abierta y remangada, faja amarilla anudada al lado, pantalón corto azul con dobladillo de pelo blanco · ✅ (arriba) · 1200×998
- **Wano, «Luffytaro» (V3):** kimono rojo `#BD1B27` / `#6E0B1F` con **parches celeste `#8EBBCE` y azul `#37628B`**, obi amarillo, espada al hombro · wiki (galería) · ⚠️ hex · 245×410
- **Egghead (V4):** **abrigo largo rojo `#E23D41` / `#A93834` con franjas naranja-amarillo `#F0B339` y el logo SSG**, guantes, auricular y zapatos DOM rojos; se lo hace una máquina de Vegapunk (cap. 1063, ep. 1092) · [wiki, Luffy](https://onepiece.fandom.com/wiki/Monkey_D._Luffy) + V4 · ✅ · 295×890
- **Elbaph (V5, el arco actual):** vikingo: **capa larga de piel roja `#C13E2D` / `#8B2D24`**, casco con cuernos `#C6975E`, pantalón corto de cuero marrón oscuro `#443B34`, faldón de tiras, cinturón ancho amarillo · wiki («Viking-style outfit… long red fur cape… wide yellow leather belt») + V5 · ✅ · 452×746
- **Film Red (V6):** camiseta roja `#E74037`, **chaleco naranja con dos altavoces** `#F8841C`, pantalón `#4F6CB6` · ⚠️ · 434×1172

**Roronoa Zoro**
- **Lo fijo:** tres espadas a la cadera izquierda, **haramaki verde**, tres pendientes de oro en la oreja izquierda, pañuelo negro atado al brazo izquierdo; tras el salto, cicatriz sobre el ojo izquierdo · wiki + P27 (WD14: `scar_across_eye`, `earrings`, `katana`, `sash`) · ✅
- **Antes del salto (V7):** camiseta blanca `#F9F2E0`, **haramaki `#70AB41` / `#1C4804`**, pantalón negro verdoso, botas · ⚠️ · 211×605
- **Tras el salto (P27, oficial):** abrigo-kimono verde `#47695D` / `#364C43` con botones de madera, faja granate `#99485B` / `#703140`, haramaki `#74A353` asomando, botas negras `#222926` · ✅ (con P14) · 1200×998
- **Wano, «Zorojuro» (V9):** kimono blanco `#DEDEDE` / `#7F7877` con olas en el bajo y **capa verde `#2B501C`** · ⚠️ · 250×445
- **Wano, final (V8):** kimono negro `#1E1D20` / `#373334` abierto y **faja roja `#BF1636` / `#700D25`** · ⚠️ · 493×958
- **Egghead (V10):** chaqueta acolchada azul acero `#38485E` con detalles naranja `#CD943B`, ropa negra `#13161F` · ⚠️ · 404×821
- **Elbaph (V11):** **capa de piel verde `#98AC6A` / `#6F814B`**, túnica verde `#5A6B40`, calentadores de piel verde azulado `#3E7E76`, cinturón `#BD754D` · ⚠️ · 398×665
- **Film Red (V12):** camiseta blanca `#EEF2F3`, vaquero roto azul marino `#1C1D34` · ⚠️ · 409×1301

**Nami**
- **Lo fijo:** pelo naranja, **tatuaje de molinillo y mandarina en el hombro izquierdo** (P54), Log Pose en la muñeca izquierda, la vara Clima-Tact; **cambia de ropa en cada arco** (la galería de la wiki enlaza 109 imágenes de su ropa: anime, películas y juegos) · wiki + P26 + P54 · ✅
- **Antes del salto (V13, East Blue):** camiseta blanca `#F1EEF0` con **franjas azules `#1C51A1`**, minifalda naranja `#E39F24`, pelo corto `#E67C3F` · ⚠️ · 403×957
- **Tras el salto (P26, oficial):** bikini verde agua `#17AB94` con rayas blancas, vaquero `#4D82A9` / `#34617F`, sandalias de tacón, pulsera dorada; pelo largo · ✅ (con V14) · 1200×998
- **Wano, «O-Nami» (V15):** kimono corto celeste `#67C4F0`, **coleta alta** `#F5A239` / `#B15616` · ⚠️ · 1366×1873
- **Egghead (V16):** traje blanco de cuello alto `#F8F2F7` con sombra lila `#DCBEDB` y logo SSG, botas rosas · ⚠️ · 990×2102
- **Elbaph (V17):** chaleco de piel amarilla `#EABE49` / `#C4A363`, top negro `#2A231D`, faldita de cuero `#69493E`, **trenza** `#C57B1F`, calentadores de piel · ⚠️ · 243×742
- **Film Red (V18):** top rojo coral `#E7654F`, falda escocesa `#912D28`, camisa blanca atada a la cintura · ⚠️ · 337×1148

**Sanji**
- **Lo fijo:** traje con corbata, **cigarro**, pelo rubio sobre el ojo izquierdo, **ceja en espiral**, barbita · wiki + P28 (WD14: `hair_over_one_eye`, `curly_eyebrows`, `cigarette`, `facial_hair`, `suit`) · ✅
- **Antes del salto (V19):** traje negro de doble botonadura con botones dorados `#C8AA44`, camisa azul claro `#BEDCFE`, corbata celeste `#73D5E1` · ⚠️ · 380×1038
- **Tras el salto (P28, V20):** **traje azul marino `#151531`**, camisa amarilla apagada `#C0A66D` (P28) / `#A19461` (V20), sin corbata; pelo `#E5E284` / `#BFA972` · ✅ traje y camisa, ⚠️ pelo · 1200×998
- **Wano (V21):** chaqueta gris `#514B57` / `#69676A` · ⚠️ · 175×405
- **Egghead (V22):** **camisa hawaiana naranja `#ECA848` con flores celestes**, pantalón corto negro `#271C1C`, botas naranja `#D9731B` · ⚠️ · 257×790
- **Elbaph (V23):** **capa azul `#3C6CAE` / `#244883`**, cota gris `#8497A2`, botas azules `#4193BE` · ⚠️ · 494×979
- **Film Red (V24):** chaqueta amarilla `#F7D687`, pantalón corto rojo `#EF6562` · ⚠️ · 341×1213

**Tony Tony Chopper**
- **Lo fijo:** **sombrero rosa con la X blanca** (el de Hiluluk), astas, nariz azul, pezuñas; tras el salto, el sombrero va sobre un gorro azul con lunares · wiki + P29 (WD14: `pink_headwear`, `antlers`, `reindeer`, `vertical-striped_shirt`, `backpack`) · ✅
- **Tras el salto (P29 oficial, V25):** sombrero `#E48B85`, X `#DEEFEF`, gorro `#44BEE0`, **camiseta de rayas verticales amarillas y blancas**, pantalón naranja `#DE884A` (sombra `#A75427`), mochila azul `#3275C3`; pelaje `#EDC487` / `#CB8852`, astas `#785845` · ✅ gorro y sombrero, ⚠️ el resto · 1200×713
- **Nariz:** azul `#315AB3` / `#18378E` en P29 · ⚠️ (en el anime antes del salto, P23, `#628190`; en el manga a color, `#192B63`: varía mucho)
- **Wano (V26):** camiseta amarilla con «WATAAME» (algodón de azúcar), gorro `#72C3E0` / `#4C8AA9` · ⚠️ · 595×620
- **Egghead (V27):** mono azul `#3474AB` / `#6AA1C5` con «SSG», **gafas de aviador doradas** `#CEAC6E`, casco blanco, botas rosas · ⚠️ · 560×737
- **Elbaph (V28):** casco vikingo rojo teja `#B55B48` con adornos dorados y capa blanca `#E8DAB8` · ⚠️ · 658×901
- **Film Red (V29):** sombrero rojo de lunares `#E77058`, abanicos «UTA» · ⚠️ · 515×693

**Nico Robin (P30, oficial)** · blusa azul `#232D69` / `#54699B`, pantalón salmón con flores verdes `#E88D80` / `#C66057` (flores `#77AB74`), pelo negro azulado `#25252E`, gafas de sol naranjas en la cabeza, piel `#F7DACB` · ⚠️ · 1200×863

**Para la lámina:**
- **Elegir UNA época y vestir igual a todos.** Mezclar a Luffy de Elbaph con Nami de East Blue es el error típico. Para #bienvenidas, la **ropa de tras el salto (P25-P30)** es la que todo el mundo reconoce, y es la de la web oficial.
- El **color propio** de cada uno (punto 1: rojo, verde, naranja, azul, rosa) coincide con su prenda principal: camisa de Luffy, kimono de Zoro, pelo de Nami, traje de Sanji, sombrero de Chopper.

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
