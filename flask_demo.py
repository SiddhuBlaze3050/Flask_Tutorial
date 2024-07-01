from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/ping", methods = ['GET'])
def pinger():
    return "<p>Hello, I am Sid!</p>"