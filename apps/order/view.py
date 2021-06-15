# -*— coding = utf-8 -*-
# @Time : 2021/5/26 8:43
# @Author : ethanyi
# @File : view.py
# @Software : PyCharm
import datetime
import time

from flask import Blueprint, render_template, request, redirect, url_for

from apps.order.model import *
from apps.product.model import Product
from apps.store.model import Store
from apps.user.model import User
from ext import db

order_bp = Blueprint('order', __name__)

@order_bp.route('/order')
def show():
    orders = Order.query.all()

    return render_template('order/order_show.html',orders = orders)


@order_bp.route('/order_search',methods=['GET','POST'])
def search():
    s_key = request.args.get("search")
    # print(s_key)
    if s_key == "":
        s_orders = Order.query.all()
    else:
        s_orders = Order.query.filter(Order.ordercode == s_key).all()

    return render_template('order/order_show.html', orders=s_orders)


@order_bp.route('/order_delete',methods=['GET','POST'])
def delete():
    id = request.args.get('id')
    order = Order.query.get(id)

    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('order.show'))

@order_bp.route('/order_add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        ordercode = request.form.get('ordercode')
        shipaddress = request.form.get('shipaddress')
        mobile = request.form.get('mobile')
        createdate = request.form.get('createdate')
        uname = request.form.get('uname')
        storename = request.form.get('storename')
        status = request.form.get('status')
        receiveraddress = request.form.get('receiveraddress')

        number = request.form.get('amount')
        pname = request.form.get('pname')

        #这里是计算确认到达时间，这个时间的模块我用了time和datetime两个模块
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        n_days = now + delta

        #开始增加订单表
        order = Order()
        order.ordercode = ordercode
        order.shipaddress = shipaddress
        order.mobile = mobile
        order.status = status

        order.receiveraddress = receiveraddress
        order.createdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        user = User.query.filter(User.name==uname).first()
        store = Store.query.filter(Store.storename == storename).first()
        product = Product.query.filter(Product.name == pname).first()
        #看有没有到货
        if status !="已收货":
            order.confirmdate = None
        else:
            order.confirmdate = n_days.strftime('%Y-%m-%d %H:%M:%S')

        #查看有没有这个用户或者这个商店
        if user :
            order.uid = user.id
        else:
            return "没有这个用户！"
        if store:
            order.sid = store.id
        else:
            return "没有这个分类！"

        #同时开始增加orderitem表
        orderitem = Orderitem()
        orderitem.number = number
        orderitem.uid = user.id
        orderitem.pid = product.id
        orderitem.oid = order.ordercode

        db.session.add(order)
        db.session.add(orderitem)

        db.session.commit()
        return redirect(url_for('order.show'))
    else:
        return render_template('order/order_create.html')


@order_bp.route('/orderitem_show',methods=['GET','POST'])
def show_item():
    orderitems = Orderitem.query.all()

    return render_template('order/orderitem_show.html', orderitems=orderitems)

@order_bp.route('/orderitem_search',methods=['GET','POST'])
def item_search():
    s_key = request.args.get("search")
    # print(s_key)
    if s_key == "":
        s_orders = Orderitem.query.all()
    else:
        s_orders = Orderitem.query.filter(Order.ordercode == s_key).all()

    return render_template('order/orderitem_show.html', orderitems=s_orders)


@order_bp.route('/orderitem_delete',methods=['GET','POST'])
def item_delete():
    id = request.args.get('id')
    orderitem = Orderitem.query.get(id)

    db.session.delete(orderitem)
    db.session.commit()
    return redirect(url_for('order.show_item'))