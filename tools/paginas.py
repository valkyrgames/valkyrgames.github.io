"""Genera las páginas de contenido del sitio (guía, blog, preguntas, nosotros, términos) con el mismo diseño, menú y pie.
uso: py tools/paginas.py   (escribe cada página en su carpeta: relampago/guia/, blog/..., preguntas/, nosotros/, terminos/)
El contenido de cada página está en tools/contenido/*.py (un diccionario con título, descripción y cuerpo en es/en)."""
import pathlib, importlib.util, html, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import juegos as J
BORR = '--borradores' in sys.argv
GP = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M2.5 1.3 9.3 8l-6.8 6.7a1 1 0 0 1-.5-.9V2.2a1 1 0 0 1 .5-.9Zm7.6 7.5 1.9 1.9-8.2 4.6 6.3-6.5Zm0-1.6L3.8.7 12 5.3l-1.9 1.9Zm2.8-1.4 2.1 1.2c.7.4.7 1.4 0 1.8l-2.1 1.2L10.8 8l2.1-2.2Z"/></svg>'
TIK = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M16.6 3c.4 2.2 1.8 3.7 4 4v3.1c-1.5 0-2.9-.5-4-1.2v6.4a5.7 5.7 0 1 1-5.7-5.7c.3 0 .6 0 .9.1v3.2a2.6 2.6 0 1 0 1.7 2.4V3h3.1Z"/></svg>'
PLAY = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M4 2.5v11l9-5.5z"/></svg>'

def L(es, en): return f'<span data-l="es">{es}</span><span data-l="en">{en}</span>'

def nav(r):
    items = [(f'{r}#juegos', 'Juegos', 'Games'), (f'{r}#estudio', 'Estudio', 'Studio'), (f'{r}#contacto', 'Contacto', 'Contact')]  # guía y blog fuera del menú (siguen publicados para Google)
    links = '\n'.join(f'      <a href="{h}"><i>0{i + 1}</i>{L(es, en)}</a>' for i, (h, es, en) in enumerate(items))
    mlinks = '\n'.join(f'  <a class="ml" href="{h}" style="--i:{i}"><i>0{i + 1}</i>{L(es, en)}</a>' for i, (h, es, en) in enumerate(items))
    lang = '<div class="lang" role="group" aria-label="Idioma / Language"><button type="button" data-set="es">ES</button><button type="button" data-set="en">EN</button></div>'
    return f'''<header class="nav">
  <div class="nav-in">
    <a class="brand" href="{r}" aria-label="Valkyr Games"><span class="bmark"><img src="{r}assets/logo-v.png" alt=""></span><span class="btxt"><b>Valkyr</b><small>Games</small></span></a>
    <nav class="links">
{links}
    </nav>
    {lang}
    <a class="btn main navplay" href="{r}relampago/jugar/">{PLAY}{L('Jugar', 'Play')}</a>
    <button class="burger" type="button" aria-label="Menú" aria-expanded="false"><span></span><span></span></button>
    <i class="prog"></i>
  </div>
</header>

<div class="mnav">
{mlinks}
  <div class="mfoot">
    <a class="btn main" href="{r}relampago/jugar/">{PLAY}{L('Jugar ahora', 'Play now')}</a>
    {lang}
  </div>
</div>'''

def footer(r):
    col = lambda t_es, t_en, links: f'<div>\n        <h4>{L(t_es, t_en)}</h4>\n' + '\n'.join(f'        <a href="{r}{h}">{L(es, en)}</a>' for h, es, en in links) + '\n      </div>'
    return f'''<footer>
  <div class="wrap">
    <div class="fcols">
      <div>
        <a class="brand" href="{r}" style="margin-bottom:16px"><span class="bmark"><img src="{r}assets/logo-v.png" alt=""></span><span class="btxt"><b>Valkyr</b><small>Games</small></span></a>
        <p>{L('Estudio independiente de videojuegos para celular.', 'Independent mobile game studio.')}</p>
        <a class="social" href="https://www.tiktok.com/@valkyrgames" target="_blank" rel="noopener">{TIK}<span>@valkyrgames</span></a>
      </div>
      {col('Juegos', 'Games', [(j['slug'] + '/', j['nombre'], j['nombre']) for j in J.publicados(BORR)])}
      {col('Estudio', 'Studio', [('nosotros/', 'Sobre nosotros', 'About us'), ('#contacto', 'Contacto', 'Contact')])}
      {col('Ayuda', 'Help', [('preguntas/', 'Preguntas frecuentes', 'FAQ'), ('privacidad/', 'Privacidad', 'Privacy'), ('terminos/', 'Términos de uso', 'Terms of use')])}
    </div>
    <div class="fbot">
      <span>© <span id="year">2026</span> Valkyr Games · <span class="flag"><i></i>{L('Hecho en Argentina', 'Made in Argentina')}</span></span>
      <button class="top" type="button">{L('Volver arriba', 'Back to top')}<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 10V2M2.5 5.5 6 2l3.5 3.5"/></svg></button>
    </div>
  </div>
</footer>'''

def page(path, c):
    depth = len(pathlib.PurePosixPath(path).parts)
    r = '../' * depth
    t_es, t_en = c['title']
    esc = lambda s: html.escape(s, quote=True)
    crumbs = ''.join(f'<a href="{r}{h}">{L(es, en)}</a> <span>›</span> ' for h, es, en in c.get('crumbs', []))
    return f'''<!doctype html>
<html lang="es" data-title-es="{esc(t_es)} · Valkyr Games" data-title-en="{esc(t_en)} · Valkyr Games">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(t_es)} · Valkyr Games</title>
<meta name="description" content="{esc(c['desc'])}">
<meta name="theme-color" content="#04060b">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(t_es)}">
<meta property="og:description" content="{esc(c['desc'])}">
<meta property="og:image" content="https://valkyrgames.com/{c.get('og', 'assets/og.jpg')}">
<link rel="canonical" href="https://valkyrgames.com/{path}/">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9158616049034617" crossorigin="anonymous"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-DX7TB0Y4TX"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-DX7TB0Y4TX');</script>
<link rel="icon" type="image/png" sizes="32x32" href="{r}assets/favicon-32.png">
<script>var d=document.documentElement,l;d.classList.add('js');try{{l=localStorage.getItem('vg-lang')}}catch(e){{}}if(!l)l=/^es/i.test(navigator.language||'')?'es':'en';if(l==='en')d.classList.add('en')</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Orbitron:wght@500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/site.css">
</head>
<body>
<div class="sky" aria-hidden="true"><i class="aur a1"></i><i class="aur a2"></i><i class="aur a3"></i><canvas></canvas><i class="flash"></i><i class="lamp"></i></div>

{nav(r)}

<main class="doc article">
<nav class="crumbs">{crumbs}</nav>
<div data-l="es">
{c['es'].replace('{R}', r)}
</div>
<div data-l="en">
{c['en'].replace('{R}', r)}
</div>
<div class="cta-in">
  {f'<a class="btn main" href="{r}{c["cta"][0]}">{L(c["cta"][1], c["cta"][2])}</a>' if c.get('cta') else f'<a class="btn main" href="{r}relampago/jugar/">{PLAY}{L("Jugar Relámpago gratis", "Play Relámpago free")}</a>'}
</div>
</main>

{footer(r)}

<script src="{r}assets/site.js"></script>
</body>
</html>
'''

# ───── juegos: botones de tienda, ficha de cada juego y tarjetas de la portada ─────
def tiendas(j, pre, big=True, tiktok=True):
    """Botones para conseguir el juego. pre = camino hasta la carpeta del juego. site.js los reordena según el celular (Android: Google Play primero; iPhone y compu: jugar en el navegador)."""
    b = ' big' if big else ''
    out = []
    if j['web'] and j['estado'] == 'disponible':
        out.append(f'<a class="btn main{b}" data-os="web" href="{pre}{j["web"]}">{PLAY}{L("Jugar gratis", "Play free")}</a>')
    if j['android']:
        out.append(f'<a class="btn {"line" if out else "main"}{b}" data-os="android" href="{j["android"]}" target="_blank" rel="noopener">{GP}{L("Descargar en Google Play", "Get it on Google Play")}</a>')
    elif j['estado'] == 'disponible':
        out.append(f'<span class="btn soon">{GP}Google Play · {L("Pronto", "Soon")}</span>')
    if j['estado'] != 'disponible':
        out.append(f'<span class="btn soon">{L("Próximamente", "Coming soon")}</span>')
        if tiktok: out.append(f'<a class="btn line{b}" href="https://www.tiktok.com/@valkyrgames" target="_blank" rel="noopener">{TIK}{L("Enterate primero", "Be the first to know")}</a>')
    return f'<div class="btns" data-stores>\n          ' + '\n          '.join(out) + '\n        </div>'

def stats(j):
    return '<div class="stats">' + ''.join(f'<div class="stat"><b data-to="{n}">{n}</b>{L(es, en)}</div>' for n, es, en in j['stats']) + '</div>'

def tarjeta(j, i):
    """Tarjeta grande de un juego en la portada (sección Juegos)."""
    a = f'assets/{j["slug"]}/'
    land = j['orient'] == 'horizontal'
    fan = '\n'.join(f'            <img src="{a}{f}" alt="" loading="lazy">' for f in j['fan'])
    ver = L('Ver juego', 'View game')
    return f'''      <article class="feature rv{' land' if land else ''}{' flip' if i % 2 else ''}" data-game="{j['slug']}">
        <canvas class="fx" data-tint="{'gold' if land else 'violet'}" aria-hidden="true"></canvas>
        <div class="grid">
          <div>
            <span class="flabel"><b></b>{L(*j['etiqueta'])}</span>
            <div class="ftitle">
              <img src="{a}icono.png" alt="" width="68" height="68">
              <h2>{j['nombre']}</h2>
            </div>
            <p class="tagline">{L(*j['tagline'])}</p>
            <p class="desc">{L(*j['corto'])}</p>
            {stats(j)}
            <div class="btns" data-stores>
              {tiendas(j, j['slug'] + '/', tiktok=False).replace('<div class="btns" data-stores>', '').replace('</div>', '').strip()}
              <a class="btn line big" href="{j['slug']}/">{ver}</a>
            </div>
          </div>
          <a class="fan{' land' if land else ''}" href="{j['slug']}/" aria-label="{j['nombre']}" tabindex="-1">
{fan}
          </a>
        </div>
      </article>'''

def ficha(j):
    """Página propia de un juego: <slug>/index.html."""
    a = f'../assets/{j["slug"]}/'
    land = j['orient'] == 'horizontal'
    esc = lambda s: html.escape(s, quote=True)
    slides = '\n'.join(f'              <img{" class=\"on\"" if k == 0 else " loading=\"lazy\""} src="{a}{f}" alt="">' for k, f in enumerate(j['slides']))
    shots = '\n'.join(f'        <img src="{a}{f}" alt="" loading="lazy">' for f in j['shots'])
    pasos = '\n'.join(f'''        <div class="step rv" style="--d:{k * 0.1:.1f}s">
          <h3>{L(t_es, t_en)}</h3>
          <p>{L(p_es, p_en)}</p>
        </div>''' for k, (t_es, t_en, p_es, p_en) in enumerate(j['pasos']))
    feats = '\n'.join(f'        <div class="feat rv" style="--d:{(k % 2) * 0.1:.1f}s"><div><b>{L(b_es, b_en)}</b><span>{L(s_es, s_en)}</span></div></div>' for k, (b_es, b_en, s_es, s_en) in enumerate(j['feats']))
    jugable = j['web'] and j['estado'] == 'disponible'
    pantalla = f'''<{'a' if jugable else 'div'} class="phone{' live' if jugable else ''}{' land' if land else ''}"{f' href="{j["web"]}" aria-label="Jugar {j["nombre"]}"' if jugable else ''}>
            <div class="screen" data-slides>
{slides}
              <span class="zap"></span>
              {f'<span class="playme"><b>{PLAY}</b></span>' if jugable else ''}
            </div>
          </{'a' if jugable else 'div'}>'''
    grande = f'<p class="fs"><span data-l="es">¿Lo querés más grande?</span><span data-l="en">Want it bigger?</span> <a href="{j["web"]}"><span data-l="es">Pantalla completa ↗</span><span data-l="en">Full screen ↗</span></a></p>' if jugable else ''
    guia = ''  # la guía ya no se enlaza desde la ficha
    nota_en = f'<span data-l="en"> {j["nota_en"]}</span>' if j.get('nota_en') else ''
    final_btns = tiendas(j, '').replace('data-stores', 'data-stores style="justify-content:center"')
    tema = f' class="{j["tema"]}"' if j.get('tema') else ''
    fuentes = '&family=Lilita+One&family=Nunito:wght@400;600;700;800' if j.get('tema') == 'atado' else ''
    titulo = (f'<h1 class="logo-h1"><img src="{a}{j["logo"]}" alt="{esc(j["nombre"])}" width="1100" height="804"></h1>' if j.get('logo')
              else f'<img class="gicon" src="{a}icono.png" alt="" width="84" height="84">\n        <h1>{j["nombre"]}</h1>')
    return f'''<!doctype html>
<html lang="es"{tema} data-title-es="{esc(j['nombre'])} · Valkyr Games" data-title-en="{esc(j['nombre'])} · Valkyr Games">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(j['nombre'])} · Valkyr Games</title>
<meta name="description" content="{esc(j['desc'])}">
<meta name="theme-color" content="#04060b">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9158616049034617" crossorigin="anonymous"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-DX7TB0Y4TX"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-DX7TB0Y4TX');</script>
<link rel="icon" type="image/png" href="{a}icono.png">
<link rel="apple-touch-icon" href="{a}icono.png">
<link rel="canonical" href="https://valkyrgames.com/{j['slug']}/">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(j['nombre'])}">
<meta property="og:description" content="{esc(j['og_desc'])}">
<meta property="og:image" content="https://valkyrgames.com/assets/{j['slug']}/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<script>var d=document.documentElement,l;d.classList.add('js');try{{l=localStorage.getItem('vg-lang')}}catch(e){{}}if(!l)l=/^es/i.test(navigator.language||'')?'es':'en';if(l==='en')d.classList.add('en')</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Orbitron:wght@500;600;700;800;900{fuentes}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/site.css">
</head>
<body data-game="{j['slug']}">
<div class="sky" aria-hidden="true"><i class="aur a1"></i><i class="aur a2"></i><i class="aur a3"></i><canvas></canvas><i class="flash"></i><i class="lamp"></i></div>

{nav('../')}

<main>
  <section class="ghero{' land' if land else ''}">
    <div class="wrap">
      <div class="rv">
        <a class="back" href="../#juegos">← {L('Todos los juegos', 'All games')}</a>
        {titulo}
        <p class="tagline">{L(*j['tagline'])}</p>
        <p class="lead">{L(*j['lead'])}</p>
        {tiendas(j, '')}
        <p class="store-note">
          {L(*j['nota'])}{nota_en}
          <span class="ios-note">{L('¿Tenés iPhone? Jugalo directo desde el navegador, sin descargar nada.', 'On iPhone? Play it right in your browser, no download needed.') if jugable else ''}</span>
          {guia}
          <br><a class="tklink" href="https://www.tiktok.com/@valkyrgames" target="_blank" rel="noopener">{TIK}{L('Mirá los videos en TikTok', 'Watch the videos on TikTok')}</a>
        </p>
      </div>
      <div class="rv" style="--d:.15s">
        <div class="stage">
          {pantalla}
        </div>
        {grande}
      </div>
    </div>
  </section>

  <hr class="rule">

  <section>
    <div class="wrap">
      <div class="sec-head">
        <div class="rv">
          <p class="kicker">{L(*j['como'][0])}</p>
          <h2>{L(*j['como'][1])}</h2>
        </div>
      </div>
      <div class="steps">
{pasos}
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="shots rv{' land' if land else ''}">
{shots}
      </div>
    </div>
  </section>

  <hr class="rule">

  <section>
    <div class="wrap">
      <div class="sec-head">
        <div class="rv">
          <p class="kicker">{L(*j['que'][0])}</p>
          <h2>{L(*j['que'][1])}</h2>
        </div>
      </div>
      <div class="feats">
{feats}
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap rv">
      <h2>{L(*j['final'])}</h2>
      {final_btns}
    </div>
  </section>
</main>

{footer('../')}

<script src="../assets/site.js"></script>
</body>
</html>
'''

def portada():
    """Pone las tarjetas de los juegos en la portada y el pie nuevo en las páginas hechas a mano."""
    p = ROOT / 'index.html'; s = p.read_text(encoding='utf-8')
    cards = '\n\n'.join(tarjeta(j, i) for i, j in enumerate(J.publicados(BORR)))
    s = re.sub(r'(<!-- juegos:inicio -->\n).*?(\n\s*<!-- juegos:fin -->)', lambda m: m.group(1) + cards + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r'<footer>.*?</footer>', lambda m: footer(''), s, count=1, flags=re.S).replace('<a class="brand" href="" ', '<a class="brand" href="./" ')
    p.write_text(s, encoding='utf-8')
    for f, r in [('privacidad/index.html', '../'), ('404.html', '/')]:
        q = ROOT / f
        if q.exists() and '<footer>' in (t := q.read_text(encoding='utf-8')):
            q.write_text(re.sub(r'<footer>.*?</footer>', lambda m: footer(r), t, count=1, flags=re.S), encoding='utf-8')

if __name__ == '__main__':
    urls = ['', 'privacidad/']
    for j in J.publicados(BORR):
        (ROOT / j['slug']).mkdir(exist_ok=True)
        (ROOT / j['slug'] / 'index.html').write_text(ficha(j), encoding='utf-8')
        urls.append(j['slug'] + '/')
        if j['web'] and j['estado'] == 'disponible': urls.append(j['slug'] + '/' + j['web'])
        print(f'{j["slug"]}: ficha ({j["estado"]})')
    portada()
    for f in sorted((ROOT / 'tools' / 'contenido').glob('*.py')):
        spec = importlib.util.spec_from_file_location(f.stem, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for path, c in m.PAGES.items():
            out = ROOT / path / 'index.html'; out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(page(path, c), encoding='utf-8')
            urls.append(path + '/')
            words = len((c['es'] + ' ' + c['en']).split())
            print(f'{path}: {words} palabras')
    sm = ''.join(f'  <url><loc>https://valkyrgames.com/{u}</loc></url>\n' for u in urls)
    (ROOT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}</urlset>\n', encoding='utf-8')
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://valkyrgames.com/sitemap.xml\n', encoding='utf-8')
    print(f'sitemap.xml: {len(urls)} páginas')
