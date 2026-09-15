"""Generate the homepage and a public-only Pages artifact."""
from pathlib import Path
from html import escape
import json,shutil
from offer_pages import render_offers
from migration import prepare, finish
from i18n import build as build_english
from knowledge_preview import build as build_knowledge
R=Path(__file__).resolve().parents[1]
def build():
 c=json.loads((R/'site.config.json').read_text());h=json.loads((R/'data/home.json').read_text());catalog=json.loads((R/'data/catalog.json').read_text());v=(R/'version.txt').read_text().strip();cards=[]
 for p in catalog:
  t=escape(p['title']);u=escape(c['paypalUrl']);price=('Od ' if p['priceFrom'] else '')+f"{float(p['price']):.2f}".replace('.',',')+' zł PLN'
  detail=escape(p['handle']+'.html')
  cards.append(f'<article class="product-card"><a class="product-image" href="{detail}" aria-label="{t} — szczegóły oferty"><img src="{escape(p["image"])}" width="600" height="600" loading="lazy" alt="{t}"></a><h3><a href="{detail}">{t}</a></h3><p class="price">{price}</p><a class="buy" data-sales-link href="{u}" aria-label="{t} — przejdź do PayPal">Przejdź do PayPal</a></article>')
 values={'BASE_URL':c['baseUrl'],'EMAIL':c['email'],'VERSION':v,'ROBOTS':'index,follow' if c['indexingEnabled'] else 'noindex,follow','TITLE':h['title'],'SUBTITLE':h['subtitle'],'INTRO_HEADING':h['introHeading'],'OFFERS_HEADING':h['offersHeading'],'MISSION':h['mission'],'VIDEO_URL':h['videoUrl'],'FACT_INTRO':h['factIntro'],'FACT_HEADING':h['factHeading'],'FACT_TEXT':h['factText']}
 page=(R/'templates/index.html').read_text()
 for k,val in values.items():page=page.replace('{{'+k+'}}',escape(val,quote=True))
 page=page.replace('{{INTRO_HTML}}',h['introHtml']).replace('{{PRODUCTS}}','\n'.join(cards));assert '{{' not in page
 (R/'index.html').write_text(page)
 prepare(R,c)
 render_offers(R,c,catalog,v,cards)
 (R/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+c['baseUrl']+'sitemap.xml\n')
 urls='<url><loc>'+escape(c['baseUrl'])+'</loc></url>' if c['indexingEnabled'] else ''
 (R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>\n')
 (R/'version.js').write_text('window.SITE_VERSION = '+json.dumps(v)+';\n')
 dest=R/'_site'
 if dest.exists():shutil.rmtree(dest)
 dest.mkdir()
 for name in ['index.html','oferta.html','kontakt.html','partnerzy.html','warunki.html','zwroty.html','prywatnosc.html','wysylka.html','nota-prawna.html','aktualnosci.html'] + [p['handle']+'.html' for p in catalog] + ['offer.css','styles.css','mobile-home.css','video.css','social.css','robots.txt','sitemap.xml','manifest.webmanifest','version.txt','.nojekyll']:shutil.copy2(R/name,dest/name)
 shutil.copytree(R/'assets',dest/'assets')
 finish(R,c,catalog)
 english_pages=build_english(R,c,catalog)
 if c['indexingEnabled']:
  sitemap=(dest/'sitemap.xml').read_text()
  extra=''.join('<url><loc>'+escape(c['baseUrl']+'en/'+('' if name=='index.html' else name))+'</loc></url>' for name in sorted(english_pages))
  sitemap=sitemap.replace('</urlset>',extra+'</urlset>')
  (dest/'sitemap.xml').write_text(sitemap);(R/'sitemap.xml').write_text(sitemap)
 build_knowledge(dest)
 print(f'Built version {v}: {len(catalog)} offers')
if __name__=='__main__':build()
