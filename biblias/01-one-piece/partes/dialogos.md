# Parte · dialogos — One Piece (puntos 5, 6 y 11)

> Investigador de diálogos (equipo de 8). Repaso: parto de §7, §8 y §13 de `biblia.md`.
> Aquí va sólo lo **nuevo**, lo **confirmado** que antes llevaba ⚠️ y lo **corregido**.
> Formato: `- dato · fuente(s) · ✅ (dos fuentes) / ⚠️ (una) · minuto o tamaño si aplica`
> Lo pesado (letras, capturas, APK) está en `/tmp/claude-0/trabajo/01-dialogos/`.

## Hallazgos

### Punto 5 · Tipografía

(en curso)

### Punto 6 · Cómo hablan y piensan en pantalla

(pendiente)

### Punto 11 · Videojuegos: interfaz, menús y cajas

Todo lo de aquí lo **miré** (Read) en capturas oficiales: 59 de Steam (7 juegos, API `appdetails`), 29 de la App Store (API de búsqueda de iTunes, México y Japón) y el tráiler de *Grand Gourmet* en Dailymotion. Colores medidos con `estilo.py` sobre recortes de cada caja (±5 por canal).

**Qué juegos hay en español de Latinoamérica** (lo que puede leer el servidor):
- *ONE PIECE ODYSSEY* (ILCA, 2023): español de España **y de Hispanoamérica** · [Steam 814000](https://store.steampowered.com/app/814000/) (API, `l=spanish`, `cc=MX`) · ⚠️ una fuente para el latino (ya estaba en la biblia).
- *ONE PIECE World Seeker* (Ganbarion, 2019): España + **Hispanoamérica** · [Steam 755500](https://store.steampowered.com/app/755500/) · ⚠️ una fuente · *nuevo*.
- *ONE PIECE Bounty Rush* (Bandai Namco / SEGA): **Hispanoamérica** · [Steam 2918150](https://store.steampowered.com/app/2918150/) + [App Store MX](https://apps.apple.com/mx/app/one-piece-bounty-rush/id1343688545) (idiomas `ES`, descripción en español: «¡Captura el botín, pirata!») · ✅ · *nuevo*.
- *ONE PIECE: Grand Gourmet* (Kairosoft, sale el **23-oct-2026**): España + **Hispanoamérica** · [Steam 3905010](https://store.steampowered.com/app/3905010/) (22-oct por huso horario) + [One Piece Wiki](https://onepiece.fandom.com/wiki/One_Piece:_Grand_Gourmet) + tráiler «Available 10.23.2026» ([Dailymotion, 1:36](https://www.dailymotion.com/video/xae7mxq?t=96)) · ✅ · *nuevo*. En Japón: 『ONE PIECE 海のごちそうレストラン』; el jugador es novato del **Baratie 2** con Sanji (wiki).
- *Pirate Warriors 3 y 4*, *Burning Blood*: sólo español **de España** · Steam 331600, 1089090, 425220 · ⚠️ una fuente.
- *ONE PIECE TREASURE CRUISE*: **no está en español** (EN, FR, JA, KO) · [App Store](https://apps.apple.com/mx/app/one-piece-treasure-cruise/id943690848) (`languageCodesISO2A`) · ⚠️ una fuente · *nuevo*.

**Las cajas y rótulos que se ven en pantalla, juego por juego:**
- **Odyssey, caja de diálogo** (repaso de lo que ya decía la biblia): banda baja **translúcida** con medallones en relieve; medida con `estilo.py` en la [captura 7](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/814000/ss_ecd6e4103c470b4b7878f0902ce91bf9743a458c.1920x1080.jpg) (1920×1080): banda `#466163`/`#4C686B`, pestaña del nombre `#38909C` (97 % plano) · ✅ confirma `#466164` y `#38909C` de la biblia. **Ojo:** en la [captura 5](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/814000/ss_1d099b6daf3b4497fd4c05f252fd85e623b2b505.1920x1080.jpg) la misma banda mide `#2E4646`: es translúcida y toma el color de lo que hay detrás. Para la lámina: verde azulado al ~75 % de opacidad, no un color fijo.
- **Odyssey, letra de la caja:** palo seco humanista algo estrecha, blanca, con **sombra oscura desplazada abajo-derecha**; el nombre («Bibi») en una negrita redondeada, blanca con sombra, sobre la pestaña de borde rasgado. Texto en España: «Sí, muchas gracias por decírmelo.» (OCR con tesseract `spa` y a ojo, captura 7) · ⚠️ la letra exacta no está publicada; ver punto 5.
- **Grand Gourmet, caja de diálogo** ([captura 6](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3905010/a8dc456ad9de44fb295b4394e2be1bb14d7979c4/ss_a8dc456ad9de44fb295b4394e2be1bb14d7979c4.1920x1080.jpg), 1920×1080): **caja crema `#FAF3E1`** con **doble filete dorado `#E8B976` y café `#84623A`**, el busto en píxeles de Sanji saliendo por arriba a la izquierda, el nombre en una barra oscura translúcida, y como «siguiente» **un ancla ⚓ gris** abajo a la derecha (no la flechita de siempre). Arriba, placa oscura con borde punteado y dos cabos: «ONE PIECE: Grand Gourmet». Marco de la escena: telón rojo y un timón y un ancla en las esquinas · ✅ (captura oficial + tráiler) · *nuevo, y es la caja «de barco» más clara de la franquicia*.
- **Grand Gourmet, segunda caja** (tráiler, [0:29](https://www.dailymotion.com/video/xae7mxq?t=29) y [1:33](https://www.dailymotion.com/video/xae7mxq?t=93)): recuadro gris muy claro con borde gris oscuro y sombra de píxel; quién habla lo marca **un triangulito verde ▼ sobre su cabeza**, no una cola · ✅ visto.
- **Grand Gourmet, rótulos del tráiler:** frases en **letra de píxel amarilla con borde oscuro** sobre una tabla de madera con dos cuchillos («Cook with Sanji!», «Customize your restaurant!», «Over 400 Characters Appear!») · [hoja del tráiler](https://www.dailymotion.com/video/xae7mxq?t=36), 0:36-1:20 · ✅ visto.
- **Treasure Cruise, los «名シーン» (escenas famosas)** ([App Store JP, captura 5](https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/96/df/44/96df4415-ad93-b2ff-b6b3-426e19a152b0/05-06_OPTC_bnr_Appstore_6.5_U30a4_U30f3_U30c1_1284x2778.png/2000x2000bb.jpg), 924×2000): la escena se cuenta **con viñetas del manga coloreadas y globos de manga de verdad**: blanco `#FFFFFF` con borde negro `#0B0A08` grueso y algo irregular, texto japonés vertical, y **un ▼ amarillo** para pasar; encima, un globo **gris `#7F7F7F`** con la frase anterior ⚠️ (interpretación mía). Botones «VOICE» y «SKIP ➜» (naranja). Marco de **madera y latón** sobre **fondo rojo `#520406` con calaveras** (Jolly Rogers) · ✅ medido · *nuevo: es la prueba de que un juego oficial usa el globo del manga, no una caja*.
- **Treasure Cruise, menús** ([App Store MX, capturas 4-6](https://apps.apple.com/mx/app/one-piece-treasure-cruise/id943690848)): barras de madera oscura con ribetes dorados, botones redondos de **timón** («ADVENTURE», «CAMPAIGN», «CREW», «HOME», «TAVERN»), el nivel como «PIRATE Lv», la recompensa con el símbolo ฿ de berry. Títulos en letra de cómic muy gruesa, blanca con borde negro y la palabra clave en rojo («RECRUIT YOUR **FAVORITE CHARACTERS**») · ✅ visto.
- **Bounty Rush, «DOOM!!»** ([Steam, captura 4](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2918150/ss_a74ae187b479661147360878280c74d21c71da14.1920x1080.jpg)): letras enormes **rojas `#D00303` con borde blanco `#FAF4EE`**, inclinadas, en medio del combate: es la versión en inglés del ドン!! · ✅ visto · qué lo dispara ⚠️ (no lo encontré).
- **Bounty Rush, frases rápidas del chat** ([captura 2](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2918150/ss_9d8f5c06c48c8681ec5a9569891ebc12015cd757.1920x1080.jpg)): placas grises en ángulo, texto **blanco en cursiva gruesa** con un icono amarillo («Leave it to me!», «Let's do this!», «Watch out!» con triángulo verde). Recompensas: ฿ + cifra gorda naranja (equipo sol) o cian (equipo ola) · ✅ visto.
- **Bounty Rush, ficha del personaje** ([captura 6](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2918150/ss_790c1bcb7f22e04cb254cb815b670eefb60aee68.1920x1080.jpg)): panel «Profile» gris translúcido con filas **Birthday / Height / Place of Origin / Bounty / VA** (Roger: «Dec 31st», «274 cm», «East Blue, Roguetown», «฿5,564,800,000», «Masane Tsukayama») · ✅ visto · sirve de modelo para la ficha de presentación.
- **Burning Blood, onomatopeyas en 3D** ([captura 5](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/425220/ss_9bdb521c64090fc46661c77ba98752e39006a337.1920x1080.jpg) y [13](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/425220/ss_0c3dfc52488e911da69b03eb53a741fb034cb08d.1920x1080.jpg)): el golpe se escribe en **katakana gigante dentro del escenario** (ズドォン!!!, バチッ, ボフッ!!, ガオオオ…), **rojo `#CC191D` con filete negro `#11151C` y borde blanco**, en perspectiva, como en el manga · ✅ medido · *nuevo*.
- **World Seeker, Pirate Warriors 3 y 4**: sus capturas de Steam (10, 15 y 6) son **sólo de combate o paisaje, sin cajas ni texto** · ✅ miradas todas · no sirven para la caja.
- **ONE PIECE BASE** (app oficial de manga de Bandai Namco; Japón oct-2024, inglés feb-2025): su «**Portrait Generator**» (『ONE PIECE似顔絵メーカー』) convierte tu foto en un retrato **al estilo de Oda** y te hace **tu propio cartel WANTED**, que puedes poner **de foto de perfil** · [App Store EN](https://apps.apple.com/mx/app/one-piece-base-en/id6739035554) + [App Store JP](https://apps.apple.com/jp/app/one-piece-base/id6499420991) («自分や友達をONE PIECE風に変換して、オリジナルの手配書を生成しよう!») · ✅ · *nuevo*.
  - El cartel tiene **reverso** ([captura 4](https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/9a/9f/06/9a9f06c6-3021-5898-a662-95fab084b149/04-portrait-generator_complete_2208_1242.jpg/2000x2000bb.jpg), 1125×2000): una **ficha en papel viejo** (`#E7CDA3`, `#F0DEC2`, texto `#4A3F33`, medido) con cinco filas separadas por una raya fina, cada una con su icono: **Nickname / Other titles** (sombrero), **Bounty** (฿), **Devil Fruits** (fruta), **Haki** (rayo), **Affiliations** (calavera) · ✅ visto.
  - Para #bienvenidas es oro: el paso «preséntate» ya existe en la franquicia como **el reverso de tu cartel**. Delante, WANTED / foto / DEAD OR ALIVE / nombre / ฿; detrás, tu ficha.

## Lo mejor para la lámina

(pendiente)

## No encontré

(pendiente)

## Bitácora

(pendiente)
