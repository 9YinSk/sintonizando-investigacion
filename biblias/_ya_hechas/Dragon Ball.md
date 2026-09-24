---
tags: [biblia, serie, laminas]
serie: "Dragon Ball"
canal: "#reto-de-la-semana"
fecha: 2026-09-23
---

# Biblia · Dragon Ball (para #reto-de-la-semana)

> [!danger] Por qué se rehace esta investigación
> Sus palabras exactas sobre las láminas anteriores: «tomas referencias muy
> cortas, sólo un par de imágenes; los personajes salen de pie con una ropa,
> cuando la gente y el arte promocional los muestran con su objeto típico, en
> portadas, con amigos, en poses de verdad; no miras vídeos ni descripciones;
> no te empapas del tema; las láminas quedan planas y parecen IA». En la tabla
> de reparto de `Discord - biblia de laminas v3 (23-sep-2026)` este canal
> figuraba como «hecha (le gustó Goku)» — pero el veredicto real es que se
> rehace. Esta nota es sólo investigación: no dibuja, no publica, no instala nada.

## 1 · Referencias visuales — cuántas y dónde están

El script `laminas_v2/v3/investigar_serie.py` bajó de **dragonball.fandom.com**
todas las imágenes enlazadas desde las páginas de Goku, Nube Voladora,
Kamehameha, Báculo Sagrado, Shenron y Radar del Dragón (y sus galerías):
**1.703 imágenes** listadas y medidas, montadas en hojas de contacto numeradas en

```
C:\Users\Proye\Desktop\YinX\herramientas\laminas_v2\v3\referencias\dragon-ball\hoja_01.jpg, hoja_02.jpg, ...
```

(mira cualquier hoja con la herramienta Read; están ordenadas de la imagen más
grande a la más chica, así que las primeras hojas concentran el arte de
artbook y los renders de videojuego en alta resolución).

🔴 **Aviso técnico**: mientras yo trabajaba, había **otros tres procesos
Python corriendo a la vez sobre esta misma carpeta** (`ps aux` los mostró con
PIDs distintos) — probablemente otra sesión tocando el mismo `laminas_v2/v3`.
Eso reescribía `indice.json` mientras yo lo leía, y los **números de la hoja de
contacto se corrieron** respecto al índice final. Para no bajar la imagen
equivocada, las 18 elegidas se bajaron **por su título exacto de archivo en la
wiki** (no por número), con un script aparte que no toca `indice.json`. Quedaron
guardadas como `titulo_*.png` (y cinco que sí coincidieron por número:
`009.png`, `016.png`, `028.png`, `033.png`, `077.png`). Si se vuelve a correr
`investigar_serie.py` en esta carpeta compartida, conviene comprobar que no
haya otra sesión escribiendo a la vez.

### Las 18 elegidas

Todas dentro de `referencias/dragon-ball/`:

| Archivo | Qué es | Para qué serviría |
|---|---|---|
| `016.png` (3085×3300) | Goku niño en la **Nube Voladora**, con el **Báculo Sagrado**, fondo verde (recortable) | el objeto+vehículo icónico completo en una sola imagen, listo para cortar |
| `titulo_Goku_art_Daizenshuu_1_.png` (1374×2048) | Arte oficial de **Toriyama** (Daizenshuu), Goku niño de pie, fondo blanco | línea y color de referencia «de la fuente», recorte limpio |
| `titulo_Goku_art_for_WJ_No_44_1985_.png` (1616×1698) | Portada de **Weekly Jump** 1985, Goku joven en postura de karate, fondo blanco | el objeto «portada de revista» real, no inventado — clave para el concepto 3 |
| `titulo_The_Last_Wish_Goku.png` (1403×2756) | Goku Super Saiyan, pose de combate dinámica, fondo oscuro liso | silueta de acción recortable, alta |
| `077.png` = `GokuRecievesHisKamehameha.png` (1445×2041) | Fotograma DBZ: Goku joven adulto, gi rasgado, postura de poder a dos puños, piso rojo dramático | pose de combate **de verdad** (no de pie), luz y color ya resueltos |
| `titulo_Raging_Blast_2_SSJ3_Goku_Alternate_outfit_.png` (1280×2180) | Render de videojuego, SSJ3 Goku, pose de ataque, fondo blanco | recorte limpio, forma muy dinámica |
| `titulo_Raging_Blast_2_SSJ_Goku_Alternate_outfit_.png` (1280×2176) | Render de videojuego, SSJ Goku, puños al frente, fondo blanco | ídem, otra pose |
| `titulo_Sparking_Zero_Goku_Z_End_artwork.png` (1382×1843) | Arte oficial 2024 del videojuego **Sparking! Zero**, Goku base, fondo verde | el Goku «de ahora», estilo moderno oficial |
| `titulo_Sparking_Zero_SSJ_Goku_Z_End_artwork.png` (1382×1843) | Misma serie, versión Super Saiyan | pareja de la anterior, para mostrar transformación |
| `033.png` = `Dragon Radar - The World's Strongest - 001.png` (3840×2160) | Primer plano del **Radar del Dragón** encendido, en 4K | el objeto perfecto para «pantalla donde se escribe info»: ya es una pantalla con puntos |
| `028.png` = `XV2 - Power Pole Pro Future Warrior.jpg` (3840×2160) | Render de videojuego del **Báculo Sagrado** extendido, en 4K | el báculo solo, para usarlo como elemento de composición (borde, marco) |
| `009.png` = `Shenron(PtP).png` (4096×3072) | Primer plano oficial de **Shenron** | fondo/telón de fondo mítico, el «genio que concede el reto» |
| `titulo_Dragon_Ball_Promotional_Postcard.png` (1585×2341) | Arte promocional oficial: Gohan niño, Bulma, Chichi y Oolong juntos | **con amigos**, lo que pidió expresamente que faltaba |
| `titulo_Characters_Special.png` (1500×1500) | Arte de grupo oficial con el reparto completo | referencia de estilo para dibujar varios personajes juntos, si hiciera falta |
| `titulo_GokuIsHealed_.png` (1352×2816) | Goku de pie, brazos cruzados, gi limpio, fondo neutro | referencia de proporciones/uniforme «de descanso», por si se necesita un plano tranquilo |
| `titulo_Capsule_corp_night.png` (1920×1080) | Fotograma oficial: **Corporación Cápsula** de noche, iluminada | el edificio-sitio icónico, para fondo con profundidad |
| `titulo_Broly_Call_Me_Kakarot.png` (1920×1080) | Primer plano de Goku (película *Broly*), gesto en la frente, expresión de reto | referencia de **gesto de la cara**, no sólo cuerpo entero |
| `titulo_DBXV2_Kame_House_Interior_Attack_Ball...jpeg` (1920×1080) | Interior de la Casa de Kame Sennin, una Cápsula de Ataque exhibida en un estante (render de videojuego) | referencia de **interior** de la Casa de Kame Sennin — salió más «objeto en un estante» que «escena habitable»; si se necesita el interior completo, buscar otro fotograma |

## 2 · Lenguaje visual (Toriyama y Toei)

- **Línea**: *ligne claire* sintetizado — trazo limpio y decidido, casi sin
  tramas ni relleno negro, sombreado plano en 1-2 tonos por color (nunca
  degradados suaves). Toriyama citó como influencias a Osamu Tezuka y a *101
  dálmatas* de Disney. ([TCJ](https://www.tcj.com/reading-without-words-akira-toriyamas-visual-manga-and-its-cross-cultural-impact/), [Kanzenshuu](https://www.kanzenshuu.com/forum/viewtopic.php?t=13464))
- **Paleta**: colores primarios brillantes, poco negro. Hex de referencia
  (⚠️ aproximados, de sitios de fans — no son el color script oficial de Toei,
  úsense sólo como punto de partida):
  - Naranja del gi: `#D67711` / variante más viva `#FF9922` ([brandpalettes.com](https://brandpalettes.com/dragon-ball-color-codes/))
  - Azul del Kamehameha cargándose: de `#4392A5` a blanco casi puro en el
    núcleo ([color-hex.com](https://www.color-hex.com/color-palette/9288))
  - Contornos: negro puro; ropa de descanso, azul marino + naranja quemado.
- **Ki y velocidad**: el efecto de energía y la silueta dominan el cuadro por
  **espacio negativo** alrededor (fondo casi vacío o muy oscuro para que el
  aura brille); líneas de velocidad rectas y radiales, nunca curvas suaves.
- **Manga — globos y cartelas**: los globos de grito se dibujan **dentados**
  (como una explosión, no ovalados); los combates casi no llevan globo, la
  onomatopeya ocupa el cuadro entero en katakana grande. Las cartelas de
  capítulo son rótulos rectos, gruesos, con la numeración del capítulo. El eje
  de lectura lo marcan los globos y las onomatopeyas, no el texto corrido. ([Manga iconography](https://en.wikipedia.org/wiki/Manga_iconography), [Comics Journal](https://www.tcj.com/reading-without-words-akira-toriyamas-visual-manga-and-its-cross-cultural-impact/))

## 3 · Tipografía

Ya están instaladas y listas para usar (del encargo `laminas_v2/ENCARGO.md`):
**Saiyan Sans** (sin tildes — para títulos cortos en mayúsculas, imita el logo
oficial: arco hacia arriba, borde negro grueso, la «Z» como emblema) y **Anime
Ace 2.0** (para el cuerpo de texto dentro de globos, con acentos). El logo real
usa el mismo tratamiento en «DRAGON» amarillo → «BALL» naranja → «Z» roja con
grosor extra. ([famfonts.com](https://famfonts.com/dragon-ball-z/), [pixelframe.design](https://pixelframe.design/dragonball-z-logo-font-generator/))

## 4 · Sitios y objetos icónicos (dónde escribir la información)

- **El Radar del Dragón**: ya es una pantalla con puntos parpadeantes — el
  candidato más directo para mostrar la etiqueta del reto o el conteo de
  participantes (imagen `033.png`).
- **La portada de Weekly Shonen Jump / el tomo**: titulares, ficha técnica,
  «próximo número» — exactamente el objeto para escribir «Reto activo»,
  fecha, y las instrucciones del reto como si fueran texto de contratapa.
- **El Báculo Sagrado** extendido puede actuar de línea/marco que atraviesa la
  composición (ya lo hace en las portadas reales).
- **Corporación Cápsula** (edificio con cúpula) y **la Casa de Kame Sennin**
  (isla con palmera) son los dos «hogares» reconocibles para dar profundidad
  de fondo sin inventar arquitectura.
- **Shenron** emergiendo entre nubes verdes es el recurso visual para «se
  concede un deseo / se abre un reto».

## 5 · Poses, gestos y frases de Goku (y su reparto)

**Poses típicas**: en la Nube Voladora con el Báculo (niño); cargando el
Kamehameha con las manos juntas a la cadera antes de lanzar (torso girado,
nunca de frente); puños en guardia muy abierta, piernas separadas, gi rasgado
tras el combate (ver `077.png`); tocándose la nuca cuando bromea o se
sorprende; señalándose la frente al recordar algo (`titulo_Broly_Call_Me_Kakarot.png`).
Manías: se rasca la cabeza, sonríe con los ojos cerrados, siempre quiere
comer o pelear con «los fuertes».

**El reparto latino** (cada nombre comprobado en dos fuentes):

| Personaje | Actor/actriz | Fuentes |
|---|---|---|
| Goku adulto | **Mario Castañeda** | [Infobae](https://www.infobae.com/que-puedo-ver/2022/09/07/mario-castaneda-el-actor-que-interpreta-a-goku-a-solas-con-infobae-es-muy-emocionante-cuando-la-gente-me-dice-eres-la-voz-de-mi-infancia/), [SuperGeek.cl](https://www.supergeek.cl/noticias/programas/cinta-cosmica-mario-castaneda-la-legendaria-voz-latina-de-goku/2024-05-22/154436.html) |
| Goku / Gohan / Goten niños | **Laura Torres** (y vuelve como Goku-mini en *Daima*, 2024-25) | [Wikipedia ES](https://es.wikipedia.org/wiki/Laura_Torres_(actriz,_1967)), [FayerWayer — Daima](https://www.fayerwayer.com/entretenimiento/2024/12/22/laura-torres-estara-en-dragon-ball-daima-recordamos-su-relato-de-como-lloro-con-la-escena-mas-emotiva-de-goku/) |
| Vegeta | **René García** | [El Sol de México](https://oem.com.mx/elsoldemexico/cultura/rene-garcia-la-voz-de-vegeta-en-dragon-ball-z-unificara-a-todos-sus-personajes-en-un-solo-show-22133907), [La República](https://larepublica.pe/cine-series/2019/08/15/dragon-ball-rene-garcia-vegeta-conto-como-se-le-ocurrio-la-frase-maldito-insecto-dragon-ball-super-anime-manga-online-mexico-japon) |
| Piccolo (y Kami) | **Carlos Segundo** | [Diario del Yaqui](https://diariodelyaqui.mx/farandula/carlos-segundo-la-voz-de-piccolo-recuerda-como-se-eligieron-las-voces-de-dragon-ball/103080), [Milenio](https://www.milenio.com/espectaculos/famosos/piccolo-actor-doblaje-despide-akira-toriyama-video-viral) |
| Freezer | **Gerardo Reyero** (desde su 2ª aparición; la 1ª fue Ricardo Brust) | [Wikipedia EN](https://en.wikipedia.org/wiki/Gerardo_Reyero), [MasGamers](https://www.masgamers.com/gerardo-reyero-dragon-ball-z-voz-freezer-latino) |
| Krilin | **Rossy Aguirre** (Dragon Ball hasta DBZ ep. 60) → **Eduardo «Lalo» Garza** (DBZ ep. 61-199, Saga de Cell) | [Wikipedia ES — Eduardo Garza](https://es.wikipedia.org/wiki/Eduardo_Garza_(actor)), [Doblaje Wiki — Krilin](https://doblaje.fandom.com/es/wiki/Krilin) |
| Bulma | **Rocío Garcel** (desde 1994; también en Kai y Super) — **Mónica Manjarrez** dobló la saga de Majin Buu y GT | [FayerWayer](https://www.fayerwayer.com/entretenimiento/2024/02/04/dragon-ball-asi-se-ve-rocio-garcel-la-mujer-detras-de-la-voz-de-bulma-en-el-doblaje-latino-desde-hace-30-anos/), [Crunchyroll ES](https://www.crunchyroll.com/es-es/news/interviews/2022/8/16/entrevista-roco-garcel-la-voz-latina-de-bulma-en-dragon-ball-super-super-hero) |

**Frases icónicas, tal como suenan en el doblaje latino** (con su historia):

- **«¡Hola, soy Goku!»** — en japonés nació de una improvisación de la actriz
  original Masako Nozawa («Ossu! Ora Goku», su «idioma Goku» de broma en el
  estudio) y quedó fija en el adelanto de cada capítulo. ([AméricaTV](https://www.americatv.com.pe/cinescape/series/dragon-ball-esta-verdadera-historia-frase-hola-soy-goku-noticia-91683))
- **«Ka-me... ha-me... ¡HA!»** — la pausa entre sílabas **no existe en
  japonés**: fue un recurso actoral de Mario Castañeda para acompañar el
  esfuerzo físico, y se volvió la versión «oficial» para toda Latinoamérica
  (España la dobló como «Onda Vital»). ([SensaCine MX](https://www.sensacine.com.mx/noticias/noticia-1000179103/))
- **«¡Maldito insecto!»** (Vegeta) — nació de una improvisación de René García
  en un ensayo y quedó como su insulto de firma. ([La República](https://larepublica.pe/cine-series/2019/08/15/dragon-ball-rene-garcia-vegeta-conto-como-se-le-ocurrio-la-frase-maldito-insecto-dragon-ball-super-anime-manga-online-mexico-japon))
- «¡Yo soy el príncipe de todos los Saiyajin!» y «No es por ustedes... es por
  mi orgullo» (Vegeta). ([Fayerwayer — mejores frases de Vegeta](https://www.fayerwayer.com/internet/2024/05/24/insecto-estas-son-las-10-mejores-frases-dichas-por-vegeta-en-dragon-ball/))

## 6 · Lo que ama el fandom latino

- El acento y las pausas del doblaje mexicano son, para el público latino, más
  icónicas que el original japonés — el «Kame-hame-ha» de Castañeda es el
  ejemplo perfecto de un «error» convertido en canon. ([SensaCine MX](https://www.sensacine.com.mx/noticias/noticia-1000179103/))
- Goku es tratado como **ícono latino** por derecho propio: proyecciones
  masivas del final de *Dragon Ball Super* reunieron miles de fans en Ciudad
  Juárez y en varios países de la región. ([Sportskeeda](https://sportskeeda.com/anime/why-dragon-ball-popular-mexico-latin-america))
- Las frases de Vegeta («maldito insecto», «príncipe de los Saiyajin») viven
  como memes y sonidos recortados todo el año, no sólo en aniversarios.

## 7 · Qué NO hacer

- **No** dibujar a Goku de pie, quieto, con un solo gi liso — es exactamente
  lo que ya rechazó dos veces.
- **No** usar un globo de historieta genérico y ovalado: en Dragon Ball el
  grito va en globo dentado o directamente como onomatopeya en el fondo.
- **No** dejar el fondo vacío o de un solo color plano detrás del personaje —
  el ki necesita espacio negativo real (aura, destellos), no un color de
  relleno sin textura.
- **No** inventar un objeto «genérico de anime» para escribir la información
  cuando la serie ya tiene el suyo (el Radar, la portada de revista, el
  Báculo).
- **No** mezclar looks: si el personaje es del anime clásico (línea de los 90),
  no pegarle un fondo hecho con render 3D moderno — se nota el pegado.

## 8 · Tres conceptos para la lámina de #reto-de-la-semana

1. **«Portada de Shonen Jump»** — la cabecera entera es la portada real de una
   revista semanal (usa `titulo_Goku_art_for_WJ_No_44_1985_.png` como base de
   composición): Goku joven en pose de karate al frente, Krilin y Bulma
   chiquitos a un lado (arte `titulo_Dragon_Ball_Promotional_Postcard.png`
   recortado), «Reto activo» como la pegatina de «¡Novedad!» en la esquina
   típica de las portadas de WJ, y la Corporación Cápsula asomando diminuta al
   fondo en la profundidad para dar parallax. El texto habla desde una
   **cartela de titular de revista** (gruesa, recta), nunca desde un globo
   redondo.
2. **«El Radar que encuentra el reto»** — el Radar del Dragón (`033.png`) en
   primer plano, en la mano de un Goku adulto en pose de tres cuartos (no de
   frente), mostrando en su pantalla un punto parpadeante con la etiqueta del
   reto de la semana en vez de una esfera; la Nube Voladora cruza detrás,
   fuera de foco, y Shenron se insinúa entre nubes verdes en el fondo más
   lejano concediendo «el reto» como si fuera un deseo. El habla sale en
   **globo dentado de grito** pegado al Báculo, que atraviesa el cuadro en
   diagonal como elemento compositivo.
3. **«La misma frase, tres edades»** — como el propio ejemplo de reto que ya
   usa el foro («la misma frase, tres edades»): tres Goku recortados de las
   referencias reales — niño en la Nube con el Báculo (`016.png`), joven
   adulto en guardia con el gi rasgado (`077.png`) y Super Saiyan en pose de
   ataque (`titulo_Raging_Blast_2_SSJ_Goku_Alternate_outfit_.png`) — dispuestos
   en profundidad decreciente (grande-mediano-chico) sobre el fondo de
   Corporación Cápsula de noche, cada uno con su propia nube de ki como
   iluminación de borde para que no queden pegados unos sobre otros. El eje
   habla de que el reto también puede grabarse a distintas edades de la voz.

## Lo que no pude verificar

- No encontré una **frase fija de despedida de los avances** («continuará…» o
  similar) específica del doblaje latino con una fuente que la confirme tal
  cual — puede que no exista una fórmula única, a diferencia de «Hola, soy
  Goku». Antes de usarla en una lámina, comprobarla viendo un avance real.
- Los **hex de la paleta** de la sección 2 son de sitios de fans
  (brandpalettes.com, color-hex.com), no un color script oficial de Toei —
  sirven de punto de partida, no de cita exacta.
- No confirmé quién dobló a Krilin **después** de la Saga de Cell (Súper,
  Kai, GT) — los resultados sólo cubren Rossy Aguirre → Lalo Garza hasta el
  episodio 199. Comprobar antes de atribuir una frase de esas sagas.

## Fuentes citadas

- [The Comics Journal — Reading without words](https://www.tcj.com/reading-without-words-akira-toriyamas-visual-manga-and-its-cross-cultural-impact/)
- [Kanzenshuu — Akira Toriyama's art style](https://www.kanzenshuu.com/forum/viewtopic.php?t=13464)
- [brandpalettes.com — Dragon Ball Color Codes](https://brandpalettes.com/dragon-ball-color-codes/)
- [color-hex.com — kamehameha palette](https://www.color-hex.com/color-palette/9288)
- [famfonts.com — Dragon Ball Z font](https://famfonts.com/dragon-ball-z/)
- [Infobae — Mario Castañeda](https://www.infobae.com/que-puedo-ver/2022/09/07/mario-castaneda-el-actor-que-interpreta-a-goku-a-solas-con-infobae-es-muy-emocionante-cuando-la-gente-me-dice-eres-la-voz-de-mi-infancia/)
- [Wikipedia ES — Laura Torres](https://es.wikipedia.org/wiki/Laura_Torres_(actriz,_1967))
- [FayerWayer — Laura Torres en Daima](https://www.fayerwayer.com/entretenimiento/2024/12/22/laura-torres-estara-en-dragon-ball-daima-recordamos-su-relato-de-como-lloro-con-la-escena-mas-emotiva-de-goku/)
- [El Sol de México — René García](https://oem.com.mx/elsoldemexico/cultura/rene-garcia-la-voz-de-vegeta-en-dragon-ball-z-unificara-a-todos-sus-personajes-en-un-solo-show-22133907)
- [La República — «Maldito insecto»](https://larepublica.pe/cine-series/2019/08/15/dragon-ball-rene-garcia-vegeta-conto-como-se-le-ocurrio-la-frase-maldito-insecto-dragon-ball-super-anime-manga-online-mexico-japon)
- [Diario del Yaqui — Carlos Segundo](https://diariodelyaqui.mx/farandula/carlos-segundo-la-voz-de-piccolo-recuerda-como-se-eligieron-las-voces-de-dragon-ball/103080)
- [Wikipedia EN — Gerardo Reyero](https://en.wikipedia.org/wiki/Gerardo_Reyero)
- [Wikipedia ES — Eduardo Garza](https://es.wikipedia.org/wiki/Eduardo_Garza_(actor))
- [Doblaje Wiki — Krilin](https://doblaje.fandom.com/es/wiki/Krilin)
- [FayerWayer — Rocío Garcel](https://www.fayerwayer.com/entretenimiento/2024/02/04/dragon-ball-asi-se-ve-rocio-garcel-la-mujer-detras-de-la-voz-de-bulma-en-el-doblaje-latino-desde-hace-30-anos/)
- [SensaCine MX — el error que se volvió canon](https://www.sensacine.com.mx/noticias/noticia-1000179103/)
- [AméricaTV — historia de «Hola, soy Goku»](https://www.americatv.com.pe/cinescape/series/dragon-ball-esta-verdadera-historia-frase-hola-soy-goku-noticia-91683)
- [Sportskeeda — Dragon Ball en México y Latinoamérica](https://sportskeeda.com/anime/why-dragon-ball-popular-mexico-latin-america)

---

## 9 · Rehecha de cero (23-sep, noche): el Torneo de las Artes Marciales

> [!important] Por qué
> Tras #reglas (AoT) pidió rehacer una de las anteriores **con la misma
> profundidad**: «renders 3D, mangas, cómics, vídeos, tráilers, fan arts,
> estilos, tipos de letra, texturas, personalidad, fondos, poses, colores, ropa…
> mira vídeos, TikToks, analiza todo». Se eligió #reto-de-la-semana, la que le
> dejó «no me termina de convencer». Lámina: `v3/reto_torneo.html`.

**La idea**: el reto semanal **es** el 天下一武道会 (Tenkaichi Budōkai): se entra,
se compite una vez, «no se gana nada y esa es la gracia», y el presentador lo
cuenta todo a gritos. El objeto: **el tablón del cuadro de combates con las reglas
debajo**, que existe tal cual en la serie (manga, 22.º Torneo: «The matches of the
World Martial Arts Tournament are made»; anime, Torneo del Otro Mundo: «Bracket
and Rules»). El cartel del tablón copia el del templo cambiando 武道 (artes
marciales) por **声優 (actores de voz)**: 天下一声優会. En la lámina se ven los dos
carteles juntos: ahí está el chiste.

### Material (todo en `v3/referencias/dragon-ball-torneo/`, 354 imágenes + `sel/`)
- **Fondos pintados originales de Toei** del Torneo (títulos «Edo dragon-ball
  budokai…» y nº 262, 270, 350): ring, templo, banderas **penjor** y la **puerta
  partida balinesa** (Toriyama se inspiró en Bali: la wiki trae la comparación, nº 304).
  Se usó el **nº 350** (templo de frente con el cartel entero), ×4 con Real-ESRGAN.
- **Arte conceptual del torneo** de Toriyama (nº 1, 3377×4096): Goku, Krilin,
  Roshi, Yamcha, Nam, Ran Fan… Para otra lámina.
- **El presentador** (TB Announcer, nº 146), **Goku y Krilin estrenando el
  uniforme de la Escuela Tortuga** (sel/…first_time.png, del mismo torneo).
- 3D revisado en Sketchfab: los estadios que hay son flojos o no se bajan
  (E.Rodrigo, ErichBlair: sin descarga; 20062020year: CC BY pero de videojuego).
  No se usaron. En ArtStation, referencias de fans: Dylan Sharp (el 21.º en
  Blender) y Sylvain Sarrailh.

### El presentador (lo que se aprendió de él)
- Rubio, gafas de sol, traje azul marino, camisa rosa y corbata roja; micrófono
  siempre en la mano; en Z le sale bigote. Presenta todos los torneos de DB a GT.
- **Voz latina: Salvador Delgado** (Doblaje Wiki, ficha de la serie y la suya):
  eps. 20-28, 84-102 y 112-148 de DB; 209-232 y 289-291 de Z. Es también la voz
  del Dr. House, Qui-Gon Jinn y Sirius Black.
- En latino suelta **«¡Santo cielo!»**; en Z (TikTok revisado con Gemini) es el
  único que sabe que Goku y los suyos vencieron a Cell y no Mr. Satán, y les
  pide: **«no quiero que destruyas la plataforma como en aquella ocasión»**.
  Eso lo celebran los fans → en la lámina, la P. D. del reglamento.
- Su defecto en la serie: empieza la cuenta de 10 tarde porque se distrae.
- Reglas oficiales del torneo (wiki): sin límite de tiempo, un solo combate,
  pierde quien sale del ring, no se levanta antes de 10 o se rinde. En el
  primer torneo se sortean los números sacando un papel de una caja roja.

### Letras
- Kanji del cartel: **Yuji Boku** (pincel, como el del templo).
- Rótulos: **Potta One**. Lo escrito a mano por la organización: **Caveat
  Brush** (se lee bien pequeña). Globos: Anime Ace (grito dentado, que es como
  grita Dragon Ball).

### Recortes (y sus trampas)
- Photoshop por MCP **no se pudo**: UXP Developer Tools pide la sesión de
  Creative Cloud iniciada. Se recortó con **Adobe en la nube**
  (`asset_initialize_file_upload` → PUT → `finalize` → `image_remove_background`).
- Adobe se lleva a la gente del fondo pegada: a Goku, la mujer del vestido rojo
  y el señor gato; a Krilin, el hombre de azul. Se quitan en
  `v3/limpiar_recortes_db.py` con polígonos medidos en rejilla. El puño derecho
  y el pelo de Goku se funden con los de la mujer (misma piel, mismo negro):
  **ese lado va tapado por el poste del tablón**. El brazo de atrás de Krilin se
  calcó (su muñequera es del mismo azul que la chaqueta del hombre) y la oreja
  se repuso del original.
- El presentador pequeño que hay en el fondo nº 350: el inpainting de OpenCV
  dejaba un borrón → **queda tapado por el presentador grande**.
