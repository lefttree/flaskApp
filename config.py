import os
# -*- coding: utf-8 -*-

WTF_CSRF_ENABLE = True
SECRET_KEY = 'you-will-never-guess'

# OpenID Providers
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

# OAuth Providers
OAUTH_CREDENTIALS = {
        'facebook': {
            'id': '155828014769435',
            'secret': '365178be5a2a1b0303a68530feb2b286'
        },
        'twitter': {
            'id': 'p2ddznP04r7HGfaDxcJrSNYZa',
            'secret': 'ZmfhBCcZqpqB2whhnfSuSYtWQcPUQzhrqw9mthASTL319TiyPH'    
        }
    }

basedir = os.path.abspath(os.path.dirname(__file__))

# required by `FLASK-SQLAlchemy`
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') + '?check_same_thread=False')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
# where we store the SQLALchemy-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# email server settings

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list

ADMINS = ['bylixiang@gmail.com']

# pagination
POSTS_PER_PAGE = 5

# avaiable languages
LANGUAGES = {
    'en': 'English',
    'zh': 'Chinese'
}

MS_TRANSLATOR_CLIENT_ID = "microblog0123"
MS_TRANSLATOR_CLIENT_SECRET = "Dv39oiHLS7uGVPqqQullkaBE7x+/X3/9/sqK6sGqva4="

SQLALCHEMY_RECORD_QUERIES = True
# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5
