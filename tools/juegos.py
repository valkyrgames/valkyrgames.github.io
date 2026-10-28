"""Lista de juegos del estudio. Cada juego tiene su ficha (<slug>/index.html) y su tarjeta en la portada (sección Juegos).
Para sumar un juego: agregar un diccionario a JUEGOS, poner sus imágenes en assets/<slug>/ y correr  py tools/paginas.py
estado: 'disponible' (se juega ya), 'pronto' (ficha con «Próximamente») o 'borrador' (no se publica; para verlo en local: py tools/paginas.py --borradores).
Botones: web = link para jugar en el navegador (o None), android = link de Google Play (o None). En iPhone se juega desde el navegador."""

JUEGOS = [
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
