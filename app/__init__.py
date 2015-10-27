import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, UserMixin
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)  # initialize database

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'oauth'
# the Flask-OPenID requeires a path to a temp folder where files can be stored
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
