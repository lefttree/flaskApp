# User Login

## OAuth

use OAuth, here is a [blog](http://blog.miguelgrinberg.com/post/oauth-authentication-with-flask)

## Configuration

`app/__init__.py`

## revisiting user model

- `is_authenticated`
- `is_active`
- `is_anonymous`
- `get_id`

## User loader callback

- `oid.loginhandler` decorator
- `g`
- `url_for`
- `session`
- `oid.try_login`
