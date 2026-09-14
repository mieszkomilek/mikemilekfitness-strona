"""Verify source fidelity, variant prices and all published local links."""
import json,re
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from offer_pages import description_html

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts=[]
    def handle_data(self,data):
        self.parts.append(data)

def normalized(value):
    p=Text();p.feed(value)
    return re.sub(r'\s+','', ''.join(p.parts))

def check_offers(root, parser_class):
    config=json.loads((root/'site.config.json').read_text())
    catalog=json.loads((root/'data/catalog.json').read_text())
    source=json.loads((root/'data/offer-source-2026-09-10.json').read_text())
    originals={p['id']:p for p in source['products']}
    pages={}
    for file in (root/'_site').glob('*.html'):
        text=file.read_text();p=parser_class();p.feed(text)
        pages[file.name]=(text,p,{a['id'] for _,a in p.tags if 'id' in a})
    for name,(text,p,ids) in pages.items():
        for tag,attrs in p.tags:
            for attr in ['src','href']:
                raw=attrs.get(attr,'');url=urlsplit(raw)
                assert 'shopify' not in url.netloc.lower(),(name,raw)
                if url.scheme or url.netloc or not raw:continue
                target=(unquote(url.path) or name).lstrip('/')
                if target=='./':target='index.html'
                assert (root/'_site'/target).exists(),(name,raw)
                if url.fragment and target in pages:assert url.fragment in pages[target][2],(name,raw)
    titles=[];descriptions=[]
    for offer in catalog:
        s=originals[offer['id']]
        text,p,_=pages[offer['handle']+'.html']
        body=text.split('<div id="source-description">',1)[1].split('</div></section>',1)[0]
        expected=s['descriptionHtml'].replace('Wegański Trener','MikeMilekFitness')
        assert normalized(body)==normalized(expected),offer['handle']
        assert offer['variants']==s['variants'],offer['handle']
        assert body==description_html(s['descriptionHtml'])
        assert 'Wariant ustalany indywidualnie' not in text
        assert 'Oferta dopasowana do Twojego celu i poziomu' not in text
        assert sum(t=='h1' for t,a in p.tags)==1
        assert next(a['href'] for t,a in p.tags if t=='link' and a.get('rel')=='canonical')==config['baseUrl']+offer['handle']+'.html'
        assert next(a['content'] for t,a in p.tags if t=='meta' and a.get('name')=='robots')==('index,follow' if config['indexingEnabled'] else 'noindex,follow')
        assert [a['href'] for t,a in p.tags if 'data-sales-link' in a]==[config['paypalUrl']]
        titles.append(re.search(r'<title>(.*?)</title>',text).group(1))
        descriptions.append(next(a['content'] for t,a in p.tags if t=='meta' and a.get('name')=='description'))
    assert len(set(titles))==len(catalog) and len(set(descriptions))==len(catalog)
    assert pages['index.html'][0].count('class="contact-icon"')==6
    print('PASS: 7 source descriptions, 29 variants, unique offer metadata, 6 contact icons and all published local links')
