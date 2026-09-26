# Texto, juegos y técnica · Hazbin Hotel y Helluva Boss

Investigador de texto (puntos 5, 6, 11, 18, 24, 25 de ENCARGO.md). Serie hermana 55-hazbin-hotel
todavía no tiene carpeta en `biblias/` (se comprobó, no existe: no hay nada que leer de ella).
`datos-texto.md` casi no trajo nada (la obra es occidental, la mayoría de recolectores de anime
fallan): la investigación de este archivo es casi toda de mano, con la API de Fandom
(`hazbinhotel.fandom.com`, que cubre las dos series) y búsquedas propias.

## 5 · Tipografía (logo, globos, interfaz, letra libre comprobada con fontTools)

Ni manga ni videojuego: son series animadas de streaming, así que «letra según cada uso» se adapta
a rótulos, chyrons de TV, pantallas de móvil y subtítulos. Todas las letras libres de abajo se
descargaron de Fontsource y se comprobaron con `fontTools` (`TTFont(f).getBestCmap()`) para á/é/í/ó/ú,
ñ/Ñ, ¿ y ¡.

- **Logo/título de Hazbin Hotel**: letra de estilo *art déco* de los años 20-30 (el hotel es un
  homenaje al glamour decadente). La comunidad la identifica como **Mr Darcy** (Insigne Design),
  con retoques propios del estudio · [hilo de Hellaverse Wiki citado en búsqueda](https://hazbinhotel.fandom.com/f/p/4400000000000089255) · ⚠️ (una fuente, no confirmada por VivziePop). Mr Darcy es gratis sólo para uso personal, no sirve para nada que se publique.
- **Letra libre gemela para el logo** (déco, con tildes/ñ/¿/¡): **Cinzel Decorative** (Google
  Fonts/Fontsource, OFL) ✅ comprobada con fontTools: á/é/í/ó/ú/ñ/Ñ/¿/¡ = todo `True` · descargada de
  `cdn.jsdelivr.net/fontsource/fonts/cinzel-decorative@latest`. Alternativa más fina: **Poiret One**
  (mismo resultado, todo `True`).
- **Logo de Helluva Boss**: letra **propia y no comercial**, garabateada, con un doble trazo rojo
  sangre debajo del blanco y letras concretas con dibujo propio (la «B» de Boss, etc.); no es una
  tipografía instalable ✅ (dos fuentes independientes coinciden en que es dibujo a mano, no
  tipografía de catálogo: [pixelframe.design](https://pixelframe.design/helluva-boss-logo-font-generator/), [dafont forum «Helluva Boss - Season 2»](https://www.dafont.com/forum/read/514789/helluva-boss-season-2)).
- **Letra libre gemela para Helluva Boss** (grunge, con sangre/rasguño): **Nosifer** (Google
  Fonts, OFL, horror-splatter) ✅ fontTools: todo `True`, incluida latin-ext. Para el rótulo de
  **I.M.P.** (letras más romas, industriales): **Butcherman** ✅ fontTools: todo `True` **excepto ¿**
  (`False`) — si se necesita «¿», usar Nosifer en su lugar.
- **Globo/diálogo normal y subtítulos**: la serie no tiene globos de cómic en pantalla (es
  animación, no manga); los subtítulos oficiales de Prime Video van en un sans-serif limpio
  estándar de plataforma, no pude identificar el nombre exacto ⚠️ (sin confirmar; Prime Video no
  publica su hoja de estilos). Letra libre recomendada para textos largos/subtítulos de lámina:
  **Oswald** (Google Fonts, OFL, condensada, muy legible en pantalla) ✅ fontTools: todo `True`.
- **Grito** (letras de énfasis, gritos de Blitzo o Angel Dust): **Bangers** (Google Fonts, cómic,
  OFL) ✅ fontTools: todo `True`.
- **Pensamiento** (poco usado; la serie prefiere monólogo hablado a texto de pensamiento): si hace
  falta, **Caveat** (manuscrita, Google Fonts, OFL) ✅ fontTools: todo `True`.
- **Onomatopeya** (disparos, golpes; aparecen poco en pantalla, casi todo es sonido, no letra
  dibujada — comprobado mirando fotogramas de peleas de Helluva Boss): si se necesita una,
  **Permanent Marker** (Google Fonts, OFL, trazo de marcador) ✅ fontTools: todo `True`.
- **Cartel del mundo** (letreros de neón de Pentagram City, el cartel del hotel, el ticker de
  «666 News»): **Monoton** (Google Fonts, OFL, imita tubos de neón) ✅ fontTools: todo `True`, ideal
  para carteles de casino/club nocturno del Pride Ring. Para el ticker de noticias tipo tabloide,
  **Special Elite** (máquina de escribir, Google Fonts, OFL) ✅ fontTools: todo `True`.
- **Interfaz de juego**: no hay videojuego oficial con interfaz propia (ver punto 11); el «mapa» del
  móvil de Blitzo (imagen `Mapapp.jpg`, 2500×2500 px) usa una letra sans genérica de app, sin rasgo
  distintivo ⚠️.
- Todas las letras libres arriba se enlazan también en `texto.json` con su licencia (OFL en todos
  los casos, uso comercial libre).

## 6 · Cómo hablan y piensan en pantalla (cuadros de diálogo, cartelas, interfaces)

Es el punto más importante del encargo: nada de burbuja blanca genérica. Hazbin Hotel/Helluva Boss
no usan globos de cómic; cada personaje con un «filtro» tiene su propio marco visual, muy
reconocible por el fandom.

- **Alastor habla con ESTÁTICA DE RADIO, no con un globo**: su voz en pantalla trae textura de
  interferencia (líneas horizontales, grano, el símbolo de «señal de radio» ondulando), y su marco
  de cámara imita un dial antiguo cuando transmite ✅ (dos fuentes: [Doblaje Wiki, Hotel Hazbin](https://doblaje.fandom.com/es/wiki/Hotel_Hazbin), guía interna `_Cuadros de dialogo por franquicia.md` del equipo). Dato de sabor: **en el doblaje latino (Chile, Caja de Ruidos) se olvidaron de quitar el filtro de radio de Alastor en el final de la T1** cuando le rompen el bastón — error real, queda grabado ✅.
- **666 News (VoxTek) usa cartela de noticiero real**: banda inferior roja con el logo de VoxTek,
  ticker de texto corriendo abajo, nombre y cargo del presentador en caja blanca, todo dentro de un
  «marco de televisor» con viñeteado, exactamente como un canal de cable de los 2000 ✅ (imagen
  `666 News main series.png`, 1920×1080, wiki oficial: [666 News](https://hazbinhotel.fandom.com/wiki/666_News); coincide con el lema «Murder! Sex! Weather!» repetido en redes oficiales) · sirve de referencia directa de «cartela del mundo».
- **VoxTek (marca del Overlord Vox/Valentino) tiene su propio logo corporativo**, año de fundación
  1952 en el lore, usado en anuncios, coches y merchandising dentro del mundo ✅ (imagen `VoxTek
  Logo.png`, 1920×1080, [wiki VoxTek](https://hazbinhotel.fandom.com/wiki/VoxTek); confirmado también en merchandising real de BoxLunch). Sirve de plantilla para cualquier «anuncio dentro del mundo» de la lámina.
- **El móvil de Blitzo (Helluva Boss) usa una app de mapa** con las siete anillas de Hell marcadas,
  interfaz tipo GPS genérico (fondo oscuro, pines de colores) ✅ (imagen `Mapapp.jpg`, 2500×2500,
  [wiki Rings of Hell](https://hazbinhotel.fandom.com/wiki/Rings_of_Hell)) — es la referencia más concreta de «interfaz de móvil» del mundo.
- **No hay manga oficial** de Hazbin Hotel/Helluva Boss (nació como piloto de YouTube y serie
  animada, no como cómic seriado); sólo hay **merchandising con paneles tipo cómic** (variant covers,
  pósters) hechos por artistas del estudio para eventos — no encontré un cómic narrativo licenciado
  con globos propios ⚠️ (búsqueda «Hazbin Hotel comic official issue» sin resultado fiable).
- **Pensamientos**: la serie casi no usa cajas de texto de pensamiento; los personajes cantan o
  hablan en voz alta lo que piensan (recurso de musical) — nada que fotografiar como «cuadro de
  pensamiento» ⚠️ propio de la obra, es una decisión de guion, no de arte.
- **Subtítulos oficiales**: sans blanco con borde negro fino, estándar de Prime Video, centrados
  abajo; no cambian de tipografía por personaje (ni siquiera para Alastor) ⚠️ (visto en clips
  oficiales de Prime Video en Dailymotion, sin acceso a archivo de subtítulos original para medir el
  tipo exacto).

## 11 · Videojuegos de la franquicia

- **No existe ningún videojuego oficial** de Hazbin Hotel ni de Helluva Boss a fecha de hoy
  (26-sep-2026) ✅ — comprobado en TCRF (`tcrf.net`, búsqueda «Hazbin» y «Helluva»: cero páginas) y
  en búsqueda directa de anuncios de publisher; lo único con ese nombre en fandoms son wikis de
  «ideas de fans» (`gameideas.fandom.com`, `audreyworks.fandom.com`) con fechas de 2026-2029 que
  se leen como ficción de fans, no como anuncios reales (el propio texto lo admite: «homebrew»,
  «Game Ideas Wiki») — **no lo cuento como real**, aviso explícito para no confundirlo.
- **Lo único oficial jugable es un juego de mesa**: *Immediate Murder Professionals: A Helluva Boss
  Official Game* (Creatist Games, con licencia de VivziePop/Spindlehorse) ✅ (dos fuentes:
  [Kickstarter](https://www.kickstarter.com/projects/creatistgames/immediate-murder-professionals-a-helluva-boss-official-game-0), [Gamefound](https://gamefound.com/en/projects/creatist-games/helluvabossgame), reseñado también en [thelatenightplayers.com](https://www.thelatenightplayers.com/news/helluva-boss-board-game-launches-on-kickstarter)). 4 personajes jugables (Blitzo, Millie, Moxxie, Loona), rueda de juego, 56 cartas base, standees de cartón; edición «Grimoire» con
  caja con forma del grimorio de Stolas y peones de cristal acrílico · recaudó más de $204,701 en
  Kickstarter ✅.
- No hay interfaz de videojuego que mirar (ni menús, ni cajas de diálogo de juego): el punto no
  aplica más allá del juego de mesa de arriba. Si el redactor necesita una interfaz de «juego»
  para la lámina, la referencia más cercana dentro del mundo ficticio es el móvil de Blitzo (ver
  punto 6) o las máquinas tragamonedas de los casinos del Pride Ring (visibles en fondos de la
  serie, sin interfaz jugable real).

## Lo mejor para la lámina

- El **filtro de radio de Alastor** (estática + dial) como «cuadro de diálogo» propio: mucho más
  fiel que cualquier globo.
- La **cartela de 666 News** (banda roja VoxTek + ticker) para cualquier texto tipo «noticia del
  canal» o «aviso del servidor».
- **Cinzel Decorative** para títulos/logo (deco, libre, con ñ/¿/¡) y **Nosifer** para lo tipo
  Helluva Boss (sangre/grunge, libre).
- El **VoxTek Logo** como plantilla de «marca dentro del mundo» si el canal necesita un anuncio.
- El **juego de mesa de I.M.P.** (Immediate Murder Professionals) como único producto jugable
  oficial: sirve si el canal quiere un gag de «minijuego», pero como referencia de cartas de mesa,
  no de HUD.

## No encontré

- Confirmación directa de VivziePop sobre el nombre exacto del tipo del logo de Hazbin Hotel
  (búsqueda «vivziepop twitter font hazbin hotel logo», en inglés: sólo fan art, sin tuit fuente).
- El nombre del tipo de letra de subtítulos/créditos oficiales de Prime Video (no hay archivo de
  subtítulos original descargable sin sesión).
- Un cómic o manga oficial con cuadros de diálogo propios de la franquicia (búsqueda «Hazbin Hotel
  official comic issue», en inglés: nada más que merchandising suelto).
- Videojuego oficial (confirmado que no existe, ver punto 11; búsquedas «Hazbin Hotel video game
  official 2026», «Helluva Boss I.M.P. app», en inglés, en tcrf.net directamente).

## Bitácora

- Fandom API (`hazbinhotel.fandom.com/api.php`, inglés): `allpages`, `search` y `parse&prop=wikitext`
  para Rings of Hell, Overlords, Extermination, Seven Deadly Sins, Pentagram City, Hazbin Hotel
  (series), Hazbin Hotel (location), 666 News, VoxTek — todas abiertas y leídas.
- `tcrf.net` (inglés): búsqueda de texto completo «Hazbin» y «Helluva» → sin resultados, confirma
  que no hay contenido descartado de un juego que no existe.
- WebSearch (inglés): «Hazbin Hotel logo font typeface identify», «Helluva Boss logo font typeface
  identify», «"Mr Darcy" font dafont free download license», «Hazbin Hotel font free alternative
  Google Fonts dafont art deco», «TCRF Hazbin Hotel OR Helluva Boss», «Hazbin Hotel official video
  game mobile app 2024 2025», «Helluva Boss video game I.M.P. app», «"Hazbin Hotel" game announced
  2026 publisher official», «vivziepop twitter font hazbin hotel logo», «Hazbin Hotel end credits
  font typeface style title cards».
- Fontsource (`api.fontsource.org/v1/fonts`, descarga directa de `cdn.jsdelivr.net`): Cinzel
  Decorative, Poiret One, Nosifer, Butcherman, Creepster, Bangers, Monoton, Special Elite, Oswald,
  Permanent Marker, Caveat — comprobadas todas con `fontTools` (`getBestCmap`) para
  á/é/í/ó/ú/ñ/Ñ/¿/¡.
- WebFetch: `pixelframe.design` (Helluva Boss font), `audreyworks.fandom.com` (Five Nights at
  Hazbin Hotel, confirmado fan-made), `thelatenightplayers.com` (juego de mesa I.M.P.),
  `gamefound.com` y Kickstarter (bloqueados por 403, se usó la reseña de thelatenightplayers.com en
  su lugar, con Gamefound/Kickstarter como enlaces directos del producto).
