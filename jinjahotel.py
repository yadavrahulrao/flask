from flask import Flask,request,redirect,url_for
from flask import render_template
from hotel import restaurant

hotel = restaurant()
app = Flask(__name__)
@app.route('/')
def hotel():
  return render_template("hotel.html",hotel = hotel)

@app.route('/hoteldetails',methods = ['GET','POST'])
def hoteldetails():
  message = " "
  if request.method == 'POST':
    action = request.form['action']
    print_menu = str(request.form['print_menu'])
    reserve_table = str(request.form['reserve_table'])
    take_order = str(request.form['take_order'])
  
    if action == 'print_menu':
      message = hotel.print_menu(print_menu) 

    elif action == 'reserve_table':
      message = hotel.reserve_table(reserve_table)

    elif action == 'take_order':
      message = hotel.take_order(take_order)

  return render_template("hoteldetails.html",hotel = hotel ,message = message)