import os

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
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# where we store the SQLALchemy-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# email server settings

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list

ADMINS = ['you@example.com']

# pagination
POSTS_PER_PAGE = 3
