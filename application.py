import flask
from flask import request
from flask import jsonify
app = flask.Flask(__name__)

@app.route("/")
def index():
    ip_addr = request.remote_addr
    return '<h1> Your IP address is:' + ip_addr + '</h1>'

@app.route('/c')
def client():
    ip_addr = request.environ['REMOTE_ADDR']
    return '<h1> Your IP address is:' + ip_addr + '</h1>'

@app.route('/pc')
def proxy_client():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return '<h1> Your IP address is:' + ip_addr + '</h1>'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
