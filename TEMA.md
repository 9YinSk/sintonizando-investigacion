# ENCARGO DE TEMA — volverse experto en un tema, para sus proyectos

Eres una sesión de Claude Code en la nube. Tu trabajo es **investigar un tema a
fondo** y dejar un informe que otra sesión, en su PC, usará para trabajar como
experta. Lee `contexto/proyectos.md`: son los proyectos del dueño, y todo lo que
investigues tiene que servirle a alguno de ellos.

## Qué investigar (con detalle concreto, fechas y fuentes; nada genérico)

1. **El estado del arte en 2026**: qué se usa hoy de verdad, qué cambió en el
   último año, qué quedó viejo. Con fecha de cada dato.
2. **Herramientas**: programas, servicios, modelos, repositorios de GitHub,
   skills y servidores MCP de Claude. Para cada una: qué hace, precio o
   licencia, si corre en Windows con una RTX 4060 Ti de 8 GB, y si toca red o
   pide claves. Marca las gratuitas.
3. **Cómo se hace, paso a paso**: los flujos de trabajo que usan los
   profesionales, con los comandos o menús concretos.
4. **Trampas y errores comunes**: lo que falla y cómo se evita.
5. **Referentes**: profesionales, canales de YouTube, cursos, comunidades,
   sobre todo **hispanohablantes y latinoamericanos**, con enlace.
6. **Ejemplos buenos**: casos reales que funcionaron y por qué.
7. **Cómo se aplica a SUS proyectos**: qué haría un experto con lo que él tiene
   (ver `contexto/proyectos.md`); ideas concretas, ordenadas por impacto.
8. **Lo que no se puede o no conviene**: límites legales, de licencias o de
   plataforma, para no perder tiempo.

Verifica lo importante en dos fuentes. Si algo no lo pudiste confirmar, dilo.

## Dónde dejarlo

En `investigaciones/<tu-tema>/`, sin tocar otras carpetas:
- `informe.md`: el informe completo, en español, **claro para leer en el
  celular**, con índice arriba y fuentes enlazadas.
- `recursos.json`: las herramientas y fuentes, cada una con `nombre`, `url`,
  `tipo`, `precio`, `licencia` y `para_que`.

Al terminar, commit y push **de tu rama**. No toques `main` ni otras carpetas.
No instales nada fuera de la sesión ni publiques nada en ningún sitio.
