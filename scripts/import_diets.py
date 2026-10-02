"""Create a public, non-sensitive meal preview export from the private planner.

The public export intentionally excludes ingredients, preparation instructions,
client data and saved plans. Run manually when the private catalog changes.
"""
from argparse import ArgumentParser
from pathlib import Path
import json
import shutil
import sqlite3
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
NUTRIENTS = ('kcal', 'protein', 'carbs', 'fat', 'fiber')
CATEGORIES = {
    'salads': ('Sałatki', 'Salads'),
    'handheld': ('Burgery, pity i wrapy', 'Burgers, pitas and wraps'),
    'sweet': ('Słodkie i owocowe', 'Sweet and fruit-based'),
    'main': ('Dania główne', 'Main dishes'),
}
UI_TRANSLATIONS = {
    'min': 'min', 'kcal': 'kcal', 'g': 'g', '— kcal': '— kcal', '— g': '— g',
    'Diety roślinne | MikeMilekFitness': 'Plant-based diets | MikeMilekFitness',
    'Przeglądaj 35 autorskich posiłków roślinnych i oblicz orientacyjne zapotrzebowanie kaloryczne.': 'Browse 35 original plant-based meals and estimate your calorie needs.',
    'Autorskie posiłki roślinne i kalkulator zapotrzebowania kalorycznego.': 'Original plant-based meals and a calorie needs calculator.',
    'Diety': 'Diets',
    'MikeMilekFitness / Diety': 'MikeMilekFitness / Diets',
    'Roślinne posiłki dopasowane do Twojego celu': 'Plant-based meals matched to your goal',
    'Poznaj 35 autorskich propozycji posiłków. Skorzystaj z kalkulatora, aby oszacować dzienny cel i kaloryczność jednego posiłku.': 'Explore 35 original meal ideas. Use the calculator to estimate your daily target and calories per meal.',
    'Kalkulator': 'Calculator',
    'Oblicz orientacyjne zapotrzebowanie': 'Estimate your calorie needs',
    'Wynik ma charakter informacyjny. W przypadku chorób, ciąży lub szczególnych potrzeb skonsultuj dietę ze specjalistą.': 'The result is for information only. Consult a qualified professional in case of illness, pregnancy or specific dietary needs.',
    'Płeć': 'Sex', 'Kobieta': 'Woman', 'Mężczyzna': 'Man', 'Wiek': 'Age',
    'Waga · kg': 'Weight · kg', 'Wzrost · cm': 'Height · cm', 'Aktywność': 'Activity',
    'Niska': 'Low', 'Lekka': 'Light', 'Umiarkowana': 'Moderate', 'Wysoka': 'High',
    'Posiłki dziennie': 'Meals per day', 'Oblicz': 'Calculate', 'Katalog': 'Catalog',
    '35 autorskich posiłków': '35 original meals', 'Szukaj posiłku': 'Search meals',
    'Nazwa posiłku': 'Meal name', 'Kategoria': 'Category', 'Wszystkie kategorie': 'All categories',
    'Brak posiłków spełniających wybrane kryteria.': 'No meals match the selected criteria.',
    'składników': 'ingredients', 'Energia': 'Energy', 'Białko': 'Protein',
    'Węglowodany': 'Carbohydrates', 'Tłuszcz': 'Fat',
    'Podgląd posiłku. Pełny przepis i skalowanie porcji są dostępne w indywidualnym planie.': 'Meal preview. The full recipe and portion scaling are available in an individual plan.',
    'Plan indywidualny': 'Individual plan', 'Potrzebujesz pełnego planu i gramatur?': 'Do you need a complete plan with precise quantities?',
    'Podgląd nie publikuje pełnych receptur. Napisz, aby ustalić cel, liczbę posiłków i wariant współpracy.': 'The preview does not publish complete recipes. Get in touch to discuss your goal, number of meals and coaching option.',
    'Zapytaj o plan diety': 'Ask about a diet plan',
}


def normalized(value):
    value = unicodedata.normalize('NFKD', value.casefold().replace('ł', 'l'))
    return ' '.join(''.join(c for c in value if not unicodedata.combining(c)).split())


def category(name):
    key = normalized(name)
    if 'salat' in key:
        return 'salads'
    if any(word in key for word in ('burger', 'bulka', 'pity', 'wrap')):
        return 'handheld'
    if any(word in key for word in ('pancake', 'nalesnik', 'owoc', 'arbuz')):
        return 'sweet'
    return 'main'


def nutrition(meal, products):
    totals = {key: 0 for key in NUTRIENTS}
    complete = True
    for ingredient in meal['ingredients']:
        product = products.get(normalized(ingredient['product']))
        if not product:
            complete = False
            continue
        grams = ingredient['baseGrams']
        for key in NUTRIENTS:
            value = product.get(key)
            if value is None:
                complete = False
            else:
                totals[key] += value * grams / 100
    return ({key: round(value) for key, value in totals.items()} if complete else None)


def main():
    parser = ArgumentParser()
    parser.add_argument('--planner-dir', type=Path, required=True)
    parser.add_argument('--getdiet-db', type=Path, required=True)
    args = parser.parse_args()
    catalog = json.loads((args.planner_dir/'app/catalog.json').read_text())
    products = {normalized(item['name']): item for item in catalog['products']}
    connection = sqlite3.connect(args.getdiet_db)
    english = {row[0] - 200: row[1] for row in connection.execute(
        'select meal_id, meal_name_us from calories_meal order by meal_id'
    )}
    connection.close()
    output = []
    assets = ROOT/'assets/diets'
    assets.mkdir(parents=True, exist_ok=True)
    for meal in catalog['meals']:
        meal_id = int(meal['id'])
        source = args.planner_dir/f'app/assets/meal-{meal_id}.jpg'
        if not source.is_file():
            raise FileNotFoundError(source)
        shutil.copy2(source, assets/source.name)
        group = category(meal['name'])
        output.append({
            'id': meal_id,
            'name': meal['name'],
            'nameEn': english.get(meal_id, meal['name']),
            'image': f'assets/diets/{source.name}',
            'category': group,
            'categoryLabel': CATEGORIES[group][0],
            'categoryLabelEn': CATEGORIES[group][1],
            'preparationMinutes': 20,
            'ingredientCount': len(meal['ingredients']),
            'nutrition': nutrition(meal, products),
        })
    (ROOT/'data/diets.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    translations_path = ROOT/'data/translations-en.json'
    translations = json.loads(translations_path.read_text())
    translations.update(UI_TRANSLATIONS)
    for item in output:
        translations[item['name']] = item['nameEn']
        translations[item['name'].casefold()] = item['nameEn'].casefold()
        translations[item['categoryLabel']] = item['categoryLabelEn']
        translations[str(item['preparationMinutes'])] = str(item['preparationMinutes'])
        translations[str(item['ingredientCount'])] = str(item['ingredientCount'])
        if item['nutrition']:
            for key, value in item['nutrition'].items():
                translations[str(value)] = str(value)
                unit = 'kcal' if key == 'kcal' else 'g'
                translations[f'{value} {unit}'] = f'{value} {unit}'
    translations_path.write_text(json.dumps(translations, ensure_ascii=False, indent=2, sort_keys=True) + '\n')
    print(f"Imported {len(output)} public meal previews; no recipes or client data")


if __name__ == '__main__':
    main()
