from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World"


@app.route('/health')
def sanity_Check():
    return "OK"


app.run(port=5000)
