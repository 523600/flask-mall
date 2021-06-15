# -*— coding = utf-8 -*-
# @Time : 2021/6/3 14:49
# @Author : ethanyi
# @File : view.py
# @Software : PyCharm
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_

from apps.category.model import Category
from ext import db

category_bp = Blueprint('category', __name__)

@category_bp.route('/category',methods=['GET','POST'])
def show():
    categories = Category.query.all()
    return render_template('category/category_show.html',categories = categories)

@category_bp.route('/cate_search',methods=['GET','POST'])
def search():
    s_key = request.args.get("search")
    # print(sname)
    if s_key == "":
        s_categories = Category.query.all()
    else:
        s_categories = Category.query.filter(Category.name == s_key).all()

    return render_template('category/category_show.html', categories=s_categories)

@category_bp.route('/cate_add',methods=['GET','POST'])
def add():
    if request.method =='POST':
        name = request.form.get('name')


        category = Category()
        category.name = name


        db.session.add(category)
        db.session.commit()
        return redirect(url_for('category.show'))
    else:
        return render_template('category/category_create.html')

@category_bp.route('/cate_delete',methods=['GET','POST'])
def delete():
    id = request.args.get('id')
    category = Category.query.get(id)

    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('category.show'))