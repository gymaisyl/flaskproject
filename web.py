from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

"""
安装如下：
flask-sqlalchemy
flask-mysqldb

"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test'

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'hello world'


class Role(db.Model):
    """模型类创建"""
    __tablename__ = 'roles'  # 定义数据库表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    # 这行代码　实现 user.role 和role.users 关联之间的相互数据取出
    users = db.relationship('User', backref='role')


class User(db.Model):
    """模型类创建"""
    __tablename__ = 'users'  # 定义数据库表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    # 添加外键　
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))


if __name__ == '__main__':
    app.run(debug=True)
