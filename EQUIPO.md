# EQUIPO — una serie la hace un equipo, y sólo el redactor escribe la biblia

Sustituye a «un ayudante por encargo» para las series nuevas y los repasos.
Siguen valiendo `ENCARGO.md` (qué tiene que tener una biblia), `AYUDANTE.md`
(reglas del contenedor, herramientas de red, mirar vídeos) y `COMPLEMENTO.md`
(repasos).

## El método económico (desde el 24-sep-2026)

Misma exigencia de `ENCARGO.md`, bastante menos gasto. Lo lleva la skill
`serie-en-equipo`, que funciona sola de serie en serie.

| Paso | Quién | Modelo | Qué |
|---|---|---|---|
| 0 | `herramientas/recolectar.py <id> --hojas` | ninguno (gratis) | junta los datos de 13 fuentes en `partes/datos-*.md` y `datos.json`, y las hojas de contacto |
| 1 | 4 investigadores (imagen, video, voz, texto) | **Sonnet** | parten de su `datos-<rol>.md`; leen sólo sus secciones con `seccion.py`; tandas de ~70 acciones con `Sigue:` |
| 2 | redactor | **Opus** | escribe o edita la biblia con las partes; la calidad final es suya |
| 3 | jefe | el de la sesión | `revisar.py`; lo que falte, al investigador de ese punto; `subir.sh` |

**Repaso corto** (biblias a las que sólo faltan los puntos 18-25): sólo 3
investigadores, cada uno con sus puntos nuevos: imagen (19, 23), voz (20, 21,
22) y texto (18, 24, 25). El de vídeo no hace falta.

**No usar el equipo de 8** salvo que el dueño lo pida: el piloto de One Piece
gastó unos 65 dólares en 25 minutos sin terminar.

## Quién hace qué

| Quién | Qué hace | Dónde escribe |
|---|---|---|
| **Sesión principal** (jefe) | Lanza el equipo, revisa y sube. No investiga. | `DECISIONES.md`, `TANDAS.md` (con `subir.sh`) |
| **Investigador de imagen** | Puntos 1, 3, 15, 16, 19 y 23 de ENCARGO.md: arte oficial, fan art y 3D con licencia, vestuario con hex medidos, fondos de pantalla, texturas 2D, colaboraciones y su arte. Hojas de contacto con `investigar_serie.py`. | `partes/imagen.md`, `partes/imagen.json`, `hojas/` |
| **Investigador de vídeo** | Puntos 2, 4, 9, 10 y 14: opening, ending, tráiler y escenas mirados con `fotogramas.py`; poses con capítulo y minuto; luz y paleta de los sitios medida en fotogramas; música. | `partes/video.md`, `partes/video.json` |
| **Investigador de voz y personajes** | Puntos 7, 8, 12, 13, 20, 21 y 22: encuestas de popularidad, doblaje latino (dos fuentes por nombre), frases textuales de clips oficiales doblados, carácter y forma de hablar, gustos de cada personaje, por qué la aman, fan dubs en español, lo que ama el fandom y qué no hacer. | `partes/voz.md` |
| **Investigador de texto, juegos y técnica** | Puntos 5, 6, 11, 18, 24 y 25: tipografías y su letra libre (tildes, ñ, ¿, ¡ comprobados con fontTools), cuadros de diálogo de manga, cartelas y videojuegos, interfaces, estilo de dibujo y cómo replicarlo en Photoshop y Blender, obras parecidas, el mundo y sus símbolos. Fuentes en japonés, coreano o chino, TCRF y Wayback. | `partes/texto.md`, `partes/texto.json` |
| **Redactor** | Lee todas las partes, el encargo, `servidor/reglas_del_dueno.md`, `servidor/inventario.md` y `DECISIONES.md`, y escribe **él solo** la biblia: los 25 puntos (el 17, guía para IA de imagen y de texto, lo hace él), los 3 conceptos, la tabla de cumplimiento y la bitácora. Junta las referencias en `referencias.json` (todas las útiles de las partes, mínimo 20, sin máximo) y deja 3 hojas. | `biblia.md`, `referencias.json` |

Cada uno escribe **sólo en sus archivos**. Nadie más que el redactor toca
`biblia.md`, así nadie pisa el trabajo de otro.

## Equipo de 8 (caro: sólo si el dueño lo pide)

Cada rol se parte en dos; cada uno con su archivo `partes/<rol>.md` y `.json`:

| Rol | Puntos de ENCARGO.md |
|---|---|
| `arte` | 1 arte oficial variado, 15 vestuario con hex medidos, 16 fondos de pantalla; hojas de contacto |
| `fanart-3d` | 3 fan art y 3D con licencia, 19 texturas 2D, 23 colaboraciones y cruces |
| `escenas` | 2 fotogramas de escenas icónicas, 14 poses analizadas con minuto |
| `musica-videos` | 4 sitios con luz y paleta medida, 9 música, 10 vídeos y tendencias con minuto |
| `doblaje` | 8 doblaje latino y frases textuales, 22 fan dubs y comunidad hispana |
| `personajes` | 7 popularidad, 12 fandom y qué no hacer, 13 carácter y forma de hablar, 20 gustos, 21 por qué la aman |
| `dialogos` | 5 tipografía, 6 cuadros de diálogo, 11 videojuegos |
| `tecnica-mundo` | 18 estilo y cómo replicarlo, 24 obras parecidas, 25 mundo y símbolos |

## Cómo escribe cada investigador su parte

- Es una libreta de datos, no prosa bonita. Un dato por línea:
  `- dato · fuente(s) con enlace · ✅ (dos fuentes) o ⚠️ (una) · minuto o tamaño si aplica`
- Secciones fijas: **Hallazgos** (por punto de ENCARGO.md), **Lo mejor para la
  lámina** (5 líneas como mucho), **No encontré** (con las búsquedas hechas) y
  **Bitácora** (búsquedas con idioma y fuentes).
- `partes/<rol>.json`: referencias candidatas con los mismos campos que
  `referencias.json` (`url`, `fuente`, `ancho`, `alto` medidos, `que_es`,
  `para_que`, `licencia`).
- Guarda tras cada punto (el límite de uso puede cortarte). Si ya existe tu
  parte, sigue desde donde quedó.
- Cada investigador tiene su propio cupo de ~50 búsquedas web: el equipo busca
  cuatro veces más que un ayudante solo.
- Al terminar contesta en 3 líneas: cuántos datos y fuentes, lo mejor que
  encontró y lo que no pudo hacer.

## El orden

1. El jefe lanza los **4 investigadores a la vez** para una serie (como mucho 2
   series a la vez: 8 agentes).
2. Cuando terminan los 4, lanza al **redactor**.
3. El jefe corre `python3 herramientas/revisar.py <id>` y lee **sólo la tabla
   de cumplimiento**. Si falta algo, se lo pide por SendMessage **al
   investigador de ese punto** (conserva su contexto, sale más barato) y luego
   al redactor para que lo meta.
4. Cuando dice COMPLETA: `herramientas/subir.sh <id>` (o `<id> repaso`), y
   copia a `DECISIONES.md` lo que el dueño tenga que decidir u oír.

## En un repaso

Los investigadores leen primero las secciones de la biblia que les tocan y sus
⚠️ (`grep -n '⚠️' biblia.md`), y trabajan sobre eso. El redactor **edita en su
sitio** siguiendo `COMPLEMENTO.md` (no reescribe lo que está bien) y añade
«Segunda pasada · qué cambió».

## `partes/` se queda en el repositorio

Son la memoria de la investigación: el siguiente repaso parte de ahí en vez de
buscar de cero. `guardar.sh` las sube a medias y `subir.sh` las acepta.
