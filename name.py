from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/<int:name>")
def hello(name):
  return str(name)

@app.route("/test")
def rend():
  return render_template('table.html')