# Parte · Investigador de vídeo — 19-doraemon (Doraemon)

Puntos de ENCARGO.md: **2** (escenas icónicas), **4** (sitios: luz y paleta
medida), **9** (música), **10** (vídeos con minuto exacto), **14** (poses
analizadas con minuto).

> Cómo se hizo: la `biblia.md` actual se escribió con la red cerrada
> (YouTube, Fandom, dora-world… bloqueados); todos sus minutos de escena
> salen de **subtítulos** (deducidos, no vistos: "no pude ver vídeo ni
> imágenes" dice el propio §15). El aviso del jefe es exacto: **0 de los 15
> minutos citados** pasan como "minutos vistos" porque nunca se abrió un
> vídeo de verdad. Esta parte corrige eso: **sí miré vídeo real**, de fuentes
> alternativas a YouTube (que en este servidor pide iniciar sesión):
> **Dailymotion** (funciona, API + `fotogramas.py`), **Internet Archive**
> (funciona para búsqueda; los "capítulos completos" que probé eran vídeos
> cortos mal etiquetados). AnimeThemes dio error 522 (caído) en todos los
> intentos, a distintas horas; no lo pude usar. Herramientas: `fotogramas.py`
> (fotogramas con minuto y enlace `&t=`), `estilo.py` (paleta hex medida con
> Pillow) y `voz.py` (transcripción real de la canción de apertura, Whisper).
> Esperé unos 9 minutos a que apareciera `partes/datos-video.md` del
> recolector (el jefe avisó que lo estaba corriendo) y no llegó a
> aparecer en esta tanda; seguí por mi cuenta con las fuentes directas,
> como indica el arranque.

---

## Punto 2 y 10 · Vídeos y escenas mirados de verdad, con minuto real

Todo lo de esta tabla lo **vi** (fotograma sacado con `fotogramas.py`,
**no** deducido de subtítulo). El minuto es el de la fuente citada; puede
moverse 1-2 s según la copia (aviso ya en la biblia principal).

| Qué | Fuente (Dailymotion) | Minuto visto | Qué se ve | Para qué sirve |
|---|---|---|---|---|
| **Opening** 1979 «Doraemon no Uta», doblaje latino antiguo, título en pantalla «Doraemon, el gato cósmico» | [x8k1ck8](https://www.dailymotion.com/video/x8k1ck8?t=5) ✅ (contenido = animación original de 1979, confirmado por la letra cantada, ver Música) | 0:05, 0:20, 0:40 | 0:05 Doraemon sale de un túnel azul girando con el brillo del reloj/insignia; 0:20 Doraemon de pie sonriente sobre una luna creciente con estrellas; 0:40 vuela con el Takecopter sobre un fondo de bocetos de Leonardo da Vinci (máquinas voladoras), con Nobita, Shizuka, Suneo y Gigante mirando hacia arriba | luz y paleta del opening (abajo); pose de vuelo de Doraemon |
| **Ending**, doblaje de España («Castellano», no latino ⚠️) | [x2vhonl](https://www.dailymotion.com/video/x2vhonl?t=10) ⚠️ (una sola fuente; vídeo muy descolorido, posible copia de VHS) | 0:10 | cielo con nubes claras y, a lo lejos, siluetas de niños de pie en un cerro | sólo sirve para el **tono pastel del cierre**, no para el doblaje latino |
| **Tráiler** oficial en español de *Stand by Me Doraemon* (mezcla con anuncio «Esta Navidad, Doraemon…», que es de la secuela de 2020/2021 ⚠️ — el vídeo puede juntar clips de las dos películas bajo el mismo título) | [x33a56v](https://www.dailymotion.com/video/x33a56v?t=30) ✅ (marca «STAND BY ME DORAEMON Trailer 1 Oficial Español», subida verificable en Dailymotion) | 0:03 cartela «Esta Navidad, Doraemon…»; 0:30 Nobita 3D choca con la puerta corrediza de su cuarto, cabizbajo, con la mochila puesta; 1:00 Doraemon y Nobita gritan juntos, agarrados, sobre el tatami; 1:20 primer plano oscuro de un peluche/figura de Doraemon sonriendo en la pared | luz 3D real del cuarto (abajo); pose de susto conjunta |
| **Escena icónica 1** — Gigante da su recital en el descampado | [x3402n2](https://www.dailymotion.com/video/x3402n2?t=20) ✅ (coincide con lo ya citado por subtítulo en la biblia: 2006-09-08 «Empieza el recital») | 0:05, 0:20, 0:40 | Gigante con esmoquin blanco y capa roja, ojos cerrados, boca muy abierta, brazo izquierdo extendido, micrófono en la mano derecha, confeti cayendo con focos de colores detrás | **presentar / celebrar** — pose de Gigante con el micrófono (la «pista sin voz» del canal) |
| **Escena icónica 2** — Doraemon y Nobita gritan abrazados en el cuarto (de noche, sólo luz de ventana) | [x33a56v](https://www.dailymotion.com/video/x33a56v?t=60) ✅ (mismo tráiler de arriba) | 1:00 | ambos en primer plano, boca abierta, sobre el tatami, con la cómoda de madera oscura detrás; luz muy baja, casi a contraluz | **sorpresa / susto** compartido; referencia de luz nocturna del cuarto |
| **Escena icónica 3** — Gigante, asustado, dentro de lo que parece una cabina o nave (⚠️ película no identificada con certeza; posible una de las películas de ciencia-ficción de Doraemon) | [x2uugoz](https://www.dailymotion.com/video/x2uugoz?t=25) ⚠️ (copia con texto de canal pirata superpuesto todo el clip; la animación sí es original) | 0:10, 0:25 | Gigante con camiseta turquesa a rayas, ojos muy abiertos, cejas en zigzag, junto a un personaje con hombrera lila/dorada tipo uniforme; consola verde oscuro alrededor | expresión de **sorpresa/miedo** de Gigante (para el punto 14 de voz/personajes, no descrita aquí) |

> No cuento el **sonido de sacar un invento** (§12 de la biblia, enlace
> YouTube `8PCLcvDnuh0`) porque no lo encontré en Dailymotion ni Internet
> Archive con ese mismo corte; sigue sin minuto. Búsquedas: «doraemon sonido
> invento antes despues», «doraemon effect sound compilation» (Dailymotion,
> sin resultado igual).

---

## Punto 4 · Sitios: luz y paleta medida en fotogramas (Pillow, `estilo.py`)

Reemplaza/({complementa}) la tabla «Paleta ⚠️» de la biblia (§5.2), que sale
de paletas de fans y de memoria. Esta paleta sale de **fotogramas reales**,
citados arriba, medidos con `herramientas/estilo.py`.

| Sitio / toma | Fotograma | Paleta medida (hex, % de píxeles) | Estilo de sombreado |
|---|---|---|---|
| **Túnel del tiempo** (opening, 0:05) | [x8k1ck8 ?t=5](https://www.dailymotion.com/video/x8k1ck8?t=5) | `#0F1113` 25% · `#2F4863` 23% · `#3F728B` 17% · `#81947F` 12% · `#173640` 12% ✅ | degradado/pintado, línea fina `#505F59`, saturación 43%, brillo 39% |
| **Cielo nocturno / luna** (opening, 0:20) | [x8k1ck8 ?t=20](https://www.dailymotion.com/video/x8k1ck8?t=20) | `#101012` 50% · `#1E1F24` 21% · `#908D7A` 13% (luna) · `#363436` 9% ✅ | degradado, muy oscuro (brillo 20%) |
| **Fondo «bocetos de Da Vinci»** (opening, 0:40) | [x8k1ck8 ?t=40](https://www.dailymotion.com/video/x8k1ck8?t=40) | `#8D6E41` 33% · `#9E8359` 30% · `#131112` 23% · `#674B29` 11% ✅ | sepia/pergamino, línea `#474032` |
| **Descampado de noche, recital de Gigante** | [x3402n2 ?t=20](https://www.dailymotion.com/video/x3402n2?t=20) | `#395A81` 20% (cielo azul noche) · `#CA5E41` 16% (foco naranja) · `#F0AD76` 12% (piel con luz cálida) · `#803520` 10% ✅ | degradado, saturación 42%, brillo 61% (por los focos) |
| **Cuarto de Nobita, de noche/atardecer, luz de ventana** (tráiler 3D, 1:00) | [x33a56v ?t=60](https://www.dailymotion.com/video/x33a56v?t=60) | `#0F0905` 35% · `#2F2313` 27% · `#1C0E05` 20% (cómoda de madera oscura) · `#3E372C` 9% ✅ | degradado/pintado 3D, saturación 62%, **brillo muy bajo (13%)**: la habitación real está casi a oscuras salvo un rayo de luz de ventana |
| **Cuarto de Nobita, de día** (tráiler 3D, 0:30) | [x33a56v ?t=30](https://www.dailymotion.com/video/x33a56v?t=30) | `#A09B7F` 47% · `#B8B495` 26% (puertas correderas claras) · `#70624C` 15% · `#F9F9E1` 5% ✅ | tonos crema/beige, brillo 61% — de día la habitación es mucho más clara que de noche |
| **Cielo del ending** (pastel, plano) | [x2vhonl ?t=10](https://www.dailymotion.com/video/x2vhonl?t=10) | `#B6B2B5` 62% · `#96A9B4` 17% · `#67788F` 9% ⚠️ (copia descolorida, puede no ser el color real) | **sombreado plano (cel)**, sin degradado — distinto del 3D del tráiler |
| **Consola/nave, escena 3** | [x2uugoz ?t=10](https://www.dailymotion.com/video/x2uugoz?t=10) | `#303525` 36% (verde oliva oscuro) · `#D7CDC1` 31% (crema) · `#3D4A53` 14% · `#CD544B` 7% ⚠️ (película sin identificar) | degradado, línea normal `#D86860` |

**Lectura para la lámina**: la serie clásica en 2D usa **sombreado plano**
(cel, sin degradado, como el ending) y colores saturados de foco (recital);
las películas 3D (*Stand by Me*) usan **degradado pintado** con luz mucho
más dramática (el cuarto pasa de brillo 61% de día a 13% de noche con un
solo rayo de ventana). Para el canal #recursos (de día, informativo) conviene
la paleta clara del cuarto de día (`#A09B7F`/`#B8B495`/`#F9F9E1`) y no el
azul-negro del túnel, que es más para escenas de acción.

---

## Punto 9 · Música (confirmación con audio real)

- **Transcripción real** (Whisper, `voz.py`, modelo *small*, es) del
  opening [x8k1ck8](https://www.dailymotion.com/video/x8k1ck8?t=13):
  - `0:13` → **«Doraemon, el gato cósmico»** ✅ (se canta el título)
  - `0:16` → «Ojalá mi sueño se…» ✅ (frase cortada; el resto de la canción
    no lo transcribió bien Whisper, típico con canto)
  - Voz: registro medio (183 Hz), **muy expresiva** (31.3 semitonos),
    velocidad lenta (1.59 palabras/s).
- **Esto es un dato nuevo, no un error**: la biblia principal (§11) sólo
  cita el opening de **Maggie Vera**, con la letra «Shalalalala, en mi
  corazón…» (de Doraenciclopedia). La canción que transcribí aquí, con la
  **misma música de "Doraemon no Uta" pero otra letra** («Doraemon, el gato
  cósmico… Ojalá mi sueño se…»), es el **doblaje latino más antiguo**
  (Mexicanto/Chilevisión, años 80-90, la propia bitácora de la biblia ya
  lo menciona como «El gato cósmico», bitácora #5-#6) ⚠️ **dos openings
  latinos distintos con la misma música**, no una confusión: uno viejo
  (Chilevisión/México, "el gato cósmico") y otro más nuevo, de 2005 (Maggie
  Vera, "Shalalalala"). Confirmar el intérprete exacto del más viejo queda
  pendiente (no sale cantante en el vídeo ni en su ficha de Dailymotion).
- Punto ya cubierto por la biblia (openings/endings en japonés, tabla de 62
  temas): no repito esa parte, sólo añado la confirmación de audio.

---

## Punto 14 · Poses confirmadas con fotograma real (no deducidas)

La biblia principal (§15) avisa: *"cada pose sale de lo que dice el
subtítulo... la postura la deduzco"*. Estas sí están **vistas**:

| Personaje | Fotograma visto | Postura real (lo que se ve, no se deduce) | Sirve para |
|---|---|---|---|
| **Doraemon** | [x8k1ck8 ?t=40](https://www.dailymotion.com/video/x8k1ck8?t=40) | vuela con el Takecopter (aspa en la cabeza), brazos abiertos, sonrisa amplia, cuerpo inclinado hacia delante en el aire | **explicar/acción** — enseñar un invento en movimiento |
| **Doraemon** | [x33a56v ?t=60](https://www.dailymotion.com/video/x33a56v?t=60) | boca muy abierta en grito, un brazo levantado, agarrado a Nobita, sobre el tatami | **sorpresa/susto** (reacción conjunta) |
| **Nobita** | [x33a56v ?t=30](https://www.dailymotion.com/video/x33a56v?t=30) | encorvado, cabeza gacha, mochila puesta, choca de espaldas contra la puerta corredera | **cansancio/abatimiento**, entrada a su cuarto |
| **Gigante** | [x3402n2 ?t=20](https://www.dailymotion.com/video/x3402n2?t=20) | de pie, ojos cerrados, boca muy abierta, un brazo extendido al público, micrófono en la otra mano, capa roja al viento | **presentar/celebrar** — pose «recital» (la más citada por la biblia como icónica de Gigante) |
| **Gigante** | [x2uugoz ?t=10](https://www.dailymotion.com/video/x2uugoz?t=10) ⚠️ película sin identificar | cejas en zigzag, ojos muy abiertos y redondos, boca entreabierta, quieto | **sorpresa/miedo** |
| Grupo (**Nobita, Shizuka, Suneo, Gigante**) | [x8k1ck8 ?t=40](https://www.dailymotion.com/video/x8k1ck8?t=40) | los 4 de pie en fila, cabeza inclinada hacia arriba, mirando a Doraemon volar | **admirar/seguir con la mirada** — pose de grupo mirando un invento en el aire |

No pude confirmar con fotograma real las poses de **Shizuka y Suneo por
separado** ni de **Dorami**: no encontré clips limpios en Dailymotion con
esos personajes solos (búsquedas abajo). Esas 5 poses de la biblia (§15)
siguen con el aviso "deducida de subtítulo, no vista" tal cual estaba.

---

## Lo mejor para la lámina

1. **Pose de Gigante con micrófono** (recital, `x3402n2?t=20`): la más
   clara para el ícono de «pista sin voz» — capa roja, confeti, foco.
2. **Cuarto de Nobita de día**, paleta clara medida (`#A09B7F`/`#F9F9E1`,
   `x33a56v?t=30`): mejor luz de fondo que el túnel azul oscuro para un
   canal de recursos (de uso diario, no de acción).
3. **Doraemon con Takecopter** (`x8k1ck8?t=40`) sobre fondo de bocetos
   técnicos (Da Vinci): encaja literal con un foro de "programas y
   plantillas" — Doraemon "inventando/mostrando" con planos alrededor.
4. Contraste de sombreado confirmado: **serie clásica = plano (cel)** vs.
   **películas 3D = degradado dramático**; para no mezclar estilos en la
   lámina, conviene fijar uno solo.
5. El opening viejo «el gato cósmico» (con su propia letra, ≠ Maggie Vera)
   es un dato para el investigador de voz/personajes: hay **dos** openings
   latinos con historia propia, no uno.

---

## No encontré ⚠️

- **AnimeThemes** (`api.animethemes.moe`): error 522 en todos los intentos
  a distintas horas (busqué `filter[slug]=doraemon` y `search?q=doraemon`).
  No pude sacar sus `.webm` oficiales de OP/ED.
- **YouTube**: pide iniciar sesión en este servidor (confirmado, como avisa
  el arranque); no lo usé en ningún momento de esta parte.
- **El sonido de "sacar un invento"** (antes/después) con minuto propio: no
  lo encontré fuera de YouTube.
- **Escena del padre de Shizuka** (el discurso de la boda, ya citado por
  subtítulo en la biblia en 01:08:32 de *Stand by Me*): busqué clips en
  Dailymotion («stand by me doraemon escena mas triste», «doraemon nobita
  shizuka boda padre discurso») y no salió un clip limpio; sigue con el
  minuto de subtítulo, sin fotograma visto.
- **Poses vistas de Shizuka, Suneo y Dorami por separado**: no hallé clips
  limpios de Dailymotion con ellos solos (casi todo son compilaciones
  genéricas "doraemon and nobita" o contenido en hindi/indonesio con texto
  superpuesto).
- **`partes/datos-video.md`** del recolector: no apareció en los ~9 minutos
  que esperé dentro de esta tanda; si aparece después, revisar si trae
  fuentes de AnimeThemes que aquí no pude alcanzar.
- **`partes/episodios.md`**: no existe en esta carpeta; no había ficha de
  capítulo completo que revisar.

---

## Bitácora de búsqueda (esta parte)

- Confirmado con red abierta: **Dailymotion** (API `api.dailymotion.com`,
  sin cupo, no cuenta como "búsqueda web") e **Internet Archive**
  (`archive.org/advancedsearch.php`) sí responden. **AnimeThemes**
  (`api.animethemes.moe`) no respondió nunca (522/timeout).
- Búsquedas por la API de Dailymotion (no gastan el cupo de WebSearch):
  `doraemon opening`, `doraemon opening latino`, `doraemon ending`,
  `doraemon ending latino`, `Doraemon gato cosmico Maggie Vera`,
  `Doraemon el gato cosmico opening`, `stand by me doraemon trailer latino`,
  `doraemon desfile de inventos stand by me`, `stand by me doraemon final
  scene farewell`, `doraemon museo artilugios secretos trailer`, `doraemon
  gigante canta recital`, `doraemon puerta cualquier lugar escena`,
  `doraemon dorayaki escena`, `doraemon descampado tuberias escena`,
  `doraemon habitacion nobita escena`, `doraemon capitulo completo español
  latino`, `stand by me doraemon escena mas triste`, `doraemon nobita
  shizuka boda padre discurso`, `doraemon llorando escena`, `nobita cero
  examen doraemon`.
- Internet Archive: `q=doraemon` (2187 resultados, sobre todo reproducciones
  de fans y un ítem de audio con la canción de Kumiko Osugi) y
  `title:("stand by me" doraemon)` (15 resultados: DVDs ISO, bandas sonoras,
  doblajes al inglés/hindi/tagalo — ninguno es la fuente que necesitaba con
  minuto limpio, así que seguí con Dailymotion).
- `herramientas/fotogramas.py` sobre 6 vídeos de Dailymotion (opening,
  ending, tráiler ×2 tandas, 3 escenas): **17 fotogramas** sacados y
  **mirados con Read** (no sólo generados).
- `herramientas/estilo.py` sobre **8 fotogramas** para paleta y tipo de
  sombreado (túnel, luna, fondo Da Vinci, recital, cuarto ×2, ending,
  consola).
- `herramientas/voz.py` sobre el opening (`x8k1ck8`, modelo *small*, es):
  transcripción con minuto real, ver Música arriba.
- Comprobé `partes/datos-video.md` cada pocos minutos (dos esperas de
  ~4-5 min cada una, ~9 min en total): no llegó a existir en esta tanda.

Sigue: nada obligatorio pendiente de los puntos 2, 4, 9, 10 y 14 (ver tabla
de "No encontré" para lo que sí falta, que es material extra, no lo mínimo
pedido). Si aparece `partes/datos-video.md` más tarde, revisarlo por si trae
fuentes de AnimeThemes u otras escenas con Shizuka/Suneo/Dorami solos.
