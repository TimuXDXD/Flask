import flask
from flask import request
from flask import jsonify
app = flask.Flask(__name__)

@app.route("/")
def index():
    # ip = get_my_ip()
    return "Hello Heruko"

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return ('Your ip is: ' + request.remote_addr), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
