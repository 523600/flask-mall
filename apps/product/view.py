# -*— coding = utf-8 -*-
# @Time : 2021/5/26 8:37
# @Author : ethanyi
# @File : view.py
# @Software : PyCharm
import time

from flask import Blueprint, render_template, request, redirect, url_for

from apps.category.model import Category
from apps.product.model import *
from apps.store.model import Store
from ext import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/product')
def show():

    if request.args.get('cid'):
        cid = request.args.get('cid')
        products = Product.query.filter(Product.cid==cid).all()
        return render_template('product/product_show.html', products=products)
    elif request.args.get('sid'):
        sid = request.args.get('sid')
        products = Product.query.filter(Product.sid == sid).all()
        return render_template('product/product_show.html', products=products)

    products = Product.query.all()

    return render_template('product/product_show.html',products=products)

@product_bp.route('/product_search',methods =['GET','POST'])
def search():
    s_key = request.args.get("search")
    if s_key == "":
        s_products = Product.query.all()
    else:
        s_products = Product.query.filter(Product.name == s_key).all()

    return render_template('product/product_show.html', products=s_products)

@product_bp.route('/product_add',methods =['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        subtitle = request.form.get('subtitle')
        orignalprice = request.form.get('orignalprice')
        promoteprice = request.form.get('promoteprice')
        stock = request.form.get('stock')
        storename = request.form.get('storename')
        category_name = request.form.get('category_name')



        product = Product()
        product.name = name
        product.subtitle = subtitle
        product.orignalprice = orignalprice
        product.promoteprice = promoteprice
        product.stock = stock
        product.createdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        p_store = Store.query.filter(Store.storename == storename).first()
        p_category = Category.query.filter(Category.name == category_name).first()

        if p_store :
            product.sid = p_store.id
        else:
            return "没有这个商店！"

        if p_category:
            product.cid = p_category.id
        else:
            return "没有这个分类！"

        db.session.add(product)
        db.session.commit()
        return redirect(url_for('product.show'))
    else:
        return render_template('product/product_create.html')

@product_bp.route('/product_delete',methods =['GET','POST'])
def delete():
    id = request.args.get('id')
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('product.show'))


@product_bp.route('/product_img',methods =['GET','POST'])
def img_show():
    pid = request.args.get('pid')
    img = Productimage.query.filter(Productimage.pid == pid).first()


    return render_template('product/product_img_show.html',img = img)