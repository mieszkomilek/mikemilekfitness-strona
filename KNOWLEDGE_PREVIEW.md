# Wiedza — podgląd 1.14

## Zakres i decyzja 2026-09-15
Użytkownik zaakceptował wygląd lokalnego hubu oraz prostą bramkę datową mimo publicznego HTML/repo. Implementacja własna; nie kopiowano kodu, grafik ani treści strony Ewy.

Adresy: /wiedza/ oraz /en/wiedza/. Hub i siedem kategorii na język. Dział dodany do nawigacji istniejących stron podczas build. Kategorie pokazują planowane tematy; kalkulatory, atlas interaktywny i artykuły nie są jeszcze zaimplementowane.

## Bramka
Kod to aktualna data YYYYMMDD w Europe/Warsaw, obliczana według zegara urządzenia. Nie jest sekretem ani uwierzytelnianiem. sessionStorage zapamiętuje dzień odblokowania dla karty i działa przy zmianie kategorii lub języka. Po zmianie daty bramka wraca przy wejściu, powrocie do karty lub okresowej kontroli co 30 sekund. Zablokowane storage nie uniemożliwia ręcznego wejścia; bez JS widoczna jest informacja o konieczności jego włączenia.

Każda podstrona ma własną bramkę. Nie wysyła kodu do serwera. Ukrycie main w HTML zapobiega błyskowi treści podczas ładowania, ale odczyt źródła nadal daje dostęp do tekstów.

## SEO i publikacja
16 stron ma noindex,nofollow, brak w sitemap. Dotychczasowe strony nadal są indeksowalne i sitemap zawiera 34 adresy. Nie blokujemy pobierania robots.txt, aby robot mógł zobaczyć noindex. Indeksowanie Wiedzy będzie osobnym krokiem po uzupełnieniu i akceptacji treści; wtedy dodać canonical/hreflang i sitemap docelowych materiałów.

## Testy
site_build.py, site_qa.py, migration_qa.py: PASS. QA sprawdza wszystkie 16 stron podglądu, działające lokalne linki i pary językowe, pojedynczy H1, początkowe ukrycie treści, skrypt/formularz bramki oraz wykluczenie z sitemap. Dotychczasowe testy 7 ofert, 29 wariantów, 22 hashy mediów i SEO PL/EN przechodzą.
Przeglądarka lokalna: błędny kod daje komunikat PL; poprawny kod otwiera hub; przejście do Atlasu zachowuje odblokowanie, PL→EN prowadzi do tej samej kategorii i pokazuje angielską treść. Przegląd wizualny EN wykonany. Test zmiany daty i pełny zestaw urządzeń nie były wykonane.

Do potwierdzenia po pushu: wynik deploymentu i odczyt publicznych stron. Nie uznawać niniejszego wpisu za dowód wdrożenia.
