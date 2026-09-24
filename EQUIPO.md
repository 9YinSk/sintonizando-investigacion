# EQUIPO — una serie la hace un equipo, y sólo el redactor escribe la biblia

Sustituye a «un ayudante por encargo» para las series nuevas y los repasos.
Siguen valiendo `ENCARGO.md` (qué tiene que tener una biblia), `AYUDANTE.md`
(reglas del contenedor, herramientas de red, mirar vídeos) y `COMPLEMENTO.md`
(repasos).

## Quién hace qué

| Quién | Qué hace | Dónde escribe |
|---|---|---|
| **Sesión principal** (jefe) | Lanza el equipo, revisa y sube. No investiga. | `DECISIONES.md`, `TANDAS.md` (con `subir.sh`) |
| **Investigador de imagen** | Puntos 1, 3, 15 y 16 de ENCARGO.md: arte oficial, fan art y 3D con licencia, vestuario con hex medidos, fondos de pantalla. Hojas de contacto con `investigar_serie.py`. | `partes/imagen.md`, `partes/imagen.json`, `hojas/` |
| **Investigador de vídeo** | Puntos 2, 4, 9, 10 y 14: opening, ending, tráiler y escenas mirados con `fotogramas.py`; poses con capítulo y minuto; luz y paleta de los sitios medida en fotogramas; música. | `partes/video.md`, `partes/video.json` |
| **Investigador de voz y personajes** | Puntos 7, 8, 12 y 13: encuestas de popularidad, doblaje latino (dos fuentes por nombre), frases textuales de clips oficiales doblados, carácter y forma de hablar, lo que ama el fandom y qué no hacer. | `partes/voz.md` |
| **Investigador de texto y juegos** | Puntos 5, 6 y 11: tipografías y su letra libre (tildes, ñ, ¿, ¡ comprobados con fontTools), cuadros de diálogo de manga, cartelas y videojuegos, interfaces. Fuentes en japonés, coreano o chino, TCRF y Wayback. | `partes/texto.md`, `partes/texto.json` |
| **Redactor** | Lee todas las partes, el encargo, `servidor/reglas_del_dueno.md`, `servidor/inventario.md` y `DECISIONES.md`, y escribe **él solo** la biblia: los 17 puntos (el 17, guía para IA, lo hace él), los 3 conceptos, la tabla de cumplimiento y la bitácora. Junta las referencias en `referencias.json` (20-40) y deja 3 hojas. | `biblia.md`, `referencias.json` |

Cada uno escribe **sólo en sus archivos**. Nadie más que el redactor toca
`biblia.md`, así nadie pisa el trabajo de otro.

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
