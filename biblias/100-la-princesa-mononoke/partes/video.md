# Parte VÍDEO — La princesa Mononoke (puntos 2, 4, 9, 10, 14 de ENCARGO.md)

Investigador de vídeo. Punto de partida: `datos-video.md`. Película de Studio Ghibli
(1997, 133 min), no serie: no hay "capítulo", los minutos son de metraje corrido.
Fuente de vídeo principal para mirar fotogramas: copia de Internet Archive en
1920×1040 (`archive.org/details/1997-mononoke-hime-la-princesa-mononoke`, sin
licencia declarada, copyright Studio Ghibli/Tokuma/Toho — sólo referencia
interna, nunca para publicar el fotograma suelto). Copia de trabajo en
480 p (`archive.org/details/so-3f-cb-vwqm-0-d`) usada para localizar escenas
barato antes de sacar el fotograma en HD. Todos los fotogramas citados aquí
se miraron de verdad (Read de la imagen), no son suposición.

## Punto 2 — Fotogramas de escenas icónicas (1080p+, minuto exacto)

Todos sacados en 1920×1040 por streaming HTTP directo del archivo de Internet Archive
(sin descargar los 2 GB completos, con `ffmpeg -ss <s> -i <url_directa>`), mirados con Read.
Enlace de cada uno: `https://archive.org/details/1997-mononoke-hime-la-princesa-mononoke?t=<segundo>`.

- **Ashitaka tensando el arco sobre un tronco**, mirada fija, defendiendo la aldea del jabalí
  maldito (Nago) · min 0:04:20 (t=260) · ✅ (visto en fotograma HD + confirmado en la hoja de
  contacto de apertura `curse_open/hoja_01.jpg`) · 1920×1040.
- **La maldición ataca la aldea**: Nago cubierto de zarcillos negros retorciéndose, aldeanos
  huyendo, Ashitaka interviene y recibe la marca en el brazo · min 3:00–6:40 (t=180–400) ·
  ✅ (9 fotogramas mirados, hoja `curse_open/hoja_01.jpg`) · 894×480 (copia de trabajo).
- **San carga a Ashitaka herido a la espalda** por el bosque profundo, mirándolo de reojo,
  con una mariposa posada en su hombro · min 0:26:10 (t=1570) · ✅ (fotograma HD +
  hoja `san_intro/hoja_01.jpg`) · 1920×1040.
- **Okkoto (jabalí blanco gigante) y San** de pie junto a Ashitaka desmayado, con Yakul al
  lado; primer encuentro de San protegiendo a Ashitaka en el bosque · min 1:12:05 (t=4325) ·
  ✅ (fotograma HD + hoja `shishigami/hoja_01.jpg`) · 1920×1040.
- **San gruñendo como loba, colmillos fuera**, defendiendo a Ashitaka delante de la manada ·
  min 1:10:25 (t=4225) · ✅ (fotograma HD + hoja) · 1920×1040.
- **Moro enseñando los colmillos** a la luz de la luna, ojos entornados, amenazante ·
  min 1:21:00 (t=4860) · ✅ (fotograma HD + hoja `moro_roca/hoja_01.jpg`) · 1920×1040.
- **San con la cara pintada de guerra, gritando**, primer plano de furia tras el ataque a
  Irontown · min 0:53:00 (t=3180) · ✅ (fotograma HD + hoja `san_sangre/hoja_01.jpg`) ·
  1920×1040.
- **San atrapada entre los tentáculos oscuros de la maldición** (batalla final de los
  jabalíes), cara de dolor y miedo · min 1:43:45 (t=6225) · ✅ (fotograma HD + hoja
  `okkoto/hoja_01.jpg`) · 1920×1040.
- **El Nightwalker** (forma nocturna del Shishigami/dios ciervo), silueta gigante
  traslúcida azul con kodamas flotando alrededor, tras perder la cabeza · min 1:54:00
  (t=6840) · ✅ (fotograma HD + hoja `final/hoja_01.jpg`) · 1920×1040.
- **Ashitaka y San se abrazan por detrás**, escena final antes de separarse (él se queda
  en Irontown, ella vuelve al bosque) · min 1:56:00 (t=6960) · ✅ (fotograma HD + hoja) ·
  1920×1040.
- **El bosque renace** tras la muerte del dios ciervo: colinas verdes desde el aire,
  brote nuevo sobre la tierra quemada, encuadre justo después de la explosión de la
  cabeza cortada (fotogramas 15–18 de la misma hoja, min 2:04–2:07) · min 2:07:00
  (t=7620) · ⚠️ (visto en la hoja de trabajo `final/hoja_01.jpg`, 894×480; no se
  volvió a sacar en HD por presupuesto de red — es la única de las 10 escenas de este
  punto que queda en la copia de 480 p).

## Punto 4 — Fondos y sitios: luz, paleta y texturas equivalentes

Paletas medidas con `herramientas/estilo.py` sobre fotogramas HD (1920×1040) reales, no
arte promocional. Índice completo en `estilo/estilo.json` (carpeta de trabajo).

- **Montañas y bosque de la aldea Emishi** (min 0:04, t=260): verdes saturados y sombra
  casi negra. Paleta: `#19201E` 22.6% (sombra), `#22342D` 16.4%, `#69935A` 16.0%
  (verde medio iluminado), `#538044` 14.8%, `#314F39` 12.3%, `#3A6353` 7.4% ·
  sombreado **degradado/pintado** (fondo pintado a mano, no cel-shading), saturación
  media 39%, brillo medio 36%, línea normal color `#395130` · ✅ (medido con estilo.py).
- **Bosque profundo del dios ciervo (musgo, donde Ashitaka descansa)** (min 1:09,
  t=4195): verde amarillento muy saturado, hojarasca ocre. Paleta: `#404F20` 18.7%,
  `#728A1D` 17.4%, `#576B17` 15.7%, `#366278` 13.6% (agua/sombra azulada),
  `#527C36` 11.5% · sombreado degradado/pintado, saturación 63% (la más alta medida),
  brillo 45%, línea `#494C21` · ✅. Es el fondo más saturado de toda la película:
  Miyazaki quería que el santuario del bosque se sintiera "vivo" frente al gris de
  Irontown.
- **Puerta y murallas de Irontown (Tatara-ba)** (min 1:14:40, t=4480, de noche):
  paleta dominada por grises y marrones oscuros: `#1A1917` 32.6%, `#2D2A25` 18.5%,
  `#423F37` 15.0%, con un verde apagado `#9DC3AC` 10.9% (vegetación al fondo) y un
  rojo muy escaso `#76091D` 1.9% (los estandartes rojos de Eboshi, apenas visibles
  de noche) · sombreado degradado/pintado, saturación 22% (la más baja medida),
  brillo 30%, línea `#3C3A32` · ✅. Confirma lo que dice la wiki: Irontown se
  ilumina con antorchas y fuego de fragua, nunca luz de día limpia.
- **Escena nocturna con Moro** (min 1:21, t=4860): paleta fría de luna: `#14233C`
  30.3% (cielo nocturno), `#A3C7AF` 22.2% (pelaje iluminado), `#749F98` 17.9%
  (pelaje en sombra media) · sombreado **plano (cel)** para el personaje, poca
  línea, saturación 44%, brillo 46% · ✅. Contraste claro con los fondos pintados:
  los personajes llevan cel-shading, los fondos son pintura digital con degradado.
- **Textura de referencia — suelo/roca con musgo** para el santuario del bosque:
  `Ground037` (ambientcg.com/a/Ground037) y `Rock064` (ambientcg.com/a/Rock064),
  licencia CC0 · ✅ (buscado y comprobado en la API de ambientCG).
- **Textura de referencia — madera vieja** para las murallas y tablones de
  Irontown: `Wood095` (ambientcg.com/a/Wood095) y `Wood094`
  (ambientcg.com/a/Wood094), licencia CC0 · ✅.
- **Textura de referencia — metal** para las herramientas y rifles de la fragua:
  `Metal063` (ambientcg.com/a/Metal063) y `CorrugatedSteel009`
  (ambientcg.com/a/CorrugatedSteel009), licencia CC0 · ✅.
- **Luz y hora del día por sitio** (confirmado viendo el metraje, no wiki):
  aldea Emishi = luz de día limpia, verdes claros; bosque del dios ciervo = luz
  filtrada verde-azulada incluso de día, casi submarina; Irontown = noche con
  antorchas y fuego naranja de fragua, cielo casi negro; la cima donde vive Moro =
  luz de luna fría azul-verdosa. Los 4 sitios tienen paletas y temperatura de color
  claramente distintas entre sí (dato para el punto 17, guía de IA).

## Punto 9 — Música y sonido

## Punto 10 — Vídeos: tráilers, escenas, análisis y tendencias

## Punto 14 — Poses analizadas (San, Ashitaka, Moro)

## Lo mejor para la lámina

## No encontré

## Bitácora de búsqueda
