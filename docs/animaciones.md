# Animaciones del portfolio (extraídas de Webflow IX2, sitio publicado)

Fuente: `Webflow.require('ix2').store.getState().ixData` en clarasportfolio.webflow.io — 188 eventos, 29 action lists.

## 1. Aparición al hacer scroll (reveal) — la más usada (~140 elementos, todas las páginas)
Estado inicial: `translateY(60px)` + `opacity: 0`. Al entrar en viewport (offset 0%, en el hero 10%):
| Variante | Duración | Delay | Easing movimiento | Easing opacidad |
|---|---|---|---|---|
| d.00 (a-8) | 1200ms | 0 | outQuart | easeIn |
| d.03 (a-9) | 1100ms | 300ms | outQuart | easeIn |
| d.06 (a-10) | 1000ms | 600ms | outQuart | easeIn |
| d.09 (a-28) | 1000ms | 900ms | outQuart | easeIn |
Se usa en cascada (d.00 → d.03 → d.06) en grupos de 3 (cards del home, herramientas, "Beyond Product Design", contadores del About, estadísticas de Applica).

## 2. Parallax con el mouse (a-5)
Foto del hero (Home) y foto del About. Sigue el mouse en toda la página:
- Eje X: mouse a la izquierda → +32px, a la derecha → −32px.
- Eje Y: mouse arriba → −32px, abajo → +32px.

## 3. Navbar que se esconde (a-13 / a-16) — Home y About
- Scroll hacia abajo → `translateY(-100px)` 400ms outQuad.
- Scroll hacia arriba → `translateY(0)` 400ms inQuad.

## 4. Hover en cards de proyectos (a-24 / a-25)
Imágenes de los 3 proyectos del Home y las 3 cards de "Featured Work":
- Hover in: `scale(1.05)` 300ms easeInOut.
- Hover out: `scale(1)` 300ms easeInOut.

## 5. Botón "Let's talk" del navbar (a-51 / a-52) — solo desktop
- Fondo `.button4_bg-2`: ancho 0% → 100%, 500ms outCirc (sale desde el círculo).
- Texto: #111 → blanco, 200ms outCirc.
- Flecha: `translateX(0.5em)`, 500ms outCirc.
- Hover out: fondo 0% (500ms), texto #111 (500ms), flecha 0 (400ms).

## 6. Botón "See my full project" (a-42 / a-43)
- Flecha `.flecha-boton` rota 40°, 200ms easeOut; vuelve a 0° al salir.

## 7. Lottie de Carbique (a-44)
Controlado por scroll: entre el 30% y el 100% del recorrido del elemento en pantalla avanza del frame 0% al 60%.

## 8. Global
- Lenis smooth scroll en todas las páginas, `lerp: 0.07`.

## No usadas (apuntan a elementos que ya no existen en las páginas)
a-3/a-4, a-14/a-15 (.icono-flecha), a-17/a-18 (.card), a-29 (botón download), a-31/a-32 (navbar viejo).

## Accesibilidad (agregado en la versión nueva)
Con `prefers-reduced-motion: reduce`: sin reveal (contenido visible directo), sin parallax, sin Lenis, navbar fijo, Lottie en frame final estático.
