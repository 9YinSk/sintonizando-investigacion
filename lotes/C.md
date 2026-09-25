# Lote C: repasos 19-30

Sesión: https://claude.ai/code/session_013xa9LevYk3W3Dk4tmJzsjh · rama `claude/ecstatic-bardeen-wwjh43`
Cuenta: cuenta A109

Lo lleva desde las 03:16 UTC del 25 (juntada con todas las ramas a las 03:10, sin choques).
Antes: sesión https://claude.ai/code/session_01EZ7MFsW25Y7werqrTRzCEV (rama
`claude/trusting-davinci-274hb9`, hasta las 22:59 del 24) y la central,
https://claude.ai/code/session_01RJL7rbu6HGiYoChtxomcbb (rama `claude/lote-a-series-inxhbf`),
que lo tomó a las 02:45 y se quedó sin saldo enseguida: no subió nada más después de las 02:43.

## Estado (03:16 UTC del 25)

- 23 Lilo & Stitch: voz y vídeo acaban en «Sigue:» y ya llevan sus 2 tandas: no se
  relanzan. Redactor (Opus, repaso) en marcha desde las 03:16; marca ⚠️ lo que falte.
- 24 Assassination Classroom: los investigadores de la central no llegaron a escribir
  nada. 4 investigadores nuevos (Sonnet, repaso) en marcha desde las 03:16.
- 25-30: datos recolectados; faltan sus equipos.

**Si esta cuenta se corta:** la siguiente cuenta del lote C sigue así:
`herramientas/juntar.sh`, `echo C > .lote` y `siguiente.py 5 --lote C`.
- 23: si `revisar.py 23-lilo-stitch` no da COMPLETA, relanza sólo su redactor (repaso)
  para lo que falte; no relances voz ni vídeo.
- 24: relanza sólo los roles cuya parte falte o acabe en «Sigue:» (desde donde quedó).
- **19 Doraemon: COMPLETA y subida.** 2434 líneas, ✅27 ⚠️12 ❌0, 243 referencias,
  124 webs, 134 minutos citados, 79 hex, 3 hojas.
- **20 Dr. Stone: COMPLETA y subida.** 2498 líneas, ✅27 ⚠️11 ❌0, 183 referencias,
  92 webs, 166 minutos citados, 87 hex, 3 hojas.
- **21 Spider-Verse: COMPLETA y subida.** 2584 líneas, ✅28 ⚠️11 ❌0,
  197 referencias, 137 webs, 134 minutos citados, 55 hex, 3 hojas.
- **22 Violet Evergarden: COMPLETA y subida.** 2396 líneas, ✅24 ⚠️8 ❌0,
  168 referencias, 116 webs, 270 minutos citados, 34 hex, 3 hojas.
- Datos recolectados (gratis) para 19-30 (lote C entero).

## Avisos para el dueño

- Desde las 03:16 los commits de `subir.sh` y `guardar.sh` de este lote llevan el enlace
  `Claude-Session` de otra sesión (session_01PTjYZQejJbQf4MSwH4sQbi): no cambié esos dos
  archivos. Cada cuenta nueva que cambia esa línea hace que su rama choque en esos dos
  archivos con cualquier otra que también la haya cambiado, y entonces `juntar.sh` no
  junta esa rama.
- 19 Doraemon: la descripción del canal de recursos en servidor/inventario.md
  está cortada («ni cracks ni prog…»); hay que confirmar cómo termina antes
  de rotular la lámina. Sigue sin decidirse qué significa la etiqueta
  «Verificado». No hay clips oficiales doblados al latino: las 3 frases
  textuales salen de una grabación de TV en Internet Archive, transcrita con
  Whisper. Quedan sin encontrar (⚠️): la rabia de Doraemon y la vergüenza de
  todos con minuto, las poses de Shizuka/Suneo/Dorami vistas en vídeo, y el
  sonido del invento (dos versiones según la fuente).
- 20 Dr. Stone: corrección importante, el pelo de Senku es verde salvia
  `#5D906A` (no `#7DBF4A`) y su túnica es crema `#F5EBD6` (no blanca); el
  dinero Drago son monedas acuñadas, no billetes; y en el doblaje latino Gen
  habla normal, su jerga al revés no se adaptó. Quedan sin encontrar (⚠️):
  frases textuales del doblaje latino con minuto (YouTube pide iniciar
  sesión), la ropa de Gen medida, las poses de Gen y Kaseki en vídeo, y las
  vistas de los fandubs.
- 21 Spider-Verse: el punto 13 (cara en cada emoción) queda ⚠️, sólo 7 de 25
  combinaciones tienen fotograma y minuto; Miguel y Hobie no tienen ninguna
  (no hay clips suyos en Dailymotion y YouTube bloquea). También quedan ⚠️
  los hex de los trajes de Miles y Hobie, posturas de Peter B./Miguel/Hobie,
  comida favorita de 3 personajes y 2 frases icónicas en latino.
- **22 Violet Evergarden — decisión pendiente:** su biblia propone para
  #poemas «la hoja en la máquina de escribir», pero la biblia 33-frieren
  (aún sin repasar) también propone algo para #poemas («diario con pluma y
  tintero en luz dorada»). Hay que decidir qué serie se queda ese canal
  antes de hacer las láminas. Del doblaje latino sólo hay 2 frases
  textuales (audio de Doblaje Wiki, no clip oficial) y ningún fotograma
  llega a 1080p (YouTube pide iniciar sesión).

## Costos

| Serie | Rol | Modelo | Minutos | Tokens |
|---|---|---|---|---|
| 19 | imagen | Sonnet | 29 | 245 mil |
| 19 | vídeo | Sonnet | 18 | 197 mil |
| 19 | voz | Sonnet | 16 | 217 mil |
| 19 | voz (Sigue) | Sonnet | 12 | 199 mil |
| 19 | texto | Sonnet | 11 | 172 mil |
| 19 | redactor | Opus | 18 | 344 mil |
| 20 | imagen | Sonnet | 16 | 245 mil |
| 20 | vídeo | Sonnet | 15 | 214 mil |
| 20 | voz | Sonnet | 14 | 213 mil |
| 20 | texto | Sonnet | 13 | 219 mil |
| 20 | redactor | Opus | 16 | 328 mil |
| 21 | imagen | Sonnet | 10 | 222 mil |
| 21 | vídeo | Sonnet | 12 | 200 mil |
| 21 | voz | Sonnet | 13 | 236 mil |
| 21 | voz (Sigue) | Sonnet | 10 | 191 mil |
| 21 | texto | Sonnet | 11 | 180 mil |
| 21 | redactor | Opus | 17 | 333 mil |
| 22 | imagen | Sonnet | 13 | 205 mil |
| 22 | vídeo | Sonnet | 16 | 199 mil |
| 22 | voz | Sonnet | 17 | 218 mil |
| 22 | voz (Sigue) | Sonnet | 9 | 114 mil |
| 22 | texto | Sonnet | 10 | 167 mil |
| 22 | redactor | Opus | 15 | ~330 mil |
