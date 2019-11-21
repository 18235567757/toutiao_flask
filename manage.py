from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from project import app, db

# db迁移添加
Migrate(app=app, db=db)

# 让Manager 管理Flask
# 我们可以通过使用指令来管理
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
