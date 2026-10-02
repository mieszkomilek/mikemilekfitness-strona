"""Render the public diet browser and add it to site navigation."""
from html import escape
import json
import re


def _card(meal):
    nutrients = meal.get('nutrition')
    values = nutrients or {key: '—' for key in ('kcal', 'protein', 'carbs', 'fat', 'fiber')}
    return f'''<article class="diet-card" data-meal data-category="{escape(meal['category'])}" data-name="{escape(meal['name'].casefold())}">
<img src="{escape(meal['image'])}" width="900" height="1200" loading="lazy" alt="{escape(meal['name'])}">
<div class="diet-card-copy"><p class="diet-category">{escape(meal['categoryLabel'])}</p><h2>{escape(meal['name'])}</h2>
<p class="diet-meta"><span><strong>{meal['preparationMinutes']}</strong> min</span><span><strong>{meal['ingredientCount']}</strong> składników</span></p>
<section class="nutrition-label" aria-label="Wartości odżywcze"><h3>Wartości odżywcze</h3><p class="nutrition-serving"><strong>Porcja</strong><span>1 posiłek</span></p>
<div class="nutrition-calories"><span>Kalorie</span><strong>{values['kcal']} <small>kcal</small></strong></div>
<dl><div><dt>Tłuszcz</dt><dd>{values['fat']} g</dd></div><div><dt>Węglowodany</dt><dd>{values['carbs']} g</dd></div><div class="nutrition-subrow"><dt>Błonnik</dt><dd>{values['fiber']} g</dd></div><div class="nutrition-protein"><dt>Białko</dt><dd>{values['protein']} g</dd></div></dl>
<p class="nutrition-footnote">Wartości szacunkowe dla całego prezentowanego posiłku.</p></section>
<p class="diet-preview-note">Podgląd posiłku. Pełny przepis i skalowanie porcji są dostępne w indywidualnym planie.</p></div></article>'''


def render(root, config, version):
    meals = json.loads((root/'data/diets.json').read_text())
    categories = []
    for meal in meals:
        pair = (meal['category'], meal['categoryLabel'])
        if pair not in categories:
            categories.append(pair)
    options = ''.join(f'<option value="{escape(key)}">{escape(label)}</option>' for key, label in categories)
    cards = '\n'.join(_card(meal) for meal in meals)
    page = f'''<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Diety roślinne | MikeMilekFitness</title><meta name="description" content="Przeglądaj 35 autorskich posiłków roślinnych i oblicz orientacyjne zapotrzebowanie kaloryczne."><meta name="robots" content="index,follow"><link rel="canonical" href="{escape(config['baseUrl'])}diety.html"><meta property="og:title" content="Diety roślinne | MikeMilekFitness"><meta property="og:description" content="Autorskie posiłki roślinne i kalkulator zapotrzebowania kalorycznego."><meta property="og:type" content="website"><meta name="theme-color" content="#000000">
<link rel="icon" href="assets/favicon.svg"><link rel="manifest" href="manifest.webmanifest"><link rel="stylesheet" href="styles.css?v={escape(version)}"><link rel="stylesheet" href="mobile-home.css?v={escape(version)}"><link rel="stylesheet" href="social.css?v={escape(version)}"><link rel="stylesheet" href="diets.css?v={escape(version)}"><script src="assets/js/core.js?v={escape(version)}" defer></script><script src="assets/js/diets.js?v={escape(version)}" defer></script></head><body><a class="skip-link" href="#main">Przejdź do treści</a>
<header class="header"><div class="header-inner"><a href="./" aria-label="MikeMilekFitness — strona główna"><img class="logo" src="assets/shopify/files-black.png" width="50" height="60" alt="MikeMilekFitness — autorskie logo"></a><span class="brand-wordmark">MikeMilek<span>Fitness</span></span><button class="menu-toggle" aria-expanded="false" aria-controls="navigation" hidden>Menu</button><nav id="navigation" aria-label="Nawigacja główna"><a href="./">Strona Główna</a><a href="oferta.html">Oferta</a><a data-diets-link href="diety.html" aria-current="page">Diety</a><a href="kontakt.html">Kontakt</a><a href="partnerzy.html">Partnerzy</a></nav><a class="header-contact" href="kontakt.html">Napisz do mnie</a></div></header>
<main id="main"><section class="diet-hero page-width"><p class="diet-kicker">MikeMilekFitness / Diety</p><h1>Roślinne posiłki dopasowane do Twojego celu</h1><p class="diet-lead">Poznaj 35 autorskich propozycji posiłków. Skorzystaj z kalkulatora, aby oszacować dzienny cel i kaloryczność jednego posiłku.</p></section>
<section class="calculator page-width" aria-labelledby="calculator-title"><div><p class="diet-kicker">Kalkulator</p><h2 id="calculator-title">Oblicz orientacyjne zapotrzebowanie</h2><p>Wynik ma charakter informacyjny. W przypadku chorób, ciąży lub szczególnych potrzeb skonsultuj dietę ze specjalistą.</p></div><form id="diet-calculator"><label>Płeć<select name="sex"><option value="K">Kobieta</option><option value="M">Mężczyzna</option></select></label><label>Wiek<input name="age" type="number" min="16" max="100" value="30" required></label><label>Waga · kg<input name="weight" type="number" min="35" max="300" step="0.1" value="75" required></label><label>Wzrost · cm<input name="height" type="number" min="130" max="230" value="175" required></label><label>Aktywność<select name="activity"><option value="1.2">Niska</option><option value="1.375">Lekka</option><option value="1.55" selected>Umiarkowana</option><option value="1.725">Wysoka</option></select></label><label>Posiłki dziennie<input name="meals" type="number" min="1" max="6" value="4" required></label><button type="submit">Oblicz</button></form><div id="diet-result" class="diet-result" role="status" aria-live="polite"></div></section>
<section class="diet-browser page-width" aria-labelledby="diet-list-title"><div class="diet-browser-heading"><div><p class="diet-kicker">Katalog</p><h2 id="diet-list-title">35 autorskich posiłków</h2></div><p id="diet-count" aria-live="polite"></p></div><form class="diet-filters" id="diet-filters"><label>Szukaj posiłku<input name="query" type="search" placeholder="Nazwa posiłku"></label><label>Kategoria<select name="category"><option value="">Wszystkie kategorie</option>{options}</select></label></form><div class="diet-grid" id="diet-grid">{cards}</div><p id="diet-empty" class="diet-empty" hidden>Brak posiłków spełniających wybrane kryteria.</p></section>
<section class="diet-cta page-width"><div><p class="diet-kicker">Plan indywidualny</p><h2>Potrzebujesz pełnego planu i gramatur?</h2><p>Podgląd nie publikuje pełnych receptur. Napisz, aby ustalić cel, liczbę posiłków i wariant współpracy.</p></div><a class="buy" href="kontakt.html">Zapytaj o plan diety</a></section></main>
<footer><div class="footer-grid page-width"><section><h2>Info</h2><a href="oferta.html">Oferta</a><a href="diety.html">Diety</a><a href="prywatnosc.html">Polityka prywatności</a><a href="kontakt.html">Kontakt</a></section><section><h2>Misja</h2><p>Pomagam w kształtowaniu sylwetki, oferując autorskie diety roślinne i spersonalizowane plany treningowe.</p></section><section><h2>Bądźmy w kontakcie</h2><a href="mailto:{escape(config['email'])}">{escape(config['email'])}</a></section></div><div class="footer-bottom page-width"><span>© 2026 MikeMilekFitness</span><span>Wersja {escape(version)}</span></div></footer></body></html>'''
    (root/'diety.html').write_text(page)
    return len(meals)


def add_navigation(destination, source_root):
    for page in destination.glob('*.html'):
        if page.name == '404.html':
            continue
        text = page.read_text()
        if 'data-diets-link' not in text and '<nav' in text:
            separator = '' if '<nav id=' in text else ' · '
            link = f'{separator}<a data-diets-link href="diety.html">Diety</a></nav>'
            text = re.sub(r'</nav>', link, text, count=1)
            page.write_text(text)
            source = source_root/page.name
            if source.exists():
                source.write_text(text)
