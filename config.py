import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CRSF_ENABLED = FALSE
    SECRET_KEY = 'devolopment_key'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    Debug = True


class ProductionConfig(Config):
    Debug = False
