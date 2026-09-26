# Parte del investigador de TEXTO, JUEGOS Y TÉCNICA · Undertale / Deltarune

Puntos de ENCARGO.md: **5** (tipografía), **6** (cómo hablan y piensan en
pantalla), **11** (videojuegos de la franquicia), **18** (estilo de dibujo y
técnica, y cómo replicarlo), **24** (obras parecidas), **25** (el mundo, la
historia y sus símbolos). No hay serie hermana para este encargo (68). Parto
de `partes/datos-texto.md` (casi vacío: sólo la cabecera de fuentes que
fallaron — Doblaje Wiki no encontró la página, Fandom no encontró «Kris»,
«Susie» ni «Ralsei»; los reviso yo con nombres alternativos). También miro
`partes/datos-imagen.md` (ya recolectado) para no repetir capturas.

Es un videojuego (dos, en realidad: Undertale 2015 y Deltarune 2018-2025 por
capítulos), así que los puntos 5, 6 y 11 se solapan mucho: la tipografía y los
«cuadros de diálogo» son parte de la interfaz. Los trato juntos donde
corresponde y separo por punto en el título de cada bloque.

## Hallazgos · Punto 5 — Tipografía

**Fuente principal del diálogo (narración, mundo exterior, menús): 8-Bit
Operator JVE.** Confirmado en dos fuentes independientes que coinciden en el
mismo nombre técnico:
- [Fonts In Use, «Undertale: dialogue and interfaces»](https://fontsinuse.com/uses/51307/undertale-dialogue-and-interfaces)
  (sitio especializado en identificación tipográfica, no un blog de fans):
  «Undertale uses the typeface 8-Bit Operator JVE for narration, overworld
  dialogue, and as the primary interface typeface», diseñada por **Jayvee
  Enaguas** (alias harvettfox96/nipcen), publicada en Dafont en 2011. Kerning
  ajustado (tight) en menús, suelto (loose) en diálogo y narración. Se usa
  también en Deltarune y en el sitio web de ambos juegos ✅.
- Confirmado también por la propia wiki (página **Determination**, ficha del
  mecanismo de juego) y por la comunidad del font libre: la fuente **libre
  «Determination»** (ver abajo) se hizo explícitamente como «a clone of 8-Bit
  Operator JVE based on an Undertale spritesheet», precisamente para no
  depender de licencia de pago ✅ (WebSearch, resumen de fontstruct/archive.org).
- El **logo/título** «UNDERTALE» **no es esta fuente**: es «bespoke artwork
  rather than a typed line of a single retail font» / «custom display
  lettering in a pixel-influenced style» (mismo artículo de Fonts In Use) ✅.

**Cada personaje con manía de habla tiene SU PROPIA fuente** (tabla completa
de la wiki, página **Quirk**, `undertale.fandom.com/wiki/Quirk`, contrastada
con Wikipedia en inglés para Sans y Papyrus):

| Personaje | Tipografía real (de pago) | Manía de texto | Fuente |
|---|---|---|---|
| Sans | **Comic Sans** (Vincent Connare, Microsoft 1995), convertida a bitmap para encajar con el pixel art | todo en minúsculas | Wikipedia «Sans (Undertale)» ✅ + wiki Quirk ✅ (dos fuentes) — cita textual: «Fox initially named him 'Comic Sans' after the typeface» |
| Papyrus | **Papyrus** (Chris Costello, Letraset 1983), también bitmap | todo en MAYÚSCULAS | Wikipedia «Papyrus (Undertale)» ✅ + wiki Quirk ✅ — cita: «Papyrus' dialogue is communicated in the papyrus font» |
| W. D. Gaster | **Wingdings** (Charles Bigelow y Kris Holmes, Microsoft 1992) | MAYÚSCULAS, temblor/shake, sólo en 2 salas inaccesibles (264/272, hay que editar el save) | wiki «W. D. Gaster»: «Gaster's dialogue uses a unique typeface, named Wingdings» ✅ + Fonts In Use ✅ |
| Aaron | (misma 8-Bit Operator) | termina cada frase con un emoticono guiñando | wiki Quirk ✅ (una fuente) |
| Temmie | (misma 8-Bit Operator) | mayúsculas al azar | wiki Quirk ✅ (una fuente) |
| Mettaton | (misma 8-Bit Operator) | todo en MAYÚSCULAS, efecto letra a letra distinto (procesa palabra entera) | wiki Quirk ✅ (una fuente) |

**Dato de traducción muy útil para «letra libre y qué falla al traducir»**:
en la versión japonesa NO se pudo mantener el chiste Comic Sans/Papyrus (son
fuentes latinas, no existen en japonés), así que Sans pasa a una «cutesy
irreverent typeface... like a stylized advertisement or a TV variety show» y
Papyrus a un «faux hand-drawn vertical script» — Wikipedia en inglés, sección
«Concept and creation» de ambos personajes ✅ (dos páginas independientes,
mismo patrón). Sirve directamente para el punto del encargo sobre «fuentes en
japonés»: aquí la propia obra tuvo que resolver ese problema.

**Otras fuentes de pago identificadas por Fonts In Use** (uso secundario, para
quien quiera el detalle completo de la interfaz de batalla):
- **Crypt of Tomorrow** (Anna Anthropy/Auntie Pixelante, 2008): estadísticas
  del jugador en el mundo exterior.
- **8-Bit Wonder** (Joiro Hatgaya, 2001/2009): pantalla de Game Over y el
  texto «HP».
- **Hachicro** (Masachika Yamasaki, 2001): números de daño en batalla.
- **Trouble Beneath The Dome** (Anna Anthropy, 2010, antes llamada «Mars
  Needs Cunnilingus»): estadísticas en batalla.
- **DotumChe** (HanYang, viene con Windows), bitmap y con antialias: diálogo
  de batalla, a veces con «waving/shaking effect».
- **Slanted** (Anna Anthropy, 2009): sólo en la pelea contra Napstablook.
- Los botones **FIGHT / ACT / ITEM / MERCY** están **rotulados a mano**
  («hand-lettering»), no son una fuente tipeada — visto también yo mismo en
  capturas (abajo, punto 6). Todo ✅ un solo artículo pero muy especializado
  y con capturas propias del autor; no lo bajo a ⚠️ porque cruza con la wiki
  en los nombres de Sans/Papyrus/Wingdings que sí están en dos fuentes.

**Letras libres recomendadas, comprobadas una por una con fontTools**
(descargué los `.ttf` reales —no de memoria— y corrí
`TTFont(f).getBestCmap()` buscando á é í ó ú ñ Ñ ¿ ¡ ü):

| Uso (punto 5) | Letra libre | Por qué encaja | ¿Tildes/ñ/¿¡? |
|---|---|---|---|
| Globo normal / narración / interfaz (8-Bit Operator JVE) | **Determination Mono** (fan-made, Haley «JapanYoshi» Wakamatsu, 2015 — clon directo hecho desde el spritesheet real del juego) | es LA réplica del propio juego, pixel monoespaciada | ✅ completo |
| Alternativa Google Fonts si se quiere algo más «oficial-libre» | **VT323** (fonts.google.com/specimen/VT323) | monoespaciada, pixel/terminal retro, muy usada en proyectos indie tipo Undertale | ✅ completo |
| Logo / título (custom pixel-lettering) | **Silkscreen** o **Jersey 15** (Google Fonts) | pixeladas cuadradas, bold, mismo espíritu «hand-lettering pixelado» que el logo real | ✅ completo (las dos) |
| Personaje Sans (Comic Sans bitmap) | **Comic Neue** (fonts.google.com/specimen/Comic-Neue, Craig Rozynski) | rediseño libre y explícito de Comic Sans, mismo aire desenfadado | ✅ completo |
| Personaje Papyrus (Papyrus bitmap) | **Sancreek** (Google Fonts) | la más cercana libre con «latin-ext» real entre las alternativas a Papyrus que lista la prensa de tipografía (no hay clon libre 1:1 de Papyrus) | ✅ completo |
| Interfaz de juego / menús (kerning ajustado) | Determination Mono / **Press Start 2P** (Google Fonts) | Press Start 2P es EL estándar libre para menús de videojuego retro | ✅ completo |
| Subtítulos o créditos | **VT323** o **Determination Sans** (variante sin serifas del mismo clon) | legible a tamaño pequeño, coherente con el resto | ✅ completo |

Archivos verificados en `/tmp/claude-0/trabajo/68-texto/fonts/` (10 `.ttf`:
Determination Mono, Determination Sans, Comic Neue, VT323, Press Start 2P,
Sancreek, Silkscreen, Jersey 15, Pixelify Sans — las 10 completas, ninguna le
falta un solo carácter de los 10 comprobados). Nota importante de método: al
bajar de Fontsource hay que pedir el archivo del subset **`latin`** (no
`latin-ext`): «latin-ext» en Fontsource es sólo para letras raras de otros
idiomas europeos (checo, polaco…), mientras que á/é/í/ó/ú/ñ/¿/¡ viven en
Latin-1 Supplement, dentro del subset **`latin`**. Lo comprobé al revés
primero (con `latin-ext`) y daba falso negativo en tres fuentes; repetido con
el archivo correcto, las tres pasan completas.
