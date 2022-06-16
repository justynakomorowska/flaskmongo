from flask import Blueprint, render_template
from app.models import db, Product

blueprint = Blueprint("main", __name__)

@blueprint.route("/")
def index():
    products = Product.objects
    return render_template("products_table.j2", products=products)


#@blueprint.route("/")
#def index():
#    return render_template("home.j2")
