---
tags: [biblia, serie, laminas]
serie: "Pokémon"
canal: "#autoroles"
fecha: 2026-09-24
---

# Biblia · Pokémon — para #autoroles

> [!important] Cómo se hizo, y sus límites
> **Primera pasada (red cerrada).** Fandom, Bulbapedia, WikiDex, Doblaje
> Wiki, PokéAPI, Sketchfab, Google Fonts, pokemon.com y Game UI Database
> daban **403**. Se usó GitHub (código de los juegos `pret`, PokéAPI,
> subtítulos de la película de 2017, letras) y **50 búsquedas web** en
> español, inglés, japonés y coreano. De ahí salen las medidas exactas de
> la caja de texto de Game Boy y el texto oficial en español de Rojo/Azul.
>
> **Segunda pasada (24-sep-2026, red abierta).** La hizo un equipo:
> investigadores de imagen, vídeo, voz y texto, y un redactor que junta
> todo aquí. Se pudo usar:
> - **El capítulo 1 real** (Internet Archive, doblaje inglés de 4Kids),
>   **mirado fotograma a fotograma** con `fotogramas.py`. Los minutos del
>   laboratorio y de los Spearow ya son del capítulo, no de un subtítulo.
> - **Doblaje Wiki por su API**: reparto completo y **11 muestras de audio**
>   de los actores latinos, transcritas y medidas con `voz.py`.
> - **Dailymotion**: opening, ending, tráiler de Rojo/Azul, tráiler latino
>   de *¡Yo te elijo!* y el lema del Rocket, mirados y oídos.
> - **API de Bulbapedia** (la web normal sigue en 403), **API de
>   pokemon.fandom.com** (4 hojas de contacto, 180 imágenes con tamaño real),
>   **API de Sketchfab** (licencias y autores reales), `estilo.py` (colores
>   medidos), `fontTools` sobre el archivo real de Pokémon Solid, Wikipedia
>   en inglés, español y japonés, CGWORLD, AWN, Interface In Game y Arctic
>   Shift (Reddit).
> - Siguió bloqueado: **YouTube** (pide iniciar sesión), TikTok,
>   pokemon.com (anti-bot), Game UI Database y Wayback (403), AnimeThemes
>   (caída). Por eso el capítulo 1 se vio en **480p**, que es su calidad
>   original de 1997; no hay fotogramas en 1080p.
> - ✅ **confirmado**: dos fuentes, o comprobado por nosotros en el archivo,
>   el audio o el fotograma. ⚠️ **dudoso**: una sola fuente, o de memoria.
---

## Segunda pasada · qué cambió

_(se completa al terminar el repaso)_

## Índice

Las secciones 0-21 siguen el orden de la primera pasada. Las **P18-P25** son
los puntos 18-25 de `ENCARGO.md`, nuevos en esta pasada.

| Sección | Punto de ENCARGO.md |
|---|---|
| 0 · El canal · 1 · Resumen | textos del canal |
| 2 · Arte oficial (con las **hojas de contacto**) | 1 |
| 3 · Escenas icónicas con su minuto | 2 |
| 4 · Fan art y 3D | 3 |
| 5 · Sitios, luz, paleta y texturas | 4 |
| 6 · Tipografía | 5 |
| 7 · El cuadro de diálogo | 6 |
| 8 · Los personajes · 9 · El más querido | 7 y 13 |
| 10 · Doblaje latino | 8 |
| 11 · Música | 9 |
| 12 · Vídeos | 10 |
| 13 · Videojuegos | 11 |
| 14 · Lo que ama el fandom | 12 |
| 15 · Poses | 14 |
| 16 · Vestuario | 15 |
| 17 · Paisajes y fondos | 16 |
| 18 · Guía para IA de imagen y de texto | 17 |
| P18 · Estilo de dibujo y técnica | 18 |
| P19 · Texturas 2D | 19 |
| P20 · Gustos y detalles | 20 |
| P21 · Por qué la aman | 21 |
| P22 · Fan dubs y comunidad hispana | 22 |
| P23 · Colaboraciones y cruces | 23 |
| P24 · Obras parecidas | 24 |
| P25 · El mundo y sus símbolos | 25 |
| 19 · Tres conceptos · 20 · Lo que no pude verificar | conceptos |
| Cumplimiento del encargo · 21 · Bitácora | tabla y fuentes |

---

## 0 · El canal y lo que tiene que decir

Del inventario (`servidor/inventario.md`, sección EMPIEZA AQUÍ):

> **ıı・⭐・autoroles** (texto) · 0 fijados — _Tu color y tu país,
> reaccionando abajo. Lo demás se cambia en Canales y roles, arriba del
> todo. Aquí no se escribe: si algo no funciona, abr_

- El texto está **cortado** en el inventario («abr_»). Lo lógico es «abre
  un ticket en soporte»: el canal **ıı・🎫・soporte** dice «Abre un ticket:
  solo lo vemos tú y el staff». ⚠️ Es una deducción: que el dueño lo
  confirme.
- Función según el encargo: **cómo elegir tus roles en «Canales y roles»:
  qué haces, de dónde eres, qué buscas.**
- **#avisos-clases** también manda aquí: «Activa el aviso que te interese
  en Canales y roles». O sea, «qué buscas» incluye los avisos de clases.
- No tiene etiquetas ni fichas.

> [!warning] Hay una contradicción que decide el dueño
> El inventario dice que **el país se elige reaccionando abajo**, en este
> canal. El encargo pone «de dónde eres» dentro de **Canales y roles**.
> Los textos de abajo siguen al inventario, que es lo que ve la gente hoy.
> Si el país está en los dos sitios, basta cambiar una línea.

**Los textos de la lámina** (una idea cada uno, sin «·», «—» ni
paréntesis):

| # | Texto | Idea |
|---|---|---|
| 1 | **Autoroles** | nombre del canal |
| 2 | **Elige tus roles como eliges tu inicial** | la metáfora |
| 3 | **Reacciona abajo y elige tu color y tu país** | lo que se hace aquí |
| 4 | **¿Qué haces? ¿Qué buscas? Eso va en Canales y roles** | lo demás |
| 5 | **Canales y roles está arriba del todo** | dónde está |
| 6 | **Lo cambias cuando quieras** | no es para siempre |
| 7 | **Aquí no se escribe** | norma |
| 8 | **¿Algo no funciona? Abre un ticket en soporte** | qué hacer si falla |

Caben en una lámina si se reparten entre el cuadro de diálogo y el objeto.
**Lámina 2** sólo si el dueño quiere enseñar la **lista de roles** (los
colores, los países, los talentos). Esa lista **no está** en el inventario.
Propuesta en el punto 19.

---

## 1 · Resumen para quien tenga prisa

| Pregunta | Respuesta |
|---|---|
| Cuadro de diálogo propio | **La caja de texto de Pokémon Rojo y Azul**: blanca, abajo, con **doble filete y esquinas de nudo**, dos líneas de **18 letras** como mucho y un **▼ que parpadea abajo a la derecha**. Todo medido en el código del juego ✅. El ▼ señala **abajo**: justo donde están las reacciones. |
| Objeto del plan, mejorado | **El soporte del laboratorio de Oak con las Pokébolas**, como en el capítulo 1: tres huecos y **un cuarto en el centro** del que sale **la Pokébola del rayo**, la de Pikachu ✅. Cada Pokébola lleva colgada una pregunta. |
| La broma que un fan pilla | En el capítulo, Oak avisa: «hay otro, pero tiene **un problema**». Esa Pokébola, la del rayo, es la de **soporte**: «¿Algo no funciona?». |
| Frase oficial de Oak | «¡Aquí hay 3 Pokémon! ... Te daré uno. **¿Cuál quieres?**» (Pokémon Rojo/Azul en español ✅, texto del juego). |
| Minuto de la escena | **Capítulo 1 real, mirado** (Internet Archive, doblaje inglés): las tres Pokébolas en triángulo a las **5:56**, la del rayo se abre a las **6:48**, sale Pikachu a las **6:58** y el abrazo chamuscado a las **7:18** ✅. En la película de 2017: laboratorio de 00:03:03 a 00:05:11 (subtítulo no oficial). |
| El más querido | En la votación mundial oficial de 2020, **Charizard** quedó **4.º** y **Pikachu 19.º** ✅. En Japón (2016), Pikachu fue 4.º ✅. Pikachu es la cara; Charizard, el favorito de los votos. |
| Voz latina | Oak: **Hugo Navarrete** ✅, con su muletilla real «hay un problema con este último» (muestra de Doblaje Wiki). Ash: **Gabriel «Gabo» Ramos** (temporadas 1 a 12) y **Miguel Ángel Leal** desde la 13 ✅. Pikachu: **Ikue Ōtani** en todos los idiomas ✅. |
| Palabra latina | En el doblaje latino se dice **Pokébola**, no «Poké Ball» ✅ (WikiDex y reseñas del doblaje, punto P25). |
| Letras | **pokemon-font** (la de Game Boy, OFL) y **Press Start 2P** (OFL): las dos traen á é í ó ú ñ ¿ ¡ y ▼, comprobado en el archivo. Logo: **Pokémon Solid** (de fans, licencia poco clara) o **Lilita One** (OFL). |
| Tono | Mañana soleada en Pueblo Paleta. Blanco de laboratorio, madera, cielo menta y celeste. Alegre, de principio de viaje. |

---

## 2 · Arte oficial y referencias visuales

### 2.1 El arte oficial de los Pokémon (PokéAPI, en GitHub)
El repositorio [PokeAPI/sprites](https://github.com/PokeAPI/sprites) guarda
el arte oficial de cada Pokémon. Lo bajé y medí. Su licencia dice: «todo el
contenido de las imágenes es copyright de The Pokémon Company». Sólo
referencia.

| Imagen | Tamaño | Qué es | Pose |
|---|---|---|---|
| [Bulbasaur](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png) | 475×475 | arte oficial de los juegos, trazo de acuarela | a cuatro patas, boca abierta, mira al frente |
| [Charmander](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png) | 475×475 | ídem | de pie, brazos abiertos, sonríe, llama en la cola |
| [Squirtle](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png) | 475×475 | ídem | de pie, de tres cuartos, un brazo adelante |
| [Pikachu](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png) | 475×475 | ídem | salta, brazos abiertos, boca abierta: **celebrar** |
| [Charizard](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png) | 475×475 | ídem | alas abiertas, cabeza arriba |
| [Pikachu 3D de HOME](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/25.png) | 512×512 | render 3D de Pokémon HOME | brazos arriba, sonrisa: colores saturados, como el anime |

Los de HOME (`/other/home/<número>.png`) están en 512×512 para todos:
[Bulbasaur](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/1.png),
[Charmander](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/4.png),
[Squirtle](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/7.png).

### 2.2 Los sprites de Game Boy (el código de Pokémon Rojo)
En [pret/pokered](https://github.com/pret/pokered) están los dibujos
originales del juego. Los miré:
- [`gfx/trainers/prof.oak.png`](https://raw.githubusercontent.com/pret/pokered/master/gfx/trainers/prof.oak.png) (56×56): Oak de pie, bata de laboratorio, **una mano en el pecho**, cara seria.
- [`gfx/player/red.png`](https://raw.githubusercontent.com/pret/pokered/master/gfx/player/red.png) (56×56): Rojo con la gorra calada y **una mano en la cintura**.
- [`gfx/pokemon/front/pikachu.png`](https://raw.githubusercontent.com/pret/pokered/master/gfx/pokemon/front/pikachu.png) (40×40): Pikachu redondo, **chispas junto a las mejillas**.
- [`gfx/font/font.png`](https://raw.githubusercontent.com/pret/pokered/master/gfx/font/font.png) y [`font_extra.png`](https://raw.githubusercontent.com/pret/pokered/master/gfx/font/font_extra.png): la letra y **los bordes de la caja de texto** (punto 7).

### 2.3 Arte de los juegos modernos
- **Profesor Oak en Let's Go, Pikachu! / Eevee!** (2018): arte de **Ken
  Sugimori**; diseño de personajes de **Megumi Mizutani**. Galería en
  [Creative Uncut](https://www.creativeuncut.com/gallery-36/plgp-professor-oak.html)
  y todo el arte del juego en
  [Creative Uncut (A)](https://www.creativeuncut.com/art_pokemon-lets-go-pikachu-and-lets-go-eevee_a.html),
  [Bulbagarden Archives](https://archives.bulbagarden.net/wiki/Category:Art_from_Pok%C3%A9mon_Let's_Go,_Pikachu!_and_Let's_Go,_Eevee!)
  y la [galería de Nintendo Wiki](https://nintendo.fandom.com/wiki/Professor_Oak/gallery) ⚠️
  (no pude abrirlas; sale en los resultados de búsqueda).

### 2.4 Arte del anime
- Diseño de personajes del anime de 1997: **Sayuri Ichiishi** (一石小百合).
  También fue directora general de animación del capítulo 1 ✅
  ([Wikipedia japonesa](https://ja.wikipedia.org/wiki/%E4%B8%80%E7%9F%B3%E5%B0%8F%E7%99%BE%E5%90%88),
  [Pokémon Wiki japonesa](https://wiki.pokemonwiki.com/wiki/%E4%B8%80%E7%9F%B3%E5%B0%8F%E7%99%BE%E5%90%88),
  [Sakuga@wiki](https://w.atwiki.jp/sakuga/pages/732.html)). Dejó la serie
  de TV en la etapa de Advanced Generation.
- **Final de Ash** (2023): la miniserie *Aim to Be a Pokémon Master*
  vuelve a Kanto con Misty y Brock. Su póster reúne **todos los Pokémon de
  Ash en 25 años** ✅ ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Aim_to_Be_a_Pok%C3%A9mon_Master),
  [Nintendo Wiki](https://nintendo.fandom.com/wiki/Pok%C3%A9mon_To_Be_a_Pok%C3%A9mon_Master)).
  La cuenta oficial publicó un dibujo que junta **el principio y el final
  del viaje** ⚠️ ([Bulbapedia JN147](https://bulbapedia.bulbagarden.net/wiki/JN147)).
- Página oficial japonesa del anime:
  [pokemon.co.jp](https://www.pokemon.co.jp/tv_movie/anime/pokemon.html).

### 2.5 Las hojas de contacto (segunda pasada)
`investigar_serie.py` bajó **180 imágenes** de `pokemon.fandom.com`
(páginas de Pikachu y Ash) en 4 hojas numeradas. Las miramos las 4.
Quedan 3 en `hojas/`; la 3.ª (97-144: casi todo Pikachu repetido y
cartones de rango) no se guardó. El original de cada número sale del
índice de la herramienta, con su tamaño real.

**`hojas/arte-oficial_01.jpg`** (números 1-48)
| Nº | Qué es | Sirve para |
|---|---|---|
| [24](https://static.wikia.nocookie.net/pokemon/images/6/69/Ash_and_Professor_Oak.png) | Ash y **Oak en el laboratorio**, con Delia; Oak con bata a la izquierda (2876×1592) | **Oak explicando** en su sitio real; concepto A |
| [1](https://static.wikia.nocookie.net/pokemon/images/9/9a/Pikachu_%28Super_Smash_Bros._for_3DS_-_WiiU_Artwork%29.png) | Pikachu de pie, de frente, arte de Smash (4574×4369) | Pikachu **presentando**, la imagen más grande |
| [30](https://static.wikia.nocookie.net/pokemon/images/5/55/Young_Ash_and_Gary.png) | Ash y Gary de niños, riendo (2373×1800) | rivales que empezaron juntos |
| [35](https://static.wikia.nocookie.net/pokemon/images/3/36/Generation_I.png) | caja de **Pokémon Rojo**, viñetas de manga y Ash con Pikachu (2000×2000) | la generación de Oak; tramas del manga (P19) |
| [37](https://static.wikia.nocookie.net/pokemon/images/e/e9/Ash_and_Misty.png) | Ash y Misty discutiendo, Pikachu en el hombro (2147×1600) | **regañar** en grupo, época de Kanto |
| [38](https://static.wikia.nocookie.net/pokemon/images/9/9b/Hoenn_Badges.png) | estuche abierto con las 8 medallas de Hoenn (2147×1597) | un **objeto que se abre** con piezas dentro |
| [31](https://static.wikia.nocookie.net/pokemon/images/b/b0/Ash_and_his_Pok%C3%A9mon_in_the_Orange_League_Hall_of_Fame.png) | la placa del Salón de la Fama con las huellas (2357×1800) | objeto real con relieve para Blender |
| [34](https://static.wikia.nocookie.net/pokemon/images/7/71/Ash%27s_climbing_skills.png), [43](https://static.wikia.nocookie.net/pokemon/images/7/75/Ash_with_Pikachu_and_Riolu.png), [47](https://static.wikia.nocookie.net/pokemon/images/8/88/Ash_anime_Diamond_and_Pearl.png) | Ash trepando, tumbado con Pikachu y Riolu, y de cuerpo entero (Sinnoh) | poses vivas, **no de pie con una ropa** |
| 6-12 | cajas de las generaciones II-IX con viñetas de manga | arte de caja y de manga juntos |

**`hojas/vestuario_01.jpg`** (números 49-96)
| Nº | Qué es | Sirve para |
|---|---|---|
| [85](https://static.wikia.nocookie.net/pokemon/images/2/29/Ash_anime_XY_and_XYZ.png), [92](https://static.wikia.nocookie.net/pokemon/images/6/6d/Ash_anime_Journeys.png) | Ash de cuerpo entero en Kalos (corriendo) y en Viajes (mano en la gorra) | ropa de cada era, **sin mezclarlas** (punto 16) |
| [83](https://static.wikia.nocookie.net/pokemon/images/4/46/Ash_snow_wear.png), [95](https://static.wikia.nocookie.net/pokemon/images/b/b6/Ash_swimwear.png) | Ash con ropa de nieve y en bañador | ropa fuera de lo habitual |
| [88](https://static.wikia.nocookie.net/pokemon/images/e/ec/GS139_02.png) y 89 | las medallas **prendidas por dentro de la chaqueta** | detalle que un fan reconoce |
| [90](https://static.wikia.nocookie.net/pokemon/images/4/48/Pikachu_Libre_%28Pokk%C3%A9n_Tournament%29.png) | **Pikachu Libre**, máscara de luchador (Pokkén) | disfraz canon, lámina 2 |
| [60](https://static.wikia.nocookie.net/pokemon/images/d/d6/Ash_World_Coronation_Series_Trophy.png) | Ash con el trofeo de campeón mundial | **celebrar** |
| [62](https://static.wikia.nocookie.net/pokemon/images/6/63/Ash_XY_Young.png), [63](https://static.wikia.nocookie.net/pokemon/images/d/df/Ash_Young.png) | Ash de niño tendiendo la mano; Ash de niño con los puños de alegría | **invitar** y **animar** |
| 49-59 | los cristales Z en la mano de Ash | poco útil para esta lámina |

**`hojas/colaboraciones_01.jpg`** (números 145-180)
| Nº | Qué es | Sirve para |
|---|---|---|
| [147](https://static.wikia.nocookie.net/pokemon/images/4/44/XY006_17.png) | Ash **tiende la mano hacia la cámara**, en escorzo | la pose de «elige», mano hacia el que mira |
| [163](https://static.wikia.nocookie.net/pokemon/images/4/45/Ash_anime_Ruby_and_Sapphire.png) | Ash **lanzando la Pokébola**, pierna arriba (675×1280) | acción, «¡yo te elijo!» |
| [146](https://static.wikia.nocookie.net/pokemon/images/0/01/Ash_and_Pikachu.png) | Ash guiña un ojo y aprieta el puño, Pikachu en el hombro | **animar** |
| [164](https://static.wikia.nocookie.net/pokemon/images/b/b3/Ash_and_Gary.png), [160](https://static.wikia.nocookie.net/pokemon/images/5/53/Ash_and_Brock.png), [172](https://static.wikia.nocookie.net/pokemon/images/2/26/Ash_and_Dawn_high-fiving.png) | apretón de manos con Gary al atardecer, con Brock; choca los cinco con Dawn | **dar la bienvenida**, láminas en grupo |
| [154](https://static.wikia.nocookie.net/pokemon/images/7/7a/Ash_Dynamax.png) | Ash con una Pokébola gigante que brilla | Pokébola como objeto enorme |
| [149](https://static.wikia.nocookie.net/pokemon/images/8/89/Cosplay_Pikachu_anime.png) | **Cosplay Pikachu** con sus 5 trajes, en el anime | punto 16 y P23 |
| [168](https://static.wikia.nocookie.net/pokemon/images/3/39/0025Pikachu_Detective_Pikachu.png), [179](https://static.wikia.nocookie.net/pokemon/images/f/ff/Pikachu_clothing_art.jpg) | Detective Pikachu con lupa; Pikachu con ropa de camuflaje | poses nuevas por colaboraciones (P23) |
| [174](https://static.wikia.nocookie.net/pokemon/images/0/0f/Pok%C3%A9mon_the_Series_logo_English.png) | logo «Pokémon The Series» (1189×518) | letras del logo (punto 6) |
| 166, 175, 178 | Pikachu de UNITE, Holo Style y Pokkén | arte 3D moderno |

Ojo: en `partes/imagen.md` se citaron el nº155 como Cosplay Pikachu y el
nº172 como UNITE. Según el índice de la herramienta y la hoja, son el
**149** y el **166**; aquí ya van corregidos.

### 2.6 Más arte oficial fuera de la wiki
- **Portada y banner del anime** en [AniList](https://anilist.co/anime/527),
  medidos con Pillow: portada 230×345, banner 1900×400 ✅.
- **Pokémon Adventures** (manga), tomo 1: portada de **Mato** con Red,
  Saur, Poli y Pika saltando ✅
  ([How to Love Comics](https://www.howtolovecomics.com/2019/05/07/pokemon-manga-guide/),
  [CBR](https://www.cbr.com/pokemon-adventures-greatest-manga-covers/)).
  No hay enlace directo a la imagen ⚠️.
- **CD single «Mezase Pokémon Master»** (1997), el primer CD de Pokémon: un
  mini-CD con la Pikachu y el logo en **pegatinas** ✅
  ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Aim_to_Be_a_Pok%C3%A9mon_Master_(CD)),
  [J-Pop Wiki](https://jpop.fandom.com/wiki/Mezase_Pokemon_Master)).
- **Blu-ray** *Indigo League: Champion's Edition* (VIZ Media, 14-nov-2017):
  6 discos, 52 capítulos y un cómic de 64 páginas ⚠️ (una fuente:
  [ComicBook](https://comicbook.com/anime/news/pokemon-original-series-bluray/)).
- **Cartón de cuenta atrás**: sí hay uno oficial en la hoja 2, el
  [nº74 «Pokémon Day Countdown»](https://static.wikia.nocookie.net/pokemon/images/5/58/Pokemon_Day_Countdown_Pikachu.jpg)
  (1080×1920, Pikachu dormido en un cojín) ✅ (visto en la hoja).
- **Hojas de modelo** (giro del personaje) del anime: **no las encontré**
  publicadas (busqué en Sakuga Wiki y en blogs de animación japoneses) ⚠️.

---

## 3 · Escenas icónicas con su minuto

### 3.1 El capítulo 1: «¡Pokémon, yo te elijo!» (1997)
Japonés: ポケモン！きみにきめた！ ✅
([Pokémon Wiki japonesa](https://wiki.pokemonwiki.com/wiki/%E7%84%A1%E5%8D%B0%E7%B7%A8%E7%AC%AC1%E8%A9%B1),
[Pokémon Project, latino](https://pokemon-project.com/episodios/latino/serie-ash/temporada-1/episodio-1)).

Lo que pasa en el laboratorio ✅
([Twinfinite](https://twinfinite.net/features/pokemaniac-monday-rewatching-pokemon-anime-episode-1/),
[Pokémon Wiki](https://pokemon.fandom.com/es/wiki/Episodio_1_(serie_original)),
[TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Recap/PokemonS1E1PokemonIChooseYou)):
1. Ash llega tarde. Hay **tres Pokébolas en un soporte**, con **un hueco
   más en el centro**.
2. Las abre una a una: **Squirtle, vacía. Bulbasaur, vacía. Charmander,
   vacía.** Otros tres niños llegaron antes.
3. Oak admite que **tiene otro, pero hay un problema**.
4. Del hueco del centro **sube una Pokébola con un rayo pintado**.
5. Sale Pikachu. Ash lo abraza y **le da una descarga**.

Datos extra:
- Es **el único capítulo** en que se ve a Pikachu dentro de su Pokébola ✅
  ([Pokémon Wiki](https://pokemon.fandom.com/es/wiki/Episodio_1_(serie_original)),
  [Bulbapedia EP001, Trivia](https://bulbapedia.bulbagarden.net/wiki/EP001)).
- La apertura del capítulo (Ash ve por la tele un combate de Gengar contra
  Nidorino) **imita la intro de Pokémon Rojo/Verde** ✅ (Bulbapedia EP001).
- Pikachu **no quiere entrar en la Pokébola** ✅
  ([Pokémon Wiki japonesa](https://wiki.pokemonwiki.com/wiki/%E7%84%A1%E5%8D%B0%E7%B7%A8%E7%AC%AC1%E8%A9%B1),
  subtítulos de la película, abajo).
- **Vídeo oficial** del capítulo 1 en japonés, en el canal oficial:
  [YouTube `soM4HD71b6k`](https://www.youtube.com/watch?v=soM4HD71b6k).
  **Minuto sin verificar.** Es de 1997: imagen 4:3 y baja resolución.

### 3.1b El capítulo 1, **mirado de verdad** (segunda pasada)
Fuente: el capítulo real y completo en
[Internet Archive](https://archive.org/details/pokemon-indigo-league-season-1-1998)
(doblaje inglés de 4Kids, 480p, 22:23). Se recortaron dos tramos
(1:30-7:30 y 16:00-20:00) y se miraron **plano a plano** con
`fotogramas.py --cortes`. Los minutos son del capítulo en inglés; el
doblaje latino puede moverse 2-5 s.

| Minuto | Qué se ve | Fuente |
|---|---|---|
| ≈4:00 | Ash duerme con un **reloj Voltorb con un Pidgey de cuco** y lo rompe dormido | visto + [Bulbapedia EP001](https://bulbapedia.bulbagarden.net/wiki/EP001) ✅ |
| ≈4:42-5:09 | Llega tarde; **Gary** se va presumiendo: medallón yin-yang, **puño en alto**, porristas detrás | visto (fotograma 219) |
| **≈5:56** | **Tres Pokébolas en soportes en triángulo, con un hueco vacío en el centro** | visto (fotograma 266) ✅ |
| ≈6:03-6:24 | Oak abre las Pokébolas: **vacías** (Squirtle, Bulbasaur, Charmander, en ese orden) | visto + Bulbapedia ✅ |
| **≈6:48-6:52** | La Pokébola del centro, **con un rayo pintado**, se abre con un **destello dorado** | visto |
| **≈6:58** | Sale **Pikachu**, arisco, de pie sobre la mesa, chispas en las mejillas | visto (fotograma 328) |
| ≈7:04-7:12 | Pikachu **descarga** a Ash cuando lo toca | visto |
| **≈7:18** | Ash abraza a Pikachu, **los dos chamuscados y echando humo**; Oak serio detrás | visto (fotograma 348) |

- El laboratorio se ve como **sala circular** con las Pokébolas en
  soportes y **luz azulada** que entra por una claraboya ✅ (visto).
- Cada Pokébola lleva una **etiqueta en katakana** grabada. A 480p está
  borrosa: **no se pudo leer** y no la inventamos ⚠️.
- El **molino de viento** del laboratorio **no sale** en los planos de este
  capítulo (sólo el camino de subida) ⚠️.

### 3.2 La misma escena en alta: *La película Pokémon: ¡Yo te elijo!* (2017)
La película 20 **rehace el capítulo 1** para los 20 años del anime ✅
([Xataka México](https://www.xataka.com.mx/streaming/pokemon-yo-te-elijo-nos-da-una-pequena-muestra-de-su-doblaje-para-america-latina),
[Doblaje Wiki](https://doblaje.fandom.com/es/wiki/La_pel%C3%ADcula_Pok%C3%A9mon:_%C2%A1Yo_te_elijo!)).
Está **en Netflix México** con doblaje latino
([Netflix](https://www.netflix.com/mx/title/81046846)). Es **la mejor fuente
de fotogramas en 1080p** del laboratorio.

Minutos sacados de un archivo de subtítulos en inglés que está en GitHub
([imkira3/imkira3Keys](https://github.com/imkira3/imkira3Keys), archivo
`Subtitles/Pokémon Movie 20 - I Choose You.srt`). ⚠️ Es un subtítulo **no
oficial** (lleva un anuncio en la primera línea). El minuto puede moverse
unos segundos según la versión.

| Minuto | Qué se dice (inglés) | Para qué sirve |
|---|---|---|
| 00:01:39–00:02:00 | El narrador: «Este es Ash Ketchum, de Pueblo Paleta... pueden elegir su primer Pokémon del Profesor Oak: Bulbasaur, Charmander y Squirtle» | presentar las tres opciones |
| 00:02:06–00:02:19 | Ash, **dormido**, repasa «Bulbasaur... Charmander... Squirtle...» y grita «¡Yo te elijo!» | elegir en sueños |
| 00:02:31–00:02:49 | La madre: «¿Sigues dormido? ¡Llegarás tarde al laboratorio!» | la mañana, la prisa |
| 00:03:03–00:03:06 | «¡Profesor Oak, ya llegué!» / Oak: «Ah, hola, Ash.» | **saludo de Oak** |
| 00:03:10–00:03:14 | Oak: «Eres el último de los cuatro que empiezan hoy su viaje» | Oak explica |
| 00:03:22–00:03:26 | Oak: «Me temo que Squirtle se lo llevó alguien que no llegó tarde» | **regaño suave** |
| 00:03:44–00:03:48 | Oak: «Un segundo tarde a un tren, o a un Pokémon, te cambia la vida» | Oak filósofo |
| 00:03:57–00:04:05 | Oak: «Bueno, hay otro, pero... Debo avisarte de que tiene **un problema**» | **pensar, dudar** |
| 00:04:12–00:04:18 | Ash: «¡Genial! ¡Eres mi Pokémon!» → «¡Uoh!» | **sale la Pokébola del rayo** |
| 00:04:34–00:04:36 | Oak: «Este Pokémon se llama Pikachu» | **presentar** |
| 00:04:51–00:04:58 | La Pokédex: «Pikachu puede ser algo tímido, pero **electrizante cuando lo tocan**» | Pokédex habla |
| 00:05:04–00:05:07 | Oak: «Esta es **la Pokébola de Pikachu**» | **entregar** |
| 00:05:31–00:05:50 | Ash: «¡Entra en tu Pokébola!» → «Este Pikachu **odia** entrar en cualquier Pokébola» | la manía de Pikachu |

### 3.3 Otras escenas que todo fan reconoce
- **Ash se da la vuelta a la gorra** antes de un combate serio. En Kanto
  lo hacía mucho, porque reutilizaban la animación ⚠️ (resumen de
  búsqueda; vídeos de [TikTok](https://www.tiktok.com/@fandamncollectibles/video/7318016739621571882)
  y [Game Rant](https://gamerant.com/pokemon-anime-best-ash-ketchum-quotes/)).
- **«¡Pikachu, yo te elijo!»**, la frase de Ash ✅
  ([Trome](https://trome.com/espectaculos/celebridades/quien-es-gabriel-ramos-la-voz-latina-de-ash-ketchum-en-pokemon-animes-nndatl-noticia/),
  [Infobae](https://www.infobae.com/america/mexico/2022/12/16/fans-de-pokemon-le-agradecieron-a-gabo-ramos-por-haber-sido-la-primera-voz-de-ash-ketchum/)).
- **El lema del Equipo Rocket** (punto 10).
- **El final de Ash** en 2023 ([Bulbapedia JN147](https://bulbapedia.bulbagarden.net/wiki/JN147)).
  No hay clip oficial accesible sin YouTube: se deja con el enlace.
- **Ash girando la gorra**: en la segunda pasada tampoco salió un clip limpio
  (TikTok no se deja bajar; Dailymotion sin resultado) ⚠️.
### 3.4 Los Spearow y Ho-Oh (capítulo 1, mirado) ✅
Es **la escena más citada del anime** y faltaba. Mismo archivo de
Internet Archive, tramo 16:00-20:00:

| Minuto | Qué pasa |
|---|---|
| ≈16:02 | Ash conoce a **Misty**, que pesca en un río |
| ≈16:57 | Pikachu va **dormido en la cesta de la bici** de Misty |
| ≈17:16-17:19 | Una bandada de **Spearow** ataca; Pikachu lanza un rayo, pero lo hieren |
| ≈17:37-17:52 | Ash quiere meterlo en la Pokébola para protegerlo; Pikachu **se niega otra vez** |
| **≈18:03-18:23** | Ash corre bajo la lluvia con Pikachu en brazos y al final **se planta con los brazos abiertos** frente a la bandada |
| ≈18:28-19:39 | Entre el aguacero aparece un **ave dorada gigante**; sale un **arcoíris** y el ave vuela por encima |
| ≈19:58 | Ash y Pikachu, a salvo, se miran contentos: **nace la amistad** |

- El ave es **Ho-Oh** ✅ (Bulbapedia EP001 lo lista en «Pokémon debuts»).
  Que sea su primera aparición en cualquier medio, antes de Oro/Plata, es
  dato muy repetido pero con una sola fuente abierta ⚠️.
- Luz y paleta de esta escena, medidas: punto 5.

### 3.5 El lema del Equipo Rocket, mirado
[«Lema Team Rocket»](https://www.dailymotion.com/video/xs14pe) (Dailymotion,
35 s), mirado plano a plano: **Jessie y James de pie en silueta** contra un
fondo que gira (remolino de estrellas), brazo en alto; luego un primer
plano de cada cara con gesto exagerado; cierra **Meowth riendo a cámara**.
Sirve para «presentar en grupo». El idioma del clip no se pudo confirmar ⚠️.
Las dos mitades del lema en latino, con la voz real: punto 10.

---

## 4 · Fan art y 3D (sólo como referencia)

### 4.1 Modelos 3D descargables (Sketchfab)
**Segunda pasada:** las licencias, autores y caras de los modelos marcados
✅ se comprobaron con la **API de Sketchfab** (`api.sketchfab.com/v3/models/<id>`).
Dos autores estaban mal y se corrigieron. Los que siguen con ⚠️ no se
consultaron: mirar su página antes de usarlos. El crédito se pone así: «"Nombre" by Autor, licensed under CC BY
4.0». Todos son **fan art de un diseño con copyright** de Nintendo / The
Pokémon Company: valen para una lámina de fans, no para vender.

**Pokébolas** (para el concepto A):

| Modelo | Autor | Licencia (según la búsqueda) | Nota |
|---|---|---|---|
| [Poké Ball](https://sketchfab.com/3d-models/poke-ball-cd6f6c89fa5647d694991901f12becc2) | Pabluuu | **CC BY 4.0 ✅**, 227.582 caras | **hiperrealista**, materiales ya hechos: la mejor base |
| [Pokeball for Blender](https://sketchfab.com/3d-models/pokeball-for-blender-8613f35e2b734ab48a829c9cc371d8a5) | Kutter (@Foxrado) | **CC BY 4.0 ✅**, 627.964 caras | pensado para Blender; **muy pesado**: bajar el detalle antes de renderizar (regla 9 del dueño) |
| [Animated Poke Ball](https://sketchfab.com/3d-models/animated-poke-ball-2534c497425b4cde9cbb48181ea8a053) | Ayan (@Ayanbeg) | **CC BY 4.0 ✅**, 9.360 caras | se abre: sirve para una Pokébola entreabierta |
| [Pokeball (animated)](https://sketchfab.com/3d-models/pokeball-animated-a1f5d0bac5b74b73adc7d7d1eddc64d3) | Ahsan.Faraz | «Download Free» | alternativa animada |
| [Pokeball](https://sketchfab.com/3d-models/pokeball-190898b3bb1442b994b962b81b897a14) | KAOS_S4nt0 | CC BY | topología simple |
| [Poké Ball](https://sketchfab.com/3d-models/poke-ball-15ee12f8c7b14832a6b340c7a5f13649) | DravenX_Design | «Download Free» | — |
| [Low Poly Poké Ball](https://sketchfab.com/3d-models/low-poly-poke-ball-d643e45441634ab49c8aaab78998b5c5) | aolmedo910 | «Download Free» | low poly: no va con la luz real |
| [Etiqueta #pokeball](https://sketchfab.com/tags/pokeball) | varios | — | para buscar más |

**Laboratorio y Pokédex** (conceptos A y B):

| Modelo | Autor | Descarga | Nota |
|---|---|---|---|
| [Kanto Pokédex](https://sketchfab.com/3d-models/kanto-pokedex-33558224badf4058b5977bded912c70c) | Alexander Walker | **CC BY 4.0 ✅**, 6.590 caras | **la Pokédex roja**: base del concepto B |
| [Pokedex - Kanto Region (Red/Blue)](https://sketchfab.com/3d-models/pokedex-kanto-region-pokemon-redblue-ff6314a5f1c441a6998463b8bafd1ead) | BubbleGumBoio | ⚠️ ver página | otra Pokédex de Kanto |
| [Oak Lab](https://sketchfab.com/3d-models/oak-lab-fbe85c2f81a04063aa573f9161824734) | QuangCao | **CC BY 4.0 ✅**, 1.086 caras | el edificio |
| [Oak Pokemon Research Lab](https://sketchfab.com/3d-models/oak-pokemon-research-lab-31a6e01513ab42fa8d42a791ee852e9b) | hieuginta | «Download Free» | el edificio |
| [Pokémon Universal - Oak's Laboratory](https://sketchfab.com/3d-models/pokemon-universal-oaks-laboratory-4b36edc1f21f4a449bd034ffc287e884) | Lord Henry | ⚠️ ver página | interior low poly |
| [Professor Oak's Lab](https://sketchfab.com/3d-models/professor-oaks-lab-b635af0cc1514450b2027b1b161a4550) | Josh Bowman | ⚠️ | hecho con el pixel art de Rojo Fuego |
| [Pokemon Professor's Lab](https://sketchfab.com/3d-models/pokemon-professors-lab-c4c70e08bd804c40ae1cf0af2a3da76b) | OR3KI | ⚠️ | interior con estanterías y ordenadores |
| [Professor Oak's Laboratory](https://sketchfab.com/3d-models/professor-oaks-laboratory-646f17bad7e44f6caa62f490bc0fb9d1) | AlanParker17 | ⚠️ | — |
| [Pokemon Professor Oak](https://sketchfab.com/3d-models/pokemon-professor-oak-212d5d395ad14367aacac0be70922acb) | **lopuh22721** (antes ponía «3D Resource») | **CC BY 4.0 ✅**, 8.068 caras, **con esqueleto** | Oak en 3D **que se puede posar** en Blender; no pegar |

**Game Boy** (para la lámina 2 o una variante):

| Modelo | Autor | Licencia |
|---|---|---|
| [GameBoy DMG-01](https://sketchfab.com/3d-models/gameboy-dmg-01-29849a15fe0a40a6a18e01c9d544a0ed) | Let's Do 3D | **CC BY 4.0 ✅**, 18.119 caras |
| [GAME BOY](https://sketchfab.com/3d-models/game-boy-5fe78ea0dddf47a2adaecd6044d637c1) | **MaxWendt** (antes ponía «rave-games») | **CC BY 4.0 ✅**, 1.618 caras, con la textura original |
| [Nintendo Gameboy DMG-01 3D Scan](https://sketchfab.com/3d-models/nintendo-gameboy-dmg-01-3d-scan-26144110dbbe469cb87ce3a055b5c0df) | stevencmutter | CC BY-NC-ND ✅: **no se puede modificar** ni usar para vender |

**Personajes con esqueleto y otros modelos (nuevos, comprobados por la API)**

| Modelo | Autor | Licencia | Nota |
|---|---|---|---|
| [Pikachu](https://sketchfab.com/3d-models/pikachu-35716003a1964704b1b145e6c6a05b07) | Eleanie | CC BY 4.0 ✅, 106.512 caras, **con esqueleto** | sombreado tipo cómic que se puede apagar |
| [Ash Ketchum](https://sketchfab.com/3d-models/ash-ketchum-f767f1a21b924033991a7fb1fb19820d) | Neut2000 | CC BY 4.0 ✅, 8.613 caras, **con esqueleto** | el Ash en 3D que faltaba |
| [Pikachu low poly](https://sketchfab.com/3d-models/pikachu-c22dab8fc3064c76a0c502d64555a74f) | jacobjksn42 | CC BY ✅, 4.500 caras, con esqueleto | para una pose lejana |
| [Pikachu low poly](https://sketchfab.com/3d-models/pikachu-37c740f674cd4719a1d1d2970bbe8c30) | raghav-wd | CC BY ✅, 4.500 caras, con esqueleto | alternativa |
| [Pokemon RSE - Pokemon Center](https://sketchfab.com/3d-models/none-ae2858d8d212406ebe95927d4f17d328) | Wesai | CC BY 4.0 ✅, 10.041 caras | Centro Pokémon: icono de «soporte» |
| [Pokemon FireRed - Player's Room](https://sketchfab.com/3d-models/none-b23b6b253207463c97db2a7092adff74) | Wesai | CC BY 4.0 ✅, 972 caras | el cuarto del jugador |
| [Ultimate Monsters Pack](https://sketchfab.com/3d-models/none-fd72e114d119488da71fe3a16f216c4f) | quaternius | CC BY 4.0 ✅, 212.178 caras | criaturas genéricas, sólo de relleno |
| [Lucario](https://sketchfab.com/3d-models/none-32ab2458321e495084fe3bc3b3bf6a91) | **GianmArt** (el primer barrido ponía «Gianmarco») | CC BY 4.0 ✅, 63.606 caras | — |

Crédito exacto de cada uno: campo `licencia` de `referencias.json`.

### 4.2 Fan art y renders (mirar, nunca pegar)
- [Professor Oak's Lab Background](https://www.deviantart.com/willdinomaster55/art/Professor-Oak-s-Lab-Background-939863010), WillDinoMaster55: el laboratorio donde se elige inicial.
- [Professor Oak's Lab background](https://www.deviantart.com/toonsislove83/art/Professor-Oak-s-Lab-background-1039893253), Toonsislove83: fondo sacado de un capítulo.
- [Professor Oak's Lab](https://www.deviantart.com/pokemoncmg/art/Professor-Oak-s-Lab-995779070), PokemonCMG: estilo carta del juego de cartas.
- [Pokemon Prof. Oaks Lab](https://www.deviantart.com/malice936/art/Pokemon-Prof-Oaks-Lab-601381104), malice936: pixel art de 32×32.
- [Professor Oak's Lab](https://www.deviantart.com/rosegardeninhell/art/Professor-Oak-s-Lab-321160234), RosegardenInHell.
- [Pokebuildings 3D model Oak labs](https://www.deviantart.com/studioseraph/art/Pokebuildings-3D-model-Oak-labs-903344416), StudioSeraph.
- [Pokemon Oaks Lab Voxel Pixel Art](https://www.pixiv.net/en/artworks/119328838) (pixiv): **el momento de elegir inicial**, en vóxeles.
- [Etiqueta オーキド博士 en pixiv](https://www.pixiv.net/en/tags/%E3%82%AA%E3%83%BC%E3%82%AD%E3%83%89%E5%8D%9A%E5%A3%AB): 438 dibujos de Oak.
- [Professor Oak's Laboratory](https://www.artstation.com/artwork/GeqxP3) (ArtStation): 3D basado en Let's Go y en el anime.
- [Pokémon Fan Art - Poké Ball](https://www.artstation.com/artwork/d0aD5J), Ricardo Amaral Accioly (ArtStation): Pokébola realista, para la luz.
- [Pallet Town Background](https://www.deviantart.com/willdinomaster55/art/Pallet-Town-Background-865889425), WillDinoMaster55: Pueblo Paleta.
- [«Pokémon LE-GO»](https://live.staticflickr.com/8652/28615487170_7b3bfba3c0_b.jpg), Si-MOCs (Flickr, CC BY-NC-SA 2.0, 602×1024): Pokémon de ladrillos hecho por fans. Sólo para saber que la idea ya existe.
- En Danbooru, `recolectar.py` no dio con la etiqueta exacta y no se repitió a mano ⚠️.

---

## 5 · Sitios, luz, paleta y texturas

### 5.1 Pueblo Paleta (Masara)
- Satoshi Tajiri, el creador, se basó en **su ciudad, Machida**, cuando aún
  era campo y él cazaba insectos ✅
  ([GoNintendo](https://www.gonintendo.com/contents/41748-take-a-tour-of-the-japanese-city-that-inspired-pokemon-s-pallet-town),
  [TheGamer](https://www.thegamer.com/pokemon-pallet-town-trivia/),
  [Wikipedia](https://en.wikipedia.org/wiki/Satoshi_Tajiri)).
- «Paleta» viene de **la paleta de pintor**: casi todos los pueblos de Kanto
  llevan nombre de color ⚠️ (resumen de búsqueda).
- **Paleta oficial de Pueblo Paleta** en Super Game Boy, sacada del código
  ([`data/sgb/sgb_palettes.asm`](https://raw.githubusercontent.com/pret/pokered/master/data/sgb/sgb_palettes.asm)),
  convertida por mí a hex ✅:

| Nombre en el código | Colores |
|---|---|
| `PAL_PALLET` (Pueblo Paleta) | blanco `#FFEFFF` · **menta `#CEE6DE`** · **celeste `#A5D6FF`** · casi negro `#191010` |
| `PAL_ROUTE` (rutas) | blanco `#FFEFFF` · **verde hierba `#ADE65A`** · celeste `#A5D6FF` · `#191010` |
| `PAL_TOWNMAP` (mapa) | `#FFEFFF` · `#A5D6FF` · `#8CBD52` · `#191010` |
| `PAL_YELLOWMON` (Pikachu) | `#FFEFFF` · `#FFE673` · `#D6A500` · `#191010` |
| `PAL_REDMON` (Charmander) | `#FFEFFF` · `#FFA552` · `#D65231` · `#191010` |
| `PAL_BLUEMON` (Squirtle) | `#FFEFFF` · `#94A5DE` · `#5A7BBD` · `#191010` |
| `PAL_GREENMON` (Bulbasaur) | `#FFEFFF` · `#A5D684` · `#4AA55A` · `#191010` |

### 5.2 El laboratorio de Oak
- En el anime: edificio blanco en una loma, con **un molino de viento**
  (aerogenerador), **tres ventanas en el balcón interior** y cuatro en el
  segundo piso. Detrás, **el corral de Oak**: un prado donde viven los
  Pokémon de los entrenadores del pueblo ✅
  ([Pokémon Wiki](https://pokemon.fandom.com/wiki/Professor_Oak%27s_Laboratory),
  [Pallet Town Wiki](https://pallettown.fandom.com/wiki/Professor_Oak's_Laboratory),
  [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Professor_Oak's_Laboratory)).
- Ash deja ahí a todos sus Pokémon menos a Pikachu cada vez que se va a
  otra región ✅ (mismas fuentes).
- En Rojo Fuego / Verde Hoja: **tres ayudantes, estanterías llenas de
  libros, una mesa con tres Pokébolas, un ordenador y dos Pokédex en
  blanco** ✅ ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Professor_Oak's_Laboratory),
  [Pokémon Let's Play Wiki](https://pokemonlp.fandom.com/wiki/Professor_Oak's_Laboratory)).
  HeartGold/SoulSilver lo pasa a 3D con el mismo diseño.
- Japonés: オーキドけんきゅうじょ, donde los niños de Pueblo Paleta reciben
  a su primer compañero ✅
  ([Pokémon Wiki japonesa](https://wiki.xn--rckteqa2e.com/wiki/%E3%82%AA%E3%83%BC%E3%82%AD%E3%83%89%E3%81%91%E3%82%93%E3%81%8D%E3%82%85%E3%81%86%E3%81%98%E3%82%87)).
- **Luz**: es por la mañana. Ash se durmió ✅ (subtítulos, 00:02:31).
  Luz de día que entra por ventanas grandes y fluorescentes de
  laboratorio. **Segunda pasada:** en el capítulo 1 real se ve una **sala
  circular** con las Pokébolas en soportes y **luz azulada, fría**, que
  entra por una **claraboya** ✅ (visto, ≈5:56). El molino de viento no
  sale en los planos de ese capítulo: sigue con la fuente de la wiki ⚠️.

### 5.3 Colores de los iniciales, **medidos** sobre el arte oficial
Medí los colores más abundantes de cada imagen de PokéAPI (±5 por canal).
El arte de los juegos es de acuarela, más apagado. El render de HOME es
más saturado, **más parecido al anime**.

| Pokémon | Arte de los juegos | Render HOME (usar este) |
|---|---|---|
| Pikachu | `#F2D57A` · sombra `#E4C471` | **`#FEE200`** · `#F8CD00` · sombra `#E9BA00` |
| Charmander | `#E7A97C` · vientre `#F3E5CA` | **`#F98200`** · `#E37100` · vientre `#FDFD97` |
| Squirtle | `#67A2B5` · `#8EC5D2` | **`#70CFF6`** · `#6AC5E9` · `#59ADD3` |
| Bulbasaur | `#77A693` · `#94CAAD` | **`#7DC6BA`** · bulbo `#54B235` |
| Charizard | `#ECA263` · alas `#4D94A3` | — |

### 5.3b Colores medidos **en fotogramas del anime** (segunda pasada)
Con `estilo.py` sobre fotogramas del capítulo 1 real (Internet Archive,
480p). Sirven para comparar con el arte oficial de arriba.

| Fotograma | Paleta medida | Cómo está pintado |
|---|---|---|
| **Pikachu** sobre la mesa (≈6:58, sólo el cuerpo) | cuerpo **`#CAA62D`** (54 %) · sombra `#C8A527` · mejillas y franjas `#9C502A` · contorno `#322822` | **plano (cel)**, saturación 69 %, brillo 70 % |
| **Ash bajo la tormenta** (≈18:23) | azules de noche `#222D35` · `#27363F` · `#2C424F` · `#324B65` · acento verde azulado `#3F6E6E` (árboles a contraluz) | **degradado, fondo pintado a mano**, saturación 43 %, brillo 32 % |

- El amarillo del capítulo de 1997 es **más apagado y marrón** que el
  `#FEE200` de HOME: la cinta de vídeo y la compresión bajan la saturación.
  Para la lámina manda el de HOME; el `#CAA62D` sirve si se quiere un aire
  «anime clásico, cinta vieja».
- La tormenta de los Spearow es la escena **más oscura y pintada** que se
  miró: vale si una lámina quiere lluvia y drama en vez de mañana soleada.
- Gary en el capítulo 1 (≈5:09) lleva jersey **azul marino** (a ojo, sin
  medir) y el medallón yin-yang verde y amarillo ⚠️.

### 5.4 Texturas reales equivalentes (CC0)
- Mesa de laboratorio: [Wood Table Worn](https://polyhaven.com/a/wood_table_worn),
  [Wood Table 001](https://polyhaven.com/a/wood_table_001) y el modelo
  [Wooden Table 01](https://polyhaven.com/a/WoodenTable_01) (Poly Haven, CC0).
- Paredes y muebles blancos: [Painted Wood 003](https://ambientcg.com/view?id=PaintedWood003)
  (ambientCG, CC0).
- Madera del suelo o del soporte: [Wood 027](https://ambientcg.com/view?id=Wood027) (ambientCG, CC0).
- Luz de día para Blender: [HDRIs de Poly Haven](https://polyhaven.com/hdris) (CC0).
- Etiquetas de las Pokébolas: cartulina o papel kraft con cordel.
  **Resuelto:** [Paper004](https://ambientcg.com/view?id=Paper004) (papel,
  CC0) o [Cardboard002](https://ambientcg.com/view?id=Cardboard002)
  (cartón kraft, CC0), de ambientCG ✅ (API de ambientCG).

---

## 6 · Tipografía

### 6.1 Lo que usa la franquicia
- **Game Boy (Rojo, Azul, Amarillo)**: letra de píxeles de 8×8. Está en
  el código: [`gfx/font/font.png`](https://raw.githubusercontent.com/pret/pokered/master/gfx/font/font.png) ✅.
  Trae el **▼** y el **▶** del cursor.
- **Espada/Escudo y Escarlata/Púrpura**: letras «UD» de **Fontworks**:
  **Rodin NTLG DB** para japonés y **UDKakuGo Condensed 80 M** para el
  alfabeto latino ✅ (dos publicaciones de la misma cuenta, sobre dos juegos
  distintos: [Fontendo, Escarlata/Púrpura](https://x.com/Fontendou/status/1554863045259788290)
  y [Fontendo, Espada/Escudo](https://x.com/fontendou/status/1162760191898574848)).
  Son de pago.
- **El logo «Pokémon»**: amarillo con borde azul, letras gordas y
  redondas. Lista de letras de los logos en la
  [Pokémon Wiki](https://pokemon.fandom.com/wiki/List_of_fonts_used_in_Pok%C3%A9mon_logos),
  [Pokémon Aaah!](https://www.pokemonaaah.net/art/fonts/) y
  [Pokémon Dungeon](https://www.pokemondungeon.com/media-downloads/fonts) ⚠️ (no pude abrirlas).

### 6.2 Letras libres comprobadas por mí
Las bajé de GitHub y miré con fontTools si cada letra existe **y tiene
dibujo** (no una caja vacía). Además las probé escribiendo «¿Qué haces?
¡Elige tu inicial! Ñandú».

| Letra | Para qué | De dónde | Licencia | á é í ó ú ñ ¿ ¡ |
|---|---|---|---|---|
| **pokemon-font** (Superpencil, ahora «Johto font») | **la caja de Game Boy**: es un clon de la letra de Rojo/Azul, ampliada | [GitHub cooljeanius/pokemon-font](https://github.com/cooljeanius/pokemon-font), archivo `fonts/pokemon-font.ttf` | **OFL** ✅ (su LICENSE.md) | ✅ todas, y ▼. ⚠️ A tamaño pequeño la «é» se ve casi como «ê»: revisar a 1:1 |
| **Press Start 2P** | pixel genérico, más limpio | [google/fonts](https://raw.githubusercontent.com/google/fonts/main/ofl/pressstart2p/METADATA.pb) | OFL ✅ | ✅ todas, y ▼. Subconjuntos latin y latin-ext |
| **Pokémon Solid** | **el logo** | [cdnfonts](https://www.cdnfonts.com/pokemon-solid.font), [dafont](https://www.dafont.com/pokemon.font); archivo probado de [tjklint/PokePC](https://github.com/tjklint/PokePC) | de fans, diseñada por **IPBP** (2007): «libre para uso personal y comercial citando al diseñador» ✅ ([FontSpace](https://www.fontspace.com/pokemon-solid-font-f13844), [VectorDad](https://vectordad.com/fonts/pokemon-solid/)). El archivo no trae licencia dentro: vale para el Discord, con crédito | ✅ todas: `aacute`… `ntilde`, `questiondown`, `exclamdown`, **cada una con contorno dibujado** (fontTools sobre el `.ttf` real, segunda pasada) |
| **Lilita One** | logo o título gordo, **con licencia limpia** | google/fonts | OFL ✅ | ✅ todas |
| **Luckiest Guy** | título de cómic, alternativa | google/fonts | Apache 2.0 ✅ | ✅ todas |
| **M PLUS Rounded 1c** | cajas de Espada/Escarlata (en vez de Rodin) | google/fonts | OFL ✅ | ✅ todas |
| **Barlow Semi Condensed** | cajas modernas, letra latina estrecha (en vez de UDKakuGo Condensed) | google/fonts | OFL ✅ | ✅ todas |

**Consejos de uso**
- pokemon-font mide **10 px** de alto: úsala a **múltiplos de 10** (40,
  50, 60 px) y **sin suavizado**, o se emborrona ✅ (su README).
- En la caja de Game Boy **cada línea tiene como mucho 18 letras** (punto
  7). Corta los textos a mano.
- El logo es **amarillo con borde azul**. **Medido** en la segunda pasada
  con `estilo.py` sobre el [SVG oficial de Wikimedia](https://upload.wikimedia.org/wikipedia/commons/9/98/International_Pok%C3%A9mon_logo.svg)
  pasado a PNG de 1200 px ✅:

| Parte del logo | Medido | Valor de marca (usar este) |
|---|---|---|
| Relleno de las letras | `#FECA02` | **`#FFCB05`** |
| Borde de cada letra | `#3566AE` | **`#3D7DCA`** |
| Sombra 3D detrás | `#213A71` | **`#003A70`** |
| Sombreado dentro de la «o» y la «e» | `#C8A10D` | — |

  Los valores de marca salen de [Brand Palettes](https://brandpalettes.com/pokemon-color-codes/)
  y [Design Pieces](https://www.designpieces.com/palette/pokemon-logo-color-palette-hex-and-rgb/)
  ✅; difieren 1-2 puntos de lo medido por la compresión.


### 6.3 Una letra para cada uso (propuesta con las letras ya comprobadas)
El anime no usa globos: habla con **subtítulos**, la **caja de texto de
los juegos** es su «globo» (punto 7). Con las letras de 6.2:

| Uso | Letra | Por qué |
|---|---|---|
| Logo o título («Autoroles») | **Pokémon Solid**, o **Lilita One** si se quiere licencia limpia | la del logo; amarillo `#FFCB05` con borde `#3D7DCA` |
| Texto normal (caja de Game Boy) | **pokemon-font**, a 40-60 px sin suavizado | clon de la letra de Rojo/Azul |
| Texto normal (caja moderna, Let's Go o Escarlata) | **M PLUS Rounded 1c** o **Barlow Semi Condensed** | en lugar de Rodin y UDKakuGo, que son de pago |
| Grito u onomatopeya («¡Pika!», «¡Yo te elijo!») | **Luckiest Guy** | letra de cómic, gorda |
| Pensamiento | la misma de la caja, en gris | ⚠️ no se comprobó cómo marcan un pensamiento los juegos ni el anime |
| Cartel del mundo (letrero del laboratorio) | **Press Start 2P** si es pixel; Barlow si es moderno | ⚠️ no se midió un cartel real del anime |
| Interfaz de juego (menús, ▶) | **pokemon-font** o **Press Start 2P** | traen ▶ y ▼ |
| Subtítulos o créditos | **Barlow Semi Condensed** | estrecha y legible |

⚠️ No se encontraron las letras de los globos del manga *Pokémon
Adventures* ni de los carteles del anime: por eso esta tabla es una
propuesta con letras comprobadas, no una copia de la original.

---

## 7 · Cómo hablan en pantalla: el cuadro de diálogo

> [!tip] La idea clave
> En Pokémon, la gente no habla en globos: habla en **la caja de texto del
> juego**. Todo fan la reconoce. Y el **▼** parpadeante que dice «pulsa
> para seguir» apunta **hacia abajo**, justo donde están las reacciones
> de #autoroles.

### 7.1 La caja de Rojo y Azul, medida en el código ✅
Todo sale de [pret/pokered](https://github.com/pret/pokered):
[`data/text_boxes.asm`](https://raw.githubusercontent.com/pret/pokered/master/data/text_boxes.asm),
[`home/text.asm`](https://raw.githubusercontent.com/pret/pokered/master/home/text.asm),
y `gfx/font.asm` (visto con la búsqueda de código de GitHub).

| Qué | Dato exacto | Traducido a la lámina |
|---|---|---|
| Pantalla | 20×18 casillas de 8 px (160×144) | — |
| Caja de mensaje | `MESSAGE_BOX` de la casilla (0,12) a la (19,17): **todo el ancho, las 6 filas de abajo** | la caja ocupa **un tercio de alto** de la pantalla |
| Texto | empieza en la casilla (1,14); la 2.ª línea, en la (1,16) | **dos líneas** con una fila vacía entre ellas |
| Largo de línea | 18 casillas | **18 letras por línea**, como mucho |
| Flecha | `▼` en la casilla (18,16), **parpadea** hasta que pulsas A o B | abajo a la derecha, **sin caja propia** |
| Borde | casillas `┌ ─ ┐ │ └ ┘` dibujadas en `font_extra.png`: **doble línea** y **esquinas con un nudo redondo** (lo vi en el archivo) | no es un rectángulo simple: son dos filetes y esquinas de adorno |
| Color | 2 tonos: fondo claro y letra oscura. En Super Game Boy, `#FFEFFF` y `#191010` | blanco roto y casi negro |

**Cómo escribe un personaje** (texto oficial en español de Rojo/Azul, de
[abcboy101/poke-corpus](https://github.com/abcboy101/poke-corpus), archivo
`corpus/RedBlue/es_msg.txt`) ✅:
- El nombre va **delante, en mayúsculas y con dos puntos**: «**OAK:** ¡Si
  aparece un #MON salvaje, tu #MON podrá luchar contra él!».
- Los nombres de cosas van **en mayúsculas**: POKé BALL, PROF. OAK,
  PUEBLO PALETA, MAPA de PUEBLOS.
- Muchas **exclamaciones**, frases cortas.

### 7.2 Otras generaciones
| Generación | La caja | Estado |
|---|---|---|
| 3 (Rojo Fuego / Verde Hoja) | La **letra es azul** si habla un hombre y **roja** si habla una mujer. Oak habla en azul. Fondo blanco, sombra gris claro | ✅ en el código de [pret/pokefirered](https://github.com/pret/pokefirered): `include/constants/vars.h` (`NPC_TEXT_COLOR_MALE 0 // Blue`, `FEMALE 1 // Red`) y `src/new_menu_helpers.c` (`TEXT_COLOR_BLUE, TEXT_COLOR_WHITE, TEXT_COLOR_LIGHT_GRAY`); el laboratorio usa `textcolor NPC_TEXT_COLOR_MALE` |
| 7.5 (Let's Go) | **Medida en la segunda pasada** sobre [una captura real de Switch](https://interfaceingame.com/wp-content/uploads/pokemon-lets-go-pikachu/pokemon-lets-go-pikachu-dialogue.jpg) (Interface In Game, 1280×720): fondo **blanco roto cálido `#FDFCFA`-`#F3F4F1`** con una trama diagonal sutil; borde **dorado oliva apagado** de `#88893D` a `#C8C899`, 2-4 px; texto gris casi negro; **una Poké Ball pequeña abajo a la derecha** en lugar del ▼ | ✅ medido con `estilo.py` (Game UI Database siguió en 403) |
| 8 (Espada / Escudo) | cápsula blanca redonda, pestaña del nombre negra `#1F1F1F` | ✅ en la guía de cuadros (medido) |
| 9 (Escarlata / Púrpura) | rectángulo blanco translúcido, pestaña azul marino `#0B1C38`, barritas amarillas `#FCDB06` | ✅ en la guía de cuadros (medido) |

Más cajas de la saga, en la sección
[Dialogue & Speech de Game UI Database](https://gameuidatabase.com/index.php?scrn=162&series=37&set=1&sort=2&tag=41%2C30) ⚠️.

### 7.3 Otros «cuadros» que tiene Pokémon
- **La Pokédex habla.** En el anime, la de Ash (Kanto, **roja**) tiene voz
  y un poco de carácter: hasta es sarcástica con Ash ✅
  ([Pokémon Wiki](https://pokemon.fandom.com/es/wiki/Pok%C3%A9dex),
  [WikiDex](https://www.wikidex.net/wiki/Pok%C3%A9dex_(anime))). En inglés
  la llaman **Dexter**; Ash a veces la llama «Déxter» ✅
  ([Wikipedia](https://es.wikipedia.org/wiki/Pokemon_dexter),
  [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Dexter)). Voz
  japonesa de la T1 a la T5: Shinichiro Miki. Voz latina: **no la
  encontré**.
- **La entrada de Pokédex** tiene su fórmula: nombre + «el Pokémon
  Ratón» + una frase. En español: Pikachu es «**Pokémon Ratón**»,
  Charmander «**Pokémon Lagartija**», Squirtle «**Pokémon Tortuguita**»,
  Bulbasaur «**Pokémon Semilla**» ✅ ([PokeAPI, `pokemon_species_names.csv`](https://github.com/PokeAPI/pokeapi)).
- **«¿Quién es ese Pokémon?»**: la silueta negra antes del corte. En el
  latino volvió en Negro y Blanco con voces de niños ✅ (dos páginas de
  Doblaje Wiki: [la franquicia](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon_(franquicia))
  y [Pokémon: Negro y Blanco](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon_Negro_y_Blanco),
  por la API: «se buscan voces infantiles para hacerlo, pero hay bastante
  inestabilidad en cuanto a los actores»). **No hubo una voz fija**: no es
  un hueco de la investigación.
- **La voz latina de la Pokédex**: en tres capítulos de Totodile
  (temporada 3) fue **Rubén León** ⚠️ (una fuente, Doblaje Wiki). Para el
  resto de temporadas no se encontró.
- **Las lecciones del Profesor Oak** al final de cada capítulo japonés,
  con un **senryū** (poema corto) al cierre ✅
  ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Professor_Oak's_Pok%C3%A9mon_Lecture),
  [pokemon.com](https://www.pokemon.com/us/pokemon-news/professor-oaks-pokemon-poetry-on-pokemon-tv)).

### 7.4 Qué NO hacer con el texto
- Una **burbuja blanca redonda**: en Pokémon nadie habla así.
- Una caja **sin ▼** o **sin borde doble**: deja de parecer Pokémon.
- Mezclar la caja pixelada de Game Boy con letra moderna, o al revés.
- Líneas de más de 18 letras en la caja de Game Boy.
- Copiar el español de los juegos tal cual: es **de España** («Venga,
  elige uno», «estáis», «Vale»). Para el servidor, pásalo a latino.

---

## 8 · Los personajes

### Profesor Oak (Samuel Oak · オーキド・ユキナリ, Yukinari Ōkido)
**Qué es.** El «PROFESOR POKéMON» de Pueblo Paleta. Da el primer Pokémon
y la Pokédex a los niños del pueblo. En el juego se presenta así ✅
(texto oficial en español, [poke-corpus](https://github.com/abcboy101/poke-corpus)):
> «¡Hola a todos! ¡Bienvenidos al mundo de POKéMON! ¡Me llamo OAK! ¡Pero
> la gente me llama el PROFESOR POKéMON!» ... «Estudio a los POKéMON como
> profesión.»

**Su historia.**
- De joven fue **un buen entrenador**: «¡Cuando yo era joven, era un buen
  entrenador de POKéMON! Pero ahora sólo me quedan 3» ✅ (Rojo/Azul).
- Agatha, del Alto Mando, lo pica: «Hace tiempo ese viejo inútil era
  **fuerte y apuesto**... ¡Ahora sólo juguetea con su POKéDEX!» ✅ (Rojo/Azul).
- Su sueño: «Hacer una guía completa de todos los Pokémon del mundo... ¡Ese
  era mi sueño! Pero soy demasiado viejo» ✅ (Rojo Fuego, [pret/pokefirered](https://github.com/pret/pokefirered)).
- Es **abuelo de Gary**, el rival ✅ ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Professor_Oak_(anime))).
- En una versión temprana de Rojo/Verde, el juego lo llamaba
  «**Ōkido-sensei**» (profesor de escuela) y **ibas a combatir contra él al
  final** ✅ ([The Cutting Room Floor](https://tcrf.net/Pok%C3%A9mon_Red_and_Blue),
  [Unused Trainers](https://tcrf.net/Pok%C3%A9mon_Red_and_Blue/Unused_Trainers)).

**Carácter** ✅ ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Professor_Oak_(anime)),
[Wikipedia](https://en.wikipedia.org/wiki/Professor_Oak),
[TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/PokemonTheOriginalSeries)):
- **El sabio despistado**: muy listo, un poco excéntrico, se olvida de
  cosas.
- **Poeta**: escribe **senryū** sobre Pokémon y los recita al cerrar sus
  lecciones. Hasta publicó un libro de poemas en el anime.
- Presenta **cinco secciones** de final de capítulo en Japón.
- TV Tropes le apunta coqueteo con Delia, la madre de Ash, y poca vida
  social ⚠️ (una fuente).

**Cómo habla** (texto oficial y subtítulos):
- **Se olvida y se corrige en voz alta**: «¿Gary? Déjame pensar... ¡Ah,
  sí! Te pedí que vinieras» ✅ (Rojo/Azul).
- **Se ríe cortito**: «¡Bien!» en español; «Haha!» en inglés ✅.
- **Explica paso a paso y con paciencia**: «¡No sabrás más cosas sobre los
  POKéMON con sólo verlos! ¡Tienes que atraparlos!» ✅ (Rojo/Azul).
- **Regaña suave, sin gritar**: «Me temo que Squirtle se lo llevó alguien
  que no llegó tarde» ✅ (película, 00:03:22).
- **Filosofa**: «Un segundo tarde a un tren, o a un Pokémon, te cambia la
  vida» ✅ (película, 00:03:44).
- **Avisa antes**: «Debo avisarte de que hay un problema con este último»
  ✅ (película, 00:04:01).
- **Voz latina**: Hugo Navarrete. Desde mediados de la temporada 1, una voz
  **ronca, llena de experiencia** ⚠️ (Doblaje Wiki, por el resumen de la
  búsqueda).
- Lenguaje corporal: en el sprite de Game Boy, **una mano en el pecho** ✅
  (lo vi). En el anime, manos a la espalda o un dedo en alto al explicar ⚠️
  (de memoria: comprobar en los fotogramas del punto 3).

### Pikachu (el de Ash)
**Qué es.** El «**Pokémon Ratón**» ✅ ([PokeAPI](https://github.com/PokeAPI/pokeapi)).
La cara de la franquicia.

**Su historia en el anime.**
- Es **el que sobraba**: el Pokémon «con un problema» del laboratorio ✅
  (punto 3).
- **Odia la Pokébola**. Va **en el hombro o en la cabeza** de Ash ✅
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Characters/PokemonTheSeriesPikachu),
  [Pokémon Wiki](https://pokemon.fandom.com/wiki/Ash's_Pikachu)). En
  Pokémon Amarillo lo dice Oak: «Parece que a tu PIKACHU no le gustan las
  POKé BALL. Deberás tenerlo junto a ti. ¡Eso le hará feliz!» ✅ (texto
  oficial en español).
- Le encanta **el kétchup** ✅ (TV Tropes, Pokémon Wiki).
- **Rechazó evolucionar** a Raichu con una Piedra Trueno: quería demostrar
  su fuerza tal cual ⚠️ (resumen de búsqueda, TV Tropes).
- Diseño de **Atsuko Nishida**: empezó siendo una ardilla; las puntas
  negras de las orejas vienen de un diseño anterior con forma de *daifuku*
  ⚠️ (una fuente, resumen).
- Fue la mascota **en vez de Clefairy**, porque gustaba a niños y niñas
  ✅ ([Den of Geek](https://www.denofgeek.com/games/pikachu-pokemon-mascot-history-nintendo/),
  [Screen Rant](https://screenrant.com/pokemon-why-pikachu-mascot-clefairy-original-game-freak/)).

**Cómo se expresa.**
- **Sólo dice su nombre**, con la voz de **Ikue Ōtani** en todos los
  idiomas ✅ (punto 10).
- **Chispas en las mejillas** cuando se enfada o se defiende: «Las bolsas
  de las mejillas están llenas de electricidad, que libera cuando se siente
  amenazado» ✅ (Pokédex de Pokémon Y, en español).
- **Cómo saluda**: «Los miembros de esta especie **se saludan uniendo sus
  colas** y transmitiéndose corriente eléctrica» ✅ (Pokédex de Escudo).
- **Tímido pero electrizante si lo tocan** ✅ (película, 00:04:51).

### Ash Ketchum
**Qué es.** Un niño de **casi diez años** de Pueblo Paleta que quiere ser
Maestro Pokémon ✅ (película, 00:01:39).

**Carácter** (del capítulo 1 y la película):
- **Impulsivo y de buen corazón**. Llega tarde y lo asume con humor: «¿Y
  qué? Si llegué tarde, ¡el problema también lo tengo yo!» ✅ (00:04:05).
- **Cariñoso aunque le cueste**: «¡Aguanto una descarguita!» ✅ (00:05:00).
  «¡Tú y yo vamos a ser los mejores amigos!» ✅ (00:04:44).
- Iba a elegir **a Squirtle** ✅ (película, 00:03:19; Pokémon Wiki).
- **Se da la vuelta a la gorra** cuando va en serio ⚠️ (punto 3.3).
- Frase: «**¡Yo te elijo!**» ✅.
- Guiño de los juegos: en Rojo/Azul en español, **«ASH» es uno de los
  nombres que el juego te propone**, y «GARY» para el rival ✅ (menú
  «¿TU NOMBRE?»: NUEVO N. / ROJO / ASH / JAIME).

### Los tres iniciales de Kanto
Nombres y frases **oficiales en español** ✅ ([PokeAPI](https://github.com/PokeAPI/pokeapi)):

| Pokémon | Categoría | Una frase de su Pokédex | Qué transmite |
|---|---|---|---|
| **Bulbasaur** | Pokémon Semilla | «A Bulbasaur es fácil verle echándose una siesta al sol» (Rubí Omega) | calma, paciencia |
| **Charmander** | Pokémon Lagartija | «La llama de su cola **indica la fuerza vital**. Será brillante si está sano» (X). «Llamea levemente cuando está alegre y arde vigorosamente cuando está enfadado» (Rubí Omega) | **la llama dice lo que siente**: sirve de luz |
| **Squirtle** | Pokémon Tortuguita | «Se protege con su caparazón y luego contraataca lanzando agua a presión» (X) | travieso, defensivo |

En el capítulo 1 **los tres ya no están**: se los llevaron otros niños ✅.

### Los secundarios más queridos (para tenerlos a mano)
- **El Equipo Rocket**: Jessie, James y Meowth. Su lema en latino es
  historia del doblaje (punto 10). La muerte de Diana Pérez (Jessie) en
  2021 fue noticia en medio continente ✅
  ([Infobae](https://www.infobae.com/america/entretenimiento/2021/04/28/doblaje-mexicano-de-luto-cuales-fueron-los-personajes-a-los-que-les-dio-voz-diana-perez/),
  [El Universal](https://www.eluniversal.com.mx/espectaculos/james-del-equipo-rocket-lamenta-la-muerte-de-jessie-diana-perez/),
  [SuperGeek](https://www.supergeek.cl/noticias/cultura-pop/ha-fallecido-diana-perez-la-inolvidable-voz-de-jessie-en-pokemon/2021-04-28/113137.html)).
- **Charizard**: el Pokémon de Kanto más votado (punto 9).
- **Misty y Brock**: vuelven con Ash en su despedida de 2023 ✅
  ([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Aim_to_Be_a_Pok%C3%A9mon_Master)).
- **Serena**: la compañera más votada en Japón en 2021 ⚠️ (una fuente,
  [Nlab](https://nlab.itmedia.co.jp/research/articles/198660/)).

---

## 9 · ¿Quién es el más querido?

| Encuesta | Resultado | Estado |
|---|---|---|
| **Pokémon of the Year 2020**, oficial y mundial | 1.º Greninja (140.559 votos), 2.º Lucario, 3.º Mimikyu, **4.º Charizard (93.968)**, 5.º Umbreon. **Pikachu, 19.º (48.060)** | ✅ [Newsweek](https://www.newsweek.com/greninja-pokemon-year-2020-day-google-vote-results-full-list-top-1489550), [Digital Trends](https://www.digitaltrends.com/gaming/greninja-pokemon-of-the-year/), [Famitsu](https://www.famitsu.com/news/202002/27193553.html), [web oficial](https://pokemon2020.pokemon.com/en-us/) |
| **ポケモン総選挙720**, Japón, 2016 | 1.º Greninja, 2.º Arceus, 3.º Mew, **4.º Pikachu**, 5.º Sylveon | ✅ [pokemon.jp](https://www.pokemon.jp/info/event/detail/20160607_13811.html), [Oricon](https://www.oricon.co.jp/news/2072963/full/), [Cinema Today](https://www.cinematoday.jp/news/N0083941) |
| Corea, 2016 | **1.º Pikachu**, 9.º Charizard | ⚠️ [Namuwiki](https://namu.wiki/w/%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0/%EC%9D%B8%EA%B8%B0%ED%88%AC%ED%91%9C) |
| Iniciales, encuesta de fans (unas 4.000 personas, 2021) | Charizard y su línea encabezan | ⚠️ [Nintendo Life](https://www.nintendolife.com/news/2021/01/almost_4000_people_have_ranked_their_top_starter_pokemon_-_here_are_the_results), [Dexerto](https://www.dexerto.com/pokemon/pokemon-survey-most-popular-744873/) |
| Japón, 2025 | Charizard arriba | ⚠️ [CBR](https://www.cbr.com/most-popular-pokemon-2025-ranked-japan/) |

**Conclusión para la lámina**
- **Pikachu** es la cara que todos reconocen, pero **no gana los votos**
  fuera de Asia.
- De la lista del encargo, **Charmander/Charizard es el más votado** de
  verdad.
- **Oak** no es «el más querido», pero **elegir inicial es su momento**:
  es quien tiene que hablar.
- Por eso: Oak habla, Pikachu es el guiño, y un concepto se lo damos a
  Charmander.
- No hay encuesta latinoamericana ⚠️. El cariño latino al Equipo Rocket y
  a Gabo Ramos sale en la prensa, no en votos.

---

## 10 · Doblaje latino

**Estudio**: **Audiomaster 3000**, México. **Director**: **Gerardo
Vásquez**, que recibió del cliente un glosario de ataques y nombres para
Latinoamérica ✅
([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Pok%C3%A9mon),
[Azteca Jalisco](https://www.aztecajalisco.com/espectaculos/quien-hizo-el-doblaje-pokemon-en-espanol-latino-actores-estudios-y-datos-que-no),
[PRODU](https://www.produ.com/television/noticias/audiomaster-3000-inicia-doblaje-de-la-segunda-pelicula-de-pokemon/)).
Se dobló **desde la versión de Estados Unidos**. Estreno en Cartoon Network
el 6 de septiembre de 1999 ⚠️ (una fuente). Traducción: Bernardo López ⚠️
(una fuente).

| Personaje | Voz latina | Estado |
|---|---|---|
| **Profesor Oak** | **Hugo Navarrete** (también en la película de 2017) | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Hugo_Navarrete), [Xataka](https://www.xataka.com.mx/streaming/pokemon-yo-te-elijo-nos-da-una-pequena-muestra-de-su-doblaje-para-america-latina), [WikiDex](https://www.wikidex.net/wiki/Hugo_Navarrete?mobileaction=toggle_view_mobile) |
| **Ash** | **Gabriel «Gabo» Ramos**, del capítulo 1 hasta 2009 (temporadas 1 a 12). Volvió en *Viajes* como el Ash de otra dimensión | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Ash_Ketchum), [El Comercio](https://elcomercio.pe/respuestas/que/que-fue-de-la-vida-de-gabo-ramos-la-voz-de-ash-ketchum-en-pokemon-la-voz-de-ash-tdex-revtli-noticia/), [ANMTV](https://www.anmtvla.com/2022/05/viajes-pokemon-gabo-ramos-vuelve-ser-la.html), [Código Espagueti](https://codigoespagueti.com/noticias/anime/doblaje-de-viajes-pokemon-trae-de-vuelta-a-gabo-ramos-el-primer-ash-ketchum/) |
| **Ash** (desde la temporada 13 y en la película de 2017) | **Miguel Ángel Leal** | ✅ El Comercio, Xataka |
| **Pikachu** | **Ikue Ōtani**, la voz japonesa, **conservada en todos los doblajes** | ✅ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Ikue_%C5%8Ctani), [WikiDex](https://www.wikidex.net/wiki/Ikue_%C5%8Ctani), [Wikipedia](https://en.wikipedia.org/wiki/Ikue_%C5%8Ctani) |
| Pikachu cuando **habla** en la película de 2017 | Ana Lobo | ⚠️ [Doblaje Wiki](https://doblaje.fandom.com/es/wiki/La_pel%C3%ADcula_Pok%C3%A9mon:_%C2%A1Yo_te_elijo!) |
| **Misty** | **Xóchitl Ugarte** | ✅ [Otaku Press (entrevista)](https://www.otakupress.pe/2016/10/entrevista-misty-pokemon-xochitl-ugarte-otakufest.html), [Anime Argentina](https://animeargentina.net/xochitl-ugarte-doblaje/), Azteca Jalisco |
| **Brock** | **Gabriel Gama** | ✅ [Anime Argentina](https://animeargentina.net/gabriel-gama-doblaje/), Azteca Jalisco |
| **Jessie** | **Diana Pérez** (murió el 27 de abril de 2021) | ✅ Infobae, El Universal, SuperGeek |
| **James** | **Pepe Toño Macías** | ✅ El Universal, [su TikTok oficial](https://www.tiktok.com/@pepetomaciasoficial/video/7414164314644434181) |
| **Meowth** | **Gerardo Vásquez** (el director) | ✅ [TikTok de Doblaje a la Mexicana](https://www.tiktok.com/@doblajealamexicana/video/7309360974945979654), El Universal |
| La Pokédex | — | **no encontrado** |

**Frases del doblaje latino**
- «**¡Pikachu, yo te elijo!**» ✅ (Trome, Infobae).
- «**¡A la carga!**» ⚠️ (una fuente: [Trome](https://trome.com/espectaculos/celebridades/quien-es-gabriel-ramos-la-voz-latina-de-ash-ketchum-en-pokemon-animes-nndatl-noticia/)).
- **El lema del Equipo Rocket** ✅ (Pokémon Wiki en la guía de cuadros, y
  Pepe Toño Macías diciendo «¡Jame me me mes!» en su TikTok):
  > Prepárense para los problemas. Y más vale que teman. ... ¡El Equipo
  > Rocket viajando a la velocidad de la luz! ¡Ríndanse ahora o prepárense
  > a luchar! ¡Meowth! ¡Así es!
- Título del capítulo 1: «**¡Pokémon, yo te elijo!**» ✅.
- **Pokébola**: en el anime latino se dice «Pokébola»; en España, «Poké
  Ball» ⚠️ ([WikiDex](https://www.wikidex.net/wiki/Pok%C3%A9bola/Pok%C3%A9_Ball_(anime)));
  el merchandising de 1999 respetó los términos del anime
  ([ANMTV](https://www.anmtvla.com/2022/05/existe-merchandising-oficial-de-pokemon.html)).
- **Ojo**: los juegos clásicos llegaron **en español de España**. La
  primera traducción oficial al **español latino** fue la de Pokémon GO ⚠️
  (titular de [3DJuegos LATAM](https://www.3djuegos.lat/nintendo-switch/pokemon-go-sera-primer-juego-traduccion-oficial-espanol-latino-olvidate-ascuas-placaje-a-bocajarro)).
  Por eso el texto de la lámina se adapta: «Pokébola», «ustedes», sin
  «vale».

**Más para empaparse**: [Momentos del doblaje latino, por Gabo Ramos](https://www.tiktok.com/@gaboramosoficial/video/7503704723560647944);
[reparto latino de *Viajes*](https://funianime.com/conoce-al-elenco-del-doblaje-latino-de-viajes-pokemon/);
[30 años de Pokémon: dónde están los actores](https://www.elgrafico.mx/espectaculos/2026/02/26/30-anos-de-pokemon-donde-estan-hoy-los-actores-de-doblaje-que-hicieron-historia-en-mexico/);
[redoblaje de las primeras temporadas](https://www.anmtvla.com/2015/06/pokemon-episodios-de-las-primeras.html?m=1).

---

## 11 · Música

- **Pueblo Paleta** y **el laboratorio de Oak** en Rojo/Azul: de **Junichi
  Masuda**, compositor fundador de Game Freak ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Junichi_Masuda),
  [YouTube](https://www.youtube.com/watch?v=YvyKWwfAxKg),
  [YouTube](https://www.youtube.com/watch?v=DRhYIdiNiGI)). Existe un
  arreglo oficial para violín y orquesta (Ray Chen, Royal Philharmonic)
  ✅ ([Spotify](https://open.spotify.com/track/6It0cr5QyBlwk0B5Qk7DZd)).
  Ambiente: **tranquilo, de pueblo, de principio de viaje** ⚠️ (mi
  descripción).
- **Música del anime**: **Shinji Miyazaki**, que adaptó temas de los
  juegos ⚠️ (una fuente: [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Pocket_Monsters_Original_Soundtrack_Best)).
- **Opening latino**: «**¡Atrápalos ya!**», versión del tema de Estados
  Unidos que cantó **Jason Paige**. Se oyó en los primeros 83 capítulos ⚠️.
  Lo canta **Óscar Roa** ⚠️
  ([Gizmodo](https://es.gizmodo.com/esta-es-la-voz-de-la-mitica-cancion-original-de-pokemon-1784473767),
  [Pianos PUCH](https://pianospuch.com.ar/cancion-pokemon-del-inicio-letra-piano/),
  [Letras.com](https://www.letras.com/pokemon/1679402/)).
- Para la lámina: el laboratorio pide la **alegría curiosa** del tema de
  Oak. No es un mundo sombrío: nada de tonos oscuros.

---

## 12 · Vídeos

| Vídeo | Qué sirve | Minuto |
|---|---|---|
| [Capítulo 1, oficial, japonés](https://www.youtube.com/watch?v=soM4HD71b6k) | el laboratorio y la Pokébola del rayo, dibujo de 1997 | **sin verificar** |
| [*¡Yo te elijo!* en Netflix México](https://www.netflix.com/mx/title/81046846) | la misma escena **en alta y en latino** | laboratorio **00:03:03–00:05:11**; Pokébola del rayo ≈ **00:04:12** (subtítulo no oficial) |
| [Opening 1 latino en 1080p](https://www.youtube.com/watch?v=8RXz6Uru9WY) | ambiente, logo | sin verificar |
| [Opening latino con letra](https://www.youtube.com/watch?v=Rs46UiNEk-Y) | la letra de «¡Atrápalos ya!» | sin verificar |
| [Pallet Town, Junichi Masuda](https://www.youtube.com/watch?v=YvyKWwfAxKg) | el tema del pueblo | — |
| [Gabo Ramos: momentos del doblaje latino](https://www.tiktok.com/@gaboramosoficial/video/7503704723560647944) | la voz de Ash | sin verificar |
| [Pepe Toño Macías y el lema Rocket](https://www.tiktok.com/@pepetomaciasoficial/video/7414164314644434181) | James hoy, con Rebeca Gómez haciendo de Jessie | sin verificar |
| [Diana Pérez, Pepe Toño y Gerardo Vásquez](https://www.tiktok.com/@doblajealamexicana/video/7309360974945979654) | el trío Rocket original | sin verificar |
| [Ash da la vuelta a la gorra](https://www.tiktok.com/@fandamncollectibles/video/7318016739621571882) | el gesto | sin verificar |

**Tendencias de TikTok**: el eterno debate «**¿qué inicial eliges?**»,
con encuestas en los comentarios y creadores que puntúan cada inicial
contra los líderes de gimnasio ⚠️
([Kanto Starter Pokemon](https://www.tiktok.com/discover/kanto-starter-pokemon),
[Pokemon Starter Meme](https://www.tiktok.com/discover/pokemon-starter-meme)).
**Justo la pregunta de #autoroles.**

---

## 13 · Videojuegos: interfaz y menús

Menús **oficiales en español** de Rojo/Azul ✅ (poke-corpus, `es_msg.txt`):

| Pantalla | Texto real | Idea para el servidor |
|---|---|---|
| Elegir nombre | «¿TU NOMBRE?» → NUEVO N. / ROJO / **ASH** / JAIME | un menú de lista con ▶ = elegir rol |
| Nombre del rival | «¿NOMBRE RIVAL?» → NUEVO N. / AZUL / **GARY** / JUAN | — |
| Menú de inicio | POKéDEX, POKéMON, OBJETOS, GUARDAR, OPCIÓN, SALIR y tu nombre (el orden exacto no lo comprobé) | — |
| PC de Pokémon | SACAR PKMN / DEJAR PKMN / SOLTAR PKMN / CAMBIA CAJA / ¡NOS VEMOS! | **sacar y dejar = ponerte y quitarte roles** |
| Ficha de entrenador | NOM. / DIN. / TIEMPO / MEDALLAS | una ficha de quién eres |
| Centro Pokémon | CURAR / SALIR | — |
| Sí o no | SÍ / NO | — |

- En Amarillo, el nombre propuesto «ROJO» pasa a ser «**GUALDO**» ✅.
- Rojo Fuego/Verde Hoja: letra azul para hombres y roja para mujeres ✅
  (punto 7.2).
- **Contenido descartado** ([TCRF](https://tcrf.net/Pok%C3%A9mon_Red_and_Blue),
  [Unused Code](https://tcrf.net/Development:Pok%C3%A9mon_Red_and_Blue/Unused_Code),
  [Unused Maps](https://tcrf.net/Development:Pok%C3%A9mon_Red_and_Blue/Unused_Maps)) ✅:
  - El código de la Pokédex del laboratorio marca como vistos a
    Bulbasaur, Charmander, Squirtle **y también a Ivysaur**, por error.
  - Oak iba a tener **una escuela** («to okido school»).
  - Había un **combate contra Oak** al final del juego.
- Interfaz moderna: [Let's Go en Game UI Database](https://www.gameuidatabase.com/gameData.php?id=96),
  [menú de Let's Go en Interface In Game](https://interfaceingame.com/screenshots/pokemon-lets-go-pikachu-menu/),
  [Escarlata/Púrpura](https://www.gameuidatabase.com/gameData.php?id=1579) ⚠️ (no abiertas).

---

## 14 · Lo que ama el fandom, y qué NO hacer

### Lo que todos reconocen
- **«¿Eres chico o chica?»**: casi todos los profesores lo preguntan al
  empezar el juego, y es meme ✅
  ([Wikipedia](https://en.wikipedia.org/wiki/Professor_Oak),
  [me.me](https://me.me/t/pokemon-professors)).
- **El aviso de Oak que sale de la nada**: si usas algo donde no toca,
  aparece «**OAK: ¡Rojo! ¡Éste no es momento de usarlo!**» ✅ (texto
  oficial de Rojo/Azul en español). Es perfecto para «Aquí no se escribe».
- **Pikachu y la Pokébola**: no entra ni a la de tres ✅.
- **«¡Pikachu, yo te elijo!»** y **la gorra al revés** ✅ / ⚠️.
- **El Equipo Rocket saliendo volando** y su lema latino ✅.
- **El debate de los iniciales**: cuál elegiste, cuál era mejor ✅ / ⚠️
  (punto 12).
- **Ash con 10 años para siempre** ⚠️ (resumen de búsqueda).
- **Gabo Ramos**: los fans le dieron las gracias en masa cuando terminó la
  historia de Ash ✅ ([Infobae](https://www.infobae.com/america/mexico/2022/12/16/fans-de-pokemon-le-agradecieron-a-gabo-ramos-por-haber-sido-la-primera-voz-de-ash-ketchum/)).
- **Latino contra España**: los memes que comparan los dos doblajes ⚠️
  ([TikTok](https://www.tiktok.com/discover/pokemon-doblaje-latino)).

### Qué NO hacer (lo que un fan notaría)
- **Pikachu metido feliz en su Pokébola.** Sólo pasa en el capítulo 1, y a
  disgusto.
- **Charmander con la llama apagada** o junto al agua. Su Pokédex dice que
  si se apaga, se debilita o muere ✅ (Pokédex de Y y de Escudo).
- **Pikachu hablando en frases.** Sólo dice su nombre. El que habla es
  Meowth.
- **Mezclar ropas de Ash**: la gorra de Kanto con la chaqueta de otra
  región.
- **Oak sin bata** o joven: se le reconoce por la bata blanca y el pelo
  gris.
- **Escribir «Poké Ball» y «Pokébola» en la misma lámina.** Elegir una: para
  el servidor, «Pokébola».
- **Español de España** en boca de Oak («Venga», «Vale», «estáis»).
- **Una burbuja blanca redonda** (punto 7.4).
- **Colores oscuros o de terror**: Pokémon es luz de día y colores limpios.

---

## 15 · Poses analizadas por personaje

> ⚠️ Los fotogramas de la película **no los vi**: el minuto sale del
> subtítulo y la acción, de lo que se dice. Lo que sí miré (arte oficial y
> sprites) lo marco con 👁.

### Profesor Oak
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | 👁 [sprite de Game Boy](https://raw.githubusercontent.com/pret/pokered/master/gfx/trainers/prof.oak.png) | de pie, bata, **mano en el pecho**, serio | **presentar** con solemnidad |
| 2 | película, 00:03:05 | «Ah, hola, Ash» | **saludar** |
| 3 | película, 00:03:10 | cuenta que Ash es el último de cuatro | **explicar** |
| 4 | película, 00:03:22 | «alguien que no llegó tarde» | **regañar** sin enfado |
| 5 | película, 00:03:57–00:04:05 | «hay otro, pero... tiene un problema» | **pensar**, dudar |
| 6 | película, 00:04:34 | «Este Pokémon se llama Pikachu» | **presentar** (la mejor para el concepto A) |
| 7 | película, 00:05:04 | entrega la Pokébola de Pikachu | **entregar**, animar a empezar |
| 8 | [Let's Go, arte de Sugimori](https://www.creativeuncut.com/gallery-36/plgp-professor-oak.html) | arte oficial moderno | presentar ⚠️ no abierto |
| 9 | [Oak 3D en Sketchfab](https://sketchfab.com/3d-models/pokemon-professor-oak-212d5d395ad14367aacac0be70922acb) | modelo para girar y encontrar el ángulo | referencia de volumen |

### Pikachu
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | 👁 [arte oficial](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png) | salta, brazos abiertos, boca abierta | **celebrar** |
| 2 | 👁 [render HOME](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/25.png) | brazos arriba, sonrisa grande | **animar** |
| 3 | 👁 [sprite de Game Boy](https://raw.githubusercontent.com/pret/pokered/master/gfx/pokemon/front/pikachu.png) | redondo, **chispas en las mejillas** | **avisar**, enfado |
| 4 | película, 00:04:12–00:04:18 | sale de la Pokébola del rayo | **aparecer**, sorpresa |
| 5 | película, 00:04:51–00:05:02 | da una descarga a Ash | **regañar** |
| 6 | película, 00:05:31–00:05:50 | se niega a entrar en la Pokébola | terquedad, humor |
| 7 | anime, en el hombro de Ash ✅ | va sentado en el hombro | **acompañar**, señalar |
| 8 | Pokédex de Escudo ✅ | saluda uniendo la cola con otro | **saludar** (gesto propio) |

### Ash
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | 👁 [sprite de Rojo](https://raw.githubusercontent.com/pret/pokered/master/gfx/player/red.png) (el Ash de los juegos) | mano en la cintura, gorra calada | presentar con chulería |
| 2 | película, 00:02:06–00:02:19 | dormido, grita «¡Yo te elijo!» | **elegir**, humor |
| 3 | película, 00:02:43 | «Mamá, ¿por qué no me despertaste?» | prisa, apuro |
| 4 | película, 00:03:03 | entra: «¡Ya llegué!» | **llegar**, saludar |
| 5 | película, 00:04:05 | acepta al Pokémon «con problema» | decisión |
| 6 | película, 00:04:40–00:04:46 | abraza a Pikachu | **celebrar** |
| 7 | gesto de la gorra al revés ⚠️ | gira la gorra antes del combate | **animar**, ir en serio |

### Charmander
| # | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| 1 | 👁 [arte oficial](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png) | de pie, brazos abiertos, sonríe, llama arriba | **presentar**, saludar |
| 2 | 👁 [render HOME](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/4.png) | colores de anime | color de referencia |
| 3 | Pokédex ✅ | la llama arde fuerte si se enfada, suave si está alegre | **la llama cuenta el ánimo** |

---

## 16 · Vestuario

**Ash en Kanto** (la ropa «icónica») ✅
([Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Ash's_clothing),
[Costume Wall](https://costumewall.com/dress-like-ash-ketchum/),
[TV Style Guide](https://www.tvstyleguide.com/pokemon/how-to-dress-like-ash-ketchum/),
[CBR](https://www.cbr.com/pokemon-ash-ketchum-best-outfits/)):
- **Chaqueta de manga corta blanca y azul**, con bolsillos y una franja
  dorada abajo; cuello y mangas blancos.
- **Camiseta negra** debajo.
- **Vaqueros azules** con puños celestes.
- **Zapatillas negras y blancas**.
- **Guantes verdes sin dedos**, con borde verde claro.
- **Gorra roja y blanca con un símbolo verde**: la gorra de la **Pokémon
  League Expo**. La llevó en Kanto, las Islas Naranja y Johto ✅
  ([Tumblr, historia de su ropa](https://www.tumblr.com/groundrunner100/657971968801423360/the-history-of-ash-ketchums-attire-from-my)).
- Colores en hex: **no los medí** ⚠️. Sacarlos del fotograma 00:03:03 de
  la película.

**Oak**: **bata blanca** de laboratorio ✅ (sprite 👁). Pelo gris y camisa
de color debajo ⚠️ (de memoria).

**La Pokébola de Pikachu**: una Pokébola normal con **un rayo dibujado** ✅.
Color del rayo ⚠️ (no comprobado).

**Otras eras de Ash** (para no mezclarlas): cada región cambia de ropa
([CBR, 10 mejores trajes](https://www.cbr.com/pokemon-best-ash-ketchum-outfits-designs/)).

---

## 17 · Paisajes y fondos de pantalla

- **Pueblo Paleta** de día: menta `#CEE6DE` y celeste `#A5D6FF` ✅ (punto 5).
- **El laboratorio** en su loma con el molino, y **el corral** detrás ✅.
- **La Ruta 1**: verde hierba `#ADE65A` ✅.
- **Fondos de fans**: [Pallet Town Background](https://www.deviantart.com/willdinomaster55/art/Pallet-Town-Background-865889425)
  y [Professor Oak's Lab Background](https://www.deviantart.com/willdinomaster55/art/Professor-Oak-s-Lab-Background-939863010)
  (WillDinoMaster55), [fondo del laboratorio sacado de un capítulo](https://www.deviantart.com/toonsislove83/art/Professor-Oak-s-Lab-background-1039893253)
  (Toonsislove83). Tamaño: ⚠️ no lo pude ver.
- **Fondos oficiales en alta**: **no los encontré** ⚠️. Con red, mirar la
  galería de la wiki y las cuentas oficiales.
- **Paleta de colores de los juegos de Game Boy Color**: la explica
  [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Color_palette_(Generations_I%E2%80%93II)) ⚠️ (no abierta).

---

## 18 · Guía para generar con IA (Firefly, Canva)

**Rasgos que nunca cambian**
- Oak: hombre mayor, pelo gris, **bata blanca de laboratorio**.
- Pikachu: amarillo `#FEE200`, **puntas de las orejas negras**, mejillas
  rojas redondas, cola en **forma de rayo**, rayas marrones en la espalda.
- Ash (Kanto): gorra roja y blanca con símbolo verde, chaqueta blanca y
  azul de manga corta, guantes verdes sin dedos.
- Charmander: naranja `#F98200`, vientre crema, **llama siempre encendida**.
- Pokébola: mitad roja, mitad blanca, franja negra y **botón blanco** en
  el centro.

**Estilo**
- Anime de 1997: **línea fina y limpia, colores planos, sombra dura de dos
  tonos** ⚠️ (descripción mía, de memoria; comparar con el capítulo 1).
- Fondos **pintados a mano**, más suaves que los personajes ⚠️.
- Luz: **mañana soleada**, cielo celeste, sombras cortas.
- Encuadre: plano medio, cámara a la altura de la mesa.

**Palabras que ayudan**
«1990s anime cel style», «clean thin lineart», «flat colors», «two-tone
cel shading», «bright morning light», «laboratory with bookshelves and a
large window», «white lab coat», «red and white ball with a black band».

**Palabras que lo estropean**
«realistic», «3D render» (para el personaje), «dark», «grim», «horror»,
«photorealistic skin», «chibi», «watercolor» (salvo para imitar el arte de
los juegos).

**Referencias de estilo y pose**
- Estilo del Pokémon: los renders de HOME (colores) y el arte oficial
  (forma).
- Estilo del anime: fotogramas de la película de 2017, minutos del punto 3.
- Pose de Oak: fotograma 00:04:34 (presentar).
- Ojo: una IA **no debe inventar** a Oak ni a Pikachu de cero. Úsala para
  **fondos, luz y objetos**; el personaje, recortado de una imagen real.
  Y recuerda la regla del dueño: nada que parezca hecho por IA.

---

## P18 · Estilo de dibujo y técnica, y cómo replicarlo

_(pendiente)_

---

## P19 · Texturas 2D

_(pendiente)_

---

## P20 · Gustos y detalles de cada personaje

_(pendiente)_

---

## P21 · Por qué la gente la ama

_(pendiente)_

---

## P22 · Fan dubs y comunidad hispana

_(pendiente)_

---

## P23 · Colaboraciones, cruces, figuras y cosplay

_(pendiente)_

---

## P24 · Obras parecidas y temas relacionados

_(pendiente)_

---

## P25 · El mundo, la historia y sus símbolos

_(pendiente)_

---

## 19 · Tres conceptos para la lámina de #autoroles

> Los tres usan la misma idea de fondo: **elegir tus roles es elegir tu
> inicial**. Cambian el objeto, el sitio, la hora, el personaje y la caja.

### Concepto A — «La mesa de las Pokébolas» (el del plan, mejorado)
**Objeto y sitio.** El **soporte de Pokébolas del laboratorio de Oak**,
como en el capítulo 1: tres huecos y **uno en el centro**, un poco más
alto, con **la Pokébola del rayo** ✅. En Blender: la base, las cuatro
Pokébolas ([modelo de Pabluuu](https://sketchfab.com/3d-models/poke-ball-cd6f6c89fa5647d694991901f12becc2),
CC BY) y la mesa ([Wood Table Worn](https://polyhaven.com/a/wood_table_worn), CC0).
De cada Pokébola cuelga una **etiqueta de cartulina con cordel**; la tinta
sigue la curva del papel.

**Personaje.** **Oak** detrás de la mesa, con la mano abierta hacia las
Pokébolas: pose de **presentar** (película, 00:04:34). **Pikachu** sentado
junto a la Pokébola del rayo, **de espaldas a ella**, con cara de «ni lo
pienses» (odia la Pokébola ✅).

**Cómo habla.** La **caja de Rojo/Azul** (punto 7.1): abajo, un tercio de
alto, doble filete con esquinas de nudo, **dos líneas de 18 letras** y el
**▼ parpadeando abajo a la derecha**, que aquí apunta a las reacciones.
Letra: **pokemon-font** a 40 o 50 px, sin suavizado.

**Dónde va cada texto**
| Texto | Dónde |
|---|---|
| **Autoroles** | placa del soporte, en letra de logo (**Lilita One** o Pokémon Solid), amarilla con borde azul |
| **Elige tus roles como eliges tu inicial** | cartel en la pared del laboratorio, detrás de Oak |
| **Reacciona abajo y elige tu color y tu país** | **la caja de texto**, cortada así: «Tu color y tu país» (18) / «¡reacciona abajo!» (17) + ▼ |
| Pokébola 1: **¿Qué haces?** → Canales y roles | etiqueta |
| Pokébola 2: **¿De dónde eres?** → reacciona abajo | etiqueta (o Canales y roles, si el dueño lo decide así) |
| Pokébola 3: **¿Qué buscas?** → Canales y roles | etiqueta |
| **Canales y roles está arriba del todo.** / **Lo cambias cuando quieras.** | nota pegada en la base del soporte, en dos líneas |
| Pokébola del rayo: **¿Algo no funciona? Abre un ticket en soporte** | etiqueta de la del centro: **es la que «tiene un problema»** |
| **Aquí no se escribe** | cartel pequeño en el borde de la mesa, en letra de píxel. O, como guiño al aviso de Oak «¡Éste no es momento de usarlo!» ✅, una caja pequeña aparte: «OAK: ¡Aquí no» / «se escribe!» |

**Cómo no queda plano**
- **Delante**, desenfocado, el **antebrazo de Ash** entrando por abajo a la
  izquierda: guante verde sin dedos y manga blanca y azul, alargándose
  hacia una Pokébola. Se ve el brazo entero hasta el borde: la mano no
  flota. Es «tú, que llegas a elegir».
- **Luz de mañana** por una ventana grande a un lado; brillo real en las
  Pokébolas; sombras de las etiquetas sobre la madera.
- **Detrás**, desenfocado: estanterías de libros y, por la ventana, **el
  molino del laboratorio**.

### Concepto B — «La Pokédex en la Ruta 1»
**Objeto y sitio.** La **Pokédex roja de Kanto**, abierta y girada hacia
nosotros ([Kanto Pokédex de Alexander Walker](https://sketchfab.com/3d-models/kanto-pokedex-33558224badf4058b5977bded912c70c),
Blender). Sitio: **la Ruta 1**, a la salida de Pueblo Paleta, a media
mañana; hierba `#ADE65A`, cielo `#A5D6FF` ✅.

**Personaje.** **Ash** en plano medio sosteniendo la Pokédex hacia la
cámara, con el brazo entero visible. **Pikachu en su hombro** señalando la
pantalla con la pata. Ropa de Kanto (punto 16).

**Cómo habla.** Aquí **habla la Pokédex**: el texto va **en su pantalla**,
con la fórmula de una entrada («Pikachu, el Pokémon Ratón»). Debajo, una
caja de Game Boy pequeña para Ash. ⚠️ No comprobé si la Pokédex del
anime tiene una segunda pantalla: si el modelo 3D no la trae, esos textos
van en la parte de abajo de la misma pantalla.

**Dónde va cada texto**
| Texto | Dónde |
|---|---|
| **AUTOROLES, el canal Elección** | cabecera de la pantalla grande, en **Press Start 2P** |
| **Elige tus roles como eliges tu inicial** | primera línea de la «entrada» |
| **Reacciona abajo y elige tu color y tu país** | texto de la entrada, con una flecha ▼ al pie de la pantalla |
| **¿Qué haces? ¿Qué buscas? Eso va en Canales y roles** | segunda pantalla de la Pokédex |
| **Canales y roles está arriba del todo.** / **Lo cambias cuando quieras.** | segunda pantalla, debajo |
| **Aquí no se escribe** | tira de aviso en rojo al borde de la pantalla |
| **¿Algo no funciona? Abre un ticket en soporte** | segunda pantalla, última línea |
| Ash, en la caja de Game Boy | «ASH: ¡Yo ya elegí!» (18) / «¿Y tú?» + ▼ |

**Cómo no queda plano**
- **Hierba alta** en primer plano, desenfocada: la hierba donde salen los
  Pokémon salvajes.
- La **cola de Pikachu** cruza el encuadre por delante del hombro.
- Al fondo, pequeño, Pueblo Paleta y el molino. Sol alto, sombras cortas;
  la pantalla de la Pokédex brilla un poco sobre la mano.

### Concepto C — «El mapa a la luz de Charmander»
**Objeto y sitio.** Un **MAPA de PUEBLOS** de papel, como el que te dan en
Rojo/Azul («Usa el MAPA de PUEBLOS para saber dónde te encuentras» ✅),
pero dibujado con **los países del servidor** (Perú, México, Venezuela,
Colombia, Ecuador…), cada uno hecho
«pueblo» cuadrado y rutas entre ellos. Chinchetas de colores = **los
colores de rol**. En Blender: papel doblado y arrugado; la tinta sigue los
pliegues. Sitio: **el corral de Oak al anochecer** ✅, el mapa extendido
sobre un tocón o una piedra.

**Personaje.** **Charmander**, el más votado de la línea de iniciales ✅
(Charizard, 4.º mundial). Sentado junto al mapa, **levanta la cola para
iluminarlo** y señala un país con la garra. Su llama **arde fuerte y
alegre** (Pokédex ✅). Pikachu asoma por detrás del mapa.

**Cómo habla.** La **caja de Rojo Fuego/Verde Hoja**, la de Kanto en
color: fondo blanco y **letra azul porque habla un chico** ✅ (código del
juego). El diseño del marco de esa caja ⚠️ no lo comprobé: mirar una
captura de Rojo Fuego antes de dibujarlo. Habla Ash, desde fuera de
plano.

**Dónde va cada texto**
| Texto | Dónde |
|---|---|
| **Autoroles** | el título del mapa, en su cartela de esquina |
| **Elige tus roles como eliges tu inicial** | subtítulo de la cartela |
| **Reacciona abajo y elige tu color y tu país** | **la caja** de Rojo Fuego, y una **flecha ▼ dibujada** en el borde de abajo del mapa |
| **¿Qué haces? ¿Qué buscas? Eso va en Canales y roles** | la **leyenda** del mapa |
| **Canales y roles está arriba del todo.** / **Lo cambias cuando quieras.** | leyenda, debajo |
| **Aquí no se escribe** | nota clavada en la esquina con una chincheta |
| **¿Algo no funciona? Abre un ticket en soporte** | la última línea de la leyenda, junto a un icono de Centro Pokémon ⚠️ (icono no comprobado) |

**Cómo no queda plano**
- **La llama es la luz principal**: cálida y naranja sobre el mapa; todo lo
  demás, azul de noche. Contraste de color y sombras largas.
- **El borde del mapa se curva hacia la cámara** y queda desenfocado.
- Hierba del corral delante; al fondo, las ventanas encendidas del
  laboratorio.

### Lámina 2 (si el dueño pasa la lista de roles)
**«El PC del laboratorio»**: el ordenador que hay en el laboratorio ✅,
con el menú real del PC de Rojo/Azul: **SACAR PKMN / DEJAR PKMN** ✅
convertido en **PONERTE ROL / QUITARTE ROL**, y una lista con cursor ▶
como el menú «¿TU NOMBRE?» ✅. Cada rol, una fila con su emoji. Pantalla
dentro del monitor real, con reflejo de la ventana: no un panel suelto.

### ¿Cuál primero?
**A.** Es el objeto del plan, es la escena que todo fan reconoce, tiene la
broma de la Pokébola «con problema» y el ▼ que apunta a las reacciones.
C es la más bonita de luz. B es la más sencilla de montar.

---

## 20 · Lo que no pude verificar

- **Fotogramas**: no vi ni el capítulo 1 ni la película. Los minutos de la
  película salen de un **subtítulo no oficial**. Los del capítulo 1, **sin
  verificar**.
- **Hojas de contacto** y galerías de la wiki: sin red.
- **Licencias exactas de Sketchfab**: según el buscador; hay que abrir
  cada página.
- **Colores de Ash, de Oak y del rayo de la Pokébola**: sin medir.
- **Marco de la caja de Rojo Fuego**: sólo comprobé los colores de la
  letra.
- **Voz latina de la Pokédex** y de «¿Quién es ese Pokémon?»: no
  encontradas.
- **Óscar Roa** como cantante del opening: probable, no confirmado.
- **«Pokébola»**: una fuente clara (WikiDex).
- **Encuesta de popularidad latinoamericana**: no existe o no la encontré.
- **El país**: ¿reacción aquí o en Canales y roles? Lo decide el dueño.
- **La lista real de roles** (colores, países, talentos): no está en el
  inventario.

---

## Cumplimiento del encargo

_(pendiente)_

---

## 21 · Bitácora de búsqueda

### Comprobación de red (24-sep-2026)
- `community.fandom.com` → **000/403**. También 403: pokemon.fandom.com,
  Bulbapedia, Bulbagarden Archives, Doblaje Wiki, WikiDex, pokeapi.co,
  Game UI Database, Sketchfab, Google Fonts, pokemon.com, Arctic Shift,
  Azteca Jalisco (WebFetch).
- Responden: `api.github.com` (sólo repositorios concretos) y
  `raw.githubusercontent.com`. La búsqueda de código de GitHub, por el
  conector de GitHub.

### Búsquedas web (50 hechas; 1 rechazada)

**Español (17)**
1. Pokémon doblaje latino reparto Ash Pikachu Profesor Oak (en doblaje.fandom.com)
2. voz del Profesor Oak doblaje latino actor Pokémon
3. Pokémon primera temporada doblaje latino estudio director Audiomaster 3000
4. Profesor Oak voz latina primera temporada antes de Hugo Navarrete
5. Equipo Rocket voces doblaje latino Jessie James Meowth Diana Pérez Pepe Toño Macías
6. Pikachu voz Ikue Otani todos los idiomas doblaje latino
7. Ash Ketchum voz latina después de Gabriel Ramos, Diamante y Perla, Viajes
8. opening Pokémon latino «Atrápalos ya» cantante
9. Gabriel Ramos voz de Ash entrevista «¡Yo te elijo!»
10. Pokémon temporada 1 episodio 1 «¡Pokémon, yo te elijo!» latino laboratorio Oak Pokébola rayo
11. Pokédex anime Dexter voz latino Kanto
12. «¿Quién es ese Pokémon?» doblaje latino, «Pikachu impactrueno»
13. Discord «Canales y roles» incorporación elegir roles
14. «La película Pokémon: ¡Yo te elijo!» doblaje latino reparto
15. «¿Quién es ese Pokémon?» segmento anime latino silueta
16. Xóchitl Ugarte Misty, Gabriel Gama Brock
17. «Pokébola» doblaje latino contra «Poké Ball»

**Inglés (28)**
18. Pokémon of the Year 2020 poll results
19. most popular Pokémon starter poll Charizard
20. Pokémon episode 1 Oak lab three Poké Balls lightning bolt Pikachu
21. Professor Oak anime personality poet senryu
22. Pokémon Red Blue Oak's lab unused text (en tcrf.net)
23. Scarlet Violet / Sword Shield dialogue font name
24. Pokémon logo font «Pokemon Solid» license
25. Poké Ball 3D model CC Attribution (en sketchfab.com)
26. Kanto Pokédex / Professor Oak lab 3D model (en sketchfab.com)
27. laboratory HDRI, wooden table, white painted wood CC0 (en polyhaven.com y ambientcg.com)
28. Pallet Town / Oak Research Lab theme Junichi Masuda
29. anime composer Shinji Miyazaki
30. Ash Ketchum Kanto outfit colors
31. memes Professor Oak «Are you a boy or a girl»
32. FireRed LeafGreen Oak's lab interior
33. Ken Sugimori Professor Oak artwork Let's Go
34. Ash turns cap backwards
35. Ash's Pikachu personality, Atsuko Nishida
36. Professor Oak lab Poké Balls fan art (en pixiv.net, artstation.com, deviantart.com)
37. (rechazada) Reddit: episodio 1 del anime
38. Game Boy DMG 3D model CC (en sketchfab.com)
39. Let's Go dialogue box UI (en gameuidatabase.com, interfaceingame.com)
40. Pallet Town inspiration Machida
41. TV Tropes characters Professor Oak (en tvtropes.org)
42. key visual final season Ash Pikachu
43. Oak lab anime windmill corral
44. why Pikachu mascot instead of Clefairy
45. TikTok starter choice trend

**Japonés (4)**
46. ポケモン総選挙 結果 1位 ゲッコウガ
47. アニポケ 人気キャラクター ランキング 投票
48. オーキド博士 研究所 アニメ 第1話 モンスターボール 雷マーク
49. ポケモン アニメ 無印 キャラクターデザイン 一石小百合

**Coreano (1)**
50. 포켓몬 인기투표 결과 순위 피카츄 리자몽

**Chino**: no hice ninguna. Pokémon es japonés; prioricé japonés y coreano.

### GitHub (código y recursos, sin cupo)
- **[pret/pokered](https://github.com/pret/pokered)**: `text/OaksLab.asm`,
  `home/text.asm`, `data/text_boxes.asm`, `data/sgb/sgb_palettes.asm`,
  `gfx/font/font.png`, `gfx/font/font_extra.png`, `gfx/font.asm`,
  `gfx/trainers/prof.oak.png`, `gfx/player/red.png`,
  `gfx/pokemon/front/pikachu.png`, `data/maps/town_map_entries.asm`.
- **[pret/pokefirered](https://github.com/pret/pokefirered)**:
  `data/maps/PalletTown_ProfessorOaksLab/scripts.inc` y `text.inc`,
  `include/constants/vars.h`, `src/new_menu_helpers.c`.
- **[abcboy101/poke-corpus](https://github.com/abcboy101/poke-corpus)**:
  `corpus/RedBlue/es_msg.txt` y `corpus/Yellow/es_msg.txt` (texto oficial
  en español).
- **[PokeAPI/sprites](https://github.com/PokeAPI/sprites)**: arte oficial y
  HOME; medí tamaños y colores.
- **[PokeAPI/pokeapi](https://github.com/PokeAPI/pokeapi)**: CSV de nombres,
  categorías y textos de Pokédex en español; `versions.csv`.
- **[google/fonts](https://github.com/google/fonts)**: Press Start 2P,
  Lilita One, Luckiest Guy, M PLUS Rounded 1c, Barlow Semi Condensed.
- **[cooljeanius/pokemon-font](https://github.com/cooljeanius/pokemon-font)**:
  la letra y su LICENSE.md (OFL).
- **[tjklint/PokePC](https://github.com/tjklint/PokePC)**: el archivo de
  Pokémon Solid para comprobar sus glifos.
- **[imkira3/imkira3Keys](https://github.com/imkira3/imkira3Keys)**:
  subtítulos en inglés de la película 20, con tiempos.
- Mirado y descartado: [Greg-xh/GX](https://github.com/Greg-xh/GX)
  (`poke001.ass` es de la serie de 2019, no del capítulo de 1997).
- Búsquedas de código: `"Yo te elijo" Pikachu extension:srt` (0);
  `"Profesor Oak" Pikachu "Pueblo Paleta"` (97, de ahí poke-corpus);
  `"Pokemon Solid" @font-face ttf`; `NPC_TEXT_COLOR_MALE` en pokefirered;
  `TextBoxGraphics` en pokered; subtítulos con «Professor Oak» y «I choose
  you».

### Fuentes consultadas por tipo
- **Oficiales y primarias**: código de los juegos (pret), texto oficial en
  español (poke-corpus), PokéAPI, [pokemon2020.pokemon.com](https://pokemon2020.pokemon.com/en-us/),
  [pokemon.jp](https://www.pokemon.jp/info/event/detail/20160607_13811.html),
  [pokemon.co.jp](https://www.pokemon.co.jp/tv_movie/anime/pokemon.html),
  [pokemon.com](https://www.pokemon.com/us/pokemon-news/professor-oaks-pokemon-poetry-on-pokemon-tv),
  canal oficial de YouTube, Netflix México.
- **Staff**: Junichi Masuda, Ken Sugimori, Megumi Mizutani, Sayuri
  Ichiishi, Atsuko Nishida, Shinji Miyazaki, Satoshi Tajiri (sin entrevista
  directa abierta ⚠️).
- **Otros idiomas**: Famitsu, Oricon, Cinema Today, MANTANWEB, Nlab,
  Pokémon Wiki japonesa, Wikipedia japonesa, pixiv百科事典, Sakuga@wiki,
  Animate Times (japonés); Namuwiki, Ruliweb (coreano).
- **Wikis**: Pokémon Wiki (Fandom, español e inglés), Bulbapedia, WikiDex,
  Doblaje Wiki, Pallet Town Wiki, Nintendo Wiki, TV Tropes, The Cutting
  Room Floor, Wikipedia.
- **Prensa**: Newsweek, Digital Trends, Nintendo Life, Dexerto, Screen
  Rant, CBR, Den of Geek, Twinfinite, GoNintendo, TheGamer, Game Rant,
  Xataka, Infobae, El Universal, El Comercio, Trome, ANMTV, Código
  Espagueti, SuperGeek, Otaku Press, El Gráfico, Anime Argentina, PRODU,
  Gizmodo, 3DJuegos LATAM.
- **Foros**: [Bulbagarden](https://bulbagarden.net/threads/why-was-pikachu-chosen-as-the-anime-protagonist.138148/),
  [Serebii](https://forums.serebii.net/threads/how-did-pikachu-become-the-mascot.311679/).
- **Arte**: DeviantArt, pixiv, ArtStation, Creative Uncut.
- **Vídeo**: YouTube, TikTok, Netflix, Spotify.
- **3D y texturas**: Sketchfab, Poly Haven, ambientCG.
- **Interfaz**: Game UI Database, Interface In Game.
- **Letras**: Google Fonts, dafont, cdnfonts, Superpencil.
- **Discord**: [ayuda de incorporación](https://support.discord.com/hc/en-us/articles/11074987197975-Community-Onboarding-FAQ),
  [roles por reacción](https://streamlabs.com/es-es/content-hub/post/how-to-add-reaction-roles-to-discord).

### Lo que NO encontré
- Fondos de pantalla oficiales en alta, con tamaño.
- La voz latina de la Pokédex.
- Una encuesta de popularidad hecha en Latinoamérica.
- Entrevistas originales del staff sobre el laboratorio o el capítulo 1.
- Nada de Reddit: el buscador lo rechaza y Arctic Shift da 403.
- Búsquedas en chino: no hechas.
