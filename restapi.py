# import requests
# import json

# response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')


# # print(response.json()['items'])



# for data in response.json()['items']:
#   if data['answer_count']== 0:
#     print(data['title'])
#     print(data['link'])

#   else :
#     print('skipped')
# print()



from flask import Flask

from sqlalchemy import sqlalchemy
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


db = sqlalchemy(app)


class Drink(db.Model):
  id = db.Column(db.Integer , primary_key = True)
  name = db.Column(db.String(80),unique = True , nullable = False)
  description = db.Column(db.String(120))


  def __repr__(self):
    return f"{self.name} - {slef.description}"

@app.route('/')
def index():
  return 'hello'


@app.route('/drinks')
def get_drinks():
  return {"drinks":"drink data" }