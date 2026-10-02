"""Validate output links, sales destinations, SEO and media integrity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,hashlib,xml.etree.ElementTree as ET
from offer_qa import check_offers
R=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.tags=[]
 def handle_starttag(self,t,a):self.tags.append((t,dict(a)))
def check():
 root=R/'_site';text=(root/'index.html').read_text();p=Page();p.feed(text)
 c=json.loads((R/'site.config.json').read_text());catalog=json.loads((R/'data/catalog.json').read_text())
 assert sum(t=='h1' for t,a in p.tags)==1 and '<title>' in text and 'name="description"' in text
 ids=[a['id'] for t,a in p.tags if 'id' in a];assert len(ids)==len(set(ids))
 sales=[a['href'] for t,a in p.tags if 'data-sales-link' in a]
 assert len(sales)==len(catalog) and all(u==c['paypalUrl'] for u in sales)
 assert not re.search(r'href=["\'][^"\']*(?:/products/|/cart|/checkout)',text)
 for tag,a in p.tags:
  if tag=='img':assert 'alt' in a and 'width' in a and 'height' in a
  for key in ['src','href']:
   url=a.get(key,'');u=urlsplit(url)
   if not url or u.scheme or u.netloc:continue
   if u.path:assert (root/unquote(u.path).lstrip('/')).exists(),f'Missing file: {url}'
   if u.fragment:assert u.fragment in ids,f'Missing anchor: {url}'
  if tag in {'img','script'}:assert not urlsplit(a.get('src','')).netloc
 for css in ['styles.css','mobile-home.css']:
  for path in re.findall(r'url\(["\']?([^"\')]+)',(root/css).read_text()):assert (root/path).is_file(),path
 assets=json.loads((R/'data/media-manifest.json').read_text())['assets']
 for a in assets:
  data=(R/a['path']).read_bytes();assert len(data)==a['bytes'] and hashlib.sha256(data).hexdigest()==a['sha256']
 assert next(a['href'] for t,a in p.tags if t=='link' and a.get('rel')=='canonical')==c['baseUrl']
 assert ('content="noindex,follow"' in text)==(not c['indexingEnabled'])
 ET.parse(root/'sitemap.xml');json.loads((root/'manifest.webmanifest').read_text())
 assert not (root/'data').exists() and not (root/'.github').exists()
 public_meals=json.loads((R/'data/diets.json').read_text())
 allowed={'id','name','nameEn','image','category','categoryLabel','categoryLabelEn','preparationMinutes','ingredientCount','nutrition'}
 allowed_nutrients={'kcal','protein','carbs','fat','fiber'}
 assert len(public_meals)==35
 assert all(set(meal)==allowed for meal in public_meals)
 assert all(meal['nutrition'] is None or set(meal['nutrition'])==allowed_nutrients for meal in public_meals)
 assert len(list((R/'assets/diets').glob('meal-*.jpg')))==35
 diets=(root/'diety.html').read_text();diet_page=Page();diet_page.feed(diets)
 assert sum(t=='article' and 'data-meal' in a for t,a in diet_page.tags)==35
 assert diets.count('class="nutrition-label"')==35 and 'Błonnik' in diets
 assert 'id="diet-calculator"' in diets and 'id="diet-filters"' in diets
 assert 'ingredients' not in diets.lower() and 'preparation' not in diets.lower()
 print(f'PASS: HTML, local links, {len(sales)} PayPal links, {len(assets)} media hashes, SEO, public artifact')
 check_offers(R,Page)
if __name__=='__main__':check()
