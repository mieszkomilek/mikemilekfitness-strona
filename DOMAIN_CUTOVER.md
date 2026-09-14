# Przełączenie domeny — stan 2026-09-11

## Aktualny operator DNS

Do 2026-09-10 panel zarządzania domeną `mikemilekfitness.com` znajdował się w Shopify. 2026-09-10 nameservery przełączono na Cloudflare: `alice.ns.cloudflare.com` i `nile.ns.cloudflare.com`. Strefa Cloudflare ma status Active, rekordy strony i poczty są odtworzone, a 2026-09-11 certyfikat GitHub Pages został wystawiony. Rejestracja domeny nadal jest u dotychczasowego rejestratora.

## Stan odczytany z DNS przed przełączeniem

- NS: ns-cloud-c1/c2/c3/c4.googledomains.com (infrastruktura widoczna przy zarządzaniu przez Shopify).
- A @: 185.199.108.153 (ustawione w Shopify; pozostałe adresy A GitHub Pages mogą być dodane zgodnie z polityką operatora).
- AAAA @: brak na zrzucie po zmianie (nie dodawano bez potwierdzenia formularza Shopify).
- CNAME www: mieszkomilek.github.io (ustawione w Shopify).
- MX @: 1 mx.mikemilekfitness.com.cust.b.hostedemail.com.
- TXT SPF @: v=spf1 include:_spf.hostedemail.com ~all.

To odczyt rekordów, nie pełny eksport strefy. Przed zapisem zrobić eksport z panelu, w tym DKIM, DMARC, weryfikacje i pozostałe subdomeny. Nie zmieniać NS ani rekordów pocztowych.

## Docelowe rekordy

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

Zastępujemy wyłącznie dotychczasowe A/AAAA @ i CNAME www. Nie wpisywać nazwy repozytorium do CNAME.

## Kolejność wykonania — stan

1. Wykonane: Cloudflare zone utworzona, rekordy przygotowane, custom domain ustawiona w GitHub Pages.
2. Zabezpieczyć eksport strefy i dane/materiały potrzebne z Shopify; publiczne kopie źródeł w data/ nie są kopią klientów, zamówień, aplikacji ani płatnych plików.
3. Zweryfikować domenę w ustawieniach konta GitHub, publikując podany przez GitHub rekord TXT. Wartości TXT nie zgadywać.
4. Wykonane: Custom domain ustawiona na `mikemilekfitness.com`.
5. Wykonane: nameservery Shopify przełączone na Cloudflare; poczta zachowana.
6. Ustawić baseUrl=https://mikemilekfitness.com/ oraz indexingEnabled=true w site.config.json; wygenerować, sprawdzić i opublikować.
7. Certyfikat wystawiony 2026-09-11. Następny krok: zaznaczyć Enforce HTTPS i sprawdzić domenę główną, www, stare adresy produktów/polityk i kontakt.
8. W Google Search Console dodać/zweryfikować domenę i zgłosić https://mikemilekfitness.com/sitemap.xml. Potrzebna zalogowana sesja właściciela.
9. Shopify wygaszać dopiero po testach oraz zabezpieczeniu domeny/poczty i wymaganych prywatnych danych; PayPal jest osobnym późniejszym etapem.

## Zachowanie starych adresów

Generator tworzy fizyczne strony pod starymi ścieżkami z natychmiastowym meta refresh, linkiem i canonical do nowego adresu. To nie jest przekierowanie HTTP 301; GitHub Pages nie zapewnia własnych reguł 301 dla dowolnych ścieżek. Mapa znajduje się w data/redirect-map.json. Pełne 301 wymagają dodatkowej warstwy obsługi HTTP — DNS A/CNAME nie przekierowuje ścieżek URL.

## Powrót w razie problemu

Przywrócić zapisane A/AAAA/CNAME, usunąć custom domain z Pages i przywrócić konfigurację podglądu baseUrl + noindex. Zachować działający sklep do czasu weryfikacji przełączenia.

Źródło rekordów i kolejności: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site (odczyt 2026-09-10).
Przy publikacji z GitHub Actions plik CNAME w repo nie ustawia custom domain — wymagane są ustawienia Pages.
