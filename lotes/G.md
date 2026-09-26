# Lote G: series nuevas 97-116 (películas y occidentales)

Sesión: https://claude.ai/code/session_01PTvoV2YeakXpTVE1Sw4BfV · rama `claude/optimistic-turing-0es5zg`
Cuenta: cuenta R49
(sigue desde `claude/lote-g-serie-equipo-pweujx`, sesión session_01ReeeTfs7kQFygB2ZgfnNSB, cuenta .103, que dejó
97 y 98 con sus 4 partes listas.)

## Estado

- Arranque (25-sep-2026, 03:40 UTC): primera cuenta del lote. Herramientas instaladas; guardado cada 300 s; datos de 97-102 recolectados (98-101 con la wiki `ghibli`/`kiminonawa`).
- 97 Bocchi the Rock: imagen, voz y texto listos; texto en 2.ª tanda (composición por emoción); video en marcha.
- 98 El viaje de Chihiro: imagen, voz y texto (Sonnet) en marcha desde 04:00-04:10.
- Cambio de cuenta (25-sep, sesión optimistic-turing): herramientas instaladas; guardar.sh cada 300 s.
  `herramientas/juntar.sh` trajo el resto de ramas (99-101 con datos recolectados). 97 y 98: las 4 partes
  de cada uno están completas sin `Sigue:` obligatorio (98/video sólo tiene un opcional).
  Lanzados a la vez (5 agentes vivos): redactor (Opus) de 97; 4 investigadores (Sonnet) de 99 (El Castillo
  Ambulante). 98 queda en cola para redactor en cuanto se libere un hueco. Recolectando de fondo (gratis)
  los datos de 102 y 103 para no quedarnos sin cola.
- 97 Bocchi the Rock: **COMPLETA y subida** (07:2x UTC). `revisar.py`: ✅26 ⚠️11 ❌0, 1422 líneas, 185
  referencias (66 webs distintas, 168 minutos, 50 hex medidos).
- 99 El Castillo Ambulante: las 4 partes listas, sin `Sigue:` obligatorio (766 líneas voz, 377 video, 49 refs
  imagen, 17 refs texto). Redactor en cola: entra en cuanto se libere el hueco del redactor de 98.
  Corrigió un error del recolector automático: `datos-voz.md` traía el reparto de OTRA película
  («El castillo maldito», Scared Stiff 1953) por un fallo de búsqueda en Doblaje Wiki; el investigador de
  voz lo rehizo desde la ficha real (dos doblajes latinos completos: ZIMA 2005 y Wild Bunch-Netflix 2020).
- 98 El viaje de Chihiro: redactor (Opus) lanzado en cuanto se liberó el hueco del redactor de 97, en marcha.
- 100 La princesa Mononoke: 4 investigadores (Sonnet) lanzados a la vez con el redactor de 98 (5 agentes vivos).
- Reintento fallido: recolecté de nuevo 102 (El estilo Ghibli en general) sin `--nombres`/`--wiki` y pisé
  datos mejores (AniList/Fandom no la encontraron sin esas pistas); revertido con `git checkout` antes de
  subir nada. Para 102, recolectar con `--nombres` y `--wiki` explícitos cuando le toque.
- Límite de uso (25-sep, ~07:40 UTC): los 5 agentes vivos (redactor de 98 + 4 investigadores de 100)
  cortados por «session limit» de la cuenta, reset a las 11:30 UTC. 98 quedó guardado a medias (puntos
  0-23 de 25 escritos); 100 no llegó a guardar nada. Reanudado a las 12:59 UTC (aviso del dueño «Try
  again»): redactor de 98 relanzado para seguir desde donde quedó (no desde cero) y los 4 investigadores
  de 100 relanzados desde cero.
- 98 El viaje de Chihiro: **COMPLETA y subida**. `revisar.py`: ✅23 ⚠️16 ❌0, 1047 líneas, 230 referencias
  (56 webs distintas, 137 minutos, 114 hex medidos). El redactor siguió desde el punto 24 sin reescribir
  lo anterior. Redactor de 99 lanzado en cuanto se liberó el hueco.
- 100 La princesa Mononoke: las 4 partes listas, sin `Sigue:` obligatorio. Corrigió otro error del
  recolector automático: `datos-voz.md` traía el reparto de la SERIE de 2007 «Mononoke», no de la
  película (tres doblajes latinos reales: Buena Vista/Miramax 2001, Zima 2010, Wild Bunch-Netflix 2020).
  Redactor en cola para cuando se libere un hueco.
- 101 Your Name: 4 investigadores (Sonnet) lanzados a la vez con el redactor de 99 (5 agentes vivos);
  avisado el de voz para revisar con cuidado el reparto del recolector (van dos series con el error).
- Segundo límite de uso (~13:20 UTC, reset 17:50): se cortaron los 5. El dueño pidió no relanzar.
- 99 El Castillo Ambulante: el redactor llegó a cerrar la biblia antes del corte. `revisar.py`: **COMPLETA**
  (✅27 ⚠️12 ❌0, 993 líneas, 62 webs, 251 minutos, 98 hex). Subida.
- 100 La princesa Mononoke: **COMPLETA y subida** (23:50 UTC). `revisar.py`: ✅30 ⚠️10 ❌0, 1080 líneas, 177 referencias (87 webs distintas, 226 minutos, 90 hex medidos).
- 104 Steven Universe: **COMPLETA y subida** (20:30 UTC). `revisar.py`: ✅23 ⚠️7 ❌0, 1318 líneas, 125 referencias, 53 webs.
- 101 Your Name: cielos y ciudades: **COMPLETA y subida** (00:23 UTC), ✅22 ⚠️8 ❌0, 82 referencias, 43 webs.
- 103 Hazbin Hotel y Helluva Boss: **COMPLETA y subida** (01:47 UTC), ✅20 ⚠️10 ❌0, 74 referencias, 46 webs.
- 102 El estilo Ghibli en general: **COMPLETA y subida** (01:49 UTC), ✅24 ⚠️15 ❌0, 158 referencias, 75 webs.

### Para quien siga (paso a la compu del dueño con MWAPI, 25-sep 19:20 UTC)

El dueño compró saldo en MWAPI; el lote G sigue desde su compu (`LOCAL.md`), rama `claude/lote-g-local`.
La nube (sesión optimistic-turing) queda parada, sin agentes ni guardado automático.
- 97, 98, 99: COMPLETAS y subidas.
- 100 La princesa Mononoke: las 4 partes listas, sin `Sigue:` obligatorio → **lanzar su redactor**.
- 101 Your Name: cortado. Sólo quedó `partes/voz.md` a medias (204 líneas): relanzar voz para que siga
  desde ahí, e imagen, video y texto desde cero.
- 102 El estilo Ghibli en general: datos de la cuenta anterior (no volver a recolectar sin `--nombres` y
  `--wiki`). 103 Hazbin Hotel y Helluva Boss: datos recolectados.
- Ojo con `datos-voz.md`: en 99 y 100 el recolector trajo el reparto de otra obra con nombre parecido.

### Comprobación de modelos (compu del dueño, MWAPI, 25-sep 2026)

`GET /v1/models` devuelve 7 modelos: `claude-haiku-4-5-20251001`, `claude-opus-4-6`,
`claude-opus-4-7`, `claude-opus-4-8`, `claude-opus-5`, `claude-sonnet-4-6`, `claude-sonnet-5`.
Los 4 con «opus» en el nombre respondieron a la petición mínima y cada uno ecoó su propio
nombre en el campo `model`. Como advierte LOCAL.md, esto es sólo comprobación de nombres
(el revendedor pone lo que quiera), no garantía real. Elegí `claude-opus-5` (el de nombre más
alto) y lo dejé en `~/.config/mwapi/modelo-opus` para que el dueño lo ponga en
`ANTHROPIC_DEFAULT_OPUS_MODEL` y reabra `claude --continue`. La prueba real sigue siendo
`revisar.py` dando COMPLETA.

## Avisos para el dueño

- 97 Bocchi the Rock: 4 datos en que las partes no coinciden (primera guitarra de Bocchi: Les Paul o
  «Fender»; su grupo sanguíneo: B u O; en qué ending sale el «dedo» de Kita; color del uniforme de Kita).
  El redactor no pudo resolverlos con las fuentes que tenía.
- 97: las frases del doblaje latino sólo están en Crunchyroll (sin minuto posible sin oírlas en persona),
  igual que el minuto exacto del *stage dive* del episodio 12.
- 97: la descripción de #presentaciones está cortada en `servidor/inventario.md`; falta saber cómo termina.
- 99 El Castillo Ambulante: no existe videojuego oficial de la franquicia (confirmado en inglés y japonés,
  descartando un dato falso de Namco/PS2 que aparecía en búsquedas); TV Tropes y TCRF bloqueados por
  Cloudflare, no se pudieron leer; sin fuente fiable de la tipografía del logo internacional en inglés.
- 98 El viaje de Chihiro: la descripción de #presentaciones sigue cortada en `servidor/inventario.md`
  («nadie comenta…»); falta confirmar cómo termina antes de rotular la lámina.
- 100 La princesa Mononoke: Tres doblajes latinos (Buena Vista 2001, Zima 2010, Wild Bunch/Netflix 2020); hay que decidir cuál se usa. Las frases de los conceptos son del de Netflix. «¡Odio a los humanos!» sin comprobar en doblaje latino; mejor usar «¡Silencio! Yo no recibo órdenes de humanos» (Netflix). Color de ojos de San sin resolver (wiki azul real, Danbooru castaños). YouTube pidió sesión (sin ver tráiler japonés 1997 ni análisis en español). Sketchfab CC BY exige crédito. recolectar.py falló dos veces aquí (bajó reparto de 2007 de Mononoke y fan art de otras películas Ghibli): revisar en demás series Ghibli.
- 104 Steven Universe: Etiqueta «Diseno» sin ñ en #🎨・arte (¿a propósito o errata?). Texto de #🎯・reto-de-la-semana cortado en servidor/inventario.md. Revisar KYF 1:10 (sombrero y colores de Sardonyx, sin medir) y END 0:02 (mano de la estatua) antes de modelar. Crystal Universe (logo) no trae á í ó ú ñ ¿ ¡ (corrige a la 64). Licencia de Gem Glyph Font (Ayelis, itch.io) poco clara; modelos 3D CC BY-NC no comerciales; CC BY para atrezo: Big Donut, Garnet, Amatista. Faltan vistas de fandubs y minutos en 1080p (YouTube).
- 101 Your Name: Oír las frases del doblaje latino del clímax y de la pregunta por el nombre en HBO Max, Netflix o Prime (no hay clip latino accesible). El hilo fijado de #fotos ya lleva un adjunto (fotos.png): si ya tiene lámina, los conceptos 1 y 2 sirven de lámina 2. Ver el fandub latino de Steve Dub (dailymotion x6gfqxf) para anotar qué escenas dobla. Fan art de Safebooru casi sin mirar: nº13 (Takao Akizuki) y nº19, 22, 23 (Z-Kai) de personajes_01 sin comprobar, no usar. Sin buscar figuras oficiales (MyFigureCollection) ni Poly Haven (huecos de 23 y 3). Si se vuelve a correr juntar_referencias.py vuelve el fan art de otras obras de datos.json (Miku, Cirno, Kancolle): no dejes que entre. La hermana 52 sigue sin biblia: cuando se haga, que parta de ésta.
- 103 Hazbin Hotel y Helluva Boss: Comandos del bot de radio no están en inventario (lámina 2 de RADIO EN VIVO). Serie adulta: guía para IA excluye a Angel Dust y Valentino, pide frases sin insultos. Verificar palabras ⚠️ de muestras de Doblaje Wiki (Angel Dust, Niffty, Vox, Valentino, Lucifer, Blitzø, Millie). Comprobar si Angel Dust sale a 1:59 del tráiler T1. ¿Angel Dust con 4 o 6 brazos? Recolores mal asignados: #27304B (pelo de Vaggie), #F9D18E (piel de Blitzo). Fotogramas a 720p (YouTube bloqueado). Modelos Sketchfab CC BY piden crédito; Husk es CC BY-NC.
- 102 El estilo Ghibli en general: Inventario escribe «Diseno» sin eñe en #🎨・arte: confirmar antes de rotular. Nombres del doblaje latino sólo en Doblaje Wiki (salvo Chihiro): falta segunda fuente. Oír «¡Mei, mira eso!» (dailymotion x4mls0h 0:16) y la de Haku con música encima (x4bncvf 0:33). Mirar a tamaño real el gesto de Naoko (hoja arte_01 n.º 12 y fotograma kazetachinu028) antes de posar el concepto A. No hay frase de Kiki en doblaje latino con fuente: concepto B no le pone ninguna. Miyazaki llama a la animación con IA «un insulto a la vida misma».

## Costos

| Serie | Rol | Modelo | Minutos | Tokens |
|---|---|---|---|---|
| 97 | imagen | Sonnet | 13 | 226 mil |
| 97 | texto (2 tandas) | Sonnet | 20 | 248 mil |
| 97 | voz | Sonnet | 17 | 237 mil |
| 97 | video | Sonnet | 19 | 237 mil |
| 97 | redactor | Opus | 16 | 328 mil |
| 98 | voz | Sonnet | 13 | 189 mil |
| 98 | imagen | Sonnet | 18 | 253 mil |
| 99 | texto | Sonnet | 15 | 254 mil |
| 99 | imagen | Sonnet | 15 | 226 mil |
| 99 | video | Sonnet | 20 | 203 mil |
| 99 | voz | Sonnet | 21 | 238 mil |
| 98 | redactor (2 tandas: rate limit) | Opus | 10 | 219 mil |
| 100 | imagen | Sonnet | 13 | 221 mil |
| 100 | video | Sonnet | 14 | 216 mil |
| 100 | texto | Sonnet | 16 | 237 mil |
| 100 | voz | Sonnet | 20 | 289 mil |
| 99 | redactor (cortado al cerrar) | Opus | ? | ? (sin aviso de fin) |
| 100 | redactor | Opus | 18 | 256 mil |
| 101 | 4 investigadores (cortados) | Sonnet | ? | ? (sin aviso de fin) |
| 104 | equipo completo | Sonnet + Opus | — | — |
| 101 | equipo completo | Sonnet + Opus | — | — |
| 103 | equipo completo | Sonnet + Opus | — | — |
| 102 | redactor (seguir) | Opus | 16 | 282.7 mil |
