from flask import Flask

"""配置加载
    1.对象中加载：
    2.从文件中加载配置
    3.从环境中加载配置"""

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

"""
app可以直接通过app.的方式进行配置
app.debug = True
app.config['DEBUG'] = True
"""


@app.route('/')
def index():
    return "hello world"

if __name__ == '__main__':
    app.run()