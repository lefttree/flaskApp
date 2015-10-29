import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin
from flask.ext.openid import OpenID
from flask.ext.mail import Mail
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from .momentjs import momentjs

app = Flask(__name__)
app.config.from_object('config')
# export our class as a global variable to all templates
app.jinja_env.globals['momentjs'] = momentjs
db = SQLAlchemy(app)  # initialize database
# This tells jinja2 to expost our class as a global variable to all templates
app.jinja_env.globals['momentjs'] = momentjs

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'oauth'
# the Flask-OpenID requeires a path to a temp folder where files can be stored
# oid = OpenID(app, os.path.join(basedir, 'tmp'))

mail = Mail(app)

from app import views, models

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler, RotatingFileHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')
