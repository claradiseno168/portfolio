#!/usr/bin/env python3
"""Genera las páginas HTML estáticas del portfolio.
Uso: python3 tools/build.py   (desde la raíz del repo)
El contenido y las clases replican el sitio de Webflow; la semántica está corregida
(jerarquía de títulos, textos alternativos, landmarks, navegación por teclado)."""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = json.load(open(os.path.join(ROOT, 'tools', 'assets.json'), encoding='utf-8'))
SITE = 'https://clarasportfolio.vercel.app'
EMAIL = 'claradiseno168@gmail.com'
BEHANCE_APPLICA = 'https://www.behance.net/gallery/206983929/Proyecto-final-UxUI-Coder-House'
GMAIL = f'https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to={EMAIL}'
NEWTAB_GMAIL = '<span class="sr-only"> (opens Gmail in a new tab)</span>'
CARBIQUE_LIVE = 'https://carbique-bottle-water.webflow.io/'

def A(aid):
    return '/' + ASSETS[aid]['local']

def img(aid, cls='', alt='', eager=False, extra=''):
    c = f' class="{cls}"' if cls else ''
    load = 'eager" fetchpriority="high' if eager else 'lazy'
    return f'<img src="{A(aid)}"{c} alt="{html.escape(alt, quote=True)}" loading="{load}" decoding="async"{extra}>'

def R(v=0):
    """Aparición al hacer scroll: 0=d.00, 1=d.03, 2=d.06, 3=d.09"""
    return ' data-reveal' if v == 0 else f' data-reveal="{v}"'

# ---------------------------------------------------------------- piezas comunes
def head(title, desc, path, extra=''):
    d = f'<meta name="description" content="{html.escape(desc, quote=True)}">' if desc else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
{d}
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta property="og:title" content="{html.escape(title, quote=True)}">
{f'<meta property="og:description" content="{html.escape(desc, quote=True)}">' if desc else ''}
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{path}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/league-spartan-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/poppins-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/js/vendor/lenis.css">
<link rel="stylesheet" href="/css/base.css">
<link rel="stylesheet" href="/css/site.css">
{extra}
</head>'''

NAV = f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="navbar-4 w-nav">
  <div class="container-12 w-container">
    <a href="/" class="brand w-nav-brand" aria-label="Clara de Ezcurra, home">
      <div class="lgobrand" aria-hidden="true">cd.</div>
      <div class="text-block-25">Product designer</div>
    </a>
    <nav class="nav-menu-2 w-nav-menu" id="nav-menu" aria-label="Main">
      <a href="/about-me" class="nav-link w-nav-link">About</a>
      <a href="/#work" class="nav-link w-nav-link">Work</a>
      <div class="w-layout-hflex flex-block-48">
        <a href="{GMAIL}" class="button4-3 w-inline-block" target="_blank" rel="noopener">
          <div class="button4_circle-3">{img('6a122b95b4c33bf17f386be2', 'button2_icon-2', '', eager=True)}</div>
          <div class="button4_text-3">Let's talk{NEWTAB_GMAIL}</div>
          <div class="button4_bg-2" aria-hidden="true"></div>
        </a>
      </div>
    </nav>
    <button type="button" class="menu-button-2 w-nav-button" aria-controls="nav-menu" aria-expanded="false" aria-label="Open menu">
      {img('67b505e43dc3bf76cfbc0050', 'image-33', '', eager=True)}
    </button>
  </div>
</header>'''

FOOTER = f'''<footer class="footer-black">
  <div class="contenedor-principal-footer">
    <div class="w-layout-blockcontainer container-left-footer w-container">
      <div class="wrapper-get-in-touch">
        <h2 class="heading-15 as-h1">Interested in working together?</h2>
        <a href="{GMAIL}" class="footer-button w-button" target="_blank" rel="noopener">Get in Touch{NEWTAB_GMAIL}</a>
        <ul class="w-layout-hflex wrapper-figma" role="list" style="list-style:none;margin:0;padding:0">
          <li><a href="https://www.linkedin.com/in/clara-de-ezcurra-6296ba208/" class="w-inline-block" target="_blank" rel="noopener">{img('67b89d28336baea608632e98', 'image-10', 'LinkedIn (opens in a new tab)')}</a></li>
          <li><a href="https://www.behance.net/claradiseo" class="w-inline-block" target="_blank" rel="noopener">{img('67b89d60f9a79e5d617b1d8a', 'image-12', 'Behance (opens in a new tab)')}</a></li>
          <li><a href="https://t.me/claradeezcurra" class="w-inline-block" target="_blank" rel="noopener">{img('67c5dfd8311103d1bea06ae4', 'image-11', 'Telegram (opens in a new tab)')}</a></li>
        </ul>
      </div>
    </div>
    <div class="w-layout-blockcontainer container-5 w-container">
      <div class="wrapper-logo-f">
        <div class="text-block-6">Product designer</div>
        <p class="heading-16 as-h1" aria-hidden="true">cd.</p>
      </div>
      <address class="w-layout-vflex wrapper-datos" style="font-style:normal">
        <div class="text-block-7">Buenos aires, Argentina</div>
        <a class="text-block-7" href="mailto:{EMAIL}" style="text-decoration:none">{EMAIL}</a>
        <a class="text-block-7" href="tel:+5491160349523" style="text-decoration:none">+54&#8209;91160349523</a>
      </address>
    </div>
  </div>
</footer>'''

SCRIPTS = '''<script src="/js/vendor/lenis.min.js" defer></script>
{lottie}<script src="/js/main.js" defer></script>
</body>
</html>'''

def page(fname, title, desc, path, body, hide_nav=False, lottie=False, body_cls='carbique'):
    attrs = f' class="{body_cls}"' + (' data-hide-on-scroll' if hide_nav else '')
    out = head(title, desc, path) + f'\n<body{attrs}>\n' + NAV + '\n<main id="main" tabindex="-1">\n' + body + '\n</main>\n' + FOOTER + '\n' + SCRIPTS.format(lottie='<script src="/js/vendor/lottie_light.min.js" defer></script>\n' if lottie else '')
    with open(os.path.join(ROOT, fname), 'w', encoding='utf-8') as f:
        f.write(out)
    print('ok', fname)

def see_full(href, label):
    return f'''<a href="{href}" class="boton-see c-boton w-inline-block" target="_blank" rel="noopener"{R()}>
        <div class="text-block-36">See my full project<span class="sr-only">: {label} (opens in a new tab)</span></div>
        <div class="div-block-33">{img('68d6a4ea3de1c7b7c21f3fed', 'flecha-boton', '')}</div>
      </a>'''

def case_header(banner_cls, title, kind, crumb, meta, intro, intro_tablet, banner_id, banner_alt, tools):
    meta_html = '\n'.join(f'<div class="text-block-31">{m}</div>' for m in meta)
    tools_html = '\n'.join(img(t[0], t[1], t[2]) for t in tools)
    return f'''<div class="w-layout-vflex banner {banner_cls}">
  <div class="w-layout-vflex flex-block-32">
    <h1 class="heading-29 as-h3">{title}</h1>
    <div class="text-block-30">{kind}</div>
  </div>
</div>
<div class="w-layout-hflex flex-block-33">
  <nav class="w-layout-vflex flex-block-34" aria-label="Breadcrumb">
    <a href="/#work" class="link">FEATURED WORK /</a>
    <a href="#main" class="link-2" aria-current="page">{crumb}</a>
  </nav>
  <div class="w-layout-vflex flex-block-35">
    {meta_html}
  </div>
</div>
<p class="text-large light introducing{' tablet' if intro_tablet else ''}"{R()}>{intro}</p>
<div class="w-layout-vflex flex-block-36">
  {img(banner_id, 'banner-image' + (' carbique' if banner_cls == 'carbiqiue' else ''), banner_alt, eager=True, extra=R())}
  <div class="w-layout-hflex flex-block-37"{R()}>
    {tools_html}
  </div>
</div>'''

def tool(aid, cls, name):
    return (aid, cls, f'Tool used: {name}')

def block39(title, text, title_reveal=True, text_reveal=True):
    return f'''<div class="w-layout-vflex flex-block-39">
    <h2 class="heading-30 as-h4"{R() if title_reveal else ''}>{title}</h2>
    <p class="text-block-33"{R() if text_reveal else ''}>{text}</p>
  </div>'''

def section41(title, color, text, inner, title_cls='flex-block-10', title_wrap_reveal=True, text_reveal=True, title_reveal=True):
    t = f'<p class="text-block-34"{R() if text_reveal else ""}>{text}</p>' if text else ''
    return f'''<section class="w-layout-vflex flex-block-41">
  <div class="w-layout-vflex {title_cls}"{R() if title_wrap_reveal else ''}>
    <h2 class="heading-19 {color} as-h3"{R() if title_reveal else ''}>{title}</h2>
  </div>
  {t}
  {inner}
</section>'''

# ---------------------------------------------------------------- HOME
def home():
    def step(n, title, text, largo=False, reveal=True):
        return f'''<div class="w-layout-hflex flex-block-14"{R() if reveal else ''}>
          <p class="heading-20 as-h4" aria-hidden="true">{n}</p>
          <div class="w-layout-vflex flex-block-12">
            <div class="w-layout-vflex flex-block-13"><h4 class="heading-22{' largo' if largo else ''} as-h5"><span class="sr-only">{n} </span>{title}</h4></div>
            <p class="paragraph">{text}</p>
          </div>
        </div>'''
    def toolcard(aid, name, sub, r):
        return f'''<li class="w-layout-hflex flex-block-16"{r}>
            {img(aid, 'image-38', '')}
            <div class="w-layout-hflex flex-block-18">
              <p class="paragraph-3">{name}</p>
              <p class="paragraph-4">{sub}</p>
            </div>
          </li>'''
    line = img('67b3ca93bcd35b8eb468a129', 'image-35', '')
    body = f'''<section class="hero-section tablet" aria-labelledby="hero-title">
  <div class="heading-wrapper tablet">
    <p class="hero-heading tablet as-h5"{R(1)}>Hello!</p>
    <div class="div-block-7">
      <h1 id="hero-title" class="heading-2 tablet"{R()}>I am Clara de Ezcurra</h1>
      <p class="text-xlarge light tablet"{R()}>UX/UI &amp; Product Designer crafting intuitive interfaces for web and mobile products.</p>
    </div>
  </div>
  <div class="div-block-8 tablet">
    <div data-parallax>{img('67b367d6f199a003d23c5b06', 'image tablet', 'Portrait of Clara de Ezcurra with additional personal photos of nature and the beach', eager=True, extra=R(1))}</div>
  </div>
</section>
<section class="w-layout-blockcontainer contenedor w-container" aria-labelledby="intro-title">
  <h2 id="intro-title" class="heading-introudcing tablet"{R()}>Introducing Myself</h2>
  <p class="text-large light introducing tablet"{R()}>I design digital experiences that are clear, intuitive and visually polished.My work combines UX thinking, interface design and scalable visual systems to help products feel easier to use.</p>
</section>
<div class="w-layout-blockcontainer container-13 w-container">
  <div class="w-layout-hflex flex-block-9 hover-zoom"{R()}>{img('68d1d4e7781fc45c1fa7ff4a', 'image-34', 'Homepage design for Ezyer website with black background and white logo')}</div>
  <div class="w-layout-hflex flex-block-9 hover-zoom"{R(1)}>{img('68d1d6213025be05b1f449aa', 'image-34', 'Mobile app interface showing Applica financial management dashboard')}</div>
  <div class="w-layout-hflex flex-block-9 hover-zoom"{R(2)}>{img('68d1d63fd07b756a6a6fa7e3', 'image-34', '3D render of Carbique bottle product showcased on dark background')}</div>
</div>
<section class="w-layout-hflex container-14" aria-labelledby="process-title">
  <div class="w-layout-vflex flex-block-10 home"{R()}>
    <h3 id="process-title" class="heading-19">My Design Process</h3>
    {line}
  </div>
  <div class="w-layout-hflex flex-block-11 _1">
    {step('01.', 'User Research', 'I start by understanding the product, the users and the context through benchmarks, analysis and key insights.')}
    {step('02.', 'User-Centered Design', 'I organize the experience through information architecture, task flows and user flows before moving into interface design.', largo=True)}
  </div>
  <div class="w-layout-hflex flex-block-11">
    {step('03.', 'Prototyping', 'I create wireframes and interactive prototypes to test ideas, refine interactions and improve usability.')}
    {step('04.', 'Responsive &amp; Accessible', 'I design polished interfaces and reusable components to keep the experience clear, consistent and scalable.', largo=True)}
  </div>
</section>
<section class="w-layout-vflex container-15" aria-labelledby="tools-title">
  <div class="w-layout-vflex flex-block-10 home"{R()}>
    <h3 id="tools-title" class="heading-19">Essencials Tools</h3>
    {line}
  </div>
  <div class="w-layout-hflex flex-block-15">
    <ul class="w-layout-hflex flex-block-17" role="list" style="list-style:none;margin:0;padding:0"{R()}>
      {toolcard('67ae2e5777fc1a4f2176844a', 'Figma', 'Design Tool', R())}
      {toolcard('67ae344b33299da66de775b0', 'Webflow', 'No code tool', R(1))}
      {toolcard('6a12352b23be8647e995f497', 'Framer', 'Interactive websites', R(2))}
    </ul>
    <ul class="w-layout-hflex flex-block-17" role="list" style="list-style:none;margin:0;padding:0"{R()}>
      {toolcard('6a1236b55d4aa63df29efef5', 'Adobe ', 'Design tools', R())}
      {toolcard('6a123ab5418a4b94fd72cd28', 'AI Tools', 'AI workflows', R(1))}
      {toolcard('67ae33bc33299da66de6ed6d', 'Optimal Workshop', 'Ux tool', R(2))}
    </ul>
  </div>
</section>
<section id="work" class="w-layout-hflex container-16" aria-labelledby="work-title">
  <div class="w-layout-vflex flex-block-10 home"{R()}>
    <h3 id="work-title" class="heading-19">Featured Work</h3>
    {line}
  </div>
  <div class="w-layout-hflex flex-block-19">
    <a href="/applica" class="flex-block-20 w-inline-block hover-zoom"{R()}>
      <div class="w-layout-vflex flex-block-21">
        <div class="text-block-28 app">Applica</div>
        <div class="text-block-29">App-approach</div>
      </div>
      {img('67b48dfcf7be58d9970e5ed2', 'image-39', '')}
    </a>
    <div class="w-layout-hflex flex-block-22">
      <a href="/carbique" class="flex-block-23 w-inline-block hover-zoom"{R()}>
        <div class="w-layout-vflex flex-block-21">
          <div class="text-block-28">Carbique</div>
          <div class="text-block-29">Web-approach</div>
        </div>
        {img('67b48dfcf7be58d9970e5ed2', 'image-40', '')}
      </a>
      <a href="/case-of-stufy" class="case-of-study w-inline-block hover-zoom"{R(1)}>
        {img('67b48dfcf7be58d9970e5ed2', 'image-40', '')}
        <div class="w-layout-vflex flex-block-21">
          <div class="text-block-28">Case of Study</div>
          <div class="text-block-29">App &amp; Web</div>
        </div>
      </a>
    </div>
  </div>
</section>
<section class="w-layout-vflex flex-block-24" aria-labelledby="beyond-title">
  <h3 id="beyond-title" class="heading-19"{R()}>Beyond Product Design</h3>
  <ul class="w-layout-hflex flex-block-26" role="list" style="list-style:none;margin:0;padding:0">
    <li class="w-layout-vflex flex-block-27"{R()}>
      {img('68d3f9e705dfa0e5f7a19545', 'image-41', 'Coffee cups mockup with Bocado Café branding', extra=R())}
      <h4 class="heading-24">Graphic design</h4>
    </li>
    <li class="w-layout-vflex flex-block-27"{R(1)}>
      {img('68d3fb6bd72daea6e05f9b42', 'image-41', 'Branding proposal for Bocado Café including cups, menu, and graphic design', extra=R(1))}
      <h4 class="heading-24">Branding</h4>
    </li>
    <li class="w-layout-vflex flex-block-27"{R(2)}>
      {img('68d3fb86029a071ce89bd195', 'image-41', '3D design of black hoodies with futuristic illustrations', extra=R(2))}
      <h4 class="heading-24">3D Apparel Design</h4>
    </li>
  </ul>
</section>
<section class="w-layout-vflex flex-block-28" aria-labelledby="cta-title"{R()}>
  <div class="w-layout-vflex flex-block-29">
    <p class="heading-26 as-h5">Want to start a project?</p>
    <h2 id="cta-title" class="heading-28 as-h1">Let´s Talk</h2>
    <a href="{GMAIL}" class="button w-button" target="_blank" rel="noopener">Get in Touch{NEWTAB_GMAIL}</a>
  </div>
</section>'''
    page('index.html', 'Clara de Ezcurra | Product Designer Portfolio',
         'Product Designer focused on creating functional, aesthetic, and user-centered digital experiences. Portfolio showcasing UI, UX, and web design projects.',
         '/', body, hide_nav=True, body_cls='body')

# ---------------------------------------------------------------- ABOUT
def about():
    def stat(n, label, r, cls):
        return f'''<div class="w-layout-vflex datos"{r}>
        <div class="w-layout-hflex flex-block-8">
          {img('67c618797e3b430e58a5a1a8', cls, '')}
          <p class="heading-18 as-h1" data-count="{n}">{n}<span class="sr-only"> or more</span></p>
        </div>
        <div class="text-block-20">{label}</div>
      </div>'''
    body = f'''<h1 class="sr-only">About me</h1>
<div class="w-layout-blockcontainer hero-section about-me w-container"{R()}>
  <div class="w-layout-blockcontainer container-7 w-container">
    <div class="w-layout-vflex flex-block-5">
      <p class="text-block-19"{R()}>Hi! I’m Clara de Ezcurra, a UX/UI Designer passionate about crafting meaningful digital experiences. I’m curious, empathetic, and love connecting with others—whether it’s through work or in everyday life. Outside of design, I’m all about soccer, spending time in nature, and finding balance between my family, friends, and boyfriend. For me, great design comes from understanding people and staying inspired by the world around us. In the end, everything is design.</p>
    </div>
    <div class="div-block-30"{R(1)}>
      <div data-parallax>{img('68d42bc47f2b8e78dbb7b9da', 'image-22', 'Photo of Clara de Ezcurra', eager=True)}</div>
    </div>
  </div>
</div>
<section class="w-layout-hflex container-6" aria-labelledby="exp-title">
  <div class="w-layout-vflex flex-block-4"{R()}>
    <h2 id="exp-title" class="heading-17 as-h3"{R()}>About My Experience</h2>
    <div class="w-layout-hflex linea-titulo grpahic"{R()} aria-hidden="true"></div>
  </div>
  <div class="w-layout-hflex flex-block-6">
    {stat(20, 'Projects', R(), 'image-25')}
    {stat(25, 'Clients', R(1), 'image-26')}
    {stat(10, 'Tools', R(2), 'image-27')}
    {stat(8, 'Courses', R(3), 'image-28')}
  </div>
</section>'''
    page('about-me.html', 'About me', 'Clara de Ezcurra, UX/UI and Product Designer from Buenos Aires: experience, projects and tools.',
         '/about-me', body, hide_nav=True, body_cls='body-4')

# ---------------------------------------------------------------- APPLICA
def applica():
    s = lambda t: f'<strong>{t}</strong>'
    hdr = case_header('applica', 'Applica', 'App design', 'APPLICA',
        ['Project for: Coder House.', 'Year: 2024.', 'Role: Product designer.', 'Supported OS: Android.'],
        'Applica is a mobile app designed to help young adults understand their spending habits, organize their monthly budget and build healthier saving routines.', False,
        '68d4701c2e16b13d8d82b78a', 'Mobile mockup of Applica app showing spending analysis and financial dashboard',
        [tool('68d47da5463d4c531686bcdf', 'image-52', 'Figma'), tool('68d47e9f15680631ae50b9f6', 'image-53', 'Optimal Workshop'),
         tool('68d47ec4bb7b376738ce296b', 'image-54', 'Whimsical'), tool('68d47efcb16249872058d1b7', 'image-55', 'Adobe Illustrator'),
         tool('68d47f127200212b7e3818cb', 'image-56', 'Adobe Photoshop')])
    stats = f'''<ul class="w-layout-hflex flex-block-43" role="list" style="list-style:none;margin:0;padding:0">
    <li class="w-layout-vflex flex-block-42"{R()}>{img('68d55f101108e6928338c161', 'image-47', '70%')}<div class="text-block-35">Of young people in Argentina are concerned about their financial situation.</div></li>
    <li class="w-layout-vflex flex-block-42"{R(1)}>{img('68d55fd5c95d68bf1e41ea7e', 'image-48 _2', '60%')}<div class="text-block-35">Of young people don't have a budget.</div></li>
    <li class="w-layout-vflex flex-block-42"{R(2)}>{img('68d55feb3fb040525aa025f9', 'image-49 _3', '50%')}<div class="text-block-35">Of young people in Argentina don't know how to save.</div></li>
  </ul>'''
    body = hdr + f'''
<div class="w-layout-vflex flex-block-38">
  {block39('Problem:', f"Many {s('young adults')} struggle to understand where their money goes each month. With multiple {s('payment methods')}, digital wallets and credit cards, tracking expenses becomes {s('fragmented ')}and {s('stressful')}.This lack of visibility makes it harder to plan, {s('save ')}and feel in {s('control ')}of personal finances.", title_reveal=True, text_reveal=True)}
  {block39('Goal:', f"Design a simple and {s('intuitive mobile app')} that helps young adults {s('track ')}expenses, {s('organize ')}budgets and {s('create ')}realistic saving goals from {s('one place.')}", title_reveal=False, text_reveal=True)}
  {block39('Designing the solution:', f"I designed a {s('mobile experience')} that centralizes {s('expense tracking')}, {s('budget planning and saving goals')}.The app helps users {s('categorize expenses')}, understand their {s('spending patterns ')}and make better {s('financial decisions')} through a clear and accessible interface.")}
</div>
<section class="w-layout-vflex flex-block-40">
  <div class="w-layout-vflex flex-block-10"{R()}>
    <h2 class="heading-19 violet centro as-h3"{R()}>My Process: Design Thinking</h2>
  </div>
  {img('68d55a44daeeb5e81e789188', 'image-44', 'Diagram of the Design Thinking process with five steps: Empathize, Define, Ideate, Prototype, and Test', extra=R())}
</section>
''' + section41('Emphatize', 'violet', f"I started with surveys and interviews to {s('validate the problem')} and understand how young adults manage their money.The research showed that financial stress was {s('not only related to income')}, but also to the lack of {s('simple tools')} for everyday organization.", stats, text_reveal=True) + '\n' + \
    section41('Define', 'violet', f"I created {s('user personas')} based on research insights, mapping their {s('motivations, frustrations and behaviors')}.I also analyzed direct and indirect competitors to identify opportunities and define a {s('focused MVP.')}",
              f'''<div class="w-layout-hflex lottie">{img('68d5632544927190b392c510', 'userflow-netflix', 'MVP features of Applica app including: create budget, create expense categories, set a savings goal, and link cards through secure login, with two mobile mockups showing categories and cards screens', extra=R())}</div>''') + '\n' + \
    section41('Ideate', 'violet', f"With the MVP defined, I designed the {s('information architecture, user flows and task flows ')}to create a clear and intuitive experience from onboarding to daily expense management.",
              f'''<div class="w-layout-hflex lottie task">
    <h3 class="heading-31 as-h4"{R()}>Taskflow:</h3>
    {img('68d568934baa96be46ab9e37', 'userflow-netflix', 'Task flow diagram showing the user journey: enter budget section, create budget, create categories, link card, add expenses, and set a savings goal', extra=R())}
  </div>
  <div class="w-layout-hflex lottie task">
    <h3 class="heading-31 as-h4"{R()}>Userflow:</h3>
    {img('68d5724274b62b46cc76723c', 'userflow-netflix', 'User flow diagram for Applica app showing the process from registration and login to creating budgets, linking cards, and setting savings goals', extra=R())}
  </div>''', title_wrap_reveal=True, title_reveal=False) + f'''
<div class="div-block-32">{img('68d589e2f147ecee9685019d', 'image-57', 'Four Applica app screens shown side by side', extra=R())}</div>
''' + section41('Prototyping', 'violet', f"I created {s('low and high-fidelity wireframes')} and {s('developed a UI ki')}t to maintain {s('consistency ')}across the product.The final prototype focused on{s(' clarity, accessibility and ease of use.')}",
              f'''<div class="w-layout-hflex lottie">{img('68d593600c6b3cfdb5d09d3c', 'userflow-netflix', 'Progression of Applica app screens from low fidelity wireframe to high fidelity design, showing iterations through design patterns and layout grids', extra=R())}</div>''') + '\n' + \
    section41('UI kit &amp; Design System', 'violet', f"I created a visual system with {s('reusable components')}, typography, colors, icons and interface {s('patterns ')}to keep the experience consistent across the app.",
              f'''<div class="w-layout-hflex lottie">{img('68d69f7620945fefcc8b8a93', 'userflow-netflix', 'Applica UI kit: colors, typography, icons and interface components', extra=R())}</div>''') + f'''
<div class="div-block-32">{img('68d6a168b55c2ae1fc4ba055', 'image-50', 'Three Applica app screens', extra=R())}</div>
''' + section41('Conclusion', 'violet', 'This project allowed me to apply a complete UX/UI process, from research and problem definition to high-fidelity prototyping.I strengthened my skills in product thinking, mobile interaction design and visual consistency while creating a solution focused on a real everyday problem.',
              see_full(BEHANCE_APPLICA, 'Applica on Behance'))
    page('applica.html', 'Applica', 'UX/UI: Applica financial management app for young people. Full design process from research to high-fidelity prototyping by Clara de Ezcurra.',
         '/applica', body)

# ---------------------------------------------------------------- CARBIQUE
def carbique():
    s = lambda t: f'<strong>{t}</strong>'
    hdr = case_header('carbiqiue', 'Carbique', 'Web design', 'CARBIQUE BOTTLE',
        ['Project for: Webflow University.', 'Year: 2024.', 'Rol: Product designer.', 'Supported OS:Responsive design.'],
        'This project was an opportunity to combine my UI design and 3D rendering skills. Without focusing on UX research, I aimed to build a visually impactful landing page using Webflow, integrating 3D visuals to enhance product presentation and interaction.', True,
        '68ebe85fdfeb716fdbb8b439', 'Carbique landing page design shown on desktop and mobile',
        [tool('68ebe97a50a3f0603bf1842f', 'image-58', 'Webflow'), tool('68d47da5463d4c531686bcdf', 'image-59', 'Figma'),
         tool('68ebea5e41b0d79431a426f1', 'image-60', 'SolidWorks'), tool('68d47efcb16249872058d1b7', 'image-61', 'Adobe Illustrator'),
         tool('68d47f127200212b7e3818cb', 'image-62', 'Adobe Photoshop')])
    body = hdr + f'''
<div class="w-layout-vflex flex-block-38">
  {block39('Problem:', f"Many landing pages for tech products lack visual impact or product realism. They often rely heavily on mockups or flat illustrations. I wanted to{s(' break that pattern')} by making the {s('product the centerpiece')}, using full 3D renders to bring it to life within a modern, responsive UI.")}
  {block39('Goal:', f"The main goal of this project was to focus entirely on {s('UI design')}—crafting a clean, elegant, and responsive interface that could support and elevate 3D visuals.  {s('This wasn’t a UX-centered project')}; instead, the priority was on exploring layout, hierarchy, visual systems, and how to integrate product renders into a compelling landing page experience.")}
  {block39('Desinging the solution:', f"The solution was to create a complete {s('design system')} with defined breakpoints, typography styles, iconography, 3D product visuals, and animations—all working together to deliver a cohesive and visually engaging experience.")}
</div>
<section class="w-layout-vflex flex-block-40 carbique">
  <div class="w-layout-vflex flex-block-10"{R()}>
    <h2 class="heading-19 violet as-h3"{R()}>Design System</h2>
  </div>
  <p class="text-block-38"{R()}>I started by defining my design system—establishing typography, color palette, 3D visuals, and iconography to ensure visual consistency across the entire interface.</p>
  <div class="div-block-34">{img('68ffa32e67fe8a4d3ab31097', 'ui-kit-carbique', 'Style guide showing Playfair Display and Inter fonts, black, violet, gray, and white color palette, UI components, press logos, and product mockups across devices.', extra=R())}</div>
</section>
''' + section41('Animation / lottie', 'violet', '', f'''<div class="w-layout-hflex lottie">
    <div class="lottie-animation-3" data-lottie="{A('69021238e0091a07aee9d697')}" role="img" aria-label="Animated 3D render of the Carbique bottle"></div>
  </div>''') + '\n' + \
    section41('Fidelitys', 'violet', 'Then, I moved on to wireframing my designs in Figma—starting with low fidelity to define structure, progressing through mid fidelity to refine layout, and finally reaching high fidelity to polish visual details and interactions.',
              img('6902226c6f98e5c3a3ace951', '', 'Carbique landing page in low, mid and high fidelity', extra=R())) + '\n' + \
    section41('Conclusion', 'violet', 'This project allowed me to explore the intersection of design and 3D visualization, resulting in a dynamic and visually engaging product showcase built entirely in Webflow.',
              see_full(CARBIQUE_LIVE, 'Carbique live website'))
    page('carbique.html', 'carbique', 'UI design project combining 3D rendering and Webflow development. Visually impactful landing page showcasing product design and interaction skills.',
         '/carbique', body, lottie=True)

# ---------------------------------------------------------------- CASE OF STUDY
def case():
    s = lambda t: f'<strong>{t}</strong>'
    hdr = case_header('case', 'Case of Study', 'Netflix', 'CASE OF STUDY',
        ['Project for: Coder House.', 'Year: 2023.', 'Role: Product designer.', 'Supported OS: IOS &amp; Android.'],
        'Users value experiences that adapt to their real viewing habits. Being able to mark what they’ve already watched would give them more control over their journey on the platform, helping avoid confusion and improving overall navigation.', True,
        '69022aaa0d1e7de05127b1b5', 'Netflix app screens redesigned with an option to mark content as watched',
        [tool('68d47da5463d4c531686bcdf', 'image-63', 'Figma'), tool('68d47efcb16249872058d1b7', 'image-64', 'Adobe Illustrator'),
         tool('68d47f127200212b7e3818cb', 'image-65', 'Adobe Photoshop')])
    body = hdr + f'''
<div class="w-layout-vflex flex-block-38">
  {block39('Problem:', f"When content is shared across profiles —whether with a partner, friends, or family— Netflix {s('doesn’t allow users to manually mark')} an episode, movie, or series as “watched”, which makes it harder to track progress and often leads to confusion.  Additionally, in the “Continue Watching” section, the only available action is to remove the content, but not to mark it as completed —{s('creating a pain point for users who want more control over their viewing history.')}")}
  {block39('User validation research:', f"User feedback on Reddit and app reviews shows a clear need for better control over viewing history. Many users mention {s('frustration with not being able to mark content as “watched”')} or clear completed titles.  Netflix even tested a “Watched it” button internally, according to WIRED, but never launched it—{s('confirming the relevance of this pain point.')}")}
  {block39('Desinging the solution:', f"I designed a solution that gives users more control over their viewing progress. By adding the option to {s('manually mark content as “watched”')} and improving actions within the Continue Watching section, {s('the experience becomes clearer and more flexible')}—especially in shared viewing contexts. These adjustments help streamline navigation and {s('reduce confusion.')}", text_reveal=False)}
</div>
''' + section41('User journey map', 'red', '', f'''<div class="w-layout-hflex lottie task">
    <h3 class="heading-31 as-h4"{R()}>Taskflow:</h3>
    {img('69022c35a1b0ed02091431a8', 'taskflow-netflix', 'Task flow diagram for marking a title as watched in the Netflix app', extra=R())}
  </div>
  <div class="w-layout-hflex lottie task">
    <h3 class="heading-31 as-h4"{R()}>Userflow:</h3>
    {img('69022c6750f32aaeaf69476a', 'userflow-netflix', 'User flow diagram for the Netflix "mark as watched" feature', extra=R())}
  </div>''') + '\n' + \
    section41('Prototyping', 'red', 'I designed low and high-fidelity wireframes and developed a custom UI kit for consistency.  Additionally, I created a full brand manual, including color palette, typography system, iconography, and voice and tone guidelines.',
              f'''<div class="w-layout-hflex lottie">{img('690232ecd6bd20129768e29f', 'userflow-netflix', 'Before and after comparison of the Netflix screen with the new watched option', extra=R())}</div>
  <div class="w-layout-hflex lottie">{img('6902332e4c72b2961a5f63cd', 'userflow-netflix', 'Redesigned Netflix seasons section', extra=R())}</div>
  <div class="w-layout-hflex lottie">{img('690233564f990c1a468e424b', 'userflow-netflix', 'Redesigned Netflix episodes list with watched markers', extra=R())}</div>''') + '\n' + \
    section41('Conclusion', 'red', 'This solution enhances user control in shared viewing contexts through simple, intuitive actions for tracking content. Small changes like these can have a meaningful impact on usability and satisfaction, even when developed under limited time and budget and validated through quick A/B user tests.', '')
    page('case-of-stufy.html', 'Case of stufy', "UX case study exploring how adding a manual 'watched' marker improves Netflix user control and reduces confusion in shared viewing contexts.",
         '/case-of-stufy', body)

# ---------------------------------------------------------------- 404
def notfound():
    body = '''<section class="w-layout-blockcontainer contenedor w-container" style="padding-top:160px;padding-bottom:120px;text-align:center">
  <h1 class="heading-introudcing">Page not found</h1>
  <p class="text-large light">The page you are looking for doesn’t exist or was moved.</p>
  <p><a class="button w-button" href="/">Back to home</a></p>
</section>'''
    page('404.html', 'Page not found | Clara de Ezcurra', '', '/404', body, body_cls='body')

if __name__ == '__main__':
    home(); about(); applica(); carbique(); case(); notfound()
