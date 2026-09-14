"""Complete public build metadata and preserve legacy storefront URLs."""
from html import escape
from pathlib import Path
from urllib.parse import urljoin, urlsplit
import json,re
from offer_pages import description_html

POLICIES = {'TERMS_OF_SERVICE': 'warunki.html', 'REFUND_POLICY': 'zwroty.html', 'SHIPPING_POLICY': 'wysylka.html', 'LEGAL_NOTICE': 'nota-prawna.html'}

def brand(text):
    text = description_html(text).replace('Wegańskiego Trenera','MikeMilekFitness')
    text = re.sub(r'www\.weganskitrener\.pl','mikemilekfitness.com',text,flags=re.I)
    return text.replace('info@weganskitrener.pl','mieszkomilek@gmail.com')

def simple_page(title, body):
    return '<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+' — MikeMilekFitness</title><meta name="description" content="'+escape(title)+' MikeMilekFitness."><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="mobile-home.css"></head><body><main class="page-width simple-page"><nav aria-label="Nawigacja"><a href="./">MikeMilekFitness</a> · <a href="oferta.html">Oferta</a> · <a href="kontakt.html">Kontakt</a></nav><h1>'+escape(title)+'</h1>'+body+'</main></body></html>'

def prepare(root, config):
    (root/'aktualnosci.html').write_text(simple_page('Aktualności','<p>Brak opublikowanych wpisów.</p>'))
    policies = json.loads((root/'data/policies-source-2026-09-10.json').read_text())
    for policy in policies:
        if policy['type'] in POLICIES:
            body=brand(policy['body'])
            if policy['type']=='SHIPPING_POLICY':
                # User-authorized payment method replacement; no new delivery promises.
                body=body.replace('akceptuje płatności kartą kredytową oraz bramkami płatniczymi','kieruje płatności do PayPal')
            (root/POLICIES[policy['type']]).write_text(simple_page(policy['title'], '<div class="policy-body">'+body+'</div>'))
    # Privacy is adapted to the actual static site; the unmodified original is archived.
    privacy='<h2>Kontakt i dane</h2><p>Kontakt z MikeMilekFitness: <a href="mailto:mieszkomilek@gmail.com">mieszkomilek@gmail.com</a>. Dane podane w korespondencji służą do odpowiedzi i obsługi uzgodnionych usług.</p><h2>Korzystanie ze strony</h2><p>Na stronie nie ma rejestracji konta, formularza kontaktowego ani newslettera. Strona jest udostępniana przez GitHub Pages i zawiera osadzony film YouTube. Dostawcy tych usług mogą otrzymywać dane techniczne połączenia, takie jak adres IP.</p><h2>Usługi zewnętrzne</h2><p>Kontakt przez e-mail lub WhatsApp i płatność przez PayPal odbywają się w usługach tych dostawców. Linki społecznościowe prowadzą do Instagrama i Facebooka.</p><h2>Pytania o dane</h2><p>W sprawach dostępu do danych, ich usunięcia lub ograniczenia przetwarzania napisz na wskazany adres e-mail.</p>'
    (root/'prywatnosc.html').write_text(simple_page('Polityka prywatności',privacy))

def finish(root, config, catalog):
    dest=root/'_site';base=config['baseUrl']
    canonical_files=[p.name for p in dest.glob('*.html')]
    for name in canonical_files:
        p=dest/name;text=p.read_text()
        text=re.sub(r'<script type="application/ld\+json">.*?</script>', '', text, flags=re.S)
        url=base+('' if name=='index.html' else name)
        text=re.sub(r'<meta name="robots"[^>]*>|<link rel="canonical"[^>]*>', '', text)
        robots='index,follow' if config['indexingEnabled'] else 'noindex,follow'
        meta='<meta name="robots" content="'+robots+'"><link rel="canonical" href="'+escape(url)+'">'
        english_url=base+'en/'+('' if name=='index.html' else name)
        meta+='<link rel="alternate" hreflang="pl" href="'+escape(url)+'"><link rel="alternate" hreflang="en" href="'+escape(english_url)+'"><link rel="alternate" hreflang="x-default" href="'+escape(base)+'">'
        if 'rel="icon"' not in text:meta+='<link rel="icon" href="assets/favicon.svg">'
        if 'property="og:image"' not in text:meta+='<meta property="og:image" content="'+escape(base+'assets/shopify/files-MIKE-3.jpg')+'">'
        schema={'@context':'https://schema.org','@type':'WebPage','name':re.search('<title>(.*?)</title>',text).group(1),'url':url,'inLanguage':'pl'}
        if name=='index.html':
            schema={'@context':'https://schema.org','@type':'WebSite','name':'MikeMilekFitness','url':base,'inLanguage':'pl'}
        meta+='<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')+'</script><script src="/assets/js/language.js?v='+(root/'version.txt').read_text().strip()+'" defer></script>'
        text=text.replace('</head>',meta+'</head>')
        # Avoid stale asset versions in previously hand-written pages.
        text=re.sub(r'\.css\?v=[0-9.]+','.css?v='+ (root/'version.txt').read_text().strip(),text)
        p.write_text(text)
        (root/name).write_text(text)
    mapping={'pages/contact':'kontakt.html','pages/partnerzy':'partnerzy.html','collections/all':'oferta.html',
             'policies/terms-of-service':'warunki.html','policies/refund-policy':'zwroty.html','policies/privacy-policy':'prywatnosc.html','policies/shipping-policy':'wysylka.html','policies/legal-notice':'nota-prawna.html','policies/contact-information':'kontakt.html'}
    for p in catalog:mapping['products/'+p['handle']]=p['handle']+'.html'
    mapping.update(json.loads((root/'data/legacy-extra.json').read_text()))
    for old,new in mapping.items():
        target=base+new
        body='<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>Przejdź do nowej strony — MikeMilekFitness</title><meta http-equiv="refresh" content="0;url='+escape(target)+'"><link rel="canonical" href="'+escape(target)+'"><meta name="robots" content="noindex,follow"></head><body><p><a href="'+escape(target)+'">Przejdź do nowej strony</a></p></body></html>'
        path=dest/old/'index.html';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(body)
    (root/'data/redirect-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
    links=''.join('<li><a href="'+escape(base+n)+'">'+escape(n)+'</a></li>' for n in ['oferta.html','kontakt.html'])
    (dest/'404.html').write_text(simple_page('Nie znaleziono strony','<p>Wybierz stronę, której szukasz:</p><ul>'+links+'</ul>').replace('href="styles.css"','href="'+base+'styles.css"').replace('href="mobile-home.css"','href="'+base+'mobile-home.css"').replace('href="./"','href="'+base+'"').replace('href="oferta.html"','href="'+base+'oferta.html"').replace('href="kontakt.html"','href="'+base+'kontakt.html"').replace('</head>','<meta name="robots" content="noindex,follow"></head>'))
    urls=''.join('<url><loc>'+escape(base+('' if n=='index.html' else n))+'</loc></url>' for n in sorted(canonical_files)) if config['indexingEnabled'] else ''
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>\n'
    (dest/'sitemap.xml').write_text(sitemap);(root/'sitemap.xml').write_text(sitemap)
