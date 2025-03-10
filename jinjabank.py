from flask import Flask ,request ,redirect ,url_for
from flask import render_template
from bank import BankAccount

account = BankAccount(1001003067,"Rahul","01-03-2004",9000)
app = Flask(__name__)

@app.route('/')
def bank():
  return render_template("bank.html",account = account)

@app.route('/transition',methods = ['GET','POST'])
def transition():
  message = ""
  if request.method == 'POST':
    action = request.form['action']
    amount = int(request.form['amount'])

    if action == 'deposite':
      message = account.deposite(amount)
    elif action == 'debit' :
      message = account.debit(amount)

  return render_template("transition.html",account = account , message = message)