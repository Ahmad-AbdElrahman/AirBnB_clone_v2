#!/usr/bin/python3
"""Start a Flask web application
"""
from flask import Flask, render_template

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


@app.route('/number_template/<int:n>')
def numtemp(n):
    """Display “n is a number” only if n is an integer
    """
    return render_template('5-number.html', number=str(n))


@app.route('/number_odd_or_even/<int:n>')
def numtempodd(n):
    """Display “n is odd or even” only if n is an integer
    """
    even_odd = ""
    if (n % 2 == 0):
        even_odd = "even"
    else:
        even_odd = "odd"
    return render_template('6-number_odd_or_even.html',
                           number=str(n), odd=even_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
