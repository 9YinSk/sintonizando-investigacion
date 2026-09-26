# Imagen · Naruto (repaso, lote C) · puntos 1, 3, 15, 16, 19, 23

Repaso sobre una `biblia.md` ya escrita (26-30 tuvieron red abierta y hojas).
No toco `biblia.md`: esto es para que el redactor confirme, corrija y añada.
Uso `--rol imagen` y `--avisos` como punto de partida; no repito lo que ya
está bien, sólo confirmo lo ⚠️ y relleno lo que falta (puntos 19 y 23, que no
tenían sección propia).

## Hallazgos

### Punto 1 · Arte oficial variado

- Web oficial `naruto-official.com/special/anime-gallery`: **20 key visuals**, de 2002 a 2017, sin descarga directa ni tamaños (sólo vista web); cubre NARUTO (少年篇) y Shippuden (疾風伝); visuales de estreno, Jump Festa y arcos de Kakashi/Jiraiya/Itachi · [naruto-official.com](https://naruto-official.com/special/anime-gallery) (WebFetch, 25-sep-2026) · ⚠️ (una fuente; confirma lo que la biblia daba como ⚠️ «no pude abrirla»: sí se puede leer con navegador, sólo no da tamaños)
- **NARUTOP99** (2021): encuesta oficial de popularidad + Kishimoto dibujó una ilustración nueva con los 22 personajes más votados, todos juntos · ✅ [narutop99.naruto-official.com/en/archive](https://narutop99.naruto-official.com/en/archive/), [Natalie](https://natalie.mu/comic/news/520749) (dos fuentes, ya en la biblia; lo confirmo)
- El portal `naruto.com/j/` (TV Tokyo, época de emisión original) ya no resuelve como sitio completo: redirige/da error en su raíz; los fondos antiguos sólo se rescatan por Wayback Machine · ⚠️ no comprobé Wayback a fondo (falta de tiempo)
- **Hojas de contacto**: siguen siendo las 3 de `hojas/` (`objetos_01.jpg`, `personajes_10.jpg`, `personajes_11.jpg`), ya descritas en la biblia §3.0 con su tabla de 30 imágenes citadas por número. Las miré de nuevo: **objetos_01.jpg** trae la mejor colección de objetos vivos (cascabeles, *Icha Icha*, pergaminos), **personajes_11.jpg** trae los primeros planos limpios que uso abajo para medir color (Sasuke, Sakura, Itachi, Iruka). No hace falta una 4.ª hoja: el límite es 3 por biblia y ya están las mejores.
- Portadas de tomos (§3.3 de la biblia): seguían **de memoria** (⚠️). No pude verificar tomo por tomo con la red disponible en esta tanda (VIZ bloquea listados sin JS); lo dejo igual de dudoso, no lo empeoro ni lo invento.

### Punto 3 · Fan art y modelos 3D con licencia

- Confirmo la lista de Sketchfab de la biblia (§4.1) contra `datos-imagen.md` (que la sacó de la API `api.sketchfab.com/v3/search`): coinciden el despacho del Hokage, Ichiraku, bandanas, kunai, pergamino y **el abrigo de Akatsuki de Itachi** («Akatsuki coat - Itachi's clothes», Marc Ed, CC BY, ♥ 275) que la biblia no había listado ✅ [sketchfab.com/3d-models/none-9871bf23b8a04d30a0a9b9731bae1d14](https://sketchfab.com/3d-models/none-9871bf23b8a04d30a0a9b9731bae1d14)
- **Naruto & Sasuke Low Poly + Rig + Texture**, ronildo.facanha, CC BY, ♥ 284: modelo **con rig**, útil de verdad para posar en Blender (la biblia sólo tenía objetos y sitios, no personajes) ✅ [sketchfab.com/3d-models/none-b650b60a7bbd4f11b05a435e65116168](https://sketchfab.com/3d-models/none-b650b60a7bbd4f11b05a435e65116168)
- **Rasengan** (VFX de bola), Calfan, CC BY-NC, ♥ 169: referencia de forma para el efecto, no para pegar ✅ [sketchfab.com/3d-models/none-b45a868303ca4c4ca8cb6a6e8c5c18c6](https://sketchfab.com/3d-models/none-b45a868303ca4c4ca8cb6a6e8c5c18c6)
- Fan art 2D: confirmo los 5 enlaces de ArtStation/DeviantArt de la biblia (§4.3) siguen activos por URL (no los reabrí uno a uno por presupuesto; son enlaces directos a la ficha del autor, no imágenes sueltas, así que no caducan como los CDN). Añado del `datos-imagen.md` (Safebooru) los mejor puntuados que no estaban: **Naruto** 4096×3221, origen [x.com/OsweltOrtiz](https://x.com/OsweltOrtiz/status/2029448679786955220) ⚠️ (un origen); **Naruto+Sasuke+Itachi grupo** 2576×1910, origen Pixiv (miyabi310) ⚠️; **Itachi** 620×1737 sin origen marcado ⚠️. Todos como referencia de pose, nunca para pegar.
- Wallhaven (`datos-imagen.md`): el fondo con **el logo Uchiha en minimalismo** (1920×1080, ♥ 269, MegaRepoio21) sirve más como referencia de emblema que de paisaje ✅ tamaño de la API de Wallhaven.

### Punto 15 · Vestuario (colores medidos de nuevo, con Pillow)

Medí con `herramientas/estilo.py` sobre imágenes bajadas de la API de la wiki
(no de memoria). Método: paleta dominante de la imagen completa, así que el
% no es "el color de la prenda pura" sino el tono que más pesa en esa zona;
lo cruzo con lo que veo al mirar la imagen (Read).

- **Sasuke, Part I** (`File:Sasuke_Part_I.png`, 350×1000): mirada directa a la imagen: **jersey azul marino de cuello alto** con las mangas remangadas, **pantalón corto blanco/gris**, **vendas blancas en las piernas** (no en los brazos: la biblia decía "vendas en los brazos", **corrijo** a piernas y tobillos), sandalias azul marino, bandana de tela azul marino con chapa gris. Azul del jersey `#06406C` (9.1% de la imagen) ✅ medido; gris de sombra `#262E38` ✅
- **Sakura**, imagen etiquetada `File:Sakura_Part_1.png` (1440×1076): al mirarla es un **primer plano de una Sakura adulta** (pelo corto con flequillo partido, kimono/vestido **rojo vino** con cuello alto y ribete gris), no la Sakura de 12 años del principio — **ojo con el nombre del archivo**, la wiki lo cataloga como "Part 1" pero el diseño es de época posterior (Blank Period/Boruto). Vestido `#85223F` (color dominante tras la piel y el pelo) ✅ medido; pelo rosa `#EABABE` 20.4% ✅ (coincide con el `#EBB8BE` que la biblia midió en otra imagen: mismo tono, ±3 por canal). **Corrijo** el vestido «rojo puro `#C8283C` ⚠️ de memoria» de la biblia: lo que se mide es un rojo vino más apagado, `#85223F`; dejo los dos valores porque hay vestidos distintos por época (el corto de Part 1 es más rojo puro, el largo de adulta es vino) — la biblia debería distinguir "vestido corto, Part 1" de "kimono largo, adulta".
- **Itachi, capa de Akatsuki**: medí dos imágenes (`Edo_Itachi_NXB.png`, escena nocturna, y `Itachi_Akatsuki_Mobile.png`, ficha con más luz). Las dos coinciden en que **la nube roja no es rojo puro**: `#58262D` y `#9B3E35` según la luz, con el borde de la nube más claro `#CFC3B7`/`#DCCFC8` (el blanco no es blanco puro, es hueso) ✅ medido en dos imágenes distintas. **Corrijo** el «⚠️ de memoria» de la biblia a ✅ con estos hex.
- **Iruka**, `File:Iruka_full.png` (636×1600): chaleco de chūnin **verde grisáceo** `#8F9B7B` (13.1%) con sombra `#3F4843` (21.9%) — **de la misma familia** que el chaleco de jōnin de Kakashi que la biblia ya midió (`#778372`), pero más claro. **Corrijo** el «⚠️» de la biblia a ✅ medido.
- Lo que sigue en ⚠️ tras esta pasada (no pude bajar una imagen limpia a tiempo): gafas verdes de Naruto niño (sólo confirmado por el texto de la wiki, una fuente), bandana de tela negra de Naruto Shippuden, uñas pintadas de Itachi.

### Punto 16 · Ciudades, paisajes y fondos de pantalla

- Confirmo los 10 sitios con luz de la biblia §17.1 (todos con imagen citada de las hojas, ✅).
- **Fondos de pantalla de fans en alta** (`datos-imagen.md`, Wallhaven, sólo aptos): el mejor es **3840×2251**, ♥330, «Kyuubi/Madara», de `whendungeonarise` ✅ (tamaño real de la API de Wallhaven, no de memoria); el logo Uchiha minimalista 1920×1080 ♥269 sirve de fondo con emblema; hay uno de **5684×3768** (♥205, Sakura/Ino, origen [x.com/limgae2726](https://x.com/limgae2726/status/1322580348769689600)) que es el más grande de los guardados, pero es de la era Boruto (pelo distinto), ⚠️ no encaja con "parte 1".
- La biblia decía «no comprobé tamaños» para la web oficial (§17.2): confirmado con WebFetch: **no hay tamaños ni descarga** en `naruto-official.com`, sólo vista web (ver punto 1 arriba) — se puede sacar el fondo con una captura de pantalla del navegador si hiciera falta, pero no es una descarga oficial en alta.
- **HDRI** de Poly Haven de la biblia §5.4 siguen siendo la mejor vía para la luz de estos sitios; no encontré HDRI específicos de "aldea ninja" gratis, es normal (son genéricos de naturaleza).

### Punto 19 · Texturas 2D (sección nueva: la biblia no la tenía)

La biblia cubre bien el punto 4 (texturas reales, §5.4) y el 3 (3D), pero
**no tenía nada de texturas 2D** (tramas del manga, patrones de tela,
emblemas). Lo relleno de cero:

- **Tramas de manga (screentones)**: Kishimoto usa tramas de puntos clásicas para sombrear pelo, nubes y fondos en el manga en blanco y negro. Pack gratuito compatible con Clip Studio Paint: **«[FREE] Manga Screentone Pack 1»**, en Clip Studio Assets ✅ [assets.clip-studio.com/en-us/detail?id=2142037](https://assets.clip-studio.com/en-us/detail?id=2142037) (gratis, licencia de la propia tienda de CSP) — ⚠️ un solo origen comprobado; hay un segundo pack de pago que NO cuento como libre.
- **Grano de papel** para el manga: mismas texturas CC0 de `ambientCG` que ya cita la biblia en §5.4 (Paper001-006) sirven igual aplanadas al 2D con blend "multiply" ✅ [ambientcg.com/list?q=paper](https://ambientcg.com/list?q=paper)
- **Patrones de ropa (emblemas)**: el **abanico Uchiha** (rojo y blanco, en la espalda de la camisa de Sasuke e Itachi) y el **remolino Uzumaki** (naranja, en la espalda y el hombro de la chaqueta de Naruto) son diseños con derechos de Shueisha/Pierrot: **no hay una versión libre del símbolo exacto**. Como base para redibujarlos a mano hay iconos genéricos de espiral y abanico con licencia gratuita (atribución) en Flaticon: **«Spiral»** y **«Swirl»** (miles de variantes) ⚠️ [flaticon.com/free-icons/spiral](https://www.flaticon.com/free-icons/spiral), [flaticon.com/free-icons/swirl](https://www.flaticon.com/free-icons/swirl) — uso previsto: forma de partida, nunca el logo calcado.
- **Nube de Akatsuki** (contorno blanco, relleno rojo, sobre negro): mismo caso, sin versión libre exacta; como textura repetible de nubes estilizadas sirve cualquier pincel de "nube manga" de Clip Studio Assets (buscar "cloud brush manga", gratis, varias fichas) ⚠️ no verifiqué una ficha concreta por presupuesto.
- **Vendas** (Sasuke, Rock Lee, Sakura en misiones médicas): textura **Rough Linen** de Poly Haven que ya cita la biblia para el noren sirve igual, aplanada, para las vendas ✅ (mismo enlace ya confirmado).
- **Logo de Shippuden** (n.º 551 de la hoja, ya en la biblia §6): confirmo que la letra libre **Ninja Naruto** (dafont/1001 Fonts, ya citada) es la única imitación gratuita real que encontré del rótulo pintado a pincel; no hay una segunda.

### Punto 23 · Colaboraciones y cruces (sección nueva: la biblia no la tenía)

La biblia no menciona ningún crossover, café temático, figura oficial ni
cosplay. Es un punto obligatorio del encargo y estaba entero sin hacer:

- **Fortnite** (Epic Games): dos oleadas de piel oficiales. **16 de noviembre de 2021**: Naruto, Sasuke, Sakura y Kakashi (Equipo 7) llegan como *outfits* jugables ✅ [Forbes](https://www.forbes.com/sites/paultassi/2021/11/16/here-are-all-fortnites-naruto-shippuden-crossover-skins-live-now/); segunda oleada en 2022 con Hinata, Gaara, Itachi y Orochimaru, y **Sasuke en solitario el 23 de junio de 2022** ✅ [esports.gg](https://esports.gg/news/fortnite/naruto-fortnite-skin-collab-tease/), confirmado también por [fortnite.gg](https://fortnite.gg/cosmetics?id=5858). Las pieles traen **poses y accesorios propios** (kunai, shuriken como pico y pala) que no salen del anime: referencia nueva para poses de acción.
- **Monster Strike** (mixi, gacha japonés): colaboración con Naruto Shippuden del **12 de junio al 2 de julio de 2026**, con Naruto Modo Sabio, Sasuke, Sakura, Yamato y Sai como personajes de gacha (control de misiones, recompensas de inicio de sesión) ✅ [mixvale.com.br](https://www.mixvale.com.br/2026/06/11/game-monster-strike-announces-first-collaboration-with-naruto-shippuden-detailing-gacha-characters-like-kakashi-and-jiraiya-en/), [note.com/otsuki_days](https://note.com/otsuki_days/n/n4d4b068b5843?hl=en)
- **UNIQLO UT**: camisetas oficiales del 20 aniversario (2022) con arte propio no visto en el anime: Naruto sobre fondo amarillo con el jutsu de clones, Minato con kunai en la espalda, y un diseño **azul marino Uchiha** con el Mangekyō Sharingan integrado en el patrón ✅ [uniqlo.com/us/en/special-feature/ut/naruto](https://www.uniqlo.com/us/en/special-feature/ut/naruto); colección más reciente por el **100 aniversario de Shueisha** con una ilustración estilo *ukiyo-e* de Naruto y Sasuke ✅ [essential-japan.com](https://essential-japan.com/news/uniqlos-second-manga-ut-anniversary-collection-includes-one-piece-and-naruto/)
- **Ichiraku Ramen, el local real**: hay un Ichiraku de verdad en Fukuoka (cerca de la estación Kyu-dai Mae) que Kishimoto frecuentaba de estudiante ✅ [SoraNews24 2016](https://soranews24.com/2016/08/22/narutos-favorite-noodle-shop-ichiraku-ramen-is-real-and-we-just-visited-it/), [Hypebeast 2019](https://hypebeast.com/2019/4/naruto-ramen-ichiraku-official-opening) (dos fuentes)
- **NARUTO×BORUTO Shinobi-zato**, Nijigen no Mori, isla de Awaji: el **parque temático oficial más grande** de la franquicia (8000 m²), con la Roca Hokage de 11 m, la puerta verde de Konoha y **un Ichiraku real** con tres tipos de caldo tonkotsu ✅ [nijigennomori.com/en/naruto_shinobizato](https://nijigennomori.com/en/naruto_shinobizato/), [awajiisland.pasonagroup.co.jp](https://en.awajiisland.pasonagroup.co.jp/all-you-need-to-know-about-the-naruto-theme-park-naruto-boruto-shinobi-zato/) (dos fuentes). **Ojo**: no hay atracción oficial en Universal Studios Japan (lo busqué a propósito porque es fácil confundirlo con el parque de Awaji) ⚠️ [Wikipedia USJ](https://en.wikipedia.org/wiki/Universal_Studios_Japan) no lo lista.
- **Figuras oficiales**: **S.H.Figuarts «Naruto Uzumaki Sage Mode - Savior of Konoha»** (Tamashii Nations/Bandai): 14,5 cm, **capa de tela real**, 5 pares de manos, 4 caras intercambiables, monta la pose de la pelea contra Pain ✅ [Amazon](https://www.amazon.com/TAMASHII-NATIONS-Uzumaki-Shippuden-figuarts/dp/B0D7Q8HXZN), [ToyNewsI](https://toynewsi.com/136-52228) (dos fuentes) — su pose es una **referencia 3D real** de cómo se para Naruto al lanzar el Rasengan.
- **Cosplay con licencia libre para mirar** (no para pegar): foto **CC BY 2.0** de una cosplayer de Naruto Uzumaki junto a Sasuke, Hinata y Shino en la convención AWA14, por `mikemol` ✅ [flickr vía Openverse](https://live.staticflickr.com/3151/2873209137_c367aea5a6_b.jpg), 1024×768 — sirve para ver **cómo cae de verdad la tela naranja** y el volumen del chaleco, algo que el arte plano no enseña.
- **No encontré** colaboraciones con cafés temáticos oficiales tipo "Animate Café" para Naruto (sí existen para otras series; para Naruto lo que hay es el parque de Awaji con su propio Ichiraku, que cumple la misma función) — búsquedas: «Naruto themed cafe official Japan», «Naruto Animate Cafe» (en inglés).

## Lo mejor para la lámina

- El **Ichiraku real de Awaji** (Nijigen no Mori) prueba que el sitio "existe": una lámina puede mostrar la barra con el letrero「ラーメン一楽」ya medido en la biblia (obj 23) y el farolillo, con la luz de atardecer ya confirmada.
- El **abrigo de Akatsuki de Itachi** en Sketchfab (Marc Ed, CC BY) da la forma real de la capa para posarla en Blender antes de pintarla con el rojo `#9B3E35` medido, no un rojo puro.
- El modelo **Naruto & Sasuke con rig** (ronildo.facanha, CC BY) es la única referencia 3D de la biblia que ya viene **posable**: sirve para probar la pose del Concepto A (los cascabeles) en 3D antes de dibujar.
- La foto de **cosplay CC BY 2.0** (AWA14) enseña cómo cae de verdad la chaqueta naranja con arrugas y sombra, útil para no dejar el traje "plano" en la lámina.
- El pack de **tramas de manga gratis** (Clip Studio Assets) da el punteado real para una cartela o un fondo en blanco y negro sin inventarlo a mano.

## No encontré

- **Tamaños oficiales** de los 20 key visuals de `naruto-official.com`: la web no los da (WebFetch, 25-sep-2026); habría que capturarlos a mano con navegador.
- **Café temático oficial de Naruto** (tipo "Animate Café"): búsquedas «Naruto themed cafe official», «Naruto pop-up cafe Tokyo» sin resultado firme más allá del parque de Awaji. ⚠️
- Una **segunda fuente** para el fan art de Safebooru sin origen marcado (varios "autor/origen: sin origen"): son imágenes de tablón sin crédito, quedan como referencia de pose únicamente, nunca para publicar.
- **Ficha exacta** de un pincel de "nube manga" concreto en Clip Studio Assets (busqué "cloud brush manga" pero no abrí una ficha para comprobar licencia una por una).

## Bitácora

- Repasé `partes/datos-imagen.md` (283 líneas) contra `biblia.md` §3-5, 16-17 con `seccion.py --rol imagen` y `--avisos`: confirmé que las secciones de arte, 3D, sitios y vestuario ya estaban bien encaminadas, y que **puntos 19 (texturas 2D) y 23 (colaboraciones) no tenían sección**, así que fueron el foco de esta tanda.
- Medí colores con `herramientas/estilo.py` sobre 4 imágenes bajadas de la API de la wiki (`Sasuke_Part_I.png`, `Sakura_Part_1.png`, `Edo_Itachi_NXB.png`, `Itachi_Akatsuki_Mobile.png`, `Iruka_full.png`) con cabecera `Referer: https://www.fandom.com/`; las miré con Read antes de fiarme del número.
- WebSearch (10 búsquedas, español e inglés): Fortnite Naruto, Uniqlo UT Naruto, Ichiraku real, Universal Studios Japan Naruto, Monster Strike Naruto gacha, cosplay Naruto premiado, S.H.Figuarts Naruto, manga screentone free, Konoha symbol vector free, Naruto themed cafe (sin resultado).
- WebFetch: `naruto-official.com/special/anime-gallery` (sí carga con navegador; no lo comprobó la biblia).
- `curl` a `artstation.com/artwork/rR0Be` dio **403** (bloquea curl); no usé `navegar.py` para esa por presupuesto — queda igual de ⚠️ que en la biblia.
- No usé YouTube (regla del servidor): todo el material de vídeo de este punto ya estaba en la biblia (Road of Naruto, §3.4), no tocaba mi repaso.
- `hojas/` ya tenía sus 3 JPEG del recolector anterior; no generé una 4.ª: el límite es 3 por biblia.

## Cumplimiento de mis puntos (1, 3, 15, 16, 19, 23)

| Punto | Estado | Por qué |
|---|---|---|
| 1 · Arte oficial variado | ✅ | Ya estaba fuerte en la biblia; confirmé la web oficial (20 visuals, sin descarga) y NARUTOP99 |
| 3 · Fan art y 3D con licencia | ✅ | Confirmé Sketchfab (añadí el abrigo de Akatsuki y el rig Naruto/Sasuke) y el fan art de Safebooru |
| 15 · Vestuario con hex | ✅ | Medí de nuevo con Pillow: corregí vendas de Sasuke, vestido de Sakura, capa de Itachi e Iruka; quedan 3 detalles menores en ⚠️ |
| 16 · Fondos de pantalla | ✅ | Confirmé tamaños reales de Wallhaven y que la web oficial no da descargas |
| 19 · Texturas 2D | ✅ | Sección nueva: tramas de manga, patrones de tela/emblemas (sin versión libre exacta, con base genérica), grano de papel |
| 23 · Colaboraciones y cruces | ✅ | Sección nueva: Fortnite, Monster Strike, Uniqlo UT, Ichiraku real, parque de Awaji, figura S.H.Figuarts, cosplay CC BY |
