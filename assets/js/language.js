(function () {
  var path = window.location.pathname;
  var english = path === '/en' || path.indexOf('/en/') === 0;
  var localPath = english ? path.replace(/^\/en\/?/, '/') : path;
  var file = localPath.split('/').filter(Boolean).pop() || 'index.html';
  var page = file === 'index.html' ? '' : file;
  var targets = { pl: '/' + page, en: '/en/' + page };
  var preference = null;
  try { preference = window.localStorage.getItem('mmf-language'); } catch (error) {}
  var host = document.querySelector('.header-inner') || document.querySelector('header');
  if (!host) {
    var languageHeader = document.createElement('header');
    languageHeader.className = 'language-only-header';
    languageHeader.innerHTML = '<a href="' + (english ? '/en/' : '/') + '">MikeMilekFitness</a>';
    document.body.insertBefore(languageHeader, document.body.firstChild);
    host = languageHeader;
  }
  var switcher = document.createElement('nav');
  switcher.className = 'language-switcher';
  switcher.setAttribute('aria-label', english ? 'Language selection' : 'Wybór języka');
  switcher.innerHTML = '<a href="' + targets.pl + '" lang="pl" aria-current="' + (!english) + '">🇵🇱 PL</a><a href="' + targets.en + '" lang="en" aria-current="' + english + '">🇬🇧 EN</a>';
  host.appendChild(switcher);
  switcher.addEventListener('click', function (event) { var link = event.target.closest('a[lang]'); if (link) try { window.localStorage.setItem('mmf-language', link.lang); } catch (error) {} });
  function select(language) { try { window.localStorage.setItem('mmf-language', language); } catch (error) {} window.location.assign(targets[language]); }
  if (!preference && !english) {
    var dialog = document.createElement('div');
    dialog.className = 'language-choice'; dialog.setAttribute('role', 'dialog'); dialog.setAttribute('aria-modal', 'true'); dialog.setAttribute('aria-labelledby', 'language-choice-title');
    dialog.innerHTML = '<div class="language-choice-card"><h2 id="language-choice-title">Wybierz język / Choose your language</h2><p>Wybór możesz później zmienić w nagłówku.</p><div class="language-choice-actions"><button type="button" data-language="en">🇬🇧 English</button><button type="button" data-language="pl">🇵🇱 Polski</button></div></div>';
    dialog.addEventListener('click', function (event) { var button = event.target.closest('button[data-language]'); if (button) select(button.getAttribute('data-language')); });
    document.body.appendChild(dialog); dialog.querySelector('button').focus();
  }
}());
