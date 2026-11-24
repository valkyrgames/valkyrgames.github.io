"""Lista de juegos del estudio. Cada juego tiene su ficha (<slug>/index.html) y su tarjeta en la portada (sección Juegos).
Para sumar un juego: agregar un diccionario a JUEGOS, poner sus imágenes en assets/<slug>/ y correr  py tools/paginas.py
tema: estilo de la ficha (por ahora 'atado': colores del atardecer y letra del juego). logo: imagen del título en assets/<slug>/ (opcional).
estado: 'disponible' (se juega ya), 'pronto' (ficha con «Próximamente») o 'borrador' (no se publica; para verlo en local: py tools/paginas.py --borradores).
carpeta: carpeta de la ficha si no es el slug (Fit Into Place usa 'fitintoplace' porque el juego vive en valkyrgames.com/fit-into-place/, desde su propio repo).
Botones: web = link (relativo a la carpeta, o una dirección completa) para jugar en el navegador (o None), android = link de Google Play (o None). En iPhone se juega desde el navegador."""

JUEGOS = [
{
    'slug': 'atado-con-alambre', 'nombre': 'Atado con Alambre', 'estado': 'disponible', 'tema': 'atado', 'logo': 'logo-titulo.webp', 'orient': 'horizontal',
    'etiqueta': ('Ya en Google Play', 'Out now on Google Play'),
    'tagline': ('Armá la torre más alta del mundo. ¡Que no se caiga!', "Build the tallest tower in the world. Don't let it fall!"),
    'corto': ('Con una grúa apilás lo que toque, cuanto más absurdo mejor: la heladera, el lavarropas, el inodoro, una bicicleta. ¿Hasta dónde llega tu torre antes de que se venga abajo?',
              "Use a crane to stack whatever comes up, the more absurd the better: the fridge, the washing machine, the toilet, a bike. How high can your tower go before it comes crashing down?"),
    'lead': ('Un juego de apilar con física de verdad. Cada cosa pesa, rueda, se hamaca y se rompe como tiene que romperse. Bajala despacito, soltala justo y que no se caiga.',
             'A stacking game with real physics. Everything has weight, rolls, sways and breaks the way it should. Lower it gently, drop it just right and keep the tower standing.'),
    'desc': 'Atado con Alambre: armá con una grúa la torre más alta del mundo con las cosas más absurdas. Juego gratis de física para celular y navegador.',
    'og_desc': 'Armá la torre más alta del mundo con lo que toque. ¡Que no se caiga!',
    'stats': [(4, 'Ciudades', 'Cities'), (12, 'Desafíos', 'Challenges'), (3, 'Modos', 'Modes'), (50, 'Logros', 'Achievements')],
    'web': 'jugar/', 'android': 'https://play.google.com/store/apps/details?id=com.atadoconalambre.torre',
    'nota': ('Gratis en Google Play. En iPhone o la compu, se juega en el navegador.', 'Free on Google Play. On iPhone or a computer, play it in your browser.'),
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
    'slug': 'fit-into-place', 'carpeta': 'fitintoplace', 'nombre': 'Fit Into Place', 'estado': 'pronto', 'orient': 'vertical',
    'etiqueta': ('Próximamente · Android', 'Coming soon · Android'),
    'tagline': ('Armá máquinas encastrando piezas.', 'Build machines by snapping parts together.'),
    'corto': ('Girá cada pieza, alineá los dientes y clavala en su lugar. De un banquito de madera a una turbina, pieza por pieza, hasta que la máquina arranca.',
              'Rotate each part, line up the teeth and slam it into place. From a wooden stool to a turbine, part by part, until the machine comes to life.'),
    'lead': ('Un juego tranquilo y muy satisfactorio: cada pieza tiene que entrar justo. Girala, alineá los dientes y tocá para clavarla. Cuando la última encastra, la máquina se arma sola frente a tus ojos.',
             'A calm, deeply satisfying game: every part has to fit just right. Rotate it, line up the teeth and tap to slam it in. When the last one clicks, the machine comes together before your eyes.'),
    'desc': 'Fit Into Place: armá máquinas encastrando piezas. Girá, alineá los dientes y clavá cada pieza en su lugar. Seis talleres y un modo Infinito. Próximamente en Android.',
    'og_desc': 'Armá máquinas encastrando piezas. Girá, alineá y clavá.',
    'stats': [(6, 'Talleres', 'Workshops'), (55, 'Máquinas', 'Machines'), (2, 'Modos', 'Modes'), (2, 'Idiomas', 'Languages')],
    'web': None, 'android': None,
    'nota': ('Muy pronto en Google Play.', 'Coming soon to Google Play.'),
    'slides': ['1-menu.webp', '2-infinito.webp', '5-carpinteria.webp', '4-sobremarcha.webp'],
    'fan': ['2-infinito.webp', '1-menu.webp', '4-sobremarcha.webp'],
    'shots': ['1-menu.webp', '2-infinito.webp', '3-talleres.webp', '4-sobremarcha.webp', '5-carpinteria.webp'],
    'como': (('Cómo se juega', 'How to play'), ('Girá. Alineá. Clavá.', 'Rotate. Align. Slam.')),
    'pasos': [
        ('Deslizá para girar', 'Swipe to rotate', 'Cada pieza llega con su forma. Deslizá el dedo para girarla.', 'Every part arrives with its own shape. Swipe to rotate it.'),
        ('Alineá los dientes', 'Line up the teeth', 'Buscá el ángulo justo para que los dientes y las ranuras coincidan.', 'Find the exact angle so the teeth and slots match.'),
        ('Tocá para clavar', 'Tap to slam', 'Tocá y la pieza baja a su lugar. Si encaja perfecto, suma combo.', 'Tap and the part drops into place. A perfect fit builds your combo.'),
    ],
    'que': (('Qué tiene', "What's inside"), ('Del banquito a la turbina', 'From a stool to a turbine')),
    'feats': [
        ('Seis talleres', 'Six workshops', 'Carpintería, Metalurgia, Electrónica, Electrodomésticos, Mecánica e Ingeniería Avanzada.', 'Carpentry, Metalwork, Electronics, Appliances, Mechanics and Advanced Engineering.'),
        ('55 máquinas', '55 machines', 'Sillas, relojes, cámaras, lavarropas y más, cada una armada pieza por pieza.', 'Chairs, clocks, cameras, washing machines and more, each one built part by part.'),
        ('Modo Infinito', 'Endless mode', 'Piezas sin fin, combos y récord. ¿Hasta dónde llegás?', 'Endless parts, combos and high scores. How far can you go?'),
        ('Mirá por dentro', 'See inside', 'Cuando terminás, girá la máquina y mirá cómo funciona por dentro.', 'When you finish, spin the machine around and see how it works inside.'),
    ],
    'final': ('¿Encaja?', 'Does it fit?'),
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
