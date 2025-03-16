from flask import Flask
from flask import request
import pdb

app = Flask(__name__)

@app.route('/req')
def get_req():
  return dir(request)

@app.route('/hi',methods = ['POST'])
def get_api():
  return request.method
