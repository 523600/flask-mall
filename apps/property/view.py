# -*— coding = utf-8 -*-
# @Time : 2021/6/10 9:23
# @Author : ethanyi
# @File : view.py
# @Software : PyCharm
from flask import Blueprint, render_template, request

from apps.property.model import *

property_bp = Blueprint('property',__name__)

@property_bp.route('/property',methods = ['GET','POST'])
def show():
    cid = request.args.get('cid')
    properties = Property.query.filter(Property.cid == cid).all()
    return render_template('property/property_show.html',properties =properties)

@property_bp.route('/propertyvalue_show',methods = ['GET','POST'])
def value_show():
    pid = request.args.get('pid')
    values = Propertyvalue.query.filter(Propertyvalue.pid == pid).all()
    print(pid)
    print(values)

    return render_template('property/propertyvalue_show.html', values=values)
