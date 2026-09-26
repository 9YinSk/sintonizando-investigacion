# Parte de TEXTO, JUEGOS Y TÉCNICA · Death Note (repaso, 26-sep-2026)

Investigador de texto: puntos 5, 6, 11, 18, 24 y 25 de `ENCARGO.md`. La
biblia ya tiene los puntos 5, 6 y 11 con bastante detalle (secciones
«6 · Tipografía», «7 · Cómo hablan y piensan en pantalla» y
«13 · Videojuegos de la franquicia», numeración vieja de `biblia.md`, hecha
con la red cerrada). Este repaso corto **confirma lo dudoso de esos tres y
cubre a fondo los tres que faltan del todo: 18, 24 y 25**. Parte de
`partes/datos-texto.md` (AniList: obra, equipo creativo, obras parecidas y
relacionadas, capturas de Steam) sin repetir esas consultas.

Leyenda: ✅ dos fuentes (o algo que comprobé yo mismo) · ⚠️ una fuente o dudoso.

No hay serie hermana en `encargos/18-death-note.md`.

---

## Hallazgos

### Puntos 5, 6 y 11 · Verificación de lo que ya hay en la biblia

**Punto 5 (Tipografía) — bajé y comprobé las letras yo mismo con fontTools** (antes sólo se afirmaba comprobado; ahora es real, con los archivos descargados de Google Fonts, no de memoria):

- **UnifrakturMaguntia**, **IM Fell English**, **Special Elite**, **Zeyada**, **Nothing You Could Do**, **Kalam**, **Nosifer**, **Pirata One**, **Grenze Gotisch**, **UnifrakturCook**: las 10 traen á é í ó ú ñ Á É Í Ó Ú Ñ ¿ ¡ ü · comprobado con `fontTools.ttLib.TTFont(...).getBestCmap()` sobre los `.ttf` reales bajados de `fonts.gstatic.com` (24-sep-2026) ✅ (verificación propia)
- **Butcherman**: confirmado que **le falta el ¿** (igual que decía la biblia) ✅ (verificación propia con fontTools)
- Para el japonés del logo y las pausas: **Shippori Mincho B1** y **Zen Old Mincho** traen katakana (デスノート) y los kanji de prueba (死神使い方神様) completos · comprobado con fontTools ✅ (verificación propia)
- Para una interfaz o subtítulo en **coreano o chino** (la letra libre que pide `AYUDANTE.md` en esos idiomas; el juego *Killer Within* tiene textos en coreano y chino tradicional, ver punto 11 abajo): **Noto Sans KR** (hangul 데스노트 completo) y **Noto Sans SC** (hanzi 死亡笔记 completo), las dos OFL, gratis y con carácter neutro que no rompe el tono de la lámina · comprobado con fontTools ✅ (verificación propia)
- Sigue sin comprobar la licencia exacta de «**Death Font**» (imitación del logo, de joshua1985): lo intenté en dafont.com y fontbolt.com, las dos dieron error de conexión con `curl` y con `navegar.py` no cargó el detalle de licencia en el tiempo dado ⚠️ (no resuelto; recomiendo generar el logo con **UnifrakturMaguntia** o **UnifrakturCook**, que sí están 100% libres y ya comprobadas, en vez de depender de una fuente de dafont sin licencia clara)

**Punto 6 (cuadro de diálogo) y punto 11 (videojuegos)**: el contenido de la
biblia (globo del manga inexistente, «HOW TO USE IT», pantalla blanca con la
«L» gótica, monólogo interior, tabla de cómo habla cada personaje) está bien
armado y con minuto; no hace falta reescribirlo. Lo completo con la interfaz
real de **Killer Within** en el apartado del punto 11 más abajo (por eso no
lo repito aquí).

---

### Punto 18 · Estilo de dibujo y técnica, y cómo replicarlo

**rigs y tramas: ver puntos 3 y 19** (los trae el investigador de imagen).

