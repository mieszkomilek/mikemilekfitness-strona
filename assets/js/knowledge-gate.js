// A review convenience only. Public HTML and source remain accessible.
// The owner explicitly accepted this date gate; it is not authentication.
(function () {
  'use strict';
  var gate = document.getElementById('review-gate');
  var content = document.getElementById('knowledge-content');
  var footer = document.getElementById('knowledge-footer');
  var form = document.getElementById('review-form');
  var input = document.getElementById('review-code');
  var error = document.getElementById('review-error');
  var key = 'mmf-knowledge-review-date';
  var en = document.documentElement.lang === 'en';
  function today() {
    var parts = new Intl.DateTimeFormat('en', {
      timeZone: 'Europe/Warsaw', year: 'numeric', month: '2-digit', day: '2-digit'
    }).formatToParts(new Date());
    return ['year', 'month', 'day'].map(function (type) {
      return parts.find(function (part) { return part.type === type; }).value;
    }).join('');
  }
  function unlock(focus) {
    gate.hidden = true;
    content.hidden = false;
    footer.hidden = false;
    if (focus) content.focus();
  }
  function lock() {
    gate.hidden = false;
    content.hidden = true;
    footer.hidden = true;
  }
  var accepted = null;
  try { accepted = sessionStorage.getItem(key); } catch (_) {}
  if (accepted === today()) unlock(false);
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (input.value.trim() !== today()) {
      error.textContent = en ? 'Incorrect code. Please try again.' : 'Nieprawidłowy kod. Spróbuj ponownie.';
      input.setAttribute('aria-invalid', 'true');
      input.focus();
      return;
    }
    accepted = today();
    try { sessionStorage.setItem(key, accepted); } catch (_) {}
    input.value = '';
    input.removeAttribute('aria-invalid');
    error.textContent = '';
    unlock(true);
  });
  // An open tab also returns to the gate when the Polish calendar date changes.
  function checkDate() { if (accepted && accepted !== today()) { accepted = null; lock(); } }
  window.setInterval(checkDate, 30000);
  window.addEventListener('pageshow', checkDate);
  document.addEventListener('visibilitychange', checkDate);
}());
