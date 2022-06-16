from flask import flash, url_for, redirect, Blueprint, flash, render_template
from app.models import db, Product
from app.forms import BuyForm

blueprint = Blueprint("buy", __name__)

@blueprint.route("/buy", methods=("GET","POST"))
def buy():
    form = BuyForm()
    form.name.choices = Product.list_names()
    if form.validate_on_submit():
        # what to do if someone buys?

        #decrease quatity
        qty = form.quantity.data
        prod = Product.objects(name=form.name.data).first_or_404()
        qty_prev = prod.quantity
        qty_new = qty_prev - qty
        #prod.update_one(set__quantity=qty_new)
        prod.update(quantity = qty_new)
        prod.save()
        flash("You have bought something")
        #return render_template('home.j2')
        return redirect(url_for('main.index'))

    return render_template("buy.j2", form=form)