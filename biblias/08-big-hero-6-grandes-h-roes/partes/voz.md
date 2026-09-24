# Voz y personajes · Big Hero 6 (Grandes Héroes) (08-big-hero-6-grandes-h-roes)

Investigador de voz y personajes. Puntos de `ENCARGO.md`: **7** (popularidad),
**8** (doblaje latino), **12** (fandom y qué no hacer), **13** (carácter y
forma de hablar) — repaso y confirmación en dos fuentes — y **20, 21, 22**
(gustos, por qué la aman, fan dubs), nuevos.

Parto de `partes/datos-voz.md` (Doblaje Wiki, texto de personalidad de la
wiki de Disney, Dailymotion) y de las secciones 2, 9, 10 y 14 de `biblia.md`
(ya escritas en la primera pasada, con red cerrada, sin vídeos mirados). No
repito lo que ya está ✅ ahí; confirmo lo ⚠️, corrijo lo que encontré mal (los
actores de Fred, GoGo y Wasabi **sí estaban** en Doblaje Wiki, la primera
pasada no los vio) y añado lo nuevo.

Trabajo pesado (wikitext, HTML y transcripciones de `voz.py`) en
`/tmp/claude-0/trabajo/08-voz/`.

---

## 1 · Doblaje latino: los que faltaban, y estudio/dirección en dos fuentes más (punto 8)

La primera pasada (red cerrada) dijo «Fred, GoGo, Wasabi: no lo encontré» y
dejó estudio/dirección con «sólo Doblaje Wiki». **Sí estaban**: el wikitext
completo de la página `Grandes_héroes` de Doblaje Wiki (tabla «Reparto») los
trae; sólo que la tabla de `recolectar.py` no capturó esas columnas porque el
wikitext usa `colspan` distinto por fila. Lo comprobé de nuevo pidiendo el
wikitext entero
(`https://doblaje.fandom.com/es/api.php?action=parse&format=json&prop=wikitext&page=Grandes_h%C3%A9roes`)
y además encontré **dos fuentes independientes más** que traen el reparto
completo con crédito de estudio y dirección: **The Dubbing Database** (wiki
hermana, en inglés, no es Fandom de doblaje) y **CHARGUIGOU / Disney
International Dubbings** (archivo de un aficionado con los créditos exactos
de Disney Character Voices International).

| Personaje | Voz latina | Confirmado en |
|---|---|---|
| Hiro Hamada | **Memo Aponte** (Guillermo Aponte Mille) | ✅ Doblaje Wiki, PRODU (entrevista), Radio Disney MX, [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes), [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) |
| Baymax | **Alan Prieto** | ✅ Doblaje Wiki, SoundCloud, TikTok SDV, dubdb, CHARGUIGOU |
| Tadashi Hamada | **Alexis Ortega** (1989-2026) | ✅ Doblaje Wiki, El Imparcial, El Informador, LatinUS, dubdb, CHARGUIGOU |
| **Fred Frederickson** | **Noé Velázquez Pedroza** | ✅ nuevo — Doblaje Wiki (wikitext, no la tabla resumida) + [dubdb](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes) + [CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html) |
| **GoGo Tomago** | **Erika Ugalde** | ✅ nuevo — mismas tres fuentes |
| **Wasabi** | **Alan Bravo** | ✅ nuevo — mismas tres fuentes |
| Honey Lemon | **Génesis Rodríguez** (se autodobla) | ✅ Doblaje Wiki, dubdb (nota de «Trivia»: repitió su papel del inglés), CHARGUIGOU |
| Robert Callaghan / Yokai | **Humberto Vélez** | ✅ Doblaje Wiki, dubdb, CHARGUIGOU |
| Alistair Krei | **Idzi Dutkiewicz** | ✅ Doblaje Wiki, dubdb, CHARGUIGOU |
| **Tía Cass** | **Patricia Palestino** | ✅ ya no es «una fuente»: dubdb y CHARGUIGOU la confirman también |
| Abigail Callaghan | **Yadira Aedo** | ✅ Doblaje Wiki, dubdb, CHARGUIGOU |
| Padre de Fred | **Jesse Conde** | ✅ Doblaje Wiki, dubdb, CHARGUIGOU |
| Heathcliff (mayordomo de Krei) | **Arturo Mercado Chacón** | ✅ Doblaje Wiki, CHARGUIGOU (dubdb no lo lista) |
| Yama | Octavio Rojas | ✅ Doblaje Wiki, CHARGUIGOU |
| General | Paco Mauri | ✅ Doblaje Wiki, dubdb, CHARGUIGOU |
| Oficial Gerson | Germán Fabregat | ✅ Doblaje Wiki, CHARGUIGOU («Sargento») |
| Réferi | Gabriela Guzmán | ✅ Doblaje Wiki, CHARGUIGOU |
| Reportero | Agustín L. Lezama (López Lezama) | ✅ Doblaje Wiki, CHARGUIGOU |

- **Estudio y equipo, en dos fuentes más** (antes «sólo Doblaje Wiki, dos
  páginas»): **Taller Acústico, S.C.**, dirección **Ricardo Tejedo**,
  traducción Katya Ojeda Iturbide y el propio Tejedo, dirección de casting
  **Luis Daniel Ramírez**, gerencia de producción Erika Sánchez Santarelli,
  producción Yeri Casanova, edición **Diseño en Audio «DNA»**, mezcla
  **Shepperton International** (Reino Unido), ejecutivo creativo Raúl Aldana,
  versión en español producida por Disney Character Voices International ✅
  ([Doblaje Wiki](https://doblaje.fandom.com/es/wiki/Grandes_h%C3%A9roes),
  [dubdb, ficha de crew](https://dubdb.fandom.com/wiki/Grandes_h%C3%A9roes),
  [CHARGUIGOU, lista de crew completa](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html)).
- **Voces adicionales** (elenco de relleno) listadas sólo por CHARGUIGOU, 33
  nombres: Adriana Casas Basilio, Ana Luisa Pérez Compeán, Berenice Vega,
  César Filio, César Garduza, Salvador «Chava» Reyes, Daniel Lacy, Diego
  Armando Ángeles Ramírez, Emmanuel Bernal, Erick Salinas, Erika Dubka
  Sánchez, Esteban Desco, Gabriela Guzmán, Gerardo Alonso, Gisella Ramírez,
  Gwendolyne Flores, Herman López, Jahel Morga Vera, Jesse Conde, José Luis
  Miranda B., Joss Waleska, Luis Navarro, Luna Arjona, Magda Tenorio, Mark
  Pokora, Marysol Cantú, Mauricio Pérez Castillo, Orlando Rivas, Pedro
  D'Aguillón Jr., Raúl Solo, Raymundo Armijo Ugalde, Ricardo Tejedo, Roberto
  Velázquez, Sofía Huerta, Valentina Souza, Yeri Insunza Casanova ⚠️ (una sola
  fuente; no sé qué papel exacto tuvo cada uno) ([CHARGUIGOU](https://disneyinternationaldubbings.weebly.com/big-hero-6--latin-american-spanish-cast.html)).
- **No hay muestras de audio en la ficha de Doblaje Wiki** de esta película
  (comprobado en el wikitext: cero etiquetas `<sm2>`), así que las frases
  textuales con minuto de abajo salen de clips doblados reales, no de
  muestras sueltas.

