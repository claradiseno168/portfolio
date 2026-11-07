/* Portfolio Clara de Ezcurra — interacciones (réplica de las animaciones de Webflow) */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var doc = document.documentElement;
  if (!reduce.matches) doc.classList.add('js-motion');

  /* ---------- Menú mobile accesible ---------- */
  var nav = document.querySelector('.w-nav');
  var btn = nav && nav.querySelector('.w-nav-button');
  var menu = nav && nav.querySelector('.w-nav-menu');
  function setMenu(open) {
    if (!nav) return;
    nav.classList.toggle('is-open', open);
    btn.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  }
  if (btn && menu) {
    btn.addEventListener('click', function () { setMenu(!nav.classList.contains('is-open')); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { setMenu(false); btn.focus(); }
    });
    document.addEventListener('click', function (e) {
      if (nav.classList.contains('is-open') && !nav.contains(e.target)) setMenu(false);
    });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    window.matchMedia('(min-width: 768px)').addEventListener('change', function (m) { if (m.matches) setMenu(false); });
  }

  /* ---------- Marca la página actual en el menú ---------- */
  var here = location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('.w-nav-link').forEach(function (a) {
    var href = (a.getAttribute('href') || '').replace(/\/$/, '') || '/';
    if (href === here) a.setAttribute('aria-current', 'page');
  });

  if (reduce.matches) {
    initLottie(true);
    return;
  }

  /* ---------- Scroll suave (Lenis, lerp 0.07 como en Webflow) ---------- */
  var lenis = null;
  if (window.Lenis) {
    lenis = new Lenis({ lerp: 0.07 });
    (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0);
    // Los anclas internos (p. ej. "Saltar al contenido") también se mueven con Lenis
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function () {
        var target = document.querySelector(a.getAttribute('href'));
        if (target) lenis.scrollTo(target, { immediate: true });
      });
    });
  }

  /* ---------- Aparición al hacer scroll ---------- */
  var reveals = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-revealed'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -1% 0px', threshold: 0 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-revealed'); });
  }
  // Si el foco del teclado llega a un elemento todavía oculto, se muestra al instante
  document.addEventListener('focusin', function (e) {
    var r = e.target.closest('[data-reveal]');
    if (r) r.classList.add('is-revealed');
  });

  /* ---------- Navbar que se esconde al bajar ---------- */
  var hideHost = document.querySelector('[data-hide-on-scroll]');
  if (hideHost) {
    var lastY = window.scrollY, ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var y = window.scrollY;
        if (Math.abs(y - lastY) > 2) {
          hideHost.classList.toggle('nav-hidden', y > lastY && y > 96 && !(nav && nav.classList.contains('is-open')));
          lastY = y;
        }
        ticking = false;
      });
    }, { passive: true });
  }

  /* ---------- Parallax con el mouse (±32px) ---------- */
  var par = document.querySelectorAll('[data-parallax]');
  if (par.length && window.matchMedia('(hover: hover)').matches) {
    window.addEventListener('mousemove', function (e) {
      var px = e.clientX / window.innerWidth, py = e.clientY / window.innerHeight;
      var x = 32 - 64 * px, y = -32 + 64 * py;
      par.forEach(function (el) { el.style.transform = 'translate3d(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px,0)'; });
    }, { passive: true });
  }

  initLottie(false);

  /* ---------- Lottie controlado por scroll (Carbique) ---------- */
  function initLottie(staticEnd) {
    var holders = document.querySelectorAll('[data-lottie]');
    if (!holders.length || !window.lottie) return;
    holders.forEach(function (el) {
      var anim = lottie.loadAnimation({
        container: el, renderer: 'svg', loop: false, autoplay: false,
        path: el.getAttribute('data-lottie'),
        rendererSettings: { preserveAspectRatio: 'xMidYMid meet', progressiveLoad: true }
      });
      anim.addEventListener('DOMLoaded', function () {
        var svg = el.querySelector('svg');
        if (svg) { svg.setAttribute('aria-hidden', 'true'); svg.setAttribute('focusable', 'false'); }
        var total = anim.totalFrames;
        if (staticEnd) { anim.goToAndStop(Math.round(total * 0.6), true); return; }
        // Equivale a "while scrolling in view": 30% → frame 0, 100% → 60% de la animación
        function update() {
          var r = el.getBoundingClientRect(), vh = window.innerHeight;
          var p = (vh - r.top) / (vh + r.height);
          p = Math.min(1, Math.max(0, p));
          var k = p <= 0.3 ? 0 : (p - 0.3) / 0.7;
          anim.goToAndStop(k * 0.6 * (total - 1), true);
        }
        update();
        window.addEventListener('scroll', update, { passive: true });
        window.addEventListener('resize', update);
      });
    });
  }
})();
