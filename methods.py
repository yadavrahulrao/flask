from flask import Flask,request
import pdb

app = Flask(__name__)

@app.route('/get')
def get_api():
  return {
    "employee" :[
    {"firstname":"rahul","lastname":"yadav"},
    {"firstname":"rajbir","lastname":"yadav"},
    {"firstname":"vipin","lastname":"yadav"}
    ]
  }