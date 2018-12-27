from flask import Flask

app = Flask(__name__)

"""
请求上下文：request context
1.request
2.session
只有在请求发生的时候，才能获取到数据的，称为请求上下文；
在请求范围之外的话，请求之后会发生　请求之外的异常
"""


"""
应用上下文：application context
1.current_app
2.g变量
应用运行起来之后获取到的数据
"""

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)