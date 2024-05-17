#!/usr/bin/python3
"""Start a Flask web application
"""
from flask import Flask, abort

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Display 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Display 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>')
def cisfun(text):
    """Display “C ” followed by the value of the text variable
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def pythonisfun(text='is cool'):
    """Display “Python ” followed by the value of the text variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>')
def nisnumber(n):
    """Display “n is a number” only if n is an integer
    """
    try:
        num = int(n)
        return f'{num} is a number'
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
