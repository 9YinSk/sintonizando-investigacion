# Parte de VÍDEO · Sakamoto Days (puntos 2, 4, 9, 10, 14)

Investigador de vídeo. Datos, no prosa. Fuentes de `datos-video.md` comprobadas y ampliadas con `fotogramas.py` / `episodio.py`.

## 2 · Fotogramas de escenas icónicas

Tráiler oficial (Sekai, doblado/subtitulado en francés, mismo montaje que el tráiler japonés de Netflix) analizado fotograma a fotograma, cada 15 s:
- 0:00 pantalla negra, texto «Autrefois, les méchants le redoutaient» (narración de apertura) · https://www.dailymotion.com/video/x9c6rxi · ✅ (AniList lista este tráiler como oficial + Dailymotion) · min 0:00
- 0:15 Sakamoto de civil, gordo, en el sofá con su hija Hana encima («Sakamoto a pris du poids») — el gancho cómico del contraste «ex-asesino/papá de familia» · https://www.dailymotion.com/video/x9c6rxi · ✅ · min 0:15
- 0:30 cartel amarillo «Ne pas tuer» (No matar), la regla que se impuso Sakamoto · https://www.dailymotion.com/video/x9c6rxi · ✅ · min 0:30
- 0:45 primer plano del cartel de búsqueda con la foto y recompensa por Sakamoto («la récompense pour le vieux gros…») · https://www.dailymotion.com/video/x9c6rxi · ✅ · min 0:45
- 1:00 Shin (rubio) en un pasillo, «Passons aux choses sérieuses» · https://www.dailymotion.com/video/x9c6rxi · ✅ · min 1:00
- 1:15 plano doble de Sakamoto y Shin, «Salut, Sakamoto» (logo Netflix en la esquina) · https://www.dailymotion.com/video/x9c6rxi · ✅ · min 1:15

Opening 1 (serie completa, sin diálogo, Internet Archive) analizado cada 10 s:
- 0:20 tarjeta de título «SAKAMOTO DAYS / サカモトデイズ» sobre silueta de ciudad en verde apagado · https://archive.org/details/sakamoto-days-op-1 · ✅ (item de Internet Archive con 83 descargas + coincide con el OP1 emitido) · min 0:20
- 1:10 primer plano de Lu (rubia) con el brazo extendido sujetando un arma, créditos de animación superpuestos · https://archive.org/details/sakamoto-days-op-1 · ✅ · min 1:10
- 1:20 silueta de Sakamoto de espaldas sobre fondo rojo sangre, cierre del OP · https://archive.org/details/sakamoto-days-op-1 · ✅ · min 1:20

## 4 · Fondos y sitios: luz y paleta medida en fotogramas

Colores medidos con Python/Pillow (promedio por tercio superior/medio/inferior) sobre fotogramas del OP1 (Internet Archive, ver arriba). Aproximados, calibrar contra el arte oficial del punto 1.
- Calle de ciudad al atardecer, gente cruzando (min 0:30 del OP1): cielo `#60829a`, edificios medios `#435872`, sombra de calle `#1e2c44` — luz fría, azulada, contraluz de atardecer · ✅ (medido directo del fotograma, fuente única de vídeo) · min 0:30
- Puente de tren/vías elevadas sobre la ciudad (min 0:40): tono lila-rosado `#b1acd4` arriba, `#7a6692` medio, `#7b5e84` abajo — hora dorada/violeta, típica de los cortes de transición del OP · ⚠️ (una fuente) · min 0:40
- Parque junto al río, césped y ciclista (min 0:50): cielo celeste claro `#c0ebfd`, vegetación `#81b4a8`, césped `#9cda54` — luz de día limpia, alto contraste verde/azul, el único paisaje "de paz" del opening · ⚠️ (una fuente) · min 0:50
- Escena nocturna de lluvia con velas/faroles en el suelo (min 1:00): negro casi puro `#0e111a` arriba, `#221917` medio, ocre `#64533a` abajo (luz de las velas) — plano de tono serio/acción, contrasta con el resto del OP, luz cálida puntual sobre negro · ⚠️ (una fuente) · min 1:00
- Interior doméstico del piso 2 (sofá, min 0:15 del tráiler): paleta cálida, beige/madera, luz de casa normal — refuerza que Sakamoto vive una vida familiar corriente · ⚠️ · min 0:15

## 9 · Música y sonido

- Banda sonora: **SAKAMOTO DAYS Original Sound Track**, compositor **Yuki Hayashi** (林ゆうき) — dos volúmenes "Anime original Mix" (2025-03-22) y dos "Hayashi special Mix" (2025-09-15, con la segunda temporada) · https://musicbrainz.org/release-group/48a2b48a-6ecb-4c01-8ad4-9a670d7ab012 · https://musicbrainz.org/release-group/1dd61c88-037a-44bc-9722-16fddd2e0d4e · ✅ (MusicBrainz, cuatro release-groups distintos del mismo compositor) · —
- Opening 1 (el analizado arriba): estructura visual acción+comedia, arranca con paisajes urbanos fríos y cierra con silueta roja de Sakamoto; ambiente de thriller de acción con un toque pop en los créditos tipográficos · https://archive.org/details/sakamoto-days-op-1 · ✅ · 0:00-1:29
- El ítem de Internet Archive **"Sakamoto Days Part 2 OP 1"** confirma que la 2ª parte/temporada tiene opening propio (no sólo remontaje) · https://archive.org/details/sakamoto-days-part-2-op-1 · ⚠️ (un solo repositorio, falta cotejar con AnimeThemes que dio error 522 al recolectar) · —
- AnimeThemes (openings/endings en calidad máxima, con offset preciso) falló al recolectar (HTTP 522); pendiente de reintentar a mano, ver «No encontré» · animethemes.moe · — · —

## 10 · Vídeos: tráilers, escenas, análisis y tendencias

- Tráiler oficial occidental (voz: **Sekai**, canal de doblaje/subtítulos francés), 1:29, 73,2 millones de vistas en Dailymotion — la copia más vista con diferencia, es el tráiler de referencia · https://www.dailymotion.com/video/x9c6rxi · ✅ (AniList enlaza el vídeo original en YouTube con el mismo minutaje; réplica exacta en Dailymotion) · 1:29
- Segundo tráiler, 1:26, subido por Vidaextra (medio español de videojuegos/anime) · https://www.dailymotion.com/video/x9b782c · ⚠️ (una fuente) · 1:26
- Tráiler de Netflix específico, 1:13, subido por Espinof · https://www.dailymotion.com/video/x93pj28 · ⚠️ · 1:13
- Teaser tráiler, 1:21, subido por meristation (medio español de videojuegos) · https://www.dailymotion.com/video/x8z7qrk · ⚠️ · 1:21
- Vídeo de análisis/opinión: **"Sakamoto Days is Anything But a Failure and Haters Were Silenced"**, defiende la serie frente a críticas, 160 descargas en Internet Archive (copia de YouTube) · https://archive.org/details/youtube-jrwHXQTXPg8 · ⚠️ · —
- Vídeo de opinión sobre la 2ª temporada: **"Sakamoto days season 2 and my thoughts on it"** · https://archive.org/details/sakamoto-days-season-2-and-my-thoughts-on-it · ⚠️ · —
- Cover musical/fan edit con Sakamoto Taro como protagonista, en portugués: **"Sakamoto Taro — Aposentado e Perigoso (Sakamoto Days)"** por LexClash — ejemplo de tendencia de fandom hispanohablante/lusófono con memes del personaje jubilado-peligroso · https://archive.org/details/videoplayback_20250207_0833 · ⚠️ · —
- Página/redes oficiales japonesas para seguir tendencias en vivo: Twitter oficial `@SAKAMOTODAYS_PR` y sitio `sakamotodays.jp` · https://twitter.com/SAKAMOTODAYS_PR · https://sakamotodays.jp/ · ✅ (ambos enlazados desde la ficha oficial de AniList) · —
- Sakamoto Days está disponible en Netflix (streaming global, con lo que TikTok/YouTube Shorts recortan clips del doblaje de cada región) · https://www.netflix.com/title/81663325 · ✅ · —

## 14 · Poses analizadas en varias escenas

| Pose | Episodio | Minuto | Sirve para |
|---|---|---|---|
| Sakamoto tumbado en el sofá, gordo, con su hija Hana encima, cara de padre cansado | Tráiler oficial | 0:15 | Presentar (contraste cómico "ex-asesino a sueldo/papá normal") |
| Sakamoto de perfil, mirando el cartel de búsqueda con su propia foto y recompensa | Tráiler oficial | 0:45 | Explicar (contexto: fue el asesino más temido, ahora tiene precio a su cabeza) |
| Shin de pie en un pasillo, mirada seria, manos sueltas a los lados | Tráiler oficial | 1:00 | Animar / dar paso a la acción («passons aux choses sérieuses») |
| Sakamoto y Shin uno junto al otro, plano medio, gesto de saludo entre iguales | Tráiler oficial | 1:15 | Presentar dúo protagonista |
| Silueta de Sakamoto de espaldas, cuerpo entero recto sobre fondo rojo | Opening 1 | 1:20 | Celebrar / cierre de impacto (plano icónico de cierre del OP) |
| Lu con el brazo extendido sujetando un arma en primer plano, mirada fija al frente | Opening 1 | 1:10 | Regañar / amenazar (pose de combate, la única con arma visible en el OP analizado) |

Faltan 4-6 poses más por personaje con fotograma propio (Shin en acción, Sakamoto en combate real) — ver «Sigue».

## Lo mejor para la lámina

- Silueta roja de Sakamoto de espaldas (OP1, min 1:20): plano limpio, de impacto, funcionaría como icono/portada de canal · https://archive.org/details/sakamoto-days-op-1
- Contraste "papá gordo en el sofá" vs "cartel de búsqueda con recompensa" (tráiler, min 0:15 y 0:45): resume el gancho de la serie en dos fotogramas · https://www.dailymotion.com/video/x9c6rxi
- Paleta de la calle al atardecer del OP (`#60829a` / `#435872` / `#1e2c44`): fría, azulada, sirve para fondos de canales de "producción/técnica" · medido en fotograma propio
- Paleta de la escena de lluvia nocturna (`#0e111a` con acentos ocre `#64533a` de velas): dramática, sirve para anuncios o avisos serios · medido en fotograma propio
- Lu en pose de combate con arma (OP1, min 1:10): única pose de acción clara encontrada hasta ahora, útil si el canal necesita un personaje secundario femenino

## No encontré

- AnimeThemes.moe dio error 522 (servidor caído) tanto en `recolectar.py` como al reintentar — no se pudo sacar el opening/ending en calidad máxima con offset exacto de esa fuente; se usó Internet Archive como alternativa válida (⚠️ una sola fuente para el OP1 en sí, aunque el título y el contenido coinciden con lo emitido)
- No se encontró el ending (ED) de la serie en ninguna fuente accesible (Dailymotion, Internet Archive, AnimeThemes caído) — búsquedas: "Sakamoto Days ending", "Sakamoto Days ED1", "sakamoto days closing" en Dailymotion y archive.org, sin resultados claros de un ED completo
- No se pudo confirmar tendencias concretas de TikTok (la app/web no es accesible desde este servidor sin sesión); sólo hay indicios indirectos vía Dailymotion/Archive.org de qué clips corren fuera de YouTube
- No se ha comprobado si Yuki Hayashi (compositor) dio entrevistas sobre el "ambiente" que buscaba para cada tema — pendiente para el punto 9 en profundidad

## Bitácora

- `recolectar.py` (25-sep-2026): AniList, Dailymotion, Internet Archive, MusicBrainz — datos base en `datos-video.md`
- `fotogramas.py` sobre tráiler Dailymotion `x9c6rxi` cada 15 s (0:00-1:29): hoja de contacto revisada a mano
- `fotogramas.py` sobre Internet Archive `sakamoto-days-op-1` (OP1 completo) cada 10 s: hoja de contacto revisada a mano
- `fotogramas.py --fotograma 30 40 50 60` sobre el mismo OP1 + Python/Pillow para medir hex de cielo/medio/suelo en 4 escenas
- Búsquedas hechas: "Sakamoto Days trailer", "Sakamoto Days opening", "Sakamoto Days ending", "Sakamoto Days ED", "Sakamoto Days TikTok trend" (Dailymotion + Internet Archive, sin buscador web todavía)

Sigue: falta el ending (ED) con minuto exacto, más poses de acción/combate con capítulo (no sólo OP/tráiler — hace falta `episodio.py` sobre un capítulo real de la serie, que no está disponible en las fuentes abiertas usadas hasta ahora) y confirmar AnimeThemes cuando el servidor vuelva.
