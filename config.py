import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'pantalones'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accouts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'}
]

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['andymeyer747@gmail.com','andy@eissturm.com']