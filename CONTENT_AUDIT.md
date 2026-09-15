# Audyt treści — źródła z 2026-09-10

Aktualizacja 2026-09-15 — audyt PL/EN 1.13: porównano wszystkie 17 par, przywrócono w EN pominięte sekcje, kompletne opisy, FAQ, warianty, zdjęcia partnerów i treści informacyjne. Słownik `data/translations-en.json` tłumaczy opublikowaną treść PL bez skracania. Ceny i cele PayPal zachowane. Oryginalne okładki oraz film nie są tłumaczone; nie deklarujemy angielskiej zawartości płatnych materiałów. Zakres dowodów: `BILINGUAL_AUDIT_2026-09-15.md`. Nie wykonano nowego odczytu Shopify ani audytu prawnego.

Aktualizacja 2026-09-14: lokalne QA ponownie potwierdziło zgodność 7 opisów i 29 wariantów ze snapshotem. Nie pobierano nowych danych Shopify. Poniższe porównania są historyczne; SEO techniczne jest zaimplementowane, a w tym etapie włączono publiczne indeksowanie produkcji.

## Rozszerzenie w 1.10
Ponownie odczytano wszystkie 6 polityk przez Shopify Admin API. Pełny oryginał: data/policies-source-2026-09-10.json.
W 1.09 regulamin pomijał m.in. punkty 4, 7, 9, 10 i 12; zwroty pomijały 7 dni roboczych oraz zmieniały punkt o produktach cyfrowych; wysyłka wprowadzała nieźródłowe ogólne ustalenia e-mailem zamiast ośmiu punktów oryginału. W 1.10 przywrócono źródłowe dokumenty, aktualizując markę/domenę/e-mail i wskazany PayPal.
Oryginały zawierają szerokie wyłączenia odpowiedzialności, brak zwrotów cyfrowych, fizyczną wysyłkę oraz w notce możliwość publikowania treści przez użytkowników. Ich przeniesienie nie stanowi potwierdzenia zgodności z prawem ani aktualnym procesem sprzedaży. Do redakcji prawnej przed finalnym uruchomieniem.
Polityka prywatności została opisana na podstawie faktycznej implementacji (GitHub Pages, YouTube, e-mail/WhatsApp, PayPal), zamiast przepisywania nieprawdziwej rejestracji i newslettera. Nie dodawano wymyślonych okresów przechowywania ani gwarancji bezpieczeństwa.
Partnerzy porównani z /pages/partnerzy: Maczfit, Wypas, PoWolność, Szczaw i Mirabelki; brakujący adres Wypasu uzupełniony. Kod rabatowy pochodzi ze strony źródłowej; nie przeprowadzano testowego zamówienia u partnera. Dane Kontakt potwierdzone polityką CONTACT_INFORMATION; WhatsApp na polecenie użytkownika.
Mapa strony źródłowej zawiera pusty blog /blogs/news, który zachowano jako pustą stronę aktualności. Brak artykułów do migracji.
Poniższy raport 1.09 jest historyczny; ograniczenie audytu do ofert zastępują ustalenia powyżej.

Porównano wersję GitHub 1.08 (b42d9eba60dac18f7c8c4ab6dceb170640f01b56) z bieżącymi opisami siedmiu produktów pobranymi przez Shopify get_product oraz stroną główną https://mikemilekfitness.com/.
Źródłowy snapshot produktów: data/offer-source-2026-09-10.json. Żaden zapis w Shopify nie został wykonany.

## Wynik przed poprawką

Wszystkie siedem podstron zawierało nieźródłowy tekst „Oferta dopasowana do Twojego celu i poziomu” oraz „Wariant ustalany indywidualnie”. Nie były wierną migracją. Wszystkie ceny początkowe były zgodne z Shopify.

| Oferta | Braki w 1.08 uzupełnione w 1.09 | Warianty |
| --- | --- | --- |
| Wegańskie przepisy | Cały opis: ponad 30 przepisów, około 400 kcal na posiłek, makroskładniki, wskazówki | 1: 35 zł |
| Plan diety | Miesiąc, ponad 30 posiłków do wyboru, kontakt po zamówieniu i lista potrzebnych informacji | 2: po 125 zł |
| Karta prezentowa | Ważność 6 miesięcy | 6: 10, 25, 50, 100, 200, 400 zł |
| Konsultacje i prowadzenie online | Dieta, trening, monitorowanie postępów i zakres konsultacji telefonicznej | 4: 440, 620, 80, 125 zł |
| Autorskie ćwiczenia | Ponad 100 stron na partię, 4 zdjęcia, opis, QR do wideo, dostawa e-mailem | 8: wszystkie 135 zł, pojedyncza partia 35 zł |
| Trening personalny | Oryginalny opis jest jedynie nazwą produktu; lokalizacja i czas wynikają z wariantów | 4: 1 h za 125 zł lub 5 × 1 h za 530 zł, kobiety/mężczyźni, Poznań |
| Plan treningowy | Miesiąc, 4 zdjęcia ćwiczenia z ciężarami, fachowy opis i QR do wideo | 4: trzy po 125 zł, ciężary + cardio 35 zł |

## Zasady zgodności

- Pełne opisy renderowane automatycznie ze snapshotu; usunięte tylko znaczniki edytora, bez dopisywania oferty.
- Zmiana marki Wegański Trener → MikeMilekFitness w tytule i opisie karty to świadoma dyspozycja użytkownika.
- E-book z jednym domyślnym wariantem ma czytelną etykietę „E-book” zamiast technicznego „Default Title”.
- Nazwy, kolejność i ceny pozostałych wariantów są zachowane. Nietypowa cena 35 zł w planie treningowym istnieje w źródle — nie poprawiamy jej samodzielnie.
- Każdy produkt ma jedno zdjęcie w odpowiedzi get_product; wszystkie siedem zdjęć już znajduje się lokalnie. Wideo opisane jako zawartość produktu nie jest publicznym plikiem do przeniesienia.
- FAQ i metadane są skrótami faktów z opisów i wariantów. Nie stanowią tekstu identycznego słowo w słowo z Shopify.
- Strona główna: doświadczenie ponad 10 lat, dieta roślinna, trening i współpraca online/bezpośrednio są w oryginale. Nowa marka oraz 40 lat / 2017 / 2018 pochodzą z dyspozycji użytkownika. Usunięto niezweryfikowaną sugestię bieżącego rankingu tygodniowego.
- PayPal, brak newslettera, kontakt e-mail/WhatsApp i brak koszyka są zatwierdzonymi różnicami funkcjonalnymi.
- Wspólny PayPal nie przenosi produktu, wariantu ani kwoty. Nie wprowadzono automatycznej dostawy ani nowej integracji płatności.

## Walidacja i granice

scripts/offer_qa.py porównuje pełne teksty opisów ze snapshotem po normalizacji białych znaków i dopuszczonej zmianie marki, sprawdza warianty, metadane, lokalne linki i ikony.
To potwierdza zgodność z odczytem z 2026-09-10, a nie stałą synchronizację z Shopify.
W chwili audytu 1.09 punkt 3 nie był rozpoczęty. W 1.10 dodano SEO techniczne; nadal nie uruchomiono indeksowania.
W audycie 1.09 nie badano stron prawnych i Partnerów; porównanie źródłowe wykonano w 1.10 (opis powyżej). Przegląd prawny i dopasowanie polityk do procesu sprzedaży nadal pozostają otwarte.
