from flask import Flask, request, jsonify , render_template
import json

app = Flask(__name__)

with open('dummydata.json') as f:
    users_data = json.load(f)


@app.route('/', methods=['GET'])
def login():

    username = request.args.get('username')
    password = request.args.get('password')

  
    if not username or not password:
        missing_fields = []
        if not username:
            missing_fields.append("username")
            return render_template("userpassentry.html")
        if not password:
            missing_fields.append("password")
        return render_template("passentry.html")

    for dummydata in users_data:
        if dummydata['username'] == username and dummydata['password'] == password:
            return render_template("login.html")

    return render_template("invalid.html")


