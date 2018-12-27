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
    return render_template("templates.html", data=mystr)

if __name__ == '__main__':
    app.run(debug=True)