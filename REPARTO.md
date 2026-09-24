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

## Qué pegar en cada cuenta

> Lee REPARTO.md. Eres el **lote X**. Corre `herramientas/juntar.sh` y `echo X > .lote`, instala lo de la skill serie-en-equipo y sigue con ella sólo con tu lote (`python3 herramientas/siguiente.py 5 --lote X`), en cadena. No toques ESTADO.md, DECISIONES.md, COSTOS.md ni TANDAS.md: tu estado, tus avisos para el dueño y tus costos van en `lotes/X.md`.

(cambia X por la letra). Después escribe `/model sonnet` en esa sesión.

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
