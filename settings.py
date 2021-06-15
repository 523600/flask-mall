# -*— coding = utf-8 -*-
# @Time : 2021/5/26 0:16
# @Author : ethanyi
# @File : settings.py
# @Software : PyCharm
class Config:

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:525725@42.194.151.7:3306/tmall_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"


class Production(Config):
    ENV = "production"
    DEBUG = False