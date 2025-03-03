from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
  return "index page"

@app.route("/hello")
def hello():
  return "hello rahul"
