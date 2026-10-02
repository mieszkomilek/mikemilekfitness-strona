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
- Publiczne diety zawierają wyłącznie podglądy: nazwę, zdjęcie, kategorię, czas, liczbę składników i zbiorcze makro. Pełne składniki, przygotowanie, zapisane plany, wyniki klientów i historia obliczeń pozostają w prywatnym plannerze. Każdy import sprawdzać przed commitem.
- Etykieta wartości odżywczych może korzystać z czytelnej hierarchii Nutrition Facts, ale nie może sugerować formalnej etykiety produktu. Nie publikować % dziennej wartości ani brakujących mikroelementów bez uzgodnionej normy i potwierdzonych danych.
- Filtrowanie katalogu i orientacyjne kalkulatory bez trwałego zapisu realizować lokalnie w JavaScript. Backend dodawać dopiero dla kont, prywatnych danych, trwałego zapisu, panelu administracyjnego lub logiki wymagającej ochrony serwerowej.
- Wyjątek zaakceptowany przez użytkownika 2026-09-15: kosmetyczna bramka akceptacyjna działu Wiedza z datą YYYYMMDD (Europe/Warsaw). Nie nazywać jej zabezpieczeniem prywatności; brak treści poufnych. Podgląd noindex poza sitemap do odrębnej decyzji o publikacji indeksowalnej.

- Ten standard opisuje obecną statyczną stronę; nie przesądza stosu przyszłej aplikacji Java.
- Cel: media lokalne bez zależności Shopify/CDN Shopify. Obecne osadzenie YouTube jest pozostałą zależnością zewnętrzną do rozstrzygnięcia, nie lokalnym plikiem wideo.
- Polski pozostaje pod dotychczasowymi adresami, angielski pod /en/. Każda para stron ma canonical oraz hreflang pl/en/x-default. Przełącznik języka jest dostępny bez zmiany adresów polskiej wersji; preferencja użytkownika jest zapisywana wyłącznie w localStorage.
- Od 1.13 nie tworzyć skróconych, osobnych szablonów EN. Generator tłumaczy pełną strukturę PL przez data/translations-en.json, obejmując tekst, metadane i etykiety dostępności. Dodając treść PL, dostarczyć tłumaczenie EN; brak wpisu ma blokować build. Zachować media, wszystkie sekcje, warianty i ceny. Uruchamiać porównanie par w migration_qa.py oraz sprawdzać mobilną widoczność flag niezależnie od menu.
