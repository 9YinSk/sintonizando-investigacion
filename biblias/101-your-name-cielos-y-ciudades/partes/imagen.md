# Imagen · Your Name: cielos y ciudades (Kimi no Na wa. / 君の名は。)

Investigador de imagen. Puntos 1, 3, 15, 16, 19 y 23 de `ENCARGO.md`.
Parte de `partes/datos-imagen.md` (no repite esas consultas). Formato: libreta de datos, un dato por línea.

**Aviso importante de identidad de la obra (comprobado 25-sep-2026):** el AniList ID 97962 usado por
`recolectar.py` en `datos-imagen.md` (portada, sinopsis) **NO es la película**: es
«Suntory Minami Alps no Tennen Mizu» (サントリー 南アルプスの天然水), un SPECIAL de 3 anuncios comerciales
de Suntory que usan a Taki y Mitsuha con fines publicitarios (confirmado con la API GraphQL de AniList:
`{Media(id:97962){title{romaji} format episodes}}` → `Suntory Minami Alps no Tennen Mizu`, formato
SPECIAL, 3 episodios). ✅ La portada `97962-3rBcawJt63sG.jpg` de `datos-imagen.md` **no se usa** en esta
parte por ese motivo. El AniList real de la película es **id 21519** («Kimi no Na wa.» / «Your Name.»,
MOVIE, 2016, 716942 popularidad, 43331 favoritos) — confirmado con
`{Media(id:21519){title{romaji english} format startDate{year}}}`. Esto coincide con la comprobación que
ya hizo el investigador de voz en `partes/voz.md` sobre Doblaje Wiki (misma película, sin mezcla con
«El jardín de las palabras» ni «Suzume»). Los datos de personajes (favoritos Mitsuha 4560 / Taki 2865,
IDs de personaje 121514/121516/121518/121520/121522/121524) sí coinciden entre `datos-imagen.md` y el
AniList 21519 correcto, así que esa parte de `datos-imagen.md` es reutilizable.

## Hallazgos

### Punto 1 — Arte oficial, en cantidad y variado

**Key visual / póster oficial** (el arte más repetido de la franquicia) — ✅ dos fuentes:
- Póster internacional: Mitsuha y Taki de espaldas, sentados en el cráter del lago Itomori al
  atardecer, mirando el cometa Tiamat partirse en dos sobre un Tokio en miniatura abajo. Cielo en
  degradado estrellado azul-violeta-naranja, la marca de composición de Makoto Shinkai (cielo real y
  ciudad diminuta en el mismo encuadre).
  - AniList (cover del ID correcto 21519): `https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx21519-SUo3ZQuCbYhJ.png`
    (460×690, medido) ✅
  - Póster oficial latino en Doblaje Wiki (mismo key visual, edición para México/LatAm):
    `https://static.wikia.nocookie.net/doblaje/images/3/3b/Your_Name.jpg` (2000×3000, medido, vía API
    `imageinfo`) ✅ — visto en detalle: logo «Your Name.» en tipografía manuscrita fina blanca sobre el
    cielo, créditos abajo en español latino.
  - Banner ancho (mismo arte, recorte panorámico): AniList
    `https://s4.anilist.co/file/anilistcdn/media/anime/banner/21519-1ayMXgNlmByb.jpg` (1900×400, medido) ✅
- **Paleta medida con `estilo.py`** sobre el key visual (`ref/anilist_cover.png`, 460×690):
  `#059BDB` 21% · `#074D9A` 21% · `#0472B7` 13% · `#E1E4E7` 10% · `#99C0DD` 8% (azul cielo degradado,
  predominante) y en el recorte panorámico (`anilist_banner.jpg`, 1900×400) tonos de atardecer:
  `#EDD9BF` · `#96808E` · `#392830` (naranja-rosado-violeta del horizonte). ✅ (medido, no de memoria).

**Hoja de contacto propia** (`herramientas/investigar_serie.py`, wiki `kiminonawa`, páginas Taki y
Mitsuha, 39 imágenes ≥500 000 px, guardada en `hojas/personajes_01.jpg` de esta parte):
- Nº 1 Mitsuha Miyamizu 2013 (retrato limpio, pelo largo, uniforme urbano) · Nº 2-3 grupo (Shinta,
  Taki, Tsukasa / Taki y Okudera en su cita) · Nº 4 Mitsuha gritando (shock del intercambio de cuerpos)
  · Nº 10 Mitsuha y Taki en Kataware-doki (atardecer, escena cumbre) · Nº 18 «Writing» (Taki escribiendo
  en su propia mano) · Nº 24-25 retratos cuadrados estilo icono (2022) · Nº 35 «Mitsuha comet» (ella
  mirando el cometa) · Nº 38 «Futaba Death» (madre de Mitsuha) · Nº 39 reencuentro final en la
  escalinata. ✅ (mirada en Read, 2400×1420, hoja completa).
- Fuente de cada imagen: `https://kiminonawa.fandom.com/wiki/Taki_Tachibana` y
  `.../wiki/Mitsuha_Miyamizu` (API `imageinfo`, anchos y altos medidos por la propia API, ya en
  `datos-imagen.md`). ✅

**Hojas de modelo (character design) encontradas fuera de lo que trajo el recolector** (búsqueda manual
en `allimages` de la wiki, prefijos `Itomori`, `Miyamizu`, `Suit`) — ✅ (API `imageinfo`, tamaño medido):
- `Itomori_High_MaleUni.png` (1432×2160) y `Itomori_High_FemaleUni.png` (1150×1990): hoja de modelo del
  **uniforme escolar de Itomori High** (chico y chica, frente y espalda), la referencia técnica más
  limpia de vestuario que hay en la wiki.
- `Itomori_High_SweaterUni.png` (1150×1990): variante de invierno con jersey.
- `Miyamizu_Attire.jpg` (1280×686), `Miyamizu_Gohei.jpg` (1280×697), `Miyamizu_Headdress.jpg`
  (1280×720): fotogramas del ritual sintoísta familiar (kimono blanco de miko, gohei ceremonial,
  tocado), vistos en Read — escena nocturna con luz de fuego/luna, tonos morados y ocres por la
  iluminación de la escena (no son los colores planos de la tela; ver punto 15 para el hex real de la
  tela con luz neutra).
- `Suit.png` (564×1800): Taki adulto de traje (epílogo, Tokio, años después).

**Portadas de productos físicos** — ✅:
- Póster/carátula de Blu-ray latino: el mismo key visual, en Doblaje Wiki (arriba). ⚠️ no encontré la
  carátula japonesa original de CoMix Wave/Toho en alta resolución medida desde aquí (ver «No encontré»).

**Aviso para el redactor**: la única portada de `datos-imagen.md` (AniList 97962) es del especial de
Suntory, no de la película — no usarla como «portada oficial de la serie», sólo como colaboración
comercial si aplica (ver punto 23).

## Lo mejor para la lámina

_(se completa al final, punto pendiente de cerrar la tanda)_

## No encontré

_(pendiente)_

## Bitácora

_(pendiente)_

Sigue: puntos 3 (fan art/3D con licencia — ya recolectados modelos Sketchfab de torii/estación/altar
sintoísta, falta redactar y completar), 15 (vestuario con hex — falta medir el hex real del kimono
miko y del uniforme con luz neutra, ya localizadas las hojas de modelo), 16 (fondos/ciudades — ya
encontrados los lugares reales de Tokio vía Tofugu, falta redactar con hex de paisajes y agregar
Wallhaven), 19 (texturas 2D — falta buscar tramas/pinceles equivalentes), 23 (colaboraciones — sólo
hallado el comercial de Suntory y el fenómeno de turismo/peregrinación oficial, falta cosplay/figuras),
hojas de contacto definitivas en `hojas/`, `imagen.json`, «Lo mejor para la lámina», «No encontré» y
«Bitácora» completas.
