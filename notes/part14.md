# I18n and L10n

- I18n (18 stands for the number of letters between i and n)
- L10n

## config.py

add `LANGUAGES` dictionary with language codes

## views.py

a function used to decide which language to use.

```python
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())
```

it will be called before each request to give us a chance to choose the language
to use when producing its response.

For now we will do something very simple, we'll just read the `Accept-Languages` header sent by the browser in the `HTTP request` and find the best matching language from the list that we support. This is actually pretty simple, the `best_match` method does all the work for us.

## babel.cfg

## Mark texts to translate

review all our code and templates and mark all English texts that need
translating so that bebal can find them.

- `gettext()` in views
- `_()` in templates

Because we are putting HTML in the nickname placeholder we need to turn off autoescaping to render this portion of the template, if not Jinja2 would render our HTML elements as escaped text. 

But requesting to render a string without escaping is considered a security risk, it is unsafe to render texts entered by users without escaping.

So we will restricting the characters that can be used in a nickname.

## poedit

just run `sudo apt-get install poedit` to try install it

- [install wxwidget3.0](http://codelite.org/LiteEditor/WxWidgets30Binaries#toc2)
- [install icu](https://launchpad.net/ubuntu/%2Bsource/icu)
- `sudo apt-get install libgtkspell-dev`
- [build lucene++](https://github.com/luceneplusplus/LucenePlusPlus)
    + need to install libboost libraries first
- `sudo apt-get install libdb-dev libdb++-dev`

## procedure

- find all texts and wrap them in `gettext()` and `_()`
- `flask/bin/pybabel extract -F babel.cfg -o messages.pot app` to extract the texts into a seperate file
- `flask/bin/pybabel init -i messages.pot -d app/translations -l zh`
- open `poedit` and translate them then save.
- compile the texets `flask/bin/pybabel compile -d app/translations`

### Use scriptes

- `tr_init.py` extract and int  to language_code
- `tr_update` update the catalog with next texts from source file and templates
- `tr_compile.py` compile the catalog file

## Translating moment.js

download `locale` file

