
from flask import Flask
from flask import request
import json


app = Flask(__name__)
app.debug = True

# 127.0.0.1:5000/
@app.route("/")
def index():
    return "<h1>ABCD PYTHON STUDY</h1>"


# 127.0.0.1:5000/hello/abcd?q=12345
@app.route("/hello/<name>", methods=['GET'])
def hello(name):
    q = request.args.get("q")
    return "Hello %s - %s" % (name, q)
    # return "Hello {} - ".format(name) + q


# 127.0.0.1:5000/json/abcd
@app.route("/json/<name>", methods=['POST'])
def makeJson(name):
    q = request.args.get("q")
    value = {"hello": name, "q": q}
    print(value)
    result = json.dumps(value)
    return result


if __name__ == "__main__":
    app.run()