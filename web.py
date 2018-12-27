from flask import Flask
from flask import render_template

"""
Jinja2模板引擎;
模板渲染
"""
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route("/template")
def template():
    """模板渲染与数据返回"""
    mystr = "forever"
    demotest = "<h1>demotest</h1>"
    demoprice = [
        {
            "price": 10
        },
        {
            "price": 20
        }
    ]

    mylist = [1, 2, 3, 4]
    return render_template("templates.html", data=mystr,
                           test=demotest,
                           demoprice=demoprice,
                           mylist=mylist,
                           )


# 自定义过滤器
# 1.使用装饰器的方式
@app.template_filter('listreverse')
def do_listreverse(li):
    """列表反转后显示数据"""
    temp = list(li)
    temp.reverse()
    return temp

# 2.直接添加过滤器
# app.add_template_filter(do_listreverse, "listreverse")

if __name__ == '__main__':
    app.run(debug=True)