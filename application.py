import flask
from flask import request, jsonify, redirect, url_for
app = flask.Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('ip'))

@app.route('/ip')
def ip():
    template = ''
    ip = getIP()
    ip = [_ for _ in ip if not _.startswith('169.254')]
    if ip:
        template = '<h1> IP: ' + ip[0] + '</h1>'
    return template

def getIP():
    def clientV1():
        return request.remote_addr

    def clientV2():
        return request.environ['REMOTE_ADDR']

    def proxy_client():
        return request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)

    return [clientV1(), clientV2(), proxy_client()]

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
