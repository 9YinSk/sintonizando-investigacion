# Voz y personajes · Final Fantasy VII

Investigador de voz y personajes. Puntos 7, 8, 12, 13, 20, 21 y 22 de ENCARGO.md.
Libreta de datos: un dato por línea, con fuente(s), ✅ (dos fuentes) o ⚠️ (una), y minuto/tamaño si aplica.
Parte de `partes/datos-voz.md` (recolectado antes) y de búsquedas propias. Serie sin encargo hermano.

## 7 · Encuestas de popularidad

Tres medidas distintas de popularidad, todas con fuente. Cloud, Tifa y Aerith se repiten arriba en todas.

- Encuesta oficial de Famitsu sobre personajes de Final Fantasy VII Remake (jul-2020): 1º Cloud (1991 votos), 2º Tifa (1548), 3º Aerith (1433), 4º Jessie (535), 5º Barret (498), 6º Sephiroth (404), 7º Reno (376), 8º Red XIII (312), 9º Rufus (241), 10º Zack (113) · [Push Square](https://www.pushsquare.com/news/2020/07/cloud_tops_final_fantasy_vii_remake_popularity_poll_in_japan_by_some_distance) y [hilo de ResetEra con los mismos datos](https://www.resetera.com/threads/final-fantasy-vii-remake-famitsu-character-popularity-poll-spoilers.252405/) (la fuente original es el tuit de @aitaikimochi, citado en ambos) · ✅
- Encuesta nacional de NHK «Zenkoku Kessen! Final Fantasy» (2020, 468 654 votos, TODA la franquicia, no sólo VII): entre los 10 personajes más votados de toda la saga están 1º Cloud, 3º Aerith, 9º Tifa y 10º Sephiroth (Yuna, Vivi, Zidane, Emet-Selch, Tidus y Lightning ocupan el resto) · [NextN](https://www.nextn.es/2020/03/encuesta-nhk-lo-mas-querido-final-fantasy/), citada también por [LEVEL UP](https://www.levelup.com/noticias/642733/Y-Sephiroth-Segun-encuesta-el-villano-mas-popular-de-Final-Fantasy-es-de-un-MMO) · ✅
- Misma encuesta NHK, ranking de jefes/invocaciones: Knight of the Round (1º) y Bahamut Zero (8º) son de FFVII; en música, «One-Winged Angel» (6º) y «Aerith's Theme» (7º) también son de FFVII · [NextN](https://www.nextn.es/2020/03/encuesta-nhk-lo-mas-querido-final-fantasy/) · ⚠️ (una fuente; sirve como dato de contexto, no como tabla de personajes)
- Medida distinta, de fans: en Danbooru hay 41 876 dibujos etiquetados «final_fantasy_vii»; por personaje, Tifa lidera con 17 112, Cloud 16 037, Aerith 11 984, Sephiroth 5855, Zack 3373, Yuffie 2894, Barret 946, Red XIII 803 (dato ya en `datos-voz.md`) · [Danbooru](https://danbooru.donmai.us/posts?tags=final_fantasy_vii) · ✅ (recuento directo de la web, verificable por cualquiera)
- Contraste: en la encuesta oficial de Famitsu manda Cloud con ventaja clara; en el recuento de fan art manda Tifa. Es justo el caso que pide ENCARGO.md («a veces no es el protagonista» — aquí es más matiz: la más dibujada no es el que más vota en encuestas oficiales, y viceversa) · ✅

## 8 · Doblaje latino y quién dobla a cada uno

**No hay doblaje latino oficial de ningún Final Fantasy VII** (juego original, Remake, Rebirth ni la película Advent Children). Comprobado en Doblaje Wiki por su API: no existe página para «Final Fantasy VII», «Final Fantasy VII Remake», «Final Fantasy VII Rebirth» ni «Advent Children» (`action=parse` da error «missingtitle»), y una búsqueda de texto (`action=query&list=search`) por «Final Fantasy VII» y por «Advent Children» tampoco encuentra ninguna ficha de esos títulos. Doblaje Wiki sí confirma que **Final Fantasy XVI (2023) es el primer juego de toda la franquicia doblado al español y el primero para Latinoamérica** (dato ya recogido en `datos-voz.md`, ficha de Keywords Studios dirigida por Mario Heras) · [Doblaje Wiki, ficha de Final Fantasy XVI](https://doblaje.fandom.com/es/wiki/Final_Fantasy_XVI) y comprobación negativa propia sobre FFVII/Remake/Rebirth/Advent Children vía `api.php` (dos consultas independientes: `action=parse` página por página y `action=query&list=search`) · ✅
- Tampoco hay doblaje latino de Cloud/Sephiroth/Aerith en sus apariciones fuera de FFVII: revisadas las fichas de Doblaje Wiki de Kingdom Hearts III (sólo aparecen actores de Disney) y ninguna ficha para «Final Fantasy VII Ever Crisis»; los nombres latinos que aparecían al buscar «Ever Crisis» eran coincidencia con la palabra «Crisis» en títulos de otras series (comprobado abriendo cada ficha) · [Doblaje Wiki, búsqueda]·✅
- Con esto, la tabla pedida se rellena con **seiyū (japonés) y voz en inglés**, que es lo único doblado, cada nombre con dos fuentes (wiki de Final Fantasy + Behind The Voice Actors):

| Personaje | Seiyū (JP) | Voz latina | Fuente 1 | Fuente 2 |
|---|---|---|---|---|
| Cloud Strife | Takahiro Sakurai | No hay doblaje latino oficial (voz en inglés: Steve Burton, juego/Advent Children; Cody Christian, Remake/Rebirth) | [Final Fantasy Wiki](https://finalfantasy.fandom.com/wiki/Cloud_Strife) | [BTVA](https://www.behindthevoiceactors.com/characters/Final-Fantasy/Cloud-Strife/) |
| Tifa Lockhart | Ayumi Ito | No hay doblaje latino oficial (inglés: Rachael Leigh Cook, juego/AC; Britt Baron, Remake/Rebirth) | [Final Fantasy Wiki](https://finalfantasy.fandom.com/wiki/Tifa_Lockhart) | [BTVA](https://www.behindthevoiceactors.com/characters/Final-Fantasy/Tifa-Lockhart/) |
| Aerith Gainsborough | Maaya Sakamoto | No hay doblaje latino oficial (inglés: Mena Suvari, AC/KH; Andrea Bowen, Crisis Core/Dissidia; Briana White, Remake/Rebirth) | [Final Fantasy Wiki](https://finalfantasy.fandom.com/wiki/Aerith_Gainsborough) | [BTVA](https://www.behindthevoiceactors.com/characters/Final-Fantasy/Aerith-Gainsborough/) |
| Sephiroth | Toshiyuki Morikawa | No hay doblaje latino oficial (inglés: George Newbern, Crisis Core/AC/Dissidia/Remake) | [Final Fantasy Wiki](https://finalfantasy.fandom.com/wiki/Sephiroth) | [BTVA](https://www.behindthevoiceactors.com/characters/Final-Fantasy/Sephiroth/) |
| Barret Wallace | Masahiro Kobayashi (Mahito Funaki en Rebirth) | No hay doblaje latino oficial (inglés: John Eric Bentley, Remake/Rebirth; Beau Billingslea, Compilation clásica) | [Final Fantasy Wiki](https://finalfantasy.fandom.com/wiki/Barret_Wallace) | [BTVA](https://www.behindthevoiceactors.com/characters/Final-Fantasy/Barret-Wallace/) |
| Red XIII | Kappei Yamaguchi (Remake) | No hay doblaje latino oficial (inglés: Max Mittelman, Remake; Liam O'Brien, Advent Children) | [Final Fantasy Wiki](https://finalfantasy.fandom.com/wiki/Red_XIII) | [Final Fantasy Wiki (ficha EN, ref. Square Enix)](https://finalfantasy.fandom.com/wiki/Red_XIII) |
| Vincent Valentine | Shōgo Suzuki | No hay doblaje latino oficial (inglés: Steve Blum, clásico; Matthew Mercer, Remake, confirmado por la cuenta oficial de X @finalfantasyvii) | [Final Fantasy Wiki](https://finalfantasy.fandom.com/wiki/Vincent_Valentine) | [X/Twitter oficial @finalfantasyvii](https://twitter.com/finalfantasyvii/status/1713280182822605237) |

- Frases del doblaje latino textuales: **no aplica**, porque no existe doblaje latino de ningún FFVII (ver arriba). No hay clip oficial doblado que citar con minuto.

## Sigue de esta parte

Faltan por escribir: 12, 13, 20, 21 y 22 (en curso). Guardo lo hecho ahora por si hay corte.
