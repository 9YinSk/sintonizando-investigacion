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

(cambia el número por el que toque). Hay **29 encargos** en `encargos/`.

## Cómo se junta

Cada sesión deja su trabajo en su propia rama. En la PC, un chat trae todas las
ramas, revisa cada dossier y lo copia a la bóveda de Obsidian
(`00-Bandeja/Biblias de series/`).

## Qué hay aquí

- `ENCARGO.md` — las instrucciones completas para cada sesión.
- `encargos/` — un encargo por serie (qué canal, qué objeto, qué personajes).
- `servidor/` — qué hay en cada canal y foro, y lo que el dueño ha rechazado o le gustó.
- `biblias/_ya_hechas/` — ejemplos del nivel que se espera.
- `herramientas/` — el script que baja las imágenes de las wikis y monta hojas de contacto.
- `armar_kit.py` — regenera todo esto desde la PC si cambia el reparto.
