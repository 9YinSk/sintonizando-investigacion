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


# La biblioteca: series, pelis y juegos muy queridos por el público latino, sin
# canal todavía. Sirven para salas de voz, láminas 2, eventos y para cambiar un
# anfitrión si él rechaza uno. (serie, wiki sugerida, por qué está, personajes)
BIBLIOTECA = [
    ("Naruto", "naruto", "anime clave del doblaje latino", "Naruto, Sasuke, Sakura, Kakashi, Jiraiya, Itachi"),
    ("Demon Slayer (Kimetsu no Yaiba)", "kimetsu-no-yaiba", "de lo más visto en Latinoamérica", "Tanjiro, Nezuko, Zenitsu, Inosuke, Rengoku, Shinobu"),
    ("Jujutsu Kaisen", "jujutsu-kaisen", "fenómeno actual", "Itadori, Gojo, Megumi, Nobara, Sukuna"),
    ("Frieren", "frieren", "la más valorada de los últimos años", "Frieren, Fern, Stark, Himmel"),
    ("Haikyuu!!", "haikyuu", "deporte y equipo", "Hinata, Kageyama, Nishinoya, Oikawa, Bokuto"),
    ("One Punch Man", "onepunchman", "comedia de acción muy memeada", "Saitama, Genos, Tatsumaki, Mumen Rider"),
    ("Hunter x Hunter", "hunterxhunter", "clásico de culto", "Gon, Killua, Kurapika, Leorio, Hisoka"),
    ("Fullmetal Alchemist: Brotherhood", "fma", "de las mejor valoradas de la historia", "Edward, Alphonse, Roy Mustang, Winry"),
    ("Sailor Moon", "sailormoon", "clásico enorme en Latinoamérica", "Usagi, Ami, Rei, Makoto, Minako, Luna"),
    ("Saint Seiya (Los Caballeros del Zodiaco)", "saintseiya", "mito del doblaje latino", "Seiya, Shiryu, Hyoga, Shun, Ikki, Saori"),
    ("Digimon Adventure", "digimon", "nostalgia de toda una generación", "Tai, Agumon, Matt, Gabumon, Sora"),
    ("Dandadan", "dandadan", "fenómeno reciente", "Momo, Okarun, Turbo Granny, Aira"),
    ("Blue Lock", "bluelock", "fútbol, enorme en Latinoamérica", "Isagi, Bachira, Nagi, Rin"),
    ("Kaguya-sama: Love is War", "kaguyasama-wa-kokurasetai", "comedia romántica muy querida", "Kaguya, Shirogane, Chika, Ishigami"),
    ("Your Lie in April (Shigatsu)", "shigatsu-wa-kimi-no-uso", "música y emoción: encaja con canto", "Kousei, Kaori, Tsubaki, Watari"),
    ("Mob Psycho 100", "mob-psycho-100", "estilo visual único", "Mob, Reigen, Dimple"),
    ("Sakamoto Days", "sakamoto-days", "reciente y muy compartido", "Sakamoto, Shin, Lu"),
    ("Captain Tsubasa (Supercampeones)", "captaintsubasa", "nostalgia latina pura", "Oliver/Tsubasa, Benji/Genzo, Steve/Kojiro"),
    ("Inuyasha", "inuyasha", "clásico de los 2000", "Inuyasha, Kagome, Sesshomaru, Miroku, Sango"),
    ("Yu-Gi-Oh!", "yugioh", "cartas y duelos, nostalgia", "Yugi, Kaiba, Joey, el Mago Oscuro"),
    ("Cardcaptor Sakura", "ccsakura", "clásico muy querido", "Sakura, Kero, Tomoyo, Syaoran"),
    ("Studio Ghibli (Totoro, El viaje de Chihiro…)", "ghibli", "fondos y paisajes de referencia mundial", "Totoro, Chihiro, Haku, Kiki, Howl"),
    ("Your Name (Makoto Shinkai)", "kiminonawa", "cielos y ciudades de referencia", "Taki, Mitsuha"),
    ("Avatar: la leyenda de Aang", "avatar", "de las series animadas más queridas", "Aang, Katara, Sokka, Zuko, Toph, Iroh"),
    ("Gravity Falls", "gravityfalls", "misterio y códigos ocultos", "Dipper, Mabel, Stan, Bill Cipher"),
    ("Hazbin Hotel", "hazbinhotel", "musical, muy popular entre los que doblan", "Charlie, Alastor, Angel Dust, Vaggie, Husk"),
    ("The Amazing Digital Circus", "the-amazing-digital-circus", "fenómeno de internet", "Pomni, Caine, Jax, Ragatha"),
    ("Coco", "pixar", "México y la música", "Miguel, Héctor, Mamá Coco, Dante"),
    ("Encanto", "disney", "Colombia y la música", "Mirabel, Bruno, Luisa, Isabela, Abuela Alma"),
    ("Shrek", "shrek", "doblaje latino legendario (Eugenio Derbez)", "Shrek, Burro, Fiona, el Gato con Botas"),
    ("Toy Story", "pixar", "clásico del doblaje latino", "Woody, Buzz, Jessie, Rex"),
    ("Kung Fu Panda", "kungfupanda", "muy querida y memeada", "Po, Shifu, Tigresa, Oogway"),
    ("Intensamente (Inside Out)", "pixar", "las emociones: ideal para actuación de voz", "Alegría, Tristeza, Furia, Desagrado, Temor, Ansiedad"),
    ("Las Guerreras K-pop (KPop Demon Hunters)", "kpop-demon-hunters", "fenómeno musical reciente", "Rumi, Mira, Zoey, Jinu"),
    ("Steven Universe", "steven-universe", "música y personajes queridos", "Steven, Garnet, Amatista, Perla"),
    ("The Legend of Zelda", "zelda", "videojuego de referencia", "Link, Zelda, Ganon"),
    ("Persona 5", "megamitensei", "la interfaz más copiada de los juegos", "Joker, Morgana, Ann, Ryuji"),
    ("Hollow Knight", "hollowknight", "estética dibujada a mano", "el Caballero, Hornet, Quirrel"),
    ("Undertale / Deltarune", "undertale", "cuadros de diálogo icónicos", "Frisk, Sans, Papyrus, Toriel, Kris"),
    ("Genshin Impact", "genshin-impact", "muy jugado, arte oficial abundante", "Paimon, Venti, Zhongli, Raiden, Hu Tao"),
    ("Minecraft", "minecraft", "el juego que todos conocen", "Steve, Alex, Creeper, Enderman"),
    ("Five Nights at Freddy's", "freddy-fazbears-pizza", "terror muy popular (y su película)", "Freddy, Bonnie, Chica, Foxy"),
    ("Hatsune Miku (Vocaloid)", "vocaloid", "canto: la voz sintética más famosa", "Miku, Rin, Len, Luka"),
]


# Temas de conocimiento (no series): para que su Claude principal sea experto.
from catalogo import TEMAS, SERIES  # temas y series nuevas, por bloques


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
    base = len(ENCARGOS)
    for j, (serie, wiki, porque, pjs) in enumerate(BIBLIOTECA, base + 1):
        nombre = f"{j:02d}-{slug(serie)}"
        (AQUI / "encargos" / f"{nombre}.md").write_text(f"""# Encargo {j:02d} — {serie} (biblioteca)

Lee primero `ENCARGO.md` (qué investigar y dónde dejarlo). Deja todo en `biblias/{nombre}/`.

- **Serie:** {serie}
- **Por qué está:** {porque}. Todavía **no tiene canal**: investiga la serie
  entera, y en «3 conceptos de lámina» propón **para qué canal o sala** del
  servidor encajaría mejor (mira `servidor/inventario.md`) y cómo sería la lámina.
- **Personajes para empezar:** {pjs}
- **Wiki de Fandom sugerida (compruébala):** `{wiki}` → `python herramientas/investigar_serie.py --serie "{serie}" --wiki {wiki} --paginas "<personaje>" …`
""", encoding="utf-8")
    # las series nuevas del catálogo, por bloques, numeradas después de la biblioteca
    n = len(ENCARGOS) + len(BIBLIOTECA)
    bloque_de = {}
    for bloque, lista in SERIES.items():
        for serie, fijarse, pjs in lista:
            n += 1
            nombre = f"{n:02d}-{slug(serie)}"
            bloque_de[nombre] = bloque
            (AQUI / "encargos" / f"{nombre}.md").write_text(f"""# Encargo {n:02d} — {serie} ({bloque})

Lee primero `ENCARGO.md` (qué investigar y dónde dejarlo). Deja todo en `biblias/{nombre}/`.

- **Serie:** {serie}
- **En qué fijarse especialmente:** {fijarse}.
- **Personajes para empezar:** {pjs}
- Todavía **no tiene canal**: en «3 conceptos de lámina» propón para qué canal o
  sala del servidor encajaría (mira `servidor/inventario.md`).
- Busca su wiki de Fandom (`https://<nombre>.fandom.com`) y úsala con
  `python herramientas/investigar_serie.py --serie "{serie}" --wiki <nombre> --paginas "<personaje>" …`
""", encoding="utf-8")
    # las tandas de series, de 4 en 4
    todos = sorted((p.stem for p in (AQUI / "encargos").glob("*.md")), key=lambda x: int(x.split("-")[0]))
    lineas = ["# Tandas de investigación (de 4 en 4)", "",
              "En una sesión nueva en la nube, con este repositorio, pega la frase de la tanda.",
              "La sesión hace los 4 encargos con **un ayudante por encargo, en paralelo**.",
              "Marca aquí las que ya estén hechas. El mapa completo está en `MAPA.md`.", "",
              "# Parte 1 · Series, películas y videojuegos", ""]
    for t in range(0, len(todos), 4):
        grupo = todos[t:t + 4]
        k = t // 4 + 1
        lineas += [f"## Tanda S{k}", "",
                   f"> Haz la tanda S{k} de `TANDAS.md` siguiendo `ENCARGO.md`: "
                   + ", ".join(f"`encargos/{g}.md`" for g in grupo)
                   + ". Un ayudante por encargo, en paralelo. Al terminar, commit y push de tu rama.", ""]
        lineas += [f"- [ ] {g}" for g in grupo] + [""]
    # los temas, por bloques (código A01, A02…)
    (AQUI / "temas").mkdir(exist_ok=True)
    for f in (AQUI / "temas").glob("*.md"):
        f.unlink()
    lineas += ["# Parte 2 · Temas para volverse experto", ""]
    for bloque, lista in TEMAS.items():
        letra = bloque.split(" ")[0]
        codigos = []
        for k, (tema, alcance) in enumerate(lista, 1):
            nombre = f"{letra}{k:02d}-{slug(tema)}"
            codigos.append(nombre)
            (AQUI / "temas" / f"{nombre}.md").write_text(f"""# {letra}{k:02d} — {tema} ({bloque})

Lee primero `TEMA.md` (qué investigar y dónde dejarlo) y `contexto/proyectos.md`.
Deja todo en `investigaciones/{nombre}/`.

- **Tema:** {tema}
- **Qué abarca:** {alcance}.
- Profundidad: hasta el mínimo detalle. Herramientas con precio y licencia,
  pasos concretos, ejemplos reales, trampas, y cómo replicarlo, mejorarlo o
  fusionarlo para crear algo propio.
""", encoding="utf-8")
        for t in range(0, len(codigos), 4):
            grupo = codigos[t:t + 4]
            k = t // 4 + 1
            lineas += [f"## Tanda {letra}{k} · {bloque}", "",
                       f"> Haz la tanda {letra}{k} de `TANDAS.md` siguiendo `TEMA.md`: "
                       + ", ".join(f"`temas/{g}.md`" for g in grupo)
                       + ". Un ayudante por tema, en paralelo. Al terminar, commit y push de tu rama.", ""]
            lineas += [f"- [ ] {g}" for g in grupo] + [""]
    (AQUI / "TANDAS.md").write_text("\n".join(lineas), encoding="utf-8")
    # el mapa, para leerlo en el celular
    mapa = ["# Mapa de la investigación", "",
            "Todo lo que se investiga, ordenado. Las frases para pegar están en `TANDAS.md`.", "",
            "## Series, películas y videojuegos", "",
            f"- **Los canales del servidor** (encargos 01-{len(ENCARGOS):02d}): " + ", ".join(e[0] for e in ENCARGOS),
            f"- **Biblioteca** (encargos {len(ENCARGOS)+1}-{len(ENCARGOS)+len(BIBLIOTECA)}): " + ", ".join(b[0] for b in BIBLIOTECA)]
    for bloque, lista in SERIES.items():
        mapa.append(f"- **{bloque}**: " + ", ".join(x[0] for x in lista))
    mapa += ["", "## Temas para volverse experto", ""]
    for bloque, lista in TEMAS.items():
        letra = bloque.split(" ")[0]
        mapa.append(f"### {bloque}")
        mapa += [f"- **{letra}{k:02d} {t}**: {a}" for k, (t, a) in enumerate(lista, 1)]
        mapa.append("")
    total_temas = sum(len(v) for v in TEMAS.values())
    total_series = len(todos)
    mapa.insert(2, f"**{total_series} encargos de series** y **{total_temas} temas**.")
    (AQUI / "MAPA.md").write_text("\n".join(mapa), encoding="utf-8")
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
    print(f"{len(list((AQUI / 'encargos').glob('*.md')))} encargos, {len(list((AQUI / 'temas').glob('*.md')))} temas · servidor/ · biblias/_ya_hechas/ ({len(list(ya.glob('*.md')))}) · herramientas/")


if __name__ == "__main__":
    main()
