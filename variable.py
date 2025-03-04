from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route("/name/<name>")
def var(name):
  return f'user{escape(name)}'