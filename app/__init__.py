from flask import Flask
from .config import Config
#from .cli import create_db, shell_context_processor
from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap
from .init_prods import prods
db = MongoEngine()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    #app.cli.add_command(create_db)
    #create_db()
    db.init_app(app)
    bootstrap.init_app(app)
    from .views import buy_blueprint, main_blueprint, prod_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(buy_blueprint)
    app.register_blueprint(prod_blueprint)
    
    from .models import Product
    print("loading products", flush=True)
    print(prods, flush=True)
    for prod in prods:
        p = Product(**prod)
        p.save()
    #app.shell_context_processors.append(shell_context_processor)
    #db.init_app(app)
    #db.create_all() #this might cause clearing all data at restart

    #if app.config['SSL_REDIRECT']:
    #    from flask_sslify import SSLify
    #    sslify = SSLify(app)
    return app

app = create_app()