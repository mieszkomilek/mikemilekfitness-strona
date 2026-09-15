# Porównanie PL/EN — wersja 1.13

## Przyczyna i zakres
Punktem odniesienia jest main eefaa05 (1.12), zweryfikowany przez git fetch 2026-09-15. Poprzedni generator EN tworzył oddzielne, skrócone strony. Samo istnienie 17 adresów nie potwierdzało kompletności tłumaczenia.

| Obszar | Braki 1.12 uzupełnione w 1.13 |
| --- | --- |
| Główna | Film YouTube z tym samym ID i parametrami, trzy fakty, pełne intro, misja, stopka z informacjami i kontaktami, ikony i menu mobilne |
| 7 ofert | Pełne opisy zamiast jednego akapitu, ceny początkowe, wszystkie etykiety 29 wariantów, FAQ, powiązane oferty i wyjaśnienie wspólnego PayPal |
| Partnerzy | Cztery zdjęcia, odnośniki i pełne dane z PL |
| Kontakt, katalog, aktualności, polityki | Ta sama struktura, komplet tekstów, nawigacji i informacji co w PL |
| Wspólne UI/SEO | Flagi widoczne na telefonie przy zamkniętym menu, kontrast zaznaczenia, CSS przełącznika na każdej stronie, pojedyncze hreflang i language.js, produkcyjne og:image także na starych ręcznych stronach |

## Decyzja
`scripts/i18n.py` lokalizuje kompletny HTML PL podczas build. Jawne tłumaczenia w `data/translations-en.json`, bez usług tłumaczeniowych w przeglądarce i bez cichego fallbacku do PL. Nowy nieprzetłumaczony tekst blokuje build. Treść źródłowa, ceny, konfiguracja PayPal i oryginały mediów pozostają zachowane. Adresy EN zachowują dotychczasowe nazwy plików i prefiks /en/.

## Weryfikacja lokalna
- `site_build.py`, `site_qa.py`, `migration_qa.py`: pełny build, 7 opisów zgodnych ze snapshotem, 29 wariantów, 22 SHA-256 oryginalnych mediów.
- Porównanie wszystkich 17 par: kolejność elementów, klasy/ID, media, parametry osadzenia, zewnętrzne linki (w tym PayPal), lokalne cele i ceny wariantów; pojedynczy canonical, hreflang i skrypt języka. 34 adresy sitemap produkcji; podgląd noindex i pusta sitemap.
- Przeglądarka: główna EN w widoku desktop 1280×720 i telefon 390×844, stopka, oferta ćwiczeń; otwieranie menu i Escape, rozwinięcie FAQ, EN→PL na głównej oraz zachowanie tej samej oferty przy przełączeniu.
- Flagi przed poprawką znikały przez selektor chowający wszystkie nav; po poprawce widoczne z aktywnym językiem w czarnym tekście na limonkowym tle.

## Granice weryfikacji i TODO
Film ma identyczne osadzenie w PL i EN. W lokalnej przeglądarce widoczna była ramka, lecz nie potwierdzono odtwarzania YouTube; wymaga kontroli na produkcji w zwykłej przeglądarce. Nie dodano angielskiego audio ani tłumaczenia tekstu na oryginalnych okładkach. Tłumaczenie oferty nie jest deklaracją języka sprzedawanych materiałów.
Polityki są pełnym tłumaczeniem opublikowanej treści, nie jej aktualizacją prawną. Historyczne odniesienia do fizycznej wysyłki i kont nadal wymagają przeglądu właściciela opisanego w MIGRATION_PLAN.md. Nie wykonano zakupu ani testu płatności.
Wybór pierwszej wizyty nadal pojawia się na adresach PL bez zapisanej preferencji. Szersza zmiana tego przepływu nie była przedmiotem poprawki zgodności treści. Podgląd pod prefiksem GitHub ma test metadanych, nie pełny test nawigacji uruchomieniowej pod prefiksem; produkcja działa w katalogu głównym domeny.

## Publikacja
Do potwierdzenia po pushu: sukces GitHub Pages dla commita 1.13 i publiczne strony PL/EN zgodne z wygenerowanym artefaktem.
