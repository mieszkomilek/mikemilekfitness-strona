# Instrukcje dla AI
Przed pracą przeczytaj PROJECT_BRAIN.md, WEBSITE_STANDARD.md, DOMAIN_CUTOVER.md, MIGRATION_PLAN.md, CONTENT_AUDIT.md, version.txt i VERSION_HISTORY.md.
Treści marki pochodzą wyłącznie z mikemilekfitness.com. Nie kopiuj kodu, treści ani grafik z repo Ewy.
Edytuj templates/index.html oraz data/home.json i data/catalog.json; index.html jest wynikiem generatora.
Po zmianie uruchom python3 scripts/site_build.py i python3 scripts/site_qa.py.
Nie edytuj plików binarnych oryginałów assets/shopify oraz assets/fonts. Źródła i SHA-256 są w data/media-manifest.json.
Wszystkie CTA sprzedażowe wskazują paypalUrl z site.config.json. Nie zmieniaj płatności bez polecenia.
Każdą trwałą decyzję opisz w PROJECT_BRAIN.md. Wersję i opis zmian aktualizuj razem z kodem.
Polecenie użytkownika z 2026-09-10 rozszerza zakres o przygotowanie i przełączenie domeny na GitHub Pages. Zachowaj rekordy pocztowe; domenę przełącz po uzyskaniu dostępu administracyjnego i testach. PayPal i repo strona-ewamilek nie są objęte zmianami. Shopify wygaszaj dopiero po udanym przełączeniu i zabezpieczeniu potrzebnych danych.

Rozdzielaj AS-IS potwierdzony kodem/testem, deklaracje użytkownika, TO-BE i TODO. Historię czytaj jako historię. Dokumentacyjne audyty bez zmiany strony mogą zachować version.txt, z osobnym datowanym wpisem w VERSION_HISTORY.md. Po zmianach uruchom również python3 scripts/migration_qa.py. Commituj zweryfikowane zakończone zmiany; nie zapisuj sekretów, danych klientów ani płatnych materiałów. Backend Java jest kierunkiem, pozostały stos nie został wybrany. Bez osobnego zakresu nie zmieniaj płatności, widoczności repo ani nie uruchamiaj płatnych usług.
