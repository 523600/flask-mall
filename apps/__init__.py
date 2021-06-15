# -*— coding = utf-8 -*-
# @Time : 2021/5/26 8:26
# @Author : ethanyi
# @File : __init__.py.py
# @Software : PyCharm
from flask import Flask

import settings
from apps.category.view import category_bp
from apps.login.view import login_bp
from apps.product.view import product_bp
from apps.order.view import order_bp
from apps.property.view import property_bp
from apps.store.view import store_bp
from apps.user.view import customer_bp
from ext import db


def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    app.register_blueprint(customer_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(store_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(property_bp)
    app.register_blueprint(login_bp)


    db.init_app(app)

    app.config.from_object(settings.DevelopmentConfig)


    return app