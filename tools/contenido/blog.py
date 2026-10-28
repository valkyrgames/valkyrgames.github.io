POSTS = [
 ('como-nacio-relampago', '15 de octubre de 2026', 'October 15, 2026',
  'Cómo nació Relámpago', 'How Relámpago was born',
  'De una lista de quince ideas a un juego donde solo ves cuando cae un rayo.', 'From a list of fifteen ideas to a game where you only see when lightning strikes.',
'''<p>Relámpago no fue la primera idea. Antes de escribir una sola línea del juego armamos una investigación con quince propuestas de juegos para celular y las comparamos por originalidad, facilidad de hacer, chances de volverse virales y cuánto podían durarle a la gente. Después probamos otras direcciones: un sudoku en un cubo (ya existían varios), juegos mentales con balanzas y máquinas (también existían) y un juego de oleadas infinitas (un género demasiado lleno). Ninguna convencía.</p>
<p>La idea que quedó apareció pensando en una sensación más que en una mecánica: <b>la tensión de no ver</b>. Es de noche, estás en una tormenta y el camino solo aparece un instante, cuando cae un rayo. Después, oscuridad. Tenés que acordarte de lo que viste y moverte a ciegas. Se explica en una frase y se entiende mirando cinco segundos de video, dos cosas que buscábamos desde el principio.</p>
<h2>El primer prototipo</h2>
<p>La primera versión se podía jugar en el navegador el mismo día: una luz cálida que se mueve con el dedo, muros con un hueco que bajan hacia vos, rayos que iluminan todo una fracción de segundo con su trueno, lluvia para sentir la velocidad y los metros como puntaje. Al chocar, la pantalla se iluminaba para que vieras qué te había matado. Ya tenía chispas, niveles de experiencia y once cartas de mejora.</p>
<p>Desde ese día anotamos cada cambio en una bitácora. Hoy el juego va por la versión 168: tiene una campaña de cinco mundos con sus jefes, un modo infinito que cambia sin parar, desafíos diarios, ranking mundial, música propia y una versión en inglés.</p>
<h2>Lo que aprendimos</h2>
<ul>
  <li><b>Juzgar jugando, no leyendo.</b> Muchas ideas suenan bien escritas y aburren en el dedo. Al revés también pasa.</li>
  <li><b>Una sola idea fuerte.</b> Todo lo que se agregó después (cartas, jefes, eventos) gira alrededor del rayo; nada lo reemplaza.</li>
  <li><b>Que nunca sea injusto.</b> En un juego a oscuras es fácil frustrar. La regla más importante del diseño es que siempre ves el camino al menos una vez antes de tener que pasarlo.</li>
</ul>
<p>Si todavía no lo probaste, se juega gratis en el navegador, sin descargar nada.</p>''',
'''<p>Relámpago wasn't the first idea. Before writing a single line of the game we put together research with fifteen mobile game concepts and compared them by originality, how easy they were to build, their chances of going viral and how long they could keep people playing. Then we tried other directions: a sudoku on a cube (several already existed), brain games with scales and machines (those existed too) and an endless wave game (a far too crowded genre). None of them clicked.</p>
<p>The idea that stuck came from a feeling rather than a mechanic: <b>the tension of not seeing</b>. It's night, you're in a storm, and the path only appears for an instant when lightning strikes. Then darkness. You have to remember what you saw and move blind. It can be explained in one sentence and understood from five seconds of video, two things we were looking for from the start.</p>
<h2>The first prototype</h2>
<p>The first version was playable in the browser on the same day: a warm light you move with your finger, walls with a gap coming down towards you, lightning that lights everything up for a split second with its thunder, rain to feel the speed, and meters as the score. When you crashed, the screen lit up so you could see what killed you. It already had sparks, experience levels and eleven upgrade cards.</p>
<p>Since that day we've logged every change in a development diary. Today the game is on version 168: it has a five-world campaign with bosses, an endless mode that never stops changing, daily challenges, a world leaderboard, original music and an English version.</p>
<h2>What we learned</h2>
<ul>
  <li><b>Judge by playing, not by reading.</b> Many ideas sound great on paper and feel boring under your finger. The opposite happens too.</li>
  <li><b>One strong idea.</b> Everything added later (cards, bosses, events) revolves around the lightning; nothing replaces it.</li>
  <li><b>Never unfair.</b> In a game played in the dark it's easy to frustrate people. The most important design rule is that you always see the path at least once before you have to cross it.</li>
</ul>
<p>If you haven't tried it yet, it's free to play in the browser, no download needed.</p>'''),

 ('disenar-en-la-oscuridad', '22 de octubre de 2026', 'October 22, 2026',
  'Diseñar un juego que se juega a oscuras', 'Designing a game you play in the dark',
  'Cómo hacemos que no ver nada sea divertido y no frustrante.', 'How we make seeing nothing fun instead of frustrating.',
'''<p>En casi todos los juegos, ver es lo normal. En Relámpago es lo contrario: la oscuridad es lo normal y ver es un premio que dura menos de un segundo. Eso cambia cómo hay que pensar la dificultad, las ayudas y hasta la música.</p>
<h2>El rayo es información</h2>
<p>Cada rayo es una foto del camino. La dificultad sale de jugar con esa foto: qué tan seguido cae el rayo, cuánto dura, qué tan anchos son los huecos y a qué velocidad bajan los muros. Al principio caen muchos rayos largos, los huecos son anchos y vas despacio. A medida que avanzás, los rayos se espacian y se acortan, y los huecos se achican.</p>
<h2>La regla de oro: nunca imposible</h2>
<p>La peor sensación en un juego así es chocar contra algo que nunca pudiste ver. Por eso el juego calcula, según la velocidad, cada cuánto tiene que caer un rayo para que <b>siempre</b> veas un muro antes de que llegue hasta vos. Ni los jefes ni los eventos más difíciles rompen esa regla. Hasta el eclipse, el evento donde no caen rayos, arranca con un destello para que sepas dónde estás.</p>
<h2>Ayudas que no regalan</h2>
<p>Muchas cartas son formas distintas de ver: Retina deja los muros marcados un rato, Farol ilumina lo que está cerca de tu bola, Eco lanza una onda que revela lo que toca, Guía hace brillar el próximo hueco y Amanecer saca el sol unos segundos. Ninguna te deja ver todo todo el tiempo; cada una cambia un poco la forma de jugar.</p>
<h2>Chispas: guía y tentación</h2>
<p>Las chispas se ven siempre, incluso a oscuras. La mayoría está sobre el camino seguro, así que funcionan como pista. Pero algunas, sobre todo las doradas, están afuera: valen más y te tientan a salirte del camino justo cuando no ves nada. Ese pequeño dilema aparece en cada partida.</p>
<h2>Probar jugando miles de veces</h2>
<p>Para comprobar que nunca haya un tramo imposible usamos un piloto automático que juega solo, apuntando a los huecos como lo haría una persona. Lo dejamos correr miles de metros: si choca contra un muro que no pudo ver, algo del diseño está mal y se corrige. El mismo piloto es el que graba las partidas de nuestros videos.</p>''',
'''<p>In almost every game, seeing is normal. In Relámpago it's the opposite: darkness is normal and seeing is a reward that lasts less than a second. That changes how you have to think about difficulty, helpers and even the music.</p>
<h2>Lightning is information</h2>
<p>Each lightning strike is a snapshot of the path. Difficulty comes from playing with that snapshot: how often lightning strikes, how long it lasts, how wide the gaps are and how fast the walls come down. At first there's plenty of long lightning, the gaps are wide and you move slowly. As you go further, the strikes get rarer and shorter, and the gaps get smaller.</p>
<h2>The golden rule: never impossible</h2>
<p>The worst feeling in a game like this is crashing into something you never got to see. So the game works out, based on your speed, how often lightning has to strike so that you <b>always</b> see a wall before it reaches you. Not even the bosses or the hardest events break that rule. Even the eclipse, the event where no lightning falls, starts with a flash so you know where you are.</p>
<h2>Helpers that don't give it away</h2>
<p>Many cards are different ways of seeing: Retina keeps the walls marked for a while, Lantern lights up whatever is near your ball, Echo sends out a wave that reveals what it touches, Guide makes the next gap glow and Sunrise brings out the sun for a few seconds. None of them lets you see everything all the time; each one changes the way you play a little.</p>
<h2>Sparks: guide and temptation</h2>
<p>Sparks are always visible, even in the dark. Most of them sit on the safe path, so they work as a hint. But some, especially the golden ones, are off the path: they're worth more and tempt you to leave the path right when you can't see anything. That small dilemma shows up in every run.</p>
<h2>Testing by playing thousands of times</h2>
<p>To check that there's never an impossible stretch, we use an autopilot that plays on its own, aiming for the gaps like a person would. We let it run for thousands of meters: if it crashes into a wall it couldn't see, something in the design is wrong and gets fixed. The same autopilot records the gameplay for our videos.</p>'''),

 ('cinco-mundos-cinco-jefes', '25 de octubre de 2026', 'October 25, 2026',
  'Cinco mundos, cinco jefes', 'Five worlds, five bosses',
  'Cada mundo de la campaña cambia una sola cosa de cómo te movés. Y cada jefe avisa antes de atacar.', 'Each campaign world changes just one thing about how you move. And every boss warns you before it attacks.',
'''<p>La campaña de Relámpago tiene cinco mundos de cinco niveles. Al diseñarlos pusimos una regla: cada mundo tiene que cambiar algo de <b>cómo te movés</b>, no solo cómo se ve. Si un mundo nuevo se juega igual que el anterior con otro color, no es un mundo nuevo.</p>
<h2>Un cambio por mundo</h2>
<ul>
  <li><b>Bosque:</b> el mundo para aprender. Suma de a poco chispas que tientan, huecos que se mueven y murciélagos.</li>
  <li><b>Glaciar:</b> el hielo hace que la bola patine. De golpe, frenar a tiempo es parte del desafío.</li>
  <li><b>Desierto:</b> cosas que vienen de arriba (pilares que caen) y arenas movedizas que te hacen girar.</li>
  <li><b>Volcán:</b> fuerzas que te empujan: ríos de lava hacia los costados y géiseres hacia adelante.</li>
  <li><b>Espacio:</b> la gravedad deja de ser tuya: agujeros negros que te atraen y portales que te mueven de lugar.</li>
</ul>
<p>Cada nivel presenta una sola novedad, con un video corto antes de empezar, y el último nivel de cada mundo la combina con lo anterior antes del jefe.</p>
<h2>Jefes que se pueden leer</h2>
<p>En un juego a oscuras, un ataque sorpresa es injusto. Por eso todos los jefes <b>avisan</b>: la Nube de Tormenta marca en el piso dónde va a caer su rayo, la Ventisca apunta su soplido antes de largarlo, la Esfinge elige una columna y espera a que llegue el próximo muro para que el hueco sea tu refugio, el Gólem de Lava muestra dónde van a caer sus meteoritos y la Tormenta Viva siempre deja un espacio seguro entre sus anillos.</p>
<p>Ganarle a un jefe no es cuestión de suerte sino de mirar el aviso, recordar el camino y animarse a moverse a tiempo. Y cada uno te deja algo: la habilidad de su mundo y un paquete de estilos para tu bola y tu mapa.</p>
<h2>Y después, el Infinito</h2>
<p>Todo lo que aparece en la campaña vuelve en el modo Infinito, mezclado, con zonas que cambian cada mil metros, jefes cada dos mil, pactos y eventos sorpresa. La campaña enseña; el Infinito pone a prueba.</p>''',
'''<p>Relámpago's campaign has five worlds with five levels each. When designing them we set one rule: every world has to change something about <b>how you move</b>, not just how it looks. If a new world plays exactly like the previous one in a different color, it isn't a new world.</p>
<h2>One change per world</h2>
<ul>
  <li><b>Forest:</b> the world to learn in. It slowly adds tempting sparks, moving gaps and bats.</li>
  <li><b>Glacier:</b> ice makes the ball slide. Suddenly, stopping in time is part of the challenge.</li>
  <li><b>Desert:</b> things coming from above (falling pillars) and quicksand that spins you around.</li>
  <li><b>Volcano:</b> forces that push you: lava rivers sideways and geysers forward.</li>
  <li><b>Space:</b> gravity is no longer yours: black holes that pull you and portals that move you around.</li>
</ul>
<p>Each level introduces a single new thing, with a short video before it starts, and the last level of each world combines it with everything else before the boss.</p>
<h2>Bosses you can read</h2>
<p>In a game played in the dark, a surprise attack is unfair. That's why every boss <b>warns you</b>: the Storm Cloud marks on the ground where its lightning will fall, the Blizzard aims its breath before blowing, the Sphinx picks a column and waits for the next wall so its gap becomes your shelter, the Lava Golem shows where its meteors will land and the Living Storm always leaves a safe space between its rings.</p>
<p>Beating a boss isn't about luck but about reading the warning, remembering the path and daring to move in time. And each one leaves you something: its world's skill and a style pack for your ball and your map.</p>
<h2>And then, Endless</h2>
<p>Everything from the campaign comes back in Endless mode, mixed together, with zones that change every thousand meters, bosses every two thousand, pacts and surprise events. The campaign teaches; Endless puts you to the test.</p>'''),

 ('musica-y-sonido', '28 de octubre de 2026', 'October 28, 2026',
  'La música de Relámpago: hecha dentro del juego', 'The music of Relámpago: made inside the game',
  'Por qué Relámpago no trae canciones grabadas y cómo arma su música mientras jugás.', 'Why Relámpago ships no recorded songs and how it builds its music as you play.',
'''<p>Relámpago no trae canciones grabadas. Toda su música se arma dentro del propio juego, en tu celular o tu navegador, con un pequeño motor de sonido que toca baterías, bajos, acordes y melodías nota por nota. Lo hicimos así por dos razones: el juego pesa muy poco (se abre al instante desde un link) y la música puede cambiar según lo que pase en la partida.</p>
<h2>Tres estilos, muchos temas</h2>
<p>Podés elegir el estilo: <b>rap</b>, <b>trap</b> o <b>electrónica</b>. Cada estilo tiene su tema para el menú, para los niveles y para los jefes, y los desafíos tienen temas propios, como uno de synthwave oscuro para el desafío de los huecos que se achican.</p>
<h2>Música que reacciona</h2>
<ul>
  <li>Cuando aparece un <b>jefe</b>, la música cambia a su tema, más pesado.</li>
  <li>Cada uno de los <b>trece eventos sorpresa</b> del modo Infinito tiene su propio tema corto, y el cambio entra a tiempo, sin cortar el ritmo.</li>
  <li>Cuando ponés <b>pausa</b> o elegís una carta, la música baja y suena como detrás de una pared, para que se sienta que el juego espera.</li>
  <li>Los <b>pactos</b> tienen un sonido propio, oscuro y un poco inquietante, porque siempre te quitan algo.</li>
</ul>
<h2>Y para los videos, temas propios</h2>
<p>Los videos y el tráiler del juego también llevan música compuesta para cada uno, sincronizada con lo que pasa en pantalla: un golpe grave cuando aparece un texto, un trueno cuando cae un rayo, la base que arranca justo cuando empieza la acción. Así no dependemos de canciones con derechos de autor y cada video suena distinto.</p>
<p>Un consejo: jugá con sonido. En Relámpago la música no solo acompaña; también te avisa cuando algo está por cambiar.</p>''',
'''<p>Relámpago ships no recorded songs. All of its music is built inside the game itself, on your phone or in your browser, by a small sound engine that plays drums, bass, chords and melodies note by note. We did it this way for two reasons: the game is very light (it opens instantly from a link) and the music can change depending on what happens in your run.</p>
<h2>Three styles, many tracks</h2>
<p>You can pick the style: <b>rap</b>, <b>trap</b> or <b>electronic</b>. Each style has its own track for the menu, for levels and for bosses, and the challenges have their own tracks too, like a dark synthwave one for the challenge where gaps keep shrinking.</p>
<h2>Music that reacts</h2>
<ul>
  <li>When a <b>boss</b> shows up, the music switches to its heavier theme.</li>
  <li>Each of the <b>thirteen surprise events</b> in Endless mode has its own short theme, and the change comes in on the beat, without breaking the rhythm.</li>
  <li>When you <b>pause</b> or pick a card, the music drops and sounds muffled, as if behind a wall, so it feels like the game is waiting.</li>
  <li><b>Pacts</b> have their own sound, dark and a little unsettling, because they always take something from you.</li>
</ul>
<h2>And for the videos, original tracks</h2>
<p>The game's videos and trailer also carry music composed for each one, synced with what happens on screen: a deep hit when a title appears, thunder when lightning strikes, the beat kicking in right as the action starts. That way we don't depend on copyrighted songs and every video sounds different.</p>
<p>A tip: play with sound on. In Relámpago the music doesn't just come along for the ride; it also warns you when something is about to change.</p>'''),
]

PAGES = {}
for slug, d_es, d_en, t_es, t_en, s_es, s_en, b_es, b_en in POSTS:
    PAGES[f'blog/{slug}'] = {
        'title': (t_es, t_en), 'desc': s_es, 'og': 'assets/relampago/og.jpg',
        'crumbs': [('', 'Inicio', 'Home'), ('blog/', 'Blog', 'Blog')],
        'es': f'<h1>{t_es}</h1>\n<small>{d_es} · Valkyr Games</small>\n<p class="lede">{s_es}</p>\n{b_es}\n<p class="more"><a href="{{R}}relampago/guia/">Guía completa de Relámpago →</a></p>',
        'en': f'<h1>{t_en}</h1>\n<small>{d_en} · Valkyr Games</small>\n<p class="lede">{s_en}</p>\n{b_en}\n<p class="more"><a href="{{R}}relampago/guia/">Full Relámpago guide →</a></p>',
    }
card = lambda slug, d, t, s, more: f'<a class="post" href="{{R}}blog/{slug}/"><small>{d}</small><b>{t}</b><span>{s}</span><i>{more} →</i></a>'
PAGES['blog'] = {
    'title': ('Blog', 'Blog'), 'desc': 'Diario de desarrollo de Valkyr Games: cómo se hacen nuestros juegos, empezando por Relámpago.',
    'crumbs': [('', 'Inicio', 'Home')],
    'es': '<h1>Blog</h1>\n<small>Diario de desarrollo de Valkyr Games</small>\n<p class="lede">Cómo pensamos y hacemos nuestros juegos: ideas, diseño, música y lo que vamos aprendiendo.</p>\n<div class="posts">\n'
          + '\n'.join(card(p[0], p[1], p[3], p[5], 'Leer') for p in reversed(POSTS)) + '\n</div>',
    'en': '<h1>Blog</h1>\n<small>Valkyr Games development diary</small>\n<p class="lede">How we think about and make our games: ideas, design, music and what we keep learning.</p>\n<div class="posts">\n'
          + '\n'.join(card(p[0], p[2], p[4], p[6], 'Read') for p in reversed(POSTS)) + '\n</div>',
}
