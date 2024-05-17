#!/usr/bin/python3
"""Start a Flask web application
"""
from flask import Flask

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


@app.route('/python/<text>')
def pythonisfun(text):
    """Display “Python ” followed by the value of the text variable
    """
    txt = text.replace('_', ' ') if text else 'is cool'
    return f'Python {txt}'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
