from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
# from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
# 创建SQLAlchemy实例对象一定要写在加载配置文件后边，
# Warning 写在这里不对
# db=SQLAlchemy(app)

# 加载配置文件
from config import Config

app.config.from_object(Config)

# 创建SQLAlchemy实例对象
db = SQLAlchemy(app)

# 创建redis实例对象
# warning 本机需要安装Redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 设置CSRF保护
CSRFProtect(app)

# 大写的Session 方便我们管理 session
# 我们写代码的时候 还是操作 session
Session(app)

# 注册蓝图
from project.apps.home import home_blueprint

app.register_blueprint(home_blueprint)

from project.apps.user import user_blueprint

app.register_blueprint(user_blueprint)
