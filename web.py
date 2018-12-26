from flask import Flask
from flask import redirect
from flask import request
from flask import url_for

"""
自定义状态码
"""

# 创建Flask应用程序
app = Flask(__name__,  # flask对应的模板，决定静态文件从哪个路径开始找
            # static_path='/static',
            static_url_path='/static',  # 静态文件访问路径
            static_folder='static',  # 静态文件存放目录，默认是static
            template_folder='templates')  # 模板文件存放目录


# 这里使用的是从对象中加载
class Config(object):
    DEBUG = True

app.config.from_object(Config)


@app.route('/')
def index():
    return "hello world"


# 给路由添加参数，格式 <参数名>
# 视图函数需要接收这个参数
@app.route('/demo01/user/<int:user_id>')
def demo01(user_id):
    return "demo01 %s" % user_id


# 定义不同的请求方式，使用methods
@app.route('/demo02', methods=['GET', 'POST'])
def demo02():
    return request.method


@app.route('/redirect')
def demo03():
    """重定向
    url_for 到自己写的视图函数"""

    # return redirect(url_for('index'))
    return redirect(url_for('demo01', user_id=123))


@app.route('/demo04')
def demo04():
    return "demo04", 666

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)