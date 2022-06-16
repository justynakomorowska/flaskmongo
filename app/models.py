import json
from flask import Flask, request, jsonify

from . import db

class Product(db.Document):
    name = db.StringField()
    quantity = db.IntField()
    description = db.StringField()
    price = db.FloatField()

    def list_all(self):
        return [prod for prod in Product.objects]

    @classmethod
    def list_names(cls):
        names = [prod.name for prod in Product.objects]
        print(names,flush=True)
        return names

    @classmethod
    def list_stock(cls):
        stock = {}
        for prod in Product.objects:
            stock[prod.name] = prod.quantity
        print(stock,flush=True)
        return stock