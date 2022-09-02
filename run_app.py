from flask import abort
from flask import Flask
from flask import make_response
from flask import redirect
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/user/<name>')
def user(name):
    if name == 'noname':
        abort(404)
    return '<h1>Hello, %s!</h1>' % name


@app.route('/url_map')
def url_map():
    return str(app.url_map)


@app.route('/set_cookie')
def set_cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/redirection')
def redirection():
    return redirect('http://www.example.com')


if __name__ == '__main__':
    app.run(debug=True)
