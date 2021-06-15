# -*— coding = utf-8 -*-
# @Time : 2021/6/9 16:53
# @Author : ethanyi
# @File : model.py
# @Software : PyCharm
from ext import db


class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    ordercode = db.Column(db.String(255))
    shipaddress = db.Column(db.String(255))
    mobile = db.Column(db.String(255))
    createdate = db.Column(db.DateTime)
    uid = db.Column(db.Integer,db.ForeignKey('user.id'))
    status = db.Column(db.String(255))
    confirmdate = db.Column(db.DateTime)
    receiveraddress = db.Column(db.String(255))
    sid = db.Column(db.String(255),db.ForeignKey('store.id'))


class Orderitem(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    pid = db.Column(db.String(255),db.ForeignKey('product.id'))
    oid = db.Column(db.String(255),)
    uid = db.Column(db.String(255),db.ForeignKey('user.id'))
    number = db.Column(db.Integer)