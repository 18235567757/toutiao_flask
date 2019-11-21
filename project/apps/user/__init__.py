from flask import Blueprint
from flask_restful import Api,Resource
#创建蓝图
user_blueprint=Blueprint('user',__name__,url_prefix='/user')
#Api接管蓝图
api=Api(user_blueprint)
#记住 导入
from . import views


