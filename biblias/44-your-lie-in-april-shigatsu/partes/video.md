# Parte VIDEO · Your Lie in April (Shigatsu wa Kimi no Uso) · encargo 44

Investigador de vídeo. Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Libreta de datos, no prosa.

Fuente pesada principal: los 22 episodios + OVA en 1080p de Internet Archive
`https://archive.org/details/EVYourLieinApril` (subidos por el usuario "Kaminari
Project"; TV-rip con subs en inglés, marca de agua «9anime.to» en la esquina,
mp4 individuales `1.mp4`…`22.mp4`). Los fotogramas se sacaron con `ffmpeg -ss
<segundo> -i "https://archive.org/download/EVYourLieinApril/<ep>.mp4"` (equivalente
a `fotogramas.py`/`episodio.py` pero sin bajar el archivo entero, con *range
requests* de archive.org) y se miraron con Read. El minuto citado es el de
**este rip** (duración ~22:50 por episodio, con OP y ED dentro).

## 2 · Fotogramas de escenas icónicas, con capítulo y minuto

Tráiler oficial mirado con `fotogramas.py` sobre el PV2 japonés en Dailymotion
(no hace falta YouTube): `python3 herramientas/fotogramas.py
"https://www.dailymotion.com/video/x2682f1" --cada 5 --salida …`. Es el
**segundo PV oficial** del anime (A-1 Pictures, min 1:45-1:52 trae el reparto
japonés y el staff, confirma que es material oficial de TV): Hanae Natsuki
(Kousei), Oda Risa (Kaori), Sakura Ayane (Tsubaki), Aisaka Ryouta (Watari),
dir. Ishiguro Kyohei, música Yokoyama Masaru, animación A-1 Pictures.

- Tráiler oficial (PV2, jp) · Dailymotion, subido por «Filmow» (repost) · https://www.dailymotion.com/video/x2682f1?start=0 · ✅ (créditos del propio vídeo + AniList lo linka como tráiler) · 1:52
  - 0:00-0:15 cielo y cerezos en flor (planos vacíos, sólo naturaleza)
  - 0:20-0:30 Kousei con gafas, mirada seria, en su cuarto
  - 0:35-0:45 Kaori sonriendo con el puño en alto (gesto «genki»), luego primer plano sorprendida boquiabierta
  - 0:45 Watari en el gimnasio con micrófono, de rodillas, gesto animado
  - 1:00 calle con tienda de conveniencia y cerezos (fondo de pueblo)
  - 1:15 pies descalzos saltando (Kaori) sobre fondo blanco
  - 1:20 melódica/teclado de juguete tocado al aire libre
  - 1:35 Kousei de espaldas caminando hacia la escuela bajo cerezos
  - 1:45-1:52 cartela «2014年10月より フジテレビ…» (estreno oct-2014, bloque Noitamina) y créditos de reparto/staff
  - enlace directo al minuto: `https://www.dailymotion.com/video/x2682f1?start=95` (créditos)

**3 escenas icónicas** (localizadas con `ffmpeg -ss` sobre el rip de Internet
Archive, contact sheets propias, y miradas con Read; ✅ verificado dos veces:
el propio fotograma + resumen de episodio en la wiki de Fandom):

- Kaori se presenta a Kousei, «Nice to meet you!», sonriendo entre rosas (primer plano icónico, muy repetido en material promocional) · Ep. 01 «Monotone/Colorful» · min 19:00 · https://archive.org/details/EVYourLieinApril (archivo `1.mp4`, min 19:00) · ✅ (fotograma propio + resumen del episodio en la wiki: shigatsu-wa-kimi-no-uso.fandom.com/wiki/Episode_01:_Monotone/Colorful) · 19:00
- Kousei toca el piano solo, a oscuras, por primera vez desde el trauma; luego sujeta la manga de Kaori, que llora, y le promete tiempo («If you need time to prepare, you got it!») · Ep. 03 «Inside Spring» · min 18:00-21:00 · `3.mp4` · ✅ (fotograma propio + ficha de personaje de Kousei en la wiki menciona esta escena como su punto de giro) · 18:00 / 20:00 / 21:00
- Final: Kousei corre leyendo la carta-partitura de Kaori, cerezos cayendo, atardecer dorado; suena «Kirameki (versión Kousei y Kaori)» de wacci y la Balada n.º 1 de Chopin (violín Sayaka Sezaki [瀬崎明香], piano Tomoki Sakata [阪田知樹], créditos del propio episodio) · Ep. 22 «Spring Wind» · min 19:00-22:30 · `22.mp4` · ✅ (fotograma propio + «Chapter 43: Ballade» en la wiki del manga confirma que la Balada de Chopin es la pieza de esta escena) · 19:00 / 20:00 / 21:00 / 22:00 (créditos)

## 4 · Fondos y sitios: luz y paleta medida en fotogramas

Hex medidos con `herramientas/estilo.py` sobre fotogramas propios en 1080p
(no de arte de fans). Todos con degradado/pintado (no plano) y línea fina del
color del propio dibujo, típico del estudio A-1 Pictures en esta obra.

- Calle de cerezos al atardecer (camino habitual de Kousei/Tsubaki/Watari a casa) · Ep. 01, min 6:00 · `1.mp4` · paleta: #9C5E26 27% · #E5B470 18% · #5F3D28 16% · #D6774D 14% · brillo 70%, saturación 57% · ✅ (medido con estilo.py sobre fotograma propio) 
- Calle nocturna residencial (Kaori caminando sola, tono frío) · Ep. 06 «On the Way Home», min 9:00 · `6.mp4` · paleta: #1A2434 27% · #283950 26% · #0E151D 17% · #426CB1 9% · brillo 32%, saturación 47% · ✅
- Cuarto de Kousei con el piano de cola (suelo de madera, luz cálida cenital) · Ep. 22, min 18:00 · `22.mp4` · paleta: #E6E6E2 34% · #554C43 21% · #BF9955 15% · #87603C 15% · brillo 62%, saturación 25% · ✅
- Pasillo de la escuela (suelo verde, luz de tarde) · Ep. 03, min 16:00 · `3.mp4` · paleta: #4B4834 27% · #5F3526 22% · #2A241F 21% · #92D76A 17% · brillo 43%, saturación 42% · ✅
- Sala de conciertos (butacas rojas, madera cálida, luz de escenario) · Ep. 02 «Friend A», min 13:00 · `2.mp4` · paleta: #251309 26% · #B39566 19% · #3D2D22 19% · #D3C094 14% · brillo 43%, saturación 50% · ✅
- Cerezos cayendo sobre calle con cableado eléctrico, atardecer dorado (escena final) · Ep. 22, min 21:00 · `22.mp4` · paleta: #F6E1C6 32% · #E9BBA1 18% · #F4DE8C 15% · #DEAD66 15% · brillo 86%, saturación 37% · ✅

Patrón: interiores cálidos (crema/ocre) cuando hay calma o música; exteriores
con cerezos en tonos naranja-dorado (tarde) para momentos emotivos; azul frío
sólo en la calle nocturna de Kaori (soledad, su enfermedad). Sirve de guía de
paleta por escena para la lámina.
