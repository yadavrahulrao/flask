from flask import Flask
from flask import render_template
import data
app = Flask(__name__)

# @app.route('/names')
# def rahul():
#   return render_template("datadict.html",data = data.data_dict)

# @app.route('/used')
# def yadav():
#   return render_template("datadict.html",data = data.data_dict)

@app.route('/id')
def rao():
  return render_template("datadict.html",data = data.data_dict)