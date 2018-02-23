from flask import Flask
from flask import request
import json

app = Flask(__name__)

users = []
newId = 0

#GET /  ==> "Hello World!"
@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

#POST /users    "name=foo"
@app.route('/users', methods=['POST'])
def new_users():
    name = request.form['name']
    global newId
    newId+=1
    users.append({'id':newId,'name':name})
    return ("Hello {}!".format(name),201)

@app.route('/users/<id>', methods=['GET'])
def get_users(id):
    for x in users:
        if x['id'] == int(id):
            return x['name'],200


@app.route('/users/<id>', methods=['DELETE'])
def delete_users(id):
    for x in users:
        if x['id'] == int(id):
            users.remove(x)
            return ('',204)