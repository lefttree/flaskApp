# Web Forms

We are using the `Flask-wtf` extension, which integrate the `WTForms` with flask.

## Configuration

Setup a configuration file inside our folder, let's call it `config.py`.

```
WTF_CSRF_ENABLE = True
SECRET_KEY = 'you-will-never-guess'
```

The WTF_CSRF_ENABLED setting activates the cross-site request forgery prevention (note that this setting is enabled by default in current versions of Flask-WTF). In most cases you want to have this option enabled as it makes your app more secure.
The SECRET_KEY setting is only needed when CSRF is enabled, and is used to create a cryptographic token that is used to validate a form.

load the config file in `__init__.py`

`app.config.from_object('config')`

## User login form

Web forms are represented in Flask-WTF as classes, subclassed from base class Form. A form subclass simply defines the fields of the form as class variables.

Let them login using `OpenID`.

## Form templates

The good news is that the LoginForm class that we just created knows how to render form fields as HTML, so we just need to concentrate on the layout.

The `form.hidden_tag()` template argument will get replaced with a hidden field that implements the CSRF prevention that we enabled in the configuration.

The submit field does not carry any data so it doesn't need to be defined in the form class.

## Form Views

- pass data

### receive data

`validate_on_submit` does all the form processing work. when it's called, it will gather all the data
, run all the validators attached to fields, and if everything is right it will return True.

The `flash` function is a quick way to show a message on the next page presented to the user. 

`get_flashed_messages()`

### improving field validation

When a field fails validation `Flask-WTF` adds a descriptive error message to the form object. These messages are available to the template, so we just need to add a bit of logic that renders them.

As a general rule, any fields that have validators attached will have errors added under `form.field_name.errors`.

```
{% for error in form.openid.errors %}
    <span style="color: red;">[{{ error }}]</span>
{% endfor %}<br>
```

### Dealing with OpenIDs

- defind OpenID providers in `config.py`
- pass to template
- add a little javascript to populate the field
