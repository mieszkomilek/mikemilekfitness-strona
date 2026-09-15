# Standard strony
- HTML, CSS i niewielkie moduły JavaScript; Python standard library do generowania i kontroli.
- Jedno źródło konfiguracji: site.config.json. Dane treści i katalogu w data/.
- Szablony w templates/, media w assets/, narzędzia w scripts/, jeden deployment w .github/workflows/.
- Teksty, fotografie i tożsamość wyłącznie marki MikeMilekFitness.
- Jeden H1, opis, canonical i poprawne kotwice; noindex w podglądzie. Produkcyjne indeksowanie jest włączone w site.config.json.
- Nawigacja działa bez JS; menu mobilne obsługuje klawiaturę i Escape; focus jest widoczny.
- Lokalne fonty i obrazy, wymiary zdjęć, lazy loading poza głównym zdjęciem.
- Oferty dostępne bez JavaScript. Płatności pobierane z konfiguracji podczas build.
- GitHub Pages publikuje tylko _site/, bez instrukcji AI i danych źródłowych. Samo repo jest publiczne.
- Nie symulować prywatności hasłami zaszytymi w JavaScript. Brak danych klientów i sekretów w repo.

- Ten standard opisuje obecną statyczną stronę; nie przesądza stosu przyszłej aplikacji Java.
- Cel: media lokalne bez zależności Shopify/CDN Shopify. Obecne osadzenie YouTube jest pozostałą zależnością zewnętrzną do rozstrzygnięcia, nie lokalnym plikiem wideo.
- Polski pozostaje pod dotychczasowymi adresami, angielski pod /en/. Każda para stron ma canonical oraz hreflang pl/en/x-default. Przełącznik języka jest dostępny bez zmiany adresów polskiej wersji; preferencja użytkownika jest zapisywana wyłącznie w localStorage.
- Od 1.13 nie tworzyć skróconych, osobnych szablonów EN. Generator tłumaczy pełną strukturę PL przez data/translations-en.json, obejmując tekst, metadane i etykiety dostępności. Dodając treść PL, dostarczyć tłumaczenie EN; brak wpisu ma blokować build. Zachować media, wszystkie sekcje, warianty i ceny. Uruchamiać porównanie par w migration_qa.py oraz sprawdzać mobilną widoczność flag niezależnie od menu.
