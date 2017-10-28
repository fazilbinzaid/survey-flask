import os
base_dir = os.path.abspath(os.path.dirname(__file__))

# DATABASE_URL = "postgresql://localhost/db_survey"
DATABASE_URL = ""


class Config(object):
    """
    Base configuration object for the app.
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "70f656b9-ab68-42d6-a2bb-80d38c7497c1-99aa7d9b-b9dd-48c2-9d8b-534c3694735c"
    SQLALCHEMY_DATATBASE_URI = DATABASE_URL


class ProductionConfig(Config):
    """
    Production configuration.
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development Configuration.
    """
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:abcd1234@localhost/db_survey"



class StagingConfig(Config):
    """
    Heroku / Staging Configuration.
    """
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """
    Testing COnfiguration.
    """
    TESTING = True
