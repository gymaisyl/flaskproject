from flask import Flask
from flask import abort
from flask import redirect
from flask import request
from flask import url_for
from werkzeug.routing import BaseConverter

"""
请求钩子
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


class RegexConverter(BaseConverter):
    """自定义路由正则"""
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]

# 将自定义的路由转换器添加到转换器列表中
app.url_map.converters["re"] = RegexConverter


@app.route("/demo05")
def demo05():
    abort(404)
    return "demo05"


@app.errorhandler(404)
def page_not_found(error):
    return "the page is not found"


"""
before_first_request
在处理第一个请求前执行;
before_request
在每次请求前执行
如果在某修饰的函数中返回了一个响应，视图函数将不再被调用;
after_request
如果没有抛出错误，在每次请求后执行
接受一个参数：视图函数作出的响应
在此函数中可以对响应值在返回之前做最后一步修改处理
需要将参数中的响应在此参数中进行返回;
teardown_request：
在每次请求后执行
接受一个参数：错误信息，如果有相关错误抛出
"""


# 仅仅做一个demo
@app.before_request
def before_request():
    print("before_request")


@app.route("/demo06")
def demo06():
    return "demo06"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)