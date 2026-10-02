(() => {
  const form = document.querySelector('#diet-calculator');
  const result = document.querySelector('#diet-result');
  const filters = document.querySelector('#diet-filters');
  const cards = [...document.querySelectorAll('[data-meal]')];
  const count = document.querySelector('#diet-count');
  const empty = document.querySelector('#diet-empty');
  const english = document.documentElement.lang === 'en';
  const text = english ? {
    visible: n => `${n} meals shown`,
    result: (target, perMeal) => `Estimated daily target: ${target} kcal. With the selected number of meals: about ${perMeal} kcal per meal.`,
    error: 'Check the entered values.'
  } : {
    visible: n => `Wyświetlono: ${n} posiłków`,
    result: (target, perMeal) => `Orientacyjny cel dzienny: ${target} kcal. Przy wybranej liczbie posiłków: około ${perMeal} kcal na posiłek.`,
    error: 'Sprawdź poprawność wpisanych wartości.'
  };
  function calculate(event) {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const values = Object.fromEntries(new FormData(form));
    const age = Number(values.age), weight = Number(values.weight), height = Number(values.height);
    const activity = Number(values.activity), meals = Number(values.meals);
    if (![age, weight, height, activity, meals].every(Number.isFinite) || meals < 1) {
      result.textContent = text.error;
      return;
    }
    const bmr = values.sex === 'M'
      ? 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
      : 447.593 + 9.247 * weight + 3.098 * height - 4.33 * age;
    const target = Math.round(bmr * activity);
    result.textContent = text.result(target, Math.round(target / meals));
  }
  function filter() {
    const values = Object.fromEntries(new FormData(filters));
    const query = String(values.query || '').trim().toLocaleLowerCase(document.documentElement.lang);
    let visible = 0;
    for (const card of cards) {
      const show = (!values.category || card.dataset.category === values.category)
        && (!query || card.dataset.name.includes(query));
      card.hidden = !show;
      if (show) visible += 1;
    }
    count.textContent = text.visible(visible);
    empty.hidden = visible !== 0;
  }
  form.addEventListener('submit', calculate);
  filters.addEventListener('input', filter);
  filters.addEventListener('change', filter);
  filter();
})();
