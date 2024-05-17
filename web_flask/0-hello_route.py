from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False  # Disable strict slashes for all routes

@app.route('/')
def index():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')