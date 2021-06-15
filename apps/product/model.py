# -*— coding = utf-8 -*-
# @Time : 2021/6/8 11:24
# @Author : ethanyi
# @File : model.py
# @Software : PyCharm
from ext import db


class Product(db.Model):
    id = db.Column(db.Integer,autoincrement=True,nullable=False,primary_key=True)
    name = db.Column(db.String(255))
    subtitle = db.Column(db.String(255))
    orignalprice = db.Column(db.Float)
    promoteprice = db.Column(db.Float)
    stock = db.Column(db.Integer)
    createdate = db.Column(db.DateTime)

    cid = db.Column(db.Integer,db.ForeignKey('category.id'))
    sid = db.Column(db.Integer,db.ForeignKey('store.id'))

    orderitem =db.relationship('Orderitem',backref = 'product')


class Productimage(db.Model):
    id = db.Column(db.Integer,autoincrement=True,nullable=False,primary_key=True)
    pid = db.Column(db.Integer,db.ForeignKey('product.id'))
    productname = db.Column(db.String(1024),)
    url = db.Column(db.String(1024),)

    product =db.relationship('Product',backref = 'productimage')