# Parte de TEXTO, JUEGOS Y TÉCNICA · Kaguya-sama: Love is War (encargo 43)

Puntos de ENCARGO.md: **5** (tipografía), **6** (cómo hablan/piensan en pantalla), **11** (videojuegos), **18** (estilo de dibujo y cómo replicarlo), **24** (obras parecidas), **25** (mundo, historia y símbolos).
Parte de `datos-texto.md` (AniList: ficha, equipo creativo, obras parecidas y relacionadas) y de la wiki de Fandom `kaguyasama-wa-kokurasetai.fandom.com` (confirmada). No se repiten esas consultas.

## Hallazgos

### 5 · Tipografía

- **El logo oficial** かぐや様は告らせたい ～天才たちの恋愛頭脳戦～ es una tipografía gótica japonesa redondeada muy gruesa (trazo grueso y uniforme, esquinas ligeramente curvas), con dos acentos fijos: un **corazón rojo** que sustituye o decora el kanji 告 («confesar») y una **línea de pulso/cardiograma** (𝗅𝗎𝖻-𝖽𝗎𝖻) atravesando 恋愛頭脳戦 («guerra mental amorosa»). El color de relleno cambia por tomo/temporada (amarillo Vol.1, magenta Vol.2, negro con contorno blanco en el anuncio de anime) pero la forma de letra es siempre la misma. · Fuente: portadas oficiales miradas en grande — `chapter27.jpg` (tomo 1, JBE), `chapter21.jpg` (tomo 2), `anuncio1.jpg` (Chapter 110, Young Jump) y `anuncio2.jpg` (banner anuncio temporada 2) bajadas de `kaguyasama-wa-kokurasetai.fandom.com`. ✅ (el mismo diseño de logo se repite en 4 piezas oficiales distintas).
  - **Letra libre más parecida**: **M PLUS Rounded 1c** (Google Fonts/Fontsource, gótica redondeada japonesa con juego latino completo) en su peso Black/Bold — es la familia que más se acerca a un logo manga japonés redondo y grueso, y sirve igual para rotular en español. Comprobado con `fontTools` (`TTFont(f).getBestCmap()`, subset `latin` de Fontsource): trae **á é í ó ú ñ ¿ ¡ Á Ñ** ✅. `https://fontsource.org/fonts/m-plus-rounded-1c`.
- **Globo normal** (diálogo cotidiano del manga): óvalo blanco de contorno negro fino, sin cola marcada cuando el personaje está pegado al globo (se ve en `panel_rental.jpg` y `panel_confess.jpg`, capturas de las páginas de preview 176/177/180 de la wiki). La letra de la edición en inglés (VIZ) es un sans-serif de cómic limpio, todo en mayúsculas para gritos y mixed-case para diálogo normal.
  - **Letra libre**: **Patrick Hand** (Google Fonts/Fontsource) — mano de cómic legible y cercana, ni muy infantil ni muy seria. `á é í ó ú ñ ¿ ¡` ✅ comprobado con fontTools.
- **Grito**: en el mismo `panel_confess.jpg` (declaración de Kaguya y Chika) los globos de grito son ovalados con **picos triangulares cortos** en el borde (no el clásico globo dentado afilado de shonen de acción; es un grito «de comedia», más redondo). El anuncio de anime (`anuncio1.jpg`) usa mayúsculas gigantes con relleno amarillo/rosa y contorno negro grueso tipo cartel ("WE'RE GETTING AN ANIME!", "¡ITS HAPPENING!").
  - **Letra libre**: **Bangers** (Google Fonts/Fontsource) — bold cómic de trazo irregular, hecha para gritos y titulares de viñeta. `á é í ó ú ñ ¿ ¡` ✅.
- **Pensamiento**: la serie entera gira en torno al monólogo interno (ver punto 6), pero cuando es un pensamiento breve «de acotación» (no la narración completa) se dibuja con **letra cursiva manuscrita más pequeña**, a veces sin globo, flotando junto a la cara — visible en las hojas de contacto (p. ej. las notas manuscritas junto a los personajes en `hoja_02.jpg #66`, "Rental / CLOTHING", con letra distinta a la del diálogo).
  - **Letra libre**: **Caveat** (Google Fonts/Fontsource) — cursiva manuscrita suave, perfecta para la voz íntima de un pensamiento. `á é í ó ú ñ ¿ ¡` ✅.
- **Onomatopeya**: en el original japonés son katakana enormes dibujadas a mano (grito リーン, パン, etc., no confirmado un ejemplo propio en las hojas bajadas — búsqueda hecha, no lo encontré en las 75 imágenes de contacto). En la edición VIZ en inglés las onomatopeyas se traducen con letra de cómic gruesa y volumen falso (sombra duplicada). ⚠️ (una sola fuente visual, la edición inglesa, no el original japonés).
  - **Letra libre**: **Luckiest Guy** (Google Fonts/Fontsource) — cómic grueso con aire "3D" de sonido de impacto. `á é í ó ú ñ ¿ ¡` ✅.
- **Cartel del mundo** (carteles y pancartas dentro de la ficción: campaña del consejo estudiantil, festival, el letrero del colegio Shuchi'in): no se encontró una fuente oficial declarada; por el estilo geométrico y sobrio de la academia (uniformes negros, blasón elitista) conviene una letra de cartel limpia y con peso.
  - **Letra libre**: **Archivo Black** (Google Fonts/Fontsource) — geométrica, muy legible en grande, sirve para pancartas y rótulos del mundo escolar. `á é í ó ú ñ ¿ ¡` ✅.
- **Interfaz de videojuego** (menús/HUD de los juegos oficiales de la franquicia, ver punto 11: la app de la pachislot, la app de quiz, el navegador «GAME» de Young Jump): son interfaces de móvil/arcade modernas, con botones redondeados y letras sans limpias.
  - **Letra libre**: **Fredoka** (Google Fonts/Fontsource) — sans redondeada de interfaz, amistosa, usada mucho en apps y juegos casuales. `á é í ó ú ñ ¿ ¡` ✅.
- **Subtítulos o créditos** (la cartela real que usa el anime para el monólogo del Narrador en pantalla, ver punto 6): texto blanco en mayúscula/minúscula mixta, **muy grueso, con contorno negro duro** y esquinas redondeadas — se ve tal cual en `caption_ishigami.jpg` ("I want to die, so I'm going home.", cartela sobre fondo azul oscuro, episodio con Ishigami). Es el estilo estándar de subtítulo forzado japonés-occidental (blanco+contorno negro), no una fuente exclusiva de la serie. ✅ (mirado directamente en el fotograma oficial de la wiki).
  - **Letra libre**: **Anton** (Google Fonts/Fontsource) — condensada, muy gruesa, perfecta para aplicar relleno blanco + contorno negro y clonar esa cartela. `á é í ó ú ñ ¿ ¡` ✅.

Las 8 fuentes libres se comprobaron con `fontTools` sobre el `.ttf` del subset **`latin`** de la API de Fontsource (el subset `latin-ext` de Fontsource NO trae á/é/í/ó/ú/ñ/¿/¡ — son sólo los caracteres centroeuropeos adicionales; hay que pedir siempre `latin`, no `latin-ext`, para español). Script y `.ttf` de prueba en `/tmp/claude-0/trabajo/43-kaguya-sama-love-is-war-texto/fonts/`.

### 6 · Cómo hablan y piensan en pantalla

(pendiente)

### 11 · Videojuegos de la franquicia

(pendiente)

### 18 · Estilo de dibujo, técnica y cómo replicarlo

(pendiente)

### 24 · Obras parecidas y temas relacionados

(pendiente)

### 25 · El mundo, la historia y sus símbolos

(pendiente)

## Lo mejor para la lámina

(pendiente)

## No encontré

(pendiente)

## Bitácora

- Punto de partida: `partes/datos-texto.md` (AniList ficha, staff, obras parecidas/relacionadas; sección Steam vacía — recolectar.py no encontró juego en Steam).
- Wiki confirmada: `kaguyasama-wa-kokurasetai.fandom.com` (500+ páginas listadas por `allpages`, sin página dedicada a videojuego).
- Wikitext leído (action=parse&prop=wikitext): Shuchi'in Academy, Shuchi'in Academy Student Council, List of Organizations, Timeline, Crossovers.
- Hojas de contacto ya bajadas por `investigar_serie.py` (`herramientas/referencias/kaguya-sama-love-is-war/hoja_01.jpg`, `hoja_02.jpg`, 75 imágenes) miradas enteras (Read) para tipografía y cuadros de diálogo.
- Descargadas y miradas en grande: `I_probably_already_have_this_save.png` (anuncio de anime, Chapter 110 Young Jump), `Anime_Yu_Ishigami.jpg` (cartela "I want to die, so I'm going home."), `177_Preview.png` y `180_Preview.png` (páginas de manga con globos).

Sigue: 5 (tipografía: fuente libre para cada uso + fontTools), 6, 11, 18, 24, 25; Lo mejor para la lámina; No encontré.
