#!/usr/bin/python3
"""Start a Flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False  # Disable strict slashes for all routes

@app.route('/')
def index():
    """Display 'Hello HBNB!'
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)