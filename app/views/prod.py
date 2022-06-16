from flask import flash, url_for, redirect, Blueprint, flash, render_template
from app.models import db, Product
from app.forms import RestockForm, ProductForm

blueprint = Blueprint("prod", __name__)

@blueprint.route("/restock", methods=("GET","POST"))
def restock():
    form = RestockForm()
    form.name.choices = Product.list_names()
    if form.validate_on_submit():
        # what to do if someone buys?

        #decrease quatity
        qty = form.quantity.data
        prod = Product.objects(name=form.name.data).first_or_404()
        qty_prev = prod.quantity
        qty_new = qty_prev + qty
        #prod.update_one(set__quantity=qty_new)
        prod.update(quantity = qty_new)
        prod.save()
        flash("You have restocked something")
        #return render_template('home.j2')
        return redirect(url_for('main.index'))

    return render_template("restock.j2", form=form)    

@blueprint.route("/add", methods=("GET","POST"))
def add():
    form = ProductForm()
    if form.validate_on_submit():
        prod = Product(
            name = form.name.data,
            quantity = form.quantity.data,
            price = form.price.data,
            description = form.description.data
        )
        prod.save()
        flash("product added")
        return redirect(url_for('main.index'))
    return render_template("add.j2", form=form)   