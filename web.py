from flask import Flask
from flask import session

app = Flask(__name__)
app.config['SECRET_KEY'] = "weferahtrj"  # 使用session需要使用

"""
session依赖于cookie进行传递，但是没有cookie也可以在url中进行传递
"""


@app.route('/')
def index():
    user_id = session.get("user_id", None)
    user_name = session.get("user_name", None)
    return "success"


@app.route("/login")
def login():
    session["user_id"] = 1
    session["user_name"] = "laowang"

    return "success"


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("user_id", None)

    return "success"

if __name__ == '__main__':
    app.run(debug=True)