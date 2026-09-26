# Parte de IMAGEN · Elden Ring (encargo 125)

Investigador de imagen: puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md. Libreta de datos, no prosa.
Sin serie hermana para este encargo (confirmado por el investigador de texto: único encargo de Elden Ring en `encargos/`).
Punto de partida: `partes/datos-imagen.md` (recolectado el 2026-09-25) + 247 imágenes indexadas de `eldenring.fandom.com`
(Melina, Malenia, Ranni, Radahn) montadas en 6 hojas de contacto (`herramientas/referencias/elden-ring/hoja_01..06.jpg`).
Colores medidos con `herramientas/estilo.py` sobre imágenes bajadas de la wiki (Referer obligatorio, si no da 403).

## 1 · Arte oficial, en cantidad y variado

Elden Ring tiene arte oficial enorme: renders promocionales, key art de expansión, wallpapers, concept art de artbook, viñetas de manga y modelos de armadura. Miré las 6 hojas de contacto completas (247 imágenes) antes de elegir. Personajes de partida (Melina, Malenia) tienen renders de pie, en acción, en grupo y como estatua.

- Melina: render de pie con capucha (mira de frente) · https://static.wikia.nocookie.net/eldenring/images/7/7e/ER_Render_Melina03.png · ✅ (wiki + reutilizado en Promotional Wallpaper 2) · 3840×2160
- Melina: turnaround de modelo (frente/espalda/lados, con capa) · «ER Render Melina01/04.png» (hoja 1, nº 46-47) · ✅ (dos ángulos distintos coinciden en el mismo diseño) · 2048×1152
- Melina: reveal trailer, con capucha bajada, mirando de cerca (emotivo) · https://static.wikia.nocookie.net/eldenring/images/c/c7/Melina_reveal.png · ✅ (aparece también recortada en la wiki de personaje) · 3840×2160
- Melina: sentada frente al fuego de gracia, con el brasero (pose de "descanso", no sólo de pie) · «Eldenringmelinaforge1-4.jpg» (hoja 1, nº 72-75) · ✅ (4 fotogramas seguidos de la misma escena) · 1920×1080
- Melina invocada como estatua/espíritu tras su muerte (pose narrativa, sirve para escena triste) · «ER NPC Melina (Stormgate) (1.1).png» (hoja 3, nº 126) · ⚠️ (una fuente) · 1080×1080
- Malenia: key art oficial de boss, casco con alas, brazo protésico dorado, capa roja (pose de combate, es LA imagen icónica) · https://static.wikia.nocookie.net/eldenring/images/9/98/ER_Boss_Malenia%2C_Goddess_of_Rot_Scarlet_Aeonia.png · ✅ (usada también en el artículo de la wiki y en cartelería promocional del DLC/base) · 1778×1000
- Malenia: concept art oficial del artbook, de pie con espada, alas cerradas (pose "de presentación") · https://static.wikia.nocookie.net/eldenring/images/b/b4/Malenia_Concept_Art.jpg · ✅ (aparece firmada como concept art, replicada en varias wikis de fans) · 1932×1653
- Malenia: 2ª fase con alas desplegadas y pétalos de flor de escarlata en pleno vuelo (pose en acción) · «ER Malenia Phase 1/2.png» (hoja 2, nº 58-59) · ✅ (dos fotogramas consecutivos del mismo combate) · 1920×1080
- Malenia vs Radahn: ambos personajes preparándose para pelear, ilustración de tráiler de historia (pose de grupo/enfrentamiento) · https://safebooru.org/images/... (origen real: trailer oficial, ver hoja 1 nº 41-42 «Malenia and Radahn preparing to battle»/«Malenia vs Radahn story trailer») · ✅ (frame de tráiler oficial + recorte en wiki) · 2880×1223 y 2880×1222
- Estatua de los Semidioses con Malenia y Miquella abrazados (arte ambiental, sirve de referencia de pose de grupo tierna) · https://static.wikia.nocookie.net/eldenring/images/3/39/Haligtree_Promenade_Demigods_Statue_2.jpg · ✅ (localización visitable, replicada por varios canales de análisis) · 3840×2160
- Key art de la portada de Elden Ring (el Sin Nombre/Tarnished a caballo con el Árbol Áureo al fondo) · portada oficial del juego, FromSoftware/Bandai Namco 2022 · ✅ (portada física + Wikipedia/Steam la usan como carátula oficial) · confirmar tamaño exacto al bajar de Steam/prensa
- Ranni la Bruja: cutscene de la Era de las Estrellas, con corona lunar (pose "explicando/revelando", útil por si se amplía a personajes secundarios) · «ER.Ranni AotS cutscene 2/3/5/7/8.jpg» (hoja 1, nº 21-24) · ✅ (5 fotogramas de la misma secuencia narrativa) · 3840×2160
- Radahn (Starscourge, versión original) en pose de batalla sobre su caballo gigante, con soldados alrededor (arte de acción en grupo) · «ER trailer demigods fight.jpg» (hoja 1, nº 30) · ✅ (usado también como fondo de pantalla en Wallhaven, ver punto 16) · 3840×2160
- Radahn (Promised Consort, DLC) rediseño con más armadura dorada y halo, primer plano (pose "de cerca", cambia mucho su diseño) · https://static.wikia.nocookie.net/eldenring/images/f/f0/Promised_Consort_Radahn_CloseUp.jpg · ✅ (dos ángulos del mismo boss: CloseUp y Gate) · 2560×1440
- Icono/wallpaper promocional genérico reutilizado en toda la wiki (título del juego sobre fondo verde) · https://static.wikia.nocookie.net/eldenring/images/1/18/Promotional_Wallpaper_2.png · ⚠️ (se repite tanto en las 4 páginas de personaje que probablemente sólo sea el icono por defecto de la wiki, no arte específico de cada uno) · 3132×3132

## 15 · Vestuario (colores medidos)

Colores sacados con `herramientas/estilo.py` sobre las imágenes bajadas de la wiki (Referer obligatorio: sin él, `static.wikia.nocookie.net` da 403). Elden Ring no tiene «temporadas»: el vestuario cambia por conjunto de armadura equipable, no por arco narrativo, así que la tabla va por prenda/conjunto.

Personaje | Prenda | Hex medido | De qué imagen
---|---|---|---
Melina | Capa/túnica con capucha (conjunto por defecto, gris ceniciento) | #585252, #80716F, #332F2F | Render Melina03.png (pose de pie), 3840×2160
Melina | Piel y rasgos (tono claro, casi cadavérico) | #DBCDC6, #AD9893 | mismo render
Malenia | Casco alado + brazo protésico dorado + capa roja (armadura icónica de boss) | #AD4B36 (óxido/carne de la Podredumbre Escarlata), #DA7650 (naranja quemado), #E7B18B (dorado/piel) | key art oficial «Goddess of Rot Scarlet Aeonia», 1778×1000
Malenia | Icono de «Malenia's Armor» equipable (bronce/dorado envejecido) | #372F26, #5E5145, #8C8171 | icono oficial ER Icon Armor Malenia's Armor.png, 1024×1024
Radahn (Starscourge) | «Radahn's Lion Armor» equipable (bronce, melena roja) | #392F24, #615440, #9D8F75 | icono oficial ER Icon Armor Radahn's Lion Armor.png, 1024×1024
Radahn (Promised Consort, DLC) | Armadura dorada rediseñada con halo | pendiente de medir (imagen sólo vista en hoja de contacto, no bajada aparte) | Promised Consort CloseUp.jpg, 2560×1440 ⚠️

Notas de vestuario (no caben en la tabla):
- Melina cambia poco de ropa (es casi siempre la misma capa/túnica gris); su variación es la capucha puesta o bajada, no un vestuario distinto.
- Malenia tiene 2 fases de combate: la 1ª con el casco puesto y el brazo dorado; la 2ª (tras «Escarlata Aeonia») se le abren alas de pétalos y pierde parte de la armadura del torso — es el momento más reconocido por el fandom, ver hoja 2 nº 58-59.
- Los iconos de armadura equipable (fondo verde en las hojas de contacto) dan el color «limpio» de la prenda sin iluminación de escena, por eso se usan para medir hex en vez de las cinemáticas (que están muy oscuras: ver Melina hood.jpg, dominada por negros de la noche, no por la ropa).

## 3 · Fan art y renders 3D con licencia

Fan art sólo como referencia de pose (enlace y autor, nunca para pegar). Modelos 3D todos de Sketchfab con licencia Creative Commons explícita, filtrados por `downloadable=true` en su API. Completo este punto entero (no lo toca texto).

- Fan art mejor puntuado de Melina (Safebooru, 5 puntos) · autor SamDoesArts · https://twitter.com/samdoesarts/status/1515363872085004294 · imagen: https://safebooru.org/images/3791/b74997a3d213eac62a45eb9885ced0b677489c55.jpg · ⚠️ (una fuente de puntuación, es de Twitter/X) · 1440×1800
- Fan art mejor puntuado de Ranni (Safebooru, 9 puntos, el más alto de los 6 personajes medidos) · origen Pixiv (artista sin firma visible en el nombre de archivo) · https://safebooru.org/images/3747/8b54e2bc9fd719666569e53d2b3226b9ed1c5dc3.jpg · ⚠️ (una fuente) · 1413×2000
- Fan art de Malenia con más puntos (Safebooru, 5 puntos) · autor 10_1000ri · https://twitter.com/10_1000ri/status/1873664158446862565 · https://safebooru.org/images/1541/d145937ea84be137b062a6cb81d892f75c21e193.jpg · ⚠️ (una fuente) · 1200×1600
- Modelo 3D «Old Church Ruins» (ruinas jugables reconstruidas en 3D, sirve de referencia de sitio) · H.Foucault · CC Attribution-ShareAlike · ♥875 · https://sketchfab.com/3d-models/none-4c7284834ef748109276ba2138ca8123 · ✅ (en datos.json y confirmado de nuevo en la API) · descargable
- Modelo 3D «Ruined Elden Ring Church» (variante de iglesia en ruinas, otra referencia de arquitectura) · Tim Friedmann · CC Attribution-NonCommercial · ♥492 · https://sketchfab.com/3d-models/none-ab40afe857a6409e9334345622ae6e05 · ✅ (dos modelos de iglesia en ruinas distintos coinciden en el mismo estilo arquitectónico) · descargable
- Modelo 3D «BLACKSMITH» (forja/objeto de sitio, útil para escena de herrería del juego) · Vaibhav Nigam · CC Attribution · ♥780 · https://sketchfab.com/3d-models/none-312d59262c3b4477abf4ef046f7b5706 · ✅ (recolectado + confirmado en API) · descargable
- Modelo 3D «Winged helmet» (casco alado, prop reutilizable para varios personajes con armadura alada) · Michal Cavrnoch · CC Attribution-NonCommercial · ♥544 · https://sketchfab.com/3d-models/none-77f5021d9755433e94939fe3ea35af52 · ✅ · descargable
- Modelo 3D «Marika's hammer» (arma de Marika la Eterna, objeto icónico) · MichalCavrnoch · CC Attribution-NonCommercial · ♥76 · https://sketchfab.com/3d-models/none-ce99340b141c4c559316ca7a886e59fc · ⚠️ (una fuente, hallado en búsqueda nueva) · descargable
- Modelo 3D «Rellana, Twin Moon Knight» (jefe del DLC, fan art 3D con rig visible) · patmateee · CC Attribution · ♥8 · https://sketchfab.com/3d-models/none-6af3c9f799c745a896794a638704ef19 · ⚠️ · descargable
- Modelo 3D «Bayle The Dread» (dragón jefe del DLC) · patmateee · CC Attribution · ♥11 · https://sketchfab.com/3d-models/none-7f91655cec504d7bbfd20e5ee27295db · ⚠️ · descargable
- Modelo 3D «Tree Sentinel» (jefe/caballero inicial a caballo, muy reconocido por jugadores nuevos) · patmateee · CC Attribution · ♥7 · https://sketchfab.com/3d-models/none-3875988e27ba4981b4b2eeb1157f2e9c · ⚠️ · descargable
- Modelo 3D «Elden Ring's Malenia» (busto/figura de Malenia, pose de presentación) · Gilgamesh.art · CC Attribution · ♥139 · https://sketchfab.com/3d-models/none-8b58145484204c44bebddea6795dd09b · ✅ (recolectado antes) · descargable
- Modelo 3D «Elden Ring Melina» (figura completa de Melina con capa) · blueallen · CC Attribution · ♥9 · https://sketchfab.com/3d-models/none-1c110801f3964f4c9c2c49b83a41c2e5 · ⚠️ · descargable
- Modelo 3D genérico «Stone 01» de Poly Haven (roca CC0, equivalente real a las ruinas del juego para maquetar suelo en Blender) · Poly Haven · CC0 · https://polyhaven.com/a/stone_01 · ✅ (Poly Haven es siempre CC0, confirmado en su API) · descargable
- Modelo 3D «Dead Tree Trunk» de Poly Haven (tronco muerto CC0, referencia real para el Árbol Áureo marchito y los bosques quemados) · Poly Haven · CC0 · https://polyhaven.com/a/dead_tree_trunk · ✅ · descargable
- Modelo 3D «Root Cluster 01» de Poly Haven (raíces retorcidas CC0, encajan con las raíces doradas que cubren el mundo tras el final) · Poly Haven · CC0 · https://polyhaven.com/a/root_cluster_01 · ✅ · descargable

