"""Translate the complete Polish DOM; missing translations fail the build."""
from html import escape, unescape
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json
import re


class EnglishPage(HTMLParser):
    def __init__(self, translations):
        super().__init__(convert_charrefs=True)
        self.translations = translations
        self.parts = []
        self.raw = None

    def translate(self, value):
        key = ' '.join(value.split())
        if not key:
            return value
        if key in self.translations:
            result = self.translations[key]
        elif re.fullmatch(r'Wersja [0-9.]+', key):
            result = key.replace('Wersja', 'Version')
        else:
            raise ValueError('Missing English translation: ' + key)
        return value[:len(value)-len(value.lstrip())] + result + value[len(value.rstrip()):]

    def handle_decl(self, decl):
        self.parts.append('<!' + decl + '>')

    def handle_comment(self, text):
        self.parts.append('<!--' + text + '-->')

    def handle_starttag(self, tag, attrs):
        original = dict(attrs)
        translated = []
        for key, value in attrs:
            if value is None:
                translated.append(key)
                continue
            if tag == 'html' and key == 'lang':
                value = 'en'
            elif key in {'alt', 'title', 'aria-label'}:
                value = self.translate(value)
            elif tag == 'meta' and key == 'content' and original.get('name', original.get('property')) in {'description', 'og:title', 'og:description'}:
                value = self.translate(value)
            elif tag == 'meta' and key == 'content' and original.get('property') == 'og:url':
                value = self.english_url
            elif tag == 'link' and key == 'href' and original.get('rel') == 'canonical':
                value = self.english_url
            elif key in {'src', 'href'} and value and not urlsplit(value).scheme and not value.startswith(('#', '//')):
                # Relative page links stay within /en/; shared assets live at root.
                if value.startswith(('assets/', '/assets/')) or urlsplit(value).path.endswith(('.css', '.webmanifest')):
                    value = '/' + value.lstrip('/')
            translated.append(key + '="' + escape(value, quote=True) + '"')
        self.parts.append('<' + tag + (' ' if translated else '') + ' '.join(translated) + '>')
        if tag in {'script', 'style'}:
            self.raw = original.get('type', tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.parts[-1] = self.parts[-1][:-1] + '/>'

    def handle_endtag(self, tag):
        self.parts.append('</' + tag + '>')
        if tag in {'script', 'style'}:
            self.raw = None

    def handle_data(self, data):
        if self.raw == 'application/ld+json':
            schema = json.loads(data)
            schema['inLanguage'] = 'en'
            schema['url'] = self.english_url
            schema['name'] = self.translate(unescape(schema['name']))
            self.parts.append(json.dumps(schema, ensure_ascii=False).replace('<', '\\u003c'))
        elif self.raw:
            self.parts.append(data)
        else:
            self.parts.append(escape(self.translate(data), quote=False))


def build(root, config, catalog):
    translations = json.loads((root/'data/translations-en.json').read_text())
    out = root/'_site'/'en'
    out.mkdir(parents=True, exist_ok=True)
    names = []
    for source in sorted((root/'_site').glob('*.html')):
        if source.name == '404.html':
            continue
        page = EnglishPage(translations)
        page.english_url = config['baseUrl'] + 'en/' + ('' if source.name == 'index.html' else source.name)
        page.feed(source.read_text())
        (out/source.name).write_text(''.join(page.parts))
        names.append(source.name)
    return names
