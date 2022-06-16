import os


class Config(object):
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY") or "supersekrit"
    SSL_REDIRECT = True
    MONGODB_SETTINGS = {
    'db': os.getenv("MONGO_INITDB_DATABASE",'test_database'),
    'host': os.getenv("MONGO_HOST", 'mongo'),
    'port': int(os.getenv(("MONGO_PORT"), 27017)),
    'username': os.getenv("MONGO_INITDB_ROOT_USERNAME"),
    'password': os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    }