from xml.dom import ValidationErr
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from .models import db, Product
from flask_mongoengine.wtf import model_form

def validate_quantity(form, field):
    print(f"checking {form.name.data}", flush=True)
    stock = Product.list_stock()
    print(f"currently we have: {stock}")
    msg = f"Don't have enough of product: {form.name}"
    if form.quantity>stock[form.name]:
        raise ValidationError(msg)

class BuyForm(FlaskForm):
    name = SelectField("Name",  validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired()])

    def validate_on_submit(self):
        if not super(BuyForm, self).validate_on_submit():
            return False
        print(f"checking {self.name.data}", flush=True)
        stock = Product.list_stock()
        print(f"currently we have: {stock}")
        msg = f"Don't have enough of product: {self.name.data}"
        if self.quantity.data>stock[self.name.data]:
            #raise ValidationError(msg)
            flash(msg)
            return False
        return True

class RestockForm(FlaskForm):
    name = SelectField("Name",  validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    def validate_on_submit(self):
        if not super(RestockForm, self).validate_on_submit():
            return False
        if self.quantity.data <0:
            return False
        return True

class ProductForm(FlaskForm):
    name = StringField("Name",  validators=[DataRequired()])
    quantity = IntegerField("Quantity",  validators=[DataRequired()])
    price = FloatField("Price",  validators=[DataRequired()])
    description = StringField("Description",  validators=[DataRequired()])
    def validate_on_submit(self):
        if not super(ProductForm, self).validate_on_submit():
            return False
        if self.quantity.data <0:
            return False
        if self.price.data <0:
            return False
        return True