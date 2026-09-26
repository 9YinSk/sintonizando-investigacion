# Vídeo · The Apothecary Diaries (El diario de la boticaria) — encargo 91

Investigador de vídeo. Puntos 2, 4, 9, 10 y 14 de ENCARGO.md. Serie sin canal propio
todavía. Sin serie hermana declarada en `encargos/91-*.md` (no hay otro encargo de
esta obra en `encargos/`; comprobado con `grep`).

Comprobación de partida (obligatoria antes de fiarse de `datos-video.md`): AniList
161645 = confirmado por API GraphQL propia (`Media(id:161645)` → romaji "Kusuriya
no Hitorigoto", english "The Apothecary Diaries") ✅, mismo id que usó el
investigador de imagen. El tráiler de AniList (`oyHqh8ue4zw`, YouTube, bloqueado
en este servidor) tiene gemelo en Dailymotion (`x8mmgoz`, mismo tráiler de 2:33,
verificado fotograma a fotograma: título "薬屋のひとりごと / The Apothecary Diaries"
y "TVアニメ 2023年放送決定" en pantalla) ✅ — es el mismo tráiler, no otra obra.
**Aviso sobre `datos-video.md`:** el bloque "Bandas sonoras publicadas
(MusicBrainz)" está casi todo mal filtrado por buscar sólo la palabra "Diaries":
de las 14 entradas sólo las **4 primeras** (con título en japonés 薬屋のひとりごと)
son de esta obra ✅; las otras 10 (*Vodka Diaries*, *Chernobyl Diaries*, *Ranchi
Diaries*, *The Nanny Diaries*, *The Princess Diaries* ×4, *Dhobi Ghat (Mumbai
Diaries)*, *Beyond Skyrim Dev Diaries*, *Red Shoe Diaries*) son bandas sonoras de
otras películas/juegos sin relación — las descarto todas. El resto de
`datos-video.md` (Dailymotion, Internet Archive) sí es de esta obra, comprobado
por título y por mirar los vídeos.

## 2 · Fotogramas de escenas icónicas (capítulo y minuto)

Miradas con `fotogramas.py` sobre el tráiler oficial (Dailymotion, gemelo del de
AniList) y sobre el episodio 1 en inglés (Internet Archive, BD 720p — bajado por
tramos con `--desde/--hasta`, nunca el archivo entero de golpe).

- Tráiler oficial (2:33, Dailymotion `x8mmgoz` = mismo que YouTube `oyHqh8ue4zw` de AniList): té en jardín con Maomao de gala (0:05-0:10), trébol de 4 hojas en primer plano (0:15), corredor de palacio con farolillos rojos y damas en fila (0:20-0:25), silueta en un tejado al atardecer (0:25), Jinshi de perfil sonriendo con picardía (0:45), Maomao cargando una caja (0:50), primer plano extremo de un ojo (prueba de veneno, 1:15), mano sujetando un cuchillo (1:40), figura saltando de espaldas contra el cielo nocturno (1:50) · fuente https://www.dailymotion.com/video/x8mmgoz&t=5s (y sucesivos `&t=`) · ✅ (mismo tráiler indexado también como `x9xnk6i`, subido por otro canal) · minuto exacto de cada fotograma
- Episodio 1 (inglés, Internet Archive `anime-pahe-kusuriya-no-hitorigoto-eng-dub-01-bd-720p-sam.mp-4-kw`): cold open con flor naranja en negro (0:20-0:40, presenta el motivo floral del OP), OP1 "Hana ni Natte" con Maomao envuelta en pétalos (1:00-1:40), mercado de la capital con Maomao regateando "If you want to gawk, pay up!" (2:20), Maomao secuestrada y envuelta en tela dándose cuenta "Yikes!" (3:20), nacimiento del príncipe en flashback (4:40), vista aérea del palacio trasero completo (5:30), primer plano resignado de Maomao "I guess, at the very least, I get paid" (6:30), patio nocturno en azules fríos (8:00), casa de té con cotilleo sobre las consortes (8:30-9:30), retrato de Gyokuyou entre flores lilas (9:15) · fuente https://archive.org/details/anime-pahe-kusuriya-no-hitorigoto-eng-dub-01-bd-720p-sam.mp-4-kw (episodio 1 completo, doblaje inglés, con subtítulos en pantalla) · ✅ (la misma escena de la vista aérea del palacio se repite como fondo de pantalla oficial en la wiki, y el diseño de Gyokuyou coincide con su ficha de personaje) · minuto exacto arriba

## 4 · Fondos y sitios: luz y paleta medida

Colores medidos con `estilo.py` (Pillow) sobre fotogramas propios del episodio 1
(no de arte promocional, para que la luz sea la real de escena).

- **Palacio trasero, vista aérea de día** (ep.1, 5:30): paleta #69696E, #C69062, #938182, #464149, #C3B9BB, #74AFC7 — tejados naranja/teja sobre muros grises, luz plana de mediodía, saturación baja (28%) y brillo medio (60%); sombreado degradado con mucha línea fina (#7E685B) para las tejas · fuente fotograma propio (`fotograma_00330.jpg`, medido con estilo.py) ✅ (el mismo complejo de tejados naranjas se repite en todos los planos exteriores del palacio del resto del episodio)
- **Patio de palacio de noche** (ep.1, 8:00): paleta #1E1832, #16204E, #0F1120, #243468, #3D507E — azules casi negros, sombreado degradado con poca línea, saturación alta para lo oscuro (58%) y brillo muy bajo (26%): la serie usa el azul noche cerrado (casi sin negro puro) para las escenas nocturnas de palacio · fuente fotograma propio (`fotograma_00480.jpg`) ✅ (mismo tono de azul nocturno en el tráiler, fotograma 1:50)
- **Retrato de consorte con fondo floral** (Gyokuyou, ep.1, 9:15): paleta #DCE4F1, #58497D, #BDC7E3, #F8DDDA, #8C7FC2, #D89DAC — pasteles lilas y rosas, brillo muy alto (83%) y saturación baja (22%), línea normal (#7B738F): es la paleta que la serie reserva para presentar a una consorte importante (fondo decorativo con flores, no un fondo realista) · fuente fotograma propio (`fotograma_00555.jpg`) ✅ (mismo tratamiento de fondo floral pastel en las fichas de personaje "Anime Design" de la wiki, ya medidas por el investigador de imagen con otros hex de vestuario)
- Contraste: exteriores de día = paleta cálida tierra/naranja de baja saturación (edificios, mercado); interiores/noche de palacio = azules fríos oscuros; escenas de "presentación de personaje" = fondo decorativo pastel casi monocromo. Sirve de guía de luz para la lámina.

