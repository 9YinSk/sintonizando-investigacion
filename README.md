# Investigación de las láminas, en la nube

Cada sesión de Claude en la nube investiga **una serie a fondo** (arte oficial,
fotogramas, fan art, 3D, fondos, texturas, letras, cuadros de diálogo,
personajes y secundarios, doblaje latino, música, vídeos, juegos) y deja su
dossier aquí. Después, un chat en la PC lo junta todo y hace las láminas.

## Cómo se usa (desde el celular o la PC)

**La primera vez en cada cuenta** (una sola vez):
1. Abre Claude → **Code** → nueva sesión en **Cloud**. Te pedirá **conectar
   GitHub**: entra con tu cuenta `9YinSk`.
2. Elige este repositorio: **`9YinSk/sintonizando-investigacion`**.
3. En el entorno (el icono de la nube), pon **Network access → Full**. Sin eso
   no puede entrar a las wikis ni a YouTube.

**Lo más fácil (desde el 24-sep-2026):** en una sesión nueva en la nube, con este
repositorio, escribe:

> Lee ESTADO.md y sigue con la skill serie-en-equipo.

La sesión va sola de serie en serie: el recolector junta los datos gratis, 4
investigadores (Sonnet) investigan, un redactor (Opus) escribe la biblia, se
revisa y se sube. Cuánto cuesta cada una queda en `COSTOS.md`.

**Un encargo suelto:** en una sesión nueva en la nube, con este repositorio, escribe:

> Haz el encargo `encargos/05-oshi-no-ko.md` siguiendo `ENCARGO.md`.

(cambia el número por el que toque).

**Mejor por tandas de 4:** abre `TANDAS.md`, copia la frase de la tanda que toque
y pégala en una sesión nueva; la sesión hace los cuatro a la vez con ayudantes.
- **Tandas S1-S33**: 131 series, películas y videojuegos (las 29 primeras son los
  canales del servidor).
- **Tandas A1-P1**: 96 temas para volverse experto, en 16 bloques (diseño,
  personajes, VTubers, voz y doblaje, radio, redes, Discord, IA, webs y apps,
  edición, negocio y becas, Asia, PC, Minecraft, videojuegos, recursos).

**Todo ordenado en `MAPA.md`.**

## Los lotes en GitHub (con la suscripción Max)

Los lotes de series (REPARTO.md: D, E, F, G y H) corren solos en máquinas de
GitHub Actions, 5 horas y 20 minutos por vuelta, encadenando vueltas mientras su
letra esté en `.github/lotes-activos`. Cada lote trabaja en su rama
`claude/lote-<letra>-local` y apunta su estado en `lotes/<letra>.md`.

**Una sola vez:** en la PC, doble clic en **MAX EN GITHUB** (en el escritorio):
entra con la cuenta Max, copia el pase (`sk-ant-oat…`) y pégalo cuando pida
«Pase:». Eso lo guarda en GitHub como el secreto `CLAUDE_CODE_OAUTH_TOKEN` (vale
un año). Sin ese secreto los lotes no arrancan: el run avisa y no hace nada más.
Si el pase deja de valer, el run falla con un aviso claro; se repite el doble clic.

**Cuántos a la vez:** con la Max de 5x, tres letras en `.github/lotes-activos`
(G, E y D, ya puestas); con la de 20x, las cinco (añade F y H, una por línea).
Poner más lotes no hace más trabajo: la cuenta tiene un límite de uso cada
5 horas y otro semanal, y todos los lotes lo comparten.

**Arrancar:** solos, en el siguiente cron (cada 3 horas, al minuto 23), o ahora
mismo en la pestaña **Actions → Lote con la Max → Run workflow** (con la letra
vacía lanza todos los de la lista).

**Ver cómo va:** en Actions, cada run muestra la pantalla del jefe cada 10
minutos y, al terminar, qué subió y cuántos tokens gastó cada modelo. Lo hecho
queda en la rama de cada lote y en `lotes/<letra>.md`.

**Parar:** quita la letra de `.github/lotes-activos` (la vuelta en curso termina y
no se lanza otra) o cancela el run en Actions. Un lote que acaba sus series
escribe «LOTE X TERMINADO» en su `lotes/X.md` y se quita solo de la lista.

**El límite de la Max:** con el de 5 horas, Claude Code espera y sigue solo
cuando se recarga. Con el semanal, la vuelta termina, no encadena otra y el cron
lo reintenta cada 3 horas hasta que vuelva a haber cupo.

## Cómo se junta

Cada sesión deja su trabajo en su propia rama. En la PC, un chat trae todas las
ramas, revisa cada dossier y lo copia a la bóveda de Obsidian
(`00-Bandeja/Biblias de series/`).

## Qué hay aquí

- `ENCARGO.md` — las instrucciones completas para cada sesión.
- `.github/workflows/lote.yml` y `herramientas/motor_github.sh` — los lotes en GitHub; `.github/lotes-activos`, qué letras corren.
- `REPARTO.md` y `lotes/` — qué series lleva cada lote y cómo va cada uno.
- `AYUDANTE.md` — cómo trabaja cada ayudante de una tanda (red, herramientas, guardar por partes).
- `COMPLEMENTO.md` — la segunda pasada de las biblias 01-25, hechas con la red cerrada.
- `EQUIPO.md` — quién hace qué en cada serie y el método económico.
- `ESTADO.md` — dónde va el trabajo y cómo seguir en otro contenedor; `COSTOS.md`, lo que cuesta cada serie.
- `herramientas/recolectar.py` — junta gratis los datos de 13 fuentes para una serie.
- `herramientas/seccion.py` — lee sólo un trozo de una biblia; `siguiente.py` — qué toca ahora.
- `herramientas/revisar.py` — dice si una biblia está completa; `subir.sh` la sube y marca su casilla.
- `encargos/` — un encargo por serie (qué canal, qué objeto, qué personajes).
- `TEMA.md`, `temas/` y `contexto/proyectos.md` — los encargos de temas y el resumen de tus proyectos.
- `MAPA.md` — todo lo que se investiga, por bloques.
- `catalogo.py` — la lista de temas y series nuevas: se añade una línea y se corre `armar_kit.py`.
- `TANDAS.md` — los 72 encargos en 18 tandas de 4, con la frase lista para pegar.
- `servidor/` — qué hay en cada canal y foro, y lo que el dueño ha rechazado o le gustó.
- `biblias/_ya_hechas/` — ejemplos del nivel que se espera.
- `herramientas/` — el script que baja las imágenes de las wikis y monta hojas de contacto.
- `armar_kit.py` — regenera todo esto desde la PC si cambia el reparto.
