from flask import Flask
from flask import make_response
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    user_id = request.cookies.get("user_id")
    user_name = request.cookies.get("user_name")
    return '%s:%s' % (user_id, user_name)


@app.route("/login")
def login():
    response = make_response("success")
    response.set_cookie("user_id", "1", max_age=3600)
    response.set_cookie("user_name", "flask", max_age=3600)

    return response


@app.route("/logout")
def logout():
    response = make_response('success')
    response.delete_cookie("user_id")
    response.delete_cookie("user_name")

    return response

if __name__ == '__main__':
    app.run(debug=True)