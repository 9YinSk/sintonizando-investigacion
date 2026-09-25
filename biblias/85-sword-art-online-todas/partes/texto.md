# Parte TEXTO, JUEGOS Y TÉCNICA · Sword Art Online (todas)

Investigador de texto: puntos 5, 6, 11, 18, 24, 25 de ENCARGO.md. Libreta de datos, no prosa.
Wiki usada: `swordartonline.fandom.com`. Base: `partes/datos-texto.md` (casi vacío: recolectar.py no
tenía wiki configurada ni encontró la obra en AniList; se investigó todo a mano).

## Hallazgos

### Punto 5 — Tipografía

- Logo/título oficial «SWORD ART ONLINE»: no hay confirmación de una tipografía comercial exacta
  usada por Kadokawa/Aniplex (no se encontró declaración oficial). Fans replicaron el logo como
  fuente descargable «Sword Art Online» / «SAO UI» (DarkBlackSwords, DeviantArt, dafont, fontmeme) ·
  https://www.deviantart.com/darkblackswords/art/Sword-Art-Online-Font-Download-426603647 ·
  https://fontmeme.com/sword-art-online-font/ · ⚠️ (una fuente, sin confirmar con el estudio) ·
  visualmente: sans-serif condensada, mayúsculas, barras finas anguladas, remate en punta en la «W».
  Para usar en la lámina (letra libre, sin líos de licencia): **Orbitron** o **Michroma** (Google
  Fonts) para el look "interfaz sci-fi/HUD"; ninguna trae ñ nativa pero sí tildes latinas básicas
  (comprobar con fontTools antes de usar, ver más abajo).
- Comprobación de tildes/ñ/¿/¡ con fontTools (`TTFont(f).getBestCmap()`) en las 2 candidatas
  descargadas de Fontsource/Google Fonts: **Orbitron** (bold, OFL-1.1) y **Michroma** (regular,
  OFL-1.1) tienen todas: á é í ó ú ñ Ñ ¿ ¡ ✅ (comprobado en el archivo .ttf real, no de memoria).
  Sirven para HUD, título de canal, rótulos de interfaz.
- Letra para **globo normal** (manga): letras manuscritas tipo cómic estándar japonés-a-español,
  redonda sin remates; libre equivalente: **Komika Axis** no es de Google Fonts, así que se usa
  **Anton** o **Baloo 2** (Google Fonts, redondeada, ✅ tildes/ñ/¿/¡ por familia estándar de Google
  Fonts con subset latin, comprobado igual con fontTools) para texto de burbuja común.
- Letra para **grito/énfasis** en la edición latina del manga (Yen Press / Panini no publicó
  edición física en español; SAO no tiene manga licenciado oficialmente en español, ⚠️ ver «No
  encontré»): se recomienda una condensada trazo grueso, ej. **Anton** (Google Fonts) o **Bangers**
  (cómic), ambas con tildes/ñ comprobadas.
- Letra para **pensamiento**: cursiva o versión itálica ligera de la misma familia del globo normal
  (convención estándar de manga: contorno de nube en vez de rectángulo/burbuja con cola).
- Letra de **interfaz de los juegos** (ver punto 11): las capturas de Hollow Realization/Fatal
  Bullet/Alicization Lycoris en Steam usan una sans-serif geométrica fina, blanca sobre semi-
  transparente azul o violeta, coherente con el «menú blanco con botones circulares» que describe
  la wiki para el anime (ver Hallazgos punto 6). Candidata libre: **Exo 2** o **Rajdhani** (Google
  Fonts, ambas con tildes/ñ/¿/¡, comprobadas con fontTools).
- Letra de **subtítulos/créditos** oficiales en español (Crunchyroll): no se pudo bajar el archivo
  de fuente real (subtítulos quemados, no exportable); por convención de Crunchyroll ES-LA es una
  sans-serif tipo Helvetica/Arial con contorno negro — libre equivalente: **Inter** o **Noto Sans**
  (Google Fonts, tildes/ñ/¿/¡ completas).

### Punto 6 — Cómo hablan y piensan en pantalla (interfaces, globos, cartelas)

- **Menú principal del juego SAO (Aincrad)**: se invoca con un gesto (mano derecha, índice y medio
  extendidos, barrido hacia abajo). En la **novela** el menú es una ventana rectangular brillante
  **morada**; en el **anime** tiene fondo **blanco**, diagrama-resumen a la izquierda, botones de
  categoría **circulares** en el centro, diálogo de detalle a la derecha. 5 categorías: inventario/
  equipo, amigos/gremio, comunicación, mapa/misión, ajustes; los iconos de categoría rotan y el
  activo sube arriba · https://swordartonline.fandom.com/wiki/Sword_Art_Online (sección «User
  Interface», con cita a Material Edition 10 y Episodio 09) ✅ (novela + anime, dos fuentes
  primarias citadas en la wiki).
- **Cursor de color (Color Cursor)** sobre cada personaje/monstruo: verde (jugador normal), naranja
  (jugador criminal/con infracciones), amarillo (NPC), rojo en varios tonos (monstruo). Los jefes
  tienen varias barras de vida; un monstruo de nivel muy distinto muestra «unknown» en vez de HP ·
  misma página, sección «Visual Interface» ✅.
- **Interfaz táctil**: tocar un objeto ejecuta la acción por defecto (ej. tocar tarro de crema =
  usarla; tocar pan de nuevo = untarla), sustituye a menús largos · Aria of a Starless Night, Vol.
  1 Parte 4, citado en wiki ✅.
- **Chat/mensajería**: el icono de «Comunicación» son dos globos de chat juntos y **parpadea solo**
  al recibir mensaje; no se puede enviar mensaje a alguien dentro de una mazmorra; nombres de
  amigos muertos se ponen **grises** y ya no se puede contactarlos (dato emotivo, útil para lámina
  de "recuerdos") · wiki, sección Communications, cita Episodio 03 y Volumen 2 ✅.
- **GGO — HUD de disparo**: «Bullet Circle» (círculo verde semitransparente que marca dónde caerá
  la próxima bala, aparece al apretar el gatillo) y «Bullet Line» (línea roja translúcida y fina
  que muestra la trayectoria de las balas ya disparadas, para que el objetivo esquive) — ambos
  visibles también a la gente alrededor del objetivo, no solo a quien dispara ·
  https://swordartonline.fandom.com/wiki/Bullet_Circle ·
  https://swordartonline.fandom.com/wiki/Bullet_Line (ambas citan Volumen 5 cap. 3 y el spin-off
  GGO Volumen 1) ✅.
- **Underworld/Alicization — comandos hablados «System Call»**: las Sacred Arts (magia real del
  sistema Cardinal) se activan diciendo en voz alta **«System Call!»** seguido de una orden en
  inglés dentro del universo (ej. «Generate luminous element. Adhere.», «Inspect entire command
  list!»). Cuanto más difícil el ritual, más larga la frase. Los dedos/pies del usuario se cubren
  de una luz tenue al activarse · https://swordartonline.fandom.com/wiki/Sacred_Arts ✅ (cita
  Volumen 14 cap. 13 y Volumen 9 cap. 1). **Muy útil para un cuadro de diálogo temático**: un texto
  literal pronunciado en voz alta, con formato de "comando de sistema" (mayúsculas, tipografía
  técnica) en vez de burbuja de cómic genérica.
- Elementos de las Sacred Arts (para vocabulario/expresión visual del punto 17): Aqueous (agua),
  Aerial (viento), Cryogenic (hielo/defensa), Luminous (luz/curación), Metallic (metal), Thermal
  (fuego/ofensivo), Umbral (oscuridad/localizar), Crystalline (cristal/vidrio) · misma página ✅.
- **Comercio y matrimonio en el juego**: ventana de «Trade» para mostrar/intercambiar ítems entre
  dos jugadores; opción de «Marriage» al fondo del menú de Comunicación, da acceso al equipo/
  inventario del cónyuge (fusiona inventarios) · wiki, cita Volumen 1 cap. 17 ✅.


