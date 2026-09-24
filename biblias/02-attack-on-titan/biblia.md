---
tags: [biblia, serie, laminas]
serie: "Attack on Titan (Shingeki no Kyojin)"
canal: "#reglas"
fecha: 2026-09-24
amplia: "biblias/_ya_hechas/Attack on Titan.md"
---

# Biblia · Attack on Titan (2.ª vuelta) · para #reglas

> [!abstract] Qué es esto
> La biblia del 23-sep ya sirvió para la lámina 1: **la estela de piedra con las
> ocho reglas al pie de la Muralla**. Esta segunda vuelta **no la repite**: añade lo
> que faltaba para las láminas 2 y 3 y para una alternativa a la estela.
> Qué añade: el arte oficial nuevo (2023-2026), las encuestas oficiales,
> el doblaje latino con dos fuentes por nombre, los hex medidos, las letras
> comprobadas letra a letra, el juego nuevo (*Attack on Titan 3*, 10-dic-2026) y
> tres conceptos nuevos.

> [!important] Cómo se hizo (léelo primero)
> - **Dos pasadas.** La primera (24-sep-2026, mañana) se hizo **con la red
>   cerrada**: sólo buscador web (48 búsquedas) y GitHub. Sin hojas de contacto,
>   sin Doblaje Wiki por su API y sin mirar vídeos.
> - **Segunda pasada, 24-sep-2026 (tarde), con la red abierta.** Terminada. La
>   hicieron tres ayudantes seguidos (a los dos primeros los cortó el límite de
>   uso; el tercero revisó todo contra `COMPLEMENTO.md` y la cerró). Se pudo usar:
>   - **Wiki de Fandom** (`attackontitan.fandom.com`) por su API: 3 tandas de
>     `investigar_serie.py` y el tamaño real de cada imagen. Las hojas están en
>     `hojas/` (§2.0). En el cierre, 18 poses más de Hange, Mikasa y Eren (§15).
>   - **Doblaje Wiki** por la API (`action=parse`): reparto, equipo técnico,
>     datos de interés y **muestras de audio del doblaje**, pasadas por
>     reconocimiento de voz (Whisper) para sacar frases textuales (§9).
>   - **Subtítulos japoneses de Netflix** (espejo de kitsunekko en GitHub), con
>     el nombre de quien habla: de ahí salen los **minutos exactos** (§3).
>   - **YouTube con yt-dlp**: datos, títulos, descripciones y, en el cierre,
>     **subtítulos automáticos en español de los 3 clips doblados oficiales**
>     (§9.4). **La descarga del vídeo** da 403 o pide «iniciar sesión» (somos
>     varios con la misma IP). Plan B de `AYUDANTE.md`: bajé los *storyboards* y
>     los pasé por `herramientas/fotogramas.py` (hojas numeradas con su minuto,
>     ±1-2 s). Miré así el opening, el ending, dos tráileres y cinco escenas
>     (§10, §11).
>   - **Juegos**: API de Steam (capturas oficiales de 1920×1080 de *AoT 2*,
>     *Wings of Freedom* y *AoT 3*) y la web oficial japonesa de *AoT 2*, donde
>     por fin se ve **su caja de diálogo** (§12).
>   - **Chino**: Bangumi (API) y la Wikipedia china (§8, §14).
>   - **Sketchfab** (licencias por su API), FUNiAnime, ANMTV, el portal oficial
>     (imágenes medidas bajándolas), Wallhaven (API), Reddit por Arctic Shift,
>     eiga.com y un blog japonés sobre el director de arte (§5).
>   - **No respondieron**: ArtStation (403), las páginas de Wayback Machine
>     (conexión cortada), Moegirl y Baidu Baike (acceso denegado), TikTok con
>     yt-dlp y la Wikipedia japonesa (429).

## Segunda pasada · qué cambió

**Corregido (antes → ahora):**
- **El clip doblado «¡Consagren sus corazones!» de Crunchyroll**: «ep. 73,
  los reclutas apalean a Keith» → **ep. 71**. Lo miré: es la bomba en el
  despacho de Zackly y **la gente en la verja grita la frase con el puño en
  alto** (clip 0:48-0:58 = ep. 12:31-12:57). Su descripción dice «Episodio 71».
  Lo de Keith sí es del ep. 73, pero no sale en ese clip (§3, §9).
- **Frase latina de Levi «Tu determinación me dará fuerza»**: «episodio sin
  identificar» → **ep. 9 · 06:57-07:04**, a un soldado que muere (§9.3).
- **Visual de MAPPA 15**: «Mikasa… sonriendo» → **va de espaldas; no se le ve
  la cara**. Medido: 1754×2481 (§2.1).
- **Dibujo de Isayama del Día de AoT**: «quién sale no lo pude ver» (con aviso) → lo
  miré en el portal: **Eren adulto detrás, puño en alto, y Levi delante de
  brazos cruzados**, a tinta (§2.1).
- **El ending de la T1**: «todo en gris» → gris la primera mitad y **sepia de
  papel viejo desde 0:56** (§10).
- **Minutos del tráiler latino**: «MÚSICA…» 0:26 → **0:27**; añadidos
  «PRODUCCIÓN MAPPA» (0:22) y «DIRECCIÓN» (0:25) (§6).
- **Los colores de la ficha en los conceptos**: siempre cinta roja `#5C0001` y
  papel `#F4EEEF` → **la cinta del episodio que se cita** (A ocre, B verde,
  C oro viejo) y papel `#F2F2F2`, como pide §7.1 (§19).
- **Erwin sin brazo y el uniforme**: «de memoria» (con aviso) → confirmados (ep. 36 en
  los subtítulos y ficha de la wiki; uniforme en la página «Military» de la
  wiki) (§13, §16).
- De la primera mitad de esta pasada (ayudante anterior): minutos exactos de
  todas las escenas (subtítulos de Netflix); la ficha medida en sus 54 versiones
  (antes se creía de un solo color); Hange en la película es **Rossy Aguirre**
  (no Laura Torres); Reiner es **Alfonso Obregón** (no Óscar López); la frase
  de Connie era el chiste japonés, no el doblaje; el cuerpo se llama **«Legión
  de Exploración»** en el doblaje (no «de Reconocimiento»); VSI hizo sólo la
  película; Eren sale **de perfil** (no de espaldas) en el visual de *AoT 3*.

**Corregido en el cierre (tercer ayudante):**
- **Caja de diálogo de *AoT 2***: «no la pude ver» → **vista en la web oficial
  japonesa**: sin caja, nombre pequeño sobre una línea crema, dos líneas de
  texto blanco con sombra y una ✓ al final (§12). Menús de *AoT 3* en las
  capturas de Steam: pergamino sobre madera con clavos y martillo (§12).
- **Frases latinas de clips oficiales**: «los clips no dieron subtítulos» →
  **subtítulos automáticos en español de los 3 clips doblados**, con minuto y
  enlace (§9.4).
- **Chino**: «no encontré nada» → **Bangumi y la Wikipedia china**: en China el
  personaje favorito es Mikasa y Levi va segundo (§8); Levi coge la taza por el
  borde (§14, dos fuentes).
- **Poses de Hange, Mikasa y Eren**: 5 cada uno → **11, 10 y 10**, miradas y
  con enlace a la imagen (§15).
- **Entrevistas de arte**: «no se hizo» → identificados el director de arte
  (Shunichiro Yoshihara y sus «nubes de varios blancos», §5) y el artbook de
  Kyoji Asano (§2.1).

**Añadido:** 3 hojas de contacto (P·, E·, F·; 88 imágenes con tamaño medido);
frases latinas textuales de Levi, Erwin, Hange, Keith, Zackly y Nile (§9.3) y
de los clips oficiales (§9.4); hojas de fotogramas del opening, el ending, dos
tráileres y cinco escenas (§10-§11); Sketchfab y Poly Haven con licencia por
API; fan art con autor; fondos de pantalla de fans con tamaño (§17); Reddit por
Arctic Shift (§13); capturas oficiales de los tres juegos (§12); `referencias.json`
rehecho: **40 entradas**, todas con tamaño medido; la tabla «Cumplimiento del
encargo».

**Conceptos de lámina**: el **A** gana referencias oficiales nuevas: el
pergamino clavado sobre madera del menú de *AoT 3*, **Levi con mascarilla de
limpiar en *AoT 2*** como pose de cuerpo entero, el patio donde los cadetes
barren y **la caja de diálogo de *AoT 2*** como cuadro alternativo (§19). B y
C no cambian.

**Avisos ⚠️**: había **14** antes de esta pasada; ahora `grep` cuenta **8**.
Sólo **3 son datos dudosos** (Carlos Monroy, Ivett Toriz y «Legión de
Exploración», todos con una sola fuente; §20). Los otros son este aviso y las
**4 filas «a medias»** de la tabla «Cumplimiento del encargo» (fuentes
oficiales, Wayback, entrevistas a los actores latinos y vídeos vistos sólo por
*storyboard*), que se marcan así a propósito.

### Repaso corto (24-sep-2026): puntos 18-25

Tres investigadores (texto, imagen, voz) y el redactor. `ENCARGO.md` añadió
ese día los puntos 18-25; la tabla no los tenía.

**Añadido** (secciones «Punto 18» a «Punto 25», entre §18 y §19):
- **18 · Técnica**: Isayama dibuja a mano; WIT mezcla 2D y 3DCG; MAPPA, más
  CG. Cómo hacerlo en Photoshop y Blender, 7 *rigs* CC BY y encuadre por
  emoción.
- **19 · Texturas 2D**: trama y rayado mirados en el manga; papel, tela y
  cuero CC0; los uniformes no tienen estampado.
- **20 · Gustos**: el té de Levi sin azúcar, la llave de Eren, el sueño de
  Erwin, las gafas de Hange, por qué protege Mikasa.
- **21 · Por qué la aman**: tres escenas que hacen llorar, **con minuto
  exacto** (eps. 55, 67 y 93) y el mismo tema en dos de ellas, «Call of
  Silence».
- **22 · Fandubs**: fandubs y covers latinos, el debate de doblaje en TikTok.
- **23 · Colaboraciones**: *Fortnite*, gachas, UNIQLO, cafés (uno abierto
  ahora, con arte nuevo de WIT), USJ y **8 figuras con sus caras**.
- **24 · Parecidas**: AniList con votos, influencias de Isayama y cómo no
  repetir las láminas de Evangelion y Solo Leveling.
- **25 · Mundo**: 5 reglas, 9 arcos y el vocabulario.
- Antes, en este mismo repaso: una letra para cada uso (§6.1), la música de
  las escenas tristes (§10.1), cara en cada emoción y dinámicas (§14.1-14.3) y
  la guía para IA de texto (§18.1).
- `referencias.json`: **40 → 218**.

**Corregido (antes → ahora)**: la tabla de arcos de la parte decía «Levi y su
escuadrón mueren» → **muere el escuadrón de Levi** (Levi sigue vivo en el
ep. 55, Punto 21.2).

**Conceptos**: la idea de los tres no cambia; ganan referencias (al final
de §19).

**Avisos ⚠️**: antes de este repaso, `grep` contaba **26**; ahora **90** (contando los de estos avisos y la bitácora). Casi
todos son datos con una sola fuente en las secciones nuevas (alturas y
manías del Punto 20, vistas de YouTube del 22). Las filas «a medias» de la
tabla pasan de 4 a 6: se suman **20** (sin comida favorita) y **22** (vistas
sin comprobar).

---

## 0 · En corto (para leer en el celular)

- **El más querido es Levi**, no Eren. Ganó tres de las cuatro encuestas
  oficiales. Erwin ganó la tercera. En la última, Hange quedó tercera y Eren cuarto.
- **El cuadro de diálogo propio**: la ficha «Información pública del momento».
  Papel gris claro `#F2F2F2`, texto en mincho y una cinta de pincel **del color
  del episodio** (rojo sangre sólo en el ep. 1; tribunal verde, limpieza ocre,
  saludo oro viejo). Medida en sus 54 versiones (§7.1). En los juegos, **sin
  caja**: nombre sobre una línea crema, texto blanco y una ✓ (*AoT 2*, §12).
- **Frase latina segura**: «¡Consagren sus corazones!» (Erwin, Octavio Rojas,
  ep. 16 · 14:13; y la gente en el ep. 71, clip oficial de Crunchyroll).
  De Levi (Gabriel Basurto): «Yo no planeo estrategias. Eso no me compete»
  (ep. 15 · 08:44, muestra de Doblaje Wiki).
- **Lo nuevo de 2026**: el 9 de septiembre ya es oficialmente el «Día de Attack
  on Titan». Hubo un dibujo nuevo de Isayama y salió el juego *Attack on Titan 3*.
- **Tres láminas nuevas**: el reglamento del cuartel con Levi limpiando (ep. 15),
  la sentencia del tribunal para las sanciones (ep. 14) y la bandera con
  «¡Consagren sus corazones!» para aceptar (ep. 16).

---

## 1 · Qué tiene que decir el canal

Los textos reales salen de `servidor/inventario.md`:

| Dónde | Texto real |
|---|---|
| **#📜・reglas** | «Las normas. Al quedarte, las aceptas.» |
| #🧾・log-mod | «Cada sanción, quién y por qué.» |
| #🎫・soporte | «Abre un ticket: solo lo vemos tú y el staff.» |
| Foro #🗺️・guia | Tiene la etiqueta **Normas** y el hilo «Lo que hay que leer». |

- Las **ocho reglas** están en la lámina ya hecha
  (`herramientas/laminas_v2/v3/reglas_aot.html`). Ese archivo **no está en este
  repositorio**, así que aquí no copio sus textos.
- La **escala de sanciones** (aviso, silenciado, expulsión, baneo; lo grave va
  directo; se apunta en log-mod; se discute por soporte) es una **propuesta
  de la biblia anterior. Todavía no tiene su sí.** No se publica sin él.
- Según su regla 5, si no cabe todo, va **lámina 2**. Aquí propongo tres:
  1. las reglas (alternativa a la estela),
  2. qué pasa si no se cumplen,
  3. cómo se aceptan (el ✅).

---

## 2 · Arte oficial nuevo (lo que no estaba en la biblia anterior)

### 2.0 · Las hojas de contacto (lo que vi en la wiki) ✅

Corrí `investigar_serie.py` tres veces sobre `attackontitan.fandom.com`:
- **personajes** (Levi, Erwin, Hange, Eren, Mikasa, Keith, Zackly y sus fichas del anime): **1479 imágenes, 31 hojas**;
- **episodios** (3, 14, 15, 16, 19, 36, 53, 54 y las fichas «Información pública»): **175 imágenes, 4 hojas**;
- **sitios** (murallas, Trost, Stohess, Utgard, el tribunal, los cuerpos): **161 imágenes, 4 hojas**.

**Las miré.** Mucho no sirve para la lámina: unas 700 son **viñetas del manga** (otro dibujo) y unas 120 son **portadas de capítulos**. Monté **3 hojas propias** con lo mejor, y las miré otra vez: cambié 9 celdas que eran manga o no eran la escena que decía la etiqueta. En cada celda va el tamaño real (API de la wiki) y, si lo sé, el capítulo y minuto (de los subtítulos de Netflix).

**`hojas/personajes_01.jpg`** (P·): poses y caras

| N.º | Qué es | Tamaño · dónde | Para qué | Original |
|---|---|---|---|---|
| P·1 | Arte oficial: Eren, Levi y Mikasa | 2500×3513 · WIT | **presentar** en grupo; Levi de brazos cruzados (arte limpio) | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/4/45/SnK_-_Eren%2C_Levi%2C_and_Mikasa.png/revision/latest?cb=20130712033841) |
| P·2 | Arte promo: Erwin y Levi | 1500×2302 | Erwin y Levi juntos: explicar/presentar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/9/9d/Erwin_Levi_promo_art.jpg/revision/latest?cb=20210715035815) |
| P·3 | Visual de Attack on Titan 3 (portal) | 1500×2121 · 2026 | arte oficial 2026: Levi con las hojas al revés | [enlace](https://aot-portal.com/wp/wp-content/uploads/2026/09/No.68_%E3%80%90SGK%E3%80%91%E3%82%B2%E3%83%BC%E3%83%A0%E3%83%93%E3%82%B8%E3%83%A5%E3%82%A2%E3%83%AB%E7%89%88%E6%A8%A9_%E7%B4%8D%E5%93%81_RBG-1.jpg) |
| P·4 | Los reclutas saludan: puño al corazón | 3840×2160 | **aceptar** (el saludo, puño derecho) · concepto C | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/b/b0/The_trainees_offer_up_their_hearts_to_mankind.jpg/revision/latest?cb=20160412142629) |
| P·5 | Levi: ficha del anime | 1080×1080 | cara de Levi, ¾, párpado caído: presentar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/b/b1/Levi_Ackermann_%28Anime%29_character_image.png/revision/latest?cb=20231105181307) |
| P·6 | Erwin: ficha del anime | 1080×1080 | cara de Erwin de frente: explicar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/d/de/Erwin_Smith_%28Anime%29_character_image.png/revision/latest?cb=20190604212647) |
| P·7 | Hange: ficha (T4, parche) | 1080×1080 | Hange T4 (parche): comandante | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/e/e4/Hange_Zo%C3%AB_%28Anime%29_character_image.png/revision/latest?cb=20210221212604) |
| P·8 | Keith Shadis: ficha | 1080×1080 | cara de Keith: regañar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/6/68/Keith_Sadies_%28Anime%29_character_image.png/revision/latest?cb=20210322010239) |
| P·9 | Zackly: ficha | 1080×1080 | cara de Zackly: dictar sentencia · concepto B | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/3/3e/Dhalis_Zachary_%28Anime%29_character_image.png/revision/latest?cb=20210221221357) |
| P·10 | Levi con ropa de limpiar | 1920×1080 · ep. 15 | **Levi limpiando**: regañar con humor · concepto A | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/8/85/Levi_the_cleaner.png/revision/latest?cb=20240124091945) |
| P·11 | Levi encuentra polvo | 1920×1080 | Levi pasa el dedo y ve polvo: regañar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/f/f9/Levi_finds_dust.png/revision/latest?cb=20240130070732) |
| P·12 | Levi patea a Eren en el juicio | 1920×1080 · ep. 14 · 18:33 | la patada del juicio: sancionar (sin sangre) | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/8/8a/Levi_beats_up_Eren.png/revision/latest?cb=20240124091739) |
| P·13 | Levi habla a los mercaderes | 1920×1080 · ep. 14 · 13:50 | Levi, de pie y seco: advertir | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/1/13/Levi_talks_to_the_merchants.png/revision/latest?cb=20240124091545) |
| P·14 | Levi pide a Eren que elija (fuego) | 1920×1080 | Levi deja elegir: animar en serio | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/5/55/Levi_tells_Eren_to_make_a_choice.png/revision/latest?cb=20180911135336) |
| P·15 | Levi tras los barrotes de Eren | 1920×1080 | Levi tras los barrotes: vigilar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/6/61/Levi_takes_responsibility_for_Eren.png/revision/latest?cb=20201202020850) |
| P·16 | Levi escucha | 1920×1080 | Levi escucha: pensar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/1/17/Levi_listens.png/revision/latest?cb=20190415231536) |
| P·17 | Levi saluda por última vez | 1920×1080 | saludo final (T4): despedir | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/d/d5/Levi%27s_final_salute.png/revision/latest?cb=20231108143915) |
| P·18 | Levi y Erwin hacen un trato | 1920×1080 | Levi y Erwin, trato en penumbra | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/b/ba/Levi_and_Erwin_make_a_deal.png/revision/latest?cb=20240126005619) |
| P·19 | Levi sonríe (rarísimo) | 1920×1080 | Levi sonríe (casi nunca): celebrar, con cuidado | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/1/11/Levi_smiles.png/revision/latest?cb=20240221120725) |
| P·20 | Erwin propone en el juicio | 1920×1080 · ep. 14 · 20:03 | Erwin propone al tribunal: **explicar** | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/d/d5/Erwin_explains_his_idea_during_Eren%27s_trial.png/revision/latest?cb=20180721210445) |
| P·21 | Erwin arenga a sus soldados | 1920×1080 | Erwin grita: animar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/1/17/Erwin_rallies_his_soldiers.png/revision/latest?cb=20240223012338) |
| P·22 | Erwin encabeza la carga | 1920×1080 · ep. 53 · 21:51 | la carga: animar a lo grande | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/8/8f/Erwin_leads_the_suicide_charge.png/revision/latest?cb=20240223012541) |
| P·23 | Erwin grita, espada en alto (T3) | 1920×1080 | Erwin con espada: animar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/8/85/Erwin_begins_the_operation_to_retake_Wall_Maria.png/revision/latest?cb=20240222214542) |
| P·24 | Hange, feliz: Eren la escucha | 1920×1080 · ep. 15 · 10:13 | Hange entusiasmada: **explicar** | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/e/e8/Hange_is_excited_at_Eren%27s_interest_in_their_work.png/revision/latest?cb=20170921135955) |
| P·25 | Hange descubre su pasión | 1920×1080 | Hange y los titanes: explicar con pasión | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/5/56/Hange_discovers_a_passion_for_Titans.png/revision/latest?cb=20170825060040) |
| P·26 | Hange enseña la lanza rayo | 1920×1080 | Hange en la pizarra: **explicar** (concepto A, alternativa) | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/e/e5/Hange_shows_off_the_Thunder_Spear.png/revision/latest?cb=20240222231250) |
| P·27 | Sasha come patata (ante Shadis) | 1920×1080 · ep. 3 · 04:40 | Sasha y la patata: el recluta que rompe una norma | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/9/9a/Sasha_eating_a_potato.jpg/revision/latest?cb=20170731074223) |
| P·28 | Nile lee ante el tribunal | 1920×1080 | Nile ante el tribunal: acusar · concepto B | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/d/da/Nile_at_trial.png/revision/latest?cb=20170813191909) |
| P·29 | Mikasa y la bufanda | 1920×1080 | Mikasa y la bufanda: calma | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/6/61/Mikasa_thanks_Eren_for_the_scarf.png/revision/latest?cb=20240127130028) |
| P·30 | Escuadrón Levi a la mesa | 1920×1080 | interior del cuartel (mesa, jarras) | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/c/cf/Squad_Levi_at_the_table.png/revision/latest?cb=20190603115837) |

**`hojas/escenas_01.jpg`** (E·): los sitios de los tres conceptos

| N.º | Qué es | Tamaño · dónde | Para qué | Original |
|---|---|---|---|---|
| E·1 | Sala del tribunal militar | 1920×1080 · ep. 14 | **sitio del concepto B**: la sala entera | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/7/7c/The_Military_Court_Room.png/revision/latest?cb=20170805153516) |
| E·2 | Zackly llega al estrado | 1920×1615 | Zackly en el estrado: sentencia | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/3/3a/Premier_Zachary_arrives_at_the_court.png/revision/latest?cb=20170826213147) |
| E·3 | Zackly arriba; Eren al poste abajo | 1920×1080 · ep. 14 | **la composición del concepto B**: juez arriba, acusado abajo | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/1/1a/Zachly_in_the_anime.png/revision/latest?cb=20170824000150) |
| E·4 | Fachada del tribunal militar | 739×800 | fachada gótica del tribunal | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/8/87/The_military_court.png/revision/latest?cb=20130714122840) |
| E·5 | Erwin espera su sentencia (T3) | 1920×1080 | otro juicio (T3): Erwin, sereno | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/2/21/Erwin_awaiting_his_sentence.png/revision/latest?cb=20180819191150) |
| E·6 | A Erwin le quitan los grilletes | 1920×1080 | grilletes: lo que pasa si no se cumple | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/f/fe/Erwin%27s_manacles_are_removed.png/revision/latest?cb=20240131082330) |
| E·7 | Nile y Waltz saludan a Zackly | 1920×1080 | saludo a Zackly, puño al corazón | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/5/5b/Nile_and_Waltz_salute_Premier_Zachary.png/revision/latest?cb=20170826045253) |
| E·8 | Levi en la celda de Eren | 1920×1080 | **muro de piedra con luz de vela** (textura del cuartel) | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/7/72/Levi_in_Eren%27s_cell.png/revision/latest?cb=20240124050516) |
| E·9 | Hange y Mike escoltan a Eren | 1920×1080 · ep. 14 | Hange y Mike: personajes de apoyo | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/7/7b/Hange_and_Mike_escort_Eren.png/revision/latest?cb=20170805153520) |
| E·10 | Eren con pañuelo de limpiar | 1920×1080 · ep. 15-16 | **ropa de limpiar** (pañuelo, trapo): concepto A | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/5/51/Levi_Squad_in_the_middle_of_shenanigans.png/revision/latest?cb=20240130070608) |
| E·11 | Los 3 emblemas tallados en piedra | 1920×1080 | **emblemas en relieve de piedra** (estela, escudo) | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/8/86/Military.png/revision/latest?cb=20170823064044) |
| E·12 | Revisión del equipo: hoja en la mesa | 1378×1614 | **una hoja de papel sobre la mesa**: objeto real | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/e/e2/ODM_gear_inspection.png/revision/latest?cb=20190504225713) |
| E·13 | Reclutas oyen a Erwin, de noche | 1920×1080 · ep. 16 · 08:59 | noche azul del ep. 16: concepto C | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/1/1d/Recruits_listen_to_Erwin%27s_speech.png/revision/latest?cb=20240223011703) |
| E·14 | Los nuevos de la Legión | 1920×1080 · ep. 16 · 14:13 | **el saludo nocturno con antorchas**: concepto C | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/6/6c/New_Survey_Corps_members.png/revision/latest?cb=20240124092804) |
| E·15 | Erwin, antorchas y soldados (T3) | 1920×1080 | antorchas y soldados: luz | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/2/2f/Erwin_briefs_the_scouts_on_their_mission.jpg/revision/latest?cb=20170415044353) |
| E·16 | Erwin se prepara para salir | 1920×1080 | Erwin de perfil, de noche | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/d/d4/Erwin_prepares_to_lead_the_Scouts.png/revision/latest?cb=20240131083557) |
| E·17 | La Legión saluda a Levi | 1920×1080 | saludo colectivo a Levi | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/e/ec/Scout_Regiment_salutes_to_Levi_for_one_final_time.png/revision/latest?cb=20240225231348) |
| E·18 | Petra regaña a Oluo (cuartel) | 1920×1080 | cuartel: piedra y ventana | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/6/68/Petra_scolds_Oluo.png/revision/latest?cb=20240124092415) |
| E·19 | Castillo de Utgard | 1242×1080 | castillo en ruinas, luna | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/3/39/Utgard_Castle_in_the_anime.jpg/revision/latest?cb=20170415223014) |
| E·20 | Utgard de noche, con antorcha | 1896×1319 | antorcha en primer plano: profundidad | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/c/cc/The_scouts_spot_Utgard_Castle.jpg/revision/latest?cb=20170826195705) |
| E·21 | La Legión llega a la Muralla | 1918×2114 | la Muralla: escala | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/2/2e/The_Scouts_arrive.png/revision/latest?cb=20170826001936) |
| E·22 | Cadetes con cañones en la Muralla | 1920×1080 | cañones sobre la Muralla | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/f/f2/109_cadet_corps.png/revision/latest?cb=20211215002828) |
| E·23 | Trost desde el aire | 1920×1080 | Trost: tejados rojos | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/c/ca/Trost_anime.png/revision/latest?cb=20170821022042) |
| E·24 | Stohess: tejados y cúpula | 1920×1080 | Stohess: cúpula y tejados | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/f/f6/Stohess_anime.png/revision/latest?cb=20170804041210) |
| E·25 | Las murallas desde arriba | 1920×1080 | el mapa de murallas desde el cielo | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/7/77/Walls.png/revision/latest?cb=20170802115322) |
| E·26 | La Legión sale de Trost | 1063×621 | la Legión sale: carros y capas | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/e/e4/The_Scout_Regiment_leaves_Trost_District.png/revision/latest?cb=20160619070944) |
| E·27 | Salón con alfombra roja | 1920×1080 | salón oficial con alfombra roja | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/1/10/The_government_is_overthrown.png/revision/latest?cb=20201202021121) |
| E·28 | Mesa de los mandos militares | 1920×1080 | mesa de mandos (sala de reunión) | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/1/1c/The_military_convenes_over_Grisha%27s_journals.png/revision/latest?cb=20240223053235) |
| E·29 | Siluetas al atardecer (T4) | 2880×1610 | siluetas al atardecer: final | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/4/4d/Eren_and_the_Jaegerists_rendezvous.png/revision/latest?cb=20210303030338) |
| E·30 | Trost vitorea a la Legión | 1920×1080 | el pueblo vitorea: celebrar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/6/6a/Trost%27s_citizens_cheer_for_the_Scouts.png/revision/latest?cb=20190724202409) |

**`hojas/fichas_01.jpg`** (F·): cómo «habla» la serie en pantalla, emblemas y letras

| N.º | Qué es | Tamaño · dónde | Para qué | Original |
|---|---|---|---|---|
| F·1 | Ficha clara, cinta roja #5D0003 | 1920×1080 · ep. 1 | **el cuadro de diálogo**: papel claro, cinta arriba a la derecha | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/8/8a/ACPAI1B.png/revision/latest?cb=20141105215243) |
| F·2 | Ficha oscura, cinta roja | 1920×1080 · ep. 1 | versión oscura: cinta arriba a la izquierda | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/c/c5/ACPAI1A.png/revision/latest?cb=20170512214234) |
| F·3 | Tribunal: ficha oscura, verde | 1920×1080 · ep. 14 | tribunal, versión oscura | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/b/b7/ACPAI14A.png/revision/latest?cb=20170514225839) |
| F·4 | Tribunal: GUILTY/NOT GUILTY | 1920×1080 · ep. 14 | **tribunal: balanza, mazo, cadenas** · concepto B | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/0/01/ACPAI14B.png/revision/latest?cb=20170514225924) |
| F·5 | Culto de la Muralla, ocre | 1920×1080 · ep. 15 | culto: siluetas en negro | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/7/7a/ACPAI15A.png/revision/latest?cb=20170514230031) |
| F·6 | Culto: siluetas y emblemas | 1920×1080 · ep. 15 | emblemas de las 3 murallas | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/6/67/ACPAI15B.png/revision/latest?cb=20170514230114) |
| F·7 | Elegir cuerpo: 3 emblemas | 1920×1080 · ep. 16 | **elegir cuerpo** · concepto C | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/a/ae/ACPAI16A.png/revision/latest?cb=20170514230308) |
| F·8 | Elegir cuerpo: siluetas | 1920×1080 · ep. 16 | siluetas en fila | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/f/f6/ACPAI16B.png/revision/latest?cb=20170514230356) |
| F·9 | Documento con orla, oscuro | 1920×1080 · ep. 25 | **documento con orla**: formato de reglamento | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/4/4b/ACPAI25A.png/revision/latest?cb=20170514232201) |
| F·10 | Documento con orla, claro | 1920×1080 · ep. 25 | **documento con orla, claro** · concepto A | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/c/ce/ACPAI25B.png/revision/latest?cb=20170514232240) |
| F·11 | Bengalas BLACK/GREEN/RED | 1920×1080 · ep. 19 | rótulos BLACK/GREEN/RED en letra de plantilla | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/b/b6/ACPAI19B.png/revision/latest?cb=20170514230955) |
| F·12 | Los 10 mejores cadetes | 1920×1080 · ep. 4 | ranking con nombres: lista | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/2/2a/ACPAI4B.png/revision/latest?cb=20170512222413) |
| F·13 | Cadenas y emblema, verde | 1920×1080 · ep. 23 | cadenas y unicornio | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/5/59/ACPAI23A.png/revision/latest?cb=20170514231814) |
| F·14 | Cinta magenta | 1920×1080 · ep. 6 | cinta magenta | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/d/da/ACPAI6B.png/revision/latest?cb=20170514024111) |
| F·15 | Cinta azul | 1920×1080 · ep. 5 | cinta azul | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/d/d8/ACPAI5A.png/revision/latest?cb=20170512223759) |
| F·16 | Cinta violeta | 1920×1080 · ep. 10 | cinta violeta | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/4/4f/ACPAI10B.png/revision/latest?cb=20170514224801) |
| F·17 | Cinta vino | 1920×1080 · ep. 22 | cinta vino | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/6/6f/ACPAI22B.png/revision/latest?cb=20170514231727) |
| F·18 | Especial 13.5: mapa sepia | 1920×1080 · ep. 13.5 | papel sepia con fotos y notas | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/4/4a/ACPAI13.5B.png/revision/latest?cb=20231203143339) |
| F·19 | Emblema: Alas de la Libertad | 709×950 | emblema de la Legión (azul `#162873` y blanco) | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/a/a7/Survey_Corps_Logo.png/revision/latest?cb=20140307090257) |
| F·20 | Emblema: Policía Militar | 777×919 | emblema de la Policía Militar | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/4/4c/Brigade_Logo.png/revision/latest?cb=20140307090257) |
| F·21 | Emblema: Guarnición | 724×916 | emblema de la Guarnición | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/5/55/Garrison_Logo.png/revision/latest?cb=20140307090257) |
| F·22 | Emblema: cadetes 104 | 936×1172 | emblema de los cadetes (espadas cruzadas) | [enlace](https://static.wikia.nocookie.net/shingekinokyojin/images/a/a9/104th_Trainees_Squad_Logo.png/revision/latest?cb=20160506144854) |
| F·23 | OP: alas talladas en piedra | 320×180 · OP2 · 0:00 | alas talladas en piedra verde oscura | [enlace](https://www.youtube.com/watch?v=43spp3kzGVw&t=0) |
| F·24 | OP: logo sobre ladrillo blanco | 320×180 · OP2 · 1:26 | logo sobre ladrillo blanco | [enlace](https://www.youtube.com/watch?v=43spp3kzGVw&t=86) |
| F·25 | Tráiler latino: créditos serif | 320×180 · 0:00 | créditos latinos en serif espaciada | [enlace](https://www.youtube.com/watch?v=sFuAhHTgABs&t=0) |
| F·26 | «MÚSICA…» dorado espaciado | 320×180 · 0:26 | serif dorada apagada sobre textura | [enlace](https://www.youtube.com/watch?v=sFuAhHTgABs&t=26) |
| F·27 | Logo FINAL SEASON | 320×180 · 1:10 | logo occidental de la temporada final | [enlace](https://www.youtube.com/watch?v=sFuAhHTgABs&t=70) |
| F·28 | Rótulo de nombre: Erwin | 320×180 · 3:01 | rótulo de nombre en mincho blanco | [enlace](https://www.youtube.com/watch?v=O3mniZNjeqU&t=181) |

**Las más útiles, en corto:** P·10 y E·10 (Levi y Eren con ropa de limpiar), P·4 y E·14 (el saludo), E·3 y F·4 (el tribunal: composición y ficha), F·9-10 (el documento con orla para las normas), F·1 (la ficha clara).

### 2.1 · Arte oficial nuevo (2023-2026)

| Pieza | Quién sale y cómo | Para qué sirve | Fuente |
|---|---|---|---|
| **Visual de los 15 años de MAPPA** (17-jun-2026; lo **miré**, 1754×2481) | Mikasa **de espaldas** sube el camino de tierra hacia el árbol de la colina, entre lupinos y margaritas, a contraluz de una tarde dorada. Pelo recogido en coleta, bufanda, capa malva y falda gris; pétalos al viento. **No se le ve la cara** (antes ponía «sonriendo»). Dibujo de Tomohiro Kishi, *layout* de Yuichiro Hayashi | celebrar, calma, final feliz · [imagen](https://static.animecorner.me/2026/06/1781686842-a154e001e82b5b0b09f3bf0eaffc3d2f.jpg) | [Anime Corner](https://animecorner.me/attack-on-titan-final-season-gets-new-key-visual-featuring-mikasa-for-mappa-15th-anniversary/) · [PDF de MAPPA](https://www.mappa.co.jp/15th/wp/wp-content/uploads/2026/06/%E3%80%9015th%E3%80%91KV%E2%91%A1%E3%83%AA%E3%83%AA%E3%83%BC%E3%82%B9-EN-F-2.pdf) · [anmosugoi](https://anmosugoi.com/en/mappa-15-anniversary-attack-on-titan-season-final-visual-2026/) |
| **Visual de *Attack on Titan 3*** (9-sep-2026; lo **miré** en el portal oficial, 1500×2121, hoja P·3) | **Eren grande detrás, de perfil** (pelo largo, ojo verde encendido; antes ponía «de espaldas»). Delante, **Levi vendado de la temporada final**, agachado, con una lanza rayo; **Mikasa** en el centro, bufanda roja y hoja en alto; **Armin** a la derecha. Detrás, las costillas del Titán Fundador y plumas blancas. Dibujo de Arifumi Imai, supervisión de Manabu Akita (MAPPA) | presentar al grupo; **no** sirve para Levi de T1-T3 | [imagen en el portal](https://aot-portal.com/wp/wp-content/uploads/2026/09/No.68_%E3%80%90SGK%E3%80%91%E3%82%B2%E3%83%BC%E3%83%A0%E3%83%93%E3%82%B8%E3%83%A5%E3%82%A2%E3%83%AB%E7%89%88%E6%A8%A9_%E7%B4%8D%E5%93%81_RBG-1.jpg) · [Gematsu](https://www.gematsu.com/2026/09/attack-on-titan-3-opening-animation-key-visual-revealed) · [4Gamer (JA)](https://www.4gamer.net/games/013/G101375/20260909005/) |
| **Día de Attack on Titan** (9-sep-2026) | El **visual oficial reúne a los nueve titanes** y el logo «ATTACK ON TITAN DAY» se inspira en el Titán del Retumbar (web oficial). El [vídeo oficial](https://www.youtube.com/watch?v=WAn2W-WFamc) (0:44) es una **cuenta atrás del 1 al 9** con un titán por número y termina en el logo rojo sobre piedra gris ([0:38](https://www.youtube.com/watch?v=WAn2W-WFamc&t=38)). El visual (lo miré, [1920×1730](https://aot-portal.com/wp/wp-content/uploads/2026/09/SN_No.2_%E3%83%93%E3%82%B8%E3%83%A5%E3%82%A2%E3%83%AB%EF%BC%86%E3%83%AD%E3%82%B4%E7%94%BB%E5%83%8F.webp)) es un «9/9» gigante relleno de viñetas del manga, sobre negro, con el logo en blanco y rojo. **El dibujo de agradecimiento de Isayama** (lo miré en el portal, [1920×1729](https://aot-portal.com/wp/wp-content/uploads/2026/09/SN_No.3_%E9%80%B2%E6%92%83%E3%81%AE%E5%B7%A8%E4%BA%BA%E3%81%AE%E6%97%A5-%E3%81%8A%E7%A5%9D%E3%81%84%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%EF%BC%8F%E3%83%9D%E3%83%BC%E3%82%BF%E3%83%AB%E7%94%A8.webp)): a tinta, **Eren adulto** (pelo largo, ojos abiertos, puño en alto) detrás, y **Levi delante, de brazos cruzados, ceño fruncido**, con la chaqueta de T1-T3 y las alas en el bolsillo. Además, en la tienda de la *Shonen Magazine*, **Eren, Erwin y Levi con traje de tres piezas**, dibujo de Isayama, en **marcos dorados con cinta del nombre** sobre rojo, morado y verde ([2480×2234](https://aot-portal.com/wp/wp-content/uploads/2026/09/No.4_%E3%83%9E%E3%82%AC%E3%82%B8%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%97-1.jpg)) | celebrar; **Levi de brazos cruzados por el autor (2026)**: presentar o regañar | [Portal oficial](https://aot-portal.com/en/special/aotday2026/) · [Anime Corner](https://animecorner.me/attack-on-titan-day-celebrated-with-99-announcements-new-key-visual-video-hajime-isayama-art-youtube-channel-and-more/) |
| **Carteles nuevos del portal** (sep-2026) | Película recopilatoria 1 en ScreenX/4DX (**23-oct-2026**), *THE LAST ATTACK* en ScreenX (2027) y el concierto sinfónico *Symphony from Paradis* (Eren, Mikasa y Armin sobre la Muralla, con la bandera verde de la Legión) | fondos; bandera | [cartel 1](https://aot-portal.com/wp/wp-content/uploads/2026/09/No.10_aot_GY_V.jpg) (1459×2062) · [cartel 2](https://aot-portal.com/wp/wp-content/uploads/2026/09/No.11_aot_LA_V.jpg) (1459×2062) · [concierto](https://aot-portal.com/wp/wp-content/uploads/2026/09/No.14_20260320_AOT2_Web-illustration-originale-sans-aucune-modif-1080-x-1080.jpg) (1080×1080) |
| **Película *THE LAST ATTACK*** (sep-2024) | Los titanes del Retumbar y, enfrente, la Legión y los guerreros | escala, drama | [eiga.com (JA)](https://eiga.com/news/20240915/9/) |
| **Temporada final, completa (2023)** | Eren como Titán Fundador; alrededor, Mikasa, Armin, Connie, Jean, Levi y Reiner con el equipo de maniobras | acción en grupo | [animatetimes (JA)](https://www.animatetimes.com/news/details.php?id=1684649921) · [X oficial](https://x.com/anime_shingeki/status/1660208659253821445) · [Lisani](https://www.lisani.jp/0000215296/2211141800-yh-001/) |
| **Cuenta atrás** de la temporada final (2023) | Un dibujo nuevo por día en X | poses variadas | [collabo-cafe (JA)](https://collabo-cafe.com/events/collabo/shingeki-anime-the-final-season-finale2023-illust-countdown-matome/) |
| **Portada del número de los 15 años** de «Shingeki no Kyojin Magazine» | Dibujo nuevo de Isayama | estilo del autor | [Natalie (JA)](https://natalie.mu/comic/news/594324) |
| **Portada de la 2.ª encuesta** (2015) | Isayama dibujó a los tres primeros: **Levi, Erwin y Eren** | celebrar con Levi | [ANN](https://www.animenewsnetwork.com/interest/2015-04-07/levi-erwin-eren-top-attack-on-titan-popularity-poll/.86828) |
| **Visual de la temporada 1** | galería de Natalie | estilo WIT | [Natalie (JA)](https://natalie.mu/comic/gallery/news/507886/1973357) |
| **Artbook oficial *浅野恭司 進撃の巨人 総作監修正集*** (WIT STUDIO, 29-sep-2017; B5, 144 págs., a color) | Las correcciones de **Kyoji Asano** (diseño de personajes y jefe de animación) de la T1 y la T2, **ordenadas por personaje**, con sus comentarios, dibujos promocionales y la competición de diseños. Portada: Eren, dibujado para el libro. **No lo pude hojear**: lo cito por la ficha oficial | el sitio donde está **cómo se dibuja cada cara** según su diseñador; comprarlo si hace falta afinar a Levi | [shingeki.tv](https://shingeki.tv/news/archives/3364) · [ABEMA Times (JA), entrevista a Asano, 2024](https://times.abema.tv/articles/-/10128463) |

### Copias en alta que sí pude abrir (alojadas en GitHub por un fan)

Están en [khalil-hamidani/SNK](https://github.com/khalil-hamidani/SNK), una web
de fans. **Son arte de la serie; el copyright es de sus dueños.** Sirven sólo de
referencia y para medir color. Las miré una por una.

| N.º | Archivo | Tamaño | Qué es (lo que se ve) |
|---|---|---|---|
| G1 | [`img/art/1.jpg`](https://raw.githubusercontent.com/khalil-hamidani/SNK/main/img/art/1.jpg) | 3840×2160 | **Ilustración oficial escaneada.** La 104.ª promoción (Eren en el centro, Mikasa, Armin, Jean, Marco, Connie, Annie) **hace el saludo**: puño derecho al corazón. Lleva la chaqueta de reclutas con las espadas cruzadas. Detrás, la **bandera de la Legión, verde y rota**, y un cielo azul con nubes. |
| G2 | [`img/art/4.jpg`](https://raw.githubusercontent.com/khalil-hamidani/SNK/main/img/art/4.jpg) | 2160×1920 | **Levi y Eren**, con capa verde y fondo blanco. Levi coge la hoja **al revés**, con la punta hacia abajo, y tiene la mirada de párpado caído. Eren levanta la hoja y aprieta los dientes. |
| G3 | [`img/humans/levi.jpg`](https://raw.githubusercontent.com/khalil-hamidani/SNK/main/img/humans/levi.jpg) | 960×540 | Fotograma de la **temporada final**. Levi, de noche, con cuello alto negro y capa verde, sujeta el mango del equipo; se ve un destello en el cable. Tiene el ceño fruncido. |
| G4 | [`img/humans/eren.jpg`](https://raw.githubusercontent.com/khalil-hamidani/SNK/main/img/humans/eren.jpg) | 1280×720 | Eren de la temporada final: pelo largo recogido, a contraluz de una ventana con cortinas. Levanta la mano herida. |
| G5 | [`img/humans/mikasa.jpg`](https://raw.githubusercontent.com/khalil-hamidani/SNK/main/img/humans/mikasa.jpg) | 1024×1024 | Mikasa (WIT) en interior, con luz tenue, la bufanda y la mirada seria. |
| G6 | [`img/humans/armin.jpg`](https://raw.githubusercontent.com/khalil-hamidani/SNK/main/img/humans/armin.jpg) | 728×455 | Armin (T1), con tejados y humo detrás. |
| G7 | [`img/art/2.jpg`](https://raw.githubusercontent.com/khalil-hamidani/SNK/main/img/art/2.jpg) | 1600×925 | El **Acorazado** sobre la Muralla y Mikasa volando delante. La ciudad arde al atardecer. **Origen sin verificar.** |
| G8 | [`img/art/3.jpg`](https://raw.githubusercontent.com/khalil-hamidani/SNK/main/img/art/3.jpg) | 4500×2500 | El Acorazado contra el Titán de Eren, con soldados volando. Parece arte de videojuego. **Origen sin verificar.** |
| G9 | [`img/732017.jpg`](https://raw.githubusercontent.com/khalil-hamidani/SNK/main/img/732017.jpg) | 6217×3713 | El Titán Colosal en 3D entre humo rojo. Es un fondo de pantalla. **Origen sin verificar.** |

---

## 3 · Escenas icónicas (con su capítulo y minuto)

**De dónde salen los minutos (2.ª pasada).** De los **subtítulos japoneses de
Netflix** ([espejo de kitsunekko][kitsu]), que marcan quién habla. En Crunchyroll
el minuto puede moverse unos segundos. Las imágenes de cada escena están en las
hojas (P·, E·, F·; ver §2.0). Las frases de esta tabla son **traducción nuestra
del japonés**; las del doblaje latino, textuales, están en §9.3.

| Escena | Capítulo · minuto | Qué pasa (con la frase) | Hojas y fuentes |
|---|---|---|---|
| **Shadis recibe a los reclutas** | **ep. 3 · 01:39-05:01** | 01:39 «¡Eh, tú! ¿Quién demonios eres?». 02:18 «¡Vienes de una pocilga: eres menos que el ganado!». **03:53-04:03: Connie saluda con la mano izquierda** y Shadis le pregunta si tiene el corazón a la derecha (el saludo es «entregar el corazón»). 04:40 Sasha y la patata. | P·8, P·27 · [Fandom: Keith Shadis](https://attackontitan.fandom.com/wiki/Keith_Shadis) |
| **El juicio de Eren** | **ep. 14 · 10:29-21:50** | 10:29 Zackly: «Daremos inicio». 11:38 Nile propone. 12:32 Erwin propone. **13:50 Levi contra los mercaderes** («¿quién garantiza que los titanes esperarán?»). **18:33 la patada**; 18:54 «Creo que lo que mejor educa es el dolor». 20:03 la propuesta de Erwin: Eren, bajo la custodia de Levi. 20:41 Levi: «Para matarlo, sin duda». 21:50 «No lo recojas, qué asco» (el diente). | E·1, E·2, E·3, P·12, P·20, F·3-4 · [Fandom, ep. 14](https://attackontitan.fandom.com/wiki/Can%27t_Look_into_His_Eyes_Yet:_Eve_of_the_Counterattack,_Part_1) (antes enlazaba al capítulo 19 del manga) · [TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Recap/AttackOnTitanS1E14CantLookIntoHisEyesYet) |
| **Levi manda limpiar el castillo** | **ep. 15 · 04:55-07:15** | 04:55 «Dentro estará todo lleno de polvo». **04:57 Levi: «Eso es un problema grave. Empecemos ya»**. 05:39 Levi a Eren, que dormirá en el sótano: «**Es una regla que hay que cumplir**». 06:02 Petra: «**Aquí la regla es el capitán**». 06:17-06:22 Petra lo describe: bajo, maniático, brusco, difícil de tratar. **07:10-07:15 Levi: «Esto no vale nada. Hazlo todo otra vez»**. | P·10, P·11, E·10 · [Fandom, ep. 15](https://attackontitan.fandom.com/wiki/Special_Operations_Squad:_Eve_of_the_Counterattack,_Part_2) · [Know Your Meme](https://knowyourmeme.com/memes/cleaning-levi) · clip de fan, doblaje inglés, mirado por *storyboard*: el clip empieza en el ep. 04:45 ([Levi se baja el pañuelo, 0:32](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=32); [«hazlo todo otra vez», 2:24](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=144)) |
| Hange entra en escena | ep. 14 · 08:23-08:37 y ep. 15 · 10:01-15:25 | Se presenta a Eren (ep. 14). En el ep. 15 pide permiso para «el experimento» y a las 14:16-14:38 cuenta cómo bautizó a sus titanes, **Sonny y Bean**. | P·24 |
| **Erwin recluta de noche** | **ep. 16 · 08:59-14:57** | 08:59 «Soy el comandante de la Legión, Erwin Smith». 11:19 «En esos cuatro años murió más del 60 %». 12:05 «…si pueden entregar su corazón». **13:52 «¿Morirían si se lo ordeno?»**. **14:08-14:13 la bienvenida, «este es un saludo de verdad» y «¡Consagren sus corazones!»**. 14:57 Jean: «¡Saluden!». | P·4, E·13, E·14, F·7 · [Fandom, ep. 16](https://attackontitan.fandom.com/wiki/What_Needs_to_be_Done_Now:_Eve_of_the_Counterattack,_Part_3) |
| **Levi y el soldado que muere** | **ep. 9 · 06:01-07:08** | 06:01-06:04 Levi mata a un titán y mira su mano: «Tch… qué asco» (汚ねえなあ). 06:34 el soldado le pregunta si fue útil. 06:51 «Hiciste suficiente, y lo seguirás haciendo». **06:57-07:04 «Tu determinación me dará fuerza. Eso te lo prometo»** (así en el doblaje latino, §9.3). 07:05 «Exterminaré a los titanes». | subtítulos de Netflix del ep. 9 |
| **«Elige lo que no te deje arrepentimiento»** | **ep. 19 · 06:23-06:49** (antes «capítulo sin verificar») | En el bosque, Levi a Eren: «Elige: confiar en ti, o en nosotros… Elige tú lo que no te deje arrepentimiento». | P·14 · [Fandom, ep. 19](https://attackontitan.fandom.com/wiki/Bite:_The_57th_Exterior_Scouting_Mission,_Part_3) |
| Erwin pierde el brazo | **ep. 36 · 14:39-16:21** («Charge», T2) | 14:39 «¡Todos, a la carga!». 15:00 «¡Consagren sus corazones!». 16:05-16:21 un titán le atrapa el brazo derecho y él sigue gritando «¡Avancen! ¡Eren está ahí!». | [Fandom, ep. 36](https://attackontitan.fandom.com/wiki/Charge_(Episode)) |
| **«Abandona tu sueño y muere»** | **ep. 53 · 18:00-18:06** («Perfect Game», T3) | Levi, de rodillas ante Erwin: «Renuncia a tu sueño y muere». Y: «Al Titán Bestia lo mato yo». | [Fandom](https://attackontitan.fandom.com/wiki/Perfect_Game_(Episode)) · [substack iuniaaa](https://iuniaaa.substack.com/p/levi-and-erwin) |
| **«¡Soldados, rujan!»** | **ep. 53 · 21:51-21:55** | «¡Soldados, rujan! ¡Soldados, griten! ¡Soldados, luchen!». La carga suicida. | P·22 · [Know Your Meme](https://knowyourmeme.com/memes/erwin-smiths-my-soldiers-rage-speech) |
| Levi contra la Bestia | ep. 53-54 («Hero») | La carga de Erwin le da tiempo a Levi. | [Fandom «Hero»](https://attackontitan.fandom.com/wiki/Hero_(Episode)) · [IMDb](https://www.imdb.com/title/tt9906260/) |
| **La bomba de Zackly y el grito de la verja** | **ep. 71 · 11:47-12:57** (T4, «Guides») | 11:47 estalla el despacho del generalísimo Zackly (13:01: la bomba iba en su silla). 12:31-12:57 la gente en la verja del cuartel grita «¡Consagren sus corazones!» con el puño en alto. Es **el clip doblado de Crunchyroll**: lo miré por su *storyboard* (clip [0:02-0:08](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=2) la explosión; [0:48-0:58](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=48) los puños en alto). | [clip][yt-consagren] · subtítulos de Netflix del ep. 71 |
| Los reclutas apalean a Keith | **ep. 73 · 16:10-19:13** (T4) | Keith manda el simulacro de defensa (16:25); los reclutas juran «por el futuro de Eldia» y le pegan. **No es el clip de Crunchyroll** (antes se dijo que sí). | subtítulos de Netflix del ep. 73 |
| Levi contra Zeke, doblado | **ep. 73** (T4) | «En ese momento, Zeke sintió el verdadero terror»: los soldados convertidos en titanes, el recuerdo del béisbol y Levi cayendo sobre Zeke (clip [0:56-1:00](https://www.youtube.com/watch?v=wOzu2yF4HC4&t=56)); al final, Levi en el aire con la capa ([1:08](https://www.youtube.com/watch?v=wOzu2yF4HC4&t=68)). La descripción oficial acredita a **Gabriel Basurto (Levi)** y Ricardo Brust (Zeke). | [clip][yt-zeke] |

---

## 4 · Fan art y 3D (lo que hay y lo que no)

### 4.1 Modelos 3D (Sketchfab): licencia comprobada por su API ✅

Todos **CC BY** (hay que dar crédito exacto si se usan) y descargables, según
`api.sketchfab.com/v3/models/<uid>` (24-sep-2026). Los de la serie son **fan
art en 3D**: sirven de referencia de forma; para la lámina, mejor los objetos
genéricos.

| Modelo | Autor (crédito) | Caras | Para qué | Enlace |
|---|---|---|---|---|
| ODM Gear | Tipperman | 26 094 | equipo de maniobras | [47a69e56…](https://sketchfab.com/3d-models/47a69e5640c34e42b1cf56ceff7fb5d4) |
| SNK 3D Maneuver Gear | marthacuenca | 13 600 | equipo de maniobras | [254eb3c6…](https://sketchfab.com/3d-models/254eb3c63c874cad9772ca45460f84c7) |
| ODM Gear / 3DMG | ynerva | 45 005 | equipo, más detallado | [5583ec0d…](https://sketchfab.com/3d-models/5583ec0d27d1401db69bde8eecfa48d8) |
| Flare Gun - Attack On Titans | Nelesh_surve | 22 672 | pistola de bengalas (F·11) | [b375de9d…](https://sketchfab.com/3d-models/b375de9d451240ca89f6ef7fb1ad145f) |
| Attack On Titan Survey Corps Logo | colleenkewley | 252 444 | el escudo en relieve | [f199e459…](https://sketchfab.com/3d-models/f199e459b5974c73b9227bd5e229e736) |
| wings of freedom | Rhiyan.Rahman | 14 524 | las alas | [ccee8360…](https://sketchfab.com/3d-models/ccee8360acf046be9752085c755336aa) |
| Attack on Titan Jacket | Tyriese Miller | 564 800 | la chaqueta (pesado) | [0e002a35…](https://sketchfab.com/3d-models/0e002a354ac143a5845463ba92cb27aa) |
| Levi Ackerman VR/Game Ready | TKSAET | 56 333 | Levi en 3D, sólo para pose | [41ba2beb…](https://sketchfab.com/3d-models/41ba2beb495c423fa576580696994d63) |
| Wall section of Wall Maria | Khaled.Guesmi | 60 | la Muralla (muy simple) | [846677ea…](https://sketchfab.com/3d-models/846677eaaf414ff0ae44c0d96b9f6e98) |
| Trost District | Khaled.Guesmi | 3 508 | la ciudad, de lejos | [64a5f1ee…](https://sketchfab.com/3d-models/64a5f1eed2d442f58a3a08254f56db8d) |
| Attack on Titan Cannon | Skipperino | 32 442 | cañón de la Muralla (E·22) | [7bacac0f…](https://sketchfab.com/3d-models/7bacac0f2c8b443ea6df505efd02fe8c) |
| Colossal Titan | Mauricio Flores | 128 598 | el Colosal | [eea5f373…](https://sketchfab.com/3d-models/eea5f37385084170b46d9e4ca3881f84) |
| **Wooden Bucket** | FlukierJupiter | 712 | **cubo del concepto A** | [68d83e2d…](https://sketchfab.com/3d-models/68d83e2d634940f594df30998aba652c) |
| **Simple Outdoor Brooms Type A** | Mad_Lobster_Workshop | 15 761 | **escoba del concepto A** | [0b049255…](https://sketchfab.com/3d-models/0b049255562349ad8072afb9c33acfea) |
| **Iron Shackles** | George Sims (BookBoy) | 11 676 | **grilletes del concepto B** | [bd481fe4…](https://sketchfab.com/3d-models/bd481fe4f5eb44ad9f9f64786ae7f56f) |
| **Medieval Open Book 1** | J0Y (lloydrostek) | 514 | **libro de actas del concepto B** | [b30b6a90…](https://sketchfab.com/3d-models/b30b6a9018f842e7b12622387979b0fa) |
| Antique old opened book | take_model | 422 | otro libro abierto | [2fc707e6…](https://sketchfab.com/3d-models/2fc707e68e2d490cbb900fb212e04bc5) |
| **Medieval Wall Torch** | Kigha | 1 748 | **antorcha del concepto C** | [77db436d…](https://sketchfab.com/3d-models/77db436da2844cbfb4dde0bb9b396835) |
| Medieval banner | ejtamovic | 2 468 | bandera colgada | [0a87672d…](https://sketchfab.com/3d-models/0a87672db9ef4059ae559d25f199baf2) |
| Wax Seal | A9908244 | 235 426 | sello de lacre | [d485de05…](https://sketchfab.com/3d-models/d485de05a19e424fbf31e3b6022daf0c) |

### 4.2 Texturas (Poly Haven, CC0) ✅ comprobadas por su API

- `sandstone_blocks_08` y `sandstone_blocks_04` (Rob Tuytel, hasta 8K): la
  Muralla y la estela.
- `castle_brick_07` y `rough_plaster_brick` (Rob Tuytel): **el muro del
  cuartel** (E·8 es piedra con luz de vela).
- `old_wood_floor` (Guillaume Monsergent) y `worn_planks` (Dimitrios Savva):
  tablones del tablón y del estrado.
- `wood_table_001` (hasta 16K): la mesa del juez.
- `cobblestone_pavement` (Charlotte Baglioni): el patio del ep. 16.

### 4.3 Fan art con autor (sólo referencia, nunca para pegar)

| Obra | Autor | Dónde | Tamaño |
|---|---|---|---|
| «蒼穹を舞え» (Levi en vuelo) | ちぇりん | [Pixiv 149961259](https://www.pixiv.net/artworks/149961259) | 3072×4096 |
| «エルリ2026 SNK Day» (Erwin y Levi, Día de AoT) | SparkleTeaCup | [Pixiv 149472041](https://www.pixiv.net/artworks/149472041) | 1000×705 |
| «Commander Erwin Smith and Lance Corporal Levi Ackerman» | Simi Braun | [ArtStation](https://www.artstation.com/artwork/w1BAO) | — |
| «Humanity’s Strongest Soldier» | SketchSouza | [ArtStation](https://www.artstation.com/artwork/y4yZ3n) | — |
| «Survey Corps Badge Wallpaper» | Boblester122 | [DeviantArt](https://www.deviantart.com/boblester122/art/Shingeki-no-Kyojin-%3A-Survey-Corps-Badge-Wallpaper-406162731) | 1125×710 (vista previa) |
| «Attack on Titan Survey Corp Wallpaper» | Fiveby5Studios | [DeviantArt](https://www.deviantart.com/fiveby5studios/art/Attack-on-Titan-Survey-Corp-Wallpaper-467000721) | 1024×576 |
| Hange (fan art muy votado en Reddit: 1311) | レースの縁取り | [Reddit](https://www.reddit.com/r/ShingekiNoKyojin/comments/pm8qc6/) | — |

Pixiv tiene **6861 obras** con la etiqueta リヴァイ兵長 («capitán Levi»), a
24-sep-2026 (su búsqueda pública). Los tamaños de Pixiv salen de esa búsqueda;
los de DeviantArt, de su oEmbed.

### 4.4 Código (de la primera pasada; sigue valiendo)

- [UE5_Three-Dimensional-Maneuver-Gear](https://github.com/Dolaxom/UE5_Three-Dimensional-Maneuver-Gear),
  [the-tall-wall-falls](https://github.com/iamrequest/the-tall-wall-falls),
  [AoT_FanGame](https://github.com/Symon799/AoT_FanGame), [RCMod](https://github.com/rc174945/RCMod)
  y [guardian-aottg](https://github.com/winnpixie/guardian-aottg): mecánica, no
  modelos (ninguno dice su licencia).
- Hispano: [snk-bot](https://github.com/lvillegas6/snk-bot) (bot de Discord)
  dice «Cuerpo de Exploración». **El doblaje dice «Legión de Exploración»** (§9.3).

---

## 5 · Sitios, luz y paleta (hex **medidos**)

Medí con Pillow en las imágenes G1 a G9. Saqué la mediana de los píxeles del
tono que toca, en tres tramos: sombra, medio y luz. Margen: ±5 por canal.

| Qué | Sombra | Medio | Luz | Medido en |
|---|---|---|---|---|
| Capa verde de la Legión (T1-T3) | `#182018` | `#1E261F` | `#3C4E3A` | G2 |
| Bandera verde bajo el cielo | `#13201A` | `#1F342E` | `#446C59` | G1 |
| Capa verde, temporada final, de noche | `#1B1D16` | `#33382B` | `#4A5039` | G3 |
| Chaqueta marrón claro (arte limpio) | `#887054` | `#A1865D` | `#BFA97B` | G2 |
| Chaqueta, en el escaneo | `#342214` | `#523F2C` | `#A07E57` | G1 |
| Cielo de día | `#5380A6` | `#74A9CD` | `#A1CDE5` | G1 |
| Noche de la temporada final | `#161B30` | `#202743` | `#2A3857` | G3 |
| Bufanda de Mikasa (granate, a la luz del día) | `#1A0E0D` | `#2D1919` | `#743D41` | G1 |
| Bufanda en interior con luz tenue | `#43231B` | `#4F2A20` | `#532D23` | G5 |
| Pelo de Armin | `#896E01` | `#967703` | `#968051` | G6 |
| Piel a contraluz (Eren, temporada final) | `#876747` | `#B08E6A` | `#CBB294` | G4 |
| Fuego y atardecer sobre la ciudad | `#8E5833` | `#AA6C44` | `#D29258` | G7 |
| Músculo y humo del Colosal | `#420F04` | `#5B2A19` | `#A4482E` | G9 |
| **Ficha «Información pública»**, ep. 1 (primera medida) | papel `#F4EEEF` → **`#F3F3F3`** al medirla entera | cinta `#5C0001` (sólo la del ep. 1) | — | guía de cuadros; F·1 |

**Medido en la 2.ª pasada, en fotogramas 1080p de la wiki** (Pillow: paleta de
7 colores por *median cut*, o mediana por tramos del tono que toca; ±5):

| Qué | Colores (de oscuro a claro) | Medido en |
|---|---|---|
| **Sala del tribunal** (ep. 14): gris verdoso frío | `#21231F` · `#2B3737` · `#455B5E` · `#8CA09F` · `#C8D3D3` | E·1 |
| Tribunal, con Zackly arriba y Eren abajo | `#202021` · `#49524E` · `#75827D` · `#B6BFBA` | E·3 |
| **Celda con vela** (piedra y luz naranja) | `#1F150D` · `#502F1B` · `#6E4126` · `#99653D` | E·8 |
| **Patio de noche con antorchas** (ep. 16): chaquetas a la luz del fuego sobre negro | `#0C0C0E` · `#422716` · `#725036` · `#8D6B45` | E·14 |
| La misma noche, **sin fuego** (luz de luna, fría) | `#101212` · `#29292D` · `#514F57` · `#B9B4B5` · `#CBCDD1` | E·13 |
| **Levi limpiando**: pañuelo, cielo de ventana y piedra | pañuelo `#F1EEE6` · cielo `#D1E6EF` · piedra `#34362A` a `#595845` | P·10 |
| Levi y el polvo (interior del castillo) | `#1D1A19` · `#534A42` · `#88847B` · luz `#EEF3E4` | P·11 |
| Capa verde con niebla (el saludo a Levi) | `#343C2E` · `#465241` · `#58624E` | E·17 |
| Bufanda de Mikasa, en interior | `#1D0F0F` · `#331C1A` · `#552C2D` | P·29 |
| Chaqueta marrón a la luz de antorcha | `#3F2715` · `#654327` · `#8C6C47` | E·14 |
| Salón con alfombra roja | `#5B2B27` · `#71403D` · `#935C59` · paredes `#CDCED2` | E·27 |
| Trost desde el aire (tejados) | `#463C3B` · `#886F5A` · `#A39583` · `#C0C5C8` | E·23 |
| **Ficha «Información pública»** | papel `#F2F2F2` (gris neutro); tinta `#222222`-`#2E2E2E`; cinta **de un color por episodio** (§7) | F·1-17 |
| Emblema de la Legión | azul `#162873` · blanco `#E3E3E5` · escudo gris `#AFADAB` | F·19 |

**El cielo es de autor.** El director de arte de la T1 es **Shunichiro
Yoshihara** (吉原俊一郎; lo acreditan [eiga.com](https://eiga.com/person/196420/)
en las películas y el blog [OTACTURE (JA)](https://ukkah.hatenadiary.org/entry/20131210/p1)
en la serie). OTACTURE habla de las **«nubes Yoshihara»**: nubes altas y
finas, **mucho contraste con el azul** y **nubes que no son de un solo blanco,
sino de varios blancos**. Se ve en G1 (cielo `#74A9CD`-`#A1CDE5`). En la
lámina: si hay cielo, que sea alto, con nubes finas y blancos distintos.

**Lo que se ve al medir:**
- El verde de la Legión **no es verde hierba**. Es un verde oliva frío, casi negro
  en sombra. Bajo cielo abierto se vuelve verde azulado (`#446C59`).
- La bufanda de Mikasa **no es rojo puro**: es granate oscuro.
- La temporada final es más fría y oscura: noche azul (`#202743`) y ropa negra.

**Sitios para las láminas:**

| Sitio | Luz y hora | Episodio | Fuente |
|---|---|---|---|
| El viejo castillo-cuartel de la Legión | interior de piedra, luz blanca de ventana; sótano con vela (P·10-11, E·8, E·10) | ep. 15 · 04:55-07:15 | [Fandom](https://attackontitan.fandom.com/wiki/Special_Operations_Squad:_Eve_of_the_Counterattack,_Part_2) |
| Tribunal militar | interior alto, frío y gris verdoso; el juez arriba, el acusado de rodillas al poste abajo (E·1-4) | ep. 14 · 10:29-21:50 | [Fandom](https://attackontitan.fandom.com/wiki/Can%27t_Look_into_His_Eyes_Yet:_Eve_of_the_Counterattack,_Part_1) · galería de la biblia anterior, n.º 129, 255, 256, 459, 40 y 300 |
| Patio del cuartel, de noche | de noche, antorchas y luna (E·13-14) | ep. 16 · 08:59-14:57 | [Fandom](https://attackontitan.fandom.com/wiki/What_Needs_to_be_Done_Now:_Eve_of_the_Counterattack,_Part_3) |
| Campo de instrucción de los reclutas | exterior de día, cielo azul (P·27) | ep. 3 · 01:39-05:01 | [Fandom: Keith Shadis](https://attackontitan.fandom.com/wiki/Keith_Shadis) |
| Las murallas en círculos: María, Rose y Sina | mapa a tinta de la ficha «Información pública» | T1 | guía de cuadros |

**Texturas reales equivalentes**: piedra arenisca en bloques grandes y ladrillo
de castillo (Poly Haven, comprobadas por su API: §4.2). Para los papeles, papel
verjurado envejecido y madera de roble con clavos de hierro. Para el tribunal,
hierro forjado oxidado.

---

## 6 · Letras (comprobadas letra a letra)

Bajé cada fuente del repositorio `google/fonts` de GitHub, por
`raw.githubusercontent.com` (por ejemplo, la
[ficha de Cinzel](https://raw.githubusercontent.com/google/fonts/main/ofl/cinzel/METADATA.pb)),
y miré su tabla de caracteres con fontTools. **Todas traen á é í ó ú ñ ¿ ¡ y ü.**
En la 2.ª pasada volví a bajar Cinzel, Shippori Mincho B1, Yuji Boku y Stardos
Stencil, y añadí Cormorant SC e IM Fell English SC: las seis, completas.

| Para qué | Letra libre | Licencia | Nota |
|---|---|---|---|
| Texto de la ficha «Información pública» (japonés y español) | **Shippori Mincho B1** ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/shipporiminchob1/METADATA.pb)) | OFL | es el mincho sobrio de la ficha real |
| Título en la cinta de pincel | **Yuji Boku** ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/yujiboku/METADATA.pb)) | OFL | trazo de pincel; en la serie la cinta está pintada |
| Sentencias, actas y edictos del tribunal | **IM Fell English** ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/imfellenglish/METADATA.pb)) / IM Fell DW Pica | OFL | imprenta antigua, con tinta irregular |
| Texto corrido que tiene que leerse | **Cormorant Garamond** | OFL | ya usada en la lámina 1 |
| Inscripción en piedra; créditos en español | **Cinzel** | OFL | ✅ sus minúsculas son **versalitas** (fontTools: la «a» mide 614 de alto y la «A» 714): todo sale en mayúsculas. Es el estilo de los créditos del tráiler latino (F·25-26) |
| Notas a mano (Hange, un recluta) | **Kalam** o **Caveat** | OFL | Kalam parece más de pluma |
| Rótulos de cajas, sellos militares; «CULPABLE / INOCENTE» a lo GUILTY/NOT GUILTY de la ficha del tribunal (F·4) | **Stardos Stencil** | OFL | plantilla con minúsculas de verdad; tildes, ñ, ¿ y ¡ ✅ (2.ª pasada) |
| Versalitas para títulos cortos | **Cormorant SC** · **IM Fell English SC** | OFL | tildes, ñ, ¿ y ¡ ✅ (2.ª pasada) |
| Máquina de escribir | Special Elite | Apache 2.0 | **no pega** con las murallas; sólo para Marley |

- **Lo que vi en pantalla** (2.ª pasada, hojas de fotogramas por *storyboard*,
  ±1 s): los créditos japoneses del tráiler de 2012 van en **mincho blanco
  grueso, centrado, sobre negro**: 原作 諫山創 ([PV · 0:10](https://www.youtube.com/watch?v=KKzmOh4SuBc&t=10)),
  composición y diseño de personajes ([0:20](https://www.youtube.com/watch?v=KKzmOh4SuBc&t=20)),
  voces ([0:30](https://www.youtube.com/watch?v=KKzmOh4SuBc&t=30)) y música
  ([0:34](https://www.youtube.com/watch?v=KKzmOh4SuBc&t=34)); cierra con el
  logo metálico y «2013年春 TVアニメ放送決定!!» ([1:06-1:10](https://www.youtube.com/watch?v=KKzmOh4SuBc&t=66)).
  Los del tráiler latino (Especial 1), en **serif romana de mayúsculas muy
  espaciadas**, con tildes: «BASADO EN EL MANGA DE HAJIME ISAYAMA» blanco sobre
  la ciudad ([0:02](https://www.youtube.com/watch?v=sFuAhHTgABs&t=2)),
  «PRODUCCIÓN MAPPA» ([0:22](https://www.youtube.com/watch?v=sFuAhHTgABs&t=22)),
  «DIRECCIÓN YUICHIRO HAYASHI» ([0:25](https://www.youtube.com/watch?v=sFuAhHTgABs&t=25))
  y «MÚSICA KOHTA YAMAMOTO / HIROYUKI SAWANO» ([0:27](https://www.youtube.com/watch?v=sFuAhHTgABs&t=27)),
  en crema o dorado apagado (`#8C7C6E`) sobre piedra oscura; «VELO EN
  crunchyroll» sobre llamas ([1:20](https://www.youtube.com/watch?v=sFuAhHTgABs&t=80));
  el rótulo de nombre del resumen oficial, en **mincho blanco** con el cargo
  debajo ([3:01](https://www.youtube.com/watch?v=O3mniZNjeqU&t=181), F·28).
- **El logo** está dibujado a mano. Se le parecen Linotext (de pago) y Ditty, de
  FG Studios, gratis sólo para uso personal
  ([betterstudio](https://betterstudio.com/fonts/attack-on-titan-font/) ·
  [foro de dafont](https://www.dafont.com/forum/read/218843/attack-on-titan-font)).
  **No lo imites en las láminas.**
- **La escritura de dentro de las murallas** es katakana al revés (biblia
  anterior, ANN 2014). No hay fuente libre fiable.
- **Manga en inglés**: la rotulación es de Steve Wands y la traducción de Sheldon
  Drzka (Kodansha USA). Viene en la
  [ficha de biblioteca](https://glendale.iii.com/iii/encore/record/C__Rb1609224;jsessionid=FADC75AC0C303D4F463300384A387C5F?lang=eng).
  **No averigüé qué fuente usa.**

### 6.1 · Una letra según cada uso (repaso corto) ✅

Lo pide ahora el punto 5: una letra para **cada** uso. Faltaban cinco: globo
normal, grito, pensamiento, onomatopeya e interfaz. Las cinco nuevas se
bajaron de `google/fonts` y se abrieron con fontTools
(`TTFont(f).getBestCmap()`): **traen á é í ó ú Á É Í Ó Ú ñ Ñ ¿ ¡ ü Ü**.

| Uso | Qué hay en la serie | Letra libre | Licencia | Tildes, ñ, ¿ ¡ |
|---|---|---|---|---|
| **Logo o título** | dibujado a mano (arriba) | **no imitarlo**; para un título, Cinzel o Yuji Boku en cinta | OFL | ✅ |
| **Globo normal** | rotulación en inglés de Steve Wands; su fuente no se sabe ⚠️ | **Comic Neue** ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/comicneue/METADATA.pb)) | OFL | ✅ |
| **Grito** | mayúsculas gruesas dibujadas en el manga | **Bangers** ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/bangers/METADATA.pb)) | OFL | ✅ |
| **Pensamiento** | **Jun 34 de Morisawa** (gótica redondeada, de pago), según una respuesta aceptada en [Yahoo!知恵袋](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q12276462092) ⚠️ una fuente | **Zen Maru Gothic** ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/zenmarugothic/METADATA.pb)). Kosugi Maru, la prima libre más parecida, **no trae** tildes, ñ, ¿ ni ¡: descartada | OFL | ✅ |
| **Onomatopeya** | katakana grande dibujada; Isayama las llena de juegos de palabras ([ANN](https://www.animenewsnetwork.com/interest/2019-09-21/attack-on-titan-japanese-sound-effects-are-full-of-goofy-puns/.151195) · [estudio de las 99 del tomo 1, JLA/UGM](https://journal.ugm.ac.id/jla/article/view/92270)) | **Bungee** ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/bungee/METADATA.pb)) | OFL | ✅ |
| **Cartel del mundo** | ficha «Información pública» (mincho); sentencias del tribunal | **Shippori Mincho B1**; **IM Fell English** (tabla de arriba) | OFL | ✅ |
| **Interfaz de juego** | menús de *AoT 3*: sans humanista cursiva, blanco roto (§12) | **Jost Italic** (`Jost-Italic[wght].ttf`, [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/jost/METADATA.pb)) | OFL | ✅ |
| **Subtítulos o créditos** | serif romana de mayúsculas espaciadas (tráiler latino) | **Cinzel**; **Cormorant Garamond** para texto largo | OFL | ✅ |

- **Pensamiento sin globo**: en el manga el monólogo va suelto, pegado al
  fondo, sin bocadillo ⚠️ (un solo hilo de foro; ninguna fuente oficial).
- Datos de `partes/texto.md` (investigador de texto, 24-sep-2026).

---

## 7 · Cómo hablan en pantalla (amplía la guía de cuadros)

### 7.1 La ficha «Información pública del momento», medida entera (2.ª pasada) ✅

Bajé **las 54 fichas del anime** (T1, 1920×1080) de la
[wiki](https://attackontitan.fandom.com/wiki/Current_Publicly_Available_Information/Anime)
y las medí con Pillow. Lo que antes se daba por fijo (papel rosado y cinta roja)
**sólo vale para el ep. 1**. Así son de verdad (hoja F·1-18):

- **Cada episodio trae dos fichas**: la **A, oscura** (fondo negro, dibujo
  blanco, cinta **arriba a la izquierda**) y la **B, clara** (papel gris claro
  casi neutro `#F2F2F2`, tinta `#222222`, cinta **arriba a la derecha**).
- **Cada episodio tiene su color de cinta.** Mediana de los píxeles de color
  de la cinta:

| Ep. | Color de la cinta (A / B) | Tema de la ficha |
|---|---|---|
| 1 | rojo sangre `#720101` / `#5D0003` | las murallas y su mapa |
| 2 | verde `#23694D` / `#205D44` | — |
| 3 | ocre `#837446` | — |
| 4 | oro viejo `#755F1E` / `#6A571C` | los 10 mejores cadetes (F·12) |
| 5 | azul `#1F5678` | — |
| 6 | magenta `#8C4068` / `#833C60` | — |
| 10 | violeta `#6A2F6A` / `#602B5F` | — |
| **14** | **verde `#26694F` / `#235F48`** | **el tribunal militar** (F·3-4) |
| **15** | **ocre `#948352` / `#867548`** | **el culto de la Muralla** (F·5-6) |
| **16** | **oro viejo `#796120` / `#6D581E`** | **elegir cuerpo** (F·7-8) |
| 19 | verde azulado `#257171` / `#246867` | bengalas BLACK/GREEN/RED (F·11) |
| 22 | vino `#6A2F40` / `#602C3B` | — |
| **25** | **sin cinta: documento con orla** | un texto largo, enmarcado (F·9-10) |

- **La ficha del tribunal (ep. 14 B, F·4)** es la más útil para #reglas:
  **una balanza** con «GUILTY» y «NOT GUILTY» en letra romana rota, «BALANCE»
  en el centro sobre la silueta de Zackly, **un mazo** en un círculo y **cadenas
  arriba y abajo**. Su texto: «Tribunal militar especial ②: más político que
  el normal; **la decisión es del jefe de los tres cuerpos, el generalísimo
  Darius Zackly**».
- **La ficha del ep. 25 (F·9-10) es un documento**: sin cinta, **un cuento
  largo en mincho, en 20 líneas justificadas**, dentro de una **orla con
  enredaderas y dibujitos** (caballo, pistola, equipo de maniobras, mirilla,
  emblemas). Es el formato natural para **las ocho reglas enteras**.
- El título de la cinta es siempre 現在公開可能な情報, en **pincel blanco**.
  El logo 進撃の巨人 metálico va abajo a la derecha (B) o a la izquierda (A).

### 7.2 Los globos del manga (antes sin estudiar; ahora mirados)

En las páginas del manga de la wiki (hojas de personajes, n.º 47, 76 y 138;
llegan **sin texto**, limpias) los globos de Isayama son **óvalos altos y
estrechos**, casi cápsulas, de línea negra fina y **colita corta en punta**;
van al borde de la viñeta para el texto vertical japonés. El dibujo alrededor
es de trama gris y rayado a pluma. **Para texto horizontal en español no
sirven tal cual**: por eso la lámina usa la ficha del anime o un objeto escrito.

### 7.3 Lo demás

1. **Las voces del robot aspirador de Levi** (Roborock S6 Pure, 9-jun-2021).
   Hiroshi Kamiya grabó **104 frases** en el papel de Levi (✅
   [アニメハック (JA)](https://anime.eiga.com/news/113576/) y
   [ねとらぼ (JA)](https://nlab.itmedia.co.jp/nl/articles/2105/26/news119.html);
   [ANN](https://www.animenewsnetwork.com/interest/2021-06-02/attack-on-titan-levi-lends-his-voice-to-robot-vacuum/.173442)
   dice 93, quizá sin contar repeticiones). Son la mejor pista oficial de cómo
   da órdenes de limpieza (traducción nuestra):
   - «…que no quede ni una mota de polvo. Mientras viva.»
   - «Se detiene la limpieza. Bueno, elige tú lo que no te deje arrepentimiento.»
   - «Limpieza terminada. **Esto es limpiar de verdad. ¿Entendido?**»
     (「掃除が完了した。これが本物の掃除だ。分かったか？」)
2. **En la serie, Levi habla de reglas** (ep. 15, subtítulos de Netflix):
   «**Es una regla que hay que cumplir**» (05:39) y Petra: «**Aquí la regla es
   el capitán**» (06:02). Traducción nuestra: no hay muestra latina de esas dos.
3. **Rótulos en pantalla**: en el resumen oficial, el nombre va en mincho
   blanco con el cargo debajo (F·28); en los créditos latinos, serif romana
   espaciada (F·25-26).
4. **El juego *Attack on Titan 2*** (Koei Tecmo, 2018) tiene la «vida en el
   campamento»: hablas con los personajes y eliges respuestas
   ([RPG Site](https://www.rpgsite.net/review/6932-attack-on-titan-2-review) ·
   [GodisaGeek](https://godisageek.com/reviews/attack-on-titan-2-review/)).
   **Su caja de diálogo, vista en la web oficial** (§12): **sin caja**, nombre
   pequeño sobre una línea crema fina y dos líneas de texto blanco con sombra,
   con una ✓ al final. La de *Attack on Titan 3* sigue la misma idea (demo,
   §12): diálogo sin caja y una **franja de pincel oro viejo** para los títulos.
   **La franquicia nunca usa globo blanco.**
5. **Los discursos** son la otra «voz»: Erwin en los eps. 16 y 53. En la
   lámina, un discurso no va en globo: va **escrito en un objeto** (bandera,
   acta, tablón).

**Qué NO hacer con el cuadro**: burbuja blanca redonda, neón o colores
alegres. **Ni poner siempre la cinta roja**: usa la del episodio que citas
(tribunal = verde, cuartel = ocre, saludo = oro viejo). Y en latino es
«Consagren», no «Entreguen».

---

## 8 · Quién es el más querido (encuestas)

| Encuesta | Ganó | Datos | Fuentes |
|---|---|---|---|
| 1.ª oficial (dic-2012 a ene-2013) | **Levi** | **3.952 votos** ✅; luego Eren 2.244 y Mikasa 2.232; Hange, 7.ª (388). Publicada en la guía *INSIDE 抗* (pp. 182-185) | [namu.wiki (KO)](https://namu.wiki/w/%EC%A7%84%EA%B2%A9%EC%9D%98%20%EA%B1%B0%EC%9D%B8/%EC%9D%B8%EA%B8%B0%ED%88%AC%ED%91%9C) · [Fandom](https://attackontitan.fandom.com/wiki/First_Character_Popularity_Poll) |
| 2.ª oficial (mayo 2015, *Bessatsu Shōnen*) | **Levi** | 20,6 % de 50.342 votos; luego Erwin y Eren. Isayama los dibujó en portada. | [ANN](https://www.animenewsnetwork.com/interest/2015-04-07/levi-erwin-eren-top-attack-on-titan-popularity-poll/.86828) · [Fandom](https://attackontitan.fandom.com/wiki/Second_Character_Popularity_Poll) |
| 3.ª oficial (dic-2017, capítulo 100) | **Erwin** | le quitó el primer puesto a Levi | [ANN](https://www.animenewsnetwork.com/interest/2017-12-09/erwin-tops-3rd-attack-on-titan-character-popularity-poll/.124960) · [Fandom](https://attackontitan.fandom.com/wiki/Third_Character_Popularity_Poll) |
| 4.ª oficial (9-sep-2021, *Full Color Edition* 2) | **Levi** | Levi 3.130, Erwin 1.150, **Hange 1.128**, Eren 1.003, Mikasa 406, Jean 389, Armin 288 | [X @AoTWiki](https://x.com/AoTWiki/status/1435720535070019588) · [Fandom](https://attackontitan.fandom.com/wiki/Fourth_Character_Popularity_Poll) |
| Encuesta de fans de Nlab (2024) | **Levi** | primero de 30 | [ねとらぼ (JA)](https://nlab.itmedia.co.jp/research/articles/2406467/) · [otra de ねとらぼ](https://nlab.itmedia.co.jp/research/articles/2954723/) |
| Encuesta oficial «de titanes» (2021) | el **titán de la página 36 del capítulo 38** | un chiste del fandom | [Oricon (JA)](https://www.oricon.co.jp/news/2191985/full/) · [Magapoke (JA)](https://pocket.shonenmagazine.com/article/entry/shingeki_20210430) |

**Conclusión: Levi es el más querido, y por mucho.** Luego vienen Erwin y Hange.
Eren, el protagonista, queda cuarto. Para #reglas, Levi es además el que
**impone el orden**: le pega a Eren para salvarlo y limpia hasta el último rincón.

En coreano hay recopilaciones en [fmkorea](https://www.fmkorea.com/4446340048) y
[dcinside](https://m.dcinside.com/board/shingeki/979988).

**En chino** (2.ª pasada): [Bangumi](https://bgm.tv/subject/55770/characters)
(番组计划, la base de datos china de anime), por su API, 24-sep-2026. La serie
tiene nota 8,2 con 31 729 votos. Personajes guardados como favoritos (收藏):

| Personaje (nombre chino) | Favoritos | Comentarios |
|---|---|---|
| Mikasa (三笠·阿克曼) | **1019** | 151 |
| **Levi (利威尔)** | **776** | 158 |
| Eren (艾伦·耶格尔) | 528 | 277 |
| Krista (克里斯塔·连兹) | 459 | 109 |
| Erwin (艾尔文·史密斯) | 242 | 48 |
| Hange (韩吉·佐伊) | 138 | 44 |

**En China gana Mikasa**, no Levi; Levi es el primero de los secundarios y el
segundo en total. En Japón y en Occidente gana Levi (arriba). Para una lámina
en español, Levi sigue siendo la apuesta segura. La ficha china de Levi le da
los apodos **兵长** («el capitán») y **一米六** («uno sesenta», por su
estatura) y confirma 160 cm y 65 kg ([Bangumi, Levi](https://bgm.tv/character/19546)).
Moegirl (萌娘百科) y Baidu Baike no dejaron entrar (dos intentos cada una).

---

## 9 · Doblaje latino (cada nombre con dos fuentes)

### 9.1 La producción ✅

- **Estudio**: C&G Dubbing Studio (Artworks Digital Studio), Ciudad de México
  ([Doblaje Wiki, API][dw-aot] · [FUNiAnime][funi]).
- **Dirección**: **Gerardo «Gerry» Ortega**, que además dobla a Jean y fue
  ingeniero de audio ([Doblaje Wiki][dw-aot] · [FUNiAnime][funi] ·
  [ANMTV, 2025][anmtv-film]).
- **Traducción y adaptación**: Jennifer Medel (que dobla a Sasha); Brenda Nava
  adaptó los eps. 46-49. Mezcla en Cronophonia (Julio Caín). Asistente de
  dirección: Carlos Monroy ⚠️ (sólo la ficha de Doblaje Wiki; FUNiAnime no lo
  nombra y [ANMTV, 2020](https://www.anmtvla.com/2020/09/attack-on-titan-artworks-revela-toda-la.html?m=1)
  sólo como la voz de Samuel en las películas; en la serie también dobla a
  Klaus, Gustav y Keiji).
- **Grabación**: de mayo de 2020 (T1-T2) a diciembre de 2023 (T4, parte 3).
  Salió en Funimation (T1 a T4, parte 2) y en Crunchyroll (el final)
  ([Doblaje Wiki][dw-aot]). Antes se doblaron las **tres películas
  recopilatorias** (2020) con el mismo reparto ([Doblaje Wiki][dw-aot] ·
  [FUNiAnime][funi]).
- **Lo de VSI, resuelto** (antes «dudoso»): VSI Mexico City hizo **la película
  *El ataque final*** (feb-2025), también dirigida por Gerry Ortega. **Reutilizó
  las voces de la serie**, remezcladas para cine; sólo la escena poscréditos se
  grabó nueva ([Doblaje Wiki: la película][dw-film] · [ANMTV, 2-mar-2025][anmtv-film]).
- **Los títulos de los episodios se dicen en voz alta** en el doblaje (hasta el
  ep. 75), con otra traducción que la de los subtítulos ([Doblaje Wiki][dw-aot]).
- **Premio**: Miguel Ángel Leal (Eren) ganó **mejor actor de doblaje latino** en
  los Crunchyroll Anime Awards 2025 ([ANMTV][anmtv-premio]).

### 9.2 Las voces

Cada nombre, en la ficha de la serie de Doblaje Wiki (API) **y** en la lista de
[FUNiAnime][funi] (23-dic-2021). Donde FUNiAnime no llega, la ficha del actor.

| Personaje | Voz latina | Estado | Fuentes |
|---|---|---|---|
| **Levi** | **Alfredo Gabriel Basurto** (de niño, ep. 47: Ivett Toriz ⚠️, sólo Doblaje Wiki, en la ficha de la serie y en la de ella) | ✅ | [DW][dw-aot] · [FUNiAnime][funi] · [ficha del actor][dw-basurto] · **Crunchyroll en Español**, descripción del [clip oficial de Levi contra Zeke][yt-zeke]: «Gabriel Basurto – Levi» |
| **Erwin** | **Octavio Rojas** | ✅ | [DW][dw-aot] · FUNiAnime · [La Mole][lamole] |
| **Hange** | **Rossy Aguirre**, en la serie **y en la película** | ✅ | [DW][dw-aot] · [DW película][dw-film] · FUNiAnime |
| **Eren** | **Miguel Ángel Leal** | ✅ | DW · FUNiAnime · ANMTV (premio) |
| **Mikasa** | **Ana Lobo** | ✅ | DW · FUNiAnime · [Anime Argentina][animearg] |
| Armin y el narrador | Héctor Ireta de Alba | ✅ | DW · FUNiAnime |
| Jean | Gerardo Ortega | ✅ | DW · FUNiAnime |
| Sasha | Jennifer Medel | ✅ | DW · FUNiAnime |
| Connie | Alberto Bernal | ✅ | DW · FUNiAnime |
| **Reiner** | **Alfonso Obregón** | ✅ | DW · FUNiAnime |
| Annie · Historia · Ymir · Bertolt | Georgina Sánchez · Cristina Hernández · Alina Galindo · Yamil Atala | ✅ | DW · FUNiAnime |
| Marco | Óscar López | ✅ | DW · FUNiAnime |
| **Keith Shadis** (instructor) | **Carlos Segundo** | ✅ | DW · FUNiAnime |
| **Darius Zackly** (juez) | **Rubén Moya** (en las películas de 2020 era José Luis Portela) | ✅ | DW · FUNiAnime |
| Dot Pixis · Nile Dawk | Francisco Reséndez · Saúl Alvar | ✅ | DW · FUNiAnime |

**Corregido:**
- **Hange en la película no es Laura Torres.** La ficha de Laura Torres en
  Doblaje Wiki no tiene ningún papel en *Attack on Titan*; la de la película pone
  a Rossy Aguirre, y ANMTV explica que se reutilizaron las voces de la serie.
- **Reiner es Alfonso Obregón.** Óscar López dobla a **Marco**, no a Reiner:
  K-magazine los mezcló.

**Voces japonesas** (ficha de Doblaje Wiki y otra fuente): Levi, **Hiroshi
Kamiya** ✅ (ANN); Erwin, **Daisuke Ono** ✅ ([IMDb][imdb-ono]); Hange, Romi
Park; Eren, Yūki Kaji; Mikasa, Yui Ishikawa.

### 9.3 Frases propias del doblaje latino (textuales)

**De dónde salen.** YouTube no deja bajar audio (pide iniciar sesión). Pero
**Doblaje Wiki guarda muestras de audio del doblaje** de cada personaje (20-50
s). Bajé 16 y las pasé por **Whisper** (modelo *small*, en español). Corregí a
mano sólo nombres rotos obvios («Kid Sadis» → Keith Shadis, «sitanes» →
titanes, «Hanji Soe» → Hange Zoë). El capítulo y el minuto salen de cruzar cada
frase con los **subtítulos japoneses de Netflix** ([espejo de kitsunekko][kitsu]).
✅ = el sentido coincide con esos subtítulos.

| Quién | Frase del doblaje latino | Dónde | Estado |
|---|---|---|---|
| **Erwin** | «Díganme, cadetes. ¿Morirían si yo les ordenara matarse? … Comprendo. Sus miradas muestran voluntad. Escúchenme. En este momento les doy la bienvenida a la **Legión de Exploración**. Así es como se hace un verdadero saludo. Cadetes, **¡consagren sus corazones!**» | **ep. 16 · 13:52-14:13** ([muestra][dw-aot], 0:16-0:36) | ✅ |
| Erwin | «Lamento lo sucedido, pero gracias a eso conseguimos ponerte bajo nuestra custodia. … Tienes todo mi respeto.» | ep. 14 · 21:09 (a Eren, tras el juicio) | ✅ |
| **Levi** | «**Yo no planeo estrategias. Eso no me compete.** Pero conozco a Erwin. Debe estar considerando más variables que nosotros.» | **ep. 15 · 08:44** | ✅ |
| Levi | «No sabía que los cerdos podían hablar.» · «Y ese nosotros que tanto repiten son nuestros compañeros que mueren mientras ustedes engordan.» | ep. 14 · 13:50 (a los mercaderes, en el juicio) | ✅ sentido |
| Levi | «Tu determinación me dará fuerza. Eso te lo prometo.» | **ep. 9 · 06:57-07:04**, al soldado que muere (en japonés: «la voluntad que dejas me da fuerza. Te lo prometo») | ✅ sentido |
| Levi (película) | «Yo seré… quien mate a Zeke. Así que, por favor, ayúdenme.» | *El ataque final* ([muestra][dw-film]) | ✅ sentido |
| **Hange** | «Perdóname por hacerte esperar. … **Soy líder de la Cuarta División de la Legión de Exploración, Hange Zoë.**» | **ep. 14 · 08:23-08:37** | ✅ |
| Hange (película) | «Armin Arlert: desde ahora eres el decimoquinto comandante de la Legión de Exploración. La cualidad fundamental para ser el comandante de esta legión es que **nunca se rinda en el camino del conocimiento**. No hay nadie más apto que tú.» · «Recuerda que ahora Levi es tu subordinado. Así que explótalo bien.» | *El ataque final* ([muestra][dw-film]) | ✅ sentido |
| **Keith Shadis** | «Ahora ustedes son los nuevos reclutas de la tropa de cadetes 104. Y para su mala suerte, yo seré el jefe encargado de ustedes: el excomandante Keith Shadis. **No estoy para darles una cálida bienvenida.** Sólo les diré que ustedes son el ganado, a la espera de ser comidos por los titanes. No, son peor que el ganado.» | ep. 3, desde 01:39 | ✅ |
| **Darius Zackly** | «Bueno, daremos inicio. ¿Eres Eren Jaeger, correcto? … Este es un caso especial. En este juicio la ley común no va a aplicarse, así que será una **corte marcial**. Significa que **la decisión final la tomaré yo, ¿entendido?**» | **ep. 14 · 10:29** | ✅ |
| Nile Dawk | «Comandante de la Policía Militar, Nile Dawk. Yo seré quien tome la palabra.» | ep. 14 · 11:38 | ✅ |
| Mikasa | «Eren, mejor olvídate de la Legión de Exploración.» · «Volviste a dejarte llevar por tus emociones, Eren.» | T1 ([muestra][dw-aot]) | ✅ sentido |
| Jean | «¿En serio dijiste que quieres unirte a la Legión de Exploración?» | T1 ([muestra][dw-aot]) | ✅ sentido |

**Lo que cambia con esto:**
- **El cuerpo se llama «Legión de Exploración»** en el doblaje. Lo dicen cuatro
  voces distintas (Erwin, Hange, Mikasa y Jean). **No «Legión de
  Reconocimiento»** (así lo llama parte del fandom) ni «Cuerpo de Exploración»
  (la sinopsis de Crunchyroll). ⚠️ Una sola fuente (las muestras de Doblaje
  Wiki), pero cuatro grabaciones. No hallé un texto oficial que lo diga: los
  subtítulos automáticos de los tres clips oficiales de Crunchyroll en Español
  (§9.4, bajados al cierre) no nombran el cuerpo, y los títulos de clips
  latinos subidos por fans dicen «legión de exploración» tres veces y «de
  reconocimiento» una (búsqueda en YouTube, 24-sep-2026).
- **Otros términos del doblaje** (de las muestras): «tropa de cadetes 104»,
  «Policía Militar», «corte marcial», «muralla Rose», «muralla Sina», «equipo
  de maniobras tridimensional», «titanes». Reiner dice «**amonestación**» en el
  ep. 4 ([Doblaje Wiki][dw-aot]).
- **«¡Consagren sus corazones!» es de Erwin (ep. 16)**, confirmado por la
  muestra. **El clip de Crunchyroll que se citaba no es esa escena**: es del
  **ep. 71** (T4). Lo miré por su *storyboard*: tras la bomba en el despacho
  de Zackly, **la gente en la verja del cuartel grita «¡Consagren sus
  corazones!» con el puño en alto** (clip 0:48-0:58; subtítulos de Netflix del
  ep. 71, 12:31-12:57: 心臓を捧げよ, dicho por «hombre» y «gente»). Su
  descripción dice «Episodio 71». (En la primera mitad de esta pasada se había
  puesto en el ep. 73, con Keith: no es así.) El título del clip oficial es la **segunda
  fuente textual** de la frase latina, y sus subtítulos automáticos la recogen
  dos veces, mal oída (0:45 y 0:59, §9.4).
- **La frase de Connie estaba mal.** «¡Las casas están ardiendo! De seguro esa
  es la casa de Eren» es el **chiste japonés traducido** (*Eren no ie ga*). **El
  doblaje dice otra cosa**: «**Si yo fuera Eren, ¡diría que Mikasa está que
  arde!**» ([Doblaje Wiki, datos de interés][dw-aot]).
- **De Levi ya hay frases latinas con fuente** (arriba). La del aspirador
  («Esto es limpiar de verdad. ¿Entendido?») sigue siendo **traducción nuestra**
  del japonés.

### 9.4 Vídeos del doblaje (comprobados con yt-dlp)

Todos son del canal oficial **Crunchyroll en Español** y los miré por su
*storyboard* (hojas de `fotogramas.py`, ±1 s). En la primera mitad de la
pasada yt-dlp no encontró subtítulos en ninguno. **En el cierre (24-sep,
16:18-16:25) sí bajó los subtítulos automáticos en español de los tres clips
doblados** (YouTube los saca del audio doblado; al segundo o tercer intento,
porque a ratos pedía «iniciar sesión»). Ya hay **frases latinas textuales de
clips oficiales**. Levi no habla en ninguno de los tres.

**«¡Consagren sus corazones!»** (ep. 71):

| Minuto del clip | Lo que se oye (subtítulo automático; puntuación nuestra) |
|---|---|
| [0:22](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=22) | «¿Estás bien?» |
| [0:37-0:40](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=37) | «Explotó la oficina del comandante en [jefe]… ¿Dónde se encuentra?» |
| [0:45-0:46](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=45) | la gente grita la frase; la máquina oye «**pons abren sus corazones**» |
| [0:47-0:52](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=47) | «**Al fin nuestra ira fue escuchada. Ha llegado la hora de luchar.** ¡Yo también!» |
| [0:59-1:01](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=59) | otra vez la frase; la máquina oye «**sangre sus corazones**» |

La máquina oye mal «Consagren» dos veces, pero el ritmo y el «sus corazones»
cuadran con el **título oficial del clip** y con la muestra de Erwin (§9.3).

**«Declaración de Guerra»** (ep. 64), Willy Tybur y Eren:

| Minuto del clip | Frase (subtítulo automático; puntuación nuestra) |
|---|---|
| [0:05-0:10](https://www.youtube.com/watch?v=pNRP0z8IwHQ&t=5) | Willy: «…todos juntos, sé que podremos superar cualquier obstáculo.» |
| [0:13](https://www.youtube.com/watch?v=pNRP0z8IwHQ&t=13) | Eren a Reiner: «Yo soy igual… igual que tú.» |
| [0:19-0:26](https://www.youtube.com/watch?v=pNRP0z8IwHQ&t=19) | Willy: «Por favor, unamos nuestras fuerzas. Enfrentemos juntos a los demonios de la isla Paradis.» |
| [0:36-0:43](https://www.youtube.com/watch?v=pNRP0z8IwHQ&t=36) | Eren: «**Siempre continúo mi camino. Avanzo hasta matar a mis enemigos.**» (es su «sigo avanzando», 進み続ける) |

**«En ese momento, Zeke sintió el verdadero terror»** (ep. 73):

| Minuto del clip | Frase (Zeke, Ricardo Brust; subtítulo automático, puntuación nuestra) |
|---|---|
| [0:00-0:10](https://www.youtube.com/watch?v=wOzu2yF4HC4&t=0) | «Una despedida… Qué mal, al final no pudimos entendernos. No es de extrañar: después de todo, somos de mundos muy diferentes.» |
| [0:12-0:24](https://www.youtube.com/watch?v=wOzu2yF4HC4&t=12) | «Todos creyeron que tenían poder, más tiempo y otras opciones. Malentendieron completamente su situación… Ese fue su gran error.» |
| [0:36-0:51](https://www.youtube.com/watch?v=wOzu2yF4HC4&t=36) | «Saldré de este bosque para reunirme contigo. Sin embargo, espero que no olvides el lugar y la hora que acordamos, Eren.» |

Sirven de muestra del **registro del doblaje**: español neutro, «ustedes»,
frases completas y formales («Sin embargo, espero que…»). No sirven para
#reglas.

| Vídeo | Qué es (lo que vi) | Datos |
|---|---|---|
| [«¡Consagren sus corazones!»][yt-consagren] | **ep. 71**: la bomba de Zackly ([0:02](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=2)), Mikasa, Armin e Hitch en el patio de columnas ([0:34-0:46](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=34)) y **la gente con el puño en alto** en la verja ([0:48-0:58](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=48)) | 1:27 (1:05 de escena), 17-ene-2022 ✅ |
| [«En ese momento, Zeke sintió el verdadero terror»][yt-zeke] | **ep. 73**: Levi contra Zeke en el bosque; acredita a Gabriel Basurto (Levi) y Ricardo Brust (Zeke) | 1:29, 11-ene-2022 ✅ |
| [«Declaración de Guerra»][yt-guerra] | **ep. 64**: Willy Tybur en el escenario con los brazos abiertos ([0:02](https://www.youtube.com/watch?v=pNRP0z8IwHQ&t=2), [0:54](https://www.youtube.com/watch?v=pNRP0z8IwHQ&t=54)), el sótano de ladrillo con Eren y Reiner, el público con el puño en alto bajo un foco ([0:32](https://www.youtube.com/watch?v=pNRP0z8IwHQ&t=32)) | 1:26, 3-ene-2022 ✅ |
| [Tráiler del Especial 1, doblaje latino][yt-esp1] | créditos en serif espaciada con tildes (§6) | 1:25, 6-sep-2023 ✅ |
| [Tráiler de Eren, Especial 2 (dob. latino)][yt-esp2] | tráiler | 0:30, 12-dic-2023 ✅ |

Doblaje Wiki lista además entrevistas al reparto (ANISON USA, «Las voces que
amamos» con Gabriel Basurto). **No las pude abrir** (YouTube bloqueado).

---

## 10 · Música (qué ambiente da)

- **Hiroyuki Sawano**, temporadas 1 a 3. Le encanta poner letras en alemán
  ([Fandom](https://attackontitan.fandom.com/f/p/2822659075211755953) ·
  [Wikipedia](https://en.wikipedia.org/wiki/Music_of_Attack_on_Titan)).
  - **«Vogel im Käfig»** («pájaro en la jaula»; letra de Rie, voz de Cyua).
    Del 0:00 al 2:38 es luminosa y con esperanza; del 2:39 al 6:15, oscura y
    desesperada. Es la metáfora de vivir entre murallas
    ([Fandom](https://attackontitan.fandom.com/wiki/Vogel_im_K%C3%A4fig) ·
    [Lyrics Translate](https://lyricstranslate.com/en/vogel-im-k%C3%A4fig-bird-cage.html)).
    **Es el ambiente de #reglas**: estamos dentro y hay normas.
  - «ətˈæk 0N tάɪtn» (voz de Mika Kobayashi) y «Call your name» (mpi y CASG)
    ([Fandom](https://attackontitan.fandom.com/wiki/Call_your_name)).
- **Kohta Yamamoto**, temporada final, con Sawano. Ganó el Crunchyroll a mejor
  banda sonora y tocó «Ashes on the Fire» en la gala del 4-mar-2023
  ([Wikipedia](https://en.wikipedia.org/wiki/Kohta_Yamamoto) ·
  [entrevista en YouTube](https://www.youtube.com/watch?v=6g7r-JIZHv0)).
- **Openings y endings, con su intérprete** ✅ (títulos de los vídeos
  oficiales sin créditos del canal de **Pony Canyon**, comprobados con yt-dlp,
  y la ficha de cada episodio en la wiki, que da el tema de cada capítulo):

| Parte | Opening | Ending |
|---|---|---|
| T1, 1.ª mitad | «Guren no Yumiya», Linked Horizon ([vídeo](https://www.youtube.com/watch?v=AW5_k_Cf4wM)) | «Utsukushiki Zankoku na Sekai», Yoko Hikasa ([vídeo](https://www.youtube.com/watch?v=eN_rq3FvJUs)) |
| **T1, 2.ª mitad (eps. 14-25)** | «**Jiyuu no Tsubasa**», Linked Horizon ([vídeo](https://www.youtube.com/watch?v=43spp3kzGVw)) | «great escape», cinema staff ([vídeo](https://www.youtube.com/watch?v=jXeD6i0Vssg)) |
| T2 | «Shinzou wo Sasageyo!», Linked Horizon ([vídeo](https://www.youtube.com/watch?v=nAksM2HAAqo)) | «Yuugure no Tori», Shinsei Kamattechan ([vídeo](https://www.youtube.com/watch?v=Gpwt7R9pGuo)) |
| T3, parte 1 | «Red Swan», YOSHIKI feat. HYDE ([vídeo](https://www.youtube.com/watch?v=IjwuJT6q54s)) | «Akatsuki no Chinkonka» (*Requiem der Morgenröte*), Linked Horizon ([vídeo](https://www.youtube.com/watch?v=3JWKoVCkT1w)) |
| T3, parte 2 | «Shoukei to Shikabane no Michi», Linked Horizon ([vídeo](https://www.youtube.com/watch?v=5IdD-y4KKVA)) | «Name of Love», cinema staff ([vídeo](https://www.youtube.com/watch?v=R8ED7xV3hTU)) |
| Final, parte 1 | «My War» (*Boku no Sensou*), Shinsei Kamattechan ([vídeo](https://www.youtube.com/watch?v=6TolbTZXDjI)) | «Shock», Yuko Ando ([vídeo](https://www.youtube.com/watch?v=AZl8UDsqsoM)) |
| Final, parte 2 | «The Rumbling», SiM ([vídeo](https://www.youtube.com/watch?v=2S4qGKmzBJE)) | «Akuma no Ko», Ai Higuchi ([vídeo](https://www.youtube.com/watch?v=9lnh--ZOPyo)) |
| Final, capítulos finales | «Saigo no Kyojin», Linked Horizon ([vídeo](https://www.youtube.com/watch?v=d6qCbdXqsOs)) | «Itterasshai», Ai Higuchi ([vídeo](https://www.youtube.com/watch?v=DU2KGyQgso4)) |

  La wiki llama a los openings de la T1 y T2 por su título alemán: «Feuerroter
  Pfeil und Bogen», «Die Flügel der Freiheit» y «**Opfert eure Herzen!**»
  («¡Ofrezcan sus corazones!»).
- **Lo que vi en el opening de los eps. 14-25** («Jiyuu no Tsubasa», vídeo
  oficial sin créditos de Pony Canyon, 1:30; hoja de fotogramas cada 2 s sacada
  de su *storyboard*, ±1 s): abre con **un relieve oscuro en un muro de piedra
  verde** ([0:00](https://www.youtube.com/watch?v=43spp3kzGVw&t=0)); campos
  verdes desde el aire ([0:02-0:04](https://www.youtube.com/watch?v=43spp3kzGVw&t=2));
  bosque y casas de madera (0:06-0:12); **siluetas de la Legión contra un
  atardecer naranja**, con caras encima ([0:20-0:24](https://www.youtube.com/watch?v=43spp3kzGVw&t=20);
  medido: `#86411C` · `#AB6630` · `#D7A04B`, cielo `#E0A024`); un ojo con una
  lágrima (0:26); **un puño apretado a contraluz de una ventana**
  ([0:28-0:30](https://www.youtube.com/watch?v=43spp3kzGVw&t=28); luz `#E3D4AF`);
  vitrales y una iglesia (0:34-0:36); **velas** (0:38); **Levi con la capa**
  ([0:46](https://www.youtube.com/watch?v=43spp3kzGVw&t=46)) y volando entre
  los árboles (0:48-0:52); cables y hojas (0:54-1:00); primeros planos del
  **equipo de maniobras en metal beige** ([1:02-1:06](https://www.youtube.com/watch?v=43spp3kzGVw&t=62));
  la cara seria de Erwin ([1:12](https://www.youtube.com/watch?v=43spp3kzGVw&t=72));
  Eren con los ojos cerrados sobre rojo (1:16); y el **logo 進撃の巨人 sobre un
  muro de ladrillo blanco** ([1:26-1:28](https://www.youtube.com/watch?v=43spp3kzGVw&t=86)).
- **El ending de la T1** («Utsukushiki Zankoku na Sekai», Pony Canyon, 1:30;
  misma técnica) **empieza en gris, como grabado a tinta** y **pasa a sepia de
  papel viejo** en la segunda mitad:
  - gris: estrellas y una luna ([0:02-0:06](https://www.youtube.com/watch?v=eN_rq3FvJUs&t=2)),
    un cuchillo entre flores (0:10), un bosque reflejado en el agua
    (0:16-0:24), **Mikasa niña con la bufanda** ([0:26-0:30](https://www.youtube.com/watch?v=eN_rq3FvJUs&t=26))
    y rodeada de **cuchillos clavados** ([0:32-0:48](https://www.youtube.com/watch?v=eN_rq3FvJUs&t=32));
  - sepia: Mikasa mayor ([0:56](https://www.youtube.com/watch?v=eN_rq3FvJUs&t=56)),
    un ala (0:58), un pueblo de piedra con Mikasa de espaldas (1:00-1:04),
    Mikasa con la sombra de una reja (1:06-1:08), **una puerta en arco con
    alguien en la luz** ([1:10-1:14](https://www.youtube.com/watch?v=eN_rq3FvJUs&t=70)),
    Eren (1:16-1:18) y Mikasa tocándose la bufanda (1:20). Medido en el
    *storyboard*: papel `#F0EDD2`, tinta `#2C2921`, medio `#C8C2A5`.
  - Mismo lenguaje que las fichas en blanco y negro: **papel viejo y tinta**
    también sirven de «voz» de la serie.
- **Para el tono de las láminas**: «Shinzou wo Sasageyo» es el lema del saludo.
  Lámina 3.

### 10.1 · Qué suena en las escenas que hacen llorar, y los sonidos que todos reconocen (repaso corto)

**El tema de las despedidas: «Call of Silence»** (Hiroyuki Sawano, voz de
Gemie; OST de la T2, disco 1, pista 5) ✅
([Fandom, «Call of Silence»](https://attackontitan.fandom.com/wiki/Call_of_Silence),
con su lista de apariciones · [Spotify](https://open.spotify.com/track/7k1HoUdskuBhyWvm7hPctM)).
La wiki dice que es un *remix* de «eye-water» con el puente de «Call your name».

| Escena | Tema | Fuente |
|---|---|---|
| Carga suicida de Erwin (ep. 54) | «**APETITAN**» | ✅ [Fandom, «Hero»](https://attackontitan.fandom.com/wiki/Hero_(Episode)) |
| Floch trae a Erwin moribundo y hay que elegir (**ep. 55**) | «**Call of Silence**» | ✅ página de la canción |
| Mikasa besa la cabeza de Eren (**ep. 93**) | «**Call of Silence**», otra vez | ✅ página de la canción |
| Gabi dispara a Sasha (**ep. 67**) | «**Nightmare**»; luego dos pistas sin título (`進撃vc-pf20130218巨人`, `進撃vn-pf20130524巨人`) mientras se desangra | ✅ [Fandom, «Assassin's Bullet»](https://attackontitan.fandom.com/wiki/Assassin%27s_Bullet_(Episode)) |

- **La idea útil**: la misma pieza marca **dejar ir a alguien** en dos
  despedidas separadas por años (Erwin y Mikasa). Minutos en el Punto 21.
- **Sonidos que el fandom reconoce al instante** (hilo de sonidos icónicos de
  r/ShingekiNoKyojin, por Arctic Shift:
  [1u0dj12](https://www.reddit.com/r/ShingekiNoKyojin/comments/1u0dj12/)):
  - el coro **«Sasageyo, sasageyo, shinzou wo sasageyo!»** del OP de la T2
    (3 votos) ⚠️ un comentario;
  - el grito **«KEEEENNNYYY»** (Kenny Ackerman; 6 votos) ⚠️ un comentario;
  - la letra alemana del OP 1, **«Seid ihr das Essen? Nein, wir sind die
    Jäger!»** («¿Son ustedes la comida? No, somos los cazadores»), que medio
    mundo oye mal («Sie sind das Essen…» y parodias en inglés) ✅ (letra
    oficial del folleto del CD en [Fandom](https://attackontitan.fandom.com/wiki/Feuerroter_Pfeil_und_Bogen)
    + el mismo hilo, 9 votos). No encontré la versión hispana del chiste.
- **El disparo**: los subtítulos japoneses de Netflix (`ja[cc]`) marcan
  el sonido en el ep. 67: **13:26 銃声** (disparo) y **13:27 着弾音**
  (impacto) (espejo de kitsunekko, ver Punto 21).
- **Equipo de maniobras** (gancho y chorro de gas) y **vapor** de un titán al
  morir: todo el mundo los cita, pero **no encontré una ficha oficial que los
  nombre** ⚠️. No inventar un nombre técnico.
- **Onomatopeyas del manga**: katakana con juegos de palabras (§6.1).

---

## 11 · Vídeos útiles

Cómo los miré: `yt-dlp` baja el *storyboard* (mosaicos de 160×90 o 320×180,
uno por segundo en los clips cortos) y `herramientas/fotogramas.py` monta la
hoja numerada con el minuto. Precisión: ±1 s (±2 s en el clip de 2:30). Cada
enlace se comprobó con `yt-dlp` (título, canal, duración) el 24-sep-2026.

| Vídeo | Para qué | Minuto (lo que vi) |
|---|---|---|
| [«¡Consagren sus corazones!», Crunchyroll en Español (oficial, doblado)](https://www.youtube.com/watch?v=nxQCiDpxeMY) | la frase latina; **ep. 71**, no el 16 | [0:48-0:58](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=48): la gente grita con el puño en alto |
| [Levi contra Zeke, Crunchyroll en Español (oficial, doblado)](https://www.youtube.com/watch?v=wOzu2yF4HC4) | Levi en acción, T4; crédito oficial de Basurto | [0:56-1:00](https://www.youtube.com/watch?v=wOzu2yF4HC4&t=56) el golpe; [1:08](https://www.youtube.com/watch?v=wOzu2yF4HC4&t=68) Levi en el aire con la capa |
| [Levi y su escuadrón limpian (subida de fan, dub inglés, ep. 15)](https://www.youtube.com/watch?v=GLpLwuaBk-s) | **concepto A**: ropa, sitio y cara | [0:04-0:12](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=4) el castillo de torres redondas y rosetón, la Legión de espaldas con las alas; [0:14](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=14) Levi con capa y chorrera, párpado caído; [0:32-0:34](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=32) Levi con pañuelo se baja el de la boca junto a la ventana (= P·10); [0:36-0:46](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=36) Levi de espaldas habla con Eren bajo un arco de piedra; [1:08-2:20](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=68) Petra con escoba y pañuelo al cuello; [2:24-2:28](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=144) Levi en la puerta: «hazlo todo otra vez» |
| [Levi y Erwin, «Give up on your dreams and die» (subida de fan, 8 s)](https://www.youtube.com/watch?v=o8pkg7HjBIk) | Levi agachado ante Erwin | [0:00-0:05](https://www.youtube.com/watch?v=o8pkg7HjBIk&t=0) Erwin sentado, cabeza baja; [0:05-0:07](https://www.youtube.com/watch?v=o8pkg7HjBIk&t=5) Levi con capucha. *Storyboard* de 48×27: casi no se ve; mejor P·22 y los subtítulos (ep. 53 · 18:00) |
| [Opening 2 «Jiyuu no Tsubasa» (Pony Canyon)](https://www.youtube.com/watch?v=43spp3kzGVw) | ambiente, puño a contraluz, logo | ver §10 |
| [Ending 1 «Utsukushiki Zankoku na Sekai» (Pony Canyon)](https://www.youtube.com/watch?v=eN_rq3FvJUs) | gris y sepia, papel viejo | ver §10 |
| [Tráiler de 2012 (Pony Canyon)](https://www.youtube.com/watch?v=KKzmOh4SuBc) | créditos en mincho | ver §6; Mikasa con la bufanda y leña ([0:06-0:08](https://www.youtube.com/watch?v=KKzmOh4SuBc&t=6)) |
| [Tráiler del Especial 1, doblaje latino (Crunchyroll)](https://www.youtube.com/watch?v=sFuAhHTgABs) | créditos en español | ver §6; Hange de la T4 con capa, de frente ([0:30](https://www.youtube.com/watch?v=sFuAhHTgABs&t=30)) |
| [«Declaración de Guerra» (Crunchyroll, doblado)](https://www.youtube.com/watch?v=pNRP0z8IwHQ) | escenario con foco: «anuncio» | ver §9.4 |
| [Voz de Levi en español latino (subida de fan «Carl», 1:33, 17-ene-2022)](https://www.youtube.com/watch?v=UTRAXM1PCFc) | el timbre de Basurto | existe ✅; es audio: no se puede «ver» por *storyboard*. Escucharlo antes de escribir su frase |
| [Recopilación de cartelas T1-T4 (subida de fan, versión inglesa, 10:02)](https://www.youtube.com/watch?v=0LU5UpvK2Vk) | las fichas «Información pública» en vídeo | la ficha del tribunal ([2:30](https://www.youtube.com/watch?v=0LU5UpvK2Vk&t=150)); las de la temporada final **siguen el mismo formato** ([8:40-10:00](https://www.youtube.com/watch?v=0LU5UpvK2Vk&t=520)). En la versión inglesa la cinta dice «Information We Can Share So Far»: **la cinta se traduce**, así que en español puede llevar texto en español |
| [Emisión oficial de la fecha de *AoT 3* (Koei Tecmo, 9:12, 3-ago-2026)](https://www.youtube.com/watch?v=2yD_s-8A12s) | interfaz del juego nuevo | «12月10日(木)発売決定!» en serif blanca sobre los ojos de Eren ([0:55](https://www.youtube.com/watch?v=2yD_s-8A12s&t=55)); el productor lleva la chaqueta de recluta; creación de personaje ([3:10-3:20](https://www.youtube.com/watch?v=2yD_s-8A12s&t=190)); escenas con subtítulo blanco sin caja ([3:25-3:50](https://www.youtube.com/watch?v=2yD_s-8A12s&t=205)) |
| [Demo de *AoT 3* (grabada por el canal SLOplays, 10:46)](https://www.youtube.com/watch?v=R2KM0OgyU-M) | menús y cajas | ver §12: diálogo sin caja ([0:05](https://www.youtube.com/watch?v=R2KM0OgyU-M&t=5), [0:45](https://www.youtube.com/watch?v=R2KM0OgyU-M&t=45)) y **franja de pincel oro viejo** de misión ([2:55](https://www.youtube.com/watch?v=R2KM0OgyU-M&t=175)) |
| TikTok: [Gabriel Basurto saluda como Levi](https://www.tiktok.com/@robb_g89/video/7343408637378858246) · [descubrir «give up your dreams»](https://www.tiktok.com/discover/give-up-your-dreams-and-die-scene?lang=en) · [arte nuevo de MAPPA](https://www.tiktok.com/discover/mappa-new-aot-official-art) | tendencias | — |

Novedad: desde el Día de AoT (9-sep-2026) hay **canal oficial de YouTube**
([Anime Corner](https://animecorner.me/attack-on-titan-day-celebrated-with-99-announcements-new-key-visual-video-hajime-isayama-art-youtube-channel-and-more/)).

---

## 12 · Videojuegos

| Juego | Qué aporta | Fuentes |
|---|---|---|
| ***Attack on Titan 3*** (Koei Tecmo y Omega Force, **10-dic-2026**; PS5, Switch 2, Xbox Series y Steam) | Cuenta **toda la historia, hasta la temporada final**. Trae la «Investigación fuera de las murallas» (壁外調査): formas tu propio escuadrón, reclutas soldados y amplías una base. También creación de personaje, trato con Eren, Mikasa y Armin, y un modo casual. El **opening es de MAPPA** y llega en una actualización gratis. | [ANN](https://www.animenewsnetwork.com/news/2026-08-03/koei-tecmo-attack-on-titan-3-game-video-reveals-december-10-release/.240237) · [Famitsu (JA)](https://www.famitsu.com/article/202606/78936) · [4Gamer (JA)](https://www.4gamer.net/games/013/G101375/20260702018/) · [web oficial](https://www.koeitecmoamerica.com/attackontitan3/us/) · [web japonesa](https://www.gamecity.ne.jp/shingeki3/jp/) · [shingeki.tv](https://shingeki.tv/news/archives/9459) |
| *Wings of Freedom* (2016) | Cuenta los 33 primeros capítulos del manga | [TCRF](https://tcrf.net/Attack_on_Titan) · [Wikipedia](https://en.wikipedia.org/wiki/Attack_on_Titan_(video_game)) |
| *Attack on Titan 2* (2018) y *Final Battle* | la vida en el campamento y la amistad. TCRF documenta iconos sin usar (un caballo y «Unknown Character» 42/43). | [TCRF](https://tcrf.net/Attack_on_Titan_2) · [Gaming Trend](https://gamingtrend.com/reviews/dismember-the-titans-attack-on-titan-2-final-battle-review/) |
| *Attack on Titan: Assault* (móvil) | RPG por turnos con gacha; cerró en junio de 2020 | [TCRF](https://tcrf.net/Attack_on_Titan:_Assault) |
| *Attack on Titan TACTICS* (móvil) | personajes chibi, con historia original | [TCRF](https://tcrf.net/Attack_on_Titan_TACTICS) |
| *AoT VR: Unbreakable* (Meta Quest) | eres un recluta nuevo, con Eren, Mikasa, Armin y Levi | [UploadVR](https://www.uploadvr.com/attack-on-titan-unbreakable-review/) · [Screen Rant](https://screenrant.com/attack-on-titan-vr-unbreakable-review/) |

**La interfaz de *Attack on Titan 3*, vista en la demo** ([vídeo](https://www.youtube.com/watch?v=R2KM0OgyU-M),
*storyboard* de 320×180, un fotograma cada 5 s; borroso, así que es aproximado):
- **Diálogo en escena**: subtítulo blanco centrado abajo, «Nombre：frase», **sin
  caja**, sobre bandas negras de cine ([0:05](https://www.youtube.com/watch?v=R2KM0OgyU-M&t=5)).
- **Diálogo jugando**: **retrato cuadrado pequeño** de quien habla, su nombre
  encima y dos líneas de texto blanco, **sin caja**, abajo al centro; minimapa
  redondo de papel sepia abajo a la izquierda ([0:45](https://www.youtube.com/watch?v=R2KM0OgyU-M&t=45)).
- **Título de misión** («DEFENSE MISSION / 防衛戦»): **una franja ancha de
  pincel oro viejo** arriba (medida `#6D5A1B`-`#7E6922`), con un emblema en un
  rombo a la izquierda, letras latinas pequeñas y espaciadas y el título
  japonés en mincho oscuro; debajo, el mapa de la misión en papel sepia con una
  flecha roja ([2:55-3:00](https://www.youtube.com/watch?v=R2KM0OgyU-M&t=175)).
  **Es casi el mismo oro viejo que la cinta de la ficha del ep. 16**
  (`#6D581E`-`#796120`): la cinta de pincel sigue siendo el sello de la
  franquicia en 2026.
- Arriba a la derecha hay un recuadro con una persona con bufanda roja: es de
  la grabación, no de la interfaz del juego.

**Los menús de *Attack on Titan 3*, en las capturas oficiales de Steam**
(API `appdetails` de la app 2916700, 10 capturas de 1920×1080; las miré):
- **Mejorar equipo** ([captura](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2916700/228cc88fa364676b8dfd4a82b7cac9fe578cb8ec/ss_228cc88fa364676b8dfd4a82b7cac9fe578cb8ec.1920x1080.jpg)):
  la hoja de la espada sobre **un plano técnico en pergamino manchado**
  (`#7B6953`-`#AD9981`), encima de **una mesa de madera oscura** (`#32281F`-`#504742`),
  con **clavos y un martillo** al lado. Los datos van a la derecha, en blanco,
  sobre franjas grises translúcidas (`#3C352F`), separados por líneas finas. El
  elegido brilla en **dorado** (`#B0944B`, destello `#F3C13C`). Arriba a la
  izquierda, el emblema de los cadetes dibujado a línea dorada, como un sello.
  **Es el objeto del concepto A**: papel viejo clavado sobre madera.
- **Crear personaje** ([captura](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2916700/525910341eb688c952e7e6b32c9b4e88e0d3576e/ss_525910341eb688c952e7e6b32c9b4e88e0d3576e.1920x1080.jpg)):
  paneles oscuros (`#1D1815`) con **esquinas cortadas en diagonal**, la fila
  elegida con **degradado dorado** (`#9B7C50`) y **rombos dorados** en los
  deslizadores. Letra de los menús: sans humanista cursiva, en blanco roto.

**La caja de diálogo de *Attack on Titan 2*, por fin vista** (web oficial
japonesa, [sección «日常パート» y «交流»](https://www.gamecity.ne.jp/shingeki2/system2.html);
12 capturas de 960×540, miradas):
- **No hay caja.** El nombre va pequeño a la izquierda (リヴァイ), encima de
  **una línea fina color crema** (`#CDC9BE`) que se deshace hacia la derecha.
  Debajo, **dos líneas de texto blanco cálido** (`#FFFDF2`) con sombra negra
  (`#0C0C0A`), sangradas. Al final, a la derecha, **una marca ✓** para seguir
  ([captura de Levi](https://www.gamecity.ne.jp/shingeki2/images/img-system21-1.jpg)).
- **Con respuestas**: tres opciones a la derecha, cada una con **su botón
  redondo** (triángulo, cuadrado, equis) ([captura de Krista](https://www.gamecity.ne.jp/shingeki2/images/img5-3.jpg));
  si aciertas, sale **un corazón con una barra verde** de amistad ([otra](https://www.gamecity.ne.jp/shingeki2/images/img5-4.jpg)).
- **Levi con la ropa de limpiar, en el juego**: **pañuelo blanco en la cabeza y
  otro tapándole nariz y boca**, camisa blanca y correas, en un patio de piedra
  con sacos y cajas. Dice: 「……まぁいい、むしろ好都合だ　ちょうど、お前に
  話があったんでな」 («…Bueno. Mejor así. Justo tenía algo que decirte»;
  traducción nuestra) ([captura](https://www.gamecity.ne.jp/shingeki2/images/img-system21-1.jpg)).
- **Los cadetes barren el patio con escobas de ramas**, levantando polvo, y
  **Levi los vigila en el centro**, de pie y con los brazos caídos; detrás, un
  campanario de piedra y cielo azul ([captura](https://www.gamecity.ne.jp/shingeki2/images/img-system1-4.jpg)).
  Es la «vida en el campamento» de §7.3: **limpiar bajo la mirada de Levi
  también es parte de los juegos** (la web no dice si es castigo).

De *Wings of Freedom* las 5 capturas de Steam (app 449800) son de combate, sin
diálogo; las 5 de *AoT 2* en Steam (app 601050), igual. Ahí sí enseñan que
**Levi coge las hojas al revés** también en 3D ([captura](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/449800/ss_0d04e9e2182378c8c54075fa18a9eda33076e092.1920x1080.jpg)).

---

## 13 · Lo que ama el fandom, y qué NO hacer

**Lo que todos reconocen:**
- **Levi limpiando** (ep. 15), con pañuelo en la cabeza y en la boca. Tiene su
  propia página en [Know Your Meme](https://knowyourmeme.com/memes/cleaning-levi).
  Existe hasta el aspirador oficial con su voz.
- **«¡Soldados, rujan!»**: *copypasta* desde 2019 ([Know Your Meme](https://knowyourmeme.com/memes/erwin-smiths-my-soldiers-rage-speech)).
- **«Abandona tu sueño y muere»**: meme y momento cumbre de Levi y Erwin
  ([Goodreads](https://www.goodreads.com/quotes/10734692-give-up-on-your-dreams-and-die-levi-ackerman)
  · [TikTok](https://www.tiktok.com/discover/give-up-on-your-dreams-levi-meme)).
- **«¡Consagren sus corazones!»** en latino, con el saludo.
- **Hange y sus titanes Sonny y Bean**. Los nombres vienen del caníbal escocés
  Sawney Bean ([Fandom](https://attackontitan.fandom.com/wiki/Bean)).
- **La estatura de Levi**: 1,60 m, más bajo que casi todos
  ([Wikipedia](https://en.wikipedia.org/wiki/Levi_Ackerman)). Isayama le dio la
  estatura de Rorschach, y la manía de la limpieza para ser su contrario. El
  fandom chino lo llama **一米六**, «uno sesenta» ([Bangumi](https://bgm.tv/character/19546)).
- **«Tatakae»** («pelea») es palabra de culto; hasta hay bots con ese lema
  ([FoundingTitanRobot](https://github.com/asadali32117/FoundingTitanRobot)).
- **Reddit confirma que la limpieza es lo más querido de Levi** (r/ShingekiNoKyojin,
  por el archivo de Arctic Shift, búsqueda «Levi cleaning» en títulos):
  - «It's nice how Levi's clean-freak nature was shown right off the bat…»:
    **4275 votos** ([hilo](https://www.reddit.com/r/ShingekiNoKyojin/comments/ut4ps9/)).
  - «Captain Levi's Cleaning Crew», fan art de **しょくむら**: 2289 votos
    ([hilo](https://www.reddit.com/r/ShingekiNoKyojin/comments/ogpsyq/));
    del mismo autor, «Levi and his cleaning squad» (158).
  - «Eren about to be told off by Levi for not cleaning his windows» (399):
    **el chiste de «regañar por limpiar mal» ya es del fandom** (concepto A).
  - Existe hasta una figura oficial *figma* de Levi limpiando (hilos de 2014 con
    202 y 211 votos).

**Qué NO hacer (lo que a un fan le sonaría falso):**
- Levi **sonriendo abierto** o gritando de alegría. Casi no muestra emociones
  ([Fandom](https://attackontitan.fandom.com/wiki/Levi_Ackerman)).
- Levi **más alto** que Eren o que Erwin.
- **El saludo con la mano equivocada.** Es el puño **derecho** al corazón (se ve en G1).
- **Mezclar épocas**: la chaqueta marrón con la capa es de T1 a T3. La ropa negra
  y el pelo largo de Eren son de la temporada final. No juntar las dos sin motivo.
- **Erwin pierde el brazo derecho en el ep. 36 (T2)** ✅ (subtítulos de
  Netflix, 16:05-16:21, y la [ficha del anime en la wiki](https://attackontitan.fandom.com/wiki/Erwin_Smith_(Anime)):
  «se lo arrancó un titán justo debajo del hombro»). En el ep. 16 tiene los dos
  brazos; después, sólo el izquierdo. Y **desde entonces saluda con la mano
  izquierda**, «lo que se considera un saludo incorrecto» (misma ficha, ep. 49):
  si Erwin saluda después de la T2, con la izquierda.
- Pintar el verde de la Legión como **verde hierba**, o la bufanda **roja
  chillona** (ver los hex).
- Poner en boca de Levi **una frase latina inventada** como si fuera cita. Las
  que tienen fuente están en §9.3; lo demás, marcarlo como texto nuestro.

---

## 14 · Los personajes a fondo

### Levi Ackerman: el más querido
- **Carácter**: obsesionado con la limpieza. Limpia hasta las hojas en pleno campo
  de batalla, pero toca la mugre si hace falta. Es seco, grosero y de humor negro.
  Casi no muestra emociones y parece frío. En el fondo **cuida a los suyos y no
  soporta las muertes inútiles**
  ([Fandom](https://attackontitan.fandom.com/wiki/Levi_Ackerman) ·
  [Wikipedia](https://en.wikipedia.org/wiki/Levi_Ackerman) ·
  [CBR](https://www.cbr.com/attack-on-titan-levi-meaningful-death-devotion-debate/)).
- **Su herida**: en *No Regrets* murieron dos amigos suyos por una decisión suya.
  Por eso para él **elegir** pesa tanto
  ([Selvy (JA)](https://selvy.jp/attackontaitan-levi-meigen/) ·
  [Torchlight Hub (JA), sobre su manía de limpiar](https://torchlight-hub.com/archives/200/levinokeppeki/)).
- **Cómo habla**: frases cortas, órdenes y sarcasmo. Si explica, lo hace deprisa y
  deja que el otro elija: «elige lo que no te deje arrepentimiento». Se enfada en
  frío, sin gritar: patea. **No se ríe.**
- **Con quién**: Erwin (lealtad total), Hange (vieja camaradería), Eren (lo
  vigila y lo protege) y su escuadrón.
- **Cuerpo**: tieso, brazos cruzados, mirada de párpado caído. Coge la hoja **al
  revés** (G2). Isayama lo volvió a dibujar **de brazos cruzados** en 2026 (§2.1).
- **La taza de té**: bebe té negro y **coge la taza por el borde, desde
  arriba, sin tocar el asa**. En el capítulo extra «Bad Boy» explica por qué:
  de niño se le rompió el asa de la taza de su madre ([wiki, «Bad Boy»](https://attackontitan.fandom.com/wiki/Bad_Boy) ·
  [Wikipedia en chino, lista de personajes](https://zh.wikipedia.org/wiki/%E9%80%B2%E6%93%8A%E7%9A%84%E5%B7%A8%E4%BA%BA%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8):
  「喜欢喝红茶且持茶杯方式极为特殊」). Es un gesto que el fan reconoce al
  instante: **sirve para «pensar» o para presentar con calma**, taza en mano,
  en una mesa como la de [H5](https://static.wikia.nocookie.net/shingekinokyojin/images/e/ed/Hange_and_Levi_have_tea_with_the_reporters.png/revision/latest?cb=20240223053002).
- **Cómo se expresa, en pantalla** (subtítulos de Netflix; traducción nuestra
  salvo lo marcado como latino):
  - **se queja de la suciedad antes que del peligro**: mata a un titán, se mira
    la mano y dice «Tch… qué asco» (ep. 9 · 06:01-06:04);
  - **da órdenes en una línea**: «Eso es un problema grave. Empecemos ya»
    (ep. 15 · 04:55-04:59), «Es una regla que hay que cumplir» (05:38),
    «Esto no vale nada. Hazlo todo otra vez» (07:12-07:14);
  - **responde seco a lo que no le importa**: Hange pregunta qué hará Eren
    mañana y Levi contesta «Limpiar el jardín» (ep. 15 · 10:42-10:45);
  - **promete poco y en serio**: «Tu determinación me dará fuerza. Eso te lo
    prometo» (latino, ep. 9 · 06:57);
  - **así lo ven los suyos**: Petra, «Aquí la regla es el capitán» (06:01) y
    «es más bajo de lo que crees, maniático, brusco y difícil de tratar»
    (06:16-06:22).
  - **Saluda** con el puño derecho al corazón, sin gesto en la cara (P·17,
    E·17). **Se ríe** casi nunca (P·19, una sonrisa pequeña).

### Erwin Smith: el segundo más querido (ganó la 3.ª encuesta)
- **Carácter**: el comandante que se juega todo por la verdad. Pide sacrificios
  y los dice de frente: el 60 % murió.
- **Cómo habla**: discursos con preguntas y un remate que se grita, como
  «¡Consagren sus corazones!» o «¡Soldados, rujan!». Primero da el dato duro
  («en esos cuatro años murió más del 60 %», ep. 16 · 11:19), luego pregunta
  (en latino: «¿Morirían si yo les ordenara matarse?», 13:52) y al final grita el lema (14:13).
  Con Eren, tras el juicio, es cortés: «Tienes todo mi respeto» (latino,
  ep. 14 · 21:09).
  ([Know Your Meme](https://knowyourmeme.com/memes/erwin-smiths-my-soldiers-rage-speech) ·
  [Medium](https://medium.com/@matthew.starkey_79206/erwin-smith-leader-warrior-devil-512b8bd6c5c)).
- **Con quién**: Levi, que al final le da permiso para morir (ep. 53).

### Hange Zoë: tercera en la última encuesta
- **Carácter**: científica excéntrica y de mucha energía. Cambia a comandante
  solemne tras morir Erwin: es la 14.ª comandante. Tiene **compasión hasta por
  los titanes**: llora cuando le hacen daño a Bean. Empezó odiando a los titanes
  hasta que notó que pesaban muy poco
  ([Fandom](https://attackontitan.fandom.com/wiki/Hange_Zo%C3%AB) ·
  [Fandom: Sawney](https://attackontitan.fandom.com/wiki/Sawney_(Anime))).
- **Cómo habla**: rápido, con entusiasmo y explicando de más. Les pone nombre a
  sus sujetos de estudio (traducción nuestra de los subtítulos japoneses, salvo
  lo marcado como latino). **Saluda** con alegría a todo el grupo: «¡Buenas
  noches, escuadrón Levi! ¿Qué tal se vive en el castillo?» (ep. 15 · 10:00);
  pide las cosas **exagerando**: el experimento será «¡de lo más emocionante!»
  (10:30); **se presenta con su cargo completo** en el doblaje: «Soy líder de la
  Cuarta División de la Legión de Exploración, Hange Zoë» (latino, ep. 14 ·
  08:37). Bautiza a sus titanes Sonny y Bean (14:15-14:17).
- **Para la lámina**: sería la que **explica** las normas como un experimento,
  con notas y dibujos.

### Eren Jaeger: el protagonista, cuarto
- Impulsivo y gritón. En el juicio acaba **encadenado de rodillas**. En la
  temporada final tiene el pelo largo, está sereno y da miedo (G4).
- Para #reglas es **el que las rompe**. Sirve como ejemplo, no como portavoz.

### Mikasa Ackerman
- De niña era alegre. Tras el asesinato de sus padres se vuelve callada y
  protectora. **La bufanda que le dio Eren es su hogar**
  ([Wikipedia](https://en.wikipedia.org/wiki/Mikasa_Ackerman) ·
  [Poggers](https://poggers.com/blogs/anime/attack-on-titan-mikasa-ackerman)).
- En la temporada final lleva el pelo aún más corto.
- Pocas palabras. Pose de guardia.

### Secundarios para este canal
- **Keith Shadis**, el instructor del ep. 3: el sargento que humilla a gritos a
  los reclutas. Perfecto para «las normas se cumplen»
  ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/DrillsergeantNasty) ·
  [namu.wiki (EN)](https://en.namu.wiki/w/%ED%82%A4%EC%8A%A4%20%EC%83%A4%EB%94%94%EC%8A%A4)).
- **Darius Zackly**, el juez del ep. 14: el que dicta sentencia
  ([Fandom](https://attackontitan.fandom.com/wiki/Can%27t_Look_into_His_Eyes_Yet:_Eve_of_the_Counterattack,_Part_1)).

### 14.1 · Qué transmite cada uno (repaso corto)

- **Levi**: control total, aunque no lo tenga. Su cara casi no cambia ni en
  peligro; por eso, cuando se le quiebra la voz (con Erwin, ep. 55 ·
  21:31-21:47), pesa el doble. Manda porque sabe, no porque quiera el puesto:
  **no se ve como un líder igual que Erwin** ✅ [Fandom, Personality](https://attackontitan.fandom.com/wiki/Levi_Ackerman#Personality).
  Verlo da **seguridad** y un poco de miedo.
- **Erwin**: la calma de quien ya decidió que su vida es un precio. La misma
  cara fría (P·6) con la que manda a morir a los suyos… hasta la agonía del
  ep. 55, donde vuelve a ser un niño que levanta la mano. Deja **respeto y
  tristeza**.
- **Hange**: la única alegría de verdad del grupo. Curiosidad sin filtro
  (P·25, H1), a propósito contra la seriedad de Levi y Erwin. Deja **ganas de
  saber más**, y alivio.
- **Eren**: de la mirada asustada y con esperanza (ojos muy abiertos, sangre
  en la cara) al vacío de la temporada final. La serie **mide con su cara
  cuánto ha cambiado todo**. Deja **inquietud**.
- **Mikasa**: una calma que le cuesta mantener. La cabaña del ep. 93 es la
  única vez que se la ve relajada de verdad: la cara que nunca pudo tener.
  Deja **ternura y pena**.
- Fuente: `partes/voz.md` (lectura del investigador sobre la wiki y los
  fotogramas que miró) ⚠️ interpretación, no cita oficial, salvo lo enlazado.

### 14.2 · Su cara en cada emoción (fotograma y minuto)

Cruza lo que miró el investigador de voz (4 fotogramas nuevos de la wiki,
1920×1080 o más, tamaño por API) con las hojas P· y las poses de §15. El
minuto sale de los subtítulos japoneses de Netflix (Punto 21).

| | Alegría | Rabia | Tristeza | Miedo | Vergüenza o guardia baja |
|---|---|---|---|---|---|
| **Levi** | P·19, sonrisa pequeña (casi única) | P·12 · ep. 14 · 18:33, la patada: rabia **fría**, sin gritar | P·17, último saludo (T4, vendado) | **No encontré** ninguno: casi no muestra emociones | P·16, escucha con la mirada baja; ep. 55 · 21:31-21:47 le habla al cadáver de Erwin (sin fotograma ⚠️) |
| **Erwin** | **No encontré** alegría plena (una media sonrisa en el ep. 16, sin fotograma ⚠️) | P·21 y P·23 gritan; P·22 · ep. 53 · 21:51, la carga | [`Erwin_asks_a_question.png`](https://static.wikia.nocookie.net/shingekinokyojin/images/e/e0/Erwin_asks_a_question.png) · ep. 55 · 19:08-19:20: delira, levanta la mano, mirada perdida | P·22, boca y ojos muy abiertos: miedo contenido ⚠️ (lectura) | la misma del ep. 55: el único momento vulnerable de su arco |
| **Hange** | H1 (eps. 14-16), gafas que brillan y sonrisa de oreja a oreja; P·25 | **No encontré** rabia pura; H6 (T3 parte 2) grita la orden: determinación ⚠️ | llora por Bean (texto, §14); sin fotograma ⚠️ | **No encontré** | P·26, entusiasmo torpe con la lanza rayo; H2, se arrima a Levi, que mira a otro lado harto |
| **Eren** | **No encontré** alegría plena ⚠️ | R3 · ep. 1, niño, de espaldas, **puños apretados** ante dos soldados; R2 llora de rabia (en la hoja de poses, sin enlace ⚠️) | [`Eren_hears_Armin_breathe.png`](https://static.wikia.nocookie.net/shingekinokyojin/images/d/d0/Eren_hears_Armin_breathe.png): ojos muy abiertos, sangre en la mejilla (episodio no anotado ⚠️) | la misma: miedo y esperanza a la vez | R6 · ep. 3, **cabeza abajo** en el aparato de equilibrio delante de toda la promoción |
| **Mikasa** | [`Mikasa_sees_a_reality…png`](https://static.wikia.nocookie.net/shingekinokyojin/images/c/cc/Mikasa_sees_a_reality_where_she_and_Eren_remained_together.png) · ep. 93 · 16:39-17:03: sentada, tranquila, la única vez | M3 (eps. 14-16, tras la patada): **ojos en sombra**, boca recta, bufanda subida; M2, fastidio de reojo | P·29, se toca la bufanda y sonríe con lágrimas; ep. 93 · 17:25-17:29 «Perdón… no puedo» | **No encontré** | [`Mikasa_and_Armin_watch_Sasha_pass_away.png`](https://static.wikia.nocookie.net/shingekinokyojin/images/3/39/Mikasa_and_Armin_watch_Sasha_pass_away.png) (1920×2142) · ep. 67 · 14:24-14:37: **de espaldas, la cara oculta**, así esconde el dolor |

- **Lo que dice la tabla**: Levi, Erwin, Eren y Mikasa **casi nunca sonríen
  ni se avergüenzan en pantalla**. Para #reglas, la cara seria es la buena;
  nunca «sonriendo mucho» salvo Hange (va también a §18).
- Corregido de la parte de voz: la cara de Hange no es P·9 (P·9 es Zackly) y
  la rabia de Eren no es E·12 (E·12 es la hoja en la mesa). La rabia de
  Mikasa **sí tiene fotograma** (M3), aunque la parte decía que no.

### 14.3 · Dinámicas (para láminas en grupo)

- **Levi ↔ Erwin**: hablan **de tú a tú**, con pullas; Levi le habla mal
  hasta a él, pero **es el único al que obedece sin dudar** ✅
  [Fandom, Relationships de Levi](https://attackontitan.fandom.com/wiki/Levi_Ackerman#Relationships).
  Al final Levi decide por él que ya puede descansar (ep. 55).
- **Levi ↔ Hange**: confianza de años. Levi cree en sus teorías aunque no le
  gusten, y la frena cuando se emociona de más ✅ (misma fuente). Hange dijo
  que con quien mejor se llevaba era con Levi ✅ ([Fandom, Trivia de Hange](https://attackontitan.fandom.com/wiki/Hange_Zo%C3%AB#Trivia),
  *Bessatsu Shōnen*, abr-2016). Gag: Levi la bañaba a la fuerza cuando iba
  demasiado sucia ⚠️ una fuente. Pose: H2.
- **Levi ↔ Mikasa**: **empiezan mal**. Ella le guarda rencor por la patada del
  juicio (M3) y jura hacérselo pagar; tras la muerte del Escuadrón Levi,
  confía en él ✅ (Relationships de Levi). Sirve para «de la desconfianza a
  respetar las reglas». **Es con quien discute Mikasa.**
- **Levi → Armin**: mentor callado. Lo sostiene cuando duda (tras matar a un
  soldado para salvar a Jean) y le dice que tiene «poderes y habilidades que
  nadie más tiene» ✅ (misma fuente).
- **Erwin ↔ Nile**: de la misma promoción; iban a entrar juntos en la Legión,
  pero Nile se enamoró de Marie y se fue a la Policía Militar. Distanciados,
  con confianza de fondo: Erwin le avisa antes del golpe de estado ✅
  [Fandom, Relationships de Erwin](https://attackontitan.fandom.com/wiki/Erwin_Smith#Relationships).
- **Mikasa ↔ Eren**: la bufanda. Él le pide, en la cabaña, que la tire y lo
  olvide; ella no puede (ep. 93, Punto 21).
- **Quién los hace reír**: casi nadie; es un grupo serio por diseño. Dentro
  de los cinco, sólo **Hange** (torpeza con entusiasmo, P·26); fuera, **Sasha**
  (la patata, P·27).

---

## 15 · Poses, analizadas

Códigos: P·, E·, F· = celdas de las hojas (§2.0, tamaño medido); G = copias de
GitHub (§2); «clip» = hojas de fotogramas por *storyboard* (±1-2 s, §11). El
minuto del episodio sale de los subtítulos de Netflix.

**Levi** (el más querido: 10 poses)

| Dónde | Qué hace (postura, manos, mirada) | Sirve para |
|---|---|---|
| P·1 (arte oficial WIT) | de pie, **brazos cruzados**, entre Eren y Mikasa; mirada de lado | **presentar** |
| Dibujo de Isayama 2026 (§2.1) | delante de Eren, **brazos cruzados**, ceño fruncido, mira al frente | **presentar** o **regañar** |
| G2 | tres cuartos, **hoja al revés** hacia abajo, capa al viento, párpado caído | presentar |
| [clip 0:14](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=14) · ep. 15 · 04:59 | capa verde cerrada y chorrera blanca, de frente, **párpado caído**: «empecemos ya» | **explicar** una orden |
| P·10 · [clip 0:32-0:34](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=32) · ep. 15 · ~05:17 | pañuelo en la cabeza; con dos dedos **se baja el pañuelo de la boca**; ventana con cielo detrás | **regañar con humor** (concepto A) |
| P·11 | pasa **el dedo** por el marco de una ventana de celosía y mira el polvo | **regañar**, inspeccionar |
| [clip 2:24-2:28](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=144) · ep. 15 · 07:09-07:14 | con pañuelo, **asoma en la puerta de piedra**, mira de arriba abajo: «hazlo todo otra vez» | **regañar** |
| P·13 · ep. 14 · 13:50 | de pie, cuerpo recto, cara en sombra, **mira de reojo** a los mercaderes | **advertir** |
| P·12 · ep. 14 · 18:33 | de pie junto a Eren caído, en el juicio | **sancionar** (sin sangre en la lámina) |
| P·16 | primer plano, mirada baja, escucha | **pensar** |
| P·17 | saludo final, puño al corazón (T4, vendado) | **despedir**, aceptar |
| P·19 | sonrisa pequeña, casi única | **celebrar**, con cuidado |
| [clip 1:08](https://www.youtube.com/watch?v=wOzu2yF4HC4&t=68) · ep. 73 | en el aire, capa abierta, hojas en las manos | **animar** (T4) |

**Erwin**

| Dónde | Qué hace | Sirve para |
|---|---|---|
| P·20 · ep. 14 · 20:03 | de frente, sereno, habla al tribunal | **explicar** |
| E·13 · ep. 16 · 08:59 | en alto, de noche; los reclutas lo miran desde abajo | **explicar** a un grupo |
| E·14 · ep. 16 · 14:13 | los nuevos saludan con antorchas detrás de él | **aceptar** (concepto C) |
| E·16 | de perfil, de noche, antes de salir | **pensar** |
| P·21 y P·23 | grita a sus soldados; en P·23 (T3) con la espada | **animar** |
| P·22 · ep. 53 · 21:51 | a caballo, un solo brazo, grita | **animar** a lo grande |
| [OP 1:12](https://www.youtube.com/watch?v=43spp3kzGVw&t=72) | cara seria sobre negro | presentar con peso |

**Hange**

| Dónde | Qué hace | Sirve para |
|---|---|---|
| P·24 · ep. 15 · 10:13 | inclinada sobre la mesa, sonríe; Eren la escucha | **explicar** con entusiasmo |
| P·26 | ante la pizarra, sujeta la lanza rayo | **explicar** con esquema |
| P·25 | en acción junto a la cara de un titán, emocionada | **celebrar**, pasión |
| E·9 · ep. 14 | de pie, gafas, junto a Mike | presentar |
| [tráiler latino 0:30](https://www.youtube.com/watch?v=sFuAhHTgABs&t=30) | T4: capa verde, parche, de frente, brazos caídos | presentar (T4) |
| [H1](https://static.wikia.nocookie.net/shingekinokyojin/images/0/0c/Hange_has_found_a_listener.png/revision/latest?cb=20130721120241) · 919×520 · eps. 14-16 (la noche en que le explica todo a Eren) | primer plano en penumbra, **las gafas brillan** y sonríe de oreja a oreja | **explicar de más**, con humor |
| [H2](https://static.wikia.nocookie.net/shingekinokyojin/images/2/24/Hange_teases_Levi_as_they_leave_Trost_District.png/revision/latest?cb=20170921135907) · 1920×1080 · arco de Trost | con capa, **se inclina hacia Levi y sonríe**; Levi mira a otro lado, harto | **presentar** a los dos juntos |
| [H3](https://static.wikia.nocookie.net/shingekinokyojin/images/4/4d/Hange_examines_an_object.jpg/revision/latest?cb=20170415044048) · 1920×1080 · T2 | inclinada sobre un **microscopio de latón**, entre torres de libros, frascos y un **quinqué** encendido | **pensar**, estudiar (sitio para una lámina de Hange) |
| [H4](https://static.wikia.nocookie.net/shingekinokyojin/images/1/17/Hange_holds_a_meeting_in_Ehrmich.png/revision/latest?cb=20170715003338) · 1600×900 · T2 | de pie ante una mesa, a la luz de velas, con soldados encapuchados alrededor | **explicar** a un grupo |
| [H5](https://static.wikia.nocookie.net/shingekinokyojin/images/e/ed/Hange_and_Levi_have_tea_with_the_reporters.png/revision/latest?cb=20240223053002) · 1920×1080 · T3 parte 2 | vista cenital: mesa redonda con té; Hange y Levi con dos periodistas | conversar, acordar |
| [H6](https://static.wikia.nocookie.net/shingekinokyojin/images/1/1d/Hange_orders_to_attack_again.png/revision/latest?cb=20240222231531) · 1703×1080 · T3 parte 2 | agachada en un tejado, **grita la orden** con la mano abierta hacia delante | **animar**, ordenar |

Las H1-H6 las miré en una hoja propia (tamaño por la API de la wiki; el arco sale de la [galería de Hange](https://attackontitan.fandom.com/wiki/Hange_Zo%C3%AB_(Anime)/Image_Gallery)).

**Mikasa**

| Dónde | Qué hace | Sirve para |
|---|---|---|
| P·4 / G1 | saluda, puño derecho al corazón, bufanda | **aceptar** |
| MAPPA 15 (§2.1) | **de espaldas**, sube hacia el árbol | **celebrar**, final |
| P·29 | se toca la bufanda, sonríe con lágrimas | calma |
| [ED 1:20](https://www.youtube.com/watch?v=eN_rq3FvJUs&t=80) | sepia, se toca la bufanda, mira de lado | **pensar** |
| [PV 0:06-0:08](https://www.youtube.com/watch?v=KKzmOh4SuBc&t=6) | niña con la bufanda roja y leña a la espalda | presentar (infancia) |
| [M1](https://static.wikia.nocookie.net/shingekinokyojin/images/a/a0/Mikasa_during_the_military_training.png/revision/latest?cb=20240124040551) · 1920×1080 · eps. 3-4 (instrucción) | en el aire con el equipo, **hojas abiertas**, bufanda al viento, cara impasible | **presentar** en acción |
| [M2](https://static.wikia.nocookie.net/shingekinokyojin/images/b/b1/Mikasa_is_not_amused.png/revision/latest?cb=20240124101659) · 1920×1080 · eps. 14-16 | la mejilla apoyada en la mano, **mira de reojo**, fastidiada, entre los reclutas | **regañar en silencio** |
| [M3](https://static.wikia.nocookie.net/shingekinokyojin/images/7/7b/Mikasa%27s_anger_with_Levi%27s_actions.png/revision/latest?cb=20240124065952) · 1920×1080 · eps. 14-16 (tras la patada del juicio) | **ojos en sombra**, boca recta, bufanda subida: rabia contenida contra Levi | **advertir** |
| [M4](https://static.wikia.nocookie.net/shingekinokyojin/images/d/d5/Mikasa_threatens_a_merchant.png/revision/latest?cb=20180721195714) · 1920×1080 · arco de Trost | **estira la hoja** hacia el mercader que tapa la puerta; mirada fría, de lado | **advertir** (sin sangre) |
| [M6](https://static.wikia.nocookie.net/shingekinokyojin/images/b/ba/Mikasa_comforts_Armin.png/revision/latest?cb=20240131070631) · 1920×1080 · T3 parte 1 | mirada blanda, **la mano en el hombro de Armin**, fusil a la espalda | **animar** |

Las M1-M6 las miré en la misma hoja (la M5, Mikasa seria junto a Historia, no aporta pose).

**Eren**

| Dónde | Qué hace | Sirve para |
|---|---|---|
| P·4 / G1 | en el centro, saluda, cara decidida | **aceptar** |
| E·10 · [clip 0:48-0:54](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=48) | pañuelo de limpiar al cuello, serio, escucha | **el que obedece** (concepto A) |
| E·3 · ep. 14 | de rodillas, encadenado al poste | **el que rompe las reglas** |
| Dibujo de Isayama 2026 | adulto, **puño en alto**, ojos muy abiertos | amenaza (T4) |
| G4 | levanta la mano herida, a contraluz | amenaza (T4) |
| [R1](https://static.wikia.nocookie.net/shingekinokyojin/images/c/ca/Eren_becomes_a_soldier.png/revision/latest?cb=20130829142128) · 823×720 · eps. 3-4 | colgado **recto** en el aparato de equilibrio; Shadis, de espaldas, lo mira desde abajo | **cumplir** la prueba: celebrar |
| [R6](https://static.wikia.nocookie.net/shingekinokyojin/images/2/2d/Eren_upside_down_during_his_balance_test.jpg/revision/latest?cb=20161019014719) · 1280×1399 · ep. 3 | **cabeza abajo** en el mismo aparato, delante de toda la promoción en fila | **el que falla** (humor; el reverso de R1) |
| [R3](https://static.wikia.nocookie.net/shingekinokyojin/images/d/d9/Eren_confronts_a_military_guard.png/revision/latest?cb=20170731071336) · 1920×1080 · ep. 1 | Eren niño, de espaldas y **puños apretados**, planta cara a dos soldados de la Guarnición en la calle | **reclamar** (el que discute la norma) |
| [R4](https://static.wikia.nocookie.net/shingekinokyojin/images/2/26/Eren_talks_with_his_friends.jpg/revision/latest?cb=20170731070826) · 1920×1080 · eps. 3-4 | en la mesa del comedor, a la luz de una vela, **cuenta** con la cuchara en la mano; los demás lo escuchan | **explicar** |
| [R5](https://static.wikia.nocookie.net/shingekinokyojin/images/4/44/Eren_masters_using_ODM_gear.png/revision/latest?cb=20170804204232) · 1920×1080 · eps. 3-4 | vuela con el equipo **contra un atardecer dorado** | **animar** |

Las R1-R6 las miré en la hoja de poses (arco según la [galería de Eren](https://attackontitan.fandom.com/wiki/Eren_Jaeger_(Anime)/Image_Gallery); la R2, Eren llorando de rabia, no sirve para #reglas).

**Secundarios para este canal**

| Quién | Dónde | Qué hace | Sirve para |
|---|---|---|---|
| Keith Shadis | P·8 · ep. 3 · 01:39-04:03 | encara a cada recluta a gritos, muy cerca | **regañar** |
| Sasha | P·27 · ep. 3 · 04:40 | come la patata en plena formación | **el que rompe una norma** (humor) |
| Zackly | E·2, E·3 · ep. 14 · 10:29 | arriba en el estrado, mira hacia abajo | **dictar sentencia** (concepto B) |
| Nile | P·28 · ep. 14 · 11:38 | lee de un papel ante el tribunal | acusar |

## 16 · Vestuario

Descripción de la wiki ([«Military (Anime)», uniforme](https://attackontitan.fandom.com/wiki/Military_(Anime)))
cruzada con lo que se ve en las hojas; colores medidos con Pillow (§5).

| Época | Qué llevan | Colores medidos |
|---|---|---|
| Uniforme de combate, año 850 (T1-T3) ✅ | **chaqueta corta marrón claro** con el emblema del cuerpo **en los dos hombros, el bolsillo izquierdo y el centro de la espalda**; camisa clara; **faja marrón oscuro** sobre la cadera; **pantalón blanco**; **botas de cuero marrón oscuro hasta la rodilla**; correas del equipo (wiki + G1, G2, P·4) | chaqueta `#A1865D` a `#BFA97B` (arte limpio, G2); `#654327` a la luz de antorcha (E·14) |
| Reclutas (G1, P·4) | la misma chaqueta con las **espadas cruzadas** | chaqueta `#A07E57` en luz |
| Legión fuera de las murallas ✅ | **capa verde con capucha, hasta la cadera**, con las Alas de la Libertad en la espalda (wiki + clip del ep. 15, [0:08](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=8)) | capa `#1E261F` a `#3C4E3A`; con niebla `#465241` (E·17) |
| Uniforme de gala (todos los cuerpos) | **gabardina verde oliva** con los emblemas en los mismos sitios (wiki). La tropa del generalísimo lleva **emblemas en blanco** | — |
| Levi, ep. 15 | **pañuelo blanco en la cabeza** atado atrás, otro sobre la boca, camisa y correas (P·10, clip 0:32) | pañuelo `#F1EEE6` |
| Levi, siempre | **chorrera o pañuelo blanco al cuello** bajo la capa (clip [0:14](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=14)) | — |
| Temporada final, año 854 | **traje negro ajustado** con peto de metal y correas; Levi lleva el traje negro **con la capa verde de siempre** (wiki, ep. 65; G3) | capa `#33382B` |
| Mikasa | **bufanda granate** siempre; pelo corto, más corto en la temporada final; en MAPPA 15 lo lleva recogido | `#743D41` en luz; `#552C2D` en interior (P·29) |
| Eren, temporada final (G4) | pelo largo recogido, barba incipiente | piel `#B08E6A` |
| Con traje (arte de 2026) | Eren, Erwin y Levi con **traje de tres piezas** y corbata (tienda de la *Shonen Magazine*, §2.1). No es de la serie: no mezclar | — |

**Lo icónico que todos reconocen**: chaqueta marrón, capa verde con las alas
blancas y azules, pantalón blanco, botas altas y las correas del equipo de
maniobras. Es el look de T1 a T3. Para Levi, además, **el pañuelo de limpiar**.

---

## 17 · Ciudades, paisajes y fondos de pantalla

**Sitios con su luz** (detalle y hex en §5):
- **El viejo castillo-cuartel** (ep. 15): torres redondas de piedra clara,
  rosetón, hierba sin cortar, de día ([clip 0:04-0:12](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=4));
  dentro, muros de bloques con **luz blanca de ventana** (P·10-11) y el sótano
  con vela (E·8).
- **El tribunal** (ep. 14): interior alto, gris verdoso frío, juez arriba (E·1-4).
- **El patio de noche** (ep. 16): antorchas y luna (E·13-14).
- **Trost y Stohess**: tejados rojos, entramado de madera, nombres alemanes;
  la Muralla de bloques lisos enormes (E·21-25).
- **El cuartel de la T4** (ep. 71): patio de columnas de piedra y verja de
  hierro, de día ([clip 0:30-0:32](https://www.youtube.com/watch?v=nxQCiDpxeMY&t=30)).

**Fondos de pantalla oficiales** (medidos bajando la imagen, 24-sep-2026):

| Pieza | Tamaño | Enlace |
|---|---|---|
| Visual de MAPPA 15 (Mikasa y el árbol) | 1754×2481 | [imagen](https://static.animecorner.me/2026/06/1781686842-a154e001e82b5b0b09f3bf0eaffc3d2f.jpg) (copia de Anime Corner) |
| Visual de *Attack on Titan 3* | 1500×2121 | [portal](https://aot-portal.com/wp/wp-content/uploads/2026/09/No.68_%E3%80%90SGK%E3%80%91%E3%82%B2%E3%83%BC%E3%83%A0%E3%83%93%E3%82%B8%E3%83%A5%E3%82%A2%E3%83%AB%E7%89%88%E6%A8%A9_%E7%B4%8D%E5%93%81_RBG-1.jpg) |
| Visual «9/9» del Día de AoT | 1920×1730 | [portal](https://aot-portal.com/wp/wp-content/uploads/2026/09/SN_No.2_%E3%83%93%E3%82%B8%E3%83%A5%E3%82%A2%E3%83%AB%EF%BC%86%E3%83%AD%E3%82%B4%E7%94%BB%E5%83%8F.webp) |
| Carteles de las películas (ScreenX) | 1459×2062 cada uno | [1](https://aot-portal.com/wp/wp-content/uploads/2026/09/No.10_aot_GY_V.jpg) · [2](https://aot-portal.com/wp/wp-content/uploads/2026/09/No.11_aot_LA_V.jpg) |
| Concierto *Symphony from Paradis* | 1080×1080 | [portal](https://aot-portal.com/wp/wp-content/uploads/2026/09/No.14_20260320_AOT2_Web-illustration-originale-sans-aucune-modif-1080-x-1080.jpg) |
| Los reclutas saludan (P·4) | 3840×2160 | wiki (§2.0) |
| Arte oficial Eren, Levi y Mikasa (P·1) | 2500×3513 | wiki (§2.0) |

**Fondos de fans en alta** (Wallhaven, por su API, orden «más favoritos»,
búsqueda «attack on titan», 24-sep-2026; sólo los que sirven y son aptos):

| N.º | Qué es | Tamaño | Autor / fuente |
|---|---|---|---|
| W5 | minimalista: el Colosal asoma sobre la Muralla; abajo, una silueta con las alas en rojo, sobre gris azulado | 1920×1080 | **Deto15**, «Wir sind die Jäger» ([DeviantArt](https://www.deviantart.com/deto15/art/Wir-sind-die-Jager-460958222); [Wallhaven](https://wallhaven.cc/w/42v990), 289 favoritos) |
| W9 | un soldado con capucha y espada, en blanco y negro con ceniza | 1920×1080 | ArtStation [gJXR2E](https://www.artstation.com/artwork/gJXR2E) (autor sin ver: ArtStation dio 403) · [Wallhaven](https://wallhaven.cc/w/m93vg9) |
| W12 | Levi en estilo manga, blanco y negro, con sangre en la cara | 1920×1357 | ArtStation [dOQRvK](https://www.artstation.com/artwork/dOQRvK) (autor sin ver) · [Wallhaven](https://wallhaven.cc/w/96z1ww) |
| W8 | Eren de la T4 y otros entre estatuas blancas, luz clara de ventana | 1920×1080 | sin fuente · [Wallhaven](https://wallhaven.cc/w/gpqz2l) |
| G9 | el Colosal en 3D entre humo rojo | 6217×3713 | sin autor (copia en GitHub, §2) |

De los 12 primeros de Wallhaven, 4 son *fanservice* y 2 mezclan series: no
sirven. Para #reglas, **W5** (sobrio, paleta de la serie) es el único que
encaja como fondo; los demás, sólo como referencia de tono.

---

## 18 · Guía para generar con IA (Firefly o Canva)

**Rasgos que nunca cambian**
- **Levi**: pelo negro liso con raya al medio y **nuca rapada**; ojos estrechos
  **gris acero** con **ojeras**; cara joven y seria. **Bajo: 160 cm, 65 kg** ✅
  (ficha de la wiki, del folleto de la película, y Wikipedia). Pañuelo o
  chorrera blanca al cuello. Coge la hoja al revés y **la taza por el borde**
  (§14). No sonríe.
- **Erwin**: rubio con raya al lado, **cejas gruesas**, alto y ancho, corbata
  de bolo verde. **Un solo brazo (el izquierdo) desde el ep. 36** ✅.
- **Hange**: gafas, cola de caballo desordenada; en la temporada final, parche
  en un ojo (P·7).
- **Mikasa**: pelo negro corto y **bufanda granate** (no roja chillona).
- **Uniforme T1-T3**: chaqueta corta marrón claro con el emblema en hombros,
  bolsillo y espalda; faja marrón oscuro; pantalón blanco; botas marrones
  altas; correas; capa verde oliva con capucha (§16).

**Estilo**
- Anime japonés de los años 2010, estilo WIT Studio (T1-T3).
- **Contorno negro fino con muchas líneas de tensión** en cuello, ojos y
  pliegues de ropa.
- Sombra en dos tonos, dura. Poco brillo.
- Paleta apagada (§5): capa `#1E261F`-`#3C4E3A`, chaqueta `#A1865D`, piedra
  `#34362A`-`#595845`, cielo `#74A9CD`, tribunal `#455B5E`, antorcha `#D29258`.

**Cielo**: alto, azul limpio, con nubes finas de varios blancos (las «nubes
Yoshihara», §5). Palabras: *high thin cirrus clouds, layered whites, strong
blue contrast*.

**Luz**: tarde dorada con sombras frías (OP 0:20-0:24), antorcha de noche
(E·14, `#D29258`), luz blanca de ventana sobre piedra (P·10, clip del ep. 15)
o luz alta y fría del tribunal (E·1).

**Encuadre**: plano medio desde abajo, capa al viento, algo delante del
personaje (cubo, cadena, antorcha).

**Palabras que ayudan**: *Survey Corps cloak, olive green hooded cape, short
tan leather jacket, white trousers, knee-high brown boots, leather harness,
stone castle interior, window light, torchlight, parchment, WIT Studio 2013
anime style, thin black lineart with tension lines, two-tone cel shading,
muted palette*.

**Palabras que lo estropean**: *chibi, pastel, glossy, neon, 3D render, smiling
Levi, cute, tall Levi, red scarf bright*, y cualquier cosa que ponga texto con
la IA. Las letras se ponen después, con las fuentes del punto 6.

**Ejemplo de descripción (fondo, sin personaje)**: *«interior of an old stone
castle, large grey-green stone blocks, tall window with white daylight,
dust floating in the light beam, wooden bucket and broom in the foreground,
oak board with a paper notice pinned on the wall, 2013 TV anime background
art, muted palette, no people, no text»*.

**Referencias de estilo** (subirlas como imagen de referencia): P·1 y G2
(línea y color limpios de WIT), P·10 (Levi con pañuelo), E·8 y E·18 (piedra del
cuartel), E·1 (tribunal), E·14 (noche con antorchas), G1/P·4 (grupo y saludo).
**No usar** como estilo G7-G9 ni el arte de la T4 si la lámina es de T1-T3.

### 18.1 · Caras y encuadre por emoción, y guía para una IA de texto (repaso corto)

**Para la IA de imagen, la cara** (de §14.2): *shadowed eyes, straight
mouth* (rabia fría, Mikasa M3); *heavy-lidded bored stare* (Levi); *gritted
teeth* (las caras de figma de Levi, Erwin y Eren, Punto 23); *tears welling,
small smile* (P·29); *back turned to camera* (Mikasa esconde el dolor). Nunca
*smiling*, salvo Hange (*wide grin, glasses glinting*, H1). **Encuadre por
emoción** en el Punto 18.7. Las gotas de sudor y los fondos de emoción no
salen en lo reunido ⚠️: no pedirlos.

**Para la IA de texto: reglas de voz**
- **Levi**: frases cortas, órdenes, sarcasmo; «Tch»; casi sin signos de
  exclamación; remata con una orden. Se queja de la suciedad antes que del
  peligro.
- **Erwin**: dato duro → pregunta al grupo → **lema gritado** con «¡!».
- **Hange**: exclamaciones, explica de más, se presenta con el cargo entero.
- **Mikasa**: pocas palabras; casi siempre le habla a Eren por su nombre.
- **Keith** (regañar): a gritos, humilla («ganado»). **Zackly** (sentenciar):
  formal, cierra con «¿entendido?».
- En latino se dice **«Legión de Exploración»** (⚠️ §9.3), «tropa de cadetes
  104», «corte marcial», «amonestación».

**Frases reales por emoción** (latino = doblaje, §9.3; si no, traducción
nuestra de los subtítulos japoneses de Netflix):

| Emoción | Frase | Quién · dónde |
|---|---|---|
| Alegre | «¡Buenas noches, escuadrón Levi! ¿Qué tal se vive en el castillo?» | Hange · ep. 15 · 10:00 |
| Alegre | «¡De lo más emocionante!» | Hange · ep. 15 · 10:30 |
| Enfadado | «No sabía que los cerdos podían hablar.» | Levi · **latino** · ep. 14 · 13:50 |
| Enfadado | «Esto no vale nada. Hazlo todo otra vez.» | Levi · ep. 15 · 07:12 |
| Enfadado | «No estoy para darles una cálida bienvenida.» | Keith · **latino** · ep. 3 · 01:39 |
| Explicando | «Yo no planeo estrategias. Eso no me compete.» | Levi · **latino** · ep. 15 · 08:44 |
| Explicando | «…será una corte marcial. Significa que la decisión final la tomaré yo, ¿entendido?» | Zackly · **latino** · ep. 14 · 10:29 |
| Explicando | «Es una regla que hay que cumplir.» | Levi · ep. 15 · 05:38 |
| Animando | «Díganme, cadetes. ¿Morirían si yo les ordenara matarse? … ¡Consagren sus corazones!» | Erwin · **latino** · ep. 16 · 13:52-14:13 |
| Animando | «Tu determinación me dará fuerza. Eso te lo prometo.» | Levi · **latino** · ep. 9 · 06:57 |
| Triste | «Perdón… no puedo.» | Mikasa · ep. 93 · 17:25 |
| Triste | «¿Ya está lista la comida…?» · «…carne.» | Sasha · ep. 67 · 14:24-14:37 |
| Triste | «Erwin, lo de acabar con el Titán Bestia… parece que tardará más.» | Levi · ep. 55 · 21:31 |

---

> [!note] Puntos 18-25 del encargo (repaso corto, 24-sep-2026)
> Son los puntos que `ENCARGO.md` añadió el 24 de septiembre. Van aquí, entre
> la guía para IA (§18) y los conceptos (§19). Salen de `partes/texto.md`
> (18, 24, 25), `partes/imagen.md` (19, 23) y `partes/voz.md` (20, 21, 22).
> - Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo
> - Punto 19 · Texturas 2D
> - Punto 20 · Gustos y detalles de cada personaje
> - Punto 21 · Por qué la gente la ama (y las escenas que hacen llorar)
> - Punto 22 · Fan dubs y comunidad hispana
> - Punto 23 · Colaboraciones, figuras y cosplay
> - Punto 24 · Obras parecidas y láminas vecinas
> - Punto 25 · El mundo, la historia por arcos y sus símbolos

## Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**En corto**: Isayama dibuja **a mano, en papel**, con mucho tramado cruzado y
línea irregular a propósito. El anime (WIT, T1-T3) mezcla **personajes en 2D
con fondos, caballos y vuelo en 3DCG**; MAPPA (T4) usa más CG y va más pegado
al manga. Se replica con sombra dura de dos tonos, contorno negro fino y
grano suave. Datos de `partes/texto.md`.

### Punto 18.1 · Isayama: a mano y «feo a propósito» ✅

- **Dibuja en analógico**: «creo que no me saldría bien el dibujo si lo
  hiciera en digital». Rasca el papel grueso y le echa mucho corrector: su
  original **tiene relieve**. Prefiere un dibujo «memorable, aunque sea
  memorablemente malo» a uno genérico · entrevista de 2014 traducida en
  [mangabrog](https://mangabrog.wordpress.com/2014/12/24/interview-with-hajime-isayama-creator-of-attack-on-titan-better-to-have-memorable-art-even-memorably-bad-art-and-stand-out/).
- **Tramado cruzado (cross-hatching)** para sombras y caras tensas; línea
  **irregular a propósito**, para que el mundo se sienta inestable · dos
  fuentes: [FIHEROE](https://www.fiheroe.com/blogs/anime-drawing-all-things-animation/attack-on-titan-manga-art-techniques-hajime-isayama)
  y [Where Creativity Works](https://wherecreativityworks.com/illustrator-study-hajime-isayama/).
- **Cómo aprendió**: copiando páginas enteras (模写, *mosha*) de George
  Morikawa y de otro autor antes de publicar (⚠️ la parte lo escribe «Seio
  Seio»; sin comprobar) · [entrevista de Clip Studio (JA)](https://www.clipstudio.net/oekaki/archives/152645).
- **Qué programa usa hoy**: no lo encontré ⚠️. Clip Studio usa su imagen en un
  libro de consejos, pero eso no dice que lo use.
- Lo vi en el manga (Punto 19.1): rayado a mano muy denso en ropa y caballos,
  trama mecánica de puntos en los cielos y **líneas de velocidad negras**.

### Punto 18.2 · WIT Studio (T1-T3): 2D + 3DCG y «maquillaje digital»

- **Tetsurō Araki** (director T1-T3): la belleza «sale del choque entre la luz
  y la sombra»; usa mucho **destello de lente** (por el cineasta Shunji Iwai);
  ayudó a estandarizar **fondos en 3DCG con personajes en 2D**, empezando por
  AoT; *storyboard* en 3D para la acción; paleta «pesada e intensa» ·
  [fullfrontal.moe](https://fullfrontal.moe/tetsuro-araki/) ✅ (cuadra con la
  paleta apagada medida en §5).
- **Director de fotografía**: Kazuhiro Yamada ([ANN](https://www.animenewsnetwork.com/encyclopedia/people.php?id=25502)).
  Una entrevista suya sobre grano o aberración: no la encontré ⚠️.
- **3DCG de MADBOX**, con Shūhei Yabuta de director de CG: el **equipo de
  maniobras, la cámara que sigue el vuelo y los caballos** ·
  [SlashFilm](https://www.slashfilm.com/834201/the-anime-that-inspired-attack-on-titans-shift-to-cgi/)
  y [UK Anime Network, entrevista a WIT](https://uk-anime.net/articles/titans_of_animation_-_the_wit_studio_interview.html) ✅.
- **«Maquillaje digital» (T2)**: artistas digitales retocaban dibujos
  intermedios para dar textura de ilustración a pelo y ojos de titanes. Se
  llamó «Special Effects For Living Beings» (Chie Yamazaki). Los caballos, casi
  siempre en 3DCG, «la pesadilla de los animadores» ·
  [Sakuga Blog](https://blog.sakugabooru.com/2017/04/13/attack-on-titan-season-2-production-notes-1-2/) ⚠️ (una fuente, especializada).

### Punto 18.3 · MAPPA (temporada final): más CG, más manga

- WIT: parte a mano y parte CG, brillaba en el vuelo. MAPPA: **más CG**,
  **proporciones más fieles al manga**, estilo «más realista», peso en los
  combates de titanes y *rotoscoping*. Dividió al fandom ✅ (tres fuentes:
  [Gamerant](https://gamerant.com/attack-on-titan-who-did-it-better-wit-studio-vs-mappa/),
  [CBR](https://www.cbr.com/attack-on-titan-season-4-premiere-maapa-wit-animation-differences/),
  [Twinfinite](https://twinfinite.net/features/mappa-didnt-deserve-the-hate-for-attack-on-titans-final-season/);
  también [AnimeIgnite](https://animeignite.com/wit-to-mappa-aot-final-season/)).
- El director de la T4 (parte 1), Yuichirō Hayashi, se inspiró en el CG de
  *Dorohedoro*, según dijo a *Japan Forward* ⚠️ (sin enlace propio en la parte).
- **Para la lámina**: no mezclar. Si es de T1-T3, estilo WIT (§18).

### Punto 18.4 · Sombreado, línea y filtros

- **Sombra**: dos tonos, dura, poco brillo; **contorno negro fino con muchas
  líneas de tensión** (ya en §18). Es el tramado de Isayama pasado a
  cel-shading.
- **Filtros**: viñeteado suave, grano fino y algo de *bloom* en antorchas
  (`#D29258`, §5). Se ven, pero **no encontré** una entrevista que los nombre
  ⚠️: lo trato como técnica corriente del anime de 2013.

### Punto 18.5 · Cómo reproducirlo en Photoshop

- **Capas**, de abajo arriba:
  1. color plano;
  2. sombra dura en máscara de recorte, al 100 %, borde sin difuminar;
  3. línea en Multiplicar, negro casi puro (`#0D0D0D`-`#1A1A1A`, propuesta del
     investigador, no medida);
  4. papel o grano al 8-12 % en Superponer;
  5. viñeta sutil.
- **Pinceles**: tinta dura sin presión en el borde para el contorno; tramado
  cruzado a mano, o el filtro de trama de medios tonos de Photoshop para la
  trama del manga (y los pinceles de Punto 19).
- **Ajustes**: Curvas para una banda de sombra dura; Equilibrio de color hacia
  verde-ocre en las sombras (§5); *Añadir ruido* monocromático al 2-4 %.

### Punto 18.6 · Cómo reproducirlo en Blender

- **Shader toon** (nodos nativos, gratis): Diffuse BSDF → **Shader to RGB**
  (sólo Eevee) → **Color Ramp en Constante** con dos paradas → multiplicar por
  el color base. Virar la sombra a **azul o morado**, no sólo oscurecer ·
  [StraySpark Studio](https://www.strayspark.studio/blog/how-to-get-anime-toon-look-blender).
  También hay un nodo **Toon BSDF** ([manual de Blender](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/toon.html)).
- **Contorno**, tres formas nativas:
  1. **Line Art** (desde 2.93): grosor constante en píxeles, el más parecido
     al manga · [tutorial](https://www.classcentral.com/course/youtube-easy-real-time-toon-shader-outlines-with-new-blender-2-93-line-art-feature-222968).
     **El mejor para la lámina.**
  2. **Freestyle**: más lento; varía el grosor por ángulo (líneas de tensión).
  3. **Solidify invertido** con material negro y *Backface Culling*: rápido,
     pero el grosor cambia con la distancia.
- **Luz y render**: **una sola luz Sol** fuerte para un borde de sombra
  limpio. En *Color Management*, **View Transform en Estándar**, no AgX: AgX
  aplana los colores planos (StraySpark).
- **Texturas encima**: las de Poly Haven de §4.2 (`castle_brick_07`,
  `rough_plaster_brick`, `sandstone_blocks_08`), las CC0 de Punto 19, y grano
  y viñeta en *compositing*.
- **Modelos con esqueleto** (API de Sketchfab, 24-sep-2026, todos **CC BY**,
  descargables). Crédito: «ianadrielbravo en Sketchfab». Sólo para pose y
  proporción; retexturizar con los hex de §5 y no publicarlos tal cual:

| Modelo | Autor | Caras | Esqueleto | Enlace |
|---|---|---|---|---|
| **Levi Ackerman rig** | ianadrielbravo | 29 423 | ✅ | [01ffa989…](https://sketchfab.com/3d-models/01ffa989559941ef807cc07b3fed40b8) |
| Eren - attack on titan | AZlZ | 9 409 | sin comprobar | [e249261e…](https://sketchfab.com/3d-models/e249261e7d4a4bb48ffbd0a7f84001a0) |
| Aotwa_armin_arlelt rig | ianadrielbravo | 26 531 | ✅ | [eb79c080…](https://sketchfab.com/3d-models/eb79c080ba4645df8246bcf81ae8c759) |
| Aot sasha braus rig | ianadrielbravo | 18 117 | ✅ | [625e1d01…](https://sketchfab.com/3d-models/625e1d017086400481faba3019da8e77) |
| Aot Smiling Titan rig | ianadrielbravo | 18 196 | ✅ | [d697d485…](https://sketchfab.com/3d-models/d697d4856d724144beccfd7471d9f5c9) |
| Beast Titan rig | ianadrielbravo | 24 306 | ✅ | [fa271e04…](https://sketchfab.com/3d-models/fa271e0452394ca6bece9fdefd5287d7) |
| Aot female_titan | ianadrielbravo | 14 902 | sin comprobar | [05aec839…](https://sketchfab.com/3d-models/05aec8398757451fb9ceed7b304f4ab1) |

  Levi sin esqueleto (TKSAET) y el equipo de maniobras (marthacuenca) ya
  están en §4. **No comprobé** la importación en Blender ⚠️ (no hay Blender en
  el contenedor): revisar el esqueleto al bajarlos (glTF, FBX u OBJ).

### Punto 18.7 · Encuadre y composición

- **Contrapicado para los titanes**: exagera su tamaño y lo pequeño del
  humano. Se respeta la **regla de los 180°**, salvo en las persecuciones con
  el equipo de maniobras, donde se rompe a propósito para dar vértigo.
  **Paneos** en las peleas y **fotogramas congelados** en el instante clave ·
  [RedQStudios](https://www.redqstudios.com/p/attack-on-titan-shingeki-no-kyojin_3.html) ⚠️ (una fuente).
- **Por emoción** (de lo ya visto en §10, §11 y §18):

| Emoción | Encuadre | Luz | Ejemplo |
|---|---|---|---|
| Calma, explicar | plano medio frontal | plana | tribunal, E·1-E·3 |
| Tensión, pelea | contrapicado + paneo rápido | destello de lente (Araki) | carga de Erwin, P·22 |
| Duelo, discurso | primer plano de ojos | lateral dura, antorchas `#D29258` | Erwin, ep. 16 (E·13-E·14) |
| Revelación, sentencia | **simétrico**, personaje pequeño y centrado ante un fondo enorme | alta, de ventanas (Concepto B) | tribunal, E·3: juez arriba, acusado abajo |
| Pérdida | cenital, o el personaje de espaldas | madera oscura | Sasha, ep. 67 (Punto 21.4) |

- Ya en §18: plano medio desde abajo, capa al viento y **algo delante** del
  personaje.

---

## Punto 19 · Texturas 2D

**En corto**: cuatro capas. **Trama y rayado del manga**, **papel**, **tela
y cuero** del uniforme (lisos: no hay estampados) y los **4 emblemas**. Todas
tienen equivalente libre. Las texturas 3D reales (piedra, madera) están en
§4.2. Datos de `partes/imagen.md`.

### Punto 19.1 · Trama del manga y pincelada (miradas, no supuestas) ✅

- **[`Manga_Wall_Maria_operation.png`](https://static.wikia.nocookie.net/shingekinokyojin/images/9/9c/Manga_Wall_Maria_operation.png)**
  (946×643, wiki). Erwin a caballo, espada en alto, cargando. Se ve:
  - **rayado a mano muy denso** en el caballo y en las sombras de la ropa:
    líneas finas y paralelas, más juntas donde hay más sombra;
  - **trama mecánica de puntos** en cielo y hierba: gris uniforme de retícula
    fina, pegada, no dibujada;
  - **líneas de velocidad** gruesas y totalmente negras detrás de Erwin.
- **[`AoT_Manga_final_panel.png`](https://static.wikia.nocookie.net/shingekinokyojin/images/2/29/AoT_Manga_final_panel.png)**
  (843×460, wiki). El **boceto a lápiz sin entintar** del panel final, que
  Isayama dibujó en directo en el documental *Jōnetsu Tairiku* (MBS,
  18-nov-2018). Líneas sueltas, varias pasadas, sin tinta ni trama. Sirve
  para un **pincel de lápiz**, no de tinta. Real, con dos fuentes:
  [ANN](https://www.animenewsnetwork.com/news/2018-11-18/attack-on-titan-manga-final-panel-previewed-on-tv/.139667)
  y [ComicBook.com](https://comicbook.com/anime/news/attack-on-titan-manga-final-panel-finale-spoilers/) ✅.

### Punto 19.2 · Papel

- El papel de la ficha «Información pública» ya está medido: `#F2F2F2`
  (§5, §7). Es la base del cuadro de diálogo propio de la serie.
- **Libre (CC0)**: [`Paper001` de ambientcg](https://ambientcg.com/view?id=Paper001),
  papel blanco liso (2048×2048), comprobado por su API. Encima, el gris
  medido.

### Punto 19.3 · Tela y cuero (no hay estampados)

- Revisé los visuales grandes (P·5, P·6) y el texto *Appearance* de la wiki:
  **ninguna prenda de la Legión, la Policía Militar ni la Guarnición lleva
  estampado**. Son colores planos. El emblema va bordado sólo en la espalda
  de la capa. Busqué también «uniform pattern / fabric» en la wiki y «制服 柄»
  en japonés: no encontré un estampado textil.
- **Libres (CC0, ambientcg)**:
  - [`Fabric019`](https://ambientcg.com/view?id=Fabric019): lana tejida
    blanca; teñirla del verde de la capa (`#1E261F`-`#3C4E3A`, §5).
  - [`Leather037`](https://ambientcg.com/view?id=Leather037): cuero marrón
    liso, para las correas del equipo de maniobras y las botas.

### Punto 19.4 · Emblemas y logos

- Los 4 emblemas de facción ya están con tamaño (F·19-22, §2). Alas de la
  Libertad: azul `#162873`, blanco `#E3E3E5`, escudo gris `#AFADAB` (§5).
- **El propio licenciante los trata como «el juego completo»**: la mochila
  «Regiment Cloak» de *Fortnite* deja elegir **los mismos 4** como parche ·
  [Siliconera](https://www.siliconera.com/fortnite-attack-on-titan-collab-adds-eren-levi-mikasa-and-odm-gear/) ✅.
- **Vector libre para rehacer la silueta** sin copiar el emblema: alas y
  coronas de laurel en [Noun Project](https://thenounproject.com/browse/icons/term/laurel-wreath/)
  (CC BY, con atribución) o [Vecteezy «Military Wings»](https://www.vecteezy.com/free-vector/military-wings)
  (licencia gratuita con atribución) ⚠️ ninguno es CC0: poner el crédito o
  pagar.

### Punto 19.5 · Las capas, de un vistazo

| Capa | En la serie | Libre | Licencia |
|---|---|---|---|
| Trama de fondo | puntos mecánicos en cielos (19.1) | 34 pinceles de semitono `.abr` en [Brusheezy](https://www.brusheezy.com/brushes/50379-mabecman-s-screentones-halftone-brushes) | ⚠️ gratis; el texto de la licencia no cargó: revisarlo antes de un uso comercial |
| Rayado de sombra | tramado denso a mano | el mismo pack, o un pincel duro de lápiz | igual |
| Boceto | lápiz sin entintar (19.1) | pincel de lápiz de Photoshop o Clip Studio | — |
| Papel | ficha `#F2F2F2` | `Paper001` | **CC0** |
| Tela | capa verde lisa, camisa gris | `Fabric019` | **CC0** |
| Cuero | correas, botas | `Leather037` | **CC0** |
| Emblemas | F·19-22 | Noun Project o Vecteezy | CC BY o gratuita con atribución |

No hice hoja nueva: `hojas/` ya tiene sus 3. Las dos páginas de manga van con
su enlace directo.

---

## Punto 20 · Gustos y detalles de cada personaje

**En corto**: AoT **no tiene** la cultura de *databook* con «comida, color y
afición favoritos» de otros shōnen. Lo que hay sale de entrevistas a Isayama
recogidas en la wiki (Trivia) y de AniList. Lo ya dicho en §14 (la limpieza de
Levi, los titanes de Hange, la bufanda) no se repite. Datos de `partes/voz.md`.

| | Levi | Erwin | Hange | Eren | Mikasa |
|---|---|---|---|---|---|
| Cumpleaños | 25-dic ✅ | 14-oct ⚠️ | 5-sep ⚠️ | 30-mar ⚠️ | 10-feb ✅ |
| Altura | 160 cm ⚠️ | 188 cm ⚠️ | 170 cm ⚠️ | 170 cm; 183 cm adulto ⚠️ | 170-176 cm ✅ |
| Sangre | A ✅ | — | — | B ⚠️ | AB ⚠️ |
| Objeto | taza por el borde; espadas envueltas | saludo con la izquierda | gafas ✅ | **llave del sótano al cuello** ✅ | bufanda roja |

Fuentes de la tabla: [AniList](https://anilist.co/character/45627) (Levi),
[AniList](https://anilist.co/character/46496) (Erwin),
[AniList](https://anilist.co/character/71121) (Hange),
[AniList](https://anilist.co/character/40882) (Eren) y la sección Trivia de
cada ficha de la wiki. ✅ = las dos coinciden.

### Levi

- **Té negro, sin azúcar ni leche**: para Levi esos añadidos son «demasiado
  valiosos, no se los puede permitir» (Isayama, *Bessatsu Shōnen*, sep-2016) ·
  [wiki, Trivia](https://attackontitan.fandom.com/wiki/Levi_Ackerman#Trivia) ✅
  (cuadra con la tetera de §14).
- **Se corta el pelo él mismo, con maquinilla**, y **duerme 2-3 horas sentado
  en su silla**, sin cambiarse (*FRaU*, ago-2014) ✅.
- Aguanta bien el alcohol ⚠️. Le molesta que Oluo lo imite ⚠️. Su tipo ideal,
  con humor: alguien que «cumpla mis estándares de limpieza» ⚠️. De joven quiso
  abrir una **tetería** ⚠️ (todo, misma ficha).
- Edad: «treinta y pocos», según el equipo ✅.
- **Cómo se ve**: **no como un líder igual que Erwin**; deja decidir a sus
  subordinados. Sabe que es el mejor luchador vivo, sin arrogancia: nadie es
  invulnerable · [wiki, Personality](https://attackontitan.fandom.com/wiki/Levi_Ackerman#Personality) ✅.

### Erwin

- **Deja el cuarto desordenado** (al revés que Levi) y sería quien más
  aguantaría en una sauna (*Attack on Titan Magazine*, pp. 430-431) ⚠️.
- **No se casó** «porque no sabía cuándo iba a morir» (*Bessatsu Shōnen*,
  dic-2013) ⚠️ · [wiki, Trivia](https://attackontitan.fandom.com/wiki/Erwin_Smith#Trivia).
- **Lo que ama de verdad**: entender qué hay más allá del mundo y demostrar la
  teoría de su padre. Le confiesa a Levi que le importa **más** que vencer a
  los titanes. Siente a sus caídos mirándolo · [wiki, Personality](https://attackontitan.fandom.com/wiki/Erwin_Smith#Personality)
  (caps. 72 y 80) ✅.
- **Cómo se ve**: alguien que sacrificó su humanidad por una causa. Al final
  **renuncia a su sueño** y carga con sus soldados (cap. 80) ✅.
- **Con quién creció**: Nile Dok, de su promoción. Iban a la Legión juntos;
  Nile se fue a la Policía Militar por Marie · [wiki, Relationships](https://attackontitan.fandom.com/wiki/Erwin_Smith#Relationships) ✅.
- Un apodo «Ceja» sale mezclado con el propio Isayama ⚠️: no usarlo.

### Hange

- **Con quien mejor se lleva es Levi** (*Bessatsu Shōnen*, abr-2016) ·
  [wiki, Trivia](https://attackontitan.fandom.com/wiki/Hange_Zo%C3%AB#Trivia)
  y [Relationships](https://attackontitan.fandom.com/wiki/Hange_Zo%C3%AB#Relationships) ✅.
- Gag: **Levi la bañaba a la fuerza** cuando iba demasiado sucia de sus
  experimentos ⚠️.
- **Las gafas** fueron lo primero que Isayama pensó de su diseño (*artbook*,
  p. 107) ✅.
- **Género abierto a propósito** («da igual cuál de los dos»); Isayama pidió a
  Kodansha no fijarlo en la traducción ✅. Distanciada de su familia ⚠️. Su
  nombre en japonés sería «Hans Zoe» ⚠️.

### Eren

- **La llave de su padre, colgada del cuello con una cuerda, siempre**, también
  de civil (cap. 10) · [wiki, Appearance](https://attackontitan.fandom.com/wiki/Eren_Yeager#Appearance) ✅.
  Abre el sótano: es el motor de la trama.
- **Desprecio a los titanes**: los cuenta con *-hiki* (animales pequeños), no
  con *-tai* · [wiki, Trivia](https://attackontitan.fandom.com/wiki/Eren_Yeager#Trivia) ✅.
- Isayama le eligió canción: «Otoko wa Romandaze! Takeda-kun» (Shinsei
  Kamattechan) ⚠️.
- **Cómo lo ve su autor**: «un esclavo de la historia»; no esperaba que fuera
  tan popular (*Weekly Shōnen Magazine*, 2017) ✅.

### Mikasa

- **Se quita la bufanda si hace mucho calor** (*Bessatsu Shōnen*, dic-2010) ⚠️ ·
  [wiki, Trivia](https://attackontitan.fandom.com/wiki/Mikasa_Ackerman#Trivia).
- **68 kg: la mujer más pesada conocida de la serie**; ganaría un pulso en el
  104.º (*artbook*, p. 158) ⚠️.
- **Por qué protege**: según el *databook* *ANSWERS*, no es por la sangre
  Ackerman: «es sólo su naturaleza» ✅ (cuadra con §14).
- **Lo que quiere**: una vida tranquila con Eren, no la guerra. Lo confirma la
  cabaña del ep. 93 (Punto 21.3) · [wiki, «A Long Dream»](https://attackontitan.fandom.com/wiki/A_Long_Dream_(Episode)) ✅.

**No encontré** ⚠️ la **comida favorita** de Erwin, Hange, Eren y Mikasa, ni
aficiones de Erwin y Hange más allá de lo de arriba (búsqueda en la wiki,
«favorite food»). Pendiente: el *Character Encyclopedia* japonés, que la wiki
no indexa.

---

## Punto 21 · Por qué la gente la ama (y las escenas que hacen llorar)

**En corto**: se ama por el **misterio de cada capítulo**, por su
desesperanza honesta y por despedidas que duelen. Las tres escenas que más
hacen llorar tienen **minuto exacto** (subtítulos japoneses de Netflix del
espejo de kitsunekko, el mismo de §3) y dos comparten tema: **«Call of
Silence»**. Datos de `partes/voz.md`. Las frases son **traducción nuestra**
del japonés: estas escenas no tienen muestra latina en Doblaje Wiki.

### Punto 21.1 · Por qué, en números, y con quién se identifica el público

- **Más de 140 millones de copias** (nov-2023). En 2014 le quitó a *One Piece*
  el primer puesto de ventas del semestre (datos de Oricon) ·
  [Wikipedia](https://en.wikipedia.org/wiki/Attack_on_Titan#Sales) ✅.
- **Premios**: Kodansha, Attilio Micheluzzi, Harvey; mejor manga de la década
  para CBR (2019); Guinness al cómic publicado más grande (*for Giants*, 2021) ·
  [Wikipedia](https://en.wikipedia.org/wiki/Attack_on_Titan#Accolades) ✅.
- **Quién la ve** en Japón (Nikkei Entertainment, dic-2023): 33 años de media;
  **60 % mujeres** ⚠️ (una fuente).
- **Por qué conecta**: retrata «la desesperanza de la juventud actual» (Mao
  Yamawaki) y trae «un misterio nuevo en cada capítulo» (Tomofusa Kure) ·
  [Wikipedia](https://en.wikipedia.org/wiki/Attack_on_Titan#Critical_response) ✅.
- **Con quién se identifica**: con **Eren en su momento más «patético»**, no en
  el heroico. El post «por qué amo esto» con más votos del subreddit (**1080
  votos, 411 comentarios**) es la viñeta donde Eren grita que quiere que Mikasa
  piense sólo en él, y Armin le dice que no. Miré la viñeta ([imagen, 720×231](https://i.redd.it/ne6k43do49r91.jpg)):
  cara desencajada, amor egoísta. Engancha la **honestidad incómoda**, no la
  fuerza · [r/ShingekiNoKyojin](https://www.reddit.com/r/ShingekiNoKyojin/comments/xt4y15/i_dont_know_why_but_i_love_this_panel_in_the/) ✅.

### Punto 21.2 · Llorar: la muerte de Erwin (ep. 55 «Midnight Sun»)

- **Antes**: ep. 53 (el discurso, §9 y §14) y ep. 54 «Hero» (la carga, con
  **«APETITAN»**, [wiki](https://attackontitan.fandom.com/wiki/Hero_(Episode)) ✅).
- **Qué pasa**: Floch trae a Erwin moribundo justo cuando Levi iba a usar la
  única inyección de titán con Armin. Eren y Mikasa se le enfrentan; Levi
  golpea a Eren y Mikasa le pone la espada al cuello. Erwin delira: cree estar
  en clase con su padre y **levanta la mano como un niño**. Levi lo deja
  descansar y salva a Armin · [wiki, «Midnight Sun»](https://attackontitan.fandom.com/wiki/Midnight_Sun_(Episode)) ✅.
- **Minutos** ✅ ([`進撃の巨人.S04E55.白夜…ja[cc].srt`](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Shingeki%20no%20Kyojin%203%20Part%202)):
  - **19:08-19:20**: «Profesor… ¿cómo supo que no hay humanidad fuera de los
    Muros?» (先生…壁の外に人類がいないって…).
  - **21:31-21:47**: Levi al cadáver: «Erwin, lo de acabar con el Titán
    Bestia… parece que tardará más». A los **21:39** «ya ha muerto»; a los
    **21:46** «ya veo» (そうか).
- **Por qué duele**: Erwin renuncia sin saberlo al sueño que más le importaba
  (Punto 20), y es Levi quien decide que ya puede descansar.
- **Música**: **«Call of Silence»** (Sawano, voz de Gemie) desde que Floch lo
  trae · [wiki de la canción](https://attackontitan.fandom.com/wiki/Call_of_Silence) ✅ ·
  [Spotify](https://open.spotify.com/track/7k1HoUdskuBhyWvm7hPctM).
- **Cómo está dibujada**: contrapicado desde el suelo, Erwin tumbado con sangre
  en la pierna, **luz cálida de atardecer** sobre las tejas, Levi de espaldas
  con la capa verde · [`Erwin_asks_a_question.png`, 1920×1080](https://static.wikia.nocookie.net/shingekinokyojin/images/e/e0/Erwin_asks_a_question.png/revision/latest?cb=20240223040142) (mirado).

### Punto 21.3 · Llorar: el final, Mikasa besa a Eren (ep. 93 «A Long Dream»)

- Estreno: 19-nov-2023 · [wiki, «A Long Dream»](https://attackontitan.fandom.com/wiki/A_Long_Dream_(Episode)) ✅.
- **Qué pasa**: en plena batalla, Mikasa ve una vida con Eren en una cabaña de
  montaña. Él le pide que, si muere, tire la bufanda y lo olvide. Ella no
  puede. Se ata la bufanda, entra por la boca del titán, encuentra su cabeza,
  **sonríe**, la corta, la abraza y la besa. Detrás, Ymir sonríe ✅.
- **Minutos** ✅ ([`進撃の巨人.S07E93.長い夢…ja[cc].srt`](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Shingeki%20no%20Kyojin.%20The%20Final%20Season%20-%20Kanketsu-hen%20Kouhen)):
  - **16:39-17:03**: «Si muero, tira esta bufanda… olvídate de mí y sé libre».
  - **17:25-17:29**: «Perdón… no puedo» (ごめん… できない).
  - **17:32-18:04**: entra por la boca del titán («¡Eren!»).
  - Después **no hay diálogo, sólo música**, hasta **18:53-18:57**: «Que te
    vaya bien, Eren» (いってらっしゃい、エレン), al besar la cabeza.
- **Por qué duele**: se despiden los tres niños que abrieron la serie, y se
  cierra el objeto de Mikasa: la bufanda que no quiso soltar.
- **Música**: **«Call of Silence» otra vez**, la de Erwin ✅ (misma página).
- **Cómo está dibujada** la cabaña: día nublado, verde y madera, **Mikasa
  sentada de espaldas al sol**, Eren de pie mirándola ·
  [fotograma, 1920×1080](https://static.wikia.nocookie.net/shingekinokyojin/images/c/cc/Mikasa_sees_a_reality_where_she_and_Eren_remained_together.png/revision/latest?cb=20231106023804) (mirado).
- **Reacción**: **Yui Ishikawa** (Mikasa en japonés) lloró al grabar su última
  línea; Marina Inoue y Yuki Kaji la abrazaron: **1399 votos** ·
  [Reddit](https://www.reddit.com/r/ShingekiNoKyojin/comments/17prmn4/yui_ishikawa_cried_after_recording_her_last_line/) ✅.
  «Puede que haya llorado un poco», **2169 votos**, sin decir qué escena ⚠️ ·
  [Reddit](https://www.reddit.com/r/ShingekiNoKyojin/comments/mg9vj1/i_might_have_cried_a_little/).

### Punto 21.4 · Llorar: la muerte de Sasha (ep. 67 «Assassin's Bullet»)

- Estreno: 1-feb-2021 · [wiki, «Assassin's Bullet»](https://attackontitan.fandom.com/wiki/Assassin%27s_Bullet_(Episode)) ✅.
- **Qué pasa**: Gabi, una niña soldado enemiga, le dispara a bocajarro en el
  dirigible, en plena celebración. Sasha delira preguntando por la comida y su
  última palabra es **«…carne»**. Jean culpa a Eren ✅.
- **Minutos** ✅ ([`進撃の巨人.S05E67.凶弾…ja[cc].srt`](https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv/Shingeki%20no%20Kyojin.%20The%20Final%20Season)):
  **13:26** disparo (銃声) · **13:27** impacto · **13:32** cae · **13:43**
  Connie: «¡Sasha!» · **14:24-14:28** «¿Ya está lista la comida…?» ·
  **14:36-14:37** «…carne» (肉…).
- **Por qué duele**: la chica de la patata, el alivio cómico desde el ep. 3
  (§3), muere en mitad de una broma sobre comida. Ridículo y desgarrador.
- **Música**: **«Nightmare»** al disparo; luego dos pistas sin título
  (`進撃vc-pf20130218巨人`, `進撃vn-pf20130524巨人`) ✅ (lista del episodio).
- **Cómo está dibujada**: plano **cenital**, madera oscura; **Armin grita** con
  los ojos muy abiertos, **Mikasa de espaldas**, Sasha en el centro con la
  mirada perdida · [fotograma, 1920×2142](https://static.wikia.nocookie.net/shingekinokyojin/images/3/39/Mikasa_and_Armin_watch_Sasha_pass_away.png/revision/latest?cb=20210201131851)
  (mirado). El del disparo no lo miré ⚠️.

### Punto 21.5 · Gritar de emoción, y reír a la vez

- **«¡Consagren sus corazones!» en la verja de Trost** (ep. 71, §3 y §9): la
  gente con el puño en alto. Es el grito de emoción más citado.
- **Reír y emocionarse con el opening 1**: la letra alemana real es «Seid ihr
  das Essen? Nein, wir sind die Jäger!» («¿Son la comida? No, somos los
  cazadores»), y medio mundo la canta mal · [wiki](https://attackontitan.fandom.com/wiki/Feuerroter_Pfeil_und_Bogen)
  (folleto del CD) ✅ y el hilo de sonidos icónicos de
  [Reddit](https://www.reddit.com/r/ShingekiNoKyojin/comments/1u0dj12/) ✅.
  Una versión hispana del chiste: no la encontré ⚠️.
- Más sonidos en §10.1: «Sasageyo» y el grito «KEEEENNNYYY».

---

## Punto 22 · Fan dubs y comunidad hispana

**En corto**: hay *fandubs* fieles a escenas, **covers de todos los openings en
latino** y un debate vivo en TikTok sobre **doblaje o versión original**, con
cuentas grandes. Una parodia larga hispana (como la *Abridged Series* en
inglés), no la encontré. **YouTube pidió «iniciar sesión» toda la tanda**: las
vistas de YouTube van sin comprobar ⚠️; las de Dailymotion, por su API ✅.
Datos de `partes/voz.md`.

### Punto 22.1 · Fandubs de escenas

| Qué | Dónde | Vistas |
|---|---|---|
| «Attack On Titan Temporada Final - Trailer Oficial - Fandub Español latino» | [YouTube](https://www.youtube.com/watch?v=C51eBwhGLUI) | ⚠️ |
| «Eren vs Annie Español Latino Fandub» (T2) | [YouTube](https://www.youtube.com/watch?v=uoz3tSXsa-k) | ⚠️ |
| «Attack On Titan OVA Fandub en Español» | [YouTube](https://www.youtube.com/watch?v=qUJFGuENIFY) | ⚠️ |
| **Parodia**: «Attack on A-hole Titan - Fandub Español Latino» (dic-2017), con guion propio de humor | [YouTube](https://www.youtube.com/watch?v=IlIaILr1aVc) | ⚠️ |
| *Junior High* cap. 1 «¡Comenzando la escuela!» (el *spin-off* cómico) | [YouTube](https://www.youtube.com/watch?v=UasIj22HAxI) | ⚠️ |
| «Attack On Titan Titans Attacks», clip con etiqueta de fandub, JeuxVideo.com, 2:05 | [Dailymotion](https://www.dailymotion.com/video/x8hfipc) | **1545** ✅ |
| «Attack on Titan Requiem»: animación tributo de fans al final, subida con subtítulos en español por **Vidaextra** (España), 1:22. No es fandub de voz | [Dailymotion](https://www.dailymotion.com/video/x9bocts) | **15 107** ✅ |

### Punto 22.2 · Covers de openings en latino (vistas ⚠️)

- «Guren no Yumiya (Full Latino)», Alan Rojas · [YouTube](https://www.youtube.com/watch?v=_GEB8OzgoLc).
- «Shinzou wo Sasageyo (Versión Español Latino)» · [YouTube](https://www.youtube.com/watch?v=aCy2-WEqa-Q) y
  [otra versión](https://www.youtube.com/watch?v=wXMsxpGQNW8).
- «Red Swan» (T3), versión TV · [YouTube](https://www.youtube.com/watch?v=7dNUKMCGejs).
- «My War» (OP6) · [YouTube](https://www.youtube.com/watch?v=XK9mks6PpU4).
- «THE LAST TITAN» (OP9), André - A! · [YouTube](https://www.youtube.com/watch?v=QSMym9XNeZ0).
- Una **lista de reproducción** sólo de covers latinos de sus openings ·
  [YouTube](https://www.youtube.com/playlist?list=PL4yrZkKNACAcCpHTmmxkQeP_IAQV5EtXk).

### Punto 22.3 · TikTok: el debate del doblaje

- **@fangirlcast**: «el doblaje latino de Attack on Titan es de los mejores,
  con grandes actores de voz» (abr-2024) ·
  [TikTok](https://www.tiktok.com/@fangirlcast/video/7373071050575285509) ·
  [otro](https://www.tiktok.com/@fangirlcast/video/7372407719912852741).
- **@elxokas** (streamer español grande): «Doblaje vs Original: El Debate de
  Attack on Titan» · [TikTok](https://www.tiktok.com/@elxokas/video/7324828459270671649).
  El debate llega a cuentas grandes, no sólo al fandom.
- **@cocoalinnet**: capítulos y *edits* en latino (#snkedit #doblaje) ·
  [TikTok](https://www.tiktok.com/@cocoalinnet/video/7294761814213102853).
- Hay vídeos de comedia con el doblaje con **más de 143 mil «me gusta»**, sin
  enlace comprobado uno a uno ⚠️.
- **Para el servidor**: es un tema de conversación real para la comunidad de
  doblaje. Sirve para un evento o un reto de fandub.

**No encontré** ⚠️: una serie de parodia hispana larga (búsquedas «Attack on
Titan abridged parodia español» y «Ataque a los Titanes parodia serie
español»), ni las vistas reales de YouTube.

---

## Punto 23 · Colaboraciones, figuras y cosplay

**En corto**: *Fortnite*, gachas japonesas, UNIQLO, cafés con **arte nuevo de
WIT** (uno abierto ahora, hasta el 12-oct-2026), una atracción en Universal
Studios Japan, escape rooms y **figuras de Good Smile de los 5 personajes**,
cada una con 3 caras: un catálogo de expresiones en 3D. Datos de
`partes/imagen.md`.

### Punto 23.1 · Videojuegos y gachas

- ***Fortnite*** (Epic, oficial), **11-abr-2023**: Eren (pase), Levi y Mikasa
  (tienda), equipo de maniobras y lanzas de rayo jugables, la mochila
  «Regiment Cloak» con los 4 emblemas (Punto 19.4) y una pantalla de carga
  con arte nuevo, «A World Without Walls» ✅ ·
  [Siliconera](https://www.siliconera.com/fortnite-attack-on-titan-collab-adds-eren-levi-mikasa-and-odm-gear/),
  [The Loadout](https://www.theloadout.com/fortnite/attack-on-titan-mikasa-levi-ackerman-skins).
- ***Monster Strike*** (Mixi), 2.ª colaboración desde el **1-may-2023**: 10
  personajes, entre ellos **«Long-Time Comrades-in-Arms» Hange y Levi**, en
  pareja, y **Erwin ★6** exclusivo ✅ ·
  [QooApp](https://news.qoo-app.com/en/post/165419/monster-strike-x-attack-on-titan-2),
  [Pocket Gamer](https://www.pocketgamer.com/monster-strike/attack-on-titan-crossover/).
- ***Puzzle & Dragons*** (GungHo): colaboración repetida; la 2.ª, en 2015, con
  Annie y Reiner en forma de titán ✅ ·
  [QooApp](https://news.qoo-app.com/en/post/10805/qoo-news-puzzle-dragons-x-attack-on-titan-second-collaboration-announced),
  [ANN](https://www.animenewsnetwork.com/news/2015-05-31/puzzle-and-dragons-mobile-game-collaborates-with-attack-on-titan-ghost-in-the-shell-duel-masters/.88749).
- ***Ninjala***: evento anunciado en su [web oficial](https://ninjalathegame.com/en/news/info/collab-shingeki.html) ⚠️
  (una fuente; sin fecha ni personajes comprobados).

### Punto 23.2 · Ropa

- **UNIQLO UT**, **30-mar-2023** (EE. UU.): **8 camisetas** que recrean
  **viñetas del manga** enteras, con Eren y sus compañeros y frases de la serie ✅ ·
  [butwhytho](https://butwhytho.net/2023/03/attack-on-titan-uniqlo-collection/),
  [Anitrendz](https://anitrendz.net/news/2023/03/13/uniqlo-to-release-attack-on-titan-ut-collection-on-march-30-in-the-united-states/),
  [Kodansha US](https://kodansha.us/2023/04/14/get-attack-on-titan-gear-at-uniqlo/).
- Una colaboración de la marca *Levi's* con Levi: **no la encontré** ⚠️ (dos
  búsquedas, inglés y español).

### Punto 23.3 · Cafés, parques y eventos

- **«Attack on Titan Café: Adolescence Dinner»** (Tokio, BOX cafe&space Lumine
  Est Shinjuku 2), **3-sep al 12-oct-2026**: **ilustraciones nuevas de WIT** de
  Levi, Erwin, Hange, Eren, Mikasa y Armin, con el tema de la **«última cena
  antes de la batalla»**; llaveros y figuras acrílicas ✅ ·
  [Anime Corner](https://animecorner.me/attack-on-titan-cafe-opens-in-tokyo-with-new-wit-studio-illustrations/),
  [Japan Pop Now](https://www.japan-pop-now.com/calendar).
- **Tower Records Cafe Omotesando** (21-jun al 9-jul-2019): menú y **realidad
  virtual de 5 minutos** con el equipo de maniobras ✅ ·
  [grape Japan](https://grapejapan.com/116858). **Animate Cafe** (2019) ⚠️ ·
  [Geeky Travels & Fandoms](https://geekytravelsfandoms.com/2019/04/30/attack-on-titan-shingeki-no-kyojin-x-animate-cafe/).
- **Universal Studios Japan** (21-ene al 28-jun-2020): atracción XR «Race For
  Survival» y el restaurante **«Survey Corps Mess Hall»**, con **Levi y Hange a
  tamaño real** ✅ ·
  [ANN](https://www.animenewsnetwork.com/interest/2020-01-20/oricon-news-gives-inside-look-at-attack-on-titan-xr-ride/.155571),
  [ComicBook.com](https://comicbook.com/anime/news/attack-on-titan-behind-the-scenes-universal-studios-japan-ride-attraction-xr/).
- **Exposición «進撃の巨人展FINAL»**: la de 2014-2015 pasó de 450 000
  visitantes; la FINAL recorrió Asia, **Seúl del 15-jul al 15-oct-2023** ✅ ·
  [Japan Kuru](https://www.japankuru.com/en/event-calendar/e185/),
  [Pia (JA)](https://corporate.pia.jp/news/detail_final.html).
- **Real Escape Game** (SCRAP): 5 ediciones desde 2014, de Yokohama a Nueva
  York; la última, «Escape From the 5 Titans» (25-feb-2021) ✅ ·
  [ANN](https://www.animenewsnetwork.com/interest/2016-08-06/latest-attack-on-titan-real-escape-game-story-traps-players-in-a-castle/.104884),
  [CBR](https://www.cbr.com/attack-on-titan-scores-a-second-real-escape-game/),
  [Real Escape Game](https://realescapegame.com/aotus/).

### Punto 23.4 · Figuras oficiales: cada cara es una emoción en 3D

Todas de Good Smile Company ([goodsmile.info](https://www.goodsmile.info/en/product/4167/Nendoroid+Levi.html)) ✅:

| Personaje | Figura | Caras | Qué trae |
|---|---|---|---|
| Levi | [Nendoroid 390](https://www.goodsmile.info/en/product/4167/Nendoroid+Levi.html) | estándar, combate, **desdén** | doble espada en **agarre invertido**, su firma |
| Levi | [figma](https://www.goodsmile.info/en/product/4164/figma+Levi.html) | estándar, **apretando dientes**, fría | manos para el agarre invertido |
| Erwin | [Nendoroid](https://www.goodsmile.info/en/product/6468/Nendoroid+Erwin+Smith.html) | estándar, **gritando**, sonriendo | efectos de vuelo ([reseña](https://mikatan.goodsmile.info/en/2017/05/26/nendoroid-erwin-smith-attack-on-titan/)) |
| Erwin | [figma](https://www.goodsmile.info/en/product/8651/figma+Erwin+Smith.html) | fulminante, gritando, dientes apretados | **su caballo** y la capa de la Legión |
| Hange | [Nendoroid](https://www.goodsmile.info/en/product/8251/Nendoroid+Hange+Zoe.html) (2023) | estándar, sonriente en batalla, **entusiasmada** | gafas y **hoja de informe de titanes**; capa nueva ([reseña](https://mikatan.goodsmile.info/en/2019/04/16/nendoroid-hange-zoe-attack-on-titan/)) |
| Eren | [Nendoroid](https://www.goodsmile.info/en/product/4095/Nendoroid+Eren+Yeager.html) (Titán de Ataque) | estándar, combate | edificio y mini Reiner (Trost) |
| Eren | [figma](https://www.goodsmile.info/en/product/4089/figma+Eren+Yeager.html) | decidido, enfadado, **en shock** | efectos de humo |
| Mikasa | [Nendoroid](https://www.goodsmile.info/en/product/4048/Nendoroid+Mikasa+Ackerman.html) | estándar, gritando, aturdida | efectos de vuelo y de sangre |

Cruza con la tabla de caras de §14.2: sirven donde no hubo fotograma (Eren
«en shock» para el miedo, Mikasa «gritando»), y dan el grito de Erwin y el
entusiasmo de Hange en volumen.

### Punto 23.5 · Cosplay con volumen y materiales reales

- **Titán Acorazado de Hartigan Cosplay** (Bélgica): **381 horas**; espuma de
  tapicería, **látex prevulcanizado, FlexFoam-iT III y resina**; cabeza y manos
  esculpidas en Monsterclay; **mandíbula que se mueve con la suya y suelta
  humo**, ojos que brillan. 1.er puesto FX en **TwitchCon Ámsterdam 2022** ✅ ·
  [ScreenRant](https://screenrant.com/attack-on-titan-cosplay-armored-titan/),
  [CBR](https://www.cbr.com/attack-on-titans-armored-titan-awe-inspiring-cosplay/),
  [su TikTok](https://www.tiktok.com/@hartigan_cosplay/video/7124349359692516614).
- **Con licencia libre** (Openverse, en `referencias.json`): **Mangoe** como
  Mikasa en Katsucon 2014 ([foto](https://live.staticflickr.com/2037/12961434585_cdccc55b89_b.jpg),
  CC BY-NC-ND 2.0, foto de WhiteDesertSun), **Xubaet** ([foto](https://live.staticflickr.com/3902/14570790265_d6daeed5e4_b.jpg),
  CC BY 2.0) y **esby.photo** ([foto](https://live.staticflickr.com/7361/12109553753_9307e6247c_b.jpg),
  CC BY-NC-SA 2.0). Tela real de bufanda y capa.

---

## Punto 24 · Obras parecidas y láminas vecinas

**En corto**: el público la junta con *Vinland Saga* y *The Promised
Neverland*. Isayama reconoce *Parasyte*, el cine de monstruos y
*Evangelion*. En el servidor, la que más se le acerca es la lámina de
Evangelion, y el tablón del Concepto A debe distinguirse del de Solo Leveling.
Datos de `partes/texto.md`.

### Punto 24.1 · Lo que recomienda el público (AniList, con votos) ✅

*Vinland Saga* (2876) · *The Promised Neverland* (699) · *86 Eighty-Six* (366)
· *Kabaneri of the Iron Fortress* (365) · *Seraph of the End* (210) · *Kaiju
No. 8* (170) · *Fullmetal Alchemist: Brotherhood* (116) · *Parasyte -the
maxim-* (101) · *Chainsaw Man* (89) · *Claymore* (68) · *Code Geass* (59) ·
*Jujutsu Kaisen* (45) · [AniList](https://anilist.co/anime/16498).

### Punto 24.2 · Lo que el autor reconoce

- **Entrevista de 2014** ([mangabrog](https://mangabrog.wordpress.com/2014/12/24/interview-with-hajime-isayama-creator-of-attack-on-titan-better-to-have-memorable-art-even-memorably-bad-art-and-stand-out/)) ✅:
  - ***Parasyte*** (Hitoshi Iwaaki), por su estilo raro. El público también la
    recomienda (24.1).
  - ***Hell Teacher Nube***, por el diseño de monstruos.
  - **Cine kaiju**: Godzilla, Gamera.
  - ***Muv-Luv Alternative***.
  - ***Evangelion*** (Hideaki Anno), por cómo dirige y «el placer de la
    expresión animada».
- **Mikasa sale de Casca de *Berserk*** (Kentarō Miura) ·
  [IMDb/ScreenRant](https://www.imdb.com/news/ni64720057/) ✅.
- Otros dibujantes que cita: Hideki Arai, George Morikawa, Kōji Seo, Ryōji
  Minagawa y Makoto Yukimura · [Lambiek](https://www.lambiek.net/artists/i/isayama_hajime.htm) ⚠️ (un agregador).

### Punto 24.3 · Láminas vecinas del servidor (para no repetir)

Lectura cruzada de otras biblias (no hay una fuente que lo compare):

| Biblia | Canal | Se parece en | Qué hacer |
|---|---|---|---|
| `16-neon-genesis-evangelion` | #demos | es la **influencia** que reconoce Isayama; también usa una «ficha o documento oficial del mundo» | no repetir el mismo objeto si se hace una lámina 2 |
| `11-chainsaw-man` | #que-estas-viendo | la recomienda AniList tras AoT | un cine y un café: sin choque |
| `03-solo-leveling` | — | acción y supervivencia; **un tablón de misiones** | el tablón del Concepto A tiene que ser el de un **cuartel militar**: roble oscuro, clavos de hierro, ficha del anime; no uno de gremio de fantasía |

---

## Punto 25 · El mundo, la historia por arcos y sus símbolos

**En corto**: tres murallas, titanes que eran personas, nueve poderes que se
heredan con una maldición. La historia va en **9 arcos**: 7 dentro
de los Muros y 2 en Marley. Datos de `partes/texto.md`.

### Punto 25.1 · Las reglas del mundo, en cinco líneas ✅

1. La humanidad vive tras **tres murallas**, María, Rosa y Sina. Fuera hay
   **titanes** que devoran personas sin necesitar comer.
2. Los titanes **son personas**: **súbditos de Ymir** transformados por el
   **Titán Fundador** o el **Titán Bestia**, que los crean con un grito ·
   [wiki, «Founding Titan»](https://attackontitan.fandom.com/wiki/Founding_Titan).
3. Hay **nueve titanes** con poderes propios que pasan de portador en
   portador. Quien controla el **Fundador** (con sangre real Reiss/Fritz)
   manda sobre todos.
4. Quien hereda un titán muere en un plazo fijo: la **maldición de Ymir** ·
   [wiki, «Power of the Titans»](https://attackontitan.fandom.com/wiki/Power_of_the_Titans).
5. Fuera está **Marley**, que también usa titanes como arma y persigue a
   **Eldia**, el pueblo de origen de los titanes.

### Punto 25.2 · La historia por arcos ✅

La wiki la ordena en **9 arcos**, en dos bloques: *Muros* (1-7) y *Marley*
(8-9) · [wiki, «Story Arcs»](https://attackontitan.fandom.com/wiki/Story_Arcs)
(leída por su API).

| # | Arco | Manga | Anime ⚠️ | Momento clave |
|---|---|---|---|---|
| 1 | Caída de Shiganshina | vol. 1 | eps. 1-2 | El Colosal rompe el Muro María; Eren ve morir a su madre |
| 2 | Lucha por Trost | vol. 1-4 | eps. 3-9 | El Colosal vuelve; Eren descubre que es titán defendiendo la muralla |
| 3 | Entrenamiento del 104.º | vol. 4 | eps. 10-11 | Nacen las amistades y rivalidades del 104.º |
| 4 | El Titán Femenina | vol. 5-8 | eps. 12-25 | 57.ª expedición; **muere el escuadrón de Levi**; Annie, descubierta y encerrada en cristal en Stohess |
| 5 | Choque de titanes | vol. 9-12 | — | Titanes dentro del Muro Rosa; **Reiner es el Acorazado y Bertolt el Colosal**; Ymir protege a Historia |
| 6 | Gobierno Real | vol. 13-17 | — | Golpe de Erwin; Kenny el Destripador; **Historia, reina** |
| 7 | Regreso a Shiganshina | vol. 18-22 | — | Se recupera Shiganshina; **el sótano de Eren** revela el mundo de fuera |
| 8 | Marley | vol. 23-26 | — | Ataque a Liberio; Eren se lleva al Titán Bestia (Zeke) |
| 9 | Guerra por Paradis | vol. 27-34 | — | **El Retumbar**; aliados contra Eren; Mikasa acaba con él |

⚠️ Los episodios del anime de la tabla son del investigador y **no los
comprobé** capítulo a capítulo: el anime reordena el entrenamiento, así que
pueden no cuadrar. Los manga, de la wiki.

### Punto 25.3 · Emblemas, objetos y palabras que un fan reconoce al instante

- **Emblemas** (F·19-22, hex en §5): **Alas de la Libertad** (Legión), el
  **unicornio** (Policía Militar), las **rosas** (Guarnición) y las **espadas
  cruzadas** (cadetes). En latino: **«Legión de Exploración»** ⚠️ (§9.3).
- **Objetos**: el **equipo de maniobras tridimensional**; las **espadas** que
  se gastan y se cambian; la **llave del sótano** al cuello de Eren (Punto 20);
  la **bufanda** de Mikasa, que Eren le pone en el cap. 1 (el «hogar»); la
  **taza que Levi coge por el borde** (§14).
- **Palabras**: *titán* y los nueve (Colosal, Acorazado, Femenina, Bestia,
  Mandíbulas, Carro, Martillo de Guerra, Fundador y Ataque; nombres de la
  parte, no del doblaje ⚠️); *Eldia* y
  *Marley*; *el Retumbar*; *Ackerman*; *súbditos de Ymir*; *la maldición de
  Ymir*; *Muro María, Rosa y Sina*; **«ese día»** (el trauma del prólogo); y
  el **saludo**, puño derecho al corazón (§7.3, §14).

---

## 19 · Tres conceptos de lámina (nuevos; la estela ya está hecha)

### Concepto A · «Reglamento del cuartel» (las reglas, con Levi limpiando)

- **Objeto y sitio**: un **tablón de roble colgado con clavos de hierro** en el
  muro de piedra del viejo castillo-cuartel del ep. 15: la sala de bloques con
  banco de madera y ventana alta del [clip, 0:26-0:30](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=26)
  (y E·18). Encima va una **hoja de papel verjurado clavada**, con las normas,
  con la **orla de enredaderas** de la ficha del ep. 25 (F·10). En Blender es
  fácil: una tabla, un papel con ondas, clavos, el cubo y la escoba de Sketchfab
  (§4.1). **Encaja con el juego oficial**: el menú de equipo de *Attack on
  Titan 3* pone **un pergamino manchado sobre madera oscura, con clavos y un
  martillo** al lado ([captura de Steam](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2916700/228cc88fa364676b8dfd4a82b7cac9fe578cb8ec/ss_228cc88fa364676b8dfd4a82b7cac9fe578cb8ec.1920x1080.jpg), §12):
  copiar de ahí el tono del papel (`#7B6953`-`#AD9981`) y de la madera
  (`#32281F`-`#504742`).
- **Personaje**: **Levi**, el más querido, con su **ropa de limpiar**: pañuelo
  blanco en la cabeza, el de la boca bajado al cuello. Pose de «regañar con
  humor»: de tres cuartos, **con dos dedos se baja el pañuelo** como en P·10
  ([clip 0:32-0:34](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=32)), la otra
  mano con un trapo; mirada de párpado caído de la puerta del
  [clip 2:24-2:28](https://www.youtube.com/watch?v=GLpLwuaBk-s&t=144) («hazlo
  todo otra vez»). Alternativa: P·11 (el dedo con polvo). Otra, oficial y de
  cuerpo entero: **Levi en *AoT 2* con pañuelo en la cabeza y la mascarilla
  subida hasta la nariz**, de pie, brazos caídos, mirada de párpado caído
  ([captura](https://www.gamecity.ne.jp/shingeki2/images/img-system21-1.jpg), §12).
- **Fondo alternativo**: el patio del juego donde **los cadetes barren con
  escobas de ramas y Levi los vigila** en el centro ([captura](https://www.gamecity.ne.jp/shingeki2/images/img-system1-4.jpg)).
  Sirve si se quiere enseñar «qué pasa si no cumples»: te toca barrer.
- **Cómo habla**: su frase va en una **ficha «Información pública»** pequeña
  clavada en la esquina del tablón: papel `#F2F2F2`, tinta `#222222` y **la
  cinta ocre del ep. 15** (`#948352`, F·5), no la roja. Título en Yuji Boku
  blanco; frase en Shippori Mincho B1. La frase: **«Es una regla que hay que
  cumplir.»** (Levi a Eren, ep. 15 · 05:38, 守るべきルールだ). Otra: «Esto es
  limpiar de verdad. ¿Entendido?» (su aspirador oficial). Las dos son
  **traducción nuestra** del japonés: **no hay muestra latina** de ellas.
  **Cuadro alternativo, sin ficha**: el de *AoT 2* (§12): «LEVI» pequeño sobre
  una línea crema fina `#CDC9BE`, la frase debajo en blanco cálido `#FFFDF2`
  con sombra, y una ✓ al final. Encaja con #reglas: la ✓ es la misma del
  «reacciona con ✅».
- **Dónde va cada texto**:
  - En la cinta: «NORMAS DEL CUARTEL».
  - En la hoja grande, las ocho reglas: número en IM Fell English, texto en
    Cormorant Garamond.
  - Al pie de la hoja: «Al quedarte, las aceptas.»
  - En la ficha: la frase de Levi.
- **Para que no quede plano**:
  - Un rayo de luz de ventana cruza en diagonal (luz `#EEF3E4`, P·11), con
    **polvo flotando**: el chiste es que Levi lo odia (y el fandom lo adora:
    §13, 4275 votos en Reddit).
  - Delante, desenfocados: el **cubo de madera con el trapo** y el mango de la escoba.
  - Levi medio en sombra.
  - El papel proyecta sombra sobre la tabla.

### Concepto B · «La sentencia» (lámina 2: qué pasa si no se cumplen)

- **Objeto y sitio**: el **estrado del juez** del tribunal del ep. 14, con un
  **libro de actas abierto**, que es el log-mod. En primer plano, el **poste con
  los grilletes**, de hierro. Todo se puede modelar: caja de madera, libro,
  cadena.
- **Personajes**:
  - **Zackly** detrás del estrado, arriba: es el que dicta (E·2, E·3; cara de
    P·9). Composición de E·3: juez arriba, poste abajo.
  - **Levi** de brazos cruzados junto al poste, como en el dibujo de Isayama de
    2026 (§2.1), con la mirada de reojo de P·13: el que hace cumplir, sin
    sangre.
  - Así sale el más querido y no se repite la pose de A.
- **Cómo habla**:
  - La **sentencia**, escrita en el libro con IM Fell English y tinta que sigue
    la curva de las páginas.
  - Zackly, en una **ficha del tribunal con cinta verde** (`#26694F`, ep. 14,
    F·3-4), con su frase **del doblaje latino** (ep. 14 · 10:29, muestra de
    Doblaje Wiki): «**La decisión final la tomaré yo, ¿entendido?**».
  - Levi, opcional, en una ficha pequeña: «Tch. Lo que hagas, queda escrito.»
    (propuesta nuestra, no es del doblaje).
  - Arriba de la página izquierda, la balanza de F·4 con «CULPABLE / INOCENTE»
    en Stardos Stencil (el GUILTY / NOT GUILTY de la ficha).
- **Dónde va cada texto**:
  - En la página izquierda del libro: la escala de sanciones como pasos
    numerados. Aviso, silenciado, expulsión, baneo, y «lo grave, directo».
    **Esperar su sí antes de publicarla.**
  - En la página derecha: «Cada sanción queda en log-mod: quién y por qué.»
  - En una nota suelta metida entre las páginas: «¿No estás de acuerdo? Abre un
    ticket en soporte.»
- **Para que no quede plano**:
  - La **cadena del grillete**, delante y desenfocada, cruza la parte baja.
  - Luz alta de ventanas del tribunal.
  - El libro con las hojas levantadas.
  - Sombra dura bajo el estrado.

### Concepto C · «¡Consagren sus corazones!» (lámina 3: aceptar, el ✅)

- **Objeto y sitio**: la **bandera de la Legión, rota por el borde** como en G1,
  colgada de un mástil de madera en el patio del cuartel **de noche con
  antorchas** (ep. 16). En Blender, la tela se simula y la pintura sigue los
  pliegues.
- **Personaje**: **Erwin** en el estrado, con los dos brazos (es el ep. 16;
  pierde el derecho en el 36), iluminado desde abajo como en E·13. Delante, de
  espaldas y en silueta, **reclutas haciendo el saludo**, puño derecho al
  corazón (E·14 · ep. 16 · 14:13, P·4).
- **Cómo habla**:
  - La frase latina **confirmada**: «¡Consagren sus corazones!» (Erwin, ep. 16 ·
    14:13, muestra de Doblaje Wiki; y título del clip oficial de Crunchyroll).
  - Va en una **cinta de pincel oro viejo `#796120`** (la del ep. 16, F·7)
    atada al mástil, en Yuji Boku blanco. Es la cinta de la ficha «Información
    pública»: el sello de la serie. El juego *Attack on Titan 3* usa el mismo
    oro viejo en su franja de misión (§12): sigue siendo reconocible en 2026.
- **Dónde va cada texto**:
  - En la cinta, la frase de Erwin.
  - Pintado en la bandera, bajo las alas: «Al quedarte, las aceptas.»
  - En una tablilla clavada al mástil: «Reacciona con ✅ para aceptar las normas.»
- **Para que no quede plano**:
  - **Antorchas en primer plano**, con brillo `#D29258`.
  - Siluetas de espaldas que tapan el borde inferior.
  - Chispas en el aire y la noche fría del ep. 16 al fondo (`#29292D` a
    `#514F57`, medida en E·13; la `#202743` es de la temporada final).
  - La bandera ondea hacia la cámara.

> Otra idea para después: cuando salga *Attack on Titan 3* (10-dic-2026),
> capturar su interfaz en alta. La demo ya enseña que **no usa caja**: retrato
> pequeño y texto blanco, y títulos en una **franja de pincel oro viejo** (§12).
> Serviría para una lámina con la **investigación fuera de las murallas**: un
> escuadrón y sus normas.

### Lo que añaden los puntos 18-25 a los tres conceptos (repaso corto)

Los conceptos no cambian de idea; ganan referencias para hacerlos.

- **A · Reglamento del cuartel**:
  - **Pose en 3D**: el **«Levi Ackerman rig»** de Sketchfab, con esqueleto
    (CC BY, ianadrielbravo; Punto 18.6). La cara, de sus figuras: **«desdén»**
    (Nendoroid) o **«fría»** (figma) (Punto 23.4).
  - **El tablón, de cuartel militar**: roble oscuro, clavos de hierro y la
    ficha del anime, para no parecerse al tablón de gremio de Solo Leveling
    (Punto 24.3).
  - **Capas**: la hoja con `Paper001` (CC0) bajo el gris medido; contorno con
    **Line Art** y una sola luz Sol (Punto 18.6, Punto 19).
  - **Detalle humano**: una **taza de té** cogida por el borde sobre la
    repisa. Té sin azúcar ni leche, y de joven quiso abrir una tetería
    (Punto 20).
- **B · La sentencia**:
  - Levi de brazos cruzados con la cara **«fría»** del figma (Punto 23.4).
  - **Encuadre simétrico** de revelación: juez arriba, acusado pequeño abajo
    (Punto 18.7).
  - Un **sello** con el emblema de la Policía Militar (el unicornio) en el
    libro de actas: es uno de los 4 emblemas «oficiales» (Punto 19.4).
- **C · ¡Consagren sus corazones!**:
  - Erwin con la cara **«gritando»** de su Nendoroid o figma; su figma trae la
    **capa de la Legión** para ver el volumen (Punto 23.4).
  - La bandera en `Fabric019` (CC0) teñida del verde medido (Punto 19.3).
  - Luz lateral dura de antorchas, primer plano de discurso (Punto 18.7).
- **Para una lámina 2 o un evento**: el café de 2026 trae **arte nuevo de WIT
  de los cinco juntos** (Punto 23.3), y el debate latino de doblaje o versión
  original da para un reto de *fandub* (Punto 22).

---

## 20 · Lo que no pude verificar (tras la segunda pasada y su cierre)

Lo que sigue con aviso en la biblia, y por qué:
- **Carlos Monroy, asistente de dirección** (§9.1): sólo lo dice la ficha de
  Doblaje Wiki; FUNiAnime y ANMTV no lo nombran.
- **Ivett Toriz, Levi niño en el ep. 47** (§9.2): sólo Doblaje Wiki (la ficha
  de la serie y la de ella son la misma fuente).
- **«Legión de Exploración»** (§9.3): cuatro voces lo dicen en las muestras de
  Doblaje Wiki, pero no hallé un texto oficial que lo escriba.

Lo que no pude mirar o no existe con la red de hoy:
- **Los vídeos en movimiento y con sonido**: YouTube deja leer los datos a
  ratos, pero **el vídeo da 403** o pide «iniciar sesión» (probé 8 veces en el
  cierre, con 4 clientes distintos; TikTok tampoco respondió a yt-dlp). Todo lo
  visto es por *storyboard* (160×90 o 320×180, ±1-2 s).
- **Frases latinas de Levi sacadas de un clip oficial**: los tres clips
  doblados de Crunchyroll en Español ya dieron subtítulos automáticos (§9.4),
  pero **Levi no habla en ninguno**. Sus frases latinas salen de las muestras
  de audio de Doblaje Wiki (§9.3).
- **La frase latina de Levi en el ep. 15** («Es una regla que hay que
  cumplir»): no hay muestra de audio; va como traducción nuestra.
- **Autores de dos fondos de ArtStation** (W9, W12): ArtStation dio 403.
- **Wayback Machine**: su API contesta (hay copia de la web oficial de 2013 y
  de la traducción de la entrevista de Otomedia a Kyoji Asano), pero **las
  páginas se cortan** (dos intentos en cada pasada).
- **Caja de diálogo de *Wings of Freedom***: sus capturas de Steam son de
  combate. (La de *AoT 2* ya está vista, §12.)
- **Fuente de la rotulación del manga en inglés** (Kodansha USA).
- **Entrevistas de arte, por dentro**: el director de arte (Shunichiro
  Yoshihara) y el artbook de Kyoji Asano ya están identificados (§2.1, §5),
  pero no leí una entrevista suya sobre el diseño: la traducción de Otomedia
  se borró y la de ABEMA (2024) habla de su carrera, no de AoT.
- **Comentarios de los Blu-ray**: no encontré transcripciones.
- **Hex de la bufanda a pleno sol**: sólo medida en G1 y en interior.
- **Moegirl y Baidu Baike** (chino): no dejaron entrar. El chino sale de
  Bangumi y de la Wikipedia china (§8, §14).

## Cumplimiento del encargo

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | 3 hojas (88 piezas con tamaño por API), arte 2023-2026 (MAPPA 15, *AoT 3*, Día de AoT, Isayama 2026 con Levi de brazos cruzados, trajes de la tienda); poses vivas: saludo, limpieza, carga, pizarra |
| 2 · Fotogramas 1080p con capítulo y minuto | ✅ | fotogramas 1920×1080 de la wiki; los de las escenas clave con minuto de los subtítulos de Netflix (§3); algunos de las hojas (P·14-19, E·15-30) sin minuto |
| 3 · Fan art y 3D con licencia | ✅ | 20 modelos de Sketchfab CC BY (licencia y autor por API), texturas Poly Haven CC0, fan art de Pixiv, ArtStation, DeviantArt y Reddit con autor |
| 4 · Fondos, luz, paleta y texturas | ✅ | hex medidos con Pillow en 20 sitios y prendas (§5), texturas reales (§4.2) |
| 5 · Tipografía con tildes, ñ, ¿ ¡ | ✅ | **una letra para cada uso** (§6.1): logo, globo (Comic Neue), grito (Bangers), pensamiento (Zen Maru Gothic; Kosugi Maru descartada), onomatopeya (Bungee), cartel, interfaz (Jost Italic) y créditos; todas comprobadas con fontTools; créditos latinos vistos (§6). Falta la fuente del manga en inglés |
| 6 · Cómo hablan en pantalla | ✅ | la ficha «Información pública» medida en sus 54 versiones, globos del manga, cartelas de la T4, **caja de diálogo de *AoT 2*** y menús de *AoT 3* con hex (§7, §12) |
| 7 · Personajes y encuestas | ✅ | 4 encuestas oficiales + Nlab; Levi gana 3 de 4; en China (Bangumi) gana Mikasa y Levi es segundo (§8) |
| 8 · Doblaje latino, dos fuentes | ✅ | reparto y equipo en Doblaje Wiki (API) + FUNiAnime/ANMTV/Crunchyroll; quedan 3 datos con una sola fuente (§20) |
| 9 · Música | ✅ | openings y endings con intérprete (vídeos oficiales de Pony Canyon), Sawano y Yamamoto; OP 2 y ED 1 mirados (§10); **qué suena en las escenas que hacen llorar** («Call of Silence» en las muertes de Erwin y el final, «APETITAN», «Nightmare») y los sonidos que todos reconocen (§10.1). Los efectos del equipo de maniobras, sin ficha oficial ⚠️ |
| 10 · Vídeos con minuto | ✅ | 13 vídeos mirados por *storyboard* con minuto y enlace `&t=`; 31 enlaces de YouTube comprobados. Los TikTok van sin minuto |
| 11 · Videojuegos: interfaz y cajas | ✅ | **caja de diálogo de *AoT 2* vista** en la web oficial (nombre sobre línea crema, texto blanco, ✓; respuestas con botones) y Levi limpiando en el juego; menús de *AoT 3* en 10 capturas de Steam de 1920×1080, con hex; demo de *AoT 3*. *Wings of Freedom*: sólo capturas de combate (§12) |
| 12 · Lo que ama el fandom y qué NO hacer | ✅ | memes con fuente, Reddit (4275 votos a la limpieza de Levi), lista de errores (§13) |
| 13 · Carácter y forma de hablar | ✅ | Levi, Erwin, Hange con frases y minutos (§14), y el gesto de la taza de Levi (dos fuentes); **qué transmite cada uno, su cara en cada emoción y sus dinámicas**, también Eren y Mikasa (§14.1-14.3). Huecos reales: la serie casi no dibuja alegría ni vergüenza en ellos (sin fotograma, dicho en §14.2) |
| 14 · Poses con minuto | ✅ | Levi 13, Erwin 7, **Hange 11, Mikasa 10 y Eren 10** (las nuevas, miradas en una hoja propia, con enlace a la imagen, tamaño y arco); cada una dice si sirve para presentar, explicar, celebrar, regañar, pensar o animar (§15) |
| 15 · Vestuario con hex | ✅ | uniforme confirmado en la wiki y en las hojas; hex medidos (§16) |
| 16 · Ciudades y fondos de pantalla con tamaño y autor | ✅ | oficiales medidos bajándolos; fans de Wallhaven con tamaño; 2 autores de ArtStation sin ver (403) |
| 17 · Guía para IA | ✅ | IA de imagen: rasgos, paleta con hex, luz, palabras, un ejemplo y las referencias por número (§18), caras por emoción (§18.1). **IA de texto**: reglas de voz por personaje y **13 frases reales por emoción** con minuto, 6 del doblaje latino (§18.1). Gotas de sudor y fondos de emoción: no salen en lo reunido ⚠️ |
| 18 · Estilo de dibujo y técnica, y cómo replicarlo | ✅ | Isayama a mano, con tramado cruzado (entrevista de 2014); WIT 2D + 3DCG (Araki, MADBOX, «maquillaje digital»); MAPPA más CG; capas de Photoshop; *shader* toon, Line Art y luz en Blender; **7 modelos con esqueleto** CC BY; encuadre por emoción (Punto 18). Sin fuente: el programa que usa Isayama hoy y quién puso grano y aberración ⚠️; los *rigs* no se probaron en Blender |
| 19 · Texturas 2D | ✅ | trama y rayado mirados en dos páginas de manga de la wiki; papel, tela y cuero CC0 (ambientcg); no hay estampados en los uniformes (buscado en inglés y japonés); emblemas con vector libre (Punto 19). La licencia de los pinceles de semitono no cargó ⚠️ |
| 20 · Gustos y detalles | ⚠️ | cumpleaños, altura, sangre, objeto y cómo se ve cada uno de los 5, con datos de entrevistas a Isayama (Punto 20). **No encontré la comida favorita** de Erwin, Hange, Eren y Mikasa (AoT no tiene *databook* de gustos); varias alturas y manías con una sola fuente |
| 21 · Por qué la aman, y las escenas que hacen llorar | ✅ | ventas, premios, encuesta de público y crítica; con quién se identifica (post de 1080 votos); **3 escenas con minuto exacto** de los subtítulos de Netflix (eps. 55, 67 y 93), qué pasa, por qué duele, música, cómo está dibujada y reacción (1399 votos); lo que hace gritar y reír (Punto 21). Frases en traducción nuestra: sin muestra latina |
| 22 · Fan dubs y comunidad hispana | ⚠️ | 5 *fandubs* y una parodia, 6 covers latinos de openings y una lista, debate de doblaje en TikTok (@elxokas, @fangirlcast) (Punto 22). **Vistas de YouTube sin comprobar**: pedía «iniciar sesión» toda la tanda; sólo las de Dailymotion por API. Parodia hispana larga: no la encontré |
| 23 · Colaboraciones, figuras y cosplay | ✅ | *Fortnite*, *Monster Strike*, *Puzzle & Dragons*, UNIQLO, cafés (uno abierto hasta el 12-oct-2026, con arte nuevo de WIT), Universal Studios Japan, expo, escape rooms; **8 figuras de Good Smile** de los 5 con sus caras; el Titán Acorazado de Hartigan y cosplay CC (Punto 23). *Ninjala* con una fuente ⚠️ |
| 24 · Obras parecidas | ✅ | 12 recomendaciones de AniList con votos; influencias que reconoce Isayama (*Parasyte*, *Evangelion*, kaiju, *Berserk* para Mikasa); láminas vecinas del servidor y cómo no repetirlas (Punto 24) |
| 25 · Mundo, historia y símbolos | ✅ | 5 reglas del mundo, **9 arcos** con volumen y momento clave (wiki), emblemas, objetos y vocabulario (Punto 25). Los episodios del anime por arco, sin comprobar ⚠️ |
| 3 conceptos de lámina | ✅ | reglamento del cuartel, sentencia, bandera; con cinta del color del episodio y poses con número (§19). En el repaso corto ganan el *rig* de Levi, las caras de las figuras, texturas CC0 y el encuadre por emoción |
| 40 fuentes distintas | ✅ | **113 dominios** enlazados tras el repaso corto (antes 67; nuevos: entrevistas y análisis de técnica, Good Smile, ambientcg, Sketchfab, TikTok, Dailymotion, noticias de colaboraciones), más APIs sin enlace (Arctic Shift, Poly Haven) |
| Fuentes oficiales | ⚠️ | web, X y PDF de MAPPA, portal, Koei Tecmo (webs de *AoT 2* y *AoT 3*, Steam), Crunchyroll, Pony Canyon; artbook de Asano y director de arte identificados. **Falta**: hojear el artbook, comentarios de Blu-ray y una entrevista de diseño leída |
| Otros idiomas | ✅ | japonés, coreano y **chino** (Bangumi por API y Wikipedia china; Moegirl y Baidu no dejaron entrar) |
| Wikis, TV Tropes, TCRF, Wayback | ⚠️ | Fandom, Doblaje Wiki, namu.wiki, Wikipedia china, Bangumi, TV Tropes, TCRF sí; Wayback sólo respondió su API, las páginas no (dos intentos en cada pasada) |
| Foros y comunidades | ✅ | Reddit (Arctic Shift), dcinside, fmkorea, ResetEra, Tumblr |
| Arte (Pixiv, ArtStation, DeviantArt) | ✅ | con autor y tamaño; ArtStation dio 403 en esta mitad |
| Vídeo | ✅ | YouTube mirado por *storyboard*; TikTok enlazado |
| Código y recursos | ✅ | GitHub (subtítulos, fuentes, fans), Sketchfab, Poly Haven |
| Doblaje latino (Doblaje Wiki, ANMTV, Crunchyroll, entrevistas) | ⚠️ | todo salvo las entrevistas a actores en YouTube: no se pudieron ver ni oír |
| Mirar los vídeos (opening, ending, tráiler, 3 escenas) | ⚠️ | hecho por *storyboard* (plan B de `AYUDANTE.md`): OP 2, ED 1, 2 tráileres, eps. 15, 53, 64, 71 y 73. No en movimiento: en el cierre el vídeo siguió dando 403 o «iniciar sesión» (8 intentos, 4 clientes) |
| Frases latinas textuales de clips oficiales | ✅ | **subtítulos automáticos en español de los 3 clips doblados de Crunchyroll en Español**, con minuto y `&t=` (§9.4): la gente del ep. 71, Willy y Eren (ep. 64), Zeke (ep. 73). Levi no habla en ninguno: sus frases, de las muestras de Doblaje Wiki (§9.3) |
| Hojas de contacto | ✅ | 3 JPEG en `hojas/` (0,6-0,7 MB), miradas, con tabla de números (§2.0) |
| `referencias.json` | ✅ | **218 entradas**: las 40 de antes primero; luego las de las partes (fotogramas de las escenas que hacen llorar, *rigs*, manga, texturas) y las útiles de `datos.json` (wiki, cosplay CC, fondos, fan art, AniList medido hoy). Las 29 últimas son páginas sin imagen propia (noticias de colaboraciones, figuras, modelos 3D), sin tamaño |

---

## 21 · Bitácora de búsqueda

### Primera pasada (24-sep-2026, mañana, red cerrada)

**Red**: `community.fandom.com` → 000 (403). WebFetch bloqueado para todo menos
GitHub. codeload.github.com → 403. `raw.githubusercontent.com` y la API de
búsqueda de GitHub sí respondían.

**Búsquedas web (48; en la 49.ª se agotó el cupo de la sesión)**, con su idioma:

1. EN · AoT Final Season key visual MAPPA → Anime Corner, PDF de MAPPA, CBR, Gamenguide
2. JA · 進撃の巨人 キービジュアル 描き下ろし → Natalie, eiga.com, animatetimes, Lisani, collabo-cafe
3. EN · encuestas oficiales → X @AoTWiki, ANN 2015, Fandom (1.ª a 4.ª), ResetEra
4. ES · reparto latino → K-magazine, Doblaje Wiki, 3DJuegos, Diario Hoy
5. ES · Doblaje Wiki (dominio) → fichas de la serie, la franquicia, Levi y los juegos
6. ES · Crunchyroll y ANMTV → ANMTV 2021, 2022, 2023 y 2025, Crunchyroll
7. ES · «Alfredo Gabriel Basurto» → Doblaje Wiki, WikiDex, BTVA, TikTok
8. ES · Hange y «Laura Torres» → Doblaje Wiki Hange, TikTok (Rossy Aguirre), Dailymotion
9. ES · Erwin y «Octavio Rojas» → La Mole, Doblaje Wiki, Dailymotion
10. ES · Mikasa y «Ana Lobo» → Doblaje Wiki, StarCon, Anime Argentina
11. ES · Rossy Aguirre y Hange → Doblaje Wiki, iHeart, wdnes
12. ES · elenco de FUNiAnime → FUNiAnime (lista completa), Senpai, eldoblaje
13. ES · «consagren sus corazones» → YouTube de Crunchyroll, Facebook, TikTok
14. ES · frases de Levi en latino → YouTube y TikTok (**no hay frases transcritas**)
15. EN · Keith Shadis, ep. 3 → TV Tropes, Fandom, namu.wiki, YouTube
16. EN · «Perfect Game» y «Hero» → Fandom, TV Tropes, IMDb, In Asian Spaces
17. EN · ep. 14, el juicio → Fandom, TV Tropes, un blog de reseñas
18. EN · ep. 16, el discurso → Fandom, IMDb, Screenspy
19. EN · interfaz de *Wings of Freedom* → DSOGaming, Koei Wiki, Wikipedia, Steam
20. EN · TCRF (dominio) → AoT, *Assault* y *TACTICS*
21. EN · Game UI Database (dominio) → **nada de AoT**
22. EN · TCRF, contenido sin usar → *AoT 2*
23. EN · historia de *AoT 2* → RPG Site, GodisaGeek, Gaming Nexus, PSU, GameFAQs
24. EN · *AoT VR Unbreakable* → UploadVR, Screen Rant, Meta
25. EN · visual del opening de *AoT 3* → Gematsu, GoNintendo, GamingBolt, portal oficial
26. EN · fuente del logo → betterstudio, FontBolt, FontSpace, dafont
27. EN · rotulación de Kodansha → catálogos de biblioteca, Internet Archive
28. EN · *AoT 3*, fecha → RPG Site, ANN (dos noticias), AniTrendz, Collider, Gamespress
29. EN · Día de AoT 2026 → Anime Corner, portal oficial, Crunchyroll, Fandomwire
30. JA · 進撃の巨人3 → Gamer, gamebiz, Famitsu, 4Gamer, X @kt_shingeki, shingeki.tv
31. EN · demostración de *AoT 3* → web de Koei, dlcompare, Gematsu, NoobFeed, YouTube
32. JA · 進撃の巨人3 実機 → 4Gamer (tres artículos), Denfaminicogamer, Gamecity
33. EN · dibujo de Isayama del Día de AoT → Anime Corner, CBR, Screen Rant, ComicBook
34. EN · personalidad de Levi → Fandom (dos fichas), Wikipedia, dos análisis
35. EN · «give up on your dreams» → Goodreads, YouTube, CBR, Substack, Tumblr
36. EN · Hange → Fandom (Hange, Sawney y Bean), 16typesofsoul
37. JA · リヴァイ 口調 名言 → anime.eiga, ameblo, note, urbanlegend, animenb, Torchlight Hub, Selvy
38. EN · Erwin y sus discursos → Know Your Meme, Medium, IMDb
39. EN · Mikasa → Wikipedia, Medium, Poggers, Tumblr
40. JA · リヴァイ ロボット掃除機 → Famitsu, ねとらぼ, Game Watch, Robostart, PR Times, collabo-cafe
41. EN · el aspirador de Levi → ANN, SoraNews24, Hypebeast, AniTrendz, Anime Anime Global
42. EN · limpieza del ep. 15 → AnimeVice, Know Your Meme, YouTube, Fandom
43. JA · 人気投票 → Oricon, ねとらぼ (dos), Magapoke, ameblo, setochan
44. EN · 1.ª encuesta (dominios Fandom y ANN) → Fandom, ANN 2017
45. KO · 진격의 거인 인기투표 → namu.wiki, fmkorea, dcinside (dos), ruliweb
46. EN · openings y endings → Fandom, Spotify, TierMaker, YouTube
47. EN · canciones de Sawano → Wikipedia, Fandom, Lyrics Translate, namu.wiki
48. EN · Kohta Yamamoto → Fandom, Wikipedia, YouTube, ComicBook
49. JA · 美術監督 背景 → **no se hizo (cupo agotado)**
50. EN · entrevista a Kyoji Asano → **no se hizo**
51. JA · 岸友洋 インタビュー → **no se hizo**

**GitHub** (búsquedas y descargas):
- `google/fonts`: METADATA de 23 fuentes, y 13 fuentes bajadas y comprobadas con
  fontTools.
- Búsqueda de repositorios «attack on titan font/eldian», «attack on titan
  blender/3d/odm» y «shingeki no kyojin»: salen 11 repositorios, citados en el
  punto 4.
- Búsqueda de código:
  - «Legión de Reconocimiento»: 30 archivos.
  - «consagren sus corazones»: 1 archivo.
  - `data/characters.json` de [attack-on-titan-api](https://github.com/ZachMcM/attack-on-titan-api):
    Levi con 30 años y altura «unknown».
- Imágenes de [khalil-hamidani/SNK](https://github.com/khalil-hamidani/SNK):
  bajé 10, las miré y medí los hex. Se quedan en mi carpeta temporal, **no en el
  repositorio**.

**Fuentes distintas consultadas: más de 90**, de estos tipos:
- **Oficiales**: aot-portal, shingeki.tv, las webs de Koei Tecmo América y de
  Gamecity, X oficiales, el PDF de MAPPA, Crunchyroll News.
- **En japonés**: Natalie, Famitsu, 4Gamer, ねとらぼ, eiga, animatetimes,
  Oricon, Magapoke, Gamer, gamebiz, AppBank, Denfaminicogamer.
- **En coreano**: namu.wiki, fmkorea, dcinside, ruliweb.
- **Wikis**: Fandom AoT, Doblaje Wiki, WikiDex, namu.wiki, TV Tropes, TCRF.
- **Foros y comunidades**: ResetEra, discusiones de Fandom, Tumblr, dcinside.
- **Vídeo**: YouTube, TikTok, Dailymotion.
- **Código**: GitHub.
- **Doblaje**: ANMTV, FUNiAnime, K-magazine, 3DJuegos, La Mole, Anime Argentina.

**Lo que NO encontré o no pude mirar** (en la primera pasada; casi todo se
resolvió en la segunda):
- Hojas de contacto: no hay red.
- Fan art con autor.
- Sketchfab y Poly Haven nuevos.
- Cajas de diálogo de los juegos.
- Fuentes en chino.
- Reddit y Wayback Machine.
- Entrevistas de arte.
- Minutos exactos.
- Una frase latina de Levi.

### Segunda pasada (24-sep-2026, tarde, red abierta)

**Primera mitad** (ayudante anterior; su carpeta de trabajo se perdió, así que
esto sale de lo que dejó escrito):
- `investigar_serie.py` sobre `attackontitan.fandom.com`, 3 tandas: personajes
  (1479 imágenes), episodios y fichas (175), sitios (161). Montó y miró las 3
  hojas de `hojas/`.
- Doblaje Wiki por la API: la serie, la película, fichas de actores; 16
  muestras de audio pasadas por Whisper (modelo *small*, español).
- Subtítulos japoneses de Netflix del espejo de kitsunekko (GitHub).
- Sketchfab (API de modelos: licencia y autor), Poly Haven (API), `google/fonts`
  con fontTools, Pixiv (búsqueda pública), DeviantArt (oEmbed), FUNiAnime,
  ANMTV, el portal oficial, Koei Tecmo, 4Gamer, Famitsu, Gematsu.
- YouTube con yt-dlp: datos y *storyboards* del OP 2, el ED 1 y el tráiler.

**Segunda mitad** (esta sesión). Sin buscador web: todo por red directa.

| Qué (idioma) | Cómo | Resultado |
|---|---|---|
| Tamaños de 88 imágenes de las hojas (EN) | API de Fandom, `prop=imageinfo` | los 88 coinciden con lo escrito |
| Erwin, el uniforme, Levi (EN) | API de Fandom: `Erwin_Smith_(Anime)`, `Erwin_Smith`, `Military_(Anime)`, `Levi_Ackermann_(Anime)`, `Hange_Zoë_(Anime)` | brazo en el ep. 36 y saludo con la izquierda; uniforme de 850 y 854; Levi 160 cm |
| Monroy, Toriz, «Legión» (ES) | API de Doblaje Wiki: `Attack_on_Titan`, `Ivett_Toriz`, `Carlos_Monroy`; FUNiAnime y ANMTV (texto) | Toriz = Levi niño, ep. 47; Monroy sin segunda fuente; «Legión» no aparece en ningún texto |
| Minutos (JA) | espejo de kitsunekko (clon parcial con git): eps. 3, 9, 14, 15, 16, 19, 22, 53, 71 y 73; búsquedas 約束, 意志, 力を, 心臓を捧げよ, キース, 夢を諦めて | la frase de Levi es del ep. 9 · 06:57; el grito del clip es del ep. 71 · 12:31-12:57; Keith, ep. 73 · 16:10 |
| Vídeos (JA, ES, EN) | yt-dlp: datos de los 31 enlaces de YouTube de la biblia (todos existen); *storyboards* de 13 vídeos → `fotogramas.py` | hojas de OP 2, ED 1, PV 2012, tráiler latino, eps. 15, 53, 64, 71, 73, demo y emisión de *AoT 3*, cartelas, voz de Levi |
| Búsquedas en YouTube (ES) | `ytsearch`: «Attack on Titan doblaje en español Crunchyroll Levi»; «"Legión de Exploración" Attack on Titan» | clips oficiales de Crunchyroll en Español; títulos de fans con «legión de exploración» (3) y «de reconocimiento» (1) |
| Portal oficial (EN/JA) | página del Día de AoT y sus imágenes | dibujo de Isayama, visual 9/9, trajes de la tienda; tamaños medidos |
| Anime Corner (EN) | artículo de MAPPA 15 | la imagen original: Mikasa de espaldas |
| Wallhaven (EN) | API: «levi ackerman» y «survey corps» (0 resultados con el filtro de anime y 1920×1080), «attack on titan» por favoritos (549) | 12 miradas, 5 útiles (§17) |
| DeviantArt (EN) | oEmbed de «Wir sind die Jäger» | autor Deto15 |
| ArtStation (EN) | JSON de dos proyectos | **403** dos veces: autores sin ver |
| Reddit (EN) | Arctic Shift: búsqueda «Levi cleaning» (se agotó el tiempo) y luego por título | 10 hilos, el mayor con 4275 votos |
| Wayback Machine | API de disponibilidad y la página de 2013 | la API dice que hay copia; la página se cortó dos veces |
| Espejos de YouTube (Piped, Invidious) | API de 7 instancias | ninguna devolvió el vídeo |

**Cierre** (tercer ayudante, 24-sep-2026, tarde). Buscador web: 6
búsquedas; lo demás, por red directa.

| Qué (idioma) | Cómo | Resultado |
|---|---|---|
| YouTube, vídeo (JA, ES) | `fotogramas.py` y yt-dlp a mano: 8 intentos, clientes por defecto, `tv`, `web_safari` y `mweb`, formato 18 | los datos sí; **el vídeo, 403** o «iniciar sesión». Nada en movimiento |
| YouTube, subtítulos (ES) | `--write-auto-subs --sub-langs "es.*"` en los 3 clips doblados de Crunchyroll en Español (2-3 intentos cada uno) | **los tres bajados** (§9.4) |
| YouTube, búsqueda (ES) | `ytsearch25` y `ytsearch40`: «Attack on Titan (doblaje en español)» | el canal oficial sólo tiene **3 clips doblados**; el resto son subidas de fans |
| TikTok (ES) | yt-dlp sobre un vídeo de @crunchyroll_la (CCXP, Ana Lobo y Mike Leal) | error de yt-dlp: no se pudo |
| Steam (EN) | API `storesearch` y `appdetails` de las apps 601050, 449800 y 2916700 | 20 capturas de 1920×1080, miradas en 2 hojas; menús de *AoT 3* con hex |
| Web oficial de *AoT 2* (JA) | `gamecity.ne.jp/shingeki2/system.html`, `system2.html`, `system3.html` | 12 capturas de «日常パート» y «交流»: **caja de diálogo**, Levi con mascarilla, cadetes barriendo |
| Koei Tecmo América (EN) | `koeitecmoamerica.com/aot2/` | 404 |
| Bangumi (ZH) | API `search/subject`, `v0/subjects/55770/characters`, `v0/characters/<id>` (25 personajes) | nota 8,2; Mikasa 1019 favoritos, Levi 776; apodos 兵长 y 一米六 |
| Moegirl (ZH) | API y `action=raw` | «未授权操作» (2 intentos) |
| Baidu Baike (ZH) | página de Levi | 403, «百度安全验证» |
| Wikipedia china (ZH) | API `prop=extracts` de «進擊的巨人角色列表» | al 2.º intento (el 1.º, 429): la taza, la manía de limpiar |
| Wikipedia japonesa (JA) | API de 吉原俊一郎 | 429 |
| Fandom (EN) | galerías «Hange Zoë (Anime)», «Mikasa Ackermann (Anime)», «Eren Jaeger (Anime)» (`/Image Gallery`), `imageinfo` de 18 imágenes; búsqueda de texto «Levi tea cup rim»; páginas «Levi Ackerman» y «Bad Boy» | 18 poses miradas en una hoja; la taza por el borde confirmada en «Bad Boy» |
| Buscador (JA) · 進撃の巨人 美術監督 吉原俊一郎 インタビュー 背景 | → OTACTURE, eiga.com, WIT STUDIO (404) | director de arte con dos fuentes; «nubes Yoshihara» |
| Buscador (EN) · Kyoji Asano Attack on Titan character designer interview Levi design | → ANN, recopilación de Tumblr (entrevista de Otomedia) | la traducción de Tumblr ya no existe; Wayback: API sí, página no (2 intentos, curl y WebFetch) |
| Buscador (JA) · 浅野恭司 インタビュー 進撃の巨人 キャラクターデザイン 線 影 リヴァイ | → shingeki.tv (artbook), ABEMA Times | artbook oficial de 2017; la entrevista de 2024 no habla del diseño |
| Buscador (EN) · tiktok crunchyroll_la Attack on Titan doblaje latino Levi | → TikTok de @crunchyroll_la y de fans | ver fila de TikTok |
| Buscador (ES) · «Carlos Monroy» «Attack on Titan» asistente · «Ivett Toriz» Levi niño | → Doblaje Wiki, ANMTV 2020, eldoblaje.com | ANMTV sólo nombra a Monroy como voz de Samuel; Toriz, sólo Doblaje Wiki |

**Lo que NO encontré en esta pasada**: un texto oficial con «Legión de
Exploración»; una segunda fuente para Monroy y Toriz; los autores de dos fondos
de ArtStation; la caja de diálogo de *Wings of Freedom*; el vídeo de YouTube en
movimiento; una frase latina de Levi en un clip oficial (no habla en los tres
que hay); una entrevista de diseño leída por dentro; comentarios de los Blu-ray.
(Resuelto en el cierre: subtítulos en español de los clips oficiales, la caja
de diálogo de *AoT 2*, fuentes en chino, el director de arte y el artbook.)

<!-- Enlaces de la segunda pasada (en la vista de lectura no se ven) -->
[dw-aot]: https://doblaje.fandom.com/es/wiki/Attack_on_Titan
[dw-film]: https://doblaje.fandom.com/es/wiki/Attack_on_Titan:_El_ataque_final
[dw-basurto]: https://doblaje.fandom.com/es/wiki/Alfredo_Gabriel_Basurto
[funi]: https://funianime.com/conoce-al-elenco-del-doblaje-latino-de-attack-on-titan/
[anmtv-film]: https://www.anmtvla.com/2025/03/opinion-attack-on-titan-el-ataque-final.html
[anmtv-premio]: https://www.anmtvla.com/2025/05/crunchyroll-anuncia-los-ganadores-de.html?m=1
[lamole]: https://lamole.com.mx/expositores/octavio-rojas/
[animearg]: https://animeargentina.net/cumpleanos/ana-lobo-doblaje-biografia/
[imdb-ono]: https://www.imdb.com/title/tt9898836/characters/nm1328775/
[kitsu]: https://github.com/Ajatt-Tools/kitsunekko-mirror/tree/main/subtitles/anime_tv
[yt-consagren]: https://www.youtube.com/watch?v=nxQCiDpxeMY
[yt-zeke]: https://www.youtube.com/watch?v=wOzu2yF4HC4
[yt-guerra]: https://www.youtube.com/watch?v=pNRP0z8IwHQ
[yt-esp1]: https://www.youtube.com/watch?v=sFuAhHTgABs
[yt-esp2]: https://www.youtube.com/watch?v=jE89EBeajgg

### Repaso corto (24-sep-2026): puntos 18-25

Juntado de las bitácoras de `partes/texto.md`, `partes/imagen.md` y
`partes/voz.md`. Buscador web: **unas 35 búsquedas** entre los tres (texto 12, imagen 14, voz 9);
lo demás, red directa.

**Texto (18, 24, 25 y el 5 nuevo)**, buscador en inglés y japonés:
- EN: técnica de Isayama y calco de fotos (sin resultado sobre calco); WIT y
  el 3DCG del equipo de maniobras (SlashFilm, UK Anime Network, CBR, Sakuga
  Blog); MAPPA y el cambio de estilo (Gamerant, AnimeIgnite, CBR,
  Twinfinite); influencias (IMDb, Lambiek); arcos (wiki); Line Art en Blender
  (StraySpark, manual); Clip Studio de Isayama (sin confirmar); onomatopeyas
  (ANN, JLA/UGM); encuadres (RedQStudios); grano y fotografía (Araki en
  fullfrontal.moe, sin dato de grano).
- JA: 諫山創 作画 背景 写真 トレース インタビュー (entrevista de Clip Studio);
  進撃の巨人 漫画 モノローグ 心の声 ふきだし なし (Yahoo!知恵袋, Jun 34).
- Red directa: API de la wiki («Story Arcs», «Founding Titan», «Curse of
  Ymir»); API de Sketchfab (*rigs*, licencia); `google/fonts` en GitHub y
  fontTools (Comic Neue, Bangers, Zen Maru Gothic, Jost Italic, Bungee);
  Fontsource y jsdelivr (Kosugi Maru, descartada); lectura de otras biblias
  del servidor para el Punto 24.3.

**Imagen (19, 23)**, buscador en inglés y español:
- *Fortnite*; gachas (*Puzzle & Dragons*, *Monster Strike*); cafés (Animate,
  Tower Records); *Levi's* (nada); Good Smile (Nendoroid y figma de los 5);
  cosplay (World Cosplay Summit, Hartigan); trama de Isayama; pinceles de
  semitono libres; Universal Studios Japan; UNIQLO.
- Red directa: API de la wiki (`list=search` y `allimages` con prefijo
  «Manga»; tamaño de 2 páginas de manga, bajadas y miradas); API de
  ambientcg (`wool`, `leather`, `paper`, `canvas`).
- WebFetch: ScreenRant, Siliconera, Anime Corner, Brusheezy (su licencia
  no cargó entera). Ningún 403 ni 404.

**Voz (20, 21, 22)**, buscador en español:
- *fandub* latino, covers de openings, parodias y memes de TikTok, «Attack on
  Titan Requiem», «Seid ihr das Essen» en español (nada), «abridged» en
  español (nada).
- Red directa: API de la wiki con `User-Agent` propio (sin él, 403): Trivia,
  Personality y Relationships de los 5; episodios 54, 55, 67 y 93; «Call of
  Silence»; letra del opening 1. API de Wikipedia (ventas, crítica, premios).
  Reddit por Arctic Shift (posts de «cried», «finale» y el hilo de sonidos).
  API de Dailymotion (vistas). 4 fotogramas de la wiki bajados con `Referer`
  y mirados.
- **Subtítulos japoneses de Netflix** (kitsunekko en GitHub, clonado
  disperso): eps. 55, 67 y 93, leídos con Python filtrando por palabra; de
  ahí salen los minutos del Punto 21.
- **YouTube pidió «iniciar sesión» toda la tanda**: no se usó `yt-dlp`.

**Redactor**: medí con Pillow los 17 retratos y portadas de AniList de
`datos.json` (230×345 a 1900×400) para `referencias.json`; dejé fuera 9
fondos de Wallhaven que no son de la serie o no se sabe.

**Lo que NO encontré en este repaso** ⚠️: el programa digital de Isayama;
una fuente que nombre el grano y la aberración del anime; la letra del manga
en inglés; la prueba de los *rigs* en Blender; la comida favorita de Erwin,
Hange, Eren y Mikasa; fotogramas de rabia de Hange y de miedo de Hange, Mikasa
y Eren; las vistas de YouTube; una parodia hispana larga; el chiste alemán en
español; una colaboración de *Levi's*; fecha y personajes de *Ninjala*; la
licencia completa de los pinceles de Brusheezy; los episodios del anime de
cada arco comprobados uno a uno.
