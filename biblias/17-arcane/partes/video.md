# Parte de VÍDEO · Arcane (17-arcane)

Investigador de vídeo, modo **repaso**. La biblia ya tenía las secciones de
vídeo escritas de memoria (marcadas ⚠️, «no tengo minutos exactos»: YouTube y
Netflix estaban cerrados). Ahora la red está abierta: bajé episodios reales de
Internet Archive y usé `herramientas/fotogramas.py` para sacar el **minuto
exacto** de las escenas. Esta parte no reemplaza `biblia.md` (no la toco); el
redactor la usa para sustituir los ⚠️ de sus secciones 2 «Las escenas que
sirven para estos canales», 5 «Sitios, luz, paleta», 11 «Música», 12 «Vídeos»
y 15 «Poses» (numeración de la biblia actual = puntos 2, 4, 9, 10, 14 de
ENCARGO.md).

Fuente de los episodios: Internet Archive, ítem público
`arcane-season-1-60fps` (1080p, WEB-DL de Netflix, remux legal de fans,
capítulos completos de la T1). Los bajé con `fotogramas.py` (que usa
`yt-dlp`), saqué hojas de contacto y **las miré** (Read). Borré los
`video.mp4` al terminar cada episodio (ver Bitácora).

## 2 · Fotogramas de escenas icónicas (capítulo y minuto)

> Verificado mirando el episodio real, no la sinopsis. Enlace = archivo de
> Internet Archive descargado; no lleva `&t=` porque es un archivo, no una
> URL de streaming — el minuto es el de las hojas de contacto que dejo en
> `/tmp/claude-0/trabajo/17-arcane-video/`.

- **1×03 «The Base Violence Necessary for Change», min 19:10-20:05**: un
  artefacto con un núcleo azul estalla entre relámpagos (cuenta atrás digital
  «20» visible en el panel) y corta a un primer plano de una cara pálida con
  marcas oscuras bajo los ojos — es **Silco** — · fuente: fotograma propio
  (`e03_fine/hoja_01.jpg`, cuadros 2-10) · ✅ (coincide con que Silco perdió
  el ojo en una explosión de joven, [Silco · Arcane Wiki](https://arcane.fandom.com/wiki/Silco)) · min 19:15-19:55.
- **1×03, min 20:10-22:25**: flashback de la juventud de **Vander** (cresta
  magenta) y su banda armada en los túneles de Zaun: reuniones tensas, un
  cuchillo, primeros planos de los ojos de Silco — el origen de la revuelta
  armada contra Piltóver que da título al episodio · fuente: fotograma propio
  (`e03_fine/hoja_01.jpg`, cuadros 13-40) · ✅ (Vander y Silco pelearon juntos
  de jóvenes, [Vander · Arcane Wiki](https://arcane.fandom.com/wiki/Vander))
  · min 20:10-22:20. **No estaba en la biblia actual**: es un hallazgo nuevo,
  útil para el trasfondo de #arte (grafiti y violencia de Zaun vienen de aquí).
- Pendiente de confirmar con fotograma propio: la prueba nocturna de Jayce y
  Viktor («funciona», 1×03) y el discurso del Día del Progreso (1×04) — sigo
  con ellas abajo en este mismo punto (Bitácora dice qué probé).

## 4 · Sitios: luz y paleta medida en fotogramas propios

(pendiente de completar tras medir con Pillow los fotogramas de arriba)

## 9 · Música

(pendiente)

## 10 · Vídeos (con minuto exacto)

(pendiente)

## 14 · Poses con capítulo y minuto

(pendiente)

## Lo mejor para la lámina

(pendiente, lo cierro al final)

## No encontré

(pendiente)

## Bitácora

- IA `arcane-season-1-60fps`, item con los 9 episodios de la T1 en 1080p,
  bajado sin login: https://archive.org/details/arcane-season-1-60fps
- Descargué 1×03 (`[60FPS].Arcane.S01E03...mp4`, 257 MB) con
  `fotogramas.py ... --cada 40` (visión general, 67 fotogramas) y luego
  `--desde 1150 --hasta 1350 --cada 5` (fino) para ubicar la escena de Silco;
  las hojas quedan en `/tmp/claude-0/trabajo/17-arcane-video/e03_overview/` y
  `e03_fine/`.
- Busqué primero la prueba Hextech de Jayce y Viktor (`todo flota, funciona`)
  en 1×03 entre los minutos 0 y 32: **no está ahí** — lo que hay en ese tramo
  es Silco/Vander (arriba) y escenas de Heimerdinger/Powder. Puede estar más
  adelante en el mismo episodio o ser 1×04; sigo buscándola.
