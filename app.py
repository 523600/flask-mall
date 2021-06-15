import json

from flask import Flask, request, render_template, redirect, url_for
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.model import User
from apps.store.model import Store
from apps.category.model import Category
from apps.product.model import Product
from apps.order.model import *
from apps.property.model import *
from apps import create_app
from ext import db

app=create_app()


manager = Manager(app=app)

migrate = Migrate(app=app,db=db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
