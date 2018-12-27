from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route("/upload", methods=["post"])
def upload():

    file = request.files.get("pic")
    file.save("aa.png")
    return "success"


if __name__ == '__main__':
    app.run()