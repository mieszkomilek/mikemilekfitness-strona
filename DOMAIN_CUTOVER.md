# Domena — AS-IS i pozostałe kroki
Stan zweryfikowany 2026-09-14. Szczegóły testów: AUDIT_2026-09-14.md.

## Potwierdzone
Cloudflare API: strefa active, NS alice.ns.cloudflare.com i nile.ns.cloudflare.com. Wszystkie rekordy strony mają proxied=false (DNS only), więc Cloudflare nie pośredniczy w HTTP/TLS. Stronę obsługuje GitHub Pages. Poniższe rekordy są odczytane, nie tylko planowane:

| Typ | Nazwa | Wartość |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | mieszkomilek.github.io |


Poczta w odczytanej strefie: MX @ z priorytetem 1 do mx.mikemilekfitness.com.cust.b.hostedemail.com; SPF @: v=spf1 include:_spf.hostedemail.com ~all; DMARC: v=DMARC1; p=none. Jest też TXT _provider=shopify. Nie znaleziono DKIM ani rekordu weryfikacji GitHub w tej odpowiedzi. Nie usuwać ani nie uzupełniać rekordów na podstawie domysłów. To nie jest test dostarczania poczty ani dowód kompletności migracji poprzedniej strefy.

| Wejście | Wynik 2026-09-14 |
| --- | --- |
| https://mikemilekfitness.com/ | 200, TLS zaakceptowany przez curl |
| http://mikemilekfitness.com/ | 301 → https://mikemilekfitness.com/ → 200 |
| https://www.mikemilekfitness.com/ | 301 → https://mikemilekfitness.com/ → 200, TLS www poprawny |
| http://www.mikemilekfitness.com/ | 301 → https://mikemilekfitness.com/ → 200 |

Wymuszanie HTTPS działa w testowanych odpowiedziach. Checkbox Enforce HTTPS nie został odczytany: anonimowy GET GitHub /repos/mieszkomilek/strona-mikemilekfitness/pages zwrócił 404, co nie dowodzi braku konfiguracji. Nie ma potrzeby ponownego przełączania NS ani dodawania domeny tylko na podstawie historycznej checklisty.

## Niewiadome i kolejne kroki
Aktualny rejestrator, płatnik i termin odnowienia domeny wymagają sprawdzenia przez właściciela. Zmiana DNS nie oznacza transferu do Cloudflare Registrar. Stan anulowania Shopify i rozliczeń nie jest potwierdzony.
Pozostają: weryfikacja własności domeny w GitHub, produkcyjne adresy SEO, indeksowanie i Search Console, pełny test tras/UI, poczta, prywatny backup i rozliczenia. Kryteria: MIGRATION_PLAN.md. Nie wykonano tych operacji w audycie.

## Dawne adresy
Mapa data/redirect-map.json generuje 18 stron HTML z meta refresh, linkiem i canonical; nie są to HTTP 301 do nowych podstron. Cele używają obecnie baseUrl podglądu. DNS nie mapuje ścieżek. Ewentualne serwerowe 301 wymagają osobnej decyzji o warstwie HTTP.

## Historia i rollback
Według notatek z 2026-09-10 domeną zarządzano przez Shopify; wcześniejsze NS to ns-cloud-c1/c2/c3/c4.googledomains.com. Zapisane A 185.199.108.153 i CNAME www do github.io były już etapem migracji, nie konfiguracją powrotu do Shopify. Nie traktować ich jako gotowego rollbacku sklepu.
Przed kolejną zmianą DNS zabezpieczyć prywatny eksport aktualnej strefy. Powrót wersji strony: nowy revert commit i ponowny deployment sprawdzonego artefaktu. Powrót hostingu do Shopify wymaga aktualnych, potwierdzonych ustawień sklepu i domeny; nie zgadywać rekordów ani pochopnie usuwać custom domain. Zachować rekordy pocztowe.
