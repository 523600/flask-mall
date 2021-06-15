# -*— coding = utf-8 -*-
# @Time : 2021/6/3 10:06
# @Author : ethanyi
# @File : view.py
# @Software : PyCharm
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_

from apps.store.model import Store
from ext import db

store_bp = Blueprint('store', __name__)

@store_bp.route('/store_show')
def show():
    if request.method =='POST':
        pass
    else:
        stores = Store.query.all()
        return render_template('store/store_show.html',stores = stores)

@store_bp.route('/store_delete',methods=['GET','POST'])
def delete():
    sid = request.args.get('sid')
    store = Store.query.get(sid)

    db.session.delete(store)
    db.session.commit()
    return redirect(url_for('store.show'))

@store_bp.route('/store_add',methods=['GET','POST'])
def add():
    if request.method =='POST':
        storename = request.form.get('storename')
        shipaddress = request.form.get('shipaddress')

        store = Store()
        store.storename = storename
        store.shipaddress= shipaddress


        db.session.add(store)
        db.session.commit()
        return redirect(url_for('store.show'))
    else:
        return render_template('store/store_create.html')

@store_bp.route('/store_search',methods=['GET','POST'])
def search():
    s_key = request.args.get("search")
    if s_key == "":
        s_stores = Store.query.all()
    else:
        s_stores = Store.query.filter(or_(Store.storename == s_key,Store.shipaddress == s_key)).all()

    return render_template('store/store_show.html',stores = s_stores)

@store_bp.route('/store_change',methods=['GET','POST'])
def change():
    if request.method =='POST':
        sid = request.form.get('id')
        store = Store.query.get(sid)
        # print(str(sid))
        store.storename = request.form.get('name')

        store.shipaddress = request.form.get('address')

        db.session.commit()
        return redirect(url_for('store.show'))
    else:
        sid = request.args.get('id')
        store = Store.query.get(sid)



        return render_template('store/store_change.html',store=store)