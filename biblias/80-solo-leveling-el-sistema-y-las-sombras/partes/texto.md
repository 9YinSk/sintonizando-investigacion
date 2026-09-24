# Parte de TEXTO, JUEGOS Y TÉCNICA · Solo Leveling: el Sistema y las sombras

Investigador de texto (puntos 5, 6, 11, 18, 24, 25 de `ENCARGO.md`). Libreta de datos, no prosa.
Parte de `partes/datos-texto.md` (AniList: títulos, staff, obras relacionadas) y no repite esas consultas.
Ojo: esta serie ya tiene una biblia de repaso general en `biblias/03-solo-leveling/` — la cito como
referencia cruzada cuando ayuda, pero la investigación de abajo es propia (imágenes bajadas y medidas por mí,
fuentes propias). Enfoque de este encargo: **el Sistema y las sombras**.

## Hallazgos

### Punto 6 · Cuadros de diálogo (peso especial: la ventana del Sistema)

**Qué es la ventana, con fuente propia de la wiki** ✅ ([System, solo-leveling.fandom.com](https://solo-leveling.fandom.com/wiki/System), wikitext leído por API):
- Es un «programa mágico» que elige a Jinwoo como su único **Jugador**; nadie más puede verlo. Detrás hay un
  **Moderador** llamado **Kandiaru** y, al final, el propio Jinwoo la modifica y se la pasa a su hijo **Sung Suho**.
- Su primera frase, citada en la propia ficha de la wiki: «*Congratulations on becoming a Player.*» (El Sistema a
  Jinwoo, ep. 3 del anime).

**Medido por mí en `Anime_System.png`** (815×483, capturada del anime, wiki oficial) ✅ — la pantalla de ESTADO en
nivel 100:
- Marco exterior: filigrana de **circuito violeta-magenta neón**. Medido con Pillow (pixel más saturado de la
  franja): **`#D259FF`** (violeta-magenta brillante). El fondo general del cuadro es casi negro con un tinte azul
  muy oscuro, `#0E152E`.
- Panel interior: rectángulo **oscuro azul-violáceo translúcido**, medido en el centro del panel: **`#1B2337`**.
- Título «STATUS» dentro de su propio recuadro rectangular, en mayúsculas, palo seco geométrico bien espaciado.
- «100 / LEVEL»: el número gigante en un palo seco grueso y limpio (no angular tipo ciencia-ficción dura); debajo,
  «LEVEL» pequeño.
- «JOB: Shadow Monarch» / «TITLE: The One Who Overcame Adversity»: etiqueta en mayúsculas pequeñas + valor en
  blanco.
- Barras de HP y MP con icono a la izquierda (cruz y gota) y el valor numérico dentro de la barra.
- Grid de atributos (STR, AGI, PER a la izquierda; VIT, INT a la derecha), cada uno con icono, valor en blanco y el
  bono entre paréntesis **en verde**: medido, **`#2BE36A`**.
- Texto y filetes finos: blanco-azulado, medido **`#D2E7FF`**.
- **Coincide con lo ya documentado** en la guía `_ya_hechas/_Cuadros de dialogo por franquicia` y en
  `biblias/03-solo-leveling/biblia.md` §4.2 (que da `#211B32`/`#9229F9`/`#ED77F3` en otra captura): mismos tonos,
  mi muestra concreta da `#1B2337`/`#D259FF`. Dos capturas, mismo diseño ✅. La diferencia de matiz es normal por
  compresión y opacidad de la captura.

**El texto SÍ tiene un cuadro con cola: el de Jinwoo hablando** (hallazgo propio, no estaba en la guía de
franquicias) ✅ — visto en `Shop.jpg` (webtoon oficial, 718×630, wiki):
- Cuando **Jinwoo** le habla al Sistema en voz alta («Shop.», para abrir la tienda), su frase va en un **globo
  ovalado blanco clásico de manhwa, con borde negro fino y una cola hacia su boca** — el globo normal de cómic, no
  uno especial. **El Sistema es el que no tiene globo** (aparece como panel/ventana flotante); el personaje que le
  contesta en voz alta sí usa el globo de siempre.
- Al fondo, el panel del Sistema aparece como un **rectángulo azul translúcido con líneas verticales de
  interferencia (efecto de pantalla encendiéndose)**, medido: **`#4C8CFD`** (azul, no violeta: es un capítulo
  temprano — confirma lo que decía la guía de franquicias: «la primera ventana de la serie es azul», el violeta es
  de la fase «Monarca» posterior).
- La onomatopeya **«DING»** (el sonido de la ventana al aparecer) va en letras gruesas redondeadas con **contorno
  y resplandor azul cian**, medido `#3B84BD`, sin globo, flotando junto al personaje — es la onomatopeya «del
  Sistema», distinta de las onomatopeyas de combate.

**Formato del texto dentro de la ventana** ✅ (confirmado en la ficha de la wiki y en `biblias/03-solo-leveling`):
- Los mensajes van **entre corchetes** `[ ... ]`: p. ej. *"[Urgent Quest: Defeat the Enemies.]"*, *"[Knight
  Killer]"*. Es la marca tipográfica más reconocible de la serie: cualquier nombre de objeto, misión o rango que
  cita el Sistema va entre corchetes.
- Encabezados en MAYÚSCULAS dentro de su propio recuadro (STATUS, NOTIFICATION, QUEST INFO, STORE).
- Las amenazas o penalizaciones van resaltadas en un tono cálido de alerta (rojo/carmesí), el resto en blanco/cian.

**Para la lámina, el cuadro del Sistema en una línea:** rectángulo de esquinas rectas (sin redondear, sin cola),
relleno azul-violáceo oscuro translúcido `#1B2337`-`#211B32`, doble filete claro, marco de circuito neón violeta
`#9229F9`/`#D259FF` (o azul `#4C8CFD` si es una ventana «de novato», temporada 1 temprana), cabecera en recuadro
propio y MAYÚSCULAS, cuerpo blanco-cian, corchetes para nombres de objeto/misión, verde para bonos, rojo/carmesí
sólo para advertencias. Nunca un globo con cola: el Sistema no «sale» de nadie. Si el personaje habla en voz alta
（p. ej. para dar una orden como «Surge»/«Shop»), **eso sí** va en globo blanco normal con cola.

**Otro cuadro de la serie, distinto del Sistema:** el aviso del **móvil de Jinwoo** / la Asociación de Cazadores —
tarjeta blanca de app de oficina, no la ventana de juego (documentado en `biblias/03-solo-leveling` §4.2, ep. 8;
no lo repito con imagen propia por ahorrar, referencia cruzada ✅).

### Punto 5 · Tipografía

**Letras candidatas específicas para la interfaz del Sistema**, elegidas por mí a partir de lo que vi en
`Anime_System.png` y comprobadas con `fontTools` sobre el `.ttf` real (no de memoria), bajadas de Fontsource
(`api.fontsource.org`) ✅:

| Letra | De dónde | ¿á é í ó ú ñ Ñ ¿ ¡ ü? | Para qué encaja |
|---|---|---|---|
| **Exo 2** (Bold) | Google Fonts / Fontsource, SIL OFL | **sí, las 9** (comprobado) | La más cercana al «STATUS» y al «100» del panel medido: geométrica, redondeada en las curvas, nada angular. Recomendada para cabeceras y el número de nivel. |
| **Rajdhani** (Bold) | Google Fonts / Fontsource, SIL OFL | **sí, las 9** | Alternativa cuadrada/condensada para etiquetas cortas (JOB, TITLE, STR, AGI). Coincide con lo que ya proponía `biblias/03-solo-leveling` para las cifras. |
| **Orbitron** (Bold) | Google Fonts / Fontsource, SIL OFL | **sí, las 9** | Más angular y «ciencia-ficción dura»: sirve para la variante violeta «Monarca» (T2), no para la ventana azul de novato, que es más limpia. |
| **Audiowide** | Google Fonts / Fontsource, SIL OFL | **sí, las 9** | Ancha y redondeada; candidata para un logo o título corto tipo «SISTEMA», no para párrafos. |
| **Electrolize** | Google Fonts / Fontsource, SIL OFL | **sí, las 9** | Fina y técnica; sirve para etiquetas pequeñas tipo interfaz (HP, MP, botones CANCELAR/ACEPTAR). |

Comprobación hecha con `fontTools.ttLib.TTFont(...).getBestCmap()` buscando los códigos de á é í ó ú ñ Ñ ¿ ¡ ü en
cada `.ttf` bajado de `https://cdn.jsdelivr.net/fontsource/fonts/<familia>@latest/latin-700-normal.ttf`: **las 5
traen los 9 signos**, ninguna falla. Hice además una plancha comparativa (`fuentes/specimen.png`, mirada por mí)
con el texto «STATUS 100 Nv. ñÑ¿¡áéíóú» en cada una: **Exo 2 y Rajdhani son las que más se parecen** al peso y
proporción del «STATUS»/«100» reales del panel.

Esto **complementa** (no repite) la tabla ya construida en `biblias/03-solo-leveling/biblia.md` §5, que cubre el
logo del anime, el logo del juego ARISE, los rótulos de tráiler y el ending — para esos usos, remito a esa tabla
en vez de rehacer la misma investigación (ya está con `fontTools` y ✅ doble fuente).

### Punto 11 · Videojuegos: interfaz y cuadros de diálogo (con capturas propias)

**Solo Leveling: ARISE OVERDRIVE** (Netmarble Neo; PC/Steam, app 2373990) — descargué y miré las **8 capturas
oficiales de Steam** (1920×1080, `store.steampowered.com/api/appdetails?appids=2373990`) en una hoja de contacto
propia ✅:

- **Pantalla RESULT** (fin de combate), mirada en detalle (recorte propio a partir de la captura oficial):
  - Título **«RESULT»**: palo seco condensado en cursiva/inclinado, blanco con degradado gris-azulado, look
    deportivo/dinámico. Subtítulo «A New Start» en blanco, más pequeño y espaciado.
  - Panel: rectángulo de cristal **translúcido azul-marino oscuro** (deja ver el fondo del escenario detrás,
    efecto vidrio esmerilado) con **filete fino azul claro**. Nada de esquinas redondeadas vistosas: es frío,
    como pide el dueño para una interfaz de «ventana de juego».
  - Insignia de rango: **rombo** con el texto «Rank» arriba y la nota **«SSS»** enorme, en palo seco grueso
    itálico, **rojo-naranja** con sombra oscura — la letra de rango más alta, eco directo del sistema de rangos
    E-S de los cazadores (punto 25).
  - «Difficulty Bonus 1000» arriba a la derecha con icono circular.
  - Filas de estadística: barra gris redondeada, etiqueta a la izquierda, cifra en blanco alineada a la derecha
    («Action Points 13200», «Survival Points 3600», «Bonus Points 580»); la fila TOTAL se resalta con **»** y el
    número en **dorado/ámbar**.
  - Menú inferior sin caja, sólo texto blanco: «Rewards Details» / «Close» — pensado para mando (navegación por
    consola).
  - Panel «Rewards»: mismo estilo de cristal translúcido con esquina cortada en diagonal (no recta): tres
    casillas de recompensa (piedra violeta ×1, insignia «EXP» azul con brillo ×750, moneda dorada ×1900) e icono
    de botón de mando «R3» abajo a la derecha.
  - Esto **actualiza** lo que decía `biblias/03-solo-leveling` §15 («no pude medir menús ni cajas del juego»):
    **sí se puede**, con las capturas oficiales de Steam en vez de Game UI Database.
- Las otras 7 capturas son de acción/cinemática (el vestíbulo del gremio con el emblema dorado en la fachada, un
  combate contra un titán rojo, un cara a cara entre tres cazadoras con relámpagos violeta) — sirven más para el
  punto 16 (fondos) que para diálogo; las dejo anotadas en `texto.json` por si la imagen sirve de referencia de
  pose o de sitio.
- **Fecha de Steam**: apareció el 24-nov-2025 en PC/Xbox (dato ya en `biblias/03-solo-leveling`, no repetido aquí).

**Game UI Database y The Cutting Room Floor**: los volví a intentar con la red abierta — **los dos dan 403 /
reto de Cloudflare** («Just a moment...», `cf-mitigated: challenge`) igual que en el repaso general. No insistí
una tercera vez (regla de AYUDANTE.md de no gastar más de dos intentos). ⚠️ Sin acceso.

**Solo Leveling: ARISE** (móvil, Netmarble) — la Play Store con `hl=en` devolvió «Not Found» con el id de paquete
que probé (`com.netmarble.slarise`); no insistí en buscar el id correcto para no gastar más cuota. Lo que ya
recoge `biblias/03-solo-leveling` §15 (viñetas de webtoon animadas como cuerpo del relato, con escenas 3D) sigue
siendo la mejor fuente sobre su interfaz. ⚠️ Sin capturas propias de ARISE (sí de ARISE OVERDRIVE).

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

> Referencia cruzada: `biblias/03-solo-leveling/biblia.md` (Punto 18) ya documenta a fondo quién lo hizo
> (Nakashige, A-1 Pictures; DUBU/Jang Sung-rak en el webtoon), la cita del director sobre evitar «expresiones de
> dibujo animado», la mezcla 2D/3D (mocopi de Sony) y cómo replicarlo en Photoshop/Blender. No repito esa
> investigación (mismas fuentes que yo habría usado: VFX Voice, Anime Corner, Sony XYN). Lo que añado aquí es lo
> propio de **mi enfoque** (Sistema y sombras):

- **Las ventanas del Sistema son *motion graphics* aparte del dibujo del personaje**: según la propia guía de
  franquicias del repositorio y `03-solo-leveling`, las hace el equipo de gráficos de Production I.G (Takemune
  Ōshiro), no A-1 Pictures directamente. Para replicarlo en Photoshop/After Effects: es una **capa 2D compuesta
  encima del render**, con su propio brillo (Sobreexponer/Trama) y sin sombreado 3D — por eso se puede recortar y
  animar aparte de la escena, útil para el dueño si quiere una ventana del Sistema como elemento flotante sobre un
  fondo Blender.
- **Las sombras (soldados) sí llevan sombreado del anime** (luz de borde de color, casi sin línea negra — ya
  medido en `03-solo-leveling` sobre un fotograma de Igris): mismo tratamiento que Jinwoo, no un estilo aparte.
  Para Blender: el modelo de sombra puede compartir el mismo *shader* de dos-tres bandas que el personaje, sólo
  cambiando el tono de la luz de borde (violeta/rosa oscuro para Igris, ámbar oscuro para Beru — colores por
  confirmar con arte, tarea del rol de imagen).
- **Textura y contorno de la ventana**, distinto del contorno del personaje: nada de tinta; es **luz + circuito
  vectorial**, así que en Blender no se replica con Line Art/Freestyle sino con **geometría plana (planos con
  textura emissive)** o compuesto 2D encima del render, tal como recomienda ya `03-solo-leveling` para la luz de
  borde del personaje.

### Punto 24 · Obras parecidas

> Referencia cruzada: `biblias/03-solo-leveling/biblia.md` (Punto 24) ya cubre AniList (Tower of God, Eminence in
> Shadow, God of High School…), la prensa (MovieWeb, Dexerto, ScreenRant) y las declaraciones de Chugong sobre
> Diablo/Skyrim/WoW. Mismos datos que yo habría sacado de `datos-texto.md` (AniList) — no los repito. Añado lo que
> falta desde **mi ángulo** (interfaz de Sistema / progresión de niveles como género):

- **TV Tropes**: la página `Solo Leveling` en TV Tropes existe y clasifica la obra dentro de **"LevelUpFantasy"** y
  **"GameificationAnime"** (el subgénero exacto de «la vida como videojuego», con ventanas de estado, misiones,
  subida de nivel) ✅ (comprobado por búsqueda en el sitio: `https://tvtropes.org/pmwiki/pmwiki.php/Anime/SoloLeveling`
  responde 200 y lista tropos como *StatusLine*, *LevelUpFillUp*, *RPGMechanicsVerse*). No abrí la lista completa
  de tropos por ahorrar cuota; el dato útil para la lámina es el **nombre del subgénero**: sirve para explicar en
  un texto del bot qué tipo de fantasía es (útil para el hilo «De qué va esto»).
- **El gancho concreto que comparte con sus «primos» es la ventana de estado**: *Tower of God*, *The Eminence in
  Shadow* y *God of High School* (ya en `03-solo-leveling`) tienen la misma raíz de «RPG hecho carne», pero
  **Solo Leveling es el que más se apoya en la ventana de notificación como recurso visual constante** (aparece
  en casi cada episodio), más que en Tower of God (que usa más el mundo físico de la Torre) — esto es lectura
  propia a partir de haber visto las capturas y no debe tomarse como ✅ sin comprobarlo viendo los otros animes;
  queda como ⚠️ (comparación, no dato verificado en las otras series).

### Punto 25 · El mundo, la historia y sus símbolos (peso especial: rangos de cazadores, mazmorras y jerarquía de sombras)

**Rangos de cazadores** ✅ ([Class Ranks, wiki](https://solo-leveling.fandom.com/wiki/Class_Ranks), wikitext leído
por API):
- Sistema internacional de rangos **E → D → C → B → A → S** para clasificar a las personas con maná, y también
  las **mazmorras** y los **monstruos** (mismo rango sirve para los tres).
- El rango se fija en el momento del «despertar» y **es de por vida**: la única forma de subir es un «segundo
  despertar», rarísimo. **Jinwoo es la única excepción conocida** porque el Sistema le permite entrenar sin techo.
- La diferencia de poder entre rangos es enorme: un B-Rank supera fácil a un C-Rank; un S-Rank es
  «exponencialmente» más fuerte que un A-Rank (cita textual de la wiki).
- El rango determina el sueldo y el estatus: los E-Rank se consideran «desechables» y cobran poco (aún así, más
  que la mayoría de profesiones); los S-Rank «nadan en dinero».
- Existen los **«False Rankers»**: cazadores que ocultan su verdadera fuerza controlando su maná a propósito;
  suelen tener motivos siniestros.

**Mazmorras** ✅ ([Dungeon, wiki](https://solo-leveling.fandom.com/wiki/Dungeon), wikitext leído por API):
- Son «bolsillos» de un mundo del caos conectados al mundo humano por **portales (Gates)**, que aparecen al azar.
- Tienen un jefe; al matarlo, la mazmorra sigue abierta **una hora** antes de cerrarse sola.
- Si no se limpia en **7 días**, ocurre una **«Dungeon Break»**: los monstruos salen al mundo humano. En la línea
  temporal revisada, un portal así abandonado puede infectar la zona de maná y volverla inhabitable (**«Field-Type
  Dungeon»**).
- Son la fuente de ingresos de los cazadores: sueltan objetos y **Cristales de Maná**.
- **Tipos de mazmorra** (lista textual de la wiki):
  - **Low-Rank** (E/D): monstruos débiles, botín pobre.
  - **High-Rank** (A/S): requieren cazadores fuertes.
  - **Red Gates**: rarísimas y letales — el cazador queda **teletransportado dentro, sin poder salir** hasta
    limpiarla o morir (el arco del ep. 13-14 del anime es justo esto).
  - **Instance Dungeons**: únicas de Jinwoo, parte del Sistema — no son portales normales, son misiones o
    entrenamientos que el propio Sistema le genera.
- **Mazmorras notables por rango**, listadas en la wiki: S (Double Dungeon/Cartenon Temple, Demon Castle, Pyramid
  Dungeon), A (Red Gate Incident, Hunters Guild Dungeon, Busan A-Rank Dungeon), C (Insects, Goblins), D (Gwanak
  Mountain), E (Hapjeong Subway Station).

**Gremios** ✅ ([Guilds, wiki](https://solo-leveling.fandom.com/wiki/Guilds), wikitext leído por API):
- Son grupos organizados de cazadores dedicados a limpiar portales; el jefe es el **Guild Master** (casi siempre
  S-Rank en los gremios de élite).
- Los gremios grandes dan más seguridad y sueldo; los pequeños reclutan cazadores de cualquier rango para
  mazmorras por encima de su nivel → más muertes, mal vistos.
- Ejemplo económico real de la wiki: Jinwoo, como cazador independiente, pagó 40 % de impuesto al vender 49
  piedras esencia de rango C y ganó 135 000 $; en un gremio, el impuesto baja a 10 % y habría ganado ≈200 000 $.

**Jerarquía de las sombras (soldados)** ✅ ([Shadows, wiki](https://solo-leveling.fandom.com/wiki/Shadows),
wikitext leído por API) — **siete grados, de menor a mayor**, con su fuente textual exacta (la wiki distingue el
nombre de la novela `{{NV}}` del nombre del webtoon `{{WB}}` cuando difieren):
1. **Normal Grade**: el más bajo; soldados de infantería; fuerza comparable a cazadores E, D o C.
2. **Elite Grade**: el grado más común en el ejército; fuerza de B-Rank.
3. **Knight Grade**: fuerza de A-Rank; **desde aquí el Monarca de las Sombras puede darles nombre propio**.
4. **Elite Knight Grade**: fuerza de S-Rank básico (el ejemplo que da la wiki: Baek Yoonho).
5. **Commander/General Grade**: poder inmenso, capaz de plantar cara a S-Ranks avanzados; **desde aquí pueden
   hablar**.
6. **Marshal/Commander Grade**: el grado más alto al que puede *evolucionar* una sombra normalmente.
7. **Grand Marshal Grade**: el grado supremo, reservado para **la sombra más fuerte de todo el ejército**, que
   además actúa como **lugarteniente del Monarca de las Sombras**.
- Sólo desde **General** para arriba pueden hablar, y sólo en «lengua de monstruo» (la mayoría de humanos no la
  entiende); **Beru** la esquiva porque devoró cazadores japoneses y absorbió sus idiomas junto con sus
  habilidades (dato curioso para una ficha de personaje).
- Poderes compartidos por toda sombra, listados en la wiki: Regeneración, Conversación (sólo General+),
  Crecimiento (pueden subir de grado matando en batalla, pero **ascender de grado requiere autorización directa
  del Monarca**), Infiltración en sombra (se ocultan en la sombra de otra persona y vigilan/avisan a distancia),
  Transformación (en arma u objeto — Suho la domina más rápido que su padre), Aguante infinito, Inmortalidad.
  - **Corrección/matiz** frente a lo dicho en `biblias/03-solo-leveling` §6/§20 (que resume la jerarquía en 6
    pasos «Normal → Élite → Caballero → Caballero de élite → General → Mariscal»): la wiki en inglés distingue
    **siete** grados, con **Grand Marshal** como el escalón por encima de Marshal (el puesto único del
    lugarteniente del Monarca) — útil precisar esto si la lámina habla de rangos de sombra.
- Shadow Authority (página aparte, `Shadow_Authority`, leída por API): es el nombre de la **habilidad/autoridad**
  del Monarca de las Sombras sobre la muerte, la que le permite extraer y controlar sombras — no es lo mismo que
  el «grado» de una sombra concreta.

**Vocabulario del mundo** (complementa, sin repetir, el que ya reúne `biblias/03-solo-leveling` §25 con fuente en
los subtítulos latinos de Crunchyroll): *Gate* (portal), *Dungeon* (mazmorra), *Dungeon Break*, *Field-Type
Dungeon*, *Red Gate*, *Instance Dungeon*, *Essence Stone* / *Mana Crystal*, *Guild Master*, *False Ranker*,
*Shadow Authority*, los **siete grados de sombra** de arriba.

## Lo mejor para la lámina

1. **El cuadro del Sistema**: panel oscuro translúcido (`#1B2337`) con marco de circuito neón violeta (`#D259FF`)
   o azul (`#4C8CFD` si es una escena temprana/novato), corchetes para nombres de objeto o misión, verde para
   bonos, MAYÚSCULAS en recuadro propio para el título. Nunca cola de globo.
2. **El globo SÍ existe, pero es de Jinwoo, no del Sistema**: cuando él le contesta en voz alta («Shop.», «Surge»),
   usa el globo blanco normal con cola — así se puede combinar un globo clásico con una ventana de juego en la
   misma viñeta sin que choquen.
3. **Fuentes libres recomendadas**: Exo 2 o Rajdhani (Bold) para el cuerpo de la ventana; Orbitron para la
   variante «Monarca»; las 5 candidatas comprobadas con tildes/ñ/¿/¡ completas.
4. **La pantalla RESULT de ARISE OVERDRIVE** (rombo con el rango en letras gigantes rojo-naranja) es la prueba
   visual de que el sistema de rangos E→S también se usa como marcador de logro en el videojuego — sirve de
   referencia si la lámina necesita un «marcador» o insignia.
5. **Los siete grados de sombra** (Normal → Elite → Knight → Elite Knight → General → Marshal → Grand Marshal) dan
   una escalera perfecta para una lámina de jerarquía tipo organigrama, con Igris (Marshal, antes «Comandante»
   según la novela) y Beru (Grand Marshal / Rey Hormiga) como referencia.

## No encontré

- ⚠️ **Game UI Database y The Cutting Room Floor**: los dos siguen bloqueados por el reto de Cloudflare
  (`cf-mitigated: challenge`, HTTP 403) con la red abierta; probé una vez cada uno (regla de no más de dos
  intentos). No hay menús medidos de ahí; los sustituí por capturas oficiales de Steam para ARISE OVERDRIVE.
- ⚠️ **Capturas propias de la interfaz de Solo Leveling: ARISE (móvil)**: no encontré el id correcto de paquete en
  Google Play desde este servidor (la URL que probé dio «Not Found») y no insistí para no gastar cuota; la
  descripción de su interfaz se apoya en lo ya verificado por `biblias/03-solo-leveling` (viñetas de webtoon
  animadas).
- ⚠️ **Letra oficial real de la ventana del Sistema** (el archivo tipográfico que usó Production I.G): ninguna
  fuente oficial la nombra (ni VFX Voice ni AniList); sólo hay citas de fans sin verificar (Trueno Round, Circe
  Rounded, Caros Soft — ya recogidas en `03-solo-leveling` y en la guía de franquicias, con ⚠️ propio). Lo que sí
  comprobé por mi cuenta son las 5 alternativas libres de esta parte, con sus glifos.
- La comparación de «cuánto pesa la ventana del Sistema frente a otras series del género» (punto 24) es lectura
  propia a partir de las capturas vistas, no un dato con fuente que lo diga explícitamente — lo dejé marcado ⚠️
  en el hallazgo.

## Bitácora de búsqueda

- **Fandom (API, `action=parse&prop=wikitext`)**, en inglés: `System`, `Class_Ranks`, `Dungeon`, `Dungeons`,
  `Shadows`, `Shadow_Authority`, `Guilds`, `Ahjin_Guild` — todas devolvieron wikitext completo salvo
  `Shadow_Soldiers` (no existe con ese título; el contenido real está en `Shadows`).
- **Fandom (`action=query&list=search`)**: `dungeon`, `shadow army`, `guild`, `gate rank`, `intitle:notification`,
  `intitle:status` (namespace File) — para localizar nombres exactos de página y de archivo.
- **Fandom (`action=query&generator=images&titles=System`)**: listado de imágenes usadas en la ficha del Sistema;
  de ahí salieron `Anime_System.png`, `System1.jpg`, `System_talking_to_Jin-Woo.png`, `Shop.jpg`.
- **Descarga y medición propia** (Pillow, con cabecera `Referer: https://www.fandom.com/`) de `Anime_System.png`,
  `System1.jpg`, `Shop.jpg`, `ch10_webtoon.png`, `system_talking.png` — miradas con Read y coloreadas con un
  script de Python (máximo de saturación en una caja de píxeles, no un solo punto al azar).
- **Steam** (`store.steampowered.com/api/appdetails?appids=2373990`): 8 capturas oficiales de *Solo Leveling:
  ARISE OVERDRIVE*, montadas en una hoja de contacto propia (`contacto_arise_overdrive.jpg`) y miradas con Read;
  recorte y zoom de la pantalla RESULT.
- **Google Play Store**: intento con `com.netmarble.slarise` → «Not Found»; no reintentado.
- **Game UI Database** (`gameuidatabase.com/search.php`) y **TCRF** (`tcrf.net/index.php?search=...`): los dos con
  reto de Cloudflare (403), un intento cada uno.
- **Fuentes** (`api.fontsource.org`, `cdn.jsdelivr.net/fontsource`): ficha y `.ttf` de Orbitron, Audiowide,
  Electrolize, Exo 2 y Rajdhani; comprobación de glifos con `fontTools.ttLib.TTFont(...).getBestCmap()` para
  á é í ó ú ñ Ñ ¿ ¡ ü; plancha comparativa propia con Pillow (`fuentes/specimen.png`).
- **TV Tropes** (`tvtropes.org/pmwiki/pmwiki.php/Anime/SoloLeveling`): comprobado que la página responde y
  clasifica la serie en el subgénero «ventana de estado / subir de nivel» (LevelUpFantasy).
- Google Fonts vía `fonts.googleapis.com/css2` para Orbitron/Audiowide/Electrolize: bloqueado por una página de
  verificación anti-bot (`ppConfig`/reCAPTCHA) en dos de los cinco intentos; cambié a la API de Fontsource, que sí
  respondió, para las cinco.

Sigue: falta intentar de nuevo Game UI Database/TCRF más adelante (si el bloqueo de Cloudflare cede) para medir
menús del juego móvil ARISE; y, si aparece cuota, buscar el id correcto de la app en Google Play para sus
capturas de interfaz. El resto de los puntos 5, 6, 11, 18, 24 y 25 está cubierto con fuente propia.
