// Botón ES / EN: guarda la elección y cambia el título de la pestaña
(function () {
  const root = document.documentElement;
  function set(l) {
    root.classList.toggle('en', l === 'en');
    root.lang = l;
    const t = root.dataset['title' + (l === 'en' ? 'En' : 'Es')];
    if (t) document.title = t;
    try { localStorage.setItem('vg-lang', l); } catch (e) {}
  }
  set(root.classList.contains('en') ? 'en' : 'es');
  document.querySelectorAll('[data-set]').forEach(b => b.addEventListener('click', () => set(b.dataset.set)));
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
