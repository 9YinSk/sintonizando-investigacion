# Investigación de TEXTO, JUEGOS Y TÉCNICA · Spy×Family

Rol de `EQUIPO.md`: puntos **5, 6, 11, 18, 24, 25** de `ENCARGO.md`. Esta biblia
ya tenía escritos 1-17 (primera pasada, red cerrada); por «Repaso corto» de
`EQUIPO.md` los que faltaban del todo eran 18-25, y a texto le tocan **18, 24 y
25** (imagen hace 19 y 23; voz hace 20, 21 y 22). Parto de `datos-texto.md`
(AniList, staff, Steam) y no repito esas consultas. Miré las hojas de contacto
`hojas/personajes_01.jpg` y `hojas/fondos_01.jpg` (ya hechas) para el punto 18.

---

## 18 · Estilo de dibujo y técnica, y cómo replicarlo

### 18.1 Quién lo dibuja (equipo real, no genérico)
- **Coproducción inusual**: **WIT Studio** anima los episodios impares y
  **CloverWorks** los pares — repartido episodio a episodio, no por escenas ✅
  ([Sakuga Blog](https://blog.sakugabooru.com/2022/05/14/spyfam-and-the-history-of-anime-coproductions/),
  [The Mary Sue](https://www.themarysue.com/spy-x-family-how-the-anime-is-made-by-two-studios-at-once/)).
  Es de las pocas series con dos estudios grandes turnándose así.
- **Dos directores de animación de personajes**: Kazuaki Shimada
  (CloverWorks) y Kyoji Asano (WIT). **Dos directores de arte**: Kazuo Nagai
  (por WIT) e Hisayo Usui (de CloverWorks) ✅ (Sakuga Blog, coincide con
  `datos-texto.md`/AniList).
- **Para que no se note la costura**: un «libro de reglas» (*rule book*)
  compartido dice cómo tratar a los personajes y al mundo en cualquiera de
  los dos estudios; el director **Kazuhiro Furuhashi** supervisa y aprueba
  todo el resultado final ✅ (The Mary Sue).
- **Dato curioso para este mismo proyecto**: la productora de
  pre-producción, **Kazue Hayashi**, actúa como *«una especie de Biblia de
  la obra original»*: traduce el manga a storyboard antes de que cualquier
  estudio anime nada ✅ (The Mary Sue, cita textual en inglés: *"a kind of
  Bible of the original work"*).
- **El propio Endo (autor del manga) mira el anime para dibujar el manga**:
  *«Siempre reviso los dibujos que envía el Sr. Shimada […] Siempre he
  admirado cómo los animadores "dibujan hábilmente con pocas líneas".
  El arte de fondos también es buenísimo, así que a veces uso los
  escenarios que me envían como referencia para la obra original»* ✅ (cita
  completa en la entrevista oficial recopilada en
  [Tatsuya Endo/Interviews](https://spy-x-family.fandom.com/wiki/Tatsuya_Endo/Interviews),
  sección «Mini Interview» de la guía oficial *SPY×FAMILY Official Start
  Guide: ANIMATION×1st MISSION»). Es decir: **el anime influye de vuelta en
  el manga**, no sólo al revés.
- **Software de producción**: no encontré una entrevista que diga
  explícitamente si usan RETAS, Toon Boom o Clip Studio Paint (busqué en
  japonés: 「SPY×FAMILY 制作 クリップスタジオ／RETAS 作画」, sin resultado
  directo) ⚠️. Por el año (2022) y ser TV comercial japonesa, lo normal en
  el sector es **RETAS STUDIO** para el compuesto/coloreado digital y Toon
  Boom Harmony sólo en escenas puntuales; no lo doy como confirmado.

### 18.2 Línea y sombreado, medidos con `estilo.py`
Medido con `herramientas/estilo.py` sobre arte oficial ya listado en
`referencias.json` (no bajé nada nuevo):

| Imagen | Sombreado | Línea (hex) | Saturación | Brillo |
|---|---|---|---|---|
| Yor, cuerpo entero, ilustración color ([fuente](https://static.wikia.nocookie.net/spy-x-family9171/images/3/34/Yor_Forger_Colored_Full_Body.png)) | mixto (plano con degradados suaves en pelo/tela) | `#464734` | 27% | 38% |
| Loid, cuerpo entero, ilustración color ([fuente](https://static.wikia.nocookie.net/spy-x-family9171/images/9/9c/Loid_Forger_Colored_Full_Body.png)) | mixto, **línea marcada** | `#36483A` | 19% | 28% |
| Ficha de WISE sobre Donovan Desmond, fotograma ep. 7 ([fuente](https://static.wikia.nocookie.net/spy-x-family9171/images/9/91/WISE%27s_files_on_Donovan_Desmond_Anime.png)) | degradado / pintado | `#9F9174` (poca línea) | 24% | 76% |
| Berlint desde el aire, fondo del anime ([fuente](https://static.wikia.nocookie.net/spy-x-family9171/images/6/6a/Berlint_Anime.png)) | degradado / pintado | `#CC896C` | 48% | 84% |

✅ (medido, no de memoria). **Lectura**: los **personajes** llevan contorno
fino y **de color** (verde oscuro, marrón, nunca negro puro) con sombreado
mixto —zonas planas de un tono más oscuro y degradados suaves en pelo y
telas—; los **fondos y objetos de papel** (fichas, cartas) casi no llevan
línea y son degradados pintados con más brillo y saturación que los
personajes, que se ven algo apagados para resaltar sobre el fondo.

### 18.3 Fondos: pintados, con luz de la hora del día
Mirando `hojas/fondos_01.jpg` (30 fotogramas ya sacados): las paredes llevan
textura de papel pintado visible (cuadros 1, 2, 7), los interiores usan
paletas cálidas de madera y cobre, y los exteriores cambian de luz según la
escena: atardecer naranja fuerte sobre los tejados de Berlint (cuadro 9),
noche verdosa en el parque con farolas (cuadro 10), azul limpio de día en
Eden (cuadros 15-18). No hay grano de película ni aberración cromática
visibles; el «filtro» es más bien luz suave y algo de resplandor (*bloom*)
en las escenas de atardecer (cuadro 9) ⚠️ (visual, sin entrevista que lo
confirme como intención del estudio).

### 18.4 Encuadres y composición
- **El opening 1, «Mixed Nuts»** (Official HIGE DANdism), está dirigido por
  **Masashi Ishihama** y usa un estilo de **pop art de los años 50-60**:
  siluetas planas, colores de cartel, iconografía de espías de la Guerra
  Fría ✅ ([CBR](https://www.cbr.com/spy-x-family-opening-op-yuri-casting/),
  confirmado por varias fichas del OP). Sirve de referencia directa de
  encuadre para una lámina con estética retro de espionaje.
- Los **informes y fichas en pantalla** (WISE, SSS) casi siempre se
  presentan en **plano cenital o frontal, muy centrado**, como si la cámara
  fuera un escáner: ver hojas O·1, O·2, O·3 de `referencias.json`.
- Los **interiores familiares** (comedor, sala) se filman en **plano
  general con la cámara a la altura de una persona sentada**, para que quepa
  la familia entera en el encuadre (`hojas/fondos_01.jpg`, cuadros 1-6):
  sirve de referencia para una composición de «familia completa» en la
  lámina.
- **Cómo se enmarca cada emoción** (visto en `hojas/personajes_01.jpg`):
  la alegría/travesura de Anya se remata casi siempre en **primerísimo
  primer plano de la cara** (cuadros 13, 15, 17: sonrisa cerrada, ojos en
  arco); el orgullo/arrogancia de Damian y el enfado se presentan en
  **plano medio con la cabeza ligeramente en alto** (cuadro 5, hoja de
  personajes); la ternura entre Loid/Yor y Anya usa **plano general con luz
  cálida y a la altura de los niños** (cuadro 19: Loid y Anya sentados con
  Bond). Esto **complementa, no repite**, el punto 14 (poses con minuto),
  que hace el investigador de vídeo con `fotogramas.py`.

### 18.5 Cómo replicarlo en Photoshop
- **Línea**: pincel de tinta de 2-3 px con *opacidad de la pluma* activada,
  color de línea **no negro puro** (usar el `#36483A` o `#464734` medidos
  arriba, o un marrón oscuro similar) en una capa aparte en modo Multiplicar.
- **Sombreado de personaje**: capa plana de color base + una capa de sombra
  con *clipping mask*, pincel duro, modo Multiplicar al 40-60%, un solo tono
  más oscuro (no degradado) para pelo y ropa —el patrón mixto medido arriba—;
  igual para el brillo de ojos con una capa en modo Aclarar.
- **Fondos**: en vez de plano, usar **degradados suaves** (herramienta
  Degradado o pincel de aerógrafo muy blando) para el cielo y las paredes,
  con textura de papel muy sutil (60-70% de opacidad) para el papel pintado
  de las casas Forger.
- **Rótulos de ficha (WISE)**: capa de textura papel crema (`#D9D7B0` a
  `#ECE8C9`, ya medido en la biblia §5), letra a máquina (ver §6 de la
  biblia, Special Elite/Courier Prime), sello rojo semitransparente rotado
  unos 8-12°.

### 18.6 Cómo replicarlo en Blender
- **Contorno**: la línea de color (no negro) se consigue mejor con
  **Freestyle** (color de línea personalizado por objeto) que con Solidify,
  que da un contorno más uniforme y grueso; para el pelo, un modificador
  **Solidify con material de back-face culling** invertido da un remate más
  limpio en las puntas.
- **Shader tipo cel**: nodo *Shader to RGB* + una **ColorRamp de 2-3 escalones**
  (no degradado continuo) sobre el color base, igual que el sombreado
  «mixto» medido arriba; para el pelo y la ropa con brillo (Yor, capa
  exterior), un tercer escalón especular estrecho.
- **Luz**: una luz de área principal + una de relleno tenue desde abajo
  (rebote de suelo), como se ve en los interiores cálidos de
  `hojas/fondos_01.jpg`; para escenas de atardecer, luz naranja fuerte más
  niebla de volumen ligera para el *bloom* que se ve en el cuadro 9.
- **Modelos y rigs libres** (comprobados por su API, licencia real, no de
  memoria): en Sketchfab hay varios modelos de **Anya, Yor y Bond con
  licencia CC Attribution** (uso comercial permitido citando autor):
  - Anya Forger, por **tonyhoni**, descargable, 67 640 caras, CC-BY ✅
    ([modelo](https://sketchfab.com/3d-models/anya-forger-spy-x-family-a00408ce59324b2dbda2b45357e51b6e)).
  - Yor Forger, por **Acadd**, CC-BY ✅
    ([modelo](https://sketchfab.com/3d-models/none-688f5be5228a41eb9a7cd0817d46b8f3)).
  - Bond Forger, por **won1**, CC-BY ✅
    ([modelo](https://sketchfab.com/3d-models/none-481783da76df4e419132062b77c1527b)).
  - **De Loid no encontré un modelo dedicado** con licencia libre (busqué
    «Loid Forger» en la API de Sketchfab: sólo devolvió modelos de Anya) ⚠️.
  - Ninguno de estos trae *rig* de animación confirmado en la respuesta de
    la API (sólo geometría): revisar cada página antes de usarlo para
    animar. La licencia y el crédito exacto (para el punto 3/23) los debe
    cerrar el investigador de imagen; aquí sólo los dejo como candidatos
    para «cómo replicar la técnica en Blender».
- **Texturas encima**: para el papel de las fichas WISE, una textura de
  papel envejecido (ver punto 4 del encargo, ya cubierto por imagen) mapeada
  con poca rugosidad y algo de *bump* para las esquinas dobladas.

---

## 24 · Obras parecidas y temas relacionados

### 24.1 Lo que el propio Endo reconoce (fuente primaria, no de fans)
De la misma recopilación de entrevistas oficiales
([Tatsuya Endo/Interviews](https://spy-x-family.fandom.com/wiki/Tatsuya_Endo/Interviews)):
- **Referentes de dibujo declarados por Endo**: fue asistente antes de su
  serialización y tomó «lo mejor de la acción tosca de **Yusuke Nomura**
  (autor de *Blue Lock*) y el estilo brillante, algo shōjo, de **Nao Emoto**
  (autora de *O Maidens in Your Savage Season*)» ✅ (cita textual, entrevista
  «Kikan S»).
- **Personajes secundarios cómicos**: Endo dice que los diseños exagerados
  de secuaces (el amigo de Damian, el chico musculoso del dodgeball) siguen
  «la combinación clásica de los secuaces flaco y gordo junto a Doronjo, de
  **Yatterman**» ✅ (misma entrevista, cita textual).
- **Influencia de infancia**: de niño le gustaba **Akira Toriyama** como
  diseñador de personajes de *Dragon Quest*, y dibujaba parodias de la
  princesa Alena de ese juego ✅ (misma página, sección de infancia).
- **No es un especialista en espías**: Endo admite que no le interesaban
  especialmente las historias de espías al empezar la serie; la pensó desde
  el tema de **«las mentiras»**, no desde el género de espionaje ✅
  ([FandomWire](https://fandomwire.com/tatsuya-endos-lack-of-interest-in-spy-stories-turned-gave-spy-x-family-a-surprising-advantage/)).
  **No confundir esto con «no tiene influencias»**: sí las tiene, y están
  en el dibujo (arriba), no en la trama de espías.

### 24.2 De sus obras anteriores a Spy×Family (evolución del propio autor)
- Antes de esta serie, Endo dibujó **TISTA** (una asesina como protagonista,
  tono serio) y **Gekka Bijin**, ambas en *Jump Square*, con «personajes y
  trama oscuros». Al planear su tercera serialización, **él y su editor
  Shihei Lin decidieron a propósito hacer algo más positivo** —de ahí el
  contraste entre la asesina seria de *TISTA* y la asesina cómica y torpe
  de Yor ✅ (misma recopilación de entrevistas, sección «The Birth of
  SPY×FAMILY», cita del editor Lin).
- El título «SPY×FAMILY» está inspirado en el formato de **Hunter × Hunter** ⚠️
  (una fuente, resumen de prensa; no vi la cita exacta en la wikitext).

### 24.3 Comparaciones de la crítica (dos fuentes por comparación)
- **Con *Mr. & Mrs. Smith*** (película de 2005 y serie de 2024): la premisa
  —espía y asesina fingen ser pareja sin saber la identidad del otro— es
  casi idéntica; la diferencia es que Spy×Family «se apoya en lo ridículo
  de la situación en vez de pedirle al público que se lo crea» ✅
  ([Tokyo Weekender](https://www.tokyoweekender.com/entertainment/movies-tv/spy-x-family-mr-mrs-smith-comparison/),
  [CBR](https://www.cbr.com/spy-x-family-manga-coolest-cutest-family/)).
  **Dato curioso**: Endo **nunca ha visto la película** ✅ (dos fuentes:
  [FandomWire](https://fandomwire.com/that-cant-possibly-happen-tatsuya-endo-still-hasnt-watched-angelina-jolie-and-brad-pitts-one-film-that-no-spy-x-family-fan-should-miss/)
  y el mismo CBR).
- **Con *The Incredibles* / *Fantastic Four***: a medida que la «familia»
  se une, la historia toma la forma clásica de familia de superhéroes que
  esconde sus poderes ✅ (CBR, arriba).
- **Recomendadas por quien vio la serie** (AniList, ya en `datos-texto.md`,
  no repetido): *Buddy Daddies* (padres postizos + niña, votos 562),
  *Kaguya-sama* (comedia de instituto con estrategia, votos 527),
  *Great Pretender* (estafadores, votos 273), *SAKAMOTO DAYS* (asesino
  retirado con familia, votos 162), *The Yakuza's Guide to Babysitting*
  (votos 138). Sirven para el «tono»: comedia + un secreto que no puede
  salir a la luz.

### 24.4 En el propio servidor «Sintonizando»
- Repasé los 137 encargos (`encargos/*.md`) buscando «espía», «espionaje»,
  «agente secreto» y «spy»: **ninguno más toca el espionaje** ✅ (grep hecho
  sobre todos los archivos). No hay riesgo de repetir la idea del
  «expediente/ficha falsa» en otro canal.
- De las bíblias **ya terminadas** (01 a 36), ninguna comparte el tono de
  «comedia de agentes secretos en familia»; la más cercana en **estructura**
  (colegio + estrategia + comedia romántica) sería *Kaguya-sama* si se hace
  algún día (encargos 43 y 90, aún sin biblia) ⚠️ (comparación mía, no hay
  biblia de esa serie todavía que comparar imagen a imagen).

---

## 25 · El mundo, la historia y sus símbolos

### 25.1 Las reglas del mundo, en 5 líneas
1. **Westalis** (donde nació Loid) y **Ostania** (donde vive la familia,
   capital **Berlint**) llevan **décadas de guerra fría**, tras **dos
   guerras reales entre ambos países** que dejaron a Ostania muy dañada ✅
   ([Fandom, página Ostania](https://spy-x-family.fandom.com/wiki/Ostania)).
2. Ostania mantiene políticas de guerra bajo una fachada de apertura y
   economía en crecimiento ✅ (misma fuente). Es el espejo de la Alemania
   del Este / Guerra Fría que ya señala la biblia en su §5.2 (SSS = Stasi).
3. **WISE** (Inteligencia de Westalis) opera en la sombra: su propio
   discurso de bienvenida a los agentes lo resume: *«No ganarás medallas.
   Tu nombre nunca saldrá en los periódicos. Pero nunca olvides que la vida
   diaria de los demás es posible gracias a tu sangre y tu sudor»* ✅ (cita
   textual de WISE a Twilight, cap. 1 / ep. 1, wikitext de
   [Westalis Intelligence](https://spy-x-family.fandom.com/wiki/Westalis_Intelligence)).
4. **SSS** (Servicio de Seguridad del Estado, la «policía secreta») vigila,
   intercepta y detiene dentro de Ostania; es «ampliamente temida por el
   público» ✅ ([Fandom, State Security Service](https://spy-x-family.fandom.com/wiki/State_Security_Service)).
5. **Garden**, el grupo de asesinos de Yor, lleva **siglos** «al servicio de
   Ostania» «para hacer del mundo un lugar hermoso» purgando traidores; casi
   nadie sabe que existe, ni siquiera la mayoría de la SSS ✅ (misma wiki,
   página [Garden](https://spy-x-family.fandom.com/wiki/Garden)).

### 25.2 La historia por arcos (lista real de la wiki, no inventada)
De la página [Story Arcs](https://spy-x-family.fandom.com/wiki/Story_Arcs)
(21 arcos listados a fecha de hoy; anime cubre los primeros ~11) ✅:
1. **Introducción**: Twilight arma la familia falsa para la Operación Strix.
2. **Entrevista de admisión**: la familia debe engañar a Eden en la
   entrevista (la escena madre del canal, ya en §2 de la biblia).
3. **Comienzos en Eden**: Anya entra a Cecile Hall y debe acercarse a
   Damian; conoce a Becky.
4. **Policía secreta**: la SSS empieza a rondar a la familia; Yuri descubre
   el matrimonio de su hermana.
5. **Estrella Stella**: Anya compite por conseguir Estrellas Stella (ver
   §25.3).
6. **Exámenes de mitad de año**: Anya se juega la expulsión a golpe de
   Rayos Tonitrus.
7. **Torneo de tenis Campbelldon**: Twilight debe recuperar el «Expediente
   Zacharis», que «podría reavivar las llamas de la guerra».
8. **Mixer de Eruditos Imperiales**: Damian busca la atención de su padre.
9. **Aventura del crucero** (el arco **más largo**: 15 capítulos / 7
   episodios): Yor, como Thorn Princess, protege a una madre y su hijo a
   bordo del *Princess Lorelei* sin descubrir su identidad secreta ante la
   familia.
10. **Pasado de Loid**: se cuenta el origen de Twilight como espía.
11. **Planes de amistad**: Anya mejora su amistad con Damian; Yor hace una
    amiga inesperada.
12. **Secuestro del autobús**: el grupo terrorista **Red Circus** secuestra
    el autobús escolar de Anya.
13. **Caso Wheeler**: un topo roba documentos clasificados, incluida
    información de la Operación Strix.
14. **Finales de término**: Anya se juega su futuro en Eden en su primer
    examen final.
15. **Amor y guerra**: el pasado de Henry Henderson (director de Eden) con
    su vieja amiga Martha Marriott.
16. **Vacaciones de término**: la familia descansa; una sesión de terapia
    revela una pista clave.
17. **Caza de cazadores furtivos**: Thorn Princess y Garden protegen a unos
    alces en peligro; pelea con la asesina Hemlock.
18. **Escándalo en Eden**: Loid destapa la verdad sobre Sigmund Authen con
    las notas de Melinda Desmond.
19. **Isla de TV**: Yor invita a Loid a ver una grabación en vivo de un
    drama romántico.
20. **Reunión de la SSS**: Yuri lleva a Loid a una fiesta de sus compañeros
    de la policía secreta.
21. **Investigación en el hospital**: Loid es ingresado y un simposio médico
    atrae tanto a WISE como a un invitado inesperado.

Los nombres son en su mayoría **puestos por fans para organizar la wiki**
(sólo *Doggy Crisis*, *Cruise Adventure*, *Loid's Past*, *Bus Hijacking*,
*Wheeler* y *TV Island* son oficiales del propio manga) ✅ (aviso de la
propia wiki, arriba de la lista).

### 25.3 Emblemas, logos y objetos icónicos
- **El búho de WISE** con el sello rojo «TOP SECRET»: ya está en la biblia
  §3 (hallazgo O·1) y en `referencias.json`; es el emblema que más se
  reconoce de la organización de Loid.
- **El emblema de Eden Academy**: una **manzana partida por la mitad con
  las letras «EC»** (de *Eden College*, el nombre formal en el manga
  original en japonés, aunque el doblaje diga «Eden Academy»). El símbolo
  remite a la manzana bíblica del Jardín del Edén (fruta prohibida /
  conocimiento) ✅ ([ComicBook.com](https://comicbook.com/anime/news/spy-x-family-eden-academy-project-apple/),
  repetido en [The Flagship Eclipse](https://www.theflagshipeclipse.com/2025/02/19/spy-x-familys-eden-academy-could-be-hiding-a-dark-secret/),
  aunque ambos artículos podrían compartir la misma fuente original ⚠️
  parcial). Se ve bordado en el uniforme, visible en las hojas de
  personajes ya guardadas (`hojas/personajes_01.jpg`, cuadros 5-6, 26-27).
- **La Estrella Stella y el Rayo Tonitrus**: en cada examen, los dos
  mejores de cada asignatura ganan una Estrella Stella; los que no llegan
  al mínimo (nota 30) reciben un Rayo Tonitrus. La imagen de la estrella
  dorada ya está en `referencias.json` (O·19, `Stella_Star.png`) ✅
  ([Fandom, Eden Academy](https://spy-x-family.fandom.com/wiki/Eden_Academy)).
- **Los Eruditos Imperiales** (*Imperial Scholars*): el programa de honor
  de los mejores alumnos de Eden, con retratos en el «Salón de la Fama» de
  la escuela. Cita de presentación en la propia serie: *«Eden ofrece una
  educación de primer nivel en todos los campos […] los estudiantes que
  logran distinguirse incluso entre sus compañeros de élite se unen al
  programa de honor de la escuela, los llamados Eruditos Imperiales»* ✅
  (Sylvia Sherwood a Loid, cap. 7 / ep. 6, wikitext de
  [Imperial Scholars](https://spy-x-family.fandom.com/wiki/Imperial_Scholars)).
- **Proyecto Apple**: el programa militar de Ostania que creó a Bond
  (sujeto n.º 8): buscaba animales muy inteligentes para uso militar; Bond
  desarrolló clarividencia como efecto secundario no buscado ✅
  ([ScreenRant](https://screenrant.com/spyx-family-project-apple-bond-anya-mysteries/),
  [Fandom, Project Apple](https://spy-x-family.fandom.com/wiki/Project_Apple)).
  **Coincidencia de nombre con el emblema de Eden** (la manzana): un artículo
  lo señala como teoría de fans, sin confirmar en la obra ⚠️ (ComicBook.com,
  arriba, lo llama «especulación», no dato canónico).
- **Chimera**, el peluche de Anya, y el rótulo de misiones «MISSION: N /
  OPERACIÓN STRIX»: ya cubiertos en la biblia §2 y §7.

### 25.4 Vocabulario propio (glosario rápido para subtítulos y cartelas)
| Término | Qué es |
|---|---|
| **Operation Strix** | la misión de Twilight para investigar a Donovan Desmond |
| **WISE** | inteligencia de Westalis; Twilight es su agente |
| **SSS / Secret Police** | policía secreta de Ostania, dirigida por Wyman Wilker |
| **Garden** | grupo secreto de asesinos «por la belleza del mundo»; Yor es su Thorn Princess |
| **Eden Academy (Eden College)** | el colegio de élite; emblema manzana + «EC» |
| **Stella Star / Tonitrus Bolt** | premio y castigo académico en Eden |
| **Imperial Scholar** | alumno de honor de Eden |
| **Project Apple** | programa militar que creó a Bond |
| **Red Circus** | grupo terrorista del arco del secuestro del autobús |
| **Berlint** | capital de Ostania, donde vive la familia Forger |

---

## Revisión de mis puntos ya existentes (5, 6, 11) — confirmé, no rehice
No son mi encargo obligatorio en este repaso (ya estaban escritos), pero
revisé sus ⚠️ como pide el lanzamiento:
- **§6 Tipografía / §7 Cuadros de diálogo (puntos 5-6)**: los ⚠️ que quedan
  (letra exacta de los rótulos del anime, recurso gráfico propio de Yor, la
  caja de diálogo del videojuego) son de verdad indetectables sin ver el
  anime a resolución alta o el juego en marcha; **no encontré cómo
  bajarlos** de fuentes escritas (busqué «Spy x Family font rótulo
  identificación» y «SPY×FAMILY Operation Diary UI screenshot dialogue
  box», sin resultado nuevo). Los dejo ⚠️ con la búsqueda hecha, no los
  quito.
- **§13 Videojuegos (punto 11)**: comprobé The Cutting Room Floor —
  **no tiene página de SPY×FAMILY Operation Diary/Operation Memories**
  (busqué en `tcrf.net` vía buscador: «site:tcrf.net spy x family», sin
  resultados) ✅ confirmado que no existe, no que «no lo encontré».

---

## Lo mejor para la lámina
1. **La «Biblia de la obra»**: la productora Kazue Hayashi literalmente hace
   con el manga lo mismo que este equipo hace con la serie —un documento
   maestro para que dos equipos dibujen igual—. Buena anécdota para el
   propio Discord de doblaje/animación.
2. **Contorno de color, nunca negro puro** (`#36483A`, `#464734` medidos):
   corrige cualquier lámina que use trazo negro plano.
3. **El emblema de Eden (manzana + «EC»)** es un objeto pequeño y con
   significado que cabe perfecto bordado en una tela o grabado en un objeto
   de Blender.
4. **Yatterman y Blue Lock/O Maidens como influencias confirmadas por Endo**:
   sirven para explicar «por qué los secuaces se ven exagerados» sin
   inventar nada.
5. **Los 3 modelos 3D con licencia CC-BY** (Anya, Yor, Bond) son un punto de
   partida real para Blender, ya con licencia comprobada por API.

## No encontré
- ⚠️ Software exacto de producción (RETAS/Clip Studio/Toon Boom): sin
  entrevista técnica que lo confirme, ni en inglés ni en japonés.
- ⚠️ Un modelo 3D libre dedicado de **Loid** (sólo aparecieron modelos de
  Anya al buscar «Loid Forger» en la API de Sketchfab).
- ⚠️ La imagen exacta de la caja de diálogo del videojuego *SPY×FAMILY
  Operation Diary / Operation Memories* (no hay capturas de esa pantalla en
  las reseñas que revisé).
- ⚠️ Confirmación de si «Project Apple» y el emblema de Eden están
  conectados en la obra: un artículo lo plantea como teoría de fans, no
  como dato canónico.

## Bitácora de búsqueda (texto)
- WebSearch (inglés): «Tatsuya Endo interview influences James Bond»,
  «Spy x Family CloverWorks WIT Studio making of animation production
  interview», «Spy x Family Kazuaki Shimada character design interview art
  style», «Spy x Family art director Kazuo Nagai background art color
  design interview», «Spy x Family review compared to Despicable Me/Mr and
  Mrs Smith/Incredibles», «Spy x Family story arcs list manga anime wiki
  chronological», «Spy x Family WISE logo owl symbol meaning Eden Academy
  crest emblem», «Spy x Family Bond Project Apple psychic dog experiment
  origin», «Tatsuya Endo Tista Gekka Bijin previous manga influences spy
  genre interview», «Sketchfab Spy x Family Anya Loid Yor free rig model CC
  license», «Spy x Family opening 1 Mixed Nuts animation director
  storyboard cuts analysis».
- WebSearch (japonés): 「SPY×FAMILY 制作 クリップスタジオ OR RETAS 作画
  インタビュー」 (sin resultado técnico directo).
- WebFetch: Sakuga Blog (coproducción), The Mary Sue (rule book, Kazue
  Hayashi), ComicBook.com (emblema de Eden).
- API de Fandom (`spy-x-family.fandom.com/api.php`, `action=parse`,
  `prop=wikitext`): páginas *Story Arcs*, *Tatsuya Endo/Interviews*, *Eden
  Academy*, *Imperial Scholars*, *Westalis Intelligence*, *State Security
  Service*, *Garden*, *Operation Strix*, *Ostania*, *Westalis*.
- API de Sketchfab (`api.sketchfab.com/v3/search` y `/models/<uid>`):
  licencias reales de modelos de Anya, Yor, Bond, Loid.
- `herramientas/estilo.py` sobre 4 imágenes ya listadas en
  `referencias.json` (línea, sombreado, paleta).
- Revisé `hojas/personajes_01.jpg` y `hojas/fondos_01.jpg` con Read (ya
  hechas por el equipo de imagen) para el punto 18.
- `grep` sobre los 137 `encargos/*.md` para el punto 24.4 (ninguno más de
  espías).
- Comprobé The Cutting Room Floor por buscador (`site:tcrf.net`): sin
  página del juego.
