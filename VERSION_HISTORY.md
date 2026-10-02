# Historia wersji

Zmiana nazwy repo na mieszkomilek/mikemilekfitness-strona na polecenie użytkownika: zaktualizowano lokalny origin SSH, README, Second Brain i adres testowego podglądu w migration_qa.py. Fetch przez istniejący klucz SSH poprawny. Bez zmiany domeny, folderu i wersji strony 1.14; datowane audyty zachowują historyczną nazwę repo.

2026-09-15 — propozycja działu Wiedza/Knowledge: przegląd serwisów PL/świat, 42 kalkulatory/narzędzia i komponenty, mapa mięśni, 7 kategorii, strategia SEO PL/EN oraz kryteria etapów. Dokument: KNOWLEDGE_ROADMAP_2026-09-15.md. Wyłącznie dokumentacja, bez wdrażania funkcji i zmiany wersji 1.13.

2026-09-14 — włączenie produkcyjnego SEO: baseUrl domeny głównej, index,follow, canonical/OG/JSON-LD produkcji oraz produkcyjna sitemap i robots. PayPal i treści ofert bez zmian. Weryfikacja: site_qa i migration_qa.

2026-09-14 — rewizja dokumentacji przy wersji strony 1.11: audyt repo/deploymentu, HTTPS i www, odczyt Cloudflare DNS, uporządkowanie AS-IS/TO-BE/TODO oraz ograniczeń. Bez zmian kodu, SEO, DNS i płatności. Testy oraz zakres dowodów: AUDIT_2026-09-14.md. Wiersz 1.11 opisuje historyczne zdarzenie z 11 września; commit ab802aa opublikowano 14 września.
| Wersja | Data | Opis |
| --- | --- | --- |
| 1.15 | 2026-10-02 | Diety/Diets: 35 publicznych podglądów posiłków z prywatnego plannera, lokalne zdjęcia, kategorie, wyszukiwarka, zbiorcze makro i kalkulator kcal w JavaScript. Bez pełnych przepisów, zapisanych planów i danych klientów; importer, build i QA obejmują granicę publikacji. |
| 1.14 | 2026-09-15 | Zakładka Wiedza/Knowledge: 16 stron podglądu, link w nawigacji, zaakceptowana bramka z bieżącą datą Europe/Warsaw, sesja dzienna, noindex i brak wpisów sitemap. Treści i narzędzia oznaczone jako przygotowywane. |
| 1.13 | 2026-09-15 | Pełna zgodność struktury 17 par PL/EN: YouTube, intro, fakty, stopka, opisy ofert, 29 wariantów, FAQ, partnerzy i polityki. Jawny słownik tłumaczeń z przerwaniem build przy brakach; testy porównawcze, widoczne flagi na telefonie, poprawa kontrastu i usunięcie duplikatów metadanych. Szczegóły: BILINGUAL_AUDIT_2026-09-15.md. |
| 1.12 | 2026-09-14 | Wersja angielska pod /en/, wybór języka przy pierwszej wizycie, stały przełącznik PL/EN, zapamiętanie ustawienia, hreflang i 34 adresy sitemap. |
| 1.11 | 2026-09-11 | Aktywny Cloudflare DNS, wystawiony certyfikat GitHub Pages HTTPS i aktualizacja Second Brain. |
| 1.10 | 2026-09-10 | Audyt pozostałych treści, pełne polityki źródłowe, SEO wszystkich stron, stare adresy, tryb produkcji i przygotowanie DNS. |
| 1.09 | 2026-09-10 | Pełne opisy z Shopify, 29 wariantów, źródłowy audyt treści, SEO ofert, katalog i ikony kontaktu. |
| 1.01 | 2026-09-09 | Marka MikeMilekFitness, nowy opis i wyróżniona historia: 40 lat, wegetarianizm od 2017, weganizm od 2018. |
| 1.02 | 2026-09-09 | Film YouTube osadzony na stronie, wyciszony, automatycznie odtwarzany i zapętlony. |
| 1.03 | 2026-09-09 | Porównanie z Shopify, autorskie logo w nagłówku oraz widoczne linki do Instagrama i Facebooka. |
| 1.04 | 2026-09-09 | Usunięcie newslettera, kontakt wyłącznie przez e-mail oraz migracja stron Kontakt i Partnerzy bez formularza. |
| 1.08 | 2026-09-09 | Osobne podstrony siedmiu ofert z cenami i PayPal; opisy i warianty były zastępcze (poprawione w 1.09). |
| 1.07 | 2026-09-09 | Link Kontakt z nagłówka prowadzi do podstrony oraz dodane lokalne polityka prywatności i wysyłka. |
| 1.06 | 2026-09-09 | Kontakt WhatsApp, telefon, e-mail i social media oraz strona Oferta z PayPal. |
| 1.05 | 2026-09-09 | Dodane lokalne strony Warunki świadczenia usług i Polityka zwrotów; stopka prowadzi do lokalnych wersji. |
| 1.00 | 2026-09-09 | Pierwsza statyczna strona główna Wegańskiego Trenera, oryginalne media Shopify, wskazany PayPal, dokumentacja AI oraz GitHub Pages. |

Punkt przywracania: commit zawierający wersję. Przywracanie przez nowy commit/revert, bez przepisywania historii main. Nie używać numeracji repo Ewy.
