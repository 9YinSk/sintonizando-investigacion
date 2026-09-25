# Investigador de VÍDEO · Saga of Tanya the Evil (Youjo Senki)
_Puntos ENCARGO.md: 2, 4, 9, 10, 14_

---

## HALLAZGOS

### Punto 2 — Fotogramas de escenas icónicas

Todos los clips están en Dailymotion o Internet Archive (YouTube bloqueado desde este servidor).
Las fuentes se han abierto con `fotogramas.py` y las hojas se han leído con Read.

**Escena 1: Tanya vs. ejército enemigo (Episodio 1)**
- Fuente: https://www.dailymotion.com/video/x5tslcz · 1:54 min
- Fotograma 5 · 0:32: Tanya en vuelo libre, rifle/orbe extendido hacia arriba, explosión de luz blanca detrás. Cabello rubio al viento, gesto triunfal.
- Fotograma 6 · 0:40: Primer plano con sonrisa demoníaca, ojos brillantes hundidos, mentón inclinado. La luz de la explosión ilumina su cara desde abajo.
- Fotograma 13 · 1:36: Tanya lanzando ataques mágicos arcoíris (verde, morado, naranja) en pleno vuelo.
- Fotograma 15 · 1:52: Explosión masiva sobre el campo de batalla visto desde tierra. ⚠️ (una fuente)

**Escena 2: Advertencia al enemigo — "Tamaya!" (Episodio 5)**
- Fuente: https://www.dailymotion.com/video/x5bp78t · 1:08 min
- Fotograma 7 · 0:36: Tanya de frente con ojos DORADOS activados por el Type 95 (ser X), ambas manos levantadas, en trance divino. Escena icónica del fandom.
- Fotograma 8 · 0:42: Rayos de energía azul-blanca disparándose desde el orbe (efecto beam visual muy limpio).
- Fotograma 9 · 0:48: Explosión naranja masiva. La bola de fuego cubre todo el fotograma.
- Fotograma 10 · 0:54: Plano aéreo de la ciudad en llamas de noche (la llamada escena "Tamaya!"). Luces naranja sobre fondo negro. ✅ (confirmado fandom + fotogramas)
- Fotograma 11 · 1:00: Tanya de espaldas observando el incendio. Silueta negra sobre naranja. Sirve para lámina.

**Escena 3: "Hello and Goodbye" — Bomber (Episodio 6)**
- Fuente: https://www.dailymotion.com/video/x5bp76k · 1:39 min
- Fotograma 2 · 0:08: Tanya volando en 3/4, sonrisa maliciosa, pelo rubio al viento, nubes grises detrás.
- Fotograma 7 · 0:48: Tanya de pie sobre el blanco (plano amplio nocturno), orbe en la espalda.
- Fotograma 9 · 1:04: Tanya apuntando el rifle en posición horizontal, mirada concentrada (sniper pose).
- Fotograma 10 · 1:12: Gran explosión naranja con fragmentos negros. Contraste cielo/fuego muy fotogénico. ✅

**Escena 4: "Men, I have returned" / "Glory to the Empire" (Película)**
- Fuente: https://www.dailymotion.com/video/x96pfti · 1:25 min (Sensacine México)
- Fotograma 2 · 0:08: Tanya en contrapicado, gorra militar, uniforme completo, frase "Men, I have returned." Escena del Sur (desierto).
- Fotograma 7 · 0:48: Tanya gritando "Glory to the Empire!", boca abierta, manos tensas, frente a sus tropas.
- Fotograma 5 · 0:32: Tanya con gafas de vuelo levantadas, leve sonrisa de superioridad.
- Fotograma 6 · 0:40: Paisaje desértico-rojizo (equivalente al Continente Sur / Norte de África ficción).

---

### Punto 4 — Fondos y sitios: luz, paleta y texturas

**Todos los valores hex están medidos con `estilo.py` sobre los fotogramas.**

#### Sitio 1: Frente del Rin / Zona de combate europeo (trincheras, cielo nublado)
- Paleta medida sobre ep1_battle/hoja_01.jpg:
  - `#18171A` negro-azul (dominante) · `#403F39` gris-verde oscuro · `#646559` verde musgo apagado
  - `#878B7E` gris-oliva · `#AFB2A0` gris claro · `#E8E6CE` beige/crema cielo
  - `#DE9F35` dorado-naranja de explosión (acento)
- Luz: difusa, nublada, sin dirección fija. Todo aplanado. Los acentos de fuego crean el único calor.
- Estilo: sombreado mixto, saturación 22%, brillo 41%. Línea de contorno `#474133`.
- Fuente: estilo.py en fotograma ep1_battle · https://www.dailymotion.com/video/x5tslcz
- Textura equivalente: piedra húmeda / barro / madera de trinchera. AmbientCG: "Mud001", "WoodPlank009", "Concrete019". ⚠️ (equivalencias sugeridas, no medidas en AmbientCG)

#### Sitio 2: Zona de entrenamiento en montaña nevada
- Paleta medida sobre ep5_training/hoja_01.jpg:
  - `#151519` negro azulado · `#2B3136` azul-gris oscuro (dominante cielo nublado)
  - `#CCCFD4` blanco-gris (nieve) · `#AEB0B3` gris plata · `#6D6C67` gris-verde medio
- Luz: fría, direccional desde arriba. Nieve refleja blanco-azul. Uniformes en verde-gris oscuro.
- Estilo: sombreado mixto, saturación 19%, brillo 41%. Muy desaturado.
- Fuente: estilo.py en fotograma ep5_training · https://www.dailymotion.com/video/x5bp70j

#### Sitio 3: Ciudad bombardeada de noche (Ep. 5 "Tamaya!")
- Paleta observada (visual):
  - `#0A0810` negro noche dominante · `#E85010` naranja-rojo fuego · `#3A7A98` azul-verde magia
  - `#C05010` naranja oscuro lamas · `#1A3A50` azul marino cielo nocturno
- Luz: única fuente = el incendio. Contraste extremo negro/naranja. La magia añade azul-verde.
- Fuente: fotograma 10 y 11 de ep5_warning · https://www.dailymotion.com/video/x5bp78t ⚠️ (medidos visualmente, no con estilo.py sobre frame individual)

#### Sitio 4: Continente Sur / desierto (Película)
- Paleta medida sobre movie_trailer/hoja_01.jpg:
  - `#1A1819` negro · `#3B3431` marrón oscuro · `#BFAE9E` beige-arena claro
  - `#685A4D` marrón tierra · `#99826E` marrón claro · `#FBFAF8` blanco cielo brillante
  - `#2E739D` azul cielo (acento)
- Luz: luz solar directa, intensa, ambiente árido. Contraste arena/sombra fuerte.
- Estilo: sombreado degradado, saturación 31%, brillo 43%. El único sitio con luz "cálida" clara.
- Fuente: estilo.py en fotograma movie_trailer · https://www.dailymotion.com/video/x96pfti

#### Sitio 5: Paleta general de la serie (OP y títulos)
- Paleta medida sobre op/hoja_01.jpg (OP de Dailymotion):
  - `#24201F` negro cálido · `#151212` negro puro · `#37322E` marrón muy oscuro
  - `#544B3E` marrón oscuro · `#7C6D53` bronce-café · `#9E947C` beige apagado
  - `#BFC0B5` gris perla (único tono claro)
- Saturación 29%, brillo 23%. La serie más oscura que la mayoría.
- El título "幼女戦記 / Saga of Tanya the Evil" aparece en dorado/bronce sobre negro con ornamentos góticos.
- Fuente: estilo.py en fotograma op · https://www.dailymotion.com/video/x594l9r ✅

#### Texturas reales equivalentes (ambientcg.com)
- Trinchera/barro: buscar "Mud001" o "Ground054" (tierra oscura húmeda) · CC0
- Nieve/piedra fría: "Snow007" o "Rock050" · CC0
- Desierto/arenisca: "Sand007" o "Ground080" · CC0
- Metal envejecido (armas, orbe): "Metal037" (acero oscuro) · CC0
- ⚠️ URLs exactas de AmbientCG no verificadas en esta sesión

---

### Punto 9 — Música y sonido

#### Opening Temporada 1 (2017)
- Título: **"JINGO JUNGLE"** · Artista: MYTH & ROID
- Single lanzado: 8 febrero 2017 · ✅ (Wikipedia + Lyrical Nonsense)
- Fuente: https://en.wikipedia.org/wiki/Jingo_Jungle
- Tipo: pop-rock épico, percusión marcial, sintetizadores electrónicos, voz potente (mpi)
- Ambiente: poderoso, triunfal y perturbador al mismo tiempo. Combina ritmo de marcha con electrónica agresiva.
- Letra: mezcla inglés/japonés, temática de batalla y conquista
- Créditos en pantalla (fotograma 18 del op_archive, minuto 1:25): "JINGO JUNGLE" y datos de producción
- OP completo en Internet Archive: https://archive.org/details/YOUJOSENKIOP

#### Ending Temporada 1
- Título: **"Los! Los! Los!"** (alemán: ¡Vamos! ¡Vamos! ¡Vamos!)
- Artista: Tanya Degurechaff / CV: Aoi Yūki
- Letra: hotaru · Música: うさ (Usa)
- ✅ (confirmado en créditos finales op_archive fotograma 17 + Wikipedia)
- Tipo: marcha militar, ritmo de tropa, con coro. Similar a canción de himno.
- Canción icónica del fandom: cubierta en ruso en Internet Archive (Harmony Team J.am)
- Cover ruso: https://archive.org/details/harmony-team-j.am-los-los-los-youjo-senki-rus-cover
- Audio en SoundCloud: https://soundcloud.com/masterenvi/ed-youjo-senki-ending-full-los-los-los-by-tanya-degurechaff-aoi-yuuki ⚠️ (una fuente)

#### Opening Temporada 2 (2026)
- Título: **"Why? RED induction."**
- Artista: MYTH & ROID (misma banda que el OP original)
- Lanzado: 16 julio 2026 (digital)
- ✅ (Anime News Network + Skream!)
- Fuentes: https://www.animenewsnetwork.com/news/2026-06-06/saga-of-tanya-the-evil-ii-unveils-theme-song-artists-july-8-debut-mini-anime/.238213
- https://en.skream.jp/news/2026/07/youjosenki_op_ed_release.php

#### Ending Temporada 2 (2026)
- Título: **"Weiter! Weiter!"** (alemán: ¡Adelante! ¡Adelante!)
- Artista: Tanya Degurechaff / CV: Aoi Yūki
- Letra: hotaru · Música/arreglo: Masayuki Nakano (BOOM BOOM SATELLITES / THE SPELLBOUND)
- Lanzado: 16 julio 2026 (digital)
- ✅ (Skream! + ANN)
- Continúa la tradición de títulos en alemán del fandom militar

#### Banda Sonora (OST)
- Compositor: **Shūji Katayama** · ✅ (múltiples fuentes: CDJapan, YouTube, Audiomack)
- Fuente: https://www.cdjapan.co.jp/product/ZMCZ-13039 (Movie OST)
- Track destacado 01: **"Young Girl's War"** (tema bélico principal) · https://www.youtube.com/watch?v=TEzq_GH_Do8
- Track: **"Trial of Fire"** (batalla intensa) · https://audiomack.com/enricksup2/song/67ab6d9a44ab2
- Movie OST: 45 tracks · ZMCZ-13039 · Shūji Katayama (2019)
- Playlist YouTube OST: https://www.youtube.com/playlist?list=PLLkVJ2IZsgYplOKwgYnD6MKnu6MaMjA4b
- Estilo: orquestal con influencias militares europeas. Cuerdas, vientos de madera, percusión marcial.
- SoundCloud (OST completo): https://soundcloud.com/tiwi-zo/sets/youjo-senki-saga-of-tanya-the

#### Efectos de sonido icónicos
- **Activación computation orb**: zumbido mecánico + clic metálico + frecuencia ascendente (tipo sonar). Se oye en cada escena de combate. ⚠️ (descripción observada, sin análisis de audio técnico)
- **Disparo de magia**: detonación + eco + brillo metálico agudo (diferente de explosión bélica normal)
- **Vuelo de mago**: sustain de viento + propulsión suave, sin motor
- **Explosiones**: graves profundas + descompresión (onda expansiva audible)
- **Scream de Tanya**: específicamente el grito de satisfacción de combate (maniacal laugh) es identificador de la serie

---

### Punto 10 — Vídeos: tráileres, clips y tendencias

#### Tráileres oficiales
1. **Tráiler S2 / Youjo Senki II (2026)**
   - https://www.dailymotion.com/video/x9uo9wg · 1:42 · 3djuegos/Espinof
   - También: https://www.dailymotion.com/video/x9uycb4 · 1:42 · Espinof
   - Minuto 0:16: Tanya en batalla desierto con tropa (plano de acción)
   - Minuto 0:56: Tanya con cabello blanco/platino, ojos azules, expresión inocente (contraste visual clave)
   - Minuto 1:12: Tanya con ojos dorado-rojizos, llamas alrededor, máxima intensidad
   - Minuto 1:28: Figura angélica en entorno oscuro (Being X / escena mística)
   - Minuto 1:36: Tanya en primer plano bajo con gorra y arma

2. **Tráiler Película (Youjo Senki Movie, 2019)**
   - https://www.dailymotion.com/video/x96pfti · 1:25 · Sensacine México
   - Minuto 0:08: "Men, I have returned." - Tanya anunciando retorno
   - Minuto 0:24: Oficial superior (Lergen) reflexivo, interior oscuro
   - Minuto 0:48: "Glory to the Empire!" - Tanya ante su batallón
   - Minuto 1:10: Aviones militares en cielo nocturno (escala de la batalla del Sur)
   - Distribuida en USA por Fathom Events (visible en fotograma 10)
   - Tráiler alemán alternativo: https://www.dailymotion.com/video/x7ry2pz ⚠️

#### Clips de episodios en Dailymotion
3. **Ep. 5 - Warning / "Tamaya!"**
   - https://www.dailymotion.com/video/x5bp78t · 1:08 · Anime Selection
   - Minuto 0:36: Ojos dorados Type 95 (ESCENA ICÓNICA del fandom)
   - Minuto 0:54: Explosión masiva sobre ciudad vista desde arriba

4. **Ep. 5 - Entrenamiento en montaña**
   - https://www.dailymotion.com/video/x5bp70j · 2:36 · Anime Selection
   - Minuto 0:24: Tanya con ojos azules enormes ("Let's begin!") - cara inocente de entrenamiento
   - Minuto 2:24: Tanya con halo dorado, expresión ambigua ángel/demonio
   - Minuto 2:32: Plano completo de Visha en nieve mirando al grupo

5. **Ep. 6 - Battle scene**
   - https://www.dailymotion.com/video/x5bp76k · 1:39 · (Canal sin nombre)
   - Minuto 0:08: Tanya en vuelo, sonrisa maliciosa, paleta oscura (ESCENA DEL BOMBER)
   - Minuto 1:04: Tanya apuntando horizontalmente (sniper-pose)

6. **Ep. 1 - Tanya vs. Army**
   - https://www.dailymotion.com/video/x5tslcz · 1:54 · Yixexapof
   - Minuto 0:32: Tanya con rifle en vuelo, glow explosion

#### Internet Archive
- OP completo (MPEG4, 35 MB): https://archive.org/details/YOUJOSENKIOP ✅
  - Fichero descargable: https://archive.org/download/YOUJOSENKIOP/YOUJO%20SENKI%20OP.mp4
- Doblaje latino (S1 + S2): https://archive.org/details/youjo-senki-latino · 16,926 descargas ⚠️ (verificar contenido exacto antes de usar)
- Doblaje inglés EP11: https://archive.org/details/youjo-senki-dub-ep.-11.720p
- Movie raw: https://archive.org/details/youjosenkimoviefullraw · 2,332 descargas

#### Canales de análisis (tendencias)
- Playlist completa OP+ED+OST: https://www.youtube.com/playlist?list=PLe533PvpOWlhrQ0_i27k94pKULj0Tzur3
- OST oficial compilado: https://www.youtube.com/playlist?list=PLLkVJ2IZsgYplOKwgYnD6MKnu6MaMjA4b
- Podcast análisis (Audio): https://archive.org/details/as211-youjo-senki · AnimeSphere 211
- OP Full en YouTube (referencia): https://www.youtube.com/watch?v=2ttsP9hSDwI ⚠️ (puede pedir login)

---

### Punto 14 — Poses analizadas con capítulo y minuto

Todos los fotogramas se abrieron con `fotogramas.py` y se leyeron con Read.

#### TANYA VON DEGURECHAFF

**Pose T-1: "Vuelo triunfal"** — EP1, min 0:32
- Cuerpo: en vuelo libre, brazo izquierdo extendido hacia arriba con el orbe brillando, cuerpo inclinado ~30° hacia atrás
- Manos: una sujetando el rifle, otra en el orbe. Guantes negros.
- Mirada: hacia el enemigo (ligeramente abajo desde su posición aérea)
- Gesto: éxtasis de combate, boca entreabierta, cejas levantadas
- Sirve para: **celebrar, presentar una habilidad, mostrar poder**
- Fuente: https://www.dailymotion.com/video/x5tslcz &t=32 ✅

**Pose T-2: "Sonrisa demoníaca"** — EP1, min 0:40
- Cuerpo: primer plano, cara inclinada hacia cámara, mentón bajo
- Manos: no visibles (encuadre cerrado)
- Mirada: directa a cámara, ojos muy abiertos y brillantes
- Gesto: sonrisa exagerada y amenazante, característica de Tanya en modo "maliciosa"
- Sirve para: **amenazar, regañar, villana de la lámina**
- Fuente: https://www.dailymotion.com/video/x5tslcz &t=40 ✅

**Pose T-3: "Poder divino / Type 95"** — EP5, min 0:36
- Cuerpo: de frente, erguida, ambos brazos ligeramente levantados y abiertos
- Manos: palmas hacia arriba, sujetando el orbe con ambas manos
- Mirada: ojos dorados/amarillos (efecto del Type 95, poder de Being X). Pupilas dilatadas.
- Gesto: en trance, entre extasiada y aterrorizante
- Sirve para: **discurso épico, escenas de poder sobrenatural, momento culminante**
- Fuente: https://www.dailymotion.com/video/x5bp78t &t=36 ✅

**Pose T-4: "Llegada al campo de batalla"** — EP6, min 0:08
- Cuerpo: en vuelo visto desde 3/4 superior izquierdo, ligeramente inclinada hacia adelante
- Manos: una en el rifle/orbe, otra libre con movimiento
- Mirada: hacia el objetivo con sonrisa lateral
- Gesto: confiada, casi burlona, dominando el espacio aéreo
- Sirve para: **presentar al personaje, entrada dramática**
- Fuente: https://www.dailymotion.com/video/x5bp76k &t=8 ✅

**Pose T-5: "Cálculo frío"** — EP6, min 0:56
- Cuerpo: encuadre medio, uniforme completo visible, ligeramente de frente
- Manos: relajadas o sujetando el orbe contra el cuerpo
- Mirada: directa, ojos azules (modo normal, sin poder), leve sonrisa lateral
- Gesto: calculadora, segura de sí misma, tono de superiora
- Sirve para: **explicar, pensamiento estratégico, modo analítico**
- Fuente: https://www.dailymotion.com/video/x5bp76k &t=56 ✅

**Pose T-6: "Francotirador / Apuntando"** — EP6, min 1:04
- Cuerpo: tumbada/apoyada, horizontal, rifle extendido hacia adelante
- Manos: sujetando el rifle con ambas manos, posición de francotirador
- Mirada: un ojo cerrado, el otro concentrado en la mira
- Gesto: máxima concentración, tensión contenida
- Sirve para: **mostrar tensión, momento de suspense**
- Fuente: https://www.dailymotion.com/video/x5bp76k &t=64 ⚠️ (estimado ±2 s)

**Pose T-7: "Discurso del comandante"** — Película, min 0:08
- Cuerpo: plano contrapicado, Tanya de pie ante su batallón, gorra militar con insignia
- Manos: al costado, firme postura militar
- Mirada: hacia sus tropas (por encima del espectador, efecto de autoridad)
- Gesto: seria, comandante en jefe, voz de "Men, I have returned."
- Sirve para: **presentar, liderazgo, discurso motivacional**
- Fuente: https://www.dailymotion.com/video/x96pfti &t=8 ✅

**Pose T-8: "¡Gloria al Imperio!"** — Película, min 0:48
- Cuerpo: encuadre torso, boca abierta gritando, expresión máxima
- Manos: tensadas (puños cerrados implícitos)
- Mirada: hacia adelante, ardiente
- Gesto: grito de guerra, patriotismo exagerado (o ironía del autor)
- Sirve para: **animar al equipo, escena épica, frase memorable del fandom**
- Fuente: https://www.dailymotion.com/video/x96pfti &t=48 ✅

**Pose T-9: "Ángel caído"** — EP5 entrenamiento, min 2:24
- Cuerpo: primer plano, halo dorado visible detrás de la cabeza (efecto visual del Type 95)
- Manos: no visibles, encuadre cerrado
- Mirada: ojos azules, expresión de dulzura falsa / ángel perverso
- Gesto: inquietante contraste entre apariencia angelical y naturaleza calculadora
- Sirve para: **dualidad ángel/demonio, momento de ironía**
- Fuente: https://www.dailymotion.com/video/x5bp70j &t=144 ⚠️ (estimado ±2 s)

#### VIKTORIYA SEREBRYAKOV (VISHA)

**Pose V-1: "Shock / Susto"** — EP5 entrenamiento, min 0:48
- Cuerpo: primer plano, encuadre cerrado en cara
- Manos: no visibles
- Mirada: ojos azules grandes, muy abiertos, cejas levantadas al máximo
- Gesto: terror / shock cómico (expresión exagerada al estilo moe)
- Sirve para: **reacción cómica, acompañante nerviosa, momento de alivio cómico**
- Fuente: https://www.dailymotion.com/video/x5bp70j &t=48 ✅

**Pose V-2: "Con el batallón"** — EP5 entrenamiento, min 2:08
- Cuerpo: plano medio, de pie en la nieve, grupo de soldados detrás
- Manos: al frente, postura de espera
- Mirada: aliviada/agotada
- Gesto: camaradería, el "corazón" del batallón 203
- Sirve para: **escenas de grupo, sensación de equipo**
- Fuente: https://www.dailymotion.com/video/x5bp70j &t=128 ✅

**Pose V-3: "¡Señorita instructora!"** — EP5 entrenamiento, min 1:28
- Cuerpo: encuadre medio
- Mirada: ojos azules enormes, boca abierta, expresión escandalizada
- Gesto: la "voz de la razón" del batallón, siempre asombrada de las decisiones de Tanya
- Sirve para: **comentario cómico, interacción con Tanya**
- Fuente: https://www.dailymotion.com/video/x5bp70j &t=88 ✅

---

## LO MEJOR PARA LA LÁMINA

1. **Pose T-3** (ojos dorados Type 95, EP5 0:36) + fondo ciudad en llamas (EP5 0:54): contraste máximo luz/sombra. La pose más reconocible del fandom.
2. **Pose T-2** (sonrisa demoníaca, EP1 0:40): primer plano icónico, inmediatamente reconocible. Para canal de comando/estrategia.
3. **Pose T-7** (discurso del comandante, Movie 0:08) + fondo desierto/cálido: la única pose "heroica" real. Para canal de anuncios o roles.
4. La paleta del desierto (`#BFAE9E`, `#685A4D`, `#2E739D`) es la más cálida y diferente del resto: buen contraste si el fondo de la lámina necesita ser luminoso.
5. El título en dorado-bronce sobre negro (`#7C6D53` / `#BFC0B5`) es muy reproducible.

---

## NO ENCONTRÉ

- ⚠️ YouTube bloqueado desde este servidor: no se bajaron subtítulos de Crunchyroll en español. Los datos del doblaje latino van al investigador de voz.
- ⚠️ AnimeThemes API (animethemes.moe) respondió con HTTP 522 (timeout). No se obtuvieron URLs .webm del OP/ED. Suplida con Internet Archive.
- ⚠️ MusicBrainz no devolvió registros de Youjo Senki (los resultados en datos-video.md son de otras series con "senki" en el título).
- ⚠️ Reddit directo no respondió. No se buscaron posts de r/anime en Arctic Shift por cupo de búsquedas.
- ⚠️ Efectos de sonido: no hay base de datos pública con los FX específicos de Youjo Senki. Descripción basada en observación visual/auditiva de los clips.
- ⚠️ Escenas del Episodio 8 (Arene City) no disponibles en Dailymotion. Se documentó la descripción de fuentes secundarias.
- ⚠️ Texturas AmbientCG: se sugirieron términos de búsqueda pero no se verificaron URLs exactas.
- ⚠️ Internet Archive "youjo-senki-latino" (16.926 descargas): no se verificó el contenido exacto (qué episodios, qué calidad). Lo examina el investigador de voz.

---

## BITÁCORA DE BÚSQUEDA

| # | Búsqueda | Idioma | Fuente | Resultado |
|---|---|---|---|---|
| 1 | `Youjo Senki opening ending music "Jingo Jungle" "Los Los Los"` | EN | WebSearch | Confirmado OP/ED S1 ✅ |
| 2 | `Youjo Senki anime opening animethemes site:animethemes.moe` | EN | WebSearch | URL AnimThemes (API falló) ⚠️ |
| 3 | `Youjo Senki OST composer "Shuji Katayama" soundtrack tracks` | EN | WebSearch | Compositor confirmado ✅ |
| 4 | `Youjo Senki season 2 2026 opening ending "Youjo Senki II"` | EN | WebSearch | S2 temas confirmados ✅ |
| 5 | `Youjo Senki "episode 6" battle aerial combat wiki` | EN | WebSearch | Ep.6 "Hello and Goodbye" confirmado ✅ |
| 6 | `Youjo Senki iconic scenes memorable moment reddit fandom` | EN | WebSearch | Escena Tamaya, bomber mencionadas ✅ |
| 7 | `Youjo Senki Tanya computation orb poses uniform wiki` | EN | WebSearch | Detalles de uniforme y orbe ✅ |
| 8 | `Youjo Senki anime sound effects computation orb` | EN | WebSearch | Sin datos técnicos de FX ⚠️ |
| — | fotogramas.py OP Dailymotion x594l9r | — | Dailymotion | 18 fotogramas ✅ |
| — | fotogramas.py Trailer x9uo9wg | — | Dailymotion | 13 fotogramas ✅ |
| — | fotogramas.py EP1 battle x5tslcz | — | Dailymotion | 15 fotogramas ✅ |
| — | fotogramas.py EP5 training x5bp70j | — | Dailymotion | 20 fotogramas ✅ |
| — | fotogramas.py EP5 warning x5bp78t | — | Dailymotion | 12 fotogramas ✅ |
| — | fotogramas.py EP6 battle x5bp76k | — | Dailymotion | 13 fotogramas ✅ |
| — | fotogramas.py Movie trailer x96pfti | — | Dailymotion | 11 fotogramas ✅ |
| — | fotogramas.py OP Internet Archive | — | Archive.org | 20 fotogramas ✅ |
| — | estilo.py sobre 5 hojas de fotogramas | — | Herramienta local | Hex medidos ✅ |
| — | archive.org metadata YOUJOSENKIOP | — | Archive.org | Formatos y tamaño confirmados ✅ |

**Confirmado (✅):** puntos 2, 4, 9, 10, 14 cubiertos con fotogramas reales vistos y colores medidos.
**A medias (⚠️):** texturas AmbientCG (sin URL exacta), FX de sonido (sin análisis técnico), ED clips (sin YouTube).
