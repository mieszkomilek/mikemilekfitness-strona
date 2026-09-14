# Standard strony
- HTML, CSS i niewielkie moduły JavaScript; Python standard library do generowania i kontroli.
- Jedno źródło konfiguracji: site.config.json. Dane treści i katalogu w data/.
- Szablony w templates/, media w assets/, narzędzia w scripts/, jeden deployment w .github/workflows/.
- Teksty, fotografie i tożsamość wyłącznie marki MikeMilekFitness.
- Jeden H1, opis, canonical i poprawne kotwice; noindex przed świadomym uruchomieniem SEO (obecnie także na domenie produkcyjnej).
- Nawigacja działa bez JS; menu mobilne obsługuje klawiaturę i Escape; focus jest widoczny.
- Lokalne fonty i obrazy, wymiary zdjęć, lazy loading poza głównym zdjęciem.
- Oferty dostępne bez JavaScript. Płatności pobierane z konfiguracji podczas build.
- GitHub Pages publikuje tylko _site/, bez instrukcji AI i danych źródłowych. Samo repo jest publiczne.
- Nie symulować prywatności hasłami zaszytymi w JavaScript. Brak danych klientów i sekretów w repo.

- Ten standard opisuje obecną statyczną stronę; nie przesądza stosu przyszłej aplikacji Java.
- Cel: media lokalne bez zależności Shopify/CDN Shopify. Obecne osadzenie YouTube jest pozostałą zależnością zewnętrzną do rozstrzygnięcia, nie lokalnym plikiem wideo.
