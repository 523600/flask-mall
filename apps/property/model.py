# -*— coding = utf-8 -*-
# @Time : 2021/6/10 9:23
# @Author : ethanyi
# @File : model.py
# @Software : PyCharm
from ext import db


class Property(db.Model):
    __tablename__ ="property"
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    cid = db.Column(db.Integer,db.ForeignKey('category.id'))
    name = db.Column(db.String(255))




class Propertyvalue(db.Model):
    __tablename__ = "propertyvalue"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    pid = db.Column(db.Integer,db.ForeignKey('product.id'))
    ptid = db.Column(db.Integer,db.ForeignKey('property.id'))
    value = db.Column(db.String(255))

    property = db.relationship('Property', backref='property_value')