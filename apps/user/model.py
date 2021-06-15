# -*— coding = utf-8 -*-
# @Time : 2021/5/30 12:03
# @Author : ethanyi
# @File : model.py
# @Software : PyCharm
from ext import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, )
    # password = db.Column(db.String(255), nullable=False, )
    address = db.Column(db.String(255), nullable=False, )
    phonenumber = db.Column(db.String(255), nullable=False, )

    order = db.relationship('Order',backref='user')
    # orderitem = db.relationship('Orderitem', backref='user')