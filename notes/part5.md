# User Login

## OAuth

use OAuth, here is a [blog](http://blog.miguelgrinberg.com/post/oauth-authentication-with-flask)

## Configuration

`app/__init__.py`

add `LoginManager()`

## revisiting user model

- `is_authenticated`

In general return `True` unless the user should not be allowed to authenticate for some reason

- `is_active`

`True` unless inactive

- `is_anonymous`

`False` unless for fake users that are not supposed to login

- `get_id`

return a unique identifier for the user, in unicode format.

## User loader callback

loads a user from database

## login view function

- `oid.loginhandler` decorator
- `g`

`g` global is setup by Flask as a place to store and share data during the life
of a request.

- `url_for`

a clean way to obtain the URL for a given view function

- `session`
    
Once data is stored in the session object it will be available during that request and any future requests made by **the same client**. 

- `oid.try_login`

    takes 2 arguments
    + the openid
    + a list of data items that we want from the OpenID provider

## login callback

- `oid.after_login`
- `resp` contains information returned by the OpenID provider
- `before_request`, decorated with this will run before the view function each time a request is received
- `login_required`
    + protect views against non loggedin users by add this decorator
    + need to config in the `__init__.py`, `lm.login_view = 'login'`

## The g.user global

- `before_request`
- `current-user` is set by Flask-login
- setup `g.user = current_user`
- user `g.user` in `index` view

## logout

- `logout_user()`
