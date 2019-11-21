from flask import Blueprint
home_blueprint=Blueprint('home',__name__)
#记住要导入过来
from . import views

