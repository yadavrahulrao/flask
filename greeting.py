from flask import Flask
app = Flask(__name__)
@app.route("/rahul")
def hello ():
  return "<p>hello,world</p>"

