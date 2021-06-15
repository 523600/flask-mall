# -*— coding = utf-8 -*-
# @Time : 2021/6/3 10:10
# @Author : ethanyi
# @File : model.py
# @Software : PyCharm
from ext import db


class Store(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    storename = db.Column(db.String(255),nullable=False)
    shipaddress = db.Column(db.String(255),nullable=False)

    product = db.relationship('Product', backref='store')
    order = db.relationship('Order', backref='store')
    # orderitem = db.relationship('Orderitem', backref='store')