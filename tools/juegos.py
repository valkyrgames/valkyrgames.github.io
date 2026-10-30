"""Lista de juegos del estudio. Cada juego tiene su ficha (<slug>/index.html) y su tarjeta en la portada (sección Juegos).
Para sumar un juego: agregar un diccionario a JUEGOS, poner sus imágenes en assets/<slug>/ y correr  py tools/paginas.py
estado: 'disponible' (se juega ya), 'pronto' (ficha con «Próximamente») o 'borrador' (no se publica; para verlo en local: py tools/paginas.py --borradores).
Botones: web = link para jugar en el navegador (o None), android = link de Google Play (o None). En iPhone se juega desde el navegador."""

JUEGOS = [
{
    'slug': 'atado-con-alambre', 'nombre': 'Atado con Alambre', 'estado': 'disponible', 'orient': 'horizontal',
    'etiqueta': ('Juego nuevo · Ya disponible', 'New game · Out now'),
    'tagline': ('Apilá todo lo que trae el flete. ¡Que no se caiga!', "Stack everything off the truck. Don't let it fall!"),
    'corto': ('Llega el flete cargado hasta el techo y Don Tito, desde la grúa, tiene que apilar todo: la heladera, el lavarropas, el piano de la tía. ¿Hasta dónde llega tu torre antes de que se venga abajo?',
              "The moving truck shows up loaded to the roof, and Don Tito has to stack it all from his crane: the fridge, the washing machine, auntie's piano. How high can your tower go before it comes crashing down?"),
    'lead': ('Un juego de apilar con física de verdad. Cada cosa pesa, rueda, se hamaca y se rompe como tiene que romperse. Bajala despacito, soltala justo y que no se caiga.',
             'A stacking game with real physics. Everything has weight, rolls, sways and breaks the way it should. Lower it gently, drop it just right and keep the tower standing.'),
    'desc': 'Atado con Alambre: apilá con la grúa todo lo que trae el flete y armá la torre más alta. Juego gratis de física para celular y navegador.',
    'og_desc': 'Apilá todo lo que trae el flete y armá la torre más alta. ¡Que no se caiga!',
    'stats': [(4, 'Ciudades', 'Cities'), (12, 'Desafíos', 'Challenges'), (3, 'Modos', 'Modes'), (50, 'Logros', 'Achievements')],
    'web': 'jugar/', 'android': None,
    'nota': ('Se juega en el navegador del celular (de costado) o la compu. Sin descargas.', 'Plays in your phone browser (sideways) or on a computer. No download.'),
    'slides': ['1-buenos-aires.webp', '2-nueva-york.webp', '3-paris.webp', '4-dubai.webp'],
    'fan': ['2-nueva-york.webp', '1-buenos-aires.webp', '3-paris.webp'],
    'shots': ['1-buenos-aires.webp', '2-nueva-york.webp', '3-paris.webp', '4-dubai.webp', '5-tienda.webp', '6-desafios.webp', '7-ruleta.webp', '8-mapas.webp'],
    'como': (('Cómo se juega', 'How to play'), ('Bajala. Soltala. Que aguante.', 'Lower. Drop. Hold on.')),
    'pasos': [
        ('Mové la grúa', 'Move the crane', 'Llevá la carga con el dedo hasta arriba de la torre y bajala despacito.', 'Drag the load over the tower with your finger and lower it gently.'),
        ('Soltala justo', 'Drop it just right', 'Lo redondo rueda, lo frágil se rompe y lo pesado aplasta lo de abajo.', 'Round things roll, fragile things break and heavy things crush what is below.'),
        ('Atala con alambre', 'Tie it with wire', 'Cuando se pone fea, precinto, cinturón de amarre o La Gotita, y a seguir subiendo.', 'When it gets shaky, use zip ties, a strap or super glue, and keep climbing.'),
    ],
    'que': (('Qué tiene', "What's inside"), ('Del barrio al espacio', 'From the block to outer space')),
    'feats': [
        ('Cuatro ciudades', 'Four cities', 'Buenos Aires, Nueva York, París y Dubái, cada una con su hora: si allá es de noche, jugás de noche.', "Buenos Aires, New York, Paris and Dubai, each on its own clock: if it's night there, you play at night."),
        ('Infinito y Torre del día', 'Endless and Daily tower', 'Lo más alto que puedas, o la misma torre para todos, una nueva cada día.', 'As high as you can, or the same tower for everyone, a new one every day.'),
        ('12 desafíos', '12 challenges', 'La cristalería, todo redondo, día de viento, contrarreloj y más, con 3 estrellas cada uno.', 'The glassware shop, all round, windy day, against the clock and more, with 3 stars each.'),
        ('Tu grúa, tu estilo', 'Your crane, your style', 'Grúas, bases y Don Tito vestido para la ocasión, más de 50 logros y ruleta diaria.', 'Cranes, bases and Don Tito dressed for the occasion, 50+ achievements and a daily wheel.'),
    ],
    'final': ('¿Hasta dónde llega tu torre?', 'How high can your tower go?'),
},
{
    'slug': 'relampago', 'nombre': 'Relámpago', 'estado': 'disponible', 'orient': 'vertical',
    'etiqueta': ('Juego destacado · Ya disponible', 'Featured game · Out now'),
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
