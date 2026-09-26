# Voz y personajes — Reanimal

Investigador de voz y personajes (puntos 7, 8, 12, 13, 20, 21, 22 de ENCARGO.md). Empecé desde
`partes/datos-voz.md` (recolector automático) y seguí a mano: Doblaje Wiki (wikitext completo,
no solo la tabla que el recolector no supo parsear), reanimal.fandom.com (wikitext de cada
personaje), Reddit r/ReanimalGame vía Arctic Shift, Danbooru, Metacritic/reseñas, una entrevista
oficial (Xbox Wire) y 8 muestras de audio del doblaje latino oídas con `voz.py`. Reanimal es un
juego de terror y aventura (Tarsier Studios, THQ Nordic, 13-feb-2026): no es un anime, así que
varias cosas que se buscan en otras biblias (encuestas oficiales, databook, cumpleaños) no existen
aquí; lo digo en cada punto con las búsquedas hechas.

## 7 · Personajes principales y secundarios: popularidad

Es un juego de solo 7 meses de vida (lanzado 13-feb-2026): no hay una encuesta de popularidad como
en un anime. Lo más parecido es lo que se mide en Reddit y en cuánto fan art recibe cada uno.

- No existe una encuesta oficial de personaje favorito de THQ Nordic/Tarsier Studios · busqué «Reanimal personaje favorito encuesta», «Reanimal character popularity poll» (es/en), sin resultado · ⚠️
- En r/ReanimalGame (subreddit de fans), Capucha (Hood) es la que más cariño/lástima genera en los posts con más votos: «Oh hood my poor sweet girl» (65 votos) y «Kill em, Hood!!!» (71 votos, sobre vengarse del monstruo que la secuestra) · https://www.reddit.com/r/ReanimalGame/comments/1w969n0/ · https://www.reddit.com/r/ReanimalGame/comments/1wndpsv/ · ⚠️ (medida informal, un solo sitio)
- Fan art en Danbooru con tag «reanimal» (muestra muy pequeña, 7 dibujos en total): La Niña es la más dibujada (6), El Niño (5), Capucha/Benda/Cubeta empatados (4 cada uno) · https://danbooru.donmai.us/posts?tags=girl_(reanimal) (y tags boy_/hood_/bandage_/bucket_(reanimal)) · ⚠️ (muestra minúscula)
- Los monstruos compiten en cariño con los protagonistas: hay fan art propio de la Bestia Oveja («I drew The Sheep Beast looks so depth», r/ReanimalGame) · https://www.reddit.com/r/ReanimalGame/comments/1wpsmnu/ · ⚠️
- La guía de fans reanimalgame.com centra todo en El Niño y La Niña como protagonistas; no hay ranking de secundarios ahí · https://reanimalgame.com/tier-list · ⚠️

## 8 · Frases icónicas en el doblaje latino

Doblaje mexicano (estudio **Made in Spanish**), 2026. La ficha de Doblaje Wiki todavía tiene casi
todos los papeles «por identificar»: el reparto completo de actores SÍ está confirmado (créditos
oficiales del juego), pero falta que la propia wiki empareje cada actor con su personaje.

| Personaje | Voz original | Voz latina | Fuente 1 | Fuente 2 |
|---|---|---|---|---|
| El Niño (The Boy) | ¿No identificada? | Por identificar | Doblaje Wiki (ficha REANIMAL) | — |
| La Niña (The Girl) | Lisbeth Moller Fly | Por identificar | Doblaje Wiki (ficha REANIMAL) | reanimal.fandom.com (infobox The Girl) |
| Capucha (Hood) | Molly Jenkins | Por identificar | Doblaje Wiki (ficha REANIMAL) | reanimal.fandom.com (infobox Hood) |
| Benda (Bandage) | ¿No identificada? | Por identificar | Doblaje Wiki (ficha REANIMAL) | — |
| Cubeta (Bucket) | Cali Worthington | Por identificar | Doblaje Wiki (ficha REANIMAL) | — |
| Cerdo (Pig) | ¿No identificada? | Raúl Solo | Doblaje Wiki (tabla REANIMAL) | Doblaje Wiki (ficha propia de Raúl Solo) |
| Ballena / Voz (archivo suelto) | ¿No identificada? | Raúl Solo | Doblaje Wiki (tabla REANIMAL) | Doblaje Wiki (ficha propia de Raúl Solo) |

- Reparto latino confirmado en su totalidad (7 actores, aunque a la mayoría les falta personaje asignado): Regina Becerril, Sebastián García, Carlos Márquez, Victoria Ramírez, Damián Urias, Adriana Vera y Raúl Solo · Fuente 1: créditos oficiales del propio juego («Créditos REANIMAL ESLAT.png», 1366×768, leída con OCR/tesseract) · Fuente 2: Doblaje Wiki, ficha REANIMAL, lista «Participación por identificar» (mismos 6 nombres + Raúl Solo) · ✅
- Cerdo y Ballena → Raúl Solo: dos páginas de Doblaje Wiki lo confirman (la ficha de REANIMAL y la ficha propia del actor) pero es la MISMA wiki · ⚠️ (falta una fuente externa: ANMTV no respondió, ver bitácora)
- Estudio de doblaje: Made in Spanish (México) · Doblaje Wiki (ficha REANIMAL) · ⚠️ fuente única para este juego en concreto (el estudio en sí es real y verificable en madeinspanish.com, pero no vincula ahí este título)
- Traducción hecha en Brasil por Lourenço D'Almeida, Wallacy Silva y Estéfano Vitagliano · Doblaje Wiki (ficha) + créditos oficiales del juego (misma imagen OCR, sección «Translator») · ✅ dos fuentes

**Frases textuales**, oídas con `voz.py` sobre las muestras oficiales de audio de Doblaje Wiki
(cada .ogg es un clip suelto del personaje, no un capítulo del juego; el minuto es el segundo
dentro de esa muestra):

- La Niña: «Ni idea. ¿Dónde están los demás?» (0:00) · «Busquemos una llave.» (0:02) · voz aguda (276 Hz), monótona (2.8 semitonos), velocidad normal (2.83 palabras/s) · REANIMAL_Girl.ogg (Doblaje Wiki) · ✅
- El Niño: «¿Recuerdas algo de antes? ¿Qué crees que pasará ahora?» (0:00) · «Ojalá pudiéramos volver.» (0:04) · voz media (218 Hz), monótona (2.4 semitonos) · REANIMAL_Boy.ogg · ✅
- Capucha: «Deberían irse, mientras aún pueden, demasiado tarde, él ya sabe que están aquí.» (0:00) · voz aguda (241 Hz), expresividad normal (4.3 semitonos), lenta (2.07 palabras/s) · REANIMAL_Hood.ogg · ✅ · coincide con la escena de la wiki en inglés («leave while they still can»)
- Benda: «Escóndete allí, volveremos por ti.» (0:00) · voz aguda (272 Hz), la más lenta de los tres amigos (1.88 palabras/s) · REANIMAL_Bandage.ogg · ✅
- Cubeta: «Bueno, he estado mejor.» (0:00) · «Pero sí, estoy bien.» (0:02) · «¿Por qué volviste por nosotros?» (0:03) · voz media (213 Hz), la más rápida de los tres amigos (3.17 palabras/s) · REANIMAL_Bucket.ogg · ✅
- Chico (archivo suelto «Kid»): «No te preocupes, vamos a salir de esta juntos, ¿sí?» (0:00) · voz aguda (264 Hz), monótona · REANIMAL_Kid.ogg · ✅
- Ballena (archivo «Whale»): «¡Puedo ver!» (0:00) · «¡No puedo ver!» (0:02) · voz grave (101 Hz), MUY expresiva (30.9 semitonos) · REANIMAL_Whale.ogg · ✅ · **hallazgo**: es diálogo CORTADO del juego final — reanimal.fandom.com (página «Unused and Cut Content») confirma que la Ballena Espiral iba a hablar sobre haber perdido la vista y se quedó sin usar; la frase oída encaja exactamente · ✅ (dos fuentes: el audio mismo + la wiki)
- Cerdo: la muestra no tiene diálogo transcribible, es un gruñido/sonido animal sin palabras · REANIMAL_Pig.ogg · ⚠️ (sin texto que citar)

## 12 · Lo que el fandom ama (y qué NO hacer)

- Lo más votado en r/ReanimalGame no son memes de personajes: es CONTENIDO CORTADO dataminado del juego («Cut Content - Towns People», 170 votos; «Cut Content - Pigsty», 80 votos) · https://www.reddit.com/r/ReanimalGame/comments/1whgc4u/ · https://www.reddit.com/r/ReanimalGame/comments/1wmz5rw/ · ✅ (Reddit + confirmado por la propia wiki, sección «Unused and Cut Content»)
- In-joke recurrente: compasión y ganas de vengar a Capucha, la amiga que más sufre (la secuestra Sniffer, luego la devora la Bestia Oveja) · «Oh hood my poor sweet girl» (65 votos) y «Kill em, Hood!!!» (71 votos) · https://www.reddit.com/r/ReanimalGame/comments/1w969n0/ · https://www.reddit.com/r/ReanimalGame/comments/1wndpsv/ · ✅
- Fan art tipo broma visual «Hood sandwich» (64 votos, Capucha entre los otros personajes) · https://www.reddit.com/r/ReanimalGame/comments/1wifj2q/ · ⚠️ (imagen, sin texto)
- Los fans crean sus propios personajes (OCs) ambientados en la isla · «Took me long enough… Reanimal ocs!» (75 votos) · https://www.reddit.com/r/ReanimalGame/comments/1wl1uti/ · ✅
- Jugarlo acompañado es parte de lo que se ama: comentarios de gente que lo jugó "con mi papá", lo completó al 100 % y lo rejuega para fijarse en detalles · https://www.reddit.com/r/ReanimalGame/comments/1w175i2/ · ✅ (coincide con el punto 21)
- **QUÉ NO HACER** — dibujar la cara de El Niño con expresión: su máscara de saco NO tiene agujeros para ojos ni boca, es un vacío negro total en todo momento · render oficial The_Boy.png (reanimal.fandom.com) · ✅
- **QUÉ NO HACER** — confundir a Capucha/Benda/Cubeta (los 3 amigos secuestrados, personajes NO hostiles) con monstruos: el sitio de fans reanimalgame.com sí comete ese error y llama a Cubeta «Bucket Creature» tipo enemigo; la propia wiki oficial lo desmiente (categoría «Non-hostile NPC») · https://reanimalgame.com/tier-list vs. https://reanimal.fandom.com/wiki/Bucket · ✅ (contraste de dos fuentes)
- **QUÉ NO HACER** — poner diálogo largo o explicativo: el juego casi no habla, se apoya en silencio y sonido ambiente (1 a 3 frases cortas grabadas por personaje, comprobado al oír las 8 muestras) · Doblaje Wiki + entrevista Xbox Wire · ✅
- **QUÉ NO HACER** — hacer una lámina "tierna" sin más: es terror explícito, clasificación ESRB M (sangre, desnudez parcial, violencia) · ficha de Doblaje Wiki + Steam (misma clasificación) · ✅

## 13 · Descripción profunda de cada personaje

### El Niño (The Boy) — protagonista jugable
- Carácter: cariñoso sobre todo con su hermana y sus amigos, valiente, hábil con herramientas y mecánica; no sabe bien por qué está en la Isla al empezar · reanimal.fandom.com/wiki/The_Boy · ✅
- Arco: despierta a la deriva en una barca; encuentra a su hermana inconsciente en el agua y la salva; recorre la Isla rescatando a sus 3 amigos; al final, tras un encuentro con la Bestia Oveja, cambia de bando y ayuda a noquear a su propia hermana para devolverla al pozo, ignorando que ella se resiste · reanimal.fandom.com/wiki/The_Boy (coincide con The_Girl) · ✅
- Cómo se expresa: voz media (218 Hz), MONÓTONA (2.4 semitonos: casi sin variación, plano, como aturdido), ritmo normal · medido con `voz.py` sobre REANIMAL_Boy.ogg · ✅
- Frase real: «¿Recuerdas algo de antes? ¿Qué crees que pasará ahora?» / «Ojalá pudiéramos volver.» · REANIMAL_Boy.ogg · ✅
- Cara en cada emoción: NO TIENE. Su máscara (saco de tela) no deja ver ojos ni boca, es un hueco negro total siempre; toda su "expresión" se cuenta con el cuerpo (postura, manos) y con el tono de voz, nunca con la cara · render oficial The_Boy.png · ✅ · dato clave para la lámina: nunca darle rasgos faciales
- Objeto que siempre lleva: un encendedor · reanimal.fandom.com/wiki/The_Boy · ⚠️ (una sola fuente, no lo vi confirmado en vídeo)
- Dinámica: hermano protector de La Niña; con Capucha, Benda y Cubeta comparte un "juramento de sangre" de la infancia que solo recuerda al final del juego · reanimal.fandom.com/wiki/The_Boy · ✅

### La Niña (The Girl) — protagonista jugable, Jugador 1 en cooperativo
- Carácter: valiente, protectora, con un lado "feral": ataca primero si se siente en peligro; hábil con armas blancas · reanimal.fandom.com/wiki/The_Girl · ✅
- Arco: aparece flotando inconsciente en el mar; su hermano la rescata y, al despertar, ella intenta ahogarlo por instinto/shock; a medida que se acerca a su antiguo hogar empieza a sentir que la Bestia Oveja "está dentro de ella"; en el final canónico, su hermano y sus 3 amigos la traicionan y la devuelven al pozo · reanimal.fandom.com/wiki/The_Girl · ✅
- Cómo se expresa: voz aguda (276 Hz), también monótona (2.8 semitonos) pero algo más viva que su hermano, velocidad normal (2.83 palabras/s) · `voz.py` sobre REANIMAL_Girl.ogg · ✅
- Frase real: «Ni idea. ¿Dónde están los demás?» / «Busquemos una llave.» · REANIMAL_Girl.ogg · ✅
- Cara en cada emoción: es la ÚNICA con algo de cara visible. Su máscara blanca de conejo tapa solo los ojos, como un antifaz, y deja ver la boca y la barbilla; en el render oficial la boca está en reposo, sin sonreír ni gesticular, aun sosteniendo un cuchillo y un farol · render oficial TheGirl.png · ✅ · no encontré ningún fotograma oficial de ella gritando o llorando con la boca abierta pese a revisar el teaser y el tráiler de anuncio fotograma a fotograma (±3 s) · ⚠️ no encontrado
- Le importan los conejos: se angustia al encontrar uno muerto · reanimal.fandom.com/wiki/The_Girl · ⚠️ (una fuente)
- Objeto que siempre lleva: un farol de aceite y un cuchillo de combate (se ve en el render oficial) · reanimal.fandom.com/wiki/The_Girl + render TheGirl.png · ✅ (wiki + imagen propia)
- Dinámica: hermana de El Niño; termina traicionada por todos los que fue a rescatar · reanimal.fandom.com/wiki/The_Girl · ✅

### Capucha (Hood) — primera amiga rescatada
- Carácter: reacia a pedir ayuda, cuidadosa; entiende el comportamiento de los monstruos aunque no puede pelear; desaprueba que los hermanos sigan buscando en vez de huir · reanimal.fandom.com/wiki/Hood · ✅
- Arco: primera amiga encontrada; los evade varias veces "por su bien"; la secuestra el monstruo Sniffer en una furgoneta de helados; en el final ayuda a atar a La Niña, quedándose con su cuchillo · reanimal.fandom.com/wiki/Hood · ✅
- Cómo se expresa: voz aguda (241 Hz), expresividad normal (4.3 semitonos), habla LENTO (2.07 palabras/s) — la más pausada de los 3 amigos · `voz.py` sobre REANIMAL_Hood.ogg · ✅
- Frase real (coincide con la escena descrita en la wiki, «leave while they still can»): «Deberían irse, mientras aún pueden, demasiado tarde, él ya sabe que están aquí.» · REANIMAL_Hood.ogg · ✅
- Cara: máscara puntiaguda de tela con un parche naranja cosido, sin agujeros visibles para ojos en el render oficial (muy oscuro) · render Hood_render.png (328×760) · ⚠️ (no pude confirmar si tiene agujeros pequeños; imagen muy oscura)
- Es la más querida por el fandom hispanohablante y anglosajón por igual: genera lástima y protección en Reddit (ver puntos 7 y 12) · ✅

### Benda (Bandage) — segundo amigo rescatado
- Carácter: cobarde, se deja llevar por el miedo y a veces huye solo sin avisar; cariñoso pese a todo, feliz de que lo busquen · reanimal.fandom.com/wiki/Bandage · ✅
- Arco: lo secuestra un Pelícano gigante y lo cuelga en una jaula en lo alto de un faro; en el final sostiene el farol de La Niña mientras la atan · reanimal.fandom.com/wiki/Bandage · ✅
- Cómo se expresa: voz aguda (272 Hz), habla LENTO (1.88 palabras/s, el más lento de los tres) · `voz.py` sobre REANIMAL_Bandage.ogg · ✅
- Frase real: «Escóndete allí, volveremos por ti.» · REANIMAL_Bandage.ogg · ✅
- Vestuario/objeto: bufanda de rayas verdes, cabeza envuelta en vendas sucias, solo se le ven las orejas y mechones de pelo negro · reanimal.fandom.com/wiki/Bandage · ✅

### Cubeta (Bucket) — tercer amigo rescatado
- Carácter: enérgico, poco consciente del peligro, sin reflejos de pelea, confundido de por qué volvieron a buscarlo pudiendo huir ya · reanimal.fandom.com/wiki/Bucket · ✅
- Arco: cautivo en un orfanato, a punto de ser comida de la Madre (monstruo araña); rescatado tras una pelea contra los Niños Araña; en el final sostiene el conejo muerto que tocó La Niña · reanimal.fandom.com/wiki/Bucket · ✅
- Cómo se expresa: voz media (213 Hz), la MÁS RÁPIDA de los tres amigos (3.17 palabras/s) · `voz.py` sobre REANIMAL_Bucket.ogg · ✅
- Frases reales: «Bueno, he estado mejor.» / «Pero sí, estoy bien.» / «¿Por qué volviste por nosotros?» · REANIMAL_Bucket.ogg · ✅
- Le gusta comer: en el arte conceptual y su figura coleccionable aparece sosteniendo un cuenco de papas y a veces pescado; un poco más rellenito que los demás niños · reanimal.fandom.com/wiki/Bucket · ⚠️ (una fuente, no contrastada con vídeo)

### DLC «The Expanded World» (secundarios nuevos, más recientes, menos documentados)
- El Prisionero (protagonista 1 del DLC): tímido, callado, terco, quizá con poderes helados; responde «I'll live» cuando la Soldado le ofrece su abrigo · reanimal.fandom.com/wiki/The_Prisoner_(Character) · ✅
- La Soldado (protagonista 2 del DLC): rescata al Prisionero de una celda, casco plateado oxidado, trenzas rubias · reanimal.fandom.com/wiki/The_Soldier · ✅
- Recepción: el DLC divide a la comunidad, ver punto 21 · ⚠️

## 20 · Gustos y detalles de cada personaje

| Personaje | Le gusta | Odia | Aficiones | Cumpleaños | Altura | Fuente |
|---|---|---|---|---|---|---|
| El Niño | su hermana, recordar su antigua casa | perder a sus amigos | mecánica, herramientas, su encendedor | No indicado | No indicado | reanimal.fandom.com/wiki/The_Boy |
| La Niña | los conejos | ver un conejo muerto | pelear con cuchillo, cuidar su farol | No indicado | No indicado | reanimal.fandom.com/wiki/The_Girl |
| Capucha | la seguridad de sus amigos | que la sigan a la Isla en vez de huir | intuir por dónde vienen los monstruos | No indicado | No indicado | reanimal.fandom.com/wiki/Hood |
| Benda | estar con sus amigos | los monstruos de la Isla (le dan pánico) | correr y esconderse | No indicado | No indicado | reanimal.fandom.com/wiki/Bandage |
| Cubeta | comer (papas, pescado) | no entender por qué volvieron por él | esconderse | No indicado | No indicado | reanimal.fandom.com/wiki/Bucket |

- Ningún personaje tiene cumpleaños ni altura publicados: los propios desarrolladores los llaman a propósito "a nameless boy and girl" (entrevista Xbox Wire, 13-feb-2026) y el infobox de personaje de la wiki no trae esos campos · búsquedas hechas: infobox de cada personaje en reanimal.fandom.com, página del artbook «Art of REANIMAL» (solo arte, sin ficha), Steam, entrevistas (Xbox Wire, Cubed3) · ⚠️ No encontré (dato que probablemente no exista para esta obra: son niños deliberadamente anónimos)
- Cómo se ven a sí mismos: no hay monólogos internos ni diario en el juego (confirmado por lo poco hablado, punto 8); no encontré ninguna fuente con introspección de un personaje · ⚠️ No encontré

## 21 · Por qué la gente la ama

- Nota media 81/100 en reseñas de crítica · metacritic.com/game/reanimal · resumen recogido también por purexbox.com («Roundup: Here's What The Reviews Are Saying About Xbox Horror Title 'Reanimal'») · ✅ dos fuentes
- Motivo que dan los propios creadores: terror COMPARTIDO en cooperativo, pensado para que dos personas se acompañen en el miedo (idea que nació de ver cómo la gente jugaba a Little Nightmares en pass-and-play) · entrevista oficial en Xbox Wire a Andreas Johnsson (productor y cofundador) y David Mervick (director narrativo), 13-feb-2026, news.xbox.com/en-us/2026/02/13/reanimal-interview/ · ✅ (fuente primaria oficial)
- Los jugadores lo confirman: en el hilo con más votos del subreddit (160 votos, 14 comentarios) hay gente que lo jugó "con mi papá", lo completó al 100 % y lo rejuega para fijarse en detalles · reddit.com/r/ReanimalGame/comments/1w175i2/ · ✅
- Con qué personaje se identifica el público: con Capucha (Hood), la amiga que más sufre — el fandom reacciona con protección y culpa hacia ella (ver punto 12) · reddit.com/r/ReanimalGame · ✅
- Influencias que reconocen los propios autores, y que explican el tono que engancha: "Alien" y "Jaws" (tensión por lo que no se ve), los cuentos de Astrid Lindgren (crueles pero conmovedores) y el cine de David Lynch ("Twin Peaks", "Fire Walk with Me"); el director narrativo dice que con Lynch "quieres llorar tanto como esconderte" y que el equipo se guía por instinto más que por fórmula · entrevista Xbox Wire · ✅
- Escena que golpea emocionalmente (según la wiki y Reddit; no verifiqué el minuto exacto en vídeo): el secuestro y muerte de Capucha (raptada por Sniffer, devorada por la Bestia Oveja) y el giro final donde el hermano y los 3 amigos traicionan a La Niña · reanimal.fandom.com/wiki/Hood + comentarios "Poor Hood" en Reddit · ⚠️ (relato por escrito, sin fotograma propio confirmado — falta ver una guía en vídeo del capítulo exacto)
- Punto que también se comenta, para no idealizar: el DLC "The Prisoner" divide — a varios les pareció corto, caro e insatisfactorio ("Too small, waste of money"; "way too short… left very unsatisfied") · reddit.com/r/ReanimalGame/comments/1w93rzd/ (33 comentarios) · ✅

## 22 · Fan dubs y comunidad hispana

- No encontré ningún fandub (redoblaje de fans) de escenas de Reanimal en español: busqué «Reanimal fandub español», «Reanimal fandub latino» en YouTube/Dailymotion/TikTok — solo aparecen partidas comentadas ("gameplay en español latino") y listas de reproducción genéricas de fandub sin relación real con este juego · búsquedas en español e inglés, 26-sep-2026 · ⚠️ No encontré
- Explicación probable: el juego tiene muy poco diálogo hablado (1 a 3 frases cortas grabadas por personaje, ver punto 8), así que hay poco material para redoblar, a diferencia de un anime · comprobado al oír las 8 muestras de audio con `voz.py` · ✅
- Tampoco hay tema principal cantado que versionar: la banda sonora oficial (33 pistas, publicada 21-jul-2026) es instrumental, compuesta por Christian Vasselbring, Jacob Carlsson y Stefan Almqvist · open.spotify.com/album/5MLLUrklIMstRrYHykdkf2 · reanimal.fandom.com/wiki/REANIMAL_(soundtrack) · ✅ dos fuentes
- Lo que sí hace la comunidad hispana: partidas comentadas y guías al 100 % en español latino, alguna en 4K60 («REANIMAL Juego Completo en Español Latino, FINAL VERDADERO») · youtube.com/watch?v=8Cwt91Oax0k · ⚠️ (una fuente, vistas no contrastadas)
- Parodias o memes hispanos específicos de Reanimal: no encontré ninguno · búsqueda «Reanimal parodia», «Reanimal meme español» sin resultado relevante · ⚠️ No encontré

## Lo mejor para la lámina

1. El Niño NUNCA tiene cara (agujero negro total en su máscara de saco): un dato visual fuerte y nada genérico para cualquier lámina donde aparezca.
2. La frase real de Capucha «Deberían irse, mientras aún pueden…» (audio oficial del doblaje latino) sirve como cuadro de diálogo de terror suave, lejos de la burbuja blanca genérica.
3. El audio de la «Ballena» es diálogo CORTADO del juego («¡Puedo ver!» / «¡No puedo ver!»): un dato de coleccionista que un fan de verdad reconocería.
4. Capucha es la secundaria más querida por el fandom (Reddit) — mejor candidata a "personaje secundario más querido" que Benda o Cubeta.
5. Lo que más se ama del juego es jugarlo ACOMPAÑADO (cooperativo): cualquier lámina sobre "hacer algo junto a alguien" conecta con el motivo real de por qué la gente lo ama.

## No encontré (con las búsquedas hechas)

- Encuesta oficial de popularidad de personajes (THQ Nordic/Tarsier) · busqué en español e inglés, sin resultado.
- Cumpleaños y altura de cualquier personaje · revisé el infobox de cada uno en la wiki (vacío), el artbook «Art of REANIMAL» y dos entrevistas oficiales (Xbox Wire, Cubed3); probablemente no exista porque los autores los quieren "sin nombre".
- Segunda fuente EXTERNA (fuera de Doblaje Wiki) para el estudio "Made in Spanish" en este juego, y para la asignación de Raúl Solo a Cerdo/Ballena · intenté ANMTV (`anmtv.la` no respondió ni por curl ni por `navegar.py`: `ERR_TUNNEL_CONNECTION_FAILED`) y una búsqueda web dedicada.
- Fandubs reales (redoblajes de fans) en español de escenas de Reanimal · búsqueda en YouTube/Dailymotion/TikTok, en español e inglés.
- Parodias o memes hispanos específicos de Reanimal · búsqueda en español.
- Fotograma oficial de La Niña o El Niño mostrando una emoción fuerte (miedo, llanto) con la boca/cuerpo bien visible · revisé el teaser oficial (31 fotogramas, cada 3 s) y el tráiler de anuncio (26 fotogramas, cada 3 s): ambos son muy oscuros y de plano general, sin primeros planos de los protagonistas.

## Bitácora de búsqueda

- Doblaje Wiki, API `action=parse&prop=wikitext`, página REANIMAL completa (no solo la tabla parseada por el recolector) → reparto, estudio, traductores, créditos.
- reanimal.fandom.com, API `action=query&prop=revisions` sobre: The Boy, The Girl, The Brother, The Sister, Hood, Bandage, Bucket, Masks, Masked Children, The Mother, The Prisoner (Character), The Second Prisoner, The Soldier, The Watcher, Pigs, The Spiral Whale, Unused and Cut Content, Art of REANIMAL, Critters, Skins, REANIMAL (soundtrack).
- Imagen de créditos del doblaje descargada (`Créditos REANIMAL ESLAT.png`, formato WebP real) y leída con `tesseract -l spa`, contrastada mirando la imagen directamente.
- Renders oficiales descargados y mirados: TheGirl.png, The_Boy.png (para comprobar los agujeros de la máscara).
- `voz.py` sobre las 8 muestras oficiales de audio del doblaje latino (Boy, Girl, Hood, Bandage, Bucket, Pig, Whale, Kid) — todas oídas, no solo listadas.
- `fotogramas.py` sobre el teaser oficial (dailymotion/xa1mxgm, cada 3 s, 31 fotogramas) y el tráiler de anuncio (dailymotion/x94c4ui, cada 3 s, 26 fotogramas + 3 fotogramas sueltos en 0:30, 0:45 y 0:51), todos mirados con Read.
- Reddit r/ReanimalGame vía Arctic Shift (`/api/posts/search`, 100 posts; `/api/comments/search` sobre 3 hilos) — búsqueda por tema (favorite character, why I love, best scene) sin resultado por `title=`, así que ordené por puntuación a mano.
- Danbooru: `/counts/posts.json` para los tags `girl_(reanimal)`, `boy_(reanimal)`, `hood_(reanimal)`, `reanimal` (contraste del dato ya recolectado).
- WebSearch (en español e inglés): «Reanimal doblaje latino elenco», «Reanimal review Tarsier Studios metacritic score», «Reanimal ending explained cry sad scene reddit», «Reanimal fandub español latino youtube», «"Reanimal" personaje favorito encuesta poll», «"Made in Spanish" estudio doblaje Reanimal México», «Reanimal opening ending song vocal theme soundtrack», «Reanimal Tarsier Studios interview director character design Boy Girl».
- `navegar.py` sobre news.xbox.com/en-us/2026/02/13/reanimal-interview (entrevista completa leída), tvtropes.org/pmwiki/pmwiki.php/Characters/Reanimal (solo el índice, las carpetas están cerradas por JS) y reanimalgame.com/tier-list (guía de fans, sin relación oficial).
- `anmtv.la` inalcanzable (curl: timeout; navegar.py: `ERR_TUNNEL_CONNECTION_FAILED`) — no pude usarlo como segunda fuente de doblaje pese a intentarlo dos veces.
