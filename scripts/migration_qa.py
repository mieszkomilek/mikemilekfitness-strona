"""Exercise preview and production builds in isolated directories."""
from pathlib import Path
import json,re,shutil,subprocess,tempfile
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlsplit, urljoin, unquote
R=Path(__file__).resolve().parents[1]

class Tags(HTMLParser):
    def __init__(self):super().__init__();self.tags=[]
    def handle_starttag(self,t,a):self.tags.append((t,dict(a)))

def verify(root,production):
    site=root/'_site';c=json.loads((root/'site.config.json').read_text())
    allpages=list(site.glob('*.html'))
    for p in allpages:
        text=p.read_text();parser=Tags();parser.feed(text)
        assert sum(t=='h1' for t,a in parser.tags)==1,p
        robots=[a['content'] for t,a in parser.tags if t=='meta' and a.get('name')=='robots']
        assert robots==[('index,follow' if production else 'noindex,follow') if p.name!='404.html' else 'noindex,follow'],p
        for t,a in parser.tags:
            for key in ('src','href'):
                url=urlsplit(a.get(key,''))
                assert not (url.hostname and ('shopify' in url.hostname)),(p,a)
        if p.name!='404.html':
            assert text.count('type="application/ld+json"')==1,p
            canon=[a['href'] for t,a in parser.tags if t=='link' and a.get('rel')=='canonical']
            assert canon==[c['baseUrl']+('' if p.name=='index.html' else p.name)]
    mapping=json.loads((root/'data/redirect-map.json').read_text())
    for old,new in mapping.items():
        target=site/old/'index.html';assert target.exists()
        assert c['baseUrl']+new in target.read_text()
        assert (site/new).exists()
    urls=ET.parse(site/'sitemap.xml').findall('.//{*}loc')
    english_pages=list((site/'en').glob('*.html'))
    assert len(english_pages)==17
    for p in english_pages:
        text=p.read_text();parser=Tags();parser.feed(text)
        polish=Tags();polish.feed((site/p.name).read_text())
        pl_prices=re.findall(r'<td>([0-9,]+) zł</td>',(site/p.name).read_text())
        en_prices=re.findall(r'<td>([0-9.]+) PLN</td>',text)
        assert [v.replace(',','.') for v in pl_prices]==en_prices,(p,'variant prices')
        # Structural parity catches dropped video, sections, FAQ, tables and footer.
        assert [t for t,a in parser.tags]==[t for t,a in polish.tags],p
        for (tag, en), (_, pl) in zip(parser.tags,polish.tags):
            for key in ('class','id','loading','allow','allowfullscreen','width','height'):
                assert en.get(key)==pl.get(key),(p,tag,key)
            if tag in ('img','iframe','script'):
                assert en.get('src','').lstrip('/')==pl.get('src','').lstrip('/'),(p,tag)
            if tag=='a' and urlsplit(pl.get('href','')).scheme:
                assert en.get('href')==pl.get('href'),(p,'external link changed')
            for key in ('src','href'):
                link=en.get(key,'');parsed=urlsplit(link)
                if not link or parsed.scheme or parsed.netloc:continue
                path=unquote(urlsplit(urljoin('/en/'+p.name,link)).path)
                target=site/path.lstrip('/')
                if path.endswith('/'):target=target/'index.html'
                assert target.exists(),(p,link,target)
        robots=[a['content'] for t,a in parser.tags if t=='meta' and a.get('name')=='robots']
        assert robots==['index,follow' if production else 'noindex,follow'],p
        canon=[a['href'] for t,a in parser.tags if t=='link' and a.get('rel')=='canonical']
        assert canon==[c['baseUrl']+'en/'+('' if p.name=='index.html' else p.name)],p
        assert sum(t=='link' and a.get('rel')=='alternate' for t,a in parser.tags)==3,p
        assert sum(t=='script' and 'language.js' in a.get('src','') for t,a in parser.tags)==1,p
        assert '<html lang="en">' in text and 'hreflang="pl"' in text and 'hreflang="en"' in text,p
        assert text.count('type="application/ld+json"')==1,p
        assert sum(t=='h1' for t,a in parser.tags)==1,p
        assert any(t=='script' and a.get('src','').startswith('/assets/js/language.js') for t,a in parser.tags),p
    expected=(len(allpages)-1+len(english_pages)) if production else 0
    assert len(urls)==expected
    assert not (site/'data').exists()
    print(f'PASS {"production" if production else "preview"}: {len(allpages)} Polish pages, {len(english_pages)} English pages, {len(mapping)} legacy routes, sitemap, metadata, external dependency scan')

def main():
    verify(R,json.loads((R/'site.config.json').read_text())['indexingEnabled'])
    with tempfile.TemporaryDirectory(prefix='mike-production-') as tmp:
        root=Path(tmp)/'site'
        shutil.copytree(R,root,ignore=shutil.ignore_patterns('.git','_site','__pycache__'))
        config=json.loads((root/'site.config.json').read_text())
        config['baseUrl']='https://mieszkomilek.github.io/strona-mikemilekfitness/';config['indexingEnabled']=False
        (root/'site.config.json').write_text(json.dumps(config))
        subprocess.run(['python3',str(root/'scripts/site_build.py')],check=True)
        subprocess.run(['python3',str(root/'scripts/site_qa.py')],check=True)
        verify(root,False)
if __name__=='__main__':main()
