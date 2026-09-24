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

**Cada encargo:** en una sesión nueva en la nube, con este repositorio, escribe:

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

## Cómo se junta

Cada sesión deja su trabajo en su propia rama. En la PC, un chat trae todas las
ramas, revisa cada dossier y lo copia a la bóveda de Obsidian
(`00-Bandeja/Biblias de series/`).

## Qué hay aquí

- `ENCARGO.md` — las instrucciones completas para cada sesión.
- `AYUDANTE.md` — cómo trabaja cada ayudante de una tanda (red, herramientas, guardar por partes).
- `COMPLEMENTO.md` — la segunda pasada de las biblias 01-25, hechas con la red cerrada.
- `herramientas/subir.sh` — sube el trabajo de un ayudante y marca su casilla.
- `encargos/` — un encargo por serie (qué canal, qué objeto, qué personajes).
- `TEMA.md`, `temas/` y `contexto/proyectos.md` — los encargos de temas y el resumen de tus proyectos.
- `MAPA.md` — todo lo que se investiga, por bloques.
- `catalogo.py` — la lista de temas y series nuevas: se añade una línea y se corre `armar_kit.py`.
- `TANDAS.md` — los 72 encargos en 18 tandas de 4, con la frase lista para pegar.
- `servidor/` — qué hay en cada canal y foro, y lo que el dueño ha rechazado o le gustó.
- `biblias/_ya_hechas/` — ejemplos del nivel que se espera.
- `herramientas/` — el script que baja las imágenes de las wikis y monta hojas de contacto.
- `armar_kit.py` — regenera todo esto desde la PC si cambia el reparto.
