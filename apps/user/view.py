# -*— coding = utf-8 -*-
# @Time : 2021/5/26 8:31
# @Author : ethanyi
# @File : view.py
# @Software : PyCharm
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_

from apps.user.model import User
from ext import db

customer_bp = Blueprint('user', __name__)

@customer_bp.route('/index',methods=['GET','POST'])
def index():
    return render_template('./main.html')

@customer_bp.route('/user_show',methods=['GET','POST'])
def show():
    users = User.query.all()

    return render_template('user/user_index.html',users= users)



@customer_bp.route('/user_delete',methods=['GET','POST'])
def delete():
    uid = request.args.get('id')
    user = User.query.get(uid)

    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user.show'))

@customer_bp.route('/user_add',methods=['GET','POST'])
def add():
    if request.method =='POST':
        phone = request.form.get('phone')
        uname = request.form.get('name')
        address = request.form.get('address')

        user = User()
        user.name = uname
        user.phonenumber= phone
        user.address = address

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user.show'))
    else:
        return render_template('user/user_create.html')


@customer_bp.route('/user_search',methods=['GET','POST'])
def search():
    s_key = request.args.get("search")
    if s_key == "":
        s_users = User.query.all()
    else:
        s_users = User.query.filter(or_(User.name == s_key,User.phonenumber == s_key)).all()

    return render_template('user/user_index.html',users = s_users)

@customer_bp.route('/user_change',methods=['GET','POST'])
def change():
    if request.method =='POST':
        id = request.form.get('id')
        # print('uid= '+id)
        user = User.query.get(id)
        # print(type(user))
        #
        user.name = request.form.get('name')
        user.phonenumber = request.form.get('phone')
        user.address = request.form.get('address')

        db.session.commit()
        return redirect(url_for('user.show'))
    else:
        uid = request.args.get('id')
        user = User.query.get(uid)

        # user.phonenumber = request.form.get('phone')
        # user.uname = request.form.get('uname')
        # user.uaddress = request.form.get('address')


        return render_template('user/user_change.html',user=user)