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
    txt = ""
    for i in text:
        if (i != '_'):
            txt += i
        else:
            txt += " "
    return f'C {txt}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
