# Flask App

## About

Had some experience on Django, just wanna test the more flexible flask

follow [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Also plan to read the "Flask Web Development" book

## To Do

- integrate the layout with latest bootstrap and ajust responsive rendering
- add personal note which supports markdown

## Structure

```
.
├── LICENSE
├── README.md
├── app
│   ├── __init__.py
│   ├── decorators.py
│   ├── emails.py
│   ├── forms.py
│   ├── models.py
│   ├── momentjs.py
│   ├── run.py
│   ├── runp.py
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap-responsive.min.css
│   │   │   └── bootstrap.min.css
│   │   ├── img
│   │   │   ├── facebook.png
│   │   │   ├── glyphicons-halflings-white.png
│   │   │   ├── glyphicons-halflings.png
│   │   │   ├── loading.gif
│   │   │   └── twitter.png
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       ├── moment-zh.min.js
│   │       ├── moment.min.js
│   │       └── translate.js
│   ├── templates
│   │   ├── 404.html
│   │   ├── 500.html
│   │   ├── base.html
│   │   ├── edit.html
│   │   ├── flash.html
│   │   ├── follower_email.html
│   │   ├── follower_email.txt
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── oauth.html
│   │   ├── post.html
│   │   └── user.html
│   ├── translate.py
│   ├── translations
│   │   ├── es
│   │   │   └── LC_MESSAGES
│   │   │       └── messages.po
│   │   └── zh
│   │       └── LC_MESSAGES
│   │           ├── messages.mo
│   │           └── messages.po
│   ├── views.py
├── babel.cfg
├── config.py
├── db_create.py
├── db_downgrade.py
├── db_migrate.py
├── db_upgrade.py
├── oauth.py
├── profile.py
├── pymonitor.py
├── run.py
├── runp.py
├── test.db
├── tests.py
├── tr_compile.py
├── tr_init.py
├── tr_update.py
└── virtualenvSetup.sh
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


### Test Coverage

```
coverage Report:

Name                Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------
app/__init__.py        45      8      6      2    76%   36, 52-58, 31->48, 35->36
app/decorators.py       6      2      0      0    67%   5-6
app/emails.py          16      7      0      0    56%   12-13, 17-20, 23
app/forms.py           29     14      8      0    41%   18-19, 22-33
app/models.py          49      2     10      0    97%   62, 100
app/momentjs.py        12      5      0      0    58%   5, 8, 11, 14, 17
app/translate.py       28      8      2      1    70%   3-4, 7-8, 16, 58-60, 15->16
app/views.py          165    122     44      0    21%   23-34, 60, 92-97, 101-105, 110-111, 120-122, 127-130, 134-161, 168-173, 181-192, 197, 202-203, 208-222, 227-242, 246, 251, 262-272
config.py              21      0      0      0   100%
oauth.py               59     42      8      0    25%   12-15, 22, 28, 31, 35-40, 45-46, 56, 63-77, 89-90, 101-105, 108-126
---------------------------------------------------------------
TOTAL                 430    210     78      3    46%
```

## License 

MIT
