# -*— coding = utf-8 -*-
# @Time : 2021/6/3 14:49
# @Author : ethanyi
# @File : model.py
# @Software : PyCharm
from ext import db


class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    name = db.Column(db.String(255),nullable=False)

    product = db.relationship('Product', backref='category')