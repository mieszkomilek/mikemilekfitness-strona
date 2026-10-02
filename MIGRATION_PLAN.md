# TODO — migracja i kolejny etap
Stan 2026-10-02. Dowody: datowane audyty; AS-IS i TO-BE: PROJECT_BRAIN.md. Migracja sklepu nie jest w całości zamknięta; publiczna część GetDiet została przeniesiona.

## Potwierdzone zakończone elementy
- [x] 1.15 lokalnie: zakładka Diety/Diets w PL/EN, 35 podglądów posiłków, zdjęcia, filtry, wyszukiwanie i kalkulator kcal działający lokalnie. Import jest powtarzalny, build i QA przechodzą; pełne przepisy, zapisane diety oraz dane klientów nie trafiają do publicznego repo ani `_site/`.
- [x] 1.14 lokalnie: hub Wiedza i 7 kategorii PL/EN, zaakceptowana bramka datowa, noindex poza sitemap, testy błędnego/poprawnego kodu i przejść PL/EN. Weryfikacja publikacji opisana w KNOWLEDGE_PREVIEW.md.
- [x] 1.13: uzupełnienie skróconego EN, zgodność struktury 17 par, cen, mediów i linków; widoczne flagi na telefonie. Testy lokalne: BILINGUAL_AUDIT_2026-09-15.md. Publikację sprawdzić po pushu.
- [x] Wersja 1.12: 17 angielskich stron pod /en/, wybór przy pierwszej wizycie, stały przełącznik PL/EN, zapamiętanie wyboru oraz hreflang i sitemap obu języków.
- [x] Statyczny katalog, siedem ofert, kontakt, partnerzy, polityki i puste aktualności są lokalne.
- [x] 22 obrazy/fonty z manifestu dostępne lokalnie; offline import i SHA-256 przechodzą.
- [x] GitHub Pages wdrożył main ab802aa, workflow #15 success; HTML produkcji zgodny z buildem.
- [x] Cloudflare DNS active, rekordy GitHub Pages DNS only; HTTPS domeny głównej i przekierowania HTTP/www działają.
- [x] Generator 18 dawnych ścieżek oraz 404; lokalne testy obu trybów SEO przechodzą. Nie oznacza to serwerowych 301 ani pełnego testu wszystkich publicznych tras.
- [x] Usunięto newsletter, formularz oraz niepotwierdzony ranking tygodniowy; opisów nie trzeba ponownie migrować od zera.

## Do zamknięcia migracji
| Priorytet | Zadanie | Kryterium ukończenia |
| --- | --- | --- |
| P1 | Produkcyjne adresy SEO i uruchomienie indeksowania | [x] baseUrl domeny głównej; canonical, OG, JSON-LD, robots, sitemap i cele 18 przejść sprawdzone lokalnie; indexingEnabled=true. Pozostaje wdrożenie i sprawdzenie publicznego HTML oraz zgłoszenie sitemap w Search Console. |
| P1 | Własność domeny w GitHub i Search Console | Potwierdzenie ustawień właściciela; poprawny rekord weryfikacji otrzymany z usługi; po uruchomieniu SEO zgłoszona produkcyjna sitemap |
| P1 | Bezpieczeństwo odejścia od Shopify | Prywatny eksport wymaganych danych i płatnych materiałów, próba odczytu/odtworzenia, inwentaryzacja aplikacji i subskrypcji, ustalony rejestrator/odnowienie domeny i koszty; dopiero osobna decyzja o wyłączeniu |
| P1 | Poczta | Test przychodzący i wychodzący z udziałem właściciela oraz wynik SPF/DKIM/DMARC; brak wysyłki bez autoryzacji; sam MX nie zamyka zadania |
| P1 | Polityki i zgodność z faktyczną sprzedażą | Uzupełnione przez właściciela dane administratora/retencja, przegląd zasad cyfrowych produktów i nieaktualnych odniesień do fizycznej wysyłki/kont użytkowników; akceptacja treści bez deklarowania audytu prawnego przez QA |
| P2 | Test użytkowy produkcji | Wszystkie 18 dawnych tras i cele, 404, kontakt, menu klawiaturą, telefon/desktop oraz przeglądarka Instagrama sprawdzone; zapisane wyniki i usterki |
| P2 | Domknięcie lokalności mediów | Ustalić prawa/dostęp do wideo, sposób lokalnego przechowania i rozmiary; usunąć zależność YouTube lub jawnie zatwierdzić wyjątek; oryginały obrazów zachować |
| P2 | Optymalizacja obrazów | Pomiary i test wizualny uzasadniają srcset/nowe warianty; oryginały pozostają bez zmian |

## Oddzielny późniejszy etap — płatności
Wspólny PayPal bez zmian. Powiązanie produktu/wariantu/ceny, dostawa i test procesu sprzedaży wymagają osobnego zakresu. Nie oznaczać sklepu cyfrowego jako gotowego na podstawie działającego linku. Płatny zakup testowy wymaga osobnego polecenia.

## Następny etap rozwoju aplikacji — najpierw specyfikacja
Diety są wdrożone jako funkcja publiczna bez backendu. Kolejne narzędzia z działu Wiedza/Knowledge i atlas pozostają do zaprojektowania; propozycje, zależności, źródła i kryteria: KNOWLEDGE_ROADMAP_2026-09-15.md. Nie oznaczać pomysłów jako gotowych funkcji.
1. Po dostarczeniu Drive/Sheets zinwentaryzować arkusze i reguły w prywatnym miejscu; do publicznego repo wyłącznie niesensytywna specyfikacja.
2. Uzgodnić jednostki, zaokrąglenia, wyjątki i przypadki brzegowe; porównać wyniki z zatwierdzonymi przykładami użytkownika. Kryterium: zgodność każdej odwzorowanej formuły albo jawnie zaakceptowana różnica.
3. Utrzymywać katalog publiczny przez `scripts/import_diets.py`; przed każdym odświeżeniem sprawdzić, że eksport nadal nie zawiera składników, instrukcji, planów ani identyfikatorów klientów.
4. Dopiero gdy zakres obejmie konta, trwały zapis lub panel admina, zaprojektować role i porównać warianty backendu, bazy i magazynu plików wraz z kosztami, backupem i eksploatacją.
