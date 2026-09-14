# MikeMilekFitness — Mike Miłek Fitness
Statyczna strona i katalog MikeMilekFitness na GitHub Pages. Bieżący AS-IS i kierunek TO-BE: PROJECT_BRAIN.md; TODO: MIGRATION_PLAN.md; dowody audytu: AUDIT_2026-09-14.md.

## Start pracy z AI
1. AGENTS.md — instrukcje pracy.
2. PROJECT_BRAIN.md — cel, decyzje, ograniczenia i stan projektu.
3. WEBSITE_STANDARD.md — struktura i standard techniczny.
4. MIGRATION_PLAN.md — ukończone oraz następne etapy.
5. version.txt i VERSION_HISTORY.md — wersja i historia zmian.

## Lokalnie
Wymagany Python 3.9 lub nowszy. Brak zależności zewnętrznych.
```sh
python3 scripts/import_media.py --offline
python3 scripts/site_build.py
python3 scripts/site_qa.py
python3 scripts/migration_qa.py
python3 -m http.server 8080 --directory _site
```
Otwórz http://localhost:8080/.

## Publikacja
Settings → Pages → Source: GitHub Actions.
Jeden workflow `.github/workflows/pages.yml` weryfikuje media, buduje, sprawdza i publikuje `_site/`.
Podgląd: https://mieszkomilek.github.io/strona-mikemilekfitness/
Produkcja: https://mikemilekfitness.com/ — GitHub Pages, Cloudflare DNS only. HTTP i www przekierowują do HTTPS domeny głównej. Produkcyjne SEO jest włączone: canonical, sitemap, robots i index,follow wskazują domenę główną. Stan rejestratora i abonamentu Shopify nie jest potwierdzony.

Wersja angielska jest publikowana pod https://mikemilekfitness.com/en/. Generator tworzy obie wersje, przełącznik języka i wspólną sitemapę.
