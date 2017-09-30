# coding: utf-8
from datetime import timedelta

DEBUG = True
LOG_LEVEL = 'DEBUG'

# SERVER_NAME = '0.0.0.0:8000'
SECRET_KEY = 'insecurekeyfordev'

# SQLAlchemy.
db_uri = 'postgresql://pms:devpassword@postgres:5432/pms'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_NAME = 'dev'
SEED_ADMIN_PASSWORD = 'devpassword'
SEED_ADMIN_PHONE = '12345678901'
REMEMBER_COOKIE_DURATION = timedelta(days=90)