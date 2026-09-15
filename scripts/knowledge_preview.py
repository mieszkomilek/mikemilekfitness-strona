"""Build the bilingual knowledge preview with a user-approved cosmetic date gate."""
from pathlib import Path
from html import escape
import argparse
import re

CATEGORIES = [
    ('nutrition-calculators', 'Kalkulatory żywieniowe', 'Nutrition calculators',
     'Od zapotrzebowania energetycznego do wygodnego planowania posiłków.',
     'From energy needs to practical meal planning.',
     [('Zapotrzebowanie kaloryczne', 'Calorie needs'), ('Makroskładniki i białko', 'Macros and protein'), ('Porcje i kaloryczność przepisów', 'Recipe portions and nutrition')]),
    ('strength-calculators', 'Kalkulatory treningowe', 'Strength calculators',
     'Planuj obciążenia, serie i kolejne kroki treningu.',
     'Plan your training loads, sets and next steps.',
     [('Maksymalny ciężar — 1RM', 'One-rep max — 1RM'), ('Talerze na sztangę', 'Barbell plate calculator'), ('Objętość i progresja', 'Volume and progression')]),
    ('exercise-library', 'Atlas ćwiczeń', 'Exercise library',
     'Poznaj ćwiczenia według mięśni i dostępnego sprzętu.',
     'Explore exercises by muscle group and available equipment.',
     [('Mapa mięśni: przód i tył', 'Muscle map: front and back'), ('Technika i częste błędy', 'Technique and common mistakes'), ('Zamienniki ćwiczeń', 'Exercise alternatives')]),
    ('strength-training', 'Trening siłowy', 'Strength training',
     'Zrozum podstawy i świadomie rozwijaj swój trening.',
     'Understand the foundations and develop your training with purpose.',
     [('Pierwsze kroki na siłowni', 'Getting started at the gym'), ('Serie, powtórzenia i RIR', 'Sets, reps and RIR'), ('Planowanie tygodnia', 'Planning your training week')]),
    ('nutrition', 'Żywienie', 'Nutrition',
     'Praktyczna wiedza o energii, składnikach i codziennych wyborach.',
     'Practical knowledge about energy, nutrients and everyday choices.',
     [('PPM a CPM', 'BMR vs TDEE'), ('Białko, tłuszcze i węglowodany', 'Protein, fats and carbohydrates'), ('Obserwowanie postępów', 'Monitoring progress')]),
    ('vegan-nutrition', 'Dieta wegańska', 'Vegan nutrition',
     'Roślinne jedzenie w praktyce osoby aktywnej.',
     'Plant-based eating for an active lifestyle.',
     [('Roślinne źródła białka', 'Plant-based protein sources'), ('Bilansowanie diety', 'Building a balanced diet'), ('B12 i pozostałe składniki', 'B12 and other nutrients')]),
    ('recipes', 'Przepisy', 'Recipes',
     'Pomysły na roślinne posiłki i wygodne przygotowanie porcji.',
     'Plant-based meal ideas and practical portion preparation.',
     [('Posiłki białkowe', 'Protein-rich meals'), ('Gotowanie na kilka dni', 'Meal preparation'), ('Skalowanie porcji', 'Scaling portions')]),
]

CSS = '''
:root{color-scheme:dark;font-family:system-ui,sans-serif;color:#fff;background:#080808}
*{box-sizing:border-box}body{margin:0}a{color:inherit}a:focus-visible{outline:3px solid #c5ff43;outline-offset:5px}
header{position:sticky;top:0;background:#080808ed;border-bottom:1px solid #333;z-index:2}
.bar{max-width:1160px;margin:auto;padding:20px 24px;display:flex;gap:24px;align-items:center;flex-wrap:wrap}
.brand{font-weight:800;text-decoration:none;letter-spacing:-.04em}.brand span{color:#c5ff43}
nav{margin-left:auto;display:flex;gap:16px}nav a{padding:8px;text-decoration:none}nav [aria-current=page]{color:#c5ff43}
main,footer{max-width:1160px;margin:auto;padding:36px 24px}.intro{max-width:780px;padding:30px 0 44px}
.label{color:#c5ff43;text-transform:uppercase;letter-spacing:.12em;font-size:12px;font-weight:700}
h1{font-size:clamp(40px,7vw,76px);line-height:1.05;letter-spacing:-.05em;margin:20px 0}p{line-height:1.7;color:#bdbdbd}
.lead{font-size:20px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.card{background:#141414;border:1px solid #303030;border-radius:16px;padding:28px;text-decoration:none;display:block}
.card:hover{border-color:#c5ff43}.card h2{font-size:24px}.number{color:#c5ff43;font-size:13px}.arrow{display:block;margin-top:24px;color:#c5ff43}
.notice{border-left:3px solid #c5ff43;padding:12px 20px;background:#141414;margin-bottom:30px}
li{padding:16px 0;border-bottom:1px solid #333}footer{border-top:1px solid #333;color:#999;font-size:13px}
@media(max-width:800px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:520px){.grid{grid-template-columns:1fr}.bar{gap:8px}nav{gap:4px}main{padding-top:16px}.intro{padding-top:12px}.lead{font-size:18px}}
'''

def page(language, category=None):
    en = language == 'en'
    index = 2 if en else 1
    title = category[index] if category else ('Knowledge' if en else 'Wiedza')
    suffix = category[0] + '.html' if category else 'index.html'
    home = '/en/' if en else '/'
    alternate = ('/wiedza/' if en else '/en/wiedza/') + suffix
    description = ('Training. Nutrition. Plant-based living.' if en else 'Trening. Żywienie. Roślinna codzienność.')
    notice = ('Preview for review. Calculators, articles and the muscle map are in preparation.' if en else 'Podgląd do akceptacji. Kalkulatory, artykuły i mapa mięśni są w przygotowaniu.')
    if category:
        body = '<p><a href="index.html">← ' + ('All knowledge categories' if en else 'Wszystkie kategorie wiedzy') + '</a></p>'
        body += '<section class="intro"><p class="label">MikeMilekFitness / '+ ('Knowledge' if en else 'Wiedza')+'</p><h1>'+title+'</h1><p class="lead">'+category[4 if en else 3]+'</p></section>'
        body += '<div class="notice">'+notice+'</div><h2>'+('Planned topics' if en else 'Planowane tematy')+'</h2><ul>'
        body += ''.join('<li>'+escape(topic[1 if en else 0])+'</li>' for topic in category[5])+'</ul>'
    else:
        body = '<section class="intro"><p class="label">MikeMilekFitness / '+('Explore & learn' if en else 'Poznaj i zrozum')+'</p><h1>'+title+'</h1><p class="lead">'+description+'</p><p>'+('Explore the topics you need: from choosing exercises to planning plant-based meals.' if en else 'Znajdź temat dla siebie: od doboru ćwiczeń po planowanie roślinnych posiłków.')+'</p></section><div class="notice">'+notice+'</div><div class="grid">'
        for n,c in enumerate(CATEGORIES,1):
            body += '<a class="card" href="'+c[0]+'.html"><span class="number">0'+str(n)+'</span><h2>'+c[index]+'</h2><p>'+c[4 if en else 3]+'</p><span class="arrow">'+('Explore category' if en else 'Poznaj kategorię')+' →</span></a>'
        body += '</div>'
    html = '<!doctype html><html lang="'+language+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>'+title+' | MikeMilekFitness</title><meta name="description" content="'+description+'"><style>'+CSS+'</style></head><body><header><div class="bar"><a class="brand" href="'+home+'">MikeMilek<span>Fitness</span></a><nav aria-label="'+('Language' if en else 'Język')+'"><a href="'+(alternate if en else suffix)+'" lang="pl"'+('' if en else ' aria-current="page"')+'>🇵🇱 PL</a><a href="'+(suffix if en else alternate)+'" lang="en"'+(' aria-current="page"' if en else '')+'>🇬🇧 EN</a></nav></div></header><main>'+body+'</main><footer>© 2026 MikeMilekFitness · '+('Knowledge preview' if en else 'Podgląd działu Wiedza')+'</footer></body></html>'
    gate_title = 'Review access' if en else 'Dostęp do podglądu'
    gate_label = 'Review code' if en else 'Kod podglądu'
    gate_copy = 'Enter the agreed code to view this draft.' if en else 'Wpisz uzgodniony kod, aby obejrzeć wersję roboczą.'
    gate = '<section id="review-gate" aria-labelledby="gate-title"><h2 id="gate-title">'+gate_title+'</h2><p>'+gate_copy+'</p><form id="review-form"><label for="review-code">'+gate_label+'</label><input id="review-code" name="code" type="password" inputmode="numeric" maxlength="8" autocomplete="off" required aria-describedby="review-error"><button type="submit">'+('Open preview' if en else 'Otwórz podgląd')+'</button><p id="review-error" role="status"></p></form><noscript>'+('Enable JavaScript to use the review gate.' if en else 'Włącz JavaScript, aby użyć bramki podglądu.')+'</noscript></section>'
    gate_css = '<style>[hidden]{display:none!important}#review-gate{max-width:560px;margin:8vh auto;padding:24px}#review-gate h2{font-size:40px}#review-form{display:grid;gap:14px}input,button{font:inherit;padding:14px;border:1px solid #777;border-radius:8px}button{background:#c5ff43;color:#080808;cursor:pointer}input:focus-visible,button:focus-visible{outline:3px solid #c5ff43;outline-offset:4px}#review-error{color:#ffb4b4;margin:0}</style>'
    html = html.replace('</head>', gate_css+'<script src="/assets/js/knowledge-gate.js?v=1.14" defer></script></head>')
    html = html.replace('<main>', gate+'<main id="knowledge-content" hidden tabindex="-1">').replace('<footer>', '<footer id="knowledge-footer" hidden>')
    return html

def build(destination):
    for language in ('pl','en'):
        folder = destination/('en/wiedza' if language == 'en' else 'wiedza')
        folder.mkdir(parents=True, exist_ok=True)
        (folder/'index.html').write_text(page(language))
        for category in CATEGORIES:
            (folder/(category[0]+'.html')).write_text(page(language,category))
    # Add navigation to existing public pages without changing their indexing.
    for source in list(destination.glob('*.html')) + list((destination/'en').glob('*.html')):
        if source.name == '404.html':
            continue
        en = source.parent.name == 'en'
        link = '<a data-knowledge-link href="' + ('/en/wiedza/' if en else '/wiedza/') + '">' + ('Knowledge' if en else 'Wiedza') + '</a>'
        text = source.read_text()
        if '<nav' in text:
            text = re.sub(r'</nav>', link+'</nav>', text, count=1)
        else:
            text = text.replace('<body>', '<body><nav>'+link+'</nav>')
        source.write_text(text)
    print('Built knowledge preview: 8 PL + 8 EN pages, noindex and daily review gate')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    build(parser.parse_args().output)
