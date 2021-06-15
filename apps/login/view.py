# -*— coding = utf-8 -*-
# @Time : 2021/6/10 14:56
# @Author : ethanyi
# @File : view.py
# @Software : PyCharm
from flask import Blueprint, render_template

login_bp = Blueprint('login', __name__)


@login_bp.route('/')
def login():
    return render_template('login/login.html')