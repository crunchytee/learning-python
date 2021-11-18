from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/2")
def bonjour_world():
    return "Bonjour, World!"