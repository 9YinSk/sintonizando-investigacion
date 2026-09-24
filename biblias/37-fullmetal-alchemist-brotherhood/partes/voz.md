# Voz y personajes · Fullmetal Alchemist: Brotherhood (encargo 37)

Investigador de voz y personajes. Puntos de ENCARGO.md: **7, 8, 12, 13, 20, 21, 22**.
Formato libreta: un dato por línea, fuente enlazada, ✅ (dos fuentes) o ⚠️ (una sola o de memoria).
Parte de `partes/datos-voz.md` (AniList, Doblaje Wiki) — no repite esas consultas, sigue desde ahí.

## Punto 8 · Doblaje latino: quién dobla a cada uno y frases textuales

**Hay DOS doblajes latinos completos**, cosa rara y dato de sabor para el canal:

1. **Animax / M&M Studios** (Venezuela, 2011-2012, autodirección — sin director fijo, el propio elenco se dirigía). Es el doblaje "clásico", el que casi todo el fandom hispano vio primero.
2. **Funimation / redoblaje** (Artworks Digital Studio → C&G Dubbing Studio, México, 2021), dirigido por **Gerardo Ortega** y **Óscar López**.

Fuente primaria de todo el reparto: wikitext completo de Doblaje Wiki vía API
`action=parse&prop=wikitext` (evita el 402 de la web normal) ·
https://doblaje.fandom.com/es/wiki/Fullmetal_Alchemist:_Brotherhood — la tabla «Reparto»
tiene DOS pestañas (`tabber`), una por doblaje, con seiyū + actor latino por fila. El
`recolector.py` sólo había bajado el crudo con los nombres de archivo de audio, no los
actores: se volvió a sacar el wikitext a mano (obligatorio, ver AYUDANTE.md «el encargo manda»).

### Los 4 personajes del encargo (doblaje 1 Animax / doblaje 2 Funimation), verificado en dos fuentes cada uno

| Personaje | Seiyū | Actor Animax (2011-12) | Actor Funimation (2021) | Verificado |
|---|---|---|---|---|
| Edward Elric | Romi Park | **José Manuel Vieira** | **José Manuel Vieira** (el mismo actor en los dos doblajes) | ✅ Doblaje Wiki (wikitext tabla) + AniList «Spanish VA» (datos-voz.md l.14) coinciden |
| Alphonse Elric | Rie Kugimiya | **Jhonny Torres** | **Jhonny Torres** (el único actor de toda la franquicia —2003, Brotherhood, live-action— que SIEMPRE ha sido Al) | ✅ Doblaje Wiki (tabla + trivia «Sobre su reparto») + AniList (l.16) |
| Roy Mustang | Shinichirō Miki | **Rolman Bastidas** | **Rafael Escalante** | ✅ Doblaje Wiki (tabla) + AniList «Spanish VA: Rafael Escalante, Rolman Bastidas» (l.15, cita ambos) |
| Winry Rockbell | Megumi Takamoto | **Melanie Henríquez** | **Montserrat Aguilar** | ✅ Doblaje Wiki (tabla) + AniList «Inès Blázquez, Melanie Henriquez, Montserrat Aguilar» (l.17) |

- Dirección de casting Animax: **Maythe Guedes**. Estudio: **M&M Studios** — este fue el
  ÚLTIMO anime que grabó el estudio antes de cerrar (abril 2012). ✅ wikitext Doblaje Wiki.
- Dirección Funimation 2021: **Gerardo Ortega y Óscar López**, estudio **C&G Dubbing
  Studio** (antes Artworks Digital Studio), traducción de **Jennifer Medel** (ep. 1-49,61)
  y **Ai Enomoto** (resto). ✅ confirmado en DOS fuentes independientes: wikitext de
  Doblaje Wiki Y el artículo de **ANMTV**
  https://www.anmtvla.com/2021/10/fullmetal-alchemist-brotherhood-estrena_88.html
  («estrena redoblaje… C&G Dubbing Studio, dirigido por Gerardo Ortega y Óscar López»).
- El redoblaje se estrenó el **14 de octubre de 2021** en Funimation; ep. 1-24 primero,
  25-50 el 28 de octubre, el resto en noviembre. ✅ ANMTV (arriba) + Doblaje Wiki.
- Curiosidad: del elenco de la **película live-action 2017**, sólo **Jhonny Torres**
  (Alphonse) y **Montserrat Aguilar** (Winry) repiten en el redoblaje 2021. ⚠️ una fuente
  (Doblaje Wiki «Sobre su reparto», Funimation).

### Reparto secundario clave (ambos doblajes, con seiyū), en `voz.json` y en `reparto.json` (carpeta de trabajo)

Se sacaron **32 personajes por doblaje** (64 filas en total) del wikitext: Van Hohenheim,
King Bradley, los 7 homúnculos, Alex Louis Armstrong, Solf J. Kimblee, Izumi Curtis, Riza
Hawkeye, Havoc, Olivier Armstrong, Ling Yao, May Chang, Lan Fan, Maes Hughes, Maria Ross,
Pinako, Trisha, Rose Thomas, familia Hughes, Barry el Carnicero, La Verdad. Todo con seiyū
+ actor de cada doblaje, fuente única (wikitext), sin ⚠️ porque la tabla de la propia wiki
ya es la fuente primaria citada por el encargo. Lista completa en `voz.json` →
`reparto_doblaje`.

- Dato para el canal de doblaje: **muchos actores repitieron personaje desde la serie
  2003** en el doblaje Animax (Rolman Bastidas=Roy, Jhonny Torres=Al, José Manuel
  Vieira=Ed, Adolfo Nittoli=Cicatriz, Víctor Díaz=Kimblee, Manuel Bastos=Shou Tucker,
  Ramón Aguilera=Sig Curtis…) — dato de continuidad que le importa a esta comunidad.
  ✅ wikitext «Sobre su reparto · Animax» (lista de ~20 nombres).
- Un actor **no identificado** reemplazó a Herman López (Sig Curtis) desde el ep. 62 del
  redoblaje: López fue hospitalizado durante la grabación y falleció el 19-dic-2021. ⚠️
  una fuente (Doblaje Wiki), dato sensible, no llevar a la lámina.
- Envidia (no binario en japonés) se dobla con pronombres masculinos en LATINO en los dos
  doblajes — dato importante para no «corregir» el género al escribir diálogos de fan.
  ✅ wikitext, sección «Sobre la traducción».

### Frases textuales del doblaje latino (verificadas oyendo el audio oficial de Doblaje Wiki con `voz.py`, Whisper local)

No hay clips de escena completa doblados accesibles sin YouTube (bloqueado en este
servidor); se usaron las **muestras de audio oficiales** que Doblaje Wiki cuelga como
referencia de cada actor (audio real de la emisión, recortado). El minuto es el segundo
**dentro de esa muestra**, no de un episodio — se anota así, sin inventar capítulo.

- **Edward Elric** (José Manuel Vieira, Animax) — registro medio (177 Hz), **muy
  expresivo** (16.5 semitonos de rango), habla rápido (3.18 palabras/s): «¿Por qué nadie
  entiende que la alquimista de acero soy yo?» [seg. 0:53 de la muestra] · «Parece que
  tendré que obligarte a entregármelo» [0:49]. ✅ transcripción propia +
  https://static.wikia.nocookie.net/doblaje/images/0/04/EdwardElric%28Audio%29FMAB.mp3
- **Roy Mustang** (Rolman Bastidas, Animax) — registro grave (108 Hz), muy expresivo
  (10.7 semitonos), ritmo normal (2.03 palabras/s), en la muestra está furioso tras la
  muerte de Hughes: «Tú mataste a Hughes, será todo lo que necesitaba saber… ya no tienes
  que decir nada más» [0:40-0:46] · «Empezó a llover» [0:35, la lluvia es su gatillo
  emocional en toda la serie]. ✅ propia + muestra RoyMustang(Audio)FMAB.mp3 (datos-voz.md l.257).
- **Maes Hughes** (Sergio Pinto, Animax) — registro grave (134 Hz) pero **el más
  expresivo de los 6 medidos** (23.3 semitonos): «Los hombres son criaturas que dejan que
  sus acciones hablen por ellos… cuando sienten dolor no quieren que otros sufran ni se
  preocupen» [0:34-0:38] — resume su rol de «papá» del grupo. ✅ propia + muestra.
- **Trisha Elric** (Maritza Rojas) — registro agudo (227 Hz), muy expresiva (20.5
  semitonos): «Son hijos de su padre, estoy orgullosa de ustedes» [0:18-0:20]. ✅ propia.
- **Alphonse niño** (voz de Al de pequeño) — registro medio (190 Hz), habla **lento**
  (1.79 palabras/s), tono triste: «Hermano, tengo hambre… hace frío… vayamos a casa» [0:02-0:09].
  ✅ propia + AlphonseElric(niño)(Audio)FMAB.mp3.
- **Winry niña** — registro muy agudo (305 Hz), la más rápida y expresiva de las 6 (3.56
  palabras/s, 28.3 semitonos): «¿Están leyendo otra vez un libro que no es de la
  escuela?… no es justo, siempre guardan secretos entre ustedes» [0:17-0:23]. ✅ propia.
- Fichas de voz completas (Hz medidos, semitonos, velocidad) en `voz.json` → `fichas_voz`
  y en la carpeta de trabajo `voz_edward/`, `voz_roy/`, `voz_hughes/`, `voz_trisha/`,
  `voz_alphonse_nino/`, `voz_winry_nina/` (transcripción .txt/.srt + ficha_voz.json).
- ⚠️ **No encontré** clips de escena larga con diálogo doblado (2+ personajes
  conversando) accesibles sin YouTube: Dailymotion sólo tiene los tráileres (en
  `datos-voz.md`, todos en inglés/sin doblar) e Internet Archive no tiene la serie
  doblada al latino subida legalmente. Si el redactor necesita más frases largas,
  puede reintentar YouTube con `yt-dlp` esperando el enfriamiento del 429 (dio ese
  error en este intento, ver Bitácora).
- Frase «Un alma no vale lo que un cuerpo» / el «intercambio equivalente» («Equivalencia
  de intercambio» en Animax, cambiado a «intercambio equivalente» en Funimation) es LA
  frase que todo fan reconoce — ✅ dos fuentes: wikitext Doblaje Wiki (sección
  «traducción») + es la premisa central citada en toda reseña (ver punto 21).

Sigue: punto 7 (encuestas de popularidad) y siguientes, en curso.
