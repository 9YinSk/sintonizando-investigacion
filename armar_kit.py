"""Arma el kit de investigación en la nube a partir del plan v4 de láminas.

    python armar_kit.py    → encargos/NN-serie.md, servidor/, biblias/_ya_hechas/, herramientas/

Se vuelve a correr si cambia el reparto: pisa lo generado, no toca biblias/<encargo>/.
"""
import shutil
from pathlib import Path

AQUI = Path(__file__).resolve().parent
YINX = Path(r"C:\Users\Proye\Desktop\YinX")
V3 = YINX / "herramientas" / "laminas_v2" / "v3"
BANDEJA = YINX / "YinX" / "00-Bandeja"

# (serie, wiki de Fandom sugerida —comprobar—, canales y su función, objeto propuesto en el plan v4, personajes clave)
ENCARGOS = [
    ("One Piece", "onepiece", "#bienvenidas: saluda a quien entra y le dice los 4 primeros pasos (Canales y roles, reglas, presentarse, la sala)",
     "carteles de SE BUSCA clavados en la madera del barco, ruta en carta náutica", "Luffy, Nami, Zoro, Sanji, Chopper; ¿quién es el más querido?"),
    ("Attack on Titan", "attackontitan", "#reglas: las normas del servidor y qué pasa si no se cumplen",
     "estela de piedra tallada al pie de la Muralla (ya hay biblia: ampliar, no repetir)", "Levi, Erwin, Hange, Eren, Mikasa"),
    ("Solo Leveling", "solo-leveling", "#guia: foro de 14 hilos que explican el servidor (cada hilo necesita su lámina)",
     "la ventana del Sistema DENTRO de un sitio: puerta de mazmorra, Asociación de Cazadores, ejército de sombras… un sitio por hilo", "Sung Jinwoo, Igris, Beru, Cha Hae-In, el Sistema"),
    ("Harry Potter", "harrypotter", "#anuncios: las novedades oficiales del servidor",
     "El Profeta doblado sobre la mesa (y sus fotos que se mueven)", "Harry, Hermione, Ron, Dumbledore, Luna, Dobby"),
    ("Oshi no Ko", "oshi-no-ko", "#redes-y-novedades (redes del servidor), #en-directo (avisos de directos), #castings (foro de audiciones con ficha)",
     "el móvil de B-Komachi, el letrero ON AIR, la hoja de audición", "Ai, Aqua, Ruby, Kana, Akane, MEM-cho"),
    ("Spy x Family", "spy-x-family", "#presentaciones: foro donde cada uno abre su ficha (Me llamo / Vengo de / Vengo a / Me gusta / Busco / Dato raro) + sus etiquetas",
     "expediente físico de WISE sobre el escritorio de Loid", "Anya, Loid, Yor, Bond, Damian, Becky"),
    ("Pokémon", "pokemon", "#autoroles: cómo elegir tus roles en «Canales y roles» (qué haces, de dónde eres, qué buscas)",
     "la mesa del laboratorio con las Poké Balls: eliges tus roles como tu inicial", "Profesor Oak, Pikachu, Ash, iniciales"),
    ("Big Hero 6 (Grandes Héroes)", "disney", "#soporte: abrir un ticket privado con el staff; la tabla del dolor para decir cuán grave es",
     "Baymax y la tabla del dolor de verdad", "Baymax, Hiro, Tadashi"),
    ("Mafalda", "mafalda", "#sugerencias: foro de propuestas con estados (Nueva, En estudio, Aprobada, Rechazada, Hecha)",
     "tira de periódico de 4 viñetas + buzón", "Mafalda, Felipe, Manolito, Susanita, Libertad, Miguelito"),
    ("K-On!", "k-on", "#general: la sala donde se habla de todo; desde aquí se manda a la gente a los demás canales",
     "la mesa del club con tazas y pastel (Blender)", "Yui, Mio, Ritsu, Mugi, Azusa, Sawako; Mio suele ganar las encuestas"),
    ("Chainsaw Man", "chainsaw-man", "#que-estas-viendo: qué series y pelis está viendo cada uno",
     "butacas de cine y entradas (la cita del ep. 8)", "Denji, Makima, Power, Aki, Pochita"),
    ("Kakegurui", "kakegurui", "#comandos-y-sorteos: los comandos de los bots (juegos, sorteos, economía) — la lista está en servidor/inventario.md",
     "mesa de casino, cartas y fichas", "Yumeko, Kirari, Mary, Ririka"),
    ("Rick and Morty", "rickandmorty", "#noticias-series: noticias de series con su debate",
     "la tele del Cable Interdimensional", "Rick, Morty, Summer, Mr. Meeseeks, Pickle Rick"),
    ("Adventure Time (Hora de aventura)", "adventuretimewithfinnandjake", "#musica-nueva: estrenos musicales",
     "el bajo-hacha de Marceline y sus discos", "Marceline, Finn, Jake, Dulce Princesa"),
    ("SpongeBob (Bob Esponja)", "spongebob", "#ofertas-y-gratis: juegos gratis y rebajas con el precio en soles",
     "la caja registradora del Crustáceo Cascarudo", "Don Cangrejo, Bob, Calamardo, Patricio, Plankton; la voz del narrador francés"),
    ("Neon Genesis Evangelion", "evangelion", "#demos: foro donde cada uno sube su ficha de voz y sus demos (19 etiquetas)",
     "ficha de piloto de NERV", "Asuka, Shinji, Rei, Misato, Gendo, Kaworu"),
    ("Arcane", "arcane", "#proyectos (foro de proyectos con estados) y #arte (foro de piezas: proceso, terminado, acepto encargos)",
     "planos de Hextech sobre la mesa de Jayce y Viktor; la pared de grafiti de Jinx", "Jinx, Vi, Jayce, Viktor, Caitlyn, Ekko, Silco"),
    ("Death Note", "deathnote", "#textos: foro de guiones para practicar (ficha: Tipo, Voces, Duración, Tono, Uso)",
     "el cuaderno sobre la mesa (tono sangriento: lo pidió alguien del servidor)", "Light, L, Ryuk, Misa, Near"),
    ("Doraemon", "doraemon", "#recursos: foro de programas, plantillas, pistas sin voz, efectos (15 etiquetas; nada pirata)",
     "el bolsillo mágico con los artilugios", "Doraemon, Nobita, Shizuka, Gigante, Suneo"),
    ("Dr. Stone", "dr-stone", "#hardware: foro de micrófonos, interfaces y auriculares con el precio delante (rangos de precio)",
     "Senku fabricando un micrófono / el laboratorio", "Senku, Chrome, Gen, Kaseki, Suika"),
    ("Spider-Man: Into/Across the Spider-Verse", "spiderverse", "#edicion: foro de edición (duda, montaje, subtítulos, miniatura…)",
     "viñetas, cajas amarillas de narración, glitch y desfase de impresión", "Miles, Gwen, Peter B., Miguel O'Hara, Hobie"),
    ("Violet Evergarden", "violet-evergarden", "#poemas: foro de poemas, letras, microrrelatos (Libre para usar / No usar sin permiso)",
     "la máquina de escribir con la carta (Blender)", "Violet, Gilbert, Claudia Hodgins, las Auto Memory Dolls"),
    ("Lilo & Stitch", "disney", "#fotos: foro de fotografía (paisaje, retrato, con el móvil, con cámara…)",
     "el álbum de fotos de Lilo (en la película ella hace fotos)", "Lilo, Stitch, Nani, Jumba, Pleakley"),
    ("Assassination Classroom", "assassinationclassroom", "#avisos-clases: horarios y avisos de las clases",
     "la pizarra de Koro-sensei", "Koro-sensei, Nagisa, Karma, Irina"),
    ("My Hero Academia", "myheroacademia", "#material-de-clase: foro donde cada profesor sube su clase (De qué fue / Material / Para practicar)",
     "los cuadernos de análisis de Deku", "Deku, All Might, Bakugo, Todoroki, Uraraka, Aizawa"),
    ("Scooby-Doo", "scoobydoo", "#dudas: foro de dudas técnicas (Resuelta / Sigue abierta)",
     "el tablero de pistas", "Scooby, Shaggy, Vilma, Fred, Daphne"),
    ("Cyberpunk: Edgerunners", "cyberpunk", "#a-que-juegas: a qué juegas, capturas y armar partida con la hora de cada país (ya hay una lámina que le gustó: ampliar referencias)",
     "la recreativa bajo la lluvia de Night City", "Lucy, David, Rebecca, Maine, Kiwi"),
    ("JoJo's Bizarre Adventure", "jojo", "#memes: el meme sin más (si lo doblas, va a fandub de memes) — ya le gustó, «se puede mejorar»",
     "fotograma congelado «To Be Continued» y ficha de Stand", "Jotaro, Dio, Joseph, Giorno, Josuke"),
    ("Por decidir — seis canales sin serie", "", "#destacados, #eventos, #noticias-anime, #noticias-gaming, #general-doblaje, #canto (y las salas de voz: Radio 24/7, Cine, Juegos, Grabación, Mesa de Trabajo, Karaoke, Aula, Escenario)",
     "proponer, para cada uno, la serie más querida por el público latino que encaje con su función, sin repetir las ya usadas", "—"),
]


def slug(t):
    import re
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:40]


def main():
    (AQUI / "encargos").mkdir(exist_ok=True)
    for f in (AQUI / "encargos").glob("*.md"):
        f.unlink()
    for i, (serie, wiki, canal, objeto, pjs) in enumerate(ENCARGOS, 1):
        nombre = f"{i:02d}-{slug(serie)}"
        (AQUI / "encargos" / f"{nombre}.md").write_text(f"""# Encargo {i:02d} — {serie}

Lee primero `ENCARGO.md` (qué investigar y dónde dejarlo). Deja todo en `biblias/{nombre}/`.

- **Serie:** {serie}
- **Canal(es) y su función:** {canal}
- **Objeto que propone el plan (puedes mejorarlo):** {objeto}
- **Personajes para empezar:** {pjs}
- **Wiki de Fandom sugerida (compruébala):** `{wiki or '—'}` → `python herramientas/investigar_serie.py --serie "{serie}" --wiki {wiki or '<wiki>'} --paginas "<personaje>" …`
- Los textos, fichas y etiquetas reales del canal: búscalos en `servidor/inventario.md`.
""", encoding="utf-8")
    # contexto del servidor
    srv = AQUI / "servidor"
    srv.mkdir(exist_ok=True)
    shutil.copy(V3 / "inventario.md", srv / "inventario.md")
    plan = (BANDEJA / "Discord - PLAN laminas v4, todas las del servidor (23-sep-2026).md").read_text(encoding="utf-8")
    ini = plan.find("## Las reglas que salen de sus veredictos")
    fin = plan.find("## El reparto")
    (srv / "reglas_del_dueno.md").write_text("# Lo que el dueño ha dicho de las láminas\n\n" + plan[ini:fin], encoding="utf-8")
    # ejemplos de nivel
    ya = AQUI / "biblias" / "_ya_hechas"
    ya.mkdir(parents=True, exist_ok=True)
    for f in (BANDEJA / "Biblias de series").glob("*.md"):
        shutil.copy(f, ya / f.name)
    # herramientas
    h = AQUI / "herramientas"
    h.mkdir(exist_ok=True)
    for f in ("investigar_serie.py", "wiki.py"):
        shutil.copy(V3 / f, h / f)
    print(f"{len(ENCARGOS)} encargos · servidor/ · biblias/_ya_hechas/ ({len(list(ya.glob('*.md')))}) · herramientas/")


if __name__ == "__main__":
    main()
