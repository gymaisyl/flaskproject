from flask import Flask
from flask_script import Manager
"""
通过命令行运行指定端口
pip install flask-script
"""

app = Flask(__name__)
manager = Manager(app)  # app与manager进行关联


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    manager.run()

    """
    运行代码方法：
        python 当前文件名　runserver
        -p: 指定端口
        -d:　制定是否是调试模式"""