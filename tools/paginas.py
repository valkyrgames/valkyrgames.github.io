"""Genera las páginas de contenido del sitio (guía, blog, preguntas, nosotros, términos) con el mismo diseño, menú y pie.
uso: py tools/paginas.py   (escribe cada página en su carpeta: relampago/guia/, blog/..., preguntas/, nosotros/, terminos/)
El contenido de cada página está en tools/contenido/*.py (un diccionario con título, descripción y cuerpo en es/en)."""
import pathlib, importlib.util, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
TIK = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M16.6 3c.4 2.2 1.8 3.7 4 4v3.1c-1.5 0-2.9-.5-4-1.2v6.4a5.7 5.7 0 1 1-5.7-5.7c.3 0 .6 0 .9.1v3.2a2.6 2.6 0 1 0 1.7 2.4V3h3.1Z"/></svg>'
PLAY = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M4 2.5v11l9-5.5z"/></svg>'

def L(es, en): return f'<span data-l="es">{es}</span><span data-l="en">{en}</span>'

def nav(r):
    items = [(f'{r}#juegos', 'Juegos', 'Games'), (f'{r}relampago/guia/', 'Guía', 'Guide'), (f'{r}blog/', 'Blog', 'Blog'),
             (f'{r}#estudio', 'Estudio', 'Studio'), (f'{r}#contacto', 'Contacto', 'Contact')]
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
      {col('Juegos', 'Games', [('relampago/', 'Relámpago', 'Relámpago'), ('relampago/guia/', 'Guía de Relámpago', 'Relámpago guide'), ('relampago/jugar/', 'Jugar ahora', 'Play now')])}
      {col('Estudio', 'Studio', [('nosotros/', 'Sobre nosotros', 'About us'), ('blog/', 'Blog', 'Blog'), ('#contacto', 'Contacto', 'Contact')])}
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
  <a class="btn main" href="{r}relampago/jugar/">{PLAY}{L('Jugar Relámpago gratis', 'Play Relámpago free')}</a>
</div>
</main>

{footer(r)}

<script src="{r}assets/site.js"></script>
</body>
</html>
'''

if __name__ == '__main__':
    urls = ['', 'relampago/', 'relampago/jugar/', 'privacidad/']
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
