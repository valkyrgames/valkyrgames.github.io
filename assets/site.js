(function () {
  const root = document.documentElement;
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $$ = s => document.querySelectorAll(s);

  // Botón ES / EN: guarda la elección y cambia el título de la pestaña
  function setLang(l) {
    root.classList.toggle('en', l === 'en');
    root.lang = l;
    const t = root.dataset['title' + (l === 'en' ? 'En' : 'Es')];
    if (t) document.title = t;
    try { localStorage.setItem('vg-lang', l); } catch (e) {}
    placeSpy();
  }
  $$('[data-set]').forEach(b => b.addEventListener('click', () => setLang(b.dataset.set)));
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Pantalla de carga: una vez por visita
  const boot = document.querySelector('.boot');
  if (boot && !root.classList.contains('booted')) {
    setTimeout(() => { boot.classList.add('out'); try { sessionStorage.setItem('vg-boot', '1'); } catch (e) {} }, 1550);
  }

  // Letras que se "descifran"
  const GL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%&/<>';
  function scramble(el) {
    if (calm || el._scr) return;
    const span = [...el.querySelectorAll('[data-l]')].find(s => s.offsetParent !== null) || el;
    if (span.children.length) return;
    const fin = span.textContent; let f = 0; const n = fin.length;
    el._scr = true;
    const id = setInterval(() => {
      f++;
      span.textContent = [...fin].map((ch, i) => ch === ' ' || i < f * n / 14 ? ch : GL[(Math.random() * GL.length) | 0]).join('');
      if (f >= 14) { clearInterval(id); span.textContent = fin; el._scr = false; }
    }, 38);
  }

  // Barra de arriba: panel al bajar, línea de progreso, sección en la que estás
  const nav = document.querySelector('.nav');
  const links = [...$$('.links a[data-spy]')];
  const spy = document.querySelector('.links .spy');
  let current = null;
  function placeSpy() {
    if (!spy) return;
    const a = links.find(l => l.dataset.spy === current);
    links.forEach(l => l.classList.toggle('on', l === a));
    if (!a) { spy.classList.remove('on'); return; }
    spy.style.setProperty('--x', (a.offsetLeft + a.offsetWidth / 2 - 3.5) + 'px');
    spy.classList.add('on');
  }
  function onScroll() {
    const s = scrollY, h = document.documentElement.scrollHeight - innerHeight;
    if (nav) {
      nav.classList.toggle('scrolled', s > 20);
      nav.style.setProperty('--p', h > 0 ? (s / h).toFixed(4) : 0);
    }
    if (links.length) {
      let cur = null;
      for (const l of links) { const sec = document.getElementById(l.dataset.spy); if (sec && sec.getBoundingClientRect().top < innerHeight * 0.4) cur = l.dataset.spy; }
      if (cur !== current) { current = cur; placeSpy(); }
    }
  }
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', placeSpy);
  setLang(root.classList.contains('en') ? 'en' : 'es');
  onScroll();
  $$('.links a').forEach(a => a.addEventListener('mouseenter', () => scramble(a)));

  // Menú del celular
  const burger = document.querySelector('.burger');
  function menu(open) {
    document.body.classList.toggle('menu-open', open);
    document.body.classList.toggle('locked', open);
    if (burger) burger.setAttribute('aria-expanded', String(open));
  }
  if (burger) burger.addEventListener('click', () => menu(!document.body.classList.contains('menu-open')));
  $$('.mnav a').forEach(a => a.addEventListener('click', () => menu(false)));
  addEventListener('keydown', e => { if (e.key === 'Escape') menu(false); });

  // Aparecer al bajar (+ títulos que se descifran y números que suben)
  function count(el) {
    const to = +el.dataset.to; if (calm) { el.textContent = to; return; }
    const t0 = performance.now(), d = 1400;
    (function step(now) {
      const k = Math.min(1, (now - t0) / d); el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3)));
      if (k < 1) requestAnimationFrame(step);
    })(t0);
  }
  function reveal(el) {
    el.classList.add('in');
    if (el.matches('[data-scr]')) scramble(el);
    el.querySelectorAll('[data-scr]').forEach(scramble);
    el.querySelectorAll('[data-to]').forEach(count);
  }
  const rv = $$('.rv');
  if ('IntersectionObserver' in window && !calm) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { reveal(e.target); io.unobserve(e.target); }
    }), { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    rv.forEach(el => io.observe(el));
  } else rv.forEach(reveal);

  // Celular: pasa capturas del juego con un relámpago en cada cambio
  $$('[data-slides]').forEach(scr => {
    const imgs = scr.querySelectorAll('img'), zap = scr.querySelector('.zap');
    if (imgs.length < 2 || calm) return;
    let i = 0;
    setInterval(() => {
      if (document.hidden || scr.closest('.live') && !scr.querySelector('img')) return;
      imgs[i].classList.remove('on'); i = (i + 1) % imgs.length; imgs[i].classList.add('on');
      if (zap) { zap.classList.remove('go'); void zap.offsetWidth; zap.classList.add('go'); }
    }, 2800);
  });

  // Botones de cada juego según el celular: en Android primero Google Play; en iPhone y compu, jugar en el navegador
  const ua = navigator.userAgent || '', ios = /iPhone|iPad|iPod/.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1), android = /Android/.test(ua);
  document.documentElement.classList.add(ios ? 'ios' : android ? 'android' : 'pc');
  if (android) $$('[data-stores]').forEach(b => {
    const gp = b.querySelector('[data-os="android"]'), web = b.querySelector('[data-os="web"]');
    if (!gp || !web) return;
    b.prepend(gp); gp.classList.replace('line', 'main'); web.classList.replace('main', 'line');
  });

  // Jugar adentro del celular (en pantallas grandes); en el celu abre el juego a pantalla completa
  const live = document.querySelector('.phone.live');
  if (live) live.addEventListener('click', e => {
    if (innerWidth < 900 || live.querySelector('iframe')) return;
    e.preventDefault();
    const f = document.createElement('iframe');
    f.src = live.getAttribute('href'); f.title = live.getAttribute('aria-label') || 'Juego'; f.allow = 'autoplay; fullscreen';
    live.querySelector('.screen').replaceChildren(f);
    const fs = document.querySelector('.fs'); if (fs) fs.classList.add('on');
    setTimeout(() => f.focus({ preventScroll: true }), 300);
  });

  // Analytics: cuántos tocan "Jugar" y desde qué parte de la página
  function track(name, params) { if (typeof gtag === 'function') gtag('event', name, params); }
  function gameOf(el) { const g = el.closest('[data-game]'); if (g) return g.dataset.game; const m = (el.getAttribute('href') || '').match(/([\w-]+)\/jugar\/$/); return m ? m[1] : 'relampago'; }
  $$('a[href$="jugar/"]:not(.live)').forEach(a => a.addEventListener('click', () => {
    const where = a.closest('.nav') ? 'barra' : a.closest('.mnav') ? 'menu' : a.closest('.hero') ? 'portada'
      : a.closest('.feature') ? 'destacado' : a.closest('.ghero') ? 'ficha' : a.closest('.cta') ? 'final' : a.closest('footer') ? 'pie' : 'otro';
    track('play_click', { game: gameOf(a), where });
  }));
  $$('a[data-os="android"]').forEach(a => a.addEventListener('click', () => track('store_click', { game: gameOf(a), store: 'google_play' })));
  if (live) live.addEventListener('click', () => { if (innerWidth >= 900) track('play_click', { game: gameOf(live), where: 'celular_en_pagina' }); });
  $$('a[href^="mailto:"]').forEach(a => a.addEventListener('click', () => track('contact_click', { method: 'mail' })));
  $$('a[href*="tiktok.com"]').forEach(a => a.addEventListener('click', () => track('social_click', { red: 'tiktok' })));

  // Copiar el mail
  $$('[data-copy]').forEach(b => b.addEventListener('click', () => {
    const done = () => { b.classList.add('ok'); setTimeout(() => b.classList.remove('ok'), 1800); };
    if (navigator.clipboard) navigator.clipboard.writeText(b.dataset.copy).then(done, () => {});
  }));
  $$('.top').forEach(b => b.addEventListener('click', () => scrollTo({ top: 0, behavior: calm ? 'auto' : 'smooth' })));

  // Cielo de toda la página: estrellas con profundidad, fugaces, rayos lejanos y la linterna del mouse
  const sky = document.querySelector('.sky');
  if (sky && !calm) {
    const cv = sky.querySelector('canvas'), ctx = cv.getContext('2d');
    const lamp = sky.querySelector('.lamp'), fl = sky.querySelector('.flash');
    let W = 0, H = 0, dpr = 1, stars = [], shoot = null, nextShoot = 3, nextFlash = 5, last = performance.now();
    let mx = innerWidth / 2, my = innerHeight * 0.4, tx = mx, ty = my, mouse = false, idle = 0;
    function size() {
      dpr = Math.min(devicePixelRatio || 1, 1.5);
      W = innerWidth; H = innerHeight; cv.width = W * dpr; cv.height = H * dpr;
      const n = Math.round(Math.min(220, W * H / 7000));
      stars = Array.from({ length: n }, () => {
        const z = Math.random();
        return { x: Math.random() * W, y: Math.random() * H, z, r: 0.4 + z * 1.4, a: 0.15 + z * 0.6, ph: Math.random() * 6.28, sp: 0.6 + Math.random() * 2 };
      });
    }
    addEventListener('pointermove', e => { if (e.pointerType === 'mouse') { mouse = true; idle = 0; tx = e.clientX; ty = e.clientY; } }, { passive: true });
    function tick(now) {
      requestAnimationFrame(tick);
      const dt = Math.min(0.05, (now - last) / 1000); last = now;
      if (document.hidden) return;
      const t = now / 1000, sy = scrollY;
      // linterna: sigue al mouse; sin mouse (o quieto un rato) se pasea sola
      idle += dt;
      if (!mouse || idle > 4) { tx = W * (0.5 + 0.38 * Math.sin(t * 0.23)); ty = H * (0.45 + 0.3 * Math.sin(t * 0.31 + 1)); }
      mx += (tx - mx) * Math.min(1, dt * (mouse && idle <= 4 ? 10 : 1.5)); my += (ty - my) * Math.min(1, dt * (mouse && idle <= 4 ? 10 : 1.5));
      lamp.style.setProperty('--mx', mx.toFixed(1) + 'px'); lamp.style.setProperty('--my', my.toFixed(1) + 'px');
      lamp.style.setProperty('--gy', (-sy * 0.15).toFixed(1) + 'px');
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
      for (const s of stars) {
        const y = ((s.y - sy * (0.04 + s.z * 0.18)) % H + H) % H;
        const a = s.a * (0.55 + 0.45 * Math.sin(t * s.sp + s.ph));
        ctx.fillStyle = s.z > 0.7 ? `rgba(170,200,255,${a})` : `rgba(255,255,255,${a})`;
        ctx.fillRect(s.x, y, s.r, s.r);
      }
      nextShoot -= dt;
      if (nextShoot <= 0) {
        const ang = 0.35 + Math.random() * 0.4, dir = Math.random() < 0.5 ? 1 : -1;
        shoot = { x: Math.random() * W, y: Math.random() * H * 0.5, vx: Math.cos(ang) * 900 * dir, vy: Math.sin(ang) * 900, life: 0.9 };
        nextShoot = 4 + Math.random() * 6;
      }
      if (shoot) {
        shoot.life -= dt; shoot.x += shoot.vx * dt; shoot.y += shoot.vy * dt;
        if (shoot.life <= 0) shoot = null;
        else {
          const k = Math.min(1, shoot.life / 0.5), len = 0.12;
          const g = ctx.createLinearGradient(shoot.x, shoot.y, shoot.x - shoot.vx * len, shoot.y - shoot.vy * len);
          g.addColorStop(0, `rgba(255,255,255,${0.9 * k})`); g.addColorStop(1, 'rgba(107,155,255,0)');
          ctx.strokeStyle = g; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.moveTo(shoot.x, shoot.y); ctx.lineTo(shoot.x - shoot.vx * len, shoot.y - shoot.vy * len); ctx.stroke();
        }
      }
      nextFlash -= dt;
      if (nextFlash <= 0) {
        fl.style.setProperty('--fx', (15 + Math.random() * 70).toFixed(0) + '%');
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
        nextFlash = 7 + Math.random() * 7;
      }
    }
    size(); addEventListener('resize', size);
    requestAnimationFrame(tick);
  }

  // Fondo vivo: chispas que suben y rayos que caen cada tanto
  if (!calm) $$('canvas.fx').forEach(cv => {
    const ctx = cv.getContext('2d');
    const tint = cv.dataset.tint, violet = tint === 'violet', gold = tint === 'gold';
    const glowC = gold ? '255,170,80' : violet ? '170,110,255' : '90,130,255', sparkC = gold ? '255,200,120' : violet ? '190,150,255' : '107,155,255';
    let W = 0, H = 0, dpr = 1, parts = [], bolt = null, nextBolt = 1.2 + Math.random() * 2, last = performance.now(), visible = true;
    function size() {
      dpr = Math.min(devicePixelRatio || 1, 2);
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = W * dpr; cv.height = H * dpr;
      const n = Math.round(Math.min(70, W * H / 16000));
      parts = Array.from({ length: n }, () => spark(true));
    }
    function spark(any) {
      return { x: Math.random() * W, y: any ? Math.random() * H : H + 10, v: 8 + Math.random() * 26, r: 0.6 + Math.random() * 1.8,
        a: 0.25 + Math.random() * 0.6, ph: Math.random() * 6.28, tint: Math.random() < 0.55 };
    }
    function makeBolt() {
      const pts = []; let x = W * (0.1 + Math.random() * 0.8), yy = -10;
      while (yy < H * (0.55 + Math.random() * 0.4)) { pts.push([x, yy]); x += (Math.random() - 0.5) * 70; yy += 18 + Math.random() * 34; }
      const br = []; const k = Math.min(pts.length - 1, 2 + Math.floor(Math.random() * Math.max(1, pts.length - 3)));
      let bx = pts[k][0], by = pts[k][1];
      for (let j = 0; j < 5; j++) { br.push([bx, by]); bx += (Math.random() - 0.3) * 50; by += 20 + Math.random() * 25; }
      return { pts, br, t: 0 };
    }
    function path(p) { ctx.beginPath(); ctx.moveTo(p[0][0], p[0][1]); for (let i = 1; i < p.length; i++) ctx.lineTo(p[i][0], p[i][1]); }
    function tick(now) {
      requestAnimationFrame(tick);
      const dt = Math.min(0.05, (now - last) / 1000); last = now;
      if (!visible || document.hidden) return;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, W, H);
      nextBolt -= dt;
      if (nextBolt <= 0) { bolt = makeBolt(); nextBolt = 3.5 + Math.random() * 5; }
      if (bolt) {
        bolt.t += dt;
        const a = bolt.t < 0.06 ? 1 : bolt.t < 0.1 ? 0.3 : bolt.t < 0.16 ? 0.9 : Math.max(0, 0.9 - (bolt.t - 0.16) * 2.4);
        if (a <= 0) bolt = null;
        else {
          ctx.fillStyle = `rgba(${glowC},${a * 0.07})`; ctx.fillRect(0, 0, W, H);
          ctx.lineJoin = 'round';
          ctx.strokeStyle = `rgba(${glowC},${a * 0.35})`; ctx.lineWidth = 7; path(bolt.pts); ctx.stroke();
          ctx.strokeStyle = `rgba(240,236,255,${a})`; ctx.lineWidth = 1.8; path(bolt.pts); ctx.stroke();
          ctx.strokeStyle = `rgba(220,210,255,${a * 0.6})`; ctx.lineWidth = 1; path(bolt.br); ctx.stroke();
        }
      }
      const t = now / 1000;
      for (const p of parts) {
        p.y -= p.v * dt; p.x += Math.sin(t + p.ph) * 6 * dt;
        if (p.y < -10) Object.assign(p, spark(false));
        const tw = p.a * (0.6 + 0.4 * Math.sin(t * 2.2 + p.ph));
        ctx.fillStyle = p.tint ? `rgba(${sparkC},${tw})` : `rgba(255,255,255,${tw})`;
        ctx.fillRect(p.x, p.y, p.r, p.r);
      }
    }
    size(); addEventListener('resize', size);
    if ('IntersectionObserver' in window) new IntersectionObserver(es => { visible = es[0].isIntersecting; }).observe(cv);
    requestAnimationFrame(tick);
  });
})();
