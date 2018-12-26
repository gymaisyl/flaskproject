from flask import Flask

"""1.导入类
    2.创建对象
    3.路由绑定
    4.编写视图函数
    5.启动运行"""

# 创建Flask应用程序
app = Flask(__name__,  # flask对应的模板，决定静态文件从哪个路径开始找
            # static_path='/static',
            static_url_path='/static',  # 静态文件访问路径
            static_folder='static',  # 静态文件存放目录，默认是static
            template_folder='templates')  # 模板文件存放目录


@app.route('/')
def index():
    return "hello world"

if __name__ == '__main__':
    app.run()