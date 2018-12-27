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
    return render_template("templates.html", data=mystr,
                           test=demotest,
                           demoprice=demoprice)

if __name__ == '__main__':
    app.run(debug=True)