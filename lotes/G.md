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
