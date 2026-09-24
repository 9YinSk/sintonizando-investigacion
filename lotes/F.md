# Lote F: series nuevas 77-96

Sesión: https://claude.ai/code/session_01DDNVaCpYyiQfao1M598h9e · rama `claude/sweet-wozniak-vmvzo4`
(parte de `claude/peaceful-maxwell-fklpkp`, juntada con los lotes A, B, C, D y E).

## Estado

- Arranque (24-sep-2026, 21:45 UTC): herramientas instaladas; guardar.sh cada 300 s; comprobación cada hora.
- 77 Wistoria: **COMPLETA y subida** (22:27 UTC). ✅20 ⚠️18 ❌0, 134 referencias, 56 webs, 1655 líneas.
- 78 Vinland Saga: **COMPLETA y subida** (22:52 UTC). ✅23 ⚠️7 ❌0, 162 referencias, 65 webs, 2031 líneas.
- **Corte por límite de sesión** (23:06-23:50 UTC, `rate_limit`, «resets 11:20pm UTC»): 5 agentes vivos murieron a mitad de tanda (79 redactor, 80 video, 81 imagen/video/voz). Nada se perdió del todo: guardar.sh había subido lo hecho hasta el corte. Relanzo los 5 desde donde quedaron en cuanto pase el reinicio.
- 79 Demon Slayer: redactor cortado justo tras «Tres conceptos de lámina» — faltan tabla de cumplimiento, bitácora y referencias.json. Relanzado 23:50 UTC.
- 80 Solo Leveling: vídeo cortado con un `Sigue:` legítimo ya escrito (fotograma del Rey Hormiga). Relanzado como relanzamiento corto.
- 81 Mushoku Tensei: imagen cortado justo después de escribir imagen.md (dice «Parte terminada») pero SIN escribir imagen.json ni hojas/ — relanzado sólo para eso. Vídeo y voz no llegaron a escribir nada: relanzados desde cero.

## Avisos para el dueño

- 90 Kaguya-sama repite la serie de 43 (lote D) con otro enfoque («comedia y rótulos»). La dejo para el final del lote: si la 43 ya está, la 90 sólo profundiza en ese enfoque.
- 79, 80 y 89 son segundas miradas a Demon Slayer (31), Solo Leveling (03) y Frieren (33) con un enfoque propio (paisajes, sistema, memoria): se parte de esas biblias para no repetir.
- Ningún encargo del lote F trae wiki de Fandom: las encontré a mano (lista en este archivo, abajo).
- **78 Vinland Saga — canal:** el redactor propone #proyectos para su lámina, pero #proyectos ya lo pidió Arcane (17-arcane). Decide tú: ¿Arcane se queda sólo con #arte y Vinland Saga usa #proyectos, o al revés? Reserva sugerida si prefieres otro: lámina 2 de #textos (ya es de Death Note, 18).
- **78 Vinland Saga:** ningún vídeo se vio en 1080p (YouTube dio 403 todo el rato); las escenas icónicas sólo se vieron en storyboard de baja resolución. El doblaje latino transcrito es sólo el de Netflix (Eduardo Garza); el de Crunchyroll (Alejandro Eguiza) quedó sin transcribir. No usar el doblaje con IA de Prime Video si aparece por ahí.
- **Aviso a `recolectar.py`** (bug real, puede afectar a otras series con nombre ambiguo): en 79-demon-slayer-paisajes-y-auras, el AniList y los juegos de Steam que trajo `--hojas` correspondían a otra obra («Onigiri», AniList id 21612), no a Kimetsu no Yaiba. El investigador de texto lo detectó, lo anotó y repitió las consultas a mano con el id correcto (101922). No toqué el script; lo dejo anotado por si el dueño quiere que alguien lo arregle.

## Wikis de Fandom del lote

- 77-wistoria-wand-and-sword: `wistoria`
- 78-vinland-saga: `vinlandsaga`
- 79-demon-slayer-paisajes-y-auras: `kimetsu-no-yaiba`
- 80-solo-leveling-el-sistema-y-las-sombras: `solo-leveling`
- 81-mushoku-tensei: `mushokutensei`
- 82-the-rising-of-the-shield-hero: `shield-hero`
- 83-overlord: `overlordmaruyama`
- 84-no-game-no-life: `no-game-no-life`
- 85-sword-art-online-todas: `swordartonline`
- 86-saga-of-tanya-the-evil: `youjo-senki`
- 87-tsukimichi-moonlit-fantasy: `tsukimichi`
- 88-konosuba: `konosuba`
- 89-frieren-paisajes-y-memoria: `frieren`
- 90-kaguya-sama-love-is-war: `kaguyasama-wa-kokurasetai`
- 91-the-apothecary-diaries-el-diario-de-la-b: `kusuriya`
- 92-a-silent-voice-la-chica-sorda: `koenokatachi`
- 93-charlotte: `charlotte`
- 94-a-lull-in-the-sea-nagi-asu: `nagiasu`
- 95-blue-period: `blue-period`
- 96-bubble-netflix: `bubble`

## Costos

| Serie | Rol | Modelo | Minutos | Tokens |
|---|---|---|---|---|
| 77-wistoria-wand-and-sword | video | sonnet | 13 | 177307 |
| 77-wistoria-wand-and-sword | texto | sonnet | 13 | 255268 |
| 77-wistoria-wand-and-sword | imagen | sonnet | 16 | 217946 |
| 77-wistoria-wand-and-sword | voz | sonnet | 16 | 235722 |
| 78-vinland-saga | imagen | sonnet | 12 | 185385 |
| 78-vinland-saga | texto | sonnet | 15 | 222527 |
| 78-vinland-saga | voz | sonnet | 16 | 208945 |
| 78-vinland-saga | video | sonnet | 19 | 222410 |
| 77-wistoria-wand-and-sword | redactor (opus) | opus | 19 | 339142 |
| 78-vinland-saga | video (relanzo) | sonnet | 7 | 116043 |
| 79-demon-slayer-paisajes-y-auras | texto | sonnet | 13 | 242801 |
| 79-demon-slayer-paisajes-y-auras | imagen | sonnet | 14 | 224994 |
| 79-demon-slayer-paisajes-y-auras | video | sonnet | 16 | 187904 |
| 79-demon-slayer-paisajes-y-auras | voz | sonnet | 17 | 245351 |
| 78-vinland-saga | redactor (opus) | opus | 21 | 343246 |
| 80-solo-leveling-el-sistema-y-las-sombras | voz | sonnet | 13 | 217899 |
| 80-solo-leveling-el-sistema-y-las-sombras | texto | sonnet | 14 | 223273 |
| 80-solo-leveling-el-sistema-y-las-sombras | imagen | sonnet | 16 | 261111 |
| 81-mushoku-tensei | imagen (2 tandas: corte+arreglo) | sonnet | 12 | 156421 |
