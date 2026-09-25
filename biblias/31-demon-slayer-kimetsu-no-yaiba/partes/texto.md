# Investigador de texto, juegos y técnica · Demon Slayer (Kimetsu no Yaiba) · repaso corto

Repaso corto: sólo los puntos **18** (estilo de dibujo y técnica, cómo
replicarlo), **24** (obras parecidas) y **25** (el mundo, la historia y sus
símbolos) de `ENCARGO.md`, nuevos en el encargo y ausentes de `biblia.md`
(comprobado con `seccion.py --indice`: no aparecen como sección propia; el
§18 actual de la biblia es «Guía para IA», que es el punto 17, no el 18).

Parto de `partes/datos-texto.md` (ya leído, no repito esas consultas: equipo
creativo de AniList, obras parecidas recomendadas, obras relacionadas,
capturas de los videojuegos de Steam). También leí `partes/imagen.md`
(puntos 19 y 23, ya hecho) para no repetir dominios ni datos.

La biblia ya cita ~35 webs distintas (bitácora §21.4) y hacen falta 40:
marco con **(dominio nuevo)** cada fuente que no esté ya en esa bitácora ni
en `imagen.md`/`imagen.json`.

## Hallazgos · Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

### 18.1 El manga: cómo dibuja Gotouge Koyoharu

- **Todo a mano, en analógico** (papel y pluma, no tableta): lo confirma el
  propio autor en una respuesta de fan citada en Yahoo! Chiebukuro (「アナロ
  グです」, «es analógico») · ⚠️ una fuente secundaria
  ([detail.chiebukuro.yahoo.co.jp](https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q13283800033) **(dominio nuevo)**),
  no encontré la entrevista original citada por nombre de revista.
- El propio autor ha dicho en entrevistas que su dibujo **no es su punto
  fuerte** y que se apoyó en la fuerza de la historia y el ritmo (nota de
  su editor de debut) · ⚠️ una fuente
  ([news.livedoor.com, entrevista al primer editor](https://news.livedoor.com/article/detail/17760339/) **(dominio nuevo)**).
- Su trazo en el manga es **deliberadamente simple y anguloso** frente al
  detalle grande de los fondos y las tramas de pantalla (screentones): se
  ve comparando cualquier página del manga (Kimetsu no Yaiba Wiki, ya
  citada en biblia.md) con el arte promocional de ufotable.

### 18.2 El anime: la técnica de ufotable, con nombres y software (✅ dos fuentes técnicas)

**Lo más importante para replicarlo**: el look de Demon Slayer **no es sólo
animación** (作画, *sakuga*). Es la suma deliberada de tres capas —dibujo,
撮影 (*satsuei*, cinematografía/compositing) y CG 3D— trabajadas por
departamentos separados dentro del mismo estudio (ufotable es de los pocos
que no subcontrata esas dos últimas). Lo dice el animador y crítico Kutsuna
Kenichi comparando la filosofía de ufotable con la de Studio Ghibli (Ghibli
apuesta todo al dibujo a mano; ufotable, a la integración de departamentos)
· ✅ [bunshun.jp](https://bunshun.jp/articles/-/42113) **(dominio nuevo)**
+ el propio patrón se repite en
[mantan-web.jp](https://mantan-web.jp/article/20201018dog00m200015000c.html) **(dominio nuevo)**
(«心技体»: cuerpo, técnica y espíritu de ufotable juntos).

- **Software confirmado, con nombres y cargos** (entrevista oficial de
  Autodesk a **Yuichi Terao**, director de fotografía/*satsuei*, y
  **Kazuki Nishiwaki**, director de 3D, del departamento Digital de
  ufotable) ✅ [area.autodesk.jp/case/animation/kimetsu-01](https://area.autodesk.jp/case/animation/kimetsu-01/)
  y [kimetsu-02](https://area.autodesk.jp/case/animation/kimetsu-02/) **(dominio nuevo)**:
  - **3ds Max** como base del 3D, con los plugins **V-Ray** (render),
    **PhoenixFD** (fluidos: el agua y el fuego de las respiraciones),
    **tyFlow** (partículas), **Forest Pack** (vegetación de fondos),
    **RailClone** (arquitectura repetida) y **HairFarm** (pelo).
  - **Pencil+** (el plugin de *cel shading*/contorno de línea para 3ds
    Max): es la pieza clave para el «look 2D» del 3D — el equivalente
    directo en Blender es **Freestyle** o el modificador **Line Art**
    (o, más simple, **Solidify** con normales invertidas y un material
    negro sin sombra), tal y como pide el propio encargo.
  - Reuniones en dos fases: primero guión gráfico con el director y el
    director de fotografía; **después** se decide qué va en CG. El CG de
    fondos es sólo **referencia** para que los animadores dibujen encima:
    «el CG se encarga de la arquitectura para que los animadores se
    concentren en las expresiones» (cita de Nishiwaki).
  - **Localizaciones reales**: el equipo hizo *location hunting* (ロケハン)
    **tres veces** para un mismo fondo, para captar cómo se agrupan los
    árboles y la vegetación baja — algo que «la imaginación no logra
    replicar del todo» (cita de Terao/Nishiwaki).
  - Un personaje puede mezclar técnicas dentro de la misma toma: el
    hermano Araña (arco de Natagumo) tiene **cuerpo en CG y cara dibujada
    a mano**, para abaratar sin perder la expresividad de la cara ✅
    (misma fuente Autodesk).
  - Diseñar una técnica visual nueva (p. ej. un tipo de respiración)
    lleva **1-2 meses de investigación** antes de meterla en producción
    (cita de Nishiwaki).

- **Rotoscopia**: los animadores rotoscopian referencia real de espadachín
  para que cada tajo de Tanjiro se sienta con el peso correcto · ✅
  ANN (entrevista oficial al productor **Yuma Takahashi**)
  [animenewsnetwork.com](https://www.animenewsnetwork.com/feature/2019-08-28/interview-demon-slayer-producer-yuma-takahashi/.149177)
  ya citado en biblia.md como fuente en inglés? — **no**, es dominio nuevo
  para esta biblia: **(dominio nuevo)**. Coincide con la etiqueta oficial
  de AniList «Rotoscoping 56%» (`datos-texto.md`).
- **Water Breathing** (la respiración del Agua): las olas del golpe están
  **casi todo dibujadas a mano**, con sólo un poco de 3DCG de apoyo — lo
  dice el propio productor Takahashi en esa entrevista ✅ (misma fuente
  ANN). Contradice la idea de fan de que «todo es CG»: es sobre todo
  dibujo, con el CG como pegamento.
- **撮影 (satsuei = compositing/cinematografía)**: ufotable trata esta capa
  como un director de fotografía de cine real, ajustando luz, niebla y
  profundidad de campo por toma — comparado por un usuario de Quora con el
  trabajo de un maquillador top ✅
  [jp.quora.com](https://jp.quora.com/%E3%82%A2%E3%83%8B%E3%83%A1-%E9%AC%BC%E6%BB%85%E3%81%AE%E5%88%83-%E3%81%AE%E5%88%B6%E4%BD%9C%E4%BC%9A%E7%A4%BE%E3%81%A7%E3%81%82%E3%82%8Bufotable%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6-%E6%92%AE%E5%BD%B1%E3%81%AE) **(dominio nuevo)**,
  y por el mismo Kutsuna Kenichi en Bunshun: la escena del cementerio del
  prólogo (T1-01) logra «sutiles fluctuaciones de luz» (光の強弱による複雑
  な揺らぎ) sólo por compositing, sin retocar la animación.
- **Combinación de framerate**: la acción base va a 12 fps (el estándar de
  sakuga japonés) pero el **temblor de cámara** (camera shake) se anima a
  24 fps por encima, dando una sensación de fluidez sin dibujar el doble
  ⚠️ una fuente (blog técnico, ver 18.3).

### 18.3 Encuadres y composición (para planificar la lámina como una toma)

De un análisis técnico plano a plano de las peleas de Demon Slayer (blog de
animación de jbsiraudin, con ejemplos de escenas y del animador **Nozomu
Abe**) ✅ [jbsiraudin.github.io/blog/demon-slayer-visual-grammar](https://jbsiraudin.github.io/blog/demon-slayer-visual-grammar/) **(dominio nuevo)**:

- **Encuadre centrado**: la acción se comprime hacia el centro del
  fotograma para que el ojo no tenga que moverse; es una elección de
  guión gráfico, no casualidad.
- **Ritmo en tres tiempos**: preparación **larga** → golpe de **un solo
  fotograma** → relajación **larga**. El golpe real dura un instante; lo
  que se «siente» es la pose de después.
- **Color por acción**: cada ataque tiene su color de flash — **azul**
  para la espada, **morado** para el enemigo, **dorado** para chispas —
  así el ojo entiende quién golpea sin necesidad de texto.
- **Fotograma de impacto en silueta**: Nozomu Abe marca el golpe con una
  silueta a máximo contraste (personaje recortado en negro sobre un flash
  de color) para que la violencia se sienta antes de entenderse del todo.
- **Aplicación a una lámina fija**: un personaje **de espaldas o en
  silueta parcial** contra un fondo de color plano (el hex de su
  respiración, §5.2 de biblia.md) funciona igual que un fotograma de
  impacto — sirve para una pose de portada o de «bienvenida» sin
  necesidad de mostrar movimiento.

### 18.4 Cómo reproducirlo en Photoshop y Blender (propuesta técnica, con la referencia real de arriba)

| Capa de Demon Slayer | Equivalente en Blender | Equivalente en Photoshop |
|---|---|---|
| **Pencil+ (contorno 3ds Max)** | **Line Art** (modificador, Grease Pencil) o **Freestyle**; alternativa barata: **Solidify** con normales invertidas y material negro sin *shading* | Pincel de tinta con *jitter* de grosor (Kyle T. Webster «Inker» o similar) sobre el *render* |
| **CG de fondos, sólo referencia** | modelar el sitio en bloques simples (Poly Haven CC0, §5.3 de biblia.md), **sin texturizar a fondo**: el animador (o aquí, el ilustrador de la lámina) dibuja encima | usar el render 3D como capa de **referencia al 30-40 % de opacidad**, debajo de las capas de dibujo |
| **PhoenixFD (fuego/agua de las respiraciones)** | el sistema de **fluidos Mantaflow** de Blender (humo/fuego) para una referencia de forma, repasada a mano encima | pintar el efecto a mano con un pincel de acuarela/humo sobre la silueta del render |
| **撮影 (compositing/luz)** | nodos de compositing de Blender: niebla (**Mist pass**), profundidad de campo, *glow* | ajustes de capa: **Color Dodge** para los brillos de la respiración, un desenfoque radial leve para el fondo, viñeta suave |
| **Cel shading plano + degradados en la sombra grande** | material Toon (**Shader to RGB** + rampa de color de 2-3 tonos) | *Multiply* con un degradado de 2 tonos, sin difuminar el borde de la sombra |
| **Rigs listos**, para posar sin animar desde cero | modelos **CC0** con *rig* de Tanjiro en Sketchfab: [«Tanjiro Constant Flux»](https://sketchfab.com/3d-models/tanjiro-constant-flux-50ba553d376e45e596eace02e9779c38) (traje de la Selección Final, texturas 2K-4K, *render* compuesto de Blender) y [«tanjiro kamado demon slayer»](https://sketchfab.com/3d-models/tanjiro-kamado-demon-slayer-dfebaddf7ec442cc8cf81f561fcb465b) (Hinokami Kagura, con el `.blend` original enlazado) — ambos CC0 según su ficha de Sketchfab ✅. Complementa los modelos de armas/sitios ya listados en `imagen.md` §4.1.

- **Filtros de imagen** (grano, aberración cromática): no encontré un
  artículo técnico que lo confirme con nombre y minuto ⚠️; por convención
  del anime de acción japonés (y visible a ojo en los tráileres ya vistos
  en biblia.md §12) hay grano ligero y un golpe de aberración cromática
  roja/azul en los impactos más fuertes — **verificar mirando un
  fotograma en Photoshop antes de replicarlo**, no darlo por hecho.

## Hallazgos · Punto 24 · Obras parecidas y temas relacionados

## Hallazgos · Punto 25 · El mundo, la historia y sus símbolos

## Lo mejor para la lámina

## No encontré

## Bitácora

### Dominios nuevos citados aquí (para llegar a 40)
