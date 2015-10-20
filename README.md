# Flask App

## About

Had some experience on Django, just wanna test the more flexible flask

follow [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Also plan to read the "Flask Web Development" book

## Structure

```
.
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-34.pyc
│   │   └── views.cpython-34.pyc
│   ├── run.py
│   ├── static
│   ├── templates
│   └── views.py
├── app.py
├── LICENSE
├── pymonitor.py
├── README.md
└── tmp
```

## Environment Setup

### virtualenv

If you don't have `virtualenv` installed, you can run the following command to install it

`pip install virtualenv` 

### setup virtualenv

1. create a virtualenv `virtualenv flask`
2. enter the virtualenv `source flask/bin/activate`
3. run the following commands to install flask and other packages

```
pip install flask
pip install flask-login
pip install flask-openid
pip install flask-mail
pip install flask-sqlalchemy
pip install sqlalchemy-migrate
pip install flask-whooshalchemy
pip install flask-wtf
pip install flask-babel
pip install guess_language
pip install flipflop
pip install coverage
```

4. to exit, `deactivate`


### pymonitor.py

pymonitor is used to auto-restart web server when any file changes

## License 

MIT
