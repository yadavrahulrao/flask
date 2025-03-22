from flask import Flask , render_template 
import json

app = Flask(__name__)


@app.route('/userid')
def showuserid():
  
  with open('work1.json') as f:
    work1 = json.load(f)

  userid = [user['userId'] for user in work1]

  return render_template("work13.html",userid=userid)

@app.route('/ids')
def showid():
  with open('work1.json') as f :
    work1 = json.load(f)

  ids = [user['id'] for user in work1]
  return render_template("work14.html",ids=ids)

