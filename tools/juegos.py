"""Lista de juegos del estudio. Cada juego tiene su ficha (<slug>/index.html) y su tarjeta en la portada (sección Juegos).
Para sumar un juego: agregar un diccionario a JUEGOS, poner sus imágenes en assets/<slug>/ y correr  py tools/paginas.py
tema: estilo de la ficha (por ahora 'atado': colores del atardecer y letra del juego). logo: imagen del título en assets/<slug>/ (opcional).
estado: 'disponible' (se juega ya), 'pronto' (ficha con «Próximamente») o 'borrador' (no se publica; para verlo en local: py tools/paginas.py --borradores).
Botones: web = link para jugar en el navegador (o None), android = link de Google Play (o None). En iPhone se juega desde el navegador."""

JUEGOS = [
{
    'slug': 'atado-con-alambre', 'nombre': 'Atado con Alambre', 'estado': 'pronto', 'tema': 'atado', 'logo': 'logo-titulo.webp', 'orient': 'horizontal',
    'etiqueta': ('Nuevo juego · Muy pronto', 'New game · Coming soon'),
    'tagline': ('Armá la torre más alta del barrio.', 'Build the tallest tower in the neighborhood.'),
    'corto': ('Una grúa, un flete lleno de cosas de una mudanza y un baldío del conurbano. Apilá heladeras, inodoros, bicicletas y lo que venga, una arriba de otra, sin que se venga abajo.',
              'A crane, a truck full of stuff from a house move and an empty lot in the Buenos Aires suburbs. Stack fridges, toilets, bikes and whatever comes, one on top of the other, without it all coming down.'),
    'lead': ('En un baldío del conurbano, Don Tito maneja la grúa y Cacho llega con el flete lleno de cosas de una mudanza. Vos apilás todo, una cosa arriba de la otra, y tratás de armar la torre más alta sin que se venga abajo. Los vecinos miran y opinan de todo.',
             'In an empty lot in the Buenos Aires suburbs, Don Tito runs the crane and Cacho shows up with a truck full of stuff from a house move. You stack it all, one thing on top of the other, and try to build the tallest tower without it falling down. The neighbors watch and have an opinion on everything.'),
    'desc': 'Atado con Alambre: apilá las cosas de una mudanza con una grúa y armá la torre más alta del barrio. Juego de física gracioso, en 3D, para celular y navegador.',
    'og_desc': 'Apilá heladeras, inodoros y bicicletas con una grúa. ¿Hasta dónde llega tu torre?',
    'stats': [(39, 'Objetos', 'Objects'), (12, 'Desafíos', 'Challenges'), (36, 'Estrellas', 'Stars'), (18, 'Logros', 'Achievements')],
    'web': 'jugar/', 'android': None,
    'nota': ('Se juega con el celular acostado. También anda en la compu, con el mouse.', 'Play with your phone sideways. It also works on a computer, with the mouse.'),
    'nota_en': 'For now the game is in Spanish only.',
    'slides': ['3-juego.webp', '4-racha.webp', '2-menu.webp', '1-llegada.webp'],
    'fan': ['2-menu.webp', '3-juego.webp', '4-racha.webp'],
    'shots': ['3-juego.webp', '2-menu.webp', '4-racha.webp', '5-desafios.webp', '1-llegada.webp'],
    'como': (('Cómo se juega', 'How to play'), ('Llevá. Apoyá. Soltá.', 'Move. Set down. Release.')),
    'pasos': [
        ('Llevá la carga', 'Move the load', 'La grúa trae una cosa colgada. Arrastrá el dedo para llevarla hasta arriba de la torre.', 'The crane brings something hanging from the hook. Drag your finger to take it over the tower.'),
        ('Apoyala', 'Set it down', 'Bajala hasta que toque. Si es alta y finita, girala y acostala.', "Lower it until it touches. If it's tall and thin, turn it and lay it down."),
        ('Soltá con cuidado', 'Release gently', 'Si la apoyaste limpia sumás racha y herramientas. Si la tirás de arriba… se rompe.', "Set it down cleanly and you build a streak and earn tools. Drop it from above… and it breaks."),
    ],
    'que': (('Qué tiene', "What's inside"), ('Puro barrio', 'Pure neighborhood')),
    'feats': [
        ('Modo Infinito', 'Endless mode', 'Apilá sin fin y marcá tu récord. Con 3 cajones de vida: cada cosa que se cae gasta uno.', 'Stack forever and set your record. You have 3 crates of lives: each thing that falls costs one.'),
        ('Torre del día', 'Tower of the day', 'Una torre nueva cada día, la misma para todos.', 'A new tower every day, the same for everyone.'),
        ('12 desafíos', '12 challenges', 'La heladera arriba, la cristalería de la abuela, el piano de la tía… 36 estrellas para ganar.', "The fridge on top, grandma's glassware, auntie's piano… 36 stars to earn."),
        ('Herramientas de barrio', 'Neighborhood tools', 'Precinto, alambre y pegamento para que la torre aguante de milagro.', 'Zip ties, wire and glue to keep the tower standing by a miracle.'),
        ('Los vecinos', 'The neighbors', 'Don Tito, Cacho, Doña Rosa, el Pibe del kiosco, la Abuela, el Relator, Firulais y el loro Pepe.', 'Don Tito, Cacho, Doña Rosa, the kiosk kid, Grandma, the radio announcer, Firulais the dog and Pepe the parrot.'),
        ('Modo foto', 'Photo mode', 'Sacale una foto a tu torre y compartila.', 'Take a photo of your tower and share it.'),
    ],
    'final': ('¿Hasta dónde llega tu torre?', 'How tall can your tower go?'),
},
{
    'slug': 'relampago', 'nombre': 'Relámpago', 'estado': 'disponible', 'orient': 'vertical',
    'etiqueta': ('Ya disponible · Gratis', 'Out now · Free'),
    'tagline': ('Solo ves cuando cae un rayo.', 'You only see when lightning strikes.'),
    'corto': ('Es de noche y hay tormenta. Guiás una bola de luz entre losas de tierra flotantes, pero el camino solo aparece un instante, con cada rayo. Memorizalo y pasá a ciegas.',
              "It's night, and a storm is raging. Guide a ball of light between floating slabs of earth, but the path only appears for an instant, with each strike. Memorize it and fly through blind."),
    'lead': ('Es de noche y estás en medio de una tormenta. Guiás una bola de luz entre losas de tierra flotantes, pero el camino solo aparece un instante, con cada rayo. Memorizalo y pasá a ciegas.',
             "It's night and you're caught in a storm. Guide a ball of light between floating slabs of earth, but the path only appears for an instant, with each strike. Memorize it and fly through blind."),
    'desc': 'Relámpago: es de noche, hay tormenta y solo ves los obstáculos cuando cae un rayo. Juego gratis de reflejos para celular y navegador.',
    'og_desc': 'Solo ves cuando cae un rayo. Memorizá el camino y pasá a ciegas.',
    'stats': [(5, 'Mundos', 'Worlds'), (25, 'Niveles', 'Levels'), (21, 'Cartas', 'Cards'), (13, 'Eventos', 'Events')],
    'web': 'jugar/', 'android': None,
    'nota': ('Se juega en el navegador del celular o la compu. Sin descargas, sin cuenta.', 'Plays in your phone or computer browser. No download, no account.'),
    'guia': 'relampago/guia/',
    'slides': ['3-juego.webp', '7-jefe.webp', '6-pacto.webp', '4-evento.webp'],
    'fan': ['7-jefe.webp', '3-juego.webp', '6-pacto.webp'],
    'shots': ['3-juego.webp', '1-menu.webp', '7-jefe.webp', '2-cartas.webp', '4-evento.webp', '6-pacto.webp', '5-mercader.webp'],
    'como': (('Cómo se juega', 'How to play'), ('Mirá. Memorizá. Pasá.', 'Look. Remember. Go.')),
    'pasos': [
        ('Esperá el rayo', 'Wait for the strike', 'Cuando cae un rayo se ilumina todo por un instante. Ahí ves dónde están los huecos.', "When lightning strikes, everything lights up for an instant. That's when you see the gaps."),
        ('Memorizá el camino', 'Memorize the path', 'Después vuelve la oscuridad. Tenés que acordarte de por dónde pasar.', 'Then darkness returns. You have to remember where to go.'),
        ('Pasá a ciegas', 'Fly through blind', 'Arrastrá el dedo para mover la bola de luz y juntá chispas en el camino.', 'Drag your finger to move the ball of light and collect sparks on the way.'),
    ],
    'que': (('Qué tiene', "What's inside"), ('Mucho más que esquivar', 'Much more than dodging')),
    'feats': [
        ('Campaña de 5 mundos', '5-world campaign', 'Bosque, Glaciar, Desierto, Volcán y Espacio, cada uno con su jefe.', 'Forest, Glacier, Desert, Volcano and Space, each with its own boss.'),
        ('Modo Infinito', 'Endless mode', '¿Hasta dónde llegás? Jefes, pactos y eventos sorpresa en cada partida.', 'How far can you go? Bosses, pacts and surprise events every run.'),
        ('Cartas y habilidades', 'Cards and skills', 'Armá tu mazo y usá saltos, cámara lenta y más con un gesto.', 'Build your deck and use jumps, slow motion and more with a swipe.'),
        ('Desafíos y ranking mundial', 'Challenges and world ranking', 'La tormenta del día y desafíos para competir contra todos.', 'The daily storm and challenges to compete against everyone.'),
    ],
    'final': ('¿Te animás a la tormenta?', 'Ready for the storm?'),
},
]

# Juegos en borrador que todavía son secretos: tools/juegos_borradores.py (no se sube a GitHub; misma forma, lista BORRADORES)
try:
    from juegos_borradores import BORRADORES
    JUEGOS += BORRADORES
except ImportError:
    pass

def publicados(borradores=False):
    return [j for j in JUEGOS if borradores or j['estado'] != 'borrador']
