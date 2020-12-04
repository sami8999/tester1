import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'kdbksdbkb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RECAPTCHA_USE_SSL= False
    RECAPTCHA_PUBLIC_KEY= '6LfJavkZAAAAAEB1GFtO1Bp0nOM4v-ddTdhrssq5'
    RECAPTCHA_PRIVATE_KEY='6LfJavkZAAAAAApk4Ig2E9C5_liW4tMyNY9TumEp'
    RECAPTCHA_OPTIONS = {'theme':'white'}
