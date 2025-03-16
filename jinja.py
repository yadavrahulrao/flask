from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/user/<username>")
def user(username):
  return render_template("user.html",name = username)

@app.route("/table/<int:number>")
def table(number):
  return render_template("table.html",number = number)

@app.route('/home/<status>')
def status(status):
  return render_template("ifelse.html",status = status)