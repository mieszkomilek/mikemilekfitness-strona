# PROJECT_BRAIN — MikeMilekFitness

## Zasady odczytu i źródła prawdy
Stan zweryfikowany 2026-09-14 opisują sekcje AS-IS poniżej oraz AUDIT_2026-09-14.md. TO-BE oznacza kierunek zaakceptowany przez użytkownika, nie wdrożenie. TODO i kryteria ukończenia: MIGRATION_PLAN.md. Starsze decyzje na końcu są historią; nie zastępują aktualnego stanu. Każda kolejna zmiana wymaga aktualizacji dokumentacji i weryfikacji przed commitem.

## AS-IS — potwierdzone kodem i odczytem usług
- Publiczne repo: mieszkomilek/strona-mikemilekfitness, main. Przed tym audytem HEAD ab802aa4e76e15c41eab3c3401bc538f07c5cdc3, wersja strony 1.11. Brak nowszych zmian w pobranej historii. Deployment #15 zakończony sukcesem 2026-09-14; publiczny HTML zgodny bajtowo z lokalnym buildem.
- Statyczny HTML/CSS/JavaScript, generator i QA w Pythonie (standard library); brak backendu, bazy, kont klientów i panelu administracyjnego. Dane: data/home.json, data/catalog.json i snapshoty; szablony w templates/. index.html jest generowany.
- GitHub Actions .github/workflows/pages.yml buduje i publikuje wyłącznie _site/. Import mediów działa z --offline, niczego nie pobiera z Shopify ani nie zapisuje do repo podczas CI.
- Hosting: GitHub Pages pod https://mikemilekfitness.com/. Cloudflare obsługuje DNS, strefa active, alice.ns.cloudflare.com i nile.ns.cloudflare.com. Cztery A i cztery AAAA GitHub Pages oraz CNAME www są DNS only. Szczegóły: DOMAIN_CUTOVER.md.
- HTTPS głównej domeny: 200. HTTP głównej, HTTP www i HTTPS www: 301 do https://mikemilekfitness.com/, następnie 200. curl weryfikował TLS bez -k. Wymuszanie HTTPS potwierdzone zachowaniem HTTP; stan checkboxa Enforce HTTPS nie został odczytany z panelu/API.
- SEO nadal przed uruchomieniem: indexingEnabled=false, baseUrl wskazuje adres github.io, productionUrl domenę główną. Publiczna strona ma noindex,follow, canonical/OG/JSON-LD podglądu, pustą sitemap; robots wskazuje sitemap podglądu. Nie włączono indeksowania w tym zadaniu.
- Lokalne strony: główna, katalog, 7 ofert, kontakt, partnerzy, 6 stron polityk/noty i puste aktualności; build zawiera też 404. 18 dawnych ścieżek ma HTML z meta refresh i linkiem (nie HTTP 301 do nowej podstrony). Obecnie cel tych przejść również wskazuje github.io.
- Oferty: 7 opisów i 29 wariantów zgodnych z zapisanym odczytem Shopify z 2026-09-10. To snapshot, nie bieżąca synchronizacja. Nie korygować samodzielnie nietypowej ceny 35 zł. CONTENT_AUDIT.md opisuje pochodzenie i ograniczenia.
- Wszystkie 22 pliki manifestu są lokalne i mają poprawne SHA-256: 18 obrazów w assets/shopify/ oraz 4 fonty w assets/fonts/ (11 067 190 bajtów). Nazwa katalogu nie oznacza zależności sieciowej. Wideo strony nadal jest osadzeniem YouTube; 8 zapisanych odnośników nie stanowi archiwum filmów. Nie ma zależności wykonawczej od CDN Shopify; pełna lokalność wideo nie jest osiągnięta.
- Kontakt: e-mail, WhatsApp i sociale; bez newslettera i formularza. Marka MikeMilekFitness. Opowieść o wieku 40 lat i weganizmie jest deklaracją użytkownika z 2026-09-09, nie wyliczeniem daty urodzenia.
- PayPal pozostaje wskazanym wcześniej wspólnym URL z site.config.json. Historyczne pochodzenie linku nie upoważnia do kopiowania repo strona-ewamilek. Link nie przekazuje produktu, wariantu ani ceny; brak automatycznej dostawy. Transakcje nie były testowane.

## Deklaracje i niewiadome
Użytkownik potwierdził HTTPS po ponownym dodaniu domeny w Pages; obecny test potwierdza działanie. Zmiana NS nie dowodzi transferu rejestracji. Aktualny rejestrator, odnowienie domeny, status abonamentu Shopify, eksport prywatnych danych i materiałów, rozliczenia oraz dostarczanie poczty nie zostały sprawdzone. MX/SPF/DMARC są w Cloudflare; nie oznacza to testu poczty. Brak DKIM w odczytanej strefie wymaga wyjaśnienia z operatorem, nie zgadywania rekordu. Nie potwierdzono weryfikacji własności domeny w GitHub ani Search Console. Nie wykonywano nowego audytu danych Shopify ani operacji PayPal.

## TO-BE — zaakceptowany kierunek, projektowanie przed implementacją
Aplikacja z backendem w Javie, wygodnym UI i panelem administracyjnym: generator diet, kalkulatory zapotrzebowania kalorycznego, atlas ćwiczeń ze zdjęciami i rysunkami oraz sprzedaż produktów cyfrowych. Najpierw odwzorować reguły i formuły użytkownika z Google Drive/Sheets oraz zweryfikować je na zaakceptowanych przykładach. Użytkownik dostarczy dane później; integracja Drive nie jest wykonana.
Spring Boot, PostgreSQL, React/Next.js, S3, Render i Hetzner są propozycjami, nie decyzjami. Wybór architektury, dostawców i kosztów wymaga osobnego projektu. Prywatne repo jest rozważane; nie zmieniać widoczności ani nie uruchamiać płatnych usług bez ustalenia zakresu i kosztów.

## Stałe ograniczenia i decyzja tego audytu
Nie rozpoczynać przebudowy ani zmian płatności. Nie kopiować kodu, treści i grafik strona-ewamilek. Nie publikować sekretów, danych klientów ani płatnych materiałów — także w historii Git. Publiczny snapshot strony nie jest backupem sklepu. Nie wyłączać Shopify przed zabezpieczeniem domeny, materiałów/danych i sprawdzeniem rozliczeń. Treści bez wymyślonych obietnic, opinii i parametrów. Media mają być lokalne; pozostałą zależność YouTube rozstrzygnąć osobno.
Audyt zmienia tylko dokumentację. version.txt pozostaje 1.11, ponieważ nie zmieniamy artefaktu strony; rewizję dokumentacji identyfikuje commit i wpis z 2026-09-14 w VERSION_HISTORY.md.

## Historyczne decyzje wersji 1.01–1.09
Poniższe zapisy dokumentują stan danego etapu. Kontakt wyłącznie mailowy został zastąpiony e-mailem/WhatsApp/socialami; opisy zastępcze 1.08 zastąpiono pełnymi w 1.09; zakres audytu polityk rozszerzono w 1.10. Bieżące ustalenia są powyżej.

## Decyzje wersji 1.04
Newsletter został usunięty z zakresu. Kontakt odbywa się wyłącznie przez `mieszkomilek@gmail.com`; nie migrujemy formularza kontaktowego. Wszystkie linki płatności nadal kierują do PayPal. Strony `kontakt.html` i `partnerzy.html` zostały dodane jako kolejny etap migracji, przed dalszymi podstronami ofertowymi. Decyzje te są częścią Second Brain i muszą pozostać aktualne przy kolejnych zmianach.

## Decyzje wersji 1.05
Dodano lokalne `warunki.html` i `zwroty.html`; stopka nie prowadzi już do Shopify. Treść jest roboczym przeniesieniem zasad odczytanych z Shopify i wymaga sprawdzenia prawnego przed uruchomieniem docelowej sprzedaży. Kontakt pozostaje wyłącznie mailowy, a płatności pozostają w PayPal.

## Branding od wersji 1.01
Główna marka to MikeMilekFitness, zamiast Wegański Trener. Nowy tekstowy logotyp i favicon M; oryginalne pliki mediów pozostają zachowane. Weganizm przedstawiamy jako wyrazistą ciekawostkę osobistą w limonkowym bloku pod hero. Użytkownik podał: 40 lat, wegetarianizm od 2017, weganizm od 2018 i nadal świetna forma. Wiek jest deklaracją na dzień 2026-09-09, nie obliczamy daty urodzenia ani nie aktualizujemy go automatycznie. Opisy produktów roślinnych i oryginalne okładki pozostają zgodne z ich zawartością. Wszystkie płatności pozostają bez zmian. Wersja 1.00 została pomyślnie opublikowana na Pages.

## Decyzje wersji 1.06
Kontakt: WhatsApp +48 606 708 185, e-mail, Instagram i Facebook. Formularza nie ma. Dodano oferta.html z PayPal.

## Decyzje wersji 1.07
Link Kontakt w nagłówku prowadzi do `kontakt.html`. Dodano lokalne `prywatnosc.html` i `wysylka.html`; kontakt i płatności pozostają bez zmian.

## Decyzje wersji 1.08
Każda z siedmiu ofert ma własną podstronę opartą na handle produktu. Karty na stronie głównej prowadzą do szczegółów, a osobny przycisk prowadzi do wspólnego PayPal. Opisy są celowo ogólne do czasu potwierdzenia pełnych treści i dostawy cyfrowej.

## Decyzje i audyt wersji 1.09 — 2026-09-10
- Przed SEO technicznym wykonano ponowny odczyt siedmiu produktów przez Shopify search_products/get_product. Źródło: data/offer-source-2026-09-10.json, bez danych klientów i stanów magazynowych.
- Wersja 1.08 nie była pełną migracją opisów: zawierała identyczny tekst zastępczy i niepotwierdzone „Wariant ustalany indywidualnie”. Usunięto oba; przywrócono pełne opisy i 29 wariantów z cenami. Ceny początkowe były zgodne.
- Treść opisów pozostaje identyczna po usunięciu znaczników edytora i normalizacji odstępów; jedyna zmiana słowna w opisach: Wegański Trener → MikeMilekFitness w karcie prezentowej, zgodnie z dyspozycją użytkownika. Nazwy i ceny wariantów zachowane, również nietypowe 35 zł dla treningu ciężary + cardio. Nie korygować ich na podstawie domysłów.
- FAQ i indywidualne metadane SEO są redakcyjnymi skrótami potwierdzonych opisów i wariantów; nie dodano terminów realizacji, gwarancji wyników ani automatycznej dostawy. Materiały ebook/video to opisy sprzedawanych produktów; prywatnych plików nie publikujemy.
- Główna: opis i misję skrócono do faktów z oryginału; osobista historia wieku i weganizmu pochodzi od użytkownika. Nagłówek ofert „Najczęściej kupowane w tym tygodniu” zastąpiono neutralnym, ponieważ statyczny katalog nie korzysta z tygodniowych statystyk.
- Ikony SVG Instagram/Facebook/e-mail w nagłówku i stopce są osadzone lokalnie, z tekstem dostępnym dla czytników. Kontakt w stopce prowadzi do kontakt.html; osobny e-mail pozostaje mailto.
- Wspólny PayPal pozostaje bez zmian. Strony jawnie wyjaśniają brak przekazywania wariantu/kwoty i odsyłają do kontaktu przed płatnością.
- oferta.html jest generowana jako pełny katalog i trafia do _site, co naprawia niedziałający link z ofert.
- Podgląd nadal noindex; bez zmiany domeny, DNS, mapy indeksowania i bez rozpoczęcia punktu 3. Testy weryfikują wszystkie lokalne linki i zgodność opisów ze snapshotem.
- Raport porównawczy: CONTENT_AUDIT.md. Audyt treści w tym etapie dotyczy strony głównej i siedmiu ofert, nie potwierdza zgodności stron prawnych ani Partnerów.
