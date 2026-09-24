---
tags: [biblia, serie, laminas]
serie: "Attack on Titan (Shingeki no Kyojin)"
canal: "#reglas"
fecha: 2026-09-23
---

# Biblia · Attack on Titan (para #reglas)

> [!abstract] Qué es
> La investigación que hay detrás de la lámina de #reglas (23-sep-2026, noche).
> Él notó que esta vez se investigó más que en las otras y **pidió el mismo nivel
> para todas**: renders 3D, manga, cómic, vídeos y tráilers, fan art, estilos,
> letras, texturas, personalidad, fondos, poses, colores y ropa.
> La lámina: `herramientas/laminas_v2/v3/reglas_aot.html` → `reglas_aot-reglas.jpg`.

## 1 · Material reunido y dónde está

| Qué | Dónde | Cuánto |
|---|---|---|
| Imágenes de la wiki (personajes, Legión, murallas, distritos, equipo de maniobras…) | `v3/referencias/attack-on-titan/hoja_01-04.jpg` | 192 |
| Galerías grandes (Levi, Erwin, Zackly, Keith, Nile, Petra, Eren, castillo de la Legión) | `v3/referencias/attack-on-titan-galerias/hoja_01-14.jpg` | 673 |
| Emblemas (Legión, Guarnición, los tres en piedra) | `v3/referencias/attack-on-titan/emblemas/` | 6 |
| Tráiler oficial T1 de Pony Canyon (WIT) + clip del ep. 16 | `_vistas/aot/*.mp4`, hojas de fotogramas `pv_s1_hoja.jpg`, `ep16_hoja.jpg` | 2 vídeos |
| Lo que vio Gemini en esos vídeos (revisado) | `_vistas/aot/gemini_videos.txt` | — |

Para mirar de cerca unas cuantas de una hoja: `python v3/ver_indices.py <carpeta> <salida.jpg> N N N`
(la hice esta vez; enseña la miniatura grande con su número, tamaño y título).

## 2 · Lo que sirve de la serie

- **«Al quedarte, las aceptas»** (el tema del canal) es literalmente el **episodio 16**:
  Erwin les dice a los cadetes que quien se quede en el patio será soldado de la
  Legión; de noche, con antorchas, y los que se quedan hacen **el saludo**: puño
  derecho al corazón, izquierdo a la espalda (*Shinzō wo sasageyo*, «entregad
  vuestros corazones»). Es la lámina de **aceptar** (el ✅), si se hace.
- **El juicio de Eren (ep. 14)**: tribunal militar, Zackly de juez, Eren
  encadenado de rodillas a un poste; Levi le da una paliza «porque el dolor es la
  mejor disciplina» — y lo hace para salvarlo. Es el sitio de la **lámina 2**
  («qué pasa si no se cumplen»). Fotogramas: galerías nº 129, 255, 256, 459, 40, 300.
- **Levi** (ficha de la wiki, «Personality»): obsesionado con la limpieza (limpia
  hasta las hojas en pleno campo de batalla), habla seco y cortante, casi no
  enseña emoción, humor negro; odia las bajas inútiles y deja decidir a los suyos.
  Frase de la lámina, original en su forma de hablar: «Tch. Son ocho. Se cumplen.
  Y el canal, limpio.»
- **La escritura de dentro de las murallas es katakana del revés**: los fans lo
  descifraron dando la vuelta a la página (Anime News Network, 13-may-2014). En la
  estela va «シンゾウヲササゲヨ» girado 180°: quien lo sepa, lo lee.
- **Los emblemas del ejército se representan en relieve de piedra** en el propio
  anime (`emblemas/Military.png`): por eso el escudo va tallado.
- **Paleta** (medida en el tráiler de WIT, no en sitios de fans): piedra de la
  Muralla gris crema, capas verde oliva oscuro, cielo azul grisáceo, sangre granate,
  negros cálidos; luz de tarde dorada con sombras frías.
- **Arquitectura**: pueblo centroeuropeo con entramado de madera y tejado rojo
  (Trost, Shiganshina); la Muralla, bloques enormes y lisos.
- **Nombres alemanes** por todas partes (Trost, Karanes, *Die Flügel der Freiheit*).

## 3 · Doblaje latino (comprobado en la ficha de la serie Y en la del actor)

Doblaje Wiki por la API (`action=parse`): C&G Dubbing Studio / Artworks Digital
Studio, dirección **Gerardo Ortega**, 2020-2024, para Funimation y Crunchyroll.

| Personaje | Voz | De paso |
|---|---|---|
| Levi | **Alfredo Gabriel Basurto** | también Sesshomaru y Zoro |
| Erwin | **Octavio Rojas** | Smithers en Los Simpson |
| Keith Shadis | Carlos Segundo | Piccolo |
| Darius Zackly | Rubén Moya (antes José Luis Portela) | — |
| Dot Pixis | Francisco Reséndez | — |
| Nile Dawk | Saúl Alvar | — |
| Armin (y narrador) | Héctor Ireta de Alba | — |

## 4 · 3D, texturas y letras

- **Sketchfab, revisados** (todos CC BY, crédito obligatorio si se usan): equipo de
  maniobras de Tipperman (`47a69e5640c34e42b1cf56ceff7fb5d4`) y de marthacuenca
  (`254eb3c6…`), pistola de bengalas de Nelesh_surve (`b375de9d…`), escudo de la
  Legión en 3D de Yanez-Designs (`8812126a…`), Titán Colosal de MauricioFlores
  (`eea5f373…`), cañón de skipperino (`7bacac0f…`). El «Torhaus» (puerta de la
  muralla) es pobre: no vale. **Usados en #reglas: ninguno** — la estela se modeló
  (es una caja) y el escudo salió del PNG de la wiki como mapa de alturas.
- **Poly Haven (CC0)**: `sandstone_blocks_08` (la Muralla: bloques grandes y
  lisos, lo más parecido al anime), `sandstone_blocks_04` (la estela),
  `cobblestone_pavement`. En `v3/blender/tex/`.
- **Letras**: Cinzel (la inscripción, como las romanas cinceladas) + Cormorant
  Garamond (el texto corrido, con minúsculas para que se lea) + Anime Ace (el
  bocadillo). La fuente del alfabeto de la serie en FontStruct («Eldiglyphs») pide
  cuenta: no se usó; el katakana del revés es más fiel.

## 5 · Las tres láminas del canal

1. ✅ **Las ocho reglas** — estela tallada al pie de la Muralla (hecha).
2. ⬜ **Qué pasa si no se cumplen** — el tribunal del ep. 14: el poste de los
   grilletes, el estrado de Zackly, la escala de sanciones como la sentencia
   (aviso → Silenciado → expulsión → baneo; lo grave, directo; se apunta en
   log-mod; se puede discutir por soporte). **La escala exacta es propuesta: falta
   su sí** antes de publicarla.
3. ⬜ **Aceptar** (el ✅) — el saludo del ep. 16 (fotograma 4K de la wiki,
   galerías nº 6).
