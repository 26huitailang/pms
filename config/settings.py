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

# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
CELERY_SCHEDULE = {

}

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_NAME = 'dev'
SEED_ADMIN_PASSWORD = 'devpassword'
SEED_ADMIN_PHONE = '12345678901'
REMEMBER_COOKIE_DURATION = timedelta(days=90)