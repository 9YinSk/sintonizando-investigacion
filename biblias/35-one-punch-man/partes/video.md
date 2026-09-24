# Parte del investigador de VÍDEO · One Punch Man (encargo 35)

Puntos de `ENCARGO.md` que me tocan (según `EQUIPO.md`): **2** (fotogramas de escenas
icónicas), **4** (fondos y sitios: luz, paleta, texturas), **9** (música y sonido),
**10** (vídeos y tendencias) y **14** (poses analizadas por personaje).

Parto de `partes/datos-video.md` (ya recolectado, no repetido) y de la biblia a medias
(`biblia.md` ya trae un §2 "Las escenas que sirven" muy trabajado de otra pasada — no lo
repito, solo sumo lo nuevo que vi en esta tanda y lo que falta: §5, §11, §12, §15).

**YouTube bloqueado** todo el turno («Sign in to confirm you're not a bot», igual que en
la pasada anterior). Usé **Dailymotion** (copias de fans y clips de medios: Vidaextra,
Sensacine, aniBattle, AnimeBrawlCollection, moviepilot) e imágenes 1080p de la wiki de
Fandom (con Referer). Vi de verdad 4 vídeos con `herramientas/episodio.py` /
`fotogramas.py` (ficha minuto a minuto en `partes/episodios.md`, hojas en
`/tmp/claude-0/trabajo/35-video/`, borrados los `.mp4` al terminar):

1. **Opening T1** «THE HERO!!» — Dailymotion moviepilot, https://www.dailymotion.com/video/x7xerpa (1:29)
2. **Saitama vs. Boros** (final de temporada 1) — Dailymotion aniBattle 4K, https://www.dailymotion.com/video/x9b8564 (6:32)
3. **Saitama vs. Genos** (primer entrenamiento real) — Dailymotion AnimeBrawlCollection, subtítulos en inglés, https://www.dailymotion.com/video/x8raxsq (4:06)
4. **Tráiler oficial T3** (Garou) — Dailymotion Vidaextra, https://www.dailymotion.com/video/x8tl06u (1:54)

---

## Hallazgos

### Punto 2 · Escenas icónicas (lo nuevo; el resto ya está en biblia.md §2)

- **Identifiqué el episodio exacto** del primer combate de entrenamiento Saitama-Genos
  que la wiki no tenía citado: es **«Saitama vs. Genos»**, manga cap. 17, **anime
  episodio 5 (T1-05)**, dentro del arco «National Superhero Registry». La wiki cita
  literalmente la misma frase que oí en el clip («Even he cannot explain the secret to
  his strength... but this battle may afford me a clue!»/«Even Master Saitama himself
  cannot explain. The secret to his power…» a 2:59-3:05 del clip) ·
  [wiki, texto](https://onepunchman.fandom.com/wiki/Saitama_vs._Genos) + clip visto
  (Dailymotion x8raxsq) · ✅ (dos fuentes, misma cita) · episodio T1-05.
- **La patada a la Luna, minutos exactos** (afina el dato de otra pasada, que decía
  «4:04-4:20» del mismo vídeo): en mi visionado va de **4:02** (Saitama sale volando,
  se ve la Tierra) a **4:16** (recoge una roca en la Luna, mirándola) ·
  [Dailymotion x9b8564](https://www.dailymotion.com/video/x9b8564?start=242) (aniBattle) ·
  ✅ (coincide con la otra pasada, mismo vídeo, mismo tramo) · T1-12.
- **Golpe Serio, tramo exacto**: la silueta de Saitama en pose de cruz (brazos y
  piernas abiertos, a punto de golpear) se ve en el **segundo 6:11-6:12**; el haz que
  parte hacia el espacio y llega a ver la Tierra desde fuera, **6:19-6:24** ·
  [Dailymotion x9b8564](https://www.dailymotion.com/video/x9b8564?start=371) · ✅ (coincide
  con «misma copia 5:44-6:20» de la otra pasada, con más precisión) · T1-12.
- **Nueva escena para la lámina — el primer entrenamiento real (T1-05)**: Genos pide
  un combate «en serio», con reglas (esquivar lo esquivable, no contenerse, seguir
  hasta no poder más); Saitama lo esquiva todo por «imagen residual» (afterimage) y
  gana tocándole la mejilla; termina con «I'm starving, time for lunch» / en japonés
  quedan a comer udon · [Dailymotion x8raxsq](https://www.dailymotion.com/video/x8raxsq)
  (sub. en inglés) + [wiki](https://onepunchman.fandom.com/wiki/Saitama_vs._Genos) ·
  ✅ · T1-05, 0:10-4:05 del clip.
- **Fotograma oficial 1080p** de este combate (Genos lanzando su Cañón de Incineración
  con el brazo entero convertido en cañón con rayos; Saitama vuela hacia atrás, cara
  inexpresiva, ropa ondeando) — sirve para «pose sin inmutarse»:
  [wiki, `Genos_vs_Saitama_spar.png`](https://static.wikia.nocookie.net/onepunchman/images/6/68/Genos_vs_Saitama_spar.png) ·
  1920×1080 (medido, API `imageinfo`) · ✅ · T1-05.
- **Tráiler oficial de la T3** (Garou, 1:54): 0:10 logo; 0:21-0:52 Garou se transforma y
  pelea contra monstruos con un cielo de atardecer rojo/rosa; 0:58 salto en silueta;
  1:15 primer plano del ojo de Saitama; 1:23-1:30 Garou con cara de monstruo; 1:34
  cartela «VS» en blanco y negro; 1:40 logo «ONE PUNCH MAN 3»; **1:50 créditos
  completos** (reparto y staff, ver punto 9 y 10) ·
  [Dailymotion x8tl06u](https://www.dailymotion.com/video/x8tl06u) (Vidaextra, 76 923
  vistas) · ✅ (créditos en pantalla, fuente primaria) · T3, oct-2025.

### Punto 4 · Sitios, luz, paleta y texturas (sección vacía en biblia.md — la lleno)

**Colores medidos con `herramientas/estilo.py`** (Pillow), sobre fotogramas que
recorté yo mismo de las hojas de `episodio.py`/`fotogramas.py` o sobre arte oficial de
la wiki. Cito siempre de dónde sale cada paleta.

- **Z-City** (la ciudad de Saitama): fondo urbano gris-azulado con cielo azul intenso y
  nubes blancas, edificios en beige/gris/blanco roto, montaña difuminada al fondo.
  Paleta medida: `#B0B1B8` 21% · `#888C98` 18% · `#5F6881` 17% · `#3C455C` 16% ·
  `#D6D6D9` 15% · `#1C2028` 13% (fondo azul-noche de las sombras) · sombreado
  degradado con mucha línea gris `#5D5E64` · [wiki, `Zcity.png`](https://static.wikia.nocookie.net/onepunchman/images/f/f8/Zcity.png)
  1280×719 (medido) · ✅ · imagen del sitio general (episodio no especificado en la wiki).
- **Campo de batalla final contra Boros** (T1-12, de noche, tras el impacto de la nave):
  paleta casi negra con rojo y naranja de fuego: `#100305` 26% · `#DB1515` 21% ·
  `#380307` 18% · `#63040D` 14% · `#A40411` 13% · `#E96826` 7% (naranja de la nave en
  llamas) — saturación 91%, brillo 45%, sombreado degradado/pintado, casi sin línea
  visible · medido sobre fotograma del min. 2:09 de [Dailymotion x9b8564](https://www.dailymotion.com/video/x9b8564?start=129) · ✅.
- **Forma verdadera de Boros** (silueta negra, ojo blanco, dientes): fondo casi negro
  `#0F040B` 37%, piel/hueso crema `#E8D5BD` 19%, granates apagados `#321420`/`#5A353F`
  — saturación 52%, brillo 37%, mucha línea marcada `#503238` · medido en el min. 1:36
  del mismo vídeo · ✅.
- **Impacto del Golpe Serio** (el fogonazo blanco antes del haz): paleta casi
  monocroma, blanco cálido `#F6F5E0` 40% + `#F2F6E0` 36% + `#F9F2E0` 17%, apenas negro
  3% — brillo 93%, sombreado plano (cel), casi sin línea · min. 6:11 · ✅. Sirve para el
  «flash» de cualquier golpe de la lámina.
- **La Tierra vista desde el espacio** (tras el Golpe Serio): `#F3EFD9` 33% (haz),
  `#0C0708` 18% (espacio), `#A3BEC5` 16% (azul Tierra), `#8B8987` 11% (nubes),
  `#594470` 11% (morado del rayo) — sombreado degradado, mucha línea `#8B8187` · min.
  6:22 · ✅.
- **Cañón/desierto del entrenamiento con Genos** (T1-05, de día): tierra clara y roca
  contra cielo azul: `#1D1917` 37% (roca en sombra) · `#C0B69D` 34% (tierra clara) ·
  `#E5DCC9` 17% (polvo/cielo claro) · `#927F5E` 9% · azul de cielo `#3858B3` 3% —
  saturación baja (23%), brillo medio (53%), línea normal `#8D7A56` · min. 0:59 de
  [Dailymotion x8raxsq](https://www.dailymotion.com/video/x8raxsq?start=59) · ✅.
- **Llamarada del Cañón de Incineración de Genos** (mismo combate): naranja de fuego
  intenso `#F1C92E` 19% + `#BD5F0C` 17% sobre marrón quemado `#291009` 31% / `#6C2A08`
  23% — saturación 80% · min. 2:30 · ✅.
- **Opening T1 — acantilados de hielo** (paisaje simbólico, sin localizar en la trama):
  paleta fría, grisazulada: `#586874` 23% · `#394751` 22% · `#7F8C93` 16% · `#ADB3B2`
  15% · `#1B2125` 13% — sombreado degradado, mucha línea `#64727E` · min. 0:22 del
  opening ([Dailymotion x7xerpa](https://www.dailymotion.com/video/x7xerpa?start=22)) · ⚠️
  (paisaje de openings, no aparece tal cual en el anime; sirve solo como referencia de
  ambiente «fin del mundo»).
- **Tráiler T3 — atardecer de la pelea con Garou**: rojos y granates oscuros
  `#2C0A15` 25% · `#411E23` 25% · `#17040C` 23% · `#592D35` 16% · rosa claro `#E5A8BA`
  5% — saturación 66%, brillo bajo (26%) · min. 0:47 del tráiler
  ([Dailymotion x8tl06u](https://www.dailymotion.com/video/x8tl06u?start=47)) · ✅.
  **Este atardecer rojo/rosa es la paleta propia de la temporada 3** (Garou), distinta
  del gris-azulado de Z-City y del negro-rojo de la pelea con Boros.
- **Texturas reales equivalentes (CC0)**, por sitio:
  - Ruinas/hormigón de la ciudad destruida → **Concrete034** (ambientCG, CC0) —
    https://ambientcg.com/view?id=Concrete034
  - Brazo/armadura de Genos y los robots → **Metal063** (ambientCG, CC0) —
    https://ambientcg.com/view?id=Metal063
  - Roca del cañón/la Luna → **Rock063** (ambientCG, CC0) —
    https://ambientcg.com/view?id=Rock063
  - ✅ (API de ambientCG, licencia CC0 confirmada en la propia ficha del recurso).

---

## Punto 9 · Música y sonido (sección vacía en biblia.md — la lleno)
