import click
from flask.cli import with_appcontext
from .models import db, Product
from .init_prods import prods

@click.command(name="createdb")
@with_appcontext
def create_db():
    db.create_all()
    db.session.commit()
    for prod in prods:
        p = Product(**prod)
        p.save()
    #app.shell_conte
    print("Database created")


def shell_context_processor():
    return {"db": db, "User": User, "OAuth": OAuth}