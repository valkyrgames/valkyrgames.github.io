(function () {
  const root = document.documentElement;
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Botón ES / EN: guarda la elección y cambia el título de la pestaña
  function setLang(l) {
    root.classList.toggle('en', l === 'en');
    root.lang = l;
    const t = root.dataset['title' + (l === 'en' ? 'En' : 'Es')];
    if (t) document.title = t;
    try { localStorage.setItem('vg-lang', l); } catch (e) {}
  }
  setLang(root.classList.contains('en') ? 'en' : 'es');
  document.querySelectorAll('[data-set]').forEach(b => b.addEventListener('click', () => setLang(b.dataset.set)));
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Pantalla de carga: una vez por visita
  const boot = document.querySelector('.boot');
  if (boot && !root.classList.contains('booted')) {
    setTimeout(() => { boot.classList.add('out'); try { sessionStorage.setItem('vg-boot', '1'); } catch (e) {} }, 1550);
  }

  // Aparecer al bajar
  const rv = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !calm) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    rv.forEach(el => io.observe(el));
  } else rv.forEach(el => el.classList.add('in'));

  // Tarjetas que se inclinan con el mouse
  if (matchMedia('(hover: hover)').matches && !calm) {
    document.querySelectorAll('a.game').forEach(c => {
      c.addEventListener('pointermove', e => {
        const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        c.style.setProperty('--ry', ((x - 0.5) * 7).toFixed(2) + 'deg');
        c.style.setProperty('--rx', ((0.5 - y) * 7).toFixed(2) + 'deg');
        c.style.setProperty('--mx', (x * 100).toFixed(1) + '%');
        c.style.setProperty('--my', (y * 100).toFixed(1) + '%');
      });
      c.addEventListener('pointerleave', () => { c.style.setProperty('--rx', '0deg'); c.style.setProperty('--ry', '0deg'); });
    });
  }

  // Celular: pasa capturas del juego con un relámpago en cada cambio
  document.querySelectorAll('[data-slides]').forEach(scr => {
    const imgs = scr.querySelectorAll('img'), zap = scr.querySelector('.zap');
    if (imgs.length < 2 || calm) return;
    let i = 0;
    setInterval(() => {
      if (document.hidden || scr.closest('.live')) return;
      imgs[i].classList.remove('on'); i = (i + 1) % imgs.length; imgs[i].classList.add('on');
      if (zap) { zap.classList.remove('go'); void zap.offsetWidth; zap.classList.add('go'); }
    }, 2800);
  });

  // Jugar adentro del celular (en pantallas grandes); en el celu abre el juego a pantalla completa
  const live = document.querySelector('.phone.live');
  if (live) live.addEventListener('click', e => {
    if (innerWidth < 900 || live.querySelector('iframe')) return;
    e.preventDefault();
    const f = document.createElement('iframe');
    f.src = live.getAttribute('href'); f.title = 'Relámpago'; f.allow = 'autoplay; fullscreen';
    live.querySelector('.screen').replaceChildren(f);
    const fs = document.querySelector('.fs'); if (fs) fs.classList.add('on');
    setTimeout(() => f.focus({ preventScroll: true }), 300);
  });

  // Fondo vivo: chispas que suben y rayos que caen cada tanto
  const cv = document.getElementById('fx');
  if (cv && !calm) {
    const ctx = cv.getContext('2d');
    let W = 0, H = 0, dpr = 1, parts = [], bolt = null, nextBolt = 1.8, last = performance.now(), visible = true;
    function size() {
      dpr = Math.min(devicePixelRatio || 1, 2);
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = W * dpr; cv.height = H * dpr;
      const n = Math.round(Math.min(70, W * H / 16000));
      parts = Array.from({ length: n }, () => spark(true));
    }
    function spark(any) {
      return { x: Math.random() * W, y: any ? Math.random() * H : H + 10, v: 8 + Math.random() * 26, r: 0.6 + Math.random() * 1.8,
        a: 0.25 + Math.random() * 0.6, ph: Math.random() * 6.28, blue: Math.random() < 0.55 };
    }
    function makeBolt() {
      const pts = []; let x = W * (0.1 + Math.random() * 0.8), yy = -10;
      while (yy < H * (0.55 + Math.random() * 0.4)) { pts.push([x, yy]); x += (Math.random() - 0.5) * 70; yy += 18 + Math.random() * 34; }
      const br = []; const k = 2 + Math.floor(Math.random() * Math.max(1, pts.length - 3));
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
          ctx.fillStyle = `rgba(120,150,255,${a * 0.07})`; ctx.fillRect(0, 0, W, H);
          ctx.lineJoin = 'round';
          ctx.strokeStyle = `rgba(90,130,255,${a * 0.35})`; ctx.lineWidth = 7; path(bolt.pts); ctx.stroke();
          ctx.strokeStyle = `rgba(235,240,255,${a})`; ctx.lineWidth = 1.8; path(bolt.pts); ctx.stroke();
          ctx.strokeStyle = `rgba(200,215,255,${a * 0.6})`; ctx.lineWidth = 1; path(bolt.br); ctx.stroke();
        }
      }
      const t = now / 1000;
      for (const p of parts) {
        p.y -= p.v * dt; p.x += Math.sin(t + p.ph) * 6 * dt;
        if (p.y < -10) Object.assign(p, spark(false));
        const tw = p.a * (0.6 + 0.4 * Math.sin(t * 2.2 + p.ph));
        ctx.fillStyle = p.blue ? `rgba(107,155,255,${tw})` : `rgba(255,255,255,${tw})`;
        ctx.fillRect(p.x, p.y, p.r, p.r);
      }
    }
    size(); addEventListener('resize', size);
    if ('IntersectionObserver' in window) new IntersectionObserver(es => { visible = es[0].isIntersecting; }).observe(cv);
    requestAnimationFrame(tick);
  }
})();
