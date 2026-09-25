# REPARTO — varias cuentas a la vez, cada una con su lote

Para acortar tiempos: cada cuenta trabaja **un lote** de series en paralelo con
las demás. El costo total es el mismo; lo que baja es el tiempo. Cada biblia
vive en su carpeta, así que las ramas de las cuentas se juntan sin chocar.

| Lote | Series | Qué son | Cuentas de 100 dólares, aprox. |
|---|---|---|---|
| **A** (la central) | 02-05, 31-36 | casi completas (repaso corto) y One Punch Man / Hunter x Hunter | 2 |
| **B** | 06-18 | repasos | 3 |
| **C** | 19-30 | repasos | 3 |
| **D** | 37-56 | series nuevas | 6 |
| **E** | 57-76 | series nuevas | 6 |
| **F** | 77-96 | series nuevas | 6 |
| **G** | 97-116 | series nuevas (películas y occidentales) | 6 |
| **H** | 117-131 | videojuegos | 5 |
| **T** | temas A-P | 96 temas | aún no: falta adaptar el sistema a temas |

Una sola cuenta por lote a la vez (si no, harían lo mismo dos veces). Cuando una
cuenta se queda sin saldo, la siguiente sigue **el mismo lote**.

## Cómo arranca un lote

**En GitHub** (lo normal, ver README): `.github/workflows/lote.yml` lanza el
motor con la letra; el motor crea o sigue la rama `claude/lote-<l>-local`,
corre `juntar.sh`, pone `.lote` y le da al jefe su mensaje. No hay que pegar
nada.

**En una sesión suelta** (nube o PC con la Max, sin motor): ver LOCAL.md. Antes,
quita la letra de `.github/lotes-activos`: dos jefes en un lote hacen el
trabajo dos veces.

## Reglas de un lote

- Sólo toca `biblias/<sus series>/` y `lotes/<su letra>.md`.
- `subir.sh` ve el archivo `.lote` y no marca TANDAS.md (lo marca la central al juntar).
- Al empezar, `herramientas/juntar.sh` trae el trabajo de todas las cuentas: así
  la cuenta nueva de un lote sigue desde lo que dejó la anterior, sin saber el
  nombre de su rama.

## La central (lote A)

De vez en cuando corre `herramientas/juntar.sh --marcar`: junta todas las ramas,
marca en TANDAS.md las biblias COMPLETAS y copia a DECISIONES.md, ESTADO.md y
COSTOS.md lo que traigan los `lotes/*.md`.
